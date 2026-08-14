# LEGACY — the SxS Interactive system (July 2026)

**Status: reference material, not a runnable pipeline. Do not run it as-is.**

---

## What this is

A complete Claude-agent pipeline built in July 2026 for the *previous* revision of this project:
seven `sxs-*` agents, a rule set, a voice corpus, two Python validators, and six saved task
sessions. It worked, and a lot of what it learned is still correct — which is why it is kept.

## Why it is not runnable now

**It is calibrated to a dead ruleset.** It targets the **2026-07-28** guide's **minimum 1 /
maximum 10** turn regime. Its `system/rules/TURN_RULES.md` states that *"ending at Turn 1 or
Turn 2 is now a correct outcome"*. The current **08-12** guide requires **minimum 10 / maximum
15**, and stopping short of 10 produces an invalid task.

Running these agents against a current task would produce work that fails the turn floor. That
is the whole objection — and it is enough.

*(The original second objection — "AI must not write the prompts" — was lifted on 2026-08-14
when leadership permitted AI-assisted drafting, provided the output is humanized. That reason no
longer applies.)*

### The useful discovery buried in here

The stale, contradictory passages in the current 08-12 guidelines (GL:134, 162, 172, 229) are
**verbatim survivals of this 07-28 regime**. The 08-12 document was edited in place and those
passages were never stripped. This system is an independent copy of the old rules, which is what
proves it.

---

## What replaced it

| Legacy | Current |
|---|---|
| `Interactive_contri_inst/system/` | `system/` at the repo root |
| `sxs-turn-writer`, `sxs-humanizer`, `sxs-preference-judge`, `sxs-response-auditor`, `sxs-reviewer-simulator`, `sxs-final-evaluator`, `sxs-lessons-scribe` | `mt-turn-writer`, `mt-humanizer`, `mt-preference-judge`, `mt-response-auditor`, `mt-compliance-auditor` (merges the last two reviewers), `mt-session-scribe`, plus the new `mt-topic-scout` |
| `system/workflows/DO_TASK.md` | `system/workflows/RUN_TASK.md` |
| min 1 / max 10 turns | min 10 / max 15 turns |

The current system carries forward this one's architecture — blind parallel auditing, a frozen
pick, a mandatory humanization gate, append-only ledgers — recalibrated to the live rules.

---

## What is still safe to use directly

- `system/rules/CAPABILITY_RULES.md` — the four capability limits are unchanged. *(The current
  version at `system/rules/CAPABILITY_RULES.md` adds the July 2025 knowledge cutoff, which this
  one predates. Prefer the current one.)*
- `system/checklists/PRE_SUBMIT_CHECKLIST.md` — as a self-check, ignoring its turn-count lines.
- `system/knowledge/REVIEWER_MODEL.md` — how QC thinks.
- `system/knowledge/HUMAN_VOICE_CORPUS.md` — the voice data is verbatim client material and is
  reproduced in the current corpus.
- `reference_tasks/` — six signed-off transcripts. Their **voice** is the target; their 3–5 turn
  **length** is not.
- `tools/validate_sxs_turn.py` — the capability and voice pattern checks are still valid. **Ignore
  any turn-count verdict it prints.**
- `tools/verify_sxs_setup.py` — expects the old repo's layout (`.claude/agents/sxs-*`,
  eighteen system files). **It will fail in this repo. That is expected, not a broken setup.**

## What is NOT safe to use

- `system/rules/TURN_RULES.md` — wrong turn regime, explicitly endorses ending at Turn 1.
- `system/workflows/DO_TASK.md` — same, plus it routes to agents that no longer exist here.
- `SETUP.md` — describes the old repository (`adu-bench-qa-annotation-system`), a different
  clone path, and the seven `sxs-*` agents living in `.claude/agents/`.
- `legacy_agents/*.md` — the seven agents, archived here **deliberately outside `.claude/agents/`
  so Claude Code will not load or auto-delegate to them.** Moving them into `.claude/agents/`
  would put agents that endorse a 1-turn conversation back in the routing table.

## Redaction note

The six files in `reference_tasks/` were downloaded from the platform with an account line at
the top carrying the email address of the contributor who authored each transcript. Those
addresses belong to other people, so they were replaced with `[contributor-email-redacted]`
before this repository was created. Nothing else in those files was touched — the transcripts
are verbatim.

## If you ever want to revive it

Rewrite `TURN_RULES.md` and `DO_TASK.md` for the 10–15 regime, re-point every agent's file
references at this repo's paths, then move the agents into `.claude/agents/` — at which point
they would duplicate the `mt-*` agents that already do the job. Reviving it is almost certainly
not worth it; reading it sometimes is.
