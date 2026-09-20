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

## §17 — A Feather task page can permanently wedge every renderer that loads it

Seen 2026-09-19 on task 6203060 (Feather task `7154eef4`). After the three textareas were
filled and each read back at its exact expected length, a `location.reload()` left the page
unresponsive to CDP: `Runtime.evaluate` timed out on `document.readyState` and even on `1+1`,
and `DOM.enable` timed out too, so the renderer process itself was blocked rather than the
evaluate channel.

**It is the page, not the browser, and not the candidate sites.** Reproduced four times:

| Attempt | Result |
|---|---|
| Reload the task tab | wedged |
| Close it, open the same URL in a brand-new tab | wedged |
| Close every other tab first, then open it | wedged |
| SPA-route a *healthy, responsive* campaign tab to it with `history.pushState` | that tab wedged too |

Throughout all four, the LinkedIn tab in the same browser answered `1+1` instantly. The two
candidate sites (full-screen animating canvases) were closed before attempts three and four,
so they were not the cause.

**What survives the hang:**

- **The reason fields and the verdicts are saved.** They were written and verified before the
  reload, and Feather persists on change, not on submit.
- **The Feather claim and the LinkedIn 24h timer both survive.** Nothing is forfeited.
- **`t<N>_final.json` on disk is the recovery copy.** Everything can be refilled from it.

**What to do:**

1. Do not kill Chrome. The profile is pinned and hardened and a restart costs the session.
2. Do not re-open the task repeatedly. Each attempt wedges another renderer.
3. Leave it and come back later, or finish it in a fresh browser session. The submit chain
   (status pill → Mark as complete → Submit Task) is all that remains.
4. If it is still wedged when the 24h timer runs low, escalate with the Task ID rather than
   letting the claim expire.

**Prevention:** the hard reload before submit exists to catch the empty-textarea trap (§NOTE).
That trap is real and cost a resubmit on task 6191089. But on a heavy task the reload is what
triggers this. Prefer verifying each field's length immediately after writing it, and treat
the reload as optional insurance rather than a required step.

### 17a — correction: Feather is fine, one task page is not, and the wedge blocks the whole loop

Three findings on 2026-09-19 that change §17 materially.

**Feather itself never went down.** With the task tab closed, `https://msft.feather-prod.azure.com/`
loaded to `/?tab=toDo` and rendered normally: `readyState complete`, full text, a live campaign
filter, and the counts `To do (1) / Awaiting response (0) / Done (81)`. The claimed task was listed
there as **Finish incomplete task — Website comparison**, linking to
`/tasks/7154eef4-…`. So the server, the session and the claim are all healthy. **Diagnose Feather
by loading the root, never by reloading the task page** — the task page is the one thing that hangs,
so using it as the probe makes a working service look dead.

**It is the page, not the navigation path.** §17 recorded four cold loads. A fifth route was tried:
a real pointer click on the task's link *from the healthy To Do page*, as an in-app SPA navigation.
The tab navigated (title became "Website comparison") and the renderer wedged exactly as before.
Cold load and warm SPA route both wedge, which rules out the load path and leaves the task page's
own render.

**The renderer is busy, not dead.** `/json/list` keeps reporting the tab with the correct URL and
the correct title throughout, so navigation and the browser process are fine. Only the renderer
stops answering CDP — consistent with a synchronous loop in page script, not a crash.

**Why this is urgent rather than something to defer.** §17 said to leave it and pick up another
task. That is wrong, and the reason is §16: claiming again returns

```
409 {"message":"Cannot claim new task results while having unfinished task results"}
```

**One unfinished task blocks every future claim.** A wedged task page is therefore not a
single-task problem to work around; it stops the loop dead until it is resolved. Fix it first, and
if it cannot be fixed, escalate immediately rather than waiting on the 24h timer.

**What is still true from §17:** the fields and verdicts are saved server-side, the claim and the
timer survive, `t<N>_final.json` is the recovery copy, and only the submit chain remains.

### 17b — the GraphQL API is reachable when the task page is not

Feather's data layer is a batched GraphQL endpoint at **`POST /api/graphql`**, plus REST under
`/api/v2/`. From **any healthy Feather tab** (the root `/?tab=toDo` renders fine) these can be
called with `credentials:'include'` and the session cookie authenticates normally. This gives a
way to read and change task state while the task's own page is unrenderable.

**Capturing the real queries.** A `window.fetch` hook installed by `Runtime.evaluate` is wiped by
the next navigation. Install it through CDP instead so it survives:

```python
raw('Page.enable', {})
raw('Page.addScriptToEvaluateOnNewDocument', {'source': open('gqlhook.js').read()})
raw('Page.navigate', {'url': 'https://msft.feather-prod.azure.com/?tab=toDo'})
```

**Introspection is disabled**, but the errors are verbose and name the valid field on a miss
("Did you mean 'updateTaskStatus'?", "Did you mean 'completedAt'?"), so the schema can be walked
one deliberate wrong guess at a time. Enum values are the exception: a bad `TaskStatus` reports
only that the value does not exist, without listing the alternatives.

**What was established for this campaign:**

| | |
|---|---|
| my todo query | `userTaskTodos(params:{completed:false}, pagination:{page:0,pageSize:N})` |
| task fields that exist | `task(id: UUID!) { id title workflowStatus }`, concrete type `WidgetLayoutTask` |
| unfinished task | `workflowStatus: "IN_PROGRESS"`, one todo `type: "STATUS_TRANSITION"`, `completedAt: null` |
| finished task | `workflowStatus: "SIGNED_OFF"`, same todo carrying a `completedAt` timestamp |
| the submit mutation | `updateTaskStatus(taskId: UUID!, status: TaskStatus!)` |

So **`SIGNED_OFF` is the end state**, confirmed against 81 of my own completed tasks rather than
guessed from the button label.

**Two cautions learned here:**

- **`POST /api/v2/tasks/search` ignores a `task_ids` filter** and returns the whole campaign —
  47,637 rows including other trainers' claims and their anonymized handles. Do not use it to look
  up one task. `userTaskTodos` returns only your own and is the right query.
- **`/api/tasks/<id>` and `/api/v2/tasks/<id>/...` are not APIs.** They return the SPA shell with
  `200 text/html`, so a naive check reads as success. Always look at `content-type` before
  treating a 200 as data.

### 17c — SOLVED: the wedge is Three.js/WebGL in the embedded candidates, and the fix is one hook

**Root cause, finally measured.** Attaching `Runtime.enable` + `Log.enable` to a blank tab *before*
navigating, then collecting console events during the load, produced the answer on the first try:

```
THREE.WARNING: Multiple instances of Three.js being imported.
```

The task page embeds both candidate sites inline. On this task both candidates were **Three.js
WebGL ocean simulations**, so the page ran two duplicated Three.js instances and two WebGL contexts
with continuous `requestAnimationFrame` loops. That saturates the renderer, and CDP never gets a
turn. This is why `DOM.enable` timed out alongside `Runtime.evaluate` — the thread was busy, not
broken.

**The fix — disable WebGL and rAF before any page script runs:**

```js
// noglhook.js, via Page.addScriptToEvaluateOnNewDocument BEFORE Page.navigate
HTMLCanvasElement.prototype.getContext = function(){ return null; };
window.requestAnimationFrame = function(){ return 0; };
```

The page then loaded to `readyState complete` in under 35 seconds, after six consecutive wedges.
Everything was intact: all six textareas (658 / 687 / 651 chars plus three short follow-ups) and
`aria-pressed="true"` on exactly one option per question — B / A / A, as recorded. Nothing had been
lost in any of the six wedges.

**Use it whenever a task's candidates are animation-heavy** — 3D scenes, canvas games, particle
fields. It costs nothing on an ordinary task, since the form itself needs neither WebGL nor rAF.
Judge the candidates in their own standalone tabs, exactly as the protocol already requires; the
hook only ever touches the Feather form page.

**Two corrections to earlier sections.** §17's original guess (the animating ocean canvases) was
right after all, and my §17 rewrite that dismissed it was wrong: attempts 3 and 4 had the candidates
closed in *separate tabs*, but the task page embeds its own copies, so closing those tabs changed
nothing. And §17's "leave it and come back later" is the wrong instruction — the renderer never
recovers on its own, verified over ~6 minutes of spaced probes and six separate loads. Fix it with
the hook instead.

**Verify the submit server-side, not from the pill.** After Submit Task the status pill still read
"In progress" while the server had already recorded `workflowStatus: "COMPLETED"`. Confirm with the
GraphQL `task(id:)` query from a healthy tab (§17b) rather than trusting stale UI.

### 17d — the standing per-task scripts

Built after §17c so the wedge cannot cost time again. All live in the session scratchpad.

| script | does |
|---|---|
| `opentask.py <uuid>` | closes any existing copy, opens the task in a fresh tab with the §17c WebGL/rAF hook installed *before* navigation, waits, reports `readyState` |
| `verify.js` | reads back every textarea length and the `aria-pressed` verdict per question group — run before submitting, never trust memory of what was typed |
| `submitchain.py <uuid>` | pre-submit check, then status pill → Mark as complete → Submit Task, each as a real pointer click |
| `svrstatus.py <uuid>` | the authoritative check: GraphQL `workflowStatus` from a healthy tab, since the pill goes stale (§17c) |

**Order per task:** `opentask.py` → judge the candidates in their own standalone tabs → fill →
`verify.js` → `submitchain.py` → `svrstatus.py` must read `COMPLETED` → then LinkedIn
(`fillurl.js` with the **claimed** uuid, then `lnksubmit.js`, confirm `POST … 202`).

### 18 — batch exhaustion: what a persistent 404 actually means

On 2026-09-19 at ~22:10 the claim endpoint began returning **404 "No claimable task results
available in pipeline"** on every attempt. A Slack notice from the project lead explained it:

> the batch has been completed in the Attempter layer, and we will now continue with the Review
> layer. Therefore, if you see the message "No task available," there is no need to report it.

**So a sustained 404 is a normal end state, not a fault.** §16 records 404 as "genuinely empty
pool"; the addition here is that an empty pool can mean the batch is *finished*, and the right
response is to stop polling rather than to keep retrying or escalate.

**How to tell exhaustion from a lull.** A lull refills within minutes and the campaign keeps an
active batch with claimable work. Exhaustion looks like: every claim 404s over a long window, the
task list shows only submitted rows, and the Feather todo queue is empty
(`userTaskTodos(params:{completed:false})` → `count: 0`). Those three together mean stop.

**Do not reach for other campaigns to keep a task count up.** `allocatedCampaigns` lists seven for
this account and several still have active batches, but they are different projects with different
rubrics and instructions. Claiming into one to keep working is a scope decision for Suraj, not a
way to fill idle time. Also note the claim API cannot be driven directly — a hand-rolled
`POST …?action=claimResults` returns **403 CSRF check failed**; only the in-app dropdown path works.

**Leave the tooling armed.** `claimloop.py` claims on the first 200 and suppresses 404 noise, so it
can be re-armed when the next batch opens without re-deriving anything.

## 19. The DA0518 3-question batch uses a different form component than the 2-question one

Measured 2026-09-20 on task #6197148 (WI 7574351). Four differences that break the
scripts written against the older batch, each one costing a retry:

**19a. The claim pill is not an antd dropdown.** `tools/claim.js` looks for
`button.ant-dropdown-trigger` and returns `NO TRIGGER BUTTON` here. This batch renders a
plain Tailwind button whose text is the status itself (`Unclaimed`), carrying `onClick`
directly in `__reactProps$`. Fire that handler, then click the `Claim task` item in the
MUI menu that opens. The same pill later offers `Mark as complete`.

**19b. There is no Submit button on the page.** Submitting is `status pill -> Mark as
complete`, and that raises a **Confirm Submission** panel with `Cancel` / `Submit Task`.
The panel is **not** a `[role=dialog]` and is invisible to a dialog query; find it from
the `.MuiAlert-message` carrying "Are you sure you want to submit this task?" and walk up
one parent for the buttons. Clicking `Mark as complete` alone leaves the task
`IN_PROGRESS`, which looks exactly like a successful submit if you only read the pill.

**19c. Half the textareas are hidden sizing mirrors.** The form shows three reason fields
but `document.querySelectorAll('textarea')` returns **six**. The odd indices are
zero-height shadow elements holding the single character `x`. The real fields are indices
**0, 2, 4**. Writing to 0,1,2 concatenates two reasons into the first box and leaves the
third empty. Filter on `getBoundingClientRect().height > 0`, or take the even indices, and
always read back `value.length` per field.

**19d. Clicking all three verdict toggles in one pass silently drops the first two.**
A single `forEach(b=>b.click())` over every `A is better` button left only the last group
selected. Set each `.MuiToggleButtonGroup-root` separately via its React `onClick`, with a
pause between, then re-read which buttons carry `Mui-selected` before submitting.

## 20. LinkedIn's printed Attempt URL can name a task id that does not exist

Task #6197148 displayed `.../tasks/a234a8b4-6265-5081-b141-57baa7dd5e2e`. Opening it
served the correct task, but GraphQL answered **`Task a234a8b4... not found` / NOT_FOUND**
for that id, while the tab's own URL had become
`b5c174b6-be37-4895-acc1-35340f732830`, which resolved normally and was the id that
actually went `IN_PROGRESS` and then `COMPLETED`.

So the id in the LinkedIn panel is not reliably the id Feather stores. **Read the real
uuid off the task tab's `location.href` after it settles**, verify it with
`svrstatus.py`, and put *that* uuid into the Attempt URL field on the way out. Filling the
printed one would have logged an attempt URL pointing at a task that does not exist.

## 21. A 200 from updateTaskStatus can still be a rejection, and the pill will not tell you

Measured 2026-09-20 on task #6190171. The submit chain ran clean: pill opened, `Mark as
complete` clicked, `Confirm Submission` appeared, `Submit Task` clicked, no error toast.
`svrstatus.py` still said `IN_PROGRESS`, five attempts running.

Capturing the actual response body showed the real answer. The mutation **did** fire and
the transport **did** return HTTP 200, but the GraphQL envelope carried an error:

```
"message": "Validation error in 42e5dc5f-...: Form data is invalid:
            'overall_scoring_reason' is a required property"
"extensions": {"service_exception_code": "INVALID_ARGUMENT"}
```

So the third reason had **never reached the server** even though the textarea read back
641 characters in the DOM. This is the §17c persistence trap again, with a new symptom:
the field looks filled, the form looks valid, and the only visible signal is that the
status never moves.

**The fix that worked.** Clear through the native setter and fire the events React
listens for, rather than only using `Input.insertText`:

```js
const s = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype,'value').set;
s.call(t, ''); t.dispatchEvent(new Event('input', {bubbles:true}));
t.focus();                       // then CDP Input.insertText
// afterwards:
t.dispatchEvent(new Event('change', {bubbles:true})); t.blur();
```

The `change` + `blur` pair is the part that was missing. Feather commits a reason field on
blur, so a field that is only ever typed into and never blurred stays local to the DOM.

**The diagnostic to reach for.** Do not guess at a silent submit. Enable `Network`, click,
match the `requestWillBeSent` whose `postData` contains `UpdateTaskStatus`, keep its
`requestId`, wait for `loadingFinished`, then call `Network.getResponseBody`. The body
names the exact missing property. This took one run and replaced five blind retries.

**Correction, same day, task 6192184.** The `change` + `blur` pair above was **not
enough**. The identical rejection came back on the overall field, on a task filled by the
patched script. A synthetic `t.focus()` does not give the element real focus, so the
synthetic blur that follows commits nothing.

What actually works, verified end to end:

1. `scrollIntoView` the textarea,
2. **click it with the mouse** (`Input.dispatchMouseEvent`), not `.focus()`,
3. select-all and Delete **as keystrokes** (`Ctrl+A`, `Delete`), not a value setter,
4. `Input.insertText`,
5. **click a neutral spot on the page** to blur it for real.

The whole chain has to go through the input pipeline. Anything that touches `value`
directly leaves React's state and the server's copy out of sync no matter what events are
dispatched afterwards. `fill3q.py` now does all five steps.

**Standing rule.** Never read success from the status pill, and do not read it from the
HTTP status either. Either query `workflowStatus` back with `svrstatus.py`, or read the
mutation body and check for an `errors` key. `submit3q.py` now blurs every field before
submitting for this reason.

---

## 22. The printed uuid can be a task that does not exist at all

Section 20 said LinkedIn's printed Attempt URL can name a uuid that GraphQL reports
`NOT_FOUND`, and that the fix is to read the real uuid from the task tab's settled
`location.href`. Task 7584334 showed a harder version of the same fault, so the
recovery has to be written down.

`opentask3q.py` printed, claimed and started `bdb50685-4320-5b3f-8512-afcb5ecd15c0`,
and reported `REAL uuid ... (SAME)`. The claim, the Start annotation and the whole
evaluation all succeeded against that page. But when the task tab was later closed and
reopened by uuid, `/tasks/bdb50685-...` rendered **"Task not found. This task may not
exist, or you may not have permission to view it."** The LinkedIn task page still
printed `bdb50685` in its link and its body text, so re-reading LinkedIn does not
recover anything.

Note the shape of that uuid: `bdb50685-4320-**5**b3f-...`. The version nibble is **5**,
so it is a name-based (SHA-1) uuid, not the random v4 Feather actually issues. It is a
**derived placeholder**, not a record id. The `(SAME)` check in `opentask3q.py` compares
the printed uuid against the tab href and so cannot catch this: before the redirect
settles, both are the placeholder.

**Recovery, and it is cheap.** Open `https://msft.feather-prod.azure.com/?tab=toDo` and
read the one `/tasks/<uuid>` link on it. A claimed, in-progress task is the only thing in
To Do, so the link is unambiguous. Here it gave
`f423ad11-505a-48c8-bef1-d73f83b4908f`, a real v4 uuid, and that page carried the right
prompt, the right two candidate origins and the six-textarea form. Everything downstream
(`fill3q.py`, `diagsub.py`, `svrstatus.py`, `lnkclose.py`) then worked first try.

**Before filling, confirm identity, never assume it.** Read the prompt text and the two
iframe srcs off the reopened page and check they match the candidates that were actually
judged. Filling a form on the wrong task is unrecoverable once submitted.

**Put the To Do uuid in the Attempt URL field**, not the printed one. `lnkclose.py
7584334 f423ad11-...` returned `POST ... 202`.

### Do not let the candidate tabs outlive the task tab

The reason the task tab had to be reopened at all: opening each candidate in its own tab
(needed, because the task page runs under the nogl hook and canvases must be real to be
judged) left the profile holding 60+ tabs, and the task tab was lost among them. Reopening
is safe, but the fill script finds the task tab by `uuid[:8]`, so a stale tab set makes it
fail with a bare `IndexError`. Close candidate tabs when the evaluation is done.

---

## 23. The second batch, jsd-s60-j40 vs exact 5p6, and how to claim from it

Joaquin's Slack named two batches. Everything up to 2026-09-20 was claimed from
`batchId=p-1868003` (DA0518 rkld-s40 vs opus5high multitab 3-question). The second,
**`batchId=p-1865005`** (`jsd-s60-j40 vs exact 5p6`), is live and was claimable on the
same day, so it is worth checking when the first one runs dry.

**Claiming from a specific batch.** `nextclaim.py` hard-codes the DA0518 batch id in its
URL, so it will never pull from the other one. To claim from `p-1865005`, navigate the
LinkedIn tab to

```
https://www.linkedin.com/ai-trainer/tasks?projectId=1253002&batchId=p-1865005&page=1
```

first, then run `claim.js` against that tab. The batch dropdown reads from the URL, and
the Slack instruction to "select the right batch in the dropdown before claiming" is
satisfied by navigating rather than by touching the dropdown. Verified: the page showed
`My tasks (0)` and "No tasks match the selected filters", the claim put one task in it,
and the row came back tagged with the `jsd-s60-j40 vs exact 5p6` batch.

**The task shape is the same.** Different batch, different task naming
(`Aesthetics/Functionality/Overall Website Preference - 086`, container
`jsd_s60_j40_exact_5p6_20260919`), but the Feather form is identical: six textareas with
only indices 0, 2 and 4 real, the same three toggle groups, the same submit chain. The
whole toolchain ran unchanged, `opentask3q.py` through `fill3q.py`, `diagsub.py`,
`svrstatus.py` and `lnkclose.py`, and the task submitted first try.

**Checking a batch's state.** Reading the rows on the batch URL gives the stage counts
directly. On 2026-09-20 `p-1868003` showed 22 claimed tasks on page one with nine already
at **Ready for delivery**, which is the stage that means the work passed review.

---

## 24. The §21 blur can still miss, because (200,300) is not always inert

Section 21 established the five-step chain that commits a reason field, ending with a
click on a neutral spot to force a real blur. `fill3q.py` uses `(200, 300)` for that
click. On task 7574392 it was not neutral, and the result was the exact §21 failure
again: `fill3q.py` reported `idx 4 want 621 got 621 OK`, all three textareas held their
text in the DOM, and `updateTaskStatus` still came back

```
'overall_scoring_reason' is a required property
```

with the task left at `IN_PROGRESS`. Only the **overall** field failed; aesthetics and
functionality committed normally, which is why the check that reads textarea length
cannot catch this. The DOM value is right either way; what is missing is React's state.

**Diagnosis.** Read the textarea lengths first (`tacheck.js` style). If all three hold
their text and the mutation still rejects one of them, the blur for that field is what
failed, not the typing.

**The fix, and the general rule.** `recommit.py <uuid> <idx> <answers.json> <key>`
re-runs the chain for a single field and, instead of trusting a fixed coordinate, asks
the page for a blur point that is provably inert:

```js
for (const y of [120,150,90,60]) for (const x of [760,600,900]) {
  const e = document.elementFromPoint(x,y);
  if (!e) continue;
  if (e.closest('textarea,input,button,a,[role=button],[contenteditable]')) continue;
  return {x,y,tag:e.tagName};          // -> DIV at 760,90 on this task
}
```

Blurring onto that point committed the field and the resubmit returned
`workflowStatus: COMPLETED` with empty `validationResults`. Picking the blur target by
hit-test rather than by constant is the durable version of the §21 fix; `fill3q.py`'s
fixed `(200,300)` is a guess that happens to be right most of the time.

**This is also the standing argument for `diagsub.py`.** A blind submit here would have
looked like it worked. Reading the mutation body named the one field that was missing.

---

## 25. React state is the field of record, not `textarea.value`

§21 and §24 established that Feather commits a reason only on a real blur, and that the blur
point has to be chosen rather than assumed. Task 63 showed the failure that survives both: the
fill verified, and the submit was still rejected.

```
fill3q.py:  overall  idx 4  want 730  got 730   OK
diagsub.py: 'overall_scoring_reason' is a required property   (inside HTTP 200)
```

The DOM held the text. React did not. The blur click landed on a `LABEL`, which absorbed it
without moving focus, so React's `onChange` never fired. Reading `textarea.value` back cannot
detect this, because the DOM node was never the thing that was broken.

**Verify through React instead.** This is now built into `tools/fill3q.py` and runs on every
field of every task:

```js
const k = Object.keys(t).find(x => x.startsWith('__reactProps'));
k ? String((t[k].value || '').length) : 'nokey'
```

A passing fill now prints both numbers, and disagreement is a hard failure:

```
overall        idx 4 want 619 dom 619 react 619  OK
```

`fill3q.py` also picks the blur target by hit test now, walking up from the textarea in 20px
steps until it finds an element that is not a `TEXTAREA`, `INPUT` or `BUTTON`, rather than
clicking a fixed `(200, 300)`. That is §24 applied to the blur point as well as the click point.

**If a submit is rejected anyway**, `tools/recommit.py <uuid8> <answers.json>` re-commits the
overall field alone with the hit-tested blur and prints the React length, which is faster than
re-running the whole fill.

## 26. The claim loop needs a FRESH TAB per claim, not `location.href`

Reproduced twice on 2026-09-20. Driving the dispatcher board by assigning
`location.href` leaves the page rendering and its data loading, but kills the Ant
portal layer: `document.body` holds only `NAV,DIV`, no `.ant-dropdown` container is
ever appended, and **every** dropdown silently opens nothing. The batch filter, the
work-status filter and the page-size selector all fail identically, which is the
tell. Three dropdowns failing the same way is one broken layer, not three bugs.

Downstream this reads as a *server* problem, which is the dangerous part:

- `Claim task` stays `disabled:true` / `cursor:not-allowed`
- the batch menu holds only `All batches`, which looks like "no work available"
- `claim.js` returns `NO TRIGGER BUTTON`, because the trigger class is only added
  to the button once a batch is selected

None of that is true. Opening the same URL in a **new tab** via
`PUT /json/new?<url>` restores everything: body gets its third `DIV` portal, the
batch menu lists every batch, and the claim goes through.

**The loop.** Per claim: close the board tabs, open one fresh, select the batch,
then claim. `freshboard.py` + `claimnext.py` in the scratchpad do exactly this.

**Two preconditions that are easy to miss.**

1. **Select the batch before claiming.** The button is disabled until exactly one
   batch is chosen, and the app says so in its own React props: `"To claim a task,
   you must select a batch first."` Read that tooltip before concluding anything
   about rate limits (P58).
2. **The uuid changes when you claim.** The claim response carries the *pre-claim*
   uuid; claiming in Feather mints a new task instance and the tab URL becomes the
   canonical one. Take the uuid from the tab list after `claimgo.js`, and put that
   in the Attempt URL. The work item page still shows the old uuid until you
   overwrite it.
3. **`Start annotation` must be pressed before `Submit` exists.** A freshly claimed
   work item is `Not started` and renders only `Start annotation` / `Skip`;
   `lnkclose.py` will report `NO SUBMIT`. Click Start, the item goes `In progress`
   and `Save` / `Submit` appear, and only then does the submit return `POST ... 202`.
