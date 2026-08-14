---
description: Full pre-submit sweep of the current conversation against every removal trigger
allowed-tools: Read, Grep, Glob, Agent
---

Run the pre-submit gate before **Mark as Complete**.

1. Load the open state file from `sessions/`.
2. Dispatch `mt-compliance-auditor` in E2 mode — the full
   `system/checklists/PRE_SUBMIT_CHECKLIST.md` sweep across **every turn**, not just the last
   one: turn count 10–15, causal dependency, no padding, capability cleanliness, PII, `↳` on
   every turn, duplicate and rotation check against `system/learning/PROMPT_LOG.md`.
3. Report BLOCK or SHIP with each finding tied to its rule citation and the owning step.
4. On SHIP, print the submit order: Feather **Mark as Complete** → Vercel **Submit Task**, and
   the post-submit ledger updates.

Extra context, if any: $ARGUMENTS
