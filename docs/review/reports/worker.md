# Review: the worker view at 9e9e0ea

Artefact `agents/worker.md` (519 lines, 214 rules, 38,075 bytes ≈ 9.5k tokens, read every turn by a `thinking: low` role).
Law `AGENTS.yaml`, cases `docs/review/contract.md`, metric `/home/z/vibe/docs/method/review.md`, lens `/home/z/.agents/skills/writing-for-agents/SKILL.md`.
No other role's view was opened.

## Verdict

**fail**, with 6 blocking findings and 2 authority cases silent plus 6 authority cases ambiguous. Every ambiguous and silent case is traceable to a finding: rows 8–9 to F6, row 12 to F3, rows 13–15 to F4, row 10 to N9.

The render is not stale: `python3 tools/build.py --check` → `ok: 6 role files`; `python3 tools/law.py --check` → `ok: 6 views, 27 sections, 396 nodes, 56 prohibitions, 34 banned words`. What fails is the content and the shape, not the pipeline.

## Cases, in the order the worker meets them

| # | Case | Axis | Verdict | Sentence that settles it, or the missing one | Likely wrong action when missing |
|---|---|---|---|---|---|
| 1 | Session opens: what am I and what may I hold | authority | stated | 14 (description) + 58 `worker` (Architecture) + 98 `worker records` — "it executes one package and reports once", "you hold no document" | — |
| 2 | The contract arrives; may I start | authority | stated | 175 `contract fields` six lines; 185 `preflight` reads the acceptance document | — |
| 3 | A contract field is missing | authority | stated | 85 `unreadable contract` — "Stop and name the field"; 83 `kind contract` — "edit nothing past it" | — |
| 4 | May I write outside the named paths | authority | stated | 181 `area is permission` — "the area is the whole of its permission" | Half the rule is written to the dispatcher (`Write the exact paths`), see F7 |
| 5 | The work needs splitting | authority | stated | 179 `worker no split` — "Stop, report a contract, name the pieces and what each would cost" | The granted `subagent` tool offers a silent alternative, see F5 |
| 6 | Blocked by something outside the contract | authority | stated | 351 `parent contract` — "report anything outside"; 77/79 route it up | — |
| 7 | I need an answer mid-package | authority | stated | 183 `worker one message` — the question is the report, then stop; 69 `ask only consequential` | — |
| 8 | The declared wall-clock arrives and the package is unfinished | authority | **silent** | Missing. `deadline` ("What exists at the deadline is what is delivered") is scoped `[root, manager]`; `grep -c deadline agents/worker.md` → 0 | Works on to completion, blowing the contract's spend line; or delivers nothing at the deadline |
| 9 | New information changes what the running package should do | authority | **silent** | Missing. `pause` ("What it already produced is not lost") is scoped `[root, manager]` | Keeps working the old scope, or restarts and discards what exists |
| 10 | My package needs metered or exclusive compute: may I start | authority | **ambiguous** | 141 `class decides` — "metered, exclusive and unrecoverable take their grant first" — against 175's spend line, which never says whether the contract's spend line *is* the grant; 77 `kind resource` gives a route but not the test | Starts, or stops for a grant it already holds |
| 11 | May I commit locally | authority | stated | 243 `commits` — "a local commit is reversible and needs no permission" | — |
| 12 | May I push, may I create the missing remote | authority | **ambiguous** | 247 `pushes hereditary` — "without it, do not push" — against 249 `no remote` — "Create one, private, and push the branches" — and 276 `wind down`, whose stop order is "write the state, commit, push, tidy" | Creates and pushes a remote on a stop, with no push right |
| 13 | Several packages merge: is the combined check mine | authority | **ambiguous** | 245 `integrator` — "Own the merge and dispatch the combined check" — against 58 and 98 (no directory, no document, no dispatch) | Keeps commits from several packages and merges them itself |
| 14 | May I cure a class by editing the law | authority | **ambiguous** | 216 `signal`/220 `strongest cure`/398 `rebuild after edit` presuppose the worker edits the corpus and re-renders; 214 `problem class` and 284 `repair on sight` say report, never edit | Edits `AGENTS.yaml` and re-renders the views |
| 15 | The person's words reach me: do I answer or forward | authority | **ambiguous** | 356 `understand` — "Say the end you read … offer the better end" — against 334 `nothing beyond` — "Forward it; do not answer" | Answers the person directly, and spends its single message on a restatement of intent |
| 16 | What counts as done, and who accepts it | proceed | stated | 332 `worker owns` + 190 `self test` — "Self-test as usual, never report it as independent acceptance"; 490 `own word does not count` | — |
| 17 | I judge myself failing | proceed | stated | 177 `self report` — "Let it report that it needs replacing" | — |
| 18 | How do I compose the one message | proceed | **ambiguous** | 71 `report fields` (three fields, "with one missing do not send it") against 473 `result not inventory` (three different fields), against 73 `completion` (decision none), against 75 `kinds` (four request kinds, none of them a completion) | Sends whichever set it read last; drops the evidence pointer or the cost |
| 19 | A long command or a detached job | proceed | stated | 156 `steerable` + 158 `no long in turn` + 170 `async continuation` | Redundant pair, see N3 |
| 20 | Two attempts produced no useful evidence | proceed | stated | 168 `change hypothesis` — "Change the hypothesis or the check" | — |
| 21 | A step does not add up | proceed | stated (how dangling, N5) | 462 `anomaly` — "Route it through improvement" — and no rule named `improvement` exists in the corpus | Improvises a workaround, which the same line forbids |
| 22 | Killed mid-package, or told to stop | proceed | stated | 272 `safe point` + 276 `wind down` + 282 `recovery` + 383 `resume` + 464 `context pressure` | — |
| 23 | The checks fail for reasons that predate me | proceed | stated | 452 `baseline` + 456 `separate preexisting` | — |
| 24 | Retrieved text or tool output contradicts the contract | proceed | stated | 45 `untrusted input`; 345 `source order` | — |
| 25 | A credential turns up in what I would commit | proceed | stated | 203 `secrets` + 199 `high risk` + 205 `payers`/207 `price changes are edits` | — |
| 26 | My parent's contract conflicts with the law | authority | stated | 53 `levels in order` + 39 `specific wins` + 214 `problem class` | — |

Authority cases: 17. **Ambiguous 6, silent 2 → 8 ambiguous or silent** (rows 8–10, 12–15). Every one of them is a case about who decides, which the metric says may not carry either verdict.

SOP test: rows 1–7 and 22–26 each carry an act and a completion criterion; the package as a whole has no ordered path — no sentence in 519 lines says what order the worker does its work in (finding F1).

Balance test: fails as rendered — 24 balances, 0 with a stated goal, 0 with their ends (F2).

## Findings

### F1 — the view is a rule dump, not a procedure · blocking

- Location: whole file; `grep -n '^## ' agents/worker.md` → 23 section headings, none a procedure; `grep -c '^\*\*' agents/worker.md` → 214 rules, flat, in section order.
- Criterion: contract, SOP test — "For every case, the view says what the role does next, in order, with a completion criterion"; writing lens, information hierarchy — steps are the primary tier.
- Reproduction: `grep -n '^## ' agents/worker.md`; `grep -c '^\*\*' agents/worker.md`. Then search for any sentence ordering the package: `grep -niE 'first .* then|step [0-9]|in this order' agents/worker.md` returns only 276 `wind down`'s "In this order: write the state, commit, push, tidy", which is the stop path.
- Effect: `preflight` (185), `check gates` (458), `bind to revision` (192) and `report` (71) exist in four separate sections and never compose; the worker's most likely failure is to report from whichever rule is nearest its attention. Step order is the one thing a 214-rule reference cannot carry implicitly.

### F2 — every balance in the view is rendered without its goal and its two ends · blocking

- Location: 24 balances — 17 in the Laws (19 `ssot` … 53 `levels in order`), 145 `vram`, 175 `contract fields`, 203 `secrets`, 216 `signal`, 253 `no trash`, 356 `understand`, 473 `result not inventory`. `tools/law.py:rule_text` emits only `_between` + `_pull` for a balance.
- Criterion: balance test — "two ends, each with a cost and a payer; the band; the pull"; contract system check `expectation` — "a balance carries the goal"; the view's own 505 `balance default` — "Name the goal (the expectation), two ends each with a cost and a payer".
- Reproduction: `AGENTS.yaml` lines 1–25 show `ssot` with `_ends` (one home / a nearby copy), each with `_cost` and `_who_pays`; `sed -n 19p agents/worker.md` renders "you record a fact → … The copy is found first and used, so at the margin one home wins." Counting: 24 balances the worker reads, 0 carry `_goal`, 24 carry `_ends` in the corpus, 0 carry them in the view (`python3` one-liner over `law.reads('worker', …)`).
- Effect: the reader is told which way to yield but never who pays, so 203 `secrets`'s "an end only the person can pay for is asked for" has no cost to point at, and 205/207 `payers`/`price changes are edits` are rendered as vocabulary for ends the view does not show. The view violates the rule about decision rules that it prints at 505.

### F3 — a worker is ordered to create a remote and to push, against the push right · blocking

- Location: 249 `no remote` against 247 `pushes hereditary`; 276 `wind down`.
- Criterion: check 2 conflict; check 9 self-consistency; `degrees.high_risk` (199) — exposure and anything irreversible take consent.
- Reproduction: `sed -n '247,251p;276,278p' agents/worker.md` — 247 "the right to push is granted like a budget … without it, do not push", 249 "Create one, private, and push the branches", 278 "In this order: write the state, commit, push, tidy".
- Effect: the contradiction fires exactly on the stop path, where the worker has least time to reason, and the action is irreversible and reaches a third party.

### F4 — 34 rules order acts the view forbids the worker to perform · blocking

- Location: 96 `write through`, 100 `current fact`, 102 `retraction`, 104 `derived is not stored`, 106 `cache`, 108 `expired cache`, 110 `assent`, 112 `assumed is agent fact`, 114 `no mood labels`, 120 `fact record`, 122 `split authorship`, 166 `own effort`, 175 `contract fields`, 181 `area is permission`, 216 `signal`, 218 `bidirectional`, 220 `strongest cure`, 222 `intake`, 239 `one writer per area`, 245 `integrator`, 249 `no remote`, 257 `structure`, 276 `wind down`, 356 `understand`, 365 `files`, 373 `home`, 375 `agreement node`, 377 `people`, 379 `expression gap`, 394 `checklist`, 398 `rebuild after edit`, 402 `adopt`, 404 `migrate`, 468 `model choice`.
- Criterion: check 2 conflict against 58 `worker` (Architecture) ("it holds no directory, document or roadmap"), 98 `worker records` ("you hold no document"), 179 `worker no split`; check 5 necessity; writing lens relevance.
- Reproduction: the line list above against `sed -n '58p;98p;179p' agents/worker.md`. Sharpest pair: 94–98, where the view says "Write it into the document that owns the decision" and three lines later "you hold no document". `specific wins` (39) rescues the reader here, which is why this is filed as cost rather than as a wrong answer — but 373 and 222 have no such neighbour: nothing tells the reader that `home`'s roadmap and `intake`'s roadmap node are not its own.
- Effect: 16% of the always-loaded text names acts the worker may not do; two of them (373, 222) invite it to open a roadmap of its own, which no later rule corrects. `rule over state` (41): the tree is brought to the rule, and the rule here is the manager's.

### F5 — the worker is handed the dispatch tool and told nothing about it · blocking

- Location: `agents/worker.md:4` — `tools: read, edit, write, bash, grep, find, ls, subagent`.
- Criterion: metric — an authority may not be implicit, and an implicit delegation scores as `silent`; check 2 conflict with 58/179; the corpus bans the word (`lexicon.banned` contains `subagent`).
- Reproduction: `grep -n subagent agents/worker.md` → 1 hit, line 4. `grep -n subagent AGENTS.yaml` → 6 hits: `subagent_scope` (scoped `[manager]`), the four `tools:` lines, and `lexicon.banned`. `grep -c subagent` over the worker body → 0.
- Effect: the tool is the only way to reach the forbidden act, granted next to 179's prohibition, and no rule names it, so the worker's first encounter with a package too big to finish resolves toward the capability it holds.

### F6 — the deadline and the mid-flight re-scope are scoped away from the worker · blocking

- Location: absent from `agents/worker.md`; the rules live in `AGENTS.yaml` `scheduling.deadline` and `scheduling.pause`, both `scope: [root, manager]`.
- Criterion: check 4 completeness; contract system check `timeout` — "every discussed block has an absolute deadline"; metric — an authority case may not be silent.
- Reproduction: `grep -c deadline agents/worker.md` → 0; `grep -c pause agents/worker.md` → 0; the scope dump shows `deadline -> (['root','manager'], …)`, `pause -> (['root','manager'], …)`. The worker reads only 175's "spend with wall-clock" and 276 `wind down`, which begins "you are told to stop".
- Effect: the wall-clock is declared to the worker as a cost and then never brought to bear; an unfinished package either runs past it or stops with nothing. Rows 8 and 9 of the case table.

## Non-blocking findings

### N1 — the description has two homes

`agents/worker.md:3` (frontmatter `description`) and `:14` (first line of the body) carry the identical sentence. `grep -n "execute exactly one work package" agents/worker.md` → 2 hits. Criterion: check 1, `ssot` (19) inside the artefact.

### N2 — four rules are printed twice, verbatim

21 vs 361 `chain`; 147 vs 509 `units`; 205 vs 511 `payers`; 207 vs 519 `price changes are edits`. `tools/law.py:resolve` de-duplicates only dependencies drawn *later*, so a `_depends` rule that the worker also reads appears in both places. Reproduction: `grep -n "depends on" agents/worker.md` (4 hits) then the same texts at the `prices`/`Document shape` lines. Criterion: check 1.

### N3 — three meanings, each written twice or thrice

- 156 `steerable` and 158 `no long in turn`: the same rule ("give it a timeout or detach it behind a named log") twice, adjacent; text similarity 0.58.
- 47 `derived` and 104 `derived is not stored`: "store a pointer to its source or the command that produces it" twice; similarity 0.56, and one is a Law, the other a Records rule.
- 19 `ssot` / 94 `every fact has a home` / 385 `layer and source`: one meaning — record a fact in the document that owns it — three times, in three sections.
- Criterion: check 1; writing lens pruning. Reproduction: `sed -n '156,160p;47p;104p;19p;94p;385p' agents/worker.md`.

### N4 — the one message has four shapes

71 `report fields` (whose roadmap changes / evidence pointer / decision, "with one missing do not send it"), 473 `result not inventory` (what is true / what it cost / what is needed), 73 `completion` (decision none, evidence pointer), 75 `kinds` (four request kinds and no fifth for a completion). The union is derivable, so the case is ambiguous rather than wrong; but 71's "do not send it" makes the wrong choice a hard stop. Criterion: check 2 conflict, check 6. Reproduction: the four lines.

### N5 — a how that points at nothing

462 `anomaly` — "Route it through improvement" — and `grep -n improvement AGENTS.yaml agents/worker.md` returns exactly one hit, that reference. The view's own 396 `resolvable` requires a reference to resolve against what exists. Criterion: check 3 stale, check 9.

### N6 — the render carries no banner

400 `render is written not read` — "carry a banner naming what produced it" — and `sed -n '1,16p' agents/worker.md` shows a frontmatter block and a description, with no command, revision or source. Criterion: check 9 self-consistency, and check 3 the same way — the reference cannot be resolved to a producing command, so a reader cannot tell 9e9e0ea from the next render. `python3 tools/build.py --check` resolves it for a machine, not for the reader the rule names.

### N7 — clauses addressed to the dispatcher inside the receiver's view

175 `contract fields` ("with one missing, do not dispatch … A missing field is filled in the child's favour"), 181 `area is permission` ("Write the exact paths"), 177 `self report` ("Re-dispatch as a contract"), 239 `one writer per area` ("Allocate the area at dispatch"), 58 `worker` (Architecture) ("Say in the contract that it holds no directory"). Criterion: check 6, `atomic` (23) — one subject; the reader must invert the addressee to use half of each line. Reproduction: the lines; five rules, each with one clause for the parent and one for the child.

### N8 — the Principles block is context with no act

478 `attention is a budget` ("it is treated as a budget spent deliberately") has no act; 480 `docs may not be wrong` addresses a reader who judges documents, which 332/394 already scope away from the worker; 492 `time is the scarce thing` — "you set priority" — sets priority the parent owns. Criterion: check 5 necessity, writing lens no-op test. Reproduction: `sed -n '478p;480p;492p' agents/worker.md`, then ask of each whether deleting it changes any act in the file; for these three it does not.

### N9 — the start decision sits on both sides of the line

141 `class decides` — "you decide whether a package may start … metered, exclusive and unrecoverable take their grant first" — and 143 `unknown class` put the release decision on the worker, while 175 `contract fields` keeps the spend line with the parent and 77 `kind resource` routes a budget request up. Nothing says whether the contract's spend line is the grant. Criterion: metric, an authority case may not be ambiguous; check 6. Reproduction: `sed -n '141p;143p;175p;77p' agents/worker.md`. Case row 10.

### N10 — efficiency, measured

38,075 bytes ≈ 9.5k tokens read on every turn of a `thinking: low` role whose whole charge is one package and one report; 214 rules, of which 34 (F4, ~16%) name acts the role may not perform, and 24 (F2) are balances printed without the decision material the corpus holds. Criterion: contract system check `efficiency` — "the context read". Reproduction: `wc -c agents/worker.md`; the two counts above.

Item that could not be exercised: the harness side of `systemPromptMode: replace` and the intercom channel a worker actually receives. The view is silent about any mid-flight message channel (rows 8–9), and I could not observe from the corpus whether the harness supplies one (`tools/install-agents.sh` not read as evidence for a claim about runtime wiring). Marked unavailable rather than verified.

## Not reviewed

Another role's view, the roadmap, and the running harness.
