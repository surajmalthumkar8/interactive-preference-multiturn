# PROMPT LOG — every opening prompt we have used (anti-repetition ledger)

Checked at MODE START. **Rotation now runs on FOUR axes** (2026-07-28 guide: "Vary
your topics, complexity levels, prompt lengths, and styles across tasks"). Pick the
least-recently-used combination; never reuse a scenario/artifact/detail already
listed. Reference-task prompts are pre-seeded so we never accidentally clone them.

- **Complexity:** lookup · single task · multi-step · open dilemma
- **Length band:** micro (1–8 w) · short (9–45 w) · rambling (45–120 w) · pasted
- **Turns:** the final user-turn count (1 is valid and wanted sometimes)

| Date | Task | Domain | Complexity | Length | Turns | Status | Opening line (short) |
|---|---|---|---|---|---|---|---|
| (ref) | task-1 | writing help | single task | short | 5 | ref | cancel dinner with friend, honest not dramatic |
| (ref) | task2 | coding | open dilemma | short | 3 | ref | DSA interview in 15 days, weak at DSA |
| (ref) | task3 | factual/explaining | lookup | micro | 4 | ref | Clash Royale launch date |
| (ref) | task4 | planning | multi-step | short | 3 | ref | weekly routine, ask me questions first |
| (ref) | task5 | planning | multi-step | short | 3 | ref | tomorrow's workday, 4 priorities + gym |
| (ref) | task6 | coding | single task | pasted | 3 | ref | Django fields.E304 reverse accessor paste |
| 2026-07-24 | task 977 | brainstorming | open dilemma | short | 4 | CLOSED (superseded) | dad's 60th gift, ~$100, anti-clutter, experience lean |
| 2026-07-24 | task 172 | summarizing/explaining | multi-step | short | 4 | **CLOSED** 2026-07-31 | new job health plan, deductible vs coinsurance vs out of pocket max |
| 2026-07-24 | task 33 | coding | multi-step | short | 4 | **CLOSED** 2026-07-31 | 3gb csv blows up RAM in pandas, filter status=failed without loading whole file |
| 2026-07-31 | task 3154 | personal/situational | open dilemma | short (27/29/20 w) | **3**, ENDed on resolution | **CLOSED** 2026-07-31 | 2800 transmission on a 2013 worth 4000, repair or junk it |
| 2026-07-31 | task 3252 | **writing/professional** | **single task** | short (27 w) | **2**, ENDed on resolution | **CLOSED** 2026-07-31 | one more week on a report due Friday, word it without sounding like an excuse |
| 2026-07-31 | task 3260 | **factual/explaining (personal finance)** | **lookup** | short (23/20 w) | **2**, ENDed on resolution | **CLOSED** 2026-07-31 | roth vs traditional IRA in plain terms, 28 and just started saving |

**Retroactive closures (2026-07-31).** Tasks 172 and 33 were delivered and submitted on
2026-07-29 but never formally closed — their state files sat at `[OPEN]` with `_pending_`
turn rows even though all four turns of each had shipped. Closed now. Their ledgers stay
incomplete on the record (task 33's ledger still shows the 49-word T1 *first attempt*
that errored, not the 31-word version actually sent). Lesson carried into the checklist:
the state file is updated BEFORE the deliverable goes out, and closure is a step, not a
side effect of moving to the next task.

## ⚠ THE ROTATION LEDGER IS A TIEBREAKER, NOT A GENERATOR (added 2026-07-31, task 3260)

Task 3260's first plan was built backwards from this gap list: a `[raw-paste]` lease
clause chosen because it closed two named gaps at once. It passed the humanizer AND the
validator. **Suraj rejected it on sight** and asked for a plain short prompt. The
replacement (roth vs traditional IRA, 23 words) worked first time.

The gap list had started steering the work instead of serving it. Cost: three agent
dispatches, a full reviewer-simulator cycle, and a discarded turn, on a session where
Suraj had already said "do it faster" twice.

**Binding, from now on:** generate candidate prompts from "what would a real person
actually type", THEN use this list to break ties between them. Never the reverse. If a
prompt needs a paragraph of justification, it is the wrong prompt. A gap staying open
for another task is a cheaper failure than an inauthentic prompt shipping.

## Standing gaps to close (updated 2026-07-31 after task 3154)

**Closed by task 3154:** the personal/situational category gap (a real non-professional
life decision, first of its kind for us).

**Still open — pick from these next:**
- a **micro / lookup / 1-turn** task (guide examples "mitosis??", "should i get
  organic berries?") — and actually END at one turn, do not inflate it. This is now the
  oldest open gap; it has been deferred three tasks running.
- a **pasted-context** task (guide examples #8 meeting notes, #13 n8n code) — short
  framing plus untrimmed paste, with the paste itself kept small enough to send.
- **Writing/Professional** — the last unused PROMPT_SPECTRUM category. Combine it with
  the micro/1-turn gap if the scenario allows.

**Retired gap — "a rambling 60–130 word personal-decision task".** This was listed on
07-28 and is now **unreachable**: the 07-30 one-or-two-liner rule caps prose at 35 words
because the platform errors above it (see AUTHENTICITY_RULES). The guide's rambling
examples describe the ideal; the platform forbids it. Length variety now lives inside
micro (1–8) vs short (9–30) vs pasted, not in a rambling band. Do not re-add this gap.

**Complexity monoculture — live warning.** Our four tasks are open dilemma, multi-step,
multi-step, open dilemma. Zero **lookup** and zero **single task**. Turn counts are 4,
4, 4, **3** — task 3154 was the first to break the 4-turn run, by ending on resolution
rather than by design. Complexity is still a monoculture on an axis the guide names
explicitly. The next task should break it: a lookup or single-task prompt that genuinely
ends in 1–2 turns.
