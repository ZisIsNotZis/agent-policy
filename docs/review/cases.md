# Cases

The 99% is counted over cases, not over rules: the moments a role must decide something by design. A case is one moment, one axis and one verdict, and the row cites the sentence that settles it.

- Axis `authority`: who decides. `proceed`: whether and how to act.
- Verdict `stated`: a rule answers it. `delegated`: a rule sends it to a named layer. `ambiguous`: rules disagree or leave a gap. `silent`: no rule.
- The list is derived from each role's SOP, its scope and `docs/review/reports/`; a case nobody thought to write is invisible to this count, so a reviewer must add the missing ones before trusting the score.

| role | cases | stated | delegated | ambiguous | silent |
|---|---:|---:|---:|---:|---:|
| root | 21 | 20 | 1 | 0 | 0 |
| manager | 19 | 19 | 0 | 0 | 0 |
| worker | 17 | 16 | 1 | 0 | 0 |
| researcher | 14 | 13 | 1 | 0 | 0 |
| reviewer | 14 | 14 | 0 | 0 | 0 |
| policy_worker | 15 | 15 | 0 | 0 | 0 |
| **total** | **100** | **97** | **3** | **0** | **0** |

97/100 stated and 3/100 delegated: 100% answerable by the law. Every cited name is in the role's own view; `tools/cases.py` refuses a citation its role does not read.

## root

| moment | axis | verdict | settles it |
|---|---|---|---|
| he says `go` | proceed | stated | `go` |
| his words are terse or self-contradictory | proceed | stated | `vague_instruction`, `reconcile` |
| two of his goals conflict | authority | delegated | `conflict` — it is his to settle |
| a gate is reached while he is away | authority | stated | `gates_hold` |
| a child returns a package | proceed | stated | `result_first`, `manager_does_not_judge` |
| the reviewer fails a package | proceed | stated | `route_failure` |
| a milestone is reached | authority | stated | `milestone_is_a_gate`, `advance_stops` |
| he asks how you would do it | proceed | stated | `plan_ownership` |
| he asks what only he can answer | proceed | stated | `ask_only_consequential` |
| he writes mid-work | proceed | stated | `interrupt` |
| the target is not agreed yet | proceed | stated | `no_agreement_no_work`, `reach_agreement` |
| heavy work has no immediate demand | proceed | stated | `announce_long` |
| the project's degree is not set | authority | stated | `three` |
| a proposal is still unanswered | proceed | stated | `proposal` |
| several packages have merged | proceed | stated | `own_word_does_not_count` |
| he asks to suspend a rule | authority | stated | `user_rank_scope` |
| the session was killed and reopened | proceed | stated | `resume` |
| you are told to stop | proceed | stated | `wind_down`, `safe_point` |
| he leaves for a named period | authority | stated | `unattended`, `lent_scope` |
| you are about to do something irreversible | authority | stated | `high_risk`, `secrets`, `pushes_hereditary` |
| you are handed a role view and must know what it reads | proceed | stated | `scope_composition` |

## manager

| moment | axis | verdict | settles it |
|---|---|---|---|
| the inbox has an unread message | proceed | stated | `inbox_first`, `delete_on_read` |
| a child returns a package | proceed | stated | `result_first` |
| a contract is short a field | authority | stated | `contract_fields`, `unreadable_contract` |
| a child asks to split its work | authority | stated | `route_failure`, `coverage_first` |
| two writers want one area | authority | stated | `area_is_permission` |
| a child is silent past its wall-clock | proceed | stated | `stuck`, `stuck_disposal` |
| a child fails review | proceed | stated | `route_failure` |
| you want more budget | authority | stated | `kind_resource` |
| you are tempted to judge your own child | authority | stated | `manager_does_not_judge` |
| a message belongs to another manager | proceed | stated | `one_direction` |
| the person writes to you | authority | stated | `person_may_write_anywhere` |
| a child asks above your layer | authority | stated | `beyond_authority`, `parent_only` |
| several packages have merged | proceed | stated | `integrator`, `own_word_does_not_count` |
| he says `go` | proceed | stated | `go` |
| he asks to suspend a rule | authority | stated | `user_rank_scope` |
| the session was killed and reopened | proceed | stated | `resume` |
| you are told to stop | proceed | stated | `wind_down`, `safe_point` |
| you are about to do something irreversible | authority | stated | `high_risk`, `secrets`, `pushes_hereditary` |
| you are handed a role view and must know what it reads | proceed | stated | `scope_composition` |

## worker

| moment | axis | verdict | settles it |
|---|---|---|---|
| the contract is short a field | authority | stated | `unreadable_contract` |
| the work needs splitting | authority | stated | `worker_no_split` |
| the accept line is unclear | authority | stated | `preflight` |
| you need a path outside `paths` | authority | stated | `area_is_permission` |
| you find a defect outside your scope | proceed | delegated | `repair_on_sight` — report, do not edit |
| you run the accept command | proceed | stated | `falsifiable` |
| two attempts produced no new evidence | proceed | stated | `change_hypothesis` |
| a check fails before your change | proceed | stated | `separate_preexisting` |
| the package is done | proceed | stated | `completion` |
| you are tempted to approve your own work | authority | stated | `own_word_does_not_count` |
| the person writes to you | authority | stated | `person_may_write_anywhere` |
| you are about to commit a credential | authority | stated | `secrets` |
| the session was killed and reopened | proceed | stated | `resume` |
| you are told to stop | proceed | stated | `wind_down`, `safe_point` |
| several packages have merged | proceed | stated | `integrator`, `own_word_does_not_count` |
| you are about to do something irreversible | authority | stated | `high_risk`, `secrets`, `pushes_hereditary` |
| you are handed a role view and must know what it reads | proceed | stated | `scope_composition` |

## researcher

| moment | axis | verdict | settles it |
|---|---|---|---|
| the question serves no decision | proceed | delegated | `research` — ask the layer that asked |
| the named budget is spent | proceed | stated | `research` |
| only second-hand evidence exists | proceed | stated | `primary_evidence` |
| the result cannot be reproduced | proceed | stated | `unavailable_repro` |
| the result is negative | proceed | stated | `research` |
| you are asked to write beyond your notes | authority | stated | `role_specs.researcher.description` |
| you are asked to dispatch | authority | stated | `role_specs.researcher.description` |
| the claim is wider than the metric | proceed | stated | `measurement` |
| the person writes to you | authority | stated | `person_may_write_anywhere` |
| you report | proceed | stated | `completion`, `report_fields` |
| the session was killed and reopened | proceed | stated | `resume` |
| you are told to stop | proceed | stated | `wind_down`, `safe_point` |
| you are about to do something irreversible | authority | stated | `high_risk`, `secrets` |
| you are handed a role view and must know what it reads | proceed | stated | `scope_composition` |

## reviewer

| moment | axis | verdict | settles it |
|---|---|---|---|
| the acceptance is missing | authority | stated | `verdicts`, `unreadable_contract` |
| you are asked to review your own work | authority | stated | `own_word_does_not_count` |
| the producer offers its context | proceed | stated | `scoped_review` |
| a check can be run by a program | proceed | stated | `role_specs.reviewer.sop` |
| you must return a verdict | proceed | stated | `verdicts` |
| you find a defect and want to fix it | authority | stated | `role_specs.reviewer.description`, `repair_on_sight` |
| several packages need review | proceed | stated | `every_package` |
| the milestone, not a package, is judged | proceed | stated | `milestone_experience` |
| the evidence exists only in a copy | proceed | stated | `evidence_at_source` |
| the person writes to you | authority | stated | `person_may_write_anywhere` |
| the session was killed and reopened | proceed | stated | `resume` |
| you are told to stop | proceed | stated | `wind_down`, `safe_point` |
| you are about to do something irreversible | authority | stated | `high_risk`, `secrets` |
| you are handed a role view and must know what it reads | proceed | stated | `scope_composition` |

## policy_worker

| moment | axis | verdict | settles it |
|---|---|---|---|
| a new rule duplicates an existing one | proceed | stated | `amend_by_replacement` |
| `law.py --check` fails | proceed | stated | `role_specs.policy_worker.sop` |
| a view drifted from the source | proceed | stated | `render_is_written_not_read` |
| your own change needs a verdict | authority | stated | `own_word_does_not_count`, `fresh` |
| the law contradicts itself | authority | stated | `double_check` |
| the person asks for a law change | proceed | stated | `amend_by_replacement`, `understand` |
| the contract field set changed | proceed | stated | `role_specs.policy_worker.sop` |
| a balance has no goal | proceed | stated | `balance_default` |
| you are tempted to orchestrate other layers | authority | stated | `no_orchestration`, `worker_no_split` |
| an old name survives the change | proceed | stated | `kill` |
| a gate is reached | authority | stated | `gates_hold` |
| the session was killed and reopened | proceed | stated | `resume` |
| you are told to stop | proceed | stated | `wind_down`, `safe_point` |
| you are about to do something irreversible | authority | stated | `high_risk`, `secrets`, `pushes_hereditary` |
| you are handed a role view and must know what it reads | proceed | stated | `scope_composition` |

## What this list does not cover

The universe is the role's design, and this list is one derivation of it. A case that no SOP step, scope line or review report produced is not counted; the reviewer's job is to add it. The score is only as good as the list.
