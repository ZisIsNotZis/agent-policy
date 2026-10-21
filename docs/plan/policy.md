# Policy

The product is the law in `law/`, rendered to `AGENTS.md` and to one agent definition per role, and checked by `python3 tools/law.py --check`. This is the plan for that product.

## Status

- `law/` is the only source and `AGENTS.md` plus `agents/*.md` are its generated views; `python3 tools/law.py --check` passes in 0.09 s and runs on every commit through `.githooks/pre-commit`, enabled once per clone by `git config core.hooksPath .githooks`, and in CI for a contributor's pull request.
- The law lives here and the workspace consumes it at a pinned submodule, with its root `AGENTS.md` a symlink into that submodule, so the text has one home and is still physically at the level an agent reads.
- No document cites a ticket, an issue or a session.

## Amendment one, agreed

Rulings: a claim that no longer describes the world dies while retraction, a negative finding and evidence survive; `upkeep.archive` and the compatibility clause die; `roles.inversion` carries the end/means split, one round of argument, then execution with the dissent recorded, and urgency buys one line of explanation; the superseded catalogue work records are killed rather than annotated.

Nodes: `ssot.kill`, `upkeep.supersede`, `record.plan_tree`, `roles.inversion`, `discussion.corrected`, `self_improvement.intake`.
Edits: `discussion.divergence` also covers the terse or heated message; `outdated` loses the compatibility clause; `people` and `files` no longer assume this repository is the only scope; the naming rule loses its guidance-only mark once the lint refuses the shape.

## Amendment two, applied

The law changed form: from one 315-node tree read whole by every agent, to four prose documents plus one guide per role, so that a node reads only what its own work needs. `docs/method/law-shape.md` holds the form; `law/` holds the text.

The old tree loaded 97,698 characters into every session, carried the same imperative strength on every node, and could only grow because addition was free and deletion was not. The law is now 7,511 characters, with a banned-word check, a view check and a ledger behind it.

`milestone` is a relation rather than a category: a milestone is a point a node must report to the layer above, and a work package is a unit it executes without reporting. Both are recursive, so each layer owns its own roadmap, and a work package large enough becomes a child node holding a roadmap of its own. The root's milestones are therefore the only ones a person sees, which is what `milestone_list` already meant.

A node lives exactly as long as its roadmap. It is not re-created per work package or per milestone, and no rule asks it to weigh reuse against a fresh start: the question is dropped rather than answered, because paying that judgement at every layer costs more than the rare case it saves. A node's context stays small by construction, since its doc carries only its roadmap, the milestone it is on, and the last report.

A node may execute and may also split. What it may not do is split, and then execute the piece it just split off.

### Seven destinations

Every current node lands in exactly one of these.

- `core` — who is a node, who speaks to whom, the three fields of a report, and what needs consent.
- `guides` — one prose guide per role: its trigger, steps, acceptance and failure route, carrying the method for diagnosis, design, testing, review and research.
- `records` — how a fact carries its coordinates, what assent means, and the shape of a node's doc.
- `ops` — the run discipline: nothing long inside a turn, checkpoint before the act, the safe point.
- `lexicon` — one word per concept with its banned synonyms, held by a grep.
- `retired` — a claim the discussion falsified, killed with its retraction rather than annotated: the discussion/advance axis, `timeout` as the guard against a stuck process, `dispatch_identity`'s global goal, and a milestone as a user-only gate.
- `people` — unchanged where it is.

### The ledger

`tools/migration-ledger.tsv`, one row per current node: key, destination, home, form, note.

- Every key in the source has exactly one row.
- Every `home` names a file that exists when the migration ends.
- `destination` is one of the seven.
- The check fails on a missing row, a duplicate row, an empty home, or a value outside the seven.

That turns "no information is lost" from a promise into a property of the file.

### Work packages

- `ledger` — extract every key, write the skeleton, and let the check fail until each row names its home.
- `core` — the hard core, in prose.
- `guides` — one guide per role.
- `records-and-ops` — the two remaining prose documents.
- `lexicon` — the word table and its grep, wired into the existing pre-commit hook.
- `rerun` — run one fixed set of tasks under the old law and the new, and compare what each violated.
- `delete` — the source and the old render go to git history, and a grep for every name they carried returns nothing.

## Work packages

- `ledger` — done. 315 rows in `docs/result/migration-ledger.tsv`, one destination each: 57 core, 131 guides, 81 ops, 26 records, 20 retired. The source and the ledger script are deleted with it, so the ledger is a record rather than a check.
- `core` — done. `law/core.md`, 411 words.
- `guides` — done. Six guides, one per role, each claimed by exactly one role and checked.
- `records-and-ops` — done. `law/records.md` and `law/ops.md`.
- `lexicon` — done. 23 banned words, refused by `tools/law.py`.
- `rerun` — done for the report shape and the scope boundary. Three runs of the same contract: a builtin worker returned a five-section progress report, and the law's worker returned the three fields twice, once at low thinking and once at high. Not done: the blocking behaviour, which the law states and the cheap model still violates.
- `delete` — done. `AGENTS.yaml`, `render_policy.py` and `tools/ledger.py` are gone; a grep for either name returns nothing outside the ledger and this line.

- `1.structural-move` — done. `plain_name` sits beside `one_name`, and the render differs by that one line alone.
- `2.amendment` — done. Six nodes at their homes (`ssot.kill`, `upkeep.supersede`, `record.plan_tree`, `roles.inversion`, `discussion.corrected`, `self_improvement.intake`), `upkeep.archive` deleted, and `outdated`, `people`, `files`, `retraction`, `align`, `divergence` and `plain_name` corrected against it; the check passes and the render carries all six.
- `3.names` — the lint over document text and file names, in this repository and in the workspace. Acceptance: zero hits, check passes, the workspace's catalogue scripts still reproduce their artefacts.
- `4.inheritance` — the renderer chains a scope's own source onto this one and refuses a duplicate key, so a scope can refine these rules without copying them.

## Open questions

- Whether a guide is authored under `guides/` and rendered into `.pi/agents/`, or authored there. The renderer emits one file today, so a second target is the cost of the first answer.
