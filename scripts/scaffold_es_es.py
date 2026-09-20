#!/usr/bin/env python3
"""
Scaffolds content/es-es by:
1. Copying shared foundational schemas, tests, drills, conversation scenarios.
2. Copying A1 and A2 curriculum, lessons, exercises, vocabulary, grammar, and stories.
3. Copying B1 Core units (b1-01 through b1-36).
4. Constructing content/es-es/curriculum/units/b1.json with:
   - 36 Core Spanish units
   - 36 Cultura y Ciudadanía units (based on CCSE 5 tasks)
5. Generating initial lesson, exercise, vocab, and grammar files for the first CCSE units.
"""
import os
import re
import json
import shutil
from pathlib import Path

ROOT = Path(".")
SRC = ROOT / "content" / "es-latam"
DST = ROOT / "content" / "es-es"

def copy_file(src_path, dst_path):
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_path, dst_path)

def copy_tree_files(src_dir, dst_dir, pattern="*"):
    if not src_dir.exists():
        return
    for path in src_dir.rglob(pattern):
        if path.is_file():
            rel = path.relative_to(src_dir)
            target = dst_dir / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)

def main():
    print(f"Scaffolding {DST} from {SRC}...")

    # 1. Base files and directories
    for folder in ["schemas", "tests", "drills", "imports"]:
        s = SRC / folder
        d = DST / folder
        if s.exists():
            print(f"  Copying {folder}...")
            copy_tree_files(s, d)

    if (SRC / "conversation-scenarios.json").exists():
        copy_file(SRC / "conversation-scenarios.json", DST / "conversation-scenarios.json")

    # 2. Units tables for A1 & A2
    print("  Setting up curriculum unit tables...")
    copy_file(SRC / "curriculum" / "units" / "a1.json", DST / "curriculum" / "units" / "a1.json")
    copy_file(SRC / "curriculum" / "units" / "a2.json", DST / "curriculum" / "units" / "a2.json")

    # 3. A1 and A2 content
    for lvl in ["a1", "a2"]:
        print(f"  Copying {lvl.upper()} lessons, exercises, vocabulary, grammar, and stories...")
        for kind in ["lessons", "exercises", "vocabulary", "grammar"]:
            copy_tree_files(SRC / kind / lvl, DST / kind / lvl)
        
        # Stories
        if (SRC / "stories" / "original" / lvl).exists():
            copy_tree_files(SRC / "stories" / "original" / lvl, DST / "stories" / "original" / lvl)
        if (SRC / "stories" / "classics" / lvl).exists():
            copy_tree_files(SRC / "stories" / "classics" / lvl, DST / "stories" / "classics" / lvl)

    # 4. B1 Core content (numeric stem files only: b1-01 to b1-36)
    print("  Copying B1 Core content (numeric units b1-01 to b1-36)...")
    numeric_unit_re = re.compile(r"^b1-\d{2}-")

    for kind in ["lessons", "exercises", "vocabulary", "grammar"]:
        s_b1 = SRC / kind / "b1"
        d_b1 = DST / kind / "b1"
        d_b1.mkdir(parents=True, exist_ok=True)
        if s_b1.exists():
            for f in s_b1.glob("*.json"):
                if numeric_unit_re.match(f.stem):
                    copy_file(f, d_b1 / f.name)

    # Copy B1 Classics stories (e.g. Don Quijote)
    if (SRC / "stories" / "classics" / "b1").exists():
        copy_tree_files(SRC / "stories" / "classics" / "b1", DST / "stories" / "classics" / "b1")

    # 5. Build content/es-es/curriculum/units/b1.json
    print("  Constructing B1 curriculum units table (Core + Cultura y Ciudadanía)...")
    with open(SRC / "curriculum" / "units" / "b1.json", "r", encoding="utf-8") as f:
        src_b1_units = json.load(f)

    # Extract all Core units from es-latam B1
    core_units = [u for u in src_b1_units if u.get("track") == "core"]

    # Define the 36 CCSE Cultura y Ciudadanía units
    # (Aligned with Instituto Cervantes CCSE 5 Tasks)
    ccse_topics = [
        # Task 1: Gobierno, poderes e instituciones del Estado (Units 1-12)
        ("b1-ccse-constitucion", "La Constitución Española de 1978"),
        ("b1-ccse-monarquia", "La Corona y la Jefatura del Estado"),
        ("b1-ccse-cortes", "Las Cortes Generales: Congreso y Senado"),
        ("b1-ccse-gobierno", "El Gobierno y la Administración del Estado"),
        ("b1-ccse-judicial", "El Poder Judicial y el Tribunal Constitucional"),
        ("b1-ccse-autonomias-inst", "Las Instituciones Autonómicas y Locales"),
        ("b1-ccse-participacion", "Elecciones y Participación Ciudadana"),
        ("b1-ccse-fuerzas-seguridad", "Fuerzas Armadas y Cuerpos de Seguridad"),
        ("b1-ccse-union-europea", "España en la Unión Europea"),
        ("b1-ccse-simbolos", "Símbolos del Estado: Bandera, Escudo e Himno"),
        ("b1-ccse-lenguas", "El Castellano y las Lenguas Cooficiales"),
        ("b1-ccse-instituto-cervantes", "Difusión Cultural: El Instituto Cervantes"),

        # Task 2: Derechos y deberes fundamentales (Units 13-16)
        ("b1-ccse-derechos-fundamentales", "Derechos y Libertades Fundamentales"),
        ("b1-ccse-igualdad-genero", "Igualdad de Género y No Discriminación"),
        ("b1-ccse-deberes-ciudadanos", "Deberes Ciudadanos y Sistema Tributario"),
        ("b1-ccse-defensor-pueblo", "Garantías Constitucionales y Defensor del Pueblo"),

        # Task 3: Organización territorial y geografía física y política (Units 17-21)
        ("b1-ccse-geografia-fisica", "Geografía Física: Relieve, Costas y Ríos"),
        ("b1-ccse-comunidades-norte", "Comunidades del Norte y la Cornisa Cantábrica"),
        ("b1-ccse-comunidades-mediterraneo", "Comunidades del Mediterráneo e Islas Baleares"),
        ("b1-ccse-comunidades-centro-sur", "Comunidades del Centro, Sur y Canarias"),
        ("b1-ccse-ciudades-autonomas", "Ceuta, Melilla y Municipios de España"),

        # Task 4: Tradiciones, arte, historia y cultura (Units 22-28)
        ("b1-ccse-historia-antigua", "Historia: De Hispania al Siglo de Oro"),
        ("b1-ccse-historia-contemporanea", "Historia Contemporánea y Transición a la Democracia"),
        ("b1-ccse-literatura-letras", "Literatura Española: De Cervantes a la Generación del 27"),
        ("b1-ccse-arte-pintura", "Pintura y Escultura: Velázquez, Goya, Picasso y Dalí"),
        ("b1-ccse-musica-cine", "Música, Danza y Cine Español"),
        ("b1-ccse-fiestas-tradiciones", "Fiestas Nacionales, Autonómicas y Tradiciones"),
        ("b1-ccse-gastronomia", "Gastronomía Española y Dieta Mediterránea"),

        # Task 5: Vida cotidiana y sociedad (Units 29-36)
        ("b1-ccse-sanidad", "El Sistema Nacional de Salud y la Tarjeta Sanitaria"),
        ("b1-ccse-educacion", "El Sistema Educativo Español"),
        ("b1-ccse-empleo-seguridad-social", "Mercado Laboral y Seguridad Social"),
        ("b1-ccse-vivienda-padron", "Vivienda, Registro y Empadronamiento"),
        ("b1-ccse-tramites-dni", "Documentación: DNI, NIE y Registro Civil"),
        ("b1-ccse-servicios-emergencias", "Transporte, Comunicaciones y Emergencias 112"),
        ("b1-ccse-consumo-banca", "Consumo, Horarios y Servicios Bancarios"),
        ("b1-ccse-simulacro-examen", "Simulacro General de Examen CCSE")
    ]

    cultura_units = []
    for slug, title in ccse_topics:
        stems = [f"{slug}-01", f"{slug}-02", f"{slug}-03", f"{slug}-04", f"{slug}-05", f"{slug}-consolidation"]
        cultura_units.append({
            "title": title,
            "stems": stems,
            "track": "cultura"
        })

    # Interleave Core and Cultura units in curriculum table for smooth progression
    interleaved_b1 = []
    for i in range(max(len(core_units), len(cultura_units))):
        if i < len(core_units):
            interleaved_b1.append(core_units[i])
        if i < len(cultura_units):
            interleaved_b1.append(cultura_units[i])

    b1_table_path = DST / "curriculum" / "units" / "b1.json"
    b1_table_path.parent.mkdir(parents=True, exist_ok=True)
    with open(b1_table_path, "w", encoding="utf-8") as f:
        json.dump(interleaved_b1, f, indent=2, ensure_ascii=False)

    print(f"  Created B1 units table with {len(core_units)} Core + {len(cultura_units)} Cultura units.")

    # 6. Scaffold initial lessons for CCSE Unit 1: La Constitución Española de 1978
    print("  Authoring scaffold lessons for CCSE Unit 1 (La Constitución Española)...")
    unit1_slug = "b1-ccse-constitucion"
    lessons_dir = DST / "lessons" / "b1"
    exercises_dir = DST / "exercises" / "b1"
    vocab_dir = DST / "vocabulary" / "b1"
    grammar_dir = DST / "grammar" / "b1"

    unit1_lessons = [
        {
            "num": "01",
            "title": "La Constitución de 1978",
            "goal": "Comprender los principios fundamentales del Estado social y democrático de Derecho.",
            "grammar": "Estructuras impersonales con 'se'",
            "ccse_q": "España se constituye en un Estado social y democrático de Derecho.",
            "vocab": [
                {"lemma": "constitución", "translation": "constitution", "pos": "noun", "gender": "f"},
                {"lemma": "soberanía", "translation": "sovereignty", "pos": "noun", "gender": "f"},
                {"lemma": "derecho", "translation": "law / right", "pos": "noun", "gender": "m"},
                {"lemma": "democrático", "translation": "democratic", "pos": "adjective", "gender": "m"},
                {"lemma": "monarquía", "translation": "monarchy", "pos": "noun", "gender": "f"}
            ]
        },
        {
            "num": "02",
            "title": "La Monarquía Parlamentaria",
            "goal": "Aprender la forma política del Estado español y el papel del Rey.",
            "grammar": "Voz pasiva y oraciones subordinadas",
            "ccse_q": "La forma política del Estado español es la monarquía parlamentaria.",
            "vocab": [
                {"lemma": "monarca", "translation": "monarch", "pos": "noun", "gender": "m"},
                {"lemma": "parlamento", "translation": "parliament", "pos": "noun", "gender": "m"},
                {"lemma": "jefe", "translation": "head / chief", "pos": "noun", "gender": "m"},
                {"lemma": "sancionar", "translation": "to sanction / give royal assent", "pos": "verb"},
                {"lemma": "reinar", "translation": "to reign", "pos": "verb"}
            ]
        },
        {
            "num": "03",
            "title": "La Soberanía Nacional",
            "goal": "Conocer de dónde emanan los poderes del Estado y cómo participan los ciudadanos.",
            "grammar": "Uso del subjuntivo en expresiones de voluntad y mandato",
            "ccse_q": "La soberanía nacional reside en el pueblo español.",
            "vocab": [
                {"lemma": "pueblo", "translation": "people / town", "pos": "noun", "gender": "m"},
                {"lemma": "poder", "translation": "power", "pos": "noun", "gender": "m"},
                {"lemma": "ciudadano", "translation": "citizen", "pos": "noun", "gender": "m"},
                {"lemma": "voto", "translation": "vote", "pos": "noun", "gender": "m"},
                {"lemma": "emanar", "translation": "to emanate / derive", "pos": "verb"}
            ]
        },
        {
            "num": "04",
            "title": "La Capital del Estado",
            "goal": "Identificar los símbolos, la capital y la lengua oficial del Estado.",
            "grammar": "Concordancia de adjetivos gentilicios y geográficos",
            "ccse_q": "La capital del Estado es la villa de Madrid.",
            "vocab": [
                {"lemma": "capital", "translation": "capital city", "pos": "noun", "gender": "f"},
                {"lemma": "oficial", "translation": "official", "pos": "adjective"},
                {"lemma": "castellano", "translation": "Castilian Spanish", "pos": "noun", "gender": "m"},
                {"lemma": "bandera", "translation": "flag", "pos": "noun", "gender": "f"},
                {"lemma": "escudo", "translation": "coat of arms", "pos": "noun", "gender": "m"}
            ]
        },
        {
            "num": "05",
            "title": "Valores Superiores",
            "goal": "Explicar los valores de libertad, justicia, igualdad y pluralismo político.",
            "grammar": "Conectores argumentativos y de causa",
            "ccse_q": "Los valores superiores del ordenamiento jurídico son la libertad, la justicia, la igualdad y el pluralismo político.",
            "vocab": [
                {"lemma": "justicia", "translation": "justice", "pos": "noun", "gender": "f"},
                {"lemma": "libertad", "translation": "freedom", "pos": "noun", "gender": "f"},
                {"lemma": "igualdad", "translation": "equality", "pos": "noun", "gender": "f"},
                {"lemma": "pluralismo", "translation": "pluralism", "pos": "noun", "gender": "m"},
                {"lemma": "ordenamiento", "translation": "legal system / framework", "pos": "noun", "gender": "m"}
            ]
        }
    ]

    for item in unit1_lessons:
        stem = f"{unit1_slug}-{item['num']}"
        lesson_id = f"lesson.{stem.replace('-', '.')}"
        voc_id = f"voc.{stem.replace('-', '.')}"
        gr_id = f"gr.{stem.replace('-', '.')}"
        ex_id = f"ex.{stem.replace('-', '.')}"

        # Vocab file
        voc_data = {
            "id": voc_id,
            "lesson": stem,
            "title": item["title"],
            "words": item["vocab"]
        }
        with open(vocab_dir / f"{stem}-voc.json", "w", encoding="utf-8") as f:
            json.dump(voc_data, f, indent=2, ensure_ascii=False)

        # Grammar file
        gr_data = {
            "id": gr_id,
            "title": item["grammar"],
            "sections": [
                {
                    "type": "text",
                    "content": f"En este tema analizamos: {item['grammar']}. Aplicado al contexto de la Constitución Española y el examen CCSE."
                },
                {
                    "type": "examples",
                    "items": [
                        {
                            "spanish": item["ccse_q"],
                            "english": f"Official CCSE premise: {item['title']}"
                        }
                    ]
                }
            ]
        }
        with open(grammar_dir / f"{stem}-gr.json", "w", encoding="utf-8") as f:
            json.dump(gr_data, f, indent=2, ensure_ascii=False)

        # Exercise file
        words = item["ccse_q"].rstrip(".").split()
        ex_data = {
            "id": ex_id,
            "exercises": [
                {
                    "id": f"{ex_id}.1",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": f"¿Qué afirma la Constitución Española sobre: {item['title']}?",
                    "options": [item["ccse_q"], "Es una república federal.", "No está regulado en la Constitución."],
                    "answer": item["ccse_q"],
                    "explanation": f"Pregunta oficial del banco CCSE: {item['ccse_q']}",
                    "teaches": ["constitucion", "ccse"]
                },
                {
                    "id": f"{ex_id}.2",
                    "type": "fill-in-blank",
                    "category": "grammar",
                    "sentence": f"La soberanía nacional ___ en el pueblo español.",
                    "answer": "reside",
                    "options": ["reside", "residen", "residía"],
                    "explanation": "La soberanía (singular) reside en el pueblo.",
                    "teaches": ["constitucion", "verbos-presente"]
                },
                {
                    "id": f"{ex_id}.3",
                    "type": "sentence-builder",
                    "category": "syntax",
                    "english": f"Official CCSE premise: {item['title']}",
                    "solution": words + ["."],
                    "pool": words + [".", "rey", "gobierno"],
                    "teaches": ["constitucion", "ccse"]
                }
            ]
        }
        with open(exercises_dir / f"{stem}-ex.json", "w", encoding="utf-8") as f:
            json.dump(ex_data, f, indent=2, ensure_ascii=False)

        # Lesson file
        lesson_data = {
            "id": lesson_id,
            "level": "b1",
            "title": item["title"],
            "grammar": item["grammar"],
            "goal": item["goal"],
            "track": "cultura",
            "metadata": {"estimatedMinutes": 12},
            "sections": [
                {
                    "type": "vocabulary",
                    "title": "Vocabulario Cívico",
                    "content": {"ref": f"vocabulary/b1/{stem}-voc.json"}
                },
                {
                    "type": "grammar",
                    "title": item["grammar"],
                    "content": {"ref": f"grammar/b1/{stem}-gr.json"}
                },
                {
                    "type": "exercise-group",
                    "title": "Práctica y Preguntas CCSE",
                    "exerciseRefs": [f"{ex_id}.1", f"{ex_id}.2"],
                    "content": {"ref": f"exercises/b1/{stem}-ex.json"}
                }
            ]
        }
        with open(lessons_dir / f"{stem}.json", "w", encoding="utf-8") as f:
            json.dump(lesson_data, f, indent=2, ensure_ascii=False)

    # Consolidation lesson for Unit 1
    stem_cons = f"{unit1_slug}-consolidation"
    cons_lesson_id = f"lesson.{stem_cons.replace('-', '.')}"
    cons_data = {
        "id": cons_lesson_id,
        "level": "b1",
        "title": "Repaso y Simulacro: La Constitución de 1978",
        "grammar": "Consolidación de estructuras constitucionales",
        "goal": "Revisar y afianzar las preguntas del examen CCSE sobre la Constitución.",
        "track": "cultura",
        "metadata": {"estimatedMinutes": 15},
        "sections": [
            {
                "type": "exercise-group",
                "title": "Simulacro de Repaso",
                "exerciseRefs": [f"ex.{unit1_slug}.01.1", f"ex.{unit1_slug}.02.1"],
                "content": {"ref": f"exercises/b1/{unit1_slug}-01-ex.json"}
            }
        ]
    }
    with open(lessons_dir / f"{stem_cons}.json", "w", encoding="utf-8") as f:
        json.dump(cons_data, f, indent=2, ensure_ascii=False)

    # Also author placeholder lessons for remaining CCSE units so curriculum generator completes all 36 units
    print("  Authoring scaffold placeholders for remaining CCSE units 2-36...")
    for slug, title in ccse_topics[1:]:
        for num in ["01", "02", "03", "04", "05", "consolidation"]:
            stem = f"{slug}-{num}"
            l_id = f"lesson.{stem.replace('-', '.')}"
            is_cons = num == "consolidation"
            l_title = f"Repaso: {title}" if is_cons else f"{title} — Parte {num}"
            
            # Simple valid lesson structure
            l_obj = {
                "id": l_id,
                "level": "b1",
                "title": l_title,
                "grammar": "Conocimientos constitucionales y socioculturales de España",
                "goal": f"Estudio y preparación CCSE: {title}",
                "track": "cultura",
                "metadata": {"estimatedMinutes": 10},
                "sections": []
            }
            with open(lessons_dir / f"{stem}.json", "w", encoding="utf-8") as f:
                json.dump(l_obj, f, indent=2, ensure_ascii=False)

    print("[OK] Done scaffolding content/es-es successfully!")

if __name__ == "__main__":
    main()
