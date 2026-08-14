---
description: Start a new MAI Multi-Turn task — validate the topic for 10-15 turns of depth, then produce Turn 1
argument-hint: [topic or pasted history prompt, optional]
allowed-tools: Read, Grep, Glob, Agent, Skill
---

Start a new Interactive Preference Multi-Turn task.

Candidate topic (may be empty): $ARGUMENTS

Run MODE START of `system/workflows/RUN_TASK.md`:

1. If no topic was given, **ask first** whether there is something genuinely asked of
   ChatGPT/Gemini/Claude/Copilot recently, or a real current need — filtered by thread
   **length**, not just topic. Real history outranks anything invented.
2. Dispatch `mt-topic-scout`. A REJECT means pick another topic — never start and hope.
3. Dispatch `mt-turn-writer` in MODE START.
4. Run the capability gate inline.
5. Dispatch `mt-humanizer`.
6. Dispatch `mt-compliance-auditor`.
7. Deliver per `system/templates/DELIVERABLE_TEMPLATE.md`, create the session state file, and
   dispatch `mt-session-scribe`.

Before Turn 1, remind him of the pre-claim prep list in `system/knowledge/TOPIC_PLAYBOOK.md` §6 —
the clock starts on claim.
