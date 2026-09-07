# Uritorco fast path: the runbook that cuts the clock

Task #2935 took roughly 45 minutes. Most of that was avoidable. This file is the order of
operations that removes the waste, plus the paste-in prompt that starts a session already
knowing all of it.

## Where the time actually went

| Phase | First run | Why it was slow |
|---|---|---|
| Reading the platform | ~8 min | Discovered the form shape, the duplicate ids and the rating widgets by trial |
| Inspecting both apps | ~20 min | Read source AND drove the live app for the same findings |
| Drafting and gates | ~8 min | Two subagents run one after the other |
| Filling and submitting | ~9 min | Located every selector live |

Nothing above needs repeating. The platform mechanics are now recorded in
`PLATFORM_MECHANICS.md` and the selectors do not change between tasks.

## The five things that save the most time

**1. Download the zip first and read both sources before touching the previews.**
The zip auto-downloads to the Playwright output directory when the task page opens. Reading
`left/` and `right/` takes about ninety seconds and tells you exactly which of the prompt's
named fields each app implements, where the media queries are, and which handlers exist. Every
finding it gives you is a *hypothesis*, and the live check that follows is then a targeted
confirmation rather than an open-ended hunt.

**2. One batched measurement per app, not fifteen small ones.**
The single biggest waste on the first run was round-tripping to the browser for one number at a
time. `probe.js` in this folder runs the whole visual and layout audit in one `browser_evaluate`
call: page overflow at the current width, which columns fall outside the viewport, form-row
wrapping, pill fragment counts, empty-state text, media queries in effect. Two calls total, one
per app, per width.

**3. Run both gates at once.**
`mt-humanizer` and `mt-mark-inspector` were dispatched sequentially and cost about 50 seconds of
pure waiting. The inspector reads the file and never rewrites, so it does not depend on the
humanizer's output. **Dispatch both in the same message.** They finish in parallel and the
humanizer's edits get re-validated afterwards either way.

**4. Fill the whole form in one evaluate.**
Seven textareas and six ratings is thirteen interactions if done one by one. The ratings need
real clicks because they are MUI toggle buttons, but all seven textareas go in a single
`browser_evaluate` using the native setter, followed by ONE real keystroke to trigger autosave.

**5. Do not screenshot to find layout bugs. Measure, then screenshot to confirm.**
A full-page screenshot widens the canvas to fit the content, which HIDES horizontal overflow.
On this task the full-page capture of the right candidate showed a complete table; the viewport
capture showed the Actions column missing entirely. Measure `documentElement.scrollWidth`
against `window.innerWidth` first, then take a **viewport** screenshot to see what a user sees.

## The order that works

```
1. Open the Vercel task, confirm the project and that it is In Progress
2. Open the Feather task, let it settle 3s, read the Task prompt
   -> the zip has already downloaded; extract it
3. Read left/ and right/ source            (~90s, gives you the hypothesis list)
4. Live check, desktop 1440: probe.js on each app          (2 calls)
5. Live check, mobile 390:  probe.js on each app           (2 calls)
6. Exercise every control that matters: add, edit, delete, search, filter, toggle
   -> a control you did not click cannot appear in the Functionality field
7. Draft the 8 fields into a JSON file
8. validate_rubrics.py
9. Dispatch mt-humanizer AND mt-mark-inspector in the SAME message
10. Apply findings, validate_rubrics.py again
11. Fill: 6 rating clicks, 1 evaluate for all 7 textareas, 1 keystroke
12. Hard reload, verify every field survived
13. Mark as complete -> Submit Task
14. Vercel: Attempt URL (the LIVE task url), Save, Submit Task, confirm
```

## Traps that cost real time on the first run

**The Vercel task variables can hold a dead Feather link.** Task #2935's stored link
(`1eeab42d...`) returned "Task not found" while the live claimed task was `955b913c...`. The
task-variable link is the pre-claim id. **Trust the URL of the task that is actually In
progress and assigned to the account**, and put that one in Attempt URL.

**Preview origins expire and return 502.** Left's sandbox died mid-inspection. Refreshing the
Feather task page re-provisions BOTH apps on brand new origins. This is preview infrastructure,
not an app defect, and it must never be rated against a candidate. A new origin also means
empty localStorage, so redo any persistence test there.

**Left and Right share element ids.** `root_rule_0_rationale` exists twice. `getElementById`
always returns the Left one. Disambiguate by x-position (Left < 760 < Right) or Playwright
`nth=0` / `nth=1`.

**A `confirm()` or `alert()` blocks the next call.** Both apps use them for delete and save.
Click, then `browser_handle_dialog`. The click result will say a modal is present.

**favicon 404s are sandbox noise.** Not a finding.
