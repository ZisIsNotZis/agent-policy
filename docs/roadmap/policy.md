# Policy

The product is the law in `AGENTS.yaml`, rendered to one agent definition per role under `agents/` and checked by `python3 tools/policy.py --check`. This is the roadmap for that product.

## Current facts

- `AGENTS.yaml` is the only source: the rules, the six `role_specs`, the `lexicon.banned` list and the prohibition ceiling.
- `agents/<role>.md` is the view a role reads; `AGENTS.md` does not exist. A view is generated and never edited.
- `sh tools/check.sh` refuses a stale view, a rule with no scope, a banned word, a prohibition count over the ceiling, a dispatcher field set that drifted from the law, a case row that cites a sentence its role does not read or a score table that disagrees with its rows, a duplicate key, a key in two sections, a key naming its own section, a per-section count that drifted from the corpus, and two rules with the same band. One command runs them: `python3 tools/policy.py --check`, or `sh tools/check.sh`.
- `tools/contract.py` reads a contract's field names out of `AGENTS.yaml` — the identity, the six floor lines, the lines above the floor and the nine of a review contract — and refuses a contract short of them, `stop: none`, a `stop:` that only restates the wall-clock, the old field names, and a payload over 16384 bytes.
- The workspace consumes this repository at a pinned submodule, so the text has one home and is still at the level an agent reads.
- The current commit holds current facts; process and history live in git.
- A proposal is a fact with `assent: assumed`, an author and a source; it lives in this document's open questions, not in a separate area. `work/` does not exist.
- An identifier carries a name in snake_case; a number is a prefix only when order matters (`1_snake_case`); the name is globally unique.
- The meta-rules are current: `problem_class`, `double_check`, `balance_default`, `timeout_clock`.
- Every discussed wait carries one absolute moment and one detached timer (`timeout_clock`: now / one day / three days by the answer's cost, a lent period overriding, only the empty wait unlimited); `block_timeout`, `gates_hold` and `no_agreement_no_work` read that clock, and `no_sleep` names the timer instead of banning `sleep`.
- The first balance slice is `ssot`, `kill`, `no_trash`, `contract_fields`, `verdicts`, `signal`, `gates_hold`, `go`, `result_not_inventory`, `block_timeout`; the test that decided the other 62 is in `docs/roadmap/balance_migration.md`; `law.py` renders a balance as when → goal. band. pull.
- Every balance carries a goal; `python3 tools/policy.py --check` refuses a balance with no `_goal`.
- The helpful rules are current: `understand`, `no_blind_agreement` and `brainstorm` are balances; `trace_requirements` merged into `understand`.
- The RDI case is `docs/review/rdi_case.md`; `intake` carries the case, expectation, rule, observation, evidence and class.
- Every rule that presents a live choice is a balance; the per-section count is in `docs/roadmap/balance_migration.md`, which `tools/counts.py` recomputes from the corpus and refuses if it drifts.
- The review contract is `docs/review/contract.md`: the nine content checks, the case metric, the SOP test and the balance test.
- The `policy_worker` is the law's manager: it holds `AGENTS.yaml`, `agents/*.md` and this roadmap, so `self test` reaches it and `worker records` and `worker owns` no longer do.
- Every role spec carries a `sop`, rendered after the description and before the rules; `tools/law.py --check` refuses a role with no SOP, or a step naming a file that is gone.
- `area is permission` names both halves: the parent writes the paths in the contract, the child writes inside them.
- `worker no split` names the one child a worker may launch: the reviewer of its own slice.
- No document cites a ticket, an issue or a session.

## Roadmap

The target: six files and one command.

```
AGENTS.yaml          rules only; every rule is a balance; keys are leading words, globally unique
AGENTS.schema.yaml   the one schema: required, optional, enums, no extra field, first level only
roles.yaml           the harness fields a role file needs, and nothing else
banned.yaml          the forbidden terms
schema.py            the one tool: validate, render, write; the only flag is --depth N
agents/              the render, English and Chinese
```

A rule is: a leading-word key; `_when` (one sentence, exceptions inline); `_know` (one text field: the facts to have an impression of before deciding); `_why` (optional, the derivation as a list of rule keys, never rendered); `_choices` (a list of plausible choices, each a long SOP direction with its `gain` and `cost` in text; the agent picks one); `_scope`; and `_goal` (the ideal end state, never the method). `_depends_on` is a list of rule keys, resolved against the corpus; whether a view draws one is not the schema's business. The render writes `@key` at the end of the row for each dependency it includes, because markdown is generated and `@` is lean there. No `_kind`, no `_between`, no `_pull`, no rubric, no ends list, no `_links` field.

A package is one file or one manual pass. Check the box when its accept line has run.

### 1_schema

- [x] `schema_file`: write `AGENTS.schema.yaml` — the fields `_when`, `_know`, `_why`, `_choices`, `_depends_on`, `_scope`, `_goal`; no extra field; first-level underscore only.
- [x] `schema_kind`: `_kind` dies; every rule carries the same fields.
- [x] `schema_choices`: `_choices` is a list of objects; each has `move`, `gain`, `cost`, all non-empty text; at least two, and every one plausible — no decoy.
- [x] `schema_depends`: `_depends_on` is a list of keys; each resolves to a rule; a dependency need not be drawn.
- [x] `schema_know`: `_know` is a text field, present on every rule, allowed to be empty.
- [x] `schema_why`: `_why` optional, a list of rule keys, never rendered.

Accept: a three-rule fixture validates; a corrupt fixture fails once per violation, naming the field.

Evidence at this revision: `python3 tools/schema.py tools/fixtures/valid.yaml` → `ok: 3 rules`; `python3 tools/schema.py tools/fixtures/invalid.yaml` → nine `FAIL` lines, one per violation, exit 1.

### 2_data (one file or one field set per package)

- [ ] `roles_file`: extract `roles.yaml` (name, description, tools, thinking, ruleset).
- [ ] `banned_file`: extract `banned.yaml`.
- [ ] `sop_rules`: SOP steps become rules with `role` and `order`.
- [x] `yaml_names`: `_ends` becomes `_choices`; `_between` and `_pull` die; `_when`, `_goal`, `_scope` keep their underscore.
- [x] `yaml_cost_rule`: one rule named `cost` absorbs `units` and `payers`, so `_depends_on: [cost]` resolves and the seven units and four payers live in one home.
- [ ] `yaml_choices`: every rule's band, pull and ends become choices — a long SOP direction with `gain` and `cost` in text.
- [x] `yaml_know`: write the `_know` text for every rule, by hand; the facts differ per rule and cannot be derived.
- [x] `yaml_style`: every `_goal` speaks in degrees — no 零、没有、不必、不让、definite — and uses the law's vocabulary without listing resources.

Accept: every rule validates; the rendered text reads as before or better; one commit per package.

One-to-one is complete in `AGENTS.next.yaml`: 381 rules, the old key set and order, every rule validating (`ok: 381 rules`). The old `AGENTS.yaml` stays authoritative until the swap; the render is package `5_tool`.

### 3_links (manual, rule by rule)

- [ ] `links_audit`: every `@` decided by one question — without it, can the reader act? Keep, delete, or add. No script. Started: laws and architecture are in `docs/roadmap/links.md`; 31 rules, 6 links.
- [ ] `links_scope`: every kept link names who needs it.

Accept: a table of rule → link → verdict → why, read by the person.

### 4_split

- [ ] `role_split`: `policy_worker` → `policy_writer`; add `policy_reviewer`; scopes updated.
- [ ] `worker_no_child`: a worker launches nothing; the manager dispatches the reviewer.
- [ ] `token_lens`: `policy_reviewer` names token efficiency among what it judges.

Accept: both policy views; the worker view carries no subagent right.

### 5_tool

- [ ] `tool_one`: write `schema.py` — load once, validate, render, write; `--depth N` the only flag, default 0.
- [ ] `tool_depth`: N and N+1 visibility — the open decision below.
- [ ] `tool_fast`: one parse, one render, one write, under two seconds.

Accept: `python3 tools/schema.py` writes every view in under two seconds; a corrupt fixture fails before anything is written.

### 6_cleanup

- [ ] `cleanup_files`: delete `tools/policy.py`, the checks that lived in it, every reference to the old model, and `AGENTS.next.yaml` after the swap.
- [ ] `cleanup_review`: decide the fate of `docs/review/cases.md` — review artefact, or delete.
- [ ] `cleanup_readme`: the README describes six files and one command.
- [ ] `cleanup_hook`: `.githooks/pre-commit` runs `python3 tools/schema.py`, not the old tool.
- [ ] `cleanup_agents`: `tools/install-agents.sh` and the `~/.pi/agent/agents` links carry `policy_writer` and `policy_reviewer`; the old `policy_worker` link and its view are gone.
- [ ] `cleanup_hidden`: confirm no `*` hidden-name logic exists anywhere; today it does not, and nothing reintroduces it.

Accept: a search for every old name returns nothing but git history.

### Migration notes

The one-to-one pass writes `AGENTS.next.yaml`: flat, every rule in the new shape, no merges and no semantic changes. Observations that need a later pass:

- `ssot`, `derived` and `inferable` overlap: a pointer is one way to keep one home, and no-duplication is ssot's consequence. Candidate merge, decided in the merge pass, not now.
- `kill` and `change.supersede` are twins: one says delete the old name, the other says replace with no trace. Candidate merge.
- `no_op` and `top_down` share the add-a-rule moment and test different things; keep both.
- `ssot` probably needs `_depends_on: [chain]`; the manual links pass decides.
- `rule_over_state` no longer names `migrate_on_touch`; the action is written out, so the link may go.
- `two_kinds` and `kind_test` share the manager-vs-worker moment: one is the test, one the consequence. Candidate merge.
- `worker` says what a worker holds; it may fold into `two_kinds`. Candidate merge.
- `info_ownership` and `everything_under_itself` both place information: one by the layer that uses it, one under the project directory. Candidate merge or a clear split.
- `recursion_depth` is a runtime limit, not a decision; candidate move to configuration or delete.
- Every act has one `_how`, so its one-to-one form has **one** choice. The schema needs two. The acts are procedures, not menus; the merge pass decides whether a second choice exists, whether the procedure folds into a balance, or whether it is deleted.

Worksets: `1_schema` and `5_tool` can start together, since the tool reads the schema; `2_data` after both; `3_links` after `yaml_names`; `4_split` after `links_scope`; `6_cleanup` last.

## Open questions

These are proposed, not law. Author: policy_worker. Source: the person's 2026-10-21 message. Assent: assumed.

| rule | what it says |
|---|---|
| `review_metric_home` | The case metric lives in the parent `docs/method/review.md`; a rule about role MDs belongs with the law. Decide: move it to `docs/review/`, or point at it and leave the parent copy as the owner. |
| `depth_boundary` | At depth `N`, layers 0..N are drawn. Is layer `N+1` shown as a one-line stub (`@key — goal`) so the reader can judge whether to raise the depth, or not shown at all? Recommendation: the stub; your last word was "not included = not shown", so this is your call. |
| `sections_in_yaml` | Sections stay as YAML nesting — grouping only, no semantics — or `AGENTS.yaml` becomes one flat map of rules? Recommendation: keep the nesting; it orders the view and costs nothing. |
| `goal_every_rule` | Every rule carries `goal`, the expectation. Confirm under "everything is a balance". |
| `text_language` | Every text stays `{zh, en}`, or one language per field? Recommendation: keep both; the Chinese view already exists and the migration cost is the same either way. |
| `case_file` | `docs/review/cases.md` is review evidence, not law. Keep it as evidence, or delete it at `cleanup_review`. |
| `unique_keys` | I do not agree that global uniqueness is manual: the schema cannot express it, but `schema.py` can collect keys and report duplicates mechanically. Recommendation: the tool checks it. |
| `why_render` | `_why` is not rendered for now; it lives in the source for the maintainer. Confirm this stays true when the renderer is rewritten. |
| `know_length` | `_know` lists every fact, or only the ones easy to forget? Recommendation: only the easy-to-forget ones, otherwise every rule becomes a checklist. |

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
- `python3 tools/policy.py --template` — the contract skeleton, generated from the law's field names.
