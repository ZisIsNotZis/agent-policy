# Review — `agents/policy_worker.md`

Revision: `9e9e0ea6776625c51081ca47451f1f63ac859cda` (`git rev-parse HEAD`).
Scope: `agents/policy_worker.md` read against `AGENTS.yaml`, `docs/review/contract.md`, `/home/z/vibe/docs/method/review.md` and the writing lens; `tools/`, `README.md` and `docs/roadmap/policy.md` read only as evidence of what the view points at.
No other role view was opened, and the two existing files in `docs/review/reports/` were not read.

## Evidence bound to the revision

```
python3 tools/law.py --check   -> ok: 6 views, 27 sections, 396 nodes, 56 prohibitions, 34 banned words (exit 0)
python3 tools/build.py --check -> ok: 6 role files (exit 0)
python3 tools/contract.py --self-test -> ok: identity, six fields, old names, command, wall-clock, byte limit (exit 0)
grep -c "AGENTS.yaml\|tools/\|generated" agents/*.md -> 0 in all six
```

So the artefact is a faithful render at this revision: no staleness finding, and every finding below is a defect of the corpus as this role reads it, not drift.

## Cases, in the order a session meets them

| # | Moment | Axis | Verdict | Sentence that settles it, or the one missing | Likely wrong action when it is missing |
|---|---|---|---|---|---|
| 1 | Session opens: which files do I read first (preflight) | proceed | silent | `preflight` says "Read the named files"; the view names none. `AGENTS.yaml`, `tools/`, `build.py`, `check.sh` each return 0 hits | Sweeps the tree, against `layout first` (703); or treats the file it was handed, `agents/policy_worker.md`, as the source |
| 2 | May I write this path | authority | delegated | `area is permission` (316) bounds it to the contract; `parent contract` (558) binds it | Writes `docs/roadmap/` or another layer's file because a law change "touches" it |
| 3 | The contract I received is missing a field | proceed | stated | `unreadable contract` (119): name the field, stop, the edit waits | Guesses the field (`own inference`) and edits anyway |
| 4 | A message is waiting in `inbox/` | proceed | stated | `inbox first` (283) outranks what I was about to start | Starts the law edit and reads the message later |
| 5 | Where does the fact from that message (or from my own finding) land | authority | ambiguous | `delete on read` (154) "the fact into the document" against `worker records` (175) "you hold no document. Hand the answer back as a report" | Reports it and lets the manager file it, so a law fact ends in another layer's document; or writes a document it does not own |
| 6 | Which file carries the law: source or render | proceed | silent | `doc first` (453) says "Edit the source, never the render"; nothing in the view identifies the source, and the render carries no banner (688 requires one) | Edits `agents/policy_worker.md`, the file it was given, which the law forbids |
| 7 | A defect in the law itself is reported, or a review finds one | authority | ambiguous | `problem class` (443) "report to the law's owner" and `double check` (748) "report it to the rule's owner" are this role; `intake` (451) says "write it as a node on your roadmap"; `worker records` (175) says it has none | Fixes the instance and drops the class node, so the signal has no home and recurs; or creates a roadmap it does not hold |
| 8 | Regenerate the views | proceed | silent | `rebuild after edit` (686) says the render regenerates "in the same act"; no command, no path, no target file | Hand-edits the six renders, or believes the edit is done once `AGENTS.yaml` is saved |
| 9 | Run the checks; which are "every applicable one" | proceed | silent | `rebuild after edit` (686) "Run every applicable one"; `coverage check` (469) "three things are checked by machine"; `check gates` (746) "the project's checks ... have run". None is named | Runs one check (`law.py`) and skips `build.py`, which is exactly the drift the repository ships a check for; or calls `git status` a check |
| 10 | A check fails and it also failed before my edit | proceed | stated | `baseline` (740) and `separate preexisting` (744) | Reports a pre-existing failure as its own, or fixes it inside a law package |
| 11 | The rule and the tree disagree | proceed | stated | `rule over state` (41) | Bends the rule to keep the tree |
| 12 | May I read a role file as input, since `review axes` tells me to review one | authority | ambiguous | `review axes` (361) "you review a corpus, a role file or a change" against `render is written not read` (688) "nobody treats it as input. Never hand-edit or read it back" | Reads the render and "fixes" it; or refuses the review and reports it blocked |
| 13 | Who approves my law change, and may I launch the reviewer myself | authority | ambiguous | `own word does not count` (818), `manager does not judge` (335), `every package` (345), `reviewer contract` (341) and the `subagent` tool grant say launch a reviewer; `worker records` (175), `worker owns` (537) and `two kinds` (58) say report once and hold nothing; `kind test` (62) never decides this role; `self test` is absent from the view (worker-only) | Self-approves a law every other role then reads; or spends a grant it does not hold (`contract grant`: "it gets a share of yours") |
| 14 | Write the reviewer's contract | proceed | ambiguous | `contract fields` (298) "Six lines ... with one missing, do not dispatch" against `reviewer contract` (341) "Write nine: rev, accept, change, ran, judge, blocking, budget, escalate, repair", plus `model cost` (756) and `subagent scope` (754) | Writes six and drops `judge`/`escalate`/`repair`, so the verdict it gets back is not the shape `verdicts` accepts; or writes nine and drops `goal`/`scope`, which `contract fields` refuses |
| 15 | Is this law change an interface change needing consent | authority | ambiguous | `high risk` (405) asks before "interface changes"; `commits` (484) says a local commit is reversible and needs no permission; no rule says which law edits are interface changes | Narrows its own `scope:` list or deletes a rule without asking; or asks its parent before every one-line edit |
| 16 | Kill an old name, retire a rule | proceed | stated | `kill` (25), `amend by replacement` (457), `dead code` (696), `coverage check` (469) | Annotates the old rule instead of deleting it |
| 17 | Commit the step | proceed | stated | `commits` (484): commit, a local commit needs no permission | Batches a whole section so a kill loses the step |
| 18 | Push | authority | stated | `pushes hereditary` (488): the root holds it; a package that must push says so in its contract | Pushes a law change no one granted, or pushes published history |
| 19 | Told to stop, or the wall-clock runs out mid-migration | proceed | stated | `wind down` (517), `safe point` (513), `intent before act` (515) settle the order; the "write the state" home is finding B | Leaves the corpus edited and the renders stale |
| 20 | Report back | proceed | stated | `report fields` (105), `completion` | Sends a status update with no evidence pointer |
| 21 | A person writes to me directly | authority | stated | `person may write anywhere` (133): forward upward unchanged, do not answer, wake the owner | Answers a question above its parent |

## Findings

### Blocking

**A. The role's three core acts carry a goal and no how: the source, the render and the check are named nowhere.**
Location: `rebuild after edit` (686), `coverage check` (469), `doc first` (453), `review axes` (361).
Criterion: SOP test (a goal without a how is not an SOP); content checks 8 (SMART/actionable) and 9 (the view obeys the law it states — `concrete` at 430 demands "the file, the command, the number, the commit", `how not what` at 438 demands "Write the file, the command, the check, in order").
Reproduction: `grep -c "AGENTS.yaml\|tools/\|build.py\|check.sh\|python3" agents/policy_worker.md` → 0, 0, 0, 0, 0. The charge itself is in the frontmatter ("you edit the corpus, re-render the views, and run the checks") and no rule in the body names one corpus file or one command for it.
Consequence: cases 1, 6, 8, 9 are silent. The likeliest wrong action is the one the law forbids: the role holds the complete law text in `agents/policy_worker.md` and edits it, because that is the only law file it can see.

**B. A role that "holds no document" is given eight rules that require a document, a directory or a roadmap.**
Location: `worker records` (175) against `entrance` (169), `entrance for next session` (171), `missing entrance` (173), `home` (649), `intake` (451), `context pressure` (752), `go` (95), `take next` (294).
Criterion: content checks 2 (conflict) and 6 (logical self-consistency: parent and child relations hold); system check idempotency (kill, reopen, `go`: the state is the same — with no document the "taken" set and the seven items of `context pressure` have no home, so a restart cannot reproduce the state).
Reproduction: `grep -n "your document\|your roadmap\|your directory" agents/policy_worker.md` → 169, 451, 535, 649, all manager-scoped and drawn into this view by the composition, against 175 which says the reader holds none.
Consequence: cases 5, 7, 19. A fact this role discovers has no declared home, and after a kill the seven recovery items are written "before yielding" into nothing.

**C. The authority to dispatch is granted and withheld in the same view.**
Location: `manager does not judge` (335), `every package` (345), `reviewer contract` (341), `subagent scope` (754), `model cost` (756), frontmatter `tools: ... subagent` — against `worker records` (175), `worker owns` (537), `two kinds` (58); `kind test` (62), which is the rule that would decide the kind, is drawn in but answers "manager or worker" only for a role that holds several independent things, and never names this one. `self test` (the worker-rules-only self-check) is absent from the view.
Criterion: content checks 2 and 6; the case metric's rule that an authority case may not be ambiguous.
Reproduction: `python3 tools/law.py --render policy_worker | grep -c "manager does not judge"` → 1 while `grep -c "^\*\*self test" agents/policy_worker.md` → 0; `README.md` states the opposite of the tool grant: "The last four are flavours of a worker ... none of them dispatches".
Consequence: case 13. Either the role approves its own law change, or it launches a reviewer against a grant it does not hold.

### Non-blocking

**D. Ten dependency blocks repeat a rule's full text twice in the same file.**
Location: dependency line then the rule's own row — 21/637 (`chain`), 285/154 (`delete on read`), 226/843 (`units`), 411/845 (`payers`), 413/853 (`price changes are edits`), 289/343 (`verdicts`), 330/58 (`two kinds`), 363/438 (`how not what`), 367/361 (`review axes`), 374/612 (`vertical slice`).
Criterion: content check 1 (redundancy); `inferable` and `ssot` as the view states them.
Reproduction: `grep -c "depends on \*\*payers\*\*" agents/policy_worker.md` → 1 and `grep -c "^\*\*payers\.\*\*" agents/policy_worker.md` → 1 in one file; `python3 - <<'EOF'` counting `^\*\*(.+?)\.\*\*` names found 368 unique names, so the duplication is in `render()`'s `drawn` set, which suppresses the second dependency render but not the later row. Fix belongs in `tools/law.py`.

**E. Four lists describe what a contract must carry, and no two agree.**
Location: `contract fields` (298, six lines), `reviewer contract` (341, nine), `subagent scope` (754), `model cost` (756); `tools/contract.py` enforces identity plus exactly the six.
Criterion: content checks 1 and 2; `ssot`.
Reproduction: quote 298 and 341; `python3 tools/contract.py --template` prints only identity and the six, so the nine named at 341 are unenforced and the extra two at 754/756 are optional in practice.
Consequence: case 14.

**F. The review criteria have two homes with different counts.**
Location: `review axes` (361, "all six axes") and `docs/review/contract.md` (the nine content checks, which is the acceptance this review was run against).
Criterion: content check 1 (redundancy) and `ssot`; check 9, since the law's own review rule and the repository's review contract are two lists for one activity and neither points at the other.
Reproduction: open 361 and `docs/review/contract.md` §"The nine content checks"; `logical self-consistency`, `omission` and `SMART` exist in the second list and not in the first.
Consequence: a reviewer dispatched by this role cannot tell which list is its acceptance.

**G. `rebuild after edit` requires a banner on every render; no render carries one.**
Location: 688 against the frontmatter and title of `agents/policy_worker.md` (lines 1–15).
Criterion: content check 9 (the view obeys the law it states).
Reproduction: `grep -c "AGENTS.yaml\|generated\|tools/" agents/*.md` → 0 for all six files.
Consequence: the only artefact that would tell a reader which file is the source is missing, which is the mechanism that leaves finding A unfixable in practice.

**H. Two decision rules fail the balance test.**
Location: `stuck disposal` (265) "Cancel when the loss is smaller; otherwise report a cost"; `self execute` (296) "worth less than about ten times the fixed cost of a dispatch".
Criterion: the balance test (two ends, each with a cost and a payer; the band; the pull) and `observable` (849: "A unit plus a command, a measurement or a named event; an adjective is not a price"); `balance default` (839) states the shape the corpus requires.
Reproduction: `python3 -c "import yaml;d=yaml.safe_load(open('AGENTS.yaml'));print(d['scheduling']['stuck_disposal']['_kind'], d['dispatch']['self_execute']['_kind'])"` → `act act`, and neither node has `_ends` or `_pull`; "the loss" and "ten times the fixed cost" name no unit and no payer.
Note: `docs/roadmap/policy.md` already records the migration as open ("351 acts remain, 114 decision candidates"), so this is a known-open instance, not a discovery; it is still a defect in this view today.

**I. A blocked contract has no absolute deadline.**
Location: `unreadable contract` (119) "Stop and name the field", and `kind contract` (117) — no time limit; `timeout clock` (657) shortens an agreement wait but names no threshold.
Criterion: system check timeout (every discussed block has an absolute deadline; only the no-discussion case waits forever).
Reproduction: read 117–119; neither line bounds the wait, and the rules that do bound waits (657, `block timeout`) are about an agreement or a question, not a contract the role cannot read.

**J. The law requires a Chinese side for every rule; the only view its writer reads never says so.**
Location: the whole view (`grep -c "zh\|Chinese" agents/policy_worker.md` → 0), against `tools/law.py --check`.
Criterion: content check 4 (completeness) and 9.
Reproduction, bounded and in an isolated copy (`/tmp`, since deleted): copy `AGENTS.yaml`, `tools/`, `agents/`; delete one `_goal.zh`; `python3 tools/law.py --check` → `FAIL architecture.two_kinds _goal has no zh` (exit 1), while the unmutated copy prints `ok`. A negative control that fails without the mutation: `laws.ssot` has no `_goal`, so stripping its `_when.zh` passes — the check has a hole for the 31 balance-slice nodes.
Consequence: low, because the check fails loud and teaches the field; recorded because the requirement is nowhere stated in the artefact.

**K. Same-meaning pairs inside the view.**
Location: `steerable` (251) against `no long in turn` (253) (identical act, adjacent); `one direction` (142) against `doorstep not shelf` (148) (both: write into their `inbox/`, never file it for them, never keep it at home); `ssot` (19) against `every fact has a home` (165); `derived` (47) against `derived is not stored` (181); `doc first` (453) against `rebuild after edit` (686).
Criterion: content check 1 (redundancy), and the writing lens's single-source-of-truth pruning.
Reproduction: the quoted line numbers; each pair states one meaning in two places, and in the `steerable`/`no long in turn` pair the two rulings differ slightly ("a long command" versus "takes minutes"), so a reader cannot tell which threshold binds.

## System checks

- Idempotency: fails for this role. `go` (95) and `take next` (294) tell it to take work and "write down that it is taken", and `context pressure` (752) names seven items to write before yielding; `worker records` (175) gives both no home, so a kill and reopen cannot reproduce the taken set. See finding B.
- Timeout: one discussed block waits without a deadline — the unreadable contract (finding I). Every other wait in the view either names a threshold (`block timeout`, `timeout clock`) or is the declared no-discussion case (`no agreement no work`).
- Efficiency: the artefact gives the role no way to know its own budget; `spend.class decides` and `deadline` are about packages the role dispatches. The contract I was given carried neither `paths` nor `spend` with a wall-clock, so the run itself had no declared budget to compare against — reported below, not counted against the artefact.
- Expectation: `rebuild after edit`, `coverage check` and `doc first` name an expectation and no how (finding A). The information the role must collect outside the contract — the corpus topology — is named nowhere, which the contract classifies as a contract defect to report; reported.

## Counts

Authority cases: 7 (rows 2, 5, 7, 12, 13, 15, 18).
Of these, **5 are `ambiguous` or `silent`** (rows 5, 7, 12, 13, 15; none `silent`, all five `ambiguous`); 2 are settled (delegated 2, stated 18).
Proceed cases: 14, of which 4 are `silent` (rows 1, 6, 8, 9), 1 `ambiguous` (row 14), 9 `stated`.
Total settled: 11 of 21 (`stated` 10, `delegated` 1) = 52%, against the review contract's 99% target.

## Not settled here, and what the parent should know

The contract I received named no `kind`, `roadmap`, `paths` or `spend` line, which `contract fields` (298) refuses at dispatch; I worked inside the scope it did name (this one artefact, this one report path) and record the omission as a contract defect rather than reading it as permission to sweep.
I did not read `docs/review/reports/researcher.md` or `docs/review/reports/worker.md`, nor any other role's view.
No commit was made and the artefact was not edited: this report is the only file I wrote, untracked at the revision above.
