# agent-policy

Standing law for AI agents working in a repository: who is a node, who speaks to whom, what a report carries, where a fact lives, and who may decide.

**For** someone who wants an agent held to something checkable, and for reading what this author's agents actually work under.
**Not for** a product, a framework or a promise. It is one author's law, written for one human working with agents. It refuses most of what a coding agent does by default: it kills deprecated material instead of annotating it, it treats a person's words as evidence about the end rather than a specification of the means, and it sends a failure to the layer that should have prevented it.

## Read it

[AGENTS.md](AGENTS.md) is the law plus the node procedure, generated from [law/](law) and never edited. It is four short documents and the six role guides, of which a session reads one, 9,950 characters, which a session reads instead of a project's instructions.

- [law/core.md](law/core.md) — structure, speech, reports, consent, argument, subordination, amendment.
- [law/records.md](law/records.md) — the shape of a node's document, and the coordinates a fact carries.
- [law/ops.md](law/ops.md) — nothing long inside a turn, land before reporting, the safe point, durability, no trash.
- [law/lexicon.md](law/lexicon.md) — one word per concept, and the banned synonyms a check refuses.
- [law/guides/](law/guides) — one procedure per role: node, worker, reviewer, diagnoser, builder, researcher.

A node reads one document: itself. It does not read another node's document, and it does not read this law twice.

## Check it

```sh
python3 tools/law.py --check
```

Prints `ok: 7 views, 1287 words, 7153 chars, 23 banned words, 6 roles` and takes 0.2 s on a fresh clone with Python 3.12 and PyYAML. It refuses a view that no longer matches the source, a banned word outside the lexicon table, a role claiming a guide that does not exist, and a guide no role claims.

Run it on every commit instead of remembering to:

```sh
git config core.hooksPath .githooks
```

## Install it

`tools/law.py` writes `AGENTS.md` and one agent definition per role into `agents/`. In a workspace, link both:

```sh
ln -s ../../agent-policy/AGENTS.md AGENTS.md
for r in root worker reviewer diagnoser builder researcher; do
  ln -s ../../../agent-policy/agents/$r.md .pi/agents/$r.md
done
```

Each generated agent carries `inheritProjectContext: false`, so a child gets the law and its own procedure and never a project's instructions or a policy source it met in passing.

## Status and limits

- Status and work in flight live in [docs/plan/policy.md](docs/plan/policy.md); the commitment is [docs/product/policy.md](docs/product/policy.md); the shape of the law is [docs/method/law-shape.md](docs/method/law-shape.md).
- [docs/result/migration-ledger.tsv](docs/result/migration-ledger.tsv) records where each of the 315 rules of the previous law went, one row each, with the twenty that were retired and what falsified them.
- The rule a check can enforce is enforced; the rest is prose. Prose is followed unevenly by a cheap model, so any rule here that matters in practice should be moved into a check rather than trusted.

## Report a problem

Open an issue at [ZisIsNotZis/agent-policy/issues](https://github.com/ZisIsNotZis/agent-policy/issues). A defect report is most useful with the rule's name, the situation it fired in, and what the agent did instead.

## Licence

MIT. Take the rules, change them, ship them.
