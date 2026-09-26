#!/usr/bin/env python3
"""
Generates Hungarian B2 Core Units 19, 20, and 21 (b2-19, b2-20, b2-21)
using build_core_unit from b2_unit_builder_helper.py.
"""
import sys
from pathlib import Path

sys.path.insert(
    0,
    r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch",
)
from b2_unit_builder_helper import build_core_unit


# ==============================================================================
# Exercise Builder Helpers
# ==============================================================================

def mc(cat, stage, question, options, correct, teaches=None):
    res = {
        "type": "multiple-choice",
        "category": cat,
        "stage": stage,
        "question": question,
        "options": options,
        "correct": correct,
    }
    if teaches:
        res["teaches"] = teaches
    return res


def match(cat, stage, pairs, teaches):
    return {
        "type": "matching",
        "category": cat,
        "stage": stage,
        "pairs": pairs,
        "teaches": teaches,
    }


def fb(cat, stage, sentence, answer, english, teaches):
    return {
        "type": "fill-blank",
        "category": cat,
        "stage": stage,
        "sentence": sentence,
        "answer": answer,
        "english": english,
        "teaches": teaches,
    }


def sb(cat, stage, tiles, solution, english, teaches):
    return {
        "type": "sentence-builder",
        "category": cat,
        "stage": stage,
        "tiles": tiles,
        "solution": solution,
        "english": english,
        "teaches": teaches,
    }


def dc(stage, prompt, options, correct, teaches):
    return {
        "type": "dialogue-complete",
        "category": "dialogue",
        "stage": stage,
        "prompt": prompt,
        "options": options,
        "correct": correct,
        "teaches": teaches,
    }


def sw(stage, template, teaches):
    return {
        "type": "structured-writing",
        "category": "writing",
        "stage": stage,
        "template": template,
        "teaches": teaches,
    }


def main():
    scope = {
        "mc": mc,
        "match": match,
        "fb": fb,
        "sb": sb,
        "dc": dc,
        "sw": sw,
    }
    scratch_dir = Path(r"C:\Users\Admin\.gemini\antigravity\brain\88f00c8c-948f-4b0c-b4aa-9eb37679731c\scratch")

    for u in (19, 20, 21):
        code_file = scratch_dir / f"unit{u}_code.py"
        exec(code_file.read_text(encoding="utf-8"), scope)
        unit_spec = scope[f"UNIT_{u}"]
        print(f"Building Core Unit {u}: {unit_spec['title']}")
        build_core_unit(unit_spec)

    print("Successfully built Hungarian B2 Core Units 19, 20, and 21!")


if __name__ == "__main__":
    main()
