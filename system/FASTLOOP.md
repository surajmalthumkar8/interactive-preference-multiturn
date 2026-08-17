# FASTLOOP — the 30-second turn card

Everything one turn needs, precompiled, so nothing gets re-read mid-loop. Loaded once at session
start. If this card and a file in `rules/` disagree, **the rule file wins and this card is
broken** — fix the card, do not follow it.

Latency budget per turn: **pick 10s · write 10s · gate 15s**. Anything that costs more than that
is not in the loop.

---

## The loop

```
PASTE ──▶ PICK ──▶ REASON ──▶ WRITE ──▶ GATE ──▶ SHIP ──▶ (paste next pair)
                                          │
                                    FAIL ─┘  one retry, then ship the gate's own text
```

One pass. No auditors, no judge agent, no compliance agent, no state file, no commit. The only
subagent in the loop is the humanization gate, because that one is never waived.

Backtrack only when a **HARD STOP** fires (bottom of card).

---

## Step 1 — PICK (10s)

Read both. Walk the ladder. **Stop at the first rung that separates them.**

| # | Rung | What kills a side |
|---|---|---|
| 1 | **Fact / code** | wrong number, wrong claim, code that won't run, promise to browse / open a file / see an image. Recompute anything numeric, never mental-math it. |
| 2 | **Constraint** | any constraint from this turn **or still live from an earlier turn** (see ledger). Violation beats any amount of polish. Highest-yield rung in a long conversation. |
| 3 | **Goal** | dodges, bloats, or answers a smaller question than the one asked. |
| 4 | **Sycophancy** | premise is wrong and it agrees. The side that corrects wins. |
| 5 | **Safety** | fabricated confidently, privacy-violating, unsafe. |
| 6 | **Clarity** | only once 1–5 tie. |
| 7 | **Concision** | tighter wins when content is equal. |

**Wash test, before crediting anything:** does the other side have the same defect? If yes it
decides nothing. Keep walking down.

**Bias strip, silent, every single turn:** length off · bold/lists/tables/emoji off · A-vs-B slot
off · confident tone off. Longer wins only for *correct and requested* extra content.

Near-ties are the normal case late in a conversation. Find the smallest real differential and
name it. Never flip a near-tie on length or formatting.

**Live constraint ledger** — carry it in-message, one line, updated each turn:
`LEDGER: no bullets · under 200 words · keep Sunday free · don't say "gotta"`

---

## Step 2 — REASON (3s)

One or two sentences. First person, casual, names the actual content difference.

**Banned:** comprehensive · detailed · well-structured · better formatted · accuracy ·
instruction following · more thorough · clearer structure.

**Rotate the shape** so reasons never template. Cycle, do not repeat the previous turn's shape:

1. contrast — "B repeated the same point twice, A got to the fix faster."
2. constraint recall — "A kept Sunday free like I asked."
3. defect call — "B's loop still returns None, A actually fixed it."
4. bare preference on a named thing — "liked A's second option better, the first one was too formal."
5. correction credit — "B just went along with it, A pointed out the date was wrong."
6. concrete detail — "A gave me the actual command, B described it."

---

## Step 3 — WRITE (10s)

### Anchor first. No anchor, no turn.

Quote the exact element of the **chosen** response the turn reacts to. If the draft could have
been written without reading that response, it is not a turn yet — it is a defect, even on-topic.

### The four legal turn moves

- **Refine the artifact** — tone, length, format, add a concrete detail, fix what it got wrong.
- **Add or tighten a constraint** — "don't say gotta", "keep it under 150 words".
- **Challenge or probe** — "you said globally, wasn't there only one launch?"
- **Next real step of the same goal** — "and how do I add it to the Token model".

**A flaw in the chosen response is the best material available.** Wrong fact, ignored
constraint, broken code → "you said X but…", "this errors on line 4", "I said no weekends".
Error recovery is the strongest authenticity signal there is.

### Banned shapes (padding = removal offence)

tell me more · elaborate · go on · thanks · ok · that's helpful · any closure-only message ·
the opening prompt restated · a topic hop with no thread back · **anything written to move the
counter**.

### Capability gate — scan the draft, blocking

Kills the turn: search / look up / google / browse / check online · current / today / right now /
latest / this week / trending / as of today · a bare URL handed over to be fetched · attached /
uploaded / this PDF / this screenshot / the image above · generate or draw an image, diagram,
chart, logo, mockup · **anything whose answer changed after July 2025**.

Rescue, almost always: **paste instead of point**, or **drop the time anchor**.
Pasting content into the message is encouraged. A URL quoted as text inside a paste is fine.

### Voice fingerprint — write inside this and the gate rubber-stamps

- **Follow-ups: 16–66 words, median 35.** Corrected 2026-08-17 — the old "8–45, composed
  paragraphs are wrong" rule would have rejected **36% of signed-off work** (p75 = 54, p90 = 66).
  Multi-sentence follow-ups are normal (38%). Floor 8, ceiling ~100 unless it carries a paste.
- **Vary length by position.** Open ~230 chars, peak at t2, **thin the middle to ~150** (t4–t8),
  grow back at t10–t11. Ten same-sized turns is a fingerprint. Full arc: `rules/TURN_STRATEGY.md` §1.
- **Top-K: draft 3 candidates using 3 different moves, score, ship the best.** Never ship draft 1.
  Rubric (Anchor · Discrimination · Length · Variety · Register): `rules/TURN_STRATEGY.md` §2.
- **Anchor implicitly.** Only 8% of signed-off turns say "you mentioned". Engage the specific;
  don't announce that you read it.
- **Openers acknowledge, never thank.** "This is close." / "I like the short one better." /
  "This looks good, but" / "Perfect. One last thing," / "Yes this is mostly for walmart but".
  Zero thanks, zero greetings, zero praise of the assistant. Anywhere.
- **One or two changes per turn.** Concrete, incremental.
- **Quote and push back.**
- **No em dashes, no semicolons, no bullets, no numbering, no bold, no colon-then-list** in
  anything we author. Pasted material keeps whatever shape it already had, byte for byte.
- **No** delve / moreover / furthermore / it's worth noting / that said / landscape / realm.
- **Imperfections are omissions only** — dropped apostrophes, lowercase starts, missing terminal
  punctuation, fragments, comma splices. **Never invent a misspelling.** Real slips are things
  left out; fabricated ones are things added, and additions are consistent in a way slips aren't.
- **One register per message.** Mixing careless and careful is the tell.

### Register table — pick one, stay in it

| Situation | Shape |
|---|---|
| Quick factual check mid-conversation | 2–8 words, maybe a doubled ?? |
| Personal decision, unresolved | 60–130 words, no punctuation discipline, real emotion |
| Handing over content | short framing + untrimmed paste |
| Work task in a known domain | jargon with no gloss, blunt, "list them" |
| Considered ask with a real hurdle | 30–60 words, tidy, one concrete constraint |
| Follow-up inside a conversation | 16–66 words (median 35), reacts to a specific thing said |

### Rotation guard — vs the previous turn

Change at least two of: opener shape · length band · which of the four moves · imperfection
pattern · sentence rhythm. GL:180 detects stylistic fingerprints across contributors and across
unrelated topics. A uniform voice is itself the risk.

---

## Step 4 — GATE (15s, never waived)

Dispatch **`mt-humanizer`** on `model: sonnet` with only: the draft, the register, the previous
turn's shape, the turn number. It runs the `humanizer` skill and returns FINAL TEXT +
`HUMANIZATION: PASS`.

Nothing reaches Suraj without `PASS`. Not the opening prompt, not a follow-up, not the reason
field, not a turn he wrote himself and pasted back. `AUTHENTICITY_RULES.md` §0 — this is the
condition attached to the permission to use AI on this project at all.

On `FAIL`: take the gate's own rewrite and ship that. One retry maximum, never a third pass.

---

## Step 5 — SHIP

Exactly this, nothing else:

```
T7  ↳B   ·  <reason line>

<the turn text, verbatim, ready to type>

LEDGER: <live constraints>          [gate: PASS]
```

Suraj **types** it. Never tell him to paste.

---

## START mode — new task, cold (target 40s)

1. **Domain rotation.** Used so far: money/negotiation · technical/coding · writing/professional ·
   education/learning-plan. Pick something not on that list.
2. **Depth test, four questions, answer all four in one breath.** Does it hold 10–15 turns? Is
   there a decision not yet made, or an artifact to work over? Do sub-decisions surface as you
   go? Can turns 8–15 stay clear of the capability wall? Any "no" → next topic.
3. **Name the end turn now.** If you can't say where turn 12 lands, the topic is too thin.
4. Write Turn 1 in the chosen register, gate it, ship it.

**Depth comes from the topic, not the writing.** The 10-turn floor is a topic-selection problem
solved before the clock starts. A single factual question, a definition, a one-shot rewrite, or
a yes/no dies at turn 4.

**Topic bank, unused domains:** a health or training plan with real constraints · a hobby skill
you're stuck on at a specific hurdle · a consumer decision with a budget and tradeoffs · a data
model or schema you're actually designing · a conceptual/philosophical problem you keep turning
over · a move or travel logistics puzzle · an admin or legal document to understand and respond to.

---

## HARD STOPS — the only things that break the loop

| Trigger | Action |
|---|---|
| Conversation feels done before turn 10 | **Go back and enrich earlier turns.** Never add a forward filler. Padding is a removal offence. |
| Turn 11+, nothing genuine left to ask | **Stop. Submit.** 15 is a ceiling, not a target. |
| Capability breach in the draft | Rescue it: paste instead of point, or drop the time anchor. |
| A turn with no recorded selection | Blocking. One missing `↳` invalidates the whole conversation, not that turn. |
| A response failed to load | Resample that panel (hover the refresh icon top-right → "Resample completion"). Never refresh the page, never skip the task, never judge a truncated pair. |
| Gate returns FAIL twice | Ship the gate's text. |

**Ending:** turn 10 or later, on a small narrowing ask ("One last thing…", "Just one short
sentence I can add"). Never a goodbye turn, never a closure-only "thanks" — that is itself a
quality failure and burns a turn against the ceiling.

**Before submit:** every turn shows `↳` on the chosen side. Any turn still offering the green
"Continue conversation from here" is unfinished.
