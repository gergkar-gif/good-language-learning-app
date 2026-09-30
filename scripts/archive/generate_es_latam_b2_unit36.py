#!/usr/bin/env python3
"""
generate_es_latam_b2_unit36.py

Generates Latin American Spanish B2 Unit 36 (Capstone) for both tracks:
- Track 1 (Core B2): Unit 36 - Síntesis B2: La voz propia en español
  Classic: Jorge Luis Borges - El Aleph (1949)
- Track 2 (Regional Studies): Unit 36 - América Latina en el escenario global: Identidad, multilateralismo y porvenir
  Overview + 5 lessons + consolidation story

Strict schema conformance:
- Vocabulary: root {id: 'vocab.b2.36.01', lesson: 'b2-36-01', title, words: [{lemma, translation, pos}]}
- Exercises: root {lesson: 'b2-36-01', exercises: [{id: 'b2-36-01.ex01', type, category, teaches, ...}]}
- Grammar: root {id: 'grammar.b2.36.01.<skill>', title, sections: [{type: 'text'|'table'|'tip', content, rows}]}
- Lessons: root {id: 'lesson.b2.36.01', title, level: 'B2', sections: [...]}
- Stories: root {id, title, level: 'B2', lesson, type, estimatedMinutes, summary, characters, paragraphs: [{type: 'narration', text}], narration: {pedagogical: {comprehensionQuestions: [...]}}}
- Story word count strictly in [650, 825] words.
"""

import json
import re
from pathlib import Path

from make_unit36_stories import STORIES
from unit36_grammar_data import GRAMMAR_DATA
from unit36_exercises_data import EXERCISES_DATA
from unit36_lessons_data import LESSONS_DATA, CURRICULUM_ENTRIES

REPO_ROOT = Path(__file__).resolve().parent.parent
LATAM_DIR = REPO_ROOT / "content" / "es-latam"

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

NEW_SKILLS = {
    # Core 36 grammar skills
    "voz-cadencia-ritmo-sintactico": {
        "name": "syntactic rhythm and sentence cadence in formal prose",
        "kind": "grammar",
        "category": "grammar"
    },
    "voz-modalizacion-epistemica-compleja": {
        "name": "complex epistemic modalization and persuasive nuance",
        "kind": "grammar",
        "category": "grammar"
    },
    "voz-organizadores-macroestructurales-ensayo": {
        "name": "macrostructural organizers and essayistic cohesion",
        "kind": "grammar",
        "category": "grammar"
    },
    "voz-metaforas-conceptuales-retorica": {
        "name": "conceptual metaphors and rhetorical framing in public discourse",
        "kind": "grammar",
        "category": "grammar"
    },
    "voz-integracion-registro-estilo": {
        "name": "integration of personal voice and stylistic register modulation",
        "kind": "grammar",
        "category": "grammar"
    },
    # Regional 36 grammar skills
    "futuro-prospectiva-hipotesis-complejas": {
        "name": "complex predictive hypotheses and regional integration scenarios",
        "kind": "grammar",
        "category": "grammar"
    },
    "futuro-concesivas-ponderacion-riesgos": {
        "name": "strategic concession and risk weighting with si bien and aun a riesgo de",
        "kind": "grammar",
        "category": "grammar"
    },
    "futuro-diplomacia-compromiso-vinculante": {
        "name": "multilateral diplomatic commitments with binding subjunctives",
        "kind": "grammar",
        "category": "grammar"
    },
    "futuro-relativos-complejos-tratados": {
        "name": "complex relative clauses with el cual and cuyo in treaties",
        "kind": "grammar",
        "category": "grammar"
    },
    "futuro-sintesis-estrategica-proyeccion": {
        "name": "executive strategic synthesis and continental projection",
        "kind": "grammar",
        "category": "grammar"
    },
    # Vocabulary unit themes
    "b2-36-01-vocab": {
        "name": "syntactic rhythm and formal prose vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-36-02-vocab": {
        "name": "epistemic nuance and modal argumentation vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-36-03-vocab": {
        "name": "essay macrostructure and cohesive transitions vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-36-04-vocab": {
        "name": "conceptual metaphors and rhetorical framing vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-36-05-vocab": {
        "name": "personal voice and stylistic mastery vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "futuro-01-vocab": {
        "name": "geopolitical foresight and integration scenarios vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "futuro-02-vocab": {
        "name": "resource sovereignty and risk assessment vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "futuro-03-vocab": {
        "name": "multilateral climate diplomacy and treaties vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "futuro-04-vocab": {
        "name": "international treaty law and jurisdictional phrasing vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "futuro-05-vocab": {
        "name": "executive synthesis and continental integration vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    }
}

NEW_GRAMMAR_TITLES = {
    "voz-cadencia-ritmo-sintactico": "syntactic rhythm and sentence cadence in formal prose",
    "voz-modalizacion-epistemica-compleja": "complex epistemic modalization and persuasive nuance",
    "voz-organizadores-macroestructurales-ensayo": "macrostructural organizers and essayistic cohesion",
    "voz-metaforas-conceptuales-retorica": "conceptual metaphors and rhetorical framing in public discourse",
    "voz-integracion-registro-estilo": "personal voice integration and stylistic register modulation",
    "futuro-prospectiva-hipotesis-complejas": "complex predictive hypotheses and regional integration scenarios",
    "futuro-concesivas-ponderacion-riesgos": "strategic concession and risk weighting with si bien",
    "futuro-diplomacia-compromiso-vinculante": "multilateral diplomatic commitments with binding subjunctives",
    "futuro-relativos-complejos-tratados": "complex relative clauses with el cual and cuyo",
    "futuro-sintesis-estrategica-proyeccion": "executive strategic synthesis and continental projection"
}

VOCAB_DATA = {
    "b2-36-01": {
        "title": "Cadencia rítmica y prosa formal",
        "words": [
            {"lemma": "cadencia", "translation": "cadence / rhythmic flow", "pos": "noun"},
            {"lemma": "bimembrismo", "translation": "two-part parallel structure", "pos": "noun"},
            {"lemma": "contundencia", "translation": "persuasiveness / forceful impact", "pos": "noun"},
            {"lemma": "modulación", "translation": "modulation / tonal variation", "pos": "noun"},
            {"lemma": "armónico", "translation": "harmonious", "pos": "adjective"},
            {"lemma": "aforístico", "translation": "aphoristic / pithy", "pos": "adjective"},
            {"lemma": "compás", "translation": "rhythm / measure", "pos": "noun"},
            {"lemma": "alternar", "translation": "to alternate", "pos": "verb"},
            {"lemma": "hilvanar", "translation": "to weave together / stitch together ideas", "pos": "verb"},
            {"lemma": "elocuencia", "translation": "eloquence", "pos": "noun"}
        ]
    },
    "b2-36-02": {
        "title": "Modalización epistémica y matización",
        "words": [
            {"lemma": "cabría postular", "translation": "it might be posited", "pos": "expression"},
            {"lemma": "presumiblemente", "translation": "presumably", "pos": "adverb"},
            {"lemma": "inexorablemente", "translation": "inexorably", "pos": "adverb"},
            {"lemma": "aventurado", "translation": "bold / risky to assert", "pos": "adjective"},
            {"lemma": "colegirse", "translation": "to be deduced / gathered", "pos": "verb"},
            {"lemma": "matización", "translation": "nuance / qualification", "pos": "noun"},
            {"lemma": "certidumbre", "translation": "certainty", "pos": "noun"},
            {"lemma": "juicio crítico", "translation": "critical judgment", "pos": "expression"},
            {"lemma": "plausibilidad", "translation": "plausibility", "pos": "noun"},
            {"lemma": "distanciamiento reflexivo", "translation": "reflective distancing", "pos": "expression"}
        ]
    },
    "b2-36-03": {
        "title": "Macroestructura ensayística y cohesión",
        "words": [
            {"lemma": "por lo que atañe a", "translation": "as far as ... is concerned", "pos": "expression"},
            {"lemma": "en consonancia con", "translation": "in keeping with / in line with", "pos": "expression"},
            {"lemma": "a la luz de", "translation": "in light of", "pos": "expression"},
            {"lemma": "articulación", "translation": "structural articulation", "pos": "noun"},
            {"lemma": "macroestructura", "translation": "macrostructure", "pos": "noun"},
            {"lemma": "hilo conductor", "translation": "guiding thread", "pos": "expression"},
            {"lemma": "cohesión discursiva", "translation": "discursive cohesion", "pos": "expression"},
            {"lemma": "transición", "translation": "transition", "pos": "noun"},
            {"lemma": "correlato", "translation": "correlate / parallel", "pos": "noun"},
            {"lemma": "refrendar", "translation": "to substantiate / endorse", "pos": "verb"}
        ]
    },
    "b2-36-04": {
        "title": "Metáforas conceptuales y encuadre retórico",
        "words": [
            {"lemma": "metáfora conceptual", "translation": "conceptual metaphor", "pos": "expression"},
            {"lemma": "prisma", "translation": "prism / analytical lens", "pos": "noun"},
            {"lemma": "cauce", "translation": "riverbed / guiding channel", "pos": "noun"},
            {"lemma": "fragua", "translation": "forge / crucible", "pos": "noun"},
            {"lemma": "polisemia", "translation": "polysemy / multiple meanings", "pos": "noun"},
            {"lemma": "alegoría", "translation": "allegory", "pos": "noun"},
            {"lemma": "evocar", "translation": "to evoke", "pos": "verb"},
            {"lemma": "condensar", "translation": "to condense", "pos": "verb"},
            {"lemma": "resonancia", "translation": "resonance", "pos": "noun"},
            {"lemma": "imaginario colectivo", "translation": "collective imaginary", "pos": "expression"}
        ]
    },
    "b2-36-05": {
        "title": "Voz propia y madurez estilística",
        "words": [
            {"lemma": "voz propia", "translation": "personal authorial voice", "pos": "expression"},
            {"lemma": "impronta", "translation": "hallmark / imprint", "pos": "noun"},
            {"lemma": "versatilidad", "translation": "versatility", "pos": "noun"},
            {"lemma": "lucidez", "translation": "lucidity / intellectual clarity", "pos": "noun"},
            {"lemma": "sobriedad", "translation": "sobriety / restraint in style", "pos": "noun"},
            {"lemma": "madurez estilística", "translation": "stylistic maturity", "pos": "expression"},
            {"lemma": "desentrañar", "translation": "to unravel / fathom", "pos": "verb"},
            {"lemma": "plasmar", "translation": "to capture / express tangibly", "pos": "verb"},
            {"lemma": "convicción", "translation": "conviction", "pos": "noun"},
            {"lemma": "plenitud", "translation": "fullness / culmination", "pos": "noun"}
        ]
    },
    "b2-futuro-01": {
        "title": "Prospectiva geopolítica e integración",
        "words": [
            {"lemma": "prospectiva", "translation": "foresight / prospective analysis", "pos": "noun"},
            {"lemma": "de mediar", "translation": "if there were / should there be", "pos": "expression"},
            {"lemma": "escenario tendencial", "translation": "baseline projection scenario", "pos": "expression"},
            {"lemma": "viabilidad", "translation": "viability / feasibility", "pos": "noun"},
            {"lemma": "convergencia", "translation": "convergence", "pos": "noun"},
            {"lemma": "coyuntura geopolítica", "translation": "geopolitical juncture", "pos": "expression"},
            {"lemma": "amortiguar", "translation": "to cushion / absorb impact", "pos": "verb"},
            {"lemma": "interdependencia", "translation": "interdependence", "pos": "noun"},
            {"lemma": "asimetría", "translation": "asymmetry", "pos": "noun"},
            {"lemma": "proyectar", "translation": "to project / extrapolate", "pos": "verb"}
        ]
    },
    "b2-futuro-02": {
        "title": "Soberanía de recursos y ponderación de riesgos",
        "words": [
            {"lemma": "si bien", "translation": "while / although", "pos": "expression"},
            {"lemma": "aun a riesgo de", "translation": "even at the risk of", "pos": "expression"},
            {"lemma": "salvaguardia", "translation": "safeguard", "pos": "noun"},
            {"lemma": "litio", "translation": "lithium", "pos": "noun"},
            {"lemma": "cadena de valor", "translation": "value chain", "pos": "expression"},
            {"lemma": "soberanía energética", "translation": "energy sovereignty", "pos": "expression"},
            {"lemma": "despojo", "translation": "despoilment / dispossession", "pos": "noun"},
            {"lemma": "arbitraje internacional", "translation": "international arbitration", "pos": "expression"},
            {"lemma": "ponderar", "translation": "to weigh / balance", "pos": "verb"},
            {"lemma": "no alineamiento activo", "translation": "active non-alignment", "pos": "expression"}
        ]
    },
    "b2-futuro-03": {
        "title": "Compromiso multilateral y tratados",
        "words": [
            {"lemma": "refrendar el compromiso", "translation": "to endorse the commitment", "pos": "expression"},
            {"lemma": "convenir en que", "translation": "to agree that", "pos": "expression"},
            {"lemma": "vinculante", "translation": "binding", "pos": "adjective"},
            {"lemma": "fondo de contingencia", "translation": "contingency fund", "pos": "expression"},
            {"lemma": "multilateralismo", "translation": "multilateralism", "pos": "noun"},
            {"lemma": "concertación", "translation": "concertation / policy coordination", "pos": "noun"},
            {"lemma": "salvaguardar", "translation": "to safeguard", "pos": "verb"},
            {"lemma": "homologación", "translation": "reciprocal accreditation / standardization", "pos": "noun"},
            {"lemma": "diferendo limítrofe", "translation": "boundary dispute", "pos": "expression"},
            {"lemma": "declaración conjunta", "translation": "joint declaration", "pos": "expression"}
        ]
    },
    "b2-futuro-04": {
        "title": "Relativos formales y tratados internacionales",
        "words": [
            {"lemma": "en virtud del cual", "translation": "under which / by virtue of which", "pos": "expression"},
            {"lemma": "cuyo", "translation": "whose", "pos": "pronoun"},
            {"lemma": "al amparo del cual", "translation": "under the auspices of which", "pos": "expression"},
            {"lemma": "unívoco", "translation": "unambiguous / unequivocal", "pos": "adjective"},
            {"lemma": "cláusula dispositiva", "translation": "operative clause", "pos": "expression"},
            {"lemma": "instrumento de ratificación", "translation": "instrument of ratification", "pos": "expression"},
            {"lemma": "prevalecer", "translation": "to prevail", "pos": "verb"},
            {"lemma": "supletorio", "translation": "supplementary / subsidiary", "pos": "adjective"},
            {"lemma": "preámbulo", "translation": "preamble", "pos": "noun"},
            {"lemma": "patrimonio intangible", "translation": "intangible heritage", "pos": "expression"}
        ]
    },
    "b2-futuro-05": {
        "title": "Síntesis ejecutiva y horizontes continentales",
        "words": [
            {"lemma": "en síntesis", "translation": "in synthesis / in summary", "pos": "expression"},
            {"lemma": "a modo de corolario", "translation": "by way of corollary", "pos": "expression"},
            {"lemma": "punto de inflexión", "translation": "turning point", "pos": "expression"},
            {"lemma": "porvenir", "translation": "future / horizon ahead", "pos": "noun"},
            {"lemma": "Patria Grande", "translation": "Great Homeland (unified Latin America)", "pos": "expression"},
            {"lemma": "corolario", "translation": "corollary", "pos": "noun"},
            {"lemma": "recapitulación", "translation": "recapitulation", "pos": "noun"},
            {"lemma": "hoja de ruta", "translation": "roadmap", "pos": "expression"},
            {"lemma": "fraternidad continental", "translation": "continental brotherhood", "pos": "expression"},
            {"lemma": "consolidación", "translation": "consolidation", "pos": "noun"}
        ]
    }
}

def update_skill_registry():
    path = LATAM_DIR / "indexes" / "skill-registry.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_SKILLS.items():
        data["skills"][k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated skill-registry.json for Unit 36")

def update_grammar_titles():
    path = LATAM_DIR / "indexes" / "grammar-titles.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_GRAMMAR_TITLES.items():
        data[k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated grammar-titles.json for Unit 36")

def write_vocabulary():
    vocab_dir = LATAM_DIR / "vocabulary" / "b2"
    vocab_dir.mkdir(parents=True, exist_ok=True)
    for stem, vdata in VOCAB_DATA.items():
        if stem.startswith("b2-36"):
            vocab_id = f"vocab.b2.36.{stem.split('-')[-1]}"
        else:
            vocab_id = f"vocab.b2.futuro.{stem.split('-')[-1]}"
        doc = {
            "id": vocab_id,
            "lesson": stem,
            "title": vdata["title"],
            "words": vdata["words"]
        }
        out_path = vocab_dir / f"{stem}-voc.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")

def write_grammar():
    grammar_dir = LATAM_DIR / "grammar" / "b2"
    grammar_dir.mkdir(parents=True, exist_ok=True)
    slug_map = {
        "b2-36-01-a": ("grammar.b2.36.01.voz-cadencia-ritmo-sintactico", "voz-cadencia-ritmo-sintactico"),
        "b2-36-02-a": ("grammar.b2.36.02.voz-modalizacion-epistemica-compleja", "voz-modalizacion-epistemica-compleja"),
        "b2-36-03-a": ("grammar.b2.36.03.voz-organizadores-macroestructurales-ensayo", "voz-organizadores-macroestructurales-ensayo"),
        "b2-36-04-a": ("grammar.b2.36.04.voz-metaforas-conceptuales-retorica", "voz-metaforas-conceptuales-retorica"),
        "b2-36-05-a": ("grammar.b2.36.05.voz-integracion-registro-estilo", "voz-integracion-registro-estilo"),
        "b2-futuro-01-a": ("grammar.b2.futuro.01.futuro-prospectiva-hipotesis-complejas", "futuro-prospectiva-hipotesis-complejas"),
        "b2-futuro-02-a": ("grammar.b2.futuro.02.futuro-concesivas-ponderacion-riesgos", "futuro-concesivas-ponderacion-riesgos"),
        "b2-futuro-03-a": ("grammar.b2.futuro.03.futuro-diplomacia-compromiso-vinculante", "futuro-diplomacia-compromiso-vinculante"),
        "b2-futuro-04-a": ("grammar.b2.futuro.04.futuro-relativos-complejos-tratados", "futuro-relativos-complejos-tratados"),
        "b2-futuro-05-a": ("grammar.b2.futuro.05.futuro-sintesis-estrategica-proyeccion", "futuro-sintesis-estrategica-proyeccion")
    }
    for stem, gdata in GRAMMAR_DATA.items():
        gid, skill_slug = slug_map[stem]
        doc = {
            "id": gid,
            "title": gdata["title"],
            "sections": gdata["sections"]
        }
        out_path = grammar_dir / f"{stem}-gr.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")

def write_stories():
    for rel_key, story in STORIES.items():
        out_path = LATAM_DIR / "stories" / f"{rel_key}.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        full_text = " ".join(p["text"] for p in story["paragraphs"])
        wc = word_count(full_text)
        print(f"stories/{rel_key}.json: {wc} words")
        assert 650 <= wc <= 825, f"Word count out of bounds for {rel_key}: {wc}"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(story, f, ensure_ascii=False, indent=2)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")

def write_exercises():
    ex_dir = LATAM_DIR / "exercises" / "b2"
    ex_dir.mkdir(parents=True, exist_ok=True)
    for stem, ex_list in EXERCISES_DATA.items():
        doc = {
            "lesson": stem,
            "exercises": ex_list
        }
        out_path = ex_dir / f"{stem}-ex.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")

def write_lessons():
    lessons_dir = LATAM_DIR / "lessons" / "b2"
    lessons_dir.mkdir(parents=True, exist_ok=True)
    for stem, ldata in LESSONS_DATA.items():
        if stem.startswith("b2-36"):
            if "consolidation" in stem:
                lesson_id = "lesson.b2.36.consolidation"
            else:
                lesson_id = f"lesson.b2.36.{stem.split('-')[-1]}"
        else:
            if "consolidation" in stem:
                lesson_id = "lesson.b2.futuro.consolidation"
            else:
                lesson_id = f"lesson.b2.futuro.{stem.split('-')[-1]}"
        sections = []
        if "story_ref" in ldata:
            sections.append({
                "type": "story",
                "ref": ldata["story_ref"]
            })
        if "grammar_ref" in ldata:
            sections.append({
                "type": "grammar",
                "ref": ldata["grammar_ref"]
            })
        if "vocab_ref" in ldata:
            sections.append({
                "type": "vocabulary",
                "ref": ldata["vocab_ref"]
            })
        if "ex_ref" in ldata:
            group_title = "Review" if "consolidation" in stem else "Practice"
            sections.append({
                "type": "exercise-group",
                "title": group_title,
                "ref": ldata["ex_ref"],
                "exerciseRefs": ldata["ex_ids"]
            })
        doc = {
            "id": lesson_id,
            "title": ldata["title"],
            "level": "B2",
            "sections": sections
        }
        out_path = lessons_dir / f"{stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")

def update_curriculum():
    units_file = LATAM_DIR / "curriculum" / "units" / "b2.json"
    with open(units_file, "r", encoding="utf-8") as f:
        units = json.load(f)
    existing_stems = {s for u in units for s in u.get("stems", [])}
    for entry in CURRICULUM_ENTRIES:
        if not any(s in existing_stems for s in entry["stems"]):
            units.append(entry)
    with open(units_file, "w", encoding="utf-8") as f:
        json.dump(units, f, ensure_ascii=False, indent=2)
    print("Updated curriculum/units/b2.json with Unit 36!")

def main():
    update_skill_registry()
    update_grammar_titles()
    write_vocabulary()
    write_grammar()
    write_stories()
    write_exercises()
    write_lessons()
    update_curriculum()
    print("Unit 36 generation complete!")

if __name__ == "__main__":
    main()
