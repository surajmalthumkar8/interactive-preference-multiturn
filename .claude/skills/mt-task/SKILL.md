---
name: mt-task
description: Run an MAI Interactive Preference Multi-Turn task end to end. Use whenever Suraj pastes task content from Feather — a task intro, an A/B response pair, a single continued response — or asks for an opening prompt, a follow-up turn, a preference pick, a pre-submit check, or the claim sequence. Enforces the 10-15 turn regime, the capability gate, and the mandatory humanization pass.
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Agent, Skill
---

# MAI Multi-Turn — task runner

You are running a live annotation task. Suraj is at the platform; you produce the words and the
decisions, he types and clicks. **No preamble, no explanation he did not ask for.** Deliverable
format: `system/templates/DELIVERABLE_TEMPLATE.md`.

## Read before acting (every session, not from memory)

1. `PROJECT_KNOWLEDGE.md` — the reconciled manual. It outranks the raw guidelines file, which
   contradicts itself.
2. `system/workflows/RUN_TASK.md` — the pipeline you are executing.
3. `system/rules/` — TURN, CAPABILITY, AUTHENTICITY, PREFERENCE, WORKFLOW. All binding.
4. `system/learning/PROMPT_LOG.md` and `LESSONS.md`.
5. `sessions/` — any OPEN state file (possibly from the other laptop).

## The five facts that decide most questions

1. **10 turns minimum, 15 maximum.** Turn 1 is the opening prompt. The guidelines file still
   contains 07-28 text saying one turn is fine (GL:134, 162, 172, 229) — **all of it is stale**.
2. **Padding to reach 10 is a removal offence.** The sanctioned fix for a conversation that runs
   dry early is to **go back and enrich earlier turns**, never to add a forward filler.
3. **The model has no web, no real-time data, no files, no images, and a July 2025 cutoff.**
   Paste content, never point at it.
4. **Every turn must engage the specifics of the previous response.** A follow-up that could
   have been written without reading the response is a defect even when it is on-topic.
5. **Every turn needs a recorded preference**, verified by `↳` on the chosen side. A single
   missing selection invalidates the whole conversation.

## Mode routing

| What Suraj pasted | Mode | Do |
|---|---|---|
| A task intro / "start a task" / a topic | START | `mt-topic-scout` → `mt-turn-writer` → capability gate → `mt-humanizer` → `mt-compliance-auditor` → deliver |
| An A/B pair | COMPARE | `mt-response-auditor` ×2 **blind, in parallel, in one message** → `mt-preference-judge` → adjudicate → `mt-turn-writer` (chosen response only) → capability gate → `mt-humanizer` → `mt-compliance-auditor` → deliver |
| One response, no pair | SINGLE | same as COMPARE minus the pick |
| "wrap it up" / arc complete at turn ≥10 | END | final pick if a pair is showing → full `PRE_SUBMIT_CHECKLIST.md` sweep → submit instructions |
| "task not found", a failed panel, a claim question | OPS | `system/workflows/CLAIM_TASK.md` |

After every delivered turn, dispatch `mt-session-scribe` to update `sessions/<task-id>_state.md`.

## Blocking gates — never waived

- **Capability gate** — inline, after every draft. Any web / real-time / file / image /
  post-July-2025 assumption ⇒ rewrite or redraft.
- **Humanization gate** — `mt-humanizer` runs the `humanizer` skill on every turn and every
  reason line. `HUMANIZATION: PASS` or it does not ship.
- **Dependency gate** — the turn must quote its anchor in the previous response.
- **Turn-count gate** — below 10, `END` is unavailable; the only legal exits are another real
  turn or `BACKTRACK`.
- **Completeness gate** — never judge a blank, truncated, or unpaired response. Ask for a
  Resample ↺ instead.

## Detailed procedure

Follow `system/workflows/RUN_TASK.md` step by step — S0–S6, C1–C8, E1–E3. Do not compress it
because a turn looks obvious.

## Hard reminders for the deliverable

- Tell him to **type** the turn into Feather, not paste it.
- Give the turn number as "turn N of planned M (10–15)".
- Never include the losing response's content or the judge's internal reasoning.
- Never use rubric words ("comprehensive", "well-structured") in a reason line.
