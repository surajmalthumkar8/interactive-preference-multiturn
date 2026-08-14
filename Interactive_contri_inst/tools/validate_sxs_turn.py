#!/usr/bin/env python3
"""Mechanical validator for SxS Interactive per-paste submissions (DO_TASK S4/C6).

Usage: python validate_sxs_turn.py <submission.md>
Prints CLEAN (exit 0) when no FAIL; otherwise NOT CLEAN (exit 1) with findings.
WARN lines never block but must be consciously accepted by the orchestrator.

Section format: system/templates/SUBMISSION_TEMPLATE.md (## MODE / ## TURN /
## PICK / ## REASON / ## NEXT MESSAGE / ## INTERNAL). Rules enforced:
system/rules/AUTHENTICITY_RULES.md + TURN_RULES.md + PREFERENCE_RULES.md.

A NEXT MESSAGE whose first line is exactly "[raw-paste]" (a pasted error/snippet/
document/email prompt) skips the voice/length/formatting checks; the orchestrator
strips that marker before delivering. Keep the pasted block small - the platform's
length limit applies to the whole message.

Aligned to the 2026-07-28 contributor guide + measured platform behaviour:
  - turns 1..10 (was 3..5); END is legal at any turn >= 1
  - model capability limits are a hard FAIL (no web search, real-time info, file
    uploads, image generation/reading) -- see system/rules/CAPABILITY_RULES.md
  - ONE-OR-TWO-LINER length rule: WARN over 30 words, FAIL over 35. The platform
    errors out on longer prompts (measured: 43/49/57-word messages all failed; all
    four at <=31 words worked), and every example on the client's Spectrum of
    Authenticity slide is 17-27 words.
"""
import re
import sys

MODES = ["START", "COMPARE", "SINGLE", "END"]
PICKS = ["A", "B", "N/A"]

MAX_TURNS = 10          # 07-28 guide: maximum 10 user turns
MIN_TURNS_TO_END = 1    # 07-28 guide: a single turn is complete and valid

# Model capability limits (07-28 guide "Model capability note"). Each entry is
# (regex, human-readable capability). These are BLOCKING - a prompt that assumes an
# unsupported capability wastes the task.
CAPABILITY_PATTERNS = [
    (r"\bsearch (?:the )?(?:web|internet|online)\b", "web search"),
    (r"\b(?:google|bing) (?:it|this|for)\b", "web search"),
    (r"\blook (?:it |this |that )?up (?:online|on the web|for me)\b", "web search"),
    (r"\b(?:can|could) you look (?:it |this |that )?up\b", "web search"),
    (r"\bbrowse (?:to|the web)\b", "web search"),
    (r"\bfind (?:it |this |that )?(?:online|on the web)\b", "web search"),
    (r"\b(?:search|look) for .{0,30}\b(?:online|on the web)\b", "web search"),
    (r"https?://", "opening a URL"),
    (r"\bopen (?:this|the) (?:url|link|file|document|pdf|doc)\b", "opening a URL/file"),
    (r"\bwhat(?:'s| is) the weather\b", "real-time information"),
    (r"\bwhat happened (?:yesterday|today|this week|recently)\b",
     "real-time information"),
    (r"\blatest news\b", "real-time information"),
    # Time-anchored asks: the anchor and the quantity may be several words apart
    # ("the current mortgage rate", "today's average gas price"). Constrain the gap
    # so it cannot span a sentence boundary.
    (r"\b(?:current|latest|today'?s|this week'?s|up to date|up-to-date)\b"
     r"[^.?!\n]{0,40}?\b(?:price|pricing|rate|rates|cost|weather|news|score|scores|"
     r"version|release|figure|stats?|standings|forecast|headline)\b",
     "real-time information"),
    (r"\b(?:price|pricing|rate|rates|cost|weather|news|score|version|release)\b"
     r"[^.?!\n]{0,25}?\b(?:right now|as of today|as of now|currently|at the moment|"
     r"this week|today)\b",
     "real-time information"),
    (r"\b(?:what(?:'s|s| is| are)|how much (?:is|are|does|do))\b[^.?!\n]{0,40}?"
     r"\b(?:right now|as of today|currently|at the moment)\b",
     "real-time information"),
    (r"\b(?:i(?:'ve)? )?attached\b", "file upload"),
    (r"\bthe (?:attached|uploaded)\b", "file upload"),
    (r"\bthis (?:screenshot|image|photo|picture|pdf|spreadsheet)\b", "file upload"),
    (r"\bfile i uploaded\b", "file upload"),
    (r"\b(?:generate|create|draw|make) (?:me )?an? (?:image|picture|logo|diagram|chart|mockup)\b",
     "image generation"),
    (r"\blook at (?:this|the) (?:image|photo|picture|screenshot)\b", "image input"),
    (r"\bwhat do you see in\b", "image input"),
]

# AI-tell vocabulary banned in user-side text (AUTHENTICITY_RULES hard bans).
# Expanded 2026-07-30 from the research brief (see knowledge/HUMANIZED_PROMPTING.md).
# Measured excess frequencies vs a pre-ChatGPT counterfactual: delves 28.0x,
# underscores 13.8x, showcasing 10.7x. The practitioner list is time-stratified and
# shrinking as models get tuned against it - RE-CHECK THIS LIST EVERY ~6 MONTHS.
BANNED_VOCAB = [
    # original set
    "delve", "crucial", "pivotal", "moreover", "furthermore", "additionally",
    "comprehensive", "leverage", "utilize", "robust", "nuanced", "underscore",
    "testament", "intricate", "tapestry", "vibrant", "streamline", "foster",
    "i appreciate", "certainly", "kindly",
    # 2026-07-30 additions: vocabulary
    "bolstered", "garner", "interplay", "navigate", "resonate", "commendable",
    "meticulous", "meticulously", "insights", "notably", "showcasing", "emphasizing",
    "enduring", "boasts", "align with",
    # 2026-07-30 additions: copula avoidance (used where a plain "is/are" belongs)
    "serves as", "stands as", "functions as",
    # 2026-07-30 additions: double hedging + self-narration
    "might potentially", "could possibly", "as you mentioned earlier",
    "to clarify my earlier",
]
# Corruption-class typos read as INJECTED noise, not human error. Detection research
# canonicalizes text and measures the edit distance back, so manufactured typos are
# their own fingerprint (82.6% TPR @ 1% FPR). Real human error is OMISSION (dropped
# capitals/apostrophes/terminal punctuation), which we allow. See
# knowledge/HUMANIZED_PROMPTING.md "omission, not corruption".
CORRUPTION_TYPOS = [
    r"\bteh\b", r"\bhte\b", r"\brecieve[ds]?\b", r"\bseperate\b",
    r"\bdefinately\b", r"\boccured\b", r"\bthier\b", r"\bbecuase\b",
    r"\bwaht\b", r"\bwiht\b", r"\badn\b", r"\bnad\b", r"\bexplaination\b",
    r"\bwierd\b", r"\balot\b",
    # A letter repeated 3+ times: helppp, sooo, yesss. No real English word
    # does this, so it is a safe signal for manufactured emphasis.
    r"([a-z])\1{2,}",
]
# Zero instances in the human corpus — banned outright.
GRATITUDE = [r"\bthanks\b", r"\bthank you\b", r"\bthx\b", r"\bappreciate\b",
             r"\bgreat answer\b", r"\bawesome answer\b"]
# Reason field: surface-feature justifications are never acceptable.
BANNED_REASONS = ["better formatted", "more detailed", "more comprehensive",
                  "nicely formatted", "well formatted", "well structured",
                  "instruction following", "accuracy", "rubric", "criteria"]

INTERNAL_KEYS = ["Decisive differentials", "Bias check", "Constraint ledger",
                 "Turn anchor", "Persona/PII", "Gates"]

END_SENTINEL = "END - send nothing further"


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\b[^\n]*$(.*?)(?=^## |\Z)", text,
                  re.M | re.S)
    return m.group(1).strip() if m else None


def strip_comments(s):
    return re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()


def check_capabilities(label, body, fails):
    """Hard gate: the model has no web search, real-time info, files, or images."""
    low = body.lower()
    seen = set()
    for pat, capability in CAPABILITY_PATTERNS:
        if capability in seen:
            continue
        if re.search(pat, low):
            seen.add(capability)
            fails.append(
                f"{label} assumes {capability}, which the model does not support "
                "(07-28 guide, Model capability note) - paste the content instead "
                "of pointing at it, or drop the time anchor")


def check_user_text(label, body, fails, warns, max_words=35, warn_words=30):
    """Voice checks shared by NEXT MESSAGE and REASON.

    Length caps TIGHTENED 2026-07-30 to the one-or-two-liner rule. This is a platform
    constraint, not a style preference: measured in the 2026-07-29 session, messages at
    43, 49 and 57 words all caused BOTH responses to fail with "Error while creating
    completion", while all four messages at or under 31 words generated cleanly. One
    51-word message did succeed, so the limit is probabilistic rather than a clean
    cutoff - which is why we write to the band that has never failed. Every example on
    the
    client's own Spectrum of Authenticity slide is 17-27 words. A long message does not
    merely risk a flag, it wastes the task.

    Pasted material is exempt via the [raw-paste] marker, but keep the paste small -
    the platform limit applies to the whole message.
    """
    words = len(body.split())
    if words > max_words:
        fails.append(f"{label} is {words} words; hard cap {max_words}. Prompts must "
                     "be one or two liners - the platform errors out on longer ones "
                     "(every message we sent at 43-57 words failed; every one at <=31 "
                     "words worked). Cut it or split the ask "
                     "across turns. Pasted material: use the [raw-paste] marker")
    elif words > warn_words:
        warns.append(f"{label} is {words} words; target is 10-30. Every client "
                     "example is 17-27 words - trim before sending")
    if re.search(r"[—–]", body):
        fails.append(f"{label} contains an em/en dash - real user turns never do")
    if re.search(r"[“”‘’]", body):
        fails.append(f"{label} contains curly quotes - use straight quotes")
    if "…" in body:
        fails.append(f"{label} contains an ellipsis character")
    low = body.lower()
    for term in BANNED_VOCAB:
        if re.search(rf"\b{re.escape(term)}\b", low):
            fails.append(f"{label} contains AI-tell vocabulary: {term!r}")
    for pat in CORRUPTION_TYPOS:
        m = re.search(pat, low)
        if m:
            fails.append(f"{label} contains a corruption-class typo {m.group(0)!r} - "
                         "manufactured typos are a detection signature. Use the "
                         "omission class instead (lowercase i, dropped apostrophe, "
                         "missing terminal period)")
            break
    for pat in GRATITUDE:
        if re.search(pat, low):
            fails.append(f"{label} thanks/praises the assistant - zero instances "
                         "exist in the human corpus")
    # Markdown formatting in a user turn.
    for line in body.splitlines():
        ls = line.strip()
        if re.match(r"^([-*#]|\d+[.)])\s", ls) or "**" in ls:
            fails.append(f"{label} contains list/heading/bold formatting - user "
                         "turns are plain sentences")
            break
    if ";" in body:
        warns.append(f"{label} contains a semicolon - real users almost never "
                     "use them")
    if re.search(r"\bnot (just|only)\b.*\bbut\b", low):
        warns.append(f"{label} uses negative parallelism ('not just X but Y') - "
                     "an AI tell; rephrase")


def main(path):
    fails, warns = [], []
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"NOT CLEAN\nFAIL: cannot read {path}: {e}")
        return 1

    mode = strip_comments(section(text, "MODE") or "")
    turn = strip_comments(section(text, "TURN") or "")
    pick = strip_comments(section(text, "PICK") or "")
    reason = strip_comments(section(text, "REASON") or "")
    message = section(text, "NEXT MESSAGE")
    internal = section(text, "INTERNAL")

    # --- MODE ---
    if mode not in MODES:
        fails.append(f"MODE must be one of {MODES}; got: {mode!r}")

    # --- TURN ---
    n = None
    m = re.search(r"\b([1-9]\d*)\b", turn or "")
    if not turn or not m:
        fails.append("TURN section missing or has no turn number")
    else:
        n = int(m.group(1))
        if n > MAX_TURNS:
            fails.append(f"TURN {n} exceeds the {MAX_TURNS}-turn maximum")
        if mode == "END" and n < MIN_TURNS_TO_END:
            fails.append(f"END at turn {n}: minimum is {MIN_TURNS_TO_END} user turn")
        if mode == "START" and n != 1:
            fails.append(f"MODE START must be Turn 1; got {n}")

    # --- PICK ---
    if pick not in PICKS:
        fails.append(f"PICK must be one of {PICKS}; got: {pick!r}")
    else:
        if mode == "COMPARE" and pick == "N/A":
            fails.append("MODE COMPARE requires PICK A or B")
        if mode in ("START", "SINGLE") and pick != "N/A":
            fails.append(f"MODE {mode} must have PICK N/A")

    # --- NEXT MESSAGE ---
    if not message or not message.strip():
        fails.append("NEXT MESSAGE section missing or empty")
    else:
        body = message.strip()
        if mode == "END":
            if not body.startswith("END"):
                fails.append("MODE END: NEXT MESSAGE must be the END sentinel "
                             f"({END_SENTINEL!r})")
        else:
            raw = body.splitlines()[0].strip() == "[raw-paste]"
            if raw:
                if mode != "START":
                    warns.append("[raw-paste] outside MODE START - confirm a "
                                 "mid-conversation paste is genuinely natural")
                # Voice/length checks are skipped for pasted material, but a
                # capability breach still matters. Downgraded to WARN because a URL
                # or the word "attached" may legitimately appear INSIDE a pasted
                # email or document - the orchestrator must judge which it is.
                cap_fails = []
                check_capabilities("NEXT MESSAGE", body, cap_fails)
                for c in cap_fails:
                    warns.append(c + " [raw-paste: confirm this is inside the "
                                 "pasted content, not our own ask]")
            else:
                check_user_text("NEXT MESSAGE", body, fails, warns)
                check_capabilities("NEXT MESSAGE", body, fails)

    # --- REASON ---
    if mode == "COMPARE":
        if not reason:
            fails.append("REASON section missing (write one or put N/A)")
        elif reason != "N/A":
            check_user_text("REASON", reason, fails, warns,
                            max_words=35, warn_words=25)
            low = reason.lower()
            for term in BANNED_REASONS:
                if term in low:
                    fails.append(f"REASON justifies by surface features/rubric: "
                                 f"{term!r} - cite the content differential")

    # --- INTERNAL ---
    if internal is None:
        fails.append("INTERNAL section missing - gates need the verification "
                     "record")
    else:
        for key in INTERNAL_KEYS:
            if key.lower() not in internal.lower():
                warns.append(f"INTERNAL record is missing '{key}'")
        if mode == "COMPARE" and re.search(
                r"Decisive differentials:\s*(N/A|none)", internal, re.I):
            fails.append("MODE COMPARE with no decisive differentials recorded - "
                         "the pick must cite what decided it")

    for w in warns:
        print(f"WARN: {w}")
    if fails:
        print("NOT CLEAN")
        for f in fails:
            print(f"FAIL: {f}")
        return 1
    print("CLEAN")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_sxs_turn.py <submission.md>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
