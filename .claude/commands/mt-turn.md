---
description: Process a pasted A/B pair — judge it, then write the next turn
argument-hint: [paste response A and response B]
allowed-tools: Read, Grep, Glob, Bash, Agent, Skill
---

Pasted content:

$ARGUMENTS

Run MODE COMPARE of `system/workflows/RUN_TASK.md`:

1. **Completeness gate** — if either response is blank, truncated, or missing, stop and ask for
   a Resample ↺. Never judge a partial pair.
2. Dispatch **two** `mt-response-auditor` agents blind and in parallel, in a single message —
   each gets the history plus **one** response, with no mention of the other.
3. Dispatch `mt-preference-judge` with both responses and both audits.
4. Adjudicate inline: cross-check every decisive fact against the audits and the raw text. Any
   disagreement blocks the pick until resolved.
5. Dispatch `mt-turn-writer` with the **chosen response only** — never the loser, never the
   judge's reasoning. Below turn 10 it may return BACKTRACK but never END and never filler.
6. Capability gate inline → `mt-humanizer` → `mt-compliance-auditor`.
7. Deliver PICK + reason + the next turn to type + the turn count, then dispatch
   `mt-session-scribe`.

Remind him to confirm `↳` appears on the chosen side before continuing.
