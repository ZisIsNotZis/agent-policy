# Policy

The product is the law: one flat rule file, one schema, one tool, and the views the tool writes. This is the roadmap for that product.

## Current facts

- `AGENTS.yaml` is every rule: a flat map keyed by a leading word. A rule carries `_when`, `_know`, `_choices` (at least two, each with a long move and its gain and cost), `_scope` and `_goal`; optionally `_why`, `_depends_on` and `_order`. Nothing else is a field.
- `AGENTS.schema.yaml` is the one schema. `tools/schema.py` reads it and validates the corpus; the schema is never checked.
- `roles.yaml` is the harness: name, description, tools, thinking and ruleset for each of the seven roles. `banned.yaml` is the forbidden-term list.
- `tools/schema.py` is the one tool: one parse, validate, render, write. `--depth N` is the only flag; there is no check-only mode.
- `agents/<role>.md` is generated and never edited. The old `agents/zh/` copies are gone: the corpus is written in Chinese, so one view per role is the whole render.
- The law holds 423 rules: 381 migrated one-to-one from the old shape, plus 42 SOP steps added as rules with `_order`.
- `_depends_on` holds 84 links, each decided one by one by the question "without this, can the reader act?"; the evidence is `docs/roadmap/links.md`.
- The role split is current: `policy_writer` writes the law, `policy_reviewer` reviews it, and a worker launches nothing. The two law roles read root and manager rules in addition to their own.
- `banned.yaml` names 34 terms; the tool refuses a rule whose text uses one.
- No `_kind`, no `_between`, no `_pull`, no `_ends`, no `_links`, no sections, no `role_specs`, no `lexicon`, no `ceiling`: the old shape died at the swap; git holds it.
- `docs/review/cases.md` is bound to the pre-schema law and is history, not a current fact. `docs/review/contract.md` still describes the checks a policy reviewer applies.

## Roadmap

All six packages are done.

### 1_schema

- [x] `schema_file`: `AGENTS.schema.yaml` — `_when`, `_know`, `_why`, `_choices`, `_depends_on`, `_scope`, `_goal`, `_order`; no extra field.
- [x] `schema_kind`: `_kind` died; every rule carries the same fields.
- [x] `schema_choices`: a list of objects, each `move`/`gain`/`cost`, at least two, every one plausible.
- [x] `schema_depends`: `_depends_on` is a list of keys; each resolves.
- [x] `schema_know`: `_know` is text, present on every rule.
- [x] `schema_why`: `_why` optional, keys, never rendered.

### 2_data

- [x] `roles_file`: `roles.yaml` holds the harness fields of seven roles.
- [x] `banned_file`: `banned.yaml` holds the forbidden terms.
- [x] `sop_rules`: 42 SOP steps became rules with `_scope` and `_order`.
- [x] `yaml_names`, `yaml_cost_rule`, `yaml_choices`, `yaml_know`, `yaml_style`: the old fields folded into the new shape; one-to-one, 381 rules.

### 3_links

- [x] `links_audit`: every `_depends_on` decided by hand, rule by rule; 84 links, the table in `docs/roadmap/links.md`.
- [x] `links_scope`: each kept link names the reader's need, not the rule's origin.

### 4_split

- [x] `role_split`: `policy_worker` became `policy_writer`; `policy_reviewer` was added; scopes updated.
- [x] `worker_no_child`: the worker's SOP carries no reviewer launch; managers dispatch reviews.
- [x] `token_lens`: `policy_reviewer` judges the token price of a rule.

### 5_tool

- [x] `tool_one`: `tools/schema.py` loads once, validates, renders and writes; `--depth` is the only flag.
- [x] `tool_depth`: a view includes N levels of `_depends_on`; the default is 0.
- [x] `tool_fast`: one parse, one render, one write; no subprocess, no second pass.

### 6_cleanup

- [x] `cleanup_files`: the old tool, the old views, the migration files and the old references are deleted.
- [x] `cleanup_review`: `cases.md` is kept as history with a banner; the contract stays.
- [x] `cleanup_readme`: the README describes four sources, one tool and seven roles.
- [x] `cleanup_hook`: `.githooks/pre-commit` runs `tools/schema.py` and refuses a commit that leaves a view changed.
- [x] `cleanup_agents`: `install-agents.sh` links the six child roles, including both law roles.
- [x] `cleanup_hidden`: no `*` hidden-name logic remains.

### result_gate

- [ ] The person accepts the law, or names the rule that is wrong. This is the only stop.

## Open questions

| question | state |
|---|---|
| `depth_boundary` | A view at depth N draws layers 0..N. The N+1 boundary is not stubbed; the reader sees nothing of it. Kept as the person's call. |
| `view_size` | The root view is about 200k characters. Narrowing the scopes or rendering only the moves would cut it; not done, because the static brainstorm is the point. |
| `why_render` | `_why` is never rendered. It is the maintainer's provenance, not the agent's instruction. |
| `cases_history` | `cases.md` is kept with a banner. Delete it when its last reference goes. |
| `merge_candidates` | The one-to-one pass found pairs that may be one rule: `ssot`/`derived`/`inferable`, `kill`/`supersede`, `two_kinds`/`kind_test`/`worker`, `info_ownership`/`everything_under_itself`, `subagent_scope`/`model_cost`. Not merged; the migration kept one-to-one. |
| `why_empty` | `_why` is optional and empty on every rule. The derivation is not recorded yet; the links pass recorded reader needs, not provenance. |

## Evidence

- `python3 tools/schema.py` → `ok: 423 rules, 7 views, depth 0`.
- `sh tools/check.sh` → the same line.
- `docs/roadmap/links.md` → the link pass, rule by rule.

## Retraction

The old law — sections, `_kind`, act/balance/principle, bilingual fields, `role_specs`, `lexicon`, `ceiling`, six Python tools, `--check`, the `agents/zh/` copies — is dead at the swap commit. The flat file, the schema, the axis-then-choice model and the one tool replaced it; git holds the migration.
