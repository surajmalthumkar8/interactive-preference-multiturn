# TOPIC PLAYBOOK — choosing an opener that survives 10 turns

The 10-turn floor cannot be met by writing well. It is met by **choosing a topic with ten turns
of genuine depth in it before Turn 1** (`../rules/TURN_RULES.md` §4). Everything here runs
*before* a task is claimed, while the clock is not running.

---

## 1. The depth test — all four must pass

A candidate topic is only viable if you can answer yes to all of these **in advance**:

1. **Is it unresolved for me right now?** A question already settled produces a conversation
   that ends when the model confirms what you knew. Real live uncertainty regenerates itself.
2. **Does the first good answer create the next question?** Sketch turns 2–4 before starting.
   If the arc is "ask → get answer → done", it dies at turn 3 no matter how good the writing is.
3. **Is there an artifact or a decision at the end of it?** A message to send, a plan to follow,
   code that runs, a choice made. Artifacts get refined — refinement is what fills turns 4–12.
4. **Can it run 15 turns without web, files, images, or anything post-July-2025?**
   (`../rules/CAPABILITY_RULES.md`.) Check the *late* turns especially — topics drift toward
   "what's the current…" around turn 8.

Fail any one → pick another topic. Do not start and hope.

---

## 2. Shapes that reliably sustain 10–15 turns

| Shape | Why it lasts | Turn engine |
|---|---|---|
| **Refinement arc** (§A task-1) | one artifact, many passes | each turn changes tone / length / format / one constraint |
| **Real decision not yet made** (§B #4, §C prompt 2) | genuinely undecided | each answer surfaces a new consideration to push on |
| **Debugging / build thread** (§A task6, §B #7) | the code keeps not working | fix → new error → next feature → edge case |
| **Practitioner hurdle** (§C prompt 3) | you can report back what happened | try the advice → describe the result → adjust |
| **Document worked over** (§B #8, #12) | the material is dense | extract → challenge an extraction → reshape → next section |
| **Planning under constraints** (§A task4/5) | constraints emerge as you go | add a constraint each turn, watch it get honoured or dropped |

The long-horizon behaviour the dataset is *for* — dropped constraints, self-contradiction, tone
drift, re-explaining what was settled — shows up fastest in the refinement arc and the
constraint-accumulating plan. Those are the highest-value shapes, not just the longest.

---

## 3. Shapes that die early — do not open with them

- a single factual lookup ("when did X launch")
- a definition request
- a one-shot rewrite with no further constraints
- anything with a yes/no answer
- a topic you already know the answer to
- something intentionally minimal ("should i get organic berries?" — screening Q5 marks this the
  *least* useful contribution)

---

## 4. Sourcing order (`../rules/AUTHENTICITY_RULES.md` §1)

1. **Real AI history** — search ChatGPT / Gemini / Claude / Copilot for a thread that already
   ran long. A conversation that genuinely went ten turns once will go ten turns again.
2. **A real current need** — something put off, an unmade decision, a message still owed, a
   document or codebase in progress, a recent frustration.
3. **Invent** — last resort, and it must still be a real need of yours.

**Prefer history threads that already have depth over interesting single questions.** The
history search should be filtered by length, not just by topic.

---

## 5. Rotation — plan the portfolio, don't improvise

GL:56 and screening Q3 score variety **across tasks**. Before each task, check
`../learning/PROMPT_LOG.md` and deliberately move on at least three of these axes:

| Axis | Values to rotate through |
|---|---|
| **Domain** | code · writing · personal decision · money/negotiation · study/learning · planning · document work · health/admin · hobby |
| **Complexity** | quick-but-deep · multi-step technical · open-ended judgment · high-constraint |
| **Opener length band** | micro (2–8 w) · default (10–30 w) · rambling (60–130 w) · pasted-context |
| **Register** | tidy · rushed |
| **Conversation shape** | refinement · decision · debugging · practitioner · document · planning |
| **Turn count** | vary within 10–15; do not land every task on exactly 10 |

Two consecutive tasks must never share domain *and* shape *and* register.

> Note: the micro opener band is only usable when the micro question genuinely opens onto a deep
> thread. "mitosis??" as Turn 1 of a real study conversation that runs to turn 12 is fine;
> "mitosis??" answered in one paragraph is a dead task.

---

## 6. Pre-claim prep checklist

Do all of this **before** clicking claim — the clock starts on claim.

- [ ] Topic chosen and passes all four depth-test questions
- [ ] Turns 2–4 sketched (not written — sketched)
- [ ] Planned end point named (10–15, and *why* it ends there)
- [ ] Any pasted material collected in full, untrimmed, and **PII-scrubbed**
- [ ] Checked against `PROMPT_LOG.md`: no duplicate, no paraphrase, rotation satisfied
- [ ] Capability-clean across the whole planned arc, including late turns
