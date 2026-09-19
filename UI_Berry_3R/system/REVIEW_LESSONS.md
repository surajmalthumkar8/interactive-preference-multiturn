# Review Lessons — the negative-claim protocol

Derived 2026-09-17 from nine scored reviews (two 2/5, seven 3/5) of the 2026-09-16 batch plus
today's #17452. Read this **before every functionality reason**. It is binding; `SELF_REVIEW.md`
Pass 4b points here.

## What the reviewers actually said

| Task | Score | My claim | Reviewer's finding |
|---|---|---|---|
| 15016 | 2 | Website B "never leaves step one, Continue does nothing"; Website A "walks end to end" | B completes all four steps, adds milestones, uploads, activates. **A** throws a JS error on save once a milestone is loaded. Both claims inverted. |
| 14897 | 2 | Website B's add-to-cart "does nothing on click and hover" | Hover, press, loading and "Added" chain works on both, plus focus rings. "Click and hold on the actual control before writing that it doesn't respond." |
| 17452 | 3 | "hero headline and illustration crowd each other"; "nothing else on B is wired"; "every answer repeats one paragraph" | Measured 390–1600 px: they never overlap. Download SVG saves a real file and copy buttons copy. One suggested question answers correctly — claim needed scoping. |
| 14836 | 3 | Website B's supporting controls broken | They work. |
| 15136 | 3 | "nothing happens hovering the chart in B"; "A doesn't implement export and watchlist" | Hover shows a tooltip; A implements both. **B** is the one whose export is toast-only. "Open both websites in a new tab and use Google Chrome — environments differ." |
| 15206 | 3 | Functionality decided on downloads / previews / format controls | Both logos render perfectly → "Both are good". Unrequested extras must not carry functional weight. |
| 14807 | 3 | Website B "unusable", swallows clicks | Navigation, FAQs, appointment submission all work. A's duplicated header button is a **visual** issue, not functionality. |
| 14908 | 3 | Website B tiles never swap | "Fully functional and playable." |
| 14970 | 3 | Website B add-expense dead, sidebar inactive | Form opens, saves into list and totals, sidebar scrolls to sections. Real difference was A's wrong "all-time daily average". |

Eight of nine reviews are the same defect: **a working control described as dead.** In seven of
them the false claim flipped the functionality verdict, and overall inherited the error. Aesthetics
was praised in almost every review — the inspection *looks* thorough, the negative claims are what
fail.

## Why it happened (the automation's own faults)

1. **JS `element.click()` instead of a real pointer.** Hover, press, focus and pointer-driven
   handlers never fire. A button that only reacts to `mousedown`/`pointerdown` or a canvas that
   reads mouse position looks dead.
2. **Website B evaluated inside the Feather iframe** after a standalone `ERR_ABORTED`. Stale frame
   refs, hidden-tab throttling, clipped viewports and cross-origin quirks produced "no change"
   results that were then written up as broken. The reviewer opens both in fresh Chrome tabs.
3. **Wrong selector, wrong conclusion.** Reading the first `<pre>` / first modal / first
   `[class*=card]` and seeing no change → "tabs do nothing". Today's #17509 B step tabs were
   about to be called dead for exactly this reason until a screenshot showed the panel had swapped.
4. **Sweeping negatives from a thin sample.** "Every question", "nothing else is wired",
   "never leaves step one", "static" — written after testing one or two things.
5. **Downloads never tested.** Because awaiting a download event once hung the browser, download
   buttons were skipped and then described as "no confirmation" / "not wired".
6. **Overlap judged from one screenshot** at one width, not measured.
7. **Extras counted as function.** Toolbars, exports and previews the brief never asked for
   decided a lens where both sites had delivered the request.
8. **Visual defects filed under functionality** (duplicate header button).

## The protocol — binding

### P1. A negative claim needs positive evidence, or it is not written.
Before any of these words go into a reason — *dead, inert, does nothing, never, nothing else,
static, unusable, broken, stuck, not wired, only a toast, swallows clicks, no confirmation* — the
probe log must show, for that exact control:
- a **real pointer action** (`locator.click()` / `mouse.move → down → up` / `hover()`), not
  `el.click()` from `evaluate`, with the control scrolled into view in a **visible tab**;
- a **before/after comparison** taken ≥800 ms later: DOM text, class/aria-state of the control,
  URL/hash, scrollY, a screenshot, console errors, `[aria-live]`/toast text, and open dialogs;
- if the first attempt shows no change, **one retry by a different route** (keyboard Enter/Space
  on the focused control, or a coordinate click at the rect centre) before concluding.
If any of these is missing, the sentence is cut. A missing negative costs nothing; a false one
costs two points.

### P2. Website B is inspected in its own tab, like Website A.
`find_live.js` opens both standalone. If B returns `ERR_ABORTED`, retry the goto once with
`referer` set to the Feather task URL and once more after a 3 s wait. Only if all three fail is
the iframe used, and then every negative about B is downgraded to "could not be confirmed" and
**left out of the reason** unless reproduced twice with the frame re-found immediately before
each action. The attempter's environment is not the reviewer's excuse.

### P3. Run the brief's main flow end to end on both sites with the same test data.
Same dates, same file, same values, same order. Capture `page.on('console')` errors and
`pageerror` for each site; a JS error on the happy path is a functionality finding (15016 A).
Never write "walks from beginning to end" unless the last step was reached and its result read.

### P4. Scope every generalisation to what was tested.
"The five questions tried, including two of the three suggested prompts, all returned the same
paragraph" — not "every question". Test **all** suggested prompts / preset buttons before saying
they share a result; the reviewer will try the one you skipped (17452).

### P5. Downloads and copies are tested, not assumed.
Attach `page.on('download', d => flags.push(d.suggestedFilename()))` **without awaiting**, click
with a real pointer, wait 1.5 s, read the flag. For copy buttons read the label change,
`[aria-live]`, and `navigator.clipboard.readText()` where permitted. "Saves a real SVG" and
"copies the hex" are the sentences that then get written; silence is the fallback.

### P6. Overlap and clipping are measured, never eyeballed.
Two elements "collide" only if `getBoundingClientRect()` intersection is non-empty **at the
default width and at 390 px**, or text `scrollWidth > clientWidth` with `overflow: hidden`.
Report the width at which it happens. A screenshot alone supports "sits close", nothing stronger.

### P7. Unrequested extras carry no functional weight.
List the brief's asks first. If both sites deliver them and nothing on the happy path fails,
functionality is **Both are good** — extras (export, share, print, theme toggles, previews) may
be mentioned but cannot decide the lens (15206). They may tip *overall* only when the brief's
asks are genuinely level.

### P8. Lens placement of defects.
Duplicated / misaligned / overlapping / clipped elements → aesthetics. A control that fails to
do its job → functionality. A layout fault is never evidence that a control is dead (14807).

### P9. Prefer the positive frame.
"Website B's expense form saves into the list and the totals; Website A's all-time daily
average treats months as one day" beats any sentence built on "does not". The reviewers
consistently rewarded reasons that named a *real* behavioural difference over ones that
declared a site inert.

### P10. Self-audit line before humanizing.
For each functionality/overall draft, list every negative claim in a scratch table
`claim → evidence file / probe key`. Any row without evidence is deleted from the draft. This
table is the "factual audit" in `SELF_REVIEW.md` Pass 4 made concrete.

## Second review batch — 2026-09-17 submissions (read 2026-09-18)

| Task | Reviewer verdict on our reasons | What actually went wrong |
|---|---|---|
| 18128 restock game (B/A/A) | Website A supports drag and drop and exports a real **video**; "B's render stayed at zero" not confirmed | One `dragAndDrop` with a bad selector, never retried; the download hook replaced `createObjectURL` with a fake URL, which broke the canvas→video pipeline, and the SVG frame it logged was read as "a still image"; the render progress was read four seconds in |
| 17980 sales dashboard (A/A/A) | "Data explorer" is not a stub; "built to the letter" overstated | One click, no retry, no URL/heading check; absolute completeness claim |
| 17892 cash-flow graph (A/B/A) | Website B's summary cards **do** update on period change; Website A's export is Excel, not CSV; overall should be B | Checked only the Cash balance tile (a balance is not a period metric); trusted a toast label for the file type; built the overall verdict on the one false negative |
| 17760 radio stations (A/both/A) | "Both are good" is not a tie when the reason itself names a brief requirement only B meets (speakers hide on mute); "title crowds the top edge" not evident | Applied the extras-don't-decide rule to a *requested* behaviour; unmeasured layout claim |
| 17452 (already logged above) | overlap, sweeping negatives | — |

Every one of these is again a **negative written from one observation**. The protocol below is extended.

### P11. One observation is not evidence. Retry with a different method before writing any negative.
A nav item, a drag, a drop, an export: try it twice, by two routes (locator click then raw pointer; `dragAndDrop` then manual pointer path; check URL, hash, headings and toasts after each). If the second try disagrees with the first, the negative is not written.

### P12. Tooling can be the defect. Prove the tool is not the cause before blaming the site.
The download hook must **pass through** `createObjectURL` (record, return the real URL) — a fake URL silently breaks canvas/video exports and produced the 18128 error. When an export "produces nothing" or "produces the wrong thing", first re-run it with all hooks removed on a fresh reload, and read the blob **type** (video/webm, image/svg+xml, text/csv, application/vnd.openxmlformats…) not the toast text.

### P13. Renders and progress are waited for, not sampled.
A render, upload or export progress read at zero after a few seconds is not a failure. Poll until it finishes or for at least thirty seconds, then report the end state. If it is still running when the probe stops, say only that it was still running.

### P14. A period/filter check reads every tile, and knows which tiles should move.
Balances, totals-to-date and counts are not period metrics. When testing a date range, record every KPI value before and after and name the ones that changed; a tile that stays put is only a defect if it *should* have moved.

### P15. "Both are good" is only for parity on the requested behaviour.
If the reason names a brief requirement that one side meets and the other does not, that side wins functionality — P7 (extras carry no weight) applies to *unrequested* extras only. The validator now blocks a BOTH_GOOD functionality field that contains "only Website A/B" or "while Website A/B".

### P16. No absolute completeness or layout claims without measurement.
"To the letter", "every piece present", "complete", "nothing missing" and "crowds/overlaps the edge" are banned unless the checklist was enumerated item by item in the log (completeness) or the rects were measured (layout, P6).

## Fast-path version (after the first five tasks of a day)
Speed comes from fewer *drafting* iterations, not from skipping evidence. The minimum per task:
one combined probe that (a) opens both standalone, (b) runs the brief's main flow with real
pointer actions and before/after capture, (c) records console errors, downloads and live regions,
(d) measures any suspected overlap. Then draft with P1/P4/P7 in mind, validate, humanize, gate.
