"""Refuse two rules that say the same thing in the same place.

Two rules with the same band and an overlapping scope are one rule twice; the reader pays for
both and the second copy drifts. This catches a verbatim copy. A paraphrase is not caught here:
`amend_by_replacement` and the reviewer's redundancy check are what close that case.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import law  # noqa: E402

THRESHOLD = 0.8


def words(text: str) -> set[str]:
    text = re.sub(r"`|\*", "", text.lower())
    return {w for w in re.findall(r"[a-z][a-z_]+", text) if len(w) > 2}


def main() -> int:
    rules = []
    for name, body in law.corpus().items():
        if not isinstance(body, dict) or name in {"role_specs", "lexicon", "ceiling"}:
            continue
        for key, node in body.items():
            if not isinstance(node, dict) or node.get("_kind") not in {"act", "balance"}:
                continue
            band = node.get("_between") or node.get("_how") or {}
            text = band.get("en") or ""
            if not text:
                continue
            rules.append((key, words(text), set(node.get("scope") or [])))

    fails = []
    for i, (name, bag, scope) in enumerate(rules):
        for other, obag, oscope in rules[i + 1:]:
            if not scope & oscope:
                continue
            union = bag | obag
            if not union:
                continue
            if len(bag & obag) / len(union) >= THRESHOLD:
                fails.append((name, other))

    if fails:
        for a, b in fails:
            print(f"FAIL {a} and {b} say the same thing to the same roles")
        return 1
    print(f"ok: {len(rules)} rules, no band is copied verbatim")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
