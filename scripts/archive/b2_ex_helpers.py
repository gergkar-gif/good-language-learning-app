"""
Exercise builder helpers for Hungarian B2 Core Units.
Ensures strict compliance with category, stage, teaches, and english fields.
"""

def mc(cat, stage, question, options, correct, teaches):
    assert cat in ("vocabulary", "grammar", "reading"), f"Invalid category: {cat}"
    assert isinstance(options, list) and len(options) >= 2, "Options must be a list of at least 2 items"
    assert 0 <= correct < len(options), f"Correct index {correct} out of range for options"
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
    assert cat in ("vocabulary", "grammar"), f"Invalid category: {cat}"
    assert isinstance(pairs, list) and len(pairs) >= 2, "Pairs must be a list of at least 2 pairs"
    return {
        "type": "matching",
        "category": cat,
        "stage": stage,
        "pairs": pairs,
        "teaches": teaches,
    }


def fb(cat, stage, sentence, answer, english, teaches):
    assert cat in ("vocabulary", "grammar"), f"Invalid category: {cat}"
    assert "____" in sentence, f"Sentence must contain blank '____': {sentence}"
    assert english and len(english.strip()) > 0, "English translation required for fill-blank"
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
    assert cat in ("vocabulary", "grammar"), f"Invalid category: {cat}"
    assert isinstance(tiles, list) and len(tiles) >= 2, "Tiles must be a list of at least 2 tokens"
    assert isinstance(solution, list) and len(solution) >= 2, "Solution must be a list of tokens"
    assert english and len(english.strip()) > 0, "English translation required for sentence-builder"
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
    assert isinstance(prompt, list) and len(prompt) >= 2, "Prompt must be a list of dialogue turns"
    assert isinstance(options, list) and len(options) >= 2, "Options must be a list of at least 2 choices"
    assert 0 <= correct < len(options), f"Correct index {correct} out of range"
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
    assert isinstance(template, list) and len(template) >= 1, "Template must be a list of prompt/answer dicts"
    return {
        "type": "structured-writing",
        "category": "writing",
        "stage": stage,
        "template": template,
        "teaches": teaches,
    }
