# WORKFLOW: RUN_TASK — the primary loop

**Trigger:** Suraj pastes task content — a task intro, an A/B response pair, a single continued
response, or "wrap it up". The assistant runs this pipeline and returns a deliverable per
`../templates/DELIVERABLE_TEMPLATE.md`. Platform clicks (claim, select, type, Resample ↺,
submit) stay on Suraj's side.

**Compulsory** (`../rules/WORKFLOW_RULES.md`): every step, in order, every paste. Nothing is
skipped, however obvious the pick or simple the turn.

**Source of truth:** `PROJECT_KNOWLEDGE.md` (reconciled) over
`MAI Interactive — Multi-Turn Guidelines (updated 08_12).md` (raw, internally contradictory).
Turn range **10–15**. Capability limits are a blocking gate on every user-side message.

---

## Step 0 — Session sync (first task of a session only)

- Read `../learning/LESSONS.md` and `../learning/PROMPT_LOG.md`.
- Check `sessions/` for an OPEN task state left from the other laptop.
- Confirm the guidelines file on disk is still the **08-12** revision. If a newer one appears,
  reconcile the whole system before working — do not start a task on unreconciled rules.

## Step 1 — Intake, mode detection, state (BLOCKING)

Parse the paste. Load or create `sessions/<task-id>_state.md` from `../templates/STATE_TEMPLATE.md`.

| Mode | Trigger | Steps |
|---|---|---|
| **START** | new task, no responses yet | S0–S6 |
| **COMPARE** | an A/B pair is pasted | C1–C8 |
| **SINGLE** | one response only (no pair shown) | C4–C8, no pick |
| **END** | at turn ≥10 and the arc is complete, or Suraj says wrap up | E1–E3 |

**Completeness gate:** a response that is blank, truncated mid-sentence, or missing its pair ⇒
STOP and ask for the missing piece; mention **Resample ↺** if a panel failed. Never judge a
partial pair.

---

## MODE START — the opening prompt

- **S0 — Ask for real history first.** Before composing anything, ask whether there is something
  genuinely asked of ChatGPT/Gemini/Claude/Copilot recently, or a real current need. If yes,
  **that is the prompt** — scrub PII, leave the mess intact, and skip to S3.
- **S1 (AGENT: `mt-topic-scout`)** Dispatch with the candidate topic (or the request to pick
  one), `PROMPT_LOG.md`, and the rotation state → returns: depth verdict (all four depth-test
  questions), a sketched 10–15 turn arc, the rotation axes moved, duplicate check, and a
  capability read of the **whole planned arc**. A FAIL here means pick another topic — never
  start and hope.
- **S2 (AGENT: `mt-turn-writer`, MODE START)** Dispatch with topic, persona, register, length
  band, and the arc sketch → returns the draft opening prompt.
- **S2b — Capability gate (BLOCKING, inline).** Check the draft against
  `../rules/CAPABILITY_RULES.md`. Any breach ⇒ convert (paste instead of point, drop the time
  anchor) or return to S2.
- **S3 (AGENT: `mt-humanizer`)** Dispatch with the draft + target register → corpus-voice final
  text. **Always runs the `humanizer` skill.** Pasted content is never touched.
- **S4** Write the deliverable + state file. Optional mechanical check:
  `python "Interactive_contri_inst/tools/validate_sxs_turn.py" <file>` (legacy tool — its
  capability and voice patterns are still valid; ignore any turn-count verdict it prints).
- **S5 (AGENT: `mt-compliance-auditor`)** Adversarial pass per `../knowledge/REVIEWER_MODEL.md`
  → APPROVE with zero confirmed findings, or loop back to the owning step.
- **S6** Deliver the prompt + the arc note (planned end turn and why). Append to `PROMPT_LOG.md`.
  Dispatch `mt-session-scribe`.

**Deliverable to Suraj:** the prompt to type, the planned arc, and a reminder that this is Turn 1
of a planned N (10–15).

---

## MODE COMPARE — judge the pair, write the next turn

- **C1 (AGENTS: `mt-response-auditor` ×2 — blind, parallel, one message)** One auditor per
  response. Each prompt contains the conversation history plus **that response only**.
  **Firewall: no mention of the other response, no comparison, no leaning.** Each returns claim
  and code verification, a constraint-adherence checklist (current turn **and every earlier
  turn**), a flaw list with quotes, and a goal-advancement read.
- **C2 (AGENT: `mt-preference-judge`)** Dispatch with history, both responses, both audits →
  PICK, decisive differentials with quotes, NEAR-TIE flag, draft one-line reason, bias-guard
  report (`../rules/PREFERENCE_RULES.md`).
- **C3 — Adjudicate (inline, BLOCKING).** Cross-check the judge's decisive facts against both
  audits and the pasted text. Any disagreement on a decisive fact ⇒ re-read before the pick
  stands. Confirm no trap fired (length / format / sycophancy / position). Pick is now FROZEN.
- **C4 (AGENT: `mt-turn-writer`, MODE FOLLOW-UP)** Dispatch with history + **the chosen response
  only** (never the loser, never the judge's reasoning) + state + turn number → returns the next
  user message anchored to a specific element of the chosen response, with the anchor quoted.
  - At turn **<10**: ending is not available. If the thread feels exhausted, the writer returns
    `BACKTRACK` with the earlier turn to rebuild from and what to deepen there — never a filler
    turn (`../rules/TURN_RULES.md` §2–3).
  - At turn **≥10**: the writer may return `END` when a real person would genuinely stop.
- **C4b — Capability gate (BLOCKING, inline).** Same check as S2b.
- **C5 (AGENT: `mt-humanizer`)** Draft turn + draft reason → corpus voice. **Always runs the
  `humanizer` skill.** No content edits after this except by looping back.
- **C6** Update the deliverable and the state file: turn counter, constraint ledger, anchor
  history, register/imperfection rotation, pick record.
- **C7 (AGENT: `mt-compliance-auditor`)** Adversarial pass: does the pick follow from the
  differentials, does the turn react to the chosen response, is the count on track, is
  humanization confirmed → SHIP or loop (voice → C5, pick → C2–C3, turn → C4).
- **C8** Deliver: PICK + reason + next message (or BACKTRACK / END call) + turn status +
  verification summary. Dispatch `mt-session-scribe`.

---

## MODE END — close the task

- **E1** Verify the count is **≥10**. If it is not, this is not END — it is BACKTRACK
  (`../rules/TURN_RULES.md` §2). If a pair is on screen, C1–C3 still run for the final pick.
- **E2 (AGENT: `mt-compliance-auditor`)** Full `../checklists/PRE_SUBMIT_CHECKLIST.md` sweep —
  every turn re-checked for capability, dependency, padding, PII, and a recorded `↳`.
- **E3** Deliver: the final pick, "send nothing further", the submit order (Feather **Mark as
  Complete** → Vercel **Submit Task**), and the checklist result. `mt-session-scribe` closes the
  task: LESSONS + PROMPT_LOG + state archived.

---

## Failure discipline

A flag, a rejection, or a caught mistake ⇒ `FIX_TASK.md`, then a LESSONS entry naming root
cause, owning step, and the rule edit — **before** the next task.
