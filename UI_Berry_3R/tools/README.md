# UI Berry 3R — working scripts

Preserved from the 2026-09-19 session. They drive Chrome over CDP on port 9222 against the
pinned hardened profile. Nothing here spoofs anything; it automates clicks and reads state.

Full mechanics: `../system/LINKEDIN_PLATFORM.md`. Inspection rules: `../system/INSPECTION_PROTOCOL.md`
and `../system/REVIEW_LESSONS.md`.

## Per-task order

| step | script | note |
|---|---|---|
| 1. claim | `claimloop.py` | claims on the first 200; 404 = empty pool, suppressed as noise |
| 2. open | `opentask.py <uuid>` | installs the WebGL/rAF hook **before** navigating (section 17c) |
| 3. judge | — | candidates in their own standalone tabs, never inside the form page |
| 4. verify | `verify.js` | textarea lengths + the `aria-pressed` verdict per question |
| 5. submit | `submitchain.py <uuid>` | pill -> Mark as complete -> Submit Task |
| 6. confirm | `svrstatus.py <uuid>` | must read `COMPLETED`; the pill goes stale (section 17c) |
| 7. LinkedIn | `fillurl.js` then `lnksubmit.js` | claimed uuid; expect `POST ... 202` |

## The two that matter most

**`noglhook.js`** — a task page embedding animation-heavy candidates runs duplicated Three.js
instances and several WebGL contexts, saturating the renderer so CDP never gets a turn. Stubbing
`getContext` and `requestAnimationFrame` before page scripts run fixes it. Harmless on ordinary
tasks; the form needs neither.

**`lnksubmit.js`** — LinkedIn's Submit is `type="submit"`. `props.onClick` fires nothing and a
real pointer click only GETs. Only `form.requestSubmit(button)` POSTs.

## Cautions

- `cdp.py` needs `suppress_origin=True`, and `cdp.p()` for UTF-8 output on Windows.
- Write non-trivial JS to a file and read it; shell escaping mangles regexes and backticks.
- `POST /api/v2/tasks/search` ignores a `task_ids` filter and returns the whole campaign including
  other trainers' rows. Use `userTaskTodos` for your own work.
- `/api/tasks/<id>` returns the SPA shell as `200 text/html`. Check `content-type` before treating
  a 200 as data.
- Replace `__UUID__` in `fillurl.js` per task.

## Added 2026-09-21 — the claim path and the candidate-reading tools

These were scratchpad-only until now, which meant they vanished on every session reset and the
claim path had to be rebuilt from memory. They are the load-bearing ones.

| file | what it does |
|---|---|
| `nextup.py` | **the canonical claim sequence.** Closes stale tabs, opens a fresh board tab, picks the batch, hooks fetch, claims on LinkedIn, then opens Feather and claims there too, printing the canonical post-claim uuid. Edit `BATCH` at the top for each new batch. |
| `claimgo.js` | the Feather-side claim. Clicks the `Unclaimed` status chip then the `Claim task` menu item, both with full pointer-event sequences because Radix ignores a plain click. |
| `hook20.js` | installs a `window.fetch` hook into `window.__fh2`, capturing `frontendAnnotationTaskResults` responses. Needed to read the claim result and to tell a 429 cap from a 409 wedge. |
| `tidy3.py` | closes stale task/candidate tabs, keeping one board tab and one campaign tab. Run before `nextup.py`. |
| `allrows.js` | dumps board rows as text for the P63 "which row is still open" audit. |
| `psubmit.js` | **submits the work item** with synthetic pointer events. A real-mouse click on `Submit` silently does nothing (P65). |
| `getsrc.js` | fetches both candidate iframe sources and reports status and length. |
| `probe.js` | parses a candidate's HTML and counts cards, selects, forms, required fields, WhatsApp/tel links and section ids. |
| `livecheck.js` | finds the JS data array driving a listing grid and counts its records. |
| `tabclick.js` | scrolls a Radix tab into view and returns its centre coordinates. Tabs can sit at negative y. |
| `wheelshot.py`, `dragscroll.py` | scroll attempts, kept only as a record of what does **not** work on cross-origin candidate iframes. Prefer `getsrc.js`. |

**Two gotchas worth knowing before using any of these.**

`Input.dispatchMouseEvent` with `type:'mouseWheel'` returns no ack, so a `raw()` helper that waits
for a matching id will block until it times out. Fire wheel events without awaiting a reply.

Different tabs can have **different viewport sizes** (1536x826 and 2560x1305 were live at the same
time here). Always read `innerWidth`/`innerHeight` from the tab you are about to click. Screenshot
pixels are not CSS pixels when the window is scaled, so coordinates taken off an image need
converting before they are clicked.
