# STATE TEMPLATE — per-task conversation state

One file per task at `Interactive_contri_inst/sessions/<task-id>_state.md`,
updated at every paste BEFORE the deliverable goes out. Archived (kept, marked
CLOSED) at MODE END.

```markdown
# Task state: <task-id or short label>   [OPEN|CLOSED]

- Started: <date>
- Category: <playbook category> · Persona: <one line>
- Planned arc: <one line, updated as it evolves>

## Turn ledger
| Turn | User message (verbatim) | Words | Pick | Decisive differential |
|---|---|---|---|---|
| 1 | ... | 24 | A | ... |

One row per user message ACTUALLY SENT. When the task ends, the END row's stated turn
count must equal the number of message rows above it.

## Imperfection patterns spent (anti-fingerprint ledger — AUTHENTICITY_RULES)
| Turn | Pattern(s) used (named) | Class |
|---|---|---|
| 1 | dropped apostrophe · no terminal period | omission |
| 2 | <must differ from T1> | omission |

A pattern used in the previous turn is unusable; a pattern used twice in this task is
unusable for the rest of it. Omission class only. If nothing unspent fits, ship clean.

## Constraint ledger (accumulates; every future response is checked against ALL)
- T1: <constraint>
- T2: ...

## Chosen-response memory (what the model has already said/committed to)
- T1: <key facts, artifacts, offers made>

## Notes
- <anything unusual: resamples, near-ties, reviewer risks>
```
