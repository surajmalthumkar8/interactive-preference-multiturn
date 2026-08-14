# LESSONS — every miss becomes structure

Append-only. One entry per flag, rejection, or self-caught mistake, written **before the next
task** (`../workflows/FIX_TASK.md`). Never delete an entry; supersede it with a newer one.

Entry format:

```
## <date> — <one-line symptom>
**Task:** <task id>
**What happened:** <facts, no interpretation>
**Root cause:** <the actual mechanism>
**Owning step:** <RUN_TASK step + agent>
**Rule edit:** <file + what changed>
**Recurrence check:** <what would now catch it>
```

---

# Carried forward from the previous system (pre-production)

These were learned on the SxS Interactive pipeline in July 2026 and re-verified against the
current guidelines. They are here because they cost something to learn the first time.

## 2026-07-30 — Long prompts errored both response panels
**What happened:** 43-, 49-, and 57-word opening prompts caused both panels to error;
everything at or under 31 words generated cleanly (7 for 7).
**Root cause:** platform-side generation limit, not a rule.
**Status now:** ⚠️ **Unverified on the current Feather campaign.** The 08-12 guidelines
actively publish 70- and 130-word examples and encourage pasting entire documents, so either
the limit was lifted or it never applied to this campaign. **Treat as a live unknown:** if a
long opener errors twice, shorten it and resample rather than assuming a content problem. Do
not pre-emptively cap prompts at 31 words — that would contradict the client's own examples.

## 2026-07-30 — Injected typos are their own fingerprint
**What happened:** deliberately added corruption-class typos ("helppp", "explaination") read as
manufactured mess.
**Root cause:** real typos are omissions (dropped apostrophes, lowercase, missing punctuation);
invented ones are additions, and additions are stylistically consistent in a way real slips are
not.
**Rule:** `../rules/AUTHENTICITY_RULES.md` §3 — omission class only. Strip AI polish, never add
fake damage. Retyping the turn by hand is the safest humanization pass.

## 2026-07-xx — A defect both responses share decides nothing
**What happened:** a blind auditor flagged a real defect in B; A carried the identical defect;
it was nearly credited as a differential (task 977).
**Root cause:** blind auditors see one response, so a genuine flag can still be non-differential.
**Rule:** `../rules/PREFERENCE_RULES.md` §3 — shared-defect neutralize, cross-check the
counterpart before any flag earns weight.

## 2026-08-13 — The guidelines file contradicts itself on turn count
**What happened:** the same file states both min 1 / max 10 and min 10 / max 15.
**Root cause:** the 08-12 revision was edited in place over the 07-28 text and the superseded
passages (GL:134, 162, 172, 229) were never stripped.
**Rule:** `../rules/TURN_RULES.md` §1 — 10 floor, 15 ceiling, stale lines named explicitly.
**Recurrence check:** if a future revision appears, reconcile the whole system before working
(`../workflows/RUN_TASK.md` step 0).

## 2026-08-13 — Two billing-critical steps exist only inside an image
**What happened:** the copy-URL-after-claim and paste-into-`Attempt URL` steps are absent from
the written procedure (GL:367–435) and appear only in the final flowchart image — which is
embedded as base64, so it is invisible to text search and grep.
**Root cause:** reading the prose is not reading the guide.
**Rule:** `../workflows/CLAIM_TASK.md` — the full sequence, with the image-only steps flagged.
**Recurrence check:** when a new doc arrives, extract and read every embedded image before
trusting a grep.

## 2026-08-14 — AI drafting policy reversed
**What happened:** leadership posted a Slack update permitting AI (including Claude Code) to
help write prompts and turns, provided the output is humanized.
**Status:** reported by Suraj, **not independently verified against the platform**. The
screening's Quality Standards Q2 still lists "ask an AI to generate a prompt, then paste it" as
a wrong answer, and it is unknown whether the screening doc was updated.
**Rule:** `../rules/AUTHENTICITY_RULES.md` §0 — allowed, humanization mandatory, sourcing
preference order unchanged.
**Recurrence check:** if quality or removal issues ever surface, this mismatch is the first
place to look.
