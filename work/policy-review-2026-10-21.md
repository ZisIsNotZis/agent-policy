# 从 2026-10-21 那次 root 会话看，这套法该怎么改

输入：`/home/z/.pi/agent/sessions/--home-z-vibe--/2026-10-21T12-58-56-240Z_01a15e8b-176f-7254-999a-5854fa096a4b.jsonl`，232 行，我全读了。下文的行号是文件行号，用 `sed -n 'Np' <该路径>` 就能打开那一行；引用都是该行里的原文片段，不是我对会话气氛的转述。

那次会话的真实结果是三件事：三个提交（`86f0224`、`623e6d8`、`32fd189`）、十份经理契约**写好了但一份都没发出去**、那个人打断两次（`128` 行 "no, do not create node role"、`198` 行 "pause"）。

## 0. 先说一个前提事实，它决定下面所有"支付"怎么算

`law/ceiling` 写的是 `words 0` 与 `prohibitions 62`（`sed -n '221p'`），但**仓库里没有任何命令算这个词数**：`grep -n words tools/*.py` 只命中 `banned_words`，`tools/law.py:62-66` 的 `ceiling()` 只读 `prohibitions` 行。也就是说"法正好用满字数"是一个声明，不是被检查的事实；那次会话的根也只能猜它的意思（`sed -n '223p'`：says words 0 — meaning zero words available? … suggests the ceiling is reached exactly）。我自己也是从这句话猜的，我的契约里写着"0 words free"。

所以下面每条支付我都写口径：`wc -w`，只数该规则 `_when`/`_goal`/`_how` 的英文；删一条算整条三段，改一条只算被改的那段。这是提案，不是验证。四条加起来净 －53 词，不是"刚好抵平"。

## 1. 提案一：一份没人运行的检查不是检查

**错误类与机制.** 法说契约缺一项就不许派出（`dispatch.contract_fields` 的 `_how` 末句 "with one missing, do not dispatch"），但唯一能拒绝契约的机器 `tools/contract.py` 没有被任何入口调用：`grep -rn 'contract\.py' --exclude-dir=.git .` 除它自己外 **0 处**，`tools/check.sh` 只调 `law.py` 与 `build.py`。于是那次会话里唯一拒绝契约的机器是传输层，它按字节拒绝，不按字段——三次同一句 `tasks input exceeds 16384 bytes.`。让这种错误写得出来的机制是 `change.coverage_check`：它把"机器检查的三件事"写成一句枚举（scope、渲染一致、可达），而不是扫目录；`tools/` 下多出一个工具、且不被任何入口调用，没有任何检查会红。`tools/check.sh` 自己的注释说 "One entry point for every check this repository makes"，这句话同样没有东西验证。

**证据.**
- `sed -n '227p'`：那次真实派出的契约全文，2081 字节（`task` 字段）。我用仓库自己的 linter 跑它：`python3 tools/contract.py --check <抽出的契约>` → 退出码 1，五条 FAIL（`boundary`/`area`/`acceptance`/`report target`/`wall-clock`），只有 `spend` 过。
- `sed -n '188p;192p;196p'`：三次 `tasks input exceeds 16384 bytes.`；`sed -n '194p'`：根用估算代替测量——each task ~1.6KB × 10 = 16KB+。
- 仓库侧：`git log --oneline -1 -- tools/contract.py` → `aabcde6 tools: a contract linter, because nobody was checking the dispatcher`。提交信息自己说出了错误类，而 linter 到今天仍然没人调。

**梯级.** 检查（拒绝 + 自动运行），两处落点。
(a) `tools/law.py --check` 增一条：`tools/` 下任何接受 `--check` 的脚本若不在 `tools/check.sh` 里被调用，即 FAIL。这样"一个没人运行的检查"写不出来。
(b) `dispatch.contract_fields` 点名那个命令，并让它打印字节数：作者量一次，而不是猜两次。

顺带必须杀掉的第二个家：linter 现在的字段名（boundary/area/acceptance/report target/wall-clock）和法里的六个字段（goal/scope/accept+command/paths/spend+wall-clock/stop）不是同一套，同一个东西两个家。linter 改成法的六个字段，旧字段名按 `laws.kill` 一起死；改完后它对 `227` 行那份契约只该剩一条 FAIL：`accept` 没有命令。（这一条是推断，来自两份文本的对照，我没跑改后的 linter。）

**支付.** 删掉 `dispatch.contract_inheritance` 整条：
`_when: You write a contract` / `_goal: The contract does not restate what the child already reads` / `_how: Cite the rule by name when it must hold, and name the one suspended for this package`
它的前半是 `laws.inferable` 的重复；后半（点名被暂停的那一条）并入 `contract_fields` 的清单。
新 `_how`：`Six lines: goal, scope, accept with its command, paths, spend with wall-clock, stop, and the one rule suspended for this package; run `python3 tools/contract.py --check` on the composed text, send nothing it refuses, and read the byte count it prints`
算术：19 → 40，＋21；删 31；净 **－10**。

## 2. 提案二：引用法的句子先解析，`kill` 的搜索要说出搜哪些树

**错误类与机制.** 一条已经死掉的名字活在"引用了法的文档"里，最后发现它的人是那个人。机制有两层：`laws.kill` 要求"把旧名字搜一遍、搜不到才算完"，但从不说搜哪些树，而法自己的检查只读本仓库——引用它的文档在上一层（workspace 根），不在任何一次搜索里；`upkeep.resolvable` 又只写 "resolve it against what exists"，这是目标句不是步骤，完成与否看不出来，作者读成了建议。于是那个根已经把 `.pi/agents/node.md` 当成"要先创建的东西"了。

**证据.**
- `sed -n '86p'`：grep 输出里有 `docs/plan/portfolio.md:34:`node` is that agent, defined at `.pi/agents/node.md``，而那个文件**从未存在过**。
- `sed -n '66p'`：根的想法原文 "I need to create the node agent definition before dispatching"——它准备按一份陈旧文档造出一个法里没有的角色。
- `sed -n '128p'`：那个人的纠正 "no, do not create node role, our rule has updated, stick to latest rule"。
- 对照在同一文件里：`portfolio.md` 的另一条不变量有机器在管（`tools/scope.py`），`sed -n '172p'` 是它一秒内的 FAIL，根当场改掉。两处差别只有一个：有没有机器在读那条性质。

**梯级.** 判定标准（写的人自己应用）＋步骤带命令。上限我照实说：检查梯级在这个仓库够不着，因为引用文档不在本仓库，`law.py --check` 看不到它。这是残留缺口，不是我打到了最高一级。

**支付.** 删掉 `records.every_fact_has_a_home` 整条：
`_when: You have a fact` / `_goal: It is in a file, not in a conversation` / `_how: Write it into the document that owns the decision`
它的行动句是 `laws.ssot` 行动句的真子集。
改两处：`upkeep.resolvable` 的 `_how` → `A path, a heading, a command; run `ls` on it, and write nothing that does not resolve`（11 → 17，＋6）；`laws.kill` 的 `_how` 末尾 → `Kill the sentence, the identifier, the config key, the fixture and the file name in the same act; the evidence is a search for every name it had, under every tree that reads the law, returning nothing`（30 → 37，＋7）。
算术：＋13 删 22；净 **－9**。

## 3. 提案三：报告里"现在存在什么"是命令打印的那一行，不是一句断言

**错误类与机制.** 报告里的一句断言被同一轮的输出否掉，而没有人再读一遍。机制：`delivery.completion_proof` 的第三项 "what exists now" 没有形状，散文就满足了；`principles.true_because_checked` 说"你叫它真，得有检查这么说"，但没有任何报告字段要求把检查的那一行带上来。同一个缺陷也在 `speech.report_fields` 的 "an evidence pointer" 上：它指向命令，不指向命令的输出。

**证据.**
- `sed -n '184p'`：git 输出原文含 `? local_lm_research`、`? nomos`、` M pathlm`——三处都没钉住。
- `sed -n '212p'`：同一轮的报告说 "submodule pointers pinned at the state the managers would have started from"。
两行相隔不到一分钟，断言与输出直接矛盾。

**梯级.** 形式：第三项写不成断言，只能是命令打印的那一行。

**支付.** 删掉 `speech.completion` 整条：
`_when: You finish` / `_goal: It is a report whose decision is none` / `_how: Report it with an evidence pointer`
它被 `speech.report_fields` 覆盖（decision may be none ＋ evidence pointer）。
改 `delivery.completion_proof` 的 `_how` → `Five: the end as given, whether it changed and to what, what exists now as the line the command printed, the command itself, and which review passed it`（24 → 28，＋4）。
算术：＋4 删 16；净 **－12**。

## 4. 提案四：字数上限是一个没人算的数

**错误类与机制.** 这条是给上面三条托底的。法最贵的那个约束——加一句必须删一句——没有执行者：`laws.derived` 说派生的值不许存、要存产生它的命令，而 `law/ceiling` 存的正是派生值（`words 0`），没有任何命令产生它。后果可以直接验：往语料里加词，`sh tools/check.sh` 照样 `ok`。那次会话的根和我都只能猜这个数的意思。

**证据.**
- `sed -n '221p'`：`cat law/ceiling` 的输出 `words 0` / `prohibitions 62`；`sed -n '223p'`：根在猜（"meaning zero words available?"）。
- 仓库侧：`grep -n words tools/*.py` 只命中 `banned_words`；`ceiling()` 只解析 `prohibitions` 行。

**梯级.** 检查：`law.py --check` 数 root 视图的词，与 `law/ceiling` 里的上限比，超了就拒绝；文件里存上限，"还剩多少"变成命令的输出而不是一个人写在文件里的数。

**支付.** 删掉 `scheduling.no_long_in_turn` 整条：
`_when: You are about to run something that takes minutes` / `_goal: The turn stays interruptible` / `_how: Keep it out of the turn: give it a timeout, or detach it behind a named log`
它与 `scheduling.steerable` 是同一个动作、同一句例子，而 `steerable` 多一句它没有的内容（write the naming state first），所以死的是没有独有信息的那条。
语料里只动一句：`change.coverage_check` 的 `_how` → `Every rule declares a scope, every render matches, no rule reaches nobody, and the word count stays inside the ceiling`（12 → 20，＋8）。
算术：＋8 删 30；净 **－22**。

## 5. 我不提的，和为什么

- **不把 `node` 加进 lexicon 的禁用词表。** 会立刻把法自己判红：`\bnode\b` 在法文本里有 4 条合法使用（`take_next`、`intake`、`plan_tree`、`announce_long`），而检查是对全部规则文本做正则。lexicon 现在用散文写 "Node names a point in a roadmap graph and nothing else" 是对的形态。这次的错不在词，在那个路径（提案二）。
- **不为"根照文档造角色"单独立一条规则。** 单次事件，类已被 `source order` 与 `ssot` 覆盖；提案二的步骤正是它会触发的机制。为一次事故收一条规则，就是把事故抄进法里。
- **不把 16384 字节写进法里。** 那是工具的数，会变；`laws.derived` 不许把别处的数抄进来。提案一让契约有形状、让 linter 报字节，作者量而不猜。
- **不设并发上限。** 那次会话里没有一个子代理真正跑起来，失败全在载荷上，不在并发上。没有证据。
- **不提 provider 失败、不提 `pi models` 猜命令。** 一个是环境，一个是单次误用，都不是法。
- **不提"pause 之后要把状态写下来"。** 已经做到了，而且是那次会话做得最好的一处：三个提交、报告写明"十份契约写了但没有一份发出"、并列出三处它没有碰的缺口。这一处法是有效的，留着当对照。

## 6. 残留风险

1. 我的支付算术用 `wc -w` 且只数英文；仓库里没有命令定义"词"。这四个"净减"是提案的记账，不是验证过的数（提案四正是要让第一个数成为可算的）。
2. 提案一(b) 把 `tools/contract.py` 这个路径写进法里，是一个实现细节进语料；linter 改名，法就错。替代是写命令名而不是路径，我选了路径，因为作者能 `ls` 它——这和提案二是同一条纪律。
3. 提案二的检查梯级够不着外层文档，那个人仍可能再当一次检查器。
4. 我只读了这一个 session 和本仓库，没读 `/home/z/vibe` 的任何项目目录；所有关于 workspace 的断言都来自会话里的输出，不是我自己看到的。
