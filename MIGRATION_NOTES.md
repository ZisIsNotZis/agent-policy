# LAW v7 — Migration and change notes

## Purpose

v7 incorporates the design review while preserving the three-role architecture: Communicator, Manager, Worker. It does not add a permanent Reviewer role or make the user a required day-to-day control loop.

## Decisions and changes

### 1. Communication chain and Communicator boundary

- Clarifies that Communicator is the root Manager's **communication parent/interface**, not an authority-bearing Manager or member of the project-management hierarchy.
- Communicator interprets and preserves user intent, relays it to the one Manager at the exact same CWD, and filters/consolidates outbound information to protect the user's attention.
- Communicator may read only the root Manager's explicitly published `STATE.md` status interface (or equivalent), read-only. It may not browse other project records or independently investigate project state.
- Filtering is attention management, not permission to distort or conceal material information.

### 2. Decision economics instead of an “irreversible action” gate

- Replaces irreversibility as a blanket escalation trigger with comparison of expected benefit, likelihood of matching expressed intent/preferences, action cost, recovery/reversal cost, cost of delay, and value/cost of further information.
- This is a reasoning framework, not a requirement for numeric calculations on every action.
- Actual legal, safety, security, platform, explicit user, and authorization constraints remain hard boundaries. Expected value cannot override them.
- Genuine user-dependent decisions are routed through Communicator; ordinary project decisions remain within Manager authority.

### 3. Bounded autonomy and resource ceilings

- Adds explicit prohibitions on unbounded agent/process spawning, retries, and exploration.
- Requires runtime/deployment-configured ceilings where applicable: hierarchy depth, fan-out, concurrent agents/processes, spend/usage, execution duration, and retry counts.
- Does not invent universal numeric caps. `templates/RUNTIME_LIMITS.example.yaml` is a configuration example, not an enforced policy by itself.
- Runtime enforcement is required for hard ceilings. If limits are absent, Managers must use conservative local bounds, avoid unbounded work, record the gap, and continue unaffected work.
- Limits must not be evaded through nested agents or relaunches.

### 4. Independent verification without a fourth role

- For consequential, novel, uncertain, or cross-component outcomes, Manager obtains an independent check from a Worker who did not produce the artifact, or an equivalent independent mechanism.
- The verifier receives the Goal and acceptance conditions and reports evidence/findings.
- Mechanical checks are preferred where suitable. Manager remains accountable for integration and the overall outcome.
- Review effort is proportional; trivial low-risk work does not require a second agent by default.

### 5. Scope, CWD, and concurrency

- Separates process CWD, Manager managed scope, and Worker work-package/write scope.
- Worker assignments must identify write scope and shared interfaces/resources.
- Parallel agents must not make uncontrolled concurrent changes to shared mutable files or repository state.
- Isolation (worktrees/branches/copies) is preferred when useful; otherwise assign shared-resource ownership or serialize conflicting operations.
- No particular VCS or workspace tool is mandated.

### 6. Async execution is specified as a runtime contract

- Removes implementation-specific sleep-process/timer instructions from LAW.
- Requires non-blocking launch, durable run identity, inspectable status/output, cancellation where applicable, and completion/failure events that wake or trigger reassessment.
- Completion events are signals, not authoritative results. Durable state/output must survive lost events and agent restarts.
- Runtime owns mechanics and enforcement; LAW specifies behavioral requirements.
- Missing async capability is reported precisely; unaffected work continues. It is not automatically a project failure or a reason to abandon all work.

### 7. Standard authoritative records

Added templates:
- `templates/GOAL.md`
- `templates/PLAN.md`
- `templates/STATE.md`
- `templates/HANDOFF.md`

Every Manager uses these as the default minimum scope records. Child Managers maintain records in their child scopes; parents summarize and link. The root Manager publishes concise user-facing status in `STATE.md` for Communicator's read-only access.

### 8. Role-view size and skills

- Narrowed role tags so Communicator no longer receives project research, project documentation, planning, execution, or engineering-quality procedures that it cannot perform.
- Kept shared epistemic and communication requirements where they serve the role.
- Updated planning, documentation/SSOT, and engineering-quality skills to align with bounded resources, async event recovery, explicit write scopes, standard records, and independent verification.
- No arbitrary 2–3 KB role-view target was imposed. The compiler emits per-role word counts and warns at a configurable threshold; it does not delete content to meet a size target.

### 9. Compiler lint and behavioral evaluations

Added:
- `tools/lint_policy.py`: standalone reference parser/renderer/linter for role tags, role contracts, empty headings, dangling `Section N` references, and per-role word-count warnings.
- `evals/role-and-runtime-scenarios.md`: action-based behavioral scenarios for role boundaries, Manager startup failure, status filtering, directory/concurrency rules, verification, bounded autonomy, decision economics, async recovery, and compiler checks.

**Renderer caveat:** the supplied production renderer was not available as a file in this working bundle. The included tool is a local reference implementation of the documented heading/tag inheritance semantics, not a claim that the user's production renderer was modified or executed. Run the production renderer and this lint suite in the target repository before deployment.

## Compatibility and migration

- Role tags remain `@communicator`, `@manager`, and `@worker`; no new role is introduced.
- The root Manager must still use the Communicator's exact CWD; Child Managers require distinct, non-overlapping managed scopes; their CWD need not be beneath the parent CWD. Workers may use an assigned working directory.
- The Communicator's status access is limited to a published `STATE.md`/equivalent interface; this does not weaken its no-project-investigation boundary.
- Existing project docs need not be rewritten all at once. Managers should migrate the active scope's Goal, plan, state, and handoff information into the templates as work naturally touches them, avoiding duplicate competing sources.
- Runtime limits must be wired into actual harness enforcement. A YAML example alone does not enforce anything.
- Runtime async completion events must be verified in the target harness; do not assume the described capability exists without testing it.

## Recommended rollout order

1. Run the target renderer and compare all three generated views.
2. Run `tools/lint_policy.py LAW.md --out <preview-dir>` and resolve errors.
3. Configure and test runtime ceilings and async completion/recovery behavior.
4. Introduce the standard record templates in one representative scope.
5. Run the behavioral scenarios against the actual agent harness; record observed actions, not merely verbal acknowledgments.
6. Roll out to other scopes after the role routing, limits, status publication, and recovery paths pass.

## v7 role-view size snapshot

The local reference renderer produced these word counts on the final source (counts are words, not tokenizer-derived tokens):

| Role | Words |
|---|---:|
| Communicator | 2,180 |
| Manager | 5,813 |
| Worker | 4,615 |

The Communicator view is intentionally much smaller and excludes project research, project documentation, management decomposition, and engineering execution guidance. Manager and Worker views remain longer because they carry project ownership/execution invariants. Further reduction should move detailed procedures into on-demand skills rather than remove necessary invariants. The production renderer may produce slightly different counts or heading layout; validate its actual output.


## v9 — independently rooted trees and user modeling

- Each tree starts at the Communicator's explicitly selected CWD with an explicit Goal/scope; no upward goal discovery.
- Exactly one root Manager per tree; user communicates only with its Communicator. User avoids overlapping tree roots, so adoption/re-parenting and cross-tree synchronization are not part of the operating model.
- Descendant Manager CWD need not be beneath parent CWD; managed scope and authority, not path nesting, define ownership.
- Defined recursive principal/escalation: root Manager serves the user through Communicator; descendants serve their parent Manager.
- Added single-outcome and multi-outcome scope modes for themed collections of distinct projects.
- Added authoritative root-owned `USER_MODEL.md`, Communicator-owned raw evidence, scoped preference rules, prediction calibration, and structured decision packets.
- Added `user-model-and-questions` and `portfolio-management` skills, plus `INTENT.md`, `USER_MODEL.md`, and `DECISION_PACKET.md` templates. `STATE.md` now has a proposed fixed-schema summary header; mechanical aggregation remains a runtime optimization, not something LAW pretends to implement.
- Deferred leases/fencing, mechanical rollups, subtree cancellation mechanics, and capability enforcement to runtime work.


## v10 — autonomous continuity, quiet communication, and recursive learning

- Made the LAW's governing behavioral principles explicitly higher than local `AGENTS.md`, project prompts, skills, and task instructions, while preserving actual system, safety, legal, platform, and runtime constraints.
- Made user participation strictly optional once a sufficiently intelligible Goal exists; every genuine wait for user input now requires a finite expiry and safe default.
- Replaced the Communicator's event-driven default with user-return polling. Only exceptional, genuinely time-sensitive notifications may wake it; it can emit, defer, batch, or suppress them. A timed review milestone includes an expiry/default and does not freeze unrelated work.
- Added quiet-output discipline: tools for action and coordination, internal reasoning for thinking, concise final parent handoffs, and no routine progress narration. A message reaching the Communicator is not itself a reason to notify the user.
- Added recursive escalation filtering: each agent must investigate and act within scope; parents return premature escalations with concrete next steps and only genuine authority/capability blockers move upward.
- Added recursive constructive learning for both produced artifacts/agents and the agent's own methods, driven by compiler/runtime warnings and errors, checks, reviews, peer feedback, and user corrections.
- Removed arbitrary hierarchy-depth, fan-out, concurrency, and retry ceilings as LAW requirements. Real platform/authorization limits still apply; responsible resource use remains a judgment duty rather than an austerity quota.
- Added missing YAML frontmatter to `portfolio-management` and `user-model-and-questions` skills.
- Added Pi subagent configuration directly to the generated Manager definition: the `npm:pi-subagents` child-session provider, nested-subagent permission, and a finite two-hour `timeoutMs`. Added deployment guidance for the extension’s separate finite depth guard; the documented default is two levels, so `PI_SUBAGENT_MAX_DEPTH` must be raised before Pi starts. The extension does not document unlimited depth. The v10 two-hour child timeout was removed in v11; see the v11 entry below for the current no-arbitrary-deadline rule.
- Reworked the English README and added a synchronized Simplified Chinese README, plus a small SVG mark. Documentation describes only files and commands present in this bundle.


## v11 — Goal fidelity, abstraction boundaries, recursive learning, and no arbitrary child deadline

- Added an explicit Goal-fidelity discipline: a technically successful proxy task is not success when it does not demonstrate the requested capability or use an explicitly required engine/platform. Managers must challenge method drift before more effort is spent.
- Added a compact Goal anchor as a living aid to judgment, not a rigid pre-execution specification.
- Made abstraction boundaries explicit: upward reports are translated into the parent's outcome language; internal IDs, thresholds, raw metrics, and implementation inventories remain in durable records unless needed for a decision.
- Tightened Communicator silence: no reassurance or "no action needed" filler. A lower-level report is not automatically a user notification.
- Strengthened recursive improvement: diagnose the earliest failed safeguard, update the responsible layer, add a regression scenario for the corrected invariant, and verify changed behavior. Parents must also learn from their own faulty framing, assignments, reviews, and acceptance criteria.
- Removed the two-hour `timeoutMs` defaults from both Manager and Worker generated definitions. Runtime guidance now distinguishes a bounded parent wait from a child-killing execution deadline and forbids arbitrary execution deadlines as a project-management policy.
- Added behavioral scenarios for requested-capability drift, upward abstraction, quiet handling of internal findings, recursive system-level learning, and opaque identifiers/plan worship.
- Updated both README languages to describe the revised policy and runtime configuration accurately.


## v12 — translated technical boundary, strict async, and consumed RSI staging

- **Worker-to-Manager firewall:** Workers retain technical ownership and translate why/how/result, Goal implications, uncertainty, and next action before reporting. Managers do not decode raw diagnostics or debug; they request a clearer translated report or independent qualified Worker review.
- **Strict async threshold:** any operation expected to exceed 60 seconds, or whose duration could reasonably exceed 60 seconds, must run asynchronously while the agent remains responsive to coordination messages.
- **Infrastructure PANIC:** inability to satisfy mandatory async, responsiveness, durable recovery, or message-path requirements is surfaced immediately and propagated to the user. No silent synchronous fallback.
- **Preserve active Managers:** never kill/relaunch an active Manager just to change timeout/configuration. If a finite runtime execution timeout is mandatory, it must be at least seven days; this is distinct from a user-decision wait timeout.
- **Actionable RSI:** added `root-cause-and-learning` skill and `templates/STAGING.md` (instantiated in each scope as `0_STAGING.md`). Staging entries are newcomer-readable, owned, actionable, due no later than the next milestone review, and must be processed, verified, moved to a durable home, then deleted. Critical invariant failures bypass ordinary staging.
- Added behavioral scenarios for technical translation, strict async, PANIC propagation, timeout preservation, root-cause learning, and staging consumption.

Markdown specifies these requirements but cannot itself make a harness asynchronous, keep a process alive, deliver messages, or enforce a timeout. The runtime must be tested; any discovered incompatibility with the mandatory rules is PANIC, not a reason to claim the requirement is operational.
