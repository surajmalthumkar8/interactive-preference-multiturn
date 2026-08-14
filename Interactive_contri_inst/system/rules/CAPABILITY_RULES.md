# CAPABILITY RULES — what the model under test cannot do (binding, BLOCKING)

New in the 2026-07-28 contributor guide ("Model capability note — please read").
This is a **hard filter on every user-side message we write**, opening prompt and
follow-up alike, and a blocking gate in the validator, the reviewer-simulator and the
final-evaluator. A prompt that assumes an unsupported capability wastes the task.

## The four limits (verbatim from the guide)

> **This model does not have web search and cannot access real-time information. The
> model cannot receive file uploads or generate images.** Please make sure your
> prompts do not assume any of these capabilities.

1. **No web search** — it cannot look anything up.
2. **No real-time / current information** — no live prices, weather, news, scores,
   stock quotes, "today", "right now", "latest version as of".
3. **No file uploads** — it cannot open, read, or receive an attached file.
4. **No image generation** (and no image input) — it cannot make, edit, or look at
   a picture, screenshot, diagram, or chart.

## Banned prompt shapes (the guide's own examples)

- "search the web for..."
- "look at this image..."
- "open this file..."
- "what is the weather like today"
- "open this URL"
- "what happened yesterday in the news"

## Extended ban list (same failure, other wording — treat as FAIL)

- "check / look up / google / find online / browse to..."
- "what's the current price of...", "how much does X cost right now"
- "what's the latest release of X", "as of today", "this week's...", "trending"
- "here's a link, read it", any bare http:// or https:// URL handed over to be
  *fetched* (a URL quoted as text inside pasted content is fine)
- "I've attached...", "see the attached", "the file I uploaded", "this PDF",
  "this spreadsheet", "this screenshot", "the image above"
- "generate / draw / make me an image, logo, diagram, chart, mockup, picture"
- "what do you see in this", "describe this photo"
- Anything whose correct answer would change between yesterday and today.

## What IS still fine (do not over-filter)

- **Pasting the content directly into the message.** The guide actively encourages
  this: an entire email thread, a block of code, a contract excerpt, a meeting
  transcript, a long document. The rule is "paste it, don't reference it".
  "Here are the notes from our last three team syncs [long context pasted]" is a
  guide example — that is a paste, not an upload.
- **Stable factual knowledge** — how compound interest works, what a quick ratio is,
  what mitosis is, standard library behavior, how a deductible interacts with an
  out-of-pocket max. None of that needs live data.
- **Named real products and companies as stable facts** — "Clash Royale", "walmart",
  "netbeans", "n8n". Asking *about* them is fine; asking for their *current* state is
  not.
- **Code, math, writing, planning, explaining, brainstorming** — all unaffected.
- **Describing an image in words** instead of showing it ("the chart shows revenue
  flat for three quarters") is fine.

## The conversion rule (how to rescue a banned prompt)

A prompt that trips this filter is almost always rescued by **pasting instead of
pointing**, or by **removing the time anchor**:

| Banned | Rescued |
|---|---|
| "read this article at <url> and summarize it" | paste the article text, then "pull out the key points" |
| "look at this error screenshot" | paste the traceback as text |
| "what's the current mortgage rate" | "if I'm looking at a rate around 6.5 percent, how does..." |
| "what's the latest pandas syntax for X" | "how do I do X in pandas" (stable API question) |
| "make me a diagram of this flow" | "describe the flow as a numbered list I can draw myself" |

## Where this is enforced

- `sxs-turn-writer` — must self-check every draft against this file before returning.
- `sxs-humanizer` — must not introduce a capability assumption while rewriting
  (e.g. do not turn "here's the code" into "here's my file").
- `tools/validate_sxs_turn.py` — mechanical FAIL on the banned patterns.
- `sxs-reviewer-simulator` and `sxs-final-evaluator` — independent re-check; a
  capability breach is an automatic REJECT / DO-NOT-SHIP.
- Also applies when judging: if a **response** promises to browse, open a file, or
  produce an image, that is a factual defect in the response and counts against it
  under PREFERENCE_RULES Tier 1.
