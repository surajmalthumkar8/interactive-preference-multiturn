# Uritorco: the paste-in start prompt

Start Claude Code **in the repo root**, then paste the block below as the first message. It
loads the rules, the mechanics and the fast path in one go, so the session does not spend the
first ten minutes rediscovering the platform.

Then every task after that is one line: paste the two URLs.

---

```
This repo is my working setup for the Uritorco WebDev side-by-side rating project on
Feather. Set yourself up before we do anything else.

READ, in full, from disk, in this order:
  1. Uritorco/system/BATCH_RULES.md        - the client's six corrections, these outrank everything
  2. Uritorco/system/PLATFORM_MECHANICS.md - measured selectors, do not rediscover them
  3. Uritorco/system/FASTPATH.md           - the order of operations that keeps this quick
  4. Uritorco/system/LEARNINGS.md          - what previous tasks got wrong

CONFIRM back to me in one line each:
  1. The three rubric fields carry NEGATIVES ONLY. No praise about a candidate in
     completeness, functionality or visual. Positives belong only in the preference
     rationale, which needs pros AND cons for both candidates.
  2. Nothing negative to report means the score is 5, not 4. A 5 uses the exact
     phrase "Excellent with no meaningful issues." and nothing else.
  3. The preference rationale opens with the selection restated verbatim, e.g.
     "The left candidate is slightly preferred because".
  4. Completeness carries the most weight when picking the winner.
  5. A fault that needs a specific sequence gets the steps written out.
  6. Every claim is verified against the live app before it is written. Measure
     privately, then describe what a person would see. No pixel counts in the prose.
  7. Claim from the Vercel dashboard, never from the Feather campaign list.

HOW TO RUN EACH TASK - follow FASTPATH.md, and specifically:
  - Extract the auto-downloaded zip and read left/ and right/ source FIRST. It is 90
    seconds and it turns the live inspection into targeted confirmation. Findings from
    source are hypotheses, never conclusions.
  - Use Uritorco/system/probe.js in ONE browser_evaluate per app per width. Do not
    round-trip for one number at a time. Desktop 1440, then mobile 390.
  - Never diagnose layout from a full-page screenshot. It widens the canvas and HIDES
    horizontal overflow. Measure scrollWidth against innerWidth, then take a VIEWPORT
    screenshot to confirm.
  - Click every control that matters. A control you did not exercise cannot appear in
    the Functionality field.
  - Dispatch mt-humanizer and mt-mark-inspector IN THE SAME MESSAGE so they run in
    parallel. The inspector never rewrites, so it does not wait on the humanizer.
  - Run validate_rubrics.py before AND after the humanizer.
  - Fill: 6 rating clicks, ONE evaluate for all 7 textareas, ONE real keystroke for
    autosave. Hard reload and verify before submitting.

Then wait. From my next message on I paste a Vercel task URL and a Feather task URL and
you run the whole thing end to end without stopping to ask. No preamble, no narration of
what you are about to do. Tell me the six ratings, the preference and the decisive
finding when it is submitted on both platforms.
```

---

## After that, each task is one line

```
https://annotation-platform-henna.vercel.app/tasks/<id>
https://msft.feather-prod.azure.com/tasks/<id>
```

## What actually makes it faster

The slow parts of the first run were all one-time discovery: learning the form shape, finding
the selectors, and probing the apps one measurement at a time. Those are now written down.

The two changes that save the most on every future task are **batching the measurements** into
one `probe.js` call per app per width instead of a dozen round trips, and **dispatching both
gate agents in the same message** instead of one after the other.

The one thing worth spending time on is clicking the controls. A rating that says a control
works, written without clicking it, is the defect this whole rubric exists to catch.
