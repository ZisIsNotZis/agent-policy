"""Check a contract before it is dispatched.

The law says a contract carries four things and two declarations, and that a contract missing
one of them is a report rather than a dispatch. Nothing checked the dispatcher, so the first
review to look at a package found its own contract missing the report target, the spend class
and the write area. This reads a contract and names what is absent.

    python3 tools/contract.py --check contract.md
    python3 tools/contract.py --check -        # from stdin
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FIELDS = {
    "boundary": ("boundary", "what this package is for"),
    "area": ("area", "what may be written, and `none` when nothing may"),
    "acceptance": ("acceptance", "the observation that decides done"),
    "target": ("report target", "the node whose roadmap the result would change"),
    "spend": ("spend", "one of the five classes, or `unknown` and when it becomes known"),
    "wall-clock": ("wall-clock", "how long the package may hold its node"),
}

CLASSES = {"time", "idle-compute", "metered-compute", "exclusive", "unrecoverable", "unknown"}

HEADING = re.compile(r"^\s*[-*#>\s]*(?P<key>[A-Za-z][A-Za-z \-]*?)\s*:\s*(?P<value>.*)$")


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
    for key, (label, what) in FIELDS.items():
        value = found.get(label)
        if value is None:
            failures.append(f"no `{label}:` line — the contract must say {what}")
        elif not value:
            failures.append(f"`{label}:` is empty — a blank field is not a declaration")
    spend = found.get("spend", "")
    if spend:
        named = {w.strip(" `,;.()").lower() for w in spend.split()} & CLASSES
        if not named:
            failures.append(
                f"`spend:` names no class — one of {', '.join(sorted(CLASSES))}, "
                "and `unknown` with the moment it becomes known")
        elif "unknown" in named and len(spend.split()) < 4:
            failures.append("`spend: unknown` must say when it becomes known")
    area = found.get("area", "").lower()
    if area and re.search(r"\bnone\b|\bnothing\b", area) and not re.search(r"read|judge|review|write nothing", area):
        failures.append("`area:` says nothing may be written, so say what the package does instead")
    return failures


def main() -> int:
    args = sys.argv[1:]
    if "--check" not in args:
        print(__doc__.strip())
        return 2
    arg = args[args.index("--check") + 1] if args.index("--check") + 1 < len(args) else "-"
    text = sys.stdin.read() if arg == "-" else Path(arg).read_text(encoding="utf-8")
    failures = check(text)
    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    print("ok: boundary, area, acceptance, report target, spend class, wall-clock")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
