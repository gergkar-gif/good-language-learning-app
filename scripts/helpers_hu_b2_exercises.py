#!/usr/bin/env python3
"""
Common exercise builder helper functions for Hungarian B2 Core Units.
Ensures uniform schema compliance and metadata tagging.
"""

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
