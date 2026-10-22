# Policy

The product is the law in `AGENTS.yaml`, rendered to `AGENTS.md` and to one agent definition per role, and checked by `python3 tools/law.py --check`. This is the roadmap for that product.

## Current facts

- `AGENTS.yaml` is the only source: the rules, the six `role_specs`, the `lexicon.banned` list and the prohibition ceiling.
- `AGENTS.md` is a symlink to `agents/root.md`; `.pi/agents/*.md` are symlinks to the other five views. A view is generated and never edited.
- `sh tools/check.sh` refuses a stale view, a rule with no scope, a banned word, a prohibition count over the ceiling and a dispatcher field set that drifted from the law.
- `tools/contract.py` checks a contract's identity and six fields, refuses the old field names, and prints its byte count before dispatch.
- The workspace consumes this repository at a pinned submodule, so the text has one home and is still at the level an agent reads.
- The current commit holds current facts; process and history live in git.
- A proposal is a fact with `assent: assumed`, an author and a source; it lives in this document's open questions, not in a separate area. `work/` does not exist.
- An identifier carries a name in snake_case; a number is a prefix only when order matters (`1_snake_case`); the name is globally unique.
- The meta-rules are current: `problem_class`, `double_check`, `balance_default`, `timeout_clock`.
- The balance slice is current: `ssot`, `kill`, `no_trash`, `contract_fields`, `verdicts`, `signal`, `gates_hold`, `go`, `result_not_inventory`, `block_timeout`; `law.py` renders the pull.
- The helpful rules are current: `understand`, `no_blind_agreement` and `brainstorm` are balances; `trace_requirements` merged into `understand`.
- The RDI case is `docs/review/rdi_case.md`; `intake` carries the case, expectation, rule, observation, evidence and class.
- The `laws` section is migrated: 15 acts are balances; 351 acts remain, 114 decision candidates, in `docs/roadmap/balance_migration.md`.
- The review contract is `docs/review/contract.md`: the nine content checks, the case metric, the SOP test and the balance test.
- The `policy_worker` is the law's manager: it holds `AGENTS.yaml`, `agents/*.md` and this roadmap, so `self test` reaches it and `worker records` and `worker owns` no longer do.
- Every role spec carries a `sop`, rendered after the description and before the rules; `tools/law.py --check` refuses a role with no SOP, or a step naming a file that is gone.
- `area is permission` names both halves: the parent writes the paths in the contract, the child writes inside them.
- `worker no split` names the one child a worker may launch: the reviewer of its own slice.
- No document cites a ticket, an issue or a session.

## Roadmap

The result: every decision rule is a balance; each role's case list scores 99% `stated` or `delegated`; the helpful rules are agent-native; a problem is classified, routed and fixed at the class; the six views are readable; `sh tools/check.sh` is green; a fresh review passes.

```
1_foundation (done)
2_migration: law:  helpful_rewrite (done) -> rdi_chain (done) -> balance_migration (laws done; 351 acts)
             docs: case_lists (six files, one writer each)
3_measure:   baseline_score
4_gap:       gap_migration
5_rerun:     rerun_behavior
6_result:    result_gate (person)
7_cleanup:   cleanup
```

Worksets:

- `1_foundation` is done: the meta-rules and the ten-rule balance slice.
- `2_migration` starts now: the law stream is one writer, in order; the six case lists are separate files, so the root can dispatch them in parallel. The `balance_migration` has the `laws` section done; the 351 acts remain.
- `3_measure` after `case_lists`; `4_gap` after `3_measure` and the law stream.
- `5_rerun`, `6_result`, `7_cleanup` in order.

### balance_migration (the big change)

Outcome: every remaining decision act is a balance: two ends, each with a cost in the seven units and a payer, the band where the role acts, and the pull that says which way to yield; every procedure stays a how, with the balance that chooses it named; the `laws` section is done.
Deliverable: one commit per law section; the regenerated views; the word delta.
How: the section table, the decision/procedure method and the section order are in `docs/roadmap/balance_migration.md`; the `laws` section is the model; a rule that cannot be written as a balance is a design defect, not an exception.
Acceptance: the balance test in `docs/review/contract.md`; `check.sh` green; a fresh review; the case coverage.
Owner: the root dispatches one package per section in a worktree; the policy_worker merges the law file; the fresh review is the root's.

### case_lists

Outcome: six case lists: the moment, the axis (`authority`/`proceed`), the current verdict, the sentence that settles it or the missing one.
Deliverable: `docs/review/cases/<role>.md`; a merged index.
Seed: the six reports at `417ab94`; the role's law sections; the SOP cases from the 10-20 review.
Acceptance: every case is a moment, not a topic; the axis is marked; the verdict is backed by a quote or an absence; a fresh reviewer can reproduce it.

### helpful_rewrite

Outcome: `understand`, `trace_requirements`, `no_blind_agreement` and `brainstorm` are amended to agent-native language and scoped to every role; the old names die.
Deliverable: the commit; the views.
Acceptance: no new rule; the four are amended; the request-understanding cases improve; a fresh review.

### rdi_chain

Outcome: `problem_class`, `double_check`, the report payload and the `signal`/`intake` route are complete; a simulated problem walks from detection to rule fix.
Deliverable: the commit; the test; the views.
Acceptance: a fresh reviewer traces detection, class, owner and fix; the payload carries case, expectation, rule, observation, evidence and class.

### baseline_score

Outcome: the current law's coverage per role: counts of `stated`/`delegated`/`ambiguous`/`silent`; the gap list ranked by cost.
Deliverable: the score table and the gap nodes.
Acceptance: the counts sum to the case list; irreversible and expensive gaps are first; the 99% target is computed from the list.

### gap_migration

Outcome: the cases the baseline marks `ambiguous`/`silent` are closed by migrating their rules; the case list grows with each new case; coverage is re-scored.
Deliverable: one commit per workset; the updated case lists; the score table.
Acceptance: 99% `stated`/`delegated`; no new gap; `check.sh` green; a fresh review.
Order: irreversible and expensive gaps first, then the frequent ones.

### rerun_behavior

Outcome: one fixed task set runs under the old and the current law; the violations are compared.
Deliverable: the run log and the comparison.
Acceptance: the same tasks and model; only the law differs; every difference is attributed.

### result_gate (person)

Outcome: the person sees the rendered root and worker views, the case coverage table and the diff.
Deliverable: the views, the score, the rerun, the commit.
Acceptance: the person judges the direction; dependent work waits.

### cleanup

Outcome: the proposals graduate or die; the old forms die; this roadmap reflects the result; the final commit.
Deliverable: the commit; the README.
Acceptance: no proposal left as an open question; `check.sh` green; a safe point.

## Open questions

These are proposed, not law. Author: policy_worker. Source: the person's 2026-10-21 message. Assent: assumed.

| rule | what it says |
|---|---|
| `review_metric_home` | The case metric lives in the parent `docs/method/review.md`; a rule about role MDs belongs with the law. Decide: move it to `docs/review/`, or point at it and leave the parent copy as the owner. |

## Retraction

The four prose documents, the per-role guides and the `node` role were superseded by one `AGENTS.yaml` and two kinds, manager and worker. The old form and its dead names do not exist at this revision; git history holds the migration maps and the ledger.

`work/` and the discussion record died: an unconfirmed fact is still a fact, so it lives in the owning document's open questions with `assent: assumed`, its author and its source. A separate diary duplicated git history and violated the current-fact rule.

`plan` died for `roadmap`: `plan_tree` became `agreement_node`, and `docs/plan/` became `docs/roadmap/`. A bare number stopped being an identifier: `named_ids` requires a name.

The ten `act` forms of the balance slice died: their keys now carry balances, and the old goal/how pair is gone from those ten.

## Evidence

- `AGENTS.yaml` — the source.
- `sh tools/check.sh` — the pass line.
- `agents/*.md` — the generated views.
- `docs/review/contract.md` — the review criteria.
- `python3 tools/contract.py --template` — the contract skeleton, generated from the field set.
