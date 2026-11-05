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
    ("timeoutMs", "7200000"),  # 2 hours; finite, not unlimited
)
```

The generated Manager definition includes `timeoutMs = 7200000` (two hours) as a finite starting point. In current `pi-subagents`, `timeoutMs` is a positive integer in milliseconds. A global default can also be set in `~/.pi/agent/extensions/subagent/config.json`:

```json
{
  "timeoutMs": 7200000
}
```

The extension documents a 30-minute default for applicable foreground and plain single-agent async runs. The global setting replaces that default when no call-level timeout applies; a selected agent's own `timeoutMs` frontmatter can take precedence. Set the Manager definition's `timeoutMs` too if it declares its own shorter default. This is a run deadline, not a guarantee that the model can answer: Pi's separate `httpIdleTimeoutMs` defaults to five minutes and may also need adjustment for unusually slow local model responses. Keep all timeouts finite, but long enough for legitimate work and recovery/checkpointing.

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
6. A long-running delegated task survives beyond the former 30-minute default when the configured finite timeout permits it.
7. Parent and child can inspect durable run state/output and recover after interruption.

These generated fields and environment settings configure the harness; LAW defines the organizational requirement. A policy statement cannot load an extension, grant a tool, or change a process timeout by itself.
