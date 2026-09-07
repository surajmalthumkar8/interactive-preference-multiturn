# Uritorco platform mechanics, measured not guessed

Everything here was verified against Feather task `955b913c` (Vercel #2935) on 2026-09-07.
Selectors do not change between tasks in a batch. Read this instead of rediscovering it.

## The form: 8 required fields

Two rating panels side by side, then a shared preference block.

| Field | Control | Selector |
|---|---|---|
| Rating x6 | MUI ToggleButtonGroup | `div#root_rule_<0-2>_rating` then `button:has-text("<n>")` |
| Evidence x6 | textarea | `textarea#root_rule_<0-2>_rationale` |
| Overall preference | button group, 7 options | `button:has-text("Slightly prefer Left")` etc |
| Confidence | button group, 3 options | `button:has-text("Medium")` |
| Preference rationale | textarea | `textarea#root_rationale` |

`root_rule_0` is Completeness, `root_rule_1` is Functionality, `root_rule_2` is Visual and
responsive quality.

## The trap: Left and Right share every id

`root_rule_0_rationale` exists **twice** in the DOM, once per panel. `getElementById` always
returns the Left one, so writing both sides through it puts both texts in the Left panel.

Two reliable ways to disambiguate:

```js
// by x position: Left panel starts at x=16, Right at x=768 on a 1536 wide window
const el = [...document.querySelectorAll('textarea')]
  .find(t => t.id === 'root_rule_0_rationale' && (t.getBoundingClientRect().x < 760));
```

```
# Playwright: nth=0 is Left, nth=1 is Right
div#root_rule_0_rating >> nth=0 >> button:has-text("3")
```

The wrapper ids `rollout_a_visual_form` and `rollout_b_visual_form` appear only inside
`comment:widget_layout:...` attribute strings, not as real ancestor element ids, so they cannot
be used as CSS parents. Confirm the mapping is a=Left, b=Right.

## Writing the fields

Ratings need **real clicks** (`browser_click`). They are MUI toggle buttons and a synthetic
dispatch does not reliably flip `aria-pressed`.

Textareas take the native setter, all seven in one call:

```js
const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
setter.call(el, text);
el.dispatchEvent(new Event('input',  {bubbles: true}));
el.dispatchEvent(new Event('change', {bubbles: true}));
```

Then **one real keystroke** to fire the debounced autosave: focus the last field,
`setSelectionRange(len, len)`, press Backspace, press the character it removed. Verify the
final length is unchanged before moving on.

Confirm everything with a **hard reload** of the task URL before submitting. Ratings read back
through `aria-pressed="true"`.

## Submitting

There is no Submit button in the main flow. Open the status menu:

```
button:has-text("In progress")  ->  [role="menuitem"]:has-text("Mark as complete")
```

A confirm dialog appears: `Confirm Submission` with Cancel and **Submit Task**.

```
.MuiModal-root button:has-text("Submit Task")
```

Success redirects to the campaign page. Reload the task URL to confirm: status reads
`Completed` and all seven textareas are `readOnly: true`.

Then Vercel: paste the **live** Feather task URL into Attempt URL, Save, Submit Task, and
confirm in the `.swal2-popup` with `role=button[name="Submit"]`. The success page reads
`Task #NNNN submitted!`.

## Preview apps

Two cross-origin iframes on distinct sandbox hosts, Left at x=16 and Right at x=768:

```js
[...document.querySelectorAll('iframe')].map(f => f.src)
```

`contentDocument` is null, so the apps cannot be inspected through the iframes. Open each
origin's root (`https://<host>/`) in its own tab, which is what the platform's own
open-in-new-tab button does.

**Origins expire.** A dead sandbox returns HTTP 502. Refreshing the Feather task page
re-provisions **both** apps on brand new hostnames. This is infrastructure, not an app defect,
and it must never be written into a rating. A new origin also means empty localStorage, so any
persistence test has to be redone there.

The task page also auto-downloads a zip of both apps' source to the Playwright output
directory when it opens. Structure is `left/` and `right/`.

## Vercel side

The task page shows `Taxonomy`, `Task Variables` (id, link, title), `Attempt URL`, `Notes`.

**The `link` in Task Variables is the TEMPLATE id, not your attempt.** Corrected on #2987,
which showed what is really happening. Opening that link lands on a task whose status reads
**Unclaimed**, and an unclaimed task renders **no preview iframes at all**, only two empty
panels. Claiming it (status menu, `Claim task`) redirects to a **brand new task id**, which is
your attempt, and the previews mount there.

So the sequence on every task is:

```
Vercel Start Tasking  ->  open the Task Variables link  ->  status reads Unclaimed
  ->  status menu  ->  Claim task  ->  REDIRECTS to a new id, status In progress
  ->  previews mount  ->  that new URL is what goes in Attempt URL
```

On #2935 the template link returned "Task not found" rather than Unclaimed, which is the same
story with an expired template. **Do not diagnose empty previews as a broken task.** Check the
status chip in the header first. If it says Unclaimed, claim it; the refresh advice in the
platform's own instructions does not help, because nothing is loading yet.

Dashboard counters for this project read `0/20 submits` with no claims cap shown.

## Timing

Feather pages need about 3 seconds after navigation before `User request`, status, or form
fields are readable. Queried immediately they return `...` or null. The task page after a
submit needs about 5.
