---
name: mt-attempt-url-hidden-step
description: "The billing-critical \"copy Feather URL after claiming, paste as Attempt URL in Vercel\" step appears only inside a flowchart image, not in the prose"
metadata: 
  node_type: memory
  type: project
  originSessionId: 245c96c2-20a4-4909-b2a6-fe539a64b62a
  modified: 2026-08-13T19:25:49.935Z
---

The MAI guidelines' written claim procedure (Steps 1–7, lines 367–435) **omits** two steps that
the final flowchart image marks as critical to billing: after claiming the task in Feather,
**copy the full browser URL from the address bar — only after claiming, because the URL changes
on claim — then paste it into the Attempt URL field back on the Vercel Data Annotation
Platform** (it cannot be edited afterwards). The flowchart states "Skipping one step = task will
not be paid. No exceptions."

**Confirmed by the official screening.** All four Operational Workflow quiz questions test this
one sequence. The Vercel field is literally named **`Attempt URL`**. You must also confirm the
Feather status changes to **"In progress"** before copying. Two distractor answers to avoid:
copying the URL *before* claiming, and — if you hit "Task not found" — sourcing a replacement
task directly from Feather instead of going back to Vercel (that screen means the task's claims
are exhausted; always re-enter through Vercel).

**Why:** Vercel and Feather are separate systems and that URL is the join key binding the
conversation record to the billable task record. Anyone reading only the prose produces unpaid
work and fails the screening.

**How to apply:** Always include these steps when describing the claim flow. The flowchart was
embedded as base64 in the .md, so it is invisible to text search/grep — the extracted PNGs are in
the session scratchpad, and the reconciled flow is in PROJECT_KNOWLEDGE.md §10.2. Part of
[[interactive-preference-multiturn]].
