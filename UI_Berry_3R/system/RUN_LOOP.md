# The task loop — the fast path, 8 to 10 minutes per task

**Written 2026-09-19 after four submits on the LinkedIn platform.** Every trap below cost real
time once. Following this file, the mechanics take about two minutes and the rest is inspection.

---

## The order, and why it cannot change

```
LinkedIn: Claim task (caret) -> Annotation        [task becomes Pending attempt, 24h timer]
Feather:  open the pre-claim link, VERIFY it is Unclaimed and not "Task not found"
Feather:  claim it                                 [URL changes to the ATTEMPT url - copy it]
LinkedIn: Start annotation                         [Skip disappears for good at this point]
LinkedIn: paste the attempt URL, Save, reload to confirm it persisted
  ... inspect, draft, gate, fill ...
Feather:  status pill -> Mark as complete -> Submit Task
LinkedIn: Submit
```

Verify on Feather **before** Start annotation. After that click a task cannot be skipped, and
dropping it needs a Slack post quoting the Task ID.

---

## Control invocation — check `type` and `closest('form')` before clicking

| Control | Invocation |
|---|---|
| LinkedIn `Claim task` | real mouse click at `rect.right - 14` (the caret, not the centre) |
| LinkedIn `Start annotation`, `Save` | React `onClick` (`type="button"`, no form) |
| LinkedIn `Submit` | **`form.requestSubmit(button)`** (`type="submit"` in a form) |
| Feather status pill | React `onClick` |
| Feather menu item | real mouse click **after** polling `opacity === '1'` |
| Feather rating toggles | React `onChange(evt, label)`, one group at a time, ~2.5s apart |
| Feather reason fields | set by **id**, then one real keystroke via CDP `Input.insertText` |

**`page.bringToFront()` first, always.** Background tabs throttle: the MUI menu never reaches
opacity 1 and Start annotation silently no-ops. A control that works when watched and fails when
not is this, not a dead control.

**Re-read every rect after a navigation.** A stale coordinate is indistinguishable from a dead
button.

---

## Inspection — the part that decides the score

Read the request and split it into two columns first: style words feed aesthetics, named
sections and features feed functionality.

Then, per site, in its own full tab:
1. Scroll top to bottom in ~400px steps (scroll-reveal sections sit at `opacity: 0` until seen).
2. Click every control with a **real pointer** and confirm the content changes.
3. Run the brief's main flow end to end.

### Before writing any negative
Trigger words: *dead, inert, does nothing, never, nothing else, static, unusable, broken, stuck,
not wired, no confirmation.*

- Real pointer action, visible foreground tab, before/after capture at least 800ms apart.
- **A second route** (keyboard Enter on the focused control, or a coordinate click). If the two
  disagree, the negative is not written.
- Rule the tool out: a `createObjectURL` hook must return the real URL, and a suspect export is
  re-run with hooks removed **during the task** (candidate containers 502 once it closes).
- Read blob **type**, never the toast label.

**Four false negatives were caught this way on 2026-09-19 alone**: biome markers that answered
the keyboard but not the mouse, anchors that only looked dead from the wrong scroll position, a
PNG export that had worked all along, and a thumbnail gallery that scrolls instead of swapping.
Every one would have been a scored 2.

**Measure the right signal.** Before calling a gallery dead, check whether slides stack (all
carrying `.on`) or swap. Before calling a layout broken, measure rects at default width and at
390px, and remember `overflow-x: auto` is a scroller, not a clipping bug.

---

## The gate chain, in order, no exceptions

```
draft -> validate_reasons.py -> mt-humanizer -> validate AGAIN -> mt-mark-inspector -> fill -> hard reload -> submit
```

The second validation is not ceremony. On 2026-09-19 the humanizer introduced `laid out` into a
functionality field and `piece of work` into an aesthetics field, both instant BLOCKs, on two
different tasks.

**Length:** 40 to 160 is the hard range, but the signed-off corpus centres on **100 to 120**.
Do not pad.

**Openers:** the validator anchors on `Website A is better because` / `Website B is better
because` / `Website A is better overall because`. Anything else BLOCKs.

---

## Reading the queue

| What you see | What it means |
|---|---|
| A row `Pending attempt` / `In progress` | work it |
| Claim dropdown opens with `Annotation` / `Review` | supply available |
| **Claim dropdown opens empty** | pool dry or the review gate is holding you. Wait, do not debug |
| Every row `Submitted`, some `In review` | a reviewer has to clear them before new claims |

After the **first** task of an account, a reviewer must review it before another can be claimed.
That gate applies once.
