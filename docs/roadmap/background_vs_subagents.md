# Background tasks vs subagents

## Verdict

Keep `pi-subagents` 0.80.0 and `pi-bg-bash` 0.4.1 as they are; do not install `pi-background-tasks`.
`pi-background-tasks` exists (2.6.10) and is a different package from `pi-bg-bash`: different author, different tools, different shape.
It cannot replace `pi-subagents` in this project: its delegated child is inspect-only and accepts no agent definition, while this project's role views are `pi-subagents` agent files whose frontmatter `tools/law.py` enforces.
Pi has no built-in background bash: `background:true`, `bash_tasks`, `bash_output` and `bash_kill` are `pi-bg-bash`'s surface, so the "overlap with built-ins" in the task premise does not exist.
Under `async_only` and `no_orchestration`, the simplest correct shape is one direct async `subagent({ agent, task })` for a role child and `bash({ command, background: true })` for shell work: no workflow script, no chain, no `bg_wait`.

## 1. What each package does, and what pi-background-tasks is

`pi-subagents` 0.80.0 is a Pi extension for single-agent delegation and scripted multi-agent workflows (`/home/z/.pi/agent/npm/node_modules/pi-subagents/package.json:4`).
Its unit is a child Pi session: "A subagent is a focused child Pi session with its own job"; foreground children run in the parent process and background children run "as sessions inside a detached runner process" (`pi-subagents/README.md:43`, `:45`).
It ships role agents (`scout`, `researcher`, `evidence-auditor`, `worker`, `reviewer`, `oracle`, `delegate`), each a Markdown file whose body is the system prompt and whose frontmatter sets the tool allowlist, thinking, model and acceptance role (`pi-subagents/README.md:55-70`; `pi-subagents/agents/reviewer.md:1-10`).
It also ships workflow scripts, missions and schedules, a watchdog, an intercom/`contact_supervisor` bridge, fleet observability, external-CLI runners and external-job providers (`pi-subagents/README.md:115-132`; `pi-subagents/package.json` `exports`).

`pi-bg-bash` 0.4.1 runs the model's bash commands as detached background tasks and wakes the agent when they finish (`pi-bg-bash/package.json:4`).
It "replaces Pi's `bash` tool with the same tool plus a `background` flag" (`pi-bg-bash/README.md:4`).
It adds `bash_output`, `bash_tasks`, `bash_kill`, the `/bg` list, the `ctrl+shift+b` shortcut, a `bg: N` footer, 120 s foreground promotion, logs under `$XDG_STATE_HOME/pi-bg/<session-id>/`, a group kill, a crash watcher and one completion message per task (`pi-bg-bash/README.md:60-90`, `:153-160`, `:124-140`).
It launches no model: its launch path is `sh` spawned detached with a watcher, and its tool schema is Pi's bash schema plus `background`/`waitFor` (`pi-bg-bash/src/launch.ts:161-210`; `pi-bg-bash/src/index.ts:76-93`).

`pi-background-tasks` 2.6.10 is a third, distinct package (`npm view pi-background-tasks version description repository.url`, run 2026-10-22): "Pi extension for durable background shell tasks, read-only delegated agents, local attested Pi runs, and fixed-purpose Fusion workflows through child Pi processes".
Its surfaces are `bg_run`, `bg_status`, `bg_logs`, `bg_kill`, `bg_delegate`, `bg_result`, `bg_run_pi_attested` and four `fusion_*` tools, with commands `/bg`, `/jobs`, `/tasks`, `/fusion` (`/tmp/pbt/package/README.md:48`; fetched as the published tarball `npm pack pi-background-tasks@2.6.10`).
It is not installed here: `ls /home/z/.pi/agent/npm/node_modules | grep -ci background` returns 0.
`pi-bg-tasks` 0.1.4 is yet another package (`github.com/cyzlmh/pi-extensions`); `pi-bg-bash`'s README already names it as the one not to install alongside (`pi-bg-bash/README.md:19-20`).

## 2. Can a background bash task launch a role agent?

Not as a feature of `pi-bg-bash`.
Its `bash` tool takes a command and nothing else: Pi's `{ command, timeout }` plus `background` and `waitFor`, with no agent, prompt, model or route parameter (`pi-bg-bash/src/index.ts:76-93`; `pi-bg-bash/README.md:60-77`).
Its launch path spawns `sh` and a watcher and never a Pi process (`pi-bg-bash/src/launch.ts:161-210`), and its completion message is exit state plus the last 20 lines of output capped at 4 KiB (`pi-bg-bash/README.md:153-160`).

A shell command can of course start a Pi process, and the CLI has the flags for it: `-p/--print` runs the prompt once and writes the final assistant text (`pi docs/cli.md:45`), `--tools` replaces the tool selection with an allowlist (`pi docs/cli.md:119-120`), and `--system-prompt` / `--append-system-prompt` take text or a file (`pi docs/cli.md:229-231`).
That route is hand-built and lossy: the CLI has no `--agent` flag (`grep -n -- "--agent" pi docs/cli.md` returns nothing), the CLI parses no `pi-subagents` frontmatter (`systemPromptMode`, `acceptanceRole`, `thinking`, `model`), and the parent gets an exit code and a 4 KiB tail instead of a structured result, a run id, `resume`, `steer` or an acceptance gate.

The mechanism does exist natively, in two other places.
In `pi-subagents`, a background child is a session in the detached runner, and its agent file supplies the system prompt (`systemPromptMode: replace`), the tool allowlist, the model/thinking and the acceptance role (`pi-subagents/README.md:45`; `pi-subagents/agents/reviewer.md:1-10`; `pi-subagents/docs/standalone-background.md:1-10`).
In `pi-background-tasks`, `bg_delegate` starts one child Pi with its own session and a pinned route, but only for inspection: "Only \"inspect\" (read/search/list, no shell, no writes, no network, no recursion) is supported" (`/tmp/pbt/package/docs/tools/bg_delegate.md:23`), `DELEGATE_CAPABILITIES = ['inspect']` (`/tmp/pbt/package/src/core/delegate/types.ts:35`), and its parameters are `name`, `prompt`, `capability`, `route`, limits and delivery modes, with no agent definition or system-prompt override.
So the only extension here that can run a `worker` or `manager` role with its own system prompt and write tools is `pi-subagents`.

## 3. Does pi-subagents force a workflow, chain or tasks shape?

No. The direct `{ agent, task }` call is the default simple shape and is async by default.
The schema's top level is `agent`, `task`, `workflow`, `args`, `async`, `model`, `cwd`, `worktree`, `output`, `action`, `id`, `message` (`pi-subagents/docs/tool-reference.md:70`; `pi-subagents/src/extension/schemas.js:138-139`, `:221`).
`async` is documented "default-on. Background execution. Workflows default to background. `async:false` blocks the parent until completion" (`pi-subagents/docs/tool-reference.md:104`).
The skill says: "Use async/background by default. Set `async:false` only when the parent must block" (`pi-subagents/skills/pi-subagents/SKILL.md:69`).
The skill also refuses the shape the premise worries about: "Native direct `{ agent, task }` calls have no top-level `label` parameter; do not invent one or wrap a tiny single task in a workflow just to label it" (`pi-subagents/skills/pi-subagents/SKILL.md:64-66`).
The reference has a section "Single agent" with `subagent({ agent: "oracle", task: ... })` and says: "Use direct single-agent execution for one bounded task when no stable key, branching, retained-child lookup, or aggregate workflow result is needed" (`pi-subagents/skills/pi-subagents/references/execution-controls.md:37-50`).
The recipes file says: "Run subagents asynchronously by default; direct one-child execution is enough for one bounded task, while a workflow script ... is the composition surface for JavaScript control flow and data-dependent branching" (`pi-subagents/skills/pi-subagents/references/constraints-and-recipes.md:37`).
The chain/tasks shape is the deprecated one: "Legacy top-level `chain`, `tasks`, and `parallel` inputs are not supported, except that `disabledFeatures: ["workflow-scripts"]` replaces workflow scripts with top-level `chain` and `tasks`" (`pi-subagents/docs/tool-reference.md:13`).
One friction point worth knowing: a fresh parent session may first expose the loader `subagents_enable` instead of the full schema, and Pi can call it itself when the request authorizes delegation (`pi-subagents/README.md:47`); `bg_wait` and supervisor replies stay available without activation.

## 4. What overlaps with pi's built-in bash background tasks?

Nothing, because there is no built-in bash background facility in the installed Pi.
The installed Pi is 1.3.0 (`node -e require(.../pi-coding-agent/package.json).version`), and its bash tool schema is `{ command: string, timeout?: number }` (`.../pi-coding-agent/dist/core/tools/bash.d.ts:6-9`; `dist/core/tools/bash.js:29-30`).
`grep -rl "bash_tasks"` over the installed Pi package (14984 files) returns 0 files; `bash_output` likewise 0.
The same check on the latest release, 1.4.0 (`npm view @earendil-works/pi-coding-agent version` -> 1.4.0, modified 2026-10-21), returns 0 files for `bash_tasks` across 1279 files, and its `bashSchema` is still `command` + `timeout` with no occurrence of `background` in `bash.d.ts`.
So `background:true`, `bash_tasks`, `bash_output` and `bash_kill` are `pi-bg-bash`'s additions, not Pi's, and the premise's "overlap with pi's built-in bash background tasks" is empty.

What does overlap, between the two installed extensions, is small and complementary:
Both wake the parent on completion: `pi-bg-bash` sends one `pi.sendMessage` with `deliverAs: "steer"` and `triggerTurn: true` (`pi-bg-bash/README.md:153-160`), and `pi-subagents` wakes the parent when an async run completes (`pi-subagents/skills/pi-subagents/SKILL.md:73-77`).
Both show a status surface: `bg: N` in the footer (`pi-bg-bash/README.md:167`) and the FleetView/`/subagents-fleet` inspector (`pi-subagents/README.md:95-103`).
They cover different payloads: one runs a shell command, the other runs a model child; neither can do the other's job.
They meet in one place: background children load the parent's ambient extensions, so `pi-bg-bash` is present inside a detached-runner child, while foreground children never load ambient extensions (`pi-subagents/docs/agents.md:424`, `:522`); inference: a child can therefore start its own background shell task, which the parent's `bash_tasks` does not list, since tasks belong to the session that started them (`pi-bg-bash/README.md:84`).

If `pi-background-tasks` were installed, the overlap would be real and messy:
it registers `/bg` and `/jobs`, `/tasks`, `/logs`, `/kill`, which collides with `pi-bg-bash`'s `/bg` (`/tmp/pbt/package/README.md:48`; `pi-bg-bash/README.md:80`).
It does not replace the `bash` tool: `grep -rl createBashTool src extensions` returns 0 files and the only `name: 'bash'` hit is a type union at `src/core/common.ts:1011`, so the two would keep two task registries, two wake channels and two status surfaces.
`pi-bg-bash`'s install notes already require no other extension that replaces the `bash` tool or registers `/bg` or `ctrl+shift+b` (`pi-bg-bash/README.md:17-20`).

## 5. Recommendation

Keep both installed packages; change nothing; do not adopt `pi-background-tasks`.
Four reasons, each from evidence above:
The project's role agents are `pi-subagents` agent files: `agents/*.md` carry `systemPromptMode: replace`, `acceptanceRole`, `tools` and `model: inherit` (`agents/manager.md:1-11`), and `tools/law.py` refuses a role that loses `systemPromptMode: replace`, `inheritProjectContext: false` or `inheritGlobalContext: false` (`tools/law.py:203-208`).
The dispatch protocol this corpus relies on uses `contact_supervisor`, which `pi-subagents` registers in children (`pi-subagents/src/runs/shared/child-tool-plan.js:243-255`; `agents/reviewer.md:4`; this session's own tool list).
`pi-background-tasks`' child is inspect-only and cannot host `worker`, `manager` or `policy_worker`, which write files (`/tmp/pbt/package/docs/tools/bg_delegate.md:23`; `agents/worker.md:4`).
Its Fusion surfaces are a fixed three-candidate workflow with evaluator, repair and merger (`/tmp/pbt/package/README.md:189-192`), which is the orchestration shape `no_orchestration` forbids (`agents/manager.md:245`; `AGENTS.yaml:1801`).

The simplest correct shape under `async only` (`agents/manager.md:243`; `AGENTS.yaml:1789`) and `no orchestration` (`agents/manager.md:245`):
A role child is one call: `subagent({ agent: "reviewer", task: "<one bounded task>" })`; it is async by default, it needs no key, no workflow and no chain, and its completion wakes the parent (`pi-subagents/docs/tool-reference.md:104`; `pi-subagents/skills/pi-subagents/references/execution-controls.md:37-50`).
Shell work is `bash({ command, background: true })`, read with `bash_output({ id })`, stopped with `bash_kill({ id })` (`pi-bg-bash/README.md:60-75`).
Do not compose: no `subagent({ workflow: true })`, no `runs.run`/`runs.all`, no top-level `chain`/`tasks`, no cross-layer script (`pi-subagents/docs/tool-reference.md:13`; `AGENTS.yaml:1801`).
Do not poll: no `bg_wait`, no `sleep` (`pi-subagents/skills/pi-subagents/SKILL.md:73-77`; `AGENTS.yaml:2004`).
Leave `asyncByDefault` at its default; it only governs the legacy single-run primitive and workflow script calls (`pi-subagents/docs/configuration.md:239-245`).

## Sources

Local packages (read from disk, 2026-10-22):
`/home/z/.pi/agent/npm/node_modules/pi-subagents` 0.80.0: `README.md`, `package.json`, `docs/{tool-reference,agents,configuration,standalone-background}.md`, `skills/pi-subagents/SKILL.md`, `skills/pi-subagents/references/{execution-controls,constraints-and-recipes}.md`, `agents/{reviewer,worker,manager}.md`, `src/extension/schemas.js`, `src/runs/shared/child-tool-plan.js`.
`/home/z/.pi/agent/npm/node_modules/pi-bg-bash` 0.4.1: `README.md`, `package.json`, `CHANGELOG.md`, `src/{index,launch,foreground,notify,registry}.ts`.
Pi host 1.3.0: `/home/z/.local/share/fnm/node-versions/v24.18.1/installation/lib/node_modules/@earendil-works/pi-coding-agent/{docs/cli.md,docs/extensions.md,dist/core/tools/bash.d.ts,dist/core/tools/bash.js}`.
Project rule: `AGENTS.yaml:1789-1808`, `agents/manager.md:241-246`, `tools/law.py:203-208`.

Registry queries (`npm`, run 2026-10-22):
`npm view pi-background-tasks version description dist-tags time.modified repository.url` -> 2.6.10, ISC, `github.com/ismailsaleekh/pi-background-tasks`, modified 2026-10-13.
`npm view pi-bg-tasks version description` -> 0.1.4, `github.com/cyzlmh/pi-extensions`.
`npm view pi-subagents version` -> 0.80.0. `npm view pi-bg-bash version` -> 0.4.1.
`npm view @earendil-works/pi-coding-agent version time.modified` -> 1.4.0, modified 2026-10-21.
`npm view pi-background-tasks readme` and `npm pack pi-background-tasks@2.6.10` produced the third-party README, `docs/tools/bg_delegate.md` and `src/core/delegate/types.ts` cited above (read from `/tmp/pbt/package`).
Raw GitHub fetch of the same README timed out, so the registry copies are the primary channel used for that package; no third-party source was executed.

Absence checks, with counts:
`ls /home/z/.pi/agent/npm/node_modules | grep -ci background` -> 0 (no `pi-background-tasks` installed).
`grep -rl "bash_tasks" <pi 1.3.0 package>` -> 0 files of 14984; `grep -rl "bash_output" <same>` -> 0.
`grep -rl "bash_tasks" <pi 1.4.0 package>` -> 0 files of 1279; `grep -c background dist/core/tools/bash.d.ts` -> 0.
`grep -n -- "--agent" <pi docs/cli.md>` -> 0 matches.
`grep -rl createBashTool /tmp/pbt/package/{src,extensions}` -> 0 files; `grep -rn "name: 'bash'" /tmp/pbt/package/{src,extensions}` -> 1 hit, a type union at `src/core/common.ts:1011`, so no bash tool replacement.

## What stayed unverified

`pi-background-tasks` runtime behavior: not installed and not executed; every claim about it is from its published README, shipped docs and source, which is the vendor's own account.
Which extension wins a `/bg` command collision, and whether the two packages' footer status keys collide, was not tested; both document `/bg`.
Whether a `pi-bg-bash` task started inside a `pi-subagents` background child works end to end (log directory, watcher, completion) is inference from `pi-subagents/docs/agents.md:522`, not a run.
Pi 1.4.0 was checked for the bash tool contract and for the absence of `bash_tasks` anywhere in the package; its changelog and its other new features were not read.
Cost, token and latency differences between one async `subagent` child and one `pi --print` child were not measured; the report makes no performance claim.
Telemetry from `npm view` timestamps is as the registry reports it and was not cross-checked against the repositories' release tags.
This file is the only path this run added; it is evidence for one decision and can be folded into the roadmap or removed once that decision is recorded.
