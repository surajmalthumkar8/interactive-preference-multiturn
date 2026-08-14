---
name: mt-turn-count-conflict
description: The guidelines contain stale single-turn text contradicting the 10–15 turn requirement; 10 is a hard floor
metadata: 
  node_type: memory
  type: project
  originSessionId: 245c96c2-20a4-4909-b2a6-fe539a64b62a
  modified: 2026-08-13T19:21:42.648Z
---

The MAI guidelines file carries leftover text from an earlier **single-turn** version of the
project that directly contradicts the multi-turn requirement. Authoritative: **minimum 10 user
turns, maximum 15** (guidelines lines 168–170, echoed in all three admin docs). Stale text to
ignore: lines 134, 162, 172, 229 — including "If one turn says it all, that is absolutely fine"
and "you may send follow-up messages up to a total of ten turns".

Padding to reach 10 is a **removal offence** (line 115). The sanctioned remedy when a
conversation ends naturally before turn 10 is to **go back, delete turns, and rebuild from an
earlier branch point** (line 113) — never to add filler.

**Why:** Both versions of the rule sit in the same file, so reading any one section in isolation
gives the wrong answer. This is the most likely cause of a failed screening.

**How to apply:** Treat 10 as a hard floor and 15 as the ceiling. Because backtracking is
expensive, the real constraint is upstream — pick an opening topic with 10+ turns of genuine
depth *before* starting. Part of [[interactive-preference-multiturn]].
