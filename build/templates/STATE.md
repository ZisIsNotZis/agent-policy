# STATE

> Scope: `<scope name>`  
> Published by: `<Manager identity>`  
> CWD: `<absolute path>`  
> Last updated: `<ISO-8601 timestamp>`

## User-facing summary

`<Concise, plain-language status. State what matters; omit routine internal chatter.>`

## Machine-readable summary fields

```yaml
status: not_started  # not_started | in_progress | at_risk | blocked | achieved | paused | archived
needs_attention: false
stakes: low  # low | medium | high | critical
deadline: null  # ISO-8601 or null
default_action: continue  # continue | investigate | escalate | pause | stop
heartbeat: null  # ISO-8601 timestamp
scope_mode: single_outcome  # single_outcome | multi_outcome
```

Keep this header current. Parent summaries should be generated from these fields plus exception reports where runtime support exists; do not require a parent to reread every descendant STATE file.

## Outcome status

`<Not started | In progress | At risk | Blocked | Achieved | Closed>`

## Verified facts

- `<observable fact + evidence/location>`

## Inferences and assumptions

- `<interpretation or assumption, confidence, basis>`

## Work state

| Work package | Owner | State | Evidence / result | Next action |
|---|---|---|---|---|
| `<id>` | `<owner>` | `<planned/active/attempted/implemented/tested/verified/blocked>` | `<link or concise result>` | `<action>` |

## Material changes and decisions

- `<what changed, why, decision owner, affected work>`

## Blockers and risks

- `<issue, impact, owner, mitigation, whether user input is needed>`

## Pending user input

- `<specific question, why it matters, what continues meanwhile, or none>`

## Next meaningful actions

1. `<action and owner>`
