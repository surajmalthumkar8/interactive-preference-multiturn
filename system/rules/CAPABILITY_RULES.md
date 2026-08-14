# CAPABILITY RULES — what the model under test cannot do (BINDING, BLOCKING)

A hard filter on **every user-side message**, opening prompt and follow-up alike. A prompt that
assumes an unsupported capability makes both responses fail the same way, so the pairwise
comparison carries **zero information** and the task is wasted (PROJECT_KNOWLEDGE.md §2).

This is scored dimension #1: **Prompt Capability Alignment** (GL:60–123).

---

## 1. The four stated limits (verbatim from the guidelines)

> **This model does not have web search and cannot access real-time information. The model
> cannot receive file uploads or generate images.**

1. **No web search** — it cannot look anything up.
2. **No real-time / current information** — no live prices, weather, news, scores, quotes,
   "today", "right now", "latest version as of".
3. **No file uploads** — it cannot open, read, or receive an attached file.
4. **No image generation** *(and no image input)* — it cannot make, edit, or look at a picture,
   screenshot, diagram, or chart.

## 2. The fifth limit — stated only on the live task, not in the guidelines

> **The model's knowledge cuts off in July 2025.**

Seen on the live task intro (campaign `[general-multi-turn]`), absent from the written
guidelines. So a prompt fails capability alignment not only when it asks the model to *fetch*
something, but also when it **depends on anything that happened after July 2025** — a library
release, a product launch, an election, a rule change, a price level, a sports result.

**Check recency as well as tool use.** Today is well past the cutoff; anything you personally
learned this year is suspect.

---

## 3. Banned prompt shapes

The guidelines' own examples:

- "search the web for…"
- "look at this image…"
- "open this file…"
- "what is the weather like today"
- "open this URL"
- "what happened yesterday in the news"

Extended ban list — same failure, other wording:

- "check / look up / google / find online / browse to…"
- "what's the current price of…", "how much does X cost right now"
- "what's the latest release of X", "as of today", "this week's…", "trending"
- "here's a link, read it" — any bare `http://` / `https://` handed over **to be fetched**
  (a URL quoted as text inside pasted content is fine)
- "I've attached…", "see the attached", "the file I uploaded", "this PDF", "this spreadsheet",
  "this screenshot", "the image above"
- "generate / draw / make me an image, logo, diagram, chart, mockup, picture"
- "what do you see in this", "describe this photo"
- anything whose correct answer changed after **July 2025**
- anything whose correct answer would change between yesterday and today

---

## 4. What is still fine — do not over-filter

- **Pasting content directly into the message.** Actively encouraged (GL:188, GL:211):
  a whole email thread, a block of code, a contract excerpt, meeting notes, a long document.
  Screening Q4 accepts *"Here are notes from three team meetings, can you identify the open
  action items? [notes]"*. **Paste, don't point.**
- **Stable factual knowledge** — how compound interest works, what a quick ratio is, what
  mitosis is, standard library behaviour, how a deductible interacts with an out-of-pocket max.
- **Named real products and companies as stable facts** — "Clash Royale", "walmart", "netbeans",
  "n8n". Asking *about* them is fine; asking for their *current* state is not.
- **Code, math, writing, planning, explaining, brainstorming** — all unaffected.
- **Describing an image in words** instead of showing it ("the chart shows revenue flat for
  three quarters").

### The paste/upload distinction, stated plainly

| | |
|---|---|
| Text of a document **inside** the prompt | ✅ allowed and encouraged |
| A reference to a document the model must open | ❌ capability breach |

---

## 5. The conversion rule — how to rescue a banned prompt

Almost always: **paste instead of point**, or **drop the time anchor**.

| Banned | Rescued |
|---|---|
| "read this article at \<url\> and summarize it" | paste the article text, then "pull out the key points" |
| "look at this error screenshot" | paste the traceback as text |
| "what's the current mortgage rate" | "if I'm looking at a rate around 6.5 percent, how does…" |
| "what's the latest pandas syntax for X" | "how do I do X in pandas" (stable API question) |
| "make me a diagram of this flow" | "describe the flow as a numbered list I can draw myself" |
| "is the new version of X out yet" | "here's how we use X today [paste], what would you change" |

---

## 6. Where this is enforced

- `mt-topic-scout` — rejects a candidate topic that cannot survive 10 turns without tools or
  post-cutoff facts. Turns 8–15 are where a topic quietly drifts into "what's the latest…".
- `mt-turn-writer` — self-checks every draft before returning; reports CAPABILITY CHECK.
- `mt-humanizer` — must not *introduce* a breach while rewriting (never turn "here's the code"
  into "here's my file").
- `mt-compliance-auditor` — independent re-check of every turn; a breach is an automatic BLOCK.
- `Interactive_contri_inst/tools/validate_sxs_turn.py` — mechanical pattern check (legacy tool,
  still valid for this rule; see `../../Interactive_contri_inst/LEGACY_README.md`).

Also applies when **judging**: if a response promises to browse, open a file, or produce an
image, that is a factual defect in the response and counts against it under
`PREFERENCE_RULES.md` step 1.
