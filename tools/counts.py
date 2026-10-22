"""Check the per-section table against the corpus.

The table in docs/roadmap/balance_migration.md is derived, so it must equal AGENTS.yaml.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import law  # noqa: E402

DOC = HERE.parent / "docs/roadmap/balance_migration.md"


def main() -> int:
    corpus = law.corpus()
    sections = [name for name, body in corpus.items()
                if isinstance(body, dict) and name not in {"role_specs", "lexicon", "ceiling"}]
    want = {}
    for name in sections:
        body = corpus[name]
        want[name] = (
            sum(1 for r in body.values() if isinstance(r, dict) and r.get("_kind") == "act"),
            sum(1 for r in body.values() if isinstance(r, dict) and r.get("_kind") == "balance"),
        )

    rows = {}
    total = None
    for line in DOC.read_text(encoding="utf-8").split("\n"):
        cells = [c.strip().strip("*") for c in line.strip("|").split("|")]
        if len(cells) != 3:
            continue
        try:
            pair = (int(cells[1]), int(cells[2]))
        except ValueError:
            continue
        if cells[0] == "total":
            total = pair
        elif cells[0] in want:
            rows[cells[0]] = pair

    for name, pair in want.items():
        if rows.get(name) != pair:
            print(f"FAIL {name}: table {rows.get(name)} does not match corpus {pair}")
            return 1
    if len(rows) != len(want):
        print(f"FAIL the table names {len(rows)} sections, the corpus {len(want)}")
        return 1
    sums = (sum(a for a, _ in want.values()), sum(b for _, b in want.values()))
    if total != sums:
        print(f"FAIL total {total} does not match {sums}")
        return 1
    print(f"ok: {len(want)} sections, {sums[0]} acts, {sums[1]} balances")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
