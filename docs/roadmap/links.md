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
