# TASK STATE — sxs-529-learning-plan

Created from `system/templates/STATE_TEMPLATE.md` at intake. Update **every turn**, never at the
end. Created **before turn 1 is typed** — `mt-topic-scout` flagged this file as a blocking
precondition (LESSONS 2026-08-14: "the compliance auditor blocked on a missing state file").

---

## Header

| | |
|---|---|
| Task ID | Side-by-Side Conversation 529 (`side_by_side_conversation` / `general-multi-turn`, created 2026-08-12 13:13:39) |
| Status | OPEN |
| Opened | 2026-08-15 (claimed today) |
| Vercel task claimed | yes (confirmed by Suraj) |
| Feather status confirmed "In progress" | yes (per pasted task page) |
| `Attempt URL` pasted in Vercel | **not confirmed — OPEN, billing-critical.** See Open issues. Do not treat as done. |
| Planned turn count | 14 (floor 10, ceiling 15 — `system/rules/TURN_RULES.md` §1) |
| Current turn | **2** — turn 1 typed, both panels returned, pick recorded (B). Turn 2 drafted and humanizer-PASSed, **not yet typed**. |

## Topic

- **Domain:** study/learning, non-work. First use of this domain (`PROMPT_LOG.md` rotation state
  lists study/learning under "Domains not yet used").
- **Client category:** **Explaining Concepts** — one of the two least-used (Creative ✓ and
  Explaining ✓ both sit at ×1; Writing/Professional was consumed by Conv 462, which is not yet
  logged in `PROMPT_LOG.md`).
- **Conversation shape:** planning under accumulating constraints. Unused this session
  (`PROMPT_LOG.md` lists planning under "Shapes not yet used").
- **Register:** tidy / considered — 0–2 light slips only. Unused this session; Conv 101 and
  Conv 462 both ran rushed/handing-over-content, so this closes that repeat.
- **Opener length band:** 30–60 words, tidy, one concrete constraint, **no paste**. The no-paste
  choice is deliberate: it removes the paste-vs-point capability risk from the opener entirely
  (`CAPABILITY_RULES.md`).
- **Opener (verbatim, as typed into Feather):** **ARCHIVED 2026-08-15.** Confirmed submitted —
  it was typed and both panels responded.

  > I want to be able to hold a real conversation in Spanish and I have 40 minutes a day for it.
  > I did this once before and quit about six weeks in, mostly because I could read fine but froze
  > the second someone actually spoke to me. How should I split the 40 minutes?

  **54 words** (inside the planned 30–60 band) · register **tidy** · opener shape
  **statement-first** · **no paste** · imperfection: **one omission-class slip** — missing comma
  before "and I have 40 minutes a day for it". One slip, inside the tidy budget of 0–2.
  This closes the archive gap that was missed on both Conv 55 and Conv 101 (LESSONS 2026-08-15).
- **Default instance (scout's approved recommendation, GO verdict):** a self-directed learning
  plan — learn Spanish well enough to hold a real conversation, 40 minutes a day, having quit once
  already about six weeks in.
- **Source:** **invented** (disclosed exception). Suraj was asked directly and confirmed no real
  AI-history thread was available to source from instead. This is
  `system/rules/AUTHENTICITY_RULES.md` §1's last-resort tier, used deliberately and disclosed —
  same pattern as Conv 55 and Conv 462. **Fourth consecutive invented topic** (55, 101, 462, 529);
  see Open issues, this is a pattern the log has already flagged twice.
- **Depth test:** unresolved ☑ (why the last attempt died at week 6 is a genuine open diagnosis) ·
  next question generated ☑ (each answer narrows the plan and exposes the next assumption) ·
  artifact or decision at the end ☑ (a one-page weekly plan plus a named drop-decision) ·
  capability-clean across all 14 turns ☑ **by construction** — see the three named breach vectors
  in the constraint ledger.
- **Planned arc (turns 2–4 sketched, end point named):**
  - T1: the plan request — 40 min/day, conversational goal, one prior failed attempt named. Tidy,
    30–60 words, no paste. ✔ **done, typed, pick B.**
  - T2 (planned): react to a **specific defect in the plan produced** — the wrong day count, or
    grammar theory front-loaded ahead of any speaking. Must engage the actual output, not a
    pre-written move (TURN_RULES §4).
  - **T2 (as drafted, deviates from plan):** neither planned defect was present — B's actual
    output contained no wrong day count and did not front-load grammar theory. Used the real
    defect instead: a **self-contradiction inside B's own response**, its gradual-ramp claim set
    against its permission to jump straight to the hardest block. Deviation is deliberate and
    correct: TURN_RULES §4 requires engaging the actual output, and executing the pre-written move
    would have meant inventing a defect that was not there. Precedent for a justified T2
    deviation: Conv 462, `sessions/self-review-writeup_state.md` (planned "dropped item" → drafted
    "misfiling" because that was the defect the response actually had).
    The planned day-count / grammar-front-loading probe is **not lost** — carry it forward if
    either defect surfaces in a later response.
  - T3: add a 20-minute-day constraint, with a **named cut** and a **named floor** (what goes, and
    what must survive at 20 minutes).
  - T4: challenge the underlying **method**, not the schedule.
  - T5–T10: the six-week-failure post-mortem · a measurement question (how would I know this is
    working) · the plan compresses to one page · a late format constraint forces a rewrite of
    already-approved material.
  - T11–T12: **constraint-drop probe** — hold the plan to the T3 20-minute floor **and** T2's
    day-count rule simultaneously. Long threads quietly shed early constraints; this is where that
    gets tested.
  - T14: close with one small narrowing ask, then stop. **Stop earlier at T12 if it genuinely
    completes there** — a forward filler turn to reach a number is a removal offence; the fix for a
    short conversation is enriching earlier turns, never padding.

## Constraint ledger

Everything the user has asked for that must still hold. Grows every turn; the judge checks
**all** of it on every pair.

| Turn set | Constraint | Still live? |
|---|---|---|
| Intake (guardrail, not user-stated) | **Breach vector 1 — tool naming.** Around T7–T9, never ask "which app / deck / tool should I use". Rewrite as "what would you change about how I'm doing it". No naming or recommending current tools. | yes |
| Intake (guardrail, not user-stated) | **Breach vector 2 — exam anchors.** No exam or certification anchor carrying dates or a format. Use a self-set deadline instead (a trip, a personal goal). An official cert format may have changed after the July 2025 cutoff. | yes |
| Intake (guardrail, not user-stated) | **Breach vector 3 — currency framing.** Never "what does current research say" or "is there a newer method". Rewrite as "what's the argument against X" — stable-knowledge framing. | yes |
| Intake (scope guard, not user-stated) | The T2–T4 spine must **never** become "how do I stay consistent". That is corpus §A task2's territory and is duplicate-adjacent. | yes |
| Intake (scope guard, not user-stated) | No health framing anywhere in this arc (cortisol/sleep/energy). Deliberately excluded to keep the banned-scenario clearance clean. | yes |
| T1 (user-stated) | **40 minutes a day is the total budget.** Any proposed split must add up inside it — no plan that quietly needs more. | yes |
| T1 (user-stated) | **The plan must engage the six-week quit history**, not just the immediate freezing symptom. Attrition is the stated problem; a plan that only fixes the freeze has not answered the question. **This became the decisive pick differential at T1** — see Pick record. | yes |
| T1 (user-stated) | **Reading is already a strength — prescribe no reading-skill time.** "I could read fine" was stated as the part that already works. Minutes spent on reading are minutes taken from the deficit. | yes |

## Turn log

| # | Register | Len band | Opener shape | Anchor quoted from previous response | Imperfection pattern used | Pick | `↳` verified |
|---|---|---|---|---|---|---|---|
| 1 | tidy / considered | 54w, no paste | statement-first | (n/a — opener) | **omission** — missing comma before "and I have 40 minutes a day for it" (1 slip) | **B** | **unconfirmed — see Open issues** |
| 2 | tidy / considered | ~39w, no paste | **quote-first** (unspent until now) | B: "The fix is to bridge that gap gradually, so you're already speaking a little before you ever talk to a real person" — set against B's own "Do it first or second if you know motivation drops later" | **omission ×2** — missing comma before "but"; no terminal question mark. **Same class as T1 — see rotation flag** | not yet typed | n/a yet |

**Turn 2 anchor, in full.** The turn quotes B against itself: the ramp claim ("bridge that gap
gradually, so you're already speaking a little before you ever talk to a real person") versus the
permission to skip straight to the hardest block ("Do it first or second if you know motivation
drops later"). Both sentences are B's own text, so the turn cannot have been written without
reading the response — TURN_RULES §4 satisfied on the strongest available basis.

**Turn 2 status:** drafted, `HUMANIZATION: PASS`, **not yet typed by Suraj.**
**Turn 2 verbatim text is NOT archived here — it was not supplied to the scribe.** Per the
archive rule that this file's own Topic section invokes, the humanization-PASS text must be
recorded verbatim *before* it is typed, and the typed text must not diverge. Supply it and this
gap closes; until then it is an open gap, not a formality.

## Pick record

| # | Pick | Decisive differential | Near-tie? | Reason text used |
|---|---|---|---|---|
| 1 | **B** | **Forward horizon against the stated attrition history.** A acknowledges the six-week quit *rhetorically* — "That sounds really common" — but its whole forward horizon stops at "at least 2 weeks before changing anything" and it never designs past week 2. B addresses week 6 at three separate points: a tips header "especially past week 6", a bad-day fallback rule, and a relapse-expectation reframe; it also names a week 3–4 progression. **Secondary:** A closes by asking which tool the user prefers — a re-ask — while B had already named its tools up front. | **no** | see below |

**Reason text used at turn 1** (logged verbatim so the next reason can be worded differently):

> B actually planned around the six-week wall — what to keep on a bad day, and that the freeze
> will come back some days anyway. A's plan runs out at two weeks and then asks me which podcast
> I want.

**Do not reuse this wording or its shape.** Next reason must not lead on "actually planned
around" or close with an A-re-asks-me contrast.

**Note on the secondary differential:** A's closing tool question is a *model-side* re-ask and is
scored as a response defect. It does **not** touch constraint-ledger breach vector 1, which binds
the *user-side* turns (Suraj must never ask "which app should I use"). Recorded so a later reading
does not confuse the two.

## Rotation guard

- Imperfection patterns already spent this task: **omission class only, both turns.**
  - T1: missing comma (before "and I have 40 minutes a day for it").
  - T2: missing comma (before "but") + missing terminal question mark.
  - ⚠️ **FLAG — thin variation, act on this at T3.** Two turns running inside the same slip
    *category* is a weak spread. T2's missing terminal punctuation is a different *instance* but
    the same *class*, and both turns also repeat the missing-comma slip specifically. The rotation
    requirement is a genuine spread of pattern, not of wording. **T3–T4 must leave the omission
    class**: use mid-sentence self-correction, or a lowercase "i" in an otherwise tidy line. This
    is a directive for the next turn writer, not an observation.
  - Spent on other tasks this session, avoid repeating as a task signature: Conv 55 run-ons ·
    Conv 101 fragment-chaining · Conv 462 T1 dropped apostrophe + comma-chain, T2 comma-splice +
    bare fragment with zero contractions.
  - Still available: mid-sentence self-correction · trailing "…" · lowercase "i" in an otherwise
    tidy line. Register is **tidy**, so budget stays 0–2 light slips per turn, not a texture.
    (Missing comma and missing terminal punctuation are now both spent.)
- Opener shapes already spent this task: **statement-first (T1) · quote-first (T2).**
  Still available: question-first · condition-first ("if…") · constraint-first.
- Streak check (A/B): **B ×1** (T1). No streak. Flag if either side reaches 3 consecutive and
  re-examine whether the differentials are genuinely independent.
- **Rotation vs Conv 462 — 6 axes moved** (≥3 required, `TOPIC_PLAYBOOK.md` §5): Domain
  (Writing/Professional → study/learning non-work) · Shape (document worked over → planning under
  accumulating constraints) · Register (rushed → tidy) · Length band (default + ~330w paste →
  30–60w, no paste) · Turn count (13 → 14) · Client category (Writing/Professional → Explaining
  Concepts).

## Open issues

- ✅ **RESOLVED 2026-08-15 — turn 1's imperfection pattern is no longer TBD.** It is recorded as
  omission class (missing comma), which was what blocked confirming no-repeat at turn 2. The
  comparison can now be made, and it comes back **negative**: T2 repeats the class. See the
  rotation-guard flag — resolving this gap immediately surfaced a real one.
- **`Attempt URL` not confirmed pasted in Vercel — billing-critical, still OPEN, carried
  forward.** Unchanged by this update. The copy-URL-after-claim step exists only inside a
  flowchart image in the guidelines (LESSONS 2026-08-13), so it is the step most often skipped.
  Turn 1 is now typed and turn 2 is drafted — the task is no longer early. Confirm with Suraj now.
- **Turn 1 `↳` verification is UNCONFIRMED.** The pick (B) is recorded and both panels responded,
  but nobody has confirmed the `↳` marker actually shows on the chosen side in Feather. A turn
  without a recorded selection is a removal trigger that invalidates the **whole** conversation,
  not just that turn. This makes **four** state files in a row carrying an unverified `↳` (55,
  101, 462, 529) — the file already flagged the pattern below, and it has now recurred on the
  task that flagged it. Verify before turn 2 is typed.
- **Turn 2's verbatim text is not archived in this file.** It was not supplied to the scribe. The
  archive-before-typing rule exists because Conv 55 and Conv 101 both lost their opener text; the
  T1 gap was just closed and T2 immediately re-opens it one turn later. Paste the humanization-PASS
  text into the turn log before Suraj types it.
- **Was Conv 462's turn-1 `↳` resolved before turn 1 of this task was typed?** `unknown.` The
  Open-issues entry below made that an explicit precondition. Turn 1 here has now been typed, so
  either the precondition was met and went unrecorded, or it was bypassed. Check 462's state file
  and record the answer; do not assume the former.
- **Banned-scenario clearance (S1 verdict, recorded before turn 1 per LESSONS 2026-08-14):**
  contractor quote — CLEAR · landlord lease — CLEAR · cortisol/health — CLEAR (deliberately
  excluded, no health framing anywhere in this arc) · product naming — CLEAR · Node.js race
  condition — CLEAR.
- **Duplicate check:** closest neighbour is Conv 462 — shares "artifact refined against a hard
  constraint" abstractly, but the need differs (compression-to-a-cap vs forward-plan
  construction). No real overlap with Conv 55 or Conv 101. The only other Explaining-category
  entry, legacy task 172 (deductible vs out-of-pocket), is a one-shot mechanism question rather
  than a plan — no overlap.
- **Sourcing — fourth consecutive invented topic (55, 101, 462, 529).** `PROMPT_LOG.md`'s flag on
  task 2 said plainly: "Next task: source from real history, or state plainly that the gap could
  not be closed." Conv 462 did not close it and neither does this task. Suraj was asked directly
  and confirmed no history was available, so the exception is disclosed and deliberate each time —
  but four in a row is now a standing property of the portfolio, not an exception, and it should be
  named in the close-out rather than re-disclosed a fifth time.
- **Turn-count rationale partly unverified.** The scout's reasoning was that the 13 and 15 bands
  are "spent this session". The ledger supports 11 (Conv 55), 12 (Conv 101) and 13 (Conv 462,
  planned). **No 15-turn task is recorded anywhere** — that half of the rationale is `unknown`. The
  choice of 14 stands on its own (unused band, comfortably inside 10–15), so this is a bookkeeping
  correction, not a reason to re-plan.
- **`PROMPT_LOG.md` does not yet carry a Conv 462 row** (462 is still OPEN, so it has not been
  logged). Anything in this file that says "Writing/Professional is spent" is true of the session
  but not yet true of the ledger. Log 462 at its close before running this task's duplicate check
  again.
- **Conv 462 is still OPEN and mid-flight while this task is being opened.** Its turn-1 `↳` is
  unverified and its turn 2 is drafted-but-not-typed. A turn without a recorded selection is a
  removal trigger that invalidates the **whole** conversation. Two concurrent open tasks also
  raises the risk of a state-file mix-up. Resolve 462's `↳` before turn 1 of this task is typed.
- **Cross-task carry-over, not this task's blocker:** Conv 55 and Conv 101 both still show `↳`
  verification as TBD/open, and Conv 101 carries a turn-4 pick discrepancy (state file says A,
  close-out says B). Three state files in a row now carry an unverified `↳` — the pattern needs
  closing out, not just the instances.
- **Platform length limit:** `LESSONS.md` records an unconfirmed ~35-word cap. Conv 101 and Conv
  462 both submitted ~330–350-word pasted openers with both panels generating cleanly, so the
  recorded cap is stale. This task's opener is 30–60 words with no paste, so the risk does not
  apply here either way.
- **Failed panels / resamples:** none yet.
- **Anything to raise in Slack:** nothing yet.
