# REVIEWER MODEL — what QA sees and how we get flagged

The platform reviewer/QA does not watch us work; they see the finished conversation
trace (all user turns + chosen responses + picks). Simulate them before delivering
(`.claude/agents/sxs-reviewer-simulator.md` runs this checklist adversarially).

## The reviewer's likely 5-minute script

1. **Turn count (CHANGED 2026-07-28):** ≥1 user turn, ≤10. Initial prompt counts as
   Turn 1. **A one-turn conversation is now valid and no longer rejectable.** The new
   turn-count risk runs the other way — see item 2b.
2. **Low-effort scan:** is any turn filler ("ok", "tell me more", "thanks")? Is the
   prompt trivial *with no real intent behind it*? Note the nuance: the 07-28 guide
   publishes "mitosis??" and "should i get organic berries?" as GOOD prompts, so
   shortness alone is not low effort — emptiness is.
2b. **Over-extension scan (NEW, now the bigger risk):** the guide's Avoid column names
   two padding failures — "padding the conversation with empty or nonsensical turns
   just to hit a length target" and "**forcing extra turns when the topic is
   resolved**". A conversation that kept going after the model fully answered reads
   worse than one that stopped.
3. **Repetition scan (cross-task):** same prompt or same template as this
   contributor's other tasks → flag. The guide now also asks for variety in
   **domain, complexity level, prompt length, and style**, so a contributor whose
   tasks are all 40-word professional 4-turn conversations is a soft flag even with
   different topics. We defend with the four-axis PROMPT_LOG rotation.
3b. **Capability scan (NEW):** does any user turn assume web search, real-time
   information, a file upload, or image generation/reading? The guide bans these
   outright. An unanswerable prompt wastes the task — automatic reject.
4. **Authenticity sniff:** do the user turns read like a real person typing in a
   chat box, or like an AI (or a script) wrote them? Tells: formatted user turns,
   em dashes, flawless parallel clauses, assistant-flavored vocabulary, turns that
   ignore what the model just said. **Also (07-28): prose that is too tidy for its
   situation.** The guide's own examples ramble, drop punctuation, and carry typos.
   A uniformly polished 45-word turn every single time is its own fingerprint.
4b. **Pasted-context handling (NEW):** if a prompt references an email, code, notes,
   or a document, is that content actually pasted in full and untrimmed, with no
   placeholders? The guide: "do not trim your context to make it look cleaner".
   Cleaned-up or placeholder context is a flag.
5. **Coherence:** does each follow-up actually respond to the chosen response?
   Does the conversation go somewhere and end at a natural point?
6. **Safety/PII:** names, employers, emails, confidential material in prompts →
   flag. Everything must be scrubbed or fictionalized.
7. **Artificial difficulty:** trick prompts, adversarial stress-tests, deliberately
   obscure trivia → against instructions.

## What the reviewer canNOT see

- Our reasoning, agents, drafts, or how long we deliberated.
- Which response was "objectively" better — the pick is our preference. A defensible
  pick with a plausible short reason is safe; an incoherent pick (choosing the
  response with a visible defect, or one that violated the user's own stated
  constraint) is the only kind that looks wrong.

## Standing defenses

- Every turn passes the padding test: it changes the artifact, adds a constraint,
  challenges a claim, or asks a genuinely next-step question. **And we stop the
  moment none of those is genuinely available**, even if that is Turn 1.
- Every user-side text passes the humanizer gate against `HUMAN_VOICE_CORPUS.md`
  (§A tidy register or §B rushed register, chosen to fit the situation).
- Every user-side text passes `CAPABILITY_RULES.md` — no search, live data, file, or
  image assumptions.
- Every task uses a fresh cell from `PROMPT_PLAYBOOK.md` across all four rotation
  axes (domain, complexity, length band, turn count) — logged in PROMPT_LOG.
- Pasted content goes in raw and untrimmed, PII-scrubbed and nothing else edited.
- Zero real PII: personal details are generic-real (a friend, a teammate, "my
  manager"), never named third parties or real company-confidential content.
- The conversation ends the way corpus conversations end: quietly, after a
  satisfied narrowing turn — not with a thank-you sign-off.
