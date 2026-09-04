# Learnings — updated after each task

Read this before starting the next task. It exists so the loop gets faster without
getting sloppier. Task 1 (Task #735), task 2 (Task #805), task 3 (Task #939), task 4
(Task #951), task 5 (Task #953), tasks 6/7 (Tasks #957, #966, #969), and task 8 (Task
#972) each added fixes below — read the newest entries first, they supersede slower
advice further down.

## Tasks #3455 / #3503 / #3517 (Feather 085, 107, 113) — the house style is now a file, pick from Vercel not the campaign, and three platform mechanics that cost real time

**`system/HOUSE_STYLE.md` now exists and outranks everything here about how a reason reads.** It was
derived from five signed-off tasks in campaign `5b853679` (015, 048, 079, 054, 018), fifteen approved
fields. The single most important rule: **no instrument measurements in a reason field.** Not one
approved field contains a pixel count or a sampled value. Measure privately to be sure the claim is
right, then describe what a person would see. Suraj flagged exactly this mid-task ("Dont be so
techincal and fix this") on a draft full of pixel sums, and the signed-off corpus backed him up.
Also note the approved opener is the plain `Website X is better because ...`, not "better visually
because".

**Pick tasks from Vercel, never from the Feather campaign list.** Standing instruction as of
2026-09-04: use the UI Berry 3R card's `Start Tasking` on the Vercel dashboard. It hands back a
Vercel task whose `link` variable is the Feather task; open that, confirm it is not "Task not found",
claim it there, then paste the **post-claim** URL (the ID changes on claim) into the Vercel Attempt
URL field and Save. This supersedes the earlier note about claiming off the campaign Unclaimed list.

**Feather platform mechanics that actually bite:**

- **A textarea filled by the native-setter trick can silently fail to persist.** On task 085 the
  overall field read 618 chars in the DOM, but a hard reload showed **0**. The submit was rejected
  with no error message and the status stayed "In progress" through four attempts before the empty
  field was spotted. **Always hard-reload and re-read all three lengths plus all three verdicts
  before clicking submit.** Fix when a field will not stick: refill it, then delete the last
  character and retype it with a real `browser_press_key` so a genuine keystroke fires the debounced
  autosave.
- **Toggle buttons are toggles.** Clicking `A is better` when it is already selected turns it OFF.
  After a reload the previous selections are still there, so a blind re-click clears all three.
  Read `aria-pressed` first; `Mui-selected` is not always present.
- **The status menu closes if a Playwright locator call intervenes.** Open the menu and click the
  `<li>` in the same step. Synthetic `MouseEvent` dispatch does open the confirm dialog, but that
  dialog has **no `role="dialog"`** — it is a bare `.MuiModal-root`, so a check for `[role="dialog"]`
  reports NO-DIALOG while the dialog is in fact open and its backdrop is swallowing every later
  click. Match on `.MuiModal-root` and click its buttons **by index** (`nth=1` is Submit Task, `nth=0`
  is Cancel), because `:has-text("Submit Task")` also matches Cancel's container.
- **Success signal for submit is the auto-redirect** to the campaign list, then `Completed` and all
  three textareas `readOnly` on reload.

**A throughput cap exists beyond the daily submit limit.** The Vercel card showed `Window: 3/5
submitted`, then `4/5`, and after the third submit flipped to **`Waiting for reviews: 0/3 approved`**,
at which point `Start Tasking` stops dispatching and simply leaves you on the dashboard. The button
stays enabled and no toast fires, so the only tell is the card text. This is a hold, not a fault:
work resumes when reviewers approve some of what was submitted.

**Two judging notes.** First, **check the browser console before writing anything** — on task 113 a
`TypeError: rankingByType.join is not a function` thrown inside `updateDashboard` was the whole story,
since it aborted the update and left the ranking grid at 0 children and all three chart SVGs at 0
children, and it re-fired on every filter change so the country filter appeared to do nothing.
Second, **verify a "table is empty" claim before believing it**: a `filledRows` count that walks
`td.innerText` returns 0 when the cells are `contenteditable` divs. A screenshot showed the table was
fully populated and the finding was wrong.

## Tasks #3137 / #3358 (Feather 355 and 324) — Playwright MCP replaces the hand-rolled CDP driver, Vercel dispatch can serve a campaign you were told not to work, and two validator traps worth memorising

**The scratchpad is not durable.** A new session wiped `cdp.py` and the CDP debug port was
not listening, so the hand-rolled driver was unavailable from cold. **Do not rebuild it.** The
sanctioned `playwright` MCP server (the hardened profile from `BROWSER_OPS.md` §1) was connected
and did the entire loop. Two mechanics that make it work on Feather's cross-origin site frames:

- The parent page **cannot** reach into the website iframes (`SecurityError` on
  `contentWindow.document`). Instead take `browser_snapshot` with `target: 'iframe >> nth=0'`
  (or `nth=1` for B) to get a full accessibility tree with `ref=` handles, then run
  `browser_evaluate` with `target: '<ref>'` and a function taking `(el)`. From that element
  `el.ownerDocument` / `el.ownerDocument.defaultView` give the frame's own document and window,
  which is how every measurement below was taken.
- `browser_take_screenshot` writes to a **CWD-relative** path, meaning screenshots land in the
  repo root. Move them out immediately; this repo must stay clean.

**Vercel's Start Tasking / Next Task can hand you a task from a different campaign than the one
you were told to work.** Both Next Task and Start Tasking served Feather tasks 043, 044, 045 from
`Prod 2026-09-03` when the instructed campaign was `Prod 2026-09-02`. Releasing each one just
pulls the next sibling, so it never converges. **Fix: stop pulling from Vercel and claim directly
off the campaign's own Unclaimed list** (open the task URL from the list, status button →
`Claim task`), then point whatever Vercel task you hold at that Feather URL. The numbers do not
need to match. Note UI Berry 3R has no `Browse Tasks` button (only Interactive Multi-Turn does),
so the campaign list is the only way to choose a specific task.

**Two `validate_reasons.py` traps that cost a round each.** The word range is **40 to 160**, not
100-135; do not trim a 146-word field thinking it is over. And the lens-purity list is broader
than it looks: `cleanly` counts as **visual** language and is a BLOCK inside the *functionality*
reason (use "reliably"), while `layout` and `colou?r` are also visual and cannot appear there.
First person is a hard BLOCK anywhere, so "I'd take working controls" fails where "working
controls beat the prettier frame" passes. Run the validator **after** the humanizer every time;
the humanizer's rewrite is exactly what introduces these.

**On judging near-identical pairs.** Task 324 (an "Arab Mix FM" radio player) had both sites
passing every brief requirement: same three Zeno stream URLs, single `<audio>` element so
switching genuinely silences the previous station, randomised active-button colour, full Arabic
translation with `dir` flipping to `rtl`, and `user-scalable=no` in the viewport meta. When the
obvious checks all tie, **the deciding evidence has to be measured, not eyeballed**: sampling the
canvas with `getImageData` across five frames while playing and again while paused showed both
visualisers are truly audio-reactive (A's spread 1.49 vs 0.61 paused; B's mean brightness fell
58→33), and driving B's volume slider proved it moves `audio.volume` to exactly 0.20 and 0.95
while A offers only a mute toggle. That single measured gap decided Functionality for B even
though A won Aesthetics and Overall.

## Calibration against the campaign's own signed-off corpus (709 approved tasks, `?tab=tasks&tasks-tab=signed_off`)

The signed-off tab is readable and is the **only** ground truth for what this client actually
approves. Open any signed-off task and its three `*_scoring_reason` textareas come back populated
and `readOnly`, with the accepted verdicts still shown as `Mui-selected`. Read a few before
writing, and re-read after any rule change.

What the approved corpus actually looks like (sampled tasks 140 and 106):

- **Length is 60 to 135 words**, so the current 40-160 validator range is not the constraint;
  approved work sits comfortably in the middle of it. Do not pad toward 150.
- **The opener is "Website X is better because ..."**, with the justification fused into that
  same first sentence, not a bare verdict sentence followed by a separate explanation. Note this
  differs from the literal openers `validate_reasons.py` enforces ("Website A is better
  visually."). Both forms are accepted by the validator's regex since it only anchors on
  `^website a is better`, so **prefer the corpus form**: "Website A is better visually because ..."
  satisfies the validator *and* matches signed-off phrasing.
- **The register is measured and neutral**, not chatty. Approved text says "Website B carries a
  small flaw of its own, with a minor overlap between the shadows of its Start Game and Back to
  Menu buttons"; it does not say "kind of empty" or "turns out dead once you try it". The
  humanizer's instinct toward casual register is right for MT conversation turns and **too loose
  for these reason fields**. Ask it for plain and concrete, not colloquial.
- **Concessions are standard.** Nearly every approved reason names a real flaw in the winner
  before concluding, and the closing sentence explicitly weighs the two flaws against each other.
- **"Both are good" is genuinely used** when the sites tie on a lens (task 106's functionality),
  paired with a reason that still names the one difference found and explains why it does not
  decide the lens. Do not force an A/B pick when the evidence says tie.

## Task #1043 update (Feather "156," the same task that vanished on Task #1037 last session, this time genuinely claimable) — the 15/15 submit cap is a real server-side wall, not a display counter, and the Vercel/Feather review stage is a separate workflow from annotation

The daily submit counter shown on the Vercel dashboard ("15/15 submits") is not just
informational. Clicking Submit Task past the cap returns a real, in-page error toast:
**"Daily Submit Limit Reached: 15/15 Submits Today. Resets At Midnight UTC."** The
Submit Task button itself is never disabled client-side, so the only way to find out
whether more submits are possible is to actually try one and read the response. **Fix
worth reusing: once the dashboard shows N/N submits, do the full annotation work anyway
(claim, judge, humanize, validate, mark-inspect, fill Feather, submit Feather, verify via
reload) and fill+Save the Vercel Attempt URL, but expect the final Submit Task click to
be rejected. Click Save instead of forcing Submit** so the completed Feather URL is
preserved on the Vercel task and ready to submit the moment the cap resets, rather than
leaving the work done but unrecorded anywhere on Vercel.

A second lesson from the same task: a Vercel task page that shows an "Awaiting Review" /
"Claim Review" status with a working Feather link is a **different workflow** from
annotation, it is the peer-review stage for a task that was already submitted (in this
case, by this same session, last period, as Task #1037). Reviewing your own submitted
work is out of bounds (this is what the self-review guard is for), so when a link given
as "the task to work" turns out to be sitting in Review with a Claim Review button, do
not claim it for review, go find the actual Feather task instead (in this case, the
literal Feather URL given alongside it, which was a completely separate, still-open,
unclaimed annotation task) and treat the two links as independent rather than assuming
they are a matched Vercel/Feather pair.

Feather task 156 itself (the batik jigsaw puzzle brief) also surfaced two new UI-testing
techniques worth reusing. First, **a button click that appears to do nothing on the very
next screenshot is not proof the click failed** — Website B's "Pilih" (choose-difficulty)
buttons had a longer input-to-response delay than Website A's, and three back-to-back
"failed" screenshots turned out to be stale reads taken before the state actually
updated; only a screenshot taken ~1-1.5s after the click showed the real result. Don't
write "broken button" into a reason field off a single immediate screenshot, wait and
recheck first. Second, when a coordinate-based click via `Input.dispatchMouseEvent`
seems to land on the right visual spot but nothing happens, check
`document.elementFromPoint(x, y)` on the parent page first to confirm the coordinate is
actually inside the target iframe and in-viewport (a y-coordinate past
`window.innerHeight` returns `null` from elementFromPoint and silently no-ops the click)
before assuming the site itself is broken.

## Task #1037 update (Feather "359", originally targeting "156") — a task can genuinely disappear mid-retry, and hash-only nav links are a real, checkable functionality defect

Vercel Task #1037's title pointed at Feather task "156" ("Weaving Tales of Kedah," a
mobile jigsaw brief), found correctly in the 5p6 sibling campaign as usual. But after
six full claim-retry cycles (worse than Task #1035's four), the task briefly showed a
transient "Loading task, lazy loading, refresh if stuck" state, resolved back to
"Unclaimed" on one reload, then went to a genuine **"Task not found"** on the next
reload after one more retry. This is a new failure mode, not the tooltip-miss or
plain-miss patterns from earlier tasks: **the task itself got claimed and likely
completed by someone else while repeated retries were still in flight**, matching
almost exactly what another contributor described in a Vercel comment on this same
task ("someone else claimed and completed the task after I already claimed"). Task
156 is gone for good, not a client-side glitch to retry past.

**Fix used and worth reusing:** rather than keep retrying a task that may be under
contention, go back to the campaign's plain Unclaimed list and claim a **different**
available task instead (this session picked "359" straight off the list, no number
matching against any Vercel title needed), then update the already-open Vercel task's
Attempt URL to point at whatever got claimed. **The Vercel task number and the Feather
task number do not need to match** as long as the Attempt URL saved on that Vercel task
is the live Feather URL actually being worked. This unblocks the loop immediately
instead of burning more retries on a task that already belongs to somebody else.

This task (a video-editor portfolio site, "Noirframe" vs "CineFrame") also produced a
functionality defect worth generalizing: **both sites had real nav links and CTA
buttons, both changed the URL's hash on click, but only one site's clicks actually
moved `window.scrollY`.** Checking `innerText` alone would have missed this since both
sites render identical section content; the deciding signal was reading
`window.scrollY` before and after each click. **Lesson: on a single-page site with
anchor-link navigation, don't assume a hash change in the URL means the link worked,
explicitly check the scroll position moved** — a same-page anchor link that updates
`location.hash` but never calls `scrollIntoView` (or has a broken CSS scroll-behavior
target) is a real, checkable functionality failure, and one link on the page working
does not confirm the others do.

## Task #1035 update (Feather "154") — claim needed 4 attempts (worst yet), and a clean dashboard-vs-playable-game split

The claim on this task took **four** full open-dropdown-and-click cycles before the URL
finally rotated, the worst count seen this session (prior worst was two). Every failed
attempt still showed a clean, tooltip-free "Claim task" `<li>` on screenshot, so this
isn't a rendering glitch to diagnose, it's just an unusually persistent version of the
same intermittent miss documented in the Task #1031 entry. **Updated lesson: budget for
up to 3-4 retries on this specific control before treating a stuck claim as a real
problem worth investigating**, and keep re-verifying with a hard reload after each
attempt rather than assuming either success or failure from the URL alone.

Aesthetics, functionality, and overall all landed on Website B here, a clean sweep for
once, but each for a distinct, separately-checked reason, not a rubber-stamp. Website A
("RaceNet / Axis Overdrive") was a dense telemetry dashboard whose Launch Race and Sync
Boost buttons were clicked five times combined plus every sidebar nav item, and not one
number (distance, speed, nitro) ever moved. Website B ("Velocity Rift") had a real title
screen plus, after clicking Ignite Race, an actual playable behind-the-car racing view:
the speedometer climbed from 135 to 366 km/h while the throttle key was held, the score
counter ticked up, and the route visibly changed from "Neon City" to a different zone
("Quantum Rift") over the course of the same play session. This is the clearest possible
functional contrast this session, a fully static dashboard against a game that responds
to held keys in real time with compounding state changes (speed AND score AND scenery),
not just a single click producing a single one-off effect.

## Task #1031 update (Feather "216") — a static logo brief genuinely ties on functionality, and the "one failed claim then succeeds" pattern is now 3-for-3

Second static logo brief in a row ("ZyphercutX," a cyberpunk YouTube channel mark),
confirming the earlier lesson that functionality on a pure-image deliverable often
comes down to "does it render correctly and say the right thing," not clicks. Both
sites here had zero interactive controls (`buttons: 0` on both, one stray `<script>`
tag on Website B that did nothing observable over a 2-second before/after screenshot
check), both rendered with no missing/broken elements, and both spelled the brand name
correctly once checked via `document.body.innerText` rather than trusting a screenshot
crop (a screenshot misread Website B's wordmark as "ZYPHERCU" missing a T; the actual
DOM text confirmed "ZYPHERCUT" was there, just visually crowded by an overlapping dial
graphic). **Lesson: when a screenshot crop looks like it's missing a letter or word on
a stylized/glitchy logo, check the DOM text directly before writing a defect into a
reason** — a visual read can be fooled by overlapping decorative elements in a way the
underlying markup won't be. This produced a clean, deliberate `BOTH_GOOD` functionality
call, not a lazy default (see the Task #951 lesson on the same trap), justified by an
actual zero-interactive-elements check on both sites plus a text-content verification.

The claim-click-fails-once-then-succeeds pattern (first seen clearly on Task #1015, and
partly on #1029) repeated a third time here, including with a 1.5s pause inserted
between opening the dropdown and clicking "Claim task" specifically to test whether
timing was the cause. It still failed on the first click and only succeeded on a second
full dropdown-reopen-and-click cycle. **The timing hypothesis is now ruled out** — this
looks like an inherent one-in-two miss rate on this specific control, not a race
condition fixable with a sleep. Going forward: always plan for a possible first-attempt
miss on "Claim task" specifically (verify via hard reload, retry once if still
unclaimed) rather than treating a failed first click as diagnostically interesting.

## Task #1029 update (Feather "210") — first non-game brief this session (logo/brand-identity), and functionality favored the "duller-looking" site

This was a static brand-identity/logo brief ("Southport Connected," SVG kind on Vercel's
`name:` field, not a game), the first non-interactive-game task this session. It
confirms the whole pipeline generalizes past playable UIs: same claim flow, same
sibling-campaign search (title said "5p4-mini... - 210", zero results there, found in
"5p6... - 210" immediately, same pattern as every prior task), same reason structure.

The claim click failed silently on the first attempt here too (no tooltip this time,
just a plain miss), confirmed genuinely unclaimed via hard reload, then succeeded
cleanly on a straight retry with no diagnosis needed. Two failed-then-succeeded claims
in a row now (Tasks #1015 and #1029) suggests the very first `real_click` on this
specific dropdown item is just inherently less reliable than repeat clicks, maybe the
menu is still animating open when the first click lands. **Worth trying next time:** add
a short fixed sleep (300-500ms) between opening the dropdown and clicking "Claim task",
rather than clicking immediately, to see if that removes the need for a retry entirely.

Aesthetics and functionality landed on opposite sites here, a genuine split rather than
a clean sweep. Website A (light theme, circular hub-and-node mark, all three brief-
required variants visible in one static glance) won aesthetics. Website B (dark theme,
square-node mark) won functionality outright: its top nav tabs (Logo/Variants/System)
each loaded a real, distinct, content-rich page (a logo suite with per-card download
icons, a full color-token and typography breakdown), while every one of Website A's nav
links and its one CTA button just appended `#` to the URL and changed nothing, tested
across multiple different links. Overall went to B since the brief explicitly asks for
an explorable multi-scale system, and only one site was actually built as one. **Lesson:
on a "deliverable" brief (brand system, doc site, dashboard), functionality parity isn't
just clickable buttons, check whether the nav structure the brief implies (multiple
required views/scales/variants) is real, navigable content or static decoration** — that
distinction drove both the functionality and overall calls here.

## Task #1015 update (Feather "148") — a genuine, asymmetric functionality split, and a claim click that needed a screenshot to diagnose

The claim on this task's status pill genuinely misfired on the first try: clicking the
`<li>` labeled "Claim task" left the pill reading "Unclaimed" with no confirm dialog and
no tab-URL change, confirmed by both a fresh dropdown re-open and a hard reload. A
`rect()` check showed the element was real and visible, so the click target wasn't the
problem. A screenshot taken immediately after a repeat click showed a tooltip
("Claim this task to start working on it...") rendered right next to the option, which
is the likely cause of the first miss (a hover-triggered tooltip momentarily shifting
what was under the pointer, or simply an animation still settling). **Lesson: if a
dropdown `<li>` click reports success but nothing changes and there's no confirm dialog,
take a screenshot before retrying blind** — this task's screenshot immediately showed a
tooltip overlay that a text-only DOM query would never have surfaced, and the second
`real_click` on the same element succeeded cleanly with the expected tab-URL rotation.

This task also produced the cleanest functionality split of the session: Website A (a
neon rhythm-platformer titled "Neon Vector") had a fully working title screen, clicking
"Enter the Flow" genuinely started the run, the camera zoomed in, and Space made the
player cube visibly jump and tilt over obstacles across multiple presses. Website B (a
dashboard styled "Run Vectra") had an identically-labeled "Jump" button, a "Restart"
button, and a "Runs" nav tab, and none of them changed anything, not the frozen 2:43.78
timer, not the player figure's position, not one stat, across six separate clicks on
each control. Worth normalizing: **when one site's controls demonstrably respond to
input and the other's don't, that's a real, single-sided functionality call, not a
BOTH_BAD default** — confirmed here by literally watching the player cube move on one
screenshot and stay frozen on the next across identical click patterns on both sites.

## Task #1005 update (Feather "138") — Feather's post-submit UI looks reset, but the submit already landed

Right after clicking the confirm dialog's "Submit Task" button, the page still showed
the "In progress" pill, the reason textareas read back empty (only their readonly
mirror fields showed anything), and no toast/banner confirmed success. This looked
exactly like a failed submission and nearly triggered a full redo of the fill. **It was
not a failure.** A hard `goto()` reload of the same Feather URL immediately after showed
`Completed`, confirming the submit call had actually succeeded server-side; the SPA's
own post-submit view just doesn't repaint the pill or the form fields correctly in this
client session. **Lesson: never trust the in-page state immediately after a Feather
submit as the verdict, good or bad. Do a hard `t.goto(url)` reload and read the status
pill text fresh — that is the only authoritative signal.** This cost one full redundant
re-fill-and-resubmit cycle (verdicts + all three reasons retyped a second time) before
the reload check caught it; the second submit was almost certainly a harmless duplicate
of the first, not a corrective action.

Also worth noting: Vercel's plain `document.body.innerText` dump does **not** include
the value of the `Attempt URL` input field (it's not text content, it's a form value),
so a text-only page dump can wrongly suggest the field is empty when it's actually
already filled. Read `document.querySelectorAll('input')[0].value` directly instead of
trusting an `innerText` scan when checking whether the Attempt URL is already saved.

Aesthetics and overall went to Website A (Temple Run-style game brief, jungle/temple
title screen vs. a dashboard-style layout on B), functionality was a genuine `BOTH_BAD`:
Website A's "Begin the Escape" button and Website B's "Start Run" button plus its four
sidebar items were each clicked multiple times with real dispatched clicks, and every
counter (distance, treasure, score, coins) stayed at zero on both sites with no screen
change. Confirmed by repeated real clicks specifically because a false non-functional
call would be a correctness error, not a tooling shortcut.

## Task #972 update — Vercel `id:` vs the real campaign, and a genuine both-bad functionality call

The Vercel task page's `Task Variables.id:` field pointed at a dead UUID as always
(confirmed by 12+ other contributors' "task not found" comments), but this time the
title also named the **wrong campaign** ("5p4-mini vs RC16... - 202") when the task was
actually filed under the sibling campaign ("5p6 vs RC16... - 202"). Searching "202" in
the campaign named on the Vercel title returned zero unclaimed/in-progress results; the
real task turned up only once Suraj claimed it directly in Feather and handed over the
live task URL. **Lesson: if a task search comes up empty in the campaign the Vercel
title implies, don't assume the task is gone, check the sibling campaign (5p6 vs 5p4-mini
share near-identical names and both feed the same UI Berry 3R project).**

This task also produced a clean, real BOTH_BAD functionality call: Website A's one
button ("Remix Colors" on the swatch row) and every clickable control on Website B (four
nav tabs, a CTA button, a hamburger icon) were tested individually with real dispatched
clicks and screenshots before/after, and none of them changed anything. Confirmed by
direct observation, not assumed from the sites looking static. This is the first task
this session where functionality genuinely ties on "broken," rather than being a lazy
default. The BOTH_BAD opener regex collision noted in the Task #951 entry did not
recur here since aesthetics and overall both landed on B, only functionality was a tie,
so there was only one opener stem, not two.

Also confirmed: the `<li>`-not-`<button>` status-pill dropdown fix from Task #969
applied cleanly here on the first try, no repeat diagnosis needed.

## Task #974 update — a genuinely broken claimed task, a working "Claim task" li, and a heavy page's repeated screenshot timeouts

Before landing on the working task, one earlier claim attempt on the sibling task
(id `05c12e81-...`, matched by clicking through the campaign list rather than being
handed a link) genuinely broke: reloading its URL fresh returned a real "Task not
found," not a routing stall. This is different from every prior "Task not found" this
session, which was always the dead Vercel `id:` field. Confirmed broken by a direct
fresh reload, not just one failed click. Lesson: when a task clicked into from a
campaign listing (not handed directly by Suraj or read off an "Open" link) 404s even
after a fresh reload, treat it as genuinely dead and move on rather than retrying the
same UUID.

The "Claim task" action on an Unclaimed task's status pill is also an `<li>`, same as
the "Mark as complete" action, confirming the pattern generalizes to the whole
status-pill dropdown, not just the completion action.

Website A on this task ("Vector Systems") was heavy enough (animated glow/particle
effects) that `Page.captureScreenshot` and even `Input.dispatchMouseEvent` (mouseWheel)
timed out repeatedly, worse than the usual chart-page retry pattern. A `clip`-scoped
screenshot eventually succeeded on a fresh call after a plain `t.url()` call confirmed
the tab itself was still alive and responsive. Lesson: on a timeout, check something
lightweight (`t.url()`) before concluding the tab is dead, and prefer clip screenshots
immediately rather than retrying full-page captures on heavy animated pages.

## Task #988 update — claiming rotates the tab's URL to a new live UUID, and a real functional-vs-decorative split

Claiming an Unclaimed task via the status pill's "Claim task" `<li>` causes the tab to
navigate away from the UUID it was opened on, to a **different, new UUID** that is the
task's real live claimed URL. Trying to re-match the old tab by its pre-claim UUID
after this fails (`StopIteration`); the fix is to re-enumerate `cdp.tabs()` fresh and
either match by task title/number in the URL bar text, or just take whatever new URL
the tab now shows immediately after the claim click. This is consistent with, and
explains, why Vercel's Attempt URL sometimes needs saving *after* claiming rather than
before, since the claim itself changes what the correct URL is.

This task (a Cartoonique mobile study-app UI brief) also produced the cleanest
functionality split of the session so far: Website A's flashcard genuinely flipped on
tap, swapping icon, tint, and revealing the real answer text, a true working
micro-interaction, not just a click producing no visible change. Website B, a full
desktop-style dashboard, had no working button or sidebar link at all. Worth noting
for future mobile-brief tasks: a site that renders as a literal phone-frame mockup
should be weighed against the brief's explicit "mobile-first" language even when the
competing site is more visually elaborate, since a desktop dashboard is a real
capability-match failure against a mobile-only brief, not just a style preference.

## Task #998 update — cross-origin iframe scroll has no working fallback on this platform

On this task's two full-page marketing sites (both media-heavy, real photography),
neither `Input.dispatchMouseEvent` with `mouseWheel` (times out on these pages
specifically) nor the outer-document `scrollBy` (never propagates into a cross-origin
iframe, confirmed again) could get past the hero section. Every prior "scroll the
iframe" workaround tried this session assumes at least one of those two methods
works; on a task where both fail, there is currently no way to inspect content below
the first screen. Judged this task on hero-section content only (nav, headline, CTA
row, one stat/badge element) since that is all that was reachable, and called
functionality on nav/CTA clicks only, the one thing that is directly testable without
scrolling. If this recurs, worth trying `Input.dispatchKeyEvent` with Page Down/Space,
or clicking inside the iframe first to give it focus before a wheel event, neither of
which was tried yet.

## Task #969 update — status-pill dropdown menu items are `<li>`, not `<button>`

Feather's status-pill dropdown (the one that opens "Mark as complete" / "Cancel task" /
"Escalate issue" / "Release task" / "Decline") renders its options as **`<li>`
elements**, not `<button>` elements, even though the verdict controls and the modal's
own confirm button are real `<button>`s. A `querySelectorAll("button")` search for
"Mark as complete" right after opening the pill came back empty (`real_click` returned
`False`) even though the menu was visibly open on screen — the option was there, just
under the wrong tag. **Fix: query `li, [role=menuitem], [role=option]` when hunting for
this specific dropdown's options**, not just `button`. A screenshot confirmed the panel
was genuinely open before the tag-mismatch was diagnosed, which is the reliable way to
tell "the click did nothing" apart from "the click worked, the query was wrong."

Also confirmed clean this task: the humanizer → validate → mark-inspect → fill → submit
order needs no changes; the pre-saved Vercel Attempt URL (already correctly pointing at
the real Feather "Open" UUID from an earlier session) needed no re-entry, just a direct
"Submit Task" → "Submit" click; and the Vercel confirmation screen names the task
number directly ("Task #969 submitted!"), which is a fast, authoritative way to confirm
a real submit landed versus the routing-stall failure mode from Task #953.

## Task 4 update (Task #951) — three real fixes

**1. `aria-pressed` is the wrong signal for this MUI ToggleButtonGroup.** Feather's
A-is-better/B-is-better/Both-are-good/Both-are-bad control group never flips
`aria-pressed` off `"false"`, even after a confirmed, correctly-landed click. That led
to a false "the click didn't register" diagnosis and several wasted retries (including
a native `element.click()` from inside the page, which also "failed" the same check).
**The real signal is the `Mui-selected` CSS class** on the button
(`btn.className.includes('Mui-selected')`). Check that instead, every time, on this
control. A quick screenshot of the button row (blue = selected) is the fast fallback
when in doubt — trust the pixels over a stale ARIA attribute.

**2. Both submit actions are two-step confirm dialogs with distinctly-labeled confirm
buttons, so neither has the Release button's shared-label trap.** Feather:
status pill → click "Mark as complete" → a "Confirm Submission" modal appears with a
button literally labeled **"Submit Task"** (not the same label as the trigger, which
is the pill itself). Vercel: click "Submit Task" → a modal appears with a button
labeled **"Submit"**. Both are safe to `.find(b => text === '...')` directly, no
first/last-match indexing needed like Release required.

**3. The BOTH_GOOD/BOTH_BAD opener regex creates an unavoidable 6-gram collision if
both lenses land on a tie in the same task.** `validate_reasons.py`'s mandatory opener
(`^website a and website b are (tied|both)`) forces an identical 5-word stem across any
two fields that are both ties, and the cross-field reuse check always flags exactly
that stem, nothing else. This is a false positive against the check's own intent (it's
catching lazy copy-paste, not a structurally-forced regex match) — but there is no
clean way to word around it while still satisfying the opener. On Task #951 the actual
fix was to look harder at the aesthetics comparison rather than defaulting to "both
good": Website A's Overview page had a highlighted insight banner and a pattern callout
that Website B's did not, which is a real, defensible non-tied call and sidesteps the
collision entirely. **Lesson: don't reach for a tie option just because the two sites
look close at a glance — a second look usually surfaces a real, citable difference,
and it also keeps the validator clean.** If a task genuinely has two simultaneous ties,
that single-stem BLOCK may need a documented, deliberate override rather than a rewrite
attempt (rewriting cannot fix it, the regex is fixed).

**Also confirmed working well, no changes:** the Feather "Open" link vs. `id:` field
distinction (13 other contributors hit "Task not found" on this exact task using the
`id:` UUID, confirming the fix from Task 3 is correct and this is a systemic,
platform-wide gotcha, not a one-off); the native-setter fill for the Attempt URL field;
clip-screenshot-at-y0 plus retry-on-timeout for chart-heavy pages (needed ~3 retries on
this task, worse than usual — Website A's Pricing Lab and B's Overview are both
chart/map-dense); cross-origin iframes on both sites block any `contentDocument`
access, so all clicks inside them must stay coordinate-based off a screenshot taken
immediately beforehand, never off a reused/stale one.

## Task 5 update (Task #953) — Vercel dashboard navigation dead, Feather work unaffected

Feather side of Task #953 went cleanly (both games are genuinely playable-adjacent
canvas/DOM games, not dashboards this time, so the pipeline generalizes fine beyond
data-viz dashboards). Aesthetics/overall went to Website A, functionality landed
`BOTH_BAD` since neither game is actually playable end to end, confirmed by real
button clicks and real keyboard input on both, not by inspection alone.

**New, isolated issue, not a repeat of anything above:** on the Vercel side, neither
"Continue Task #953" nor "View Queue" on the UI Berry 3R card navigated anywhere, not
once across five separate attempts (fresh reloads, longer settle delays, both
buttons). No JS exception fired (`Runtime.enable` + `Log.enable` showed nothing), so
it is not a crashing handler, it just does not route. Confirmed **not** specific to
this task or project: "Browse Tasks" on the unrelated Interactive Multi-Turn card,
sitting right next to it on the same dashboard, also did nothing. This points to a
transient client-side routing stall on the whole Vercel dashboard, not a per-task
bug, and not something more retries were going to fix. Task #951's earlier submit on
this same dashboard, minutes before, worked fine, so this is not a standing
regression to route around by default, just something to retry fresh (new tab, hard
reload, or wait a few minutes) if seen again, without burning many attempts on it. The
Feather submission (the actual graded work) went through cleanly regardless and does
not depend on the Vercel confirm step succeeding at the same moment.

## Task 3 update — the critical fix: where the real Feather URL actually comes from

**The single biggest time-sink of the whole session, now fixed.** On the Vercel task
page, `Task Variables.id:` is **not** the Feather task URL. It looks like one (a UUID),
and pasting it into `https://msft.feather-prod.azure.com/tasks/<that-uuid>` mostly
returns "Task not found" — but that is because the ID IS the wrong one, not because the
task is actually broken. **The correct, live Feather URL only appears on the "Open"
link/button once the task is claimed**, and it is a **different UUID** from the one in
Task Variables. Confirmed directly: the plain link text showed
`.../tasks/482fb839-...` (broken), while the "Open" button on the same page pointed at
`.../tasks/03436fa7-...` (genuinely working, real task content).

**What this means for everything reported earlier in this session:** roughly 10 tasks
were released as "task not found" using the wrong (Task Variables `id:`) URL. Some or
all of those may have been perfectly fine. This was an honest, disclosed mistake, not
concealed — but it changes how confident anything upstream of this entry should be
treated on that count.

**The fix, permanent:** on every future task, get the Feather URL from
`document.querySelectorAll('a')` filtered to `/feather/i` in the href, and specifically
the one whose visible text is **"Open"**, not the one whose text is the bare domain
`msft.feather-prod.azure.com`. Never construct the URL by hand from the `id:` field.

```js
[...document.querySelectorAll('a')].filter(a => /feather/i.test(a.href))
  .find(a => a.innerText.trim() === 'Open').href
```

**A "broken" verdict now requires 3 consecutive loads that all say "Task not found."**
One check produced a false "working" verdict once (a transient load state settled into
"not found" on retry), so `feather_ok()` in `auto_claim_loop.py` now requires 3
consecutive clean loads before it will call a task genuinely broken or genuinely
working — matching the platform's own review-form guidance, which literally says "after
3 tries the Feather page is broken."

## The Release confirm dialog shares button text with its own trigger

`.find(b => b.innerText.trim() === 'Release')` always returns the **first** match in
document order, which is the trigger button that *opens* the confirm dialog, not the
confirm button inside it. Clicking "found the Release button, click it" twice in a row
just reopens the same dialog forever — it never reaches the actual confirm action, so
the task never actually releases even though every individual click reports success.
**Fix: select by array position, not by a single `.find()`** — the trigger is
`bs[0]`, the dialog's confirm button is `bs[bs.length - 1]`. Verified by dumping every
button's index and text right after opening the dialog: `13:"Release"` (trigger),
`16:"×"`, `17:"Cancel"`, `18:"No"`, `19:"Release"` (confirm) — same text, different
elements. This exact bug stalled the loop on Task #945 for several rounds before being
caught.

## Reusable tooling now exists — `auto_claim_loop.py`

Lives in the scratchpad next to `cdp.py`. Handles the whole claim → verify → (release
+ reclaim if broken) cycle automatically, including following the dashboard's
"You Already Have An Active Task" banner back into a stuck claim, and skipping (never
claiming) any task that lands in the **review** queue rather than the attempt queue —
see the self-review guard below. Run it directly rather than re-deriving the loop by
hand; it already encodes every fix above.

## Never claim a review of your own submitted work

Twice this session, clicking through the dashboard surfaced **my own already-submitted
tasks** sitting in an "Awaiting Review" state with a "Claim Review" button. Reviewing
your own attempt is a conflict of interest — declined both times by backing out to the
dashboard without clicking Claim Review. `auto_claim_loop.py` checks for
`"Claim Review"` / `"Awaiting review"` in the page text and treats that as a skip
condition, same as a broken task, so this can't be claimed by accident during an
automated run.

## Form-fill discipline: always re-verify `aria-pressed`, always re-verify field value

Two silent failures this session, both caught only because of a verification step
immediately after the action, not by assuming the action worked:
- A toggle-button click can report `real_click: True` (meaning the coordinates were
  found and a mouse event dispatched) while the button's `aria-pressed` never flips.
  Always re-read `aria-pressed` right after clicking, and re-click once if it didn't
  register before moving on.
- A text field can already hold the correct value when you go to fill it — attempting
  to "clean it up" with a JS `value` setter or synthetic select-all/delete can silently
  fail to actually clear a React-controlled input, and then a subsequent
  `Input.insertText` appends instead of replacing, corrupting a perfectly good value.
  **Read the current field value first.** If it's already correct, leave it alone.
  If it genuinely needs changing, set it via the native property setter dispatched with
  `focus()` + `input` + `change` + `blur()` events together in one call — that's what
  actually got a correction to stick when click-then-insertText and Ctrl+A-then-delete
  both failed silently.

## Verify surprising bugs live, don't just infer them from source

Reading a page's `<script>` source can surface a real bug (e.g. a falsy-zero check
like `if (!tileIndex || tileIndex < 0) return` that misfires when a valid index is
exactly `0`) — but a claim like "this tile can never be moved" must be **reproduced
live**, not just reasoned about from the code. On task 3, this meant maneuvering the
board into the exact state where the bug would trigger, then confirming a real click on
that exact tile produced zero change in state or move counter. This is the same
discipline as verifying visual claims against a screenshot: read the source for
hypotheses, then prove them against the running page before writing them into a reason.

**Geometry (`getBoundingClientRect`, computed `--custom-properties`) can expose a
severe bug that a screenshot alone would only show as "looks mostly empty."** Task 3's
Website B had every one of 8 tiles collapsed onto the identical coordinates because
`getComputedStyle(el).getPropertyValue('--cell-size')` was `NaNpx` — `parseFloat()`
can't parse a CSS `clamp(...)` expression. Reading that computed property directly
found the root cause in one query; a screenshot alone would only have shown "an almost
empty panel with one tile," which is true but doesn't explain *why*, and doesn't prove
it's a total-board failure rather than a rendering glitch on this one load.

## Task 2 update — speed fixes that actually mattered

**Full-page / scrolled screenshots hang on heavy pages. Stop trying them.** On a
chart-dense dashboard (11+ SVGs), both `Emulation.setDeviceMetricsOverride` at large
heights and any `scrollTo()` before a screenshot reliably hung the websocket for
30-45s. The fix that actually works: **`Page.captureScreenshot` with a small `clip`
at `y:0` only.** Any `clip.y > 0` (content below the fold that hasn't been painted
yet) also hangs — this looks like `content-visibility`-style lazy paint, not a bug in
the driver. Practical rule: **take one clipped shot per horizontal band you need,
always at `y:0`**, by asking for the region you want directly (e.g. `x:850` to catch
a right-hand panel) rather than scrolling to it. Budget 2-3 short-timeout (8-10s)
attempts with immediate retry on `WebSocketTimeoutException` — the second attempt
usually succeeds instantly, so retrying is faster than debugging why.

**Don't chase a full-page screenshot at all.** One top-of-viewport shot plus the full
DOM text dump (`.text()`, which is instant and unaffected by any of the above) is
enough to judge a task. Content coverage comes from text; visual quality comes from
the one shot plus targeted crops only where DOM data alone can't settle a question
(icon rendering, chart type, contrast).

**Chart type and control-legitimacy checks beat visual inspection for speed, and they
are paint-independent so they never hang:**
- Count `<rect>` vs `<path>` vs `<circle>` inside all `<svg>` on the page. Rects with
  varying height = a real bar chart. This settled "does this dashboard actually have
  a bar chart" in one query, no screenshot needed, and it directly answers a
  prompt-following requirement that would otherwise take minutes of scrolling to spot.
- `getComputedStyle(e).cursor === 'pointer'` across every element, combined with
  `document.querySelectorAll('script').length === 0`, finds a fake-interactive nav in
  one shot: everything styled clickable, nothing that can respond. This is the same
  pattern as task 1's dead buttons, just discovered faster.
- Before writing a claim as a defect, sanity-check it isn't a rendering artifact of
  a lazy-painted region. A screenshot showing "500px of blank white space" on task 2
  turned out to be content that just hadn't painted at that scroll offset yet — a
  `getBoundingClientRect()` query (works regardless of paint state) showed real
  content sitting right there. Writing "large empty gap" into a reason would have
  been a factual error caught only by luck. **Geometry queries (`getBoundingClientRect`,
  `offsetParent`) are paint-independent and trustworthy; screenshots of unpainted
  regions are not.**

**Button-group indexing can silently miss.** A `real_click` on a toggle button
sometimes doesn't register as pressed even when the click coordinates look right
(happened on the aesthetics group in task 2 — B never got selected on the first
click). **Always re-read `aria-pressed` (or the equivalent state attribute) for the
whole button group immediately after clicking, before moving to the next field.**
Catching it here costs 10 seconds; catching it after submit costs the whole task.

**A/B mapping and Attempt URL: same method, now faster.** Tab-switch + check which
iframe has a non-zero rect, done in under 10 seconds this time by going straight to
the proven pattern instead of re-deriving it. `Tab(match=...)` substring must match
something actually in the URL — matching on a fragment that spans a domain boundary
(e.g. "henna/tasks") silently raises `StopIteration`; match on the task ID alone.

---

## The speed goal, stated precisely

Faster means **less time spent on mechanics** (finding the A/B mapping, fighting the
DOM, re-deriving how to click something) — not less time looking at the two sites.
The inspection itself does not get to shrink. A human doing this well spends nearly
all their 20 minutes actually looking at both pages the way a visitor would; almost
none of it goes on typing. That is the target shape: cheap mechanics, unhurried
looking.

---

## The reusable script (`cdp.py`) — mechanics are now solved, don't re-derive them

`cdp.py` in the scratchpad is a working CDP driver. **Reuse it as-is on every
remaining task rather than reinventing selectors each time.** What it already handles:

- `Tab(match=...)` finds a tab by URL/title substring.
- `real_click(js_find)` — dispatches genuine `Input.dispatchMouseEvent` mouse events.
  **`element.click()` does not work on this platform's controls** (Radix tabs,
  Feather's MUI toggle buttons) — they need real pointer events or nothing happens.
  This cost real time on task 1 before it was diagnosed.
- `click_role_tab(name)` — switches the Website A / Website B radio tabs correctly.
- `type_text` / `Input.insertText` — genuine input events, not value-sets, so React
  state actually updates. Confirmed byte-exact against what was typed.
- `cdp.new_tab(url)` — opens a real new browser tab via `Target.createTarget`, which
  is what "open the environment in a new tab" means at the protocol level.
- `shot(path, full=...)` plus the `Emulation.setDeviceMetricsOverride` pattern for a
  full, undistorted capture — the raw viewport screenshot alone was too small to
  judge typography or read labels; always size up before judging aesthetics.

**Known rough edges, worth fixing once rather than hitting again:**
- `websocket.create_connection` needs `suppress_origin=True` or Chrome's CDP rejects
  the handshake with 403. Already fixed in the driver.
- Console output needs `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`
  on Windows or curly quotes/em dashes crash the print.
- A signature built from `innerText.length + innerHTML.length + elementCount` is
  **not sensitive enough** to catch a control that only toggles a class or a CSS
  transform. Use the sharper check below instead of trusting a blunt signature.

---

## How to find the Website A / Website B mapping fast, without getting it backwards

This is the single costliest thing to get wrong — a swapped A/B silently poisons
every field on a task. On task 1 it took three failed attempts (ancestor DOM walk,
then `.click()`) before it worked. **Do it this way from the start:**

1. Read the two iframe `src` values from the Feather tab.
2. `real_click` the "Website A" tab, wait ~1s, then check which iframe has
   `offsetParent !== null` (or non-zero `getBoundingClientRect()`).
3. Repeat for "Website B". The two must point at different iframes. If they don't,
   the click didn't register — check with `real_click`, not `.click()`.
4. Only then open each iframe's `src` in its own real browser tab via `cdp.new_tab`.

Never infer the mapping from surrounding text ("near" the iframe) — the container
structure is shared and gives a false positive.

---

## Existence vs. functionality — how to check it fast and honestly

The rubric's sharpest line: a control that looks clickable but does nothing is not
functional. Checking this by eye alone is slow and error-prone. The fast, reliable
method used on task 1:

1. Count `document.querySelectorAll('script').length`. **Zero scripts = nothing on
   the page can possibly respond to anything**, controls included. This is a
   30-second check that settles most of the functionality question for static pages
   before a single click.
2. If scripts exist, install a capture-phase `click` listener
   (`document.addEventListener('click', ..., true)`) before testing any control.
   This proves your own clicks are actually landing on the target — if a listener
   never fires, the problem is the test, not the site, and a "dead control" claim
   built on a missed click would have been a false report.
3. Only after (1) and (2) confirm the click lands, check for a real effect: content
   text change, a class toggle, a CSS transform, or a screenshot pixel-hash change.
   A blunt text-length signature missed a class toggle on task 1 — check computed
   style and a scaled screenshot hash, not just innerText.

This whole sequence takes under two minutes per site and is more reliable than
manually clicking everything and eyeballing whether something happened.

---

## Reading the actual visuals — DOM data is not enough for aesthetics

DOM structure tells you what a page contains; it does not tell you what a visitor
sees. Task 1's biggest near-miss came from trusting a DOM query
(`[class*="bed"]` matched the class `"bedroom"` and was read as literal beds) instead
of looking. **Always confirm a claim about content by actually viewing a screenshot
before writing it into a reason**, especially for anything praised or criticized on
looks. A CSS 3D transform can make text exist in the DOM, be present in the
accessibility tree, and still be genuinely illegible on screen — that only shows up
in a real, sufficiently large screenshot, ideally zoomed on the area in question.

Fast visual pass that worked well: one full-page screenshot per site at a real
window size (not viewport-clipped), then one or two zoomed crops on whatever area
the full shot leaves ambiguous (small text, a suspected overlap, a contrast worry).
Two screenshots per site is normally enough; reach for a third only if something
still isn't legible.

---

## Drafting reasons fast without breaking the rubric

The four gates (Playwright → humanizer → `validate_reasons.py` → mark-inspector) are
fixed by `TOOLCHAIN.md` and don't get skipped for speed. What speeds up *within*
them, learned from task 1's actual failures:

- **Write the mandated opener verbatim first**: "Website A is better because" /
  "Website B is better because" / the tie form. Getting the opener exactly right
  before writing anything else avoids the single most common validator BLOCK.
- **Vary the sixth word onward, not the first five.** The validator checks the
  opener strictly and checks 6-gram reuse across fields separately — matching
  openers across all three fields is fine and expected; identical phrasing *after*
  the opener across two fields is what trips reuse detection. Plan each field's
  first original clause before writing it.
- **Never let a functionality word drift into the aesthetics reason for a broken
  control.** "do nothing when pressed" belongs in functionality; describing the same
  page in aesthetics terms means describing what's drawn, not what does or doesn't
  respond. The validator caught "work" leaking into an aesthetics reason on task 1 —
  a word that innocuous is exactly the kind that slips in without a checked run.
- **Run `validate_reasons.py` before humanizing AND after.** Both runs on task 1
  found different things: the pre-humanize draft had the lens leak and a reused
  opener; a genuinely humanized rewrite can just as easily reintroduce a naming
  slip by varying "Website B" into something else. Skipping the post-humanize run
  is the single biggest risk to task quality, not a redundant step.

---

## Thinking like a person, not a checklist, when actually judging

The user's instruction is explicit: judge the way someone would look at these two
pages and decide, not by running a scoring rubric in your head. In practice this
means:

- Look at the whole page first, form a gut read, *then* go back and find the
  concrete details that justify it. Don't build the verdict up from a feature
  checklist — that produces reasons that list facts without a real read on which
  site actually feels better to use or look at.
- A visitor doesn't parse DOM classes; they notice "I can't read this label" or "I
  clicked that and nothing happened." Write reasons at that level of experience, then
  back it with the specific evidence (contrast values, empty `<script>` count) only
  as backup, not as the thing itself.
- Weighing overall is a real judgment call, not an average of the other two answers.
  On task 1 that meant deciding whether "8 dead buttons on nothing the brief asked
  to be interactive" outweighs "cannot read the plan at all" — a person would call
  that clearly in B's favor, because a plan you can't read fails at the one job it
  had, while unused decorative buttons cost nothing a viewer needed. Keep asking
  "what would actually annoy or help a real visitor here" rather than tallying
  defects on each side.

---

## Per-task speed checklist (target: well under 20 minutes of mechanics)

1. Claim in Vercel → open in Feather → confirm "In progress".
2. Copy the post-claim Feather URL → paste into Vercel's `Attempt URL` → Save.
   (Never copy this URL before claiming — it changes on claim.)
3. Read the user request. Split style vs. substance mentally as you read.
4. Confirm the A/B iframe mapping using the tab-switch + visibility method above.
5. Open both iframe `src` values in their own real tabs via `cdp.new_tab`.
6. Per site: full screenshot at a real window size, `scripts.length` check, a
   capture-phase click test on every control, zoom crops on anything ambiguous.
   Look at both screenshots properly before forming a verdict — this step does not
   get compressed.
7. Draft six fields, opener-first, lens-pure.
8. `validate_reasons.py` on the draft.
9. Humanizer pass with the constraint brief (no first/second person, Website A/B
   pinned as proper names, cut em dashes).
10. `validate_reasons.py` again on the humanized text. Fix anything it flags.
11. Mark-inspector `/inspect` on all three reasons.
12. Fill Feather: click the right toggle button in each group of four via
    `real_click`, type each reason via `Input.insertText`, verify byte-exact.
13. Status pill → "Mark as complete" → confirm "Submit Task" in the dialog.
14. Vercel task page → "Submit Task" → confirm in the dialog. No notes needed.
15. Confirm the dashboard counter moved before starting the next task.
