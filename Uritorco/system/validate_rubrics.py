#!/usr/bin/env python3
"""
Uritorco / WebDev side-by-side rating - mechanical validator for the eight fields.

Run it twice on every task: once on the draft, and AGAIN after the humanizer pass,
because humanization is a rewrite and can silently break the exact-phrase rule, the
negatives-only rule, or the required opener.

Usage:
    python validate_rubrics.py task.json

Input JSON:
{
  "left":  {"completeness": {"rating": 1-5, "reason": "..."},
            "functionality": {...}, "visual": {...}},
  "right": {... same ...},
  "preference": {"selection": "Slightly prefer Left", "confidence": "Medium",
                 "reason": "..."}
}

Checks the six client batch rules from BATCH_RULES.md. Exit 0 is clean.
It cannot check whether a claim is TRUE. That audit is still manual.
"""
import json
import re
import sys

# Rule 3: the exact phrase for a 5, taken verbatim from the platform's rating scale.
EXACT_5 = "Excellent with no meaningful issues."

# Rule 5: selection -> required opening clause.
OPENERS = {
    "Strongly prefer Left": "The left candidate is strongly preferred because",
    "Prefer Left": "The left candidate is preferred because",
    "Slightly prefer Left": "The left candidate is slightly preferred because",
    "Slightly prefer Right": "The right candidate is slightly preferred because",
    "Prefer Right": "The right candidate is preferred because",
    "Strongly prefer Right": "The right candidate is strongly preferred because",
    "Tie": None,  # free opener, but must explain the tie
}

# Rule 1: positive language has no place in a rubric field.
POSITIVE = re.compile(
    r"\b(excellent|great|good|nicely|nice|well[- ](?:built|designed|handled|laid)|strong(?:er|est)?"
    r"|polished|impressive|helpful|useful|solid|pleasant|attractive|thoughtful|neat|elegant"
    r"|robust|comprehensive|intuitive|smooth|effective|successful|advantage|benefit"
    r"|does a good|works well|handles .* correctly|correctly handles"
    # A rubric field is negatives only, so any clause saying something DOES work is a
    # violation even when it carries no adjective. The humanizer caught "the controls
    # themselves behave correctly" sitting in a negatives-only field after the adjective
    # list above had passed it clean. Match the shape, not the vocabulary.
    r"|behaves? correctly|behaved correctly|work(?:s|ed)? (?:correctly|as expected|fine|properly)"
    r"|function(?:s|ed)? (?:correctly|as expected|properly)|operate(?:s|d)? correctly"
    r"|no (?:issues|problems|faults|defects) (?:were |was )?(?:found|observed|seen)"
    r"|performs? (?:well|correctly)|is (?:accurate|correct)|are (?:accurate|correct))\b",
    re.I,
)

FIRST_PERSON = re.compile(r"\b(I|I'm|I've|my|we|our|us)\b")
SECOND_PERSON = re.compile(r"\b(you|your|you're|yours)\b")
DASHES = re.compile(r"[—–]")
# Rule 6: a bug claim should carry steps.
BUG_WORDS = re.compile(r"\b(broken|fails?|does not work|doesn't work|crash|error|bug)\b", re.I)
STEP_WORDS = re.compile(
    r"\b(click|clicking|type|typing|enter|entering|select|selecting|open|opening"
    r"|repro|steps?|at a width|resiz|scroll|submit|after)\b", re.I)

LENSES = ("completeness", "functionality", "visual")
SIDES = ("left", "right")


def block(msgs, where, text):
    msgs.append(("BLOCK", where, text))


def note(msgs, where, text):
    msgs.append(("NOTE", where, text))


def check(path):
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)

    msgs = []
    totals = {}

    for side in SIDES:
        if side not in d:
            block(msgs, side, "missing side")
            continue
        total = 0
        for lens in LENSES:
            where = f"{side}/{lens}"
            field = d[side].get(lens)
            if not field:
                block(msgs, where, "missing field")
                continue

            rating = field.get("rating")
            reason = (field.get("reason") or "").strip()
            if rating not in (1, 2, 3, 4, 5):
                block(msgs, where, f"rating must be 1-5, got {rating!r}")
                continue
            total += rating

            if not reason:
                block(msgs, where, "reason is empty")
                continue

            # Rules 2 and 3: a 5 uses the exact phrase, and only a 5 may use it.
            if rating == 5 and reason != EXACT_5:
                block(msgs, where, f"rating 5 must read exactly {EXACT_5!r}, got {reason!r}")
            if rating != 5 and reason == EXACT_5:
                block(msgs, where, f"exact 5 phrase used on a rating of {rating}")

            if rating == 5:
                continue  # the fixed phrase is exempt from the prose checks below

            # Rule 1: negatives only.
            hits = sorted(set(m.group(0).lower() for m in POSITIVE.finditer(reason)))
            if hits:
                block(msgs, where, f"positive language in a rubric field: {hits}")

            for label, pat in (("first person", FIRST_PERSON), ("second person", SECOND_PERSON)):
                found = sorted(set(m.group(0) for m in pat.finditer(reason)))
                if found:
                    block(msgs, where, f"{label}: {found}")

            if DASHES.search(reason):
                block(msgs, where, "em or en dash present")

            # Rule 6: a bug claim needs reproduction steps.
            if BUG_WORDS.search(reason) and not STEP_WORDS.search(reason):
                note(msgs, where, "describes a fault but names no steps to reproduce it")

            words = len(reason.split())
            if words < 25:
                note(msgs, where, f"only {words} words, thin for an evidence field")

        totals[side] = total

    # Rule 4 and 5: the preference must follow the totals and match its own opener.
    pref = d.get("preference") or {}
    sel = pref.get("selection")
    reason = (pref.get("reason") or "").strip()

    if sel not in OPENERS:
        block(msgs, "preference", f"unknown selection {sel!r}")
    else:
        need = OPENERS[sel]
        if need and not reason.startswith(need):
            block(msgs, "preference", f"must open with {need!r}")
        if sel == "Tie" and not re.search(r"\btie|tied\b", reason, re.I):
            block(msgs, "preference", "Tie selected but the reason never explains the tie")
        if need:
            for side in SIDES:
                if f"{side} candidate" not in reason.lower():
                    block(msgs, "preference",
                          f"comparative summary never mentions the {side} candidate")

    if DASHES.search(reason):
        block(msgs, "preference", "em or en dash present")
    for label, pat in (("first person", FIRST_PERSON), ("second person", SECOND_PERSON)):
        found = sorted(set(m.group(0) for m in pat.finditer(reason)))
        if found:
            block(msgs, "preference", f"{label}: {found}")

    if pref.get("confidence") not in ("Low", "Medium", "High"):
        block(msgs, "preference", f"confidence must be Low/Medium/High, got {pref.get('confidence')!r}")

    # Rule 4: the totals have to point the same way as the selection.
    if len(totals) == 2 and sel in OPENERS:
        lt, rt = totals["left"], totals["right"]
        lc = d["left"]["completeness"]["rating"]
        rc = d["right"]["completeness"]["rating"]
        print(f"    totals: left {lt} (completeness {lc}), right {rt} (completeness {rc})")
        if sel != "Tie":
            picked = "left" if "Left" in sel else "right"
            loser_total = rt if picked == "left" else lt
            win_total = lt if picked == "left" else rt
            if win_total < loser_total:
                block(msgs, "preference",
                      f"{picked} selected but scores lower on total ({win_total} vs {loser_total})")
            elif win_total == loser_total:
                note(msgs, "preference",
                     f"totals are level at {win_total}; completeness must carry the choice "
                     f"(left {lc}, right {rc})")
            picked_c = lc if picked == "left" else rc
            other_c = rc if picked == "left" else lc
            if picked_c < other_c:
                note(msgs, "preference",
                     f"{picked} selected but loses on completeness ({picked_c} vs {other_c}), "
                     "which carries the most weight; make sure the rationale justifies that")
        else:
            if lt != rt:
                note(msgs, "preference", f"Tie selected but totals differ ({lt} vs {rt})")

    for side in SIDES:
        for lens in LENSES:
            f = d.get(side, {}).get(lens)
            if f and f.get("reason"):
                print(f"    {side:5} {lens:14} rating {f.get('rating')}  "
                      f"{len(f['reason'].split()):3} words")
    if reason:
        print(f"    preference   {sel!r} / {pref.get('confidence')!r}  {len(reason.split())} words")

    blocks = [m for m in msgs if m[0] == "BLOCK"]
    notes = [m for m in msgs if m[0] == "NOTE"]
    print()
    for kind, where, text in blocks + notes:
        print(f"{kind}  {where}: {text}")

    if blocks:
        print(f"\n{len(blocks)} BLOCK(s) must be cleared before submitting.")
        return 1
    print("\nCLEAN - no mechanical findings. Exact phrase, openers, negativity and totals all pass.")
    print("Mechanical checks only. The factual audit against the two apps is still on you.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(check(sys.argv[1]))
