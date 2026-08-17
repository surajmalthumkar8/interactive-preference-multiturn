# HUMAN VOICE CORPUS — real user turns, verbatim

The voice target for every prompt and follow-up. The humanizer's test: **would this turn blend
in here without standing out?**

Three sections, all binding:

- **§A** — six signed-off reference transcripts (`Interactive_contri_inst/reference_tasks/`).
  Tidy register. The best model for *follow-up* turns inside a considered conversation.
- **§B** — the example prompts published in the contributor guide as "drawn from real user
  conversation history". Rougher and often longer. It is the client's own illustration of what a
  prompt *may* look like. Seven of these fifteen are reproduced verbatim in the **current 08-12**
  guidelines' Example Prompts table (marked ★); the rest come from the 07-28 revision, whose
  *voice* guidance was carried forward unchanged even though its turn counts were not.
- **§C** — the three worked "why it works" examples added in the 08-12 revision.

> ### ⚠️ CORRECTED 2026-08-17 — §B no longer outranks §A on mess
>
> This file previously said §B "**outranks §A wherever they disagree — on length, mess, and pasted
> context**". Measured against **20 signed-off conversations / 207 user turns**, that is wrong and
> was pushing us away from what gets approved:
>
> | | §B implies | Signed-off reality |
> |---|---|---|
> | missing apostrophes | pervasive | **2.1%** of follow-ups |
> | starts lowercase | typical | 25% of follow-ups |
> | length | long, run-on | median **193 chars / 35 words** |
> | em dash / bullets / bold | — | **0.0%** (bans confirmed) |
> | thanks the assistant | — | **0.0%** (ban confirmed) |
>
> **Approved work sits in §A's tidy register, not §B's rough one.** Treat §B as *permission* to be
> informal when the moment is genuinely informal — never as a target to imitate. Manufacturing
> messiness to match §B is itself the shared-pattern risk GL:180 hunts for.
>
> §B still outranks §A on one thing: **pasted context**. Paste raw and untrimmed, always.
> Evidence: `SIGNED_OFF_PATTERNS.md`. Length and move rules: `../rules/TURN_STRATEGY.md`.

New signed-off examples get appended verbatim. Never paraphrase into this file.

> **Scope warning.** §B calibrates *register and texture*, not *task scope*. Several §B entries
> ("mitosis??", "should i get organic berries?") are perfectly good illustrations of voice and
> completely unusable as openers, because the current regime needs a topic with **10–15 turns of
> genuine depth** (`../rules/TURN_RULES.md` §4). Imitate the texture, never the scope.

---

# §A — Reference transcripts (tidy register)

## task-1 — writing help (cancel dinner message) — 5 user turns
1. "I need to cancel plans with a friend this Saturday because something came up at work. We were supposed to get dinner. Can you help me write a short message that sounds honest and apologetic, but not dramatic? I still want to reschedule soon."
2. "I like the short one better. Can you make it sound a little warmer? Also don't say "gotta" - that feels too casual for this friend."
3. "This is close. Can you suggest two nights next week in the message, like Tuesday or Thursday? I don't want to leave it totally open-ended."
4. "Perfect. One last thing, can you make a slightly shorter version I can send as a text? Same meaning, just fewer words."
5. "This works. Can you also give me one backup line in case they can't do Tuesday or Thursday? Just one short sentence I can add."

## task2 — coding interview prep advice — 3 user turns
1. "If i have a coding interview in 15 days and i am not that good at DSA but know the basics, what do you think is the best approach to get a good grasp on it?"
2. "Yes this is mostly for walmart but the thing is i always start at arrays but by the time i reach DP/Graphs i have lost interest and which is why i am very weak at them, so how to keep consistency?"
3. "but doesn't keeping on switching between topics harming the brain to learn/ recognize the pattern? as ultimately in interview recognizing the pattern is what is going to help?"

## task3 — factual lookup (Clash Royale) — 4 user turns
1. "When was the launche date for Clash Royale?"
2. "You specified "globally", wasn't only one launch? Or why this explanation?"
3. "Was this the first game of Supercell?"
4. "Which one of the Supercell games is the most popular?"

## task4 — weekly routine planning — 3 user turns
1. "I want to build a realistic weekly routine that balances work, exercise, errands, and downtime without feeling overly strict. Ask me a few questions about my current schedule, then create a flexible plan I can actually follow."
2. "I work 9 AM to 6 PM on weekdays. I want to exercise three evenings a week, do chores on weekends, and have one hour to relax each night. Please make me a simple weekly plan."
3. "This looks good, but I'd rather finish all chores on Saturday and keep Sunday mostly free. Can you revise the plan?"

## task5 — workday scheduling — 3 user turns
1. "I'm planning my workday tomorrow and have these priorities: reply to client emails, finish a project update, review a teammate's draft, and go to the gym after work. Can you help me organize this into a realistic schedule?"
2. "Can you make the schedule more flexible in case the project update takes longer than expected?"
3. "Can you turn it into a short checklist I can follow during the day?"

## task6 — Django error debugging — 3 user turns
1. (raw error paste, no prose at all)
   "auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'authentication.User.groups'.
           HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'authentication.User.groups'."
2. "And how can I add it to a Token model fro tracking?"
3. "Give me the service for create and deactivate tokens by user"

> These six run 3–5 turns because they were produced under the dead 1–10 regime. Their **voice**
> is the target; their **length** is not. Under 10–15 turns, task-1's refinement arc is the
> shape that scales — it just keeps refining for another seven turns.

---

# §B — Guide example prompts, verbatim (the rougher register)

Reproduced exactly as published, mess intact. The guide's framing: *"prompts tend to be casual
and direct, sometimes rushed or mid-thought, grounded in personal context, occasionally messy
with shorthand, missing punctuation, or sentences that trail off."*

1. `mitosis??`
2. `if a train leaves chicago at 60mph and another train leaves new york at 80mph and theyre 800 miles apart when do they meet helppp (this is for hw not a real train situation)`
3. `"The quick ratio, also known as the acid-test ratio, measures a company's ability to meet its short-term obligations" what does that mean for a small business`
4. ★ `so i was thinking about switching careers into UX design but I don't have a portfolio and I don't know where to start and someone told me i should do a bootcamp but those are expensive and I don't know if they're worth it and I have a graphic design background so maybe that counts for something I don't know what do you think`
5. `hi so i got this email from my landlord and i'm not sure if it's legal; Dear Tenant, Please be advised that effective January 1st your monthly rent will increase by $400 due to rising operational costs and market adjustments. Failure to comply with the updated payment schedule will result in initiation of eviction proceedings per local ordinance 47.2(b). is he allowed to do this?? we're in seattle if that matters. also my lease doesn't end until april. i don't know if i should respond or just ignore it or call someone, i really can't afford this right now`
6. ★ `I'm trying to negotiate a contractor quote down from $18,000 to $12,000. The work is a fence, shower install, and fridge cabinet prep. what's a good approach and what's realistic to ask for?`
7. ★ `Why does this return None def process(data): result = [] for item in data: if item > 0: result.append(item * 2) print(result) process([1, -2, 3]) i'm calling it and storing the return but getting None back every time`
8. `Here are the notes from our last three team syncs, can you pull out the open action items and who owns each one? [long context pasted]` (followed by three verbatim sync blocks with attendee names, unresolved threads, and mid-sentence detail)
9. `help me improve this plan and plz let me know your thoughts on it: [Paste long context] I'm preparing for interview about API testing rest sharp based framework HAPPY framework Recqnroll facade pattern building pattern schema testing contract testing how to fix errors common api interview questions and detailed answers can you prep detailed explaination about all of these for me`
10. `should i get organic berries?`
11. ★ `i have a sqlite db with 500k rows with SEO keyword-phrases. what options do I have when i want them embedd them with many dimensions? list them`
12. ★ `could you remove the words like gamma and put in the appropriate symbols: [document copy pasted]`
13. `replace current closing tag into CTA section and remove zoom option and restructure the n8n workflow and dont merge with border line [pasted several hundred lines of code]`
14. ★ `how to make a rounded corners jframe in java netbeans ide [pasted code]`
15. ★ `above is my sp user is saying the fmSuppressAuth is not coping please find the issue and provide me solution`

## What §B adds that §A does not

- **Long stream-of-consciousness is legitimate.** #4 runs ~70 words with no commas and no full
  stops, chaining on "and… and… and", ending "I don't know what do you think". #5 runs ~130
  words, embeds a pasted email mid-sentence, doubles a question mark, and closes on real emotion.
- **Pasted context, untrimmed.** #7 pastes code with the formatting flattened. #8 pastes three
  meeting blocks with real names. #12/#13/#14 paste documents and hundreds of lines of code. The
  prose around them is minimal.
- **Real typos nobody corrected** — "theyre", "plz", "embedd", "Recqnroll", "explaination",
  "coping" (meant copying), "fro tracking".
- **Domain jargon dumped with no gloss** — #9 lists eight framework terms with no connective
  tissue; #15 assumes "sp" and "fmSuppressAuth" need no explanation.
- **Emotional and situational framing** — "(this is for hw not a real train situation)",
  "i really can't afford this right now", "we're in seattle if that matters".
- **Opening with a quote from something else** (#3 quotes a definition, then asks what it means).
- **A lowercase "hi so" opener** (#5) — a scene-setter, not a greeting *to the assistant*, so it
  doesn't violate the no-greeting ban. Praise and thanks are absent from all fifteen.

---

# §C — The 08-12 worked examples ("why it works")

**Prompt 2** — *"If everything we do comes from our brain chemistry and our upbringing and stuff
we didn't choose, then do we actually decide anything? And if we don't, what's the point of
trying to be a better person?"*

> Asks a conceptual question the model can handle without external tools. No PII. Genuine and
> substantive, grounded in a classic philosophical problem. Reads like someone who has been
> turning an idea over in their head.

**Prompt 3** — *"I've been working on jazz standards for a few months but my solos over ii-V-I
progressions still sound stiff. A friend told me to start with modal tunes like So What to free
up my phrasing. I get the concept but I'm not really hearing it yet in my own playing. Should I
focus on transcribing solos or just spend more time sitting with the changes?"*

> Answerable from internal knowledge of music theory. Reads like a real musician describing a
> specific practice hurdle, with concrete harmonic references and an honest admission of not
> fully connecting with the concept. Names real tunes, ends with a clear, answerable question
> about two concrete approaches.

**What §C teaches that §A/§B don't:** these two are *tidy* and still authentic. Polish is not
the enemy — **inauthenticity** is. A considered, well-formed question about something you are
genuinely stuck on passes. Both also happen to be exactly the kind of topic that sustains 10–15
turns, which is why they are the closest published match to what this project now needs.

---

## Voice fingerprint (what the humanizer enforces)

- **Length — corrected 2026-08-17.** Follow-ups cluster at **16–66 words, median 35**; the old
  "8–45, composed paragraphs are wrong" figure would have rejected **36% of signed-off work**.
  Multi-sentence follow-ups are normal (38% of approved turns). Opening prompts run **30–70 words**
  plus however many pasted lines the situation carries. An untrimmed paste is still right; a
  *manufactured* run-on is not. Bands and the per-position arc: `../rules/TURN_STRATEGY.md` §1.
- **Openers acknowledge, never thank.** "I like the short one better." / "This is close." /
  "Perfect. One last thing," / "This works." / "This looks good, but" / "Yes this is mostly for
  walmart but". Zero thanks, zero greetings, zero praise of the assistant anywhere in the corpus.
- **Concrete, incremental asks** — one or two changes per turn.
- **They quote and push back** — "don't say 'gotta'" / "You specified 'globally', wasn't only
  one launch?" / "but doesn't keeping on switching between topics harming the brain…?"
- **Imperfections scale with register.** Tidy register: 0–2 light slips. Rushed register: the
  whole message is lowercase, unpunctuated, typo-bearing — and that is correct. Choose a
  register and stay inside it; mixing careless and careful is the tell.
- **No composed formatting** in anything you author — no bullets, no numbering, no bold, no
  colon-then-list. Pasted material keeps whatever shape it already had.
- **No em dashes, no semicolons, no "delve / moreover / furthermore".**
- **Endings are quiet** — the last turn narrows to one small ask ("One last thing", "Just one
  short sentence I can add"), then it stops. No goodbye.

## Register selection table

| Situation | Imitate | Shape |
|---|---|---|
| Quick factual lookup (mid-conversation only) | §B #1, #10 | 2–8 words, maybe a doubled ?? |
| Homework / puzzle with stakes | §B #2 | run-on, parenthetical aside |
| Personal decision, unresolved | §B #4, #5 · §C prompt 2 | 60–130 words, no punctuation discipline, emotion |
| Handing over content | §B #7, #8, #12, #13 | short framing + untrimmed paste |
| Work task in a known domain | §B #9, #11, #15 | jargon, no gloss, typos, "list them" |
| Considered ask with a real hurdle | §C prompt 3 · §A task-1 | 30–60 words, tidy, one concrete constraint |
| Follow-up inside a conversation | §A all | 16–66 words (median 35), reacts to a specific thing said |
