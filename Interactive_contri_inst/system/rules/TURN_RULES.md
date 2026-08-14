# TURN RULES — conversation flow, turn count, ending (binding)

Updated 2026-07-28 for the revised contributor guide. The old 3–5 regime is dead.

## Counting (hard platform constraint — CHANGED)

- The initial prompt is **Turn 1**. Minimum **1** user turn, maximum **10**.
- **A single turn is complete and valid.** Zero follow-ups are required. The guide:
  "Stop when the conversation feels complete — even after just one turn."
- Every deliverable states "this will be Turn N of up to 10".
- The state record (`../templates/STATE_TEMPLATE.md`) tracks the turn number.

## The new failure mode: over-extension

The 07-28 guide names two separate padding failures in its Avoid column:
- "Padding the conversation with empty or nonsensical turns just to hit a length target"
- "**Forcing extra turns when the topic is resolved**"

So the question at every turn is no longer *"have we hit 3 yet?"* — it is
**"is there something a real person would genuinely still say here?"** If the answer
is no, END. Ending at Turn 1 or Turn 2 because the model fully answered is now a
*correct* outcome, not a shortfall. Never invent a turn to look thorough.

## Every follow-up turn must earn its place (anti-padding)

A turn is valid only if it does at least one of:
- **Refines the artifact** — changes tone, length, adds a concrete detail, converts
  format (checklist), fixes what the model got wrong.
- **Adds or tightens a constraint** — "don't say gotta", "keep Sunday free",
  "under $50".
- **Challenges or probes the response** — "You specified 'globally', wasn't only one
  launch?", "but doesn't switching harm pattern recognition?".
- **Takes the genuine next step of the same goal** — "And how can I add it to a
  Token model", "Give me the service for create and deactivate tokens".

BANNED turns: "tell me more", "can you elaborate", "thanks, looks good", restating
the opening prompt, topic hops with no thread, any message written only to reach a
turn count. Research note: ~80% of real user follow-ups react to something specific
in the model's previous answer — ours must too, by quoting or pinpointing it.

## Reacting to the chosen response is mandatory

The turn-writer receives the chosen response and must anchor the follow-up to a
specific element of it (a word it used, an option it offered, a gap it left, a
question it asked back). A follow-up that could have been written without reading
the response is a defect.

## When the model's response has a flaw

Real users notice: a wrong fact, ignored constraint, or broken code in the CHOSEN
response is prime follow-up material ("you said X but...", "this errors on line...",
"I said no weekends"). Use it — error recovery is a strong authenticity signal.

## Ending (MODE END)

- **End is allowed at ANY turn ≥1** and SHOULD happen as soon as the conversation
  feels complete. There is no floor to clear.
- Decide END by the content, not the count. END when: the model fully answered and a
  real person would close the tab; the artifact the user wanted exists; or the next
  plausible turn would only be "thanks" or a restatement.
- End the corpus way: the final turn is a small, satisfied, narrowing ask
  ("Perfect. One last thing...", "Just one short sentence I can add") — after its
  response, stop. **No thank-you sign-off, no goodbye turn** (zero exist in corpus;
  a goodbye message would waste a turn and read as padding).
- If a single turn already resolved it, END immediately after the first pick. No
  apology, no filler turn.
- The END deliverable tells Suraj: make the final pick (if a pair is showing),
  send nothing further, submit.

## Turn-length variety is now a requirement, not a nicety

The guide asks contributors to "vary your topics, complexity levels, **prompt
lengths**, and styles across tasks". Track this in `../learning/PROMPT_LOG.md`:
log each task's turn count and prompt length band. Do not let every task land at the
same shape. A one-turn quick lookup, a three-turn refinement, and a long
pasted-context task are all wanted — deliberately mix them across tasks.

## Multiple prompts per task

The platform allows trying a different prompt in the same task. Default: one
coherent conversation per task (all six references do this). Only start a second
thread if Suraj asks or the platform forces it; the same rules apply per thread.
