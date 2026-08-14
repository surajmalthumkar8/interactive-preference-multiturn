---
name: mt-legacy-system-stale-and-off-limits
description: The Interactive_contri_inst/ automation system still targets the superseded 07-28 turn-count regime — that's now the only reason it's off-limits
metadata: 
  node_type: memory
  type: project
  originSessionId: 245c96c2-20a4-4909-b2a6-fe539a64b62a
  modified: 2026-08-14T06:56:56.418Z
---

`c:\Users\Suraj\Downloads\project_interactive_linkedin\Interactive_contri_inst\` holds a
Claude-agent pipeline Suraj built in July 2026 (7 `sxs-*` agents, rules, a voice corpus,
validators, and 6 saved task sessions).

**Update 2026-08-14:** Leadership reversed the "AI must not write prompts" rule (per Suraj, via
Slack — see [[mt-never-ai-write-prompts]]), so the original reason #1 below no longer blocks this
system. Reason #2 still stands unchanged:

1. ~~It automates the parts that must be human~~ — no longer a violation now that AI-assisted
   drafting is permitted, provided output is humanized before submission.
2. **It is still calibrated to a dead ruleset.** It targets the **07-28** guide's **min 1 / max
   10** turns, and its TURN_RULES.md states "ending at Turn 1 or Turn 2 is now a *correct*
   outcome." The current 08-12 guide requires **min 10 / max 15**. See [[mt-turn-count-conflict]].

**Why:** Useful discovery — the stale contradictory passages in the 08-12 guidelines
(lines 134, 162, 172, 229) are verbatim leftovers of this 07-28 regime. The 08-12 doc was edited
in place and those passages were never stripped. This system is an independent copy of the old
rules, which is what confirms it.

**How to apply:** Don't run, extend, or port it *as-is* — the turn-count logic is wrong for
current tasks. It could be revived if TURN_RULES.md (and any other 1–10-turn assumptions) were
first updated to the 10–15 regime; until that rework happens, treat it as reference material, not
a runnable pipeline. Components already safe to use standalone as *self-check* tools:
`system/rules/CAPABILITY_RULES.md`, `system/checklists/PRE_SUBMIT_CHECKLIST.md`, and
`system/knowledge/REVIEWER_MODEL.md`.
