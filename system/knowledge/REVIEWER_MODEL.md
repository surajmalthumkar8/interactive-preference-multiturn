# REVIEWER MODEL — how the work actually gets checked

There is **no contributor-to-contributor review layer** (`projecthub.md:36`,
`contributor_journey.md:60-61`, Production Ops §6). Nobody is assigned to review a task, and
nobody reviews yours. QC is **organic** — sampling plus automated checks.

That absence is *why* the rules are blunt: with no reviewer to catch a borderline case, the
project relies on rules that can be enforced mechanically at scale, and on removal rather than
correction.

---

## 1. What can be checked automatically, at scale

Assume every one of these is running on every submission:

| Signal | Detects | Rule it enforces |
|---|---|---|
| Turn counter | <10 or >15 user turns | TURN_RULES §1 |
| Selection completeness | any turn without a recorded preference | GL:309 (removal #7) |
| Near-duplicate / paraphrase matching across your own submissions **and across all contributors** | reused prompts | GL:56 (removal #1) |
| Stylometry across contributors | shared writing fingerprints, AI-voice uniformity | GL:180 (removal #5) |
| AI-text classifiers on prompt text | unhumanized model output | GL:101 / AUTHENTICITY_RULES §0 |
| PII / regex + entity detection | names, emails, phones, account numbers | GL:121 (removal #4) |
| Language detection | non-English | GL:305 (removal #6) |
| Attempt-URL join | Vercel record ↔ Feather conversation | GL:27, §10.2 (removal #9) |
| Turn-similarity within a task | filler / padded turns, near-identical response pairs | GL:115 (removal #3) |
| Response-pair divergence | turns where both responses are ~identical → coin-flip labels | the padding tell |

**Implication for drafting:** the checks that will catch you are statistical, not editorial.
They compare your task against your other tasks and against everyone else's. Local quality does
not protect a task that is globally repetitive.

---

## 2. What a human sampler would look at

When a task is pulled for human review, the reading order is roughly the four scored dimensions:

1. **Capability alignment** — scan every user turn for tool/recency assumptions.
2. **Human authenticity** — does the voice read as one real person, and does it read as
   *differently* real from other contributors?
3. **Conversation-wise naturalness** — does turn N actually engage with response N-1? Is there a
   filler turn? Does it end on a contentless closure?
4. **Safety** — any PII or confidential material left in.

Then the operational record: was it claimed through Vercel, is the Attempt URL present, is a
preference recorded on every turn.

---

## 3. The adversarial questions to ask your own task before submitting

Run these as if you were trying to reject the task:

- Could **any** turn here have been written without reading the previous response? *(Screening
  Q6 — that's the defect, even if the topic is consistent.)*
- Is there a turn whose only function is to move the counter toward 10?
- Would a stylometric comparison against my last five tasks find the same opener shape, the same
  connective, the same rhythm?
- Does any turn assume web access, a file, an image, or a fact from after July 2025?
- Is there a single name, email, employer, or figure that identifies a real person?
- Is the conversation still recognizably *one* conversation, or did it become a bundle of
  independent questions on one theme?
- Does every turn show `↳` on the side I chose?
- Did I read both responses in full on every turn, or did I skim any of them?

Any "yes" on the first six, or "no" on the last two, blocks submission.

---

## 4. The pattern in the screening — the tie-breaker heuristic

Across both screening sections, **the correct answer is consistently the one that is more work**:
rework earlier turns rather than pad · go back to Vercel rather than grab a Feather task · scrub
and reuse rather than discard · read both responses fully rather than heuristic-pick.

When an edge case is genuinely ambiguous, choose the more effortful option. It has been the
right answer every documented time.
