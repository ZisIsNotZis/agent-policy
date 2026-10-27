[English](README.md) | 简体中文

<p align="center">
  <img src="assets/logo.svg" width="88" height="88" alt="agent-policy logo">
</p>

<h1 align="center">agent-policy</h1>

<p align="center"><strong>给由智能体推进的项目的一份工作法。</strong></p>

一份手写的 `LAW.md`，会成为每个角色的指令：经理拥有目标、路线、评审与发布，工人拥有架构、契约、细节与交付。重点不是增加流程，而是让路线只有一个家——项目换手时，不会丢掉它在做什么，也不会丢掉为什么。

## 快速开始

需要 Python 3 和 POSIX shell。安装步骤面向 pi agent harness。

```sh
git clone https://github.com/ZisIsNotZis/agent-policy.git
cd agent-policy
sh tools/install-agents.sh
sh tools/check.sh
```

`install-agents.sh` 会把 `~/.pi/agent/agents` 链接到这份代码，把全局 `AGENTS.md` 链接到 `manager.md`，并启用仓库的 pre-commit 钩子。两处都是链接，所以改一次法律就到达每个角色，不用重装。如果这两个路径上已经有真实文件，脚本会把它移到旁边（`~/.pi/agent/AGENTS.md.local`），不会删掉。装完可以用 `sh tools/install-agents.sh --check` 验证链接；`check.sh` 在渲染结果过期时失败。

## 现在能做什么

- **一个来源。** 只有 `LAW.md` 需要手写。
- **角色视图。** `@manager`、`@worker` 这类标记把同一份法律拆成每个角色实际收到的指令。
- **渲染与检查。** `tools/render.py` 写出视图；`tools/check.sh` 在视图过期时失败。
- **一步安装。** harness 拿到的是链接而不是副本，所以改一次法律，每个角色都会看到。
- **提交前守卫。** 提交法律、禁用词或渲染器时，钩子会重新渲染并暂存视图。
- **没有运行时。** 这个仓库是法律和它周围的脚本，不是框架、服务或 CLI。

## 结构

一份手写文件，一趟渲染，三个文件：先按角色标记解析法律，再把每个标记下的章节和段落收成视图；经理视图写两次——一次是角色定义，一次是 harness 的全局上下文文件。安装步骤只是把 harness 指过去，不往里拷任何东西，所以不存在会逐渐偏离的第二份副本。

```text
LAW.md ──tools/render.py──> agents/manager.md  （角色定义）
                         └> manager.md         （全局上下文）
                                      │
                         tools/install-agents.sh
                                      ▼
                         ~/.pi/agent/agents -> agents/
                         ~/.pi/agent/AGENTS.md -> manager.md
```

`LAW.md` 是手写的。`agents/` 和 `manager.md` 下的内容都是生成的，并带有生成标记；要改就改法律，不要改视图。`banned.txt` 收集会把写作带偏的词。

| 路径 | 作用 |
| --- | --- |
| `LAW.md` | 法律：从痛点到发布的同一条链。 |
| `banned.txt` | 法律用自己的词替换掉的词。 |
| `tools/render.py` | 从带角色标记的章节和段落渲染角色视图。 |
| `tools/check.sh` | 磁盘上的视图与法律不一致时失败。 |
| `tools/install-agents.sh` | 把视图链接进 harness，并启用钩子。 |
| `.githooks/pre-commit` | 提交源文件时重新渲染并暂存视图。 |
| `agents/`、`manager.md` | 生成的视图。不要手改。 |
| `assets/logo.svg` | 本页顶部用的标记。 |
| `README.zh-CN.md` | 本页的简体中文版。 |

## 开发

修改 `LAW.md`，然后渲染：

```sh
python3 tools/render.py
sh tools/check.sh
```

提交相关内容时，pre-commit 钩子会做同样的事。每个克隆启用一次：

```sh
git config core.hooksPath .githooks
```

除了这个过期检查，没有别的测试套件：渲染器很小，而它唯一的失败方式——磁盘上的视图和法律不再一致——正好就是 `check.sh` 观察到的东西。

## 贡献

先读 `LAW.md`，改法律而不改生成的视图，开 PR 前跑 `sh tools/check.sh`。范围、检查项，以及一次改动需要带上什么，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 路线图

**已实现**

- 九环链、目标确认、路线、评审和每次发布都会跑的收尾步骤。
- 按角色标记的章节和段落，渲染成经理与工人视图。
- 链接式安装和视图过期检查。
- 这份法律正作为 [auto-dead-serious](https://github.com/ZisIsNotZis/auto-dead-serious) 的策略子模块使用。

**未实现**

没有公开路线图。项目碰到法律答不出的缺口时，法律就改；那个缺口就是下一步。带上具体情形和证据开 issue。

### 未来

项目换手时应该还能接上原来的线：一份读得懂的法律，一条路线，一个同时放着目标、评审和发布的地方。视图保持薄，法律保持小；每一次增加，都要让真实的交接更清楚，否则就不加。

## 许可证

MIT，见 [LICENSE](LICENSE)。
