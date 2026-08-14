# WORKFLOW: CLAIM_TASK — the billable claim sequence

> **"Only correctly claimed tasks are billable — follow every step, no exceptions."**
> **"Skipping one step = task will not be paid. No exceptions."**
> — headings of the claim flowchart (guidelines, image16)

Steps 4 and 5 below **do not appear in the written Steps 1–7 of the guidelines (GL:367–435)**.
They exist only inside that flowchart image — and all four Operational Workflow screening
questions test them. Reading only the prose produces unpaid work.

---

## The invariant

> **Always start in Vercel, then go to Feather. Never work in Feather alone. Never work only in
> Vercel.** (GL:23–25, repeated GL:359–361)

- **Vercel** — Data Annotation Platform — https://annotation-platform-henna.vercel.app/
- **Feather** — where prompts are written and responses chosen — https://msft.feather-prod.azure.com/
  (log in with **"Log In with LinkedIn"**)

---

## The sequence

1. **[Vercel]** Click the task link in the **task Variables** panel.
2. **[Feather]** The link opens the task. It **must show "Unclaimed"**.
3. **[Feather]** **Claim the task.** **Confirm the status changes to "In progress"** before doing
   anything else.
4. **[Feather] — CRITICAL** — **Copy the full browser URL from the address bar.**
   ⚠️ **Only after claiming.** The URL changes on claim; a URL copied before claiming is stale
   and the task will not register.
5. **[Vercel]** **Paste it into the field named `Attempt URL`.** It **cannot be edited
   afterwards** — check it before committing.
6. **[Feather]** Begin annotating. The task is now billable.

**One sentence:** *Vercel link → open in Feather → claim in Feather → confirm "In progress" →
copy the browser URL → paste into `Attempt URL` in Vercel → annotate in Feather.*

### Why the order is non-negotiable

Vercel and Feather are separate systems. That pasted URL is the **join key** binding the
conversation record to the billable task record. No key → orphaned data → cannot be attributed
→ cannot be paid or ingested.

Distractor answers the screening rejects: that there's a time limit after claiming · that
Feather deletes tasks on a bad URL · that anything must be claimed twice. None of those. It is
purely about registration and billing eligibility.

---

## Before the first claim ever

- [ ] LinkedIn **primary** email == the email the invitation was sent to
      (fix at https://www.linkedin.com/mypreferences/d/manage-email-addresses)
- [ ] Vercel email == Feather email == Slack email — identical across all three
- [ ] Onboarding session attended (required for project access)
- [ ] Feather login via LinkedIn tested
- [ ] Topic prepared per `../knowledge/TOPIC_PLAYBOOK.md` §6 — **the clock starts on claim**

---

## "Task not found" in Feather

**What it means:** the task is no longer available to anyone — its claims are exhausted. Not a
bug on your end, not recoverable.

**Do:** release the dead task on the Vercel side and click **Start Tasking** again for a new
assignment. *Every task must be re-entered through Vercel.*

**Do NOT:**
- Cancel the task
- Escalate it to notify the client
- Go hunting for an unclaimed task **directly in Feather** and paste its URL into the original
  Vercel task's `Attempt URL` — this is the trap answer. It looks resourceful and it is a
  data-integrity violation: it binds one Vercel record to an unrelated Feather conversation.

---

## Submitting and releasing

**Submit:** Feather → **Mark as Complete**, then Vercel → **Submit Task**.

**Release:** release in **Feather first**, verify the release took, then release in Vercel. If it
was never claimed in Feather, just release in Vercel.

**Never** use **Cancel task**, **Escalate Issue**, or **Decline** (GL:419).

---

## Payment eligibility (GL:460–475)

Two independent conditions, **both** required:

1. Correct registration via the complete operational process above, **and**
2. All applicable quality requirements met.

Plus: no skipped steps · all required fields completed · a preference selected on every
applicable turn · all Project Team spreadsheets completed.
