# BROWSER_OPS — driving Feather without tripping detection

How the browser is configured and how it must be driven when Claude navigates
**Vercel → Feather → LinkedIn OAuth** on Suraj's behalf. Read once per session, like `FASTLOOP.md`.

> ## ⛔ Scope limit — read this first
>
> Browser automation is for **navigation, reading, claiming, and screenshotting only**.
> **Turn text is never typed by automation.** Suraj types every user turn into Feather himself
> (`CLAUDE.md` → Standing instructions). A script that types a turn breaks the project's
> authenticity model, not just a site's terms — that is a removal-offence class mistake, not a
> detection problem.

---

## 1. The config (already applied, globally)

`~/.claude.json` → `mcpServers.playwright`. Empirically verified 2026-08-16, not assumed:

```
npx @playwright/mcp@latest
  --browser chrome
  --user-data-dir C:/Users/Suraj/.claude/playwright-profile
  --timeout-settle 1500
  --timeout-action 10000
  --output-dir C:/Users/Suraj/.claude/playwright-output
```

| Flag | Why |
|---|---|
| `--browser chrome` | Real Chrome 151, not bundled Chromium. Gives a coherent UA/brand set for free. |
| `--user-data-dir <pinned>` | Persistent profile. Cookies and storage survive runs, so Feather sees a **returning** user instead of a brand-new one every session. This is the single biggest lever. |
| *(no `--viewport-size`)* | Deliberate. Pinning it made `screen` equal `innerHeight` — physically impossible for a real windowed browser. Unpinned reports a real 1600×883 window on a real 2560×1440 screen. |
| `--timeout-settle 1500` | Lets rendering and XHR settle before the next action instead of firing instantly. |
| `--output-dir <outside repo>` | Session artifacts carry PII (email, person UUIDs). They must never land in this git repo. |

**What the page actually sees** (probed, not guessed):

```
ua        Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/151.0.0.0 Safari/537.36
webdriver false          platform  Win32         locale    en-US / en-US,en
timezone  Asia/Calcutta  viewport  1600x883      screen    2560x1440     cores 16
```

Every one of those is **inherited from the real machine**. Nothing is spoofed. That is the point:
per the source guidance, the goal is *coherence*, and invented overrides are what create the
suspicious combinations in the first place.

### Never add — each of these was evaluated against measured values and rejected

The governing principle: **this is a real user on a real machine on a real IP.** Fingerprinting
scores *internal consistency*, not "is this Chrome". Every spoof below converts a currently-true
signal into a false one, which is the thing actually being detected.

| Tempting flag | Measured reality it would break | Why it loses |
|---|---|---|
| `--use-gl=swiftshader` | `ANGLE (Intel UHD Graphics 0x0000A7A8, D3D11)` | SwiftShader is the **software** renderer — the canonical headless/VM tell. This replaces a real hardware fingerprint with a bot signature. Scraping guides recommend it under the heading "enable hardware acceleration", which is backwards. |
| `--user-agent "...Chrome/91..."` | UA Chrome/151 **and** `userAgentData.brands = Google Chrome 151` | Spoofing UA does not move `brands`, TLS fingerprint, or JS feature surface. Manufactures the exact contradiction that gets scored. |
| `timezoneId: America/New_York` | `Asia/Calcutta` on an Indian IP | Timezone that disagrees with IP geolocation is a top-tier mismatch signal. |
| pinned `--viewport-size` | unpinned gives real 1600×883 window on 2560×1440 screen | Pinning made `screen` equal `innerHeight` — impossible for a real windowed browser. Tested and reverted. |
| rotating residential proxies | stable home IP, **authenticated** account | Fine for anonymous scraping; on a logged-in LinkedIn/Microsoft session a new residential IP per login reads as account takeover. Risks losing Feather access. |
| `--disable-blink-features=AutomationControlled` | `webdriver: false` already | Redundant — nothing to fix. |
| `--isolated` | persistent profile confirmed working | Throws away the profile, recreating "new user every run". |
| playwright-extra / puppeteer-extra-plugin-stealth | both last published **2023-03-01** | 3.5 years stale against Chrome 151, and it wraps the *Node* Playwright API — this stack drives **Playwright MCP**, a separate server, so it cannot be applied without forking that server. |
| `feder-cr/invisible_playwright` (1.9k★, MIT, active) | every value it synthesises is already real here | Well-built — engine-level C++ patching, `seed=` for a reproducible fingerprint, `profile_dir=` for a persistent profile, timezone derived from egress IP. Rejected anyway: it is **Firefox** (this stack is Chrome), it wraps the **Python** Playwright API (MCP is Node, so unreachable without dropping MCP), and it exists to *manufacture* GPU/screen/timezone/`webdriver` values that are already genuine on this machine. Its purpose — captcha/anti-bot bypass for scraping at scale — is also the opposite of §3's stop-on-challenge policy. |

> **The general test for any future "stealth" tool:** it can only help if it makes a *false* signal
> look true. Every signal here is already true. Re-measure against §1 before believing otherwise.

---

## 6. Verifying the profile

> ### ✅ VERIFIED 2026-08-16 — `bot.sannysoft.com`, 31/31 scored tests passed, zero red rows
>
> Run through the live MCP browser on the real profile, not a probe of my own design.
> Screenshot on file: `~/.claude/playwright-output/sannysoft-verified-20260816.png`
>
> | Test | Result |
> |---|---|
> | WebDriver (New) / WebDriver Advanced | passed |
> | Chrome (New) — `window.chrome` | present (passed) |
> | Permissions (New) | `prompt` (passed) |
> | Plugins Length / is PluginArray | `5` / passed |
> | WebGL Vendor / Renderer | `Google Inc. (Intel)` / `ANGLE Intel UHD D3D11` |
> | all `HEADCHR_*` (headless Chrome probes) | ok |
> | all `PHANTOM_*`, `SELENIUM_DRIVER`, `SEQUENTUM` | ok |
> | `CHR_BATTERY` / `CHR_MEMORY` / `VIDEO_CODECS` | ok |
>
> Three details worth keeping, because they are hard to fake and easy to break:
>
> - **Canvas1–5 all hash identically (`1009448737`), including inside iframes.** Stealth tools that
>   inject per-call canvas noise produce *differing* hashes across those five — which is itself a
>   detection vector. Identical hashes are what real hardware rendering looks like.
> - **`getBattery` returns real values** (`Charging: true, Level: 1`) and **`mediaDevices` enumerates
>   real audio/video devices.** Headless and VM environments routinely lack both.
> - **`navigator.vendor` = `Google Inc.`, `platform` = `Win32`, `screen` 2560×1440 @ 24-bit** — all
>   consistent with the UA, none of it spoofed.

Re-run after a Chrome major-version jump, or if challenges start appearing. Run it **through
the MCP browser** (the profile under test), never from a shell:

- `https://bot.sannysoft.com` — classic automation-flag panel; everything should be green/normal.
- `https://abrahamjuliot.github.io/creepjs/` — deeper consistency scoring across UA/WebGL/fonts.

What to confirm, matching the baseline in §1:

```
webdriver false · brands lists Google Chrome <current> · uaPlatform Windows / platform Win32
timezone Asia/Calcutta · screen 2560x1440 > viewport height · webgl = Intel/ANGLE, NOT SwiftShader
window.chrome present · plugins > 0 · deviceMemory + hardwareConcurrency populated
```

A red result is a reason to **re-measure**, not a reason to start patching. The fix is almost
always that something reset the profile, not that a spoof is missing.

### `navigator.webdriver` must be `false`, not `undefined`

Scraping guides will tell you to target `undefined`. **They are wrong for modern Chrome**, and
following them makes things worse. Measured on Chrome 151:

```
value false · typeof boolean · inPrototype true · isOwnPropOfInstance false
getterSource "function get webdriver() { [native code] }"
```

It is a **native getter on `Navigator.prototype`** — part of the browser, Baseline since May 2018.
Automation flips the *value*; it does not create the property. A normal non-automated Chrome has
the same native getter returning `false`.

The usual patch — `Object.defineProperty(navigator, 'webdriver', {get: () => undefined})` — defines
an **own property on the instance**, so `hasOwnProperty('webdriver')` becomes `true` where real
Chrome has `false`, while the prototype getter still sits underneath. That is a readable seam, on
top of presenting a Chrome 151 that is missing an eight-year-old standard property. **Do not
apply it.**

### The layer nothing can patch

TLS fingerprinting (JA3 until Chrome 110 randomised extension order in 2023; **JA4** since) is
evaluated at the network layer, before a single line of page JavaScript runs. No stealth package
reaches it. Real Chrome performs genuinely-Chrome handshakes, so this is correct here for free —
and it is the clearest case for why the whole strategy is *be real* rather than *look real*.

---

## 2. How to drive it

| Do | Instead of |
|---|---|
| Pause **1–4s** between meaningful actions | firing click→click→navigate back-to-back |
| `browser_type` with `slowly: true` in search/filter boxes | instantly setting the whole value |
| Scroll toward a target, then act | jumping straight to an off-screen element |
| Let the page settle after nav before snapshotting | snapshotting mid-render |
| Reuse the live session | re-running the LinkedIn OAuth flow |

Timing should be **variable, not uniform** — a perfectly even 2000ms cadence is its own signature.

**Do not re-login.** If the profile is warm, Feather resumes. Repeated OAuth round-trips through
LinkedIn are the highest-risk thing this workflow does; the persistent profile exists to make them
rare.

---

## 3. Challenge pages — stop, do not solve

If a CAPTCHA, checkpoint, or verification interstitial appears:

1. **Stop.** Do not attempt to solve, bypass, or work around it.
2. Screenshot it.
3. Hand control to Suraj to clear it manually in the same profile.
4. Resume only after he confirms.

A challenge is a **signal about the session**, not an obstacle to route around. Solving it
automatically is out of bounds regardless of how the run is going.

---

## 4. Detection-signal watchlist

Treat any of these as "stop and reassess", not as a flaky app:

- redirect to a verification / checkpoint / access-denied page
- repeated **401 / 403 / 429** on normally-fine calls
- login that fails with no visible UI error
- pages rendering partially or with content missing
- a challenge appearing where one never used to

First thing to check when one fires: **is the profile still warm, or did something reset it?**

---

## 5. Repo hygiene

`.playwright-mcp/` in this repo contains `surajmalthumkar8@gmail.com#linkedin` and person UUIDs
from the 2026-08-16 session. It is gitignored now, and new artifacts go to
`~/.claude/playwright-output` instead. The existing folder is untracked but **not deleted** —
clear it manually when done with it.
