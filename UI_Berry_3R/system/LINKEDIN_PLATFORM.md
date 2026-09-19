# LinkedIn AI Trainer — the claim and submit runbook

**Written 2026-09-19 from `OB ATT DAS.mp4` + `transcript_linkedin_platform.md`, and verified
end to end on task #6210077 the same day.** This replaces the Vercel dispatcher described in
`SESSION_HANDOFF.md`.

---

## 0. The one thing that goes wrong

**Feather is claimed BEFORE LinkedIn is started.** Not the other way round.

The moment `Start annotation` is pressed on LinkedIn, the Skip button vanishes and cannot come
back. If the Feather task turns out to be dead, broken, or already taken, you are stuck with it:
recovering needs a Feather release *and* a Slack post quoting the task number so a QM removes it
by hand. Verify first, commit second.

---

## 1. Where the work is

```
https://www.linkedin.com/ai-trainer/tasks?projectId=1253002&batchId=p-1875002&page=1
```

Pre-filtered to project **UI Berry**, batch **DA0518 5p6 vs opus5high multitab 3-question**.
Reaching it by hand: left nav → checklist icon → `My tasks` → `All projects` → UI Berry →
`All batches` → DA0518.

**Pick the batch without the pause symbol.** A paused batch answers every claim with "no
available tasks". The video calls this out at 00:41.

### Reading the table

| Column | Meaning |
|---|---|
| Task ID | the LinkedIn work record, e.g. `6210077`. Quote this to Slack when asking for a removal. |
| Work item ID | the path segment for the detail page: `/ai-trainer/tasks/<workItemId>`. **Not the Task ID.** |
| Work status | `Not started` / `In progress` / `Submitted` |
| Task stage | `Pending attempt` → `In progress` → `Pending review` → `Reviewed` → `Ready for delivery` |

The task to work is the row reading **In progress**.

---

## 2. The sequence

1. **LinkedIn** → `Claim task` ▾ → `Annotation`. (Reviewers also see `Review`.)
   Task becomes *Pending attempt*, **24h timer** starts.
2. Open the detail page. Note the **Attempt URL** box on the right.
3. **Stop. Do not press `Start annotation`.**
4. **Feather** → open the task → status pill → `Claim task`.
   Confirm it is real: no "Task not found", and both Website A and Website B load.
5. Back to **LinkedIn** → `Start annotation`. *Skip is now gone forever.*
6. Copy the live Feather task URL into **Attempt URL** → `Save`.
7. Do the evaluation in Feather. Mark complete there first.
8. Return to LinkedIn → `Submit`.

### First task only
After your first submission you cannot claim another until a reviewer has reviewed it. Expect an
error on the next claim. This gate applies once, not every time.

---

## 3. Feather login from a fresh browser profile

Feather offers Microsoft / GitHub / **LinkedIn**. Use LinkedIn — same account, same email.
If the LinkedIn session is already live the OAuth round-trip completes unattended; a
`/uas/login` screen flashing past on the way to `/callback` is normal, not a failure.

---

## 4. Submitting on Feather — the mechanics that actually work

There is **no Submit button** on the Feather form. Submission is the status pill.

1. The pill `In progress` opens its menu only via its React `onClick`. A genuine mouse click on
   the pill does nothing.
2. The menu is a **MUI Popover rendered into a portal**. Its `.MuiPaper-root` starts at
   `opacity: 0` and animates in. **Clicking the item while the paper is still transparent is
   silently swallowed.** Poll until `getComputedStyle(paper).opacity === '1'` (roughly 2s), then
   click `li.MuiMenuItem-root` at its real coordinates.
3. Menu: `Mark as complete` · `Cancel task` · `Escalate issue` · `Release task` · `Decline`.
4. **A "Confirm Submission" dialog now appears** — "Are you sure you want to submit this task?"
   with `Cancel` and `Submit Task`. Click `Submit Task`.
5. The tab redirects itself to the campaign page. **That is success, not a failure.** Do not
   re-click. Reload the task URL: it should read `Completed` with all six fields `readOnly`.

> Earlier notes said Mark as complete submits with no confirm dialog. That is no longer true.

## 5. Submitting on LinkedIn

> ### ⚠️ The Submit button ignores clicks. Use `form.requestSubmit()`.
> **Found 2026-09-19 on task 6194086, after four real pointer clicks and a React `onClick`
> all did nothing — no network request, no error, no toast, status stuck on In progress.**
>
> The button is Ant Design, `type="submit"`, and lives inside a `<form>`. Clicking it (even
> with `page.mouse.down/up` at the rect centre) and calling its React `onClick` both fail
> silently. What works is asking the form itself to submit:
>
> ```js
> const b = [...document.querySelectorAll('button')].find(x => x.innerText.trim() === 'Submit');
> const f = b.closest('form');
> f.requestSubmit(b);          // passes the submitter, so the right handler runs
> ```
>
> Success signals, all three together: `POST /ai-trainer/api/frontendAnnotationTaskResults/<id>`,
> an **HTTP 202**, and a redirect to `/ai-trainer/tasks`. The row then reads
> `Pending review · Submitted`.
>
> **Do not keep clicking.** A click that produces no network request at all is this bug, not a
> missed target. Check the row on the task list before concluding anything.



`Submit` commits **immediately, with no confirm dialog**, and redirects to `/ai-trainer/tasks`.
The row then reads `Pending review · Submitted`. Verify there before calling it done.

---

## 6. Skipping, and why it has to be early

- `Skip` exists only while the task is *Not started*, and asks for a reason.
- After `Start annotation` it is gone.
- To drop one after that: release on Feather, then post in Slack with the **Task ID** and ask for
  it to be removed. You cannot do it yourself.

---

## 7. Claiming the next task — the caret, not the button

The `Claim task` control is one Ant button carrying `ant-dropdown-trigger`. Clicking its centre
does nothing visible. **Click ~14px inside its right edge** (the chevron zone) and the menu opens
with `Annotation` and `Review`.

```js
const el = [...document.querySelectorAll('button')].find(x => /Claim task/i.test(x.innerText));
const r  = el.getBoundingClientRect();
await page.mouse.click(r.right - 14, r.y + r.height / 2);   // caret, not centre
```

Then click `Annotation`. The new row appears as *Pending attempt · Not started* with a 24h timer.

**Read coordinates fresh every time.** Cached rects go stale after a navigation and send clicks
into empty space, which looks exactly like a dead control.
