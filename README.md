# Interactive Preference | Multi-Turn (MAI) — working repository

Everything needed to work this project from any machine: the reconciled operating manual, the
client source documents, the binding rules, the Claude Code agent pipeline, and the saved
project memory.

**New machine? Read [SETUP.md](SETUP.md). Cloning this repo is the setup.**

---

## What the project is

A **Microsoft AI ("MAI")** human-preference data collection project. One task = one **10–15
turn** conversation: at every turn Suraj writes a user prompt, receives two responses from two
different model configurations, and picks the one he prefers. The chosen response continues the
conversation.

He is both the user and the judge. There is no peer-review layer — QC is organic and automated,
which is why the rules are blunt and several carry immediate removal.

Claim in **Vercel** → work in **Feather** (LinkedIn login). Never the other order, never one
alone.

---

## Start here

| File | What it is |
|---|---|
| **[PROJECT_KNOWLEDGE.md](PROJECT_KNOWLEDGE.md)** | **The reconciled manual — the single source of truth.** Derived line by line from all four client docs plus the sixteen screenshots embedded as base64 in the guidelines file, then cross-checked against the official screening. |
| [CLAUDE.md](CLAUDE.md) | Project instructions for Claude Code: routing, standing instructions, the five facts that decide most questions |
| [SETUP.md](SETUP.md) | New-laptop bootstrap and the daily flow |

---

## Repository map

```
.
├── PROJECT_KNOWLEDGE.md          the reconciled manual (read this first)
├── CLAUDE.md                     project instructions for Claude Code
├── SETUP.md                      new-laptop bootstrap
│
├── .claude/
│   ├── agents/                   7 mt-* subagents (the task pipeline)
│   ├── commands/                 /mt-start /mt-turn /mt-check /mt-claim /mt-status /mt-sync
│   ├── skills/
│   │   ├── mt-task/              the end-to-end task runner skill
│   │   └── humanizer/            vendored — the mandatory humanization pass
│   └── settings.json             committed project permissions
│
├── system/                       the operating system for the current 10–15 turn regime
│   ├── rules/                    TURN · CAPABILITY · AUTHENTICITY · PREFERENCE · WORKFLOW
│   ├── knowledge/                HUMAN_VOICE_CORPUS · TOPIC_PLAYBOOK · REVIEWER_MODEL
│   ├── workflows/                RUN_TASK · CLAIM_TASK · FIX_TASK
│   ├── checklists/               PRE_SUBMIT_CHECKLIST
│   ├── templates/                STATE · DELIVERABLE
│   └── learning/                 PROMPT_LOG (duplicate + variety ledger) · LESSONS
│
├── sessions/                     live task state, synced between laptops
├── memory/                       saved Claude auto-memory for this project
│
├── client docs (unedited evidence)
│   ├── MAI Interactive — Multi-Turn Guidelines (updated 08_12).md
│   ├── projecthub.md
│   ├── contributor_journey.md
│   ├── Training & Screening.md
│   ├── Production Ops.md  ·  prod_ops.md
│   └── project_QA.md             screening questions with the official answers
│
└── Interactive_contri_inst/      LEGACY — July 2026 system, built for the dead 1–10 turn
                                  regime. Reference only. See LEGACY_README.md.
```

---

## The five facts that decide most questions

1. **10 turns minimum, 15 maximum.** The opening prompt is Turn 1. The guidelines file still
   carries text from the superseded 07-28 revision saying one turn is fine (GL:134, 162, 172,
   229) — all of it is stale and produces invalid tasks.
2. **Padding to reach 10 is a removal offence.** The sanctioned fix for a conversation that runs
   dry early is to go back and **enrich earlier turns**, never to add a forward filler.
3. **The model under test has no web search, no real-time data, no file uploads, no images, and
   a July 2025 knowledge cutoff.** Paste content into the prompt; never point at it.
4. **Every turn must engage the specifics of the previous response.** A follow-up that could
   have been written without reading the response is a defect even when it is on-topic.
5. **Every turn needs a recorded preference**, verified by `↳` on the chosen side. One missing
   selection invalidates the whole conversation.

Two things this repo exists to stop anyone re-learning the hard way:

- The guidelines document **contradicts itself on turn count** because the 08-12 revision was
  edited in place over the 07-28 text and the old passages were never removed.
- **Two billing-critical steps exist only inside a flowchart image** — copy the Feather URL
  *after* claiming, paste it into `Attempt URL` in Vercel. They are absent from the written
  procedure, they are invisible to grep because the image is base64, and all four Operational
  Workflow screening questions test them.

---

## The pipeline

| Agent | Role |
|---|---|
| `mt-topic-scout` | gates the topic **before claiming** — does it hold 10–15 turns of real depth? |
| `mt-turn-writer` | writes the opening prompt and every follow-up, anchored to the previous response |
| `mt-humanizer` | the mandatory humanization gate; always runs the `humanizer` skill |
| `mt-response-auditor` | blind single-response audit, dispatched ×2 in parallel |
| `mt-preference-judge` | the A/B decision — the only agent that sees both responses |
| `mt-compliance-auditor` | adversarial pre-ship gate against all ten removal triggers |
| `mt-session-scribe` | the only writer of `sessions/` and `system/learning/` |

Full procedure: [system/workflows/RUN_TASK.md](system/workflows/RUN_TASK.md).

---

## Conventions

- The four client source documents are **evidence** — never edited except for clearly marked
  update callouts.
- `PROJECT_KNOWLEDGE.md` is **derived** — update it when the sources or the platform change, and
  keep its `file:line` citations accurate.
- **No PII anywhere in this repository**, including session files and ledgers.
- `sessions/` and `system/learning/` are the state that moves between machines. Push after every
  session, pull before starting.
- When a rule proves ambiguous, fix the **rule file**, not just the task
  ([system/workflows/FIX_TASK.md](system/workflows/FIX_TASK.md)).

---

## Credits

`.claude/skills/humanizer/` is vendored from [blader/humanizer](https://github.com/blader/humanizer)
(MIT), pinned here so the humanization gate works on a fresh clone with nothing else installed.
