# WORKFLOW RULES — how the assistant runs a task (BINDING)

Governs the pipeline in `../workflows/RUN_TASK.md`. Platform clicks stay on Suraj's side;
drafting, judging, and verification are the assistant's.

---

## 1. Division of labour

| Suraj does | The assistant does |
|---|---|
| Claim / release in Vercel + Feather | Draft the opening prompt and every follow-up |
| Paste the task intro, then each A/B pair | Judge each pair with reasons and evidence |
| **Type** every user turn into Feather | Track state, turn count, constraints, variety |
| Click the preference, verify `↳` | Run the compliance gate before submit |
| Submit / release | Log lessons and prompt history |

**Type, don't paste, into the platform.** Keystroke telemetry on a task that is supposed to be
hand-written is a needless risk, and retyping *is* the humanization pass (AUTHENTICITY_RULES §3).

---

## 2. Compulsory execution

Every step of `RUN_TASK.md` runs on every paste, in order, however obvious the pick or simple
the turn. Nothing is skipped for speed. The specific gates that are **blocking**:

| Gate | Owner | Blocks on |
|---|---|---|
| Capability gate | inline + `mt-turn-writer` | any web/real-time/file/image/post-July-2025 assumption |
| Humanization gate | `mt-humanizer` | any turn that has not been through the `humanizer` skill |
| Dependency gate | `mt-turn-writer` | a turn with no quotable anchor in the previous response |
| Duplicate gate | `mt-topic-scout` | a topic overlapping anything in `PROMPT_LOG.md` |
| Turn-count gate | `mt-compliance-auditor` | ending below 10, exceeding 15, or any padded turn |
| Selection gate | `mt-compliance-auditor` | any turn without a recorded `↳` selection |

A failed gate loops back to the owning step. It never gets waived.

---

## 3. Completeness gate on intake

A pasted response that is blank, truncated mid-sentence, or missing its pair ⇒ **stop and ask**.
Mention Resample ↺ if a panel failed. Never judge a partial pair, never guess the missing side.

---

## 4. Blind auditing

The two response auditors run **blind and in parallel**: each sees the conversation history and
**one** response only, with no mention of the other response, no comparison, and no leaning.
Only `mt-preference-judge` sees both. This is what keeps the audits independent enough to be
worth cross-checking.

The turn writer receives the **chosen** response only — never the loser, never the judge's
reasoning. It reacts to what "its" assistant said, the way Suraj will.

---

## 5. State

One state file per task at `../../sessions/<task-id>_state.md`, from
`../templates/STATE_TEMPLATE.md`. Updated every turn, never at the end. It carries the turn
counter, the constraint ledger, the anchor history, the register/imperfection rotation, and the
pick record.

Commit and push `sessions/` and `system/learning/` after every working session so state moves
between laptops. `git pull` before starting on the other machine.

---

## 6. Failure discipline

A flag, a rejected task, or a caught mistake ⇒ run `../workflows/FIX_TASK.md`, then write a
`LESSONS.md` entry naming the root cause, the owning step, and the rule edit — **before** the
next task. Every miss becomes structure. No miss repeats.

---

## 7. Escalation

Project or quality question ⇒ **check the FAQ first**, then post a Slack thread (screening Q7).
Operational failure (can't access, can't claim, can't submit) ⇒ Get Help → Operational Issue.
Payments ⇒ `#all-trainer-hub`, never the project channel. Never DM a QM. English only.
