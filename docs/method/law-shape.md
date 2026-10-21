# Law shape

How the law is written, so that a node reads only what its own work needs.

## What it was, and why it stopped working

One YAML tree of 315 nodes, rendered into a single 97,698-character view that every session in the workspace loads. Three measured properties made it ineffective rather than merely large.

Every session spent about 2,700 tokens of context before doing anything. Every node carried the same imperative strength, so no node was harder than another and all of them read as advice. And an addition was free while a deletion cost an argument, so the tree could only grow.

## The form now

Four prose documents and six guides, held in `law/`.

`core.md` states the structure, speech, reports, consent, argument, subordination and amendment. It is the part no node may violate.

`records.md` states the shape of a node's document and the coordinates a fact carries.

`ops.md` states the run discipline: nothing long inside a turn, land before reporting, intent before the act, the safe point, durability, no trash, recovery.

`lexicon.md` holds one word per concept and the banned synonyms, refused by the check.

`guides/` holds one procedure per role. A guide states the trigger, the steps, the acceptance and the failure route for that role's work, and nothing general.

The law is 3,933 words, 87 per cent smaller than the view it replaced. The check prints the current figure, because a number restated in prose drifts.

## Why prose

A list lets fragments be stapled together; a paragraph forces one coherent model. The old tree grew exactly because each indentation level was an independently weldable point that needed to agree with nothing. Prose costs more to write and refuses that.

## The views

`tools/law.py` renders two kinds of view from one source.

`AGENTS.md` is the whole law, which is what a session in the workspace reads. It is the complete text and there is no second place where a rule lives.

`agents/<role>.md` is one agent definition per role: the whole law plus that role's guide, with `inheritProjectContext: false` so a child gets the law and its procedure and never a project's instructions or a policy source it saw in passing.

The views are generated and never edited. `--check` refuses a view that no longer matches, a banned word outside the lexicon table, a role claiming a guide that does not exist, and a guide no role claims.

## The ledger

`docs/result/migration-ledger.tsv` holds one row per node of the old tree: its key, its destination among seven, the home it landed in, and what absorbed it.

The check refuses a missing row, a duplicate row, a home that does not exist and a destination outside the seven, so "no rule was lost" is a property of the file rather than a claim about the migration.

## Seven destinations

`core`, `guides`, `records`, `ops`, `lexicon`, `retired`, `people`.

Sixty-two rows land in core, 131 in the guides, 81 in ops, 26 in records and 20 are retired. Each retired row names what falsified it, so the same two-hundred-word rule cannot come back.
