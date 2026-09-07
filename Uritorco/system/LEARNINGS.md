# Uritorco learnings: read before the next task

Newest first. These are things a previous task got wrong or nearly got wrong.

## The queue is gated on review, and the platform does not say so on the task page

After the fifth submit, Vercel's Next Task returned "No more tasks available for this project
right now." The batch had not run out. The dashboard card carries the reason:
**"Waiting for reviews: 0/3 approved"**, next to `5/20 submits`. Three of the submitted
tasks have to be reviewed and approved before the queue opens again, and nothing an attempter
does locally moves that.

Do not treat an empty queue as a bug and do not go hunting for tasks in the Feather campaign
lists to work around it. Read the dashboard card first.

The `/api/projects/<id>/next-task` response is worth capturing when this happens, because it
names the cause outright. Hook `window.fetch` before clicking, then read the body:

```json
{"found": false, "reason": "pool_exhausted",
 "detail": {"gateBlocked": false, "allSkippedByUser": true,
            "replicaBlocked": true, "wallBlocked": false, "totalAtStage": 3}}
```

`replicaBlocked` and `allSkippedByUser` are different reasons from `gateBlocked` and
`wallBlocked`, and only the response distinguishes them. The card text does not.

## Task #3032 (Feather a26faee6): one missing brace, seventeen blank charts

Verdict: Left 2/1/2 (total 5), Right 4/5/4 (total 13), Strongly prefer Right, High.

**A syntax error anywhere in an inline script kills every chart on the page.** The
left candidate configured 17 Chart.js charts and rendered none of them. Chart.js itself loaded
from the CDN, `window.Chart` was defined, and yet zero chart instances were registered and all
17 canvases sat at the default 300x150 with nothing painted. The cause was a single unclosed
options object in the `cashFlowChart` definition. The script never parsed and nothing in it ran.

**Extract the inline script and run `node --check` on it.** That is what pinned the exact
construct, `SyntaxError: Unexpected token ')'`, in a couple of seconds. Reading the console
message alone tells you the page is broken but not which of 17 definitions did it, and
guessing from a 25KB file is slow. Pull the script text out of the HTML, write it to a temp
file, check it.

**"Configured" and "rendered" are separate questions and completeness is scored on rendered.**
The left candidate was the more ambitious build on paper: 17 charts against the right
candidate's 6, across bar, line and doughnut, plus a richer top KPI row. None of it reaches a
board member. Rate the page on what it renders.

**Test the library and the drawing separately.** `window.Chart !== undefined` says the CDN
worked. Counting registered instances and sampling canvas pixels says whether anything drew.
Conflating those two would have produced the wrong diagnosis here, because the CDN was fine.

**A self-contained build beat a dependency-heavy one.** The right candidate hand-draws six
canvases with no external library and every one renders at both widths. Not a rule that fewer
dependencies is better, but here the candidate with no external dependency had no load failure
to hit.

**Feather's autosave can fail without saying so.** Five `ERR_NAME_NOT_RESOLVED` failures hit
`/api/graphql` mid-fill during a local DNS drop. Nothing in the UI indicated the fields had not
persisted. Confirmed DNS had recovered, hard-reloaded the task, and verified all eight fields
survived before submitting. **Always hard-reload and re-read every field after filling.** That
step already existed for correctness reasons; it also catches this.

**Self-check the draft before dispatching the humanizer.** The `so`/`which` consequence hinge
from #3028 reappeared in 5 of 6 fields. Cutting it to 1 before dispatch turned what would have
been a rewrite cycle into a single finding. Grep the draft for the shapes previous tasks were
pulled up on; it is faster than waiting for the gate to say the same thing.

## Task #3028 (Feather 1cb21cf6): judging animation, and an x-threshold that silently lies

Verdict: Left 4/3/4 (total 11), Right 3/2/2 (total 7), Prefer Left, High.

**THE MECHANICAL ONE: the `x < 760` side test is wrong and fails silently.** The Right panel
starts at x=768 on a 1536 window but x=720 on a 1440 one, so on a 1440 viewport every element
classifies as Left and both sides' text lands in the Left panel. Caught only by printing the
actual x values while verifying ratings. **Use DOM order instead: the first three rating groups
and the first three rule textareas are Left, the next three are Right.** `PLATFORM_MECHANICS.md`
is corrected.

**How to judge an animation brief.** Screenshots are nearly useless here; four techniques did
the work:
- `document.getAnimations()` gives running CSS animations with names, durations and playState.
  The left candidate returned 30 running, with 20s/30s/40s/60s durations matching the brief's
  "very slow and smooth".
- **Canvas animation is invisible to `getAnimations()`.** Sample the pixels instead:
  `ctx.getImageData(...)` at intervals and compare. That is how the right candidate's hero and
  map were confirmed to be genuinely animating.
- **Sample several points on a canvas, not one.** A single centre-pixel read said the right
  candidate's map was static; six points across it showed all six changing. The centre was
  empty ocean. Nearly a false finding.
- **For scroll-driven motion, step the scroll and record the transform.** Reading it at four
  coarse positions suggested the right candidate's product row moved; stepping every 50px
  showed it holds at 0, snaps to -620 in ONE step, and holds. That single jump is the defect,
  and only fine granularity exposes it.

**Compare travel against travel needed.** The left candidate's product row moves 109px when the
track needs 661px, so two of five named products never come into view. `scrollWidth -
clientWidth` versus the measured transform range makes that concrete.

**Section overlap is measurable.** The brief called it VERY IMPORTANT. Reading each section's
top minus the previous section's bottom gave -90 on all eight boundaries for the left candidate
(margin-top: -90px) and exactly 0 for the right candidate. A clean requirement, cleanly checked.

**Another withdrawal from trusting one signal.** The right candidate has
`scroll-behavior: auto`, which looked like a miss on the brief's first global rule. Clicking a
nav link and sampling scrollY over time showed 0 -> 95 -> 1739, so it animates the scroll in
JS. **CSS property absent does not mean behaviour absent.**

**The humanizer found a NEW repeated shape after I fixed the old one.** Varying the openers
worked (six distinct shapes), but then `so`/`which` consequence hinges appeared in 5 of 7
fields. Reduced to 3. **Each pass fixes one shape and can expose another, so ask the humanizer
to look for repeated shape generally, and name the shapes already fixed so it looks past them.**

## Task #3010 (Feather c2d15f9c): three withdrawals in one task, and a route-specific overflow

Verdict: Left 3/3/3 (total 9), Right 3/2/2 (total 7), Prefer Left, Medium.

**Overflow can be route-specific, so measure on the page the fault lives on.** The right
candidate's home screen measured clean at 390 (375 < 390). Its CHECKOUT page overflows by
206px, with the CVV input starting at x=408 on a 390 viewport, entirely off-screen, because its
row is `flex-wrap: nowrap`. **A clean measurement on the home screen says nothing about the
other routes.** Re-run the probe on the screen where the interaction actually happens.

**Three findings withdrawn on this task, all from being too quick to conclude:**
- *"The left candidate's cart is empty after adding".* My own artifact. I forced the cart
  overlay open by adding the `active` class instead of clicking the button, which skipped the
  render. Calling `renderCart()` showed the item correctly. **Do not open UI by editing
  classes; click the control the user clicks.**
- *"The right candidate's Checkout link is inert".* It has no `data-action` while every other
  control does, and the first read still showed the cart. It routes fine; it needed a moment
  to render. **Wait and re-read before calling a control dead.**
- *"The right candidate's checkout has no address or payment fields".* `innerText` does not
  include placeholder text. Querying the inputs found Name, Email, Shipping Address, Card
  number, Expiry and CVV. **A form can be complete and still look empty to innerText.**

**A bad grep nearly produced a shared false finding.** An early `grep -P` for Devanagari
returned zero for both apps and I almost wrote that neither delivered the Hindi the prompt
asked for. Counting properly in Python found 442 chars in the left candidate and 879 in the
right. **When a check returns zero for both candidates, suspect the check.**

**Two valid readings of one requirement.** "Hindi/English" was met differently: the left
candidate prints both languages side by side ("Men / पुरुष") and its search matches Hindi
input, while the right candidate has a real EN/HI toggle that swaps the whole interface and
persists the choice. Both satisfy the brief. Neither is a defect.

**`role=button[name="X"]` is the reliable selector for the preference row.**
`button:has-text("Prefer Left")` is ambiguous, since "Strongly prefer Left" and "Slightly
prefer Left" both contain it, and a synthetic `.click()` does not register on these MUI
toggles at all. Also worth knowing: a rating click can silently fail to stick, so **re-read
`aria-pressed` after setting the preference and confidence, not just after the ratings.**

## Task #2987 (Feather 8f3e87fa): the claim flow, and two sites that fail opposite ways

Verdict: Left 4/2/3 (total 9), Right 4/5/2 (total 11), Slightly prefer Right, Medium.

**THE BIG ONE, and it corrects what #2935 recorded.** The Vercel Task Variables `link` is the
**template** id, not your attempt. Opening it lands on a task whose status chip reads
**Unclaimed**, and an unclaimed task renders **no preview iframes at all**, just two empty
panels. Claiming it from the status menu redirects to a **brand new task id**, and the previews
mount there. #2935's link returned "Task not found" instead of Unclaimed, which is the same
thing with an expired template, and the "dead link" reading was wrong.

**So: empty previews are almost never a broken task. Check the status chip first.** The
platform's own advice (refresh the task page once) does not help here, because nothing is
loading yet. Read `PLATFORM_MECHANICS.md` for the corrected sequence.

**Both sites failed the Gallery, in opposite ways, and the worse-looking one is not the worse
site.** The left candidate's gallery is nine empty grey tiles with captions: quiet, tidy, and
empty. The right candidate references an `assets/` folder that was never delivered, so all 17
images 404 and the broken-image icon appears in the header and hero before any scrolling.
The right candidate looks far worse, and still won, because everything on it works.

**A CSS class the JS toggles is worth nothing if no rule listens for it.** The left candidate's
hamburger adds `.active` to `.nav-menu` on click. The stylesheet has `.nav-menu {display:none}`
in the mobile breakpoint and **no `.nav-menu.active` rule**, so computed display stays `none`
and zero links appear. Verified by clicking, then reading `classList.contains('active')` (true)
against `getComputedStyle().display` (none). **Check the computed style after the click, not
just that the class landed.**

**A form with no action leaks its contents into the URL.** The left candidate's contact form
has no `action`, no `method` and no submit handler, so the browser default GET writes every
field into the query string. Submitting put the visitor's name, email and message into the
address bar, cleared the form, and showed no confirmation. Reproduced end to end before writing.

**Two more findings died on measurement:**
- *The right candidate's logo is clipped at mobile.* Measured left 0, right 44,
  `clippedLeft: false`. The cut-off look is the broken-image ALT TEXT rendering, not clipping.
- *Its mobile dropdown overlaps the hero.* Real overlap of 112x104, but the panel is
  `position: absolute` with an opaque white background. That is what a dropdown does.

**The humanizer caught sentence-SHAPE repetition again, a different shape from last time.**
Three of six fields opened with a flat verdict sentence then unpacked it ("The mobile menu never
opens.", "Every picture the site tries to show is missing.", "The first thing on screen is
broken."). The validator cannot see this. **Ask the humanizer explicitly to check for repeated
sentence shape across fields, not just vocabulary.**

## Task #2935 (Feather 955b913c): the first task on this project

Verdict: Left 3/5/3 (total 11), Right 4/4/2 (total 10), Slightly prefer Left, Medium.
Submitted and confirmed on both platforms.

**A full-page screenshot hides horizontal overflow, and it nearly cost a real finding.**
The full-page capture of the right candidate showed a complete, tidy table. The viewport
capture at the same width showed the Personnel and Department columns and the entire Actions
column, holding Edit and Delete, sitting off the right edge. A full-page capture widens the
canvas to fit the content, so page-level overflow disappears from it. **Measure
`documentElement.scrollWidth` against `window.innerWidth` first, then take a VIEWPORT
screenshot.** This is the mirror image of the UI Berry trap where a short viewport faked a
clipping bug; both come from trusting a screenshot over a measurement.

**A wide table is not automatically a defect.** The left candidate's table is 1843px wide on a
1440 viewport and that is fine, because it lives in its own `overflow-x: auto` container and
the page does not overflow. The right candidate's table is narrower but the PAGE overflows, so
its controls become unreachable. Check whether the page overflows and whether the user can
still reach the controls. A table being wider than the screen decides nothing on its own.

**Breakpoints existing is not the same as breakpoints working.** The right candidate has two
media queries and the left candidate has none, yet the left candidate stacks correctly on
mobile and the right candidate does not. The left candidate uses
`repeat(auto-fit, minmax(180px, 1fr))`, which is intrinsically responsive. The right
candidate's breakpoints fix its container and its table but never touch `.form-row`, which
stays `display:flex` with `flex-wrap: nowrap` and overflows by 18px. **Check the computed
style of the element that overflows, not the presence of a media query.**

**`display: inline` on a status pill breaks its background across lines.** Two-word statuses
on the right candidate ("Normal Use", "Under Repair") each painted as two separate coloured
blocks; one-word statuses ("Idle", "Scrapped") looked correct. `getClientRects().length`
returns 2 for the broken ones and 1 for the good ones, which is the clean way to prove it.
An earlier read of this as "clipping" was wrong: all four pills measured INSIDE their cells.

**Prove a hidden field with a unique string.** The right candidate collects Main Technical
Specifications and never displays it. Typing `UNIQUESPEC 480V 3-phase` and then checking
`document.body.innerText.includes('UNIQUESPEC')` returns false while the stored value is
correct. That is a reproduction, not an inference, and rule 6 wants the steps.

**Read the whole prompt back before scoring completeness.** Both apps implement all
15 named fields and all 5 summary counts. The prompt also said "implement this step by step,
with detailed instructions as if for a beginner". The left candidate has zero instructional
content, verified by a regex for step|instruction|guide|beginner|help returning no matches.
That is a wholly missing named requirement and it is what set its completeness to 3.

**The Vercel task variables can hold a DEAD Feather link.** #2935's stored link
(`1eeab42d...`) returned "Task not found" while the live claimed task was `955b913c...`. Do not
conclude the task is dead and release it. The stored link is the pre-claim id; the live one is
the task that is In progress and assigned to the account. Put the LIVE url in Attempt URL.

**Preview origins expire mid-task with a 502.** The left candidate's sandbox died during
inspection. Refreshing the Feather task page re-provisioned BOTH apps on new hostnames. This is
infrastructure and must never be rated against a candidate. The new origin also has empty
localStorage, so any persistence test has to be redone there.

**Left and Right share every element id.** `root_rule_0_rationale` exists twice.
`getElementById` returns the Left one, so both texts land in the Left panel if you are not
careful. Disambiguate by DOM order (first 3 rule textareas Left, next 3 Right) or Playwright
`nth`. **Corrected on #3028:** this entry originally said to use x position with a `< 760`
threshold. That is wrong and fails silently on a 1440 window. See the #3028 entry above.

**The validator caught an arithmetic error in my own rationale.** The draft claimed the left
candidate "totals thirteen" when it totals eleven. Numbers written into a rationale are as
checkable as numbers written into an evidence field. The validator now prints both totals.

**The humanizer caught a positive-language violation my regex missed.** "The controls
themselves behave correctly" sat in a negatives-only field and passed the adjective list clean,
because it carries no adjective. `validate_rubrics.py` now matches the SHAPE
(`behaves correctly`, `works as expected`, `no issues were found`) rather than the vocabulary.
**Run both gates; they catch different classes of error.**

**A rating of 5 is a claim, not a default.** Rule 2 says award it when there is nothing
negative to report, which raises the bar on inspection rather than lowering it. The left
candidate got a functionality 5 only after add, edit, delete, the counter routing, the
persistence reload and the confirm dialog were each exercised. Right's functionality stayed at
4 because following its own instructions misleads a user about which fields are mandatory, and
that is a workflow defect even though every control works.
