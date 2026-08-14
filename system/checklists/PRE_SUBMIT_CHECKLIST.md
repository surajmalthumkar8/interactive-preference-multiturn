# PRE-SUBMIT CHECKLIST

Run every line before **Mark as Complete** in Feather. Nothing here is optional; each item maps
to a scored dimension, a removal trigger, or a payment condition.

---

## A. Turn structure

- [ ] User turns are **≥10 and ≤15** (opening prompt is Turn 1)
- [ ] No turn exists only to reach the count — every turn refines, constrains, challenges, or
      takes the next step
- [ ] Every turn quotes or pinpoints something specific in the previous response
- [ ] No turn could have been written without reading the previous response
- [ ] The conversation does not end on "thanks / ok / that's all"
- [ ] The last turn is a small narrowing ask, not a sign-off

## B. Capability alignment

- [ ] No turn asks the model to search, browse, open a URL, or look anything up
- [ ] No turn depends on real-time or current information
- [ ] No turn references an attached, uploaded, or shared file
- [ ] No turn asks for or refers to an image, screenshot, diagram, or chart
- [ ] Nothing depends on facts from **after July 2025**
- [ ] All referenced material is **pasted in full**, never pointed at, never `[placeholder]`

## C. Authenticity

- [ ] Every turn was run through the `humanizer` skill
- [ ] Voice matches `../knowledge/HUMAN_VOICE_CORPUS.md` — no em dashes, no semicolons, no
      bullets I authored, no "delve/moreover/furthermore", no thanks or greetings
- [ ] Register is consistent within each turn (not mixing careless and careful)
- [ ] Rhythm, opener shape, and imperfection patterns **vary across turns**
- [ ] Nothing in this task duplicates or paraphrases a previous task
      (checked against `../learning/PROMPT_LOG.md`)
- [ ] This task rotates on ≥3 axes vs. the previous task (domain, shape, register, length band)
- [ ] Every turn was **typed** into Feather, not pasted

## D. Safety

- [ ] No real names, emails, phone numbers, or addresses
- [ ] No employer names, client names, or account/credential data
- [ ] No confidential or NDA material
- [ ] No sensitive personal data (health, financial, biometric, political)
- [ ] Pasted content re-read end to end specifically for identifiers

## E. Preference selections

- [ ] **Both responses read in full on every single turn**
- [ ] A preference recorded on **every applicable turn**
- [ ] `↳` visible on the chosen side for every turn (`↳A B` or `A ↳B`)
- [ ] **No turn shows the green "Continue conversation from here" button** — scan all of them
- [ ] Picks are not streaking to one side without cause
- [ ] Any reason text is specific, casual, and not templated across turns

## F. Operational — the billable sequence

- [ ] Task was entered from **Vercel**, never claimed directly in Feather
- [ ] Feather status showed **"In progress"** after claiming
- [ ] Full Feather browser URL was copied **after** claiming
- [ ] URL pasted into the **`Attempt URL`** field in Vercel
- [ ] All required Vercel fields completed
- [ ] Any Project Team spreadsheet updated — enabled contributor columns only, no filters, no
      structural edits

## G. Submit order

1. Feather → **Mark as Complete**
2. Vercel → **Submit Task**

Never use **Cancel task**, **Escalate Issue**, or **Decline**.

To release instead: release in **Feather first**, verify it, then release in Vercel.

---

## After submitting

- [ ] `PROMPT_LOG.md` updated — domain, shape, register, length band, turn count, opener
- [ ] Session state file closed out in `sessions/`
- [ ] Anything learned written into `LESSONS.md`
- [ ] `git add . && git commit && git push` so the other laptop is in sync
