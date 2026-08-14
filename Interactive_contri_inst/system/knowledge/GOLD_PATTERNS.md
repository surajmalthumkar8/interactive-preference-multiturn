# GOLD PATTERNS — distilled from the six reference transcripts

Patterns that separate signed-off SxS conversations from flagged ones. Feed these to
the judge, the turn-writer, and the reviewer-simulator. Grows via the lessons loop.

## Conversation-shape patterns

1. **The refinement arc (task-1, task4, task5).** Open with a concrete need → model
   delivers → each follow-up tightens one screw (warmer tone, no "gotta", add two
   concrete dates, shorter version, one backup line). The arc has direction; by the
   last turn the artifact is finished and the user stops. This is the safest,
   most-signed-off shape for writing/planning prompts.
2. **The curiosity chain (task3).** Factual question → notice something in the answer
   ("globally"?) → challenge it → branch to adjacent facts (first Supercell game? most
   popular?). Each turn grows out of the previous ANSWER, not out of a script.
3. **The practitioner thread (task2, task6).** Real personal context ("interview in
   15 days", a pasted Django traceback) → progressively deeper, more specific asks
   (Walmart-specific, consistency problem, "but doesn't switching harm pattern
   recognition?" / Token model → service layer). Shows genuine stakes; pushback on
   the model's advice is a strong authenticity signal.
4. **Turn counts in the corpus: 5, 3, 4, 3, 3, 3.** Three turns is the norm; five
   only when the artifact genuinely needed that many passes. Never stretch.

## Preference-judgment patterns

5. **Near-identical pairs are normal.** Final A/B pairs in the corpus are often 90%
   the same (task4, task5, task3). The pick then hinges on small real differentials:
   tighter wording, a slightly more useful structure, honoring an earlier constraint
   better, fresher/more concrete data ("over 2 billion downloads" vs vague).
6. **Defects decide.** task6 response B contains a stray `}` closing a Python class —
   a syntax error that would crash the file. **Always lint/scan code responses
   char-by-char; a syntax error or API misuse is decisive against that response.**
7. **Constraint memory decides.** When the user set a constraint in an earlier turn
   (no "gotta", chores Saturday only, Sunday free), the response that silently drops
   or dilutes it loses (task4: B shrank the chore window it was asked to keep flexible).
8. **Never reward length or markdown-density for its own sake.** Both corpus models
   over-format; the picks track substance (correctness, constraint-following,
   usefulness of the added detail), not bulk.
8a. **A run of same-side picks is not evidence of bias; flipping for variety is the
   actual violation** (task 3154). Three consecutive comparisons went to B — B second
   position every time, B the more sycophantic side every time (exclamation closes,
   "I can tailor this!", a pointless "what's the weather like" question). Each pick was
   still correct, because each rested on a *quoted* differential the other response got
   wrong. The temptation to pick A once "for balance" is the bias, not the streak.
   Guard shape: when the streak makes you uneasy, the remedy is to re-verify the
   differential is quoted and factual — **never to change the pick.** A/B side is
   randomized per comparison anyway, so a streak carries no information. Record the
   variance neutralization explicitly in the state file (task 3154 did), so the
   reviewer can see the streak was noticed and consciously not acted on.
8b. **Converged pairs are decided by unforced derived-number errors** (task 3154, all
   three comparisons). When both responses reach the *same* recommendation with
   near-identical structure, stop comparing prose — the pick is almost always sitting
   in a small checkable number a fast reader skims past. Real examples: `$116.70` vs
   `$116.67` for 2800/24 (a 3-cent rounding error, and the response that rounded also
   bolted on a non-sequitur about loan interest when no loan was in the framing); "the
   car is already **12** years old" for a 2013 car in 2026 (it is 13).
   **Highest-yield place to look: numbers the USER never supplied.** A figure the user
   typed can only be copied or dropped; a figure the model *derived* (an age, a monthly
   equivalent, a total, a percentage of value) is where an unforced error can exist at
   all. Procedure: list every number in each response, mark which are user-given vs
   derived, and recompute every derived one with code. A wrong derived number is a
   Tier 1 correctness defect and outranks tone, length and polish.

## Prompt-choice patterns

9. **Everyday, specific, low-stakes-real:** cancel-dinner message, interview prep,
   game trivia, weekly routine, workday plan, Django error. Each has one concrete
   personal detail that makes it real (Saturday dinner, 15 days, Walmart, 9-to-6).
10. **A raw paste is a valid prompt** (task6): errors, snippets, a paragraph to fix —
    with zero prose around it. Very strong authenticity signal for coding tasks.
11. **"Ask me a few questions first" (task4)** is a natural interactive pattern the
    client likes — it forces a genuine multi-turn exchange without padding.

## Trap list (each one has a rule pointing here)

- **Padding trap:** filler turns ("can you elaborate?", "tell me more", "thanks,
  looks good") to hit turn counts → flagged as low effort. Every turn must change
  the artifact or the understanding.
- **Perfect-typist trap:** flawless punctuation, em dashes, semicolons, colons with
  lists, "furthermore" in a user turn → reads as AI-written, kills authenticity.
- **Stress-test trap:** trick questions, jailbreaks, artificial difficulty →
  explicitly against instructions.
- **Repetition trap:** same prompt genre/topic task after task → flagged. Rotate via
  `PROMPT_PLAYBOOK.md` and log every used prompt in `../learning/PROMPT_LOG.md`.
- **Length-bias trap:** picking the longer/prettier response without verifying its
  content. Verify first; length is never the reason.
- **Anchoring trap:** drafting the follow-up before the pick is settled, then
  bending the pick to fit the drafted follow-up. Pick first, then write.
