# SIGNED_OFF_PATTERNS — what actually gets approved

Evidence base: **20 signed-off conversations, 207 user turns**, harvested read-only from the
`[general-multi-turn] Side-by-Side Conversation 2026-08-12` campaign on 2026-08-17. These are other
contributors' tasks that passed client sign-off. Nothing was edited; navigation and text extraction
only.

Raw corpus: `harvest/all_user_turns.txt` (scratchpad, not committed — it is other contributors' work).

---

## 1. The numbers, measured not guessed

| | median | mean | range |
|---|---|---|---|
| Opening prompt | **231 chars / 43 words** | 253 | 44 – 574 |
| Follow-up prompt | **193 chars / 35 words** | 227 | 21 – 926 |
| Assistant response | 2,846 chars | 3,561 | 265 – 18,901 |

**Turn count: every single one ran 10 or 11 user turns. None reached 12–15.** Ten is not a floor
people scrape past — it is where good conversations actually land. Aim at 10–11 and stop.

**Length arc across a conversation** (median chars by position):

```
t1 231 · t2 250 · t3 219 · t4 175 · t5 190 · t6 149 · t7 181 · t8 166 · t9 191 · t10 217 · t11 270
```

Opening and turn 2 are the longest, the middle **thins out to ~150–190**, and the last two turns
grow again. Do not write ten uniformly-sized paragraphs — real conversations breathe.

---

## 2. Register — softer than the guidelines' examples

| Trait | Openings | Follow-ups |
|---|---|---|
| First person (`I`, `my`) | 85% | 73% |
| Ends with a question mark | 80% | 73% |
| **No question mark at all** | 20% | 27% |
| Starts lowercase | 10% | 25% |
| Missing apostrophes (`dont`, `hes`) | 15% | 2% |
| Pushback / disagreement | 70% | 39% |
| Explicit constraint (budget, only, must) | 30% | 23% |

> ### ⚠️ Cross-check finding — the guidelines' examples are messier than what gets signed off
>
> GL:194–205 shows deliberately raw prompts ("so i was thinking about switching careers into UX
> design but I don't have a portfolio and I don't know where to start and someone told me…").
> **The signed-off corpus is noticeably more composed than that.** Three-quarters use normal
> capitalisation and punctuation; only 3% of follow-ups drop apostrophes.
>
> Read the guideline examples as *permission* to be informal, not as a target to imitate. Writing
> deliberately messy prose to match them is itself a shared-pattern risk under GL:180.

**Non-native English is well represented and signs off fine.** conv284 ("what is the most important
feature that could I start first"), conv268, conv271 all carry L2 word order and were approved.
Natural imperfection beats polished uniformity.

---

## 3. Anchoring — the single strongest signal

**76.5% of follow-ups reuse specific terms introduced by the response they answer.** Median
per-conversation rate: **84%**. The deep technical ones hit 100% (conv261, conv284, conv298).

**Control test:** the same turns scored against randomly shuffled responses give **46.6%**
(sd 3.0, 20 shuffles). About half the raw overlap is shared topic vocabulary, so the honest figure
is the **+29.9 point lift (~10σ)**, not 76.5%. The effect is real; the raw percentage overstates it.

**Parser integrity:** all 207 parsed user turns verified as verbatim substrings of the source
pages, zero mismatches — the numbers are not extraction artefacts.

**But only 8% say "you mentioned" or "going back to".** Anchoring is overwhelmingly *implicit* —
they engage the substance directly instead of announcing that they read it:

> *"why are we making two separate batches of potatoes though? … if the tofu and potatoes sit there
> for 30 minutes while the chicken cooks, i'm worried they're going to be lukewarm"* — conv273

That turn is unmistakably a reply to a specific plan. It never says "you suggested". **Prefer this.**
Reserve explicit callbacks for genuine long-range returns ("going back to something you said
earlier, if his wife can get work authorization once the 485 is filed…" — conv296 t9).

---

## 4. Four archetypes, all approved

**A. Iterative refiner** (conv273, dinner party) — the strongest pattern in the corpus. Every turn
finds a concrete flaw in the last output and demands a fix. Includes correcting the model's
misreading of the user's *own* words:

> *"Maybe making this harder than it needs to be. when i said completely separate, i meant i don't
> want the vegetarian food touching the chicken … i'm fine with separate trays being in the oven at
> the same time."*

**B. Systematic learner** (conv279, cooking technique) — a curriculum. Each turn opens a new
sub-problem in a deliberate arc: browning → pan heat → fond → pan sauce → salt correction →
substitution logic → baking limits → practice plan → checklist. Clean prose, no messiness at all.

**C. Decision driver** (conv281, architecture) — short turns (52–248 chars), each locking one
decision and moving on: *"So, it's settled that C# will be used for the backend with microservices,
now, which database do you recommend I use?"* Lowest anchoring rate (50%) and still signed off.

**D. Investigator** (conv296, H-1B backlog) — all-lowercase, probes consequences and hypotheticals:
*"say the worst happens and he loses the job tomorrow…"*, *"is this how the system was designed to
work or has it just drifted into this because of the backlog"*.

---

## 5. Moves worth stealing

- **Load the opening with real constraints.** conv273: six people, one vegetarian, no spice, *one
  oven*. Constraints give the model something to fail at, which makes the A/B choice meaningful.
- **Reject an assumption the model made.** *"i don't think i want to make the whole dinner
  vegetarian just because one person is."*
- **Challenge a specific number with reasoning.** *"a whole pound of tofu for one person and more
  than three pounds of chicken for five … remember, everyone is also eating feta, potatoes, green
  beans and dessert."*
- **Notice a pattern across the whole artifact.** *"we went a little overboard with lemon. it's in
  the chicken, the tofu, the green beans, and then the dessert is lemon too."*
- **Stress-test with a hypothetical.** *"say the worst happens and he loses the job tomorrow."*
- **Name your own bias.** *"I think 'future-proofing' is probably where I rationalize upgrades the
  most."*

## 6. How they close

Three endings recur, all clean — none is a filler turn:

1. **Ask for a consolidating artifact** — checklist, routine, wrap-up (conv279, conv252, conv67).
2. **Flip the interaction** — *"Ask me the questions you need one at a time, and then help me build
   the final plan"* (conv267, conv283). Strong: it converts the whole history into a new frame.
3. **Land the deepest remaining doubt** — *"last thing. after all this the part i still cant get
   past is that six years went by and nothing happened."* (conv296).

---

## 7. What this changes for our turns

- Target **10–11 user turns**, not 13–15.
- Opening **~230 chars** with at least one hard constraint or number; follow-ups **~190**, and let
  the middle drop to ~150.
- **Anchor implicitly.** Engage a named specific from the response; do not announce that you read it.
- Vary the archetype **across tasks** — running "iterative refiner" every time is exactly the
  cross-task fingerprint GL:180 looks for.
- Keep normal punctuation by default. Informality is permitted, not required, and manufactured
  messiness is its own tell.
- Close on an artifact, a frame-flip, or the honest remaining doubt.
