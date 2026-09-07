# Self-Review Gate

Run this on your own submission before you send it, in the role of the reviewer who will
score it 1–5. The discipline is to look for the reason to **dock a point**, not for
confirmation. Any **BLOCK** below must be fixed before submitting.

The order matters: mechanical checks first (they are cheap and objective), then lens
purity, then the factual audit, which is the expensive one and the one that decides
whether the submission is honest work.

---

## Pass 0 — the mandatory toolchain (`TOOLCHAIN.md`)

None of these is optional. Confirm each one actually ran.

- [ ] Both sites inspected in **real Chrome via the hardened Playwright profile**, each in
      its own full tab, scrolled top to bottom, every control exercised. **BLOCK**
- [ ] No stealth flag, UA override or proxy was added on top of the profile. **BLOCK**
- [ ] Any challenge page was **stopped on and handed to Suraj**, never solved. **BLOCK**
- [ ] All three reasons passed the **`humanizer` skill**, with the constraint brief
      attached (suppress PERSONALITY AND SOUL; "Website A"/"Website B" are proper names
      and never varied; third person, no "you"). **BLOCK**
- [ ] `python system/validate_reasons.py task.json` run **after** humanization and exits
      clean. Humanization is a rewrite, so the pre-humanization run does not count. **BLOCK**
- [ ] `mark-inspector` `/inspect` run on all three reasons, `suspicious: false`. **BLOCK**
- [ ] Layer B `/clean` was **not** run on any reason. **BLOCK**

A clean validator run covers Pass 1 and Pass 2 mechanically. Passes 3 and 4 are still
yours — no tool can check them.

---

## Pass 1 — Mechanics (each failure is a scored **2**)

- [ ] All six fields non-empty. **BLOCK**
- [ ] Each reason is 40–160 words, counted individually. **BLOCK**
      *Only waiver:* both websites broken, which lifts the floor but never the ceiling.
- [ ] Every mention of a candidate reads **"Website A"** or **"Website B"** in full.
      No bare letters, no "the first one", no "the other site". **BLOCK**
- [ ] Each reason opens by stating its own outcome, and that opening **matches the
      option selected in that same question**. **BLOCK**
- [ ] No text is reused across the three fields — not a sentence, not a clause. **BLOCK**
- [ ] Third person throughout; no mention of the browser, the tabs, or the platform.
      *Only waiver:* stating that a site had to be inspected from the preview because
      its tab did not load.

## Pass 2 — Lens purity (each failure is a scored **2**)

- [ ] The aesthetics reason contains **nothing** about controls, features, links, forms,
      loading, or whether anything works. **BLOCK**
- [ ] The functionality reason contains **nothing** about color, fonts, spacing, layout,
      or beauty. **BLOCK**
- [ ] Category labels are absent from all three bodies — no "aesthetics",
      "functionality", "visual quality", "usability" used as a label.
- [ ] Breakage described in the aesthetics reason, if any, is phrased as a **visual
      absence** ("an empty viewport with nothing to assess"), never as a behavioral
      failure ("fails to load", "throws an error").

## Pass 3 — The verdicts

- [ ] Each question was decided on its own criteria, not inherited from another.
- [ ] If all three match, there is a stated reason why that is earned rather than habit.
- [ ] Any "Both" option survives the tie test: **you genuinely cannot argue either
      side.** If you can build a case for one, change it to A or B. **BLOCK**
- [ ] A "Both" verdict's reason is **balanced** — it does not list more faults for one
      site, and no sentence in it names a winner ("more complete", "clearer",
      "less broken"). **BLOCK**
- [ ] Where one site is broken, the working site won all three questions.
- [ ] No side was rewarded for the sheer *number* of features over actual fulfillment of
      the request.
- [ ] The overall reason **shows the weighing**. If it only argues looks, or only
      argues behavior, or restates another field, it is not answering the question.
      **BLOCK**

## Pass 4 — The factual audit (a failure here is the most serious defect there is)

Go back to both tabs. This pass is what separates a real submission from a plausible one.

- [ ] Every section, control and failure named in a reason **exists in the website it is
      attributed to**. Verify each claim individually against the page. **BLOCK**
- [ ] No failure is **swapped** between the two sites. **BLOCK**
- [ ] Nothing important was missed — a requested section that is absent, or a control
      that does nothing, that the reasons never mention.
- [ ] Both websites are described in each reason, not only the winner.
- [ ] Every claim is concrete enough that a reviewer could go and verify it. Replace any
      claim you could not point at on screen.

---

## Self-score

Score the submission honestly on the reviewer's scale, then act on it.

| Score | Meaning | Action |
|---|---|---|
| **1** | Fields empty or nonsense; reasons unrelated to the sites; inspection not really done. | Redo the task. |
| **2** | Any Pass 1, Pass 2 or Pass 4 **BLOCK** is live, or a wrong website was chosen. | Fix, then re-run this gate from Pass 1. |
| **3** | Several minor problems, or one that noticeably weakens a justification — something important unmentioned, a detail described inaccurately — options still correct. | Fix before submitting; it is cheap now and costs a point later. |
| **4** | One small problem affecting neither the outcome nor the strength of the reasoning. | Fix if time remains, otherwise ship. |
| **5** | Three right options; three reasons accurate, complete, in-lens, in-range. | Ship. |

**Self-scoring honestly is the whole point.** A gate that always returns 5 is not a
gate. If a pass produced no findings at all, re-read the two reasons you wrote fastest —
that is where the finding usually is.

---

## Reviewing someone else's task

Same passes, plus the rules that govern the reviewer rather than the work:

- **Re-do the inspection first.** Chrome, both tabs, full scroll, every control. A review
  written from the reasons alone cannot tell a correct claim from an invented one, and
  telling them apart is the entire contribution.
- **Never dock for taste.** Not because you find one site prettier, not because you would
  have worded it differently. Only for something verifiable: a claim that does not match
  the sites, a rule broken, or an option the evidence does not support. A defensible call
  stands even against your own preference.
- **Extra restraint on the overall question.** Two people can weigh the same trade-off
  differently and both be right. Challenge it only when it contradicts the attempter's
  own evidence, or when its reason never explains the weighing at all.
- **Any score below 5 needs three things in the feedback:** which field, what exactly is
  wrong, and what it should have said or chosen instead. "The task had errors" teaches
  nothing and wastes the review.
