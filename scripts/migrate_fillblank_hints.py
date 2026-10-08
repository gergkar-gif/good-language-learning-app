"""Move fill-blank hints out of `sentence` into the typed `hint` field.

    python scripts/migrate_fillblank_hints.py            # dry run: counts + leftovers
    python scripts/migrate_fillblank_hints.py --write    # edit the files

Until ROADMAP 149 the hint was written into the sentence as a parenthetical:
"Ayer __ una carta. (escribir)", "Nem ____ (because of you) maradt el." It now
lives in its own field (course-generation-brief.md § 6.4):
{"sentence": "Ayer __ una carta.", "hint": "escribir"}.

A parenthetical is taken as the hint when it sits right after the blank, or at
the end of the sentence (before closing punctuation, or before a trailing
"[English]" gloss). An all-capitals acronym ("(BOE)", "(DGT)") is part of the
sentence and stays; so does a parenthetical anywhere else ("(Nochevieja)").
HAND_PICKED lists the few hints that sit a word or two away from the blank.
A sentence with two candidate hints is reported, not guessed.

Edits are surgical text replacements on the `"sentence": ...` line, so the
rest of each file keeps its formatting, and every edited file is re-parsed
and compared with the intended result before it is written. Rerunnable: a
fill-blank that already has `hint` is skipped.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLANK = re.compile(r"_{2,}")
ACRONYM = re.compile(r"^(?=.*[A-ZÁÉÍÓÖŐÚÜŰ].*[A-ZÁÉÍÓÖŐÚÜŰ])[A-ZÁÉÍÓÖŐÚÜŰ0-9\-]+$")
TAIL = re.compile(r"^[\s.?!…]*(\[[^\]]*\])?[\s.?!…]*$")

# Hints a word or two from the blank, checked by hand 2026-10-08.
HAND_PICKED = {
    "a2-108-controlled-3", "a2-211-check-2", "c1-16-05-controlled-2",
    "c1-mediakritika-02-controlled-2", "c1-mestersegesintelligencia-03-controlled-2",
    "c1-mestersegesintelligencia-04-controlled-2",
}


def paren_groups(s):
    """Top-level balanced (...) spans as (start, end) pairs; end is exclusive."""
    out, depth, start = [], 0, None
    for i, ch in enumerate(s):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
            if depth == 0:
                out.append((start, i + 1))
    return out


def find_hint(ex):
    """(start, end) of the hint parenthetical in ex['sentence'], None, or 'ambiguous'."""
    s = ex["sentence"]
    cands = []
    for a, b in paren_groups(s):
        inner = s[a + 1:b - 1].strip()
        # A structural hint may show a blank ("(minél … ___)"); skip only the
        # parenthetical that holds the sentence's own blank.
        if not inner or not BLANK.search(s[:a] + s[b:]) or ACRONYM.match(inner):
            continue
        after_blank = re.search(r"_{2,}['\"’”]?[\s,]*$", s[:a]) is not None
        at_end = TAIL.match(s[b:]) is not None
        if after_blank or at_end or ex.get("id") in HAND_PICKED:
            cands.append((a, b))
    if not cands:
        return None
    return cands[0] if len(cands) == 1 else "ambiguous"


def strip_hint(s, a, b):
    out = s[:a].rstrip() + " " + s[b:].lstrip()
    out = re.sub(r"\s+([,.;:!?…])", r"\1", out)
    out = re.sub(r",(?=[.!?])", "", out)  # "_____, (hint)." left a stray comma
    return re.sub(r"\s{2,}", " ", out).strip()


def encodings(value):
    return [json.dumps(value, ensure_ascii=False), json.dumps(value)]


def migrate_file(path, write):
    text = open(path, encoding="utf-8").read()
    data = json.loads(text)
    moved, leftovers, plan = 0, [], {}
    for ex in data.get("exercises", []):
        if ex.get("type") != "fill-blank" or not isinstance(ex.get("sentence"), str) or "hint" in ex:
            continue
        span = find_hint(ex)
        if span is None:
            continue
        if span == "ambiguous":
            leftovers.append(f"{ex.get('id')}: two candidate hints: {ex['sentence']}")
            continue
        a, b = span
        old = ex["sentence"]
        plan.setdefault(old, set()).add((strip_hint(old, a, b), old[a + 1:b - 1].strip()))
    for old, outcomes in plan.items():
        if len(outcomes) != 1:
            leftovers.append(f"same sentence, different outcomes: {old}")
            continue
        new, hint = next(iter(outcomes))
        for enc in encodings(old):
            pattern = re.compile(r'(?m)^([ \t]*)"sentence": ' + re.escape(enc) + r"|" + r'"sentence": ' + re.escape(enc))
            if not pattern.search(text):
                continue

            def repl(m):
                indent = m.group(1)
                sep = ("\n" + indent) if indent is not None else " "
                return (indent or "") + '"sentence": ' + json.dumps(new, ensure_ascii=False) + "," + sep + '"hint": ' + json.dumps(hint, ensure_ascii=False)
            text, n = pattern.subn(repl, text)
            moved += n
            break
        else:
            leftovers.append(f"sentence not found as text: {old}")

    if moved:
        # Re-parse and compare with the intended result before writing.
        expect = json.loads(open(path, encoding="utf-8").read())
        for ex in expect.get("exercises", []):
            if ex.get("type") == "fill-blank" and "hint" not in ex and ex.get("sentence") in plan and len(plan[ex["sentence"]]) == 1:
                new, hint = next(iter(plan[ex["sentence"]]))
                ex["sentence"], ex["hint"] = new, hint
        got = json.loads(text)
        if got != expect:
            return 0, [f"{path}: edited file does not match the intended result; not written"]
        if write:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
    return moved, leftovers


def main():
    write = "--write" in sys.argv
    total, files, leftovers = 0, 0, []
    for path in sorted(glob.glob(os.path.join(ROOT, "content", "*", "exercises", "**", "*.json"), recursive=True)):
        n, left = migrate_file(path, write)
        total += n
        files += bool(n)
        leftovers += [f"{os.path.relpath(path, ROOT)}: {x}" for x in left]
    print(f"{'moved' if write else 'would move'} {total} hints in {files} files")
    for x in leftovers:
        print("  LEFT", x)


if __name__ == "__main__":
    main()
