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

---

# UI Berry, the second project in this repo

`UI_Berry_3R/` is a different job from everything above. There are no conversations and no
turns. One task shows two candidate websites built from the same prompt, and you answer three
questions about them: which looks better, which works better, which is better overall. Each
answer needs a written reason of 40 to 160 words.

**Only `UI_Berry_3R/system/` is in this repo.** That folder is ours: the house style, the
validator, the learnings, the worked example. The eleven Learning Hub pages that used to sit
beside it are Microsoft AI's own training documents and are gitignored, because **this
repository is public** and publishing client material is removal trigger #4. Re-download them
from the Learning Hub on the new laptop; they are read-only reference and nothing in the
toolchain reads them at runtime.

Read `UI_Berry_3R/system/TOOLCHAIN.md` first. It is the operating card and it carries the
measured rationale behind every flag mentioned below.

## The four gates, in this order

```
inspect both sites  ──▶  draft the    ──▶  humanize   ──▶  re-validate  ──▶  provenance  ──▶  submit
 [hardened Chrome]       six fields        [rewriter]      [validator]        [inspect]
```

Two of these gates are easy to run in the wrong order.

**Re-validate runs after the humanizer, not before.** The humanizer is a rewriter, and it can
silently break a hard constraint that the draft satisfied: push the word count past 160, drop
a hyphen and change the count, or replace "Website B" with "the second site". This does not
happen on the multi-turn project, where user turns have no word range and no naming rule, so
the instinct carried over from that side of the repo is wrong here. Run the validator on the
draft, then again on the humanized output.

**The mark-inspector never rewrites.** It inspects and reports. The humanizer is the only
sanctioned rewriter, and a second rewrite on top of it undoes the first.

## What does not travel with the clone

Two things live outside the repo and have to be set up per machine.

### 1. The watermark service

This is the piece people miss. The skill is global at `~/.claude/skills/remove-ai-marks`, and
it talks to a local service that is a clone of the upstream project:

```bash
git clone https://github.com/guillaumemeyer/watermarks-remover.git ~/.claude/watermarks-remover
```

A `SessionStart` hook in `~/.claude/settings.json` runs
`~/.claude/watermarks-remover/start-if-down.py`, which starts it only if port 8765 is not
already listening and always exits 0, so it cannot break a session. Start it by hand if
needed, and check health with Python rather than curl, which is denied in this project:

```bash
python ~/.claude/watermarks-remover/start-if-down.py
python -c "import urllib.request;print(urllib.request.urlopen('http://127.0.0.1:8765/health').read())"
# -> {"ok": true, ...}
```

**Do not go past Layer A.** `/inspect` finds invisible Unicode (zero-width characters, word
joiners, invisible-times) and that layer is deterministic and worth running. `/clean` also
offers Layer B, a statistical rewrite, and that is off limits on a reason field for the same
reason a second humanizer pass is.

**Be honest about what a pass means.** Text a human typed has nothing to strip, so
`suspicious: false` is a check, not a laundering step, and it is not evidence of human
authorship. The upstream repo's own ethics note rules out that claim and so does ours.

### 2. Playwright

Configured globally in `~/.claude.json` under `mcpServers`, not in the repo. Two entries,
kept side by side:

```
playwright      npx @playwright/mcp@latest --browser chrome
                  --user-data-dir C:/Users/<you>/.claude/playwright-profile
                  --timeout-settle 1500 --timeout-action 10000
                  --output-dir C:/Users/<you>/.claude/playwright-output

playwright-cdp  npx @playwright/mcp@latest --cdp-endpoint http://127.0.0.1:9222
                  --timeout-settle 1500 --timeout-action 10000
                  --output-dir C:/Users/<you>/.claude/playwright-output
```

Run one or the other, never both: launch mode wants to open its own Chrome on the same
`--user-data-dir` that a CDP Chrome already holds locked. Config changes need `/mcp` to
reconnect before the tools appear.

CDP attach is the normal mode here. You log in yourself, then Claude attaches to that
window:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" \
  --remote-debugging-port=9222 \
  --user-data-dir="C:\Users\<you>\.claude\playwright-profile" \
  --no-first-run --no-default-browser-check
```

The non-default `--user-data-dir` is required rather than cosmetic: Chrome refuses
`--remote-debugging-port` on the default profile, and pointing it at the pinned profile keeps
cookies warm so Feather sees a returning user.

**The output directory sits outside the repo deliberately.** Snapshots capture the logged-in
Feather UI, including the account email and person UUIDs, and those must never land in a git
repository.

### On staying undetectable

The approach is to have nothing to hide rather than to hide something. `--browser chrome`
drives real Chrome with the real profile, so every signal a detector reads is simply true:
the WebGL renderer is the actual Intel GPU, the timezone matches the machine and the IP, the
viewport is genuinely smaller than the screen, `navigator.webdriver` is a prototype getter
returning false rather than an own property, and there are no `cdc_` or selenium leftovers.
Verified 31/31 on `bot.sannysoft.com`, and again 10/10 under CDP attach, which is if anything
cleaner because Chrome starts without `--enable-automation` and shows no automation infobar.

**Never add a stealth package, a UA override, a proxy, `--use-gl=swiftshader`, or a pinned
`--viewport-size`.** Each one measurably breaks something, and `BROWSER_OPS.md` §1 records
what. A spoof can only help by making a false signal look true. Every signal
here is already true, so a spoof can only take a passing value and make it inconsistent with
the rest of the machine. A pinned viewport that does not match the real screen is a tell no
real user produces.

When driving, pause 1 to 4 seconds between meaningful actions and keep the timing variable,
because an even 2000ms cadence is its own signature. Scroll toward a target before acting on
it and let pages settle before snapshotting.

**On a challenge page: stop, do not solve it.** Screenshot it, hand control back, resume only
on confirmation. A challenge is a signal about the session, not an obstacle to route around.
Defeating bot detection and solving challenges are out of bounds, unchanged.

## Writing the reasons

`UI_Berry_3R/system/HOUSE_STYLE.md` is binding and short. It was taken from fifteen reason
fields the client actually signed off, so where it and any other note disagree, it wins.

**Write the reason the way a person who just looked at both pages would explain their choice
to a colleague. Describe what you saw, not what you measured.**

Measuring is still how you make sure you are right. Not one of the fifteen approved fields
contains a pixel count or a sampled value, and a figure that could only come from a devtools
console is the single clearest tell that separates a machine-written reason from an approved
one. Measure privately, then throw the numbers away and write what the measurement means to
someone looking at the page. Figures a viewer can read off the page itself, a price or a
headline percentage, are fine, because a person sees those.

The rest of the approved shape: open with the plain `Website A is better because`, stay in
third person with no "I" and no "you", name the winner's own flaw plainly, and close with one
short verdict line. Ninety to 160 words, with most of the corpus near 100. Do not pad toward
150 to look thorough.

The humanizer's own defaults fight three of these rules, so pass it the constraint brief in
`TOOLCHAIN.md` §2 every time. Its PERSONALITY AND SOUL section wants first person and
opinions, which is an instant scope break here; its elegant-variation rule will reach for
"the second site" rather than repeating "Website B"; and its passive-voice rule rewrites into
"you". The skill's own carve-out covers the first of those: reference text is correctly
neutral and plain.

## Running the validator

```bash
cd UI_Berry_3R
python system/validate_reasons.py task.json     # once on the draft, again after humanizing
```

Exit 0 is clean and any BLOCK has to clear before submitting. It checks the word range
counted both ways, because the client's counter is unknown and hyphens change the total; the
opening verdict and whether it matches the selected option; full "Website A" / "Website B"
naming with bare-letter and "the second site" detection; lens purity in both directions;
first person and platform references; ties whose reason secretly names a winner; and 6-grams
reused across the three fields.

**What it cannot do is tell whether a claim is true.** The factual audit against the two live
tabs stays manual, and a claim describing something that does not exist is the most serious
defect a submission can carry. A green validator run is not a reviewed task.

## Daily flow

1. `git pull`.
2. Pick the task **on the Vercel dashboard**, never from the Feather campaign list. Vercel is
   the binding queue. It can show an empty queue while Feather shows hundreds of unclaimed
   tasks, and a full Feather campaign is not permission to claim from Feather.
3. Claim it, then open both candidate sites in their own full tabs.
4. Inspect: scroll each site top to bottom and click every control to confirm it updates
   content. Existence is not functionality. This is the evidence base for the functionality
   reason and automating it does not shorten it.
5. Draft the three options and three reasons → validate → humanize → validate again →
   inspect → fill → hard-reload to confirm the fields persisted → submit on Feather → confirm
   Completed → submit on Vercel.
6. Append anything learned to `UI_Berry_3R/system/LEARNINGS.md`, then commit and push.

Caps measured on recent batches: 25 claims and 15 submits per day on the UI-Berry batch, and
20 submits on the older 3R batch. Plan the day around submits, not claims.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Health check refused on 8765 | service not running, or not cloned on this machine | `python ~/.claude/watermarks-remover/start-if-down.py`; clone it first if missing |
| `curl` denied | deliberate on this project | use `python`/`urllib` |
| Playwright tools missing after a config edit | MCP not reconnected | `/mcp` |
| Chrome refuses `--remote-debugging-port` | pointed at the default profile | use the pinned `--user-data-dir` |
| Launch-mode Playwright cannot start Chrome | a CDP Chrome holds the same profile locked | use `playwright-cdp`, or close the CDP window |
| Validator blocks on a word the lens forbids | substring match, e.g. `broken` inside `unbroken` | reword; the filter is deliberately blunt |
| Humanizer swapped a legal word out | it over-corrects across lenses, e.g. `italic` is fine in aesthetics | revert that edit, re-run the validator |
| A screenshot shows clipping the DOM denies | short viewport with `overflow:hidden`, not a real bug | `browser_resize` taller and re-shoot before writing any clipping finding |
| Feather page reads `Task not found` | dead link, and re-claiming returns the same dead id | type `task not found` in Vercel Notes, Save, Release, confirm; do not loop on re-claiming |

---

# Uritorco, the third project in this repo

`Uritorco/` is a WebDev side-by-side rating job. One task shows two candidate web apps built
from the same prompt, Left and Right, and you rate each one independently on three rubrics
(Completeness, Functionality, Visual and responsive quality) from 1 to 5, each with a written
evidence field. Then an overall preference on a seven point scale, a confidence level, and a
rationale. Eight fields in total.

**To start a session, paste `Uritorco/START_PROMPT.md` as your first message.** It loads the
rules, the measured platform mechanics and the fast path in one go, so the session does not
spend its first ten minutes rediscovering the form. After that each task is two URLs.

## Read these, in this order

1. `system/BATCH_RULES.md`, the client's own six corrections for this batch. They outrank
   any habit carried over from UI Berry, and three of them invert it.
2. `system/PLATFORM_MECHANICS.md`, measured selectors, the duplicate-id trap, how to submit.
3. `system/FASTPATH.md`, the order of operations that keeps a task quick.
4. `system/LEARNINGS.md`, what previous tasks got wrong.

## The three rules that catch people out

**Rubric fields are negatives only.** No praise about a candidate in any of the six evidence
fields. This is the opposite of UI Berry's house style, which requires conceding the winner's
flaw and reads as balanced. Positives belong in the preference rationale, which wants pros and
cons for both candidates.

**Nothing negative to report means 5, not 4.** Withholding a 5 because nothing is ever perfect
is the exact error the client named. A 5 also uses one mandated phrase verbatim,
"Excellent with no meaningful issues.", and nothing else. That raises the bar on inspection
rather than lowering it: a 5 is a claim that you looked and found nothing.

**The rationale opens with the selection restated.** Select "Slightly prefer Left" and the
first words are "The left candidate is slightly preferred because". Completeness carries the
most weight when choosing the winner.

## Running it

```bash
cd Uritorco
python system/validate_rubrics.py task.json     # before AND after the humanizer
```

The validator enforces the exact-5 phrase, negatives-only, the matching opener, first and
second person, em dashes, and whether the totals point the same way as the selection. It cannot
tell whether a claim is true.

`system/probe.js` is the layout audit. Paste it as a single `browser_evaluate` per app per
width, desktop 1440 then mobile 390, instead of round-tripping for one number at a time.

## What makes it fast

Extract the zip that auto-downloads with the task page and read both sources first. It takes
about ninety seconds and turns the live inspection into targeted confirmation rather than an
open-ended hunt. Findings from source are hypotheses; the live app decides.

Dispatch `mt-humanizer` and `mt-mark-inspector` in the same message. The inspector never
rewrites, so it does not wait on the humanizer, and running them in sequence wastes about
fifty seconds per task.

Fill the form as six rating clicks (real clicks, they are MUI toggles), one `browser_evaluate`
for all seven textareas, and one real keystroke to fire the autosave.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Both texts land in the Left panel | Left and Right share every element id | disambiguate by **DOM order**, first 3 rule textareas are Left and the next 3 are Right, or Playwright `nth=0`/`nth=1`. A hardcoded `x < 760` test is wrong: the Right panel sits at x=768 on a 1536 window but x=720 on a 1440 one, and it fails silently |
| `No more tasks available for this project right now.` | the queue is gated on review, not empty | read the dashboard card. `Waiting for reviews: 0/3 approved` means three submits must be approved before it reopens. Nothing local fixes it, and do not go looking for tasks in the Feather campaign lists instead |
| Preview returns HTTP 502 | sandbox origin expired | refresh the Feather task page; both apps re-provision on new hostnames. Never rate this against a candidate |
| The Vercel link says `Task not found` | task variables hold the pre-claim id | use the task that is actually In progress; put that URL in Attempt URL |
| A screenshot shows no overflow but columns are missing | full-page capture widens the canvas and hides it | measure `scrollWidth` vs `innerWidth`, then take a **viewport** screenshot |
| Next call fails after clicking Delete or Save | the app used `confirm()` or `alert()` | `browser_handle_dialog` |
| Validator blocks on a 5 | a 5 must read exactly `Excellent with no meaningful issues.` | use the phrase, or lower the rating and write the negative |
| favicon 404 in console | sandbox noise | not a finding |
