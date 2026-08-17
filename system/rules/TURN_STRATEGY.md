# TURN STRATEGY — how a turn gets written (BINDING)

Derived from **20 signed-off conversations / 207 user turns** measured 2026-08-17
(`system/knowledge/SIGNED_OFF_PATTERNS.md`). Where this file and a memory of "how we write turns"
disagree, **this file wins** — it is the only part of the system calibrated against work the
client actually approved.

Applies to `mt-turn-writer`, `/mt-loop` Step 3, and `/mt-start`.

---

## 1. Length bands — corrected, and they were wrong before

`FASTLOOP.md` said *"Follow-ups: 8–45 words. Composed paragraphs are wrong."*
**Measured: 36.4% of signed-off follow-ups exceed 45 words** (p75 = 54, p90 = 66, max = 158), and
**31% are both >45 words and multi-sentence** — i.e. exactly the "composed paragraph" the old rule
banned. The old cap would have rejected a third of approved work.

| | words | chars |
|---|---|---|
| Opening (turn 1) | **30–70** (median 43) | ~230 |
| Follow-up, general | **16–66** (median 35) | ~193 |
| Hard floor | 8 (only 1.6% sit below) | — |
| Hard ceiling | ~100; beyond that only for a paste | — |

### Length arc — the shape matters more than any single turn

Median chars by position across all 20 conversations:

```
t1 231 · t2 250 · t3 219 · t4 175 · t5 190 · t6 149 · t7 181 · t8 166 · t9 191 · t10 217 · t11 270
```

**Open long → peak at t2 → thin through the middle (~150) → grow back at the close.**
Ten same-sized turns is a fingerprint. Turns 4–8 should be visibly terser than turns 1–2 and 10–11.

### Turn count

**All 20 conversations ended at 10 or 11 user turns. Zero reached 12.** Plan the arc to land at
**10–11**. 15 is not a target and never was; planning toward 13 is planning to pad.

---

## 2. Top-K turn selection — mandatory

Never ship the first draft. For every turn:

1. **Draft K candidates.** K = **3** in `/mt-loop`, K = **5** in `/mt-task`.
   Each candidate must use a *different move* from §4 — not three rewordings of one idea.
2. **Score each 0–2** on the rubric below.
3. **Ship the highest total.** Tie-break on **Discrimination** (D), then on the shorter draft.
4. Note the winning move type in state so §3 rotation can see it.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| **A** | **Anchor** — reuses a specific named in the chosen response | could have been written without reading it | topical only | names a specific element and reacts to it |
| **D** | **Discrimination** — will two models answer this *differently*? | any competent model answers identically | mild variation | a real constraint, edge case or challenge forces divergence |
| **L** | **Length fit** for this turn position (§1 arc) | outside band | at the edge | inside band, and varies from the previous turn |
| **V** | **Move variety** vs the last two turns | same move as last turn | same as two turns ago | fresh move |
| **R** | **Register** — one voice, no AI tells | mixed register or a banned token | flat but clean | reads like one person mid-conversation |

**D is the criterion we have been missing.** The client is buying a *preference*, not a
conversation. A turn both responses answer the same way produces a coin-flip pick and near-zero
signal. Constraints, counter-examples, quantities and challenges force divergence; "tell me more
about X" does not.

---

## 3. Archetype rotation — one per task, logged

Four archetypes all sign off. Pick one per task, **not per turn**, and rotate across tasks.
Record it in `PROMPT_LOG.md` beside the topic; never run the same archetype twice in a row.

| Archetype | Shape | Evidence |
|---|---|---|
| **Iterative refiner** | every turn finds a concrete flaw in the last output and demands a fix | conv273 |
| **Systematic learner** | a curriculum; each turn opens the next sub-problem in a deliberate arc | conv279 |
| **Decision driver** | short turns (50–250 chars), each locking one decision and moving on | conv281 |
| **Investigator** | probes consequences and hypotheticals, casual register | conv296 |

Decision-driver signed off with **52-character turns and only 50% anchoring** — the band is wider
than our rules implied. GL:180 hunts cross-*task* fingerprints, so varying archetype between tasks
matters more than varying sentence shape inside one.

---

## 4. The move library

Every candidate draft picks one. The starred ones are new and under-used by us.

- **Refine the artifact** — tone, length, format, fix what it got wrong.
- **Add or tighten a constraint** — "keep it under 150 words", "don't say gotta".
- **Challenge or probe** — "you said globally, wasn't there only one launch?"
- **Next real step** — "and how do I add it to the Token model".
- ★ **Correct a misreading of your own earlier words** — *"when i said completely separate, i meant
  i don't want the vegetarian food touching the chicken"* (conv273 t5). No LLM-drafted turn does
  this naturally; it is among the strongest human signals available.
- ★ **Challenge a specific quantity with reasoning** — *"a whole pound of tofu for one person…
  remember, everyone is also eating feta, potatoes, green beans and dessert"* (conv273 t8).
- ★ **Notice a pattern across the whole artifact** — *"we went a little overboard with lemon. it's
  in the chicken, the tofu, the green beans, and the dessert too"* (conv273 t6).
- ★ **Stress-test with a hypothetical** — *"say the worst happens and he loses the job tomorrow"*
  (conv296 t4).
- ★ **Name your own bias** — *"I think 'future-proofing' is probably where I rationalize upgrades
  the most"* (conv288).

**Error recovery still outranks everything.** If the chosen response has a wrong fact, an ignored
constraint or broken code, reacting to it is the best turn on the table.

---

## 5. Anchor implicitly

76.5% of signed-off follow-ups reuse a specific from the response they answer — but **only 8% say
"you mentioned" / "going back to"**.

> **Control-tested 2026-08-17.** Scoring the same turns against *randomly shuffled* responses
> yields 46.6% (sd 3.0, 20 shuffles) — so roughly half of raw overlap is just shared topic
> vocabulary. The real signal is the **+29.9 point lift**, about 10σ above chance. Anchoring is
> genuine, but do not read "76.5%" as the strength of the effect; the lift is.

**Engage the substance; do not announce that you read it.** `mt-turn-writer` must still *report*
its anchor quote to the caller, but the anchor must not surface as a callback phrase in the turn
itself. Reserve explicit callbacks for genuine long-range returns across several turns
(conv296 t9 does this correctly, once, at turn 9).

---

## 6. Opening prompts — load them with constraints

30% of signed-off openings carry an explicit constraint; the best carry several. conv273 packs four
into one paragraph: *six people · one vegetarian · nobody likes spicy · only one oven*.

Constraints are not decoration. They are what the two models can **fail at differently**, which is
what makes the preference meaningful. An opener with no constraint scores 0 on **D**.

Also measured in openings: 85% first person, 80% end in a question mark, 70% carry pushback or
stated uncertainty.

---

## 7. Closing moves — pick one, never drift to a stop

1. **Consolidating artifact** — checklist, routine, wrap-up plan (conv279, conv252, conv67).
2. **Frame-flip** — *"Ask me the questions you need one at a time, then help me build the final
   plan"* (conv267, conv283). Converts the whole history into a new frame and earns real depth
   without padding.
3. **Deepest remaining doubt** — *"last thing. after all this the part i still cant get past is
   that six years went by and nothing happened"* (conv296).

---

## 8. Punctuation bans — re-verified, keep them

Measured across all 207 signed-off user turns:

| Token | Occurrence | Verdict |
|---|---|---|
| em dash `—` | **0.0%** | ban holds |
| bullet line | **0.0%** | ban holds |
| numbered list | **0.0%** | ban holds |
| bold `**` | **0.0%** | ban holds |
| semicolon | 1.0% | effectively banned |
| "thanks / thank you" | **0.0%** | ban holds |

Two corrections to over-strict wording:

- **Acknowledge-openers are normal — 12.6%** ("Okay,", "I like the idea of", "This is close.",
  "So,"). Keep using them.
- **Light praise appears in 4.3%** ("Perfect. One last thing,"). Rare but authentic, so not banned.
  *Thanking* the assistant remains at a true zero — that ban is absolute.
