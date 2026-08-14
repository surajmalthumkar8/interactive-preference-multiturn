# LESSONS — every miss becomes structure

Append-only. One entry per flag, rejection, or self-caught mistake, written **before the next
task** (`../workflows/FIX_TASK.md`). Never delete an entry; supersede it with a newer one.

Entry format:

```
## <date> — <one-line symptom>
**Task:** <task id>
**What happened:** <facts, no interpretation>
**Root cause:** <the actual mechanism>
**Owning step:** <RUN_TASK step + agent>
**Rule edit:** <file + what changed>
**Recurrence check:** <what would now catch it>
```

---

# Carried forward from the previous system (pre-production)

These were learned on the SxS Interactive pipeline in July 2026 and re-verified against the
current guidelines. They are here because they cost something to learn the first time.

## 2026-07-30 — Long prompts errored both response panels
**What happened:** 43-, 49-, and 57-word opening prompts caused both panels to error;
everything at or under 31 words generated cleanly (7 for 7).
**Root cause:** platform-side generation limit, not a rule.
**Status now:** ⚠️ **Unverified on the current Feather campaign.** The 08-12 guidelines
actively publish 70- and 130-word examples and encourage pasting entire documents, so either
the limit was lifted or it never applied to this campaign. **Treat as a live unknown:** if a
long opener errors twice, shorten it and resample rather than assuming a content problem. Do
not pre-emptively cap prompts at 31 words — that would contradict the client's own examples.

## 2026-07-30 — Injected typos are their own fingerprint
**What happened:** deliberately added corruption-class typos ("helppp", "explaination") read as
manufactured mess.
**Root cause:** real typos are omissions (dropped apostrophes, lowercase, missing punctuation);
invented ones are additions, and additions are stylistically consistent in a way real slips are
not.
**Rule:** `../rules/AUTHENTICITY_RULES.md` §3 — omission class only. Strip AI polish, never add
fake damage. Retyping the turn by hand is the safest humanization pass.

## 2026-07-xx — A defect both responses share decides nothing
**What happened:** a blind auditor flagged a real defect in B; A carried the identical defect;
it was nearly credited as a differential (task 977).
**Root cause:** blind auditors see one response, so a genuine flag can still be non-differential.
**Rule:** `../rules/PREFERENCE_RULES.md` §3 — shared-defect neutralize, cross-check the
counterpart before any flag earns weight.

## 2026-08-13 — The guidelines file contradicts itself on turn count
**What happened:** the same file states both min 1 / max 10 and min 10 / max 15.
**Root cause:** the 08-12 revision was edited in place over the 07-28 text and the superseded
passages (GL:134, 162, 172, 229) were never stripped.
**Rule:** `../rules/TURN_RULES.md` §1 — 10 floor, 15 ceiling, stale lines named explicitly.
**Recurrence check:** if a future revision appears, reconcile the whole system before working
(`../workflows/RUN_TASK.md` step 0).

## 2026-08-13 — Two billing-critical steps exist only inside an image
**What happened:** the copy-URL-after-claim and paste-into-`Attempt URL` steps are absent from
the written procedure (GL:367–435) and appear only in the final flowchart image — which is
embedded as base64, so it is invisible to text search and grep.
**Root cause:** reading the prose is not reading the guide.
**Rule:** `../workflows/CLAIM_TASK.md` — the full sequence, with the image-only steps flagged.
**Recurrence check:** when a new doc arrives, extract and read every embedded image before
trusting a grep.

## 2026-08-14 — AI drafting policy reversed
**What happened:** leadership posted a Slack update permitting AI (including Claude Code) to
help write prompts and turns, provided the output is humanized.
**Status:** reported by Suraj, **not independently verified against the platform**. The
screening's Quality Standards Q2 still lists "ask an AI to generate a prompt, then paste it" as
a wrong answer, and it is unknown whether the screening doc was updated.
**Rule:** `../rules/AUTHENTICITY_RULES.md` §0 — allowed, humanization mandatory, sourcing
preference order unchanged.
**Recurrence check:** if quality or removal issues ever surface, this mismatch is the first
place to look.

---

# Production tasks

## 2026-08-14 — A response's stated total contradicted its own line items
**Task:** Feather SxS Conv 55 (rent renewal), user turn 10
**What happened:** response A listed six moving-cost line items summing to ~$4,280–$6,550, then
stated the total as "$2,300–$5,000" — a ~$2,000 gap against its own numbers. Its break-even claim
of 9–20 months is 17–26 months on its own inputs. B's total tracked its line items and was hedged
"in most cases". This decided the pick.
**Root cause:** the derived-number check was being run against *external* facts (is +$340 on
$2,450 really 13.88%). A response can be internally self-contradictory with no external fact to
check it against — stated total vs listed parts is a second, separate check, and everything
computed *from* the total inherits the error.
**Owning step:** `RUN_TASK.md` C1 `mt-response-auditor` (missed on the blind pass), caught at C3.
**Rule edit:** PENDING — `../rules/PREFERENCE_RULES.md` §2 step 1: add "re-sum every stated total
against the response's own line items, then re-derive anything computed from that total
(break-even, payback, monthly equivalent)". This extends legacy `GOLD_PATTERNS.md` §8b, which
covers only numbers the user never supplied.
**Recurrence check:** any response carrying a list of numbers plus a total gets both checks — the
total against its parts, then the figures derived from the total.

## 2026-08-14 — A two-questions-in-one-sentence bundle is a checkable defect, not a style preference
**Task:** Feather SxS Conv 55, user turn 8 (Feather index 14)
**What happened:** the turn needed two answers back from the landlord — the counteroffer and the
notice deadline. B fused both into one sentence with "and also"; A gave each its own sentence and
paragraph. That was the entire differential; A was picked.
**Root cause:** it was nearly filed under clarity/organization (decision order step 6) and
therefore nearly discounted as taste. It belongs at step 3, goal advancement: a recipient who
answers the first half of a compound question and drops the second is a real downstream failure —
here, a missed deadline with an auto-renew behind it.
**Owning step:** `RUN_TASK.md` C2 `mt-preference-judge`.
**Rule edit:** PENDING — `../rules/PREFERENCE_RULES.md` §2 step 3: when a turn requires two things
of a third party, check that each gets its own sentence or paragraph. A bundled ask scores as
goal advancement, not clarity.
**Recurrence check:** count the asks the user's turn implies, then count the sentences carrying
them in each response. Fewer sentences than asks is a flag.

## 2026-08-14 — Rule-of-three filler clusters on the closing turn
**Task:** Feather SxS Conv 55, user turn 11 (final)
**What happened:** at the close one response produced three bullets whose third ("stick to your
max") restated a point already made three-plus times earlier in the same conversation. The other
gave one still-open item (the lease deadline) plus a concrete offer. Picked the latter.
**Root cause:** by the closing turn the substantive advice is exhausted, so a model reaching for a
third bullet can only restate. The filler is predictable by **position in the arc**, not by topic
— and redundancy against turn 4 is invisible if the bullet is only checked against turn 11.
**Owning step:** `RUN_TASK.md` C1 `mt-response-auditor`; `MODE END` E1–E2.
**Rule edit:** PENDING — `../knowledge/REVIEWER_MODEL.md`: on any wrap-up pair (turn ≥10), trace
each bullet to its first appearance in the thread. Restating settled advice is redundancy, not
reinforcement.
**Recurrence check:** closing-pair audits check bullets against the whole conversation, not just
the current turn.

## 2026-08-14 — The compliance auditor blocked on a missing state file while the turn text was clean
**Task:** Feather SxS Conv 55, at user turn 8
**What happened:** `mt-compliance-auditor` returned BLOCK mid-task because
`sessions/rent-negotiation_state.md` did not exist. The turn itself had zero findings. Creating
the file retroactively cost a full extra round trip under a running claim clock.
**Root cause:** the state file was treated as write-up to be done later. The rule already exists
and is already marked BLOCKING (`RUN_TASK.md` step 1, "load or create … at intake") — it was not
followed, and nothing between step 1 and C7 notices the file is absent, so the cost lands as late
as possible.
**Owning step:** `RUN_TASK.md` step 1 (intake).
**Rule edit:** PENDING — `RUN_TASK.md` S1 and C6: state the auditor's precondition inline, "no
state file ⇒ C7 BLOCKs regardless of turn quality", so the cost is visible at the step that skips
it rather than eight turns downstream.
**Recurrence check:** the state file is created at turn 1, before `mt-topic-scout` is dispatched.

## 2026-08-14 — Feather's message index is not the user-turn number
**Task:** Feather SxS Conv 55
**What happened:** Feather numbers every message, user and model alike. User turn *n* appears at
index **2n − 2** — turn 1 at index 0, turn 8 at index 14. Cross-checking "how many turns so far"
against the visible indices reads as roughly double the real count.
**Root cause:** turn counting is documented only in user-turn terms; the UI's own numbering is
undocumented, so the two get compared directly and the count comes out wrong in the direction that
looks safe (over the minimum when it is not).
**Owning step:** `RUN_TASK.md` C6; `../checklists/PRE_SUBMIT_CHECKLIST.md` count verification.
**Rule edit:** PENDING — `../rules/TURN_RULES.md` §1: add the mapping beside the 10/15 table —
`user turn n = Feather index 2n − 2`, and `(highest index ÷ 2) + 1 = user-turn count`.
**Recurrence check:** the count comes from the state file's turn log, never from the visible index.

## 2026-08-14 — Topic brushed two of the client's five banned example scenarios, with no collision verdict on record
**Task:** Feather SxS Conv 55
**What happened:** the topic was assistant-picked — Suraj had no real history to hand that
session, a disclosed exception to `../rules/AUTHENTICITY_RULES.md` §1, not an accident. The
scenario (email a landlord about a lease renewal, firm but "must not sound whiny", draft supplied
and refined) sits close to the client slide's Writing/Professional example: *"I need to tell my
landlord our lease broke down but I want to sound firm without being rude. Here's the draft."*
`PROMPT_SPECTRUM.md` names that scenario off-limits twice, explicitly. The arc — negotiate $340
down to $150, "what's a good approach" — also mirrors the Personal/Situational example's shape.
Neither collision has an S1 verdict recorded in the state file.
**Root cause:** the two documents that make this checkable — `PROMPT_SPECTRUM.md` (five
categories, five banned scenarios, category rotation ledger) and `GOLD_PATTERNS.md` — exist only
inside `Interactive_contri_inst/`, the legacy tree flagged stale and off-limits. The live system
has no copy, so the duplicate check at S1 had no in-system source for the banned list and the
check silently reduced to "is the wording different".
**Owning step:** `RUN_TASK.md` S1 `mt-topic-scout` (duplicate check).
**Rule edit:** PENDING — port the binding parts of
`Interactive_contri_inst/system/knowledge/PROMPT_SPECTRUM.md` into `../knowledge/` and cite it
from `TOPIC_PLAYBOOK.md` §5. Until that port lands, S1 must read the legacy file explicitly
despite the tree being otherwise off-limits.
**Recurrence check:** S1 returns a named verdict against each of the five client example scenarios
(contractor quote, landlord lease, cortisol, product naming, Node.js race condition) and the
verdict is written into the state file before turn 1.
**Severity:** not a confirmed duplicate — the specific need genuinely differs (a rent-increase
counteroffer vs a broken lease). Logged so that if a reviewer ever flags Conv 55 there is a
written history. GL:56 duplicates are removal offence #1; this deserved an explicit verdict and
did not get one.

## 2026-08-15 — A delivered, closed task left its state file reading OPEN for a full day
**Task:** Feather SxS Conv 101 (cron retry policy), sxs-101
**What happened:** the task ran to turn 12 of a planned 12, the close-out message went to Suraj on
2026-08-14 (final pick, "send nothing further", Feather Mark as Complete → Vercel Submit Task, and
the 12-turn checklist). `sessions/cron-retry-bug_state.md` was still `Status: OPEN` /
`Current turn: 12` on 2026-08-15. Turn 12 had no Turn log row, the Pick record table was empty for
all twelve turns, the Rotation guard still read "(none yet)" and "no picks yet", and no
`PROMPT_LOG.md` row existed. A fresh session reading the file would have concluded the task was
mid-flight and resumed writing turn 13 — into a conversation already submitted, past the 15
ceiling's only safe margin and straight into the padding removal trigger.
**Root cause:** the close-out bookkeeping is a *single* dispatch (`MODE END` E3
`mt-session-scribe`) that runs after the deliverable is already in Suraj's hands. Once the useful
output has shipped, nothing downstream depends on E3, so when the dispatch was skipped or lost
across a context compaction there was no consumer to notice its absence. The same failure shape as
2026-08-14's compliance-auditor BLOCK: state-file work deferred until after the thing that would
have caught it. Per-turn updates have a natural checker (the next turn reads the file); the final
update has none.
**Owning step:** `../workflows/RUN_TASK.md` `MODE END` E3 (`mt-session-scribe`).
**Rule edit:** `RUN_TASK.md` `MODE END` — E3 moves **before** the close-out message to Suraj, not
after, and the close-out message is not sent until the scribe returns. Add to E3's exit criteria
that the state file must read `Status: CLOSED` and carry a Turn log row for the final turn, and
that the `PROMPT_LOG.md` row is appended in the same dispatch. Add to `RUN_TASK.md` step 0
(session sync): scan `sessions/*_state.md` for any file whose `Current turn` equals its
`Planned turn count` while `Status` is still OPEN, and resolve it before starting new work.
**Recurrence check:** step 0 of every session surfaces a stale-OPEN state file, so the gap is
caught at the next session start at the latest instead of by chance. A task cannot be reported
closed to Suraj before its state file says CLOSED.

## 2026-08-15 — The "archive the opener text" fix was written down and then not done, twice
**Task:** Feather SxS Conv 101 (repeat of the same miss at Conv 55)
**What happened:** `PROMPT_LOG.md`'s rotation state after task 1 said "archive the exact opener
text in the state file at turn 1 from now on". Conv 101 recorded the opener's *shape* ("bare noun
phrase → symptom → ask → paste") and word count, but not its words. Both log rows now carry an
unusable Opener column.
**Root cause:** the instruction was parked in the rotation-state prose of a *different* file from
the one being written at turn 1, and the state template's Turn log has a column for opener shape
but none for opener text — so following the template correctly still loses the text. A fix written
somewhere other than the artefact it governs is not a fix.
**Owning step:** `../workflows/RUN_TASK.md` step 1 / turn 1 (`mt-session-scribe` per-turn update).
**Rule edit:** `../templates/STATE_TEMPLATE.md` — add a required "Opener (verbatim, as typed into
Feather)" field to the Topic block, so the text is captured by the template rather than by memory
of an instruction filed elsewhere. `PROMPT_LOG.md`'s duplicate-check procedure step 1 already
assumes this text exists; it cannot run without it.
**Recurrence check:** the duplicate check at S1 fails loudly on any log row whose Opener column
reads `unknown`, instead of quietly degrading to "is the wording different".

## 2026-08-14 — AI-drafting reversal: live rules already reconciled (addendum, verification only)
**Task:** Feather SxS Conv 55 close
**What happened:** swept the live rule set for language predating the 2026-08-14 Slack reversal.
None found. `../rules/AUTHENTICITY_RULES.md` §0 carries the new policy; §1's banned-sourcing table
already reads "AI may *help draft*, but pasting raw model output is still wrong — it must be
humanized and grounded in a real need"; `Interactive_contri_inst/LEGACY_README.md:23` records the
lift for the legacy tree. No contradictory guidance is sitting in place.
**Root cause:** n/a — verification, not a miss.
**Owning step:** `RUN_TASK.md` step 0 session sync.
**Rule edit:** none required. Two things did **not** move and are the live constraints: sourcing
order (reuse > adapt > invent) and GL:180 stylometry. Conv 55 ran fully under the new policy —
every turn drafted with assistance, humanizer gate on each, Suraj picking and approving.
**Recurrence check:** if a quality or removal flag ever cites AI-written prompts, the unverified
surface is the screening doc's Quality Standards Q2, not this repo.
