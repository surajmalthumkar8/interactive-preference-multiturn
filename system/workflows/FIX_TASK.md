# WORKFLOW: FIX_TASK — after a flag, a rejection, or a caught mistake

Runs **before the next task**, not later. A miss that doesn't change the system repeats.

---

## 1. Freeze

Stop task work. Do not start a new task with the fault still live in the pipeline.

## 2. Reconstruct

Pull the task's state file from `sessions/`, the deliverables, and the `PROMPT_LOG.md` entry.
Write down exactly what was submitted and what the feedback (or your own observation) says.

## 3. Root cause — name the owning step

Every fault belongs to exactly one step of `RUN_TASK.md`. Assigning it to "the whole pipeline"
means it hasn't been diagnosed.

| Symptom | Usual owner |
|---|---|
| Topic died before turn 10 | S1 `mt-topic-scout` — depth test passed something it shouldn't have |
| Turn didn't engage with the response | C4 `mt-turn-writer` — anchor was weak or absent |
| Reads like AI | C5 `mt-humanizer` — skill not run, or run and not enforced |
| Capability breach shipped | S2b / C4b — the inline gate was skipped |
| Wrong pick | C2–C3 — a bias guard or the cross-check failed |
| Duplicate topic | S1 — `PROMPT_LOG.md` wasn't consulted |
| Missing selection / turn count | E2 — the checklist sweep was partial |
| Unpaid / unregistered task | `CLAIM_TASK.md` — a step in the claim sequence was skipped |

## 4. Fix the rule, not just the task

Edit the owning rule file so the same input cannot produce the same output again. A fix that
lives only in your memory of this conversation is not a fix. Concretely: add the missed case to
the ban list, tighten the gate's wording, add a row to a table, or add a checklist line.

## 5. Log it

Append to `../learning/LESSONS.md`:

```
## <date> — <one-line symptom>
**Task:** <task id>
**What happened:** <facts, no interpretation>
**Root cause:** <the actual mechanism>
**Owning step:** <RUN_TASK step + agent>
**Rule edit:** <file + what changed>
**Recurrence check:** <what would now catch it>
```

## 6. Re-verify the current task, if it is still open

If the task can still be edited, apply the fix and re-run the affected gates only — then the
full `../checklists/PRE_SUBMIT_CHECKLIST.md` before resubmitting. If it cannot be edited, note
that in LESSONS and move on.

## 7. Commit

`git add . && git commit && git push` — the rule edit needs to reach the other laptop before the
next session starts there.
