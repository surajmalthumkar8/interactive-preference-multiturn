# TURN RULES — turn count, dependency, stopping (BINDING)

Calibrated to the **08-12 guidelines** (`MAI Interactive — Multi-Turn Guidelines (updated 08_12).md`)
and the official screening. Supersedes `Interactive_contri_inst/system/rules/TURN_RULES.md`,
which encodes the dead **07-28** regime (min 1 / max 10).

---

## 1. Counting — the only numbers that are live

| | |
|---|---|
| Your opening prompt | **Turn 1** |
| Minimum user turns | **10** (hard floor) |
| Maximum user turns | **15** (ceiling, not a target) |

Source: guidelines turn-count table (GL:168–170), `projecthub.md:12`,
`contributor_journey.md:55`, `Training & Screening.md:44`, and PROJECT_KNOWLEDGE.md §5.

### Stale text in the same guidelines file — ignore all of it

GL:134, GL:162, GL:172, GL:229 are verbatim survivals of the superseded 07-28 revision:

- "You can go up to ten turns total… If one turn says it all, that is absolutely fine."
- "Many real AI interactions are one question and one answer, and that is absolutely fine."
- "you may send follow-up messages up to a total of ten turns"
- "A minimum of ten turns is fine! You do not need to extend the conversation…"

Anything calibrated to those sentences produces an **invalid** task. If a future revision of the
guidelines removes the 10–15 table, stop and confirm with the Project Team before changing this
file.

---

## 2. The stopping rule (screening Quality Standards Q7 — settled)

| Situation | Correct action |
|---|---|
| Turn 6, conversation already feels complete | **Extend or rework the conversation** |
| Turn 11, nothing else to ask, range allows 15 | **Stop — the conversation is complete** |

Never correct, in either row: *"Add a filler if needed"* · *"Stop — even if minimum isn't met."*

The official explanation names the mechanism:

> "at turn 6 the minimum isn't met, and because the conversation already feels complete, the fix
> isn't tacking on forward questions but **enriching the earlier turns** so that reaching turn 10
> feels natural… the 15-turn upper bound is a ceiling, not a target to fill."

**Operating rule: go backwards and deepen, never forwards and pad. Never stretch toward 15.**

---

## 3. Padding is a removal offence

GL:115 — adding artificial turns just to reach the 10-turn minimum triggers **immediate
removal**. GL:113 gives the sanctioned remedy:

> If adding another turn would make it feel forced, **go back and remove as many turns as
> needed** until reaching an earlier point where the conversation can continue naturally and
> still reach the 10-turn minimum.

Banned turn shapes, no exceptions:

- "tell me more" · "can you elaborate" · "go on"
- "thanks" · "ok" · "that's helpful" · any closure-only message
- restating the opening prompt with different wording
- a topic hop with no thread back to what was just said
- **any message written only to move the counter**

---

## 4. The real constraint is upstream: topic selection

Backtracking is expensive and happens under a running clock once a task is claimed. So the
floor of 10 is a **topic-selection problem, not a writing problem**.

Choose an opening subject with **at least 10 turns of genuine depth in it before you start**.

| Sustains 10–15 turns | Dies at turn 4 |
|---|---|
| A real decision you have not made yet | A single factual question |
| A document / codebase you are actually working on | A definition |
| A multi-step problem with sub-decisions | A one-shot rewrite |
| An ongoing project whose constraints surface as you go | A yes/no |

See `../knowledge/TOPIC_PLAYBOOK.md` for the depth test applied before Turn 1.

---

## 5. Every turn must be causally dependent on the previous answer

Screening Q6 rejects *"several self-contained questions on the same topic… even if they don't
engage with the specifics of the model's response"* with the reasoning:

> "Prompts that don't engage with the specifics of the model's response **could have been
> submitted in separate, independent tasks** because they don't share the context of the same
> conversation."

**Thematic coherence is worth nothing on its own.** A follow-up you could have written *without
reading the response* is a defect even when it is on the same subject.

A turn is valid only if it does at least one of:

- **Refines the artifact** — change tone, length, format, add a concrete detail, fix what the
  model got wrong.
- **Adds or tightens a constraint** — "don't say gotta", "keep Sunday free", "under $50".
- **Challenges or probes** — "You specified 'globally', wasn't only one launch?", "but doesn't
  switching topics harm pattern recognition?"
- **Takes the genuine next step of the same goal** — "And how can I add it to a Token model".

Every drafted turn must be able to **quote the specific element of the previous response it
reacts to**. If it cannot, it is not a turn yet.

### When the response has a flaw, that is the best follow-up material

A wrong fact, an ignored constraint, or broken code in the **chosen** response is prime
material ("you said X but…", "this errors on line…", "I said no weekends"). Error recovery is
the strongest authenticity signal available.

---

## 6. Ending

- End only at **turn 10 or later**. If the conversation runs dry before 10, go back and rebuild
  (§2), do not push forward.
- Do not end on a contentless turn. A closure-only "Thanks / That's all" **is itself a quality
  failure** (GL:107–111) and wastes a turn against the ceiling.
- End the corpus way: the last turn is a small, satisfied, narrowing ask ("One last thing…",
  "Just one short sentence I can add"). After its response — make the final selection, send
  nothing further, submit.
- No goodbye turn. Zero appear in the reference corpus.

---

## 7. Variety across tasks is a scored requirement

GL:56 and screening Q3: vary domain, complexity, prompt length, and style **across tasks**, and
plan the portfolio rather than improvising ("Planning your own contributions to the project as
a whole is key to success").

Log every task's domain, length band, and turn count in `../learning/PROMPT_LOG.md`. Do not let
consecutive tasks land on the same shape.

---

## 8. Enforcement

| Where | What it checks |
|---|---|
| `mt-topic-scout` | ≥10 turns of depth exist *before* Turn 1 |
| `mt-turn-writer` | anchor quote present; turn earns its place; no padding shapes |
| `mt-compliance-auditor` | turn count in 10–15; every turn causally dependent; no filler |
| `../checklists/PRE_SUBMIT_CHECKLIST.md` | final count + selection on every turn |
