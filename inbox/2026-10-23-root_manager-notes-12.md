# Delivered from root_manager — the sixteenth class: the artifact was published through a channel the person cannot open

## 16. "Open it for them" was done with a mechanism only root_manager can see

- **Rule in play:** `to_human.reviewing.open` — "the person's attention lands on the artifact rather than on finding it. The artifact is opened for them rather than described by path." Also `reviewing.off_machine` and `reviewing.pinned`.
- **The incident:** root_manager attached artifacts through its own publishing tool, which produces a reference in root_manager's own session. The person: "use `xdg-open` in the future, your publish whatever tool, I don't even know where does that come from, don't work."
- **Why it happened:** the rule says *open*, and root_manager chose the mechanism that was one call away rather than the one that opens on the person's machine. A hand-off whose receiving side is root_manager's session is not a hand-off — the same defect as class 7 (a note kept on the writer's side) and the same as the law's hand-off with no inbox. Root_manager has produced this shape three times today in three different materials: a note, a mailbox, an artifact.
- **What root_manager makes of it:** "opened for them" is a claim about *their* screen, and only a command that runs on their side can make it true. Everything else is describing a path in a new costume.
- **Suggestion:** name the receiving surface, not the intention: an artifact is opened with `xdg-open` on the machine the person is sitting at (and, where the artifact cannot be shown that way, the message says so plainly and gives the command they would run). And the general shape — one sentence: a hand-off is only complete when it lands on the receiver's surface, which is never the sender's own tool's output.
