[English](README.md) | 简体中文

<p align="center">
  <img src="assets/logo.svg" width="88" height="88" alt="agent-policy 标志">
</p>

<h1 align="center">agent-policy</h1>

<p align="center"><strong>由自主智能体运行项目的工作法则。</strong></p>

一份手工维护的 `LAW.md`，定义 Communicator、递归 Manager 与 Worker 如何承担结果、委派工作、持续学习、验证质量并进行沟通。用户可以随时回来参与，但项目不能依赖用户一直在线。目标不是增加流程或消息，而是建立持续的责任归属、优秀的成果、安静的运行方式和可靠的交接。

## 快速开始

需要 Python 3。渲染器面向 Pi 全局 Agent 环境，默认将生成的角色指令安装到 `~/.agents/`。

```sh
git clone https://github.com/ZisIsNotZis/agent-policy.git
cd agent-policy
python3 tools/render.py
python3 tools/render.py --install --install-dir ~/.pi/agent
```

使用 `--out PATH` 指定构建目录，或使用 `--install-dir PATH` 指定安装目录。上面的安装命令面向 Pi 的全局 Agent 目录。为保持兼容，单独使用 `--install` 时仍默认安装到 `~/.agents/`；安装到 Pi 时请明确指定 `~/.pi/agent`。安装会合并生成文件，不会删除目标目录中的无关文件。安装到现有 Agent 环境前，请先检查生成的角色指令。

如需 Pi 递归委派，请按照 [runtime/PI_SUBAGENTS_CONFIGURATION.md](runtime/PI_SUBAGENTS_CONFIGURATION.md) 配置并验证 `pi-subagents` 扩展及其运行时深度保护。Manager 和 Worker 定义不设置任意执行期限。策略文本本身无法加载扩展或授予运行时权限。

## 功能

- **单一事实来源。** `LAW.md` 是手工维护的最高层组织行为策略。
- **三个角色视图。** Communicator 是唯一面向用户的接口；Manager 递归管理各自范围；Worker 负责边界明确的工作包。
- **自主持续推进。** 只要目标已有足够清晰的轮廓即可开始。用户参与完全可选；每次真正等待用户输入都必须有超时和安全默认动作。
- **安静沟通。** 不进行例行打扰或过程播报。只有对相应上级或用户真正有用的最终消息才向外发送。
- **目标忠实与抽象分层。** 每一层都保护用户真正要求的能力，防止执行漂移成代理任务。Manager 向上翻译成结果层面的语言；实现细节留在负责该细节的层级。
- **递归升级与学习。** 上级过滤过早升级的问题；每一层都诊断根因，并改进成果、自身指令、委派方式、检查机制和工作方法。
- **质量与验证。** 根据目标和证据判断是否完成，而不是根据活动量或看似合理的产物。
- **技能与模板。** 通过按需加载的操作手册和标准记录，让核心法则保持聚焦。

## 架构

```text
                         用户
                          │
                    Communicator
               （用户回来时轮询；
                 仅紧急情况主动唤醒）
                          │
                     根 Manager
                      （树根）
                     /       \
                 Manager    Worker
                 /    \
             Manager  Worker
                │
              Worker
```

每棵树都从用户选定的范围独立建立，并由用户通过 Communicator 明确提供目标。一个管理树可以负责一个需要整合的结果，也可以负责多个共享主题的独立结果。子 Manager 的工作目录不必位于父 Manager 的目录之下；真正定义所有权的是管理范围与权限。不同树彼此独立。

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| `LAW.md` | 权威行为策略及带角色标签的源文件。 |
| `agent-policy-skills/` | 按需加载的操作手册。 |
| `templates/` | Goal、Plan、State、Handoff、Intent、User Model 和 Decision Packet 模板。 |
| `tools/render.py` | 生成角色指令并安装完整构建结果。 |
| `tools/lint_policy.py` | 角色标签解析与参考检查工具。 |
| `tools/test_bundle.py` | Bundle 结构检查。 |
| `evals/` | 用于测试已部署 Agent 行为的场景。 |
| `runtime/` | Harness 集成契约及 Pi 子 Agent 配置说明。 |
| `MIGRATION_NOTES.md` | 版本变更原因与迁移历史。 |
| `build/` | 生成的安装文件；不要手工编辑。 |
| `rendered/` | 参考角色视图；应从 `LAW.md` 重新生成。 |
| `assets/logo.svg` | README 标志。 |
| `README.md` | 英文版说明。 |

## 开发与验证

编辑 `LAW.md` 以及相关技能或模板，然后运行渲染和验证：

```sh
python3 tools/render.py
python3 tools/lint_policy.py LAW.md --out /tmp/agent-policy-lint
python3 tools/test_bundle.py
```

生产渲染器负责生成实际角色视图。Linter 只是参考检查，不能代替检查最终指令或在 Pi 中测试。递归子 Agent 启动、无任意子 Agent 执行期限、异步恢复和事件投递等运行时能力，都必须在实际 Harness 中验证。

## 贡献

应修改源法则，而不是手工编辑生成视图。若改动解决了反复出现的行为问题，应增加对应的行为场景测试。英文 README 更新时，也应同步更新简体中文版。完成上述检查，并在目标 Harness 中测试重要行为后，才能声称该行为已得到实际执行保障。

## 许可证

MIT。请参阅 [LICENSE](LICENSE)。
