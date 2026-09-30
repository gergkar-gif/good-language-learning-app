#!/usr/bin/env python3
"""
generate_es_latam_b2_unit34.py

Generates Latin American Spanish B2 Unit 34 for both tracks:
- Track 1 (Core B2): Unit 34 - Sociolingüística y variación dialectal II: Léxico, registros y pragmática
  Classic: Manuel Scorza - Redoble por Rancas (1970)
- Track 2 (Regional Studies): Unit 34 - Migraciones suramericanas y diáspora: Desplazamientos, refugio y comunidades transnacionales
  Overview + 5 lessons + consolidation story

Strict schema conformance:
- Vocabulary: root {id: 'vocab.b2.34.01', lesson: 'b2-34-01', title, words: [{lemma, translation, pos}]}
- Exercises: root {lesson: 'b2-34-01', exercises: [{id: 'b2-34-01.ex01', type, category, teaches, ...}]}
- Grammar: root {id: 'grammar.b2.34.01.<skill>', title, sections: [{type: 'text'|'table'|'tip', content, rows}]}
- Lessons: root {id: 'lesson.b2.34.01', title, level: 'B2', sections: [...]}
- Stories: root {id, title, level: 'B2', lesson, type, estimatedMinutes, summary, characters, paragraphs: [{type: 'narration', text}], narration: {pedagogical: {comprehensionQuestions: [...]}}}
- Story word count strictly in [650, 825] words.
"""

import json
import re
from pathlib import Path

from make_unit34_stories import STORIES
from unit34_grammar_data import GRAMMAR_DATA
from unit34_exercises_data import EXERCISES_DATA
from unit34_lessons_data import LESSONS_DATA, CURRICULUM_ENTRIES

REPO_ROOT = Path(__file__).resolve().parent.parent
LATAM_DIR = REPO_ROOT / "content" / "es-latam"

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

NEW_SKILLS = {
    # Core 34 grammar skills
    "sociolinguistica-tratamiento-cortesia": {
        "name": "forms of address and honorific deference in formal discourse",
        "kind": "grammar",
        "category": "grammar"
    },
    "sociolinguistica-variacion-lexica-diatonica": {
        "name": "diatopic lexical variation and regional semantic shifts",
        "kind": "grammar",
        "category": "grammar"
    },
    "pragmatica-atenuacion-modalidad-epistemica": {
        "name": "epistemic modality and pragmatic attenuation devices",
        "kind": "grammar",
        "category": "grammar"
    },
    "pragmatica-actos-habla-directivos-formales": {
        "name": "indirect speech acts and formal directive strategies",
        "kind": "grammar",
        "category": "grammar"
    },
    "sociolinguistica-adecuacion-cambio-registro": {
        "name": "register shifts and communicative code switching in dialogue",
        "kind": "grammar",
        "category": "grammar"
    },
    # Regional 34 grammar skills
    "migracion-clausulas-temporales-limite": {
        "name": "temporal boundary clauses with hasta tanto and en tanto",
        "kind": "grammar",
        "category": "grammar"
    },
    "migracion-obligacion-institucional-subjuntivo": {
        "name": "impersonal obligation structures with es preceptivo que and subjunctive",
        "kind": "grammar",
        "category": "grammar"
    },
    "migracion-relativas-indefinidas-distributivas": {
        "name": "indefinite relative clauses with cuantos and dondequiera que",
        "kind": "grammar",
        "category": "grammar"
    },
    "migracion-concesivas-factuales-complejas": {
        "name": "complex factual concession with bien que and si bien",
        "kind": "grammar",
        "category": "grammar"
    },
    "migracion-pasivas-reflejas-generalizacion": {
        "name": "passive reflexive structures in institutional and legal contexts",
        "kind": "grammar",
        "category": "grammar"
    },
    # Vocabulary unit themes
    "b2-34-01-vocab": {
        "name": "honorific address and courtesy formulas vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-34-02-vocab": {
        "name": "pan-hispanic diatopic variation vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-34-03-vocab": {
        "name": "epistemic attenuation and hedging vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-34-04-vocab": {
        "name": "formal directive speech acts vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-34-05-vocab": {
        "name": "sociolinguistic register adaptation vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "migracion-01-vocab": {
        "name": "historical south american migratory cycles vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "migracion-02-vocab": {
        "name": "humanitarian corridors and refuge vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "migracion-03-vocab": {
        "name": "border crossings and consular regularization vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "migracion-04-vocab": {
        "name": "remittances and diaspora economy vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "migracion-05-vocab": {
        "name": "transnational identity and cultural integration vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    }
}

NEW_GRAMMAR_TITLES = {
    "sociolinguistica-tratamiento-cortesia": "forms of address and honorific deference in formal discourse",
    "sociolinguistica-variacion-lexica-diatonica": "diatopic lexical variation and regional semantic shifts",
    "pragmatica-atenuacion-modalidad-epistemica": "epistemic modality and pragmatic attenuation devices",
    "pragmatica-actos-habla-directivos-formales": "indirect speech acts and formal directive strategies",
    "sociolinguistica-adecuacion-cambio-registro": "register shifts and communicative code switching in dialogue",
    "migracion-clausulas-temporales-limite": "temporal boundary clauses with hasta tanto and en tanto",
    "migracion-obligacion-institucional-subjuntivo": "impersonal obligation structures with es preceptivo que and subjunctive",
    "migracion-relativas-indefinidas-distributivas": "indefinite relative clauses with cuantos and dondequiera que",
    "migracion-concesivas-factuales-complejas": "complex factual concession with bien que and si bien",
    "migracion-pasivas-reflejas-generalizacion": "passive reflexive structures in institutional and legal contexts"
}

VOCAB_DATA = {
    "b2-34-01": {
        "title": "Sistemas de tratamiento y deferencia",
        "words": [
            {"lemma": "voseo", "translation": "use of vos as second-person pronoun", "pos": "noun"},
            {"lemma": "tuteo", "translation": "use of tú as second-person pronoun", "pos": "noun"},
            {"lemma": "ustedeo", "translation": "use of usted for familiarity or respect", "pos": "noun"},
            {"lemma": "deferencia", "translation": "deference / respectful regard", "pos": "noun"},
            {"lemma": "reverencial", "translation": "reverential / highly respectful", "pos": "adjective"},
            {"lemma": "interlocutor", "translation": "interlocutor / speaking partner", "pos": "noun"},
            {"lemma": "protocolar", "translation": "protocol-related / formal", "pos": "adjective"},
            {"lemma": "jerarquía", "translation": "hierarchy / ranking", "pos": "noun"},
            {"lemma": "tutear", "translation": "to address as tú", "pos": "verb"},
            {"lemma": "vosear", "translation": "to address as vos", "pos": "verb"}
        ]
    },
    "b2-34-02": {
        "title": "Variación léxica diatópica",
        "words": [
            {"lemma": "geosinónimo", "translation": "regional synonym", "pos": "noun"},
            {"lemma": "diatópico", "translation": "geographically variable", "pos": "adjective"},
            {"lemma": "cédula", "translation": "identity card / credential", "pos": "noun"},
            {"lemma": "arraigo", "translation": "social roots / established residence", "pos": "noun"},
            {"lemma": "colectividad", "translation": "community / collective group", "pos": "noun"},
            {"lemma": "divergencia", "translation": "divergence / difference", "pos": "noun"},
            {"lemma": "convalidar", "translation": "to recognize officially / validate", "pos": "verb"},
            {"lemma": "homologación", "translation": "official validation / homologation", "pos": "noun"},
            {"lemma": "vernáculo", "translation": "vernacular / native", "pos": "adjective"},
            {"lemma": "habla regional", "translation": "regional speech / dialect", "pos": "expression"}
        ]
    },
    "b2-34-03": {
        "title": "Atenuación discursiva y modestia epistémica",
        "words": [
            {"lemma": "atenuación", "translation": "mitigation / pragmatic softening", "pos": "noun"},
            {"lemma": "epistémico", "translation": "epistemic / knowledge-related", "pos": "adjective"},
            {"lemma": "asertividad", "translation": "assertiveness / force of claim", "pos": "noun"},
            {"lemma": "cautela", "translation": "caution / circumspection", "pos": "noun"},
            {"lemma": "cabría advertir", "translation": "it might be noted / warned", "pos": "expression"},
            {"lemma": "dar la impresión", "translation": "to give the impression", "pos": "expression"},
            {"lemma": "disenso", "translation": "dissent / polite disagreement", "pos": "noun"},
            {"lemma": "matiz", "translation": "nuance / shade of meaning", "pos": "noun"},
            {"lemma": "mitigar", "translation": "to mitigate / soften", "pos": "verb"},
            {"lemma": "ponderar", "translation": "to weigh / consider carefully", "pos": "verb"}
        ]
    },
    "b2-34-04": {
        "title": "Actos de habla directivos formales",
        "words": [
            {"lemma": "tener a bien", "translation": "to kindly agree to / see fit to", "pos": "expression"},
            {"lemma": "visar", "translation": "to endorse / officially stamp", "pos": "verb"},
            {"lemma": "remitir", "translation": "to remit / forward", "pos": "verb"},
            {"lemma": "peticionario", "translation": "petitioner / applicant", "pos": "noun"},
            {"lemma": "requerimiento", "translation": "formal request / injunction", "pos": "noun"},
            {"lemma": "exhortar", "translation": "to exhort / urge formally", "pos": "verb"},
            {"lemma": "memorial", "translation": "formal petition / memorandum", "pos": "noun"},
            {"lemma": "diligencia", "translation": "administrative proceeding / errand", "pos": "noun"},
            {"lemma": "solicitar", "translation": "to request / apply for", "pos": "verb"},
            {"lemma": "vinculación", "translation": "connection / institutional tie", "pos": "noun"}
        ]
    },
    "b2-34-05": {
        "title": "Adecuación pragmática y registros",
        "words": [
            {"lemma": "homologar", "translation": "to validate / accredit officially", "pos": "verb"},
            {"lemma": "diastrático", "translation": "socially or register-based variable", "pos": "adjective"},
            {"lemma": "coloquialismo", "translation": "colloquial expression", "pos": "noun"},
            {"lemma": "solemne", "translation": "solemn / formal", "pos": "adjective"},
            {"lemma": "cambio de código", "translation": "code switching", "pos": "expression"},
            {"lemma": "registro formal", "translation": "formal register", "pos": "expression"},
            {"lemma": "pertinencia", "translation": "relevance / appropriateness", "pos": "noun"},
            {"lemma": "elocuencia", "translation": "eloquence", "pos": "noun"},
            {"lemma": "adecuación", "translation": "situational adaptation", "pos": "noun"},
            {"lemma": "competencia discursiva", "translation": "discursive competence", "pos": "expression"}
        ]
    },
    "b2-migracion-01": {
        "title": "Ciclos migratorios históricos",
        "words": [
            {"lemma": "éxodo", "translation": "exodus / mass departure", "pos": "noun"},
            {"lemma": "diáspora", "translation": "diaspora / dispersion", "pos": "noun"},
            {"lemma": "hasta tanto", "translation": "until such time as", "pos": "expression"},
            {"lemma": "en tanto que", "translation": "inasmuch as / while", "pos": "expression"},
            {"lemma": "desplazamiento", "translation": "displacement / movement", "pos": "noun"},
            {"lemma": "asentamiento", "translation": "settlement / colony", "pos": "noun"},
            {"lemma": "transfronterizo", "translation": "cross-border", "pos": "adjective"},
            {"lemma": "contingente", "translation": "contingent / group", "pos": "noun"},
            {"lemma": "poblamiento", "translation": "settlement / populating process", "pos": "noun"},
            {"lemma": "arraigar", "translation": "to take root / establish residency", "pos": "verb"}
        ]
    },
    "b2-migracion-02": {
        "title": "Corredores humanitarios y refugio",
        "words": [
            {"lemma": "preceptivo", "translation": "mandatory / prescribed by law", "pos": "adjective"},
            {"lemma": "salvoconducto", "translation": "safe-conduct pass", "pos": "noun"},
            {"lemma": "repatriación", "translation": "repatriation", "pos": "noun"},
            {"lemma": "contingencia", "translation": "emergency / contingency", "pos": "noun"},
            {"lemma": "asilo", "translation": "asylum / refuge", "pos": "noun"},
            {"lemma": "apátrida", "translation": "stateless person", "pos": "noun"},
            {"lemma": "albergue", "translation": "shelter / refuge center", "pos": "noun"},
            {"lemma": "corredor humanitario", "translation": "humanitarian corridor", "pos": "expression"},
            {"lemma": "perentorio", "translation": "urgent / pressing", "pos": "adjective"},
            {"lemma": "vulnerabilidad", "translation": "vulnerability", "pos": "noun"}
        ]
    },
    "b2-migracion-03": {
        "title": "Pasos fronterizos y regularización",
        "words": [
            {"lemma": "regularización", "translation": "regularization of migratory status", "pos": "noun"},
            {"lemma": "radicación", "translation": "legal settlement / residency", "pos": "noun"},
            {"lemma": "cualesquiera", "translation": "whichever / whatever (plural)", "pos": "pronoun"},
            {"lemma": "dondequiera", "translation": "wherever", "pos": "adverb"},
            {"lemma": "aduana", "translation": "customs / border checkpoint", "pos": "noun"},
            {"lemma": "control biométrico", "translation": "biometric control", "pos": "expression"},
            {"lemma": "indocumentado", "translation": "undocumented person", "pos": "adjective"},
            {"lemma": "salvaguarda", "translation": "safeguard / protection", "pos": "noun"},
            {"lemma": "empadronamiento", "translation": "census registration / enrollment", "pos": "noun"},
            {"lemma": "tramitar", "translation": "to process / file paperwork", "pos": "verb"}
        ]
    },
    "b2-migracion-04": {
        "title": "Remesas y economía de la diáspora",
        "words": [
            {"lemma": "remesa", "translation": "remittance / funds transfer", "pos": "noun"},
            {"lemma": "bancarización", "translation": "financial inclusion / banking access", "pos": "noun"},
            {"lemma": "fuga de talentos", "translation": "brain drain / skilled emigration", "pos": "expression"},
            {"lemma": "si bien", "translation": "while / although (factual)", "pos": "conjunction"},
            {"lemma": "bien que", "translation": "although / even though", "pos": "conjunction"},
            {"lemma": "transferencia", "translation": "bank transfer", "pos": "noun"},
            {"lemma": "divisa", "translation": "foreign currency", "pos": "noun"},
            {"lemma": "subsistencia", "translation": "subsistence / livelihood", "pos": "noun"},
            {"lemma": "costo transaccional", "translation": "transaction fee / cost", "pos": "expression"},
            {"lemma": "dinamizar", "translation": "to stimulate / energize", "pos": "verb"}
        ]
    },
    "b2-migracion-05": {
        "title": "Identidad transnacional y cohesión",
        "words": [
            {"lemma": "interculturalidad", "translation": "interculturality / mutual exchange", "pos": "noun"},
            {"lemma": "cohesión social", "translation": "social cohesion", "pos": "expression"},
            {"lemma": "transnacional", "translation": "transnational", "pos": "adjective"},
            {"lemma": "pasiva refleja", "translation": "passive reflexive construction", "pos": "expression"},
            {"lemma": "mutualismo", "translation": "mutual aid movement", "pos": "noun"},
            {"lemma": "hermandad", "translation": "brotherhood / fraternity", "pos": "noun"},
            {"lemma": "convalidación", "translation": "degree recognition", "pos": "noun"},
            {"lemma": "pluricultural", "translation": "pluricultural / multicultural", "pos": "adjective"},
            {"lemma": "asociacionismo", "translation": "associational life / civic organization", "pos": "noun"},
            {"lemma": "integración", "translation": "integration / inclusion", "pos": "noun"}
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
    print("Updated skill-registry.json for Unit 34")

def update_grammar_titles():
    path = LATAM_DIR / "indexes" / "grammar-titles.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_GRAMMAR_TITLES.items():
        data[k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated grammar-titles.json for Unit 34")

def write_vocabulary():
    vocab_dir = LATAM_DIR / "vocabulary" / "b2"
    vocab_dir.mkdir(parents=True, exist_ok=True)
    for stem, vdata in VOCAB_DATA.items():
        if stem.startswith("b2-34"):
            vocab_id = f"vocab.b2.34.{stem.split('-')[-1]}"
        else:
            vocab_id = f"vocab.b2.migracion.{stem.split('-')[-1]}"
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
        "b2-34-01-a": ("grammar.b2.34.01.sociolinguistica-tratamiento-cortesia", "sociolinguistica-tratamiento-cortesia"),
        "b2-34-02-a": ("grammar.b2.34.02.sociolinguistica-variacion-lexica-diatonica", "sociolinguistica-variacion-lexica-diatonica"),
        "b2-34-03-a": ("grammar.b2.34.03.pragmatica-atenuacion-modalidad-epistemica", "pragmatica-atenuacion-modalidad-epistemica"),
        "b2-34-04-a": ("grammar.b2.34.04.pragmatica-actos-habla-directivos-formales", "pragmatica-actos-habla-directivos-formales"),
        "b2-34-05-a": ("grammar.b2.34.05.sociolinguistica-adecuacion-cambio-registro", "sociolinguistica-adecuacion-cambio-registro"),
        "b2-migracion-01-a": ("grammar.b2.migracion.01.migracion-clausulas-temporales-limite", "migracion-clausulas-temporales-limite"),
        "b2-migracion-02-a": ("grammar.b2.migracion.02.migracion-obligacion-institucional-subjuntivo", "migracion-obligacion-institucional-subjuntivo"),
        "b2-migracion-03-a": ("grammar.b2.migracion.03.migracion-relativas-indefinidas-distributivas", "migracion-relativas-indefinidas-distributivas"),
        "b2-migracion-04-a": ("grammar.b2.migracion.04.migracion-concesivas-factuales-complejas", "migracion-concesivas-factuales-complejas"),
        "b2-migracion-05-a": ("grammar.b2.migracion.05.migracion-pasivas-reflejas-generalizacion", "migracion-pasivas-reflejas-generalizacion")
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
        if stem.startswith("b2-34"):
            if "consolidation" in stem:
                lesson_id = "lesson.b2.34.consolidation"
            else:
                lesson_id = f"lesson.b2.34.{stem.split('-')[-1]}"
        else:
            if "consolidation" in stem:
                lesson_id = "lesson.b2.migracion.consolidation"
            else:
                lesson_id = f"lesson.b2.migracion.{stem.split('-')[-1]}"
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
    print("Updated curriculum/units/b2.json with Unit 34!")

def main():
    update_skill_registry()
    update_grammar_titles()
    write_vocabulary()
    write_grammar()
    write_stories()
    write_exercises()
    write_lessons()
    update_curriculum()
    print("Unit 34 generation complete!")

if __name__ == "__main__":
    main()
