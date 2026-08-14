---
description: Where the current task stands — turn count, live constraints, rotation, open issues
allowed-tools: Read, Grep, Glob, Bash
---

Report the current position without re-deriving anything:

1. Open state file in `sessions/` — task ID, current turn of planned N, live constraint ledger,
   A/B streak, anchor history, open issues.
2. `system/learning/PROMPT_LOG.md` — the last logged task, and which rotation axes this task has
   moved vs. that one.
3. Anything unsynced: `git status --short`.

Then one line on what comes next — another turn, a backtrack, or the pre-submit sweep — with the
reason.

If no open state file exists, say so plainly and offer `/mt-start`.
