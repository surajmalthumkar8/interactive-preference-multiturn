# PROMPT SPECTRUM — the client's own category examples (binding)

Source: the client's "**The Spectrum of Authenticity: Bring Your Real Life to the
Chat**" slide, supplied by Suraj 2026-07-30. This is the client showing exactly what a
good prompt looks like per category, so it outranks anything we invented.

Slide headline: *"Real prompts are messy and context-heavy. A mix of quick
single-question **lookups**, **multi-step problems**, and personal situations makes the
dataset infinitely more valuable."*

## The five categories, with the client's own examples verbatim

| Category | Client example | Words |
|---|---|---|
| **Technical / Coding** | "I'm getting a weird race condition in my async Node.js code. The callback fires before the DB write completes, but only sometimes. Here's the relevant chunk: [paste]." | 27 |
| **Personal / Situational** | "I'm trying to negotiate a contractor quote down from $18,000 to $12,000. The work is fence, shower, fridge prep. What's a good approach?" | 24 |
| **Writing / Professional** | "I need to tell my landlord our lease broke down but I want to sound firm without being rude. Here's the draft: [paste]." | 23 |
| **Creative / Brainstorming** | "I'm naming a new product line, we want something that evokes ancient history and discovery, like Petra or Olympia. What else fits that vibe?" | 24 |
| **Explaining Concepts** | "My doctor mentioned I might have elevated cortisol. What does that actually mean for day-to-day health?" | 17 |

**Pro-Tip panel on the slide:** *"Reuse Your History! You are highly encouraged to
copy-paste your genuine past conversations from ChatGPT, Gemini, Claude, or Copilot.
(Just scrub sensitive and confidential info first.)"*

## What this slide settles

1. **Length: every single client example is 17–27 words.** Not one is a paragraph. This
   is the target shape, and it matches the platform's measured behaviour (prompts over
   ~35 words error out — see AUTHENTICITY_RULES). "Messy and context-heavy" in the
   headline means **one real concrete detail**, not volume.
2. **The shared skeleton of all five:** *situation in one clause → the specific
   detail/number/constraint → a plain direct ask.* That is the template.
   - situation: "I'm trying to negotiate a contractor quote"
   - detail: "down from $18,000 to $12,000... fence, shower, fridge prep"
   - ask: "What's a good approach?"
3. **Concrete specifics carry the authenticity**, and they are always ordinary-real:
   real dollar figures, a named technology (async Node.js), a named comparison (Petra,
   Olympia), a real-life trigger ("my doctor mentioned"). Never a generic placeholder.
4. **`[paste]` goes at the END**, introduced by a short lead-in ("Here's the relevant
   chunk:", "Here's the draft:"). The prose stays one or two lines regardless. Keep the
   pasted block itself small — the platform's length limit applies to the whole message.
5. **The ask is blunt.** "What's a good approach?" / "What else fits that vibe?" /
   "What does that actually mean for day-to-day health?" No hedging, no politeness
   scaffolding, no multi-part compound questions.
6. **"Lookups" are explicitly valued** — a quick single-question prompt is not low
   effort. It is one of the three named ingredients of a valuable dataset.

## Rotation across the five categories

Log every task's category in `../learning/PROMPT_LOG.md` and rotate. Our history:
- Technical/Coding — task 33 (3gb csv / pandas RAM) ✓
- Personal/Situational — task 3154 (repair vs junk a 2013 car, $2,800 transmission) ✓
- Writing/Professional — **not yet used** (highest priority next)
- Creative/Brainstorming — task 977 (dad's 60th gift) ✓
- Explaining Concepts — task 172 (deductible vs out-of-pocket max) ✓

All five categories are now used except Writing/Professional. Take it next, and take it
as a **micro / lookup / 1-turn** task if the scenario allows — that closes two open gaps
at once (see PROMPT_LOG's standing gaps). Do not reuse the slide's own landlord-lease
scenario.

Do not reuse a client example's own scenario (contractor quote, landlord lease,
cortisol, product naming, Node.js race condition). Same SHAPE, different situation.

## Capability reminder (interacts with this slide)

The Technical and Writing examples both hand over content with `[paste]` — they do NOT
attach a file or link to one. That is the pattern: **paste, never point.** The model
has no web search, no real-time data, no file uploads, no images
(`../rules/CAPABILITY_RULES.md`).
