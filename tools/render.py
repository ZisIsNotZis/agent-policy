#!/usr/bin/env python3
"""Render the role views from LAW.md.

LAW.md is the law: one hand-written source. A heading carries its role tags
(`@manager`, `@submanager`, `@worker`); a view is the shared sections plus the
role's sections.

    "# Heading @manager @submanager"   the whole section, children included, belongs to those roles
    "# Heading"                        no tags: inherit the nearest tagged ancestor heading

A heading with no tags takes its parent heading's role set, and that inherits up
the chain. A chain with no tag anywhere belongs to no role: it is source and
compiler material, and no view includes it. So content for every role needs
`@manager @submanager @worker` on its heading.

Tags never appear in a view. Three roles, three targets:

    manager.md             the root manager body alone, no frontmatter: the default agent's context
    agents/submanager.md   a sub-manager definition: frontmatter, then the body
    agents/worker.md       a worker definition: frontmatter, then the body

    python3 tools/render.py            render every view
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAW = ROOT / "LAW.md"
MARK = "<!-- generated from LAW.md by tools/render.py; edit LAW.md, not this file -->"

# Views the law no longer defines; removed on a render so no stale role survives.
OBSOLETE = ["agents/manager.md"]

# A role tag is trailing: whitespace, @, the role name.
TAG_END = re.compile(r"[ \t]+@([a-z_]+)\s*$")
HEADING = re.compile(r"(#{1,6})[ \t]")

ROLES = {
    "manager": {
        "agent": None,
        "context": "AGENTS.md",
        "frontmatter": [],
    },
    "submanager": {
        "agent": "agents/submanager.md",
        "context": None,
        "frontmatter": [
            ("name", "submanager"),
            ("description", "You run one subproject under a parent Manager. You own its docs, its Roadmap, and the agents under it."),
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
            ("description", "You execute exactly one work package in your manager's area, and report once."),
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


def main(argv):
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
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    for rel in OBSOLETE:
        path = ROOT / rel
        if path.exists():
            path.unlink()
    if stale:
        print("wrote: " + ", ".join(stale))
    else:
        print("unchanged: views already match the law")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
