---
name: mt-never-ai-write-prompts
description: "Policy reversed 2026-08-14: AI (incl. Claude Code) may now write/help write prompts for this project, provided output is humanized"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 245c96c2-20a4-4909-b2a6-fe539a64b62a
  modified: 2026-08-14T06:56:42.590Z
---

**SUPERSEDED 2026-08-14.** Suraj reported that leadership posted a Slack update reversing the
"write everything yourself" rule: AI tools, including Claude Code, may now be used to help draft
prompts and conversation turns for the Interactive Preference Multi-Turn project. The one hard
requirement that survives: **every AI-assisted prompt must be humanized** before it goes into
Feather — it still has to read like something he'd genuinely type, typos included. He asked me to
add this to his reference copy of the guidelines, which I did:
`c:\Users\Suraj\Downloads\project_interactive_linkedin\MAI Interactive — Multi-Turn Guidelines (updated 08_12).md`
(update callout after the intro, plus the "Where your prompts should come from" and "Human
Authenticity" sections).

**Original rule (kept for context, no longer in force):** the guidelines text still elsewhere
calls invented/polished prompts "far less useful" than real history (line ~58) and the official
screening's Quality Standards Q2 lists "ask an AI to generate a prompt, then paste it" as an
explicitly wrong answer (unconfirmed whether the screening doc itself was updated — I have not
independently verified the Slack post, only Suraj's report of it). If task quality/removal issues
come up later, this is the first place to check for a mismatch between the reference doc and the
live platform rules.

**There is a legacy system in the repo built for exactly this** —
`Interactive_contri_inst/` (built Jul 2026) is a Claude pipeline whose `DO_TASK.md` workflow has
agents write the opening prompt, write every follow-up, run both through a "humanizer" to strip
AI tells, and make the A/B preference pick. Reason 1 for keeping it off-limits (automates
human-only work) no longer applies under the new policy. Reason 2 still applies as-is: it's
calibrated to the superseded 07-28 guide's 1–10 turn regime, not the current 10–15. See
[[mt-legacy-system-stale-and-off-limits]] and [[mt-turn-count-conflict]].

**How to apply:** AI-assisted drafting of prompt/turn text is now in scope — use the `humanizer`
skill on anything meant for submission. Still prefer sourcing from his real
ChatGPT/Gemini/Claude/Copilot history over invented scenarios where possible; that's the
project's stated preferred methodology and wasn't reversed, just supplemented.
Part of [[interactive-preference-multiturn]].
