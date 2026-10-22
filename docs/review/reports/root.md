> Bound to `9e9e0ea`. The quotations below are evidence at that revision, not current facts; `docs/review/cases.md` carries the current case list.

# Review — `agents/root.md` at 9e9e0ea

Artefact: `agents/root.md`, revision `9e9e0ea` (781 lines, 62,802 bytes, 341 rules plus 9 `depends on` lines), read as the consumer reads it.
Law read from `AGENTS.yaml` at the same revision; metric `docs/method/review.md`; contract `docs/review/contract.md`; lens `writing-for-agents/SKILL.md`.
Nothing below changes the artefact.

## Verdict

fail — six blocking findings, five of them an authority case the view leaves ambiguous.
Cases enumerated: 37, thirteen on the authority axis; **authority `ambiguous` = 6, `silent` = 0**.
Rendering checks all pass: `sh tools/check.sh` → `ok: 6 views, 27 sections, 396 nodes, 56 prohibitions, 34 banned words`; `ok: 6 role files`; `ok: identity, six fields, old names, command, wall-clock, byte limit`.
The view is complete and current; it is wrong where two rules fire on the same moment and disagree, and where a reference has no referent.

## Cases, in the order a root meets them

| # | the moment | axis | verdict | the sentence that settles it, or the missing one | what the root does instead when it is missing |
|---|---|---|---|---|---|
| 1 | session opens, or resumes after a kill | proceed | stated | `recovery` (464): resume from the current state, not from memory | — |
| 2 | an unread message is sitting in `inbox/` | proceed | stated | `inbox first` (270): read, land, delete, and only then go back | — |
| 3 | the person says go | proceed | stated | `go` (84): take the next workset by `take next` | — |
| 4 | killed after a take, reopened, the person says go again | proceed | **ambiguous** | `take next` (281) takes "every node whose dependencies are met" and never excludes a node already taken | re-dispatches a package that is still running: two writers on one area (421) and the spend twice |
| 5 | the person raises a project; what level is he talking at | proceed | **ambiguous** | `root depth` (61) says ask "the manager that owns it"; at that moment no manager owns it, and the rule names no other source | reconstructs the level from the code or the internal documents, which the same rule forbids, or guesses it for the first manager |
| 6 | how much the person wants to be involved | authority | stated | `three` (360): ask which of the three, inherit it down; bounded by `mixed attention` (372) | — |
| 7 | instruction is terse, heated or self-contradictory | proceed | stated | `vague instruction`: say the state read; `reconcile`: name the conflict, take the later one, mark it unconfirmed | — |
| 8 | the person asks to suspend a rule | authority | stated | `user rank scope`: he must name the rule and say the case is urgent, or nothing is suspended | — |
| 9 | a target is being aligned, or has just been agreed | proceed | stated | `reach agreement` (355), `agreement state` (585), `no agreement no work` (587) | — |
| 10 | the target is agreed and work must start | authority | **ambiguous** | `auto advance` (593) "needs no further word" against `milestone list` (548) "the milestone list is approved first" | dispatches before the ordered list is approved, or idles waiting for an approval the agreement already gave |
| 11 | the root splits the agreed target into milestones and packages | authority | **ambiguous** | `manager owns` (471) "you own … the splits" and `auto advance` against `sub owner` (75) "Split only under explicit permission"; the view never says who grants it or where it is recorded | splits without the person's word, or stalls the whole tree waiting for a permission nobody issues |
| 12 | manager or worker for this package | proceed | stated | `kind test` (51) | — |
| 13 | writing the contract | proceed | stated | `contract fields` (285), `contract identity`, `contract grant`, `pass boundary`, `budget caps`, `model cost`, `subagent scope` | — |
| 14 | is this piece worth splitting at all | proceed | stated | `self execute` (283): do it below about ten times the fixed cost of a dispatch | — |
| 15 | pricing what a package spends | proceed | stated | `classes` (193), `time`, `unknown class` (207), `class decides` (205) | — |
| 16 | a package wants a resource beyond the lent grant | authority | stated | `grant` (225): grant from what you were lent, exhaustion travels up; `queue`, `preempt`, `payer decides` (779) | — |
| 17 | launching children | proceed | stated | `async only`, `fresh context`, `child context`, `subagent scope`, `say that you started` | — |
| 18 | the person sends a message while children run | proceed | ambiguous | `interrupt` (719) "Dispatch nothing new" against `go` (84) "the packages leave before you read any project" | halts a workset he asked to leave, or dispatches while a message needed an answer |
| 19 | a child's result comes back | authority | **ambiguous** | `result first` (274) "Judge it or send it for review" against `manager does not judge` (312) "Do not judge it" and `own word does not count` (752) | passes its own child's work and moves on |
| 20 | a review verdict comes back fail | proceed | stated | `verdicts` (320), `route failure`, `every package` (322) | — |
| 21 | a milestone is reached | authority | stated | `milestone is a gate`, `ship at gate`, `vertical slice` (546) | — |
| 22 | a gate is reached and the person is away | authority | stated | `gates hold`, `lent scope`, `advance stops` | — |
| 23 | a question blocks advancement and he has not answered | authority | **ambiguous** | `wait for yes` (713) "you neither act nor invent work" against `block timeout` (589) "Cheap: decide now and record it as assumed" and `timeout clock` (591) "stop waiting, do what does not depend on the answer" | idles the tree on a cheap reversible question, or decides an irreversible one by reading `block timeout` broadly |
| 24 | a child has written nothing | proceed | stated | `stuck` (250): silence beyond the declared wall-clock; `stuck disposal`, `pause` | — |
| 25 | a child reports a cost, a resource or a taste need | authority | stated | `kinds` (98), `kind cost` (102), `kind direction`, `effort required` (110), `forward adds` | — |
| 26 | a question arrives from above the root or beyond its authority | proceed | stated | `parent only` (63), `nothing beyond` (473), `beyond authority` (116), `person may write anywhere` | — |
| 27 | judging a returned artefact | proceed | stated | `evidence at source`, `bind to revision`, `defect evidence` | — |
| 28 | several packages have passed | authority | ambiguous | `integration` (328) "Run the combined check yourself" against `own word does not count` (752) | signs off its own integration |
| 29 | an error appears, in its own work or in the tree | proceed | stated | `problem class` (396), `signal` (398), `intake`, `supersede` | — |
| 30 | the law itself is wrong | authority | **ambiguous** | `problem class` (396) "report to the law's owner"; the view names no owner — the only nearby referent is "the law worker" (414), in a rule about who reads what | edits `AGENTS.yaml` itself, which `one loop`, `ssot` and `supersede` all instruct it to do in place, or reports to itself |
| 31 | a fact must be written; a proposal is unanswered | proceed | ambiguous | `write through` (156) "marked provisional" against `proposal` (55) "`assent: assumed`" and `assent` (174), whose four levels do not include provisional | writes a level of `provisional` that no other rule reads, or writes `assumed` and drops provisional |
| 32 | about to push, rewrite history, or a credential appears | authority | stated | `pushes hereditary`, `high risk` (374), `secrets` (378), `untrack` | — |
| 33 | he asks how the root would do it | proceed | stated | `plan ownership`, `design options` | — |
| 34 | the root must ask him something | proceed | stated | `ask only consequential`, `unanswerable only`, `self contained`, `extraction` | — |
| 35 | reporting a result or a completion | proceed | stated | `report fields` (94), `completion` (96), `completion proof`, `result not inventory` (731) | — |
| 36 | the person says stop, or the session ends | proceed | stated | `wind down`; `context pressure` (the seven items before yielding); `safe point` | — |
| 37 | the project has no remote, or must be rebuildable | proceed | stated | `no remote`, `bootstrap`, `readme` | — |

## Blocking findings

**B1 — what the person must approve before dispatch is stated two ways.**
Location: `agents/root.md:548` (`milestone list`) and `agents/root.md:593` (`auto advance`).
Criterion: contract check 2 (conflict) and check 6 (a rule's how reaches its goal); metric: authority case may not be ambiguous.
Reproduction: `grep -n "no further word\|approved first" agents/root.md` → 548 says the strict ordered milestone list is approved first, 593 says a just-agreed target needs no further word. Both triggers are the same moment; neither rule is more specific, so `specific wins` cannot break the tie. `agreement state` (585) adds a third bound with a different object (write `aligning` or `agreed` beside the target).
Likely wrong action: dispatch on `auto advance` and never show the ordered list; or hold an agreed project waiting for an approval that `reach agreement` already got.
Missing sentence: which document the person approves — the agreed target, or the ordered milestone list derived from it.

**B2 — the root's authority to split its own layer is stated both ways.**
Location: `agents/root.md:471` (`manager owns`), `agents/root.md:593` (`auto advance`), `agents/root.md:75` (`sub owner`).
Criterion: contract check 2; metric: authority case may not be ambiguous.
Reproduction: `grep -n "the splits\|explicit permission" agents/root.md` → 471 "you own the roadmap, the splits …", 593 "advancement needs no further word", 75 "Split only under explicit permission and runtime bounds". `word from parent` makes the granter the person, but no rule says the permission exists, when it is granted, or where it is recorded, so one reading asks and the other splits.
Likely wrong action: a root that reads `manager owns` re-splits silently and never asks; a root that reads `sub owner` blocks every split on a permission it cannot see, which stops the tree.
Missing sentence: whether the root's own subtree split needs the person's word once the target is agreed, and if it does, where that grant is written.

**B3 — who judges a returned package result.**
Location: `agents/root.md:274` (`result first`) and `agents/root.md:312` (`manager does not judge`), `agents/root.md:752` (`own word does not count`).
Criterion: contract check 2; metric: authority case may not be ambiguous; the view's own `docs may not be wrong` / `own word does not count`.
Reproduction: `grep -n "Judge it or send it for review\|Do not judge it" agents/root.md` → 274 permits judging, 312 forbids it. Same trigger (a child or package result arrives), opposite acts, neither more specific.
Likely wrong action: the root reads `result first` as permission and closes its own child's package, so the only verdict in the tree is the producer's.
Missing sentence: the root acts on a verdict it did not write; "judge it" in 274 is struck or replaced by "send it for review".

**B4 — while the person is silent, wait or decide.**
Location: `agents/root.md:713` (`wait for yes`) against `agents/root.md:589` (`block timeout`) and `agents/root.md:591` (`timeout clock`).
Criterion: contract check 2, system check timeout; metric: authority case may not be ambiguous.
Reproduction: `grep -n "neither act nor invent work\|decide now and record it as assumed" agents/root.md` → 713 says no act and no invented work while he has not answered; 589 says a cheap blocking question is decided now and recorded as assumed, and 591 says the wait ends and independent work runs. All three fire when the person has not answered a question the root raised after agreement.
Likely wrong action: the root parks the project on a cheap reversible question, or it decides an irreversible one under 589 and reads 713 later, when the person objects.
Missing sentence: which rule owns the wait when the question is one the person was asked — the tier in 589, or the confirmation in 713.

**B5 — "the law's owner" has no referent in this view.**
Location: `agents/root.md:396` (`problem class`); the only nearby referent is `agents/root.md:414` (`scope composition`, "the law worker reads …").
Criterion: contract check 3 (stale/unresolvable reference), check 6, check 8 (SMART: the act is not actionable as written); metric: authority case may not be ambiguous.
Reproduction: `grep -n "law's owner\|law worker" agents/root.md` → two hits, neither saying the law worker owns the law. Nothing in the root view says the corpus is owned by another layer, so the report target cannot be resolved without guessing.
Likely wrong action: the root edits `AGENTS.yaml` itself and records it, which `ssot`, `one loop`, `supersede` and `kill` all tell it to do in place, so the corpus gets a second writer.
Missing sentence: the policy worker owns the corpus; a law change goes to it as a `contract` report.

**B6 — `take next` is not idempotent across a restart.**
Location: `agents/root.md:281` (and its copy at 86).
Criterion: contract system check idempotency ("kill at a stable point, reopen, say `go`; the roadmap state is the same, and no node becomes ready because the session restarted").
Reproduction: `grep -n "whose dependencies are met" agents/root.md` → 281. The predicate is "dependencies are met" and "taken" is only written down, never read. A node marked taken still has its dependencies met, so after a kill and `go` (84, "the roadmap already holds the state") it qualifies again. Negative control: a fixture roadmap where node P is marked taken with all dependencies met must not be returned by `take next`; today it is.
Likely wrong action: after every kill, a package is dispatched a second time, which breaks `one writer per area` (421) and spends the class twice.
Missing sentence: take every node whose dependencies are met and that is not marked taken.

## Non-blocking findings

**N1 — nine rule texts are rendered twice.**
Location: `10`/`571` (`chain`), `47`/`307` (`two kinds`), `86`/`281` (`take next`), `143`/`272` (`delete on read`), `213`/`771` (`units`), `276`/`320` (`verdicts`), `343`/`546` (`vertical slice`), `380`/`773` (`payers`), `382`/`781` (`price changes are edits`).
Criterion: contract check 1 (redundancy) and check 9 (the view states `inferable` — "The file carries no duplicate" — and carries nine).
Reproduction: extract every line matching `^\*\*` and `^  depends on`, group by body; nine bodies occur twice (`python3` scan of the file; 341 rule lines plus 9 dependency lines, 9 duplicated bodies).
Cause: `tools/law.py:render` adds a dependency beside its parent and the same node is rendered again in its own section. The dep copy is the useful one; the second is the copy `inferable` forbids.

**N2 — forwarding above the root is written three times.**
Location: `63` (`parent only`), `473` (`nothing beyond`), `116` (`beyond authority`).
Criterion: check 1; the writing lens ("synonyms that rename a single branch are one branch written twice").
Reproduction: read the three lines; each says the question goes to the layer that can answer it and the root does not answer. For a root the three have the same act; the only distinction is the wording of the trigger.

**N3 — the kind's goal is stated twice, thirty lines apart, and `worker` restates it.**
Location: `47` (`two kinds`, "the kind is set once and does not change"), `51` (`kind test`, "the kind is decided once and never changed"), `worker` ("reports once").
Criterion: check 1 and `atomic` (one subject, one rule).
Reproduction: `grep -n "set once and does not change\|decided once and never changed" agents/root.md` → 47 and 51. One rule's goal split across two siblings; the reader must hold both to have the subject.

**N4 — `scope composition` says the root reads "all but worker-only", which the corpus does not do.**
Location: `agents/root.md:414`; the fact in `tools/law.py:reads`.
Criterion: check 3 (a claim that no longer holds) and check 8.
Reproduction: 396 nodes, 55 unread by the root, of which 24 are not worker-scoped (`('policy',)`, `('researcher',)`, `('reviewer',)`, and mixed sets). The rule's sentence is true of nothing in the corpus; the honest form is "any rule scoped to the root or to a manager".

**N5 — `root depth` cannot be executed at the moment it fires.**
Location: `agents/root.md:61`.
Criterion: check 6, and the SOP test (no next step, no completion criterion).
Reproduction: read line 61. The trigger is the person raising a project; the how is "ask the manager that owns it what the level is". At that moment the root has not dispatched a manager, and the view nowhere says to dispatch one first or to ask the person instead. "The level" is undefined, so no completion criterion. Likely wrong action is the one the same rule forbids: reconstruct the level from the code.

**N6 — the timeout is named but never set.**
Location: `agents/root.md:591` ("When the wait passes its threshold"), `agents/root.md:589` ("wait for the next natural stop").
Criterion: contract system check timeout ("every discussed block has an absolute deadline; only the no-discussion case waits forever").
Reproduction: `grep -n "threshold" agents/root.md` → one hit, and no rule sets it; `natural stop` is likewise undated. Two waits are declared unlimited — `no agreement no work` (587, declared) and `wait for yes` (713, undeclared); the contract allows only the empty case to wait forever.

**N7 — two labels for one record state.**
Location: `156` (`write through`, "marked provisional"), `55` (`proposal`, "`assent: assumed`"), `174` (`assent`, four levels).
Criterion: check 2 (a record field cannot hold both) and `ssot` (one home for the label).
Reproduction: `grep -n "marked provisional\|assent: assumed" agents/root.md` → the same unanswered proposal is written as `provisional` in one rule and `assumed` in another; `assent` enumerates stated/agreed/tolerated/assumed, so `provisional` is a value no other rule reads.

**N8 — no balance in the view carries its goal, and the ends never reach the reader.**
Location: all 31 balance rules as rendered, e.g. `laws.ssot` at line 8, `speech.go` at 84, `docs_shape.block_timeout` at 589.
Criterion: contract expectation check ("every rule names its goal … a balance carries the goal") and the balance test.
Reproduction: 31 rules with `_kind: balance` are visible to the root; 0 carry `_goal` in `AGENTS.yaml`, and `tools/law.py:rule_text` renders the band and the pull only, so the two ends, their costs and their payers never appear. Example: `ssot` at line 8 gives band and pull; the ends (`person_time: the reader pays one lookup`, paid by self; `trust: the copy drifts`, paid by the person) are in the source and not in the view, so `payer decides` (779) cannot be applied to the rule it was written for. The design is a balance; the artefact cannot be used as one.

**N9 — `go` and `interrupt` claim the same message.**
Location: `84`, `719`.
Criterion: check 2.
Reproduction: `grep -n "Dispatch nothing new\|packages leave before" agents/root.md` → 84 dispatches, 719 dispatches nothing; both trigger on a message from the person. `go` is the narrower trigger, so `specific wins` resolves it, but 719 names no exception and a root reading it will stop the workset.

**N10 — the integrated outcome has two judges.**
Location: `328` (`integration`, "Run the combined check yourself"), `752` (`own word does not count`).
Criterion: check 2, borderline.
Reproduction: read the two lines. Where the combined check is a command the verdict is the program's and the lines agree; where the integration needs judgement (the interfaces between packages) the root is both producer and approver. `milestone experience` covers the milestone-level answer, so the exposure is the package-set that is not a milestone.

**N11 — `split follows logic` is a tautology that another rule already carries.**
Location: `agents/root.md:758`; the actionable form is `logical level` at `agents/root.md:299`.
Criterion: check 5 (no-op) and check 8 (`logic` is undefined; the goal restates the trigger).
Reproduction: 758 reads "you split something → the split follows logic.": no act, no observation, no criterion. 299 states the same goal with a how ("Split on a key every fact has exactly one value of"). Delete 758 and the behaviour is unchanged.

**N12 — the declared spend is never compared with the actual.**
Location: `193` (`classes`), `731` (`result not inventory`).
Criterion: contract system check efficiency ("the declared wall-clock against the actual").
Reproduction: `classes` requires a class in the contract and `result not inventory` requires "what it cost" in an upward report; no rule reads the reported cost against the declared class, so a class never calibrates and the efficiency check has nothing to compare. `bounded calibration` calibrates a workload, not a price.

## System checks

- **Idempotency — fail.** See B6: `take next` (281) reads dependencies only; a taken node re-qualifies after a restart. `go` (84), `recovery` (464) and `safe point` all assume the roadmap holds the taken state, and 281 never reads it.
- **Timeout — fail.** `timeout clock` (591) names a threshold no rule sets; `block timeout` (589) names a "natural stop" no rule dates. Two waits are unlimited: 587 (declared) and 713 (undeclared). Gates wait by design (`gates hold`), which the contract permits only for the empty case.
- **Efficiency — partial.** Declared spend is present (class plus wall-clock in `contract fields`; `stuck` 250 compares declared silence), actual spend is carried upward (`result not inventory` 731) but never compared; no exploration outside the contract was found in the view. Context read: 62,802 bytes, 781 lines, 341 rules plus 9 dependency lines, 56 prohibition sentences against a ceiling of 62, always loaded. The nine duplicated bodies in N1 are the measurable waste inside that budget.
- **Expectation — fail for balances.** Every act rule carries a goal and a how (the renderer refuses otherwise); 31 of 31 balances carry neither goal nor ends (N8).

## The other tests

- **Balance test.** The design passes: 31 balances visible to the root, each with exactly two ends, each end carrying a cost and a payer from the four, plus a band and a pull in `AGENTS.yaml` (measured; `law.py --check` also validates the payer). The artefact fails it: band and pull only, no ends, no costs, no payers, no goal (N8). Where the pull is the only guide, a reader cannot tell whose cost the band protects.
- **SOP test.** Passes for 33 of 37 cases: the trigger, the act in order and a checkable completion are present. Fails at 61 (`root depth`: no next step, "the level" is not checkable), 396 (`problem class`: the completion is a report to a person who is not named), 548 against 593 (the order of approval is contested), and 713 (`wait for yes`: no completion, no deadline).
- **The nine content checks.** 1 redundancy: N1, N2, N3. 2 conflict: B1–B4, N7, N9, N10. 3 stale: N4, and B5 as an unresolvable reference. 4 completeness: no case in the 37 is without a rule; the failures are disagreements, not absences. 5 no-op: N11, and the duplicate goal in N3. 6 logical self-consistency: B2, B6, N5. 7 omission: none found at case level; what is missing is a named granter of split permission (B2) and a named owner of the law (B5), both omissions inside an existing rule rather than an absent class. 8 SMART: 61, 396, 591, 758. 9 self-consistency: the view fails its own `inferable` (nine duplicates, N1) and its own `ssot` for the record label (N7).
- **Writing lens.** Leading words are doing their work (`band`, `pull`, `gate`, `workset`, `trace`, `one home`, `take next`); progressive disclosure is not available to a system prompt, so the cure for the 62.8 KB is deletion, and N1, N2, N3, N11 name it. 56 prohibition sentences: the lens asks for the positive target beside a prohibition; most here already carry one.

## What is unresolved

Nothing is blocked: every claim above carries a command that reproduces it.
Next action, for the corpus owner: decide B1–B5 as one change each (one sentence added, one struck), then B6's clause, then N1's renderer fix (`tools/law.py:render` should mark a node drawn when it is rendered as a dependency and skip it in its own section), then N8's `_goal` on the 31 balances.
This report is complete; no finding waits on a missing input.

## Observed, not scored

`agents/root.md` has no frontmatter, unlike the other five role files (`tools/build.py:build`, `head = fm(role) if role != "root" else ""`). If the root file is ever loaded the way the manager and worker files are, it carries no `name`, `tools` or `systemPromptMode: replace`; today no rule states how the root file is loaded, so there is no criterion to violate.
