English | [简体中文](README.zh-CN.md)

<p align="center">
  <img src="assets/logo.svg" width="88" height="88" alt="agent-policy logo">
</p>

<h1 align="center">agent-policy</h1>

<p align="center"><strong>The working law for projects run by autonomous agents.</strong></p>

One hand-written `LAW.md` defines how the Communicator, recursive Managers, and Workers own outcomes, delegate, learn, verify, and communicate. The user can drop in at any time, but the project must not depend on the user staying present. The aim is not more process or more messages: it is durable ownership, excellent outcomes, quiet operation, and reliable handoffs.

## Quick start

Requires Python 3. The renderer builds role views for Pi. Its generic install default is `~/.agents/`; use the Pi-specific install target shown below for Pi global agents.

```sh
git clone https://github.com/ZisIsNotZis/agent-policy.git
cd agent-policy
python3 tools/render.py
python3 tools/render.py --install --install-dir ~/.pi/agent
```

Use `--out PATH` to choose a build directory, or `--install-dir PATH` to choose the installation directory. The install command above targets Pi's global agent directory. For compatibility, bare `--install` still defaults to `~/.agents/`; choose `~/.pi/agent` explicitly when installing into Pi. Installation merges generated files; it does not remove unrelated files. Review the generated role views before installing them into an existing agent environment.

For recursive Pi delegation, configure and verify the `pi-subagents` extension, its finite depth guard, and a longer finite execution timeout as described in [runtime/PI_SUBAGENTS_CONFIGURATION.md](runtime/PI_SUBAGENTS_CONFIGURATION.md). The policy cannot load or authorize a harness extension on its own.

## What it does

- **One source of truth.** `LAW.md` is the hand-written governing policy.
- **Three role views.** The Communicator is the only user-facing interface; Managers recursively own scopes; Workers own bounded work packages.
- **Autonomous continuity.** A sufficiently clear Goal is enough to start. User participation is optional; every genuine wait has a timeout and a safe default.
- **Quiet communication.** No routine check-ins or progress narration. Only material, useful final messages reach the relevant parent or user.
- **Recursive escalation and learning.** Parents filter premature escalations; every level improves both its outputs and its own working method from errors, warnings, checks, reviews, and feedback.
- **Quality and verification.** Completion is judged against outcomes and evidence, not activity or plausible-looking artifacts.
- **Skills and templates.** Detailed playbooks and standard records keep the core law focused.

## Architecture

```text
                         User
                           │
                    Communicator
                 (poll on user return;
                  rare urgent wake-up)
                           │
                     Root Manager
                     (tree root)
                     /         \
              Manager         Worker
              /    \
          Manager  Worker
             │
           Worker
```

Each tree is independently rooted at a user-selected scope and receives an explicit Goal through its Communicator. A tree may own one integrated outcome or several distinct outcomes under a shared theme. A child Manager's CWD need not be nested under its parent's CWD; managed scope and authority define ownership. Separate trees are independent.

## Repository map

| Path | Purpose |
| --- | --- |
| `LAW.md` | Authoritative behavioral policy and role-tagged source. |
| `agent-policy-skills/` | On-demand procedural playbooks. |
| `templates/` | Goal, plan, state, handoff, intent, user-model, and decision-packet records. |
| `tools/render.py` | Builds role-specific instructions and installs the completed build. |
| `tools/lint_policy.py` | Reference role-tag parser/linter. |
| `tools/test_bundle.py` | Structural bundle checks. |
| `evals/` | Behavioral scenarios for testing the deployed agents. |
| `runtime/` | Harness integration contracts and Pi subagent configuration guidance. |
| `MIGRATION_NOTES.md` | Versioned rationale and migration history. |
| `build/` | Generated installation output; do not hand-edit. |
| `rendered/` | Reference rendered views; regenerate from `LAW.md`. |
| `assets/logo.svg` | README mark. |
| `README.zh-CN.md` | Simplified Chinese version of this README. |

## Develop and validate

Edit `LAW.md` and any relevant skill/template, then render and validate:

```sh
python3 tools/render.py
python3 tools/lint_policy.py LAW.md --out /tmp/agent-policy-lint
python3 tools/test_bundle.py
```

The production renderer is responsible for the actual role views. The linter is a reference check, not a substitute for inspecting the rendered instructions or testing them in Pi. Runtime capabilities—including nested subagent launch, finite execution timeouts, asynchronous recovery, and event delivery—must be verified in the actual harness.

## Contributing

Change the governing law rather than editing generated views. Add a behavioral scenario when a change addresses a recurring failure mode. Update the Simplified Chinese README when the English README changes. Run the checks above and test consequential behavior in the target harness before claiming it is enforced.

## License

MIT. See [LICENSE](LICENSE).
