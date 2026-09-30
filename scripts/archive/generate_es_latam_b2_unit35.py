#!/usr/bin/env python3
"""
generate_es_latam_b2_unit35.py

Generates Latin American Spanish B2 Unit 35 for both tracks:
- Track 1 (Core B2): Unit 35 - Registros formales, ensayísticos y de prensa
  Classic: José María Arguedas - Los ríos profundos (1958)
- Track 2 (Regional Studies): Unit 35 - Pluralismo jurídico, autodeterminación y derechos indígenas en el siglo XXI
  Overview + 5 lessons + consolidation story

Strict schema conformance:
- Vocabulary: root {id: 'vocab.b2.35.01', lesson: 'b2-35-01', title, words: [{lemma, translation, pos}]}
- Exercises: root {lesson: 'b2-35-01', exercises: [{id: 'b2-35-01.ex01', type, category, teaches, ...}]}
- Grammar: root {id: 'grammar.b2.35.01.<skill>', title, sections: [{type: 'text'|'table'|'tip', content, rows}]}
- Lessons: root {id: 'lesson.b2.35.01', title, level: 'B2', sections: [...]}
- Stories: root {id, title, level: 'B2', lesson, type, estimatedMinutes, summary, characters, paragraphs: [{type: 'narration', text}], narration: {pedagogical: {comprehensionQuestions: [...]}}}
- Story word count strictly in [650, 825] words.
"""

import json
import re
from pathlib import Path

from make_unit35_stories import STORIES
from unit35_grammar_data import GRAMMAR_DATA
from unit35_exercises_data import EXERCISES_DATA
from unit35_lessons_data import LESSONS_DATA, CURRICULUM_ENTRIES

REPO_ROOT = Path(__file__).resolve().parent.parent
LATAM_DIR = REPO_ROOT / "content" / "es-latam"

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

NEW_SKILLS = {
    # Core 35 grammar skills
    "registro-nominalizacion-estilo-ensayistico": {
        "name": "nominalization strategies in academic and essayistic prose",
        "kind": "grammar",
        "category": "grammar"
    },
    "registro-impersonalidad-distanciamiento-discursivo": {
        "name": "discursive distancing and impersonal attribution in journalism",
        "kind": "grammar",
        "category": "grammar"
    },
    "registro-marcadores-contraargumentacion-formal": {
        "name": "formal adversative and counter-argumentative discourse markers",
        "kind": "grammar",
        "category": "grammar"
    },
    "registro-formulas-protocolarias-correspondencia": {
        "name": "epistolary protocol formulas in institutional communication",
        "kind": "grammar",
        "category": "grammar"
    },
    "registro-densidad-lexica-sintesis": {
        "name": "lexical density and complex subordinate clause synthesis",
        "kind": "grammar",
        "category": "grammar"
    },
    # Regional 35 grammar skills
    "pluralismo-concesivas-oposicion-reivindicativa": {
        "name": "restrictive concessive clauses with a despecho de and aun cuando",
        "kind": "grammar",
        "category": "grammar"
    },
    "pluralismo-relativas-preposicionales-institucionales": {
        "name": "complex prepositional relative clauses in legal frameworks",
        "kind": "grammar",
        "category": "grammar"
    },
    "pluralismo-formulas-reconocimiento-constitucional": {
        "name": "declarative constitutional recognition formulas with subjunctives",
        "kind": "grammar",
        "category": "grammar"
    },
    "pluralismo-causales-explicativas-jurisprudencia": {
        "name": "explanatory causal connectors in judicial rulings",
        "kind": "grammar",
        "category": "grammar"
    },
    "pluralismo-perifrasis-obligacion-estatutaria": {
        "name": "statutory obligation periphrases with haber de and deber de",
        "kind": "grammar",
        "category": "grammar"
    },
    # Vocabulary unit themes
    "b2-35-01-vocab": {
        "name": "essayistic nominalization vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-35-02-vocab": {
        "name": "journalistic objectivity and attribution vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-35-03-vocab": {
        "name": "formal counter-argumentative debate vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-35-04-vocab": {
        "name": "institutional epistolary protocol vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-35-05-vocab": {
        "name": "academic lexical synthesis vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "pluralismo-01-vocab": {
        "name": "indigenous self-determination and customary law vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "pluralismo-02-vocab": {
        "name": "communal justice and legal pluralism vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "pluralismo-03-vocab": {
        "name": "rights of nature and ecological jurisprudence vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "pluralismo-04-vocab": {
        "name": "intercultural bilingual education and language revitalization vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "pluralismo-05-vocab": {
        "name": "indigenous environmental defenders and land stewardship vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    }
}

NEW_GRAMMAR_TITLES = {
    "registro-nominalizacion-estilo-ensayistico": "nominalization strategies in academic and essayistic prose",
    "registro-impersonalidad-distanciamiento-discursivo": "discursive distancing and impersonal attribution in journalism",
    "registro-marcadores-contraargumentacion-formal": "formal adversative and counter-argumentative discourse markers",
    "registro-formulas-protocolarias-correspondencia": "epistolary protocol formulas in institutional communication",
    "registro-densidad-lexica-sintesis": "lexical density and complex subordinate clause synthesis",
    "pluralismo-concesivas-oposicion-reivindicativa": "restrictive concessive clauses with a despecho de and aun cuando",
    "pluralismo-relativas-preposicionales-institucionales": "complex prepositional relative clauses in legal frameworks",
    "pluralismo-formulas-reconocimiento-constitucional": "declarative constitutional recognition formulas with subjunctives",
    "pluralismo-causales-explicativas-jurisprudencia": "explanatory causal connectors in judicial rulings",
    "pluralismo-perifrasis-obligacion-estatutaria": "statutory obligation periphrases with haber de and deber de"
}

VOCAB_DATA = {
    "b2-35-01": {
        "title": "Nominalización y prosa ensayística",
        "words": [
            {"lemma": "nominalización", "translation": "nominalization", "pos": "noun"},
            {"lemma": "desarticulación", "translation": "dismantling / disruption", "pos": "noun"},
            {"lemma": "legitimación", "translation": "legitimization", "pos": "noun"},
            {"lemma": "abstracción", "translation": "abstraction", "pos": "noun"},
            {"lemma": "subordinación", "translation": "subordination", "pos": "noun"},
            {"lemma": "propiciar", "translation": "to foster / bring about", "pos": "verb"},
            {"lemma": "paulatino", "translation": "gradual / step-by-step", "pos": "adjective"},
            {"lemma": "densidad", "translation": "density / depth", "pos": "noun"},
            {"lemma": "rigor", "translation": "rigor / precision", "pos": "noun"},
            {"lemma": "conceptual", "translation": "conceptual", "pos": "adjective"}
        ]
    },
    "b2-35-02": {
        "title": "Distanciamiento e impersonalidad periodística",
        "words": [
            {"lemma": "cabe colegir", "translation": "it can be gathered / deduced", "pos": "expression"},
            {"lemma": "deontológico", "translation": "ethical / professional ethics-related", "pos": "adjective"},
            {"lemma": "fehaciente", "translation": "irrefutable / conclusive", "pos": "adjective"},
            {"lemma": "distanciamiento", "translation": "distancing / objectivity", "pos": "noun"},
            {"lemma": "puntualizar", "translation": "to point out / specify", "pos": "verb"},
            {"lemma": "desmentir", "translation": "to deny / refute", "pos": "verb"},
            {"lemma": "imparcialidad", "translation": "impartiality", "pos": "noun"},
            {"lemma": "constatar", "translation": "to verify / confirm", "pos": "verb"},
            {"lemma": "presunción", "translation": "presumption / assumption", "pos": "noun"},
            {"lemma": "fuente fidedigna", "translation": "reliable source", "pos": "expression"}
        ]
    },
    "b2-35-03": {
        "title": "Marcadores contraargumentativos y debate",
        "words": [
            {"lemma": "antes bien", "translation": "rather / on the contrary", "pos": "expression"},
            {"lemma": "en contrapartida", "translation": "in contrast / on the other hand", "pos": "expression"},
            {"lemma": "refutación", "translation": "rebuttal / refutation", "pos": "noun"},
            {"lemma": "antítesis", "translation": "antithesis", "pos": "noun"},
            {"lemma": "ahora bien", "translation": "now then / however", "pos": "expression"},
            {"lemma": "discrepancia", "translation": "discrepancy / disagreement", "pos": "noun"},
            {"lemma": "contraargumento", "translation": "counter-argument", "pos": "noun"},
            {"lemma": "desestimar", "translation": "to dismiss / reject", "pos": "verb"},
            {"lemma": "sostener", "translation": "to maintain / hold a position", "pos": "verb"},
            {"lemma": "dialéctica", "translation": "dialectics / argumentative reasoning", "pos": "noun"}
        ]
    },
    "b2-35-04": {
        "title": "Tratamiento protocolar e institucional",
        "words": [
            {"lemma": "cúmpleme", "translation": "it is my duty to", "pos": "expression"},
            {"lemma": "antecedente", "translation": "background / prior record", "pos": "noun"},
            {"lemma": "despacho", "translation": "official office / dispatch", "pos": "noun"},
            {"lemma": "certificar", "translation": "to certify / attest officially", "pos": "verb"},
            {"lemma": "protocolar", "translation": "protocol-related / formal", "pos": "adjective"},
            {"lemma": "distinguido", "translation": "distinguished", "pos": "adjective"},
            {"lemma": "diligenciar", "translation": "to process / execute an official errand", "pos": "verb"},
            {"lemma": "rubricar", "translation": "to sign / endorse", "pos": "verb"},
            {"lemma": "decreto", "translation": "decree / executive order", "pos": "noun"},
            {"lemma": "solemnidad", "translation": "solemnity / formality", "pos": "noun"}
        ]
    },
    "b2-35-05": {
        "title": "Síntesis y densidad argumentativa",
        "words": [
            {"lemma": "participio absoluto", "translation": "absolute participle construction", "pos": "expression"},
            {"lemma": "concisión", "translation": "conciseness / brevity", "pos": "noun"},
            {"lemma": "diáfano", "translation": "crystal clear / lucid", "pos": "adjective"},
            {"lemma": "vínculo jurídico", "translation": "legal bond / nexus", "pos": "expression"},
            {"lemma": "sintetizar", "translation": "to synthesize / summarize", "pos": "verb"},
            {"lemma": "período sintáctico", "translation": "complex syntactic sentence", "pos": "expression"},
            {"lemma": "apositivo", "translation": "appositive", "pos": "adjective"},
            {"lemma": "elocuente", "translation": "eloquent", "pos": "adjective"},
            {"lemma": "coherencia", "translation": "coherence / logical flow", "pos": "noun"},
            {"lemma": "articulación", "translation": "articulation / structuring", "pos": "noun"}
        ]
    },
    "b2-pluralismo-01": {
        "title": "Autodeterminación y soberanía comunitaria",
        "words": [
            {"lemma": "a despecho de", "translation": "in spite of / in defiance of", "pos": "expression"},
            {"lemma": "autodeterminación", "translation": "self-determination", "pos": "noun"},
            {"lemma": "aculturación", "translation": "acculturation / forced assimilation", "pos": "noun"},
            {"lemma": "inalienable", "translation": "inalienable / non-transferable", "pos": "adjective"},
            {"lemma": "resguardo", "translation": "indigenous collective reserve", "pos": "noun"},
            {"lemma": "asimilacionismo", "translation": "assimilationism", "pos": "noun"},
            {"lemma": "consulta previa", "translation": "prior informed consultation", "pos": "expression"},
            {"lemma": "plurinacional", "translation": "plurinational", "pos": "adjective"},
            {"lemma": "emancipación", "translation": "emancipation", "pos": "noun"},
            {"lemma": "titularidad", "translation": "legal ownership / entitlement", "pos": "noun"}
        ]
    },
    "b2-pluralismo-02": {
        "title": "Pluralismo jurídico y justicia consuetudinaria",
        "words": [
            {"lemma": "al amparo de", "translation": "under the protection of", "pos": "expression"},
            {"lemma": "con arreglo a", "translation": "in accordance with / pursuant to", "pos": "expression"},
            {"lemma": "deslinde", "translation": "demarcation / jurisdictional boundary", "pos": "noun"},
            {"lemma": "consuetudinario", "translation": "customary / based on tradition", "pos": "adjective"},
            {"lemma": "ronda campesina", "translation": "peasant self-defense and justice patrol", "pos": "expression"},
            {"lemma": "reparador", "translation": "restorative / reparative", "pos": "adjective"},
            {"lemma": "cosa juzgada", "translation": "res judicata / final binding judgment", "pos": "expression"},
            {"lemma": "interjurisdiccional", "translation": "interjurisdictional", "pos": "adjective"},
            {"lemma": "abigeato", "translation": "cattle rustling / livestock theft", "pos": "noun"},
            {"lemma": "armonización", "translation": "harmonization / coordination", "pos": "noun"}
        ]
    },
    "b2-pluralismo-03": {
        "title": "Ecoderecho y derechos de la naturaleza",
        "words": [
            {"lemma": "biocéntrico", "translation": "biocentric / life-centered", "pos": "adjective"},
            {"lemma": "sujeto de derechos", "translation": "subject of legal rights", "pos": "expression"},
            {"lemma": "cuenca hidrográfica", "translation": "hydrographic river basin", "pos": "expression"},
            {"lemma": "remediación", "translation": "environmental remediation / cleanup", "pos": "noun"},
            {"lemma": "antropoceno", "translation": "anthropocene", "pos": "noun"},
            {"lemma": "tutelado", "translation": "protected / under guardianship", "pos": "adjective"},
            {"lemma": "vertimiento", "translation": "dumping / industrial discharge", "pos": "noun"},
            {"lemma": "restauración", "translation": "restoration / ecological recovery", "pos": "noun"},
            {"lemma": "pacto intergeneracional", "translation": "intergenerational pact", "pos": "expression"},
            {"lemma": "tutela judicial", "translation": "judicial protection / writ of protection", "pos": "expression"}
        ]
    },
    "b2-pluralismo-04": {
        "title": "Educación bilingüe y revitalización digital",
        "words": [
            {"lemma": "habida cuenta de que", "translation": "taking into account that", "pos": "expression"},
            {"lemma": "toda vez que", "translation": "inasmuch as / since", "pos": "expression"},
            {"lemma": "bilingüismo aditivo", "translation": "additive bilingualism", "pos": "expression"},
            {"lemma": "revitalización", "translation": "linguistic revitalization", "pos": "noun"},
            {"lemma": "intercultural", "translation": "intercultural", "pos": "adjective"},
            {"lemma": "descolonización", "translation": "decolonization", "pos": "noun"},
            {"lemma": "vernáculo", "translation": "vernacular / native language", "pos": "adjective"},
            {"lemma": "normalización", "translation": "linguistic standardization", "pos": "noun"},
            {"lemma": "cooficialidad", "translation": "co-official language status", "pos": "noun"},
            {"lemma": "gamificación", "translation": "gamification", "pos": "noun"}
        ]
    },
    "b2-pluralismo-05": {
        "title": "Ecofeminismo y defensoras territoriales",
        "words": [
            {"lemma": "haber de", "translation": "to have to / bound to by statute", "pos": "verb"},
            {"lemma": "ecofeminismo", "translation": "ecofeminism / community environmental feminism", "pos": "noun"},
            {"lemma": "lideresa", "translation": "female leader / grassroots woman leader", "pos": "noun"},
            {"lemma": "cautelar", "translation": "preventive / protective measure", "pos": "adjective"},
            {"lemma": "semilla nativa", "translation": "native heirloom seed", "pos": "expression"},
            {"lemma": "soberanía alimentaria", "translation": "food sovereignty", "pos": "expression"},
            {"lemma": "hostigamiento", "translation": "harassment", "pos": "noun"},
            {"lemma": "estigmatización", "translation": "stigmatization", "pos": "noun"},
            {"lemma": "vínculo sagrado", "translation": "sacred bond", "pos": "expression"},
            {"lemma": "indivisible", "translation": "indivisible", "pos": "adjective"}
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
    print("Updated skill-registry.json for Unit 35")

def update_grammar_titles():
    path = LATAM_DIR / "indexes" / "grammar-titles.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_GRAMMAR_TITLES.items():
        data[k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated grammar-titles.json for Unit 35")

def write_vocabulary():
    vocab_dir = LATAM_DIR / "vocabulary" / "b2"
    vocab_dir.mkdir(parents=True, exist_ok=True)
    for stem, vdata in VOCAB_DATA.items():
        if stem.startswith("b2-35"):
            vocab_id = f"vocab.b2.35.{stem.split('-')[-1]}"
        else:
            vocab_id = f"vocab.b2.pluralismo.{stem.split('-')[-1]}"
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
        "b2-35-01-a": ("grammar.b2.35.01.registro-nominalizacion-estilo-ensayistico", "registro-nominalizacion-estilo-ensayistico"),
        "b2-35-02-a": ("grammar.b2.35.02.registro-impersonalidad-distanciamiento-discursivo", "registro-impersonalidad-distanciamiento-discursivo"),
        "b2-35-03-a": ("grammar.b2.35.03.registro-marcadores-contraargumentacion-formal", "registro-marcadores-contraargumentacion-formal"),
        "b2-35-04-a": ("grammar.b2.35.04.registro-formulas-protocolarias-correspondencia", "registro-formulas-protocolarias-correspondencia"),
        "b2-35-05-a": ("grammar.b2.35.05.registro-densidad-lexica-sintesis", "registro-densidad-lexica-sintesis"),
        "b2-pluralismo-01-a": ("grammar.b2.pluralismo.01.pluralismo-concesivas-oposicion-reivindicativa", "pluralismo-concesivas-oposicion-reivindicativa"),
        "b2-pluralismo-02-a": ("grammar.b2.pluralismo.02.pluralismo-relativas-preposicionales-institucionales", "pluralismo-relativas-preposicionales-institucionales"),
        "b2-pluralismo-03-a": ("grammar.b2.pluralismo.03.pluralismo-formulas-reconocimiento-constitucional", "pluralismo-formulas-reconocimiento-constitucional"),
        "b2-pluralismo-04-a": ("grammar.b2.pluralismo.04.pluralismo-causales-explicativas-jurisprudencia", "pluralismo-causales-explicativas-jurisprudencia"),
        "b2-pluralismo-05-a": ("grammar.b2.pluralismo.05.pluralismo-perifrasis-obligacion-estatutaria", "pluralismo-perifrasis-obligacion-estatutaria")
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
        if stem.startswith("b2-35"):
            if "consolidation" in stem:
                lesson_id = "lesson.b2.35.consolidation"
            else:
                lesson_id = f"lesson.b2.35.{stem.split('-')[-1]}"
        else:
            if "consolidation" in stem:
                lesson_id = "lesson.b2.pluralismo.consolidation"
            else:
                lesson_id = f"lesson.b2.pluralismo.{stem.split('-')[-1]}"
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
    print("Updated curriculum/units/b2.json with Unit 35!")

def main():
    update_skill_registry()
    update_grammar_titles()
    write_vocabulary()
    write_grammar()
    write_stories()
    write_exercises()
    write_lessons()
    update_curriculum()
    print("Unit 35 generation complete!")

if __name__ == "__main__":
    main()
