"""Check a contract before it is dispatched.

The law names a contract's identity and six fields: `contract_identity` says the kind, the
name and whose roadmap it serves; `contract_fields` says goal, scope, accept with its command,
paths, spend with wall-clock, stop. A contract missing one of them is a report rather than a
dispatch. Nothing ran this check, so the field names here had drifted from the law and ten
contracts were built by hand until the transport refused them at 16384 bytes.

    python3 tools/contract.py --check contract.md
    python3 tools/contract.py --check -        # from stdin
    python3 tools/contract.py --template       # the skeleton, generated from the fields below
    python3 tools/contract.py --self-test      # the check refuses what the law refuses
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

IDENTITY = {
    "kind": "the kind of contract, e.g. `worker contract` or `manager contract`",
    "name": "the package's name",
    "roadmap": "whose roadmap the result would change",
}

FIELDS = {
    "goal": "what the package is for",
    "scope": "what is inside it, and what is excluded",
    "accept": "the observation that decides done, with the command that produces it",
    "paths": "the exact paths that may be written, or `none` and what is done instead",
    "spend": "one class and a wall-clock, or `unknown` and when it becomes known",
    "stop": "the first condition that ends the package",
}

OLD_NAMES = {
    "boundary": "goal",
    "area": "paths",
    "acceptance": "accept",
    "report target": "roadmap",
    "wall-clock": "spend",
}

CLASSES = {"time", "idle-compute", "metered-compute", "exclusive", "unrecoverable", "unknown"}
MAX_BYTES = 16384
HEADING = re.compile(r"^\s*[-*#>\s]*(?P<key>[A-Za-z][A-Za-z \-]*?)\s*:\s*(?P<value>.*)$")
COMMAND = re.compile(r"`[^`]+`|\b(python3?|sh|bash|npm|make|cargo|pytest|go test)\b")
DURATION = re.compile(r"\b\d+(?:\.\d+)?\s*(?:s|sec|min|h|hour|day)s?\b", re.I)
NOTHING = re.compile(r"\bnone\b|\bnothing\b", re.I)
READ_ONLY = re.compile(r"read|judge|review|write nothing", re.I)


def fields(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for line in text.splitlines():
        m = HEADING.match(line)
        if not m:
            continue
        key = " ".join(m.group("key").lower().split())
        found.setdefault(key, m.group("value").strip())
    return found


def check(text: str) -> list[str]:
    found = fields(text)
    failures: list[str] = []
    for key, what in {**IDENTITY, **FIELDS}.items():
        value = found.get(key)
        if value is None:
            failures.append(f"no `{key}:` line — the contract must say {what}")
        elif not value:
            failures.append(f"`{key}:` is empty — a blank field is not a declaration")
    for old, new in OLD_NAMES.items():
        if old in found:
            failures.append(f"`{old}:` is the old name; the law says `{new}:`")

    accept = found.get("accept", "")
    if accept and not COMMAND.search(accept):
        failures.append("`accept:` names no command — say how the observation is produced, in backticks")

    spend = found.get("spend", "")
    if spend:
        named = {w.strip(" `,;.()").lower() for w in spend.split()} & CLASSES
        if not named:
            failures.append(
                f"`spend:` names no class — one of {', '.join(sorted(CLASSES))}, "
                "and `unknown` with the moment it becomes known")
        elif "unknown" in named and len(spend.split()) < 4:
            failures.append("`spend: unknown` must say when it becomes known")
        elif not DURATION.search(spend):
            failures.append("`spend:` names no wall-clock — add how long it may hold the node")

    paths = found.get("paths", "")
    if paths and NOTHING.search(paths) and not READ_ONLY.search(paths):
        failures.append("`paths:` says nothing may be written, so say what the package does instead")

    size = len(text.encode("utf-8"))
    if size > MAX_BYTES:
        failures.append(f"{size} bytes — the dispatch transport refuses a tasks payload above {MAX_BYTES}")
    return failures


def template() -> str:
    lines = ["kind: <worker|manager> contract", "name: <package>", "roadmap: <whose roadmap it serves>", ""]
    for key, what in FIELDS.items():
        lines.append(f"{key}: <{what}>")
    return "\n".join(lines) + "\n"


def self_test() -> list[str]:
    good = """kind: worker contract
name: self-test
roadmap: agent-policy

goal: prove the check refuses what the law refuses
scope: this tool; no other directory
accept: `python3 tools/contract.py --self-test` exits 0
paths: none; reads only
spend: idle-compute, 5 min wall-clock
stop: the self-test exits
"""
    failures: list[str] = []
    if check(good):
        failures.append(f"a valid contract was refused: {check(good)}")
    for key in (*IDENTITY, *FIELDS):
        broken = "\n".join(line for line in good.splitlines() if not line.startswith(f"{key}:"))
        if not any(f.startswith(f"no `{key}:`") for f in check(broken)):
            failures.append(f"a contract without `{key}:` passed")
    for old in OLD_NAMES:
        renamed = good.replace("paths:", f"{old}:", 1)
        if not any(old in f for f in check(renamed)):
            failures.append(f"the old name `{old}:` passed")
    if not check(good.replace("`python3 tools/contract.py --self-test` exits 0", "it works")):
        failures.append("`accept:` with no command passed")
    if not check(good.replace("spend: idle-compute, 5 min wall-clock", "spend: idle-compute")):
        failures.append("`spend:` with no wall-clock passed")
    if not check(template()):
        failures.append("the generated template passed")
    return failures


def main() -> int:
    args = sys.argv[1:]
    if "--template" in args:
        print(template(), end="")
        return 0
    if "--self-test" in args:
        failures = self_test()
        if failures:
            print("\n".join(f"FAIL {f}" for f in failures))
            return 1
        print("ok: identity, six fields, old names, command, wall-clock, byte limit")
        return 0
    if "--check" not in args:
        print(__doc__.strip())
        return 2
    arg = args[args.index("--check") + 1] if args.index("--check") + 1 < len(args) else "-"
    text = sys.stdin.read() if arg == "-" else Path(arg).read_text(encoding="utf-8")
    failures = check(text)
    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    print(f"ok: identity, six fields, {len(text.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
