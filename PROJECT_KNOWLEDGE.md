# Interactive Preference — Multi-Turn (MAI): Consolidated Project Knowledge

Derived from a full line-by-line read of all 4 source documents in this folder plus the 16
screenshots embedded as base64 in the guidelines file. Citations are `file:line`.
Source docs: `MAI Interactive — Multi-Turn Guidelines (updated 08_12).md` (referred to below as
**GL**), `projecthub.md`, `contributor_journey.md`, `Training & Screening.md`.

---

## 1. What this project actually is

**Client:** Microsoft AI ("MAI"). The tasking platform is `msft.feather-prod.azure.com`
(GL:371) and the Feather login screen offers Microsoft / GitHub / LinkedIn SSO (image7).

**Product being built:** a **multi-turn human preference dataset**. Each task = one
10–15-turn conversation where, at *every* turn, the contributor writes a prompt, receives two
responses from **two different model configurations** (GL:132), and picks the preferred one.
The picked response becomes the conversation's continuation; the rejected one is discarded.

**What is being collected, precisely:** an ordered chain of `(context, prompt, chosen,
rejected)` tuples, 10–15 deep, where every link is conditioned on the human's previous choice.

**Contributor's role:** *both* the user and the judge. You supply the prompt distribution and
the preference signal. You are not reviewing anyone else's work and nobody is assigned to
review yours (`projecthub.md:36`, `contributor_journey.md:60-61`) — QC is "organic"
(sampling/automated), which is why the removal-triggering rules are so blunt.

---

## 2. Why they are asking for it this way (the intent behind each rule)

Understanding the *why* makes the rules self-explanatory and prevents guessing at edge cases.

| Requirement | Why it exists |
|---|---|
| **10–15 turns, not 1–3** | Single-turn preference data is abundant and cheap. Models fail *specifically* at long-horizon behaviour: losing earlier constraints, contradicting themselves, drifting in tone, re-explaining what was settled. Those failures only become visible — and therefore only become trainable preference signal — deep into a conversation. Turn 12 is the product; turns 1–3 are the setup cost. |
| **Prompts from your real AI history** (GL:11, GL:42, GL:209) | Distribution match. A reward model trained on polished, invented prompts learns to serve polished prompts and degrades on real traffic, which is messy, rushed, mid-thought, and full of pasted raw material. The typos and run-ons are the signal, not noise (GL:190). |
| **No LLM-written prompts** (GL:101, immediate removal) | LLM-written prompts are self-referential — the model would be trained on its own output distribution, which collapses diversity and bakes in existing model bias. This is the single most damaging way to poison this dataset. |
| **No shared writing style across contributors** (GL:180) | Fraud detection. Identical stylistic fingerprints across "different" contributors indicate collusion, a shared prompt farm, or a shared LLM. Stylometry catches this even across unrelated topics. |
| **No prompts needing web/tools/images/files** (GL:64) | The model under test has **no** web search, real-time data, code execution, file upload, or image generation. If the prompt requires any of them, *both* responses fail in the same way, the pairwise comparison carries zero information, and the task is worthless. |
| **A selection on every single turn** (GL:309) | The preference pair *is* the training signal. A turn with no choice yields no pair — and because each turn is conditioned on the previous choice, a gap also severs the chain, invalidating the whole conversation, not just that turn. |
| **No padding / filler turns** (GL:174, GL:275) | A filler turn ("can you elaborate?" after a complete answer) produces two near-identical responses. The preference becomes a coin flip, which injects **label noise** — actively worse than no data, because it teaches the reward model that a real quality gap exists where none does. |
| **No duplicate/paraphrased prompts across tasks** (GL:56, immediate removal) | Duplicates over-weight one region of the input distribution and inflate task counts without adding coverage. |
| **PII scrubbing** (GL:121) | The dataset is shared and retained. Legal/compliance exposure. |
| **The exact claim→URL→paste flow** (image16) | Vercel and Feather are two separate systems. The pasted Feather URL is the **join key** binding the conversation record to the billable task record. No key → orphaned data → cannot be attributed → cannot be paid or ingested. |

---

## 3. The four scored quality dimensions (GL:60–123)

Every task is graded on these. Failing any one invalidates the task; several carry removal.

1. **Prompt Capability Alignment** — asks only for what a bare, tool-less model can do.
   ⚠️ **The live task intro adds a limit the guidelines never state: the model's knowledge
   cuts off in July 2025.** So a prompt is invalid not only when it asks the model to *fetch*
   something, but also when it depends on anything that happened after July 2025 — a library
   version, a product release, an election, a rule change. Check recency as well as tool use.
   (Campaign name on the live task: `[general-multi-turn]`, confirming the 10–15 turn range.)
2. **Human Authenticity** — reads like *you* actually typed it; written without LLM help.
   *Grammar and polish are explicitly not wanted.* (GL:99–103)
3. **Conversation-Wise Naturalness** — each turn builds on the previous answer; no filler,
   no ignoring the model's reply, no abrupt unconnected topic jumps, no ending on a
   contentless "Thanks"/"That's all". (GL:107–111)
4. **Safety** — no PII, no sensitive personal data, no confidential material. (GL:117–123)
   Screening Q8: when a genuinely good history prompt contains a client name, email, and
   confidential details, the answer is **replace or remove the sensitive information and use
   it** — not discard it, and not submit it with a disclaimer note attached.

### 3.1 What "multi-turn" actually requires: dependency, not just topic continuity

Screening Q6 draws a distinction the guidelines only imply. The wrong answer to avoid is
sending *"several self-contained questions on the same topic… even if they don't engage with the
specifics of the model's response."* The official reasoning:

> "Prompts that don't engage with the specifics of the model's response **could have been
> submitted in separate, independent tasks** because they don't share the context of the same
> conversation."

So thematic coherence is worth nothing on its own. **Each turn must be causally dependent on the
answer before it** — clarify it, push back on it, refine it, or take its genuine next step.
A follow-up you could have written *without reading the response* is a defect, even if it is on
the same subject. This is the whole reason the dataset is multi-turn rather than a bundle of
single-turn tasks.

### 3.2 Pasted content ≠ file upload

Screening Q4 accepts *"Here are notes from three team meetings, can you identify the open action
items? [notes]"* while rejecting *"What happened in the news yesterday?"*. The distinction is
**where the content lives**: pasting a document's text into the prompt is not only allowed, it is
encouraged (GL:188, GL:211). Asking the model to *open*, *fetch*, or *look at* anything is the
violation. Paste, don't point.

---

## 4. Hard rules that trigger **immediate removal**

Every one of these is stated in the guidelines as removal-triggering, not merely a
quality deduction:

| # | Rule | Cite |
|---|---|---|
| 1 | Reusing or paraphrasing the same prompt across tasks | GL:56, GL:265–273 |
| 2 | Using LLM-generated prompts | GL:101 |
| 3 | Adding artificial turns just to reach the 10-turn minimum | GL:115 |
| 4 | Submitting direct PII / sensitive PII / confidential material | GL:121 |
| 5 | Distinctive writing patterns shared across contributors | GL:180 |
| 6 | Submitting a prompt not written in English | GL:305 |
| 7 | Submitting an **incomplete conversation** (any turn lacking a selection) — *"no exceptions"* | GL:309 |
| 8 | Discrimination, insults, inappropriate conduct | GL:497 |
| 9 | Breaking the Vercel→Feather sequence (also corrupts data & blocks invoicing) | GL:27, GL:363 |
| 10 | Claiming tasks directly in Feather without going through the platform | GL:381 (offboarding + non-billable) |

---

## 5. Turn count — **the documented conflict, and the resolution**

The guidelines contain **stale text from an earlier single-turn version of this project**.
Both versions are still in the file. This is the most likely source of a failed screening,
so it is worth being explicit.

**Authoritative (multi-turn):**
- "10–15-turn conversations" — GL:7, GL:9, `projecthub.md:12`, `contributor_journey.md:55`,
  `Training & Screening.md:44`
- Explicit table: **Minimum 10 user turns / Maximum 15 user turns** — GL:168–170
- "the minimum number of turns you have to complete on this project is 10" — GL:287
- "still reach the 10-turn minimum" — GL:113

**Stale / contradictory (ignore):**
- GL:134 — "You can go up to ten turns total… **If one turn says it all, that is absolutely fine.**"
- GL:162 — "Many real AI interactions are one question and one answer, and that is absolutely fine."
- GL:172 — "you may send follow-up messages up to a total of ten turns" (states 10 as the *ceiling*)
- GL:229 — "A minimum of ten turns is fine! You do not need to extend the conversation…"

**Operating rule: 10 is a hard floor, 15 is the ceiling.** Your opening prompt is Turn 1
(GL:172).

### 5.0 ✅ Definitively settled by the screening (Quality Standards Q7, "Stopping rule")

The screening tests this directly with a two-row matrix, and the answers remove all doubt:

| Situation | Correct action |
|---|---|
| **S1** — at turn 6, the conversation already feels complete | **Extend or rework the conversation** |
| **S2** — at turn 11, nothing else to ask, range allows up to 15 | **Stop — the conversation is complete** |

Two distractor columns are *never* correct: **"Add a filler if needed"** and **"Stop — even if
minimum isn't met."**

The official explanation is worth quoting, because it specifies *how* to extend:

> "at turn 6 the minimum isn't met, and because the conversation already feels complete, the fix
> isn't tacking on forward questions but **enriching the earlier turns** so that reaching turn 10
> feels natural. S2 is a stop because the 10-turn minimum is met and the conversation is done,
> and **the 15-turn upper bound is a ceiling, not a target to fill.**"

So: **go backwards and deepen, never forwards and pad.** And never stretch toward 15.

### 5.1a Why the contradictory text exists (root cause)

The stale passages are **verbatim survivals of the previous 2026-07-28 revision** of this guide,
which ran a **minimum 1 / maximum 10** regime in which a single-turn task was explicitly valid.
The 08-12 revision was edited in place and those passages were never stripped. That is why
GL:134/162/172/229 read as a coherent ruleset — they *are* one, just the superseded one.

| Area | 07-28 guide (dead) | 08-12 guide (current) |
|---|---|---|
| Turn count | min **1**, max **10** | min **10**, max **15** |
| Follow-ups | optional; zero required | mandatory to reach 10 |
| Single-turn task | explicitly valid | invalid |
| Named risk | over-extension / forcing turns | under-length + padding |

Anything calibrated to the 07-28 numbers now produces **invalid** tasks.

### 5.1 The genuine tension this creates, and the official way out

Rule 3 above forbids padding to reach 10. The floor of 10 is nonetheless mandatory. GL:113–115
gives the sanctioned resolution, and it is not "pad anyway":

> If adding another turn would make it feel forced, **go back and remove as many turns as
> needed** until reaching an earlier point where the conversation can continue naturally and
> still reach the 10-turn minimum.

**The real implication — this is a topic-selection problem, not a writing problem.** You must
choose an opening subject with at least 10 turns of *genuine* depth in it *before you start*.
Backtracking and rebuilding is the fallback, not the plan. Topics that reliably sustain 10–15
turns: an actual decision you have not made, a real document/codebase you are working on, a
multi-step problem with sub-decisions, an ongoing project with constraints that surface as
you go. Topics that die at turn 4: single factual questions, definitions, one-shot rewrites.

---

## 6. Prompt sourcing — the preferred methodology (GL:207–213)

Stated priority order (GL:209): **reuse > adapt/expand > invent**.

1. **First step, always:** open your ChatGPT / Gemini / Claude / Copilot history and search it
   for something you genuinely asked. Copy it *exactly as written*, then remove personal
   details (GL:42).
2. If no history, use something you genuinely need *right now* (GL:44–52): a task you have
   been putting off, an unmade decision, a message you still need to send, a document or
   codebase you are actually working on, something that recently frustrated you.
3. **Paste the real content — never placeholders.** No `[paste context here]`. Include the
   full email thread, the actual code block, the real contract excerpt. Do not tidy it up.
   The prompt must be self-contained and answerable on its own (GL:211–213).

**Style target** (GL:190): casual, direct, sometimes rushed or mid-thought, grounded in
personal context, occasionally messy — shorthand, missing punctuation, trailing sentences.
The worked examples at GL:194–201 are deliberately unpolished; several have no capitalisation
and run-on structure. That is the target, not a tolerance.

**Diversity is a core requirement, not a bonus** (GL:56): vary domain, complexity, and style
across tasks. Mix quick questions, deep problems, personal situations, professional tasks.
Screening Q3 adds a planning instruction: *"Planning your own contributions to the project as a
whole is key to success."* — treat your task portfolio as something to plan, not improvise.

### 6.1 Banned sourcing methods (screening Quality Standards Q2 — all four wrong answers)

The screening lists four ways of sourcing a prompt, all incorrect. Two are **not** stated
anywhere in the guidelines document and are only discoverable here:

| Method | Verdict |
|---|---|
| Ask an AI model to generate a realistic-sounding prompt, then paste it | ❌ Removal offence (GL:101) |
| **Paste questions from exams, quizzes, or educational materials** | ❌ **Not in the guidelines — screening-only rule** |
| **Take an interesting query found online that isn't your own actual AI use** | ❌ **Not in the guidelines — screening-only rule** |
| Reuse a history conversation very similar in topic/approach to one already submitted | ❌ Duplicate-adjacent (GL:56) |

The single correct method: **your own history → pick one meaningfully different from what you've
already submitted → scrub PII → paste into Feather → continue naturally.**

### 6.2 Authentic is necessary but not sufficient (screening Q5)

*"should i get organic berries?"* is a perfectly real thing a person might type — and it is the
**wrong** answer, marked the least useful contribution, because it is intentionally minimal and
trivial. Contrast with the accepted examples: an API-testing interview prep, extracting action
items from pasted meeting notes, negotiating a contractor quote from $18k to $12k.

**The bar is two-part: genuinely yours *and* substantial enough to sustain 10–15 turns.** A real
but thin prompt fails both the triviality rule and, downstream, the turn floor.

---

## 7. Choosing between the two responses (GL:219–221)

- Read **both responses in full** before choosing.
- The choice must be **reasoned and grounded in what the response actually says** and how well
  it meets your need.
- Explicitly forbidden heuristics: picking at random, picking for emojis, picking the longer
  one because it is longer.
- Blank/failed response → see §9, do **not** guess.

---

## 8. Verifying a conversation is complete — the visual check (GL:309–326 + images 1–3)

This is the #7 removal trigger and the easiest to trip accidentally, so learn the UI tells:

| What you see | Meaning |
|---|---|
| Green **"Continue conversation from here"** button under a response | **NO selection recorded** → task is INCOMPLETE (image1) |
| **"Hide completions" / "Show completions"** toggle on the right of the panel | Selection WAS recorded (image2, image3) |
| Badge **"CONVERSATION CONTINUES FROM HERE"** on a response | That response is the selected one (image2) |
| The **`↳`** arrow prefixed to A or B in the A/B pill — e.g. `↳A  B` or `A  ↳B` | Marks which side was chosen (GL:454, image3) |

**Before submitting, scan every single turn** (GL:326). If any turn still shows *"Continue
conversation from here"*, the task is not finished.

Note on GL:454: the `↳` is the platform's own indicator of a registered selection, not
something you type. Treat that instruction as a **verification** step — confirm the arrow is
present on your preferred side for every turn.

---

## 9. Failure handling during tasking

**A response fails to load or comes back blank** (GL:518–526):
- Do **not** skip the task. Do **not** refresh the page.
- Hover the circular refresh icon at the top right of the response panel → tooltip
  *"Resample completion"* → click it. Progress is preserved.
- One response failed → resample that one. Both failed → resample each individually.
- Still failing → unclaim the task and reclaim it.

**"Task not found" on Feather** (GL:328–347, refined by the official Operational Workflow quiz Q3):

- **What it means:** the task is **no longer available to anyone** — typically its claims have
  been exhausted. It is not a bug on your end and it is not recoverable.
- **What to do:** **go back to Vercel and look for another task** via the standard procedure.
  Mechanically that means releasing the dead task on the Data Annotation platform (GL:346,
  image6) and clicking **Start Tasking** again for a new assignment.
- **What NOT to do** — all three are explicitly wrong answers on the screening quiz:
  - Do **not** Cancel the task.
  - Do **not** Escalate it to notify the client.
  - Do **not** go hunting for an unclaimed task **directly in Feather** and paste its URL into
    the Attempt URL field of the original Vercel task. This is the trap option: it looks like a
    resourceful workaround and it is a data-integrity violation — it binds one Vercel task
    record to an unrelated Feather conversation.

> Note the emphasis: the quiz's correct answer is *"look for another task in Vercel"*, not
> *"release the task"*. Releasing is just the mechanic; the principle being tested is that
> **every task must be re-entered through Vercel — never sourced from Feather.**

---

## 10. The operational workflow — and its critical undocumented step

### 10.1 The invariant

> **Always start in Vercel, then go to Feather. Never work in Feather alone. Never work only
> in Vercel.** (GL:23–25, repeated GL:359–361)

Breaking it corrupts data, risks removal, and prevents correct invoicing (GL:27).

- **Vercel** = the Data Annotation Platform → `annotation-platform-henna.vercel.app` (GL:386)
- **Feather** = where you actually write prompts and pick responses → `msft.feather-prod.azure.com` (GL:371)

### 10.2 The billable claim sequence (flowchart, image16) — **read this one carefully**

> ✅ **CONFIRMED** by the official Operational Workflow screening quiz (Q1, Q2, Q4). This is
> the single most heavily tested procedure in the screening — four questions, all on this.

The flowchart is headed *"Only correctly claimed tasks are billable — follow every step, no
exceptions"* and footed *"Skipping one step = task will not be paid. No exceptions."*

1. **[Vercel]** Click the task link in the **task Variables** panel (image5, image10).
2. **[Feather]** The link opens the task in Feather. Locate it — it **must show "Unclaimed"**.
3. **[Feather]** **Claim the task**, and **confirm the status changes to "In progress"** (image13).
4. **[Feather] — flagged CRITICAL** — **Copy the full browser URL from the address bar.**
   ⚠️ **Copy it only *after* claiming — the URL changes on claim.** Copying before claiming
   captures a stale URL and the task will not register.
5. **[Vercel]** **Paste it into the field literally named `Attempt URL`** — cannot be edited afterwards.
6. **[Feather]** Begin annotation. The task is now billable.

**Memorised as a sentence:** *Vercel link → open in Feather → claim in Feather → confirm
"In progress" → copy the browser URL → paste into `Attempt URL` in Vercel → annotate in Feather.*

**Why the order is non-negotiable** (quiz Q4): only correctly claimed and registered tasks are
eligible for billing. Skipping any step affects payment eligibility. It is *not* because of a
time limit after claiming, *not* because Feather deletes tasks on a bad URL, and *not* because
anything must be claimed twice — those are all distractor answers on the screening.

> **Steps 4 and 5 do not appear anywhere in the written Steps 1–7 (GL:367–435).** They exist
> only inside the final flowchart image — yet the screening tests them directly. Anyone who
> reads only the prose will both fail the screening and produce unpaid work.

### 10.3 Submitting / releasing (GL:412–430)

- **Submit:** Feather → **"Mark as Complete"**, then Vercel → **"Submit Task"**.
- **Release:** release in **Feather first**, then Vercel. Always verify the Feather release
  before releasing on Vercel. If you never claimed it in Feather, just release on Vercel.
- **Never** use **"Cancel task"**, **"Escalate Issue"**, or **"Decline"** (GL:419; these
  appear in the Feather status dropdown, image14).

### 10.4 Account integrity (GL:376, GL:508–516)

- Feather login is via **"Log In with LinkedIn"**.
- Your **LinkedIn primary email must match the email you were invited with**. Check/fix at
  `https://www.linkedin.com/mypreferences/d/manage-email-addresses` *before* first login.
- **Vercel email == Feather email == Slack email.** Identical across all three, plus any
  team-provided spreadsheet or tool.

### 10.5 Payment eligibility (GL:460–475)

Two independent conditions, both required:
1. Correct registration via the **complete** operational process, and
2. **All** applicable quality requirements met.

Pre-submit checklist: no skipped steps · all required fields completed · **a preference
selected on every applicable turn** · all Project Team spreadsheets completed (GL:440–446).

---

## 11. Communication rules (GL:481–506)

- **Slack is the only official channel.** Email and other platforms are not valid corporate
  communication and will not be answered — the sole exception being live onboarding sessions.
- Before asking: check previous threads → check instructions/FAQ → check pinned messages.
- **English only.**
- Avoid DMing Project Team members unless strictly personal; use public threads.
- **Discussing payments is strictly prohibited** in the project channel — route payment
  questions to the `#all-trainer-hub` Slack channel.
  *(Note: `projecthub.md:52` spells this `#all-trainner-hub`; GL:500 spells it
  `#all-trainer-hub`. Confirm the exact handle in Slack.)*
- Only official Project Team members may make announcements; peer support is encouraged but
  is not authoritative.

**Escalation order (screening Q7):** **check the FAQ first → if still unresolved, post a Slack
thread.** Not: post immediately, not: DM a QM, not: wait for the next onboarding session.

### 11.1 Project Team spreadsheets (screening Q5 — select-all)

When the Project Team provides a shared spreadsheet, **do only this**: complete the enabled
contributor-facing columns using the available selection or free-text options, exactly as
specified in official communications.

**Never:**
- Apply a filter — it changes the view **for everyone**, not just you.
- Add or remove rows or columns "to make it easier to work with".
- Delete existing data, including other contributors' email addresses, even when it looks
  obsolete.
- Work in columns reserved for the Project Team.

The principle: it is a shared live document. Do not modify its structure, its existing data, or
anyone else's view.

---

## 12. Where you are in the journey

`Allocation → Channel → Onboarding → Screening → Production → Project Wrap`
(`projecthub.md:22`, `contributor_journey.md:13-15`)

**Phase 1 — Onboarding:** review the Project Hub → complete training materials and guidelines
→ **attend an onboarding session (required for project access**, GL:386) → take the screening.
Screening is completed **independently** and is graded on whether you can apply the guidelines
in practice (`Training & Screening.md:51-59`). Outcome is communicated via Slack; a retake may
be available per the retake policy.

**Phase 2 — Production:** receive credentials → added to **Vercel** and **Feather**
(`contributor_journey.md:48-49`) → claim, produce, submit → organic QC.

**Participation ends** at project wrap, or by removal for performance/behaviour
(`contributor_journey.md:65-70`).

---

## 13. Pre-screening readiness checklist

Operational:
- [ ] LinkedIn **primary** email == invited email (fix at the LinkedIn settings URL above)
- [ ] Vercel email == Feather email == Slack email
- [ ] Onboarding session attended
- [ ] Feather login via LinkedIn tested successfully

Understanding (the screening tests application, not recall):
- [ ] Can name the 4 quality dimensions and what fails each
- [ ] Know the turn range is **10 min / 15 max**, and that the "one turn is fine" text is stale
- [ ] Know the *backtrack-and-rebuild* remedy for a conversation that ends early — never pad
- [ ] Can spot an unselected turn from the green "Continue conversation from here" button
- [ ] Know the claim sequence **including copy-URL-after-claim → paste Attempt URL**
- [ ] Know to resample, not refresh/skip, on a failed response
- [ ] Have 10–15 genuinely distinct real prompts sourced from actual AI history, PII scrubbed

Sourcing prep (do this before, not during, a claimed task — the clock is running once claimed):
- [ ] Exported/opened ChatGPT, Gemini, Claude, Copilot history
- [ ] Shortlisted candidate threads with real 10+ turn depth
- [ ] Confirmed none of them require web/tools/images/files
- [ ] Confirmed no two are paraphrases of each other
- [ ] Scrubbed names, emails, phone numbers, employers, credentials, financials

---

## 14. Open items to confirm with the Project Team

1. **Turn ceiling in prose vs. table** — GL:172 says follow-ups run "up to a total of ten
   turns" while GL:168–170 sets the maximum at 15. Confirm 15 is the ceiling.
2. **`min_turns` task variable** — image10 shows a task-variables panel carrying
   `min_turns: 4` (from an "Interactive - German" batch, image9/image11). If tasks in this
   project expose a per-task `min_turns`, confirm whether it overrides the 10-turn floor or
   whether 10 always governs.
3. ~~**`↳` symbol**~~ — ✅ **RESOLVED** by screening Q6. Selecting on every applicable turn is
   correct but *incomplete* as an answer; the full correct answer requires that **`↳` is
   prefixed to the preferred response** (`↳A B` or `A ↳B`). Treat it as a mandatory
   per-turn verification, and note that "only select where the responses differ substantially"
   and "only select on turns where you continue" are both explicitly wrong.
4. ~~**Attempt URL field**~~ — ✅ **RESOLVED** by screening quiz Q1: the field is on the Vercel
   side and is literally named **`Attempt URL`**.
5. **Slack payment channel handle** — `#all-trainer-hub` vs `#all-trainner-hub`.
6. **Daily quota** — image9 shows counters like `0/10 claims`, `0/10 submits`. Confirm whether
   a per-day claim/submit cap applies here.

---

## 16. Verified against the official screening

The **Operational Workflow** screening section ("The Task-Claiming Procedure", Q1–Q4) has been
cross-checked against this document. Results:

| Q | Tests | Status |
|---|---|---|
| Q1 | Full claim sequence, in order | ✅ Matches §10.2 exactly. Confirms the `Attempt URL` field name. |
| Q2 | Claim **before** copying the URL; confirm "In progress" first | ✅ Matches §10.2 step 3–4. |
| Q3 | "Task not found" handling | ⚠️ **Refined §9** — the answer is *go back to Vercel for another task*, and the cause is that the task's claims are exhausted. Details added above. |
| Q4 | *Why* the order matters | ✅ Matches §10.2 — only correctly claimed and registered tasks are billable. |
| Q5 | Shared spreadsheets | ➕ **New material** → §11.1 |
| Q6 | Preference recording + `↳` | ✅ Resolves open item 3 → §8, §14 |
| Q7 | Support escalation order | ➕ **New material** → §11 |

**Quality Standards section:**

| Q | Tests | Status |
|---|---|---|
| Q1 | Which prompt meets the standard | ✅ Confirms §6 — the messy, unpunctuated career-change prompt wins over the polished ones |
| Q2 | Preferred sourcing method | ➕ **Two new banned methods** (exam questions, online-sourced queries) → §6.1 |
| Q3 | Variety across tasks | ✅ Confirms §6; adds "plan your contributions as a whole" |
| Q4 | Model capabilities | ✅ Confirms §3 — and clarifies pasted text ≠ file upload → §3.2 |
| Q5 | Trivial prompts | ➕ Authentic-but-thin still fails → §6.2 |
| Q6 | Follow-up quality | ➕ **Turns must be causally dependent, not just on-topic** → §3.1 |
| Q7 | **Stopping rule** | ✅✅ **Definitively settles the 10–15 conflict** → §5.0. Extend/rework at turn 6; stop at turn 11. Filler never correct. |
| Q8 | PII in a good history prompt | ✅ Confirms §3 — scrub and use it |

**Overall pattern across both sections:** the screening consistently rewards the answer that is
*more work* — rework earlier turns rather than pad, go back to Vercel rather than grab a Feather
task, scrub and reuse rather than discard, read both responses fully rather than heuristic-pick.
Every "efficient shortcut" option is a wrong answer.

**Pattern worth noting:** all four operational-workflow questions test the claim/URL/billing
sequence, and the two hardest distractors are (a) copying the URL *before* claiming and
(b) sourcing a replacement task directly from Feather. Both are the "resourceful shortcut"
answers. The screening is built to catch exactly the person who reads the prose and skips the
flowchart.

---

## 15. The single most important thing

The project's entire value rests on the prompts being **genuinely yours**. Two separate rules
(GL:101 LLM-generated prompts; GL:180 shared writing patterns across contributors) make
AI-assisted prompt writing a **removal offence**, and stylometric similarity is detectable
across unrelated topics.

**Practical consequence: do not use an AI assistant — including this one — to write, polish,
rephrase, or "improve" any prompt or conversation turn you submit.** Use AI to understand the
guidelines and to organise your workflow; write every submitted word yourself, in your own
voice, typos and all. That is not a limitation of the task — it is the task.
