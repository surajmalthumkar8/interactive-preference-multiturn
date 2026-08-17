# AUTHENTICITY RULES — voice, sourcing, and the humanization gate (BINDING)

Scored dimension #2: **Human Authenticity** (GL:99–103). It reads like *you* actually typed it.
Grammar and polish are explicitly **not** wanted.

---

## 0. Standing instruction — the policy position as of 2026-08-14

**AI-assisted drafting is allowed.** Per the leadership Slack update reflected in the callout at
the top of `MAI Interactive — Multi-Turn Guidelines (updated 08_12).md`, AI tools including
Claude Code may help write prompts and turns for this project.

**The condition is absolute: every AI-assisted word must be humanized before it enters Feather.**
It has to read like something Suraj would genuinely type, typos and all.

Two things did **not** change:

1. **Sourcing preference order still stands** (GL:209): **reuse > adapt/expand > invent.** Real
   history beats a well-constructed invention every time. AI assistance supplements the
   methodology; it does not replace it.
2. **GL:180 stylometry detection still stands.** "We actively look for shared writing patterns
   across experts." A uniform assistant voice applied consistently across tasks is itself the
   risk — not just individual AI tells. See §4.

> If the live platform or a later Slack post contradicts this, the platform wins. This callout
> is Suraj's report of a Slack update, independently unverified. Flag any mismatch before
> submitting.

---

## 1. Sourcing (GL:207–213 + screening Quality Standards Q2)

**Step one, always:** open ChatGPT / Gemini / Claude / Copilot history and search for something
genuinely asked. Copy it *exactly as written*, then scrub personal details.

If there is no history, use something genuinely needed **right now**: a task put off, an unmade
decision, a message still owed, a document or codebase actually being worked on, something that
recently caused frustration.

### The four banned sourcing methods

| Method | Verdict |
|---|---|
| Ask an AI to generate a realistic-sounding prompt and paste it unchanged | ❌ Under the old rule this was a removal offence. Under the new policy AI may *help draft*, but pasting raw model output is still wrong — it must be humanized and it must be grounded in a real need of Suraj's. |
| Paste questions from exams, quizzes, or educational materials | ❌ **Screening-only rule — not in the guidelines** |
| Take an interesting query found online that isn't your own actual AI use | ❌ **Screening-only rule — not in the guidelines** |
| Reuse a history conversation very similar in topic/approach to one already submitted | ❌ Duplicate-adjacent (GL:56 — removal) |

The single correct method: **own history → pick one meaningfully different from what's already
submitted → scrub PII → paste into Feather → continue naturally.**

### Authentic is necessary but not sufficient (screening Q5)

*"should i get organic berries?"* is real, and it is the **wrong** answer — marked the least
useful contribution because it is intentionally minimal. The bar is two-part: **genuinely yours
AND substantial enough to sustain 10–15 turns.**

*(Note the tension with the published example list, which includes that exact prompt as a
sample of real voice. Resolution: it is a fine illustration of **register**, and an unusable
**task opener**, because it has no depth. Imitate its texture, never its scope.)*

### No placeholders, ever

If a prompt references an email, code, notes, or a document, **the full real text goes in**.
Never `[paste context here]`. Do not tidy the pasted material, do not trim it, do not reformat
it. The prompt must be self-contained and answerable on its own (GL:211–213).

---

## 2. The voice target

Full calibration corpus: `../knowledge/HUMAN_VOICE_CORPUS.md`. Read it before writing, every
time. The distilled fingerprint:

- **Openers acknowledge, never thank.** "I like the short one better." / "This is close." /
  "Perfect. One last thing," / "This works." / "This looks good, but" / "Yes this is mostly for
  walmart but". **Zero instances of "thanks", "thank you", greetings, or praise of the
  assistant appear anywhere in the corpus.**
- **Concrete, incremental asks** — one or two changes per turn.
- **They quote and push back**: "don't say 'gotta'" / "You specified 'globally', wasn't only one
  launch?"
- **No composed formatting** in anything you author — no bullets, no numbered lists, no bold, no
  colon-then-list. Plain sentences. (Pasted material keeps whatever shape it already had.)
- **No em dashes, no semicolons, no "delve / moreover / furthermore / it's not just X, it's Y"** —
  none appear in any real user turn.
- **Endings are quiet** — the last turn narrows to one small ask, then it just stops.

### Register: pick one per turn and stay inside it

| Situation | Shape |
|---|---|
| Quick factual lookup | 2–8 words, maybe a doubled `??` |
| Homework / puzzle with stakes | run-on, "helppp", parenthetical aside |
| Personal decision, unresolved | 60–130 words, no punctuation discipline, real emotion |
| Handing over content | short framing + untrimmed paste |
| Work task in a known domain | jargon with no gloss, typos, "list them" |
| Considered ask with tone constraints | 30–50 words, tidy, one concrete constraint |
| Follow-up inside a conversation | 16–66 words (median 35), reacts to a specific thing said |

**Mixing careless and careful inside one message is the tell.**

---

## 3. Imperfections: omission class only

| Allowed — omission class | Banned — corruption class |
|---|---|
| dropped apostrophes ("thats", "theyre") | injected letter noise ("helppp" unless genuinely how you type) |
| lowercase sentence starts, lowercase "i" | doubled or transposed letters added on purpose |
| missing terminal punctuation | misspellings invented to look human ("explaination") |
| missing commas, comma splices, run-ons | any "typo" you had to think about |
| fragments, trailing-off sentences | cartoonish mess |

The published examples *do* contain corruption-class typos ("theyre", "helppp", "embedd",
"Recqnroll", "explaination", "coping", "fro tracking") — because those were **real slips by real
people**. The distinction that matters: **naturally occurring vs deliberately injected**.
Deliberately injected typos are their own fingerprint and are exactly what stylometry catches.

**Practical rule when AI drafted the text:** strip AI polish; do not add fake damage. Let
Suraj's own typing supply the mess — the safest humanization pass is Suraj retyping the draft
rather than pasting it.

---

## 4. Stylometry — the fingerprint risk (GL:180, removal offence)

> "We actively look for shared writing patterns across experts. If submissions from different
> contributors show a distinctive and recognizable way of writing, even across completely
> different topics."

A consistent AI voice across a portfolio is detectable **across unrelated topics**. So:

- Vary sentence rhythm and punctuation habits **turn to turn and task to task**.
- Never reuse a signature phrasing pattern (a favourite opener, a recurring connective, an
  identical acknowledge-then-ask shape).
- Track what has been spent in `../learning/PROMPT_LOG.md` — register, length band, opener
  shape, imperfection pattern — and deliberately rotate.
- The same applies to the optional **reason** field on the preference selection: vary the
  wording, never template it.

---

## 5. The humanization gate (mandatory, every single turn)

Standing instruction from Suraj — not optional, not a one-time pass:

1. **Check the draft against the doc's own style rules first** — Golden Rule (~GL:180),
   Quick Tips (~GL:209), and the example-prompt table (~GL:194–205).
2. **Run the `humanizer` skill on every turn**, opening prompt and follow-up alike. The skill
   travels with this repo at `.claude/skills/humanizer/`.
3. **Vary phrasing and rhythm** across turns and across task sessions.

The humanizer must **never**:

- touch pasted content (no tidying, trimming, reformatting),
- introduce a capability breach (`CAPABILITY_RULES.md`),
- change what the turn asks for — voice only,
- add an em dash, a semicolon, a list, or a thank-you.

Output of every drafting step carries `HUMANIZATION: PASS` or the turn does not ship.

---

## 6. Safety — scrub, don't discard (GL:117–123, screening Q8)

PII, sensitive personal data, and confidential material are a **removal offence** if submitted.
When a genuinely good history prompt contains a client name, an email address, and confidential
details, the correct action is to **replace or remove the sensitive information and use it** —
not to discard the prompt, and not to submit it with a disclaimer attached.

Scrub before drafting, not after: names, emails, phone numbers, addresses, employer names,
credentials, account numbers, financial figures tied to a real person, health details, anything
under NDA. Replace with plausible substitutes that keep the prompt answerable — the mess stays,
the identity goes.
