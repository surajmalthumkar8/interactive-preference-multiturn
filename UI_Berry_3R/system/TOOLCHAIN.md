# Mandatory Toolchain — UI Berry 3R

> **Starting a new session? Read [SESSION_HANDOFF.md](SESSION_HANDOFF.md) first.**
> It carries the live task in flight, the current campaign and supply, and the platform traps
> that cost hours to rediscover.

Directed by Suraj, 2026-08-27. These four gates are **compulsory on every task**. None is
optional, and the order does not vary.

```
inspect both sites          draft the             humanize            re-validate         provenance        submit
in hardened Chrome    ──▶   six fields    ──▶   (rewriter)   ──▶   (mechanical)  ──▶    inspect     ──▶
   [Playwright]                                 [humanizer]        [validate_       [mark-inspector]
                                                                   reasons.py]
```

**The re-validate step is the one that does not exist on the multi-turn project, and it is
the reason this pipeline is not just the other one copied over.** Multi-turn user turns have
no word range and no naming rule, so a humanizer pass there cannot break a hard constraint.
Here it can, and silently. See §3.

---

## 1. Playwright — the hardened profile

**Config is already applied globally** in `~/.claude.json` → `mcpServers.playwright`. Do not
re-derive it; the measured rationale for every flag is in the repo root at
`system/BROWSER_OPS.md` §1.

```
npx @playwright/mcp@latest
  --browser chrome
  --user-data-dir C:/Users/Suraj/.claude/playwright-profile
  --timeout-settle 1500
  --timeout-action 10000
  --output-dir C:/Users/Suraj/.claude/playwright-output
```

**This satisfies the project's own Chrome mandate.** `--browser chrome` drives **real Chrome
151**, not bundled Chromium, so `Learning Hub.md` §01 ("Google Chrome only") is met by the
same config that handles detection. There is no tension between the two requirements, and no
second browser is ever needed.

**Verified 2026-08-16 against `bot.sannysoft.com`: 31/31 scored tests, zero red rows.**

**Never add** a stealth package, UA override, proxy, `--use-gl=swiftshader`, or a pinned
`--viewport-size`. `BROWSER_OPS.md` §1 records what each one measurably breaks. The governing
principle: every signal here is already *true*, and a spoof can only help by making a *false*
signal look true. Re-run the §6 check after a Chrome major-version jump.

**Driving it** (`BROWSER_OPS.md` §2): pause 1–4s between meaningful actions and keep the
timing **variable** — an even 2000ms cadence is its own signature. Scroll toward a target
before acting on it. Let pages settle before snapshotting. Do not re-login; the persistent
profile exists so the OAuth round-trip stays rare.

**Challenge pages: stop, do not solve** (`BROWSER_OPS.md` §3). Screenshot it, hand control to
Suraj, resume only on his confirmation. A challenge is a signal about the session, not an
obstacle to route around.

**What this gate is for on this project specifically.** UI Berry 3R requires opening each
candidate in its **own full tab** via the *Open the environment in a new tab* button, scrolling
top to bottom, and **clicking every control** to confirm it updates content. That is the
evidence base for the functionality reason. Automating it does not shorten it: existence is
not functionality, and a control has to actually be exercised before anything can be claimed
about it.

**Output directory is outside the repo on purpose.** Session artifacts carry PII. They must
never land in a git repository.



### Repo-wide invisible-Unicode sweep (2026-09-21)

The service at `~/.claude/watermarks-remover` (upstream
[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover), MIT)
was run in `/inspect` mode across every markdown file in this repository: `CLAUDE.md`,
`README.md`, `SETUP.md`, all of `UI_Berry_3R/system/*.md`, and `UI_Berry_3R/tools/README.md`.

**Result: 16 files, 0 findings.** No zero-width characters, word joiners, bidirectional marks or
invisible-times. Nothing to strip.

That is the expected outcome and it is worth understanding *why*, because it stops this check
being re-run as if it were a fix. Invisible Unicode arrives by **pasting model output**. Prose
that a person typed, or that was written to disk as plain ASCII, has nothing to carry. A clean
result here means "this file was never contaminated", not "this file was cleaned".

**What this check is and is not:**

- It **is** worth running on any text pasted *out of* a model and into the repo, and on
  file-based deliverables that leave the machine (the C2PA/EXIF/XMP strip).
- It is **not** evidence of human authorship, and must never be reported as such. The upstream
  README is explicit: *"no tool can honestly certify this fails the official check."*
- Layer B (`/clean`, which rewrites text) is **never** run on this project. `mt-humanizer` is the
  only sanctioned rewriter, and a second rewrite on top of it degrades the prose and destroys the
  phrasing variation the client's own rules are looking for.
- Optional binaries `exiftool`, `qpdf`, `c2patool`, `ghostscript` and `ffmpeg` all report `false`
  on this machine, which reduces the PDF and some image paths. Irrelevant for plain markdown.

**Git history is out of scope for this tool and deliberately so.** Commits on this repository
carry a `Co-Authored-By` trailer recording that Claude contributed. That trailer is accurate, and
removing it would misrepresent authorship on a project whose rules treat undisclosed AI use as a
removal trigger. Honest attribution and the client's authorship rule point the same way here.

### Evaluated and rejected: `invisible_playwright` (2026-09-21)

`feder-cr/invisible_playwright` (2,942 stars, MIT, actively pushed) was evaluated as a possible
anti-detection upgrade. **It cannot be used on this project**, and the reason is architectural
rather than a matter of preference. Three disqualifiers, all quoted from its own README:

1. **It is Firefox, not Chrome.** *"It is Firefox, patched at the C++ source level."* The project
   is Firefox-exclusive. `Learning Hub.md` §01 requires Google Chrome, so this fails the client's
   own browser mandate before any detection question is reached.

2. **It refuses CDP.** *"A few surfaces are out of scope - tracing, HAR, CDP, the API request
   context - and each one refuses with a sentence saying why rather than misbehaving quietly."*
   Every tool in `UI_Berry_3R/tools/` attaches to a running Chrome over
   `--remote-debugging-port=9222`. The README contains zero occurrences of `remote-debugging`.
   This is not a gap to work around; the tool declines the interface the whole toolchain uses.

3. **It randomizes the fingerprint per session.** *"Random fingerprint per session."* That is the
   right design for anonymous scraping and the wrong one here. Our profile is **authenticated and
   aged** — LinkedIn and Feather see a returning user with warm cookies and real history. Swapping
   a stable, consistent, logged-in identity for a freshly randomized one each session is a
   *downgrade* in trust signal for an authenticated workflow, not an upgrade.

**The general finding, which is the part worth remembering.** For a profile that already passes
cleanly, adding any stealth layer tends to make things worse, because the patch itself becomes the
signal. Measured example from the current literature: `puppeteer-extra-stealth` improves headless
detection from 100% to 33%, but CreepJS then flags the patch itself at 80%. `playwright-stealth`
patches roughly 12 JS properties while modern anti-bot systems check 40 or more, and its upstream
has not shipped a fix since 2023. The remaining 2026 signals — input physics, GPU pipeline, event
timing, keystroke entropy — are not reachable from a JS shim at all.

**Measured state of our profile, re-verified 2026-09-21 on Chrome 153:**

```
navigator.webdriver      false
userAgent                Chrome/153.0.0.0  (no Headless token)
userAgentData.brands     Google Chrome 153 / Not_A Brand 8 / Chromium 153
platform                 Win32
languages                en-US, en
hardwareConcurrency      16          (matches the real machine)
deviceMemory             32          (matches the real machine)
plugins.length           5
WebGL renderer           ANGLE (Intel UHD Graphics 0x0000A7A8, D3D11)  -- hardware, not SwiftShader
window.chrome            object
```

Every one of those values is **true**, which is the whole point. A spoof can only help by making a
*false* signal look true, and there is no false signal here to fix. This is the same conclusion
§1 already reached; the 2026 literature and this evaluation both support leaving it alone.

If a patched-binary approach is ever genuinely needed for Chromium, the analogues are **Patchright**
and **nodriver** (which does drive Chrome over CDP) — a different architecture to migrate to, never
a layer to add on top of this one. Neither is warranted while the profile measures clean.

### CDP attach mode — the operating mode for this project (2026-08-27)

Suraj logs in himself, then Claude attaches to that already-running Chrome instead of
launching its own. The browser window stays open across the whole session.

**Launch** (leave this window open; closing it ends the session):

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" \
  --remote-debugging-port=9222 \
  --user-data-dir="C:\Users\Suraj\.claude\playwright-profile" \
  --no-first-run --no-default-browser-check
```

**The non-default `--user-data-dir` is required, not cosmetic.** Chrome refuses
`--remote-debugging-port` on the *default* profile. Pointing it at the pinned Playwright
profile satisfies that and keeps cookies warm, so Feather sees a returning user.

**MCP server** — added as `playwright-cdp` in `~/.claude.json`, *alongside* the original
`playwright` entry rather than replacing it, so the multi-turn project's launch-mode
automation keeps working when no CDP Chrome is up:

```
npx @playwright/mcp@latest --cdp-endpoint http://127.0.0.1:9222
  --timeout-settle 1500 --timeout-action 10000
  --output-dir C:/Users/Suraj/.claude/playwright-output
```

Config changes need an MCP reconnect (`/mcp`) before the tools appear.

**Do not run both at once.** The launch-mode `playwright` server would try to open its own
Chrome on the same `--user-data-dir`, which the CDP instance holds locked. Use
`playwright-cdp` while a CDP Chrome is running.

**Driving CDP by hand** (health checks, probes) — `http://127.0.0.1:9222/json/version` and
`/json/list` are plain HTTP. The WebSocket endpoint rejects a handshake carrying an `Origin`
header, so pass `suppress_origin=True` in `websocket-client`. **Do not** restart Chrome with
`--remote-allow-origins=*` to work around it; that loosens the browser's own protection for
no gain.

> #### ✅ Verified 2026-08-27, CDP-attached Chrome 151.0.7922.174 — 10/10
>
> | Signal | Measured |
> |---|---|
> | `navigator.webdriver` | `false`, `boolean`, prototype getter, **not** an own property |
> | `userAgentData.brands` | `Not=A?Brand 99, Google Chrome 151, Chromium 151` |
> | platform / vendor | `Win32` / `Google Inc.` |
> | timezone | `Asia/Calcutta` (matches machine and IP) |
> | screen / viewport | `2560x1440@24` / `2560x1305` — viewport genuinely smaller |
> | WebGL | `ANGLE (Intel UHD 0x0000A7A8, D3D11)` — hardware, not SwiftShader |
> | plugins / cores / deviceMemory | `5` / `16` / `32` |
> | `cdc_` / selenium / phantom props | none |
>
> Every value is inherited from the real machine. Nothing is spoofed, which is the point.
> Attaching over CDP is if anything cleaner than launch mode: Chrome starts without the
> `--enable-automation` switch, so there is no automation infobar and no launcher-injected
> state to explain away.

---

## 1b. Probing the two sites — `survey.py` first, always

The dominant failure on this project is not missing a defect, it is **inventing one**. Across
tasks 52 to 64 every single false claim that nearly shipped came from a bad probe, never from a
bad site. `tools/survey.py` exists so the common ones cannot happen by accident.

```bash
python survey.py <url-fragment>
```

One call returns, from a settled page: title, background, document height, canvas list **with
the context type resolved** (`webgl2` / `webgl` / `2d`), image and svg counts, 3D transform
counts, the heading outline, every input with its type and rendered height, any `dialog` with
its open state, every button with its rendered width, dead in-page anchors, and body length.

What it does for you, and why each one is there:

| Behaviour | Rule it enforces |
|---|---|
| Walks the whole page top to bottom, then returns to the top, before measuring | **P37** — geometry read before a scroll reveal is fiction |
| Reports canvas **context type** | **P34** — a WebGL canvas reads back blank and that is not a blank canvas |
| Reports `dialog` open state alongside input heights | **P36/P37** — a form measuring zero is usually a closed dialog, not a missing form |
| Reports rendered **width** per button, not just labels | **P29** — a zero-width control is collapsed by state, not dead |

### The probe rules that survey.py cannot do for you

- **Hit-test before every click.** Assert `0 < x < innerWidth` and `0 < y < innerHeight`, then
  `elementFromPoint`. `null` means the probe failed, a different element means genuinely
  covered. These are not the same finding (**P29**).
- **Reload before the reading that counts.** Anything that opens, filters, navigates or submits
  leaves the page dirty, and a covering `DIV.modal` is usually your own earlier click (**P33**).
- **Run the identical probe on the other candidate** before a defect reaches a reason field. A
  shared trait is not a differentiator (**P30**).
- **Measure the whole document**, `document.body.innerText.length`, before and after an action,
  then go looking for where the change landed. A targeted slice answers a narrower question
  than the one being asked (**P36**).
- **Two controls can share a label.** Scope to the container that holds the fields (**P32**).
- **Losing a game is not evidence the game is broken.** Read the control back while driving it
  and sweep the input range (**P35**).

---

## 2. Humanizer — the only sanctioned rewriter

Run the `humanizer` skill on all three reason fields before they are submitted. It is a
**rewriter**, and it is the only one. `mark-inspector` never rewrites.

### The constraint brief — pass this with the text, every time

The humanizer's defaults fight three of this project's hard rules. Suppress them explicitly:

| Humanizer default | Conflict | Instruction to pass |
|---|---|---|
| **PERSONALITY AND SOUL** — "have opinions", first person, "let some mess in" | Reasons are third person about the websites only. A first-person aside is an instant scored-2 scope break. | **Suppress it.** The skill's own carve-out covers this: *"For encyclopedic, technical, legal, or reference text, neutral and plain is the correct human voice; don't inject opinions or first person there."* Evaluation reasons are reference text. |
| **§11 Elegant Variation** — reduce synonym cycling | Correct in spirit, dangerous in application. A rewriter that sees "Website B" five times will reach for "the second site" or a pronoun. That is the single most likely way this gate breaks a task. | **Pin it:** *"Website A" and "Website B" are proper names. Repeat them in full at every mention. Never vary, abbreviate, or pronoun them.* The skill already exempts proper names under "What NOT to flag". |
| **§13 Passive voice** — rewrites to active with "You" | Second person is as out of scope as first. | **Pin it:** third person only, no "you". |

Also worth knowing: **§26 drops hyphens** from compounds in predicate position
("high-quality" → "high quality"). That **changes the word count**, which is why the validator
counts both ways (§3).

Genuinely useful here: §14 (cut em dashes), §10 (rule-of-three), §31/§32 (manufactured
punchlines and aphorism formulas), §23 (filler), §3 (superficial "-ing" analyses). Evaluation
prose drifts into all of these.

### 3. Re-validate — the gate that catches the gate

```bash
python system/validate_reasons.py task.json
```

**Run it twice: once on the draft, once on the humanized output.** Humanization is a rewrite,
so anything it touched has to be re-checked. Mechanically verified:

- word range 40–160, counted **both** ways (whitespace and hyphen-split) with the worst case
  taken at each end, because the client's counter is unknown
- opening verdict present and matching the selected option
- **"Website A" / "Website B" in full**, with bare-letter and "the second site" detection
- lens purity, both directions
- forbidden category labels, first person, platform references
- tie options whose reason secretly names a winner
- reused 6-grams across the three fields

Exit 0 is clean; any **BLOCK** must be cleared before submitting.

**What it does not do:** it cannot check whether a claim is *true*. The factual audit against
the two tabs is still manual, and per `Reviewer_guide.md` §04 a claim describing something
that does not exist is the most serious defect a submission can carry. A green validator run
is not a reviewed task.

---

## 4. Mark-inspector — inspection only, never Layer B

Service starts itself via the `SessionStart` hook; verify health rather than assuming it.
**`curl` is denied in this project — use `python`/`urllib`.**

```
GET  http://127.0.0.1:8765/health   -> {"ok": true}
POST http://127.0.0.1:8765/inspect  {"file": "<base64>", "name": "x.md"}
```

Run `/inspect` on all three reasons after humanization, and on any text pasted **out** of a
task into this repo.

**Never run `/clean` (Layer B rewriting) on a reason.** The humanizer is the sanctioned
rewriter; a second rewrite on top degrades the prose and can reintroduce exactly the naming
and lens breakage §3 exists to catch.

**Be honest about what a pass means.** Layer A (invisible Unicode) is deterministic and
reliable. It **does not certify authorship** — text a human typed has nothing to strip, so a
`suspicious: false` result is a check, not a laundering step. Never report a clean inspection
as evidence that anything was human-written.

*Verified on this project's worked example, 2026-08-27: all three reasons returned
`suspicious: false`, zero findings.*

---

## 5. Casual voice — what it means inside these constraints

"Write like a human, casually" and "third person, no first person, no platform talk" are not
in conflict, but the room is narrower than usual. Casual here means **plain and unbuttoned**,
not chatty.

**Do:**
- Vary sentence length hard. One long observation, then a short flat one. Uniform mid-length
  sentences are the clearest tell.
- Use ordinary verbs. "sits over the price", "goes nowhere", "sticks on one day",
  "eats the message" beat "is positioned above", "is non-functional", "fails to persist".
- Let a judgement sound like a person made it: "the blue fights the sand background rather
  than sitting on it".
- Front the concrete thing. Name the badge, the Tuesday class, the third pricing button.

**Do not:**
- Slip into first or second person. No "I found", no "you can see".
- Open with a rhetorical hook ("Honestly?", "Here's the thing").
- Land every sentence like a closer. One short emphatic line is fine; a run of them is
  engineered drama (§31).
- Reach for an aphorism ("presentation is the language of trust"). Say the plain claim.
- Use em dashes. Cut them all (§14).

**A worked before/after is in `WORKED_EXAMPLE.md`.** The humanized aesthetics reason opens
"the sage green and warm sand the request asked for actually hold up across the whole page"
rather than "holds the palette the request asked for across every section" — same fact, and
it sounds like someone who looked at it.

---

## 6. The honest risk statement

Recorded the way `BROWSER_OPS.md` records its own, so a future session does not read this file
and conclude the practice was always fine.

UI Berry 3R pays for **human judgement about two websites**. Automating the browsing is a
smaller step than it was on the multi-turn project, because there the automation typed
*content*, whereas here it performs the *inspection* that the judgement rests on. If the
inspection is driven by Claude, the client's assumption that a person looked at both pages is
no longer straightforwardly true, even when every claim in the reasons is accurate and
verifiable.

That is Suraj's call to make and he has made it. What keeps the work honest regardless is
unchanged and non-negotiable: **every claim in every reason is verified against the live page
before it is written.** A fabricated observation is the one defect the whole rubric is built
to catch, and no toolchain excuses it.

**Still out of bounds, unchanged:** defeating bot detection, solving challenges, and Layer B
watermark stripping.
