# Uritorco batch rules: the client's own corrections

Posted by the team lead at the start of the Amber Otter batch, 2026-09-05. These are
corrections to errors seen in the previous batch, so each one is a live defect the client is
actively marking down. They **outrank** any habit carried over from UI Berry.

## The six rules, as given

1. **In the rubrics, write only about the negatives or issues.** Do not mention anything
   positive about the candidate across the three rubric sections.
2. **If everything works correctly, the score must be 5, not 4.** If there is nothing negative
   to report, do not lower the score.
3. **If the score is 5, use the exact phrase provided in the instructions.** Any other phrasing
   is prohibited.
4. **The total score must be considered when selecting the winning candidate.** Completeness
   always carries the most weight; it evaluates whether the prompt's requirements were met.
5. **The candidate selection and the overall justification must match.** If you select
   "Strongly prefer Left", you must start by saying "The left candidate is strongly preferred
   because..." followed by a comparative summary of the pros and cons for each candidate.
6. **If an error can only be reproduced in a specific way, you must specify the steps.**

## What each one changes in practice

**Rule 1 kills the concession habit.** UI Berry's house style requires naming the winner's own
flaw and reads as balanced. Here the three rubric fields are negatives only. A sentence
praising the candidate in a rubric field is the error the client called out. Praise belongs in
the preference rationale (rule 5 asks for pros there), not in the six rubric fields.

**Rule 2 kills defensive scoring.** The instinct to withhold a 5 because nothing is ever
perfect is the exact error named. No negatives found means 5. This raises the bar on
inspection rather than lowering it: a 5 is a claim that you looked and found nothing, so look
properly before awarding one.

**Rule 3 means a 5 is not free prose.** There is a required phrase and it must be used
verbatim. **Find it in the platform's own instructions before writing any 5.** Do not
improvise a "nothing negative to report" line.

**Rule 4 is the tie-breaker rule.** Add the three scores per side and let the total drive the
preference, with Completeness weighted heaviest because it measures whether the prompt was
satisfied. A side that wins on polish but loses on Completeness does not win.

**Rule 5 fixes the opener.** The rationale must open with the exact selection restated:
"The left candidate is strongly preferred because...". Seven selections, so seven openers:

| Selection | Required opener |
|---|---|
| Strongly prefer Left | The left candidate is strongly preferred because |
| Prefer Left | The left candidate is preferred because |
| Slightly prefer Left | The left candidate is slightly preferred because |
| Tie | Neither candidate is preferred because (state why it is a tie) |
| Slightly prefer Right | The right candidate is slightly preferred because |
| Prefer Right | The right candidate is preferred because |
| Strongly prefer Right | The right candidate is strongly preferred because |

Then a **comparative** summary carrying pros and cons for **each** candidate. This field is
the one place positives belong.

**Rule 6 raises the bar on the Functionality field.** A bug report without steps is
incomplete. If it only appears after a specific sequence, write the sequence.

## Carried over from the other projects, still binding

- **Every claim is verified against the live app before it is written.** A claim describing
  something that does not exist is the most serious defect a submission can carry, and no
  automation excuses it.
- **Measure privately, then write what a person would see.** No pixel counts or console
  readings in the prose.
- **Humanize, then re-validate, then inspect.** The humanizer is the only rewriter; the
  mark-inspector never rewrites.
- **Claim from Vercel, never from the Feather campaign list.**
