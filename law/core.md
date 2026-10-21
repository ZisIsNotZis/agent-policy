# Law

A node is one agent, one directory, one document. The document holds only what this node's own decisions need; everything else stays where it is and is read when it is needed.

## Structure

A node splits its work or executes it. Splitting creates child nodes, each with its own directory, its own document and its own roadmap. How a node splits is its own decision, and no layer above it may dictate the split.

A roadmap holds milestones, work packages and child nodes. A milestone is a point the node must report to the layer above. A work package is a unit it executes without reporting. A child node is a node it created and does not execute. A node lives exactly as long as its roadmap.

A node whose entries are children and whose roadmap holds one milestone is a container. It advances several children in parallel, holds nothing of their internal state, and reports once, when they are all done.

A node may execute and may also split. What it may not do is split, and then execute the piece it just split off.

Everything about a node lives under that node's own directory. The only trace it leaves above is its name and the path that name resolves to, because a noun has to resolve somewhere.

The interface is two fixed paths and nothing else: a node's inbox, which others write, and its outbox, which others read.

A judgement that compares siblings cannot be made by any one of them, because a comparison needs all of them at once. That is the only thing that lives above a node and is not its name.

## Speech

Exactly one node speaks to a person: the root. Every other node speaks to the layer above it and to nobody else, so a node that wants a person is a node that has not found the right layer.

A node that is not the root takes its word from the contract that created it, not from the person. Nothing is waiting for a `go` that was never going to reach it.

## Reports

A report carries the node whose roadmap the finding would change, an evidence pointer, and the decision it needs, which may be none. Nothing else fits. A report missing one of the three is refused, not summarised.

A completion is a report whose decision is none. Above the root there is no node, so the root's reports are addressed to the person and carry the same three fields.

The node named may be several layers above the parent. A report that names no node is a status message, and it is not sent. A milestone is a state of that node, so the report does not carry it as a fourth field.

A report names its own kind, and the kind decides the route, so no layer has to judge whether it understands the question.

- `resource`: a budget, an accelerator, a device or a wall-clock. It goes to the nearest ancestor that holds that budget, and a container can always answer it.
- `cost`: the work invalidates or reopens a commitment, or the act would destroy work, spend money or expose something private. It goes to the node that owns the commitment, and at the root to the person, because those are the acts that wait.
- `direction`: what this should be, whether the idea is right, whether the design is right. It goes to the person, unchanged through every layer above, because no layer in the tree has the standing to answer it.
- `contract`: the contract contradicts itself, or the acceptance cannot be observed. It goes to the sender's parent, which owns that contract.

A contract missing its area, its acceptance or its spend class, or one whose acceptance cannot be observed, is a `contract` report naming the field, and nothing is edited past it until it is answered.

A layer answers only a kind it holds the authority for. Refusing to forward a `direction` report is the one thing a container may never do. A layer that passes a report on adds the cost, the priority against its siblings, and its own recommendation, and never an answer.

A `direction` report is read or tasted. A tasted one carries a pinned artefact and the command that rebuilds it, and it expires when that artefact's revision moves, because a judgement of something nobody can still run is not evidence.

Three things decide a report's fate, and they are independent. Its kind decides the route. What it spends decides who may release it. The degree of agency its project runs at decides how much reaches the person at all.

A `direction` or `cost` report is admitted only with its effort: what was tried, why each path is closed, and the observation that would reopen one. A report without it is bounced back, because a layer that has not exhausted itself has not found a question.

## Consent

A node acts until it would destroy work, publish, spend money, change a contract another tree depends on, or expose private material. Those wait for a person.

Everything else needs no permission. Asking anyway is a defect, not caution.

A node that may not reach a person raises the wait to its parent instead: it reports what the act would destroy or spend, and it neither proceeds nor stays silent. The parent answers it or carries it further.

## Subordination

A node reads what its work needs. Another node's document is not evidence for its own, and a rule seen in passing is not a rule for it.

