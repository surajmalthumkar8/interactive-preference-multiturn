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

Paste this into Claude Code once, in the repo root:

```
Read CLAUDE.md, then PROJECT_KNOWLEDGE.md, then every file in system/rules/, then
system/workflows/RUN_TASK.md and system/knowledge/HUMAN_VOICE_CORPUS.md.

Then confirm back to me, in under fifteen lines:
1. the turn range you will enforce, and which lines of the guidelines file are stale
2. what the model under test cannot do, including its knowledge cutoff
3. the exact claim sequence including the two steps that only appear in a flowchart image
4. the seven mt-* agents you can see, and that the humanizer skill resolves
5. any OPEN session in sessions/ that I might be resuming
6. one line confirming you will run the humanizer on every turn and never pad to reach ten

Then wait. From my next message on I paste task content and you run
system/workflows/RUN_TASK.md on it, with no preamble.
```

If any of the six answers comes back wrong, stop and fix the setup before working a task — a
wrong turn range or a missed claim step costs a whole task.

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
