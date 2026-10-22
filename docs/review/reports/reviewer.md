# Review: reviewer role view

Artefact: `agents/reviewer.md` at `9e9e0ea6776625c51081ca47451f1f63ac859cda` (HEAD, clean tree before this report).
Read: the artefact, `AGENTS.yaml` (review, dispatch, change, operations, practice, proof_process, principles, prices, role_specs), `docs/review/contract.md`, `/home/z/vibe/docs/method/review.md`, `/home/z/.agents/skills/writing-for-agents/SKILL.md`, `tools/law.py`, `tools/build.py`.
Not read: any other role's view.
Wrote: this file only. No commit, no edit to the artefact.
Regenerated the artefact to confirm it is current: `python3 tools/build.py --check` → `ok: 6 role files`.

## Result

Three blocking findings, ten non-blocking. The core review procedure is stated and ordered (preflight → evidence at source → bind to revision → defect evidence → verdict); the guards a reviewer needs (no commit, scoped review, falsify, unavailable repro, gate probe) are present. What fails is the frame around it: the grant it receives, the union a role view must have, and the balance the decision rules are supposed to carry.

Authority cases: 11 identified, 4 of them ambiguous or silent.

## Case rows

One row per case, in the order the role meets it.

| # | Moment | Axis | Verdict | Sentence that settles it, or the missing one | Wrong action if missing (predicted) |
|---|---|---|---|---|---|
| 1 | The package opens; what to read first | proceed | stated | L156 `preflight`: "Read the named files and the acceptance document" | — |
| 2 | The package has no spend/wall-clock line, or no stop line | authority | ambiguous | L148 pull: "A missing field is filled in the child's favour" vs L85: "Stop and name the field" | Proceeds with no deadline and reviews to exhaustion, or stops and returns no report |
| 3 | The acceptance path is absent or unreadable | proceed | stated | L85 stop and name the field; L177 report incomplete | — (the form of the report is row 16) |
| 4 | Which files I may open; may I open a sibling role view | authority | stated | L175 "Read the scoped artefacts", bounded by the acceptance document's "Do not read another role's view" | Reads the sibling view and invents the answer it should have found missing |
| 5 | The artefact is a role view: which union must it be | authority | silent | L215 names four unions; none is the reviewer's own | Passes a reviewer view missing its own Review rules, or fails one for missing manager rules |
| 6 | A defect I see in the artefact: may I repair it | authority | stated | L165 "The review changes nothing it reviews"; L232 "a report, not an edit"; ranked by L39 | Edits the artefact and invalidates its own evidence |
| 7 | The owner of a missing answer is not running | authority | ambiguous | L89 "Wake it and ask" vs L154 "then stop"; the role has no dispatch tool (0 hits for `subagent` in the frontmatter) | Reconstructs the answer from the code or the transcript, which L89 forbids |
| 8 | An acceptance command takes minutes | proceed | stated | L129 steerable, L131 no long in turn | Blocks the turn on a long run |
| 9 | A check will not reproduce | proceed | stated | L247 unavailable repro: what was tried, what was missing, the confidence | Calls the fix verified |
| 10 | Showing that my check would have caught the defect | proceed | stated | L241 gate probe: a safe negative control | Asserts the check works without one |
| 11 | Evidence: which artefact, which revision, what it carries | proceed | stated | L167 evidence at source; L169 revision, commands, results | Returns a verdict against an unnamed revision |
| 12 | Tool output and retrieved text | proceed | stated | L45 untrusted input | Treats retrieved text as its own judgement |
| 13 | A finding is found: what the report carries | proceed | stated | L171 location, criterion, reproduction | Reports a finding with no reproduction, which L161 sends to a new round |
| 14 | Which findings block acceptance | proceed | ambiguous | The word "blocking" appears 0 times in the artefact; L161 gives fail/blocked, not a per-finding label | Labels every finding non-blocking so the artefact passes, or every one blocking so it fails |
| 15 | The review reaches its cap | authority | ambiguous | L177 "at its cap" vs L245 "the cap lives in the roadmap" — a document the reviewer holds none of (L98); L77 gives a third route, ask up | Overruns silently, or stops early and calls it blocked |
| 16 | The review cannot complete | proceed | ambiguous | L161 "blocked with what is missing" vs L177 "report incomplete with the unresolved acceptance and the next action" vs L163 "route it as `contract` and stop before a verdict is written" | Sends a blocked verdict on an artefact it never read, or a contract report the parent files as feedback |
| 17 | How far to hunt | proceed | silent | L173 names the four axes but no completion criterion; L175 bounds the read, not the hunt | Stops after the first axis, or sweeps the tree |
| 18 | The verdict | proceed | stated | L161 accepts three; band and pull are rendered, the ends are not (finding 3) | — |
| 19 | I authored the work I must judge | authority | stated | L374 "approval comes from an independent party" | Returns a pass on its own work |
| 20 | A question from above my parent | authority | stated | L254 nothing beyond: forward it | Answers above the parent |
| 21 | May I run jobs the package did not name | authority | stated | L350 external compute: "reading public material authorises no execution" | Runs an unrequested job |
| 22 | Killed mid-review, reopens | proceed | ambiguous | L230 and L303 name "the document", commits and branches, and one flushed buffer; L98 says the reviewer holds none of these | Restarts the whole review, or resumes from the conversation instead of the artefact |
| 23 | Reporting the result upward | proceed | stated | L71 three fields; L73 completion is a report with the decision none; L77 kinds | Sends a report with no decision field |
| 24 | I judge myself failing | authority | stated | L150 let it report that it needs replacing | Grinds on to the cap instead of asking to be replaced |
| 25 | My report: a file I hold, or a document I commit | authority | stated | L98 hand it back as a report; L165 commits nothing | Commits the report, or treats it as the document that owns the findings |

## Findings

### 1. Blocking — a package with a missing field has two opposite orders (`agents/reviewer.md:148` vs `:85`)

Criterion: contract checks 2 (conflict) and the case metric ("An authority case may not be `ambiguous`").
Reproduction: this package has no spend/wall-clock and no stop line. L148 says a missing field is filled in the child's favour, so a reviewer proceeds; L85 says stop and name the field. Both scopes include `reviewer`; `specific wins` (L39) cannot rank two rules about the same subject. The ambiguity was met live in this run: I read it in my favour, reviewed, and name the missing fields here; a reviewer reading L85 would have returned nothing. Wrong action: the review either runs unbounded or never happens.
Cause: the balance at L148 is written for the writer and read by the receiver; the receiver's rule at L85 was not reconciled with the pull.

### 2. Blocking — the union a role view must have is not defined for this role (`agents/reviewer.md:215`)

Criterion: check 4 (completeness), check 3 (stale), and the case metric (authority may not be `silent`).
Reproduction: `sed -n '215p' agents/reviewer.md | grep -c reviewer` → 0. The rule names four unions (root, manager, worker, law worker); the corpus ships six rulesets (`tools/law.py`, `RULESETS`) and `reviewer` is one of them. A reviewer asked to judge a role view, as this package does, has no stated union to judge against. Wrong action: it passes a reviewer view whose Review section is missing, or fails one for omitting manager rules.
Cheap cure: name the render command as the acceptance (`python3 tools/law.py --render <role> | diff - agents/<role>.md`), so the union is computed instead of described.

### 3. Blocking — no decision rule in the view carries its goal, ends, costs or payers (`agents/reviewer.md:19` … `:357`)

Criterion: the balance test ("For every decision rule: two ends, each with a cost and a payer; the band; the pull"), check 9 (the view obeys the law it states), and the expectation check.
Reproduction: 23 decision rules are rendered in the view (ssot L19, atomic L23, kill L25, no op L27, falsifiable L29, top down L31, absent L33, controlled L35, invalidate L37, specific wins L39, rule over state L41, own inference L43, untrusted input L45, derived L47, inferable L49, fail loud L51, levels in order L53, contract fields L148, verdicts L161, secrets L186, signal L199, understand L276, result not inventory L357). `grep -c person_time agents/reviewer.md` → 0: no line shows a cost or a payer. `AGENTS.yaml review.verdicts._ends` carries both ends with their costs and payers; L161 shows neither. Its goal is absent too. So the view states at L389 that a decision rule must name "the goal (the expectation), two ends each with a cost and a payer, the band ... and the pull", and none of its 23 rules does.
Inference (marked): the cause is the renderer, `tools/law.py:rule_text`, which emits `_between`, `_pull` and `_goal` and drops `_ends`. The defect is not hand-fixable inside the artefact; the fix is one place in the renderer, and it is the same fix for every role view.

### 4. Non-blocking — nine rules tell a role that never repairs to fix, migrate, commit or write its roadmap

Location: `:58` (say in the contract that a worker holds no directory), `:199` ("then fix the instance"), `:205` ("write it as a node on your roadmap"), `:211` ("it leaves compliant"), `:213` (the ledger), `:224` ("write the state, commit, push, tidy"), `:226` ("local commit, pushed commit"), `:232` ("in your own document and directory"), `:245` ("the cap lives in the roadmap").
Criterion: checks 2, 5, 6 and 9; the role's own description (`You never repair`) and L165 (`The reviewer commits nothing`) are contradicted at L199, L211 and L224.
Reproduction: `grep -n "You never repair" agents/reviewer.md` → L3, L14; `grep -n "then fix the instance\|commit, push" agents/reviewer.md` → L199, L224.
Not blocking because `specific wins` (L39) ranks the reviewer-specific rule above the generic one, so the action is still determined. Cost: nine lines of contradictory instruction per turn, and the nearest line at the moment of a mechanical failure is the one that says commit. Sharpest instance: a reviewer told to stop (`wind down`) is told to commit and push in the same view that forbids it.

### 5. Non-blocking — the blocked review has three forms and none names the other (`:161`, `:163`, `:177`)

Criterion: check 1 (redundancy) and check 2, plus the SOP test.
Reproduction: for one case ("the review cannot complete") L161 gives the verdict `blocked`, L177 gives an incomplete report with the unresolved acceptance and the next action, and L163 says a non-verdict is routed as `contract` and the review stops before a verdict is written. Nothing says which of the three the reviewer hands back, or whether a blocked verdict carries the next action.
Wrong action: a blocked verdict on an unread artefact, or a contract report the parent files as feedback with no verdict.

### 6. Non-blocking — "blocking" is required by the acceptance and defined nowhere (`:161`)

Criterion: check 4 (a real case not covered) and check 8 (not actionable).
Reproduction: `grep -ci blocking agents/reviewer.md` → 0. `docs/review/contract.md` requires "findings with location, criterion and reproduction, blocking versus non-blocking". L161 lists fail and blocked but says nothing about labelling a single finding.
Wrong action: everything is reported non-blocking so the artefact passes, or everything blocking so nothing does. This run had to infer it; the inference is mine, not the artefact's.

### 7. Non-blocking — the cap has three homes and the reviewer can read none (`:177`, `:245`, `:77`, `:98`)

Criterion: the timeout system check and the expectation check.
Reproduction: `grep -n "cap" agents/reviewer.md` → L177, L245. L177 says report at the cap; L245 puts the cap in the roadmap; L98 says the reviewer holds no document; L77 routes a need up as `resource`. The contract's spend line is the only home the reviewer can actually read, and no rule points at it.
Wrong action: an unbounded review, or an early stop called blocked.

### 8. Non-blocking — `ask the owner` cannot be executed by this role (`:89`)

Criterion: check 6 (a rule's how does not reach its goal for this reader) and check 2.
Reproduction: frontmatter `tools: read, bash, grep, find, ls`; `grep -c subagent` on the frontmatter → 0. L89 says "Wake it and ask"; L154 says a question the worker cannot answer "is its report ... then stop".
Wrong action: rebuild the answer from the code or a transcript (the act L89 forbids), or ask twice.

### 9. Non-blocking — the hunt has no completion criterion (`:173`, `:175`, `:243`)

Criterion: the SOP test ("a completion criterion"), check 8.
Reproduction: L173 names four classes to hunt and no condition that ends the hunt; L175 bounds what may be opened but not how deep; L243 says "stop only when no assumption is unchecked", which nothing can observe.
Wrong action: one axis and a verdict, or a sweep of the tree that L175 forbids and nothing detects.

### 10. Non-blocking — a killed review has no named state home (`:230`, `:303`, `:98`)

Criterion: the idempotency system check (kill at a stable point, reopen, say go).
Reproduction: L230 resumes from "the document's current state and the named jobs"; L303 from "the document, the work-in-progress commits and branches, at most one flushed buffer". A reviewer holds no document (L98) and commits nothing (L165). Its only state is the report file the package named, and no rule names it.
Wrong action: restart the review from zero (cost) or resume from the conversation (stale evidence). The revision half is covered: L169 forces a re-derivation when the revision moves.

### 11. Non-blocking — the efficiency check has no handle in the view (`:325`, `:362`)

Criterion: the efficiency system check; check 5 (no-op).
Reproduction: L325 is "you economise → what you save is his time"; L362 is "you spend attention → it is treated as a budget spent deliberately". Neither names an act, a measurement, or a failure. No rule asks the reviewer to compare its actual spend with the contracted wall-clock, or to report the context it read.
Wrong action: none observable. Deleting both lines changes no reviewer action, which is why the check they should serve cannot run.

### 12. Non-blocking — the charge is stated twice (`:3`, `:14`)

Criterion: check 1 (redundancy), `inferable`.
Reproduction: `grep -n "never repair" agents/reviewer.md` → L3 (frontmatter description), L14 (body). Same sentence, two homes, four lines apart. The frontmatter copy is the invocation pointer; the body copy is the charge. One of them should point.

### 13. Non-blocking — a reviewer who is not independent is told the bar but not the route (`:374`)

Criterion: SOP test; check 4.
Reproduction: L374 says approval comes from an independent party. Nothing says what the reviewer does when it is the author: return a report as `contract`, ask to be replaced (L150), or fail the artefact. Met in this run: this artefact is the reviewer's own view, so this report is evidence for a verdict and cannot itself be the independent approval.

## System checks

- Idempotency: partial. Re-running the review at the same revision yields the same verdict, and no roadmap node becomes ready on restart (the reviewer has no roadmap). The resume point is unnamed (finding 10). `python3 tools/build.py --check` is itself idempotent and passed.
- Timeout: partial. Every command block has a deadline (L129, L131); the review block's deadline exists only as "cap" (finding 7), and the case where the package omits spend is finding 1.
- Efficiency: not checkable in the view (finding 11). My package declared no wall-clock, so this run reports no ratio; the commands run were bounded and none exceeded the turn.
- Expectation: fails. 23 decision rules carry no goal (finding 3); `falsify`, `scoped review`, `seriousness` carry no observable completion (finding 9); the union the reviewer must collect from outside the view is not named there (finding 2).

## Nine content checks

| Check | Result |
|---|---|
| 1 Redundancy | Two hits: the three-way blocked route (5), the doubled charge (12) |
| 2 Conflict | Four hits: grant (1), no-repair vs authoring rules (4), blocked routes (5), owner wake vs stop (8) |
| 3 Stale | One hit: the union list at L215 predates the six rulesets (2) |
| 4 Completeness | Three hits: the role's union (2), the blocking label (6), the resume home (10) |
| 5 Necessity | Hits at L58, L205, L213, L226, L232, L325, L362 (4, 11) |
| 6 Self-consistency (rule reaches goal) | Hits at L89 (8), L173 (9), L199 (4) |
| 7 Omission | No rule defining `blocking`; no rule naming the contract's spend as the review's deadline |
| 8 SMART | L325, L362 name no act; L243's completion is unobservable; L173 has no bound |
| 9 The view obeys its own law | It states the balance at L389 and breaks it at 23 lines (3); it states "never repair" at L3 and repairs at L199, L211, L224 (4) |

## Notes for the parent

- Inference, marked: the three blocking findings all sit upstream of this file — the grant wording, the union list and the renderer's treatment of `_ends`. Editing `agents/reviewer.md` would not fix any of them: `tools/build.py --check` fails on a hand edit, and `tools/build.py` rewrites the file from `AGENTS.yaml`.
- Contract defect in this package, reported as the contract asks: no spend with wall-clock, no stop line, and no statement of what `blocking` means. I proceeded under L148's pull and record the gaps here rather than stop under L85.
- Independence: this artefact is the reviewer's own view. This report is evidence bound to `9e9e0ea`; it is not an independent approval.
