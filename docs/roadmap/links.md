# Links

The pass over `_depends_on`: for each rule, read it as its reader, and ask one question — without this other rule, can the reader still do what this one says? If yes, no link. If no, the key goes in `_depends_on` and the reason goes below. The link is the reader's need, not where the rule came from; provenance is `_why` and is not filled here.

The table is the evidence of the pass. It grows section by section; a rule with no link says so and why.

## laws and architecture (31 rules)

| rule | depends_on | why |
|---|---|---|
| `ssot` | `chain` | The move says the file that owns the decision; without `chain` the reader cannot tell which layer owns it. |
| `atomic` | — | The subject and the one-line test are in the rule. |
| `kill` | — | The search for every old name is the procedure itself. |
| `no_op` | — | The five goods are the test, named in the rule. |
| `falsifiable` | — | The criterion and the safe failure are named in the rule. |
| `top_down` | — | The root is the law, not a named rule. |
| `absent` | — | The missing value and its record are the rule. |
| `controlled` | — | One variable at a time is the whole act. |
| `invalidate` | — | Finding what it reopened is the act; no other rule defines it. |
| `specific_wins` | — | The two rules and the choice are in the sentence. |
| `rule_over_state` | `migrate_on_touch` | "Bring what you touch" needs the minimal-neighbour procedure; without it the reader migrates the whole tree. |
| `own_inference` | — | The mark and the source are in the rule. |
| `untrusted_input` | — | Data versus judgement is the rule. |
| `derived` | — | The pointer or the command is the act. |
| `inferable` | — | The second home and the pointer are the rule. |
| `fail_loud` | — | The visible failure and the fallback are the rule. |
| `levels_in_order` | — | Higher and lower are the situation; the winner is the rule. |
| `two_kinds` | `kind_test` | The mapping needs the test that decides which kind this thing is. |
| `worker` | `contract_fields` | "Write it in the contract" needs the contract's line set; otherwise the line lands nowhere. |
| `kind_test` | — | The test stands alone. |
| `proposal` | `assent` | "assent 假定" is one of the four levels `assent` defines. |
| `document_parts` | — | The four parts are enumerated in the rule. |
| `roadmap_shape` | — | The statuses are enumerated in the rule. |
| `root_depth` | — | Asking the manager or the person is the act. |
| `parent_only` | — | The parent and the forward are the rule. |
| `name_is_the_trace` | — | The name and the path are the act. |
| `info_ownership` | — | Whose work the information changes is the test. |
| `everything_under_itself` | — | The project directory is the act. |
| `recursion_depth` | — | The five-level bound is the rule. |
| `workset` | — | The parallel set and the order are the rule. |
| `sub_owner` | `coverage_first` | The six things it must fix — coverage, interfaces, dependencies, ownership, acceptance, integrator — are defined there; without it the list is partial. |

## speech (22 rules)

| rule | depends_on | why |
|---|---|---|
| `upward_reports` | `report_fields` | "A report" is defined by its three fields; without them the reader writes a message, not a report. |
| `word_from_parent` | — | The parent is a role, not a rule. |
| `go` | `take_next` | The move says take the next workset by that procedure; the name is the procedure. |
| `parent_authorises` | `kinds` | The four things it can authorise are the four report kinds; without them the reader knows the words but not the routes. |
| `no_blind_agreement` | — | End, means and taste are separated in the rule itself. |
| `ask_only_consequential` | — | The test is in the rule. |
| `report_fields` | — | The fields are the rule. |
| `completion` | `report_fields` | A completion report is one of those reports; the three fields are not restated. |
| `kinds` | — | It defines them. |
| `kind_resource` | — | The route is the whole act. |
| `kind_cost` | — | The route is the whole act. |
| `kind_direction` | — | The route is the whole act. |
| `kind_contract` | — | The route is the whole act. |
| `unreadable_contract` | `kind_contract` | "Send it by kind contract" is that route; without it the reader knows to send it but not how. |
| `effort_required` | `kinds` | Cost and direction are two of the four kinds. |
| `forward_adds` | `recommend` | "Where the degree permits" is the recommend rule; without it the reader adds a recommendation in silent. |
| `beyond_authority` | — | The forward is the act. |
| `tasted` | — | The pinned artefact and the rebuild are the rule. |
| `three_deciders` | `kinds`, `classes`, `three` | It names the three deciders; each is defined by one of these. |
| `person_may_write_anywhere` | — | The forward and the wake are in the rule. |
| `ask_the_owner` | — | The wake and the record are in the rule. |
| `say_that_you_started` | — | The one line is the rule. |

## inbox (9 rules)

| rule | depends_on | why |
|---|---|---|
| `one_direction` | — | The directory and the two don'ts are the rule. |
| `tracked` | — | Version control is the act. |
| `file_shape` | — | The four header names are enumerated in the rule. |
| `sender_decides_nothing` | `alive_or_not` | "Send now or let it wake" is that rule's two routes; without it the stance has no method. |
| `alive_or_not` | — | It defines the two states and their routes. |
| `delete_on_read` | — | Land, then delete, is the whole act. |
| `delete_is_tidying` | — | The act is the rule. |
| `fire_and_forget` | — | The three returns are enumerated. |
| `correct_by_author` | — | The author and the pass-back are the rule. |

## records (17 rules)

| rule | depends_on | why |
|---|---|---|
| `write_through` | `ssot` | "The document that owns it" is ssot's home rule; without it the reader picks any document. |
| `entrance` | — | The four things an entrance carries are enumerated. |
| `entrance_for_next_session` | — | The one reader and the silence are the rule. |
| `missing_entrance` | — | Doing a little and reporting the block is the act. |
| `worker_records` | `report_fields` | The answer goes back as a report; the three fields are not restated. |
| `current_fact` | — | The present tense and git are the rule. |
| `retraction` | — | The reason stays; the dead claim is not restated — that is the act. |
| `cache` | — | The revision and the recompute command are in the rule. |
| `expired_cache` | — | Recompute or label is the whole act. |
| `assent` | — | It defines the four levels. |
| `assumed_is_agent_fact` | `assent` | "假定" is one of its four levels; without it the mark has no scale. |
| `no_mood_labels` | — | The occasion and the evidence are the rule. |
| `absent_claim` | — | The command and the hit count are the rule. |
| `no_manual_wrap` | — | One statement per line is the rule. |
| `fact_record` | `assent` | "status" is one of the levels `assent` defines; without it the coordinate is undefined. |
| `split_authorship` | — | Two records and the pointer are the rule. |
| `scratch_retired` | `migrate_on_touch` | The move names that procedure for relocating what still matters. |

## spend (18 rules)

| rule | depends_on | why |
|---|---|---|
| `classes` | — | It defines the classes. |
| `time` | — | The wall-clock and the split are in the rule. |
| `idle` | — | The site's power and the class are in the rule. |
| `metered` | — | The unit price is the act. |
| `exclusive` | — | The device, memory or port is in the rule. |
| `unrecoverable` | — | The rerun cost is the act. |
| `class_decides` | `classes`, `contract_grant` | The classes and the grant; without them "拿到授权" has no route. |
| `unknown_class` | — | Unknown plus the settlement step is the rule. |
| `no_hold_while_unsure` | — | Idle or settle first is the act. |
| `vram` | — | Headroom against what is held is the rule; the cost units are not needed to act. |
| `preempt` | `pause` | The resume point is that rule's stop, land, resume; without it "续跑点" is a word. |
| `missing_infra_is_not_missing_permission` | — | The permission and the infra are distinguished in the rule. |
| `advisory_limits` | — | Saying it is advisory is the act. |
| `claim_enforced` | — | Binding the job and its descendants is the act. |
| `significant_only` | — | The significant occupancy is defined in the rule. |
| `grant` | — | The split from what you were lent is the rule. |
| `queue` | — | The request and the trigger are the rule. |
| `price_clock` | — | The throughput/wait distinction is the rule. |

## scheduling (19 rules)

| rule | depends_on | why |
|---|---|---|
| `async_only` | — | Launch and wake are the rule. |
| `no_orchestration` | — | The direct child is the rule. |
| `steerable` | — | The timeout or the named log is the act. |
| `timeout_is_not_a_guard` | — | What the timeout does and does not kill is the rule. |
| `no_sleep` | `timeout_clock` | The detached timer is that rule's clock; without it the timer has no shape. |
| `client_budget` | — | The retry cap and idle timeout are the rule. |
| `no_watching` | — | Not watching is the act. |
| `stuck` | — | The declared wall-clock is the trigger. |
| `stuck_disposal` | `kind_cost` | "Report a cost" is that kind; without it the report has no route. |
| `own_effort` | — | Absorbing the obstacle is the act. |
| `change_hypothesis` | — | Change the hypothesis or the check is the rule. |
| `budget_caps` | — | The three numbers are the rule. |
| `always_a_path` | `kind_cost` | The escalation carries effort, which is the cost report. |
| `steer` | — | The correction in place is the act. |
| `async_continuation` | `async_only` | The trigger is the completion notification that rule defines. |
| `deadline` | `timeout_clock` | The detached timer is that rule's clock. |
| `pause` | `safe_point` | The stop point and the landing are that rule. |
| `inbox_first` | — | Reading first is the act. |
| `result_first` | `reviewer_contract` | Dispatching the review needs the nine lines; without them the dispatch is a sentence. |

## dispatch (18 rules)

| rule | depends_on | why |
|---|---|---|
| `take_next` | `roadmap_shape` | The `ready`/`running` statuses it reads are defined there. |
| `self_execute` | — | The trade is in the rule. |
| `contract_fields` | `reviewer_contract`, `budget_caps`, `subagent_scope`, `model_cost`, `worker` | "The lines other rules name" cannot be found without the rules that name them. |
| `contract_identity` | — | Kind, name and roadmap are in the rule. |
| `contract_grant` | `classes` | The grant is written in the spend classes. |
| `pass_boundary` | — | The boundary and the exclusion are the rule. |
| `coverage_first` | — | The six things are enumerated. |
| `persist_split` | `agreement_node` | The node with owner and acceptance is that rule. |
| `route_failure` | `coverage_first`, `roadmap_shape` | A re-split and a rewritten roadmap are those two. |
| `self_report` | `contract_fields` | The re-dispatch is a contract. |
| `worker_no_split` | `kind_contract` | The report it sends is that kind. |
| `area_is_permission` | `contract_fields` | The `paths` line is defined there. |
| `worker_one_message` | — | One report with what it found is the act. |
| `logical_level` | — | The one-value key is the test. |
| `logic_is_physical` | — | Converging the two boundaries is the act. |
| `preflight` | `contract_fields` | The named files and acceptance are the contract's lines. |
| `fresh_context` | — | Fresh or inherited is the trade. |
| `child_context` | `two_kinds` | Manager or worker is that rule's pair. |

## review (20 rules)

| rule | depends_on | why |
|---|---|---|
| `manager_does_not_judge` | `fresh`, `reviewer_contract` | The reviewer is fresh and dispatched with the nine; without them the dispatch is a sentence. |
| `fresh` | — | The fresh context and the scoped artefacts are the rule. |
| `judgement_only` | — | Mechanical first, judgement last is the act. |
| `reviewer_contract` | — | The nine are enumerated. |
| `verdicts` | — | It defines the three. |
| `not_a_verdict` | `kinds` | The three routes are the report kinds. |
| `no_commit` | `bind_to_revision` | The evidence bound to a revision is that rule. |
| `every_package` | — | One verdict per package is the rule. |
| `milestone_experience` | — | The milestone question is the rule. |
| `multimodal` | — | Looking first is the act. |
| `self_test` | `own_word_does_not_count` | A self-test is not independent acceptance; that principle says why. |
| `evidence_at_source` | — | The consumer's copy is the act. |
| `bind_to_revision` | — | The hash and the rerun are the rule. |
| `defect_evidence` | — | Location, criterion, reproduction are the rule. |
| `falsify` | — | The counterexample search is the act. |
| `scoped_review` | `reviewer_contract` | The scope is a contract line. |
| `three_kinds_of_review` | `every_package`, `milestone_experience` | The two kinds it separates are those rules. |
| `review_axes` | `how_not_what` | The step-shape axis is that rule. |
| `review_cost` | — | The token price is the rule. |
| `report_incomplete` | — | The unfinished acceptance and the next step are the rule. |

## gates and degrees (18 rules)

| rule | depends_on | why |
|---|---|---|
| `milestone_is_a_gate` | `vertical_slice` | The judgeable slice is that rule. |
| `few_milestones` | — | The one question is the rule. |
| `ship_at_gate` | — | Ship the real thing and hold dependants is the act. |
| `gates_hold` | `timeout_clock`, `lent_scope` | The finite wait and the lent period are those rules. |
| `invent_no_gate` | — | The small clear package is the test. |
| `advance_stops` | — | The three stops are enumerated. |
| `reach_agreement` | — | The four things are enumerated. |
| `three` | — | It defines the degrees. |
| `recommend` | — | The recommendation at that degree is the act. |
| `decide` | `assent` | "Record it as assumed" is one of assent's levels. |
| `silent` | — | The options and the cost are the act. |
| `unattended` | `assent`, `lent_scope` | The assumed decisions and the named gates are those rules. |
| `lent_scope` | `gates_hold` | A gate it does not name still waits — that is the hold rule. |
| `mixed_attention` | — | The observation and the depth are the rule. |
| `high_risk` | — | The list is enumerated. |
| `absorb_risk` | — | Defusing inside your authority is the act. |
| `secrets` | — | The value-based price is the rule. |
| `covered_once` | — | Not asking twice is the act. |

## writing (9 rules)

| rule | depends_on | why |
|---|---|---|
| `rule_form` | — | Situation, act, completion, failure route are enumerated. |
| `prose` | — | The order and the cuts are the rule. |
| `no_significance_clause` | — | What to delete is enumerated. |
| `no_hedging_known` | — | Assert or mark once is the act. |
| `concrete` | — | Name the thing is the act. |
| `user_language` | `expression_gap` | The gap is recorded and named by that rule. |
| `human_shape_and_rule_shape` | — | Two shapes, two readers is the rule. |
| `no_enumeration_invoice` | — | Re-derive the intent is the act. |
| `how_not_what` | — | The file, the command, the check are the rule. |

## change (15 rules)

| rule | depends_on | why |
|---|---|---|
| `problem_class` | — | The four classes are enumerated. |
| `signal` | `strongest_cure` | The rungs of the cure are that rule. |
| `bidirectional` | — | The class travels up, the person grows — the rule. |
| `strongest_cure` | — | The four rungs are enumerated. |
| `intake` | `roadmap_shape` | The node it becomes is a roadmap node. |
| `cut_repetition` | — | Search, then the smallest act, is the rule. |
| `amend_by_replacement` | — | Replace or merge in the same act is the rule. |
| `propagate_down` | — | Re-check down the chain is the act. |
| `supersede` | — | Delete the trace and re-derive is the rule. |
| `migrate_on_touch` | — | The minimal neighbour is the act. |
| `lossless` | — | One row per claim is the rule. |
| `scope_field` | `scope_composition` | What the scope list means is that rule. |
| `coverage_check` | `scope_composition` | "Every rule declares a scope" reads that meaning. |
| `scope_composition` | — | It defines the view. |
| `write_stricter` | — | Stricter for the actor, slack for the reader, is the rule. |

## docs shape, upkeep and resources (44 rules)

| rule | depends_on | why |
|---|---|---|
| `chain` | — | It defines the layer. |
| `layout` | — | One directory per layer is the rule. |
| `files` | — | The four kinds of file are enumerated. |
| `file_kind` | `render_is_written_not_read` | The render is the kind that may not be edited. |
| `granularity` | — | Split only to reduce ambiguity is the rule. |
| `rollup` | — | Compute, do not hand-write, is the act. |
| `home` | — | The roadmap and the open decision are the rule. |
| `agreement_state` | — | `aligning` and `agreed` are defined. |
| `no_agreement_no_work` | `timeout_clock`, `lent_scope` | The finite wait and the lent period are those rules. |
| `block_timeout` | `timeout_clock` | The tiers are measured on that clock. |
| `timeout_clock` | `no_sleep` | The detached timer is that rule's command. |
| `auto_advance` | `milestone_list` | The approved table is that rule. |
| `agreement_node` | — | One node with owner and acceptance is the rule. |
| `named_ids` | — | The number-name shape is the rule. |
| `people` | — | The one file is the rule. |
| `expression_gap` | — | Record first, name on the second, is the rule. |
| `keep_evidence` | — | Keep the evidence and the command is the act. |
| `resume` | — | Read the state, rerun the invalidated, is the rule. |
| `stereotype` | — | The three shapes are enumerated. |
| `partition` | — | One field, one value per group, is the rule. |
| `checklist` | — | The eleven are enumerated. |
| `resolvable` | — | Resolve the reference is the act. |
| `rebuild_after_edit` | `render_is_written_not_read` | The render is regenerated, never edited. |
| `render_is_written_not_read` | — | It defines the render. |
| `adopt` | — | Read all, decide each layer, then convert — the rule. |
| `migrate` | — | Idempotent, recorded, re-checked — the rule. |
| `outdated` | — | Value decides, not age — the rule. |
| `dead_code` | — | Reachability evidence is the rule. |
| `read_once` | — | One read per revision is the act. |
| `layout_first` | `layout` | The declared layout is that rule. |
| `defect_surface` | — | Shift left, make failure visible — the rule. |
| `efficiency` | — | Saving his time is the rule. |
| `start_early` | — | Start what is ready — the act. |
| `concurrency` | — | Real load and capacity — the rule. |
| `overlap_waits` | — | Fill the wait — the act. |
| `bounded_calibration` | — | One representative run — the rule. |
| `recovery_reserve` | — | Headroom from conditions — the rule. |
| `grant_recovery` | — | Confirm the jobs are dead — the act. |
| `follow_toolchain` | — | The lock and the scripts — the rule. |
| `bootstrap` | `readme` | The one command lives in the front door. |
| `local_config_first` | — | Local config, then the source — the rule. |
| `diagnose_network` | — | Diagnose before switching — the act. |
| `cleanup_check` | — | Uncommitted, unpushed, children — the rule. |
| `reproduce_or_artefact` | — | Reproduce or freeze — the rule. |

## roles, precedence, intent and delivery (43 rules)

| rule | depends_on | why |
|---|---|---|
| `manager_owns` | — | The four things it owns are enumerated. |
| `worker_owns` | — | The acceptance and the blocker are the rule. |
| `product_owner` | — | Roadmap, questions and quality are the act. |
| `trust_is_earned` | — | The five questions are the test. |
| `verify_the_fact` | — | The three checks are the act. |
| `watch_for_poison` | — | The four poisons are enumerated. |
| `source_order` | — | The order is enumerated. |
| `user_rank_scope` | — | Naming the rule and the urgency is the act. |
| `conflict` | `current_fact` | The "current fact" it compares is defined there. |
| `parent_contract` | `contract_fields` | `paths` and `accept` are contract lines. |
| `commitment` | — | Tier, audience, artefact, openness are enumerated. |
| `quality_dimensions` | — | Observation and tier per dimension is the rule. |
| `non_goals` | — | Writing what is not built is the act. |
| `derive_non_goals` | — | The proposed exclusions are the act. |
| `mechanism_triad` | — | The three answers are the test. |
| `cost_function` | `commitment` | The quality tier it stays inside is that rule. |
| `waste` | — | Buying a better result is the test. |
| `true_metric` | — | The claim shapes are enumerated. |
| `user_model` | `people` | The file it reasons from is that rule. |
| `self_contained` | — | The three carried things are the rule. |
| `understand` | — | The four questions are the act. |
| `reconcile` | — | Naming the conflict and choosing a reading is the rule. |
| `plan_ownership` | — | Options, effects, recommendation are the act. |
| `design_options` | — | One measure and the changing observation are the rule. |
| `question_frontier` | — | The prerequisite is the act. |
| `consequential` | — | The seven checks are enumerated. |
| `replan_lower` | — | Architecture, method, order versus product is the rule. |
| `hold_the_goal` | — | The priced decision is the act. |
| `substitute_design` | — | Reason, attempts and cost-benefit are the rule. |
| `disclose_changes` | — | Record it and say it at the milestone. |
| `fixed_milestones` | — | The agreed milestone is not moved. |
| `no_authority` | — | Preference versus authority is the rule. |
| `vertical_slice` | — | The thing itself is the rule. |
| `milestone_list` | — | The four things per milestone are enumerated. |
| `work_package` | — | The cohesive checkable outcome is the test. |
| `poc` | — | Hypothesis, method, criterion are the rule. |
| `protect_willingness` | — | Walking the acceptance and the failures is the act. |
| `presentable` | — | The surface reflects the work — the rule. |
| `readme` | — | The seven parts are enumerated. |
| `orientation` | — | The three links are the act. |
| `hard_metric_end` | — | One milestone at the end is the rule. |
| `completion_proof` | `verdicts` | "Which review passed it" is a verdict. |
| `readme_tested` | `readme` | The quickstart it runs is the front door. |

## proof, communication, principles and prices (53 rules)

| rule | depends_on | why |
|---|---|---|
| `think_first` | — | The five considerations are the act. |
| `baseline` | — | The scoped baseline is the act. |
| `only_authorized` | `falsifiable` | The check that catches the defect is that rule. |
| `separate_preexisting` | — | Separating pre-existing from introduced is the act. |
| `check_gates` | — | The three checks are the act. |
| `double_check` | — | Comparing result to goal is the act. |
| `anomaly` | `signal` | The improvement route is that rule. |
| `context_pressure` | — | The seven things are enumerated. |
| `subagent_scope` | `contract_fields` | The tools line is a contract line. |
| `model_cost` | `contract_fields` | The model is named in the contract. |
| `external_compute` | — | The spend, privacy and safety bounds are the rule. |
| `model_choice` | — | The site's table is the rule. |
| `extraction` | — | One question at a time is the act. |
| `ask_the_gap` | — | Asking while continuing is the act. |
| `report_only_effect` | — | The four effects are the test. |
| `match_user` | — | Language, level and order are the rule. |
| `vague_instruction` | — | State what you read is the act. |
| `round_as_diff` | — | The diff reading is the act. |
| `wait_for_yes` | — | Waiting is the act. |
| `divergence` | — | Naming the divergence is the act. |
| `announce_long` | `roadmap_shape` | The node it becomes is a roadmap node. |
| `interrupt` | `safe_point`, `steer` | The stopping state and the in-place correction are those rules. |
| `silent_advance` | — | Advancing without announcing is the act. |
| `brainstorm` | — | The six are enumerated. |
| `open_for_user` | — | Opening or uploading is the act. |
| `human_voice` | — | The six removals are enumerated. |
| `standing_list` | — | Name, count, the thing — the rule. |
| `result_not_inventory` | `report_fields` | The three fields are that rule. |
| `attention_is_a_budget` | — | The budget is the principle. |
| `docs_may_not_be_wrong` | — | The priority is the principle. |
| `true_because_checked` | — | The check is the principle. |
| `negotiable_not_editable` | — | Evidence and reason are the principle. |
| `risk_is_his_cost` | — | His cost is the principle. |
| `depth_over_breadth` | — | Depth first is the principle. |
| `provable_or_not_done` | — | Provability is the principle. |
| `explicit_criteria` | — | Criterion, failure, uncertainty are the principle. |
| `own_word_does_not_count` | — | Independence is the principle. |
| `time_is_the_scarce_thing` | — | Time first is the principle. |
| `scheduling_shape` | — | Early and waiting are the principle. |
| `split_follows_logic` | — | Logic is the principle. |
| `one_loop` | — | Find, write, point, re-check — the principle. |
| `intrinsic_benchmark` | `measurement` | Workload, correctness and resources are that rule's conditions. |
| `operational_load` | — | Concurrency, admission, interference are the principle. |
| `product_surface` | `readme` | The front door is one of its surfaces. |
| `method_selection` | — | Package kind and risk are the principle. |
| `balance_default` | — | It defines the balance shape. |
| `intro` | `units`, `payers`, `order`, `observable`, `payer_decides` | The six it names are the table. |
| `units` | — | It defines the units. |
| `payers` | — | It defines the payers. |
| `order` | — | It defines the order. |
| `observable` | — | The evidence is the rule. |
| `payer_decides` | — | The payer's choice is the rule. |
| `price_changes_are_edits` | — | The corpus edit is the act. |

## git, operations and practice (45 rules)

| rule | depends_on | why |
|---|---|---|
| `main_area` | — | The integration branch is the rule. |
| `one_writer_per_area` | — | Allocating the area is the act. |
| `worktree` | — | The worktree outside the tree is the rule. |
| `commits` | — | The local commit is the act. |
| `integrator` | `manager_does_not_judge` | The combined check goes to an independent party. |
| `pushes_hereditary` | — | The grant is the rule. |
| `no_remote` | — | Creating the private remote is the act. |
| `untrack` | — | Untrack, ignore, then rewrite is the act. |
| `no_trash` | — | Find the owner; never commit another's change. |
| `track_or_ignore` | — | Track by default is the rule. |
| `structure` | — | Owner and purpose are the rule. |
| `artefacts_home` | — | Keep it in the project is the act. |
| `store_or_declare` | — | The manifest is the rule. |
| `preserve` | — | No forced reset is the act. |
| `preserve_work` | — | Work around it is the act. |
| `regeneration_cost` | — | Ship what consumers need is the rule. |
| `safe_point` | `commits`, `main_area` | The committed state on the integration branch is those rules. |
| `intent_before_act` | — | The four written things are the rule. |
| `wind_down` | `commits`, `pushes_hereditary`, `steer` | Write, commit, push, steer — those rules. |
| `durability` | — | The rungs are enumerated. |
| `transient` | — | Ignore and delete freely is the rule. |
| `repair_on_sight` | — | Repair your own, report another's, is the rule. |
| `design` | — | The interface is the rule. |
| `abstraction_cost` | — | Naming the removed complexity is the test. |
| `feature` | `vertical_slice` | The behaviour-complete slice is that rule. |
| `diagnosis` | — | The loop first is the rule. |
| `reproduce_minimize` | — | One thing at a time is the act. |
| `hypothesis_probe` | — | One condition at a time is the act. |
| `diagnosis_closure` | — | Minimal fix and rerun is the rule. |
| `refactor` | — | Two commits, behaviour first — the rule. |
| `testing` | — | Behaviour interface and independent expectation — the rule. |
| `research` | — | The three written first are the rule. |
| `primary_evidence` | — | Version, date, query — the rule. |
| `experiment_record` | — | The bindings are enumerated. |
| `measurement` | — | Workload, correctness, resources — the rule. |
| `gate_probe` | — | The safe negative control is the rule. |
| `seriousness` | — | The five moves are enumerated. |
| `earned_budget` | `roadmap_shape` | The cap lives in the roadmap. |
| `caller_complexity` | — | The caller's knowledge is the rule. |
| `dependency_isolation` | — | The four classifications are the rule. |
| `test_scope` | — | Caller-observable first is the rule. |
| `test_doubles` | — | External effect, not orchestration — the rule. |
| `unavailable_repro` | — | Bounded attempts, then record. |
| `caller_migration` | — | Callers, behaviour, reversible migration — the rule. |
| `evaluation_integrity` | — | Population, data, metric, baseline — the rule. |
