# Agent Policy Skills

These are optional, on-demand procedural playbooks referenced by `LAW.md`. Load a skill when its description matches the work. They supplement the policy; they do not override the Goal, actual operating constraints, or LAW. Expectations in LAW define durable outcomes and boundaries; MUST procedures in LAW and skills translate critical expectations into action at recurring decision points. Do not treat a required procedure as optional merely because another action is more familiar or convenient.

| Skill | Use when |
|---|---|
| `research-and-discovery` | Uncertain, novel, research-heavy, creative, or potentially misframed work |
| `project-framing-and-validation` | Understanding intent, reframing an existing effort, and defining success |
| `planning-and-decomposition` | Decomposing outcomes, choosing child Managers versus Workers, delegation, dependencies, and integration |
| `documentation-and-ssot` | Project memory, documentation hierarchy, and authoritative sources |
| `engineering-quality` | Software implementation, testing, debugging, and review |
| `release-and-delivery` | User-facing delivery, packaging, publishing, and reachability |
| `repository-hygiene` | Repository structure, naming, indexing, and cleanup |
| `safe-migration` | Broad refactors, schema changes, and structural/data migrations |

## Organization model

- **Communicator:** default user-facing interface; primarily passive/event-driven, consolidates briefings on user return, and delivers genuinely urgent notifications.
- **Manager:** recursively owns an assigned scope, decomposes work, creates child Managers or Workers, coordinates, integrates, and remains accountable for the outcome.
- **Worker:** owns and validates one bounded work package.

The Manager hierarchy has no fixed depth. Create a child Manager only when its scope needs independent decomposition, coordination, and integration. Otherwise delegate a bounded package to a Worker.

Each skill is self-contained in its own directory as `SKILL.md`.

## Role identity and runtime continuity

The loaded role instruction is the source of role identity. The first identity statement in each role instruction should explicitly say `You are the Communicator`, `You are the Manager`, or `You are the Worker`, with the matching role tag where the compiler expects it. Do not rely on harness-supplied agent names or process labels to establish role identity. The LAW role sections provide both role expectations and mandatory operating procedures. Before substantive work, classify the responsibility and route work that belongs to another role; do not perform it first and acknowledge the boundary violation afterward.

Asynchronous process execution is the minimum runtime capability for non-blocking work. Long-running subprocesses and delegated agent runs must be launched asynchronously; native async-subagent support is optional because a separate harness CLI instance can serve as a fallback. Use platform-native process facilities rather than requiring Bash or a persistent terminal. See the Planning and Decomposition and Research and Discovery skills for task tracking, timers, and reassessment guidance.

Role-specific operating contracts are placed before the universal policy in the source LAW so each compiled system prompt begins with the agent's own identity, responsibilities, and required intake/execution procedures. Compiler metadata and tag semantics belong in the untagged source preamble; they are not agent-facing instructions.
