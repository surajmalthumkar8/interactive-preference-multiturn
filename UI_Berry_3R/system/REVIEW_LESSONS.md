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

---

## The eleven near-misses of 2026-09-19 — a catalogue of causes

Eleven times in one session a control read as dead and **every one was the instrument, not the
site**. Zero real dead controls were found across seven tasks. That ratio is the point: when a
probe says "nothing happened", the prior should be that the probe is wrong.

Grouped by root cause, with the check that settles each:

### 1. The probe never reached the element (4 of 11)
| Case | What happened | The check |
|---|---|---|
| Showcase cards "dead" ×3 | Clicks landed below the fold; `inViewport:false` | Assert `getBoundingClientRect()` is inside the viewport **and** `document.elementFromPoint(cx,cy)` returns the target, before clicking |
| Option buttons "not registering" | Three synthetic clicks batched in one `evaluate`; only the last survived | One call per control, with a settle between |
| Textarea insertText wrote nothing | Click did not focus it; `activeElement` was BODY | Call `.focus()` explicitly, then verify `document.activeElement.id` |
| Avatar toggle "dead" | Settle too short, read before React re-rendered | Settle ≥ 2s before re-reading state |

### 2. The measurement looked in the wrong place (4 of 11)
| Case | What happened | The check |
|---|---|---|
| Theme switch "no change" | Sampled a transparent wrapper, not the themed panel | Sample an element with a non-transparent background and a real size |
| Pose rig "dead" | Read `getAttribute('transform')` (null) and matched a section heading, not the readout | Measure rendered geometry (`getBBox`) when an attribute reads null |
| Export PNG "produces nothing" | Hooked `createObjectURL`; this export used `toDataURL` + anchor download | Hook **all three**: `toDataURL`, `toBlob`, `HTMLAnchorElement.click` |
| Route "404" | Typed the URL from the visible label ("Youths"); real href is `youth` | Read the `href` from the DOM, never retype it from the label |

### 3. Tested in a state where the control has no meaning (2 of 11)
| Case | What happened | The check |
|---|---|---|
| Pause key "dead" | Pressed on the death screen | Establish the state the control belongs to first, then press |
| Contact form "does nothing" | Two submits were rejected by validation on a field I had left empty | Diff `innerText` before/after; the page names the missing field |

### 4. The API cannot be observed the naive way (1 of 11)
| Case | What happened | The check |
|---|---|---|
| "Neither game has audio" | Scanned `window` for an AudioContext; it is closure-held and needs a gesture | `Page.addScriptToEvaluateOnNewDocument` wrapping the constructor, reload, **then** a real gesture |

## The generalisation

Before writing any negative, answer these four:

1. **Did my event reach the element?** (in viewport, hit-tested, focused)
2. **Am I reading the thing that would change?** (right element, right property)
3. **Is the control meaningful in this state?** (alive vs dead, open vs closed, paused vs running)
4. **Would this API even be visible to my probe?** (closure-held, gesture-gated, different method)

If any answer is "not sure", the negative does not ship. A missing negative costs nothing.

## Corollary: measuring something does not entitle you to claim it

Also this session, three measurements were taken and then **deliberately dropped**:
a bone index summing to 186 against a stated 206 (the gap is exactly facial bones plus
ossicles, which a body radiograph would not itemise); ribs drawn as an evenly pitched ladder
rather than anatomical curves (the brief asked for visible bones, not a medical illustration);
and a "clipped" first message that was only the transcript's scroll position after my own
test sends. Rigour includes discarding true-but-irrelevant findings.

## The instrument, not the site — what 2026-09-19 actually proved (P17–P20)

Across this batch, **twelve claims of a dead control were investigated and twelve were my own
tooling.** Zero were real. That ratio, not any individual catch, is the finding: on a batch where
both candidates are competent, the base rate of genuinely dead controls is very low, and the base
rate of *probes that miss* is high. Weight the prior accordingly.

**P17 — Attach the listener before the thing you are diagnosing runs.**
A Feather task page hung six consecutive renderers. An hour went into probing the wedged tab, which
by definition cannot answer. `Runtime.enable` + `Log.enable` on a *blank* tab before navigating
produced the cause in one shot: `THREE.WARNING: Multiple instances of Three.js`. When something is
already stuck, stop interrogating it and instrument the next attempt from before it starts.

**P18 — Diagnose a service by its cheapest page.**
Feather's root rendered perfectly the whole time one task page was unloadable. Probing with the
heavy page made a healthy service look dead and produced a wrong written diagnosis. Always have a
cheap control for "is the service up" that is separate from "is this page up".

**P19 — A disconfirming test only counts if it removed the suspect.**
I cleared the animating ocean canvases as the cause because two wedge attempts had those *tabs*
closed. But the task page embeds its own copies of both candidates, so closing the tabs removed
nothing, and the original suspicion was right all along. Before accepting "it still happened
without X", verify X was actually absent.

**P20 — Verify the write at the layer that stores it.**
After Submit Task the UI pill still read "In progress" while the server already held
`workflowStatus: COMPLETED`. Conversely a textarea can read back full in the DOM and still not be
saved. Neither direction of UI state is evidence; check the store.

**The corollary that ties these together.** Three of the four are the same mistake in different
clothes: trusting a reading taken from the wrong place. A measurement is only evidence about the
thing it actually touched. Before any negative claim ships, name the layer the measurement came
from and confirm that layer is the one the claim is about.

## P21. A control that reads as dead is usually a control you never actually hit

Five times in this run a control looked broken and was not. Every one was my own probe.

- **Task 34.** Website B's add-to-cart badge stayed at 0. The card I targeted had been
  hidden by a filter I had left applied, so the button sat inside an `article` with
  `display: none` and my click went nowhere. Resetting the filter fixed it first try.
- **Task 37.** Website B's quantity stepper read stuck at 1. The button was below the
  fold; the click never landed. After `scrollIntoView` it counted 1, 2, 3, 4 cleanly.
- **Task 40.** Website B's department filter appeared not to recalculate. Opening the
  menu in one call and clicking the option in the next let the popup close in between.
  Done in a single evaluated script it worked immediately.
- **Task 33.** The inverse, and the reason this rule is not "assume it works": Website A's
  ball genuinely never launched. What made that finding safe was the control case, the
  same harness scored on Website B on the first serve.

**The rule.** Before a control goes in a reason field as broken, it needs all four:
1. the element scrolled into view and confirmed hit-testable at the coordinates used,
2. no ancestor with `display: none` or zero height,
3. the interaction performed atomically where a popup is involved,
4. a control case, either the same harness succeeding on the other candidate or the same
   control succeeding under a different route.

Three of those four failures would have shipped a false negative, which is the exact
class of error that produced eight of nine historical bad scores.

## P22. Check a claim against its own neighbour before shipping

Task 40's overall field said Website B "buries most of its job roles in one bucket". The
functionality field, forty words earlier, correctly said the opposite: Website B names
nine roles and Website A buckets them. Both fields were drafted in one pass and the
inversion survived until the validator forced a rewrite for an unrelated lens word.

Read the three fields against each other as a set, not just each against the notes. Where
two fields touch the same fact they must agree, and the cheapest check is to grep the
draft for the candidate names and confirm each claim points the right way.

---

### P23 — a slow control needs a slow window before it is called dead

Task 42, Website A ("Quiet Tide"). Its tidal rhythm marker was sampled twice over six
seconds and did not move a pixel. On that evidence the honest-looking write-up was "the
tidal indicator is static", and it would have been wrong.

Watched over seventy seconds instead, the marker moved (1463 -> 1465.2) and the state
label turned from TIDE RISING to TIDE FALLING as it passed high water. The control was
working the entire time. It was modelling a tide, and a tide is supposed to be slow.

**The rule.** Before reporting that something does not change, ask what period the thing
being modelled would actually have, and sample for at least one full cycle of it. Tides,
day/night cycles, weather and season controls are all deliberately slow. A six-second
window proves nothing about a two-minute cycle. Where the page states its own cycle
length (Website B printed "Cycle length 2.0 min"), use that number rather than guessing.

This is P21 in the time dimension: P21 asks whether the control was reachable, P23 asks
whether the observation window was long enough for the effect to be visible. Both failure
modes produce the same false negative.

### P24 — localize a partial failure to a region before describing it

Same task, Website B. Pause looked broken: pixels kept changing after it was pressed, on
two separate runs, even after letting eased transitions settle. Calling it "pause does not
work" would have been both wrong and unfair, since B's pause does most of its job.

Hashing three horizontal bands separately (sky, open sea, shore surf) showed sky and sea
frozen, the clock held at 15:11, the tide held at 2.8m, and only the **surf band** still
animating. The accurate claim is narrow and checkable: pausing stops the swell, the light
cycle and the tide, but the shore foam keeps running.

**The rule.** When a whole-canvas check says "still moving", split the canvas and find out
what is moving before writing anything. A defect that affects one band is a different
claim from one that affects the page, and the narrow claim is the one that survives review.

---

### P25 — a synthetic click proves nothing about a canvas game

Task 44, Website A ("World Cricket Champions"). The first probe called
`element.click()` on the QUICK MATCH card and the screen did not change. Written up
from that, the claim would have been "the mode cards do not respond", and the whole
evaluation would have collapsed on it.

A real `Input.dispatchMouseEvent` at the same coordinates opened team selection
immediately. The game listens for pointer events on a canvas; a synthetic `.click()`
never reaches it.

**The rule.** Before any negative claim about a control, the interaction has to have
gone through the real input pipeline. `mclick.py` sends a genuine mouse press and
release at page coordinates; `apress.py` sends real key events. A `.click()` from
`runjs.py` is fine for *positive* evidence (if the page reacted, it reacted) but is
worthless as evidence of a defect. This is the same principle as section 21 on the
Feather form, where a synthetic `.focus()` left the field uncommitted.

### P26 — an overlay is not a broken control, and the state text lags

Task 44 produced two more near misses on the same task, both worth naming.

**The replay overlay.** Website A's bowling innings appeared stuck at 0.1 overs. Six
clicks on BOWL, several space presses, no movement, and the canvas was still animating.
The draft claim was "the match cannot progress past the first ball". What actually held
it was a wicket replay that had to be cleared by clicking BOWL at its hit-tested centre;
after that the innings ran normally to 4 for 0 off four balls with a full ball-by-ball
record. A modal that needs dismissing is not a dead control.

**Website B's match brief.** The START MATCH button hit-tested as covered by an element
with class `overlay show`, z-index 30, `pointer-events: auto`, at all six probe points
across the button. That reads exactly like a blocking-overlay bug. It was the intended
MATCH BRIEF panel, carrying its own TAKE THE CREASE dismiss button. Reading the
overlay's own contents before judging it is what separated the two cases.

**The state text lags the canvas.** Several probes reported a stale score because
`document.body.innerText` had not caught up with the frame, and one regex missed a
wicket because it only matched `\d+-\d+`. Sample more than once, and make the pattern
tolerant of the states being looked for.

**The rule.** When a control looks blocked, read what is covering it. When a game looks
frozen, look for a modal, clear it, and retry before writing anything down. Three
separate false negatives on one task, all caught at this step, is why the step exists.
