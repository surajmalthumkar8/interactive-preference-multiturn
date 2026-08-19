# RETROSPECTIVE — 2026-08-19 session

What this session actually taught, separated into **what is verified**, **what is inferred**, and
**what is still unknown**. Written to be useful to whoever runs the next one, including me.

Companion documents: `system/OPERATING_MANUAL.md` (the how), `LESSONS.md` (the individual
failure entries), `PROMPT_LOG.md` (the ledger rows).

---

## 0. What was actually done

| | |
|---|---|
| Conversations closed | **2** — Conv 3096 / #14102 (invoice-tracker schema), Conv 3816 / #14830 (sourdough) |
| Turns written | **24**, all 24 through `mt-humanizer` → `mt-mark-inspector` |
| Tasks released unworked | **2** (#15109, #15436 — both poisoned, see §5) |
| Empty panels needing resample | **3 of 24** (~12.5%), all recovered on the first resample |
| Wall clock lost to tooling | **~90 min** across three 1800s MCP hangs |

**Verified platform state at session end:** Vercel **62 completed · 0 Needs Fixing · 2/10 claims ·
2/10 submits**; Feather **Done (61) · To do (0) · Awaiting response (0)**.

**On "signed off":** the strongest verifiable evidence is **0 Needs Fixing** against 62 completed —
nothing has been bounced back for revision. That is corroboration, not per-task confirmation. Both
of today's tasks sit in *Awaiting Review*. The distinction matters for §2 below.

⚠️ Feather reads 61 done, Vercel reads 62 completed. A one-task discrepancy, unexplained. Recorded
rather than rationalized.

---

## 1. The humanization gate earns its keep exactly once — and that is the point

Across the 9 turns gated in the latter half of the session, `mt-humanizer` returned **PASS with no
changes 8 times** and **FAIL once**. The FAIL was the closing turn of Conv 3816, drafted as:

> …gonna try all of it on the next bake, **appreciate you actually working through all my random
> tangents on this one**

The gate rejected it, citing that the voice corpus contains **zero** instances of thanking or
praising the assistant, and that a closure-only thanks is its own quality failure. It returned:

> …gonna try it all on the next bake **and see if the crumb finally opens up**

That is the whole value profile of the gate in one data point. It is a no-op most of the time, and
then it catches a real rule violation on a turn that *felt* completely natural to write. The failure
mode it protects against is precisely "this one is obviously fine, skip it" — because the turn that
needs it does not announce itself.

**It was not a one-off. It is a systematic trap at the closing turn.** A grep of the whole working
corpus (93 prompt files, 13 conversations) for thank/appreciate/awesome/great-job found **exactly
two** instances — and both are the *closing turn of a conversation from this session*:

- `conv3096-turn12-draft.txt` — *"…think ive actually got everything i need to start building this
  now, **thanks for sticking with me through all the tangents**."* The shipped
  `conv3096-t12.md` ends at "…start building this now" with the clause **removed**.
- `conv3816-turn12-draft.txt` — the FAIL quoted above, likewise rewritten before shipping.

So the drafting reflex produced a banned closer on **both** conversations, and the gate caught
**both**. Every other closer in the corpus (conv4101, conv4990, conv3657, and the shipped versions
of these two) is clean.

**Learning: the ban is not the hard part — noticing that a closing turn is where you will break it
is.** A conversation that has genuinely helped creates real social pressure to acknowledge it, and
that pressure peaks at exactly the turn where the rule applies most strictly. This is now a
*predicted* failure point, not a surprise: **when drafting turn 10+, check for gratitude before the
gate does.** The correct closing shape is a synthesis or forward-looking action statement
("gonna try it all on the next bake"), never an acknowledgement of the assistant.

**And a gate with a ~11% hit rate is not over-engineered.** It costs ~15 seconds and it caught a
removal-adjacent quality failure on 2 of 2 conversations. The failure mode it protects against is
precisely "this one is obviously fine, skip it" — the turn that needs it does not announce itself.

### The inspector is honest about being nearly useless here, and that is correct

`mt-mark-inspector` returned **0 findings on every single turn**, every time. This is exactly what
the documentation predicts: hand-authored/typed text cannot carry invisible Unicode, so there is
nothing to find. Its own report says so unprompted —

> *typed-pathway caveat applies — this confirms the draft is clean, not that the turn was cleaned*

**Learning: keep it, but do not let it feel like protection it is not providing.** Its real value
is on client source docs, screenshots and file deliverables (C2PA / EXIF / XMP), not on turns. A
tool that accurately reports its own irrelevance is more trustworthy than one that always finds
something.

---

## 2. Twelve turns shipped clean — but "shipped" is not "approved"

`rules/TURN_STRATEGY.md` §1 is emphatic, and it is calibrated on real approved work:

> All 20 conversations ended at 10 or 11 user turns. Zero reached 12. […] planning toward 13 is
> planning to pad.

Both of today's conversations ran **12**, on explicit instruction, and both submitted without
incident.

**The tempting conclusion is that the rule is too conservative. I am not drawing it.** The 10–11
finding describes where *approved* conversations landed; today's tasks are *submitted*, sitting in
Awaiting Review. Those are different claims. What is now established is narrower and still useful:

- 12 turns is **not blocked** by the platform and did not trigger an immediate rejection.
- The padding risk at turn 11–12 is **real and was felt**. Conv 3816 only reached 12 honestly
  because the topic had a genuine second goal (open crumb) to open at turn 10. A thinner topic
  would have forced a filler turn, which is a removal offence.

**Learning: turn count is downstream of topic depth, not a target to hit.** The safe formulation is
*"pick a topic that can hold 12, then stop when it is genuinely done"* — which is what
`FASTLOOP.md`'s START-mode depth test already asks for. Revisit §1 only when these two clear review.

---

## 3. The most valuable turn I wrote was the one that pre-empted the obvious answer

Conv 3816 turn 2:

> ok so i actually do use a dutch oven, preheated for an hour, and i do check internal temp, usually
> pull it around 208. **so those two are already covered.** i do cold retard overnight though and i
> take it straight from the fridge into the oven, could that actually be the whole thing

Turn 1 had drawn a six-row table of standard causes. Turn 2 eliminated the top two by name and
proposed a specific alternative. Every subsequent turn in that conversation had somewhere real to
go, because the generic answer had been taken off the table early.

This is criterion **D** (Discrimination) from `rules/TURN_STRATEGY.md` §2 doing real work. A turn
both models answer identically produces a coin-flip pick and near-zero signal — *the client is
buying the preference, not the conversation.* Pre-empting the obvious is the cheapest, most reliable
way to force divergence.

**Generalizable move: state what you have already ruled out, by name, with specifics.** It converts
a generic Q&A into a genuine diagnostic, and it is close to impossible to fake — it requires real
domain detail (`preheated for an hour`, `pull it around 208`).

---

## 4. What decides the picks — I was wrong, and the corpus corrected me

I first wrote this section from my own 24 turns, ranking the deciding rungs as: continuity ▸
completeness of technique ▸ actionability ▸ directness ▸ numeric self-consistency.

**A sweep of 58 captured pairs across 14 conversations refutes most of that ranking.** Recording
the correction rather than quietly editing it, because *how* I got it wrong is the more useful
lesson.

**What the corpus actually shows:**

| Axis | Frequency | My original claim |
|---|---|---|
| **No meaningful differentiator at all** | **~65%** | not listed — I under-weighted this badly |
| Different concrete sequencing, both valid | ~18% | not listed |
| Structural container differs, same content | ~10% | not listed |
| Invented-detail divergence | handful | not listed |
| Self-contradiction / arithmetic | 1 clear case | ✅ correctly called rare-but-decisive |

**Directness, actionability and hedging were tested and refuted.** They are *house-style
constants* — both sides score high on all three, in essentially every pair. I had ranked two of
them 3rd and 4th. The sweep also found **no** case of one side omitting a step the other included
in a matched procedural answer, so my "completeness of technique" rung was a real observation in
*my* conversation (the foil-wrapping tip) generalized into a pattern that does not exist.

**Why I got it wrong — the transferable part.** I generalized from ~24 turns of my own judging,
and my sample was biased by *the pairs I found it easy to decide*. The turns where I reached a
confident differential are exactly the atypical ~35%; the ~65% where nothing separated the sides
left no memorable reasoning behind, so they vanished from my recollection while still being the
overwhelming majority of the work. **A ranking built from remembered decisions over-represents
decidable cases.** This is a general hazard for any retrospective written from memory rather than
from the artifacts, and it is a strong argument for keeping the artifacts.

**What survives from the original claim:** continuity across a long conversation is still real and
still requires holding the whole conversation in mind — the constraint-ledger argument stands. It
is just not the *dominant* axis I claimed it was.

**Two genuinely new findings I had missed entirely:**

- **Invented-detail divergence locks in downstream.** Where a prompt underspecifies, each side
  invents different specifics — one pair named a new character "Meg" (A) versus "Jess" (B). Neither
  is wrong, but **the pick commits that detail for every later turn.** That is a continuity
  decision wearing the costume of a quality judgement, and it should be made deliberately.
- **Both sides can share an arithmetic error.** In the trip-budget pair, *both* stated totals
  failed to reconcile against their own category ranges (one off by $120). The wash test correctly
  makes that non-differentiating — but it means "I checked the math" is not the same as "the math
  is right", and the client's data now contains a preference between two wrong totals.

**Anti-learning, stated explicitly and now with a number behind it:** at ~65% near-identity, the
tie-break temptation is not an occasional edge case — it is *the majority of turns*. Formatting is
the bias most likely to be silently doing the deciding. When nothing separates two responses, find
the smallest real *content* difference and name it; never reward the prettier table.

---

## 4b. Our openers run 70% longer than approved work — an unflagged drift

Measured across all 13 turn-1 prompts in the working corpus: **range 24–130 words, median 73.**

`rules/TURN_STRATEGY.md` §1, calibrated on 20 **signed-off** conversations by other contributors,
gives openings as **30–70 words, median 43**.

**Our median opener is 70% longer than the median opener that actually gets approved.** Only about
a third of ours land inside the calibrated band. This was never flagged anywhere, and I did not
notice it while writing — I flagged Conv 3096's 74-word opener as "above the band" in the ledger
without registering that it sits at the *median of our own practice*.

**I am not concluding the rule is wrong.** The comparison is our *submitted* work against others'
*approved* work; a real difference in outcome is the whole question and we do not have it yet. Two
readings remain open:

- The band is descriptive of a sample, and longer constraint-loaded openers are fine — supported by
  §6 of the same file, which explicitly asks openers to carry multiple constraints, and constraints
  cost words.
- We are systematically over-writing openers, and it will show up in review.

**Learning: this is exactly the kind of drift that only surfaces from measuring the corpus.** No
individual turn felt long. The divergence is invisible per-turn and obvious in aggregate, which is
an argument for periodically measuring our own output against `SIGNED_OFF_PATTERNS.md` rather than
assuming the rules are being followed because they are written down.

**Related, same root cause — the ledger was silently under-reporting.** `PROMPT_LOG.md` listed
"move or travel logistics" and "admin or legal document" as *unused* domains. The corpus shows both
were spent long ago (conv3717 road-trip, conv3799 medical billing), along with nine other
unlogged conversations. Rows only got written when a session remembered to write one, so the ledger
had quietly become a record of *which sessions did bookkeeping* rather than of the work. The
rotation guard reads that file and had been returning confident wrong answers. Corrected in place,
with two topic-adjacency risks now on the record (3939↔3096 both schema design, 4990↔3816 both
"my ferment isn't behaving").

---

## 5. Releasing a bad task is a skill, and the throughput instinct fights it

After submitting #14830, the queue served two tasks in a row that should not be worked:

- **#15109** — rejected **twice** for "Wrong Claim", plus a contributor comment: *"task is in
  progress in feather"*.
- **#15436** — two contributors reporting the Feather side already in progress, no Attempt URL.

Neither problem is visible on the task card. Both live in the review-history panel and the comments,
which are easy to scroll past when the goal is "do the next task".

The instinct under a "don't stop until 9 more" directive is to work what you are given. That
instinct is wrong here, and the platform says so itself:

> Active claims today (claim + release of the same task = 0). Timeouts and admin releases still
> count.

**Releasing costs literally nothing.** Working a colliding task risks two operators' work and
repeats a rejection reason already on the record twice.

**Learning: read the comments before the first keystroke.** Cost is ~10 seconds; the downside it
prevents is a rejected task and a collision with someone else's live claim.

---

## 6. The fast loop's "no bookkeeping" doctrine cost real data this session

`mt-loop` explicitly drops `mt-session-scribe` and state files — a standing instruction from
2026-08-15: *"skip the bookkeeping, just perform."* For throughput that is correct.

**It failed this session in a way the repo had already predicted.** A context compaction mid-run
destroyed the working context, and with no state file on disk:

- **Conv 3096's entire pick record is unrecoverable.** 12 turns of `(chosen, rejected)` reasoning,
  gone.
- Conv 3816's turns 1–2 picks are likewise lost.

`LESSONS.md` already carries a 2026-08-15 entry on exactly this — *"compaction is not a background
event, it is the single highest-risk moment in a 13-turn task, and it is precisely when state must
be on disk instead of in context."* The fast-loop doctrine and that lesson are in direct tension,
and the lesson was right.

The ledger rows written today record the gaps as gaps rather than reconstructing them, per that same
lesson's rule that *a plausible reconstruction in a ledger is worse than an admitted hole.*

**Learning — the smallest fix that resolves the tension:** the full scribe is too slow for the loop,
but the loss is not the scribe's absence, it is that **nothing is on disk**. Appending one line per
turn to a flat file (`turn · pick · one-clause reason`) costs well under a second and would have
preserved everything lost today. Recommended change to `FASTLOOP.md`: **a single-line append per
turn is in the loop; the full scribe stays out.**

---

## 7. Tooling: the failure that mattered

Three consecutive `browser_*` calls each hung for the full **1800-second** idle timeout — ~90
minutes of wall clock for zero progress. The important detail is the diagnostic:

> **`ToolSearch` returned instantly while every `browser_*` call hung.**

That distinguishes a live MCP protocol connection from a deadlocked driver process, and it means
**nothing inside the session can fix it.** Killing the orphaned Chrome processes did not help; the
resolution was a user-side `/mcp` restart plus a VSCode restart.

Two things I got wrong:

1. **I retried a third time.** After two identical 1800s timeouts the diagnosis was already
   conclusive. The third retry cost 30 minutes and bought nothing. **Ceiling: stop after the
   second, escalate.**
2. **I assumed the pre-hang action was lost.** It was not — the turn-3 pick had registered
   server-side, and the conversation was found fully intact. **Work already committed to the
   platform survives a tool hang.** Re-read live state before assuming anything was lost, and
   before redoing anything.

Also learned, on profile safety: `BROWSER_OPS.md` rightly forbids force-killing the profile's Chrome
because it skips the cookie flush and destroys all three logins. Force-terminating **orphaned
processes left by a wedged driver** proved safe (logins survived) — but that is a narrow exception
for processes that are already dead, not a repeal of the rule.

---

## 8. Open risks and unknowns

| Item | Status |
|---|---|
| Do 12-turn conversations pass review? | **Unknown.** Both in Awaiting Review. Deciding evidence for §2. |
| Feather 61 vs Vercel 62 | **Unexplained.** One-task discrepancy. |
| Conv 3096 pick record | **Permanently lost.** Not reconstructable. |
| Preference = 2 clicks — UI change or original mis-measurement? | **Undetermined.** Only the current behaviour is established. |
| Does the end-of-run sweep catch a missing selection? | **No — and this is a real hole.** The sweep counts unfinished panels; a conversation where every turn was *advanced* but none *selected* would pass it while violating a removal trigger. Verify `[active]` per turn. |

---

## 9. If I ran this again tomorrow

1. **Append one line per turn to disk.** The single highest-value change here (§6). Everything lost
   today was preventable for under a second per turn.
2. **Read task comments and review history before the first keystroke** (§5).
3. **Cap tool-hang retries at two**, then escalate (§7).
4. **Verify `[active]` on the chosen letter at pick time**, per turn — the end sweep cannot catch
   this (§8).
5. **Pick topics that can hold 12 turns honestly**, and stop when done rather than at a number (§2).
6. **Front-load constraints into the opener and pre-empt the obvious answer by turn 2** (§3).
7. **Never break a near-tie on formatting** (§4).
