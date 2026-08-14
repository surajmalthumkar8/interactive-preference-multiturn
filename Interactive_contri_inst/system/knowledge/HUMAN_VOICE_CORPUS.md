# HUMAN VOICE CORPUS — real user turns, verbatim

The voice target for every prompt and follow-up we write. The humanizer's test:
would our turn blend in here without standing out?

**Two sections, both binding:**
- **§A** — the six signed-off reference transcripts
  (`Interactive_contri_inst/reference_tasks/`). Tidy register. Good model for
  *follow-up* turns inside a considered conversation.
- **§B** — the 15 real prompts published in the **2026-07-28 contributor guide** §3,
  described there as "drawn from real user conversation history". Much rougher and
  often much longer. **This is the client's own statement of what a good prompt looks
  like, so it outranks §A wherever they disagree** — especially on length, mess, and
  pasted context.

New signed-off examples get appended verbatim.

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

---

# §B — Official guide examples (2026-07-28, §3) — verbatim, the rougher register

Reproduced exactly as published, mess intact. The guide's own framing: "prompts can
be more casual and direct, sometimes rushed or mid-thought, grounded in personal
context, occasionally messy with shorthand, missing punctuation, minor errors, and
sentences that trail off."

1. `mitosis??`
2. `if a train leaves chicago at 60mph and another train leaves new york at 80mph and theyre 800 miles apart when do they meet helppp (this is for hw not a real train situation)`
3. `"The quick ratio, also known as the acid-test ratio, measures a company's ability to meet its short-term obligations" what does that mean for a small business`
4. `so i was thinking about switching careers into UX design but I don't have a portfolio and I don't know where to start and someone told me i should do a bootcamp but those are expensive and I don't know if they're worth it and I have a graphic design background so maybe that counts for something I don't know what do you think`
5. `hi so i got this email from my landlord and i'm not sure if it's legal; Dear Tenant, Please be advised that effective January 1st your monthly rent will increase by $400 due to rising operational costs and market adjustments. Failure to comply with the updated payment schedule will result in initiation of eviction proceedings per local ordinance 47.2(b). is he allowed to do this?? we're in seattle if that matters. also my lease doesn't end until april. i don't know if i should respond or just ignore it or call someone, i really can't afford this right now`
6. `I'm trying to negotiate a contractor quote down from $18,000 to $12,000. The work is a fence, shower install, and fridge cabinet prep. what's a good approach and what's realistic to ask for?`
7. `Why does this return None def process(data): result = [] for item in data: if item > 0: result.append(item * 2) print(result) process([1, -2, 3]) i'm calling it and storing the return but getting None back every time`
8. `Here are the notes from our last three team syncs, can you pull out the open action items and who owns each one? [long context pasted]` (followed by three verbatim sync blocks with attendee names, unresolved threads, and mid-sentence detail)
9. `help me improve this plan and plz let me know your thoughts on it: [Paste long context] I'm preparing for interview about API testing rest sharp based framework HAPPY framework Recqnroll facade pattern building pattern schema testing contract testing how to fix errors common api interview questions and detailed answers can you prep detailed explaination about all of these for me`
10. `should i get organic berries?`
11. `i have a sqlite db with 500k rows with SEO keyword-phrases. what options do I have when i want them embedd them with many dimensions? list them`
12. `could you remove the words like gamma and put in the appropriate symbols: [document copy pasted]`
13. `replace current closing tag into CTA section and remove zoom option and restructure the n8n workflow and dont merge with border line [pasted several hundred lines of code]`
14. `how to make a rounded corners jframe in java netbeans ide [pasted code]`
15. `above is my sp user is saying the fmSuppressAuth is not coping please find the issue and provide me solution`

## What §B adds that §A does not have

- **Micro prompts are legitimate.** "mitosis??" is two words and a doubled question
  mark. "should i get organic berries?" is five. Neither is "too minimal" — the guide
  publishes both as good.
- **Long stream-of-consciousness is legitimate.** #4 runs ~70 words with no commas and
  no full stops, chaining on "and... and... and", ending "I don't know what do you
  think". #5 runs ~130 words, mixes a pasted email into the middle of the sentence,
  double question mark, and closes on real emotion ("i really can't afford this").
- **Pasted context, untrimmed.** #7 pastes code with the formatting flattened. #8
  pastes three meeting blocks with real names. #12/#13/#14 paste documents and
  several hundred lines of code. The prose around them is minimal.
- **Real typos that are not cute.** "theyre", "helppp", "plz", "embedd", "Recqnroll",
  "explaination", "coping" (meant "copying"), "fro tracking". Nobody corrected them.
- **Domain jargon dumped without explanation.** #9 lists eight framework terms with no
  connective tissue. #15 assumes "sp" and "fmSuppressAuth" need no gloss.
- **Emotional and situational framing.** "helppp", "(this is for hw not a real train
  situation)", "i really can't afford this right now", "we're in seattle if that
  matters". Real stakes leak into real prompts.
- **Opening a message with a quote from something else** (#3 opens with a quoted
  definition, then asks what it means).
- **A lowercase "hi so" opener** (#5) — note this is a scene-setter, not a greeting
  *to the assistant*, so it does not violate the no-greeting ban. Praise and thanks
  are still absent from all 16.

## Register selection (which section to imitate)

| Situation | Imitate | Shape |
|---|---|---|
| Quick factual lookup | §B #1, #10 | 2–8 words, maybe a doubled ?? |
| Homework / puzzle with stakes | §B #2 | run-on, "helppp", parenthetical aside |
| Personal decision, unresolved | §B #4, #5 | 60–130 words, no punctuation discipline, emotion |
| Handing over content | §B #7, #8, #12, #13 | short framing + untrimmed paste |
| Work task in a known domain | §B #9, #11, #15 | jargon, no gloss, typos, "list them" |
| Considered ask with tone constraints | §A task-1, task4, task5 | 30–50 words, tidy, one concrete constraint |
| Follow-up inside a conversation | §A all | 8–45 words, reacts to a specific thing said |

---

## Voice fingerprint (distilled — the humanizer enforces this)

- **Length (updated 07-28):** follow-ups cluster at 8–45 words. **Opening prompts span
  2 words to several hundred lines** — see the §B band table. Composed paragraphs are
  still wrong; a rambling run-on or an untrimmed paste is right. A developer may open
  by pasting a raw error with zero prose.
- **Openers acknowledge, never thank:** "I like the short one better." / "This is
  close." / "Perfect. One last thing," / "This works." / "This looks good, but" /
  "Yes this is mostly for walmart but". **Zero instances of "thanks", "thank you",
  greetings, or praise of the assistant** in the whole corpus.
- **Concrete, incremental asks:** one or two changes per turn ("make it warmer",
  "suggest Tuesday or Thursday", "fewer words", "turn it into a checklist").
- **They quote and push back on the response:** "don't say "gotta"" / "You
  specified "globally", wasn't only one launch?" / "but doesn't keeping on switching
  between topics harming the brain...?"
- **Imperfections scale with register (updated 07-28):** the "never more than one or
  two per turn" limit below applies to the TIDY register (§A). In the rushed register
  (§B #2, #4, #5, #9) the whole message is lowercase, unpunctuated and typo-bearing,
  and that is correct. Choose a register, then stay inside it — mixing careless and
  careful is the tell.
- **Imperfections are real and unforced:** lowercase "i", "walmart", "launche
  date", "fro tracking", a turn starting with "but", a hyphen used instead of a
  dash, comma splices, ESL-flavored phrasing ("Give me the service for create and
  deactivate tokens by user"). Never more than one or two per turn; never cartoonish.
- **No composed formatting:** no bullets, no numbered lists, no bold, no
  colons-then-list that WE authored. Plain sentences only. (Pasted material keeps
  whatever shape it already had — do not tidy it, do not reformat it.)
- **No em dashes, no semicolons, no "delve/moreover/furthermore"** — none appear in
  any real user turn.
- **Endings are quiet:** the conversation just stops after a satisfied turn; the
  last turn often narrows to one small final ask ("One last thing", "Just one short
  sentence I can add"). Under the 07-28 guide a conversation may also simply stop
  after Turn 1 — that is a legitimate ending, not an abandoned task.
