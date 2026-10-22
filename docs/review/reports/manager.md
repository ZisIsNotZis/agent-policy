> Bound to `9e9e0ea`. The quotations below are evidence at that revision, not current facts; `docs/review/cases.md` carries the current case list.

# Review: the manager view

Artefact: `agents/manager.md` (the render of `AGENTS.yaml` for role `manager`: 696 lines, 293 rules).
Revision: `9e9e0ea6776625c51081ca47451f1f63ac859cda` (HEAD). Worktree clean apart from two untracked sibling reports, which I did not open or touch.
Law `AGENTS.yaml`, criteria `docs/review/contract.md`, metric `/home/z/vibe/docs/method/review.md`, lens `/home/z/.agents/skills/writing-for-agents/SKILL.md`.
The view is a render: every repair named below lands in `AGENTS.yaml` and is re-rendered, never in `agents/manager.md` (`render is written not read`, line 571).
Location, criterion and reproduction are observations. Every "wrong action" is inference by construction - the metric asks for the likely action, not for a sighting.

## What ran

- `./tools/check.sh` -> exit 0: `ok: 6 views, 27 sections, 396 nodes, 56 prohibitions, 34 banned words`; `ok: 6 role files`; `ok: identity, six fields, old names, command, wall-clock, byte limit`.
- `python3 tools/law.py --render manager` diffed against `agents/manager.md` -> body identical; only the 11-line frontmatter differs, and `build.py` adds that.
- Scope completeness: the 293 rules the manager scope resolves to are exactly the 293 rendered rows - 0 missing, 0 extra. Nothing the manager should read is absent, nothing outside its scope leaked in.
- Reference resolution: every backticked and snake_case token resolves inside the view (`docs/`, `inbox/`, `aligning`, `agreed`, `1_snake_case`, 4 payers, 7 units). No stale reference of that kind.
- RDI case (`docs/review/rdi_case.md`): its fix is carried by `falsifiable` (29, "a step that did not run did not pass") and `bind to revision` (341). Present.
- No repair made, nothing committed, no command of my own invented as an acceptance.

## Cases, in the order a manager meets them

| # | case | axis | verdict | settling sentence, or the missing one | likely wrong action when missing |
|---|---|---|---|---|---|
| 1 | a message waits in `inbox/` | proceed | stated | `inbox first` (279) + `delete on read` (152) | none |
| 2 | session resumes mid-package | proceed | stated | `recovery` (459), `resume` (554), `commits` (420) | none |
| 3 | the person says "go" | proceed | stated | `go` (93) | none |
| 4 | a target with no agreement | authority | stated | `no agreement no work` (536), `reach agreement` (364), `agreement state` (534) | none |
| 5 | who may call the target agreed | authority | stated | `reach agreement` (364): "it is agreed when they can restate it without contradicting you" | none |
| 6 | start executing: the milestone list | authority | **ambiguous** | missing: the approver. `milestone list` (497) says "approved first" and names nobody; `auto advance` (542) says "advancement needs no further word"; `go` (93) says "without interpreting the word" | asks the person to approve every list, the attention `go` exists to spare, or starts and finds the list was never approved |
| 7 | split this piece or do it myself | proceed | stated | `self execute` (292), `work package` (499) | none |
| 8 | how to grade the split | proceed | delegated | `coverage first` (302), `sub owner` (84), `logical level` (308) | none |
| 9 | write the child's contract | proceed | stated | `contract fields` (294) + `contract identity` (296) + `contract grant` (298) + `pass boundary` (300) + `budget caps` (267) + `child context` (314) | the six-line test is not the whole test (F5) |
| 10 | launch and return | proceed | stated | `async only` (243), `say that you started` (135), `no watching` (257) | none |
| 11 | kill after launch, restart, "go" again | proceed | **silent** | missing: the taken marker written before the launch (F3). `take next` (290) writes it after; `intent before act` (451) covers only minutes-long steps | a second child on the same package; two writers on one area (416) |
| 12 | steer a running package | proceed | stated | `steer` (271), `pause` (277) | widening is outside the list at 271 (F15) |
| 13 | child silent past its declared wall-clock | proceed | stated | `stuck` (259), `stuck disposal` (261), `no watching` (257) | none |
| 14 | send at half and at three quarters | proceed | **ambiguous** | `deadline` (275) with no way to be awake at those moments; the only wakes are a child's completion (243) and a person's message (133, 148) (F16) | no deadline instruction is sent at all, or the manager polls, against 257 |
| 15 | a child's result comes back: who judges | authority | **ambiguous** | conflicting: `result first` (283) "Judge it or send it for review" against `manager does not judge` (321) "Do not judge it" (F1) | the manager approves its own child's work |
| 16 | dispatch the review | proceed | stated | `manager does not judge` (321), `fresh` (323), `judgement only` (325), `reviewer contract` (327), `every package` (331) | none |
| 17 | the review passes | proceed | stated | `integration` (337), `integrator` (422) | none |
| 18 | the review fails | proceed | stated | `route failure` (306), `always a path` (269), `budget caps` (267), `change hypothesis` (265) | none |
| 19 | the review is blocked | proceed | **silent** | `verdicts` (329) defines `blocked`; no rule states the manager's act on it - `route failure` (306) covers "a package fails" (F14) | treats blocked as fail and re-splits, spending a package on a missing fact |
| 20 | two packages touch one area | proceed | stated | `one writer per area` (416), `worktree` (418), `integrator` (422), `preserve` (440) | none |
| 21 | milestone reached: who says it is the thing wanted | authority | stated | `milestone experience` (333), `milestone is a gate` (350), `three kinds of review` (345) | none |
| 22 | gate reached, the person is away | authority | stated | `gates hold` (358), `ship at gate` (356), `timeout clock` (540) | none |
| 23 | a question blocks advancement, agreement exists | proceed | stated | `block timeout` (538) + `timeout clock` (540); neither names an absolute deadline (F4) | none |
| 24 | a question blocks advancement, no agreement yet | proceed | **ambiguous** | `no agreement no work` (536) "this wait has no timeout" against `timeout clock` (540) "the wait is finite" (F4) | idles the project indefinitely, or abandons alignment and starts work that is thrown away |
| 25 | the parent orders something the manager believes is wrong | authority | stated | `no blind agreement` (99), `parent contract` (485), `problem class` (391) | none |
| 26 | a question above the parent | authority | stated | `nothing beyond` (468), `parent only` (72), `person may write anywhere` (131) | none |
| 27 | the person asks for taste the manager cannot answer | proceed | stated | `kind direction` (113), `forward never refused` (123), `ask the owner` (133) | none |
| 28 | report upward at a milestone | proceed | stated | `report fields` (103), `completion proof` (513), `milestone is a gate` (350), `result not inventory` (650) | none |
| 29 | the package cannot be done: who moves the goal | authority | **ambiguous** | `always a path` (269): "the goal moves only by a decision that names its cost" names no decider; `no blind agreement` (99) says "change the end if you may" and gives no test for "may" | silently drops the person's stated acceptance once the path gets expensive |
| 30 | the grant runs out | authority | stated | `advance stops` (362), `grant` (234), `kind resource` (109) | none |
| 31 | something irreversible, or a live credential | authority | stated | `high risk` (369), `secrets` (373), `covered once` (379), `gates hold` (358) | none |
| 32 | the person asks to suspend a rule | authority | stated | `user rank scope` (481) | none |
| 33 | stop or hand control back | proceed | stated | `safe point` (449), `wind down` (453), `context pressure` (635) | none |
| 34 | the parent's contract is missing a field | authority | stated | `kind contract` (115), `unreadable contract` (117) | none |

Authority cases: 4, 5, 6, 15, 21, 22, 25, 26, 29, 30, 31, 32, 34 = **13**.
Proceed cases: **21**.

## The count of authority cases ambiguous or silent

**3 of 13** are ambiguous: case 6 (the milestone list's approver), case 15 (who judges a child's result), case 29 (who may move the goal). **0 silent.**
The metric allows neither ambiguous nor silent for an authority case, so these three are defects of the artefact, not preferences of mine.

Proceed cases: 1 silent (case 11), 3 ambiguous (14, 19, 24).

## Findings

### Blocking

**F1 - two rules give different answers on who renders a child's verdict.**
Location: `agents/manager.md:283` (`result first`, `AGENTS.yaml` scheduling.result_first) against `agents/manager.md:321` (`manager does not judge`, review.manager_does_not_judge).
Criterion: contract check 2 (conflict); the metric's rule that authority may not be ambiguous; check 6 (the two hows cannot reach one goal).
Reproduction: `grep -n "Judge it or send it for review\|Do not judge it" agents/manager.md` -> one hit each. The first offers judging as an option; the second forbids it. `specific wins` (39) does resolve it in favour of 321, but only after the reader notices the two bear on one act - and 283 offers the shortcut 38 lines earlier.
Blocking because the wrong reading is self-approval, the act `own word does not count` (669) and the RDI case exist to prevent, and nothing downstream can see it happened.
Second conflict on the same axis, same finding: 283 says act on the returned result "before you take the next package", while `take next` (290) says take every node whose dependencies are met. A manager holding three ready nodes reads 290 and defers the returned result.

**F2 - the milestone list must be "approved", and no rule names the approver.**
Location: `agents/manager.md:497` (`milestone list`, delivery.milestone_list) against `agents/manager.md:542` (`auto advance`, docs_shape.auto_advance) and `agents/manager.md:93` (`go`, speech.go).
Criterion: metric, authority case 6; check 6 (the how, "write a strict ordered one", never reaches the goal "approved first"); check 8 (SMART: "approved" names no agent).
Reproduction: `grep -n "milestone list is approved\|needs no further word\|without interpreting the word" agents/manager.md` -> 497, 542, 93. `own word does not count` (669) rules out the manager approving its own list, which leaves the person and the parent, whose prices differ: the person's attention against one more hop. The list is not one of the three gate kinds (350), so `gates hold` (358) does not settle it either.
Blocking because it is an authority case with two readings that spend different payers: a sub-manager reading it as "the person approves" spends the attention `go` exists to protect, and one reading it as "my parent approves" skips the synchronisation point the rule exists for.

**F3 - the taken marker is ordered after the launch, so a kill re-dispatches.**
Location: `agents/manager.md:290` (`take next`, dispatch.take_next), with `agents/manager.md:243` (`async only`) and `agents/manager.md:451` (`intent before act`).
Criterion: contract system check, Idempotency ("kill at a stable point, reopen, say `go`; the roadmap state is the same, and no node becomes ready because the session restarted"); check 4.
Reproduction: the how at 290 reads "Walk in order, take every node whose dependencies are met, write down that it is taken" - the write is the last clause, after the taking. `async only` (243) launches at the take. `intent before act` (451) writes state first only for "a step that takes minutes", and a dispatch does not. Kill between the launch and the marker write, reopen, say `go`: 290 finds the dependencies met, sees no taken marker, and launches a second child on the same paths, against `one writer per area` (416). No rule orders the marker before the launch and none records a launched child: `grep -in "launch record\|record the launch" agents/manager.md` -> 0 hits; `grep -in "in flight" agents/manager.md` -> 1 hit, at 430, about an untracked change, not a child.
Blocking because the failure is silent, costs a duplicate package and two writers on one area, and no rule in the view corrects it.
Not exercised: no harness here to kill a session at that boundary, so the reproduction is described, not run. Confidence high on the order in the text; medium on whether the runtime re-enters `take next` on `go`.

### Non-blocking

**F4 - the blocking wait has no absolute deadline, and two rules disagree on whether it ends.**
Location: `agents/manager.md:536` (`no agreement no work`) against `agents/manager.md:540` (`timeout clock`); `agents/manager.md:538` (`block timeout`).
Criterion: contract system check, Timeout ("every discussed block has an absolute deadline; only the no-discussion (empty) case waits forever"); check 2; check 8.
Reproduction: 536 ends "Do only that; this wait has no timeout"; 540's goal is "The wait is finite" and its how fires "When the wait passes its threshold", a threshold never named; 538 adds a third unnamed scale, "the next natural stop". The aligning case is a discussion, so the empty-case exemption does not reach it (inference).
Non-blocking: 540 is present and `specific wins` (39) points at 536 for the state test, not for the duration.

**F5 - "Six lines ... with one missing, do not dispatch" declares complete a contract that four other rules call incomplete.**
Location: `agents/manager.md:294` (`contract fields`) against `296` (`contract identity`), `267` (`budget caps`), `637` (`subagent scope`), `639` (`model cost`), `60` (`worker`), `327` (`reviewer contract`).
Criterion: check 2; check 6 (the six-line test cannot reach its goal, "do not dispatch an incomplete contract").
Reproduction: write a contract with exactly the six named lines and nothing else, then apply 267 (attempts, review rounds, no-progress rounds), 637 (tools and limits), 639 (model and thinking), 296 (kind, name, whose roadmap). All four fail while the contract passes the only test that says "do not dispatch". `worker` (60) and `reviewer contract` (327) each add a further mandatory line.
Non-blocking: every field rule is in the view; the repair is to make "six" a floor.

**F6 - nine rules are rendered twice, verbatim, and the copy can read first.**
Location: the dep line against the rule's own row, for `chain` 21/520, `take next` 95/290, `units` 222/686, `delete on read` 281/152, `verdicts` 285/329, `two kinds` 316/58, `vertical slice` 352/495, `payers` 375/688, `price changes are edits` 377/696.
Criterion: check 1 (redundancy inside the view); check 9 (the view breaks `ssot`, 19, which says "The copy is found first and used" - for `verdicts` the copy at 285 is read before the row at 329).
Reproduction: `python3` over `agents/manager.md`, matching `^\*\*(.+?)\.\*\* (.+)$` and `^  depends on \*\*(.+?)\*\*: (.+)$` and grouping by sentence -> 9 sentences, 2 occurrences each. Mechanism: `tools/law.py:resolve()` - `drawn` stops a dependency repeating as another dependency, not as its own row.
Non-blocking: same words, no behaviour changes until an edit lands on one copy.

**F7 - one decision, two homes: `queue` and `queue behind`.**
Location: `agents/manager.md:236` (`queue`, spend.queue) and `agents/manager.md:596` (`queue behind`, resources.queue_behind).
Criterion: check 1; check 9 (`ssot`, 19).
Reproduction: both open "a scarce resource is held" and both say "Record the queued request and its trigger"; 236 adds "the holding carries holder, device and return time", 596 adds "does not hold indefinitely". Neither contains the other, so a manager who reads one keeps an incomplete record.
Non-blocking: the union is cheap and both are in one view.

**F8 - `steerable` and `no long in turn` are one rule, and only one carries the naming state.**
Location: `agents/manager.md:247` against `agents/manager.md:249`.
Criterion: check 1.
Reproduction: 247 "Give it a timeout or detach it behind a named log; write the naming state first"; 249 "Keep it out of the turn: give it a timeout, or detach it behind a named log". Same act, same cost; a manager who triggers on "takes minutes" (249) never writes the naming state, the part that makes a detach recoverable.
Non-blocking: 247 states the full act, two lines away.

**F9 - two more double homes: `preserve`/`preserve work` and `split follows logic`/`logical level`.**
Location: `agents/manager.md:440` against `442`; `agents/manager.md:675` (principles) against `agents/manager.md:308` (dispatch).
Criterion: check 1; check 5 for 675, which adds no act to 308.
Reproduction: 440 "Do not cover it with a forced reset or checkout", 442 "Work around it, never discard it" - one end in two statements. 308 is the whole rule ("Split on a key every fact has exactly one value of"); 675 is its first clause.
Non-blocking: identical behaviour, so the cost is context, not correctness.

**F10 - `scratch retired` refers to a path that exists nowhere in the corpus.**
Location: `agents/manager.md:197` (`scratch retired`, records.scratch_retired).
Criterion: check 3 (stale); check 5 (no-op).
Reproduction: `grep -rn "scratch" --include=*.md --include=*.yaml --include=*.py --include=*.sh . | grep -v "^./agents/"` -> 3 hits, all lines of the node itself (`AGENTS.yaml:1495`, `1498`, `1499`). No `.scratch` exists, and the second clause ("move leftovers out under migrate_on_touch") describes leftovers the corpus no longer has.
Non-blocking, and the clearest delete in the view: it costs every manager every turn and changes no act.

**F11 - four decision rules are typed as acts, so the balance test is never applied to them.**
Location: `agents/manager.md:261` (`stuck disposal`), `292` (`self execute`), `238` (`price clock`), `312` (`fresh context`).
Criterion: the balance test (two ends with a cost and a payer; the band; the pull) applied to every decision rule.
Reproduction: `_kind` for the four is `act` and `_ends` is empty (script over `AGENTS.yaml`: `stuck_disposal ends=0`, `self_execute ends=0`, `price_clock ends=0`, `fresh_context ends=0`). 261 reads "Cancel when the loss is smaller" with no unit for "loss" and no payer; 292 reads "worth less than about ten times the fixed cost of a dispatch" with no payer. `tools/law.py --check` demands `_ends`/`_pull` only when `_kind == "balance"`, so these pass the check by construction.
Non-blocking: the comparison stays actionable and `order` (690) supplies the direction.

**F12 - 31 balances carry no goal: the Expectation check fails 31/31.**
Location: every balance in the view; the ones whose purpose is least visible are `verdicts` (329), `contract fields` (294), `gates hold` (358), `signal` (393), `result not inventory` (650).
Criterion: contract system check, Expectation ("every rule names its goal ... a balance carries the goal").
Reproduction: script over `AGENTS.yaml` for nodes whose scope contains `manager` and `_kind == "balance"` -> 31 nodes, `_goal` present in 0. `rule_text()` prepends a goal only when `_goal` exists, so each renders as "when -> band. pull." with no statement of what it is for.
Non-blocking: the band usually implies the end; the cost is that `double check` (631) cannot compare the how against a stated goal.

**F13 - rules that state a value and no act.**
Location: `agents/manager.md:354` (`few milestones`), `590` (`efficiency`), `655` (`attention is a budget`), `663` (`depth over breadth`), `671` (`time is the scarce thing`).
Criterion: check 5 (no-op test); check 8 (SMART); the SOP test (no next act, no completion criterion).
Reproduction: delete each and re-read the view; no step changes. 354 ("fewer is better, until nobody judges the direction") gives no act and no bound on "nobody judges"; 590, 655, 663 and 671 are values already enforced by 292, `order` (690) and the Gates section.
Non-blocking, and the second-cheapest cut after F10: they spend the attention the live rules need.

**F14 - a `blocked` verdict has no stated manager act.**
Location: `agents/manager.md:329` (`verdicts`, also reached at 285) against `agents/manager.md:306` (`route failure`).
Criterion: check 4 (completeness); the SOP test.
Reproduction: `grep -n "blocked" agents/manager.md` -> 285 and 329 only, both defining the verdict. 306's trigger is "a package fails", and blocked is not a fail but "what is missing". Pass and fail each have an act; blocked has none.
Non-blocking: `always a path` (269) and `ask only consequential` (101) leave the manager somewhere to go.

**F15 - widening a dispatched child's boundary is outside every list.**
Location: `agents/manager.md:271` (`steer`: "a correction, a narrowing, a missing fact") against `300` (`pass boundary`), `637` (`subagent scope`), `294` (`contract fields`), `277` (`pause`).
Criterion: check 4; check 2 (two readings, different actions).
Reproduction: `grep -in "widen\|extend" agents/manager.md` -> 0 hits. The steer list names narrowing; the boundary is fixed at dispatch by 300 and 637; `pause` (277) produces a new contract but never says a boundary may change. Two readings: widen in place at 271, or stop and re-dispatch at 277.
Non-blocking: the package still runs; only the evidence trail differs, since the review's `rev` (327, 341) would bind to a contract that no longer exists.

**F16 - the deadline instruction has no way to be issued on time.**
Location: `agents/manager.md:275` (`deadline`: "Send an instruction at half and at three quarters") against `243` (`async only`), `257` (`no watching`), `253` (`no sleep`).
Criterion: the SOP test (a how with no mechanism); check 6.
Reproduction: `grep -in "wake\|timer" agents/manager.md` -> `timer` 0 hits; the wakes are a child's completion (243), a person's message (133, 148) and "your next roadmap read" (257). Nothing puts the manager awake at half a package's wall-clock; `no watching` stops it checking, `async only` stops it holding the turn, `no sleep` stops the block.
Non-blocking only because `steer` (271) still reaches a running child whenever the manager next wakes.

**F17 - context load: 53,898 characters, about 13.5k tokens, loaded every turn.**
Location: the file as a whole.
Criterion: the writing lens (sprawl; context load is spent every turn); contract system check, Efficiency.
Reproduction: `wc -c agents/manager.md` -> 53,898, 696 lines, 293 rules. The 30 lines named in F6-F9 and F13 measure 4,553 characters, about 1,138 tokens - of which the nine duplicate copies are about 393 tokens. Deleting those is a 2% cut that removes nothing live; the ladder (disclosure behind a pointer) is the larger cut and is a design question for the law's owner.
Non-blocking: an observation about the whole, not a defect in one rule.

## Unresolved and next

F1, F2 and F3 are the three I would not accept the artefact with. F1 and F3 are one-node edits in `scheduling`/`dispatch`. F2 needs an answer I may not give - person or parent approves the milestone list - and if the answer is the person's, it belongs in a `direction` report, not an edit.
Not exercised: the runtime kill behind F3 (no harness here), the spend paths (`vram` 220, `price clock` 238, `idle`/`metered`/`exclusive`/`unrecoverable` 206-212) which a manager of another project meets and this one does not, and `recursion depth` (80), a claim about a runtime I cannot see.
