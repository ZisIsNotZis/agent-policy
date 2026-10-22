# Migration spec

One-to-one. Every rule in `AGENTS.yaml` appears once in `AGENTS.next.yaml`, in the new shape. No merge, no delete, no add. Anything that needs one goes in a `needs-decision` list; it is not done here.

Read first: `AGENTS.schema.yaml` (the shape), `AGENTS.next.yaml` (31 migrated rules as the model), the sections you are given in `AGENTS.yaml`, `tools/schema.py` (the check).

## Shape

```yaml
key:
  _when: 一句话，例外写在句子里
  _know: 做这个决定前该有数的事实；具体的（在哪、谁读、多久变、能不能回头），不是比喻
  _scope: [roles]
  _choices:
    - move: 一段长的 SOP 动作（做什么、在哪、按什么顺序）
      gain: 这个动作单独买到什么
      cost: 这个动作单独付出什么；付款人不是人时写出来
  _goal: 理想态，用程度（少一些、低一些、相称）；不写方法；不写零、没有、绝不；不列资源清单
```

`_why` and `_depends_on` are omitted here; the links pass owns them.

`_scope`: copy the old scope exactly. The old `policy` becomes both `policy_writer` and `policy_reviewer`.

## The two tests

- **no-op**: delete the sentence. Does the agent lose a decision? If not, it is filler.
- **decoy**: would a competent agent ever pick this choice in some real situation? If not, it is fake. Find the real alternative, or put the rule in `needs-decision`.

Every choice must be a full answer to the same question; they need not be orthogonal, only plausible.

## Examples

A balance, `ssot` (in `AGENTS.next.yaml`): one fact, three ways to keep it — one home, two with the source marked, a pointer.

An act, `reproduce_minimize`:

```yaml
reproduce_minimize:
  _when: 你要复现一个缺陷
  _know: 原始场景里哪些输入是必需的；哪些配置和版本参与；哪个输出确实是错的
  _scope: [worker]
  _choices:
    - move: 记下脱敏输入、配置、版本和确实错的输出，一次减一样，直到再减症状就消失
      gain: 输入最小，原因的范围跟着缩小
      cost: 每减一样都要重跑，减到最小要花时间
    - move: 在原始场景上直接复现，不做削减
      gain: 快，场景是真的
      cost: 输入太大，原因藏在很多变量里，别人难重跑
    - move: 用最少的猜测搭一个假场景
      gain: 快，可控
      cost: 它可能不是原来的缺陷，修好了原场景还在
  _goal: 别人拿你记下的东西能重跑出同一个症状，且变量少到能指向原因
```

Another act, `design`:

```yaml
design:
  _when: 你要定一个接口
  _know: 谁会调用它；他们的场景；哪些会变；哪些错误必须被看见
  _scope: [worker]
  _choices:
    - move: 按调用场景和变更局部性定边界，把类型、不变量、顺序、配置、错误模式和可依赖的性能写进接口
      gain: 调用方知道该知道的一切，附带复杂度被藏起来
      cost: 定边界要花时间，猜错的场景会把接缝放错地方
    - move: 先把内部结构暴露出来，让调用方自己取
      gain: 现在快，不用设计
      cost: 调用方依赖内部，改一次要动所有人
    - move: 只写一个最小签名，其余留给实现
      gain: 小，好改
      cost: 调用方要猜错误模式和顺序，猜错就在运行时发现
  _goal: 调用方按接口就能写对，改内部时他们不用动
```

## Things to notice

- Keep the old meaning. The migration is not the place to improve the rule.
- A balance's `_ends`, `_between` and `_pull` fold into `_choices` and `_goal`. The band's action becomes the first choice; the pull's direction becomes why one choice's cost is heavier, written in that choice's cost.
- An act's `_how` becomes the first choice, spelled out as a specific action. The second choice is the real alternative that was rejected: skip it, do it later, do it another way, or do it by hand. If no real alternative exists, `needs-decision`.
- Do not write a choice that only makes sense as a step of another choice. One choice, one action.
- `_know` asks for facts the agent can have an impression of from the context; it is not an investigation order.

## Output

Write one flat YAML file per group, `migrations/<group>.yaml`. Validate it with `python3 tools/schema.py migrations/<group>.yaml`. Return the validation line and the `needs-decision` list; write nothing else.
