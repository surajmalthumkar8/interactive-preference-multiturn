# SETUP — this project on a new laptop

Everything the system needs travels inside this repo: the reconciled manual, the operating rules,
the seven `mt-*` subagents, the six slash commands, the vendored `humanizer` skill, the client
source documents, the legacy system, and the saved Claude memory. **Cloning the repo is the
setup.** The steps below verify it and wire up Claude Code.

---

## Prerequisites

1. **Git** and access to the repository
2. **Claude Code** installed and logged in — https://claude.com/claude-code
3. **Python 3.8+** on PATH — only needed for the legacy validators in
   `Interactive_contri_inst/tools/`, which are optional
4. Nothing else. No API keys, no npm install, no build step.

---

## 1. Clone

```bash
git clone https://github.com/surajmalthumkar8/interactive-preference-multiturn.git
cd interactive-preference-multiturn
```

Any directory is fine. Nothing in the repo hardcodes an absolute path except the older entries in
`memory/`, which are notes rather than working references.

## 2. Start Claude Code **in the repo root**

```bash
claude
```

This matters: `CLAUDE.md`, `.claude/agents/`, `.claude/skills/`, and `.claude/commands/` are all
project-scoped. Starting Claude Code anywhere else loads none of them.

## 3. Verify the wiring

Inside Claude Code:

```
/agents
```

Expect the seven project agents: `mt-topic-scout`, `mt-turn-writer`, `mt-humanizer`,
`mt-response-auditor`, `mt-preference-judge`, `mt-compliance-auditor`, `mt-session-scribe`.

```
/mt-status
```

Expect either an open session or a clean "no open task".

Then confirm the humanizer resolves — ask Claude to *"invoke the humanizer skill on the sentence:
'This comprehensive solution delivers robust value.'"* It should return a rewritten sentence, not
an error. The skill is vendored at `.claude/skills/humanizer/`, so it should resolve without
installing anything.

## 4. Restore the Claude memory (optional but recommended)

`memory/` holds the auto-memory written on the first laptop. Copying it into Claude Code's
per-project memory directory gives a fresh session the same background without re-reading
everything.

The destination is `~/.claude/projects/<slugified-repo-path>/memory/`, where the slug is the
absolute repo path with drive colons and separators replaced by dashes. Easiest way to find it:
start Claude Code in the repo, ask *"what is my memory directory for this project?"*, then:

```bash
# macOS / Linux / Git Bash
cp memory/*.md "<that directory>/"
```

```powershell
# Windows PowerShell
Copy-Item memory\*.md "<that directory>\"
```

Skipping this costs nothing critical — `CLAUDE.md` and `PROJECT_KNOWLEDGE.md` carry the same
facts. The memory files just make them recallable without a read.

## 5. First-run prompt

Paste this into Claude Code once, in the repo root. It is the whole setup handshake — read it
back, verify it, and lock in the standing rules.

```
This repo is my working setup for the MAI "Interactive Preference | Multi-Turn" project.
Set yourself up before we do anything else.

READ, in this order, in full, from disk — not from memory of them:
  1. CLAUDE.md
  2. PROJECT_KNOWLEDGE.md
  3. system/rules/TURN_RULES.md, CAPABILITY_RULES.md, AUTHENTICITY_RULES.md,
     PREFERENCE_RULES.md, WORKFLOW_RULES.md
  4. system/workflows/RUN_TASK.md and system/workflows/CLAIM_TASK.md
  5. system/knowledge/HUMAN_VOICE_CORPUS.md and TOPIC_PLAYBOOK.md
  6. system/checklists/PRE_SUBMIT_CHECKLIST.md
  7. system/learning/PROMPT_LOG.md and LESSONS.md
  8. sessions/ — list any OPEN state file I may be resuming from my other laptop

VERIFY and report:
  - the seven mt-* agents in .claude/agents/ are available to you, by name
  - the `humanizer` skill resolves via the Skill tool. Prove it now: run it on
    "This comprehensive solution delivers robust value across the entire landscape."
    and show me the rewritten line. If it does not resolve, say so loudly and stop.

STANDING RULES — confirm each one back to me in your own words, one line each:
  1. HUMANIZER, EVERY TIME. Every user-side word that will go into Feather — the
     opening prompt, every follow-up, and the optional reason field — goes through
     the mt-humanizer agent, which runs the `humanizer` skill, before you show it to
     me. No exceptions, no "this one is already casual", no batching it for later.
     Nothing ships without HUMANIZATION: PASS on it. If I ever paste a turn back to
     you after editing it, re-humanize it — my edits are not exempt either.
  2. Before humanizing, check the draft against the guidelines' own style rules:
     Golden Rule (~GL:180), Quick Tips (~GL:209), and the example prompt table
     (~GL:194-205), plus system/knowledge/HUMAN_VOICE_CORPUS.md. Read the corpus each
     time; do not work from memory of it.
  3. Vary rhythm, opener shape, and imperfection pattern turn to turn AND task to
     task. GL:180 detects shared writing patterns across contributors and across
     unrelated topics — a consistent AI voice is itself the risk.
  4. 10 turns minimum, 15 maximum. The "one turn is fine" text at GL:134/162/172/229
     is stale 07-28 leftovers. Below turn 10 you may return BACKTRACK, never END and
     never a filler turn — padding to reach 10 is a removal offence.
  5. The model under test has no web search, no real-time data, no file uploads, no
     images, and a July 2025 knowledge cutoff. Paste content, never point at it.
  6. Every turn must engage the specifics of the previous response, with the anchor
     quoted back to me.
  7. Every turn needs a recorded preference, verified by the arrow on the chosen side.
  8. I TYPE every turn into Feather. Never tell me to paste one.

Then wait. From my next message on, I paste task content and you run
system/workflows/RUN_TASK.md on it — no preamble, no summary of what you are about to
do, just the deliverable.
```

If any answer comes back wrong — especially the turn range, the humanizer proof, or the claim
sequence — stop and fix the setup before working a task. A wrong turn range or a missed claim
step costs the whole task.

### Make it permanent (optional, 10 seconds)

The first-run prompt sets up one session. `CLAUDE.md` already carries the same standing rules
into every future session automatically, so you do not need to repeat the paste. If you ever
want the humanizer rule stated even louder, add one line to the top of `CLAUDE.md` under
**Standing instructions** — it loads before anything you type.

---

## Daily flow

1. `git pull` — pick up state from the other laptop.
2. Prepare the topic **before claiming** (`system/knowledge/TOPIC_PLAYBOOK.md` §6). The clock
   starts on claim.
3. Claim: Vercel → Feather → claim → confirm "In progress" → **copy the URL** → paste into
   `Attempt URL` in Vercel. `/mt-claim` prints the sequence.
4. `/mt-start` → type Turn 1 into Feather.
5. Paste each A/B pair → `/mt-turn` → confirm `↳` on the chosen side → type the next turn.
6. At turn 10–15, `/mt-check` → Feather **Mark as Complete** → Vercel **Submit Task**.
7. `/mt-sync` — commit and push so the other laptop is current.

**Type every turn into Feather. Do not paste.**

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| No `mt-*` agents in `/agents` | Claude Code started outside the repo root | quit, `cd` into the repo, `claude` |
| `humanizer` skill not found | `.claude/skills/humanizer/SKILL.md` missing from the clone | re-clone, or reinstall from https://github.com/blader/humanizer |
| `verify_sxs_setup.py` fails | it verifies the **old** repo's layout | expected — see `Interactive_contri_inst/LEGACY_README.md` |
| Claude proposes ending at turn 3 | it is reading the legacy `Interactive_contri_inst/system/rules/TURN_RULES.md` | point it at `system/rules/TURN_RULES.md`; that folder is legacy |
| Claude suggests pasting the turn into Feather | it missed the standing instruction | `CLAUDE.md` → Standing instructions |
