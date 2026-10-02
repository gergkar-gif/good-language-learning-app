#!/usr/bin/env python3
"""
Generator for Hungarian C1 Block 1 Remaining Units:
  - Unit 02: Core (c1-02) & Discourse (c1-esszemuveszet)
  - Unit 03: Core (c1-03) & Discourse (c1-tudomanyelmelet)
  - Unit 04: Core (c1-04) & Discourse (c1-vitakultura)
  - Unit 05: Core (c1-05) & Discourse (c1-pesti-ironia)
  - Unit 06: Core (c1-06) & Discourse (c1-metaforak)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "content" / "hu"


def write_json(rel_path: str, data: dict):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def mc(cat, stage, question, options, correct, teaches):
    res = {
        "id": "",
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
        "id": "",
        "type": "matching",
        "category": cat,
        "stage": stage,
        "pairs": pairs,
        "teaches": teaches,
    }


def fb(cat, stage, sentence, answer, english, teaches):
    assert "____" in sentence, f"Sentence must contain blank '____': {sentence}"
    assert english and len(english.strip()) > 0, "English translation required for fill-blank"
    return {
        "id": "",
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
        "id": "",
        "type": "sentence-builder",
        "category": cat,
        "stage": stage,
        "tiles": tiles,
        "solution": solution,
        "english": english,
        "teaches": teaches,
    }


def update_registries():
    # 1. skill-registry.json
    sr_path = BASE / "indexes" / "skill-registry.json"
    sr = json.loads(sr_path.read_text(encoding="utf-8"))
    new_skills = {
        # Vocab skills
        "c1-02-vocab": {"kind": "vocabulary"},
        "c1-esszemuveszet-vocab": {"kind": "vocabulary"},
        "c1-03-vocab": {"kind": "vocabulary"},
        "c1-tudomanyelmelet-vocab": {"kind": "vocabulary"},
        "c1-04-vocab": {"kind": "vocabulary"},
        "c1-vitakultura-vocab": {"kind": "vocabulary"},
        "c1-05-vocab": {"kind": "vocabulary"},
        "c1-pestiironia-vocab": {"kind": "vocabulary"},
        "c1-06-vocab": {"kind": "vocabulary"},
        "c1-metaforak-vocab": {"kind": "vocabulary"},

        # Grammar skills
        "c1-dense-participles": {"kind": "grammar"},
        "c1-complex-adverbials": {"kind": "grammar"},
        "c1-nominal-compression": {"kind": "grammar"},
        "c1-essayistic-register": {"kind": "grammar"},
        "c1-stylistic-politeness": {"kind": "grammar"},

        "c1-epistemic-hedging": {"kind": "grammar"},
        "c1-evidentiality-markers": {"kind": "grammar"},
        "c1-modal-distancing": {"kind": "grammar"},
        "c1-scientific-paradigm-discourse": {"kind": "grammar"},
        "c1-epistemic-skepticism": {"kind": "grammar"},

        "c1-rhetorical-refutation": {"kind": "grammar"},
        "c1-polemical-topicalization": {"kind": "grammar"},
        "c1-reductio-argumentation": {"kind": "grammar"},
        "c1-parliamentary-debate": {"kind": "grammar"},
        "c1-persuasive-oratory": {"kind": "grammar"},

        "c1-ironic-particles": {"kind": "grammar"},
        "c1-antiphrasis-understatement": {"kind": "grammar"},
        "c1-subtle-disclaimer": {"kind": "grammar"},
        "c1-satirical-discourse": {"kind": "grammar"},
        "c1-parodic-inversion": {"kind": "grammar"},

        "c1-idiomatic-compounding": {"kind": "grammar"},
        "c1-conceptual-blending": {"kind": "grammar"},
        "c1-deadjectival-abstraction": {"kind": "grammar"},
        "c1-embodied-spatial-metaphor": {"kind": "grammar"},
        "c1-cultural-semiotics": {"kind": "grammar"},
    }
    for k, v in new_skills.items():
        if k not in sr["skills"]:
            sr["skills"][k] = v
    sr_path.write_text(json.dumps(sr, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Updated skill-registry.json")

    # 2. grammar-titles.json
    gt_path = BASE / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))
    new_titles = {
        "c1-02-vocab": "reading",
        "c1-esszemuveszet-vocab": "reading",
        "c1-03-vocab": "reading",
        "c1-tudomanyelmelet-vocab": "reading",
        "c1-04-vocab": "reading",
        "c1-vitakultura-vocab": "reading",
        "c1-05-vocab": "reading",
        "c1-pestiironia-vocab": "reading",
        "c1-06-vocab": "reading",
        "c1-metaforak-vocab": "reading",

        "c1-dense-participles": "dense left-branching participial clauses and pre-nominal structures",
        "c1-complex-adverbials": "complex adverbial structures and temporal clause stacking",
        "c1-nominal-compression": "syntactic compression and abstract nominal constructions",
        "c1-essayistic-register": "essayistic register markers and stylistic literary phrasing",
        "c1-stylistic-politeness": "stylistic politeness and formal discourse distancing",

        "c1-epistemic-hedging": "epistemic hedging and degrees of academic certainty",
        "c1-evidentiality-markers": "evidentiality markers and reported information calibration",
        "c1-modal-distancing": "modal distancing and hypothetical epistemic formulations",
        "c1-scientific-paradigm-discourse": "scientific paradigm discourse and academic reasoning",
        "c1-epistemic-skepticism": "philosophical skepticism and critical empirical framing",

        "c1-rhetorical-refutation": "rhetorical refutation and polemical counter-argumentation",
        "c1-polemical-topicalization": "polemical focus topicalization and emphatic word order",
        "c1-reductio-argumentation": "reductio ad absurdum and logical contradiction framing",
        "c1-parliamentary-debate": "formal parliamentary debate phrasing and procedural rhetoric",
        "c1-persuasive-oratory": "persuasive public oratory and oratorical discourse formulas",

        "c1-ironic-particles": "nuanced ironic pragmatic particles in public commentary",
        "c1-antiphrasis-understatement": "rhetorical understatement antiphrasis and litotes",
        "c1-subtle-disclaimer": "subtle disclaimers and polite dissent formulations",
        "c1-satirical-discourse": "satirical discourse and urban humor registers",
        "c1-parodic-inversion": "parodic register inversion and cultural mock debate",

        "c1-idiomatic-compounding": "advanced idiomatic compound nouns and metaphoric expressions",
        "c1-conceptual-blending": "conceptual blending and complex figurative imagery",
        "c1-deadjectival-abstraction": "deadjectival abstract nominalizations and poetic philosophy",
        "c1-embodied-spatial-metaphor": "embodied spatial metaphors and Hungarian directional cases",
        "c1-cultural-semiotics": "cultural semiotics and idiomatic world models",
    }
    for k, v in new_titles.items():
        gt[k] = v
    gt_path.write_text(json.dumps(gt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json")

    # 3. curriculum/units/c1.json
    unit_table = [
        # Unit 1
        {
            "title": "The Architecture of Argument & Logical Cohesion",
            "stems": ["c1-01-01", "c1-01-02", "c1-01-03", "c1-01-04", "c1-01-05", "c1-01-consolidation"],
            "track": "core"
        },
        {
            "title": "Language as Worldview: Humboldt, Kosztolányi & Cognitive Linguistics",
            "stems": ["c1-nyelvfilozofia-01", "c1-nyelvfilozofia-02", "c1-nyelvfilozofia-03", "c1-nyelvfilozofia-04", "c1-nyelvfilozofia-05", "c1-nyelvfilozofia-consolidation"],
            "track": "discourse"
        },
        # Unit 2
        {
            "title": "Syntactic Compression & Dense Participial Modification",
            "stems": ["c1-02-01", "c1-02-02", "c1-02-03", "c1-02-04", "c1-02-05", "c1-02-consolidation"],
            "track": "core"
        },
        {
            "title": "The Golden Age of the Hungarian Essay",
            "stems": ["c1-esszemuveszet-01", "c1-esszemuveszet-02", "c1-esszemuveszet-03", "c1-esszemuveszet-04", "c1-esszemuveszet-05", "c1-esszemuveszet-consolidation"],
            "track": "discourse"
        },
        # Unit 3
        {
            "title": "Epistemic Hedging, Probability & Evidential Stance",
            "stems": ["c1-03-01", "c1-03-02", "c1-03-03", "c1-03-04", "c1-03-05", "c1-03-consolidation"],
            "track": "core"
        },
        {
            "title": "Epistemology & Scientific Paradigm Shifts",
            "stems": ["c1-tudomanyelmelet-01", "c1-tudomanyelmelet-02", "c1-tudomanyelmelet-03", "c1-tudomanyelmelet-04", "c1-tudomanyelmelet-05", "c1-tudomanyelmelet-consolidation"],
            "track": "discourse"
        },
        # Unit 4
        {
            "title": "The Mechanics of Polemics & Rhetorical Refutation",
            "stems": ["c1-04-01", "c1-04-02", "c1-04-03", "c1-04-04", "c1-04-05", "c1-04-consolidation"],
            "track": "core"
        },
        {
            "title": "The Art of Hungarian Public Debate",
            "stems": ["c1-vitakultura-01", "c1-vitakultura-02", "c1-vitakultura-03", "c1-vitakultura-04", "c1-vitakultura-05", "c1-vitakultura-consolidation"],
            "track": "discourse"
        },
        # Unit 5
        {
            "title": "Irony, Understatement & Sarcastic Register Shifting",
            "stems": ["c1-05-01", "c1-05-02", "c1-05-03", "c1-05-04", "c1-05-05", "c1-05-consolidation"],
            "track": "core"
        },
        {
            "title": "Urban Satire as Political Defense",
            "stems": ["c1-pestiironia-01", "c1-pestiironia-02", "c1-pestiironia-03", "c1-pestiironia-04", "c1-pestiironia-05", "c1-pestiironia-consolidation"],
            "track": "discourse"
        },
        # Unit 6
        {
            "title": "Metaphor, Idiomatic Resonance & Conceptual Blending",
            "stems": ["c1-06-01", "c1-06-02", "c1-06-03", "c1-06-04", "c1-06-05", "c1-06-consolidation"],
            "track": "core"
        },
        {
            "title": "The Metaphorical Landscape of Hungarian",
            "stems": ["c1-metaforak-01", "c1-metaforak-02", "c1-metaforak-03", "c1-metaforak-04", "c1-metaforak-05", "c1-metaforak-consolidation"],
            "track": "discourse"
        },
    ]
    u_path = BASE / "curriculum" / "units" / "c1.json"
    u_path.parent.mkdir(parents=True, exist_ok=True)
    u_path.write_text(json.dumps(unit_table, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Wrote curriculum/units/c1.json")


if __name__ == "__main__":
    update_registries()

