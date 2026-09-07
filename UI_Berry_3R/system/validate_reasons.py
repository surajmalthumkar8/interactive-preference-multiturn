#!/usr/bin/env python3
"""
UI Berry 3R — mechanical validator for the three reason fields.

Run it twice on every task: once on the draft, and AGAIN after the humanizer pass,
because humanization is a rewrite and can silently break the word range, the
"Website A" / "Website B" naming rule, or lens purity.

Usage:
    python validate_reasons.py task.json
    python validate_reasons.py --demo

Input JSON:
{
  "aesthetics":   {"option": "A", "reason": "..."},
  "functionality":{"option": "B", "reason": "..."},
  "overall":      {"option": "B", "reason": "..."},
  "both_broken": false,
  "preview_exception": false
}

option is one of: A, B, BOTH_GOOD, BOTH_BAD

Exit code 0 = clean, 1 = findings. BLOCK findings must be fixed before submitting.
"""

import json
import re
import sys

# Vocabulary that must never appear in the aesthetics reason (behavior//function talk).
FUNCTION_WORDS = [
    r"button", r"link\b", r"links\b", r"click", r"clicking", r"submit", r"submits",
    r"submitted", r"\bform\b", r"\bforms\b", r"load\b", r"loads\b", r"loaded",
    r"loading", r"broken", r"navigat", r"filter", r"\btabs?\b", r"control",
    r"dropdown", r"toggle", r"slider", r"carousel", r"calculator", r"\bwork\b",
    r"works\b", r"working", r"function", r"interact", r"responds?\b", r"clickable",
    r"dead\b", r"crash", r"anchor", r"\bmenu\b", r"validat", r"\bupdates?\b",
]

# Vocabulary that must never appear in the functionality reason (visual talk).
VISUAL_WORDS = [
    r"colou?r", r"\bfont", r"typeface", r"typograph", r"spacing", r"palette",
    r"beautiful", r"pretty", r"\bugly\b", r"\bclean(ly)?\b", r"\bneat(ly)?\b",
    r"\btidy\b", r"layout", r"laid out", r"margin", r"padding", r"align",
    r"white ?space", r"hierarchy", r"aesthetic", r"polish(ed)?", r"serif",
    r"contrast", r"\bhue\b", r"cramped", r"crowded", r"elegant", r"composition",
    r"\bstyl(e|ish|ing)\b", r"visual", r"appearance", r"\bbold\b", r"italic",
    r"shadow", r"rounded", r"\bimagery\b",
    r"\blooks? (good|bad|clean|nice|professional|polished|dated|cheap|modern)\b",
]

# Category labels forbidden in every reason body.
CATEGORY_LABELS = [r"aesthetics?", r"functionality", r"visual quality", r"usability"]

# Abbreviated / informal candidate references — all rejected.
BAD_NAMING = [
    r"\bthe first (one|site|website)\b", r"\bthe second (one|site|website)\b",
    r"\bthe other (one|site|website)\b", r"\bsite [AB]\b", r"\boption [AB]\b",
    r"\bcandidate [AB]\b", r"\bpage [AB]\b", r"\bversion [AB]\b",
]

# Platform / out-of-scope references. NOTE the tab patterns are deliberately
# context-bound: a website's own "day tabs" or "category tabs" are page controls,
# not browser tabs, and must not be flagged.
PLATFORM_WORDS = [
    r"\bbrowser\b", r"\bchrome\b", r"\bfirefox\b", r"\bsafari\b",
    r"\b(new|browser|own|separate|full|second)\s+tab\b", r"\bthe tab\b",
    r"\bplatform\b", r"\bembedded\b", r"\bthe task\b", r"\bevaluat", r"\bannotat",
]

FIRST_PERSON = [r"\bI\b", r"\bmy\b", r"\bme\b", r"\bwe\b", r"\bour\b", r"\bus\b"]

VERDICT_OPENERS = {
    "A": r"^website a is better",
    "B": r"^website b is better",
    "BOTH_GOOD": r"^website a and website b are (tied|both)",
    "BOTH_BAD": r"^website a and website b are (tied|both)",
}

# Words that betray a "tie" reason secretly naming a winner.
TIE_WINNER_WORDS = [
    r"more complete", r"clearer", r"less broken", r"better than", r"outperform",
    r"stronger than", r"wins", r"beats", r"whereas .* fails", r"superior",
]


def words(text):
    """Whitespace-split count, matching `wc -w` and most word counters:
    'sans-serif' counts as one word."""
    return text.split()


def words_split(text):
    """Stricter count that splits hyphenated compounds: 'sans-serif' counts as two.
    The client's counter is unknown, so near a boundary we assume the worst case."""
    return re.findall(r"[A-Za-z0-9']+", text)


# Verbs that mark a bare "A" as a candidate reference rather than an article.
_CAND_VERB = re.compile(
    r"\s+(is|was|are|were|has|have|does|did|offers|shows|scores|wins|loses|fails|keeps|"
    r"renders|delivers|lacks|misses)\b")
_CAND_LEAD = re.compile(r"(than|and|or|versus|vs|over|while|whereas|beats|unlike)\s+$", re.I)


def bare_candidate_letters(text):
    """Bare 'A'/'B' used as a candidate name, i.e. not written as 'Website A'/'Website B'.

    'B' is never an ordinary English word, so any standalone capital B counts.
    'A' is the indefinite article, so it counts only in candidate-like context --
    otherwise a sentence opening 'A small badge...' would false-positive.
    """
    found = set()
    for m in re.finditer(r"\b([AB])\b", text):
        letter = m.group(1)
        before = text[:m.start()]
        if before.endswith("Website "):
            continue                                    # correctly named, skip
        if letter == "B":
            found.add("B")
            continue
        after = text[m.end():]
        if _CAND_VERB.match(after) or after.startswith("'s") or _CAND_LEAD.search(before):
            found.add("A")
    return found


def hits(patterns, text):
    found = []
    for p in patterns:
        for m in re.finditer(p, text, re.I):
            found.append(m.group(0))
    return sorted(set(f.lower() for f in found))


def ngrams(text, n=6):
    w = [x.lower() for x in words(text)]
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def check(task):
    findings = []

    def add(level, field, msg):
        findings.append((level, field, msg))

    both_broken = task.get("both_broken", False)
    preview_exc = task.get("preview_exception", False)

    fields = ["aesthetics", "functionality", "overall"]

    for f in fields:
        if f not in task:
            add("BLOCK", f, "field missing entirely; all six fields are required")
            continue
        opt = task[f].get("option", "").strip().upper()
        reason = (task[f].get("reason") or "").strip()

        if not reason:
            add("BLOCK", f, "reason is empty; all six fields are required")
            continue
        if opt not in VERDICT_OPENERS:
            add("BLOCK", f, f"option {opt!r} invalid; use A, B, BOTH_GOOD or BOTH_BAD")
            continue

        # --- word range -------------------------------------------------
        # Two counters disagree on hyphenated compounds and the client's is unknown,
        # so take the worst case at each end of the range.
        lo = min(len(words(reason)), len(words_split(reason)))
        hi = max(len(words(reason)), len(words_split(reason)))
        if hi > 160:
            add("BLOCK", f, f"{hi} words (strictest count); ceiling is 160 and is never waived")
        elif lo < 40 and not both_broken:
            add("BLOCK", f, f"{lo} words (strictest count); floor is 40 "
                            f"(waived only when BOTH sites are broken)")
        elif lo < 40 and both_broken:
            add("INFO", f, f"{lo} words; under 40 but both sites broken, so the floor is waived")
        elif lo < 45 or hi > 155:
            add("INFO", f, f"{lo}-{hi} words depending on how hyphens are counted; "
                           f"close to a boundary, add or trim a clause for margin")

        # --- opening verdict matches the option -------------------------
        if not re.match(VERDICT_OPENERS[opt], reason.strip(), re.I):
            add("BLOCK", f, f"opening does not state the outcome matching option {opt}. "
                            f"Starts: {reason[:60]!r}")

        # --- naming rule -------------------------------------------------
        bad = hits(BAD_NAMING, reason)
        if bad:
            add("BLOCK", f, f"abbreviated candidate names: {bad}. Use 'Website A' / 'Website B' in full")

        bare = bare_candidate_letters(reason)
        if bare:
            add("BLOCK", f, f"bare candidate letter(s) {sorted(bare)} not preceded by 'Website'")

        if not re.search(r"website a", reason, re.I) or not re.search(r"website b", reason, re.I):
            add("BLOCK", f, "both websites must be described, not only the winner "
                            "(one of them is never named)")

        # --- category labels ---------------------------------------------
        cats = hits(CATEGORY_LABELS, reason)
        if cats:
            add("WARN", f, f"names an evaluation category: {cats}. Describe what the site shows/does instead")

        # --- first person / platform -------------------------------------
        fp = hits(FIRST_PERSON, reason)
        if fp:
            add("BLOCK", f, f"first person {fp}; reasons are third person about the websites only")

        plat = hits(PLATFORM_WORDS, reason)
        if plat and not (preview_exc and re.search(r"preview", reason, re.I)):
            add("WARN", f, f"platform/browser reference {plat}; out of scope except the preview exception")

        # --- tie balance ---------------------------------------------------
        if opt.startswith("BOTH"):
            tw = hits(TIE_WINNER_WORDS, reason)
            if tw:
                add("BLOCK", f, f"tie option chosen but the reason names a winner: {tw}")

    # --- lens purity --------------------------------------------------------
    if "aesthetics" in task and task["aesthetics"].get("reason"):
        leak = hits(FUNCTION_WORDS, task["aesthetics"]["reason"])
        if leak:
            add("BLOCK", "aesthetics", f"behavior/function language in the visual lens: {leak}")

    if "functionality" in task and task["functionality"].get("reason"):
        leak = hits(VISUAL_WORDS, task["functionality"]["reason"])
        if leak:
            add("BLOCK", "functionality", f"visual language in the behavior lens: {leak}")

    # --- cross-field text reuse ---------------------------------------------
    present = [f for f in fields if task.get(f, {}).get("reason")]
    for i in range(len(present)):
        for j in range(i + 1, len(present)):
            a, b = present[i], present[j]
            shared = ngrams(task[a]["reason"]) & ngrams(task[b]["reason"])
            if shared:
                add("BLOCK", f"{a}+{b}", f"reused phrasing across fields: {sorted(shared)[:3]}")

    return findings


DEMO = {
    "aesthetics": {"option": "A", "reason":
        "Website A is better because it holds the sage green and warm sand palette the request "
        "asked for across every section, pairs a serif headline with a single clean sans-serif "
        "for body text, and leaves generous margins around each block so the page never feels "
        "crowded. Section headings keep one consistent size and weight, and the photography is "
        "sharp and consistently toned. Website B drifts to a bright default blue as its accent "
        "color, which sits awkwardly against the sand background, and it varies heading sizes "
        "between sections while pressing its opening headline hard against the photograph behind "
        "it. On Website B a small badge on the middle pricing card overlaps the price beneath it, "
        "and one instructor portrait is stretched out of proportion."},
    "functionality": {"option": "B", "reason":
        "Website B is better because every section the request named is present and responds. "
        "The day tabs above the schedule swap the listed classes, the instructor cards expand to "
        "show a short biography, each pricing tier links onward to a sign-up step, and the contact "
        "form flags a missing email address and returns a confirmation message once it is sent. "
        "The top navigation jumps to the correct section. Website A shows the same four sections, "
        "but its schedule is fixed to a single day and its day tabs never change the rows beneath "
        "them, the contact form on Website A accepts input yet does nothing when submitted, two of "
        "its three pricing buttons lead nowhere, and its instructor cards do not open."},
    "overall": {"option": "B", "reason":
        "Website B is better because this is a request a visitor has to act on, and only Website B "
        "lets them. Someone arriving to find a Tuesday evening class can change the day, read who "
        "teaches it, and send a message that is actually received. On Website A that same visitor "
        "meets a calmer, better-composed page, then reaches a schedule frozen on one day and a form "
        "that swallows their message without a word. The looser color and the cramped top of the "
        "page on Website B do cost the studio some poise, which is a real loss for a business "
        "selling calm. But presentation can be tidied in an afternoon, while a page that silently "
        "drops enquiries loses the booking outright."},
    "both_broken": False,
    "preview_exception": False,
}


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        task = DEMO
    elif len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as fh:
            task = json.load(fh)
    else:
        print(__doc__)
        return 2

    for f in ["aesthetics", "functionality", "overall"]:
        if task.get(f, {}).get("reason"):
            r = task[f]["reason"]
            a, b = len(words(r)), len(words_split(r))
            rng = str(a) if a == b else f"{min(a, b)}-{max(a, b)}"
            print(f"{f:>14}: {rng} words, option {task[f].get('option')}")

    findings = check(task)
    blocks = [x for x in findings if x[0] == "BLOCK"]

    print()
    if not findings:
        print("CLEAN - no mechanical findings. Lens purity, naming, range and reuse all pass.")
        print("Mechanical checks only. The factual audit against the two tabs is still on you.")
        return 0

    for level, field, msg in sorted(findings, key=lambda x: {"BLOCK": 0, "WARN": 1, "INFO": 2}[x[0]]):
        print(f"[{level:5}] {field}: {msg}")

    print()
    print(f"{len(blocks)} BLOCK finding(s), {len(findings) - len(blocks)} advisory.")
    if blocks:
        print("Do not submit until every BLOCK is cleared.")
    return 1 if blocks else 0


if __name__ == "__main__":
    sys.exit(main())
