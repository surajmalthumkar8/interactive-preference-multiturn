---
description: Commit and push session state and learnings so the other laptop is current
allowed-tools: Read, Bash, Agent
---

Sync this machine's work to GitHub so the other laptop can pick it up.

1. Dispatch `mt-session-scribe` first if the current turn is not yet written to state.
2. `git status --short` — show what changed.
3. **Scan the diff for PII before committing.** Session files and ledgers are committed to a
   repository; names, emails, employers, and client details must already be scrubbed. If
   anything looks identifying, stop and flag it instead of committing.
4. Commit with a plain message describing the session (for example
   `sessions: task <id> through turn <n>`), then push.

Message override, if given: $ARGUMENTS

On the other laptop, `git pull` before starting.
