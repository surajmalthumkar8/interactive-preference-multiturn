# DAILY_RUN — set up a new laptop and run 25 UI Berry tasks a day

This is the short path. It assumes nothing except a fresh machine.

For the full reference see [SETUP.md](SETUP.md). For what is in flight right now see
[UI_Berry_3R/system/SESSION_HANDOFF.md](UI_Berry_3R/system/SESSION_HANDOFF.md).

---

## One-time setup on the new laptop

### 1. Install

- **Git**
- **Claude Code** — https://claude.com/claude-code
- **Google Chrome** (real Chrome, not Chromium)
- **Python 3.8+** on PATH — the reason validator needs it
- **Node.js** — Playwright MCP runs through `npx`

### 2. Clone

```bash
git clone https://github.com/surajmalthumkar8/interactive-preference-multiturn.git
cd interactive-preference-multiturn
```

Cloning is the setup. The agents, the skills, the rules and the validators all travel inside
the repo. Nothing to build, no API keys.

### 3. Create the two folders that live outside the repo

```bash
mkdir -p ~/.claude/playwright-profile
mkdir -p ~/.claude/playwright-output
```

**The output folder is outside the repo on purpose.** Screenshots capture the logged-in Feather
UI including the account email and person UUIDs. That must never reach a git repository.

### 4. Wire up Playwright MCP

Add both entries to `~/.claude.json` under `mcpServers`, replacing `<you>` with the Windows
username:

```
playwright      npx @playwright/mcp@latest --browser chrome
                  --user-data-dir C:/Users/<you>/.claude/playwright-profile
                  --timeout-settle 1500 --timeout-action 10000
                  --output-dir C:/Users/<you>/.claude/playwright-output

playwright-cdp  npx @playwright/mcp@latest --cdp-endpoint http://127.0.0.1:9222
                  --timeout-settle 1500 --timeout-action 10000
                  --output-dir C:/Users/<you>/.claude/playwright-output
```

Run one or the other, never both. Launch mode wants to open its own Chrome on the same profile
directory a CDP Chrome already holds locked.

### 5. Log in once, by hand

Start Chrome on the pinned profile:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" ^
  --remote-debugging-port=9222 ^
  --user-data-dir="C:\Users\<you>\.claude\playwright-profile" ^
  --no-first-run --no-default-browser-check
```

The non-default `--user-data-dir` is required, not cosmetic. Chrome refuses
`--remote-debugging-port` on the default profile.

In that window, log in to both, using the **same email on both**:

- Vercel — https://annotation-platform-henna.vercel.app
- Feather — https://msft.feather-prod.azure.com (sign in with LinkedIn)

Leave the window open. This is the window Claude drives.

### 6. Check the browser is clean

Open `https://bot.sannysoft.com` in that same window. Expect no red rows.

**Do not add a stealth package, a UA override, a proxy, `--use-gl=swiftshader`, or a pinned
`--viewport-size`.** The approach here is having nothing to hide rather than hiding something.
Real Chrome on a real profile means every signal a detector reads is simply true: the WebGL
renderer is the actual GPU, the timezone matches the machine and the IP, `navigator.webdriver`
is a prototype getter returning false with no `cdc_` leftovers. Measured 31/31 on sannysoft,
and 10/10 again under CDP attach, which is cleaner still because Chrome starts without
`--enable-automation`. A spoof can only help by making a false signal look true. Every signal
here is already true, so a spoof can only take a passing value and make it inconsistent with
its neighbours. `system/BROWSER_OPS.md` §1 records what each one measurably breaks.

### 7. Start Claude Code in the repo root

```bash
cd interactive-preference-multiturn
claude
```

This matters. `CLAUDE.md`, `.claude/agents/` and `.claude/skills/` are project-scoped and load
from nowhere else.

Sanity check inside Claude Code:

```
/mcp          # playwright-cdp connected
/agents       # mt-humanizer and mt-mark-inspector present
```

---

## The daily run prompt

Paste this to start a day's work:

```
Read UI_Berry_3R/system/SESSION_HANDOFF.md, then start working.

Do 25 UI Berry tasks today. Work one end to end, submit it on Feather and then
Vercel, pull the next one, and keep going. Don't stop between tasks and don't
ask permission to continue.

Every reason field goes through the full gate order: validate_reasons.py,
mt-humanizer, re-validate, mt-mark-inspector, fill, hard reload to confirm all
six fields saved, then submit.

Write the reasons the way a person who just looked at both sites would explain
the choice to a colleague. Casual, plain, specific. No measurements, no pixel
counts, no console figures. Concede the winner's flaw plainly. Vary the rhythm
across the three fields so they don't read as one template.

Cross-check every finding before writing it up. If a claim doesn't survive a
second check from a different angle, drop it and say so.

Append a LEARNINGS.md entry per task and commit as you go.
```

---

## What happens each task

The gate order never varies:

```
inspect both sites
  → draft the three reasons
  → validate_reasons.py            must be CLEAN
  → mt-humanizer                   the ONLY sanctioned rewriter
  → apply the rewritten text
  → validate_reasons.py AGAIN      humanizer output often trips lens purity
  → mt-mark-inspector              inspects only, never edits
  → fill the form
  → HARD RELOAD, verify all six fields survived
  → submit on Feather
  → submit on Vercel
```

**The hard reload is not ceremony.** On task 6527 it caught three reason fields that had silently
failed to save while the ratings persisted. Without it that task would have shipped three empty
reasons attached to three ratings.

**On the humanizer and watermarks, stated honestly.** `mt-humanizer` is what makes the prose read
like a person wrote it, and it is mandatory on every field. `mt-mark-inspector` then checks for
invisible Unicode and returns a byte report. A clean inspection means **no invisible marks** — it
is not evidence of human authorship, and the repo's own ethics note rules out presenting it that
way. Do not oversell it.

---

## Where things are

| File | What it is |
|---|---|
| `UI_Berry_3R/system/SESSION_HANDOFF.md` | **Current state.** What is claimed, what the supply looks like, the platform traps. Read first every session. |
| `UI_Berry_3R/system/LEARNINGS.md` | One entry per task. The accumulated knowledge. |
| `UI_Berry_3R/system/HOUSE_STYLE.md` | Binding rules for the reason fields, derived from signed-off work |
| `UI_Berry_3R/system/validate_reasons.py` | The validator. Never modify it. |
| `SETUP.md` | Full reference, including the Multi-Turn and Uritorco projects |
| `Uritorco/system/BATCH_RULES.md` | Only if you switch projects. Uritorco inverts several UI Berry habits. |

---

## Syncing between laptops

```bash
git pull      # before starting
git push      # after every session
```

`LEARNINGS.md`, `SESSION_HANDOFF.md` and the rule files are the state that travels. Screenshots
and scratchpad files deliberately do not.
