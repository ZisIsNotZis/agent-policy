#!/usr/bin/env python3
"""Render the role views from LAW.md.

LAW.md is the law: one hand-written markdown file, edited by hand. A role reads a
view, never the law itself. Two tags do the split:

    "# Heading @manager"       the whole section belongs to those roles; no tag: every role
    "- item ... @worker"       the block (this line plus its indented children) belongs to those roles

Tags never appear in a view. A view is written to two places:

    agents/<role>.md   an agent definition: frontmatter, then the body
    AGENTS.md          the manager body alone, no frontmatter: the default agent's context file

`~/.pi/agent/agents` is a symlink to `agents/`, so a view is installed by being written here.

    python3 tools/render.py            render every view
    python3 tools/render.py --check    fail if a view on disk differs from what the law renders
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAW = ROOT / "LAW.md"
MARK = "<!-- generated from LAW.md by tools/render.py; edit LAW.md, not this file -->"

# A role tag is trailing: whitespace, @, the role name, and either the line end or another tag.
TAG_END = re.compile(r"[ \t]+@([a-z_]+)\s*$")

ROLES = {
    "manager": {
        "agent": "agents/manager.md",
        "context": "manager.md",
        "frontmatter": [
            ("name", "manager"),
            ("description", "You hold a project: its docs, its roadmap and the agents under it."),
            ("tools", "read, edit, write, bash, grep, find, ls, subagent"),
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
            ("description", "You execute exactly one workpackage in your manager's area, and report once."),
            ("tools", "read, edit, write, bash, grep, find, ls"),
            ("thinking", "low"),
            ("advertise", "true"),
            ("systemPromptMode", "replace"),
            ("inheritProjectContext", "false"),
            ("inheritGlobalContext", "false"),
            ("inheritSkills", "true"),
        ],
    },
}


def parse(text):
    """Return [(heading line or None, [body lines])] split on level-1 headings outside fences."""
    sections = []
    current = None
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("# "):
            current = (line, [])
            sections.append(current)
        else:
            if current is None:
                current = (None, [])
                sections.append(current)
            current[1].append(line)
    return sections


def take_tags(line):
    """Strip the trailing role tags off one line; return (roles, stripped line).

    Only trailing tags whose name is a role are stripped, so a sentence ending in
    an @-token that is not a role survives in every view."""
    roles = set()
    while True:
        m = TAG_END.search(line)
        if m is None or m.group(1) not in ROLES:
            return roles, line.rstrip()
        roles.add(m.group(1))
        line = line[: m.start()]


def filter_body(body, role):
    """Keep one role's blocks: a tagged line and its indented children follow that line's fate."""
    kept = []
    drop_indent = None
    for line in body:
        if not line.strip():
            kept.append("")
            continue
        indent = len(line) - len(line.lstrip(" \t"))
        if drop_indent is not None and indent > drop_indent:
            continue
        drop_indent = None
        roles, stripped = take_tags(line)
        if roles and role not in roles:
            drop_indent = indent
            continue
        kept.append(stripped)
    while kept and not kept[-1].strip():
        kept.pop()
    while kept and not kept[0].strip():
        kept.pop(0)
    out = []
    for line in kept:
        if not line.strip() and out and not out[-1].strip():
            continue
        out.append(line)
    return out


def render_body(role):
    body = []
    for heading, lines in parse(LAW.read_text(encoding="utf-8")):
        roles = set()
        if heading is not None:
            roles, heading = take_tags(heading)
        if roles and role not in roles:
            continue
        if heading is not None:
            if body:
                body.append("")
            body.append(heading)
        body.extend(filter_body(lines, role))
    return "\n".join(body).strip() + "\n"


def frontmatter(spec):
    lines = ["---"]
    for key, value in spec:
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def main(argv):
    check = "--check" in argv
    stale = []
    for role, spec in ROLES.items():
        for target, head in ((spec["agent"], frontmatter(spec["frontmatter"])), (spec["context"], "")):
            if target is None:
                continue
            path = ROOT / target
            text = head + MARK + "\n\n" + render_body(role)
            old = path.read_text(encoding="utf-8") if path.exists() else None
            if old == text:
                continue
            stale.append(target)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
    if check:
        if stale:
            print("stale: " + ", ".join(stale))
            return 1
        print("ok: views match the law")
        return 0
    if stale:
        print("wrote: " + ", ".join(stale))
    else:
        print("unchanged: views already match the law")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
