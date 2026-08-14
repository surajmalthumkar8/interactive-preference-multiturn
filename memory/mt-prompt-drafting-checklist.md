---
name: mt-prompt-drafting-checklist
description: When drafting MAI multi-turn prompts with AI (now allowed), always cross-check the guidelines doc's style rules and run the humanizer skill on every turn
metadata:
  node_type: memory
  type: feedback
  originSessionId: 245c96c2-20a4-4909-b2a6-fe539a64b62a
  modified: 2026-08-14T07:21:03.826Z
---

Now that AI-assisted drafting is allowed (see [[mt-never-ai-write-prompts]]), Suraj wants every
drafted turn checked against the guidelines doc's actual style rules first, and run through the
`humanizer` skill every single time — not optional, not a one-time pass.

**Where the style rules live:** `MAI Interactive — Multi-Turn Guidelines (updated 08_12).md`,
sections "Golden Rule" (~line 180), "Quick Tips" (~line 209), and the raw example prompts table
(~line 196-205). Key points from those sections:
- Real prompts run on, skip punctuation, trail off mid-thought, stay lowercase/casual — not clean
  sentences. The example table is the concrete calibration target.
- "Paste the actual content. Do not use placeholders" — if a prompt references an email/code/doc,
  the full real text goes in, never `[paste here]`.
- The guide explicitly warns it looks for **shared writing patterns across contributors**
  (stylometry). A uniform "Claude voice" applied consistently across tasks is itself a risk, not
  just individual AI-tells — vary sentence rhythm/punctuation habits turn to turn and task to task,
  don't reuse a signature phrasing pattern.

**Why:** Suraj's instruction, given directly after I'd already drafted a few turns without
re-checking the doc each time. He wants this to be a standing habit for this project, not a
one-off correction.

**How to apply:** Before handing over any drafted prompt for this project, (1) match it against
the example-prompt calibration and Golden Rule above, (2) run it through the `humanizer` skill,
(3) keep phrasing/rhythm varied across turns and across separate task sessions rather than
settling into one recognizable style. Part of [[interactive-preference-multiturn]].
