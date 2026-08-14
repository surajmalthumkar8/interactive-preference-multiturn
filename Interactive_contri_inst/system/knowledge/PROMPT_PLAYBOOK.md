# PROMPT PLAYBOOK — authentic prompt seeds + rotation discipline

Used in DO_TASK MODE START when Claude must supply the opening prompt.
**Rewritten 2026-07-28** for the revised contributor guide.

Goal: every task opens with a genuinely everyday prompt, and no two tasks look alike
in topic, complexity, length, or style. Log every used prompt in
`../learning/PROMPT_LOG.md` (date, task id, category, length band, turn count,
opening line) BEFORE delivering.

## Sourcing order (NEW — the guide is directive about this)

The 07-28 guide does not say "feel free to reuse history". It says open it **right
now**:

> "Open your ChatGPT, Gemini, Claude, or Copilot conversation history right now and
> find things you genuinely asked. Copy them over but make sure you scrub any
> sensitive details first. Real past interactions are far more valuable than anything
> you invent on the spot."

So the order is:

1. **Suraj's own real AI history.** If he pastes or describes something he actually
   asked an assistant, that is the prompt — scrub PII, otherwise leave it alone,
   including its typos and its mess. This beats anything we compose. **Ask for it when
   starting a fresh task** ("anything you actually asked ChatGPT recently?") before
   falling back to generation.
2. **A real current need of his**, per the guide's fallback list: something he has been
   putting off, a decision he hasn't made, something that frustrated him recently, a
   message he still needs to send, or a document/code/project he is already working on.
3. **Composed from a seed below** — last resort, and it must still pass every
   authenticity and capability gate.

## Capability filter (BLOCKING, applies before anything else)

Every candidate prompt is checked against `../rules/CAPABILITY_RULES.md`. No web
search, no real-time info, no file uploads, no image generation or image reading.
When a genuine past prompt trips this, convert it (paste instead of point; drop the
time anchor) rather than discarding it.

## Rotation rule (binding — now four axes, not one)

Pick the combination least-recently used in PROMPT_LOG, across ALL of:

| Axis | Values to rotate |
|---|---|
| **Domain** | writing · coding · summarizing/explaining · brainstorming · planning · personal decision · money/admin · learning |
| **Complexity** | quick lookup · single concrete task · multi-step problem · open-ended dilemma |
| **Length band** | micro (1–8 w) · short (9–45 w) · rambling (45–120 w) · pasted-context (unbounded) |
| **Turn count** | 1 · 2–3 · 4–6 · 7–10 |

The guide: "A mix of quick single-question lookups, multi-step problems, personal
situations, and professional tasks makes the dataset far more useful than a set of
similar prompts." **Deliberately ship some one-turn micro tasks.** Our first three
tasks were all short-prose, 3–4 turn, professional — that is exactly the monoculture
this rule exists to break.

Within an axis value, never reuse a scenario, artifact type, or named detail already
in the log.

## Categories and seed shapes

Each seed is a SHAPE, not a script. The turn-writer instantiates it with fresh,
concrete, scrubbed-real details; the humanizer sets the register.

### 1. Writing help (§A task-1)
Rework a real message: cancel/reschedule, decline an invite, chase a landlord or
neighbour, ask a manager for something — with tone constraints ("honest but not
dramatic"). Improve an email / cover letter / profile blurb. Arc: draft → tone tweak →
concrete detail → shorter version.

### 2. Coding (§A task2, task6 · §B #7, #11, #13, #14, #15)
Paste a raw error/traceback or a broken function with almost no prose. "Why does this
return None". Practical decisions: make this query faster, which embedding approach
for 500k rows, how do I do X in this IDE. Paste the code untrimmed. Arc: fix →
extend → "give me the service/util for X" → edge case.

### 3. Summarizing / explaining (§B #1, #3, #8, #12)
"mitosis??" · quote a definition and ask what it means for your situation · paste
meeting notes and ask for the action items and owners · paste a document and ask for
a mechanical transformation. Arc: explain → challenge or narrow → apply it.

### 4. Brainstorming
Offsite ideas, saving on groceries, a gift under a budget, weekend options, what to
cook. Arc: options → constrain → pick one and go deeper → concrete artifact.

### 5. Planning / productivity (§A task4, task5)
Weekly routine, tomorrow's workday around real priorities, study plan around a
deadline. The "ask me a few questions first" opener guarantees a real exchange.
Arc: plan → revise one preference → convert format.

### 6. Personal decision / dilemma (§B #4, #5, #6) — NEW, underused by us
Career switch doubts, a landlord letter, negotiating a contractor quote, whether a
bootcamp is worth it. These carry real stakes and rambling register. High value:
they are the guide's own showcase examples and we have shipped zero of them.

### 7. Quick lookup (§B #1, #10) — NEW, underused by us
"should i get organic berries?" · "mitosis??" · one-line consumer or factual
questions. **These are explicitly endorsed and may be a complete task at one turn.**
Do not inflate them into multi-turn conversations to look thorough.

## Persona discipline

Stay ONE plausible person per task (a working professional who codes a bit, plans
their week, texts friends, deals with landlords and contractors). Details are
generic-real: "a friend", "my teammate", "Saturday", "9 to 6", "we're in seattle".
Never real names, employers, addresses, or anything from Suraj's actual life/PII —
including inside pasted content. Company names as public consumer facts are fine.

## Prompt quality bar (all must hold)

- Would a person actually type this into ChatGPT on a Tuesday? (No trick questions,
  no benchmark puzzles, no artificial difficulty.)
- Does it pass `CAPABILITY_RULES.md` — no search, no live data, no file, no image?
- Does it carry at least one concrete personal detail that makes it real?
- Is the length band chosen deliberately, and different from recent tasks?
- If it is a lookup, are we prepared to END at one turn rather than pad it?
- If it references content (email, code, notes, document), is that content **pasted
  in full and untrimmed**, with no placeholders?
- Is it in the right register for the situation, per HUMAN_VOICE_CORPUS §B?
