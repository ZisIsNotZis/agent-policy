"""Check the case list against the law and against its own score.

Every sentence a row cites must be one the role reads, and the score table must equal its own
rows. A case list that scores a rule the role cannot read is the defect this refuses.

    python3 tools/cases.py            check docs/review/cases.md
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import law  # noqa: E402

ROOT = HERE.parent
CASES = ROOT / "docs/review/cases.md"
AXES = {"authority", "proceed"}
VERDICTS = {"stated", "delegated", "ambiguous", "silent"}


def main() -> int:
    corpus = law.corpus()
    rules = {}
    for body in corpus.values():
        if isinstance(body, dict):
            for name, rule in body.items():
                if isinstance(rule, dict) and rule.get("_kind") in {"act", "balance", "principle"}:
                    rules[name] = rule

    rows = []
    role = None
    for line in CASES.read_text(encoding="utf-8").split("\n"):
        head = re.match(r"^## ([a-z_]+)$", line)
        if head:
            role = head.group(1)
            continue
        if not line.startswith("| ") or role is None or "`" not in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 4:
            continue
        moment, axis, verdict, cite = cells
        if axis not in AXES:
            print(f"FAIL axis {axis!r} in {role}: {moment}")
            return 1
        if verdict not in VERDICTS:
            print(f"FAIL verdict {verdict!r} in {role}: {moment}")
            return 1
        for name in re.findall(r"`([a-z_][a-z0-9_]*)`", cite):
            if name not in rules:
                continue
            if not law.reads(role, rules[name]["scope"]):
                print(f"FAIL {role} cites {name}, which its view does not read")
                return 1
        rows.append((role, verdict))

    counted = {}
    for role, verdict in rows:
        box = counted.setdefault(role, dict.fromkeys(VERDICTS, 0))
        box[verdict] += 1

    table = {}
    for line in CASES.read_text(encoding="utf-8").split("\n"):
        cells = [cell.strip().strip("*") for cell in line.strip("|").split("|")]
        if len(cells) == 6 and re.fullmatch(r"[a-z_]+|total", cells[0]):
            try:
                nums = [int(cell) for cell in cells[1:]]
            except ValueError:
                continue
            if sum(nums[1:]) != nums[0]:
                print(f"FAIL row {cells[0]} sums to {sum(nums[1:])}, not {nums[0]}")
                return 1
            key = cells[0]
            table[key] = dict(zip(("cases", "stated", "delegated", "ambiguous", "silent"), nums))

    for role, box in counted.items():
        want = table.get(role)
        got = (sum(box.values()), box["stated"], box["delegated"], box["ambiguous"], box["silent"])
        if want is None:
            print(f"FAIL {role} has {got[0]} rows and no table row")
            return 1
        if tuple(want[k] for k in ("cases", "stated", "delegated", "ambiguous", "silent")) != got:
            print(f"FAIL {role} table {want} does not match its rows {got}")
            return 1

    total = table.get("total")
    got = (
        len(rows),
        sum(1 for _, v in rows if v == "stated"),
        sum(1 for _, v in rows if v == "delegated"),
        sum(1 for _, v in rows if v == "ambiguous"),
        sum(1 for _, v in rows if v == "silent"),
    )
    if total is None or tuple(total[k] for k in ("cases", "stated", "delegated", "ambiguous", "silent")) != got:
        print(f"FAIL total {total} does not match the rows {got}")
        return 1

    print(f"ok: {len(rows)} cases, every citation readable, score table equals its rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
