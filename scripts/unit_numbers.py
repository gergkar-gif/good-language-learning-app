"""Unit numbers as the app shows them: the one rule for every course (user, 2026-11-13).

build-manifest.py numbers units per track: in a level with two tracks, each
starts at Unit 1. Every "Unit N" written in content follows it:

- "<Level> Unit N" is the Nth unit of the level's core track (or of its only
  track): "You know *viszont* from B1 Unit 11".
- A unit of another track names it: "<Level> <Track> Unit N", with <Track> the
  short name below ("from B1 Citizenship Unit 7", "B2 Culture Unit 4").

Used by prior_knowledge.py (knowledge sheets), check_unit_refs.py (recap
check) and renumber_unit_refs.py (the one-time conversion of recaps written
by table position).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]
# short track names used in text, per (course, track id); titles in build-manifest.py LEVEL_TRACKS
SHORT = {"citizenship": "Citizenship", "culture": "Culture", "cultura": "Cultura", "latam": "Latin America"}
REF = re.compile(r"\b(A1|A2|B1|B2|C1|C2)(?: (Citizenship|Culture|Cultura|Latin America))? Unit (\d+)\b")


def table(course, level):
    p = ROOT / f"content/{course}/curriculum/units/{level}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else []


def main_track(units):
    tracks = [u.get("track") for u in units]
    return "core" if "core" in tracks else (tracks[0] if tracks else None)


def number(course, level, index, units=None):
    """(track, N) of the unit at table index `index` (0-based)."""
    units = units if units is not None else table(course, level)
    tr = units[index].get("track")
    return tr, sum(1 for u in units[:index + 1] if u.get("track") == tr)


def name(course, level, index, units=None):
    """The text name of the unit at table index `index`: "B1 Unit 11", "B1 Citizenship Unit 7"."""
    units = units if units is not None else table(course, level)
    tr, n = number(course, level, index, units)
    if tr == main_track(units) or tr is None:
        return f"{level.upper()} Unit {n}"
    return f"{level.upper()} {SHORT.get(tr, tr.title())} Unit {n}"


def resolve(course, level, track_name, n, units=None):
    """Table index of "<level> [<track>] Unit n", or None."""
    units = units if units is not None else table(course, level)
    if track_name:
        tr = next((k for k, v in SHORT.items() if v == track_name), track_name.lower())
    else:
        tr = main_track(units)
    c = 0
    for i, u in enumerate(units):
        if u.get("track") == tr:
            c += 1
            if c == n:
                return i
    return None
