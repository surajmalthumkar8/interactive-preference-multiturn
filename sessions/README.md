# sessions/ — live task state

One file per task: `<task-id>_state.md`, created from
[../system/templates/STATE_TEMPLATE.md](../system/templates/STATE_TEMPLATE.md) at intake and
updated **every turn** by the `mt-session-scribe` agent — the only writer of this directory.

These files are what let a task survive a context reset, a closed terminal, or a switch to the
other laptop. They carry the turn counter, the constraint ledger, the anchor history, the
rotation guard, and the pick record.

**Push after every working session, pull before starting on the other machine.**

## Rules for this directory

- **No PII.** These files are committed to a git repository. Scrub before writing, not after.
- **No verbatim model responses.** Store the quoted differential that decided a pick, not the
  full text of either response.
- Never edit a closed state file. Supersede it with a note saying what changed and why.
- Keep closed tasks — the history is the value, and `PROMPT_LOG.md` depends on it for the
  duplicate check.

*(Legacy sessions from the July 2026 system are at
[../Interactive_contri_inst/sessions/](../Interactive_contri_inst/sessions/) and use the old
1–10 turn format.)*
