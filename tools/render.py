#!/usr/bin/env python3
"""Build and optionally install the global Pi agent policy bundle.

    python3 tools/render.py                 build a release in ./build/
    python3 tools/render.py --install       build, then install into ~/.agents/
    python3 tools/render.py --out dist      build into ./dist/
    python3 tools/render.py --install --install-dir ~/.agents

The build directory mirrors the deployable ~/.agents/ layout. Source policy,
compiler code, tests, evals, and migration documentation are not shipped.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAW = ROOT / "LAW.md"
MARK = "<!-- generated from LAW.md by tools/render.py; edit LAW.md, not this file -->"
DEFAULT_BUILD = ROOT / "build"
DEFAULT_INSTALL = Path.home() / ".agents"
SKILLS_SOURCE = ROOT / "agent-policy-skills"
TEMPLATES_SOURCE = ROOT / "templates"

# Views the law no longer defines; removed on a render so no stale role survives.
OBSOLETE = []

# A role tag is trailing: whitespace, @, the role name.
TAG_END = re.compile(r"[ \t]+@([a-z_]+)\s*$")
HEADING = re.compile(r"(#{1,6})[ \t]")

ROLES = {
    "communicator": {
        "agent": None,
        "context": "AGENTS.md",
        "frontmatter": [],
    },
    "manager": {
        "agent": "agents/manager.md",
        "context": None,
        "frontmatter": [
            ("name", "manager"),
            ("description", "Manager responsible for the scope explicitly assigned."),
            ("tools", "read, edit, write, bash, grep, find, ls, subagent"),
            # The tool allowlist alone does not load the provider in child sessions.
            ("subagentOnlyExtensions", "npm:pi-subagents"),
            ("allowNestedSubagents", "true"),
            # Two hours is a finite default for scopes that exceed Pi's 30-minute default.
            ("timeoutMs", "7200000"),
            ("thinking", "medium"),
            ("advertise", "true"),
            ("systemPromptMode", "replace"),
            ("inheritProjectContext", "false"),
            ("inheritGlobalContext", "false"),
            ("inheritSkills", "true"),
        ],
    },
    "worker": {
        "agent": "agents/worker.md",
        "context": None,
        "frontmatter": [
            ("name", "worker"),
            ("description", "You execute exactly one work package in your manager's area, and report once."),
            ("tools", "read, edit, write, bash, grep, find, ls"),
            # Workers may also own long-running bounded packages; keep a finite deadline.
            ("timeoutMs", "7200000"),
            ("thinking", "low"),
            ("advertise", "true"),
            ("systemPromptMode", "replace"),
            ("inheritProjectContext", "false"),
            ("inheritGlobalContext", "false"),
            ("inheritSkills", "true"),
        ],
    },
}


def take_tags(line):
    """Strip the trailing role tags off one line; return (roles, stripped line).

    Only trailing tags whose name is a role are stripped, so a sentence ending in
    an @-token that is not a role survives intact."""
    roles = set()
    while True:
        m = TAG_END.search(line)
        if m is None or m.group(1) not in ROLES:
            return roles, line.rstrip()
        roles.add(m.group(1))
        line = line[: m.start()]


def parse(text):
    """Return [(heading or None, level, effective roles, [body lines])].

    Splits on headings outside fences and resolves each heading's role set: the
    heading's own tags, else the nearest ancestor heading's set, else no role at
    all. Text before the first heading has no heading and no role."""
    sections = []
    current = None
    stack = []  # [(level, roles)] for the open headings
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        m = None if fenced else HEADING.match(line)
        if m is not None:
            level = len(m.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            roles, heading = take_tags(line)
            if not roles and stack:
                roles = stack[-1][1]
            stack.append((level, set(roles)))
            current = (heading, level, set(roles), [])
            sections.append(current)
        else:
            if current is None:
                current = (None, 0, set(), [])
                sections.append(current)
            current[3].append(line)
    return sections


def tidy(lines):
    """Trim blank edges and collapse runs of blank lines."""
    out = []
    for line in lines:
        if not line.strip() and (not out or not out[-1].strip()):
            continue
        out.append(line)
    while out and not out[-1].strip():
        out.pop()
    return out


def render_body(role):
    body = []
    for heading, _level, roles, lines in parse(LAW.read_text(encoding="utf-8")):
        if role not in roles:
            continue
        if heading is not None:
            if body:
                body.append("")
            body.append(heading)
        body.extend(tidy(lines))
    return "\n".join(tidy(body)).strip() + "\n"


def frontmatter(spec):
    lines = ["---"]
    for key, value in spec:
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Build and install the Pi global agent policy bundle.")
    parser.add_argument("--out", type=Path, default=DEFAULT_BUILD,
                        help="release build directory (default: ./build)")
    parser.add_argument("--install", action="store_true",
                        help="install the completed build into ~/.agents after validation")
    parser.add_argument("--install-dir", type=Path, default=DEFAULT_INSTALL,
                        help="installation directory (default: ~/.agents)")
    return parser.parse_args(argv)


def safe_build_path(path):
    resolved = path.expanduser().resolve()
    root = ROOT.resolve()
    if resolved == root or resolved in root.parents:
        raise ValueError(f"refusing to use source tree or its parent as build output: {resolved}")
    return resolved


def copy_runtime_assets(build_dir):
    """Copy every deployable companion directory, retaining relative layout."""
    if not SKILLS_SOURCE.is_dir():
        raise FileNotFoundError(f"skills source directory not found: {SKILLS_SOURCE}")
    if not TEMPLATES_SOURCE.is_dir():
        raise FileNotFoundError(f"templates source directory not found: {TEMPLATES_SOURCE}")
    shutil.copytree(SKILLS_SOURCE, build_dir / "skills")
    shutil.copytree(TEMPLATES_SOURCE, build_dir / "templates")


def build_release(build_dir):
    if not LAW.is_file():
        raise FileNotFoundError(f"LAW source not found: {LAW}")

    # A release is reproducible: remove stale generated files from the previous build.
    if build_dir.exists():
        if build_dir.is_symlink():
            raise ValueError(f"refusing to clear symlink build directory: {build_dir}")
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True)

    written = []
    for role, spec in ROLES.items():
        target = spec["context"] or spec["agent"]
        if target is None:
            continue
        path = build_dir / target
        content = frontmatter(spec["frontmatter"]) if spec["frontmatter"] else ""
        content += MARK + "\n\n" + render_body(role)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        written.append(target)

    copy_runtime_assets(build_dir)
    return written


def install_release(build_dir, install_dir):
    """Merge the release into ~/.agents without deleting unrelated user files."""
    destination = install_dir.expanduser().resolve()
    if destination == Path.home().resolve() or destination == Path.home().resolve().parent:
        raise ValueError(f"refusing unsafe installation destination: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    # Copy contents, not the build directory itself, so paths land directly under ~/.agents.
    for child in build_dir.iterdir():
        target = destination / child.name
        if child.is_dir():
            shutil.copytree(child, target, dirs_exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(child, target)
    return destination


def main(argv):
    args = parse_args(argv)
    try:
        build_dir = safe_build_path(args.out)
        written = build_release(build_dir)
        print(f"built release: {build_dir}")
        print("generated: " + ", ".join(written))
        print("included: skills/, templates/")
        if args.install:
            destination = install_release(build_dir, args.install_dir)
            print(f"installed release contents to: {destination}")
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
