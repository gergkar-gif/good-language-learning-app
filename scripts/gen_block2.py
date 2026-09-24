# -*- coding: utf-8 -*-
"""
Generator for Block 2: Units 9–12 (Hungarian Citizenship Track)
Unit 9:  b1-mohacs (The Battle of Mohács 1526)
Unit 10: b1-haromresz (Three Parts of Hungary 1541-1686)
Unit 11: b1-erdelyaranykora (Transylvania's Golden Age)
Unit 12: b1-torokkiuzese (Driving Out the Ottomans)
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(".")
LESSONS_DIR = ROOT / "content/hu/lessons/b1"
GRAMMAR_DIR = ROOT / "content/hu/grammar/b1"
VOCAB_DIR = ROOT / "content/hu/vocabulary/b1"
EXERCISES_DIR = ROOT / "content/hu/exercises/b1"
STORIES_DIR = ROOT / "content/hu/stories/world/b1"

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def make_story(id_str, title, summary, location, grammar_topics, vocab_topics, paragraphs_text, key_voc, comp_questions):
    paras = [{"type": "narration", "text": p} for p in paragraphs_text]
    total_time = 0.0
    segments = []
    for i, p in enumerate(paragraphs_text):
        dur = max(4.0, round(len(p.split()) * 0.45, 1))
        start = total_time
        end = round(start + dur, 1)
        total_time = end
        segments.append({
            "paraIndex": i,
            "startTime": start,
            "endTime": end,
            "speaker": "Narrator",
            "lang": "hu",
            "cues": [{"type": "pause", "durationMs": 250, "reason": "clause-boundary"}] if i < len(paragraphs_text)-1 else [],
            "pronunciations": []
        })

    return {
        "id": id_str,
        "title": title,
        "level": "B1",
        "estimatedMinutes": 5,
        "summary": summary,
        "characters": [],
        "location": location,
        "grammar": grammar_topics,
        "vocabularyTopics": vocab_topics,
        "paragraphs": paras,
        "narration": {
            "durationSeconds": total_time,
            "pacing": {
                "speedMultiplier": 1.0,
                "rate_str": "+0%",
                "rate_wpm": 150,
                "style": "natural, expressive"
            },
            "speakers": {
                "Narrator": {
                    "role": "narrator",
                    "gender": "neutral",
                    "tone": "clear, warm, steady storytelling guide"
                }
            },
            "segments": segments,
            "pedagogical": {
                "keyVocabulary": key_voc,
                "targetGrammar": grammar_topics,
                "comprehensionQuestions": comp_questions
            }
        }
    }

def make_lesson(lesson_id, title, grammar_label, intro_body, goals, story_ref, voc_ref, gr_ref, ex_ref, ex_ids):
    sections = [
        {"type": "intro", "title": title.split(" - ")[0] if " - " in title else title, "body": intro_body},
        {"type": "goal", "title": "Lesson Goals", "items": goals},
        {"type": "recycle", "count": 3},
        {"type": "story", "ref": story_ref},
        {"type": "vocabulary", "ref": voc_ref},
        {"type": "grammar", "ref": gr_ref},
        {"type": "exercise-group", "title": "Practice", "ref": ex_ref, "exerciseRefs": ex_ids},
        {"type": "srs"},
        {"type": "checklist", "items": goals}
    ]
    return {
        "id": lesson_id,
        "title": title,
        "level": "B1",
        "track": "citizenship",
        "estimatedMinutes": 15,
        "prerequisites": [],
        "grammar": [grammar_label],
        "vocabulary": [voc_ref],
        "culturalContext": "Magyar történelem és állampolgársági ismeretek (Honosítási tananyag)",
        "sections": sections
    }

def make_vocab(voc_id, title, desc, entries):
    return {
        "id": voc_id,
        "title": title,
        "description": desc,
        "entries": entries
    }

def make_grammar(gr_id, title, desc, rules, tables, examples):
    return {
        "id": gr_id,
        "title": title,
        "description": desc,
        "rules": rules,
        "tables": tables,
        "examples": examples
    }

def make_exercise_group(group_id, title, desc, exercises):
    return {
        "id": group_id,
        "title": title,
        "description": desc,
        "exercises": exercises
    }

def make_consolidation_lesson(cons_id, title, intro_body, goals, ex_ref, ex_ids):
    sections = [
        {"type": "intro", "title": title, "body": intro_body},
        {"type": "goal", "title": "Consolidation Goals", "items": goals},
        {"type": "exercise-group", "title": "Comprehensive Unit Practice", "ref": ex_ref, "exerciseRefs": ex_ids},
        {"type": "checklist", "items": goals}
    ]
    return {
        "id": cons_id,
        "title": title,
        "level": "B1",
        "track": "citizenship",
        "estimatedMinutes": 25,
        "prerequisites": [],
        "grammar": ["Unit review"],
        "vocabulary": ["Unit review"],
        "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
        "sections": sections
    }

print("Block 2 generator base loaded...")
