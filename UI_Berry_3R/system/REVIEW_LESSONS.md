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

---

### P27 — pick an indicator that actually changes, or the control looks dead

Task 46 (WI 7574389). Website A's sidebar was probed by reading `h1`/`h2` after each
click. Nothing moved, across synthetic clicks and then real mouse clicks, so the draft
claim was "the side navigation does not work". It was wrong, and it was wrong in the
worst direction: the finding was then mirrored onto Website B and the two were compared
on a defect neither had been measured for properly.

The headings on that page are **section titles inside the scrolling document**, so they
are the same on every view. The breadcrumb is what carries the current view. Read that
instead and the picture inverts: Website A tracked `Health intelligence > Trends >
Biomarkers > Overview` across three clicks, working perfectly, while Website B stayed
pinned on `Your workspace / Overview` through five entries and landed all five on the
identical `scrollY` 226.

**The rule.** Before reporting that a control does nothing, confirm the thing being read
is something that *would* change if the control worked. Prefer an indicator the page
itself uses to say where it is: a breadcrumb, a selected-state class, an `aria-pressed`,
a URL fragment, a value that is recomputed. A heading, a page length, or a whole-body
text hash can all stay constant through a perfectly good state change.

This is the third shape of the same false negative. P21 asks whether the control was
reachable, P23 whether the window was long enough, P25 whether the input was real, and
P27 asks whether the *observation* was pointed at the right thing.

### P28 — selected state is not proof the control did anything

Same task, the other direction. Website A's 1M / 3M / 1Y range control moves its own
highlight correctly, which on a quick look reads as working. It is not. The chart's
x-axis stayed `MAR, APR, MAY, JUN` on all three settings and the SVG came back
byte-identical, 64 paths and 25 circles before and after.

Website B's equivalent genuinely recomputed: the axis came off the hourly scale and the
heart-rate-variability reading moved 59, then 61, then 54.

**The rule.** For anything that claims to change data, check the data, not the chrome. A
highlight that moves proves a click handler fired, nothing more. Two candidates can both
"respond" and only one of them can be doing the work.

### P29 — `scrollIntoView` can push the target out of a clipped viewport

Task 52 (`c8e9706f`, treasury dashboards). Four of Website A's controls read as dead on
the first pass: `Help & methodology`, `View curve`, `Explore analysis` and `View all` all
produced no change in body text, no modal, no scroll and no hash move. Four inert controls
on one page is a strong-looking functionality defect, and it was entirely wrong.

The probe did `b.scrollIntoView({block:'center'})`, read `getBoundingClientRect()`, then
clicked the centre of that rect with `Input.dispatchMouseEvent`. On a page whose document
is barely taller than the window, `scrollIntoView` moves very little, but the rect it
returns can still sit below the clipped viewport the screenshot and the input system
actually use. `document.elementFromPoint(cx, cy)` returned **`null`** — not another
element, `null`, which means the point is outside the viewport entirely. The click went
nowhere.

Clicking the same buttons by id proved every one of them works: `View all` flips its own
label to `Show less` and takes the observations table from 5 rows to 20 of 20, and the
other three each open a distinct modal (`A note on the numbers`, `The fictional yield
curve`, `The market narrative`).

**The rule.** Treat `elementFromPoint` returning `null` as *probe failure*, never as
evidence about the site. Distinguish the two null-ish outcomes before believing a negative:

- `null` → the point is off-viewport. The click was never delivered. Re-probe.
- a different element → genuinely covered. That is a real finding (and see §24).

Assert the point is inside `0 < y < innerHeight` and `0 < x < innerWidth` before clicking,
and when a control looks dead, confirm by a second route (direct `.click()` by id) before
writing it down. This is the fourth shape of the same false negative and the first where
the control was neither unreachable, nor slow, nor mis-observed — it was simply never hit.

### P30 — a shared trait is not a differentiator

Same task. Website A's sidebar anchors update `location.hash` and move the active class
but leave `scrollY` at 0, even at a short viewport with 800px of scroll available and the
targets well below the fold. Written up on its own that is a clean, well-evidenced defect.

Website B does exactly the same thing on all six of its nav items.

**The rule.** Before a defect goes in a reason field, run the identical probe against the
other candidate. A behaviour both sites share cancels out and says nothing about which is
better, and a comparative lens is the only thing being scored. Half a probe produces a
finding that is true about the page and useless about the pair.

### P31 — a static panel that looks live is worse than no panel

Task 57 (`3ce370a7`, NEC4 onboarding wizards). Both candidates built a working four-step
wizard: every step advanced, typed values survived moving forward and back, milestones
added, documents uploaded. On the surface there was nothing between them.

Website A added a sidebar carrying a **Project summary** and a **Readiness** checklist.
The summary is genuinely live: typing `CHANGED-REF` into the reference field and picking a
different value band showed both back immediately. The readiness list below it is not. All
four items carry a tick from the opening step, and only one of them ever holds the `ok`
class, unchanged through all four steps and unchanged when the field a given item tracks is
cleared.

**The rule.** When a panel claims to report state, drive the state and read the panel, then
drive it the other way and read it again. Two checks, because one reading cannot tell a
live panel from a frozen one that happens to start in the right place. Track it across
every step, not just the first, and clear a field as well as filling one.

The sharper point for the write-up: A's summary working is what makes the frozen list
beside it a real defect rather than a cosmetic one. A viewer who watches one panel update
correctly has every reason to trust the one underneath it.

### P32 — two buttons with the same label are not the same button

Same task. Website B's Key dates step has an **Add milestone** button that opens the entry
form, and a second **Add milestone** button inside that form that commits it. Clicking by
label found the opener both times, so the form toggled shut and the milestone never
appeared, which read as a broken feature across two separate attempts.

Driving the form directly, by filling `milestoneName` and `milestoneDate` and then clicking
the submit **inside the field's own container**, added the milestone and cleared the "No key
dates added yet" message. Website A behaved identically. Neither site was broken.

**The rule.** Before believing a submit did nothing, count how many controls share that
label. Scope the lookup to the container holding the fields (`input.closest('form')` or the
nearest common ancestor) rather than searching the whole document, and check the form is
still open after the click. A form that closed without saving is a mis-aimed click far more
often than it is a bug.

### P33 — re-probing mutates state, so reload before the reading that counts

Tasks 54 and 57. Repeated probe clicks left Website B in task 54 with six modals stacked
open and its card grid down to a single car, and left task 57's wizard parked on step four.
Both looked like defects in a later reading and neither was: reloading restored six cars
and a clean step one.

**The rule.** Anything that opens, filters, navigates or submits leaves the page changed.
When a probe reports a surprising count or an empty region after earlier interaction, reload
and take the measurement again before it goes anywhere near a reason field. Cheap to do,
and it separates what the site does from what the probing did to it.

## P34 — a WebGL canvas reads back blank, and that is not a blank canvas

Task 59. Both candidates were a single full-bleed canvas and nothing else. Sampling pixels
by drawing the canvas into a scratch 2D context and calling `getImageData` returned an
all-zero luminance grid for Website A on every sample, while Website B returned a sensible
grid. The obvious reading was that A rendered nothing. The screenshot said otherwise: A was
rendering a lit 3D scene.

The cause is `preserveDrawingBuffer: false`, which is the default and which A set explicitly.
Once a WebGL frame is presented, the drawing buffer is cleared, so anything that reads it
afterwards gets zeros. B read back fine because B was a plain 2D canvas, not WebGL at all.
The probe was not measuring the site, it was measuring the context type.

**The rule.** Never judge a canvas by a pixel read-back. Check `getContext('webgl2')` /
`getContext('webgl')` and `getContextAttributes().preserveDrawingBuffer` first. When the
context is WebGL and the flag is false, an all-zero read is *expected* and carries no
information, exactly like `elementFromPoint` returning `null` in P29. Use the screenshot
path instead, which goes through the compositor and captures what is actually on screen.

**The corollary that decided the task.** Motion on a canvas is proved by hashing successive
screenshots, not by reading pixels and not by counting animation frames. A frame counter only
proves the loop is alive. Website A's loop ticked the whole time and its rendered output never
changed by a single byte across a reload, four foreground captures and real cursor movement.
A live loop with a frozen image is a real defect, and it is invisible to a frame counter.

**Do not report frame rate.** Both candidates measured far below their real rate here because
of tab throttling and the capture overhead of the probe itself. Frame rate in this harness says
more about the harness than the site, and it is an instrument number besides (HOUSE_STYLE §2).

## P35 — losing a game is not evidence the game is broken

Task 60, two penalty shootout games. Fifteen shots were taken against Website A aiming at
every corner and every power level, and all fifteen were saved. Nought from fifteen looks
exactly like a rigged keeper, and "the player cannot score" was one edit away from a reason
field.

It was technique. Website A charges its power meter slowly, so a synthetic hold of half a
second reached only about a third of the bar and the shot was still inside the TOO SOFT band.
Charging all the way to full overshoots the other way. Once the hold was driven by reading the
meter back and releasing inside the sweet band, the same site conceded two goals in five.

**The rule.** Before reporting that a game mechanic cannot be beaten, prove the input reached
the value the mechanic wanted. Read the control back while driving it, do not assume a timed
hold maps to the intended strength, and sweep the input range rather than repeating one value.
A uniform bad outcome across many attempts is a signal to suspect the harness first.

**The second near miss in the same task.** A drag across Website A's aim track changed nothing,
and every element under the pointer reported `cursor: auto`, which read as a dead control. The
aim is not an input at all, it is a readout driven by pointer position over the pitch and by
the arrow keys. Moving the pointer to the far left and far right swung it from Left to Right
immediately. Confirm what drives a widget before calling the widget dead, and remember that a
readout with no cursor affordance is a design choice, not a defect.

**The third.** Website B's defend buttons measured zero wide and never grew while polling for
eighteen seconds with the mouse. They are keyboard driven, exactly as that site's own
instructions say, and arrow keys produced "Diving left" and a save. Read the instructions the
site ships before concluding its controls do not respond.

## P36 — read the whole page before deciding a submit did nothing

Task 61. Website A's Quick transfer took a recipient and a typed amount, then its Continue
button appeared to do nothing: the card's own text was unchanged and the form did not reset.
"Continue does not respond" was one edit away from a reason field again.

The confirmation existed. It was appended at the very end of the document body, far below the
card that produced it, reading "$250.00 is ready to send to Mia" with a tick. The slice being
read covered only the neighbourhood of the Quick transfer heading, so it could never have seen
it. Measuring the length of the whole body text caught it immediately: 1167 characters before
the click, 1194 after.

**The rule.** When testing whether an action did anything, compare a whole-document measure
before and after, such as `document.body.innerText.length` or the element count, and only then
go looking for where the change landed. A targeted slice answers a narrower question than the
one being asked, and a negative from it is not evidence.

**The same task, three more near misses.** Website A's chart toggles looked inert because the
probe was reading path lengths from sidebar icons rather than the chart, and the real chart
swapped its amount, its axis labels and its geometry on every toggle. Website B's sidebar
looked like it highlighted without routing, and it was in fact appending a whole new section
below the grid, which the heading list showed and a heading count did not. Website B's action
buttons read as covered by a DIV, which was the modal a previous click had opened.

Four false negatives in one task, every one of them a probe that answered the wrong question.
When a well built site suddenly appears to have a dead control, suspect the probe first.

## P37 — on a scroll-animated page, geometry read before the reveal is fiction

Task 62. Website A's booking form reported an absolute position of 624 on a 6627 pixel page,
which put it inside the hero. Clicks aimed there were swallowed by the hero visual, focus
stayed on BODY, and four text fields read back empty. The obvious conclusion was that the 3D
layer sat over the form and blocked it.

Wrong. The page reveals sections on scroll, so anything below the fold had not been laid out
yet and every rectangle below the first screen was meaningless. Walking the whole page in
steps of a few hundred pixels first, then re-measuring, put the form at 5733, where it was
reachable and where all eight fields took input and submitted to a real confirmation.

**The rule.** On any long page, scroll from top to bottom once before measuring anything, then
re-read the geometry. `scrollIntoView` is not enough on its own, because it targets a position
the page has not built yet and can stop short. A covering element that changes identity between
consecutive probes, hero then trust-item then services, is the signature of this failure, not
the signature of a real overlap.

**Corollary.** A form that cannot be found on the page may be inside a `dialog` that is still
`display: none`. Check for a closed dialog before concluding a form is missing or broken.

## P38 — the DOM value can be right while React state is empty

Task 63. `fill3q.py` reported all three fields filled and verified, "want 730 got 730" on the
overall reason, and the toggles all stuck. Feather then rejected the submit inside an HTTP 200:

    'overall_scoring_reason' is a required property

The textarea held the text. React did not. The section 21 chain ends by clicking a neutral
point to force a real blur, and the fixed point it used, (200, 300), landed on a LABEL on this
task's layout, which absorbed the click without moving focus. No blur, no commit, and the DOM
readback still looked perfect because the DOM was never the problem.

**The rule.** Verify the field through React, not through `textarea.value`:

    const k = Object.keys(t).find(x => x.startsWith('__reactProps'));
    t[k].value.length

If that disagrees with the DOM length, the field is not committed no matter what the DOM says.
Pick the blur target by hit test above the textarea rather than trusting a fixed coordinate,
which is section 24 applied to the blur point as well as the click point.

Both are now in `tools/fill3q.py`, so the check runs on every task instead of being remembered.

### P39 — a screenshot shows you where to look, never what is true

Tasks 67, 68 and 69 each produced a defect that existed only in my reading of a PNG. Every one
would have shipped as a false negative if the claim had gone in unverified.

- **Task 67.** Website A's "show all models" control looked unreachable, measured offscreen twice
  in a row. Scrolling the page to its limit first put the control at a normal viewport position,
  fully hittable. The earlier reads happened before the scroll, which is P37 wearing a new hat.
- **Task 68.** Website A's bag mark looked sliced flat along the bottom. The body path ends well
  inside the viewBox and carries proper rounded corners; the flat-looking base is a drawn tote
  silhouette. There was nothing to report.
- **Task 69.** Website A's last assistant message looked cut off behind the composer. The
  conversation is a scroll container, the full text was already in the DOM, and a real wheel event
  reached the end of the reply cleanly.

The rule: a screenshot is a pointer to a question, not an answer to one. When an image suggests
something is clipped, cut, overlapping or unreachable, go and measure that specific thing before
writing it down. Geometry, path data and scroll state decide it.

**The inverse also holds, and it is why the screenshot still matters.** Task 67's real defect was
invisible to every DOM probe run before the screenshot: Website A renders a "no reported scores"
empty-state panel directly over a chart that is drawn and populated. Nothing in the series data or
the control state hints at it. It was visible instantly in the image, and `display: flex` with
full opacity over the chart's own box confirmed it afterwards.

Screenshot to find candidates. Probe to confirm them. Neither one alone is evidence.

### P40 — on a WebGL task, read the framebuffer inside a frame, and do not let a metric outrank the image

Task 71 paired two 3D sneaker configurators. Three separate probes gave answers that pointed the
wrong way before the right evidence arrived.

- **The blank readback.** Copying the canvas with `drawImage` into a 2D context and sampling it
  returned `maxLum: 0` across 174k pixels on Website A. That is not an empty scene, it is the
  ordinary `preserveDrawingBuffer: false` readback failure. Anything sampled outside a frame is
  already cleared. The fix is `gl.readPixels` on the live context inside a double
  `requestAnimationFrame`, which immediately returned a real image.
- **The draw-call count said the opposite of the truth.** Instrumenting `drawArrays` and
  `drawElements` showed Website A pushing roughly twice Website B's triangles per frame. Read
  naively that says A has the richer model. A was in fact drawing a cloud of disconnected shards.
  Geometry volume says nothing about whether the geometry resolves into the requested object.
- **The clever metric that had to be thrown away.** A connected-component count over a brightness
  mask was built to prove "A is fragmented, B is solid". It said B had *more* blobs at three of
  four angles, because B's matte black panels fall under any brightness threshold that excludes
  the grid. The metric did not support the claim, so it was discarded rather than reported.

What actually decided it was the rendered image at four rotation angles on each side, with a real
pointer drag between them: A showed the same scatter of shards from every angle, B showed a
coherent shoe from every angle.

The rule: on a canvas task the picture is the deliverable, so the picture is the evidence. Probes
exist to confirm that the thing responds and to explain *why* it looks how it looks, not to
substitute a number for looking. And when a metric built to support a claim contradicts it, the
metric goes in the bin, not into the reason field.

Corollary to P39: a screenshot is still only a pointer, so the render was checked at four angles
rather than one, and the interaction was driven with real pointer events before anything was
written down.

### P41 — a text input that measures 0x0 is off-view, and a synthetic value set is not a typed query

Task 72's Website B has a search box above its stage list. Three probes ran against it and the first
two both said "the search does not filter", which would have been a false negative in the
functionality field.

- **Probe 1, native setter.** Setting `.value` through the `HTMLInputElement` prototype setter and
  firing `input`/`change` left all 18 stage rows visible for `deploy`, `zzzznomatch` and `seo`
  alike. The tell that the probe was wrong, not the site: at the end of the run `s.value` read back
  as the empty string. The component never took the value.
- **Probe 2, real click and insertText, wrong view.** Driving it with `mouse.click_at` plus
  `Input.insertText` still typed nothing, because the box measured `{x: 0, y: 0}`. A control at the
  origin with no size is not rendered in the current view. The click landed on the page corner.
- **Probe 3, correct view first.** Clicking the sidebar item that owns the workflow view, then
  scrolling the input into view, put it at a real viewport position. The same click and insertText
  then produced `value: "deploy"`, the list collapsed from 18 rows to the 4 phase headers, and an
  empty-state message appeared.

Only probe 3 was evidence, and it reversed the finding: the search *does* filter. The real defect it
then exposed is narrower and true, that the filter reports nothing found for `deployment`, `lead`
and `handover`, each of which names one of B's own stages. Four of five terms came back empty.

Two rules fall out, and they generalise past search boxes:

1. **Read the box's own value back before trusting what the list did.** If `value` is empty after the
   set, the probe failed and the list never had a query to respond to. This is P25 (React state is
   the field of record) applied to a control rather than a textarea.
2. **A `0x0` or origin-positioned control is not a broken control, it is one on another view.** Find
   the view that owns it before concluding anything, which is P37 and P39 wearing another hat.

The general form: before reporting that an input does nothing, prove the input received something.

### P42 — count a deliverable by exercising it, not by scraping the page for tokens

Task 73 was a logo brief with five numbered deliverables. Scraping the rendered text for hex codes
produced a clean, confident, wrong comparison, and it pointed at the wrong winner.

- **The scrape.** Counting `#RRGGBB` in `document.body.innerText` gave Website A nine codes and
  Website B three. Read naively that says A supplied palette variants and B supplied one palette.
  The functionality verdict was drafted that way.
- **What exercising it showed.** Website B has three palette tabs. Clicking each one swaps the
  whole set: Signature, then Midnight, then Monochrome, each with its own three codes, nine
  distinct codes in total. B had the variants the brief asked for. They were simply never all in
  the DOM at the same instant.
- **And the mirror image.** Website A's three tabs are labelled Light, Dark and Mono, and they
  returned the same nine codes on every tab, because A's variants are printed as static swatches
  and the tabs re-render the *marks*, not the palette. The nine-versus-three gap was an artefact of
  one page showing everything at once and the other showing one view at a time.

The verdict that survived came from a different question entirely: not "how many codes are printed"
but "what happens when the export is pressed". One press of B's raster option produced four real
PNG blobs at rising sizes plus separate vector and guide saves. Every download control on A was
pressed and produced only SVG, all three filenames marked as the mono version regardless of the
selected mode, with no raster control anywhere on the page.

The rule: a deliverable is a thing the page *does*, so count it by making the page do it. Text
scraping measures what is currently rendered, which on a tabbed layout is one slice of the answer
and on a static layout is all of it. Comparing those two numbers compares the layouts, not the work.

This is P39's "probe to confirm" applied to content rather than defects, and it is also why four
separate candidate defects on this task died: A's palette tabs, A's active-state "lag" (a CSS
transition read too early, `mismatch: false` at a 2.5s settle), A's gradients (all 1px grid
overlays at or below 7% alpha, zero SVG gradient defs) and B's off-palette colours (all Feather
host chrome). Only the export gap survived being checked.

## P43 — an SVG bounding box is in the wrong coordinate space until you resolve the transform

Task 74. Candidate B's four navy letter paths reported `getBBox()` extents reaching
x 4186-4562 and y -2034, against a `viewBox` of `0 0 800 800`. The union of every element
measured **555% of the viewBox width and 315% of its height**. Read literally that is a
catastrophic authoring error with most of the mark off-canvas.

Nothing was off-canvas. The parent `<g>` carried `transform="translate(140 410) scale(.11 -.11)"`,
which is the ordinary signature of glyph outlines exported from a font: a large em-square
coordinate system, a negative Y scale to flip the font's Y-up axis into SVG's Y-down, and a
translate to place it. Resolving each path through `getCTM()` put all eight elements inside
the viewBox, `outsideViewBox: false` on every one.

`getBBox()` returns the element's box in its **own** user space, before ancestor transforms.
Comparing that number to the `viewBox` compares two different coordinate systems, so the
comparison is meaningless on any document that uses a transform, which is most of them.

**Rule.** Never compare `getBBox()` to `viewBox`. Map the box through `getCTM()` (or
`getScreenCTM()` and back) into the root's space first, and only then ask whether anything
is clipped. A negative scale factor and a large coordinate range together mean "exported
from a font", not "broken".

The finding that survived on this task came from the other direction: the *resolved*
coordinates showed B's fourth path at height 213 against 71-93 for the three letter masses,
starting 35 units right of where they ended. That is a real detached, disproportionate stroke,
and it matched both the screenshot and an independent pixel blob count. General form:
**a defect is real when the resolved geometry, the rendered pixels and the picture all say
the same thing, and a probe artifact is what happens when only the raw numbers do.**

## P44 — the dispatcher's Attempt URL is a placeholder until the task is claimed in Feather

Task 75. The LinkedIn work item printed
`https://msft.feather-prod.azure.com/tasks/b5f8ae65-2414-578d-b603-45f195486c6d`
as its Attempt URL, and that uuid carries version nibble **5**. Task 70 taught that a v5 uuid
is usually stale, so the reflex was to hunt for a v4 replacement. That reflex produced a
wasted detour: a v4 uuid scraped out of the page HTML, `e50c5e4d-...-404c-...`, which Feather
answered with "Task not found" just as firmly.

The nibble was never the problem. Two separate things were true:

1. **A dead link can mean a paused batch, not a stale id.** Work item 7592206's link failed
   because its page said, in plain text, *"The batch containing this task is currently paused."*
   That item was also already `Submitted`. Nothing about its uuid was wrong.
2. **The v5 Attempt URL resolves fine.** Opening `b5f8ae65-...` loaded the real task, six
   textareas and all. It showed status **Unclaimed**, and both candidate tabs read
   *"Claim this task to interact with the environment"*. The candidates do not render until
   the task is claimed.

The claim control is not a button labelled Claim. It is the **status chip** in the top right
(reading `Unclaimed`), which opens a menu containing `Action: Claim task`. Claiming rewrites
the URL to the canonical task id, which is where the real v4 uuid finally appears
(`5d6e0642-eaa2-4b5d-abd4-15577639ea26`), and only then do the candidate iframes exist.

Two mechanics worth keeping:

- `elementFromPoint` on that chip returns a **DIV**, not the button, so a hit-tested real
  mouse click lands on an overlay and silently does nothing. What worked was dispatching the
  full sequence `pointerdown, mousedown, pointerup, mouseup, click` on the element itself.
  Radix menus listen on pointer events, not on `click` alone.
- The tab panel ids are Radix-generated (`radix-:rf:-content-layout_node_4`) and **change on
  re-render**, so an id captured before claiming is dead afterwards. Re-query the tabs.

**Rule.** Do not judge an Attempt URL by its version nibble. Open it. If it says *Task not
found*, read the work item page for a paused batch or an already-submitted state before
hunting for another id. If it loads but shows *Unclaimed*, claim it through the status chip
with a pointer-event sequence, then take the uuid from the **resulting** URL.

## P45 — on a game, read the scoreboard, and start the run before judging the run

Task 76, two 2D pixel shooters. Three separate false defects almost shipped, all from
sampling a live simulation at the wrong moment.

1. **"Website A starts the player dead."** The landing state showed a game over panel,
   `health 0`, and a paused run. It is simply A's entry screen. Pressing *START A NEW RUN*
   gave `health 100/100`, modal dismissed, unpaused, and health then fell to 52 over four
   seconds of real monster contact. A title screen that happens to be a game over card is
   an odd choice, not a bug.
2. **"Website B's shooting does not register."** First pass ended `coins 0, kills 0`. The
   mechanic was fine; the aim was bad. Sweeping the pointer in a circle while holding fire
   moved it to `kills 2`, and the bounty text counted down from *Slay 15 more* to *Slay 13
   more*, which is the game's own confirmation.
3. **"Website A's run stalls at level 2."** Two samples eleven rounds apart read identically
   and `hp` came back `null`. Nothing had stalled: A had levelled up, its modal was waiting
   on an upgrade choice, and the upgrade had raised max health from 100 to **110**, so a
   probe regex hunting `/100` matched nothing. The null was the probe's, not the game's.

What survived, because it was measured the same careful way: A's upgrade buttons really do
report a zero-size box, so there is nothing to aim at, and both canvases are undistorted
(identical 1.778 aspect on backing store and CSS box, `image-rendering: pixelated` on both),
which killed a fourth candidate finding about B being "stretched".

**Rules.**
- **Start the game before judging it.** An idle canvas is not a broken one.
- **Prefer the game's own counters** over pixel diffs. Kills, coins, wave and bounty text are
  the app telling you whether your input landed; `lit pixel count` barely moves and says
  nothing.
- **A probe regex encodes an assumption.** `/100` assumed max health is constant. When a
  field goes `null` mid-session, suspect the pattern before the product.
- **Aim is part of the test.** Sweep the pointer across the field before concluding a weapon
  is inert.

## P46 — to prove a control produces nothing, diff the whole view around the action

Task 77, two data tables against a seven item checklist. The decisive finding was that
Website B has no bulk actions bar: its row checkboxes tick, and nothing else in the page
responds. That is a negative claim about a required feature, so P1 demands real evidence,
and a keyword scrape cannot supply it. Absence of the word "selected" only proves the word
is missing, not the bar.

What proved it: capture the **whole visible view** before and after the action and compare.

```js
const vis=e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0;};
// before AND after one checkbox click:
{ txt: document.body.innerText.replace(/\s+/g,' '),
  nodes: [...document.querySelectorAll('*')].filter(vis).length }
```

Website B: `440 -> 440` visible nodes, and the set difference of the words was **empty**.
Nothing was added anywhere on the page, so there is no bar, no count and no toolbar hiding
off to one side. Website A: the count text moved `0 -> 2 -> 8 customers selected` against a
bar that was already present.

That same run also corrected the opposite error. Scraping for "empty/loading/error" found all
three words in **both** candidates' HTML, which suggested both shipped the states. Exercising
them told a different story: only B could be switched into them, and only a *visibility*
check separated the states (`visibleRows 0 / visibleSkeletons 21` for loading, `0/0` plus
"No customers found" for empty). A present-in-DOM check had said all three states were live
in every mode at once, because all three panels exist in the markup simultaneously.

**Rules.**
- A word in the HTML is not a feature. A visible element that changes when acted on is.
- **Filter probes by `getBoundingClientRect()`**, not by `querySelector` alone, whenever the
  page keeps several states mounted together.
- For "this control does nothing", the evidence is a before/after diff of visible node count
  and page text across the action, quoted in the finding. Anything less is a guess.
- Absence of one affordance does not condemn the build. Website B lost this one feature and
  still won the fallback views outright, and the reason fields said so.

## P47 — a zero is a value, and a default range can be the reason for it

Task 78, two sales dashboards. All four of Website A's KPI cards read
`0.0% vs previous period`, identically, while Website B showed varied deltas
(`+12.0%`, `+0.0%`, `-0.0%`). The obvious reading is that A's comparison is unwired, and
that finding was one step from being written into a reason field.

It was wrong. A's default range spans **Jan 2023 to Dec 2024**, which is the whole dataset,
so there is no earlier period to compare against and zero is the honest answer. Moving the
start month to Jan 2024 produced **13.8%, 15.3%, 1.3%, 13.9%** on the four cards. The
feature works; the default hides it. Meanwhile B's `-0.0%` is the real formatting slip of
the pair, and B was the one shipping seven unrounded floats such as `51.21036790119342%`.

The same task carried a second trap in the opposite direction. B's regional map renders as a
flattened spiky band, and the instinct was to call it a broken SVG. Measuring both showed
**both** candidates stretch SVGs: A's line chart also carries `preserveAspectRatio="none"`.
What separates them is degree and kind. A's map squashes by 1.4 under the default `meet`, so
the geography survives; B's squashes by 2.37, and the shape does not. Stretching a *chart* is
ordinary practice because only the plotted values carry meaning. Stretching a *map* destroys
the thing being drawn.

**Rules.**
- **Before calling a computed field dead, change the input it depends on.** A constant zero
  across every card is a hypothesis, not a finding.
- **A defect shared by both candidates is not a differentiator.** Measure the same property on
  both before spending it in a reason field.
- **`preserveAspectRatio="none"` is not automatically a bug.** Ask what the graphic means: a
  distorted line chart still reads correctly, a distorted map does not.
- Ratio of the CSS box aspect to the viewBox aspect is the number that separates "letterboxed"
  from "crushed". Compute it for both sides.

## P48 — when a brief names the delivery size, render at that size and look

Task 79, two "DARK LOOP" channel logos. At full width both are handsome and both honour the
palette: black dominant, blue as the main accent, red as a highlight, verified by sampling
each mark's lit pixels. Judged on the hero view alone the choice is nearly arbitrary, and
Website A's ringed composition is arguably the richer picture.

The brief settled it by naming a constraint the hero view cannot show: *"High contrast for
visibility in small size"*, for a **YouTube profile**. So the mark was rasterised at the sizes
it will actually be seen at, 48px and 88px, and measured:

| | lit pixels at 48px | at 88px |
|---|---|---|
| Website A | 0.3% | 0.6% |
| Website B | 8.1% | 7.5% |

Then the 88px render was upscaled with `imageSmoothingEnabled=false`, pinned into the page and
screenshotted, so the numbers could be checked against the picture. They agreed, but the
picture was the more honest of the two: A's eye and red iris do survive at avatar size, more
than "0.3% lit" implies, while its wordmark and ring micro-text dissolve completely. The
number alone would have overstated the defect; the image gave the finding its correct scope.

**Rules.**
- **Read the brief for a delivery context** (avatar, favicon, print, thumbnail) and reproduce
  it. A logo task is not judged at hero size just because that is what the page shows.
- Render small with `drawImage` into a small canvas, then **upscale nearest-neighbour and
  screenshot it**, so a human eye can confirm what the histogram claims. Per P40, the picture
  decides.
- Say what actually survives. "The wordmark and ring lettering smear into nothing" is true and
  checkable; "the logo disappears" would not have been.

## P49 — measure every instance of a repeated component, not the first one you see

Task 80, two builds of the same local business site from prescribed copy. Website A's header
"Get a Free Quote" sets `rgb(82,97,112)` grey on its own `rgb(45,108,223)` blue fill, a
contrast ratio of **1.31**, which is unreadable. The tempting finding is "Website A's call to
action fails contrast".

That would have been wrong, and the probe said so because it collected **all four** instances
rather than stopping at the first. A's other three quote buttons are white on the same blue at
**4.86** and pass. The defect is one broken instance out of four, and the reason field had to
say exactly that: the other three "read fine, which makes the one at the top look like
something nobody checked". A single bad instance among correct siblings is a stronger, more
credible observation than a sweeping claim, and it is the one that is actually true.

The same run corrected a copy-fidelity finding in the other direction. A literal string check
reported Website B "missing" the required bullet **Affordable pricing**, while Website A matched
all ten required strings. Reading B's actual section showed it covers affordability thoroughly,
with a pricing section and the words "Affordable", "Pricing" and "price" throughout; it simply
paraphrases that one bullet. A paraphrase of prescribed copy is a minor fidelity point, not a
missing feature, and it was weighted accordingly rather than reported as a gap.

**Rules.**
- When a component repeats (a CTA, a card, a row), **measure every visible instance** and report
  the count that fails. `querySelectorAll` plus a filter, never `querySelector`.
- A string absent from a checklist is a **prompt** to go read that section, not a finding.
  Confirm the concept is missing, not just the wording.
- Scope the claim to what failed. "The one at the top" beats "the buttons", and it survives
  review because a reviewer can check it.

## P50 — on an illustration brief, a word count measures captions, not the build

Task 81, a post-apocalyptic vehicle spec with roughly twenty named features: bull bar,
railroad spikes, roll cage, jerry cans, barbed wire, nailed bat, searchlight, CB antenna,
kill tally, spiked hubcaps, chainlink, welded door, spare tire and the rest.

A keyword sweep of each page's visible text scored **Website A 5 of 20** and Website B 7 of 20,
which points at B. The screenshot said the opposite: A's drawing visibly contains the spiked
ram bar, the roof rack with fuel cans, the wire coil, the nailed bat, the flag antenna, the
caged windows, the tally strokes and the studded wheels. None of those were words on the page.
They were **drawn**, and the scrape had no way to see them.

Two failures in one number. The features were in the artwork rather than the copy, and A's
per-assembly notes only load once a view is selected, so the initial scrape read one fifth of
the available text. Clicking through A's five views produced exactly the "missing" vocabulary:
roll cage, fuel cans, barbed wire, a nailed bat, the plated-shut driver door, the chained trunk
and the exposed spare.

The finding that did survive came from the P46 diff, applied to both sides so the comparison
was fair. Website B's three view labels change only their own highlight: 319 visible nodes
before and after, no words added or removed, and the vehicle pixel-identical. Website A's views
swap real content, 359 to 361 nodes with a whole vocabulary exchanged, a new part number and
different weight and condition figures. Website A's *lighting* pair is equally inert, measured
the same way, and the reason field conceded it.

**Rules.**
- **Never score an illustration brief by scraping text.** Look at the image, then click through
  whatever reveals more of it.
- A checklist sweep on a tabbed page reads only the open tab. Open them all before counting.
- When a scrape and a screenshot disagree on a drawing, the screenshot wins (P40), and the
  scrape gets deleted rather than reported.
- Run the same diff on both candidates. The concession about Website A's dead lighting pair is
  what made the claim about Website B's dead tabs credible.

## P51 — to verify an end state, drive the app to it

Task 82, two 3x3 sliding puzzles. The brief demanded a shuffle that **guarantees solvability**
and a victory screen when the tiles reach 1 to 8. Neither claim can be settled by looking at
the page, and both are exactly the kind of thing a candidate can fake with static markup.

Both were checked by playing:

**Solvability, five shuffles each.** Read the board, compute the inversion parity (for a 3x3
with the blank, an even inversion count is solvable), repeat. Both candidates returned five
distinct, genuinely scrambled, provably solvable boards. Neither was faked, and the finding
that looked promising early — Website B loads at `1,2,3,4,6,7,5,8`, two tiles from solved —
turned out to be its *initial* state only. Its shuffle works. That downgraded a suspected
defect to a first-impression note, which is what the reason field said.

**The victory screen, by winning.** A breadth-first search over the 9! state space finds the
move sequence from the live board to `1..8,0`, and each move is a real `mouse.click_at` on the
tile adjacent to the blank, re-reading the grid between moves. Website A solved in 22 moves,
Website B in 8. Both then raised a genuine end card with the final move count and clock.
A ten-line BFS is cheaper than arguing about whether a screen exists.

One detector caveat worth keeping: the overlay probe reported `overlayCount: 0` for Website B
because its card is not `position: fixed` or `absolute`. The card was plainly there in the text
and the screenshot. **A structural selector that finds nothing has not proven absence** (P46
wants a diff, P39 wants the picture); here the text dump and the screenshot both contradicted
the selector, so the selector lost.

**Rules.**
- When a brief names an end state, **compute a path to it and execute the path.** Do not infer.
- For any puzzle or generator, verify the *invariant* the brief names (solvability, uniqueness,
  ordering) across several runs, not once.
- Re-read the live state between scripted moves. A queued click list goes stale the moment an
  animation reorders the board.

## P52 — a probe written for dark pages inverts on light ones, and a tie is sometimes the answer

Task 83, two blueprint-style lantern logos on white grounds.

**The inverted probe.** `small.js`, written for the neon-dark logo in task 79, fills a canvas
black and counts pixels *brighter* than a threshold. Run against a charcoal-on-white drawing it
returned `litPct 0, maxLum 0` at 48px, 88px **and 400px** for Website A. Read literally that
says the logo does not exist. The screenshot showed a fully drawn lantern. The probe was
measuring the wrong polarity, and a `maxLum` of exactly 0 at a size where the mark is plainly
visible is the tell: a real blank would still pick up the page ground.

Rewritten to fill **white** and count pixels *darker* than the threshold, both candidates came
back healthy, near 18 and 19 percent ink at avatar size. The correct move was to fix the probe,
not to report "Website A renders nothing", which would have been a serious false claim on a
page that was fine.

**The tie.** Both pages were static SVG marks. The interactivity sweep returned the identical
result on each, one clickable element that belongs to the Feather frame rather than the site,
and `scripts: 0`. Both drew completely, both held up when shrunk, neither offered any export.
There was no functional difference to find, so the functionality verdict was **BOTH_GOOD**
rather than a coin toss dressed as a preference.

`validate_reasons.py` enforces a distinct opener for that verdict:
`^website a and website b are (tied|both)`. The A/B opener is rejected, and the field must still
name and describe both sites.

**Rules.**
- **A probe carries the assumptions of the page it was written for.** Check polarity, background
  and threshold before trusting a reused one, especially when a result is exactly zero.
- An impossible reading at a large size means the instrument is wrong, not the subject.
- When two candidates measure identically on a lens, **say so**. `BOTH_GOOD` exists, and
  inventing a separation that the evidence does not support is worse than a tie.

## P53 — check the content against what the page claims about it

Task 84, two landing pages for an AI image generator. Both ticked every box on the section
checklist: exact hero headline, the three named features, the three named tiers, the footer
links, a masonry gallery with working category chips. A checklist pass separated nothing.

What separated them was **what was inside the gallery**. Website A showed six photographic
scenes, a city at dusk, misty mountains, ocean water, a star field. Website B showed flat
vector drawings, a grinning face and a spaceman, directly beneath its own sentence *"Every
image below was generated in under a second"* on a page selling **ultra-realistic** images.
The section contradicted the sentence above it. No probe surfaces that; it needs a screenshot
of the section and a reading of the brief's adjectives, not just its nouns.

Two probe corrections on the way there, both worth keeping:

- **`<img>` count is not an imagery count.** Website B returned `imgTags: 0` because its tiles
  are SVG. That is a legitimate technique, not an absence, and the first read nearly became a
  false finding.
- **A node diff can miss a real filter.** Clicking Website B's category chips changed neither
  the visible node count nor the page text, which by P46 looks inert. Measuring the *visible
  tiles* showed 8 to 4 to 4 to 8 with different dimensions each time: the filter works and the
  hidden tiles simply keep their nodes. P46's diff proves a control does nothing only when the
  thing it would change is in the diff.

The second real finding came from emulation: at phone width Website A reflowed to the given
width with a menu toggle and nothing outside the viewport, while Website B refused to render
below a much wider measure and left more than a dozen elements overflowing, against a brief
that asked for mobile explicitly.

**Rules.**
- Read the brief's **adjectives**, not only its section list. "Ultra-realistic", "high-quality"
  and "hyper-realistic" are requirements, and a checklist cannot see them.
- When a page asserts something about its own content, check the content against the assertion.
  A section that contradicts its own caption is a real, quotable defect.
- Choose the metric that would actually move if the feature worked. Count visible tiles for a
  gallery filter, not DOM nodes.

## P54 — separate the broken thing from the working thing around it

Task 85, a 3D cutaway of a specific Indian house. Website A's model collapsed into a tall smear
of stretched slivers narrowing to a point, room labels floating over the wreckage. Website B
produced a proper furnished dollhouse. The verdict is easy; reporting it honestly is not,
because **almost everything else on Website A was good**: a calm sidebar listing all eight
spaces with the exact dimensions from the brief, label/furniture/daylight switches, an export
control. Its *data* matched the plan perfectly. Only the mesh failed.

Three checks made the claim safe to make:

1. **Reload and re-shoot.** Pixel-identical after a full reload plus a 22 second settle, so not
   a capture-timing artifact (P39, P45).
2. **Move the camera.** A drag-orbit changed the framebuffer, ink samples going from roughly
   twelve thousand to forty thousand, and the picture stayed a smeared wedge. The viewer is
   alive and redrawing; the geometry is what is wrong. Without this, "broken render" could
   have meant "captured before first paint".
3. **Read the framebuffer, not the DOM.** An SVG geometry sweep found nothing extreme on either
   side, because A draws into a 2245x1047 **WebGL canvas** and B composes its house from CSS
   `matrix3d` transforms. The column-occupancy read (ink across 71% of rows but only 38% of
   columns) is the numeric form of the vertical spike in the screenshot.

Both viewers were confirmed interactive before the functionality field was written, so the
finding is "the shape being built is wrong", not "the controls do nothing".

**Rules.**
- **Name what works before naming what fails.** A page whose data is right and whose mesh is
  wrong deserves that sentence, and the reason field is more credible for it.
- For a 3D failure, **move the camera before calling it broken**. A static bad frame has three
  possible causes and only one of them is the model.
- Match the probe to the rendering technology. WebGL needs `readPixels`; CSS 3D needs the
  computed `transform` matrix; neither shows up in an SVG bbox sweep.

## P55 — measure a colour brief by hue coverage, and check the fields against each other

Task 86, two vector line-art flowers against a brief asking for "intense rainbow spectrum
colors" and "vivid complementary colors". Both drawings were competent, both sat on pure white
at a `1600x900` viewBox (exactly the 16:9 requested), and both were genuinely free of gradients
and shading. Eyeballing them, Website B looked like the better flower: closed petals, a stem,
leaves, a complete plant.

The brief was decided by converting every stroke colour to **hue** and bucketing the wheel into
twelve 30-degree families:

- Website A: **9 of 12** families, running red, orange, yellow, lime, green, cyan, blue, violet.
- Website B: **5 of 12**, with 31 strokes in the red bucket, 20 in orange, 26 in green, 9 in
  blue, and whole arcs of the wheel at zero.

"Rainbow" is not a vibe when the brief says it; it is coverage, and coverage is countable.
Counting distinct colours would have missed this, because B has twelve distinct colours that
are mostly shades of two hues.

Two corrections on the way, both from the existing protocol:

- A suspected **gradient** on Website B's petals (orange shading into red) was a probe-free
  assumption from the screenshot. The gradient sweep returned zero `linearGradient`,
  `radialGradient`, filter and pattern defs on both, and neither uses a canvas. The effect is
  overlapping strokes of different colours. Finding deleted.
- Website A's rendered box aspect of 1.96 against a 1.78 viewBox looked like stretching until
  `preserveAspectRatio="xMidYMid meet"` showed it letterboxes (P47).

The last catch came from the humanizer, not a probe: the overall field said Website B used
"three colours" while the aesthetics field named four. **Fields that contradict each other are
a defect in the submission**, and nothing mechanical checks it.

**Rules.**
- For a colour brief, measure **hue coverage**, not colour count. Convert to HSL, bucket the
  wheel, report families used.
- Read the three reason fields against each other before shipping. Every number and claim in
  one must survive the others.

## P56 — a claim that silently yields no row is a daily cap, not a broken claim

End of the run after task 86. `claim.js` reported `ANNOTATION onClick invoked` exactly as it
does on a good claim, and the dashboard stayed healthy: trigger button present, 41 tasks listed,
the previous task showing `Submitted`. Only the new row never appeared. Two attempts, same
silent result.

The claim button is not the place to look. Hooking `window.fetch` around the click showed the
dispatcher answering plainly:

```
POST /ai-trainer/api/frontendAnnotationTaskResults?action=claim  ->  429
{"message":"Daily task limit reached. You can claim more tasks after midnight Pacific Time","status":429}
```

A 429 is the platform working correctly, not a wedge, a challenge or a stale uuid, and the
right response is to **stop claiming**. Retrying a rate limit is how a working account starts
looking like a scripted one.

Before stopping, audit the board: every row must read `Submitted`, with nothing left
`Not started` or `In progress`. Ten of ten were closed here, so no task was stranded mid-flight
by the cap.

**Rules.**
- When a claim returns no row but the page looks fine, **hook `fetch` and read the response
  body** before touching anything else. The dispatcher usually says exactly what is wrong.
- Treat `429` as a stop signal for the day, not an error to work around.
- Audit for stranded rows before ending a run. A task left `In progress` past the cap is one
  that cannot be finished until the limit resets.

## P57 — compute Pacific time in Python, not with `TZ=` in this shell

Claiming returned 429 "after midnight Pacific Time". To decide whether the cap had
reset I ran `TZ=America/Los_Angeles date`, read `14:21`, and concluded the window
had reopened. It had not. Git Bash on Windows ignored the `TZ` prefix and printed
UTC — the output said `GMT` right there in the string and I read past it.

Real Pacific time was 07:23, not 14:21. The cap had been hit that same morning PT
and the reset was still most of a day away.

**The rule.** Never derive a timezone from `TZ=... date` in this environment. Use
Python, which has real zone data:

```bash
python -c "import datetime,zoneinfo; print(datetime.datetime.now(zoneinfo.ZoneInfo('America/Los_Angeles')))"
```

And when a command prints a zone abbreviation, read it and check it is the zone you
asked for. A wrong clock does not fail loudly; it just makes the next decision wrong.

**Generalises to:** any gate expressed in someone else's timezone. Convert once,
print the zone name next to the number, and confirm the two agree before acting.
