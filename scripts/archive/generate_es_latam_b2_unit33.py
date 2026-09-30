#!/usr/bin/env python3
"""
generate_es_latam_b2_unit33.py

Generates Latin American Spanish B2 Unit 33 for both tracks:
- Track 1 (Core B2): Unit 33 - Subordinación adverbial II: Condicionales complejas y contrafácticas
  Classic: Julio Cortázar - Rayuela (1963)
- Track 2 (Regional Studies): Unit 33 - Integración regional, corredores bioceánicos y energía compartida
  Overview + 5 lessons + consolidation story

Strict schema conformance:
- Vocabulary: root {id: 'vocab.b2.33.01', lesson: 'b2-33-01', title, words: [{lemma, translation, pos}]}
- Exercises: root {lesson: 'b2-33-01', exercises: [{id: 'b2-33-01.ex01', type, category, teaches, ...}]}
- Grammar: root {id: 'grammar.b2.33.01.<skill>', title, sections: [{type: 'text'|'table'|'tip', content, rows}]}
- Lessons: root {id: 'lesson.b2.33.01', title, level: 'B2', sections: [...]}
- Stories: root {id, title, level: 'B2', lesson, type, estimatedMinutes, summary, characters, paragraphs: [{type: 'narration', text}], narration: {pedagogical: {comprehensionQuestions: [...]}}}
- Story word count strictly in [650, 825] words.
"""

import json
import re
from pathlib import Path

from make_unit33_stories import STORIES
from unit33_grammar_data import GRAMMAR_DATA
from unit33_exercises_data import EXERCISES_DATA
from unit33_lessons_data import LESSONS_DATA, CURRICULUM_ENTRIES

REPO_ROOT = Path(__file__).resolve().parent.parent
LATAM_DIR = REPO_ROOT / "content" / "es-latam"

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

NEW_SKILLS = {
    # Core 33 grammar skills
    "condicionales-a-condicion-con-tal": {
        "name": "conditional clauses with a condición de que and con tal de que",
        "kind": "grammar",
        "category": "grammar"
    },
    "condicionales-salvedad-exclusion": {
        "name": "conditional exception clauses with a menos que and salvo que",
        "kind": "grammar",
        "category": "grammar"
    },
    "condicionales-gerundio-de-infinitivo": {
        "name": "implicit conditional structures with gerund and de plus infinitive",
        "kind": "grammar",
        "category": "grammar"
    },
    "condicionales-como-no-advertencia": {
        "name": "conditional warning clauses with como no and subjunctive",
        "kind": "grammar",
        "category": "grammar"
    },
    "desiderativas-contrafacticas-ponderativas": {
        "name": "counterfactual optative clauses with ojalá and quién pudiera",
        "kind": "grammar",
        "category": "grammar"
    },
    # Regional 33 grammar skills
    "integracion-formulas-restrictivas-alcance": {
        "name": "restrictive conditional clauses with en la medida en que",
        "kind": "grammar",
        "category": "grammar"
    },
    "integracion-condicionales-inversion-enfasis": {
        "name": "emphatic inverted conditional structures with así and subjunctive",
        "kind": "grammar",
        "category": "grammar"
    },
    "integracion-consecutivas-intensivas": {
        "name": "intensive consecutive clauses with de tal suerte que",
        "kind": "grammar",
        "category": "grammar"
    },
    "integracion-modales-correspondencia": {
        "name": "proportional manner clauses with a medida que and conforme",
        "kind": "grammar",
        "category": "grammar"
    },
    "integracion-desiderativas-institucionales": {
        "name": "institutional optative formulas with es menester que and subjunctive",
        "kind": "grammar",
        "category": "grammar"
    },
    # Vocabulary unit themes
    "b2-33-01-vocab": {
        "name": "strict conditional commitments vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-33-02-vocab": {
        "name": "exceptions and reservations vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-33-03-vocab": {
        "name": "hypothetical deductions and causality vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-33-04-vocab": {
        "name": "warnings admonitions and risks vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-33-05-vocab": {
        "name": "wishes yearnings and regrets vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "integracion-01-vocab": {
        "name": "mercosur customs union and tariffs vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "integracion-02-vocab": {
        "name": "pacific alliance and value chains vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "integracion-03-vocab": {
        "name": "bioceanic corridors and ports vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "integracion-04-vocab": {
        "name": "binational hydroelectric dams and energy vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "integracion-05-vocab": {
        "name": "south american citizenship and mobility vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    }
}

NEW_GRAMMAR_TITLES = {
    "condicionales-a-condicion-con-tal": "strict conditional clauses with a condición de que",
    "condicionales-salvedad-exclusion": "conditional exception clauses with a menos que and salvo que",
    "condicionales-gerundio-de-infinitivo": "implicit conditional structures with gerund and de plus infinitive",
    "condicionales-como-no-advertencia": "conditional warning clauses with como no and subjunctive",
    "desiderativas-contrafacticas-ponderativas": "counterfactual optative clauses with ojalá and quién pudiera",
    "integracion-formulas-restrictivas-alcance": "restrictive conditional clauses with en la medida en que",
    "integracion-condicionales-inversion-enfasis": "emphatic inverted conditional structures with así and subjunctive",
    "integracion-consecutivas-intensivas": "intensive consecutive clauses with de tal suerte que",
    "integracion-modales-correspondencia": "proportional manner clauses with a medida que and conforme",
    "integracion-desiderativas-institucionales": "institutional optative formulas with es menester que and subjunctive"
}

VOCAB_DATA = {
    "b2-33-01": {
        "title": "Compromisos condicionales y garantías",
        "words": [
            {"lemma": "a condición de que", "translation": "on condition that", "pos": "expression"},
            {"lemma": "con tal de que", "translation": "provided that / as long as", "pos": "expression"},
            {"lemma": "estipulación", "translation": "stipulation / condition", "pos": "noun"},
            {"lemma": "cláusula", "translation": "clause / provision", "pos": "noun"},
            {"lemma": "suscribir", "translation": "to subscribe / sign", "pos": "verb"},
            {"lemma": "vinculante", "translation": "binding / mandatory", "pos": "adjective"},
            {"lemma": "exigibilidad", "translation": "enforceability", "pos": "noun"},
            {"lemma": "supeditado", "translation": "subject to / dependent on", "pos": "adjective"},
            {"lemma": "salvaguardia", "translation": "safeguard", "pos": "noun"},
            {"lemma": "incondicional", "translation": "unconditional", "pos": "adjective"}
        ]
    },
    "b2-33-02": {
        "title": "Salvedades y exclusiones condicionales",
        "words": [
            {"lemma": "a menos que", "translation": "unless", "pos": "expression"},
            {"lemma": "a no ser que", "translation": "unless / barring that", "pos": "expression"},
            {"lemma": "salvo que", "translation": "except that / unless", "pos": "expression"},
            {"lemma": "exceptuando", "translation": "excepting / with the exception of", "pos": "preposition"},
            {"lemma": "salvedad", "translation": "qualification / reservation", "pos": "noun"},
            {"lemma": "eximente", "translation": "exempting circumstance / exemption", "pos": "noun"},
            {"lemma": "prescindir", "translation": "to dispense with / forgo", "pos": "verb"},
            {"lemma": "contingencia", "translation": "contingency", "pos": "noun"},
            {"lemma": "irrevocable", "translation": "irrevocable", "pos": "adjective"},
            {"lemma": "restringir", "translation": "to restrict / limit", "pos": "verb"}
        ]
    },
    "b2-33-03": {
        "title": "Deducciones hipotéticas y causalidad implícita",
        "words": [
            {"lemma": "de haber mediado", "translation": "had there been mediation", "pos": "expression"},
            {"lemma": "actuando así", "translation": "by acting thus / acting in this way", "pos": "expression"},
            {"lemma": "deducción", "translation": "deduction / inference", "pos": "noun"},
            {"lemma": "inferencia", "translation": "inference", "pos": "noun"},
            {"lemma": "premisas", "translation": "premises", "pos": "noun"},
            {"lemma": "corolario", "translation": "corollary", "pos": "noun"},
            {"lemma": "conjeturar", "translation": "to conjecture / surmise", "pos": "verb"},
            {"lemma": "plausible", "translation": "plausible", "pos": "adjective"},
            {"lemma": "ineludible", "translation": "inescapable / unavoidable", "pos": "adjective"},
            {"lemma": "fundamento", "translation": "foundation / basis", "pos": "noun"}
        ]
    },
    "b2-33-04": {
        "title": "Advertencias, admoniciones y riesgos",
        "words": [
            {"lemma": "como no intervengas", "translation": "unless you intervene", "pos": "expression"},
            {"lemma": "admonición", "translation": "admonition / formal warning", "pos": "noun"},
            {"lemma": "apercibimiento", "translation": "warning / summons", "pos": "noun"},
            {"lemma": "inminente", "translation": "imminent", "pos": "adjective"},
            {"lemma": "desacato", "translation": "contempt / insubordination", "pos": "noun"},
            {"lemma": "transgredir", "translation": "to transgress / violate", "pos": "verb"},
            {"lemma": "sancionatorio", "translation": "punitive / sanctioning", "pos": "adjective"},
            {"lemma": "represalia", "translation": "reprisal / retaliation", "pos": "noun"},
            {"lemma": "prevenir", "translation": "to warn / anticipate", "pos": "verb"},
            {"lemma": "cautela", "translation": "caution / prudence", "pos": "noun"}
        ]
    },
    "b2-33-05": {
        "title": "Deseos, anhelos y lamentaciones contrafácticas",
        "words": [
            {"lemma": "quién pudiera", "translation": "would that one could / if only one could", "pos": "expression"},
            {"lemma": "ojalá hubiera", "translation": "if only there had been / would that there had been", "pos": "expression"},
            {"lemma": "anhelo", "translation": "yearning / longing", "pos": "noun"},
            {"lemma": "añoranza", "translation": "nostalgia / yearning", "pos": "noun"},
            {"lemma": "desazón", "translation": "uneasiness / sorrow", "pos": "noun"},
            {"lemma": "frustración", "translation": "frustration", "pos": "noun"},
            {"lemma": "quimera", "translation": "chimera / impossible dream", "pos": "noun"},
            {"lemma": "inaplazable", "translation": "urgent / not deferrable", "pos": "adjective"},
            {"lemma": "evocar", "translation": "to evoke / recall", "pos": "verb"},
            {"lemma": "redención", "translation": "redemption", "pos": "noun"}
        ]
    },
    "b2-integracion-01": {
        "title": "Mercosur y unión aduanera",
        "words": [
            {"lemma": "arancel común", "translation": "common external tariff", "pos": "expression"},
            {"lemma": "asimetría", "translation": "asymmetry / disparity", "pos": "noun"},
            {"lemma": "convergencia", "translation": "convergence", "pos": "noun"},
            {"lemma": "desgravación", "translation": "tariff reduction / tax relief", "pos": "noun"},
            {"lemma": "contingente", "translation": "quota / contingent", "pos": "noun"},
            {"lemma": "bloque", "translation": "regional bloc", "pos": "noun"},
            {"lemma": "unilateral", "translation": "unilateral", "pos": "adjective"},
            {"lemma": "arbitraje", "translation": "arbitration", "pos": "noun"},
            {"lemma": "salvaguarda", "translation": "safeguard", "pos": "noun"},
            {"lemma": "armonizar", "translation": "to harmonize", "pos": "verb"}
        ]
    },
    "b2-integracion-02": {
        "title": "Alianza del Pacífico y cadenas de valor",
        "words": [
            {"lemma": "cadena de valor", "translation": "value chain", "pos": "expression"},
            {"lemma": "apertura", "translation": "openness / trade liberalization", "pos": "noun"},
            {"lemma": "homologación", "translation": "standardization / homologation", "pos": "noun"},
            {"lemma": "pragmático", "translation": "pragmatic", "pos": "adjective"},
            {"lemma": "bursátil", "translation": "stock exchange / securities-related", "pos": "adjective"},
            {"lemma": "encadenamiento", "translation": "linkage / networking", "pos": "noun"},
            {"lemma": "competitividad", "translation": "competitiveness", "pos": "noun"},
            {"lemma": "arancelario", "translation": "tariff-related", "pos": "adjective"},
            {"lemma": "cuenca del Pacífico", "translation": "Pacific Basin", "pos": "expression"},
            {"lemma": "desregulador", "translation": "deregulating", "pos": "adjective"}
        ]
    },
    "b2-integracion-03": {
        "title": "Corredores bioceánicos y puertos",
        "words": [
            {"lemma": "paso cordillerano", "translation": "mountain pass", "pos": "expression"},
            {"lemma": "bioceánico", "translation": "bioceanic / linking two oceans", "pos": "adjective"},
            {"lemma": "ferrovía", "translation": "railway / railroad track", "pos": "noun"},
            {"lemma": "cabotaje", "translation": "coastal trade / cabotage", "pos": "noun"},
            {"lemma": "calado", "translation": "draft / vessel water depth", "pos": "noun"},
            {"lemma": "multimodal", "translation": "multimodal (transport)", "pos": "adjective"},
            {"lemma": "megapuerto", "translation": "mega-port", "pos": "noun"},
            {"lemma": "dragado", "translation": "dredging", "pos": "noun"},
            {"lemma": "hinterland", "translation": "hinterland / tributary trade zone", "pos": "noun"},
            {"lemma": "interconexión", "translation": "interconnection", "pos": "noun"}
        ]
    },
    "b2-integracion-04": {
        "title": "Energía compartida y represas binacionales",
        "words": [
            {"lemma": "represa binacional", "translation": "binational dam", "pos": "expression"},
            {"lemma": "hidroelectricidad", "translation": "hydroelectricity", "pos": "noun"},
            {"lemma": "caudal", "translation": "water discharge / flow volume", "pos": "noun"},
            {"lemma": "turbina", "translation": "turbine", "pos": "noun"},
            {"lemma": "excedente", "translation": "surplus", "pos": "noun"},
            {"lemma": "gasoducto", "translation": "gas pipeline", "pos": "noun"},
            {"lemma": "interconectado", "translation": "interconnected", "pos": "adjective"},
            {"lemma": "regalía", "translation": "royalty", "pos": "noun"},
            {"lemma": "matriz energética", "translation": "energy matrix", "pos": "expression"},
            {"lemma": "renegociación", "translation": "renegotiation", "pos": "noun"}
        ]
    },
    "b2-integracion-05": {
        "title": "Ciudadanía suramericana y movilidad",
        "words": [
            {"lemma": "libre tránsito", "translation": "free transit / unhindered movement", "pos": "expression"},
            {"lemma": "convalidación", "translation": "recognition / validation of degrees", "pos": "noun"},
            {"lemma": "residencia", "translation": "residency", "pos": "noun"},
            {"lemma": "acuerdo migratorio", "translation": "migration accord", "pos": "expression"},
            {"lemma": "homologar", "translation": "to equate / validate", "pos": "verb"},
            {"lemma": "soberanía compartida", "translation": "shared sovereignty", "pos": "expression"},
            {"lemma": "radicación", "translation": "settlement / legal residency process", "pos": "noun"},
            {"lemma": "previsional", "translation": "pension / social security-related", "pos": "adjective"},
            {"lemma": "fraternidad", "translation": "fraternity / brotherhood", "pos": "noun"},
            {"lemma": "supranacional", "translation": "supranational", "pos": "adjective"}
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
    print("Updated skill-registry.json for Unit 33")

def update_grammar_titles():
    path = LATAM_DIR / "indexes" / "grammar-titles.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_GRAMMAR_TITLES.items():
        data[k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated grammar-titles.json for Unit 33")

def write_vocabulary():
    vocab_dir = LATAM_DIR / "vocabulary" / "b2"
    vocab_dir.mkdir(parents=True, exist_ok=True)
    for stem, vdata in VOCAB_DATA.items():
        if stem.startswith("b2-33"):
            vocab_id = f"vocab.b2.33.{stem.split('-')[-1]}"
        else:
            vocab_id = f"vocab.b2.integracion.{stem.split('-')[-1]}"
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
        "b2-33-01-a": ("grammar.b2.33.01.condicionales-a-condicion-con-tal", "condicionales-a-condicion-con-tal"),
        "b2-33-02-a": ("grammar.b2.33.02.condicionales-salvedad-exclusion", "condicionales-salvedad-exclusion"),
        "b2-33-03-a": ("grammar.b2.33.03.condicionales-gerundio-de-infinitivo", "condicionales-gerundio-de-infinitivo"),
        "b2-33-04-a": ("grammar.b2.33.04.condicionales-como-no-advertencia", "condicionales-como-no-advertencia"),
        "b2-33-05-a": ("grammar.b2.33.05.desiderativas-contrafacticas-ponderativas", "desiderativas-contrafacticas-ponderativas"),
        "b2-integracion-01-a": ("grammar.b2.integracion.01.integracion-formulas-restrictivas-alcance", "integracion-formulas-restrictivas-alcance"),
        "b2-integracion-02-a": ("grammar.b2.integracion.02.integracion-condicionales-inversion-enfasis", "integracion-condicionales-inversion-enfasis"),
        "b2-integracion-03-a": ("grammar.b2.integracion.03.integracion-consecutivas-intensivas", "integracion-consecutivas-intensivas"),
        "b2-integracion-04-a": ("grammar.b2.integracion.04.integracion-modales-correspondencia", "integracion-modales-correspondencia"),
        "b2-integracion-05-a": ("grammar.b2.integracion.05.integracion-desiderativas-institucionales", "integracion-desiderativas-institucionales")
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
        if stem.startswith("b2-33"):
            if "consolidation" in stem:
                lesson_id = "lesson.b2.33.consolidation"
            else:
                lesson_id = f"lesson.b2.33.{stem.split('-')[-1]}"
        else:
            if "consolidation" in stem:
                lesson_id = "lesson.b2.integracion.consolidation"
            else:
                lesson_id = f"lesson.b2.integracion.{stem.split('-')[-1]}"
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
    print("Updated curriculum/units/b2.json with Unit 33!")

def main():
    update_skill_registry()
    update_grammar_titles()
    write_vocabulary()
    write_grammar()
    write_stories()
    write_exercises()
    write_lessons()
    update_curriculum()
    print("Unit 33 generation complete!")

if __name__ == "__main__":
    main()
