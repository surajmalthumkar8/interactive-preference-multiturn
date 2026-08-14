# PROMPT LOG — the duplicate ledger and the variety ledger

Two jobs:

1. **Duplicate prevention.** Reusing or paraphrasing a prompt across tasks is removal offence #1
   (GL:56). Every submitted opener gets logged here so the next one can be checked against it.
2. **Variety enforcement.** GL:56 and screening Q3 score variation across domain, complexity,
   length, and style. Consecutive tasks must rotate on ≥3 axes
   (`../knowledge/TOPIC_PLAYBOOK.md` §5).

Append one row per submitted task. Never edit a past row.

---

## Log

| # | Date | Task ID | Domain | Shape | Register | Len band | Turns | Opener (first 8 words) | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-08-14 | Feather SxS Conv 55 · `general-multi-turn / 2026-08-12 13:13:39` | personal/situational — money & negotiation (rent renewal) | decision → document (counteroffer email) → refinement | personal decision, unresolved — lowercase starts, run-ons | unknown | 11 | "my landlord just told me rent's going up" | assistant-picked topic, not history-sourced; scenario adjacency — see flags |
| 2 | 2026-08-14 | Feather SxS Conv 101 · `side_by_side_conversation / 2026-08-12 13:13:39` | Technical/Coding — cron job retry policy | debugging → classification/policy decision → build → test | work task in a known domain — blunt/jargon-dense (T1–T2), plainer-casual from T3 | default framing (~30 words) + untrimmed paste | 12 | **unknown — opener text never archived** (state file records only its shape: bare noun phrase → symptom → ask → paste) | assistant-constructed topic per the disclosed exception; **second consecutive invented topic that session** — next task must prefer real history or close the gap. Delivered/closed 2026-08-14; state file finalized 2026-08-15 |

*(The pre-production placeholder row was replaced, not edited — it recorded no task. Rows 1+ are
append-only from here.)*

State file: [`sessions/rent-negotiation_state.md`](../../sessions/rent-negotiation_state.md) —
full pick table, constraint ledger, and per-turn differentials live there, not here.

### Flags on task 1 (raise before the next task)

1. **Provenance — topic was assistant-picked, not sourced from Suraj's history.** He had no real
   prompt on hand that session, so the scenario was invented. This is a *disclosed, deliberate*
   exception to `../rules/AUTHENTICITY_RULES.md` §1 (own history → scrub → paste), which permits
   "something genuinely needed right now" but not an invented situation. Do **not** count this row
   as equivalent to a history-sourced prompt for GOLD_PATTERNS rotation purposes. Flagged for
   review, not treated as settled.
2. **Category rotation is thin on this axis.** Personal/Situational was already spent on task 3154
   (repair vs junk a 2013 car). This is the second. Per `PROMPT_SPECTRUM.md` §"Rotation",
   **Writing/Professional remains the only unused category and is still the priority gap** — take
   it next, ideally as a micro/lookup shape to close two gaps at once.
3. **Scenario adjacency to the client's own banned examples.** The landlord + lease + "firm but not
   whiny" + here's-the-draft framing sits close to the slide's Writing/Professional example, which
   `PROMPT_SPECTRUM.md` names twice as off-limits; the "negotiate $340 down to $150, what's a good
   approach" arc mirrors the Personal/Situational example's shape. No S1 collision verdict is on
   record. Not a confirmed duplicate — the specific need differs — but see LESSONS 2026-08-14.

### Flags on task 2 (raise before the next task)

1. **Provenance — second consecutive assistant-constructed topic.** Suraj again had no real prompt
   to hand, so the cron-retry scenario was built rather than sourced. Same disclosed exception to
   `../rules/AUTHENTICITY_RULES.md` §1 as task 1, but two in a row is a pattern, not an exception.
   **Next task: source from real history, or state plainly that the gap could not be closed.** Two
   invented topics do not count as two history-sourced rows for rotation purposes.
2. **Opener text was never archived — the fix from task 1 did not land.** Task 1's rotation state
   already said "archive the exact opener text in the state file at turn 1 from now on". It was not
   done for task 2 either, so the duplicate-check procedure below (step 1, "read every opener in the
   log") now has **two** rows it cannot actually read. This is the highest-priority mechanical fix.
3. **Category rotation.** Technical/Coding is now spent twice (legacy task 33, Conv 101).
   Writing/Professional is still the only unused client category and was explicitly deferred to the
   *next* task by `mt-topic-scout` — that deferral is now due.
4. **Pick-sequence discrepancy at turn 4** between the close-out report (B) and the live turn log
   (A). Recorded in `sessions/cron-retry-bug_state.md` Open issues, unresolved. Affects the ledger
   only, not the submitted data.

---

## Rotation state (update after every task)

*(Superseding update after task 2 — Conv 101. Task 1's block is preserved below for history.)*

- **Last domain:** Technical/Coding — cron job retry policy
- **Last shape:** debugging → classification/policy decision → build → test
- **Last register:** work task in a known domain — blunt and jargon-dense without gloss (T1–T2),
  plainer-casual from T3 at Suraj's request
- **Last length band:** default framing (~30 words) + untrimmed paste. **Opener text still not
  archived** — the task-1 fix did not land; see flag 2 above. Archive the exact opener text in the
  state file at turn 1, no exceptions.
- **Last turn count:** 12
- **Domains not yet used:** writing · study/learning · planning · health/admin · hobby
  *(code now spent; document work partially touched at task 1 but was not that task's domain)*
- **Shapes not yet used:** refinement · practitioner · planning
  *(decision spent at task 1; debugging and build/test spent at task 2)*
- **Client categories** (`../knowledge/` has no copy — authority is
  `Interactive_contri_inst/system/knowledge/PROMPT_SPECTRUM.md`, in the otherwise-stale legacy
  tree): **Technical ✓✓ (legacy 33, Conv 101)** · Personal/Situational ✓✓ (3154, Conv 55) ·
  Creative ✓ · Explaining ✓ · **Writing/Professional — still unused, highest priority next, and
  now explicitly due after being deferred from Conv 101.**
- **A/B streak:** task 2 picks were B B B B A B A B B A B B (A×3, B×9), longest run four B at
  turns 1–4, closed on two B. ⚠️ Turn 4 is disputed — the live turn log records A, which would make
  it A×4/B×8 with a longest run of three; see flag 4. **Cumulative across both tasks** (23 picks):
  B A A A B B B A B B B · B B B B A B A B B A B B — A×7, B×16 on the close-out reading. Slots are
  randomized per comparison, so a streak carries no signal — noticed, not acted on.

<details>
<summary>Rotation state as of task 1 (superseded, kept for history)</summary>

- **Last domain:** personal/situational — money & negotiation (rent renewal)
- **Last shape:** decision → document (counteroffer email) → refinement
- **Last register:** personal decision, unresolved — lowercase starts, run-ons, real emotion
- **Last length band:** unknown — the opener was not archived in full, only its first line.
- **Last turn count:** 11
- **Domains not yet used:** code · writing · study/learning · planning · health/admin · hobby
- **Shapes not yet used:** refinement · debugging · practitioner · planning
- **Client categories:** Technical ✓ · Personal/Situational ✓✓ (3154, Conv 55) · Creative ✓ ·
  Explaining ✓ · Writing/Professional unused.
- **A/B streak:** picks were B A A A B B B A B B B (A×4, B×7), longest run three.

</details>

## Duplicate check procedure (run before every new task)

1. Read every opener in the log.
2. Ask not "is the wording different" but **"is this the same need"** — paraphrase counts as
   duplicate.
3. Check the *shape* too: five different topics all run as refinement arcs read as one
   contributor with one habit, which is the stylometry risk (GL:180), not just a variety miss.
4. If in doubt, pick another topic. Duplicates are a removal offence; passing on a topic costs
   nothing.
