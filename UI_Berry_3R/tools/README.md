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
