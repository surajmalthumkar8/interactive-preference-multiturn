# PRE-SUBMIT CHECKLIST — final gate before any deliverable leaves (all boxes)

Aligned to the 2026-07-28 contributor guide: turns 1–10, capability limits, raw
pasted context, four-axis variety.

## Pick (COMPARE/SINGLE-with-pair only)
- [ ] Both responses read IN FULL; code/claims verified char-by-char, numerics by code
- [ ] Decision order followed (correctness → constraints → goal → sycophancy →
      safety → clarity → concision); the decisive differential is QUOTED
- [ ] Bias neutralizations done: length, format, position, confidence, shared-defect
- [ ] Constraint ledger checked — every earlier-turn constraint tested on both
- [ ] A response that promises to browse, open a file, or make an image is marked as
      a Tier 1 defect (it cannot do those)
- [ ] Near-tie recorded if applicable; pick not flipped for length/format/variance

## Capability gate (BLOCKING — every user-side message)
- [ ] No web search, "look up", "google", "find online", or bare URL to fetch
- [ ] No real-time/current info (today, latest, current price, weather, news, trending)
- [ ] No file upload reference (attached, uploaded, this PDF/spreadsheet/screenshot)
- [ ] No image generation or image reading request
- [ ] Any content the prompt refers to is PASTED IN, not pointed at

## Next message
- [ ] Anchored to a specific element of the CHOSEN response (quoted in INTERNAL)
- [ ] Earns its place (refines / constrains / challenges / next step) — zero padding
- [ ] **We are not forcing this turn.** If the topic is resolved, END instead —
      ending at any turn ≥1 is valid and over-extension is a named flag risk
- [ ] Turn number correct; ≤10 always; END has no goodbye turn
- [ ] Would blend into HUMAN_VOICE_CORPUS.md — right SECTION (§A tidy / §B rushed)
      for the situation, right length band, right imperfection level
- [ ] No AI tells: no em/en dashes, composed formatting, banned vocab, rule-of-three,
      thanks/greetings
- [ ] Length band deliberate; prose under 120 words unless genuinely rambling or
      carrying a paste
- [ ] Pasted content (if any) left raw: not trimmed, not reformatted, no placeholders,
      PII scrubbed
- [ ] Imperfections consistent with the chosen register, not repeating the previous
      turn's pattern
- [ ] **IMPERFECTION ROTATION CHECK:** the state file's "patterns spent" row was read,
      this turn's pattern is NAMED and is unspent (not used in the previous turn, not
      used twice already), and the row is updated before shipping
- [ ] No PII, nothing traceable, persona consistent with state file

## Process
- [ ] State file updated (turn ledger, constraint ledger, chosen-response memory,
      imperfection-patterns-spent row, full A/B archive)
- [ ] Turn ledger has ONE row per user message actually sent, and any END row's stated
      turn count equals the number of ledger rows (no unlogged turns, no phantom count)
- [ ] validator CLEAN → reviewer-simulator APPROVE → humanizer applied (skill ran)
      → validator CLEAN again → final-evaluator SHIP + HUMANIZATION: PASS
- [ ] Any rule derived from a document was sanity-checked against observed platform
      behaviour (a spec states the ideal; measured behaviour states the constraint)
- [ ] Message is 10-30 words; imperfections are OMISSION class only, never corruption
- [ ] MODE START only: real-history sourcing was offered first (S0); PROMPT_LOG
      updated with category, length band and planned turn count; all four rotation
      axes checked against recent tasks
- [ ] sxs-lessons-scribe dispatched (task end) or queued (mid-task pastes)
