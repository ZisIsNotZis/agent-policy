# Policy

The law is a derivation tree, written once, rendered into English views with a Chinese copy. This is its roadmap.

## The role model

Two kinds, not seven.

- **manager** is a level: it plans, splits, dispatches, collects, dispatches the review, runs the combined check, and keeps its own directory, document and roadmap. There can be zero managers or many levels.
- **root_manager** is the manager whose parent is the person. It does everything a manager does, plus the person-facing part: the target agreement, the degrees, the gates, the final report. pi reads `AGENTS.md`, a symlink to `agents/root_manager.md`; the role is `root_manager` everywhere else.
- **worker** executes one work package and reports once. It does not plan: no roadmap, no split, no dispatch, no review dispatch. It does the work in the package.

Worker specializations, same kind, different subject:

- **worker** — code, configuration, architecture, design.
- **policy_worker** — policy work: writing and changing the law; no code. The old name `policy_writer` is wrong.
- **researcher** — a question; reads, answers, writes only its own notes.
- **reviewer** — a verification; returns a verdict, repairs nothing. It verifies the worker's work: program, code, architecture, configuration, design, and the multimodal/emotional pre-review — trying to feel the thing for the person before the person feels it.
- **policy_reviewer** — the policy version of the reviewer: the law's structure, its balance shape, its coverage, its token price. No code.

**Scope follows the actor, not the judge.** A rule belongs to the role that performs its act. A role that only judges a rule gets it through its SOP's `_depends_on`, not through `_scope`. So:

- planning rules (roadmap, split, dispatch, combined check, gates, degrees, review dispatch) → `root_manager`, `manager`.
- document rules (`ssot`, `records`, `docs_shape`) → `root_manager`, `manager`, `policy_worker`. A worker writes code, not documents; a researcher writes only its own notes; neither reviewer writes anything.
- work rules (practice, proof, git, contract preflight/area) → `worker`.
- policy work (change, writing, the law's shape) → `policy_worker`.
- verification (verdicts, evidence, falsify, scoped review, multimodal) → `reviewer`; policy axes → `policy_reviewer`.

No rule lists every role. Most rules have one actor, some two.

## What is current, and what it is worth

`AGENTS.yaml` is 423 flat rules in Chinese. It is the working base, not the truth.

- The derivation tree is absent: no rule is nested under a parent; `_why` is empty on every rule.
- The 84 `_depends_on` links were asserted by me during the links pass, rule by rule. They are suspect and are not the truth; the tree pass re-derives every relation.
- The scopes have drifted: many rules list every role, which the role model above rules out. The true actor is usually one or two roles.
- The views are Chinese, large, and the SOP is special-cased with numbers and bold keys.
- `roles.yaml` carries `policy_writer`; the role is `policy_worker`.
- The old revisions — the 315-node tree and the pre-migration YAML — are **base data**: useful as a sketch of the parent relations and for the English half, polluted as a source of truth, above all in `_depends_on`. They are read, compared, and not copied.

## The target

- **Tree**: the 17 laws are the roots. Every other rule is nested under its main parent; other parents go in `_why`; `_depends_on` names concepts the reader may want to look up. Level is depth. `_` separates an attribute from a child rule's name, because a node's map holds both.
- **Bilingual**: every text is `{zh, en}`. `agents/<role>.md` is English; `agents/zh/<role>.md` is the Chinese copy.
- **Scopes**: re-derived from the actor; no rule lists every role.
- **Names**: `root_manager`, `policy_worker`.
- **SOP**: ordinary rules under their role; ordered by `_order`, rendered like every other rule — no numbers, no bold, no indent.
- **Format**: English views are ASCII; a choice starts `-` at column 0; `when -> goal`; `@key` at the end of the line; `move: gain; cost`.
- **Tool**: one pass, tree traversal, `--depth N`; it refuses a rule with no parent, a cycle, a scope naming every role, and a text without `en`.

## Roadmap

The old six packages are superseded by this rebuild. The result gate is not reached.

- [ ] `role_model_root`: the role is `root_manager`; pi reads `AGENTS.md`, a symlink to `agents/root_manager.md`; the tool refreshes it.
- [ ] `role_model_policy`: rename `policy_writer` to `policy_worker` everywhere — `roles.yaml`, every `_scope`, the `policy_writer_sop_*` keys, `install-agents.sh`, and the tool's law-role check; the descriptions follow the role model.
- [ ] `role_model_names`: the remaining SOP keys take the role's name (`root_sop_*` → `root_manager_sop_*`), so no key carries a retired role name.
- [ ] `role_model_descriptions`: the seven descriptions say what the role does, in the model above, and the reviewer's multimodal/emotional pre-review is named.
- [ ] `tree_skeleton`: decide the main parent of every rule, one by one. The old tree is base data, not truth; `_depends_on` is not evidence. `_why` gets the other parents.
- [ ] `tree_file`: shape `AGENTS.yaml` as nesting — attributes with `_`, children by name underneath their main parent; level is depth.
- [ ] `bilingual`: every text back to `{zh, en}`; the old English by key where it still fits, rewritten where the Chinese changed, written fresh for new rules.
- [ ] `scope_pass`: re-derive every scope from the actor; reviewers get criteria by `_depends_on`, not by scope; refuse any all-role list.
- [ ] `sop_plain`: SOP rules are ordinary rules; no numbering, no bold, no indent.
- [ ] `tool_tree`: rewrite `tools/schema.py` for the tree: parents, cycles, roots, scopes, bilingual texts, `--depth`; English and Chinese views in one pass.
- [ ] `views`: regenerate; English primary, Chinese copy; ASCII in English.
- [ ] `cleanup`: old names (`policy_writer`, `root` as a role), old views, old references, the old English half if it does not fit.
- [ ] `work_gate`: the tree changes only under a running package. This records the error that made it necessary. On 2026-10-22, during a discussion, the root role was renamed and `AGENTS.md` linked, then both were reverted; neither move had a go. Class: a correction of the information was executed as a change of the tree, the discussion was read as authorization, and the repair was treated as exempt from the stop. Expectation: a correction changes the owning document only; the tree changes when a package is `running` and the person has said go. Cure, strongest first: the tool refuses to write views when the roadmap has no `running` package; a pre-commit check maps the diff to that package's `paths`; the reviewer asks which package authorized the diff; the line is "a correction of the information is not a start". The person's side is recorded too: "change that" did not name the sentence or the file, so an ambiguous correction is read back as the object it names and waits.
- [ ] `result_gate`: the person reads the tree and names what is wrong, or accepts it.

Worksets: `role_model` first; `tree_skeleton` and `bilingual` can run per rule together; `tree_file` after the skeleton; `scope_pass` after the tree, since the parent informs the actor; `tool_tree` after `tree_file` and `bilingual`; `views` and `cleanup` last.

## Decisions

- `harness_name`: the role is `root_manager`; pi reads `AGENTS.md`, a symlink to `agents/root_manager.md`. The tool writes the view and refreshes the symlink.
- `law_scope`: no universal scope. Every rule, the laws included, carries the scope of its actor: `atomic` goes to the policy roles that write rules, `ssot` to the document maintainers, `falsifiable` to every role that produces evidence. The scope pass decides each; none is exempt for being a law.
- `reviewer_criteria`: the reviewer's view carries the verification rules; the work rules it judges arrive through its SOP's `_depends_on`, not through `_scope`.
- `old_english`: the old English half is used where the Chinese is unchanged; where the Chinese changed, the English is rewritten. Stale English is not copied.
- `link_truth`: no `_depends_on` survives by assertion; `tree_skeleton` re-derives every relation.

## The only person-owned decision

`result_gate`: the person reads the tree and either accepts it or names the rule that is wrong. That is the gate at the end, not a question I can answer for them.

## Evidence

- `python3 tools/schema.py` → `ok: 423 rules, 7 views, depth 0` is the current flat state, not the target.
- The old tree at `a1c47f1^` and the old YAML at `5e46382^` are read as base data.

## Retraction

The flat shape, the Chinese-only corpus, the all-role scopes, the numbered SOP and the name `policy_writer` are not the target. The old six packages are superseded; the rebuild above replaces them. Git holds the old tree and the old bilingual YAML as data, not as truth.
