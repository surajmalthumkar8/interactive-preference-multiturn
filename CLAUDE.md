# CLAUDE.md — Interactive Preference | Multi-Turn (MAI)

Project instructions for Claude Code working in this repository. Read this first, every session.

> ## ⛔ The one rule that is never waived
>
> **Every user-side word that will go into Feather passes through the `mt-humanizer` agent,
> which runs the `humanizer` skill, before it is shown to Suraj.** The opening prompt, every
> follow-up, and the reason field. Every turn, every task, no exceptions — including turns he
> edited himself and pasted back. Nothing ships without `HUMANIZATION: PASS`.
>
> This is the condition attached to the permission to use AI on this project at all
> (`system/rules/AUTHENTICITY_RULES.md` §0). Skipping it once turns an allowed workflow into a
> removal offence.

---

## What this project is

Suraj is a contributor on **Interactive Preference | Multi-Turn**, a **Microsoft AI ("MAI")**
human-preference data collection project.

One task = one **10–15 turn** conversation. At every turn he writes a user prompt, receives two
responses from two different model configurations, and picks the one he prefers. The chosen
response continues the conversation; the rejected one is discarded. He is **both the user and
the judge** — there is no peer review, QC is organic and automated.

What the client collects: an ordered chain of `(context, prompt, chosen, rejected)` tuples,
10–15 deep, where every link is conditioned on the previous human choice.

**Platforms:** claim in **Vercel** (`annotation-platform-henna.vercel.app`) → work in **Feather**
(`msft.feather-prod.azure.com`, log in with LinkedIn). Never the other order, never one alone.

---

## Source-of-truth order

1. **`PROJECT_KNOWLEDGE.md`** — the reconciled manual. Use this. It was derived line by line from
   all four source docs plus the sixteen screenshots embedded as base64 in the guidelines file,
   and cross-checked against the official screening.
2. **`system/`** — the operating rules, voice corpus, workflows, and checklists derived from it.
3. **`MAI Interactive — Multi-Turn Guidelines (updated 08_12).md`** — the raw client document.
   **It contradicts itself** (see below). Quote it for citations; do not resolve rules from it
   alone.
4. `projecthub.md`, `contributor_journey.md`, `Training & Screening.md`, `Production Ops.md`,
   `prod_ops.md`, `project_QA.md` — admin, journey, and the screening Q&A with official answers.

**`Interactive_contri_inst/` is legacy and not runnable as-is.** See
`Interactive_contri_inst/LEGACY_README.md` before touching anything in it.

---

## The five facts that decide most questions

1. **10 turns minimum, 15 maximum.** The opening prompt is Turn 1. The guidelines file still
   carries text from the superseded 07-28 revision saying a single turn is fine (GL:134, 162,
   172, 229) — **all of it is stale and produces invalid tasks.**
2. **Padding to reach 10 is a removal offence.** When a conversation runs dry before turn 10, the
   sanctioned fix is to **go back and enrich earlier turns**, never to add a forward filler.
3. **The model under test has no web search, no real-time data, no file uploads, no images, and
   a July 2025 knowledge cutoff.** Paste content into the prompt; never point at it.
4. **Every turn must engage the specifics of the previous response.** A follow-up that could have
   been written without reading the response is a defect even when it is on-topic.
5. **Every turn needs a recorded preference**, verified by `↳` on the chosen side. One missing
   selection invalidates the entire conversation, not just that turn.

---

## Standing instructions from Suraj

- **AI-assisted drafting is allowed** (leadership Slack update, 2026-08-14), including Claude
  Code — **provided every turn is humanized before it goes into Feather.**
- **Run the `humanizer` skill on every single turn.** Not optional, not a one-time pass. The
  skill ships with this repo at `.claude/skills/humanizer/`.
- **Check every draft against the guidelines' own style rules first** — Golden Rule (~GL:180),
  Quick Tips (~GL:209), and the example-prompt table (~GL:194–205) — then humanize.
- **Vary phrasing and rhythm across turns and across tasks.** GL:180 detects shared writing
  patterns across contributors and across unrelated topics; a uniform assistant voice is itself
  the risk.
- **Still prefer sourcing from his real AI history** over invented scenarios. The new policy
  supplements the methodology, it does not replace it.
- He **types** every turn into Feather. Never tell him to paste one.

---

## How to run a task

Two runners. **`mt-loop`** is the default when the clock matters: one inline pass per turn, the
humanization gate as the only subagent, ~30s from paste to ship. Its whole rulebook is
`system/FASTLOOP.md`, which is the rule files compiled down — read it once per session and
nothing else. **`mt-task`** is the careful runner (blind auditors, separate judge, compliance
sweep) for a first task on a new topic type or when something has gone wrong.

Full pipeline: `system/workflows/RUN_TASK.md`. Commands:

| Command | Does |
|---|---|
| `/mt-loop` | **fast mode** — paste a pair, get the pick and the next turn in ~30s, repeat |
| `/mt-start` | validate a topic for depth, then produce Turn 1 |
| `/mt-turn` | judge a pasted A/B pair, then write the next turn |
| `/mt-check` | full pre-submit sweep against every removal trigger |
| `/mt-claim` | the billable claim sequence and the ops failure cases |
| `/mt-status` | where the current task stands |
| `/mt-sync` | commit and push state to the other laptop |

Subagents in `.claude/agents/`:

| Agent | Role |
|---|---|
| `mt-topic-scout` | gates the topic before claiming — does it hold 10–15 turns? |
| `mt-turn-writer` | writes the opening prompt and every follow-up |
| `mt-humanizer` | the mandatory humanization gate |
| `mt-response-auditor` | blind single-response audit, dispatched ×2 in parallel |
| `mt-preference-judge` | the A/B decision, the only agent that sees both |
| `mt-compliance-auditor` | adversarial pre-ship gate |
| `mt-session-scribe` | the only writer of `sessions/` and `system/learning/` |
| `mt-mark-inspector` | mandatory provenance inspection, **after** `mt-humanizer`; inspects only, never rewrites |

---

## Rules that are binding, not advisory

`system/rules/TURN_RULES.md` · `CAPABILITY_RULES.md` · `AUTHENTICITY_RULES.md` ·
`PREFERENCE_RULES.md` · `WORKFLOW_RULES.md`

Read them from disk rather than from memory of them. They are short.

When Claude drives the browser against Vercel / Feather / LinkedIn, `system/BROWSER_OPS.md` is the
card: the verified Playwright profile, the pacing rules, and the stop-on-challenge policy. It only
ever navigates and reads — **turn text is always typed by Suraj**.

**The hardened profile is mandatory and is not optional per-session.** It lives in the global
Playwright MCP config (real Chrome + pinned persistent profile, no spoofing). Verified 2026-08-16
against `bot.sannysoft.com`: **31/31 scored tests passed, zero red rows**. Never add a stealth
package, UA override, proxy, or `swiftshader` flag on top of it — `BROWSER_OPS.md` §1 records what
each one measurably breaks. Re-run the §6 check after a Chrome major-version jump.

### `remove-ai-marks` on this project — via the `mt-mark-inspector` agent

**Mandatory on every turn.** The gate order is fixed and never varies:

```
draft ──▶ mt-humanizer (rewrites) ──▶ mt-mark-inspector (inspects) ──▶ Suraj types it
              │                              │
        HUMANIZATION: PASS            INSPECTION: PASS
```

`mt-humanizer` runs first and is the **only** rewriter. `mt-mark-inspector` runs second and
**never** edits — it reports and hands back. Neither may be skipped.

The service is started automatically by a `SessionStart` hook
(`~/.claude/watermarks-remover/start-if-down.py`); the agent verifies health rather than assuming
it. `curl` is denied in this project — the agent uses `python`/`urllib`.

Installed globally (`~/.claude/skills/remove-ai-marks` + service at `~/.claude/watermarks-remover`).
On this project it is an **inspection step, not a gate, and never a rewriter**:

- **Run `/inspect`** on any draft turn before it is shown to Suraj, and on any text pasted *out* of
  Feather into this repo. It is cheap and it catches stray invisible Unicode in model output.
- **Never run Layer B (`/clean` rewriting) on a turn.** `mt-humanizer` is the sanctioned gate and the
  only one the client's rules recognise. A second rewrite on top of it degrades the prose and
  destroys the phrasing variation GL:180 is actually looking for.
- **It does not certify authorship.** Measured 2026-08-16: hand-typed prose returns
  `suspicious: false`, zero findings, byte-identical output — because typing cannot produce
  invisible Unicode. Since Suraj types every turn, this step **cannot change what reaches Feather**.
  It verifies the draft; it does not launder it.
- Useful for real here: the four client source docs, screenshots, and any file-based deliverable
  (C2PA/EXIF/XMP strip). That is where it does actual work.

---

## The ten removal triggers

Reused/paraphrased prompt · LLM-generated prompt shipped unhumanized · artificial turns to reach
10 · PII or confidential material · writing patterns shared across contributors · a prompt not in
English · **any turn without a selection** · discrimination or insults · breaking the
Vercel→Feather sequence · claiming directly in Feather.

Full citations: `PROJECT_KNOWLEDGE.md` §4.

---

## Working conventions in this repo

- **Never edit the four client source docs** (guidelines, projecthub, contributor journey,
  training & screening) except to add clearly marked update callouts. They are evidence.
- **PROJECT_KNOWLEDGE.md is derived** — update it when the source docs or the platform change,
  and keep the `file:line` citations accurate.
- **No PII anywhere in this repo**, including session files and ledgers. It is a git repository.
- **`sessions/` and `system/learning/` are the state** that moves between laptops. Commit and
  push after every working session; pull before starting on the other machine.
- When a rule turns out to be ambiguous or wrong, fix the **rule file**, not just the current
  task (`system/workflows/FIX_TASK.md`).

## Escalation

Project or quality question → check the FAQ, then post a Slack thread. Operational failure →
Get Help → Operational Issue. Payments → `#all-trainer-hub`, never the project channel. Never DM
a QM. English only.
