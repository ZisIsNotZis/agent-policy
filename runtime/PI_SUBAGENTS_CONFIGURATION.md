# Pi subagent configuration

The Manager's ability to delegate recursively depends on the Pi subagent extension being loaded, not merely on listing `subagent` as an available tool. The following configuration entries are generated directly into `build/agents/manager.md` by `tools/render.py`. They are not merely README advice; inspect the generated file after each build:

```python
(
    ("tools", "read, edit, write, bash, grep, find, ls, subagent"),
    # `subagent` is an extension tool: naming it in `tools` is a strict
    # allowlist entry and does NOT load the extension. Without the provider
    # below, nested launches can fail with "requested unavailable child tools:
    # subagent", silently reducing the Manager to a single-threaded agent.
    ("subagentOnlyExtensions", "npm:pi-subagents"),
    ("allowNestedSubagents", "true"),
)
```

Do **not** put `timeoutMs` in Manager or Worker frontmatter when the runtime supports an unbounded run, and do not set a global child-run deadline merely for administrative convenience. If a finite timeout is mandatory in the actual runtime, it MUST be at least seven days (`604800000` ms); a shorter hard limit that can terminate legitimate work is PANIC. Work ends when the responsibility is complete, explicitly stopped by its authority, or genuinely unable to proceed—not when an arbitrary session timer expires. Audit call sites and global configuration for accidental deadlines. A bounded parent wait is not a deadline that kills the child: a wait can expire while the durable child continues running.

Do not confuse the Communicator's response-wait timeout while servicing an active user turn with a Manager or project execution deadline. Nor should provider idle timeouts, process supervision, or infrastructure failure be described as a policy-sanctioned work limit. If the runtime cannot keep a Manager alive or recover its work, treat that as a mandatory-invariant failure (PANIC)—not a reason to rush, truncate responsibility, or manufacture a handoff. Never interrupt or relaunch an active Manager merely to change its timeout; establish actual process state and preserve its work first.

### Recursive depth compatibility

The current extension also has a runtime nesting-depth guard. Its documented default is two levels; `allowNestedSubagents: true` does not remove that guard. Set `PI_SUBAGENT_MAX_DEPTH` before starting Pi to a deliberately high finite value (for example `64`) and do not add a smaller per-agent `maxSubagentDepth` frontmatter value to Manager definitions:

```sh
export PI_SUBAGENT_MAX_DEPTH=64
```

This is a compatibility workaround for the extension's finite depth guard, not a policy-level hierarchy limit. The current extension documentation does not describe an unlimited-depth setting; if the organization must exceed the configured runtime value, the extension/runtime must be changed. Do not set `PI_SUBAGENT_MAX_DEPTH=0`: the current documentation describes that value as disabling nested subagent availability, not as unlimited depth. Verify this behavior against the exact installed version.

Official references: [Pi subagent agent-definition fields](https://github.com/nicobailon/pi-subagents/blob/main/docs/agents.md), [Pi subagent configuration](https://github.com/nicobailon/pi-subagents/blob/main/docs/configuration.md), and [workflow recursion guard](https://github.com/nicobailon/pi-subagents/blob/main/docs/workflows.md).

After changing configuration, verify all of the following in the actual harness:

1. The `pi-subagents` extension is installed and loaded.
2. `subagent` is available to the Manager under the configured tool allowlist.
3. A Manager can launch a child Manager, and that child can launch its own child when its assignment requires it.
4. Child launch receives the intended role, assignment, CWD, and scope.
5. A nested launch succeeds beyond the extension's default two-level depth, and a further nested launch succeeds up to the configured finite depth.
6. A long-running delegated task continues without an arbitrary child deadline; separately verify that bounded parent waits do not terminate the durable child.
7. Parent and child can inspect durable run state/output and recover after interruption.

These generated fields and environment settings configure the harness; LAW defines the organizational requirement. A policy statement cannot load an extension, grant a tool, or change a process timeout by itself.
