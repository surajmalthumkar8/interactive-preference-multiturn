# HUMANIZED PROMPTING — evidence base (binding)

Research brief distilled 2026-07-30 (full citations in `../learning/RESEARCH_BRIEF.md`
appendix). Suraj's directive: humanized prompting is the most important part of this
project. This file is the *evidence* behind the rules; `../rules/AUTHENTICITY_RULES.md`
is the rule text. Read both.

## The single most important finding

**At 10–35 words, statistical AI detection does not work.** Detectors need ~120 words
to reach potential, ~200 for GPT-4-class text; texts under 100 words show ~40% higher
false-positive rates. At single-sentence length detection can *invert* — one study
found real human short answers scored **74.1%** "LLM-like" vs **68.6%** for actual LLM
output.

So the grader is **not a classifier. It is a human applying folk heuristics.** That
changes what to optimize. Perplexity, burstiness, sentence-length variance and lexical
diversity are all **inoperative at our length** — do not spend a single moment on them.

## The only four things that carry the signal in a short prompt

1. **Word length / lexical plainness.** Average word length is the *dominant*
   discriminator on short texts once other features are controlled. Prefer
   Anglo-Saxon monosyllables to Latinate abstractions: "check" not "verify", "use" not
   "leverage", "fix" not "remediate", "get" not "obtain".
2. **Opener shape.** Real queries are question-word-initial, imperative, or a fragment.
   Measured frequencies, real vs LLM-synthetic queries:

   | Token | Real user queries | Synthetic |
   |---|---|---|
   | "what" | **7.14%** | 3.75% |
   | "how" | **4.42%** | 1.12% |
   | "is" | **4.76%** | 2.25% |
   | "the" | 2.38% | **5.62%** |

   Real = short, direct, question-word-first. Synthetic = longer, leaning on
   determiners and noun-phrase scaffolding. **Never open with "I'm looking for...",
   "Could you kindly...", "I would appreciate it if..."**
3. **Affect / stance.** This is the **most mimicry-resistant dimension** measured, across
   nine models and three platforms. LLMs are reliably more formal, more positive, more
   motivational; humans carry **negative emotion** and personal reference. One word of
   real attitude — annoyed, skeptical, unsure, picky, impatient — is the strongest
   single lever available.
4. **Punctuation completeness.** Presence or absence of a terminal mark and a
   sentence-initial capital. Decide **per message**, never by a standing rule.

Everything else (structure, cleverness, injected noise) is either neutral or harmful.

## CORRECTION to our imperfection rule — omission, not corruption

**Deliberately inserted typos are their own detectable fingerprint.** Detection
research canonicalizes the text and measures the edit distance back to it; the
*pattern of the discrepancy* becomes a classifier feature (82.6% true-positive rate at
1% false-positive, vs 48.8% for standard methods). Separately, the humanizers that
survive detection are the ones that restructure sentences "**without introducing
awkward typos or forced errors**."

Real human error is overwhelmingly **omission**, not character corruption:

| ✅ Omission class — authentic | ❌ Corruption class — reads injected |
|---|---|
| lowercase sentence start, lowercase "i" | transposed letters ("teh", "hte", "recieve") |
| missing terminal period | doubled letters ("helppp"), random capitals |
| dropped apostrophe (dont, im, whats, thats) | homoglyphs / unicode lookalikes |
| dropped article or function word | misspelling a *rare* word (people just avoid the word) |
| comma splice, run-on, trailing off | more than one error in a 20-word message |
| fragment instead of a full sentence | the same error type in every message |

Rate calibration from real corpora: SMS to friends runs ~25% nonstandard tokens (the
largest single category being **omitted capitals**; of messages where an apostrophe was
possible only **43%** used it correctly). Real consumer health queries run 2–11% token
error rate. But AI-directed prompts sit *between* SMS and composed prose — so:

> **A 20-word message supports 0–2 omission-class deviations, and a plurality of our
> messages should have ZERO overt errors while still being informal.**

Note: the client's own guide examples do contain corruption-class typos ("helppp",
"explaination", "theyre"). Those are genuine artifacts of real typing. **We do not
manufacture them** — we use the omission class, which is both more common in real data
and not a detection signature. This is the one place where we deliberately do not
imitate the guide's examples character-for-character.

## Anti-fingerprinting is our real exposure

A single short message is near-undetectable (~80% at best). **Concatenate 10 messages
from the same author and detection goes to ~100%.** Corpus-level uniformity is what
kills us, not any individual message.

Behavioral-biometrics research on 20,680 real prompts from 1,034 users found the
"**uniqueness–consistency paradox**": real users are highly distinctive across the
population yet behaviorally **inconsistent across contexts**. Identity lives in
habitual **word choice** (lexical/surface features beat semantic encoders), and it
survives minor lexical perturbation but degrades under semantic paraphrase.

**Automated generation inverts the human pattern.** Humans: stable lexicon, unstable
structure. Machines: varied vocabulary, uniform structure. Therefore:

> **Keep a consistent small vocabulary and voice. Vary everything structural.**

Vary across our message set: length (spread 8–35 words, right-skewed), opener class
(question word / imperative / fragment / reaction), terminal punctuation present or
absent, politeness present or absent, error present or absent, question vs statement.
**Never let one imperfection type become a signature — uniform imperfection is a
stronger fingerprint than no imperfection at all.**

## Length converges with our platform constraint

Real prompt length, LMSYS-Chat-1M (1M conversations, 210k unique IPs): **median ~23
tokens**, mean 69.5 (heavily right-skewed). WildChat: mean 2.52 turns, only 3.7% of
conversations exceed 10 turns.

Our 15–30 word rule (forced by the platform erroring on longer prompts) lands **almost
exactly on the real-world median.** The constraint and authenticity point the same way.
Also note: mean turns ≈2.0–2.5 in both datasets — short conversations are the norm,
which independently supports the 07-28 guide's "a single turn is completely valid".

## Two traps to avoid

1. **The filler trap.** LLMs use "so", "well", "like", "anyway" *incorrectly* —
   misused coordination markers are a documented **LLM** signature, not a human one.
   Never sprinkle filler decoratively. Use a discourse marker only where it does real
   work (contrast, resumption, concession), preferably turn-initially in reaction to
   what was just said.
2. **The mirroring trap.** Do **not** echo the assistant's own phrasing back at it —
   exaggerated alignment that grows over a conversation is an LLM tell. This refines
   our anchoring rule: anchor by **reacting to or quoting a specific claim**, not by
   adopting the response's vocabulary. Quoting "you said copays may or may not count"
   is right; absorbing its register is wrong.

Related: politeness in real logs is **front-loaded then decays** — sustained uniform
politeness across every turn is unhuman. (We already ban thanks/praise outright.)

## Expanded ban list (with measured excess frequencies)

From a study of >15M PubMed abstracts measuring post-ChatGPT frequency against a
counterfactual baseline: **delves 28.0×**, **underscores 13.8×**, **showcasing 10.7×**.
379 excess style words identified in 2024.

The practitioner catalogue is **time-stratified** and shrinking as models get tuned
against it — 19 flagged words in 2023, down to four by mid-2025 (*emphasizing, enhance,
highlighting, showcasing*). **Re-check the list roughly every six months.**

New ban categories this brief added, now in the validator:
- **Copula avoidance:** serves as, stands as, marks, functions as, represents, boasts,
  features, offers — used where a plain "is/are" belongs.
- **Additional vocabulary:** bolstered, garner, interplay, landscape, navigate,
  resonate, commendable, align with, meticulous(ly), insights, notably, particularly.
- **Superficial -ing analysis:** a trailing participial clause making a vague impact
  claim ("..., highlighting the need for...").
- **Double hedging:** "might potentially", "could possibly".
- **Self-narration:** "As you mentioned earlier", "To clarify my earlier point".

## Honest limits of this evidence

- The best *quantitative* markers come from **academic prose**, not chat. The big chat
  corpora publish scale statistics but almost no style statistics — there is no
  published typo rate, capitalization rate, or terminal-punctuation rate for LLM prompt
  logs. SMS and medical-query corpora were substituted; both sit in a different
  register. **Treat all rate numbers as order-of-magnitude, not calibration targets.**
- Perplexity/burstiness numbers circulating online (human 80–100 vs GPT-4 20–30;
  burstiness 0.6–1.2 vs 0.2–0.4) trace to **vendor and SEO sources, not peer review**.
  Directionally plausible, numerically unverified. Irrelevant at our length anyway.
- **Sources genuinely disagree** on: whether em dashes are diagnostic (aggregate yes,
  individually "more art than science"); whether LLMs reduce stylistic variance (some
  say tight clustering, one benchmark says they shift the centroid while keeping
  dispersion); and whether typos help or hurt (they fool current detectors but are
  specifically targeted by canonicalization methods and by human readers who also
  attribute *bad* grammar to AI).
- **Human graders are near chance overall** — 49.9–57.9% on AI-text identification,
  experts ~70%. Their heuristics are internally contradictory: they call text AI for
  being *too perfect* AND for having bad grammar. The moves that satisfy both
  competing heuristics are: **plain concrete words, real attitude, direct ask** — none
  of which require any error at all.
- Our signed-off gold examples are better evidence than any of this for our specific
  rubric. Where they conflict, the gold examples win.
