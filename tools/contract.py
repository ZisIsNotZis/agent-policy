"""Check a contract before it is dispatched.

The field names come out of the law, not out of this file: `contract_identity._fields` names the
identity, `contract_fields._fields` the six floor lines and `contract_fields._above` the lines another
rule adds for this package. A contract carrying only the six is not full (`contract fields`), and a
contract missing a line goes back to the parent that wrote it (`unreadable contract`), so this tool
refuses both before the transport does.

    python3 tools/contract.py --check contract.md
    python3 tools/contract.py --check -        # from stdin
    python3 tools/contract.py --template       # the skeleton, generated from the law's names
    python3 tools/contract.py --self-test      # the check refuses what the law refuses
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent
LAW = HERE / "AGENTS.yaml"

# What each name the law lists decides. A name the law gains and this map lacks is refused loudly.
WHAT = {
    "kind": "the kind of contract, `worker contract` or `manager contract`",
    "name": "the package's name",
    "roadmap": "whose roadmap the result would change",
    "goal": "what the package is for",
    "scope": "what is inside it, and what is excluded",
    "accept": "the observation that decides done, with the command that produces it",
    "paths": "the exact paths that may be written, or `none` and what is done instead",
    "spend": "one class plus the wall-clock that ends the run, or `unknown` and when it becomes known",
    "stop": "the condition that ends the package before the clock does",
    "caps": "attempts, review rounds and no-progress rounds, as `budget caps` says",
    "tools": "the tools it gets and their limits, as `subagent scope` says",
    "model": "the model and the thinking level, named, as `model cost` says",
    "holds": "what it holds, as `worker` says: a manager's directory and name, or nothing",
    "rev": "the revision the review is bound to",
    "change": "the diff or artefact the review reads",
    "ran": "the mechanical checks and the commands that produced them",
    "judge": "the checks left to judgement",
    "blocking": "the criterion that makes a finding block",
    "budget": "the rounds and the wall-clock the review may spend",
    "escalate": "where an unanswerable question goes",
    "repair": "who repairs what the review finds",
}

CLASSES = {"time", "idle-compute", "metered-compute", "exclusive", "unrecoverable", "unknown"}
OLD_NAMES = {
    "boundary": "goal",
    "area": "paths",
    "acceptance": "accept",
    "report target": "roadmap",
    "wall-clock": "spend",
}
MAX_BYTES = 16384
HEADING = re.compile(r"^\s*[-*#>\s]*(?P<key>[A-Za-z][A-Za-z \-]*?)\s*:\s*(?P<value>.*)$")
COMMAND = re.compile(r"`[^`]+`|\b(python3?|sh|bash|npm|make|cargo|pytest|go test)\b")
DURATION = re.compile(r"\b\d+(?:\.\d+)?\s*(?:s|sec|min|h|hour|day)s?\b", re.I)
NOTHING = re.compile(r"\bnone\b|\bnothing\b", re.I)
READ_ONLY = re.compile(r"read|judge|review|write nothing", re.I)
MANAGER = re.compile(r"\bmanager\b", re.I)
REVIEW = re.compile(r"\breview\b", re.I)


def law_names() -> dict[str, dict]:
    """The names a contract carries, read from the law so this file cannot drift from it."""
    try:
        corpus = yaml.safe_load(LAW.read_text(encoding="utf-8"))
        flat = {k: v for body in corpus.values() if isinstance(body, dict) for k, v in body.items()}
        return {
            "identity": list(flat["contract_identity"]["_fields"]),
            "floor": list(flat["contract_fields"]["_fields"]),
            "above": dict(flat["contract_fields"]["_above"]),
            "review": list(flat["reviewer_contract"]["_fields"]),
        }
    except (OSError, KeyError, TypeError, AttributeError, yaml.YAMLError) as exc:
        raise SystemExit(f"FAIL the law is unreadable at {LAW}: {exc}")


def describe(name: str) -> str:
    if name not in WHAT:
        raise SystemExit(
            f"FAIL the law names `{name}:` and tools/contract.py has no line saying what it decides")
    return WHAT[name]


def fields(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for line in text.splitlines():
        m = HEADING.match(line)
        if not m:
            continue
        key = " ".join(m.group("key").lower().split())
        found.setdefault(key, m.group("value").strip())
    return found


def missing(key: str, line: str | None) -> str | None:
    if line is None:
        return f"no `{key}:` line — the contract must say {describe(key)}"
    if not line:
        return f"`{key}:` is empty — a blank field is not a declaration"
    return None


def check(text: str) -> list[str]:
    found = fields(text)
    names = law_names()
    failures: list[str] = []

    for key in names["identity"] + names["floor"]:
        bad = missing(key, found.get(key))
        if bad:
            failures.append(bad)

    for key, rule in names["above"].items():
        bad = missing(key, found.get(key))
        if bad:
            failures.append(
                f"{bad} — the six are the floor, and `{rule.replace('_', ' ')}` puts this line above it")

    for old, new in OLD_NAMES.items():
        if old in found:
            failures.append(f"`{old}:` is the old name; the law says `{new}:`")

    kind = found.get("kind", "")
    if REVIEW.search(kind):
        for key in names["review"]:
            if not found.get(key):
                failures.append(
                    f"no `{key}:` line — a review contract carries the nine of `reviewer contract`, "
                    f"and this one says {describe(key)}")

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

    stop = found.get("stop", "")
    if stop:
        if NOTHING.search(stop) and len(stop.split()) < 4:
            failures.append("`stop:` says nothing ends it — name the condition that ends the package")
        elif DURATION.search(stop) and len(DURATION.sub(" ", stop).split()) < 3:
            failures.append(
                "`stop:` restates the wall-clock — name the condition that ends the package before "
                "the clock does, or the run returns nothing when it is killed")

    holds = found.get("holds", "")
    if holds and MANAGER.search(kind) and NOTHING.search(holds):
        failures.append("`holds:` says nothing and the kind is a manager contract — a manager holds a directory and a name")

    paths = found.get("paths", "")
    if paths and NOTHING.search(paths) and not READ_ONLY.search(paths):
        failures.append("`paths:` says nothing may be written, so say what the package does instead")

    size = len(text.encode("utf-8"))
    if size > MAX_BYTES:
        failures.append(f"{size} bytes — the dispatch transport refuses a payload above {MAX_BYTES}")
    return failures


def template() -> str:
    names = law_names()
    lines = [f"{key}: <{describe(key)}>" for key in names["identity"]]
    lines.append("")
    lines += [f"{key}: <{describe(key)}>" for key in names["floor"]]
    lines.append("")
    lines += [f"{key}: <{describe(key)}>  # above the floor: `{rule.replace('_', ' ')}`"
              for key, rule in names["above"].items()]
    lines.append("")
    lines.append("# a review contract also carries " + ", ".join(
        k for k in names["review"] if k not in names["floor"]))
    return "\n".join(lines) + "\n"


def without(text: str, keys) -> str:
    prefixes = tuple(f"{key}:" for key in keys)
    return "\n".join(line for line in text.splitlines() if not line.startswith(prefixes))


def self_test() -> list[str]:
    good = """kind: worker contract
name: self-test
roadmap: agent-policy

goal: prove the check refuses what the law refuses
scope: this tool; no other directory
accept: `python3 tools/contract.py --self-test` exits 0
paths: none; reads only
spend: idle-compute, 5 min wall-clock
stop: the self-test exits, or the 5 min clock ends it

caps: 1 attempt, 1 review round, 0 no-progress rounds
tools: `read`, `bash`; writes nothing outside this repository
model: the site default, thinking low
holds: nothing; it writes no directory, document or roadmap
"""
    names = law_names()
    failures: list[str] = []
    if check(good):
        failures.append(f"a full contract was refused: {check(good)}")
    for key in names["identity"] + names["floor"] + list(names["above"]):
        if not any(f.startswith(f"no `{key}:`") for f in check(without(good, [key]))):
            failures.append(f"a contract without `{key}:` passed")
    six_only = without(good, names["above"])
    if not any("floor" in f for f in check(six_only)):
        failures.append("a contract carrying the six and nothing above them passed")
    for old in OLD_NAMES:
        if not any(old in f for f in check(good.replace("paths:", f"{old}:", 1))):
            failures.append(f"the old name `{old}:` passed")
    if not check(good.replace("`python3 tools/contract.py --self-test` exits 0", "it works")):
        failures.append("`accept:` with no command passed")
    if not check(good.replace("spend: idle-compute, 5 min wall-clock", "spend: idle-compute")):
        failures.append("`spend:` with no wall-clock passed")
    if not any("clock" in f for f in check(without(good, ["spend"]))):
        failures.append("a contract with no `spend:` line did not name the clock")
    if not check(good.replace("stop: the self-test exits, or the 5 min clock ends it", "stop: none")):
        failures.append("`stop: none` passed")
    if not check(good.replace("stop: the self-test exits, or the 5 min clock ends it", "stop: 30 min")):
        failures.append("`stop:` restating the wall-clock passed")
    manager = good.replace("kind: worker contract", "kind: manager contract").replace(
        "holds: nothing; it writes no directory, document or roadmap", "holds: nothing")
    if not check(manager):
        failures.append("a manager contract holding nothing passed")
    if not any("reviewer contract" in f for f in check(good.replace("kind: worker contract", "kind: review contract"))):
        failures.append("a review contract without the nine passed")
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
        names = law_names()
        print(f"ok: {len(names['identity'])} identity lines, {len(names['floor'])} floor lines, "
              f"{len(names['above'])} above the floor, {len(names['review'])} in a review contract, "
              f"old names, command, wall-clock, stop, byte limit")
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
    print(f"ok: identity, floor, above the floor, {len(text.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
