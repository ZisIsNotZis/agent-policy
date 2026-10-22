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
