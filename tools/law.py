#!/usr/bin/env python3
"""Render the law into the views agents read, and run every mechanical check on it.

    python3 tools/law.py            write the views
    python3 tools/law.py --check    check only, refusing any view that no longer matches

The views:
    AGENTS.md          the whole law, which is what a session in the workspace reads
    agents/<role>.md   one agent definition per role: the whole law plus that role's guide

Checks, run with the render and never apart from it:
    - every view is byte-identical to a fresh render
    - no banned word from the lexicon appears outside its own table or a frontmatter block
    - every guide is claimed by a role, and every role claims a guide that exists
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent
LAW = HERE / "law"
OUT_LAW = HERE / "AGENTS.md"
OUT_AGENTS = HERE / "agents"

SECTIONS = ["core.md", "records.md", "ops.md", "lexicon.md"]
PLANNER = "planner.md"


def read(name: str) -> str:
    return (LAW / name).read_text(encoding="utf-8").rstrip("\n") + "\n"


def prose(text: str) -> str:
    """The part of a view that is prose, not the definition table or the frontmatter."""
    if text.startswith("---\n"):
        text = text.split("\n---\n", 1)[1]
    return text.split("# Lexicon", 1)[0]


def ceiling() -> int:
    return int(read("ceiling").strip())


def banned_words() -> list[str]:
    table = read("lexicon.md")
    words: list[str] = []
    for line in table.splitlines():
        if not line.startswith("|") or "banned" in line or set(line) <= set("|- "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) == 3:
            words += [w.strip() for w in cells[2].split(",") if w.strip()]
    return words


def render_law() -> str:
    """The view an interactive session reads. It is the root, so it carries the node procedure."""
    parts = [read(s).rstrip("\n") for s in SECTIONS]
    parts.append(read(PLANNER).rstrip("\n"))
    parts.append(read("guides/node.md").rstrip("\n"))
    return "\n".join(parts) + "\n"


def render_role(role: str, spec: dict, law: str) -> str:
    """A role reads the law and its own procedure. Only the root reads the Node guide."""
    guide = LAW / "guides" / f"{spec['guide']}.md"
    front = [
        "---",
        f"name: {role}",
        f"description: {spec['description']}",
        f"tools: {spec['tools']}",
        "model: inherit",
        f"thinking: {spec['thinking']}",
        "systemPromptMode: replace",
        "inheritProjectContext: false",
        "inheritGlobalContext: false",
        "inheritSkills: false",
        "---",
    ]
    body = "" if spec["guide"] == "node" else guide.read_text(encoding="utf-8")
    return "\n".join(front) + "\n" + law + ("\n" + body if body else "")


def main() -> int:
    check = "--check" in sys.argv
    roles = yaml.safe_load(read("roles.yaml"))
    law = "\n".join(read(s).rstrip("\n") for s in SECTIONS) + "\n"
    root_view = render_law()
    views: dict[Path, str] = {OUT_LAW: root_view}
    for role, spec in roles.items():
        views[OUT_AGENTS / f"{role}.md"] = render_role(role, spec, law)

    failures: list[str] = []
    if check:
        for path, text in views.items():
            if not path.exists():
                failures.append(f"missing view: {path.relative_to(HERE)}")
            elif path.read_text(encoding="utf-8") != text:
                failures.append(f"stale view: {path.relative_to(HERE)}")
    else:
        OUT_AGENTS.mkdir(exist_ok=True)
        for path, text in views.items():
            path.write_text(text, encoding="utf-8")

    words = banned_words()
    for path, text in views.items():
        body = prose(text).lower()
        for word in words:
            if f" {word} " in f" {body} " or f" {word}." in body or f" {word}," in body:
                failures.append(f"banned word '{word}' in {path.relative_to(HERE)}")

    claimed = {s["guide"] for s in roles.values()}
    present = {p.stem for p in (LAW / "guides").glob("*.md")}
    for stale in OUT_AGENTS.glob("*.md"):
        if stale.stem not in roles:
            failures.append(f"agents/{stale.name} is no role")
    for name in sorted(claimed - present):
        failures.append(f"role claims a missing guide: {name}")
    for name in sorted(present - claimed):
        failures.append(f"guide no role claims: {name}")

    for name in SECTIONS:
        if not (LAW / name).exists():
            failures.append(f"missing section: law/{name}")

    words_in_law = len(root_view.split())
    if words_in_law > ceiling():
        failures.append(
            f"the law is {words_in_law} words over its ceiling of {ceiling()}: "
            "raise law/ceiling in the same commit, or delete what the new rule replaces")
    chars = len(law)
    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    print(f"ok: {len(views)} views, {words_in_law} words, {chars} chars, "
          f"{len(words)} banned words, {len(roles)} roles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
