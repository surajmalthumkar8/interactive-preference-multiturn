# Uritorco learnings: read before the next task

Newest first. These are things a previous task got wrong or nearly got wrong.

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
careful. Disambiguate by x position (Left < 760 < Right) or Playwright `nth`.

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
