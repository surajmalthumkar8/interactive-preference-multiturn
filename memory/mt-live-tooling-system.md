---
name: mt-live-tooling-system
description: A proper git-tracked skill/agent pipeline (mt-task, mt-turn, mt-sync, etc.) now exists for this project and is the standard entry point — supersedes ad hoc orchestration and the old Interactive_contri_inst
metadata:
  node_type: memory
  type: project
  originSessionId: 245c96c2-20a4-4909-b2a6-fe539a64b62a
  modified: 2026-08-14T08:52:25.313Z
---

As of 2026-08-14, `c:\Users\Suraj\Downloads\project_interactive_linkedin\` is a real git repo
(remote `https://github.com/surajmalthumkar8/interactive-preference-multiturn.git`, branch
`main`) with its own `.claude/skills/` and `.claude/agents/` providing a purpose-built pipeline
for running these tasks: skills `mt-task` / `mt-turn` / `mt-start` / `mt-check` / `mt-claim` /
`mt-status` / `mt-sync`, and agents `mt-topic-scout`, `mt-turn-writer`, `mt-response-auditor`,
`mt-preference-judge`, `mt-humanizer`, `mt-compliance-auditor`, `mt-session-scribe`. This runs
`RUN_TASK.md`'s staged workflow (topic scout → per-turn audit/judge/write/humanize/compliance →
session-scribe logging) and is git-synced across Suraj's two laptops via `mt-sync`.

**Why this matters:** it appeared mid-session on 2026-08-14, replacing what I'd been doing by
freehand multi-agent orchestration (dispatching `mt-response-auditor`/`mt-preference-judge`/etc.
manually one at a time). The proper way to run a task now is to invoke the `mt-task`/`mt-turn`
skill and follow its returned instructions, not to reconstruct the process from first principles.

**Relationship to prior memories:** [[mt-legacy-system-stale-and-off-limits]] documents the OLD
`Interactive_contri_inst/` pipeline (Jul 2026, ungit-tracked, calibrated to the dead 1-10 turn
regime). That system is now doubly moot: its AI-drafting objection was lifted by the policy
reversal ([[mt-never-ai-write-prompts]]), and it's functionally replaced by this new tracked
system rather than being worth repairing. Do not revive `Interactive_contri_inst/` — use this
system instead. One live gap: `Interactive_contri_inst/system/knowledge/PROMPT_SPECTRUM.md` and
`GOLD_PATTERNS.md` (the client's 5 example categories incl. their 5 banned scenarios, and the
gold-conversation patterns) have not been ported into the new tree yet — as of the first
production task (Conv 55) they're still read from the legacy location despite it being otherwise
off-limits, because there's no in-system copy. `system/learning/LESSONS.md` (2026-08-14 entry)
tracks this as a pending port.

**State/learning files, authoritative, read fresh each time rather than caching their content
here:** `sessions/<task>_state.md` (per-task, turn counter/constraint ledger/pick record),
`system/learning/PROMPT_LOG.md` (rotation tracking across tasks), `system/learning/LESSONS.md`
(accumulated fixes), `system/rules/AUTHENTICITY_RULES.md` (current humanization rules — §0
already carries the AI-drafting policy reversal).

**How to apply:** When Suraj pastes Feather task content or asks to start/continue a task, invoke
the `mt-task` or `mt-turn` skill rather than freehanding the audit/judge/write/humanize sequence
myself. Use `mt-sync` for cross-laptop git sync rather than raw git commands, unless its steps
need supplementing (e.g. I added a `git fetch` + ahead/behind check before push on 2026-08-14,
since it's a multi-machine setup and mt-sync's own steps didn't include that check).
