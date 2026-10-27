English | [简体中文](README.zh-CN.md)

<p align="center">
  <img src="assets/logo.svg" width="88" height="88" alt="agent-policy logo">
</p>

<h1 align="center">agent-policy</h1>

<p align="center"><strong>The working law for projects run by agents.</strong></p>

One hand-written `LAW.md` becomes every role's instructions: the manager who owns the Goal, route, review and release, and the worker who owns architecture, contracts, detail and shipping. The point is not more process. It is one home for the route, so a project can change hands without losing what it is doing or why.

## Quick start

Requires Python 3 and a POSIX shell. The install step targets the pi agent harness.

```sh
git clone https://github.com/ZisIsNotZis/agent-policy.git
cd agent-policy
sh tools/install-agents.sh
sh tools/check.sh
```

`install-agents.sh` links `~/.pi/agent/agents` at this checkout, links the global `AGENTS.md` at `manager.md`, and sets the repository's pre-commit hook. `check.sh` fails if a rendered view is stale.

## What it can do now

- **One source.** `LAW.md` is the only file edited by hand.
- **Role views.** Tags such as `@manager` and `@worker` split one law into the instructions each role receives.
- **Render and check.** `tools/render.py` writes the views; `tools/check.sh` fails on a stale one.
- **Install in one step.** The harness gets links rather than copies, so a law edit reaches every role.
- **Pre-commit guard.** A commit that stages the law, a banned term or the renderer regenerates and stages the views.
- **No runtime.** This repository is the law and the scripts around it, not a framework, service or CLI.

## Architecture

```text
LAW.md ──tools/render.py──> agents/manager.md  (agent definition)
                         └> manager.md         (global context)
                                      │
                         tools/install-agents.sh
                                      ▼
                         ~/.pi/agent/agents -> agents/
                         ~/.pi/agent/AGENTS.md -> manager.md
```

`LAW.md` is hand-written. Everything under `agents/` and `manager.md` is generated and marked as such; edit the law, not the views. `banned.txt` holds terms that pull writing into the wrong frame.

| Path | Role |
| --- | --- |
| `LAW.md` | The law: one chain from the pain to the release. |
| `banned.txt` | Words the law replaces with its own terms. |
| `tools/render.py` | Renders role views from tagged sections and blocks. |
| `tools/check.sh` | Fails if a view on disk differs from the law. |
| `tools/install-agents.sh` | Links the views into the harness and enables the hook. |
| `agents/`, `manager.md` | Generated views. Do not edit. |

## Develop

Edit `LAW.md`, then render:

```sh
python3 tools/render.py
sh tools/check.sh
```

The pre-commit hook does the same when a relevant file is staged. Enable it once per clone with:

```sh
git config core.hooksPath .githooks
```

## Status

**Implemented**

- The nine-link chain, the Goal confirm, the route, the review and the release pass.
- Role-tagged sections and blocks, generated into manager and worker views.
- Link-based install and a stale-view check.
- The law is in use as the policy submodule of [auto-dead-serious](https://github.com/ZisIsNotZis/auto-dead-serious).

**Planned**

No public roadmap is recorded. The law changes when a project hits a gap it cannot answer; that gap is the next change. Open an issue with the case and the evidence.

## Future vision

A project should be able to change hands without losing the thread: one readable law, one route, one place where the Goal, the review and the release live. The views stay thin, the law stays small, and every addition must earn its place by making a real hand-off clearer.

## Contributing

Read `LAW.md` first. Keep the change small, keep one home for each fact, and edit the law rather than a generated view. Run `sh tools/check.sh` before opening a pull request. Issues and pull requests are welcome; include the case, the evidence and the check that settles it.

## License

MIT. See [LICENSE](LICENSE).
