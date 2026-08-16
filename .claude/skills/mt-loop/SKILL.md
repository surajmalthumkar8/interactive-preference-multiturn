---
name: mt-loop
description: Fast feedback-loop runner for MAI Interactive Preference Multi-Turn. Use when Suraj wants to run a task at speed — he pastes an A/B pair, gets back a pick plus the next turn in one shot, pastes the next pair, and so on. Target 30-40s per turn. Collapses the audit/judge/write chain into a single inline pass and keeps only the mandatory humanization gate as a subagent. Use instead of mt-task whenever throughput matters.
allowed-tools: Read, Agent, Bash
---

# mt-loop — the fast runner

Suraj is at Feather with the clock running. He pastes, you answer, he types, he pastes again.
**Target: 30-40 seconds from his paste to your ship line.**

## Session start, once — then never again this session

Read `system/FASTLOOP.md`. That is the whole rulebook, precompiled. Do not read
`system/rules/*`, `PROJECT_KNOWLEDGE.md`, the guidelines file, `sessions/`, or `PROMPT_LOG.md`
during the loop. They are already compiled into the card. Re-reading them is where the minutes go.

Then say `loop ready` and nothing else. Wait for the paste.

## Per turn — one inline pass, one subagent

1. **PICK** — walk the ladder in FASTLOOP §1, stop at the first rung that separates them, apply
   the wash test and the bias strip. Inline. No `mt-response-auditor`, no `mt-preference-judge`.
2. **REASON** — one line, shape rotated per §2.
3. **WRITE** — anchor quote first, one of the four legal moves, capability scan, voice
   fingerprint, rotation guard. Inline. No `mt-turn-writer`.
4. **GATE** — dispatch `mt-humanizer` with `model: sonnet`, `run_in_background: false`. Send only
   the draft, the register, the previous turn's shape, and the turn number. Never waived, not
   once, not for a turn Suraj wrote himself.
5. **SHIP** — the §5 block. Nothing else.

Steps 1-3 happen in a single thinking pass before any tool call. The gate is the only tool call
in a normal turn.

## Output — exactly this, every turn

```
T7  ↳B   ·  B repeated the same point twice, A got to the fix faster.

<the turn text, verbatim, ready to type>

LEDGER: no bullets · under 200 words · keep Sunday free          [gate: PASS]
```

No preamble. No explanation of the pick unless he asks. No "here's your next turn". No summary
of what you did. He asked for speed, so the words and the letter are the whole deliverable.

If he asks **why**, then give the differential in one sentence, quoting the deciding line.

## What is deliberately not in this loop

`mt-response-auditor` · `mt-preference-judge` · `mt-turn-writer` · `mt-compliance-auditor` ·
`mt-session-scribe` · state files · `PROMPT_LOG.md` · git. Standing instruction from Suraj,
2026-08-15: skip the bookkeeping, just perform. The pre-submit sweep still exists — run
`/mt-check` once at the end of the conversation, not per turn.

## The one thing that is never dropped

The humanization gate. `AUTHENTICITY_RULES.md` §0 makes it the condition attached to the
permission to use AI on this project at all. Skipping it once turns an allowed workflow into a
removal offence. Speed comes from drafting inside the voice fingerprint so the gate passes on the
first try, never from skipping the gate.

## Modes

| He pastes | You do |
|---|---|
| an A/B pair | the five steps above |
| a task intro, or "start one" | FASTLOOP START mode — rotate the domain, four-question depth test, name the end turn, write Turn 1, gate, ship |
| a single response (no pair) | skip PICK, go straight to WRITE |
| "why?" | one sentence, quote the deciding line |
| "backtrack" or a dry conversation before turn 10 | HARD STOP table — go back and enrich an earlier turn, never pad forward |
| "check" / turn 10+ and done | hand off to `/mt-check` |
