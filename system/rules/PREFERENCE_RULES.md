# PREFERENCE RULES — how A vs B is decided (BINDING)

The preference pair **is** the training signal. Every turn needs one, and each turn's pair is
conditioned on the previous choice — a missing selection doesn't just lose one turn, it severs
the chain and invalidates the whole conversation (GL:309, removal offence #7, *"no exceptions"*).

Guidelines basis: GL:219–221. Research grounding carried over from the legacy system:
format-bias (arXiv 2409.11704), sycophancy (arXiv 2310.13548), length-bias
(arXiv 2407.01085, ACL 2025.findings-naacl.169).

---

## 1. Read both responses in full, first

Non-negotiable and explicitly stated: *"Take your time. Compare the two sides carefully."*
Explicitly forbidden heuristics: picking at random, picking for emojis, picking the longer one
because it is longer.

---

## 2. Decision order (strict — earlier beats later)

1. **Factual / technical correctness.** Verify every checkable claim and every line of code in
   both responses. Numeric or derived claims get re-computed, never mental-mathed. A defect the
   other response lacks is usually decisive.
2. **Instruction & constraint adherence.** Checklist every explicit constraint from the current
   turn **and every constraint set in earlier turns** (tone, format, scope, "don't say gotta",
   "keep Sunday free"). A violated constraint outweighs any amount of polish. In a 10–15 turn
   conversation this is the single highest-yield check — long-horizon constraint drift is the
   failure mode the whole dataset exists to capture.
3. **Goal advancement.** Which response actually moves the real goal forward, at the right
   depth, without dodging or bloating?
4. **Sycophancy check.** If the premise is wrong, the response that (kindly) corrects it beats
   the one that flatters or agrees. Never reward agreement per se.
5. **Safety / harm.** Anything unsafe, confidently fabricated, or privacy-violating loses.
6. **Clarity and organization** — only after 1–5 tie.
7. **Concision.** Prefer the tighter response when content is equal.

**Capability defects count here:** a response that promises to browse, open a file, or produce
an image has committed a factual defect under step 1 (`CAPABILITY_RULES.md` §6).

---

## 3. Bias guards — apply before deciding

- **Length-neutralize.** Longer wins only for added *correct and requested* content. "More
  detailed" is never a reason by itself.
- **Format-neutralize.** Mentally strip bold, lists, emojis, and tables before comparing
  substance. Human raters measurably over-reward these.
- **Position-neutralize.** The A/B slot is random. If you notice a pull toward whichever you
  read first, re-read in the other order.
- **Confidence-neutralize.** Assertive tone ≠ correct. Verify.
- **Shared-defect neutralize.** A defect **both** responses carry is a wash — it decides
  nothing. Confirm the counterpart doesn't share a flaw before crediting it as a differential.
- **Variance check across the conversation and across tasks.** If picks streak to one side, or
  the reasons start converging on a template, flag it. The *pick* never changes for this; the
  *wording* of reasons must not template (stylometry applies to the reason field too).

---

## 4. Near-ties are the normal case

Late-turn pairs are often ~90% identical. Pick the side with any real differential — a
constraint honoured more exactly, a more concrete fact, tighter wording, a small defect avoided
— and name that differential. Never flip a near-tie on length or formatting.

---

## 5. The reason (optional field)

One or two short sentences, first person, casual, citing the **specific content differential**.

- ✅ "B repeated the same point twice, A got to the fix faster."
- ✅ "A kept Sunday free like I asked."
- ❌ "better formatted" · "more detailed" · "more comprehensive"
- ❌ rubric-speak: "instruction following", "accuracy", "helpfulness"

Wording must vary turn to turn and task to task.

---

## 6. Recording the selection — the `↳` verification (screening Q6)

Selecting on every applicable turn is correct but **incomplete** as an answer. The full correct
answer requires that **`↳` is prefixed to the preferred response**: `↳A  B` when A is preferred,
`A  ↳B` when B is preferred.

The `↳` is the **platform's own indicator** that a selection registered — it is not something
you type. Treat it as a mandatory per-turn verification.

Both of these are explicitly **wrong**: *"only select where the responses differ substantially"*
and *"only select on turns where you continue the conversation."*

### The UI tells (GL:309–326)

| What you see | Meaning |
|---|---|
| Green **"Continue conversation from here"** under a response | **No selection recorded → task INCOMPLETE** |
| **"Hide completions" / "Show completions"** toggle | A selection WAS recorded |
| Badge **"CONVERSATION CONTINUES FROM HERE"** | That response is the selected one |
| `↳` prefixed to A or B in the A/B pill | Marks the chosen side |

**Before submitting, scan every single turn.** Any turn still offering "Continue conversation
from here" is unfinished.

---

## 7. When a response fails to load (GL:518–526)

- Do **not** skip the task. Do **not** refresh the page.
- Hover the circular refresh icon at the top right of the response panel → tooltip
  *"Resample completion"* → click it. Progress is preserved.
- One panel failed → resample that one. Both failed → resample each individually.
- Still failing → unclaim in Feather, then reclaim.
- **Never judge a partial or truncated pair.**

---

## 8. Evidence discipline

The verdict must cite the exact lines or claims that decided it. "A felt better" is not a
verdict. If the two blind audits disagree with the judge on a decisive fact, that is a
**blocking** re-read before the pick stands.
