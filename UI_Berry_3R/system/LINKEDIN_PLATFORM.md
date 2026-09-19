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

---

## 8. Background tabs throttle, and that looks exactly like a dead control

**Found 2026-09-19 across tasks 6195071 and 6201100.** Two separate failures, same cause:

- `Start annotation` on LinkedIn did nothing while its tab was in the background.
- Feather's `Mark as complete` menu stayed at `opacity: 0` forever, so the settle poll timed
  out and the click landed on a transparent element.

**Always `page.bringToFront()` before driving a tab**, and run the opacity poll *inside*
`page.evaluate` so it measures the real animation rather than a throttled one.

```js
await page.bringToFront();
await page.waitForTimeout(1500);
// ... then open the menu and poll in-page for opacity === '1'
```

Symptom to recognise: a control that works when you watch it and fails when you do not.

## 9. Which invocation each control needs

Not every button takes the same treatment. Check `type` and whether it sits in a `<form>`:

| Control | Works with |
|---|---|
| LinkedIn `Submit` | `form.requestSubmit(button)` — `type="submit"` inside a form |
| LinkedIn `Start annotation`, `Save` | React `onClick` — `type="button"`, no form |
| LinkedIn `Claim task` | real mouse click at `right - 14` (the caret) |
| Feather status pill | React `onClick` |
| Feather menu items | real mouse click **after** polling `opacity === '1'` |
| Feather rating toggles | React `onChange(evt, label)`, one group at a time |

Reading `b.type` and `b.closest('form')` first is cheaper than guessing.

---

## 10. The Claim dropdown portal never renders. Invoke the item onClick instead.

**Corrected 2026-09-19 ~16:10 IST. The earlier note in this slot was wrong** — it read the
dropdown as empty and concluded the pool was dry. It was not. Supply was there the whole time and
a claim succeeded the moment the handler was called directly.

What is actually true: `Claim task` is an `ant-dropdown-trigger`, and **no `.ant-dropdown`
element is ever added to the DOM** — not on caret click, not on centre click, not on
`click({force:true})`, not on hover. `document.querySelectorAll('.ant-dropdown').length` stays
`0`, and **zero network requests fire**, so the handler is never reached. Nothing settles later;
waiting does not help.

The items exist in the React tree the whole time. Walk the fiber from the button up to the
`memoizedProps.menu` and both are there, each carrying its own `onClick`:

```js
// in page.evaluate
const b = document.querySelector('button.ant-dropdown-trigger');
const key = Object.keys(b).find(k => k.startsWith('__reactFiber$'));
let f = b[key], menu = null, hops = 0;
while (f && hops < 25) {
  const p = f.memoizedProps;
  if (p && p.menu && Array.isArray(p.menu.items)) { menu = p.menu; break; }
  f = f.return; hops++;
}
// menu.items -> [{key:'ANNOTATION', label:'Annotation', onClick:fn},
//                {key:'VALIDATION', label:'Review',     onClick:fn}]
menu.items.find(i => i.key === 'ANNOTATION')
  .onClick({ key:'ANNOTATION', domEvent:{ stopPropagation(){}, preventDefault(){} } });
```

Note the menu takes **no `onClick` of its own** (`menu.onClick` is `undefined`) — the handler is
per item, so calling it on the menu does nothing. The synthetic `domEvent` stub is required;
Ant calls `stopPropagation` on it.

That fires `POST /ai-trainer/api/frontendAnnotationTaskResults?action=claimResults`, which
answers `{"value":{"approvedIds":[<workItemId>],"rejections":[]}}`, and a
`Claimed task #<id>` toast appears. The follow-up
`GET ...?q=annotator&...&pipelineId=<batchId>` returns the new row, and its `inputData` field
carries the **Feather URL as JSON** — read the link from there rather than from the table:

```
inputData: {"link":"https://msft.feather-prod.azure.com/tasks/<uuid>","title":"Website comparison","count":"1"}
```

**Read `rejections` before celebrating.** A non-empty `rejections` array with an empty
`approvedIds` is the real "pool is dry" signal, and it is the only trustworthy one. An absent
dropdown says nothing about supply either way.

---

## 11. A claimed task can carry a dead Feather link. Verify before Start annotation.

**Seen 2026-09-19, task 6208115 / work item 7586230.** The claim succeeded normally
(`approvedIds:[7586230]`, `rejections:[]`, toast `Claimed task #7586230`) and the detail page
showed an Attempt URL as usual. That URL answered **"Task not found for the provided ID"** —
retried three times over about fifteen seconds, identical each time. The task was unworkable.

**This is the whole reason the verify-before-start rule exists.** Because `Start annotation` had
not been pressed, `Skip` was still available and the task was dropped at no cost. Had the order
been reversed, dropping it would have needed a Feather release plus a Slack post to a QM.

### Skipping, in practice

`Skip` opens an Ant modal headed **"Skip task"**, warning that *skips are limited and tracked* and
that *skipped results will not be reclaimable*. A **Reason is required**, max 50 characters. State
the fact plainly, for example `Feather link returns Task not found`.

Two mechanics worth knowing:

- Type the reason with a CDP `Input.insertText` after focusing the field. The character counter
  (`n / 50`) confirms React saw it.
- **`elementHandle.click()` on the modal's Skip button times out** waiting for the element to be
  "stable" — the modal is still animating. Fire the React `onClick` instead, exactly as for the
  other Ant controls on this platform. Success shows `Task skipped successfully!` and returns to
  the task list.


### Dead Feather links are not rare: two in fourteen claims

Second occurrence 2026-09-19, task 6204073 / work item 7589237. Same signature as 6208115: the
claim succeeds, the detail page shows an Attempt URL, and that URL answers **"Task not found"**
on every load. Roughly **one claim in seven** on this batch. Budget for it and always verify
before `Start annotation`.

**Beware the blank-page false negative.** A retry loop that tests `notFound` on a page that has
not rendered yet returns `notFound: false` with `innerText.length === 0`, which reads as "the
link recovered". It has not. Wait for `document.body.innerText.length > 100` **before** testing,
and treat any read on a zero-length body as no reading at all:

```js
for (let i = 0; i < 20; i++) {
  await page.waitForTimeout(1500);
  const s = await page.evaluate(() => ({
    len: document.body.innerText.length,
    nf: /Task not found/i.test(document.body.innerText),
  }));
  if (s.len > 100) return s;   // only now is nf meaningful
}
```

**Skip in one call.** Fire the Skip button's React `onClick`, set the reason with the native
value setter plus an `input` event (not `Input.insertText`, which needs focus the animating modal
will not give), then fire the modal's own Skip `onClick`. Check `b.disabled` before firing so a
rejected reason is reported rather than silently swallowed. Success shows
`Task skipped successfully!` and returns to the task list.


## 12. A silent claim means HTTP 409, not an empty pool

**Seen 2026-09-19 after fifteen submits.** The Annotation item's `onClick` fired, no toast
appeared, and the obvious reading was that supply had run out. It had not:

```
409 :: {"message":"Cannot claim new task results while having unfinished task results","status":409}
```

**One task may be held at a time.** A previous claim had succeeded while its toast was missed, so
that task sat at `Pending attempt / Not started` and blocked every further claim. Nothing was
lost: its `Start annotation` was still available and it became the next task.

**Never read a missing toast as a dry pool.** Attach a response listener to `claimResults` and
read the status:

| Status | Meaning |
|---|---|
| `200` with `approvedIds:[...]` | claimed, id in the array |
| `200` with empty `approvedIds` and a non-empty `rejections` | genuinely nothing claimable |
| `409` | **an unfinished task is already held** — find it and work it |

On a 409, open `/ai-trainer/tasks` **unfiltered** and look for the row whose Work status is not
`Submitted`. The project-filtered view can lag and may not show it.

---

## §13 — The task detail route, and why the list has no buttons (2026-09-19)

The task list at `/ai-trainer/tasks` (filtered or unfiltered) renders **nine columns and zero
controls**. There is no Start annotation button on a row, no hover action, no hidden tenth
column, no expander. Hovering, clicking the Task ID cell and widening the table all find
nothing, because nothing is there.

**Every per-task action lives on its own detail page:**

```
https://www.linkedin.com/ai-trainer/tasks/<WORK_ITEM_ID>
```

Note **work item ID**, not Task ID. Passing the Task ID returns
`Annotation task result not found for id=` — which is a useful confirmation that the route
shape is right and only the identifier is wrong.

That page carries: the countdown, **Start annotation**, **Skip**, the **Attempt URL** field,
Save and Submit. Go straight there after a claim instead of hunting the list.

## §14 — Submit is `type="submit"`; a synthetic onClick does nothing at all

LinkedIn's Save and Submit both sit inside a `<form>`. Submit is `type="submit"`.

- Invoking `props.onClick` fires **zero network requests**. No error, no toast, and
  `Last modified` still updates from unrelated re-renders, so it looks like it worked.
- A real pointer click fires only a **GET** re-fetch, not the POST.
- The only thing that commits is:

```js
const b = [...document.querySelectorAll('button')].find(x => x.innerText.trim() === 'Submit');
b.closest('form').requestSubmit(b);   // -> POST .../frontendAnnotationTaskResults/<id> 202
```

**Always confirm with a response hook, never the UI.** A success is `POST ... 202`. Then check
the row reads `Submitted`; `In progress` after a submit attempt means it did not commit.

## §15 — The Attempt URL is required, empty, and must be the CLAIMED task URL

The detail page *displays* the original Attempt URL as body text, but the input
`#ATTEMPT_URL-link-single` is **empty** and the template marks it `"required": true`.
While it is empty, Submit silently refuses — no validation message is shown.

Two traps:

1. **Claiming on Feather mints a NEW task id.** The page navigates from
   `/tasks/<original>` to `/tasks/<claimed>`. The claimed one is what belongs in the field.
   Confirmed in the POST response: `{"ATTEMPT_URL":"...<claimed>"}` alongside the untouched
   `inputData.link` holding the original.
2. **`Input.insertText` alone does not populate it.** It is a controlled React input; the
   keystrokes show in `.value` but React's state never updates, so Save fires no request and
   the value reverts on reload. Use the native setter, then dispatch `input` and `change`:

```js
const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;
setter.call(input, claimedUrl);
input.dispatchEvent(new Event('input',{bubbles:true}));
input.dispatchEvent(new Event('change',{bubbles:true}));
```

`requestSubmit` then carries it. Save is not needed separately.

## §16 — The three claim status codes, and how to tell them apart

Always read the status from a response hook on `?action=claimResults`. The toast is
unreliable and all three of these look identical in the UI: nothing happens.

| Status | Body | Meaning | What to do |
|---|---|---|---|
| **200** | `{"value":{"approvedIds":[<id>],...}}` | Claimed. `<id>` is the **work item ID**. | Go to `/ai-trainer/tasks/<id>` |
| **409** | `Cannot claim new task results while having unfinished task results` | An earlier claim succeeded and its toast was missed. **One task at a time.** | Find the row whose Work status is not `Submitted` and finish it |
| **404** | `No claimable task results available in pipeline` | The dispatcher pool is genuinely empty. | Wait and retry; nothing is wrong |

**404 is the only true "no work" answer.** Confirmed 2026-09-19 after task 6206089: four
attempts across about forty seconds all returned 404, while every row in My tasks read
`Submitted`, so nothing was held.

**Feather's count does not predict LinkedIn's.** At that same moment Feather's unclaimed
list still showed **24** tasks in the batch. Those are not dispatchable until the LinkedIn
pipeline offers them, so a healthy Feather pool alongside a 404 is normal and is not a fault
to investigate. Do **not** claim directly in Feather to get around it: claiming in Feather
without a LinkedIn claim breaks the required sequence.
