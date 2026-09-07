# UI Berry 3R — Reconciled Working Knowledge

Derived from the eleven Learning Hub docs in this folder. Where this file and a source
doc disagree, the source doc wins and this file is stale. Citations point at the source
file so every rule stays traceable.

---

## 1. What the task is

Two websites — **Website A** and **Website B** — were generated from the **same user
request**. Judge the pair **three separate times** through three different lenses, and
justify each verdict on its own. (`Project_overview.md` §03)

Budget: **~20 min to attempt, ~20 min to review.** (`Project_overview.md` §01)

**Six required fields. None is ever left empty.** (`Project_overview.md` §02, §04)

| # | Field | Options | Reason length |
|---|---|---|---|
| 1 | Aesthetics — which is better? | A better / B better / Both good / Both bad | — |
| 2 | Aesthetics reason | — | 40–160 words, visual factors only |
| 3 | Functionality — which is better? | same four | — |
| 4 | Functionality reason | — | 40–160 words, behavior + prompt-following only |
| 5 | Overall — which is better? | same four | — |
| 6 | Overall reason | — | 40–160 words, must show the trade-off |

**In scope:** what the page shows, whether it works, how well it answers the request.
**Out of scope:** source code and the effort behind either site. Outcomes, not
implementations. (`Project_overview.md` §06)

---

## 2. Non-negotiable setup

1. **Google Chrome only.** No Firefox, Safari, Edge, Brave, Opera. Rendering and
   interactive behavior differ, so another browser makes the work non-comparable.
   (`Learning Hub.md` §01)
   → Satisfied by the hardened Playwright profile, which drives **real Chrome**, not
   bundled Chromium. See `TOOLCHAIN.md` §1. The four mandatory gates in that file
   (Playwright profile → humanizer → re-validate → mark-inspect) apply to **every** task.
2. **Never judge from the embedded preview.** Use the *Open the environment in a new
   tab* button — the round arrow-leaving-a-square icon in the dark bar at the bottom of
   the candidate tab, right of **Capture**. Do it for A and for B, every task.
   (`Learning Hub.md` §02)
3. **The full tab is the source of truth.** If preview and full tab disagree, the full
   tab wins. (`Learning Hub.md` §03)
4. **The single exception:** the new tab opens blank/broken **and** the preview does
   render. Only then judge from the preview, and say so in the reasons. Not applicable
   for slowness, odd layout, or convenience. (`Learning Hub.md` §04)

---

## 3. Per-task order

Read request → open both in new tabs → inspect A fully → inspect B fully → answer
aesthetics, then functionality, then overall. (`Evalution_workflow.md`)

While reading the request, split it into two columns as you go — this is the single
biggest time-saver:

- **Style column** (feeds aesthetics): palette, fonts, layout style, image style,
  reference brands.
- **Substance column** (feeds functionality): the app, its purpose, the sections,
  features and controls explicitly asked for.

While inspecting: scroll top to bottom (never judge the first screen), click **every**
control, and confirm each one **updates content** rather than merely existing. Keep
visual notes separate from behavioral notes — they feed different fields.
(`Evalution_workflow.md` §04, `Checklist.md` §02)

Answer in order, because aesthetics and functionality are the two inputs the overall
judgement is built from. (`Evalution_workflow.md` §05)

---

## 4. The three lenses

### Aesthetics — visual quality only
Layout and composition · typography · color and palette fidelity to the request ·
polish and consistency · spacing and density · visual artifacts (overlap, overflow,
cut-off, misalignment).
**Ignore whether controls work.** A beautiful page whose buttons do nothing can still
win this question. (`Three_question_set.md` §02)

### Functionality — behavior and prompt-following
Requested content actually renders · links/buttons/controls do something and update
content · navigation goes where it should · filters, forms, carousels, calculators
respond · nothing dead or broken.
**Existence is not functionality.** Scroll everything and click everything first.
**Ignore visual polish** — unless broken rendering is severe enough to prevent
functionality being inspected at all, which then counts as a functionality failure.
(`Three_question_set.md` §03)

### Overall — the complete experience
Which website a real user would rather land on **for this request**. There is **no
formula** deriving it from the other two, and it need not match either. When the lenses
disagree, decide which shortcoming does more damage — a plainer look, or missing
content and dead controls — and **make that weighing visible** in the reason.
(`Three_question_set.md` §04)

Valid outcomes include A/B/B, and A/B/Both-are-good. Invalid: defaulting overall to
whoever won functionality, or repeating the aesthetics answer out of habit.

---

## 5. Choosing among the four options

**Decision order, per question:** first ask whether one site beats the other on *that
question's* criteria. Only if they are effectively tied do you reach for a "Both"
option. (`How_to_choose_your_answer.md` §01)

**"Better" is relative, not absolute.** Picking "A is better" does not claim A is good
— only that it beats B on this question. This holds when both are strong and when both
are weak. **If one is merely less bad, it still takes the win.**
(`How_to_choose_your_answer.md` §02)

**"Both" options are for genuine ties only.** If you can argue either side, it is not a
tie. Once a tie is established, place the pair on the 1–6 quality scale to pick which
tie it is: (`How_to_choose_your_answer.md` §03)

| 1 Poor | 2 Weak | 3 Below Par | 4 Solid | 5 Good | 6 Strong |
|---|---|---|---|---|---|

- **Both are good** — tied, and the pair lands around 4–6.
- **Both are bad** — tied, and the pair lands around 1–3.

The 1–6 band is **never entered anywhere**. It is a mental check that only runs *after*
a tie has already been established.

---

## 6. Broken candidates

Breakage never blocks the task. A site that fails to load, freezes the tab, or cannot
be rendered enough to inspect is a **functionality failure**: still complete all six
fields, describe the breakage in the reasons, and move on. Nothing to report anywhere.
(`Handlish_broken_candidates.md` §01)

**Before calling it broken:** confirm Chrome · open via the new-tab button · scroll the
whole page (content can sit below the fold) · you may refresh back to the Instructions
tab and retry · if the tab is blank but the preview renders, use the preview exception.
(`Handlish_broken_candidates.md` §02)

**Effect, one site broken:** the working website wins **all three** questions.
Aesthetics — say plainly there was nothing visible to assess. Functionality — describe
what happened (blank tab, frozen page, content that never loaded). Overall — a page
that cannot be used is not an experience anyone can prefer.
(`Handlish_broken_candidates.md` §03)

**Both broken:** "Both are bad" on all three, state in each reason that neither renders
or name the error each shows, invent no differences, and the **word minimum does not
apply**. (`Handlish_broken_candidates.md` §03)

---

## 7. Writing the reasons — where the value lives

**Structure:** open with the outcome, then the concrete evidence, describing **both**
websites rather than only the winner. Each reason must stand alone and be understandable
by itself. (`writing_the_reasons.md` §01–§02)

**State the outcome explicitly**, matching the option selected. "Website A is better
because…" / "Website B is better because…" / for a tie, "Website A and Website B are
tied because…", making clear whether the pair is good or bad. Listing pros and cons
without naming a result is not enough. (`writing_the_reasons.md` §03)

**Lens purity is absolute.** No functionality in the aesthetics reason, no visual
quality in the functionality reason. A crossover is **incorrect even when everything it
says is true**. The overall reason is the only place both may appear together, because
weighing them is what that question asks. (`writing_the_reasons.md` §04)

**The ten reason rules** (`writing_the_reasons.md` §06):

1. State the outcome first, matching the selected option.
2. Stay inside the lens.
3. Name them **"Website A"** and **"Website B"** in full at **every** mention. A bare
   letter, or "the first one", is rejected.
4. Be specific and concrete — name a difference a reader could go and verify.
5. Describe both websites, not only the winner.
6. Report problems: breakage in the functionality reason, visual artifacts in the
   aesthetics reason.
7. **Do not name the evaluation categories.** Describe what each site shows or does in
   plain language instead.
8. Keep a tie balanced — it must not read as one-sided, e.g. by listing more faults for
   one side.
9. Do not reuse text across the three fields.
10. Stay in scope: third person, websites only. No mention of the browser, the tabs, or
    the platform — the one exception being that a site had to be inspected from the
    preview because its tab did not load.

**The overall reason** must show how the two lenses were weighed *for this request*.
When the other two disagree, say which shortcoming mattered more and why. When they
agree, say what makes the combined experience better rather than restating one of them.
Never recycle another field's text. (`writing_the_reasons.md` §05)

---

## 8. Resolved contradictions and sharp edges

These are cross-doc tensions found by comparing the eleven files. Each resolution names
the rule that wins and why.

**R1 — Word floor vs. the both-broken carve-out.**
`writing_the_reasons.md` §02 and `Checklist.md` set a hard 40-word floor, and
`Feedback_and_scoring_guide.md` scores a reason outside the range as a **2**. But
`Handlish_broken_candidates.md` §03 waives the minimum when *both* sites are broken.
→ **The carve-out is the more specific rule and wins, but only when both are broken.**
When only one is broken, the working site supplies ample material and the 40-word floor
stands on all three reasons. The 160-word ceiling is **never** waived.

**R2 — Describing breakage inside the aesthetics reason.**
Lens purity forbids functionality talk there, yet the broken-candidate rule *requires*
saying there was nothing visible to assess.
→ **Permitted, but phrase it as a visual absence, not a behavioral failure.** Write
"Website B presents an empty white viewport with no layout, type or imagery to assess."
Do **not** write "Website B fails to load" or "throws an error" — that is the
functionality reason's language.

**R3 — Severe rendering breakage inside the functionality reason.**
`Three_question_set.md` §03 lets broken rendering count as a functionality failure when
it blocks inspection.
→ Admit it only at the level of **"the content could not be reached or used"**, never
as "it looks bad". The bar is *prevented inspection*, not ugliness.

**R4 — Two numeric scales that are easy to confuse.**
The **1–6** scale is the attempter's, judges the *websites*, and runs only after a tie
is established to choose Both-good vs Both-bad. The **1–5** scale is the reviewer's and
judges the *submission*, not the websites. They are unrelated. Never let one leak into
the other.

**R5 — "Both are bad" when both are broken but unequally.**
`Handlish_broken_candidates.md` §03 says pick Both are bad and "do not invent
differences". `How_to_choose_your_answer.md` §04 says always pick the better side when
a real difference exists.
→ **A real, observable difference is not an invented one.** If one site is blank and
the other renders a header and half a hero before dying, that is a genuine difference
and the less-broken site wins. "Both are bad" covers the case where both fail
equivalently — two blank tabs, two crash screens.

**R6 — Stating the outcome vs. not naming the categories.**
Rule 1 demands the verdict up front; rule 7 forbids category labels.
→ Open **"Website A is better because &lt;concrete fact&gt;"**, not "Website A is better
on aesthetics because…". The verdict is named; the category is not. Avoid the words
*aesthetics*, *functionality*, *visual quality*, *usability* as labels in the body.

**S1 — The inertia trap.** Answering all three the same way is a valid outcome when
earned and a serious error when it is habit. (`Common_mistakes_to_avoid.md` §01)

**S2 — Tie contradicted by its own reason.** Picking a "Both" option and then writing
text that names a winner ("more complete", "clearer", "less broken") is the single most
frequent error. (`Common_mistakes_to_avoid.md` §01)

**S3 — Features vs. fulfillment.** Do not reward the *number* of features over actual
fulfillment of the user request. (`Common_mistakes_to_avoid.md` §03)

---

## 9. The reviewer side

A reviewer **re-does the inspection** — Chrome, both tabs, full scroll, all controls.
A review written from the reasons alone cannot separate a correct claim from an
invented one, which is the main thing a reviewer contributes.
(`Reviewer_guide.md` §01)

**Score 1–5** (`Feedback_and_scoring_guide.md` §01):

| Score | Meaning |
|---|---|
| **1** | Completely wrong. Empty/nonsense fields, reasons unrelated to the sites, inspection evidently never done. |
| **2** | Major errors: wrong website chosen, a reason describing things that do not exist, a reason contradicting its own option, a tie written as one-sided, lenses mixed, text reused, naming rule broken, reason outside the word range. |
| **3** | Several minor problems, or one that noticeably weakens a justification — something important unmentioned, or a detail described inaccurately — while the options are still correct. |
| **4** | One small problem that changes neither the outcome nor the strength of the reasoning. |
| **5** | Perfect: three right options, three reasons accurate, complete, in-lens, in-range. |

**Objectivity is binding.** Never dock points for personal taste or for wording you
would have chosen differently. Lower a score only for something **verifiable**: a claim
that does not match the sites, a rule from the guide that was broken, or an option the
evidence does not support. A defensible call stands even when your own preference points
the other way. (`Feedback_and_scoring_guide.md` §02)

**The overall question deserves extra restraint** — two people can weigh the same
trade-off differently and both be right. Only two things are legitimately challengeable
there: an overall answer that **contradicts the attempter's own evidence**, or one whose
reason **never explains the weighing at all**.

**Feedback below 5 must name three things:** which field, what exactly is wrong, and
what it should have said or chosen instead. "The task had errors" teaches nothing.
(`Feedback_and_scoring_guide.md` §03)

**Factual error is the most serious problem a submission can have**, because it means
the inspection was not really performed. Check that everything claimed exists in the
site it is attributed to, that nothing important was missed, and that failures are not
swapped between the two sites. (`Reviewer_guide.md` §04)
