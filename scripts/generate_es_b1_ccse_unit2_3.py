#!/usr/bin/env python3
"""Generate Spain CCSE Units 2 & 3 (content/es-es, B1, track: cultura).

Unit 2: La Corona y la Jefatura del Estado (b1-monarquia)
Unit 3: Las Cortes Generales: Congreso y Senado (b1-cortes)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def write_json(rel_path: str, data: dict):
    full_path = ROOT / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {rel_path}")


def make_narration(paragraphs, target_grammar, key_vocab, comp_questions):
    segments = []
    t = 0.0
    for i, p in enumerate(paragraphs):
        words = len(p["text"].split())
        dur = round(max(4.5, words * 0.42), 1)
        segments.append({
            "paraIndex": i,
            "startTime": round(t, 1),
            "endTime": round(t + dur, 1),
            "speaker": "Narrator",
            "lang": "es",
            "cues": [],
            "pronunciations": []
        })
        t += dur
    return {
        "durationSeconds": round(t, 1),
        "pacing": {
            "speedMultiplier": 1.0,
            "rate_str": "+0%",
            "rate_wpm": 145,
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
            "keyVocabulary": key_vocab,
            "targetGrammar": target_grammar,
            "comprehensionQuestions": comp_questions
        }
    }


def _convert_ex_item(ex_id: str, raw: dict, g_slug: str) -> dict:
    t = raw["type"]
    cat = raw.get("cat", "grammar")
    if t == "multiple-choice":
        opts = list(raw["options"])
        ans = raw.get("answer", opts[0])
        correct_idx = opts.index(ans) if ans in opts else 0
        out = {
            "id": ex_id,
            "type": "multiple-choice",
            "category": cat,
            "question": raw["prompt"],
            "options": opts,
            "correct": correct_idx
        }
        if cat != "reading" and g_slug:
            out["teaches"] = [g_slug]
        return out
    elif t == "fill-blank":
        out = {
            "id": ex_id,
            "type": "fill-blank",
            "category": cat,
            "sentence": raw["prompt"],
            "answer": raw["answer"],
            "english": raw["english"]
        }
        if g_slug:
            out["teaches"] = [g_slug]
        return out
    elif t == "sentence-builder":
        words = list(raw["words"])
        out = {
            "id": ex_id,
            "type": "sentence-builder",
            "category": cat,
            "tiles": words,
            "solution": words,
            "english": raw["english"]
        }
        if g_slug:
            out["teaches"] = [g_slug]
        return out
    elif t == "dictation":
        out = {
            "id": ex_id,
            "type": "dictation",
            "category": "listening",
            "sentence": raw["text"],
            "english": raw["english"]
        }
        if g_slug:
            out["teaches"] = [g_slug]
        return out
    raise ValueError(f"Unsupported exercise type: {t}")


SLUG_TO_CCSE_META = {
    "derechos": ("b1-ccse-derechos-fundamentales", "Derechos y Libertades Fundamentales"),
    "igualdad": ("b1-ccse-igualdad-genero", "Igualdad de Género y No Discriminación"),
    "deberes": ("b1-ccse-deberes-ciudadanos", "Deberes Ciudadanos y Sistema Tributario"),
    "garantias": ("b1-ccse-defensor-pueblo", "Garantías Constitucionales y Defensor del Pueblo"),
    "geografia": ("b1-ccse-geografia-fisica", "Geografía Física: Relieve, Costas y Ríos"),
    "norte": ("b1-ccse-comunidades-norte", "Comunidades del Norte y la Cornisa Cantábrica"),
    "mediterraneo": ("b1-ccse-comunidades-mediterraneo", "Comunidades del Mediterráneo e Islas Baleares"),
    "centrosur": ("b1-ccse-comunidades-centro-sur", "Comunidades del Centro, Sur y Canarias"),
    "ciudadesautonomas": ("b1-ccse-ciudades-autonomas", "Ceuta, Melilla y Municipios de España"),
    "historiaantigua": ("b1-ccse-historia-antigua", "Historia: De Hispania al Siglo de Oro"),
    "historiacontemporanea": ("b1-ccse-historia-contemporanea", "Historia Contemporánea y Transición a la Democracia"),
    "literatura": ("b1-ccse-literatura-letras", "Literatura Española: De Cervantes a la Generación del 27"),
    "arte": ("b1-ccse-arte-pintura", "Pintura y Escultura: Velázquez, Goya, Picasso y Dalí"),
    "musicacine": ("b1-ccse-musica-cine", "Música, Danza y Cine Español"),
    "fiestas": ("b1-ccse-fiestas-tradiciones", "Fiestas Nacionales, Autonómicas y Tradiciones"),
    "gastronomia": ("b1-ccse-gastronomia", "Gastronomía Española y Dieta Mediterránea"),
    "sanidad": ("b1-ccse-sanidad", "El Sistema Nacional de Salud y la Tarjeta Sanitaria"),
    "educacion": ("b1-ccse-educacion", "El Sistema Educativo Español"),
    "empleo": ("b1-ccse-empleo-seguridad-social", "Mercado Laboral y Seguridad Social"),
    "vivienda": ("b1-ccse-vivienda-padron", "Vivienda, Registro y Empadronamiento"),
    "documentacion": ("b1-ccse-tramites-dni", "Documentación: DNI, NIE y Registro Civil"),
    "transporte": ("b1-ccse-servicios-emergencias", "Transporte, Comunicaciones y Emergencias 112"),
    "consumobanca": ("b1-ccse-consumo-banca", "Consumo, Horarios y Servicios Bancarios"),
    "simulacro": ("b1-ccse-simulacro-examen", "Simulacro General de Examen CCSE"),
}


def _normalize_compact_unit(u: dict) -> dict:
    if "legacy_prefix" in u and "unit_title" in u:
        return u
    slug = u["slug"]
    legacy_prefix, exact_title = SLUG_TO_CCSE_META.get(slug, (f"b1-ccse-{slug}", u.get("title", slug)))
    u["legacy_prefix"] = legacy_prefix
    u["unit_title"] = exact_title
    u["order"] = u.get("unit_num", 49) - 36
    u["unit_summary"] = u.get("description", exact_title)

    cons_ex = []
    for lcfg in u["lessons"]:
        if "story_paragraphs" not in lcfg:
            lcfg["story_paragraphs"] = lcfg["paragraphs"]
        if "comp_questions" not in lcfg:
            lcfg["comp_questions"] = lcfg["questions"]
        if "goal" not in lcfg:
            lcfg["goal"] = lcfg["objectives"][0]
        if "grammar_summary" not in lcfg:
            lcfg["grammar_summary"] = lcfg["grammar_title"]
        if "story_summary" not in lcfg:
            lcfg["story_summary"] = lcfg["objectives"][0]
        if "story_location" not in lcfg:
            lcfg["story_location"] = "España"

        norm_examples = []
        for ex_item in lcfg["grammar_examples"]:
            if "spanish" in ex_item:
                norm_examples.append(ex_item)
            else:
                norm_examples.append({"spanish": ex_item["es"], "english": ex_item["en"]})
        lcfg["grammar_examples"] = norm_examples

        if "exercises" not in lcfg:
            ex_items = []
            # 1-3: reading MC from questions
            for q in lcfg["questions"]:
                opts = list(q["options"])
                ex_items.append({
                    "type": "multiple-choice",
                    "cat": "reading",
                    "prompt": q["question"],
                    "options": opts,
                    "answer": opts[q.get("correctIndex", 0)]
                })
            # 4-5: civic/grammar MC from ex_mc
            for m in lcfg["ex_mc"]:
                opts = list(m["options"])
                ex_items.append({
                    "type": "multiple-choice",
                    "cat": "grammar",
                    "prompt": m["prompt"],
                    "options": opts,
                    "answer": opts[m.get("correctIndex", 0)]
                })
            # 6-7: vocabulary MC from vocab
            v = lcfg["vocab"]
            for vi in (0, 3):
                target_w = v[vi]
                distractors = [v[(vi + 1) % len(v)]["translation"], v[(vi + 2) % len(v)]["translation"], v[(vi + 4) % len(v)]["translation"]]
                opts = [target_w["translation"]] + distractors
                ex_items.append({
                    "type": "multiple-choice",
                    "cat": "vocabulary",
                    "prompt": f"¿Qué significa en inglés el término «{target_w['lemma']}»?",
                    "options": opts,
                    "answer": target_w["translation"]
                })
            # 8-9: fill-blank from ex_fb
            for fb in lcfg["ex_fb"]:
                ex_items.append({
                    "type": "fill-blank",
                    "cat": "grammar",
                    "prompt": fb["sentence"],
                    "answer": fb["answer"],
                    "english": fb["english"]
                })
            # 10: sentence-builder from ex_sb
            ex_items.append({
                "type": "sentence-builder",
                "cat": "grammar",
                "words": lcfg["ex_sb"]["words"],
                "english": lcfg["ex_sb"]["english"]
            })
            # 11: dictation from ex_dict
            ex_items.append({
                "type": "dictation",
                "cat": "listening",
                "text": lcfg["ex_dict"]["audioText"],
                "english": lcfg["ex_dict"]["english"]
            })
            lcfg["exercises"] = ex_items

        # Add one MC from each lesson to consolidation
        q0 = lcfg["questions"][0]
        cons_ex.append({
            "type": "multiple-choice",
            "cat": "grammar",
            "prompt": q0["question"],
            "options": list(q0["options"]),
            "answer": q0["options"][q0.get("correctIndex", 0)]
        })

    # Add 1 fill-blank, 1 sentence-builder, 1 dictation to consolidation (8 total)
    l0 = u["lessons"][0]
    l1 = u["lessons"][1]
    l2 = u["lessons"][2]
    cons_ex.append({
        "type": "fill-blank",
        "cat": "grammar",
        "prompt": l0["ex_fb"][0]["sentence"],
        "answer": l0["ex_fb"][0]["answer"],
        "english": l0["ex_fb"][0]["english"]
    })
    cons_ex.append({
        "type": "sentence-builder",
        "cat": "grammar",
        "words": l1["ex_sb"]["words"],
        "english": l1["ex_sb"]["english"]
    })
    cons_ex.append({
        "type": "dictation",
        "cat": "listening",
        "text": l2["ex_dict"]["audioText"],
        "english": l2["ex_dict"]["english"]
    })
    u["consolidation_exercises"] = cons_ex
    return u


def emit_unit_from_dict(u: dict):
    u = _normalize_compact_unit(u)
    slug = u["slug"]
    old_prefix = u["legacy_prefix"]
    unit_title = u["unit_title"]
    order_idx = u["order"]

    for folder in ["lessons/b1", "vocabulary/b1", "grammar/b1", "exercises/b1"]:
        dir_path = ROOT / "content/es-es" / folder
        if dir_path.exists():
            for old_file in dir_path.glob(f"{old_prefix}*"):
                old_file.unlink()
                print(f"Removed legacy file {old_file.relative_to(ROOT)}")

    all_unit_paras = []
    all_unit_qs = []
    all_unit_vocab = []

    for lcfg in u["lessons"]:
        num = lcfg["num"]
        stem = f"b1-{slug}-{num}"
        g_slug = lcfg["grammar_slug"]

        # 1. Vocab
        words_formatted = []
        for w in lcfg["vocab"]:
            words_formatted.append({
                "lemma": w["lemma"],
                "pos": w["pos"],
                "translation": w["translation"]
            })
        voc_data = {
            "id": f"vocab.b1.{slug}.{num}",
            "lesson": stem,
            "title": lcfg["title"],
            "theme": unit_title,
            "words": words_formatted
        }
        vocab_rel = f"vocabulary/b1/{stem}-voc.json"
        write_json(f"content/es-es/{vocab_rel}", voc_data)

        # 2. Grammar
        gr_sections = [
            {"type": "text", "content": lcfg["grammar_text"]},
            {"type": "examples", "items": lcfg["grammar_examples"]},
            {"type": "tip", "content": lcfg["grammar_tip"]}
        ]
        gr_data = {
            "id": f"grammar.b1.{slug}.{num}.{g_slug}",
            "title": lcfg["grammar_title"],
            "sections": gr_sections
        }
        gr_rel = f"grammar/b1/{stem}-{g_slug}-gr.json"
        write_json(f"content/es-es/{gr_rel}", gr_data)

        # 3. Story
        paras = [{"type": "narration", "text": t} for t in lcfg["story_paragraphs"]]
        all_unit_paras.extend(paras)
        all_unit_qs.extend(lcfg["comp_questions"])
        kv = [
            {"lemma": words_formatted[0]["lemma"], "pos": words_formatted[0]["pos"], "cefr": "B1", "gloss": words_formatted[0]["translation"]},
            {"lemma": words_formatted[1]["lemma"], "pos": words_formatted[1]["pos"], "cefr": "B1", "gloss": words_formatted[1]["translation"]},
            {"lemma": words_formatted[2]["lemma"], "pos": words_formatted[2]["pos"], "cefr": "B1", "gloss": words_formatted[2]["translation"]}
        ]
        all_unit_vocab.extend(kv)
        story_data = {
            "id": f"story.b1.{slug}.{num}",
            "title": lcfg["story_title"],
            "level": "B1",
            "lesson": int(num),
            "order": int(num),
            "type": "world",
            "estimatedMinutes": 5,
            "summary": lcfg["story_summary"],
            "characters": [],
            "location": lcfg["story_location"],
            "grammar": [g_slug],
            "vocabularyTopics": [unit_title, lcfg["title"]],
            "paragraphs": paras,
            "narration": make_narration(paras, [g_slug], kv, lcfg["comp_questions"])
        }
        story_rel = f"stories/world/b1/{stem}-{lcfg['story_slug']}.json"
        write_json(f"content/es-es/{story_rel}", story_data)

        # 4. Exercises
        ex_list = []
        ex_refs = []
        for idx, raw_ex in enumerate(lcfg["exercises"], start=1):
            ex_id = f"{stem}.ex{idx:02d}"
            ex_refs.append(ex_id)
            ex_list.append(_convert_ex_item(ex_id, raw_ex, g_slug))
        ex_rel = f"exercises/b1/{stem}-ex.json"
        write_json(f"content/es-es/{ex_rel}", {"lesson": stem, "exercises": ex_list})

        # 5. Lesson
        goals_list = [
            lcfg["goal"],
            f"Master 8 key CCSE vocabulary terms related to {lcfg['title']}",
            f"Apply '{lcfg['grammar_title']}' in civic and constitutional contexts"
        ]
        lesson_data = {
            "id": f"lesson.b1.{slug}.{num}",
            "title": lcfg["title"],
            "level": "B1",
            "goal": lcfg["goal"],
            "grammar": lcfg["grammar_summary"],
            "sections": [
                {"type": "goal", "items": goals_list},
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_rel},
                {"type": "vocabulary", "ref": vocab_rel},
                {"type": "grammar", "ref": gr_rel},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": ex_rel,
                    "exerciseRefs": ex_refs
                },
                {"type": "srs"},
                {"type": "checklist", "items": [f"I can {g[0].lower() + g[1:]}" for g in goals_list]}
            ]
        }
        write_json(f"content/es-es/lessons/b1/{stem}.json", lesson_data)

    # Combined story (stitched with all 25 paragraphs and 15 comprehension questions)
    comb_data = {
        "id": f"story.b1.{slug}",
        "title": unit_title,
        "level": "B1",
        "order": order_idx,
        "type": "world",
        "estimatedMinutes": 12,
        "summary": u["unit_summary"],
        "characters": [],
        "location": "España",
        "grammar": [l["grammar_slug"] for l in u["lessons"]],
        "vocabularyTopics": [l["title"] for l in u["lessons"]],
        "paragraphs": all_unit_paras,
        "narration": make_narration(
            all_unit_paras,
            [l["grammar_slug"] for l in u["lessons"][:2]],
            all_unit_vocab[:15],
            all_unit_qs
        )
    }
    write_json(f"content/es-es/stories/world/b1/b1-{slug}.json", comb_data)

    # Consolidation exercises & lesson
    cons_stem = f"b1-{slug}-consolidation"
    cons_ex_list = []
    cons_ex_refs = []
    first_g_slug = u["lessons"][0]["grammar_slug"]
    for idx, raw_ex in enumerate(u["consolidation_exercises"], start=1):
        ex_id = f"{cons_stem}.ex{idx:02d}"
        cons_ex_refs.append(ex_id)
        cons_ex_list.append(_convert_ex_item(ex_id, raw_ex, first_g_slug))

    cons_ex_rel = f"exercises/b1/{cons_stem}-ex.json"
    write_json(f"content/es-es/{cons_ex_rel}", {
        "lesson": cons_stem,
        "exercises": cons_ex_list
    })

    cons_goals = [
        f"Review all 5 lessons of {unit_title} for the CCSE citizenship exam",
        "Consolidate 40 civic vocabulary terms and 5 B1 grammatical structures"
    ]
    cons_lesson = {
        "id": f"lesson.b1.{slug}.consolidation",
        "title": f"Consolidación: {unit_title}",
        "level": "B1",
        "goal": f"Consolidate your knowledge of {unit_title} for the CCSE citizenship exam.",
        "grammar": f"Review of grammatical structures from {unit_title}",
        "sections": [
            {"type": "goal", "items": cons_goals},
            {"type": "recycle", "count": 3},
            {
                "type": "exercise-group",
                "title": "Review",
                "ref": cons_ex_rel,
                "exerciseRefs": cons_ex_refs
            },
            {
                "type": "checklist",
                "items": [f"I can {g[0].lower() + g[1:]}" for g in cons_goals]
            }
        ]
    }
    write_json(f"content/es-es/lessons/b1/{cons_stem}.json", cons_lesson)

    # Update units/b1.json
    units_path = ROOT / "content/es-es/curriculum/units/b1.json"
    units_data = json.loads(units_path.read_text(encoding="utf-8"))
    new_stems = [f"b1-{slug}-{i:02d}" for i in range(1, 6)] + [f"b1-{slug}-consolidation"]
    for entry in units_data:
        if entry.get("track") == "cultura" and (unit_title in entry.get("title", "") or any(s.startswith(old_prefix) for s in entry.get("stems", []))):
            entry["stems"] = new_stems
            break
    write_json("content/es-es/curriculum/units/b1.json", units_data)


def emit_unit(slug, old_prefix=None, unit_title_match=None, order_idx=None, lessons_cfg=None, comb_story_cfg=None, consolidation_cfg=None):
    if isinstance(slug, dict):
        return emit_unit_from_dict(slug)
    # Remove legacy files
    for folder in ["lessons/b1", "vocabulary/b1", "grammar/b1", "exercises/b1"]:
        dir_path = ROOT / "content/es-es" / folder
        if dir_path.exists():
            for old_file in dir_path.glob(f"{old_prefix}*"):
                old_file.unlink()
                print(f"Removed legacy file {old_file.relative_to(ROOT)}")

    for lcfg in lessons_cfg:
        num = lcfg["num"]
        stem = f"b1-{slug}-{num}"
        # 1. Vocab
        voc_data = {
            "id": f"vocab.b1.{slug}.{num}",
            "lesson": stem,
            "title": lcfg["title"],
            "theme": lcfg["theme"],
            "words": lcfg["words"]
        }
        vocab_rel = f"vocabulary/b1/{stem}-voc.json"
        write_json(f"content/es-es/{vocab_rel}", voc_data)

        # 2. Grammar
        g_slug = lcfg["grammar_slug"]
        gr_data = {
            "id": f"grammar.b1.{slug}.{num}.{g_slug}",
            "title": lcfg["grammar_title"],
            "sections": lcfg["grammar_sections"]
        }
        gr_rel = f"grammar/b1/{stem}-{g_slug}-gr.json"
        write_json(f"content/es-es/{gr_rel}", gr_data)

        # 3. Story
        paras = [{"type": "narration", "text": t} for t in lcfg["story_paragraphs"]]
        story_data = {
            "id": f"story.b1.{slug}.{num}",
            "title": lcfg["title"],
            "level": "B1",
            "lesson": int(num),
            "order": int(num),
            "type": "world",
            "estimatedMinutes": 5,
            "summary": lcfg["story_summary"],
            "characters": [],
            "location": lcfg["location"],
            "grammar": [g_slug],
            "vocabularyTopics": [lcfg["theme"], lcfg["title"]],
            "paragraphs": paras,
            "narration": make_narration(
                paras,
                [g_slug],
                [
                    {"lemma": lcfg["words"][0]["lemma"], "pos": lcfg["words"][0]["pos"], "cefr": "B1", "gloss": lcfg["words"][0]["translation"]},
                    {"lemma": lcfg["words"][1]["lemma"], "pos": lcfg["words"][1]["pos"], "cefr": "B1", "gloss": lcfg["words"][1]["translation"]},
                    {"lemma": lcfg["words"][2]["lemma"], "pos": lcfg["words"][2]["pos"], "cefr": "B1", "gloss": lcfg["words"][2]["translation"]}
                ],
                lcfg["comp_questions"]
            )
        }
        story_rel = f"stories/world/b1/{stem}-{lcfg['story_suffix']}.json"
        write_json(f"content/es-es/{story_rel}", story_data)

        # 4. Exercises
        w = lcfg["words"]
        ex_list = [
            {
                "id": f"{stem}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [[w[i]["lemma"], w[i]["translation"]] for i in range(4)]
            },
            {
                "id": f"{stem}.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [[w[i]["lemma"], w[i]["translation"]] for i in range(4, 8)]
            },
            {
                "id": f"{stem}.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": lcfg["mc1"]["q"],
                "options": lcfg["mc1"]["opts"],
                "correct": 0
            },
            {
                "id": f"{stem}.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": lcfg["mc2"]["q"],
                "options": lcfg["mc2"]["opts"],
                "correct": 0
            },
            {
                "id": f"{stem}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": lcfg["fb"]["sentence"],
                "answer": lcfg["fb"]["answer"],
                "teaches": [g_slug],
                "english": lcfg["fb"]["english"]
            },
            {
                "id": f"{stem}.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": lcfg["mc3"]["q"],
                "options": lcfg["mc3"]["opts"],
                "correct": 0
            },
            {
                "id": f"{stem}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": lcfg["sb"]["words"],
                "solution": lcfg["sb"]["words"],
                "english": lcfg["sb"]["english"],
                "teaches": [g_slug]
            },
            {
                "id": f"{stem}.ex07",
                "type": "dialogue-complete",
                "category": "reading",
                "prompt": [
                    {"speaker": lcfg["dlg"]["s1"], "text": lcfg["dlg"]["q"]},
                    {"speaker": lcfg["dlg"]["s2"], "text": "_____"}
                ],
                "options": lcfg["dlg"]["opts"],
                "correct": 0
            },
            {
                "id": f"{stem}.ex08",
                "type": "listening-choice",
                "category": "listening",
                "sentence": lcfg["listen"]["sentence"],
                "options": lcfg["listen"]["opts"],
                "correct": 0
            }
        ]
        ex_rel = f"exercises/b1/{stem}-ex.json"
        write_json(f"content/es-es/{ex_rel}", {"lesson": stem, "exercises": ex_list})

        # 5. Lesson
        lesson_data = {
            "id": f"lesson.b1.{slug}.{num}",
            "title": lcfg["title"],
            "level": "B1",
            "goal": lcfg["goal"],
            "grammar": lcfg["grammar_short"],
            "sections": [
                {"type": "goal", "items": lcfg["goals"]},
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_rel},
                {"type": "vocabulary", "ref": vocab_rel},
                {"type": "grammar", "ref": gr_rel},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": ex_rel,
                    "exerciseRefs": [
                        f"{stem}.ex01", f"{stem}.ex01b", f"{stem}.ex02",
                        f"{stem}.ex03", f"{stem}.ex04", f"{stem}.ex05",
                        f"{stem}.ex06", f"{stem}.ex07", f"{stem}.ex08"
                    ]
                },
                {"type": "srs"},
                {"type": "checklist", "items": [f"I can {g[0].lower() + g[1:]}" for g in lcfg["goals"]]}
            ]
        }
        write_json(f"content/es-es/lessons/b1/{stem}.json", lesson_data)

    # Combined story
    c_paras = [{"type": "narration", "text": t} for t in comb_story_cfg["paragraphs"]]
    comb_data = {
        "id": f"story.b1.{slug}",
        "title": comb_story_cfg["title"],
        "level": "B1",
        "order": order_idx,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": comb_story_cfg["summary"],
        "characters": [],
        "location": "España",
        "grammar": [l["grammar_slug"] for l in lessons_cfg],
        "vocabularyTopics": [l["title"] for l in lessons_cfg],
        "paragraphs": c_paras,
        "narration": make_narration(
            c_paras,
            [lessons_cfg[0]["grammar_slug"], lessons_cfg[1]["grammar_slug"]],
            [
                {"lemma": lessons_cfg[0]["words"][0]["lemma"], "pos": lessons_cfg[0]["words"][0]["pos"], "cefr": "B1", "gloss": lessons_cfg[0]["words"][0]["translation"]},
                {"lemma": lessons_cfg[1]["words"][0]["lemma"], "pos": lessons_cfg[1]["words"][0]["pos"], "cefr": "B1", "gloss": lessons_cfg[1]["words"][0]["translation"]}
            ],
            comb_story_cfg["comp_questions"]
        )
    }
    write_json(f"content/es-es/stories/world/b1/b1-{slug}.json", comb_data)

    # Consolidation exercises & lesson
    cons_stem = f"b1-{slug}-consolidation"
    cons_ex_rel = f"exercises/b1/{cons_stem}-ex.json"
    write_json(f"content/es-es/{cons_ex_rel}", {
        "lesson": cons_stem,
        "exercises": consolidation_cfg["exercises"]
    })

    cons_lesson = {
        "id": f"lesson.b1.{slug}.consolidation",
        "title": consolidation_cfg["title"],
        "level": "B1",
        "goal": consolidation_cfg["goal"],
        "grammar": consolidation_cfg["grammar"],
        "sections": [
            {"type": "goal", "items": consolidation_cfg["goals"]},
            {"type": "recycle", "count": 3},
            {
                "type": "exercise-group",
                "title": "Review",
                "ref": cons_ex_rel,
                "exerciseRefs": [f"{cons_stem}.ex{i:02d}" for i in range(1, 19)]
            },
            {
                "type": "checklist",
                "items": [f"I can {g[0].lower() + g[1:]}" for g in consolidation_cfg["goals"]]
            }
        ]
    }
    write_json(f"content/es-es/lessons/b1/{cons_stem}.json", cons_lesson)

    # Update units/b1.json
    units_path = ROOT / "content/es-es/curriculum/units/b1.json"
    units_data = json.loads(units_path.read_text(encoding="utf-8"))
    for u in units_data:
        if u.get("track") == "cultura" and unit_title_match in u.get("title", ""):
            u["stems"] = [f"b1-{slug}-0{i}" for i in range(1, 6)] + [cons_stem]
            break
    write_json("content/es-es/curriculum/units/b1.json", units_data)


def build_unit_2():
    lessons = [
        {
            "num": "01",
            "story_suffix": "jefeestado",
            "title": "El Rey como Jefe del Estado y símbolo de unidad",
            "theme": "La Corona y la Jefatura del Estado",
            "goal": "Comprender el papel constitucional del Rey como Jefe del Estado y diferenciar sus residencias institucionales.",
            "grammar_short": "ostentar y representar",
            "grammar_slug": "ostentar-y-representar",
            "grammar_title": "Verbos de representación institucional: «ostentar», «asumir» y «representar»",
            "location": "Madrid, Palacio de la Zarzuela y Palacio Real",
            "words": [
                {"lemma": "ostentar", "translation": "to hold (an office or title)", "pos": "verb"},
                {"lemma": "la Corona", "translation": "the Crown", "pos": "noun"},
                {"lemma": "el monarca", "translation": "monarch", "pos": "noun"},
                {"lemma": "el Palacio de la Zarzuela", "translation": "Zarzuela Palace (official royal residence)", "pos": "expression"},
                {"lemma": "el Palacio Real", "translation": "Royal Palace (ceremonial palace in Madrid)", "pos": "expression"},
                {"lemma": "la neutralidad", "translation": "neutrality", "pos": "noun"},
                {"lemma": "la Casa Real", "translation": "Royal Household", "pos": "expression"},
                {"lemma": "el acto solemne", "translation": "solemn state ceremony", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "En el español institucional que emplea el Título II de la Constitución, cargos y títulos de máxima dignidad se expresan con el verbo *ostentar* (*ostentar la Jefatura del Estado*, *ostentar el título*) y *asumir* (*asumir la más alta representación*)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Rey Felipe VI ostenta la Jefatura del Estado desde su proclamación en junio de 2014.", "english": "King Felipe VI has held the Headship of State since his proclamation in June 2014."},
                        {"spanish": "El monarca asume la más alta representación del Estado español en las relaciones internacionales.", "english": "The monarch assumes the highest representation of the Spanish State in international relations."},
                        {"spanish": "El Palacio Real se utiliza para los actos solemnes, mientras que los Reyes residen en el Palacio de la Zarzuela.", "english": "The Royal Palace is used for solemn state ceremonies, whereas the King and Queen reside at the Zarzuela Palace."},
                        {"spanish": "La Corona representa la neutralidad institucional por encima de los partidos políticos.", "english": "The Crown represents institutional neutrality above political parties."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "En el lenguaje administrativo, *ostentar un cargo* es neutro y formal (equivale a *to hold an office*), sin la connotación de presunción que tiene en la lengua coloquial."
                }
            ],
            "story_summary": "Article 56 of the Constitution defines the King as Head of State and symbol of unity and permanence, distinguishing the daily work residence at the Zarzuela Palace from ceremonial state functions at the Royal Palace.",
            "story_paragraphs": [
                "El Título II de la Constitución Española, que abarca de los artículos 56 al 65, está íntegramente dedicado a la institución de la Corona.",
                "Su artículo 56 define con precisión la figura del monarca: el Rey es el Jefe del Estado, símbolo de su unidad y permanencia, y arbitra y modera el funcionamiento regular de las instituciones.",
                "Desde el 19 de junio de 2014, tras la abdicación de Juan Carlos I, el Rey de España es Felipe VI, casado con la Reina Letizia.",
                "Una pregunta clásica del examen CCSE distingue entre los dos palacios vinculados a la Jefatura del Estado en Madrid: la residencia oficial donde vive y trabaja diariamente la Familia Real es el Palacio de la Zarzuela, situado a las afueras de la capital.",
                "Por su parte, el imponente Palacio Real de Madrid, situado en la plaza de Oriente, es propiedad de Patrimonio Nacional y se reserva para las grandes ceremonias de Estado, las recepciones oficiales y la entrega de cartas credenciales de los embajadores extranjeros."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuál es la residencia oficial donde vive habitualmente el Rey de España?",
                    "options": ["El Palacio de la Zarzuela", "El Palacio de la Moncloa", "El Palacio de las Cortes", "El Museo del Prado"],
                    "correctIndex": 0,
                    "explanation": "La residencia oficial de los Reyes es el Palacio de la Zarzuela; el Palacio de la Moncloa es la sede del Presidente del Gobierno."
                },
                {
                    "question": "¿Quién es el actual Rey de España desde junio de 2014?",
                    "options": ["Felipe VI", "Juan Carlos I", "Alfonso XIII", "Carlos IV"],
                    "correctIndex": 0,
                    "explanation": "Felipe VI fue proclamado Rey ante las Cortes Generales el 19 de junio de 2014."
                },
                {
                    "question": "¿Para qué se utiliza principalmente el Palacio Real de Madrid?",
                    "options": ["Para los actos solemnes de Estado y recepciones oficiales", "Como sede del Tribunal Constitucional", "Como cámara legislativa del Senado", "Como residencia del Defensor del Pueblo"],
                    "correctIndex": 0,
                    "explanation": "El Palacio Real se emplea para ceremonias de Estado y actos oficiales solemnes."
                }
            ],
            "goals": [
                "Define the King's constitutional status under Title II (Article 56) as Head of State and symbol of unity and permanence.",
                "Identify King Felipe VI as the current monarch since June 2014.",
                "Distinguish between the Zarzuela Palace (official residence) and the Royal Palace (ceremonial state functions).",
                "Use 'ostentar' and 'asumir' to describe high constitutional offices."
            ],
            "mc1": {
                "q": "¿Cuál es la residencia oficial del Rey de España y de la Familia Real?",
                "opts": ["El Palacio de la Zarzuela.", "El Palacio de la Moncloa.", "El Palacio de Cibeles."]
            },
            "mc2": {
                "q": "¿Qué título regula la institución de la Corona en la Constitución Española?",
                "opts": ["El Título II (artículos 56 a 65).", "El Título VIII (sobre la organización territorial).", "El Título X (sobre la reforma constitucional)."]
            },
            "fb": {
                "sentence": "El Rey Felipe VI ___ la Jefatura del Estado español desde el año 2014. (ostentar)",
                "answer": "ostenta",
                "english": "King Felipe VI has held the Headship of the Spanish State since 2014."
            },
            "mc3": {
                "q": "¿Quién es el Rey de España en la actualidad?",
                "opts": ["Felipe VI.", "Juan Carlos II.", "Felipe V."]
            },
            "sb": {
                "words": ["El", "Rey", "asume", "la", "más", "alta", "representación", "del", "Estado", "español."],
                "english": "The King assumes the highest representation of the Spanish State."
            },
            "dlg": {
                "s1": "Carmen", "s2": "Álvaro",
                "q": "¿Vive el Rey en el Palacio de la Moncloa o en el Palacio de la Zarzuela?",
                "opts": [
                    "El Rey reside en el Palacio de la Zarzuela; el Palacio de la Moncloa es la residencia del Presidente del Gobierno.",
                    "El Rey vive en el Palacio de la Moncloa junto a todos los ministros.",
                    "El Rey reside en el edificio del Senado."
                ]
            },
            "listen": {
                "sentence": "El Palacio Real de Madrid se utiliza para las ceremonias de Estado, mientras que la residencia oficial del Rey es el Palacio de la Zarzuela.",
                "opts": [
                    "The Royal Palace of Madrid is used for State ceremonies, while the King's official residence is the Zarzuela Palace.",
                    "The King lives in the Moncloa Palace and presides over Parliament every day.",
                    "Title II of the Constitution regulates municipal taxes rather than the Crown."
                ]
            }
        },
        {
            "num": "02",
            "story_suffix": "funciones",
            "title": "Funciones constitucionales del Rey",
            "theme": "La Corona y la Jefatura del Estado",
            "goal": "Aprender las funciones tasadas del Rey en el artículo 62: sancionar leyes, convocar elecciones y proponer al Presidente del Gobierno.",
            "grammar_short": "a propuesta de / previa deliberación",
            "grammar_slug": "previa-propuesta-de",
            "grammar_title": "Requisitos constitucionales: «a propuesta de» y «previa deliberación de»",
            "location": "Madrid, Congreso de los Diputados",
            "words": [
                {"lemma": "proponer", "translation": "to propose, nominate", "pos": "verb"},
                {"lemma": "nombrar", "translation": "to appoint", "pos": "verb"},
                {"lemma": "disolver", "translation": "to dissolve (Parliament)", "pos": "verb"},
                {"lemma": "convocar", "translation": "to call, convene (elections or Cortes)", "pos": "verb"},
                {"lemma": "expedir", "translation": "to issue (decrees)", "pos": "verb"},
                {"lemma": "el decreto", "translation": "decree", "pos": "noun"},
                {"lemma": "la deliberación", "translation": "deliberation", "pos": "noun"},
                {"lemma": "el candidato", "translation": "candidate", "pos": "noun"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "En una monarquía parlamentaria, las funciones del Jefe del Estado son *tasadas* (estrictamente fijadas por la ley). Por ello, la Constitución utiliza locuciones como *a propuesta de* (at the proposal of) y *previa deliberación de* (following prior deliberation by) para indicar quién toma realmente la decisión política."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Rey nombra y separa a los miembros del Gobierno, a propuesta de su Presidente.", "english": "The King appoints and dismisses members of the Government, at the proposal of its President."},
                        {"spanish": "El monarca expide los decretos acordados en el Consejo de Ministros.", "english": "The monarch issues the decrees agreed upon in the Council of Ministers."},
                        {"spanish": "El Rey convoca a referéndum en los casos previstos por la Constitución, a propuesta del Presidente del Gobierno.", "english": "The King calls a referendum in the cases provided for by the Constitution, at the proposal of the Prime Minister."},
                        {"spanish": "Tras consultar con los grupos políticos con representación parlamentaria, el Rey propone un candidato a la Presidencia del Gobierno.", "english": "After consulting with the political groups with parliamentary representation, the King proposes a candidate for Prime Minister."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Observa que el Rey *nombra* formalmente a los ministros, pero siempre *a propuesta del Presidente del Gobierno*, quien los elige."
                }
            ],
            "story_summary": "How Article 62 specifies the constitutional duties of the King: sanctioning and promulgating laws within 15 days, convening and dissolving the Cortes, and proposing a candidate for Prime Minister after parliamentary consultations.",
            "story_paragraphs": [
                "¿Qué hace exactamente el Rey en una monarquía parlamentaria? El artículo 62 de la Constitución enumera con exactitud sus funciones constitucionales, todas ellas regladas y sujetas a la voluntad democrática.",
                "En el ámbito legislativo, al Rey le corresponde sancionar en el plazo de quince días las leyes aprobadas por las Cortes Generales, promulgarlas y ordenar su inmediata publicación en el Boletín Oficial del Estado.",
                "En la vida parlamentaria, el monarca convoca y disuelve las Cortes Generales y convoca elecciones generales en los términos previstos en la Constitución.",
                "Tras cada renovación del Congreso de los Diputados, el Rey se reúne con los representantes de los grupos políticos que han obtenido escaños y, a través del Presidente del Congreso, propone un candidato a la Presidencia del Gobierno para que se someta al debate de investidura.",
                "Una vez que el Congreso otorga su confianza al candidato, el Rey lo nombra Presidente del Gobierno y, posteriormente, nombra y separa a los demás ministros a propuesta del propio Presidente."
            ],
            "comp_questions": [
                {
                    "question": "¿En qué plazo sanciona el Rey las leyes aprobadas por las Cortes Generales?",
                    "options": ["En el plazo de quince días", "En el plazo de seis meses", "Antes de que las vote el Congreso", "Cada cuatro años"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 91 de la Constitución, el Rey sancionará en el plazo de quince días las leyes aprobadas por las Cortes Generales."
                },
                {
                    "question": "¿A propuesta de quién nombra el Rey a los ministros del Gobierno?",
                    "options": ["A propuesta del Presidente del Gobierno", "Por decisión personal de la Casa Real", "A propuesta de los alcaldes", "A propuesta del Tribunal Constitucional"],
                    "correctIndex": 0,
                    "explanation": "El artículo 62.e dispone que el Rey nombra y separa a los miembros del Gobierno a propuesta de su Presidente."
                },
                {
                    "question": "¿Qué hace el Rey tras celebrar consultas con los grupos políticos con representación parlamentaria?",
                    "options": ["Propone un candidato a la Presidencia del Gobierno a través del Presidente del Congreso", "Elige directamente a los 350 diputados", "Aprueba los Presupuestos Generales del Estado", "Redacta los Estatutos de Autonomía"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 99, el Rey propone un candidato a la Presidencia del Gobierno a través del Presidente del Congreso."
                }
            ],
            "goals": [
                "List the King's legislative duties: sanctioning, promulgating, and ordering the publication of laws.",
                "Explain how the King proposes a candidate for Prime Minister after consulting parliamentary groups.",
                "State that the King appoints and dismisses ministers at the proposal of the Prime Minister.",
                "Use 'a propuesta de' to describe formal institutional procedures."
            ],
            "mc1": {
                "q": "¿Quién sanciona y promulga las leyes aprobadas por las Cortes Generales?",
                "opts": ["El Rey.", "El Defensor del Pueblo.", "El Fiscal General del Estado."]
            },
            "mc2": {
                "q": "Según el artículo 62 de la Constitución, ¿cómo se nombra a los ministros del Gobierno?",
                "opts": [
                    "Los nombra el Rey, a propuesta del Presidente del Gobierno.",
                    "Los elige directamente el Senado por sorteo.",
                    "Los nombra el Tribunal Supremo cada nueve años."
                ]
            },
            "fb": {
                "sentence": "El Rey nombra y separa a los miembros del Gobierno, a ___ de su Presidente. (propuesta)",
                "answer": "propuesta",
                "english": "The King appoints and dismisses the members of the Government, at the proposal of its President."
            },
            "mc3": {
                "q": "¿A través de qué autoridad propone el Rey al candidato a la Presidencia del Gobierno?",
                "opts": ["A través del Presidente del Congreso de los Diputados.", "A través del Alcalde de Madrid.", "A través del Consejo de Estado."]
            },
            "sb": {
                "words": ["El", "Rey", "expide", "los", "decretos", "acordados", "en", "el", "Consejo", "de", "Ministros."],
                "english": "The King issues the decrees agreed upon in the Council of Ministers."
            },
            "dlg": {
                "s1": "Nuria", "s2": "Héctor",
                "q": "¿Puede el Rey negarse a sancionar una ley que han aprobado las Cortes Generales?",
                "opts": [
                    "No, en la monarquía parlamentaria la sanción real es un acto debido que se realiza en el plazo de quince días.",
                    "Sí, el Rey tiene derecho de veto absoluto sobre cualquier ley.",
                    "Sí, el Rey puede modificar el texto de la ley antes de firmarlo."
                ]
            },
            "listen": {
                "sentence": "Al Rey le corresponde convocar y disolver las Cortes Generales y convocar elecciones en los términos previstos en la Constitución.",
                "opts": [
                    "It falls to the King to convene and dissolve the Cortes Generales and call elections under the terms provided for in the Constitution.",
                    "The King drafts the laws and votes in the Congress of Deputies.",
                    "Ministers are appointed without the intervention of the Prime Minister."
                ]
            }
        },
        {
            "num": "03",
            "story_suffix": "refrendo",
            "title": "Inviolabilidad de la Corona y la institución del refrendo",
            "theme": "La Corona y la Jefatura del Estado",
            "goal": "Entender por qué los actos del Rey requieren refrendo ministerial o parlamentario y quién asume la responsabilidad jurídica.",
            "grammar_short": "carecer de validez sin",
            "grammar_slug": "carecer-de-validez-sin",
            "grammar_title": "Validez y responsabilidad jurídica: «carecer de validez» y «estar sujeto a»",
            "location": "Madrid",
            "words": [
                {"lemma": "el refrendo", "translation": "countersignature, endorsement", "pos": "noun"},
                {"lemma": "refrendar", "translation": "to countersign, endorse", "pos": "verb"},
                {"lemma": "inviolable", "translation": "inviolable", "pos": "adjective"},
                {"lemma": "la validez", "translation": "validity", "pos": "noun"},
                {"lemma": "la responsabilidad", "translation": "liability, responsibility", "pos": "noun"},
                {"lemma": "carecer de", "translation": "to lack, be devoid of", "pos": "expression"},
                {"lemma": "estar sujeto a", "translation": "to be subject to", "pos": "expression"},
                {"lemma": "el ministro competente", "translation": "competent minister (in charge of the area)", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "Para expresar cuándo un acto oficial es nulo o quién responde legalmente de él, el texto constitucional emplea dos construcciones fundamentales: *carecer de validez* (to lack validity / be null and void) y *estar sujeto a responsabilidad* (to be subject to liability)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "Los actos del Rey carecerán de validez sin el refrendo correspondiente.", "english": "The King's acts shall lack validity without the corresponding countersignature."},
                        {"spanish": "La persona del Rey es inviolable y no está sujeta a responsabilidad.", "english": "The person of the King is inviolable and is not subject to liability."},
                        {"spanish": "De los actos del Rey serán responsables las personas que los refrenden.", "english": "The persons who countersign the King's acts shall be responsible for them."},
                        {"spanish": "Los actos oficiales del monarca son refrendados por el Presidente del Gobierno o por los ministros competentes.", "english": "The official acts of the monarch are countersigned by the Prime Minister or by the competent ministers."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Carecer* rige siempre la preposición *de*: *carecer de validez*, *carecer de efecto legal*."
                }
            ],
            "story_summary": "Why Article 56.3 and Article 64 connect the King's inviolability with the institution of the countersignature ('refrendo'), transferring political and legal responsibility to the Prime Minister, competent ministers, or the President of Congress.",
            "story_paragraphs": [
                "En derecho constitucional existe una regla de oro: donde no hay poder de decisión política propia, tampoco hay responsabilidad política; y quien firma y decide, responde ante el Parlamento.",
                "Por ese motivo, el artículo 56.3 de la Constitución establece que la persona del Rey es inviolable y no está sujeta a responsabilidad, pero añade inmediatamente que sus actos estarán siempre refrendados y que carecerán de validez sin dicho refrendo.",
                "¿En qué consiste el refrendo regulado en el artículo 64? Es la firma de acompañamiento mediante la cual el Presidente del Gobierno o los ministros competentes autentican el acto del Rey y asumen plenamente la responsabilidad política y jurídica del mismo.",
                "En tres supuestos especiales —la propuesta y el nombramiento del Presidente del Gobierno, y la disolución de las cámaras si ningún candidato logra la investidura tras dos meses—, el refrendo lo realiza el Presidente del Congreso de los Diputados.",
                "La única excepción al requisito del refrendo, prevista en el artículo 65.2, es el nombramiento y relevo libre de los miembros civiles y militares de su propia Casa Real y la administración del presupuesto asignado a su familia y Casa."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué ocurre con los actos oficiales del Rey si no cuentan con el refrendo previsto en el artículo 64?",
                    "options": ["Carecen de validez", "Tienen doble valor legal", "Se convierten en leyes orgánicas", "Pasan al Senado automáticamente"],
                    "correctIndex": 0,
                    "explanation": "El artículo 56.3 dispone que los actos del Rey carecerán de validez sin el refrendo."
                },
                {
                    "question": "¿Quiénes refrendan con carácter general los actos del Rey?",
                    "options": ["El Presidente del Gobierno y, en su caso, los ministros competentes", "Los alcaldes de las capitales de provincia", "Los magistrados del Tribunal Supremo", "Los senadores autonómicos"],
                    "correctIndex": 0,
                    "explanation": "El artículo 64.1 establece que los actos del Rey serán refrendados por el Presidente del Gobierno y, en su caso, por los ministros competentes."
                },
                {
                    "question": "¿Quién asume la responsabilidad de los actos oficiales del Rey?",
                    "options": ["Las personas que los refrenden (el Presidente del Gobierno, los ministros o el Presidente del Congreso)", "Nadie asume la responsabilidad", "El Defensor del Pueblo", "El Consejo de Estado"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 64.2, de los actos del Rey serán responsables las personas que los refrenden."
                }
            ],
            "goals": [
                "Explain the connection between the King's inviolability and the constitutional institution of 'refrendo'.",
                "Identify who countersigns the King's acts: the Prime Minister, competent ministers, or the President of Congress.",
                "State that responsibility for the King's official acts belongs to the authority who countersigns them.",
                "Use 'carecer de validez' and 'estar sujeto a' in legal sentences."
            ],
            "mc1": {
                "q": "Según los artículos 56 y 64 de la Constitución, ¿por quién son refrendados los actos del Rey?",
                "opts": [
                    "Por el Presidente del Gobierno y, en su caso, por los ministros competentes (o el Presidente del Congreso en casos específicos).",
                    "Por el Presidente del Tribunal Constitucional.",
                    "Por el Fiscal General del Estado."
                ]
            },
            "mc2": {
                "q": "¿Quién es responsable jurídicamente y políticamente de los actos del Rey?",
                "opts": [
                    "Las personas que los refrenden.",
                    "El jefe de protocolo de Patrimonio Nacional.",
                    "El Cuerpo Diplomático extranjero."
                ]
            },
            "fb": {
                "sentence": "Los actos del Rey ___ de validez sin el refrendo establecido en la Constitución. (carecer)",
                "answer": "carecen",
                "english": "The King's acts lack validity without the countersignature established in the Constitution."
            },
            "mc3": {
                "q": "¿Qué acto puede realizar el Rey libremente sin necesidad de refrendo según el artículo 65.2?",
                "opts": [
                    "Nombrar y relevar a los miembros civiles y militares de su Casa Real.",
                    "Aprobar un Real Decreto-ley de urgencia.",
                    "Declarar la guerra y firmar tratados comerciales."
                ]
            },
            "sb": {
                "words": ["De", "los", "actos", "del", "Rey", "serán", "responsables", "las", "personas", "que", "los", "refrenden."],
                "english": "The persons who countersign the King's acts shall be responsible for them."
            },
            "dlg": {
                "s1": "Beatriz", "s2": "Óscar",
                "q": "¿Quién refrenda el nombramiento del nuevo Presidente del Gobierno tras la votación de investidura?",
                "opts": [
                    "El Presidente del Congreso de los Diputados.",
                    "El Alcalde de la villa de Madrid.",
                    "El Presidente saliente del Senado."
                ]
            },
            "listen": {
                "sentence": "La persona del Rey es inviolable y no está sujeta a responsabilidad; sus actos estarán siempre refrendados.",
                "opts": [
                    "The person of the King is inviolable and is not subject to liability; his acts shall always be countersigned.",
                    "The King's acts do not require the signature of any minister.",
                    "The President of the Supreme Court countersigns all royal decrees."
                ]
            }
        },
        {
            "num": "04",
            "story_suffix": "sucesion",
            "title": "La sucesión en la Corona y la Princesa de Asturias",
            "theme": "La Corona y la Jefatura del Estado",
            "goal": "Conocer las reglas de sucesión hereditaria del artículo 57, el título de Princesa de Asturias y el juramento ante las Cortes.",
            "grammar_short": "al + infinitivo temporal",
            "grammar_slug": "al-cumplir-infinitivo",
            "grammar_title": "Simultaneidad e inmediatez institucional: «al + infinitivo»",
            "location": "Madrid y Oviedo",
            "words": [
                {"lemma": "hereditario", "translation": "hereditary", "pos": "adjective"},
                {"lemma": "el sucesor", "translation": "successor", "pos": "noun"},
                {"lemma": "la Princesa de Asturias", "translation": "Princess of Asturias (heir to the Crown)", "pos": "expression"},
                {"lemma": "la mayoría de edad", "translation": "legal age of majority (18 years)", "pos": "expression"},
                {"lemma": "prestar juramento", "translation": "to take an oath", "pos": "expression"},
                {"lemma": "la abdicación", "translation": "abdication", "pos": "noun"},
                {"lemma": "la regencia", "translation": "regency", "pos": "noun"},
                {"lemma": "la primogenitura", "translation": "primogeniture", "pos": "noun"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "La construcción *al + infinitivo* (*al alcanzar la mayoría de edad*, *al ser proclamado*) expresa el momento exacto en que se activa una obligación o ceremonia constitucional, equivalente a *upon reaching / when proclaimed* en inglés."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Príncipe o la Princesa heredera presta juramento ante las Cortes Generales al alcanzar la mayoría de edad.", "english": "The Crown Prince or Princess takes an oath before the Cortes Generales upon reaching the age of majority."},
                        {"spanish": "El Rey, al ser proclamado ante las Cortes Generales, jura guardar y hacer guardar la Constitución.", "english": "The King, upon being proclaimed before the Cortes Generales, swears to uphold and enforce the Constitution."},
                        {"spanish": "En octubre de 2023, la Princesa Leonor juró la Constitución al cumplir dieciocho años.", "english": "In October 2023, Princess Leonor swore allegiance to the Constitution upon turning eighteen."},
                        {"spanish": "Al producirse una abdicación, las dudas de hecho o de derecho se resuelven por una ley orgánica.", "english": "When an abdication occurs, any doubts of fact or law are resolved by an organic law."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Al + infinitivo* comparte normalmente el mismo sujeto que el verbo principal y aporta concisión y solemnidad al estilo narrativo."
                }
            ],
            "story_summary": "How Article 57 regulates hereditary succession in the Crown of Spain, the historic title of Prince or Princess of Asturias held by the heir (currently Princess Leonor), and the solemn oath before the Cortes Generales.",
            "story_paragraphs": [
                "El artículo 57 de la Constitución establece que la Corona de España es hereditaria en los sucesores de S. M. Don Juan Carlos I de Borbón, legítimo heredero de la dinastía histórica.",
                "La sucesión en el trono sigue el orden regular de primogenitura y representación, siendo preferida siempre la línea anterior a las posteriores.",
                "¿Qué título recibe quien está llamado a heredar la Corona? Desde su nacimiento o desde que se produzca el hecho que origine el llamamiento, el heredero o heredera ostenta la dignidad de Príncipe o Princesa de Asturias, además de los demás títulos vinculados tradicionalmente al sucesor de la Corona de España (como Princesa de Girona y de Viana).",
                "En la actualidad, la heredera de la Corona es la Princesa de Asturias, Leonor de Borbón y Ortiz, hija primogénita de los Reyes Felipe VI y Letizia, mientras que su hermana menor es la Infanta Sofía.",
                "Tal como dispone el artículo 61.2, la Princesa de Asturias, al alcanzar la mayoría de edad el 31 de octubre de 2023, prestó ante las Cortes Generales el mismo juramento que el Rey: desempeñar fielmente sus funciones, guardar y hacer guardar la Constitución y las leyes, y respetar los derechos de los ciudadanos y de las comunidades autónomas."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué título principal ostenta la persona heredera de la Corona de España?",
                    "options": ["Príncipe o Princesa de Asturias", "Duque o Duquesa de Madrid", "Conde o Condesa de Castilla", "Marqués o Marquesa del Reino"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 57.2, el Príncipe heredero o Princesa heredera tiene la dignidad de Príncipe o Princesa de Asturias."
                },
                {
                    "question": "¿Quién es la actual Princesa de Asturias y heredera de la Corona española?",
                    "options": ["Leonor de Borbón y Ortiz", "Sofía de Borbón", "Elena de Borbón", "Cristina de Borbón"],
                    "correctIndex": 0,
                    "explanation": "La Princesa Leonor es la hija primogénita del Rey Felipe VI y heredera de la Corona."
                },
                {
                    "question": "¿Ante qué institución prestan juramento el Rey al ser proclamado y la Princesa heredera al alcanzar la mayoría de edad?",
                    "options": ["Ante las Cortes Generales", "Ante el Consejo de Estado", "Ante el Ayuntamiento de Oviedo", "Ante el Tribunal de Cuentas"],
                    "correctIndex": 0,
                    "explanation": "El artículo 61 establece que la proclamación y el juramento tienen lugar ante las Cortes Generales."
                }
            ],
            "goals": [
                "State that the Spanish Crown is hereditary under Article 57.",
                "Identify 'Príncipe o Princesa de Asturias' as the constitutional title of the heir to the Crown (currently Princess Leonor).",
                "Explain the oath sworn before the Cortes Generales upon proclamation or reaching the age of majority (18).",
                "Use 'al + infinitivo' to express simultaneous institutional actions."
            ],
            "mc1": {
                "q": "¿Qué título ostenta constitucionalmente el heredero o heredera de la Corona de España?",
                "opts": ["Príncipe o Princesa de Asturias.", "Príncipe o Princesa de Madrid.", "Duque o Duquesa de Toledo."]
            },
            "mc2": {
                "q": "¿Quién es en la actualidad la heredera de la Corona de España?",
                "opts": ["La Princesa de Asturias, Leonor de Borbón.", "La Infanta Sofía.", "La Reina Sofía."]
            },
            "fb": {
                "sentence": "La Princesa de Asturias prestó juramento ante las Cortes Generales ___ alcanzar la mayoría de edad. (al)",
                "answer": "al",
                "english": "The Princess of Asturias took an oath before the Cortes Generales upon reaching the age of majority."
            },
            "mc3": {
                "q": "¿Qué tipo de norma resuelve las abdicaciones y renuncias en el orden de sucesión a la Corona según el artículo 57.5?",
                "opts": ["Una ley orgánica aprobada por las Cortes Generales.", "Un reglamento municipal.", "Una orden ministerial simple."]
            },
            "sb": {
                "words": ["La", "Corona", "de", "España", "es", "hereditaria", "según", "la", "Constitución."],
                "english": "The Crown of Spain is hereditary according to the Constitution."
            },
            "dlg": {
                "s1": "Inés", "s2": "Mateo",
                "q": "¿Cuándo presta juramento de fidelidad a la Constitución el heredero o heredera de la Corona?",
                "opts": [
                    "Al alcanzar la mayoría de edad, a los dieciocho años, en sesión solemne ante las Cortes Generales.",
                    "Únicamente después de cumprir cuarenta años.",
                    "No tiene obligación de jurar la Constitución hasta ser proclamado Rey o Reina."
                ]
            },
            "listen": {
                "sentence": "El heredero de la Corona tiene la dignidad de Príncipe o Princesa de Asturias y presta juramento ante las Cortes Generales al alcanzar la mayoría de edad.",
                "opts": [
                    "The heir to the Crown holds the title of Prince or Princess of Asturias and takes an oath before the Cortes Generales upon reaching the age of majority.",
                    "The heir to the Crown is elected every four years by the Senate.",
                    "The title of Princess of Asturias belongs to the Prime Minister."
                ]
            }
        },
        {
            "num": "05",
            "story_suffix": "exterior",
            "title": "Mando supremo de las Fuerzas Armadas y representación exterior",
            "theme": "La Corona y la Jefatura del Estado",
            "goal": "Conocer las funciones del Rey como mando supremo de las Fuerzas Armadas, patrono de las Reales Academias y representante ante Iberoamérica.",
            "grammar_short": "en calidad de / en nombre de",
            "grammar_slug": "en-calidad-de",
            "grammar_title": "Locuciones de representación: «en calidad de» y «especialmente con»",
            "location": "Madrid e Iberoamérica",
            "words": [
                {"lemma": "el mando supremo", "translation": "supreme command", "pos": "expression"},
                {"lemma": "las Fuerzas Armadas", "translation": "Armed Forces", "pos": "expression"},
                {"lemma": "acreditar", "translation": "to accredit (ambassadors)", "pos": "verb"},
                {"lemma": "el embajador", "translation": "ambassador", "pos": "noun"},
                {"lemma": "el tratado internacional", "translation": "international treaty", "pos": "expression"},
                {"lemma": "el alto patronazgo", "translation": "high patronage", "pos": "expression"},
                {"lemma": "las Reales Academias", "translation": "Royal Academies", "pos": "expression"},
                {"lemma": "la comunidad histórica", "translation": "historical community (of nations)", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "Para precisar bajo qué título actúa una autoridad en el ámbito diplomático o cultural, se utiliza la locución *en calidad de* (in the capacity of / as). Asimismo, la Constitución destaca los vínculos internacionales con *especialmente con las naciones de su comunidad histórica*."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "En calidad de Jefe del Estado, el Rey acredita a los embajadores de España y recibe las cartas credenciales de los representantes extranjeros.", "english": "In his capacity as Head of State, the King accredits Spain's ambassadors and receives the letters of credence of foreign representatives."},
                        {"spanish": "El Rey ostenta el mando supremo de las Fuerzas Armadas y el alto patronazgo de las Reales Academias.", "english": "The King holds supreme command of the Armed Forces and high patronage of the Royal Academies."},
                        {"spanish": "El monarca asume la más alta representación del Estado en las relaciones internacionales, especialmente con las naciones de su comunidad histórica.", "english": "The monarch assumes the highest representation of the State in international relations, especially with the nations of its historical community."},
                        {"spanish": "Al Rey le corresponde manifestar el consentimiento del Estado para obligarse internacionalmente por medio de tratados.", "english": "It falls to the King to express the State's consent to be bound internationally by means of treaties."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "*En calidad de* va siempre seguido de un sustantivo sin artículo (*en calidad de Jefe del Estado*, *en calidad de embajador*)."
                }
            ],
            "story_summary": "The King's role as supreme commander of the Armed Forces (Article 62.h), High Patron of the Royal Academies (Article 62.j), and Spain's highest diplomatic representative, especially with the nations of its historical Ibero-American community.",
            "story_paragraphs": [
                "Además de sus funciones legislativas y de moderación política interna, los artículos 62 y 63 de la Constitución encomiendan al Rey atribuciones simbólicas y representativas esenciales en tres ámbitos: la defensa, la cultura y la política exterior.",
                "En primer lugar, el artículo 62.h establece que al Rey le corresponde el mando supremo de las Fuerzas Armadas (integradas por el Ejército de Tierra, la Armada y el Ejército del Aire y del Espacio), si bien la dirección efectiva de la defensa y de la Administración militar compete al Gobierno.",
                "En el terreno cultural y científico, el artículo 62.j confiere al monarca el Alto Patronazgo de las Reales Academias —como la Real Academia Española (RAE) o la Real Academia de la Historia—, agrupadas en el Instituto de España.",
                "En el ámbito exterior, en calidad de Jefe del Estado, el Rey acredita a los embajadores de España en el extranjero, recibe las cartas credenciales de los representantes diplomáticos acreditados en España y manifiesta el consentimiento del Estado en los tratados internacionales.",
                "Finalmente, el artículo 56.1 subraya que el Rey asume la más alta representación de España en las relaciones internacionales, especialmente con las naciones de su comunidad histórica, razón por la cual el monarca participa junto al Presidente del Gobierno en las Cumbres Iberoamericanas."
            ],
            "comp_questions": [
                {
                    "question": "¿A quién corresponde constitucionalmente el mando supremo de las Fuerzas Armadas?",
                    "options": ["Al Rey", "Al Presidente del Senado", "Al Defensor del Pueblo", "Al Fiscal General del Estado"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 62.h de la Constitución, corresponde al Rey el mando supremo de las Fuerzas Armadas."
                },
                {
                    "question": "¿Qué vínculo cultural ostenta el Rey respecto a las Reales Academias según el artículo 62.j?",
                    "options": ["El Alto Patronazgo de las Reales Academias", "La dirección de los exámenes universitarios", "La censura de libros", "La presidencia de las bibliotecas municipales"],
                    "correctIndex": 0,
                    "explanation": "El artículo 62.j atribuye al Rey el Alto Patronazgo de las Reales Academias."
                },
                {
                    "question": "Según el artículo 56.1, ¿con qué países tiene especial relevancia la representación internacional del Rey?",
                    "options": ["Especialmente con las naciones de su comunidad histórica (Iberoamérica)", "Exclusivamente con los países de Asia", "Solamente con los países sin embajada", "Únicamente con ciudades autónomas"],
                    "correctIndex": 0,
                    "explanation": "El artículo 56.1 destaca expresamente las relaciones con las naciones de su comunidad histórica."
                }
            ],
            "goals": [
                "State that the King holds the supreme command of the Armed Forces (Article 62.h).",
                "Identify the King's High Patronage of the Royal Academies (Article 62.j).",
                "Explain how the King accredits ambassadors, signs treaties, and represents Spain especially with the nations of its historical community.",
                "Use 'en calidad de' in diplomatic and institutional contexts."
            ],
            "mc1": {
                "q": "¿Quién ostenta el mando supremo de las Fuerzas Armadas en España según el artículo 62 de la Constitución?",
                "opts": ["El Rey.", "El Presidente del Tribunal Constitucional.", "El Presidente del Congreso."]
            },
            "mc2": {
                "q": "Según el artículo 63 de la Constitución, ¿quién acredita a los embajadores de España y recibe las cartas credenciales de los representantes extranjeros?",
                "opts": ["El Rey.", "El Alcalde de Madrid.", "El Defensor del Pueblo."]
            },
            "fb": {
                "sentence": "En ___ de Jefe del Estado, el Rey manifiesta el consentimiento de España en los tratados internacionales. (calidad)",
                "answer": "calidad",
                "english": "In his capacity as Head of State, the King expresses Spain's consent to international treaties."
            },
            "mc3": {
                "q": "¿Qué relación tiene el Rey con las Reales Academias según el artículo 62.j?",
                "opts": [
                    "Ejerce el Alto Patronazgo de las Reales Academias.",
                    "Nombra por decreto a todos los catedráticos de instituto.",
                    "No tiene ninguna relación constitucional con ellas."
                ]
            },
            "sb": {
                "words": ["El", "Rey", "ostenta", "el", "mando", "supremo", "de", "las", "Fuerzas", "Armadas."],
                "english": "The King holds the supreme command of the Armed Forces."
            },
            "dlg": {
                "s1": "Sofía", "s2": "Javier",
                "q": "¿A qué países se refiere la Constitución cuando menciona «las naciones de su comunidad histórica»?",
                "opts": [
                    "Se refiere especialmente a las naciones iberoamericanas y aquellas vinculadas históricamente y culturalmente con España.",
                    "Se refiere únicamente a las diecisiete comunidades autónomas.",
                    "Se refiere exclusivamente a las provincias limítrofes con Madrid."
                ]
            },
            "listen": {
                "sentence": "Corresponde al Rey el mando supremo de las Fuerzas Armadas y el Alto Patronazgo de las Reales Academias.",
                "opts": [
                    "Supreme command of the Armed Forces and High Patronage of the Royal Academies belong to the King.",
                    "The Senate commands the Armed Forces and appoints foreign ambassadors.",
                    "Ambassadors present their credentials to the Mayor of Madrid."
                ]
            }
        }
    ]

    comb = {
        "title": "La Corona y la Jefatura del Estado",
        "summary": "Comprehensive guide to Title II of the Spanish Constitution for the CCSE exam: King Felipe VI as Head of State, Zarzuela vs. Royal Palace, constitutional functions under Article 62, inviolability and countersignature (refrendo), Princess of Asturias and succession, and diplomatic/military representation.",
        "paragraphs": [
            "El Título II de la Constitución Española regula la Corona: el Rey (actualmente Felipe VI) es el Jefe del Estado y símbolo de su unidad y permanencia, reside oficialmente en el Palacio de la Zarzuela y utiliza el Palacio Real de Madrid para los actos solemnes de Estado.",
            "Conforme al artículo 62, al Rey le corresponde sancionar y promulgar las leyes en el plazo de quince días, convocar y disolver las Cortes Generales, proponer al candidato a Presidente del Gobierno tras consultar a los grupos parlamentarios y nombrar a los ministros a propuesta del Presidente.",
            "La persona del Rey es inviolable y no está sujeta a responsabilidad, pero todos sus actos oficiales deben ser refrendados por el Presidente del Gobierno, los ministros competentes o el Presidente del Congreso, quienes asumen la responsabilidad de los mismos.",
            "Según el artículo 57, la Corona es hereditaria y quien está llamado a suceder en el trono ostenta el título de Príncipe o Princesa de Asturias (actualmente la Princesa Leonor), prestando juramento ante las Cortes Generales al alcanzar la mayoría de edad.",
            "Asimismo, en calidad de Jefe del Estado, el Rey ostenta el mando supremo de las Fuerzas Armadas, ejerce el Alto Patronazgo de las Reales Academias y asume la más alta representación internacional de España, especialmente con las naciones de su comunidad histórica."
        ],
        "comp_questions": [
            {
                "question": "¿Cuál es la diferencia entre el Palacio de la Zarzuela y el Palacio Real de Madrid?",
                "options": [
                    "El Palacio de la Zarzuela es la residencia oficial donde vive el Rey, y el Palacio Real se utiliza para actos solemnes de Estado",
                    "Ambos son sedes del Congreso de los Diputados",
                    "El Palacio de la Zarzuela es la sede del Tribunal Constitucional",
                    "El Palacio Real es la residencia del Presidente del Gobierno"
                ],
                "correctIndex": 0,
                "explanation": "El Rey reside en el Palacio de la Zarzuela y celebra las ceremonias de Estado en el Palacio Real."
            },
            {
                "question": "¿Por qué los actos oficiales del Rey requieren refrendo?",
                "options": [
                    "Porque el Rey no está sujeto a responsabilidad y la responsabilidad la asumen quienes refrendan sus actos",
                    "Porque el Rey solo puede firmar documentos en el extranjero",
                    "Porque el Senado debe votar cada carta real",
                    "Porque el refrendo es opcional en las leyes"
                ],
                "correctIndex": 0,
                "explanation": "Los actos del Rey carecen de validez sin refrendo, y de ellos responden las autoridades que los refrendan."
            },
            {
                "question": "¿Qué título ostenta la heredera de la Corona de España?",
                "options": ["Princesa de Asturias", "Condesa de Madrid", "Duquesa de las Cortes", "Regente del Reino"],
                "correctIndex": 0,
                "explanation": "El artículo 57.2 establece que el sucesor o sucesora ostenta la dignidad de Príncipe o Princesa de Asturias."
            }
        ]
    }

    cons_stem = "b1-monarquia-consolidation"
    consolidation = {
        "title": "Repaso y Simulacro: La Corona y la Jefatura del Estado",
        "goal": "Consolidar las funciones del Rey, el refrendo, la sucesión, la Princesa de Asturias y las sedes institucionales para el examen CCSE.",
        "grammar": "Consolidación de verbos y locuciones del Título II",
        "goals": [
            "Consolidate CCSE exam facts on King Felipe VI, the Zarzuela Palace, and the Royal Palace.",
            "Review the King's constitutional functions under Article 62 and the institution of 'refrendo'.",
            "Verify mastery of hereditary succession, the Princess of Asturias, and Armed Forces command.",
            "Practice 'ostentar', 'a propuesta de', 'carecer de validez', 'al + infinitivo', and 'en calidad de'."
        ],
        "exercises": [
            {
                "id": f"{cons_stem}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["ostentar", "to hold (an office or title)"],
                    ["el Palacio de la Zarzuela", "Zarzuela Palace (royal residence)"],
                    ["el refrendo", "countersignature, endorsement"],
                    ["inviolable", "inviolable"],
                    ["la Princesa de Asturias", "Princess of Asturias (heir)"],
                    ["prestar juramento", "to take an oath"],
                    ["el mando supremo", "supreme command"],
                    ["acreditar", "to accredit (ambassadors)"]
                ],
                "teaches": ["ostentar-y-representar"]
            },
            {
                "id": f"{cons_stem}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración emplea el verbo adecuado para indicar que Felipe VI ocupa la Jefatura del Estado?",
                "options": [
                    "El Rey Felipe VI ostenta la Jefatura del Estado español.",
                    "El Rey Felipe VI carece la Jefatura del Estado español.",
                    "El Rey Felipe VI acredita la Jefatura del Estado español."
                ],
                "correct": 0,
                "teaches": ["ostentar-y-representar"]
            },
            {
                "id": f"{cons_stem}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cómo se expresa constitucionalmente que el Presidente del Gobierno indica al Rey a qué ministros nombrar?",
                "options": [
                    "El Rey nombra a los ministros a propuesta del Presidente del Gobierno.",
                    "El Rey nombra a los ministros en contra del Presidente del Gobierno.",
                    "El Rey nombra a los ministros sin propuesta del Presidente."
                ],
                "correct": 0,
                "teaches": ["previa-propuesta-de"]
            },
            {
                "id": f"{cons_stem}.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué expresión jurídica indica que un acto del Rey sin refrendo es nulo?",
                "options": [
                    "Los actos del Rey carecerán de validez sin dicho refrendo.",
                    "Los actos del Rey contarán de validez sin refrendo.",
                    "Los actos del Rey ostentarán validez sin refrendo."
                ],
                "correct": 0,
                "teaches": ["carecer-de-validez-sin"]
            },
            {
                "id": f"{cons_stem}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura temporal expresa el momento en que la Princesa de Asturias jura la Constitución?",
                "options": [
                    "Presta juramento ante las Cortes Generales al alcanzar la mayoría de edad.",
                    "Presta juramento ante las Cortes Generales por alcanzando la mayoría de edad.",
                    "Presta juramento ante las Cortes Generales de alcanzar la mayoría de edad."
                ],
                "correct": 0,
                "teaches": ["al-cumplir-infinitivo"]
            },
            {
                "id": f"{cons_stem}.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Rey nombra y separa a los miembros del Gobierno, a ___ de su Presidente. (propuesta)",
                "answer": "propuesta",
                "teaches": ["previa-propuesta-de"],
                "english": "The King appoints and dismisses the members of the Government, at the proposal of its President."
            },
            {
                "id": f"{cons_stem}.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los actos oficiales del Rey ___ de validez si no están refrendados. (carecer)",
                "answer": "carecen",
                "teaches": ["carecer-de-validez-sin"],
                "english": "The official acts of the King lack validity if they are not countersigned."
            },
            {
                "id": f"{cons_stem}.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En ___ de Jefe del Estado, el Rey acredita a los embajadores de España. (calidad)",
                "answer": "calidad",
                "teaches": ["en-calidad-de"],
                "english": "In his capacity as Head of State, the King accredits Spain's ambassadors."
            },
            {
                "id": f"{cons_stem}.ex09",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Rey", "es", "el", "Jefe", "del", "Estado,", "símbolo", "de", "su", "unidad", "y", "permanencia."],
                "solution": ["El", "Rey", "es", "el", "Jefe", "del", "Estado,", "símbolo", "de", "su", "unidad", "y", "permanencia."],
                "english": "The King is the Head of State, symbol of its unity and permanence.",
                "teaches": ["ostentar-y-representar"]
            },
            {
                "id": f"{cons_stem}.ex10",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "El Rey celebra consultas con los grupos políticos con representación parlamentaria. [The King holds consultations with the political groups with parliamentary representation.]",
                    "A continuación, propone un candidato a la Presidencia del Gobierno a través del Presidente del Congreso. [Next, he proposes a candidate for Prime Minister through the President of Congress.]",
                    "Una vez investido por el Congreso, el Rey lo nombra oficialmente Presidente del Gobierno. [Once invested by Congress, the King officially appoints him Prime Minister.]"
                ],
                "solution": [0, 1, 2],
                "teaches": ["previa-propuesta-de"]
            },
            {
                "id": f"{cons_stem}.ex11",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Dónde reside oficialmente el Rey y dónde reside el Presidente del Gobierno?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "El Rey reside en el Palacio de la Zarzuela, mientras que el Presidente del Gobierno reside en el Palacio de la Moncloa.",
                    "Ambos residen en el Palacio Real de la plaza de Oriente.",
                    "El Rey reside en la Moncloa y el Presidente en la Zarzuela."
                ],
                "correct": 0,
                "teaches": ["ostentar-y-representar"]
            },
            {
                "id": f"{cons_stem}.ex12",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "Al Rey le corresponde sancionar y promulgar las leyes, convocar y disolver las Cortes Generales y ostentar el mando supremo de las Fuerzas Armadas.",
                "options": [
                    "It falls to the King to sanction and promulgate laws, convene and dissolve the Cortes Generales, and hold supreme command of the Armed Forces.",
                    "The King exercises executive power and writes the national budget.",
                    "The Royal Household is part of the Constitutional Court."
                ],
                "correct": 0,
                "teaches": ["previa-propuesta-de"]
            },
            {
                "id": f"{cons_stem}.ex13",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "La Princesa de Asturias, Leonor de Borbón, es la heredera de la Corona y prestó juramento ante las Cortes Generales al cumplir dieciocho años.",
                "options": [
                    "The Princess of Asturias, Leonor de Borbón, is the heir to the Crown and took an oath before the Cortes Generales upon turning eighteen.",
                    "The title of Princess of Asturias is given to the President of the Senate.",
                    "The Spanish monarchy is elective rather than hereditary."
                ],
                "correct": 0,
                "teaches": ["al-cumplir-infinitivo"]
            },
            {
                "id": f"{cons_stem}.ex14",
                "type": "dictation",
                "category": "listening",
                "sentence": "El Rey ostenta el mando supremo de las Fuerzas Armadas.",
                "teaches": ["en-calidad-de"],
                "english": "The King holds the supreme command of the Armed Forces."
            },
            {
                "id": f"{cons_stem}.ex15",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica qué es el refrendo y quién asume la responsabilidad de los actos del Rey. [Explain what the countersignature is and who assumes responsibility for the King's acts.]",
                        "answer": "Los actos del Rey son refrendados por el Presidente del Gobierno o los ministros competentes, quienes asumen la responsabilidad política y jurídica de los mismos."
                    }
                ],
                "teaches": ["carecer-de-validez-sin"]
            },
            {
                "id": f"{cons_stem}.ex16",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Indica quién es el actual Rey de España, quién es la heredera de la Corona y qué título ostenta. [State who the current King of Spain is, who the heir to the Crown is, and what title she holds.]",
                        "answer": "El actual Rey de España es Felipe VI y la heredera de la Corona es su hija Leonor de Borbón, quien ostenta el título de Princesa de Asturias."
                    }
                ],
                "teaches": ["al-cumplir-infinitivo"]
            },
            {
                "id": f"{cons_stem}.ex17",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Resume las funciones del Rey en las relaciones internacionales y en el ámbito cultural. [Summarise the King's functions in international relations and in the cultural sphere.]",
                        "answer": "El Rey asume la más alta representación internacional de España, acredita a los embajadores y ejerce el Alto Patronazgo de las Reales Academias."
                    }
                ],
                "teaches": ["en-calidad-de"]
            },
            {
                "id": f"{cons_stem}.ex18",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Para qué se utiliza el Palacio Real de Madrid si los Reyes viven en la Zarzuela?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "Se utiliza para los actos solemnes de Estado, recepciones oficiales y entrega de cartas credenciales.",
                    "Se utiliza como vivienda privada de los diputados y senadores.",
                    "Se utiliza únicamente como archivo cerrado al público."
                ],
                "correct": 0,
                "teaches": ["ostentar-y-representar"]
            }
        ]
    }

    emit_unit("monarquia", "b1-ccse-monarquia", "La Corona", 2, lessons, comb, consolidation)


def build_unit_3():
    lessons = [
        {
            "num": "01",
            "story_suffix": "congreso",
            "title": "El sistema bicameral y el Congreso de los Diputados",
            "theme": "Las Cortes Generales",
            "goal": "Comprender la composición bicameral de las Cortes Generales y la elección de los 350 diputados del Congreso.",
            "grammar_short": "componerse de y dividirse en",
            "grammar_slug": "componerse-de-y-dividirse-en",
            "grammar_title": "Verbos de estructura institucional: «componerse de» e «integrarse por»",
            "location": "Madrid, carrera de San Jerónimo",
            "words": [
                {"lemma": "las Cortes Generales", "translation": "Cortes Generales (Spanish Parliament)", "pos": "expression"},
                {"lemma": "bicameral", "translation": "bicameral (two-chamber)", "pos": "adjective"},
                {"lemma": "el Congreso de los Diputados", "translation": "Congress of Deputies (Lower House)", "pos": "expression"},
                {"lemma": "el escaño", "translation": "parliamentary seat", "pos": "noun"},
                {"lemma": "la circunscripción", "translation": "electoral constituency / district", "pos": "noun"},
                {"lemma": "la legislatura", "translation": "parliamentary term (4 years)", "pos": "noun"},
                {"lemma": "el sufragio universal", "translation": "universal suffrage", "pos": "expression"},
                {"lemma": "la Cámara Baja", "translation": "Lower House", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "Para describir cómo está formado un órgano parlamentario, el español constitucional emplea el verbo pronominal *componerse de* (*el Congreso se compone de 350 diputados*) o el participio *estar formado / integrado por* (*las Cortes están formadas por el Congreso y el Senado*)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "Las Cortes Generales están formadas por el Congreso de los Diputados y el Senado.", "english": "The Cortes Generales are formed by the Congress of Deputies and the Senate."},
                        {"spanish": "El Congreso de los Diputados se compone actualmente de 350 diputados elegidos cada cuatro años.", "english": "The Congress of Deputies is currently composed of 350 deputies elected every four years."},
                        {"spanish": "El mandato de los diputados termina cuatro años después de su elección o el día de la disolución de la Cámara.", "english": "The deputies' term ends four years after their election or on the day the Chamber is dissolved."},
                        {"spanish": "En las elecciones al Congreso, la circunscripción electoral es la provincia.", "english": "In elections to Congress, the electoral constituency is the province."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda la preposición: *componerse DE* (*se compone de 350 miembros*) frente a *estar formado POR* (*está formado por dos cámaras*)."
                }
            ],
            "story_summary": "Title III of the Constitution establishes the Cortes Generales as Spain's bicameral parliament representing the Spanish people, with the Congress of Deputies (Lower House) composed of 350 deputies elected every 4 years by universal proportional suffrage.",
            "story_paragraphs": [
                "En el corazón de Madrid, en el Palacio de las Cortes de la carrera de San Jerónimo, flanqueado por sus dos célebres leones de bronce, se reúne el Congreso de los Diputados.",
                "El artículo 66 de la Constitución establece que las Cortes Generales representan al pueblo español y están formadas por dos cámaras: el Congreso de los Diputados (llamado también Cámara Baja) y el Senado (la Cámara Alta).",
                "Aunque la Constitución señala que el Congreso puede tener entre 300 y 400 miembros, la Ley Orgánica del Régimen Electoral General fija su número exacto en 350 diputados.",
                "Los diputados son elegidos cada cuatro años mediante sufragio universal, libre, igual, directo y secreto, siguiendo criterios de representación proporcional.",
                "En estas elecciones la circunscripción electoral es la provincia: a cada una de las cincuenta provincias le corresponde un mínimo inicial de dos diputados (y uno a Ceuta y uno a Melilla), repartiéndose los demás escaños en proporción a su población."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué dos cámaras forman las Cortes Generales de España?",
                    "options": ["El Congreso de los Diputados y el Senado", "El Consejo de Ministros y el Tribunal Supremo", "La Asamblea Municipal y la Diputación", "El Consejo de Estado y el Defensor del Pueblo"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 66.1 de la Constitución, las Cortes Generales están formadas por el Congreso de los Diputados y el Senado."
                },
                {
                    "question": "¿Cuántos diputados componen actualmente el Congreso de los Diputados?",
                    "options": ["350 diputados", "169 diputados", "500 diputados", "100 diputados"],
                    "correctIndex": 0,
                    "explanation": "El Congreso de los Diputados está compuesto por 350 diputados elegidos por sufragio universal."
                },
                {
                    "question": "¿Cuál es la duración ordinaria de una legislatura en España?",
                    "options": ["Cuatro años", "Seis años", "Cinco años", "Tres años"],
                    "correctIndex": 0,
                    "explanation": "Tanto los diputados como los senadores son elegidos por un mandato de cuatro años."
                }
            ],
            "goals": [
                "Identify the Cortes Generales as Spain's bicameral parliament formed by the Congress of Deputies and the Senate.",
                "State that the Congress of Deputies consists of 350 deputies elected for a 4-year term.",
                "Recognize the province as the electoral constituency for general elections.",
                "Use 'componerse de' and 'estar formado por' to describe parliamentary composition."
            ],
            "mc1": {
                "q": "¿Qué institución representa al pueblo español y está formada por el Congreso de los Diputados y el Senado?",
                "opts": ["Las Cortes Generales.", "El Consejo General del Poder Judicial.", "El Consejo de Estado."]
            },
            "mc2": {
                "q": "¿Cuántos diputados integran el Congreso de los Diputados en España?",
                "opts": ["350 diputados.", "250 diputados.", "450 diputados."]
            },
            "fb": {
                "sentence": "El Congreso de los Diputados se ___ de trescientos cincuenta diputados elegidos por sufragio universal. (componer)",
                "answer": "compone",
                "english": "The Congress of Deputies is composed of 350 deputies elected by universal suffrage."
            },
            "mc3": {
                "q": "¿Cuál es la circunscripción electoral en las elecciones generales al Congreso y al Senado?",
                "opts": ["La provincia (además de las ciudades autónomas de Ceuta y Melilla).", "El barrio municipal.", "El partido judicial."]
            },
            "sb": {
                "words": ["Las", "Cortes", "Generales", "están", "formadas", "por", "el", "Congreso", "y", "el", "Senado."],
                "english": "The Cortes Generales are formed by the Congress and the Senate."
            },
            "dlg": {
                "s1": "Elena", "s2": "Tomás",
                "q": "¿Cada cuántos años se celebran elecciones generales para renovar el Congreso de los Diputados?",
                "opts": [
                    "Cada cuatro años, salvo que se disuelvan las cámaras anticipadamente.",
                    "Cada seis años, coincidiendo con la reforma constitucional.",
                    "Cada dos años en todas las provincias."
                ]
            },
            "listen": {
                "sentence": "El Congreso de los Diputados es la Cámara Baja de las Cortes Generales y se compone de trescientos cincuenta diputados.",
                "opts": [
                    "The Congress of Deputies is the Lower House of the Cortes Generales and is composed of 350 deputies.",
                    "The Congress of Deputies is appointed by the Supreme Court for nine years.",
                    "Spain has a unicameral parliament without a Senate."
                ]
            }
        },
        {
            "num": "02",
            "story_suffix": "senado",
            "title": "El Senado: la cámara de representación territorial",
            "theme": "Las Cortes Generales",
            "goal": "Aprender el carácter del Senado como cámara de representación territorial y su doble vía de elección y designación.",
            "grammar_short": "tanto... como... correlativos",
            "grammar_slug": "tanto-como-correlativos",
            "grammar_title": "Coordinación correlativa: «tanto... como...»",
            "location": "Madrid, plaza de la Marina Española",
            "words": [
                {"lemma": "el Senado", "translation": "Senate (Upper House)", "pos": "noun"},
                {"lemma": "la Cámara Alta", "translation": "Upper House", "pos": "expression"},
                {"lemma": "la representación territorial", "translation": "territorial representation", "pos": "expression"},
                {"lemma": "designar", "translation": "to designate, appoint", "pos": "verb"},
                {"lemma": "la enmienda", "translation": "amendment (to a bill)", "pos": "noun"},
                {"lemma": "el veto", "translation": "veto", "pos": "noun"},
                {"lemma": "la asamblea legislativa", "translation": "legislative assembly (regional parliament)", "pos": "expression"},
                {"lemma": "el cabildo insular", "translation": "island council (Canary Islands)", "pos": "expression"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "La estructura correlativa *tanto... como...* (both... and...) permite unir en un mismo plano dos orígenes o funciones complementarias, como los dos tipos de senadores que integran la Cámara Alta."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Senado está integrado tanto por senadores elegidos en las provincias como por senadores designados por las comunidades autónomas.", "english": "The Senate is made up both of senators elected in the provinces and of senators designated by the autonomous communities."},
                        {"spanish": "Tanto el Congreso como el Senado participan en la elaboración de las leyes y en el control del Gobierno.", "english": "Both the Congress and the Senate participate in making laws and overseeing the Government."},
                        {"spanish": "En los archipiélagos eligen senadores tanto las islas mayores como las islas menores.", "english": "In the archipelagos, both the larger islands and the smaller islands elect senators."},
                        {"spanish": "El Senado puede tanto introducir enmiendas a un proyecto de ley como oponer su veto por mayoría absoluta.", "english": "The Senate can both introduce amendments to a bill and oppose its veto by an absolute majority."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Si hay preposición, debe repetirse tras *tanto* y tras *como*: *integrado tanto POR senadores provinciales como POR senadores autonómicos*."
                }
            ],
            "story_summary": "Article 69 defines the Senate (Upper House) as Spain's chamber of territorial representation, combining directly elected provincial/island senators with senators designated by the parliaments of the Autonomous Communities.",
            "story_paragraphs": [
                "Situado en el Palacio de la plaza de la Marina Española en Madrid, el Senado es la Cámara Alta de las Cortes Generales.",
                "El artículo 69.1 de la Constitución ofrece una definición que aparece con mucha frecuencia en las pruebas CCSE: «El Senado es la Cámara de representación territorial».",
                "Por esta razón, su composición combina dos vías distintas: por un lado, los votantes de cada provincia peninsular eligen directamente a cuatro senadores (mientras que las islas mayores —Gran Canaria, Mallorca y Tenerife— eligen tres, las islas menores uno, y Ceuta y Melilla eligen dos cada una).",
                "Por otro lado, la asamblea legislativa de cada comunidad autónoma designa a un senador fijo y a otro más por cada millón de habitantes de su respectivo territorio.",
                "En el proceso legislativo, todo texto aprobado por el Congreso pasa al Senado, que dispone de dos meses (o veinte días en proyectos urgentes) para introducir enmiendas o para oponer su veto por mayoría absoluta, si bien el Congreso tiene la última palabra para levantar el veto o aceptar las enmiendas."
            ],
            "comp_questions": [
                {
                    "question": "¿Cómo define el artículo 69.1 de la Constitución al Senado?",
                    "options": [
                        "Es la Cámara de representación territorial",
                        "Es el órgano de gobierno de los jueces",
                        "Es la cámara única que elige al Presidente del Gobierno",
                        "Es el tribunal que juzga los recursos de amparo"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 69.1 dispone textualmente: «El Senado es la Cámara de representación territorial»."
                },
                {
                    "question": "¿Cuántos senadores eligen directamente los ciudadanos en cada provincia peninsular?",
                    "options": ["Cuatro senadores por provincia", "Diez senadores por provincia", "Un solo senador por provincia", "Treinta y cinco senadores por provincia"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 69.2, en cada provincia se eligen cuatro senadores por sufragio universal."
                },
                {
                    "question": "Además de los senadores elegidos en las provincias e islas, ¿quién designa al resto de los senadores?",
                    "options": ["Las asambleas legislativas (parlamentos) de las comunidades autónomas", "Los alcaldes de los municipios", "El Consejo de Estado", "Los embajadores"],
                    "correctIndex": 0,
                    "explanation": "Las comunidades autónomas designan un senador y otro más por cada millón de habitantes."
                }
            ],
            "goals": [
                "Identify the Senate (Upper House) as the chamber of territorial representation (Article 69).",
                "Explain the dual origin of senators: 4 elected per peninsular province (plus islands, Ceuta, and Melilla) and regional senators designated by Autonomous Communities.",
                "Describe how the Senate reviews, amends, or vetoes bills passed by the Congress of Deputies.",
                "Use correlative 'tanto... como...' to link parallel parliamentary functions."
            ],
            "mc1": {
                "q": "¿Cuál de las dos cámaras de las Cortes Generales es la Cámara de representación territorial?",
                "opts": ["El Senado.", "El Congreso de los Diputados.", "El Consejo de Ministros."]
            },
            "mc2": {
                "q": "¿Cuántos senadores se eligen por sufragio directo en cada provincia peninsular?",
                "opts": ["Cuatro senadores.", "Dos senadores.", "Ocho senadores."]
            },
            "fb": {
                "sentence": "El Senado está compuesto ___ por senadores provinciales como por senadores designados por las comunidades autónomas. (tanto)",
                "answer": "tanto",
                "english": "The Senate is composed both of provincial senators and of senators designated by the autonomous communities."
            },
            "mc3": {
                "q": "¿Qué cámara tiene la última palabra para levantar un veto del Senado durante la aprobación de una ley?",
                "opts": ["El Congreso de los Diputados.", "El Tribunal de Cuentas.", "El Parlamento Europeo."]
            },
            "sb": {
                "words": ["El", "Senado", "es", "la", "Cámara", "de", "representación", "territorial."],
                "english": "The Senate is the Chamber of territorial representation."
            },
            "dlg": {
                "s1": "Adrián", "s2": "Paula",
                "q": "¿Cuántos senadores eligen los ciudadanos de Ceuta y de Melilla?",
                "opts": [
                    "Las poblaciones de Ceuta y de Melilla eligen cada una de ellas dos senadores.",
                    "No eligen ningún senador ni ningún diputado.",
                    "Eligen diez senadores cada una."
                ]
            },
            "listen": {
                "sentence": "El Senado es la Cámara Alta de las Cortes Generales y actúa como cámara de representación territorial.",
                "opts": [
                    "The Senate is the Upper House of the Cortes Generales and acts as the chamber of territorial representation.",
                    "The Senate is the Lower House and has 350 members.",
                    "Senators are appointed by the Constitutional Court for nine years."
                ]
            }
        },
        {
            "num": "03",
            "story_suffix": "investidura",
            "title": "La investidura y el control parlamentario al Gobierno",
            "theme": "Las Cortes Generales",
            "goal": "Comprender la sesión de investidura en el Congreso, la cuestión de confianza y la moción de censura constructiva.",
            "grammar_short": "en caso de que + subjuntivo",
            "grammar_slug": "en-caso-de-que-subjuntivo",
            "grammar_title": "Condicionales jurídicas: «en caso de que + subjuntivo»",
            "location": "Madrid, Congreso de los Diputados",
            "words": [
                {"lemma": "la investidura", "translation": "investiture (vote of confidence in a new PM)", "pos": "noun"},
                {"lemma": "la mayoría absoluta", "translation": "absolute majority (more than half of all members)", "pos": "expression"},
                {"lemma": "la mayoría simple", "translation": "simple majority (more yes than no votes)", "pos": "expression"},
                {"lemma": "la moción de censura", "translation": "motion of no confidence / censure", "pos": "expression"},
                {"lemma": "la cuestión de confianza", "translation": "question of confidence", "pos": "expression"},
                {"lemma": "la interpelación", "translation": "interpellation, parliamentary questioning", "pos": "noun"},
                {"lemma": "otorgar", "translation": "to grant (confidence)", "pos": "verb"},
                {"lemma": "controlar", "translation": "to oversee, check (government action)", "pos": "verb"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "Los reglamentos parlamentarios prevén qué sucede si no se alcanza una votación determinada mediante la locución *en caso de que* seguida siempre de subjuntivo (*en caso de que no alcance la mayoría absoluta*)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "En caso de que el candidato no alcance la mayoría absoluta en primera votación, se celebra una segunda votación cuarenta y ocho horas después.", "english": "In the event that the candidate does not achieve an absolute majority in the first ballot, a second vote is held forty-eight hours later."},
                        {"spanish": "En caso de que ningún candidato obtenga la confianza en el plazo de dos meses, el Rey disuelve ambas cámaras.", "english": "In the event that no candidate obtains confidence within two months, the King dissolves both chambers."},
                        {"spanish": "El Gobierno debe presentar su dimisión al Rey en caso de que el Congreso adopte una moción de censura.", "english": "The Government must submit its resignation to the King in the event that Congress adopts a motion of no confidence."},
                        {"spanish": "La confianza se entiende otorgada en caso de que vote a favor la mayoría simple de los diputados.", "english": "Confidence is deemed granted in the event that a simple majority of deputies votes in favor."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "*En caso de que* exige siempre subjuntivo (*alcance*, *obtenga*, *adopte*), nunca indicativo."
                }
            ],
            "story_summary": "How the Congress of Deputies elects the Prime Minister in the investiture debate (176 votes for absolute majority on the first ballot, or simple majority 48 hours later) and oversees the Government through questions, confidence votes, and constructive motions of no confidence.",
            "story_paragraphs": [
                "En un sistema parlamentario como el español, los ciudadanos no eligen directamente en una urna separada al Presidente del Gobierno, sino que eligen a los diputados y senadores de las Cortes Generales.",
                "Es exclusivamente el Congreso de los Diputados —y no el Senado— la cámara encargada de otorgar o retirar la confianza al Presidente del Gobierno mediante el debate y votación de investidura regulado en el artículo 99.",
                "En la primera votación de investidura, el candidato necesita el voto favorable de la mayoría absoluta del Congreso (al menos 176 de los 350 diputados). En caso de que no alcance dicha mayoría, se celebra una nueva votación cuarenta y ocho horas después, en la que basta la mayoría simple (más votos a favor que en contra).",
                "Durante toda la legislatura, las Cortes Generales controlan la acción del Gobierno mediante preguntas semanales, interpelaciones y comisiones de investigación.",
                "Además, existen dos mecanismos solemnes ante el Congreso: la cuestión de confianza (planteada por el propio Presidente del Gobierno, que se aprueba por mayoría simple) y la moción de censura constructiva (propuesta al menos por la décima parte de los diputados, que debe incluir un candidato alternativo a la Presidencia y exige mayoría absoluta para triunfar)."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué cámara de las Cortes Generales vota la investidura del Presidente del Gobierno?",
                    "options": ["Exclusivamente el Congreso de los Diputados", "Únicamente el Senado", "El Tribunal Constitucional", "Las Diputaciones Provinciales"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 99, el candidato expone su programa ante el Congreso de los Diputados y solicita la confianza de esta Cámara."
                },
                {
                    "question": "¿Qué mayoría necesita el candidato a Presidente del Gobierno en la primera votación de investidura?",
                    "options": [
                        "Mayoría absoluta (al menos 176 diputados); si no la alcanza, mayoría simple 48 horas después",
                        "Unanimidad de los 350 diputados en primera vuelta",
                        "Solo diez votos a favor",
                        "Tres quintos del Senado"
                    ],
                    "correctIndex": 0,
                    "explanation": "En primera votación se requiere mayoría absoluta (176 escaños) y, 48 horas después, basta mayoría simple."
                },
                {
                    "question": "¿Por qué se dice que la moción de censura en España es «constructiva»?",
                    "options": [
                        "Porque debe ser propuesta al menos por la décima parte de los diputados e incluir obligatoriamente un candidato alternativo a la Presidencia",
                        "Porque sirve únicamente para construir edificios públicos",
                        "Porque la presenta el propio Presidente del Gobierno",
                        "Porque no requiere mayoría absoluta"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 113 exige que la moción de censura incluya un candidato alternativo; si se aprueba por mayoría absoluta, dicho candidato queda investido automáticamente."
                }
            ],
            "goals": [
                "State that the Congress of Deputies invests the Prime Minister (Article 99).",
                "Distinguish the absolute majority required in the first investiture vote (176 seats) from the simple majority 48 hours later.",
                "Explain the difference between a question of confidence and a constructive motion of no confidence.",
                "Use 'en caso de que + subjunctive' for constitutional contingencies."
            ],
            "mc1": {
                "q": "¿Quién elige y otorga la confianza parlamentaria al Presidente del Gobierno en España?",
                "opts": ["El Congreso de los Diputados.", "El Senado en solitario.", "El Consejo General del Poder Judicial."]
            },
            "mc2": {
                "q": "¿Cuántos votos favorables exige la mayoría absoluta del Congreso de los Diputados en la primera votación de investidura?",
                "opts": ["Al menos 176 diputados (la mitad más uno de los 350).", "Al menos 100 diputados.", "Los 350 diputados por unanimidad."]
            },
            "fb": {
                "sentence": "En caso de que el candidato no ___ la mayoría absoluta, se procede a una segunda votación cuarenta y ocho horas después. (alcanzar, presente de subjuntivo)",
                "answer": "alcance",
                "english": "In the event that the candidate does not achieve an absolute majority, a second vote is held forty-eight hours later."
            },
            "mc3": {
                "q": "¿Qué requisito exige el artículo 113 para que una moción de censura sea admitida y aprobada en el Congreso?",
                "opts": [
                    "Ser propuesta al menos por la décima parte de los diputados, incluir un candidato alternativo y obtener mayoría absoluta.",
                    "Ser firmada por un solo senador y obtener mayoría simple.",
                    "Ser propuesta por el Tribunal de Cuentas."
                ]
            },
            "sb": {
                "words": ["Las", "Cortes", "Generales", "controlan", "la", "acción", "del", "Gobierno."],
                "english": "The Cortes Generales oversee the action of the Government."
            },
            "dlg": {
                "s1": "Laura", "s2": "Miguel",
                "q": "¿Qué pasa si transcurren dos meses desde la primera votación de investidura y ningún candidato obtiene la confianza del Congreso?",
                "opts": [
                    "El Rey disuelve ambas cámaras y convoca nuevas elecciones con el refrendo del Presidente del Congreso.",
                    "El Presidente del Senado se convierte en Presidente del Gobierno durante cuatro años.",
                    "Se suspende la Constitución indefinidamente."
                ]
            },
            "listen": {
                "sentence": "El candidato a la Presidencia del Gobierno necesita mayoría absoluta en primera votación o mayoría simple cuarenta y ocho horas después.",
                "opts": [
                    "The candidate for Prime Minister needs an absolute majority on the first ballot or a simple majority forty-eight hours later.",
                    "The Prime Minister is elected directly by the Senate every six years.",
                    "A motion of no confidence does not require an alternative candidate."
                ]
            }
        },
        {
            "num": "04",
            "story_suffix": "defensor",
            "title": "Prerrogativas parlamentarias y el Defensor del Pueblo",
            "theme": "Las Cortes Generales",
            "goal": "Conocer la inviolabilidad e inmunidad de los parlamentarios, el Tribunal de Cuentas y la figura del Defensor del Pueblo.",
            "grammar_short": "encargado de + infinitivo",
            "grammar_slug": "encargado-de-infinitivo",
            "grammar_title": "Definir órganos comisionados: «encargado de» y «designado por»",
            "location": "Madrid",
            "words": [
                {"lemma": "el Defensor del Pueblo", "translation": "Ombudsman (Defender of the People)", "pos": "expression"},
                {"lemma": "el alto comisionado", "translation": "high commissioner", "pos": "expression"},
                {"lemma": "la inmunidad", "translation": "immunity (from arrest/prosecution)", "pos": "noun"},
                {"lemma": "el mandato", "translation": "mandate, term of office", "pos": "noun"},
                {"lemma": "el Tribunal de Cuentas", "translation": "Court of Auditors", "pos": "expression"},
                {"lemma": "la queja", "translation": "complaint, grievance", "pos": "noun"},
                {"lemma": "supervisar", "translation": "to supervise, monitor", "pos": "verb"},
                {"lemma": "fiscalizar", "translation": "to audit, inspect (public accounts)", "pos": "verb"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "En las preguntas del examen CCSE que piden identificar qué institución protege los derechos ciudadanos o audita el gasto público, son clave los participios *designado por* (appointed by) y *encargado de + infinitivo* (in charge of / responsible for)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "El Defensor del Pueblo es el alto comisionado de las Cortes Generales encargado de defender los derechos fundamentales.", "english": "The Ombudsman is the high commissioner of the Cortes Generales in charge of defending fundamental rights."},
                        {"spanish": "El Defensor del Pueblo es designado por las Cortes Generales por un período de cinco años.", "english": "The Ombudsman is appointed by the Cortes Generales for a period of five years."},
                        {"spanish": "El Tribunal de Cuentas es el supremo órgano fiscalizador encargado de controlar las cuentas y la gestión económica del Estado.", "english": "The Court of Auditors is the supreme auditing body in charge of checking the accounts and economic management of the State."},
                        {"spanish": "Cualquier ciudadano puede presentar una queja gratuita ante el Defensor del Pueblo.", "english": "Any citizen may file a free complaint with the Ombudsman."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "No confundas *el Defensor del Pueblo* (protege derechos ciudadanos y supervisa a la Administración) con *el Tribunal de Cuentas* (audita las cuentas económicas del sector público); ambos dependen de las Cortes Generales."
                }
            ],
            "story_summary": "How the Constitution protects parliamentary freedom through inviolability and immunity (Article 71), and how the Cortes Generales appoint two vital oversight institutions: the Ombudsman (Defensor del Pueblo, Article 54) and the Court of Auditors (Tribunal de Cuentas, Article 136).",
            "story_paragraphs": [
                "Para que los representantes del pueblo puedan debatir y controlar al Gobierno sin presiones, el artículo 71 de la Constitución protege a los diputados y senadores con dos garantías: la inviolabilidad por las opiniones manifestadas en el ejercicio de sus funciones y la inmunidad durante el período de su mandato, siendo el Tribunal Supremo el único competente para juzgarlos.",
                "Además de legislar, las Cortes Generales cuentan con dos grandes instituciones auxiliares previstas en la Constitución que aparecen reiteradamente en los exámenes CCSE: el Defensor del Pueblo y el Tribunal de Cuentas.",
                "Regulado en el artículo 54, el Defensor del Pueblo es el alto comisionado de las Cortes Generales, designado por estas para un mandato de cinco años con la misión de defender los derechos comprendidos en el Título I de la Constitución.",
                "Para cumplir su tarea, el Defensor del Pueblo supervisa la actividad de todas las Administraciones Públicas (estatales, autonómicas y municipales), recibe las quejas gratuitas de cualquier persona —española o extranjera, sin importar su edad— y presenta un informe anual a las Cortes Generales.",
                "Por su parte, el artículo 136 regula el Tribunal de Cuentas, que depende directamente de las Cortes Generales y actúa como el supremo órgano fiscalizador de las cuentas y de la gestión económica del Estado y del sector público."
            ],
            "comp_questions": [
                {
                    "question": "¿Qué institución es el alto comisionado de las Cortes Generales encargado de defender los derechos del Título I y supervisar a la Administración?",
                    "options": ["El Defensor del Pueblo", "El Consejo de Estado", "El Banco de España", "La Abogacía del Estado"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 54, el Defensor del Pueblo es el alto comisionado de las Cortes Generales para la defensa de los derechos del Título I."
                },
                {
                    "question": "¿De qué órgano depende directamente el Defensor del Pueblo y a quién da cuenta de su actividad?",
                    "options": ["De las Cortes Generales", "Del Ministerio del Interior", "De los Ayuntamientos", "De la Presidencia de la Comunidad"],
                    "correctIndex": 0,
                    "explanation": "El Defensor del Pueblo es designado por las Cortes Generales y les rinde cuentas anualmente."
                },
                {
                    "question": "¿Cuál es el supremo órgano fiscalizador de las cuentas y de la gestión económica del Estado según el artículo 136?",
                    "options": ["El Tribunal de Cuentas", "El Tribunal Constitucional", "El Senado", "La Agencia Tributaria"],
                    "correctIndex": 0,
                    "explanation": "El artículo 136 define al Tribunal de Cuentas como el supremo órgano fiscalizador de las cuentas del Estado, dependiente de las Cortes Generales."
                }
            ],
            "goals": [
                "Identify the 'Defensor del Pueblo' (Ombudsman) as the High Commissioner of the Cortes Generales who defends Title I rights (Article 54).",
                "Identify the 'Tribunal de Cuentas' as the supreme auditing body of the State's public accounts (Article 136).",
                "Explain parliamentary inviolability and immunity under Article 71.",
                "Use 'encargado de + infinitivo' and 'designado por' to describe institutional mandates."
            ],
            "mc1": {
                "q": "¿Cuál es la institución designada por las Cortes Generales para defender los derechos fundamentales de los ciudadanos y supervisar la actividad de la Administración?",
                "opts": ["El Defensor del Pueblo.", "El Consejo de Ministros.", "El Consejo de Estado."]
            },
            "mc2": {
                "q": "¿Cuál es el supremo órgano fiscalizador de las cuentas y de la gestión económica del Estado y del sector público?",
                "opts": ["El Tribunal de Cuentas.", "El Tribunal Supremo.", "El Defensor del Pueblo."]
            },
            "fb": {
                "sentence": "El Defensor del Pueblo es el alto comisionado de las Cortes Generales ___ de defender los derechos del Título I. (encargado)",
                "answer": "encargado",
                "english": "The Ombudsman is the high commissioner of the Cortes Generales in charge of defending Title I rights."
            },
            "mc3": {
                "q": "¿Ante qué tribunal son aforados los diputados y senadores durante su mandato según el artículo 71.3?",
                "opts": ["Ante la Sala de lo Penal del Tribunal Supremo.", "Ante un juzgado municipal de paz.", "Ante el Tribunal de Cuentas."]
            },
            "sb": {
                "words": ["El", "Defensor", "del", "Pueblo", "es", "designado", "por", "las", "Cortes", "Generales."],
                "english": "The Ombudsman is appointed by the Cortes Generales."
            },
            "dlg": {
                "s1": "Valeria", "s2": "Diego",
                "q": "¿Cuánto cuesta presentar una queja ante el Defensor del Pueblo cuando una administración vulnera tus derechos?",
                "opts": [
                    "Es totalmente gratuito para cualquier ciudadano y no requiere abogado ni procurador.",
                    "Cuesta quinientos euros de tasas judiciales obligatorias.",
                    "Solo pueden presentar quejas los diputados y senadores."
                ]
            },
            "listen": {
                "sentence": "El Defensor del Pueblo es el alto comisionado de las Cortes Generales para la defensa de los derechos fundamentales y las libertades públicas.",
                "opts": [
                    "The Ombudsman is the high commissioner of the Cortes Generales for the defense of fundamental rights and public liberties.",
                    "The Court of Auditors is appointed by the mayors to collect local taxes.",
                    "Deputies and senators do not enjoy parliamentary inviolability."
                ]
            }
        },
        {
            "num": "05",
            "story_suffix": "leyes",
            "title": "La elaboración de las leyes y los Presupuestos Generales",
            "theme": "Las Cortes Generales",
            "goal": "Diferenciar proyectos de ley, proposiciones de ley, iniciativa legislativa popular (500.000 firmas), leyes orgánicas y Presupuestos Generales del Estado.",
            "grammar_short": "mediante + sustantivo",
            "grammar_slug": "mediante-y-a-traves-de",
            "grammar_title": "Instrumentos normativos: uso de «mediante» en lenguaje legal",
            "location": "Madrid, Cortes Generales",
            "words": [
                {"lemma": "el proyecto de ley", "translation": "government bill (submitted by the Cabinet)", "pos": "expression"},
                {"lemma": "la proposición de ley", "translation": "parliamentary or popular bill", "pos": "expression"},
                {"lemma": "la iniciativa legislativa popular", "translation": "popular legislative initiative (500,000 signatures)", "pos": "expression"},
                {"lemma": "la ley orgánica", "translation": "organic law (requires absolute majority)", "pos": "expression"},
                {"lemma": "los Presupuestos Generales del Estado", "translation": "General State Budget", "pos": "expression"},
                {"lemma": "la firma acreditada", "translation": "certified signature", "pos": "expression"},
                {"lemma": "la potestad legislativa", "translation": "legislative power", "pos": "expression"},
                {"lemma": "aprobar", "translation": "to pass, approve (a law or budget)", "pos": "verb"}
            ],
            "grammar_sections": [
                {
                    "type": "text",
                    "content": "La preposición *mediante* (by means of / through) se utiliza en el español jurídico para especificar qué tipo de norma o procedimiento legal exige la Constitución para regular una materia (*mediante ley orgánica*, *mediante quinientas mil firmas*)."
                },
                {
                    "type": "examples",
                    "items": [
                        {"spanish": "Los derechos fundamentales y los Estatutos de Autonomía se aprueban mediante ley orgánica.", "english": "Fundamental rights and Statutes of Autonomy are passed by means of an organic law."},
                        {"spanish": "Los ciudadanos pueden presentar una proposición de ley mediante al menos quinientas mil firmas acreditadas.", "english": "Citizens may submit a legislative bill by means of at least 500,000 certified signatures."},
                        {"spanish": "El Gobierno ejerce la iniciativa legislativa mediante la presentación de proyectos de ley.", "english": "The Government exercises legislative initiative through the submission of government bills."},
                        {"spanish": "Las Cortes Generales autorizan los ingresos y gastos anuales mediante la Ley de Presupuestos Generales del Estado.", "english": "The Cortes Generales authorize annual revenues and expenditures through the General State Budget Act."}
                    ]
                },
                {
                    "type": "tip",
                    "content": "Distingue la terminología oficial CCSE: si el texto nace del Gobierno se llama *proyecto de ley*; si nace del Congreso, del Senado, de una asamblea autonómica o de los ciudadanos se llama *proposición de ley*."
                }
            ],
            "story_summary": "How laws are born in Spain: the difference between Government bills ('proyectos de ley') and parliamentary/popular bills ('proposiciones de ley'), the 500,000 signatures required for a popular legislative initiative, organic laws (Article 81), and the General State Budget (Article 134).",
            "story_paragraphs": [
                "La primera gran función que el artículo 66.2 de la Constitución atribuye a las Cortes Generales es ejercer la potestad legislativa del Estado y aprobar sus Presupuestos.",
                "¿Quién tiene iniciativa para poner en marcha una nueva ley según el artículo 87? Cuando el texto lo envía el Gobierno tras aprobarlo en el Consejo de Ministros, recibe el nombre técnico de «proyecto de ley»; en cambio, cuando lo impulsan el Congreso, el Senado o los parlamentos autonómicos, se denomina «proposición de ley».",
                "La Constitución reconoce también la iniciativa legislativa popular (ILP): los ciudadanos pueden presentar una proposición de ley ante las Cortes Generales siempre que reúnan al menos 500.000 firmas acreditadas, quedando excluidas de esta vía las materias propias de ley orgánica, las tributarias, las de carácter internacional y la prerrogativa de gracia.",
                "Dentro de las leyes aprobadas por las Cortes, el artículo 81 destaca las «leyes orgánicas» —relativas al desarrollo de los derechos fundamentales, los Estatutos de Autonomía y el régimen electoral general—, cuya aprobación, modificación o derogación exige mayoría absoluta del Congreso en una votación final sobre el conjunto del proyecto.",
                "Finalmente, cada otoño el Gobierno elabora los Presupuestos Generales del Estado (artículo 134) y corresponde a las Cortes Generales su examen, enmienda y aprobación; si no se aprueban antes del primer día del nuevo ejercicio económico, se consideran automáticamente prorrogados los presupuestos del año anterior."
            ],
            "comp_questions": [
                {
                    "question": "¿Cuántas firmas acreditadas se exigen como mínimo para presentar una iniciativa legislativa popular en España?",
                    "options": ["Al menos 500.000 firmas acreditadas", "Al menos 10.000 firmas", "Al menos 5 millones de firmas", "Bastan 100 firmas ante un ayuntamiento"],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 87.3 de la Constitución, para la iniciativa legislativa popular se exigirán no menos de 500.000 firmas acreditadas."
                },
                {
                    "question": "¿Cómo se denomina la iniciativa de ley cuando la presenta el Gobierno al Congreso?",
                    "options": ["Proyecto de ley", "Proposición de ley", "Ordenanza municipal", "Sentencia judicial"],
                    "correctIndex": 0,
                    "explanation": "Los textos remitidos por el Gobierno se denominan proyectos de ley; los del Parlamento o ciudadanos, proposiciones de ley."
                },
                {
                    "question": "¿A quién corresponde elaborar y a quién aprobar los Presupuestos Generales del Estado según el artículo 134?",
                    "options": [
                        "Al Gobierno su elaboración y a las Cortes Generales su examen, enmienda y aprobación",
                        "Al Rey su elaboración y al Tribunal Supremo su aprobación",
                        "A los ayuntamientos su elaboración y al Defensor del Pueblo su aprobación",
                        "Al Banco Central Europeo tanto su elaboración como su aprobación"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 134.1 dispone: «Corresponde al Gobierno la elaboración de los Presupuestos Generales del Estado y a las Cortes Generales, su examen, enmienda y aprobación»."
                }
            ],
            "goals": [
                "Distinguish between a 'proyecto de ley' (from the Government) and a 'proposición de ley' (from Parliament, Autonomous Communities, or citizens).",
                "State that a popular legislative initiative requires at least 500,000 certified signatures (Article 87.3).",
                "Identify organic laws (requiring absolute majority in Congress) and explain how the General State Budget is drafted by the Government and approved by the Cortes.",
                "Use 'mediante' to specify legal instruments and requirements."
            ],
            "mc1": {
                "q": "¿Cuántas firmas de ciudadanos se necesitan como mínimo en España para presentar una iniciativa legislativa popular?",
                "opts": ["500.000 firmas acreditadas.", "50.000 firmas acreditadas.", "1.000.000 de firmas acreditadas."]
            },
            "mc2": {
                "q": "¿Qué institución elabora los Presupuestos Generales del Estado y qué institución los aprueba?",
                "opts": [
                    "El Gobierno los elabora y las Cortes Generales los examinan, enmiendan y aprueban.",
                    "Las Cortes los elaboran y el Tribunal Constitucional los aprueba.",
                    "El Consejo de Estado los elabora y el Rey los aprueba sin intervención parlamentaria."
                ]
            },
            "fb": {
                "sentence": "Los derechos fundamentales y los Estatutos de Autonomía se regulan ___ ley orgánica. (mediante)",
                "answer": "mediante",
                "english": "Fundamental rights and Statutes of Autonomy are regulated by means of an organic law."
            },
            "mc3": {
                "q": "¿Qué mayoría requiere el Congreso de los Diputados para aprobar o modificar una ley orgánica según el artículo 81?",
                "opts": ["Mayoría absoluta del Congreso.", "Mayoría simple de diez diputados.", "Sorteo entre los senadores."]
            },
            "sb": {
                "words": ["La", "iniciativa", "legislativa", "popular", "exige", "quinientas", "mil", "firmas", "acreditadas."],
                "english": "A popular legislative initiative requires five hundred thousand certified signatures."
            },
            "dlg": {
                "s1": "Sergio", "s2": "Natalia",
                "q": "¿Qué sucede si el 1 de enero aún no se han aprobado los nuevos Presupuestos Generales del Estado?",
                "opts": [
                    "Se consideran automáticamente prorrogados los Presupuestos del ejercicio anterior hasta la aprobación de los nuevos.",
                    "Se cierran todos los hospitales y colegios públicos del país.",
                    "Se disuelven inmediatamente los ayuntamientos."
                ]
            },
            "listen": {
                "sentence": "Corresponde al Gobierno la elaboración de los Presupuestos Generales del Estado y a las Cortes Generales su examen, enmienda y aprobación.",
                "opts": [
                    "It falls to the Government to draft the General State Budget and to the Cortes Generales to examine, amend, and approve it.",
                    "Popular legislative initiatives require only five thousand signatures.",
                    "Organic laws do not need to be voted on by the Congress of Deputies."
                ]
            }
        }
    ]

    comb = {
        "title": "Las Cortes Generales: Congreso y Senado",
        "summary": "Complete CCSE guide to Title III of the Spanish Constitution: the bicameral Cortes Generales, the 350-seat Congress of Deputies, the Senate as chamber of territorial representation, the investiture and oversight of the Government, the Ombudsman and Court of Auditors, and the legislative process (including the 500,000-signature popular initiative and General State Budget).",
        "paragraphs": [
            "Las Cortes Generales representan al pueblo español, ejercen la potestad legislativa, aprueban los Presupuestos y controlan al Gobierno; están formadas por dos cámaras elegidas cada cuatro años: el Congreso de los Diputados (Cámara Baja, con 350 diputados) y el Senado (Cámara Alta).",
            "El artículo 69 define al Senado como la Cámara de representación territorial, compuesta tanto por senadores elegidos directamente en las provincias, islas, Ceuta y Melilla como por senadores designados por las asambleas de las comunidades autónomas.",
            "Corresponde en exclusiva al Congreso de los Diputados votar la investidura del Presidente del Gobierno (por mayoría absoluta de 176 escaños en primera vuelta o mayoría simple 48 horas después), así como votar las cuestiones de confianza y las mociones de censura constructivas.",
            "Dependientes de las Cortes Generales actúan dos órganos clave: el Defensor del Pueblo (alto comisionado encargado de defender los derechos fundamentales del Título I y supervisar a la Administración) y el Tribunal de Cuentas (supremo órgano fiscalizador económico).",
            "Las leyes pueden iniciarse como proyectos de ley (del Gobierno) o proposiciones de ley (del Parlamento, comunidades autónomas o iniciativa legislativa popular con al menos 500.000 firmas), requiriendo mayoría absoluta del Congreso cuando se trata de leyes orgánicas."
        ],
        "comp_questions": [
            {
                "question": "¿Cuál es la diferencia esencial entre el Congreso de los Diputados y el Senado?",
                "options": [
                    "El Congreso (350 diputados) vota la investidura del Presidente y tiene primacía legislativa, mientras el Senado es la Cámara de representación territorial",
                    "El Senado elige al Presidente del Gobierno y el Congreso solo elige a los alcaldes",
                    "Ambos tienen exactamente 100 miembros nombrados por el Rey",
                    "El Congreso solo se reúne una vez cada diez años"
                ],
                "correctIndex": 0,
                "explanation": "El Congreso de los Diputados cuenta con 350 miembros e inviste al Presidente del Gobierno; el Senado es la Cámara de representación territorial."
            },
            {
                "question": "¿Quién es el alto comisionado de las Cortes Generales para la defensa de los derechos del Título I?",
                "options": ["El Defensor del Pueblo", "El Fiscal General", "El Presidente del Consejo de Estado", "El Delegado del Gobierno"],
                "correctIndex": 0,
                "explanation": "El artículo 54 regula al Defensor del Pueblo como alto comisionado de las Cortes Generales."
            },
            {
                "question": "¿Cuántas firmas ciudadanas requiere una iniciativa legislativa popular?",
                "options": ["Al menos 500.000 firmas acreditadas", "Al menos 50.000 firmas", "Al menos 25.000 firmas", "1.500.000 firmas"],
                "correctIndex": 0,
                "explanation": "El artículo 87.3 exige no menos de 500.000 firmas acreditadas."
            }
        ]
    }

    cons_stem = "b1-cortes-consolidation"
    consolidation = {
        "title": "Repaso y Simulacro: Las Cortes Generales",
        "goal": "Consolidar el funcionamiento del Congreso y del Senado, la investidura, el Defensor del Pueblo, el Tribunal de Cuentas y la elaboración de las leyes.",
        "grammar": "Consolidación de estructuras parlamentarias y legislativas",
        "goals": [
            "Consolidate CCSE exam facts on the 350 deputies of Congress and the territorial representation of the Senate.",
            "Review the investiture debate, questions of confidence, and constructive motions of no confidence.",
            "Verify mastery of the Ombudsman (Defensor del Pueblo), Court of Auditors, popular legislative initiative (500,000 signatures), and General State Budget.",
            "Practice 'componerse de', 'tanto... como...', 'en caso de que + subjunctive', 'encargado de', and 'mediante'."
        ],
        "exercises": [
            {
                "id": f"{cons_stem}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["las Cortes Generales", "Spanish Parliament (Congress and Senate)"],
                    ["el escaño", "parliamentary seat"],
                    ["el Senado", "Senate (chamber of territorial representation)"],
                    ["la investidura", "investiture vote"],
                    ["la moción de censura", "motion of no confidence"],
                    ["el Defensor del Pueblo", "Ombudsman"],
                    ["el Tribunal de Cuentas", "Court of Auditors"],
                    ["la ley orgánica", "organic law (requires absolute majority)"]
                ],
                "teaches": ["componerse-de-y-dividirse-en"]
            },
            {
                "id": f"{cons_stem}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración describe correctamente la composición del Congreso de los Diputados?",
                "options": [
                    "El Congreso de los Diputados se compone de 350 diputados elegidos cada cuatro años.",
                    "El Congreso de los Diputados se componen por 350 diputados.",
                    "El Congreso de los Diputados compone a 350 diputados."
                ],
                "correct": 0,
                "teaches": ["componerse-de-y-dividirse-en"]
            },
            {
                "id": f"{cons_stem}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración utiliza correctamente la estructura correlativa «tanto... como...»?",
                "options": [
                    "El Senado está integrado tanto por senadores provinciales como por senadores designados por las comunidades autónomas.",
                    "El Senado está integrado tanto de senadores provinciales que senadores autonómicos.",
                    "El Senado está integrado tan por senadores provinciales como autonómicos."
                ],
                "correct": 0,
                "teaches": ["tanto-como-correlativos"]
            },
            {
                "id": f"{cons_stem}.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración emplea el modo verbal correcto tras «en caso de que»?",
                "options": [
                    "En caso de que el candidato no alcance la mayoría absoluta, se celebra una segunda votación.",
                    "En caso de que el candidato no alcanza la mayoría absoluta, se celebra una segunda votación.",
                    "En caso de que el candidato no alcanzará la mayoría absoluta, se celebra una segunda votación."
                ],
                "correct": 0,
                "teaches": ["en-caso-de-que-subjuntivo"]
            },
            {
                "id": f"{cons_stem}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué preposición introduce el instrumento legal exigido para regular los derechos fundamentales?",
                "options": [
                    "Los derechos fundamentales se regulan mediante ley orgánica.",
                    "Los derechos fundamentales se regulan hacia ley orgánica.",
                    "Los derechos fundamentales se regulan contra ley orgánica."
                ],
                "correct": 0,
                "teaches": ["mediante-y-a-traves-de"]
            },
            {
                "id": f"{cons_stem}.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las Cortes Generales están ___ por el Congreso de los Diputados y el Senado. (formar, participio femenino plural)",
                "answer": "formadas",
                "teaches": ["componerse-de-y-dividirse-en"],
                "english": "The Cortes Generales are formed by the Congress of Deputies and the Senate."
            },
            {
                "id": f"{cons_stem}.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Defensor del Pueblo es el alto comisionado ___ de defender los derechos fundamentales. (encargado)",
                "answer": "encargado",
                "teaches": ["encargado-de-infinitivo"],
                "english": "The Ombudsman is the high commissioner in charge of defending fundamental rights."
            },
            {
                "id": f"{cons_stem}.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los ciudadanos pueden presentar una proposición de ley ___ quinientas mil firmas acreditadas. (mediante)",
                "answer": "mediante",
                "teaches": ["mediante-y-a-traves-de"],
                "english": "Citizens may submit a parliamentary bill by means of five hundred thousand certified signatures."
            },
            {
                "id": f"{cons_stem}.ex09",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Senado", "es", "la", "Cámara", "de", "representación", "territorial."],
                "solution": ["El", "Senado", "es", "la", "Cámara", "de", "representación", "territorial."],
                "english": "The Senate is the Chamber of territorial representation.",
                "teaches": ["tanto-como-correlativos"]
            },
            {
                "id": f"{cons_stem}.ex10",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "El Gobierno elabora y aprueba en el Consejo de Ministros un proyecto de ley. [The Government drafts and approves a bill in the Council of Ministers.]",
                    "El Congreso de los Diputados y el Senado debaten, enmiendan y votan el texto. [The Congress of Deputies and the Senate debate, amend, and vote on the text.]",
                    "Una vez aprobado por las Cortes, el Rey lo sanciona y se publica en el BOE. [Once approved by the Cortes, the King sanctions it and it is published in the BOE.]"
                ],
                "solution": [0, 1, 2],
                "teaches": ["mediante-y-a-traves-de"]
            },
            {
                "id": f"{cons_stem}.ex11",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Cuál es la diferencia entre el Defensor del Pueblo y el Tribunal de Cuentas?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "El Defensor del Pueblo protege los derechos fundamentales frente a la Administración, mientras que el Tribunal de Cuentas fiscaliza las cuentas del Estado.",
                    "El Defensor del Pueblo dirige la policía y el Tribunal de Cuentas redacta las leyes.",
                    "Ambos son ministerios que pertenecen al poder ejecutivo."
                ],
                "correct": 0,
                "teaches": ["encargado-de-infinitivo"]
            },
            {
                "id": f"{cons_stem}.ex12",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "Las Cortes Generales ejercen la potestad legislativa del Estado, aprueban sus Presupuestos y controlan la acción del Gobierno.",
                "options": [
                    "The Cortes Generales exercise the legislative power of the State, approve its Budgets, and oversee the action of the Government.",
                    "The Cortes Generales are composed of judges appointed for life.",
                    "Only the Senate participates in approving laws."
                ],
                "correct": 0,
                "teaches": ["componerse-de-y-dividirse-en"]
            },
            {
                "id": f"{cons_stem}.ex13",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "Para presentar una iniciativa legislativa popular se exigen al menos quinientas mil firmas acreditadas de los ciudadanos.",
                "options": [
                    "To submit a popular legislative initiative, at least 500,000 certified signatures from citizens are required.",
                    "A popular legislative initiative requires only one thousand signatures.",
                    "Citizens cannot submit legislative proposals in Spain."
                ],
                "correct": 0,
                "teaches": ["mediante-y-a-traves-de"]
            },
            {
                "id": f"{cons_stem}.ex14",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las Cortes Generales representan al pueblo español.",
                "teaches": ["componerse-de-y-dividirse-en"],
                "english": "The Cortes Generales represent the Spanish people."
            },
            {
                "id": f"{cons_stem}.ex15",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica qué dos cámaras forman las Cortes Generales y cuántos diputados tiene el Congreso. [Explain which two chambers form the Cortes Generales and how many deputies Congress has.]",
                        "answer": "Las Cortes Generales están formadas por el Congreso de los Diputados, que se compone de 350 diputados, y el Senado, que es la Cámara de representación territorial."
                    }
                ],
                "teaches": ["componerse-de-y-dividirse-en"]
            },
            {
                "id": f"{cons_stem}.ex16",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica qué es el Defensor del Pueblo y qué función cumple. [Explain what the Ombudsman is and what role it plays.]",
                        "answer": "El Defensor del Pueblo es el alto comisionado de las Cortes Generales encargado de defender los derechos fundamentales de los ciudadanos y supervisar la actividad de la Administración."
                    }
                ],
                "teaches": ["encargado-de-infinitivo"]
            },
            {
                "id": f"{cons_stem}.ex17",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Resume quién elabora y quién aprueba los Presupuestos Generales del Estado. [Summarise who drafts and who approves the General State Budget.]",
                        "answer": "Corresponde al Gobierno la elaboración de los Presupuestos Generales del Estado y a las Cortes Generales su examen, enmienda y aprobación."
                    }
                ],
                "teaches": ["mediante-y-a-traves-de"]
            },
            {
                "id": f"{cons_stem}.ex18",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Qué diferencia hay entre un proyecto de ley y una proposición de ley?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "El proyecto de ley lo presenta el Gobierno, mientras que la proposición de ley la presentan el Congreso, el Senado, las comunidades autónomas o los ciudadanos.",
                    "No existe ninguna diferencia: ambos los redacta el Rey.",
                    "El proyecto de ley solo se aplica en los municipios pequeños."
                ],
                "correct": 0,
                "teaches": ["mediante-y-a-traves-de"]
            }
        ]
    }

    emit_unit("cortes", "b1-ccse-cortes", "Las Cortes Generales", 3, lessons, comb, consolidation)


if __name__ == "__main__":
    build_unit_2()
    build_unit_3()
