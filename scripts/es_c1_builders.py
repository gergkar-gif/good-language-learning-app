#!/usr/bin/env python3
"""Builders for ES C1 unit files (from the Units 3-4 writer's generator, 2026-11-18).

A writer can generate a unit's JSON from short Python data instead of copying
field names from model files (the field shapes below are those of the frozen
C1 units). Import it from a scratch script run in the worktree:

    import sys; sys.path.insert(0, "scripts"); from es_c1_builders import *
    w("exercises/c1/c1-05-01-ex.json", exfile("c1-05-01", [mc(...), fb(...), ...]))

Paths given to w() are relative to content/es-latam/ in the current directory.
Every builder writes `teaches` as a one-slug list; check-content and the
validator still decide whether the result is right.
"""
import json
import os

ROOT = os.path.join(os.getcwd(), "content", "es-latam")


def w(rel, obj):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def T(t):
    return t if isinstance(t, list) else [t]


def mc(i, q, opts, c, t, cat="grammar", ds=None):
    d = {"id": i, "type": "multiple-choice", "category": cat, "question": q, "options": opts, "correct": c, "teaches": T(t)}
    if ds:
        d["distractor_skills"] = ds
    return d


def fb(i, s, a, en, h, t, answers=None):
    d = {"id": i, "type": "fill-blank", "category": "vocabulary" if str(t).endswith("vocab") else "grammar", "sentence": s}
    if answers:
        d["answers"] = answers
    else:
        d["answer"] = a
    d["english"], d["hint"], d["teaches"] = en, h, T(t)
    return d


def match(i, pairs, t):
    return {"id": i, "type": "matching", "category": "vocabulary", "pairs": pairs, "teaches": T(t)}


def dic(i, s, en, t):
    return {"id": i, "type": "dictation", "category": "listening", "sentence": s, "english": en, "teaches": T(t)}


def lc(i, s, opts, c, t):
    return {"id": i, "type": "listening-choice", "category": "listening", "sentence": s, "options": opts, "correct": c, "teaches": T(t)}


def dlg(i, a, b, opts, c, t, ds=None):
    """a = ("C" or "M", first line); the learner completes the other speaker's line (b is unused, kept for symmetry)."""
    first, second = ("Carlos", "Meg") if a[0] == "C" else ("Meg", "Carlos")
    d = {"id": i, "type": "dialogue-complete", "category": "dialogue",
         "prompt": [{"speaker": first, "text": a[1]}, {"speaker": second, "text": "_____"}],
         "options": opts, "correct": c, "teaches": T(t)}
    if ds:
        d["distractor_skills"] = ds
    return d


def sb(i, tiles, sol, en, t):
    return {"id": i, "type": "sentence-builder", "category": "grammar", "tiles": tiles, "solution": sol, "english": en, "teaches": T(t)}


def sw(i, tpl, t):
    return {"id": i, "type": "structured-writing", "category": "writing",
            "template": [{"prompt": p, "answer": a} for p, a in tpl], "teaches": T(t)}


def rd(i, q, opts, c):
    return {"id": i, "type": "multiple-choice", "category": "reading", "question": q, "options": opts, "correct": c}


def grp(title, stem, nums):
    return {"type": "exercise-group", "title": title, "ref": f"exercises/c1/{stem}-ex.json",
            "exerciseRefs": [f"{stem}.ex{n:02d}" for n in nums]}


def lesson(stem, lid, title, goal, gram, items, groups, screens, story=None):
    """groups: exercise-group dicts in order, plus the markers "STORY" and "SRS"."""
    secs = [{"type": "goal", "items": items}, {"type": "recycle", "title": "Quick Review"}]
    secs += [{"type": "grammar", "ref": f"grammar/c1/{s}.json"} for s in screens]
    if not stem.endswith("consolidation"):
        secs.append({"type": "vocabulary", "ref": f"vocabulary/c1/{stem}-voc.json"})
    for g in groups:
        if g == "STORY":
            secs.append({"type": "story", "ref": story})
        elif g == "SRS":
            secs.append({"type": "srs", "title": "Add to Review"})
        else:
            secs.append(g)
    secs.append({"type": "checklist", "title": "Can you do this?", "items": items})
    return {"id": lid, "title": title, "level": "C1", "goal": goal, "grammar": gram, "sections": secs}


def gr(gid, title, text, tables, examples, tip):
    secs = [{"type": "text", "content": text}]
    secs += [{"type": "table", "title": tt, "rows": rows} for tt, rows in tables]
    secs.append({"type": "examples", "title": "In context", "items": [{"spanish": a, "english": b} for a, b in examples]})
    secs.append({"type": "tip", "content": tip})
    return {"id": gid, "title": title, "sections": secs}


def voc(stem, title, theme, words):
    """stem like c1-05-01; words = [(lemma, translation, pos), ...]."""
    _, unit, n = stem.split("-")
    return {"id": f"vocab.c1.{unit}.{n}", "lesson": stem, "title": title, "theme": theme,
            "words": [{"lemma": a, "translation": b, "pos": c} for a, b, c in words]}


def exfile(stem, ex):
    return {"lesson": stem, "exercises": ex}
