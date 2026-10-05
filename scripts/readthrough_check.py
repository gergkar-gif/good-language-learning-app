#!/usr/bin/env python3
"""Sanity-check a unit's read-through decisions before apply_tags.py (ROADMAP 125 step 3).

    python scripts/readthrough_check.py hu a1 objects-locations decisions.json

Errors: an exercise without a decision (or a decision for one outside the
unit), an unknown or retired slug, a skill above the unit's level, a
`distractor_skills` index that isn't a wrong option or names a non-grammar
skill, a matching exercise tagged with anything but a vocabulary skill.
Warnings: a grammar skill whose screen comes after the exercise's
lesson, a category that doesn't follow the tag, identical exercises
given different tags, `distractor_skills` on a question about suffix names,
an Igen/Nem contradiction not tagged `yes-no-questions`,
`ik-verbs-dolgozom-not-dolgozok` on an answer that isn't a 1st-person -m form,
the answer printed in the prompt, and a fill-blank hint that names no person
for a person- or possessor-marked answer.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]
FOLLOWS = {"multiple-choice", "fill-blank", "sentence-builder", "matching"}
PERSON_WORDS = re.compile(r"\b(I|you|he|she|it|we|they|my|your|his|her|its|our|their|one's|yours|mine|ours|theirs|me|us|them|him)\b", re.I)
PERSON_END = re.compile(r"(om|em|öm|am|ad|ed|od|öd|unk|ünk|atok|etek|otok|ötök|uk|ük|tok|tek|tök|nk|ja|je|ják|jük|juk|ják|jék)$", re.I)
CONTENT_KEYS = ("question", "sentence", "options", "pairs", "solution", "prompt", "template", "answer", "answers")


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def words(t):
    return re.findall(r"[^\W\d_]+", (t or "").lower())


def answer_text(e):
    """The accepted answer as a string, for the item types that have one."""
    opts = e.get("options") or []
    if isinstance(e.get("correct"), int) and opts and isinstance(opts[e["correct"]], str):
        return opts[e["correct"]]
    a = e.get("answers") or e.get("answer")
    return (a[0] if isinstance(a, list) else a) if a else ""


def prompt_text(e):
    if e.get("type") == "dialogue-complete":
        return " ".join(l.get("text", "") for l in e.get("prompt") or [] if "_" not in l.get("text", ""))
    return e.get("sentence") or e.get("question") or ""


def lesson_no(ref):
    m = re.match(r"[a-z]\d-(\d+)", ref or "")
    return int(m.group(1)) if m else None


def main():
    lang, level, uid, dec_path = sys.argv[1], sys.argv[2].lower(), sys.argv[3], sys.argv[4]
    course = ROOT / "content" / lang
    unit = next(u for u in load(course / "curriculum" / "units" / f"{level}.json") if u["id"] == uid)
    reg = load(ROOT / "skills" / f"{lang.split('-')[0]}.json")["skills"]
    dec = load(dec_path)
    errors, warns = [], []
    seen, by_content = set(), defaultdict(set)
    for stem in unit["stems"]:
        ep = course / "exercises" / level / f"{stem}-ex.json"
        if not ep.exists():
            continue
        for e in load(ep)["exercises"]:
            eid = e["id"]
            seen.add(eid)
            d = dec.get(eid)
            if not d:
                errors.append(f"{eid}: no decision")
                continue
            slug = d.get("teaches")
            if not slug and (d.get("category") or e.get("category")) == "reading":
                continue  # reading comprehension stays untagged (spec: teaches not required)
            sk = reg.get(slug)
            if not sk or sk.get("retired"):
                errors.append(f"{eid}: unknown or retired slug {slug!r}")
                continue
            if LEVELS.index(sk["level"]) > LEVELS.index(level.upper()):
                errors.append(f"{eid}: {slug} is {sk['level']}")
            if sk["kind"] == "grammar":
                t, here = lesson_no(sk.get("taught_in")), lesson_no(stem)
                if sk["level"] == level.upper() and t and here and t > here:
                    warns.append(f"{eid}: {slug} is taught at {sk['taught_in']}, after this lesson")
            cat = d.get("category") or e.get("category")
            if (e.get("type") in FOLLOWS or cat in ("vocabulary", "grammar")) and cat not in ("reading", "listening") and cat != sk["kind"]:
                warns.append(f"{eid}: category {cat} but tag is {sk['kind']}")
            opts = e.get("options") or []
            if e.get("type") == "matching" and sk["kind"] != "vocabulary":
                errors.append(f"{eid}: matching is always vocabulary, not {slug}")
            ans, ptxt = answer_text(e), prompt_text(e)
            if e.get("type") in ("multiple-choice", "dialogue-complete") and len(opts) > 1 and opts and all(isinstance(o, str) for o in opts):
                if (d.get("ds") or {}) and sum(o.lstrip().startswith("-") for o in opts) * 2 > len(opts):
                    warns.append(f"{eid}: ds on options that are suffix names, not word forms")
                right, wrong = opts[e["correct"]].lower(), [o.lower() for i, o in enumerate(opts) if i != e["correct"]]
                if (right.startswith("igen,") and any(w.startswith("nem,") for w in wrong)
                        or right.startswith("nem,") and any(w.startswith("igen,") for w in wrong)) and slug != "yes-no-questions":
                    warns.append(f"{eid}: Igen/Nem contradiction, tag is {slug}, not yes-no-questions")
            if slug == "ik-verbs-dolgozom-not-dolgozok" and ans and not re.search(r"m$", ans.strip(" .!?").split()[-1] if ans.split() else "", re.I):
                warns.append(f"{eid}: ik-verbs tag but answer {ans!r} is not a 1st-person -m form")
            aw = words(ans)
            if len("".join(aw)) >= 4 and e.get("type") in ("fill-blank", "multiple-choice", "dialogue-complete", "structured-writing") and ptxt:
                pw = words(re.sub(r"\([^)]*\)", " ", ptxt))
                if any(pw[i:i + len(aw)] == aw for i in range(len(pw) - len(aw) + 1)):
                    warns.append(f"{eid}: the answer {ans!r} is printed in the prompt")
            if e.get("type") == "fill-blank" and ans:
                hint = " ".join(re.findall(r"\(([^)]*)\)", ptxt))
                last = (words(ans) or [""])[-1]
                if PERSON_END.search(last) and len(last) > 4 and hint and not PERSON_WORDS.search(hint):
                    warns.append(f"{eid}: answer {ans!r} carries a person/possessor ending but hint ({hint}) names no person")
            for i, s2 in (d.get("ds") or {}).items():
                if not str(i).isdigit() or int(i) >= len(opts) or int(i) == e.get("correct"):
                    errors.append(f"{eid}: ds index {i} is not a wrong option")
                if (reg.get(s2) or {}).get("kind") != "grammar" or s2 == slug:
                    errors.append(f"{eid}: ds slug {s2!r} must be another grammar skill")
            key = json.dumps({k: e.get(k) for k in CONTENT_KEYS if k in e}, ensure_ascii=False, sort_keys=True)
            by_content[key].add((eid, slug))
    for eid in set(dec) - seen:
        errors.append(f"{eid}: decision for an exercise outside the unit")
    for group in by_content.values():
        if len({s for _, s in group}) > 1:
            warns.append("identical exercises, different tags: " + ", ".join(f"{i}={s}" for i, s in sorted(group)))
    for w in warns:
        print("warn ", w)
    for x in errors:
        print("ERROR", x)
    print(f"{len(seen)} exercises, {len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
