# PROJECT MODEL — Interactive Preference Collection (SxS Response)

What this project IS, mechanically, so every agent shares the same mental model.
**Source of truth: `Interactive_contri_inst/Interactive Contributor Instructions
(updated 07_28).md`** (the 2026-07-28 revision) + the six reference transcripts in
`Interactive_contri_inst/reference_tasks/`. The pre-07-28 guide is superseded; where
the reference transcripts contradict the new guide, **the new guide wins** (the
transcripts were produced under the old 3–5 turn regime).

## The product being built

The client ("MAI models" beta test) is collecting **human preference data** for model
training. Each task produces one conversation where a real user:
1. types (or pastes) an authentic real-world prompt,
2. receives TWO responses (A and B) from different model configurations,
3. reads both fully, selects the preferred one,
4. **optionally** continues from the chosen response, naturally, up to **10 user
   turns total** (initial prompt = Turn 1).

The paid deliverable is two things at once:
- **preference signal** (which response won, per comparison), and
- **an authentic conversation trace** that looks like real day-to-day AI usage.

Both halves are graded. A perfect pick inside a fake-looking conversation still fails.

## Task flow on the platform (07-28 guide §2)

| Step | Action |
|---|---|
| 1 | Enter a prompt — "Single-turn is fine; depth is encouraged but not required" |
| 2 | Platform generates two responses (A, B) from different model configs |
| 3 | Read BOTH in full → select the preferred one |
| 4 | **Continue the conversation (optional)** — up to ten turns total, stop whenever it feels complete |

Note step 3: the 07-28 guide **dropped** the old "optionally note why" clause. The
reason field may or may not be present. We still draft one (it costs nothing and
helps if the field exists), but a deliverable is complete without it.

From the reference transcripts: an A/B pair can appear at **every** user turn, not
just the first. Treat EVERY pasted A/B pair as a full comparison to be judged.

## Hard constraints (binding — CHANGED 2026-07-28)

- **Turns: minimum 1, maximum 10 user turns.** The initial prompt counts as Turn 1.
  **A single turn is completely valid and requires zero follow-ups.** There is no
  minimum number of follow-ups. Stop as soon as the conversation feels complete.
  (Was 3–5. Anything in this system still asserting a 3-turn minimum is stale.)
- **MODEL CAPABILITY LIMITS (new section in the 07-28 guide — hard prompt filter).**
  The model **has no web search, no real-time information, cannot receive file
  uploads, and cannot generate images.** A prompt must not assume any of these.
  Banned prompt shapes, quoting the guide: "search the web for...", "look at this
  image...", "open this file...", "what is the weather like today", "open this URL",
  "what happened yesterday in the news". See `../rules/CAPABILITY_RULES.md` — this is
  a blocking gate on every opening prompt AND every follow-up.
- **Authenticity is everything, and history-first is the new default.** The guide now
  says: open your ChatGPT / Gemini / Claude / Copilot history **right now** and copy
  something genuine, scrubbed. "Real past interactions are far more valuable than
  anything you invent on the spot." Fallback when there is no history: something you
  genuinely wanted to accomplish recently — a task you've put off, a decision you
  haven't made, something that frustrated you, a message you still need to send, or a
  document/code/project you're already working on.
- **Paste raw, unedited context.** "AI prompts often involve pasting raw, unedited
  material like an entire email thread, a block of code, a contract excerpt, a meeting
  transcript, or a long document... **Please do not trim your context to make it look
  cleaner; leave it as is.**" Long pasted prompts are now explicitly *good*.
- **Variety across tasks is now an explicit callout.** Different domains, different
  complexity levels, different prompt lengths, different styles. "A mix of quick
  single-question lookups, multi-step problems, personal situations, and professional
  tasks." Quick lookups are wanted, not penalized.
- **Flag risks named by the client:** intentionally minimal/trivial/repetitive prompts
  across tasks, prompts assuming unsupported capabilities, **padding the conversation
  with empty or nonsensical turns just to hit a length target**, **forcing extra turns
  when the topic is resolved**, and sensitive/confidential/PII content.
- **Failed response loads:** never skip/refresh — use the Resample (↺) button on the
  affected panel ("Resample completion" tooltip); resample each side individually; if
  it persists, unclaim and reclaim the task. (Suraj's side; raise it whenever he
  reports an error or pastes a blank/truncated response.)

## What changed on 2026-07-28 (do not re-litigate)

| Area | Old guide | 07-28 guide |
|---|---|---|
| Turn count | min 3, max 5 | **min 1, max 10** |
| Follow-ups | "must send at least 2" | optional, none required |
| Model capabilities | not mentioned | **no web/real-time/files/images — hard filter** |
| Prompt sourcing | "feel free to reuse" history | **history-first, strongly directed** |
| Prompt style model | 5 tidy use-case examples | **15 messy real examples** (see HUMAN_VOICE_CORPUS §B) |
| Pasted context | not addressed | **paste it raw, do not trim it** |
| Reason field | "optionally note why" | clause removed |
| Variety | avoid repetition | **vary domain, complexity, length, style** |
| Padding | avoid filler | **two separate Avoid rows about over-extending** |

The tone shift is the important part: the old guide's risk was *too short / too
repetitive*. The new guide's risk is **that plus over-extension** — forcing turns
after the topic is resolved is now called out twice. Short and genuine now beats long
and stretched.

## Division of labor

Suraj pastes task content (the two responses, or a request to start a task).
Claude runs the compulsory pipeline (`../workflows/DO_TASK.md`) and returns a
paste-ready deliverable: **PICK (A or B) + optional short reason + the next user
message to type** (or the decision to end — which is now legal at any turn ≥1).
Platform clicks — claiming, selecting, typing, resampling, submitting — are Suraj's.

## Session state matters

This project is **stateful across pastes**: one task = one conversation spanning
several pastes. The orchestrator maintains a per-task state record (turn number,
persona, topic, constraints already introduced, what the chosen responses said, the
full A/B archive) — `../templates/STATE_TEMPLATE.md` — so every follow-up stays
coherent with everything said before, and so the whole task is documented.
