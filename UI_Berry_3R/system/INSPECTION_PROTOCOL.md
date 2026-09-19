# Inspection protocol — how a human actually checks these sites

**Adopted 2026-09-19 from the TechAegisAI fork, where it was derived from 14 scored
reviews.** `REVIEW_LESSONS.md` carries the raw reviewer feedback and protocols P1-P16.
This file is the operating procedure that follows from it.

---

## The one statistic that should govern everything

Across nine scored reviews of the 2026-09-16 batch: **two 2/5 and seven 3/5, and eight of
the nine were the same defect — a working control described as dead.** In seven of those the
false claim flipped the functionality verdict, and overall inherited the error.

**Aesthetics was praised in almost every review.** The inspection *looks* thorough. The
negative claims are what fail.

> A missing negative costs nothing. A false one costs two points.

This asymmetry decides every ambiguous call: **when in doubt, say nothing.**

---

## Reading the request — the two-column split

Do this before opening either site. It is the single biggest time-saver and it stops the
lenses bleeding into each other.

| Style column -> feeds AESTHETICS | Substance column -> feeds FUNCTIONALITY |
|---|---|
| palette, fonts, layout style | the app and its purpose |
| image style, reference brands | every section explicitly named |
| mood words (calm, bold, earthy) | every feature and control asked for |

Keep visual notes and behavioral notes in separate lists while inspecting. They feed
different fields and must never be merged.

---

## Inspecting — what counts as sufficient

1. **Real Chrome, each site in its own full tab.** Never judge from the embedded preview.
   The only exception: the tab is blank *and* the preview renders, and then you say so.
2. **Scroll top to bottom before judging anything.** Content sits below the fold.
3. **Click every control and confirm it updates content.** Existence is not functionality.
4. **Run the brief's main flow end to end on both sites with the same test data** — same
   values, same order. Capture console and pageerror. A JS error on the happy path is a
   functionality finding.

### Scroll-reveal pages break full-page screenshots
Sections waiting on an IntersectionObserver sit at `opacity: 0`, so a fullPage capture shows
a hero over thousands of pixels of blank. **Scroll in ~400px steps with a short wait before
any capture or any "empty below the fold" claim.**

---

## Before writing ANY negative — the P1 gate

Trigger words: *dead, inert, does nothing, never, nothing else, static, unusable, broken,
stuck, not wired, only a toast, swallows clicks, no confirmation.*

Before any of those reach a reason, the log must show, for **that exact control**:

- [ ] a **real pointer action** — `locator.click()` or `mouse.move -> down -> up` — in a
      **visible standalone tab**, control scrolled into view.
      **`el.click()` from `evaluate` does not count.** Hover, press, focus and
      pointer-driven handlers never fire, so a live button looks dead.
- [ ] a **before/after capture >=800ms later**: DOM text, class/aria state, URL/hash,
      scrollY, screenshot, console errors, `[aria-live]`/toast text, open dialogs.
- [ ] **a retry by a different route** (keyboard Enter/Space on the focused control, or a
      coordinate click at the rect centre). Per P11, **two routes minimum.**
      *If the second try disagrees with the first, the negative is not written.*

Missing any row -> **cut the sentence.** Do not soften it.

### P12 — the tool can be the defect
Prove the instrument is not the cause before blaming the site.

- A `createObjectURL` hook must **pass the real URL through** (record and return
  `orig.call(URL, b)`). A faked URL silently breaks canvas and video exports — that is
  exactly how task 18128 produced a false "still image" report.
- When an export produces nothing or the wrong thing, **re-run it with all hooks removed on
  a fresh reload** before writing it up.
- **Read the blob type, never the toast label.** A reviewer corrected an "exports CSV"
  claim to Excel because the toast was trusted over the MIME type.

### P13 — wait, do not sample
A render, upload or export read at zero a few seconds in is not a failure. Poll to
completion or for **at least thirty seconds**. If it is still running when you stop, say
only that it was still running.

### P16 — no absolutes without enumeration
Banned unless the checklist was walked item by item, or the rects were measured:
*to the letter, every piece present, complete, nothing missing, crowds/overlaps the edge.*

---

## Scoping — P4

Write what was tested, not what was assumed.

> "The five questions tried, including two of the three suggested prompts, all returned the
> same paragraph."

Not "every question". The reviewer will try the one you skipped.

---

## Lens placement — P8

- Duplicated, misaligned, overlapping or clipped elements -> **aesthetics**.
- A control that fails to do its job -> **functionality**.

A layout fault is never evidence that a control is dead.

## Unrequested extras — P7 and P15

- Extras the brief never asked for (export, share, print, theme toggles) **cannot decide
  functionality.** If both sites deliver the brief's asks and the happy path is clean, the
  lens is "Both are good".
- **But P15 overrides P7 for requested behaviour.** If the reason names a brief requirement
  that one side meets and the other does not, that side wins functionality — it is not a tie.
  The validator now BLOCKs a BOTH verdict whose reason says "only Website A/B" or
  "while Website A/B".

## Prefer the positive frame — P9

> "Website B's expense form saves into the list and the totals; Website A's all-time daily
> average treats months as one day."

That beats any sentence built on "does not". Reviewers consistently rewarded reasons naming
a real behavioural difference over ones declaring a site inert.

---

## The claim table — P10, run before humanizing

For every negative in the functionality and overall drafts, write a scratch table:

| claim | evidence (probe key / log line) |
|---|---|

**Any row without evidence is deleted from the draft.** This is the factual audit made
concrete, and it happens *before* the humanizer, not after.
