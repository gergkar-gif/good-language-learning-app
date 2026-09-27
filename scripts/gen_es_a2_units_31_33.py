# -*- coding: utf-8 -*-
"""
Generate Phase 10: Spanish A2 Units 31, 32, 33
- Unit 31: Indefinites & Double Negation (es-es and es-latam)
- Unit 32: Life in Duration & Periphrases (es-es and es-latam)
- Unit 33: Speaking to the Group: Vosotros in Spain (es-es only)
"""

import json
from pathlib import Path

ROOT = Path(".")
ES_ES = ROOT / "content/es-es"
ES_LATAM = ROOT / "content/es-latam"

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def make_story(id_str, title, summary, location, grammar_topics, vocab_topics, paragraphs_text, order_num):
    paras = [{"id": i + 1, "text": p} for i, p in enumerate(paragraphs_text)]
    return {
        "id": id_str,
        "title": title,
        "lesson": 5,
        "level": "A2",
        "order": order_num,
        "type": "original",
        "summary": summary,
        "characters": ["Carlos", "Meg"],
        "location": location,
        "grammar": grammar_topics,
        "vocabularyTopics": vocab_topics,
        "estimatedMinutes": 5,
        "paragraphs": paras
    }

def make_lesson(lesson_id, title, goal, grammar_label, stem, vocab_ref, exercise_refs, checklist_items):
    sections = [
        {"type": "goal", "title": "Lesson Goals", "items": [goal]},
        {"type": "recycle"},
        {"type": "grammar", "ref": f"grammar/a2/{stem}-gr.json"}
    ]
    if vocab_ref:
        sections.append({"type": "vocabulary", "title": "Lesson Vocabulary", "ref": vocab_ref})
    
    if len(exercise_refs) >= 11:
        sections.extend([
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/a2/{stem}-ex.json", "exerciseRefs": exercise_refs[0:6]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/a2/{stem}-ex.json", "exerciseRefs": exercise_refs[6:8]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/a2/{stem}-ex.json", "exerciseRefs": exercise_refs[8:10]},
            {"type": "exercise-group", "title": "Writing", "ref": f"exercises/a2/{stem}-ex.json", "exerciseRefs": exercise_refs[10:11]}
        ])
    else:
        sections.append({"type": "exercise-group", "title": "Review Practice", "ref": f"exercises/a2/{stem}-ex.json", "exerciseRefs": exercise_refs})
        
    sections.append({"type": "srs", "title": "Add to Review"})
    sections.append({"type": "checklist", "title": "Can you do this?", "items": checklist_items})
    
    return {
        "id": lesson_id,
        "title": title,
        "level": "A2",
        "goal": goal,
        "grammar": grammar_label,
        "metadata": {"estimatedMinutes": 15},
        "sections": sections
    }

def generate_unit(target_dir, stem_base, unit_id, lessons_data, cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs, story_title, story_summary, story_location, story_paras, story_order):
    for ld in lessons_data:
        stem = f"{stem_base}-{ld['num']}"
        les_id = f"lesson.a2.{unit_id}.{ld['num']}"
        
        # Clean exercises
        for ex in ld['exs']:
            if ex.get('type') == 'dialogue-complete' and 'answer' in ex:
                del ex['answer']
        ex_refs = [ex['id'] for ex in ld['exs']]
        
        # Clean vocab
        for w in ld['vocab']:
            if w.get('pos') == 'auxiliary':
                w['pos'] = 'verb'
        
        les_obj = make_lesson(
            les_id,
            ld['title'],
            ld['goal'],
            ld['grammar_title'],
            stem,
            f"vocabulary/a2/{stem}-voc.json",
            ex_refs,
            [f"I understand how to use {ld['grammar_title'].lower()} in real Spanish conversations."]
        )
        write_json(target_dir / f"lessons/a2/{stem}.json", les_obj)
        
        # Clean table rows: exactly 2 items per row
        clean_rows = [r[:2] for r in ld['table_rows']]
        gr_obj = {
            "id": f"grammar.a2.{unit_id}.{ld['num']}.{ld['grammar_slug']}",
            "title": ld['grammar_title'],
            "sections": [
                {"type": "text", "content": ld['grammar_text']},
                {"type": "table", "title": "Rules and Patterns", "rows": clean_rows},
                {"type": "examples", "items": ld['examples']},
                {"type": "tip", "content": ld['tip']}
            ]
        }
        write_json(target_dir / f"grammar/a2/{stem}-gr.json", gr_obj)
        
        voc_obj = {
            "id": f"vocab.a2.{unit_id}.{ld['num']}",
            "lesson": stem,
            "title": f"Vocabulary: {ld['title']}",
            "theme": "indefinites and communication",
            "words": ld['vocab']
        }
        write_json(target_dir / f"vocabulary/a2/{stem}-voc.json", voc_obj)
        
        ex_obj = {
            "lesson": stem,
            "exercises": ld['exs']
        }
        write_json(target_dir / f"exercises/a2/{stem}-ex.json", ex_obj)
        
    cons_stem = f"{stem_base}-consolidation"
    cons_les_id = f"lesson.a2.{unit_id}.consolidation"
    for ex in cons_exs:
        if ex.get('type') == 'dialogue-complete' and 'answer' in ex:
            del ex['answer']
    cons_refs = [ex['id'] for ex in cons_exs]
    cons_les_obj = make_lesson(cons_les_id, cons_title, cons_goal, f"{unit_id} consolidación", cons_stem, None, cons_refs, ["I can confidently apply these concepts across diverse communicative situations."])
    write_json(target_dir / f"lessons/a2/{cons_stem}.json", cons_les_obj)
    
    clean_cons_rows = [r[:2] for r in cons_table_rows]
    cons_gr_obj = {
        "id": f"grammar.a2.{unit_id}.consolidation.resumen",
        "title": f"Summary: {cons_title}",
        "sections": [
            {"type": "text", "content": cons_gr_text},
            {"type": "table", "title": "Quick Reference Table", "rows": clean_cons_rows},
            {"type": "examples", "items": cons_examples},
            {"type": "tip", "content": cons_tip}
        ]
    }
    write_json(target_dir / f"grammar/a2/{cons_stem}-gr.json", cons_gr_obj)
    write_json(target_dir / f"exercises/a2/{cons_stem}-ex.json", {"lesson": cons_stem, "exercises": cons_exs})
    
    story_obj = make_story(f"a2-original-{unit_id}", story_title, story_summary, story_location, [unit_id], ["daily life", "communication"], story_paras, story_order)
    write_json(target_dir / f"stories/original/a2/a2-{unit_id}.json", story_obj)
    print(f"Unit {unit_id} generated successfully in {target_dir}")

# ==========================================
# UNIT 31: Indefinidos & Negación
# ==========================================
def build_unit_31(target_dir):
    stem_base = "a2-indefinidosnegacion"
    unit_id = "indefinidosnegacion"
    
    lessons_data = [
        {
            "num": "01",
            "title": "Alguien and Nadie: People and Presence",
            "goal": "Express whether someone or no one is present using alguien and nadie with double negation.",
            "grammar_title": "Indefinite Pronouns: Alguien and Nadie",
            "grammar_slug": "alguien-nadie",
            "grammar_text": "In Spanish, we use **alguien** (someone, anyone) and **nadie** (no one, nobody) when referring to unspecified people.\n\n• **Double Negation Rule**: When *nadie* comes *after* the verb, you **must** place **no** before the verb:\n  *No vino nadie a la fiesta.*\n• When *nadie* comes *before* the verb, do **not** use *no*:\n  *Nadie vino a la fiesta.*",
            "table_rows": [
                ["Alguien (afirmativo)", "¿Hay alguien en la sala?", "Is there someone in the room?"],
                ["Nadie pospuesto (con 'no')", "No vi a nadie en la calle.", "I didn't see anyone in the street."],
                ["Nadie antepuesto (sin 'no')", "Nadie sabe la contraseña.", "Nobody knows the password."]
            ],
            "examples": [
                {"spanish": "¿Hay alguien esperando afuera?", "english": "Is there someone waiting outside?"},
                {"spanish": "No escuché a nadie llamar a la puerta.", "english": "I didn't hear anyone knock on the door."},
                {"spanish": "Nadie respondió a mi mensaje.", "english": "Nobody answered my message."}
            ],
            "tip": "Remember: Spanish loves double negatives! *No vino nadie* is completely grammatical and standard.",
            "vocab": [
                {"lemma": "alguien", "translation": "someone / anyone", "pos": "pronoun"},
                {"lemma": "nadie", "translation": "no one / nobody", "pos": "pronoun"},
                {"lemma": "desconocido", "translation": "stranger", "pos": "noun"},
                {"lemma": "sospechoso", "translation": "suspicious", "pos": "adjective"},
                {"lemma": "público", "translation": "audience / public", "pos": "noun"},
                {"lemma": "asistir", "translation": "to attend", "pos": "verb"},
                {"lemma": "aparecer", "translation": "to appear", "pos": "verb"},
                {"lemma": "llamar a la puerta", "translation": "to knock on the door", "pos": "expression"},
                {"lemma": "nadie más", "translation": "nobody else", "pos": "expression"},
                {"lemma": "contestar", "translation": "to answer", "pos": "verb"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.01.ex01", "category": "grammar", "type": "multiple-choice", "question": "¿Hay _____ en la cocina? Escuché un ruido.", "options": ["alguien", "nadie", "algo", "nada"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "No conozco a _____ en esta fiesta.", "answer": "nadie", "english": "I don't know anyone at this party.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Nadie", "sabe", "la", "respuesta", "correcta", "."], "solution": ["Nadie", "sabe", "la", "respuesta", "correcta", "."], "english": "Nobody knows the correct answer.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Un _____ tocó el timbre anoche.", "options": ["desconocido", "público", "alguien", "asistir"], "correct": 0, "teaches": ["a2-unit31-vocab"]},
                {"id": f"a2.{unit_id}.01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "No vino _____ a la conferencia de ayer.", "answer": "nadie", "english": "Nobody came to yesterday's conference.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex06", "category": "grammar", "type": "matching", "pairs": [["Alguien llama", "Someone is calling"], ["Nadie responde", "Nobody answers"], ["No veo a nadie", "I don't see anyone"], ["Nadie más", "Nobody else"]], "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex07", "category": "listening", "type": "listening-choice", "sentence": "Perdone, ¿ha visto a alguien salir del edificio hace diez minutos?", "options": ["Pregunta si vio a alguien salir.", "Pregunta si alguien quiere entrar.", "Pregunta si el edificio está cerrado."], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex08", "category": "listening", "type": "dictation", "sentence": "No hay nadie en la oficina a esta hora.", "english": "There is nobody in the office at this hour.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿Ha llamado alguien mientras yo estaba fuera?"}, {"speaker": "Sofía", "text": "No, no ha llamado _____."}], "answer": "nadie", "options": ["nadie", "alguien", "nada", "algo"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Policía", "text": "¿Había alguien en el pasillo durante la noche?"}, {"speaker": "Vecino", "text": "No oficial, _____ vio a ninguna persona."}], "answer": "nadie", "options": ["nadie", "alguien", "todos", "alguno"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que alguien está esperando en la entrada.", "answer": "Alguien está esperando en la entrada."}], "teaches": ["indefinidos-negativos"]}
            ]
        },
        {
            "num": "02",
            "title": "Algo and Nada: Objects and Existence",
            "goal": "Express the presence or total absence of things using algo and nada in affirmative and negative sentences.",
            "grammar_title": "Indefinite Pronouns: Algo and Nada",
            "grammar_slug": "algo-nada",
            "grammar_text": "We use **algo** (something, anything) and **nada** (nothing, not anything) for inanimate objects or concepts.\n\n• **Double Negation**: When *nada* is placed after the verb, use *no* before the verb:\n  *No quiero nada de comer.*\n• When *nada* is the subject or precedes the verb, do not use *no*:\n  *Nada es imposible.*\n• **Common expressions**: *algo de* (a little bit of), *nada de* (none of / not at all), *de nada* (you're welcome).",
            "table_rows": [
                ["Algo (afirmativo)", "¿Tienes algo de dinero?", "Do you have a bit of money?"],
                ["Nada pospuesto (con 'no')", "No tengo nada que perder.", "I have nothing to lose."],
                ["Nada antepuesto (sin 'no')", "Nada me preocupa hoy.", "Nothing worries me today."]
            ],
            "examples": [
                {"spanish": "¿Quieres comer algo antes de ir al cine?", "english": "Do you want to eat something before going to the movies?"},
                {"spanish": "No encontramos nada interesante en la tienda.", "english": "We didn't find anything interesting in the shop."},
                {"spanish": "Nada me molesta tanto como el ruido.", "english": "Nothing bothers me as much as noise."}
            ],
            "tip": "Use *algo de* before non-count nouns: *algo de agua* (a little water), *algo de tiempo* (some time).",
            "vocab": [
                {"lemma": "algo", "translation": "something / anything", "pos": "pronoun"},
                {"lemma": "nada", "translation": "nothing", "pos": "pronoun"},
                {"lemma": "asunto", "translation": "issue / matter", "pos": "noun"},
                {"lemma": "detalle", "translation": "detail", "pos": "noun"},
                {"lemma": "importar", "translation": "to matter", "pos": "verb"},
                {"lemma": "ocurrir", "translation": "to happen / occur", "pos": "verb"},
                {"lemma": "notar", "translation": "to notice", "pos": "verb"},
                {"lemma": "faltar", "translation": "to be missing / lack", "pos": "verb"},
                {"lemma": "nada de", "translation": "none of / not at all", "pos": "expression"},
                {"lemma": "de nada", "translation": "you are welcome", "pos": "expression"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.02.ex01", "category": "grammar", "type": "multiple-choice", "question": "¿Quieres comer _____ antes de que salgamos?", "options": ["algo", "nada", "alguien", "ninguno"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "No tengo _____ que decir sobre ese asunto.", "answer": "nada", "english": "I have nothing to say about that matter.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["No", "pasa", "nada", "importante", "aquí", "."], "solution": ["No", "pasa", "nada", "importante", "aquí", "."], "english": "Nothing important is happening here.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Este es un _____ muy importante para el equipo.", "options": ["asunto", "detalle", "algo", "nada"], "correct": 0, "teaches": ["a2-unit31-vocab"]},
                {"id": f"a2.{unit_id}.02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "No me falta _____ en mi nuevo apartamento.", "answer": "nada", "english": "I lack nothing in my new apartment.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex06", "category": "grammar", "type": "matching", "pairs": [["Algo nuevo", "Something new"], ["Nada importante", "Nothing important"], ["Algo de comer", "Something to eat"], ["De nada", "You are welcome"]], "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex07", "category": "listening", "type": "listening-choice", "sentence": "No te preocupes por el favor, de verdad que no fue nada.", "options": ["Dice que no fue nada importante.", "Pide que le hagan un favor.", "Quiere comprar algo."], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex08", "category": "listening", "type": "dictation", "sentence": "No entiendo nada de lo que dices.", "english": "I don't understand anything of what you say.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Camarero", "text": "¿Desean tomar algo de postre hoy?"}, {"speaker": "Cliente", "text": "No, gracias, no queremos _____."}], "answer": "nada", "options": ["nada", "algo", "nadie", "alguien"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Marta", "text": "¿Notaste algo extraño en la oficina?"}, {"speaker": "Javier", "text": "No, no noté _____ raro."}], "answer": "nada", "options": ["nada", "algo", "nadie", "ninguno"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que no tienes nada que hacer esta tarde.", "answer": "No tengo nada que hacer esta tarde."}], "teaches": ["indefinidos-negativos"]}
            ]
        },
        {
            "num": "03",
            "title": "Algún and Ningún: Adjectival Quantifiers",
            "goal": "Use algún, alguno, and ningún, ninguna with correct gender, number, and masculine apocope.",
            "grammar_title": "Indefinite Adjectives: Algún and Ningún",
            "grammar_slug": "algun-ningun",
            "grammar_text": "When modifying nouns, *alguno* and *ninguno* act as indefinite adjectives:\n\n• **Apocope**: Before a masculine singular noun, drop the final -o and add an accent:\n  *alguno* -> **algún** (*algún día*, *algún problema*)\n  *ninguno* -> **ningún** (*ningún hotel*, *ningún amigo*)\n• Feminine forms maintain standard endings: **alguna** / **ninguna** (*alguna duda*, *ninguna duda*).\n• *Ninguno/a* is almost always singular in modern Spanish (*No tengo ninguna duda*).",
            "table_rows": [
                ["Masculino singular", "algún problema / ningún problema", "some problem / no problem"],
                ["Femenino singular", "alguna duda / ninguna duda", "any doubt / no doubt"],
                ["Pronombre independiente", "¿Tienes libros? No tengo ninguno.", "Do you have books? I have none."]
            ],
            "examples": [
                {"spanish": "¿Tienes algún plan para las vacaciones?", "english": "Do you have any plan for the holidays?"},
                {"spanish": "No encontramos ningún billete barato para el tren.", "english": "We didn't find any cheap ticket for the train."},
                {"spanish": "No tengo ninguna pregunta sobre el proyecto.", "english": "I have no question about the project."}
            ],
            "tip": "Always write the accent mark on *algún* and *ningún* when they stand before a masculine noun.",
            "vocab": [
                {"lemma": "algún", "translation": "some / any (masc. sing.)", "pos": "adjective"},
                {"lemma": "alguno", "translation": "some / any (pronoun)", "pos": "pronoun"},
                {"lemma": "ningún", "translation": "no / not any (masc. sing.)", "pos": "adjective"},
                {"lemma": "ninguno", "translation": "none / not one", "pos": "pronoun"},
                {"lemma": "alguna", "translation": "some / any (fem. sing.)", "pos": "adjective"},
                {"lemma": "ninguna", "translation": "no / not any (fem. sing.)", "pos": "adjective"},
                {"lemma": "duda", "translation": "doubt / question", "pos": "noun"},
                {"lemma": "solución", "translation": "solution", "pos": "noun"},
                {"lemma": "opción", "translation": "option", "pos": "noun"},
                {"lemma": "elegir", "translation": "to choose", "pos": "verb"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.03.ex01", "category": "grammar", "type": "multiple-choice", "question": "¿Tienes _____ duda sobre la lección de gramática?", "options": ["alguna", "algún", "ninguno", "nada"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "No tengo _____ problema con ese horario.", "answer": "ningún", "english": "I have no problem with that schedule.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["No", "encontré", "ninguna", "solución", "fácil", "."], "solution": ["No", "encontré", "ninguna", "solución", "fácil", "."], "english": "I didn't find any easy solution.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Tenemos que encontrar una _____ rápida a este conflicto.", "options": ["solución", "duda", "alguna", "ninguna"], "correct": 0, "teaches": ["a2-unit31-vocab"]},
                {"id": f"a2.{unit_id}.03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "¿Conoces _____ buen restaurante por esta zona?", "answer": "algún", "english": "Do you know any good restaurant around this area?", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex06", "category": "grammar", "type": "matching", "pairs": [["Algún día", "Someday"], ["Ningún problema", "No problem"], ["Alguna duda", "Any doubt"], ["Ninguna persona", "No person"]], "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex07", "category": "listening", "type": "listening-choice", "sentence": "Lo siento, pero no queda ningún billete para el concierto.", "options": ["No hay entradas disponibles.", "Quedan muchas entradas.", "El concierto fue cancelado."], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex08", "category": "listening", "type": "dictation", "sentence": "No queda ninguna entrada para el teatro.", "english": "There is no ticket left for the theater.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Profesor", "text": "¿Hay alguna pregunta sobre el examen?"}, {"speaker": "Alumno", "text": "No profesor, no tenemos _____ duda."}], "answer": "ninguna", "options": ["ninguna", "alguna", "ningún", "nada"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Vendedora", "text": "¿Le gusta alguno de estos abrigos?"}, {"speaker": "Cliente", "text": "La verdad es que no me gusta _____."}], "answer": "ninguno", "options": ["ninguno", "algún", "ningún", "alguien"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que no tienes ningún plan para el sábado.", "answer": "No tengo ningún plan para el sábado."}], "teaches": ["indefinidos-negativos"]}
            ]
        },
        {
            "num": "04",
            "title": "Tampoco and Time: Negative Agreement",
            "goal": "Agree with negative statements using tampoco, and express frequency negation with nunca and jamás.",
            "grammar_title": "Negative Agreement and Frequency: Tampoco and Nunca",
            "grammar_slug": "tampoco-nunca",
            "grammar_text": "Spanish handles negative agreement and time with specialized adverbs:\n\n• **Tampoco** (neither, not either):\n  *—No me gusta el frío. —A mí tampoco.*\n  *—No voy a salir hoy. —Yo tampoco.*\n• **Nunca / Jamás** (never):\n  *Nunca viajo de noche.* = *No viajo de noche nunca.*\n• **Ya no** (no longer) vs. **Todavía no** (not yet):\n  *Ya no vivo en Sevilla.* (I don't live in Seville anymore.)\n  *Todavía no he terminado.* (I haven't finished yet.)",
            "table_rows": [
                ["Acuerdo afirmativo", "A mí también", "Me too"],
                ["Acuerdo negativo", "A mí tampoco", "Me neither / Neither do I"],
                ["Frecuencia cero", "Nunca / Jamás", "Never / Never ever"],
                ["Cambio temporal", "Ya no trabajo allí / Todavía no sé", "I no longer work there / I don't know yet"]
            ],
            "examples": [
                {"spanish": "—No hablo alemán. —Yo tampoco.", "english": "—I don't speak German. —Neither do I."},
                {"spanish": "Nunca he probado la comida peruana.", "english": "I have never tasted Peruvian food."},
                {"spanish": "Ya no fumo desde hace seis meses.", "english": "I no longer smoke for six months."}
            ],
            "tip": "Never say *'yo también no'*. Always say **'yo tampoco'** or **'a mí tampoco'**!",
            "vocab": [
                {"lemma": "tampoco", "translation": "neither / not either", "pos": "adverb"},
                {"lemma": "nunca", "translation": "never", "pos": "adverb"},
                {"lemma": "jamás", "translation": "never ever", "pos": "adverb"},
                {"lemma": "todavía no", "translation": "not yet", "pos": "expression"},
                {"lemma": "ya no", "translation": "no longer", "pos": "expression"},
                {"lemma": "coincidir", "translation": "to agree / coincide", "pos": "verb"},
                {"lemma": "acuerdo", "translation": "agreement", "pos": "noun"},
                {"lemma": "opinar", "translation": "to have an opinion", "pos": "verb"},
                {"lemma": "acostumbrarse", "translation": "to get used to", "pos": "verb"},
                {"lemma": "repetir", "translation": "to repeat", "pos": "verb"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.04.ex01", "category": "grammar", "type": "multiple-choice", "question": "—No me gusta el café con azúcar. —A mí _____.", "options": ["tampoco", "también", "nada", "nunca"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Yo _____ he viajado en barco en mi vida.", "answer": "nunca", "english": "I have never traveled by ship in my life.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Yo", "tampoco", "quiero", "salir", "hoy", "."], "solution": ["Yo", "tampoco", "quiero", "salir", "hoy", "."], "english": "I don't want to go out today either.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Llegamos a un _____ muy importante en la reunión.", "options": ["acuerdo", "tampoco", "nunca", "jamás"], "correct": 0, "teaches": ["a2-unit31-vocab"]},
                {"id": f"a2.{unit_id}.04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "—No comprendo las instrucciones. —Yo _____ las comprendo.", "answer": "tampoco", "english": "—I don't understand the instructions. —I don't understand them either.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex06", "category": "grammar", "type": "matching", "pairs": [["Yo tampoco", "Me neither"], ["Nunca jamás", "Never ever"], ["Ya no vivo allí", "I no longer live there"], ["Todavía no", "Not yet"]], "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex07", "category": "listening", "type": "listening-choice", "sentence": "Nunca había visto una ciudad tan animada por la noche.", "options": ["Expresa que es su primera vez viendo algo así.", "Dice que visita la ciudad a menudo.", "No le gusta la ciudad."], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex08", "category": "listening", "type": "dictation", "sentence": "Ella tampoco sabe la fecha del examen.", "english": "She doesn't know the exam date either.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Andrés", "text": "No he terminado el informe todavía."}, {"speaker": "Beatriz", "text": "Yo _____ lo he terminado."}], "answer": "tampoco", "options": ["tampoco", "también", "nunca", "nada"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "David", "text": "¿Has visitado alguna vez las islas Canarias?"}, {"speaker": "Sara", "text": "No, _____ he estado allí."}], "answer": "nunca", "options": ["nunca", "tampoco", "alguien", "nada"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una respuesta usando 'tampoco' a la frase: 'No quiero cenar fuera'.", "answer": "Yo tampoco quiero cenar fuera."}], "teaches": ["indefinidos-negativos"]}
            ]
        },
        {
            "num": "05",
            "title": "Mastering Negative Systems in Conversation",
            "goal": "Integrate all indefinite and negative words fluidly in complex conversational dialogues.",
            "grammar_title": "Integrated Negative System in Spanish",
            "grammar_slug": "sistema-negativo-integrado",
            "grammar_text": "Spanish negation follows a unified logical structure:\n\n• **People**: *alguien* ↔ *nadie*\n• **Things**: *algo* ↔ *nada*\n• **Quantities**: *algún/a* ↔ *ningún/a*\n• **Agreement**: *también* ↔ *tampoco*\n• **Time**: *siempre* ↔ *nunca / jamás*\n\nNotice how multiple negatives chain together naturally:\n*Nadie me dijo nunca nada sobre ningún problema.* (Literally: Nobody told me never nothing about no problem — completely standard Spanish!).",
            "table_rows": [
                ["Afirmativo", "alguien", "algo", "algún día", "también", "siempre"],
                ["Negativo", "nadie", "nada", "ningún día", "tampoco", "nunca / jamás"],
                ["Encadenamiento", "No hay nadie nunca", "There is never anyone"]
            ],
            "examples": [
                {"spanish": "Nadie en el grupo tenía ninguna queja.", "english": "Nobody in the group had any complaint."},
                {"spanish": "No tengo nada que añadir y él tampoco.", "english": "I have nothing to add and neither does he."},
                {"spanish": "Nunca vi a nadie tan entusiasmado.", "english": "I never saw anyone so enthusiastic."}
            ],
            "tip": "Do not fear multiple negatives! They reinforce the negative idea rather than cancelling it out.",
            "vocab": [
                {"lemma": "queja", "translation": "complaint", "pos": "noun"},
                {"lemma": "entusiasmado", "translation": "enthusiastic", "pos": "adjective"},
                {"lemma": "complicado", "translation": "complicated", "pos": "adjective"},
                {"lemma": "aclarar", "translation": "to clarify", "pos": "verb"},
                {"lemma": "situación", "translation": "situation", "pos": "noun"},
                {"lemma": "explicar", "translation": "to explain", "pos": "verb"},
                {"lemma": "entenderse", "translation": "to understand one another", "pos": "verb"},
                {"lemma": "conversación", "translation": "conversation", "pos": "noun"},
                {"lemma": "totalmente", "translation": "totally", "pos": "adverb"},
                {"lemma": "absoluto", "translation": "absolute", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.05.ex01", "category": "grammar", "type": "multiple-choice", "question": "No vino _____ a la reunión y no sabemos por qué.", "options": ["nadie", "alguien", "nada", "ninguno"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "No tenemos _____ duda sobre el plan final.", "answer": "ninguna", "english": "We have no doubt about the final plan.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Nadie", "dijo", "nada", "sobre", "el", "asunto", "."], "solution": ["Nadie", "dijo", "nada", "sobre", "el", "asunto", "."], "english": "Nobody said anything about the matter.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "El profesor ayudó a _____ todas las dudas de la clase.", "options": ["aclarar", "queja", "situación", "absoluto"], "correct": 0, "teaches": ["a2-unit31-vocab"]},
                {"id": f"a2.{unit_id}.05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Ella no tiene hambre y yo _____ tengo hambre.", "answer": "tampoco", "english": "She is not hungry and I am not hungry either.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex06", "category": "grammar", "type": "matching", "pairs": [["Alguien / Nadie", "Someone / Nobody"], ["Algo / Nada", "Something / Nothing"], ["Algún / Ningún", "Some / None"], ["También / Tampoco", "Also / Neither"]], "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex07", "category": "listening", "type": "listening-choice", "sentence": "No encontramos ningún restaurante abierto en todo el centro.", "options": ["Todos los restaurantes estaban cerrados.", "Comieron en un restaurante céntrico.", "Llegaron tarde al restaurante."], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex08", "category": "listening", "type": "dictation", "sentence": "Nadie me dijo nunca nada sobre ese problema.", "english": "Nobody ever told me anything about that problem.", "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Valeria", "text": "¿Ha quedado alguien en la sala de juntas?"}, {"speaker": "Mateo", "text": "No, ya no queda _____."}], "answer": "nadie", "options": ["nadie", "alguien", "nada", "ninguna"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Raúl", "text": "No me gusta caminar bajo la lluvia."}, {"speaker": "Elena", "text": "A mí _____ me gusta."}], "answer": "tampoco", "options": ["tampoco", "también", "nunca", "nada"], "correct": 0, "teaches": ["indefinidos-negativos"]},
                {"id": f"a2.{unit_id}.05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que nadie sabe nada sobre el secreto.", "answer": "Nadie sabe nada sobre el secreto."}], "teaches": ["indefinidos-negativos"]}
            ]
        }
    ]
    
    cons_title = "Consolidation: Indefinites and Negation"
    cons_goal = "Consolidate complete command of negative and indefinite structures in everyday Spanish communication."
    cons_gr_text = "Mastering Spanish negation means embracing the dual-position rule: if the negative word follows the verb, *no* must precede the verb (*No vi a nadie*); if it precedes the verb, *no* is omitted (*Nadie vino*)."
    cons_table_rows = [
        ["Personas", "alguien / nadie", "No conozco a nadie"],
        ["Cosas", "algo / nada", "No necesito nada"],
        ["Determinantes", "algún, alguna / ningún, ninguna", "No hay ningún problema"],
        ["Acuerdo y tiempo", "también / tampoco, nunca / jamás", "Yo tampoco lo sé"]
    ]
    cons_examples = [
        {"spanish": "Nadie vino y no ocurrió nada.", "english": "Nobody came and nothing happened."},
        {"spanish": "—No entiendo este ejercicio. —Yo tampoco.", "english": "—I don't understand this exercise. —Neither do I."}
    ]
    cons_tip = "Always remember the positive/negative pairs: alguien/nadie, algo/nada, algún/ningún, también/tampoco, siempre/nunca."
    
    cons_exs = [
        {"id": f"a2.{unit_id}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "No tengo _____ tiempo para hablar ahora.", "options": ["ningún", "nada", "alguien", "algún"], "correct": 1, "teaches": ["indefinidos-negativos"]},
        {"id": f"a2.{unit_id}.cons.ex02", "category": "grammar", "type": "fill-blank", "sentence": "No vino _____ a la fiesta.", "answer": "nadie", "english": "Nobody came to the party.", "teaches": ["indefinidos-negativos"]},
        {"id": f"a2.{unit_id}.cons.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Nadie", "quiere", "hacer", "eso", "."], "solution": ["Nadie", "quiere", "hacer", "eso", "."], "english": "Nobody wants to do that.", "teaches": ["indefinidos-negativos"]},
        {"id": f"a2.{unit_id}.cons.ex04", "category": "grammar", "type": "matching", "pairs": [["Alguien", "Someone"], ["Nadie", "Nobody"], ["Algo", "Something"], ["Nada", "Nothing"]], "teaches": ["indefinidos-negativos"]},
        {"id": f"a2.{unit_id}.cons.ex05", "category": "listening", "type": "listening-choice", "sentence": "No hay ningún problema con la reserva del hotel.", "options": ["La reserva está confirmada sin problemas.", "Hay un problema con la habitación.", "No tienen reserva."], "correct": 0, "teaches": ["indefinidos-negativos"]},
        {"id": f"a2.{unit_id}.cons.ex06", "category": "listening", "type": "dictation", "sentence": "Yo tampoco sé la dirección exacta.", "english": "I don't know the exact address either.", "teaches": ["indefinidos-negativos"]},
        {"id": f"a2.{unit_id}.cons.ex07", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Carlos", "text": "¿Has encontrado las llaves en algún sitio?"}, {"speaker": "Meg", "text": "No, no las he encontrado en _____ lugar."}], "answer": "ningún", "options": ["ningún", "algún", "nada", "nadie"], "correct": 0, "teaches": ["indefinidos-negativos"]},
        {"id": f"a2.{unit_id}.cons.ex08", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que no compraste nada en la tienda.", "answer": "No compré nada en la tienda."}], "teaches": ["indefinidos-negativos"]}
    ]
    
    story_paras = [
        "Eran las ocho de la tarde y en la oficina ya no quedaba casi nadie.",
        "Carlos y Meg buscaban las llaves del archivo confidencial por todos los rincones del despacho.",
        "«¿Has encontrado algo debajo de las mesas?», preguntó Meg con evidente preocupación.",
        "«No, no veo nada por aquí», respondió Carlos levantando varias carpetas vacías.",
        "«¿Hablaste con alguien del equipo de limpieza antes de que se marcharan?», insistió ella.",
        "«Nadie vio nada extraño», contestó él. «Y el conserje tampoco sabía dónde estaban guardadas».",
        "De repente, Meg se rió con ganas al mirar su propio bolsillo: «¡No te lo vas a creer! ¡Nadie las perdió, las tenía yo guardadas desde la mañana!»."
    ]
    
    generate_unit(
        target_dir, stem_base, unit_id, lessons_data,
        cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs,
        "Misterio en la oficina: ¿Dónde están las llaves?",
        "Carlos y Meg buscan desesperadamente las llaves del archivo confidencial sin encontrar ninguna pista en la oficina.",
        "Madrid", story_paras, 31
    )

# ==========================================
# UNIT 32: Perífrasis y Duración
# ==========================================
def build_unit_32(target_dir):
    stem_base = "a2-perifrasisduracion"
    unit_id = "perifrasisduracion"
    
    lessons_data = [
        {
            "num": "01",
            "title": "Acabar de + Infinitivo: Just Finished",
            "goal": "Express actions completed in the immediate past using acabar de in the present and imperfect.",
            "grammar_title": "Recent Actions: Acabar de + Infinitivo",
            "grammar_slug": "acabar-de-infinitivo",
            "grammar_text": "The periphrasis **acabar de + infinitivo** expresses that an action was completed just moments before the moment of speaking.\n\n• **Present indicative**: *Acabo de llegar.* (I have just arrived / I just arrived.)\n• **Imperfect indicative**: *Acababa de salir cuando me llamaste.* (I had just left when you called me.)\n• Unlike English 'just', no adverb is needed — the verb *acabar* followed by *de* encodes immediate recency.",
            "table_rows": [
                ["Yo acabo de + inf", "Acabo de comer.", "I have just eaten."],
                ["Tú acabas de + inf", "¿Acabas de ver la noticia?", "Did you just see the news?"],
                ["Él/Ella acaba de + inf", "El tren acaba de salir.", "The train just left."],
                ["Nosotros acabamos de + inf", "Acabamos de comprar los billetes.", "We just bought the tickets."],
                ["Ellos acaban de + inf", "Acaban de anunciar el vuelo.", "They just announced the flight."]
            ],
            "examples": [
                {"spanish": "Acabo de recibir un correo electrónico urgente.", "english": "I have just received an urgent email."},
                {"spanish": "¿Acabas de llegar de tu viaje?", "english": "Did you just arrive from your trip?"},
                {"spanish": "Acabábamos de cenar cuando tocaron al timbre.", "english": "We had just had dinner when the doorbell rang."}
            ],
            "tip": "Always use the infinitive after *de*: *acabo de hablar*, never *acabo de hablado*.",
            "vocab": [
                {"lemma": "acabar de", "translation": "to have just done", "pos": "verb"},
                {"lemma": "recién", "translation": "recently / freshly", "pos": "adverb"},
                {"lemma": "noticia", "translation": "news / piece of news", "pos": "noun"},
                {"lemma": "aterrizar", "translation": "to land", "pos": "verb"},
                {"lemma": "anunciar", "translation": "to announce", "pos": "verb"},
                {"lemma": "avisar", "translation": "to notify / warn", "pos": "verb"},
                {"lemma": "hace un momento", "translation": "a moment ago", "pos": "expression"},
                {"lemma": "terminar", "translation": "to finish", "pos": "verb"},
                {"lemma": "ocurrir", "translation": "to happen", "pos": "verb"},
                {"lemma": "reciente", "translation": "recent", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.01.ex01", "category": "grammar", "type": "multiple-choice", "question": "El avión _____ de aterrizar en el aeropuerto.", "options": ["acaba", "lleva", "empieza", "termina"], "correct": 0, "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Yo acabo _____ recibir tu mensaje de texto.", "answer": "de", "english": "I have just received your text message.", "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Acabo", "de", "llegar", "a", "la", "oficina", "."], "solution": ["Acabo", "de", "llegar", "a", "la", "oficina", "."], "english": "I have just arrived at the office.", "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "¿Escuchaste la última _____ en la radio?", "options": ["noticia", "aterrizar", "reciente", "acabar de"], "correct": 0, "teaches": ["a2-unit32-vocab"]},
                {"id": f"a2.{unit_id}.01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Mis amigos acaban de _____ una casa preciosa.", "answer": "comprar", "english": "My friends have just bought a lovely house.", "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex06", "category": "grammar", "type": "matching", "pairs": [["Acabo de comer", "I have just eaten"], ["Acabas de llegar", "You just arrived"], ["Acaba de salir", "It just left"], ["Acabamos de ver", "We just saw"]], "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex07", "category": "listening", "type": "listening-choice", "sentence": "Perdona que no contestara antes, acabo de salir de una reunión.", "options": ["Salió de la reunión hace un instante.", "Todavía está en la reunión.", "No fue a la reunión."], "correct": 0, "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex08", "category": "listening", "type": "dictation", "sentence": "Acabamos de escuchar la noticia por la radio.", "english": "We have just heard the news on the radio.", "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Pablo", "text": "¿Quieres venir a almorzar con nosotros?"}, {"speaker": "Clara", "text": "Muchas gracias Pablo, pero acabo de _____ ahora mismo."}], "answer": "comer", "options": ["comer", "comido", "comiendo", "como"], "correct": 0, "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Laura", "text": "¿Has visto a Martín hoy?"}, {"speaker": "Sergio", "text": "Sí, acaba _____ pasar por el pasillo."}], "answer": "de", "options": ["de", "a", "por", "en"], "correct": 0, "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que acabas de terminar tus tareas.", "answer": "Acabo de terminar mis tareas."}], "teaches": ["acabar-de"]}
            ]
        },
        {
            "num": "02",
            "title": "Llevar + Tiempo + Gerundio: Ongoing Duration",
            "goal": "Describe activities that started in the past and continue into the present using llevar + time + gerund.",
            "grammar_title": "Duration of Actions: Llevar + Tiempo + Gerundio",
            "grammar_slug": "llevar-tiempo-gerundio",
            "grammar_text": "To express how long an ongoing action has been taking place, Spanish uses:\n\n**llevar + [período de tiempo] + gerundio**\n\n• *Llevo dos años viviendo en Madrid.* (I have been living in Madrid for two years.)\n• *¿Cuánto tiempo llevas estudiando español?* (How long have you been studying Spanish?)\n• Equivalence: *Llevo seis meses trabajando aquí* = *Trabajo aquí desde hace seis meses*.\n• Note: Remember the gerund form: *-ar -> -ando* (*trabajando*), *-er/-ir -> -iendo* (*aprendiendo*, *viviendo*).",
            "table_rows": [
                ["Llevar + tiempo + gerundio", "Llevo tres meses aprendiendo español.", "I have been learning Spanish for 3 months."],
                ["Pregunta de duración", "¿Cuánto tiempo llevas viviendo aquí?", "How long have you been living here?"],
                ["Equivalencia con 'desde hace'", "Trabajo aquí desde hace dos años.", "I work here since 2 years ago."]
            ],
            "examples": [
                {"spanish": "Llevamos media hora esperando el autobús.", "english": "We have been waiting for the bus for half an hour."},
                {"spanish": "¿Cuánto tiempo llevas trabajando en esta empresa?", "english": "How long have you been working at this company?"},
                {"spanish": "Mi hermano lleva cinco años viviendo en Barcelona.", "english": "My brother has been living in Barcelona for five years."}
            ],
            "tip": "The verb *llevar* is conjugated in the present tense to show that the action is still actively happening now.",
            "vocab": [
                {"lemma": "llevar tiempo", "translation": "to have been doing for [time]", "pos": "expression"},
                {"lemma": "gerundio", "translation": "gerund", "pos": "noun"},
                {"lemma": "mes", "translation": "month", "pos": "noun"},
                {"lemma": "década", "translation": "decade", "pos": "noun"},
                {"lemma": "etapa", "translation": "stage / phase", "pos": "noun"},
                {"lemma": "convivir", "translation": "to live together / coexist", "pos": "verb"},
                {"lemma": "aprender", "translation": "to learn", "pos": "verb"},
                {"lemma": "residir", "translation": "to reside / live", "pos": "verb"},
                {"lemma": "durar", "translation": "to last", "pos": "verb"},
                {"lemma": "continuar", "translation": "to continue", "pos": "verb"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.02.ex01", "category": "grammar", "type": "multiple-choice", "question": "Llevo tres meses _____ español todos los días.", "options": ["estudiando", "estudiar", "estudio", "estudiado"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "¿Cuánto tiempo _____ viviendo en esta ciudad?", "answer": "llevas", "english": "How long have you been living in this city?", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Llevo", "dos", "horas", "esperando", "aquí", "."], "solution": ["Llevo", "dos", "horas", "esperando", "aquí", "."], "english": "I have been waiting here for two hours.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Esta es una _____ maravillosa de mi vida universitaria.", "options": ["etapa", "gerundio", "década", "mes"], "correct": 0, "teaches": ["a2-unit32-vocab"]},
                {"id": f"a2.{unit_id}.02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Nosotros llevamos un año _____ en el mismo piso.", "answer": "viviendo", "english": "We have been living in the same apartment for a year.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex06", "category": "grammar", "type": "matching", "pairs": [["Llevo un año viviendo", "I've been living for a year"], ["Llevas dos horas esperando", "You've been waiting 2 hours"], ["Lleva meses trabajando", "He's been working for months"], ["Llevamos días buscando", "We've been looking for days"]], "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex07", "category": "listening", "type": "listening-choice", "sentence": "Llevo casi diez años trabajando como diseñador gráfico en Madrid.", "options": ["Lleva una década en esa profesión.", "Empezó a trabajar hace dos meses.", "Quiere cambiar de profesión."], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex08", "category": "listening", "type": "dictation", "sentence": "Llevamos mucho tiempo esperando tu respuesta.", "english": "We have been waiting for your response for a long time.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Hugo", "text": "¿Cuánto tiempo llevas aprendiendo a tocar el piano?"}, {"speaker": "Inés", "text": "_____ tres años practicando cada semana."}], "answer": "Llevo", "options": ["Llevo", "Tengo", "Hago", "Estoy"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Marcos", "text": "¿Sigue lloviendo afuera?"}, {"speaker": "Ana", "text": "Sí, lleva toda la tarde _____ sin parar."}], "answer": "lloviendo", "options": ["lloviendo", "llover", "llueve", "llovido"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que llevas seis meses aprendiendo español.", "answer": "Llevo seis meses aprendiendo español."}], "teaches": ["llevar-tiempo-gerundio"]}
            ]
        },
        {
            "num": "03",
            "title": "Llevar + Tiempo + Sin + Infinitivo: Negative Duration",
            "goal": "Express the period of time during which an action has ceased or not occurred using llevar + time + sin + infinitive.",
            "grammar_title": "Negative Duration: Llevar + Tiempo + Sin + Infinitivo",
            "grammar_slug": "llevar-sin-infinitivo",
            "grammar_text": "To state how long an action has NOT happened, Spanish uses:\n\n**llevar + [período de tiempo] + sin + infinitivo**\n\n• *Llevo dos semanas sin fumar.* (I haven't smoked for two weeks.)\n• *Llevamos meses sin vernos.* (We haven't seen each other for months.)\n• Contrast with negative 'hace... que': *Lleva un año sin viajar* = *Hace un año que no viaja*.\n• Notice the verb after *sin* is **always** in the infinitive.",
            "table_rows": [
                ["Llevar + tiempo + sin + inf", "Llevo tres días sin dormir bien.", "I haven't slept well for three days."],
                ["Pregunta negativa", "¿Cuánto tiempo llevas sin ver a tu familia?", "How long have you gone without seeing your family?"],
                ["Equivalente con 'hace... que no'", "Hace un mes que no voy al cine.", "I haven't gone to the movies for a month."]
            ],
            "examples": [
                {"spanish": "Llevamos dos semanas sin recibir noticias suyas.", "english": "We have gone two weeks without receiving news from him."},
                {"spanish": "¿Cuánto tiempo llevas sin hacer ejercicio?", "english": "How long have you gone without exercising?"},
                {"spanish": "Llevo casi un año sin comer carne.", "english": "I have gone almost a year without eating meat."}
            ],
            "tip": "Do NOT use a gerund after *sin*: say *sin comer*, never *sin comiendo*.",
            "vocab": [
                {"lemma": "sin parar", "translation": "without stopping", "pos": "expression"},
                {"lemma": "sin falta", "translation": "without fail", "pos": "expression"},
                {"lemma": "abandonar", "translation": "to quit / abandon", "pos": "verb"},
                {"lemma": "dejar de", "translation": "to stop doing", "pos": "verb"},
                {"lemma": "contacto", "translation": "contact", "pos": "noun"},
                {"lemma": "visitar", "translation": "to visit", "pos": "verb"},
                {"lemma": "esperar", "translation": "to wait / hope", "pos": "verb"},
                {"lemma": "paciencia", "translation": "patience", "pos": "noun"},
                {"lemma": "silencio", "translation": "silence", "pos": "noun"},
                {"lemma": "costumbre", "translation": "custom / habit", "pos": "noun"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.03.ex01", "category": "grammar", "type": "multiple-choice", "question": "Llevo dos semanas _____ comer azúcar refinada.", "options": ["sin", "con", "de", "por"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Llevamos tres meses sin _____ a nuestros abuelos.", "answer": "visitar", "english": "We haven't visited our grandparents for three months.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Lleva", "un", "año", "sin", "fumar", "."], "solution": ["Lleva", "un", "año", "sin", "fumar", "."], "english": "He hasn't smoked for a year.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Perdimos el _____ con nuestros antiguos compañeros de clase.", "options": ["contacto", "silencio", "paciencia", "costumbre"], "correct": 0, "teaches": ["a2-unit32-vocab"]},
                {"id": f"a2.{unit_id}.03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "¿Cuánto tiempo llevas _____ ver esa serie?", "answer": "sin", "english": "How long have you gone without watching that series?", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex06", "category": "grammar", "type": "matching", "pairs": [["Llevo días sin dormir", "I haven't slept for days"], ["Lleva meses sin llamar", "He hasn't called for months"], ["Llevamos años sin ir", "We haven't gone for years"], ["Sin falta", "Without fail"]], "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex07", "category": "listening", "type": "listening-choice", "sentence": "¡Cuánto tiempo! Llevábamos por lo menos cinco años sin vernos.", "options": ["Hace cinco años que no se veían.", "Se vieron hace cinco días.", "Se ven todas las semanas."], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex08", "category": "listening", "type": "dictation", "sentence": "Llevo toda la semana sin tomar café.", "english": "I have gone all week without drinking coffee.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Jorge", "text": "¿Has hablado con Lucía recientemente?"}, {"speaker": "Teresa", "text": "No, llevo varias semanas _____ hablar con ella."}], "answer": "sin", "options": ["sin", "con", "de", "para"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Médico", "text": "¿Cuánto tiempo lleva sin hacer ejercicio regular?"}, {"speaker": "Paciente", "text": "Llevo unos seis meses sin _____ deporte."}], "answer": "hacer", "options": ["hacer", "haciendo", "hecho", "hago"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que llevas un mes sin ir al cine.", "answer": "Llevo un mes sin ir al cine."}], "teaches": ["llevar-tiempo-gerundio"]}
            ]
        },
        {
            "num": "04",
            "title": "Ponerse a and Al + Infinitivo: Starting and Simultaneity",
            "goal": "Express sudden inchoative actions with ponerse a + infinitive and temporal simultaneity with al + infinitive.",
            "grammar_title": "Starting and Timing: Ponerse a and Al + Infinitivo",
            "grammar_slug": "ponerse-a-al-infinitivo",
            "grammar_text": "Spanish uses two indispensable structures for narrative pace:\n\n• **Ponerse a + infinitivo** (to suddenly start doing):\n  *De repente, se puso a llover.* (Suddenly it started raining.)\n  *Me puse a limpiar la casa después del desayuno.* (I set about cleaning the house.)\n• **Al + infinitivo** (upon / when doing):\n  *Al llegar a la estación, vi que el tren ya había salido.* (= *Cuando llegué a la estación...*)\n  *Al ver a su amigo, le dio un abrazo.* (= *Cuando vio a su amigo...*)",
            "table_rows": [
                ["Ponerse a + inf (inicio)", "Se puso a llorar de emoción.", "She started crying with emotion."],
                ["Al + inf (simultaneidad temporal)", "Al entrar al museo, compramos la entrada.", "Upon entering the museum, we bought the ticket."],
                ["Equivalencia temporal", "Al llegar = Cuando llegué", "On arriving = When I arrived"]
            ],
            "examples": [
                {"spanish": "Al salir de casa, me di cuenta de que no llevaba las llaves.", "english": "Upon leaving the house, I realized I didn't have the keys."},
                {"spanish": "El bebé se puso a llorar de repente.", "english": "The baby suddenly started crying."},
                {"spanish": "Al terminar la cena, nos pusimos a charlar tranquilamente.", "english": "Upon finishing dinner, we started chatting peacefully."}
            ],
            "tip": "*Al + infinitivo* is one of the most elegant ways in Spanish to say 'when I did X' without having to repeat 'cuando'.",
            "vocab": [
                {"lemma": "ponerse a", "translation": "to start / set about doing", "pos": "verb"},
                {"lemma": "al llegar", "translation": "upon arriving", "pos": "expression"},
                {"lemma": "al ver", "translation": "upon seeing", "pos": "expression"},
                {"lemma": "de repente", "translation": "suddenly", "pos": "adverb"},
                {"lemma": "comenzar a", "translation": "to begin to", "pos": "verb"},
                {"lemma": "lluvia", "translation": "rain", "pos": "noun"},
                {"lemma": "asombro", "translation": "amazement / astonishment", "pos": "noun"},
                {"lemma": "reacción", "translation": "reaction", "pos": "noun"},
                {"lemma": "gritar", "translation": "to shout", "pos": "verb"},
                {"lemma": "entrar", "translation": "to enter", "pos": "verb"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.04.ex01", "category": "grammar", "type": "multiple-choice", "question": "De repente, el cielo se oscureció y se puso a _____ con fuerza.", "options": ["llover", "lloviendo", "llueve", "llovido"], "correct": 0, "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "_____ llegar al hotel, pedimos la llave de la habitación.", "answer": "Al", "english": "Upon arriving at the hotel, we asked for the room key.", "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Al", "ver", "el", "accidente", ",", "llamé", "a", "la", "policía", "."], "solution": ["Al", "ver", "el", "accidente", ",", "llamé", "a", "la", "policía", "."], "english": "Upon seeing the accident, I called the police.", "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Miró el paisaje con un gesto de gran _____.", "options": ["asombro", "lluvia", "reacción", "gritar"], "correct": 0, "teaches": ["a2-unit32-vocab"]},
                {"id": f"a2.{unit_id}.04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Cuando llegaron los invitados, nos pusimos _____ cenar.", "answer": "a", "english": "When the guests arrived, we started having dinner.", "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex06", "category": "grammar", "type": "matching", "pairs": [["Al llegar a casa", "Upon arriving home"], ["Se puso a reír", "He started laughing"], ["Al salir del cine", "Upon leaving the cinema"], ["Me puse a estudiar", "I set about studying"]], "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex07", "category": "listening", "type": "listening-choice", "sentence": "Al escuchar la buena noticia, toda la familia se puso a celebrar.", "options": ["Celebraron al enterarse de la noticia.", "Nadie se alegró de la noticia.", "No supieron qué hacer."], "correct": 0, "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex08", "category": "listening", "type": "dictation", "sentence": "Al cruzar la calle vi a mi viejo amigo.", "english": "Upon crossing the street I saw my old friend.", "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Nuria", "text": "¿Qué hiciste cuando empezó a llover tan fuerte?"}, {"speaker": "David", "text": "_____ ver la tormenta, me metí en una cafetería."}], "answer": "Al", "options": ["Al", "En", "Por", "Para"], "correct": 0, "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Profesor", "text": "Por favor abran el libro en la página cincuenta."}, {"speaker": "Estudiante", "text": "Sí profesor, en seguida nos ponemos _____ leer."}], "answer": "a", "options": ["a", "de", "en", "por"], "correct": 0, "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que al llegar a casa te pusiste a cocinar.", "answer": "Al llegar a casa me puse a cocinar."}], "teaches": ["perifrasis-verbales"]}
            ]
        },
        {
            "num": "05",
            "title": "Mastering Duration and Aspect in Real Life",
            "goal": "Combine acabar de, llevar + gerundio, llevar + sin, and al + infinitivo in complex temporal narratives.",
            "grammar_title": "Integrated Verbal Periphrases of Duration and Aspect",
            "grammar_slug": "perifrasis-aspecto-integradas",
            "grammar_text": "Combining periphrases allows you to articulate life stories with nuanced temporal precision:\n\n• **Immediate past**: *Acabo de terminar mi carrera.* (I just finished my degree.)\n• **Ongoing action**: *Llevo dos años buscando trabajo.* (I've been looking for work for two years.)\n• **Negative duration**: *Llevo meses sin tener una entrevista.* (I haven't had an interview for months.)\n• **Instantaneous trigger**: *Al ver esta oferta, me puse a escribir la solicitud.* (Upon seeing this offer, I set about writing the application.)",
            "table_rows": [
                ["Recién terminado", "acabar de + inf", "Acabo de llegar."],
                ["Duración continuada", "llevar + tiempo + gerundio", "Llevo un año viviendo aquí."],
                ["Duración negativa", "llevar + tiempo + sin + inf", "Llevo días sin dormir."],
                ["Simultaneidad e inicio", "al + inf / ponerse a + inf", "Al oírlo me puse a reír."]
            ],
            "examples": [
                {"spanish": "Acabamos de llegar a Valencia y ya llevamos dos horas paseando por la playa.", "english": "We just arrived in Valencia and we've already been strolling on the beach for two hours."},
                {"spanish": "Al abrir la puerta, me puse a ordenar la habitación.", "english": "Upon opening the door, I set about tidying the room."},
                {"spanish": "Llevaba meses sin verlo cuando nos encontramos por casualidad.", "english": "I hadn't seen him for months when we ran into each other by chance."}
            ],
            "tip": "Pay close attention to whether the following verb is a gerund (*-ando/-iendo*) or an infinitive (*-ar/-er/-ir*).",
            "vocab": [
                {"lemma": "carrera", "translation": "career / degree", "pos": "noun"},
                {"lemma": "solicitud", "translation": "application", "pos": "noun"},
                {"lemma": "casualidad", "translation": "chance / coincidence", "pos": "noun"},
                {"lemma": "pasear", "translation": "to stroll", "pos": "verb"},
                {"lemma": "ordenar", "translation": "to tidy / organize", "pos": "verb"},
                {"lemma": "oferta", "translation": "offer", "pos": "noun"},
                {"lemma": "tranquilamente", "translation": "calmly / peacefully", "pos": "adverb"},
                {"lemma": "maravilla", "translation": "wonder / marvel", "pos": "noun"},
                {"lemma": "rutina", "translation": "routine", "pos": "noun"},
                {"lemma": "experiencia", "translation": "experience", "pos": "noun"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.05.ex01", "category": "grammar", "type": "multiple-choice", "question": "Acabo de _____ la cena para toda la familia.", "options": ["preparar", "preparando", "preparo", "preparé"], "correct": 0, "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Llevo tres años _____ en la misma empresa.", "answer": "trabajando", "english": "I have been working at the same company for three years.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Al", "llegar", "al", "hotel", ",", "nos", "pusimos", "a", "descansar", "."], "solution": ["Al", "llegar", "al", "hotel", ",", "nos", "pusimos", "a", "descansar", "."], "english": "Upon arriving at the hotel, we set about resting.", "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Nos encontramos en el centro por pura _____.", "options": ["casualidad", "rutina", "solicitud", "maravilla"], "correct": 0, "teaches": ["a2-unit32-vocab"]},
                {"id": f"a2.{unit_id}.05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Llevamos varias semanas _____ ver a los primos.", "answer": "sin", "english": "We haven't seen the cousins for several weeks.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.05.ex06", "category": "grammar", "type": "matching", "pairs": [["Acabo de comer", "I just ate"], ["Llevo un mes estudiando", "I've been studying for a month"], ["Llevo días sin fumar", "I haven't smoked for days"], ["Al salir del trabajo", "Upon leaving work"]], "teaches": ["perifrasis-verbales"]},
                {"id": f"a2.{unit_id}.05.ex07", "category": "listening", "type": "listening-choice", "sentence": "Acabo de ver la oferta y al momento me puse a preparar el currículum.", "options": ["Vio la oferta y de inmediato preparó su currículum.", "No tiene tiempo para preparar su currículum.", "Rechazó la oferta."], "correct": 0, "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.05.ex08", "category": "listening", "type": "dictation", "sentence": "Llevo seis meses viviendo en este barrio maravilloso.", "english": "I have been living in this wonderful neighborhood for six months.", "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Sonia", "text": "¿Cuánto tiempo llevas aprendiendo a cocinar?"}, {"speaker": "Raúl", "text": "_____ un año haciendo cursos online."}], "answer": "Llevo", "options": ["Llevo", "Tengo", "Hago", "Estoy"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
                {"id": f"a2.{unit_id}.05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Carmen", "text": "¿Por qué no llamaste antes?"}, {"speaker": "Felipe", "text": "Es que acabo _____ llegar a casa ahora mismo."}], "answer": "de", "options": ["de", "a", "por", "en"], "correct": 0, "teaches": ["acabar-de"]},
                {"id": f"a2.{unit_id}.05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que al llegar a la oficina te pusiste a trabajar.", "answer": "Al llegar a la oficina me puse a trabajar."}], "teaches": ["perifrasis-verbales"]}
            ]
        }
    ]
    
    cons_title = "Consolidation: Verbal Periphrases and Duration"
    cons_goal = "Master all temporal periphrases and expressions of duration for fluent narrative Spanish."
    cons_gr_text = "Verbal periphrases enrich your ability to express aspect and time:\n• *Acabar de + inf*: immediate past\n• *Llevar + tiempo + gerundio*: ongoing duration\n• *Llevar + tiempo + sin + inf*: negative duration\n• *Ponerse a + inf*: sudden beginning\n• *Al + inf*: simultaneous temporal connection."
    cons_table_rows = [
        ["Acabo de terminar", "Immediate past", "I just finished"],
        ["Llevo tres meses viviendo", "Continuing duration", "I've been living for 3 months"],
        ["Llevo días sin dormir", "Negative duration", "I haven't slept for days"],
        ["Al llegar / Se puso a", "Timing & starting", "Upon arriving / Started doing"]
    ]
    cons_examples = [
        {"spanish": "Acabo de llegar y ya me puse a trabajar.", "english": "I just arrived and I already started working."},
        {"spanish": "Llevamos dos horas esperando el tren.", "english": "We've been waiting for the train for two hours."}
    ]
    cons_tip = "Keep gerunds and infinitives distinct: *llevar + gerundio*, but *acabar de + infinitivo* and *sin + infinitivo*."
    
    cons_exs = [
        {"id": f"a2.{unit_id}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "Carlos acaba _____ publicar su nuevo artículo.", "options": ["de", "a", "por", "en"], "correct": 0, "teaches": ["acabar-de"]},
        {"id": f"a2.{unit_id}.cons.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Llevo tres semanas _____ español intensivo.", "answer": "estudiando", "english": "I have been studying intensive Spanish for three weeks.", "teaches": ["llevar-tiempo-gerundio"]},
        {"id": f"a2.{unit_id}.cons.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Al", "ver", "la", "lluvia", ",", "abrí", "el", "paraguas", "."], "solution": ["Al", "ver", "la", "lluvia", ",", "abrí", "el", "paraguas", "."], "english": "Upon seeing the rain, I opened the umbrella.", "teaches": ["perifrasis-verbales"]},
        {"id": f"a2.{unit_id}.cons.ex04", "category": "grammar", "type": "matching", "pairs": [["Acabo de comer", "I just ate"], ["Llevo un mes viviendo", "I've been living for a month"], ["Lleva días sin llamar", "He hasn't called for days"], ["Al salir del tren", "Upon getting off the train"]], "teaches": ["perifrasis-verbales"]},
        {"id": f"a2.{unit_id}.cons.ex05", "category": "listening", "type": "listening-choice", "sentence": "Llevamos más de tres años residiendo en este barrio tan tranquilo.", "options": ["Viven allí desde hace más de tres años.", "Se mudaron la semana pasada.", "Quieren marcharse pronto."], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
        {"id": f"a2.{unit_id}.cons.ex06", "category": "listening", "type": "dictation", "sentence": "Acabo de recibir las entradas para el concierto.", "english": "I have just received the tickets for the concert.", "teaches": ["acabar-de"]},
        {"id": f"a2.{unit_id}.cons.ex07", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Elena", "text": "¿Cuánto tiempo llevas sin fumar?"}, {"speaker": "Marcos", "text": "_____ exactamente seis meses sin probar un cigarrillo."}], "answer": "Llevo", "options": ["Llevo", "Tengo", "Hago", "Estoy"], "correct": 0, "teaches": ["llevar-tiempo-gerundio"]},
        {"id": f"a2.{unit_id}.cons.ex08", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que acabas de ver a un amigo en la calle.", "answer": "Acabo de ver a un amigo en la calle."}], "teaches": ["acabar-de"]}
    ]
    
    story_paras = [
        "Meg y Carlos acaban de bajarse del tren de alta velocidad en la estación Joaquín Sorolla de Valencia.",
        "Llevan casi seis meses estudiando español con mucha dedicación, y este viaje es su primera gran aventura por el Mediterráneo.",
        "Al salir de la moderna estación, el cielo se nubló de golpe y se puso a llover con gran intensidad.",
        "«¡Vaya sorpresa!», exclamó Carlos riendo. «¡Llevábamos semanas sin ver una sola gota de lluvia en Madrid!»",
        "Rápidamente corrieron bajo el toldo de un café tradicional y se pusieron a pedir dos cafés con leche y una ración de churros recién hechos.",
        "Al probar el primer sorbo caliente, Meg sonrió satisfecha: «Acabo de darme cuenta de lo mucho que me gusta viajar por España».",
        "Diez minutos después, la lluvia cesó, salió un sol radiante y ambos se pusieron en marcha hacia el centro histórico."
    ]
    
    generate_unit(
        target_dir, stem_base, unit_id, lessons_data,
        cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs,
        "La escapada a Valencia y la lluvia inesperada",
        "Meg y Carlos viajan en tren a Valencia para celebrar seis meses viviendo en España, enfrentando una repentina tormenta con buen humor.",
        "Valencia", story_paras, 32
    )

# ==========================================
# UNIT 33: Vosotros en España (ES-ES ONLY)
# ==========================================
def build_unit_33(target_dir):
    stem_base = "a2-vosotrospeninsular"
    unit_id = "vosotrospeninsular"
    
    lessons_data = [
        {
            "num": "01",
            "title": "Vosotros in the Present: Speaking to the Group in Spain",
            "goal": "Conjugate regular and irregular verbs in the present indicative for vosotros, using os and vuestro.",
            "grammar_title": "Present Indicative of Vosotros: You All in Spain",
            "grammar_slug": "vosotros-presente-indicativo",
            "grammar_text": "In Spain, **vosotros** (and feminine **vosotras**) is the universal informal plural form used to address friends, colleagues, family, classmates, and peers:\n\n• **Endings in Present Indicative**:\n  - *-ar*: **-áis** (*habláis*, *cantáis*, *estáis*)\n  - *-er*: **-éis** (*coméis*, *leéis*, *tenéis*)\n  - *-ir*: **-ís** (*vivís*, *escribís*, *decís*)\n• **No stem diphthong**: Stem-changing verbs do NOT diphthongize in vosotros: *pensáis* (not piensáis), *queréis* (not quiéreis), *dormís* (not duérmis).\n• **Key Irregulars**: *sois* (ser), *estáis* (estar), *vais* (ir), *tenéis* (tener), *hacéis* (hacer), *sabéis* (saber).\n• **Pronouns**: Object/reflexive clitic: **os** (*¿Cómo os llamáis?*). Possessive: **vuestro / vuestra / vuestros / vuestras** (*vuestra casa*).",
            "table_rows": [
                ["Verbos en -ar", "vosotros habláis / practicáis", "you speak / practice"],
                ["Verbos en -er", "vosotros coméis / tenéis", "you eat / have"],
                ["Verbos en -ir", "vosotros vivís / decís", "you live / say"],
                ["Pronombre clítico", "¿Os apetece un café?", "Do you fancy a coffee?"],
                ["Posesivo", "¿Dónde está vuestro hotel?", "Where is your hotel?"]
            ],
            "examples": [
                {"spanish": "¿Vosotros vivís en el centro de Madrid?", "english": "Do you all live in central Madrid?"},
                {"spanish": "¿A qué hora salís de clase hoy, chicos?", "english": "What time do you guys leave class today?"},
                {"spanish": "¿Os apetece tomar unas tapas esta tarde?", "english": "Do you fancy having some tapas this afternoon?"}
            ],
            "tip": "Vosotros is essential across all regions of Spain! In informal contexts, using 'ustedes' sounds overly distant or theatrical.",
            "vocab": [
                {"lemma": "vosotros", "translation": "you all (informal, masc./mixed)", "pos": "pronoun"},
                {"lemma": "vosotras", "translation": "you all (informal, fem.)", "pos": "pronoun"},
                {"lemma": "vuestro", "translation": "your / yours (masc. sing.)", "pos": "adjective"},
                {"lemma": "vuestra", "translation": "your / yours (fem. sing.)", "pos": "adjective"},
                {"lemma": "chicos", "translation": "guys / kids", "pos": "noun"},
                {"lemma": "compañeros", "translation": "classmates / colleagues", "pos": "noun"},
                {"lemma": "quedar", "translation": "to meet up", "pos": "verb"},
                {"lemma": "tomar algo", "translation": "to have a drink / snack", "pos": "expression"},
                {"lemma": "compartir", "translation": "to share", "pos": "verb"},
                {"lemma": "charlar", "translation": "to chat", "pos": "verb"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.01.ex01", "category": "grammar", "type": "multiple-choice", "question": "¿Vosotros _____ en este barrio desde hace mucho tiempo?", "options": ["vivís", "viven", "vive", "vivo"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "¿A qué hora _____ de trabajar vosotros hoy?", "answer": "salís", "english": "What time do you all get off work today?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["¿", "De", "dónde", "sois", "vosotros", "?", "."], "solution": ["¿", "De", "dónde", "sois", "vosotros", "?", "."], "english": "Where are you all from?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Quedé con mis _____ de la universidad para almorzar.", "options": ["compañeros", "vuestro", "vosotros", "charlar"], "correct": 0, "teaches": ["a2-unit33-vocab"]},
                {"id": f"a2.{unit_id}.01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Chicos, ¿_____ apetece una caña después del trabajo?", "answer": "os", "english": "Guys, do you fancy a beer after work?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex06", "category": "grammar", "type": "matching", "pairs": [["Vosotros sois", "You are (plural)"], ["Vosotros tenéis", "You have (plural)"], ["Vosotros habláis", "You speak (plural)"], ["Vuestra casa", "Your house (plural)"]], "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex07", "category": "listening", "type": "listening-choice", "sentence": "¿Queréis venir con nosotros a tomar algo por La Latina?", "options": ["Invita al grupo a tomar algo.", "Pregunta la hora.", "Dice que no quiere salir."], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex08", "category": "listening", "type": "dictation", "sentence": "¿Cómo os llamáis vosotros?", "english": "What are your names?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Camarero", "text": "¡Hola, buenas tardes! ¿Qué _____ tomar vosotros?"}, {"speaker": "Cliente", "text": "Dos zumos de naranja y unas patatas bravas, por favor."}], "answer": "queréis", "options": ["queréis", "quieren", "quieres", "queremos"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Manuel", "text": "¿Dónde habéis dejado _____ coche?"}, {"speaker": "Bea", "text": "Lo aparcamos en el parking de la plaza."}], "answer": "vuestro", "options": ["vuestro", "su", "tu", "nuestro"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una pregunta para un grupo de amigos preguntando qué hacéis vosotros esta tarde.", "answer": "¿Qué hacéis vosotros esta tarde?"}], "teaches": ["vosotros-indicativo"]}
            ]
        },
        {
            "num": "02",
            "title": "Affirmative Imperative: Hablad, Comed, Vivid, Sentaos!",
            "goal": "Give informal group instructions in Spain using the affirmative imperative of vosotros and handle reflexive forms.",
            "grammar_title": "Affirmative Imperative of Vosotros: Group Commands in Spain",
            "grammar_slug": "vosotros-imperativo-afirmativo",
            "grammar_text": "The affirmative command for *vosotros* is the easiest imperative rule in all of Spanish:\n\n• **Rule**: Take the infinitive, drop the final **-r**, and add a **-d**:\n  - *hablar* -> **hablad** (*¡Hablad más alto!*)\n  - *comer* -> **comed** (*¡Comed despacio!*)\n  - *vivir* -> **vivid** (*¡Vivid la vida!*)\n  - *venir* -> **venid** (*¡Venid aquí, chicos!*)\n  - *hacer* -> **haced** (*¡Haced los deberes!*)\n• **Reflexive Verbs**: When attaching **os**, drop the **-d** to avoid a harsh sound:\n  - *levantar* -> *levantad + os* -> **levantaos** (*¡Levantaos ya!*)\n  - *sentar* -> *sentad + os* -> **sentaos** (*¡Sentaos, por favor!*)\n  - *callar* -> *callad + os* -> **callaos** (*¡Callaos un segundo!*)\n  - *irse* exception: **idos**.",
            "table_rows": [
                ["Regular -ar", "¡Pasad y mirad las fotos!", "Come in and look at the photos!"],
                ["Regular -er", "¡Comed y bebed tranquilos!", "Eat and drink peacefully!"],
                ["Regular -ir", "¡Venid y decid la verdad!", "Come and tell the truth!"],
                ["Verbo reflexivo", "¡Sentaos en el sofá!", "Sit down on the couch! (drop -d)"]
            ],
            "examples": [
                {"spanish": "¡Chicos, venid a ver esto ahora mismo!", "english": "Guys, come see this right now!"},
                {"spanish": "¡Pasad a casa y sentaos donde queráis!", "english": "Come in and sit down wherever you like!"},
                {"spanish": "¡Escuchad con atención las indicaciones del guía!", "english": "Listen carefully to the guide's directions!"}
            ],
            "tip": "Never keep the '-d' when adding reflexive '-os': write *sentaos* (not sentados) and *callaos* (not callados).",
            "vocab": [
                {"lemma": "hablad", "translation": "speak! (vosotros)", "pos": "verb"},
                {"lemma": "comed", "translation": "eat! (vosotros)", "pos": "verb"},
                {"lemma": "venid", "translation": "come! (vosotros)", "pos": "verb"},
                {"lemma": "sentaos", "translation": "sit down! (vosotros)", "pos": "verb"},
                {"lemma": "levantaos", "translation": "stand up! / get up! (vosotros)", "pos": "verb"},
                {"lemma": "escuchad", "translation": "listen! (vosotros)", "pos": "verb"},
                {"lemma": "mirad", "translation": "look! (vosotros)", "pos": "verb"},
                {"lemma": "pasad", "translation": "come in! / pass! (vosotros)", "pos": "verb"},
                {"lemma": "atención", "translation": "attention", "pos": "noun"},
                {"lemma": "instrucción", "translation": "instruction", "pos": "noun"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.02.ex01", "category": "grammar", "type": "multiple-choice", "question": "¡Chicos, _____ aquí que os quiero enseñar una foto!", "options": ["venid", "vengan", "ven", "venis"], "correct": 0, "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "¡Por favor, _____ en estas sillas mientras esperáis!", "answer": "sentaos", "english": "Please, sit down on these chairs while you wait!", "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["¡", "Pasad", "al", "salón", "y", "descansad", "!", "."], "solution": ["¡", "Pasad", "al", "salón", "y", "descansad", "!", "."], "english": "Come into the living room and rest!", "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Presten mucha _____ a las normas de seguridad del edificio.", "options": ["atención", "instrucción", "hablad", "pasad"], "correct": 0, "teaches": ["a2-unit33-vocab"]},
                {"id": f"a2.{unit_id}.02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "¡_____ con atención lo que dice el profesor, compañeros!", "answer": "Escuchad", "english": "Listen carefully to what the teacher says, classmates!", "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex06", "category": "grammar", "type": "matching", "pairs": [["¡Hablad!", "Speak!"], ["¡Comed!", "Eat!"], ["¡Venid!", "Come!"], ["¡Sentaos!", "Sit down!"]], "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex07", "category": "listening", "type": "listening-choice", "sentence": "¡Mirad hacia la derecha para contemplar el acueducto romano!", "options": ["Pide al grupo que mire hacia la derecha.", "Pide que caminen hacia la izquierda.", "Dice que cierren los ojos."], "correct": 0, "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex08", "category": "listening", "type": "dictation", "sentence": "¡Pasad a mi casa y sentaos cómodamente!", "english": "Come into my house and sit comfortably!", "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Anfitrión", "text": "¡Hola a todos! ¡_____ al salón que ya está lista la cena!"}, {"speaker": "Invitados", "text": "¡Muchas gracias, qué bien huele!"}], "answer": "Pasad", "options": ["Pasad", "Pasen", "Pasa", "Pasáis"], "correct": 0, "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Guía", "text": "¡Amigos, _____ aquí junto a la fuente antes de comenzar!"}, {"speaker": "Turistas", "text": "¡Perfecto, ya estamos todos listos!"}], "answer": "venid", "options": ["venid", "vengan", "ven", "venís"], "correct": 0, "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una orden positiva en vosotros diciendo que escuchéis con atención.", "answer": "Escuchad con atención."}], "teaches": ["vosotros-imperativo"]}
            ]
        },
        {
            "num": "03",
            "title": "Vosotros in Past Tenses: Pretérito Perfecto and Indefinido",
            "goal": "Conjugate and distinguish between habéis hablado and hablasteis / comisteis in Peninsular Spanish narratives.",
            "grammar_title": "Past Tenses with Vosotros: Perfecto and Indefinido",
            "grammar_slug": "vosotros-pasados-perfecto-indefinido",
            "grammar_text": "Spanish speakers in Spain constantly use two key past tenses with *vosotros*:\n\n• **Pretérito Perfecto Compuesto**: Used for recent or ongoing time frames (*hoy*, *esta semana*, *ya*, *alguna vez*):\n  **habéis + participio**\n  *¿Habéis comido ya hoy?* (Have you all eaten yet today?)\n  *¿Habéis estado alguna vez en Granada?* (Have you ever been to Granada?)\n• **Pretérito Indefinido**: Used for completed, past time frames (*ayer*, *el año pasado*, *en 2020*):\n  - *-ar*: **-asteis** (*hablasteis*, *viajasteis*, *estudiasteis*)\n  - *-er / -ir*: **-isteis** (*comisteis*, *vivisteis*, *salisteis*)\n  - Irregulars: *fuisteis* (ir/ser), *estuvisteis* (estar), *hicisteis* (hacer), *dijisteis* (decir).\n• Note: In standard Spanish, never add an extra 's' at the end of *-asteis*.",
            "table_rows": [
                ["Perfecto (reciente)", "vosotros habéis hecho / habéis ido", "you have done / have gone"],
                ["Indefinido regular -ar", "vosotros hablasteis / comprasteis", "you spoke / bought"],
                ["Indefinido regular -er/-ir", "vosotros comisteis / salisteis", "you ate / went out"],
                ["Indefinido irregulares", "vosotros fuisteis / hicisteis / dijisteis", "you went / did / said"]
            ],
            "examples": [
                {"spanish": "¿Qué habéis hecho este fin de semana en Madrid?", "english": "What did you all do this weekend in Madrid?"},
                {"spanish": "Ayer fuisteis al Museo del Prado, ¿verdad?", "english": "Yesterday you went to the Prado Museum, right?"},
                {"spanish": "¿Dónde cenasteis anoche después del concierto?", "english": "Where did you all have dinner last night after the concert?"}
            ],
            "tip": "In Spain, if it happened *today*, use *habéis hecho*; if it happened *yesterday*, use *hicisteis*.",
            "vocab": [
                {"lemma": "habéis", "translation": "you have (vosotros)", "pos": "auxiliary"},
                {"lemma": "fuisteis", "translation": "you went / were (vosotros)", "pos": "verb"},
                {"lemma": "hicisteis", "translation": "you did / made (vosotros)", "pos": "verb"},
                {"lemma": "visteis", "translation": "you saw (vosotros)", "pos": "verb"},
                {"lemma": "dijisteis", "translation": "you said (vosotros)", "pos": "verb"},
                {"lemma": "ayer", "translation": "yesterday", "pos": "adverb"},
                {"lemma": "este fin de semana", "translation": "this weekend", "pos": "expression"},
                {"lemma": "excursión", "translation": "outing / trip", "pos": "noun"},
                {"lemma": "pasarlo bien", "translation": "to have a good time", "pos": "expression"},
                {"lemma": "reunión", "translation": "meeting / gathering", "pos": "noun"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.03.ex01", "category": "grammar", "type": "multiple-choice", "question": "Chicos, ¿qué _____ hecho hoy por la mañana?", "options": ["habéis", "han", "has", "hemos"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Ayer vosotros _____ al cine a ver la nueva película.", "answer": "fuisteis", "english": "Yesterday you all went to the cinema to see the new movie.", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["¿", "Dónde", "comisteis", "vosotros", "ayer", "?", "."], "solution": ["¿", "Dónde", "comisteis", "vosotros", "ayer", "?", "."], "english": "Where did you all eat yesterday?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Hicimos una _____ inolvidable a la sierra de Guadarrama.", "options": ["excursión", "reunión", "ayer", "habéis"], "correct": 0, "teaches": ["a2-unit33-vocab"]},
                {"id": f"a2.{unit_id}.03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "¿Vosotros ya _____ visitado el Palacio Real esta semana?", "answer": "habéis", "english": "Have you already visited the Royal Palace this week?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex06", "category": "grammar", "type": "matching", "pairs": [["Habéis visto", "You have seen"], ["Fuisteis", "You went"], ["Hicisteis", "You did"], ["Comisteis", "You ate"]], "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex07", "category": "listening", "type": "listening-choice", "sentence": "¿Lo pasasteis bien vosotros en la fiesta del sábado?", "options": ["Pregunta si disfrutaron en la fiesta.", "Pregunta la hora de la fiesta.", "Dice que la fiesta fue aburrida."], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex08", "category": "listening", "type": "dictation", "sentence": "¿A qué hora llegasteis a Madrid anoche?", "english": "What time did you arrive in Madrid last night?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Marta", "text": "¡Hola chicos! ¿Qué tal la escapada a Toledo?"}, {"speaker": "Lucas", "text": "¡Increíble! _____ muchísimas fotos por las calles históricas."}], "answer": "Hicimos", "options": ["Hicimos", "Hicisteis", "Han hecho", "Hizo"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Carlos", "text": "Chicos, ¿_____ terminado ya de almorzar?"}, {"speaker": "Amigos", "text": "Sí, acabamos de terminar ahora mismo."}], "answer": "habéis", "options": ["habéis", "han", "has", "hemos"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una pregunta en vosotros para saber adónde fuisteis ayer.", "answer": "¿Adónde fuisteis ayer vosotros?"}], "teaches": ["vosotros-indicativo"]}
            ]
        },
        {
            "num": "04",
            "title": "Sociolinguistic Registers in Spain: Vosotros vs. Ustedes",
            "goal": "Apply the correct social registers in Spain: using vosotros for peers and ustedes for formal distance.",
            "grammar_title": "Social Distance and Register: Vosotros vs. Ustedes in Spain",
            "grammar_slug": "vosotros-vs-ustedes-espana",
            "grammar_text": "In Peninsular Spanish, the distinction between **vosotros** and **ustedes** reflects social relationship and hierarchy:\n\n• **Vosotros** (tuteo plural): Used with anyone you would call *tú* individually:\n  - Friends, colleagues, peers, classmates, relatives, neighbours, children.\n  - Shopkeepers and waitstaff addressing young or peer customers.\n• **Ustedes** (formal plural): Conjugates in third-person plural (*ustedes hablan*, *ustedes tienen*). Reserved strictly for:\n  - Elderly strangers as a mark of generational respect.\n  - Official legal, judicial, and police interactions.\n  - Highly formal institutional ceremonies or luxury corporate settings.\n• In Latin America, *ustedes* replaces *vosotros* entirely, but in Spain, using *ustedes* with friends sounds cold or comical!",
            "table_rows": [
                ["Plural informal (España)", "vosotros habláis / ¿os apetece?", "Friends, peers, family"],
                ["Plural formal (España)", "ustedes hablan / ¿les apetece?", "Elderly, formal authority"],
                ["Vocabulario coloquial", "chavales, colegas, pandilla", "Colloquial peer group terms"],
                ["Trato social", "tutear (usar tú/vosotros)", "To speak informally"]
            ],
            "examples": [
                {"spanish": "—Buenas tardes señores, ¿tienen ustedes reserva? (Formal)", "english": "—Good afternoon gentlemen, do you have a reservation? (Formal)"},
                {"spanish": "—¡Hola chicos! ¿Qué os pongo? (Informal Peninsular)", "english": "—Hey guys! What can I get you? (Informal Peninsular)"},
                {"spanish": "En esta oficina todos nos tuteamos y nos llamamos de vosotros.", "english": "In this office we all use informal address with each other."}
            ],
            "tip": "When in Spain, if people your age speak to you in a bar or café, they will almost always address your group as *vosotros*.",
            "vocab": [
                {"lemma": "chavales", "translation": "kids / youngsters (colloquial Spain)", "pos": "noun"},
                {"lemma": "colegas", "translation": "pals / buddies (Spain)", "pos": "noun"},
                {"lemma": "pandilla", "translation": "circle of friends / group", "pos": "noun"},
                {"lemma": "quedada", "translation": "get-together / meetup", "pos": "noun"},
                {"lemma": "tapeo", "translation": "tapas-hopping (Spain)", "pos": "noun"},
                {"lemma": "barrio", "translation": "neighborhood", "pos": "noun"},
                {"lemma": "tutear", "translation": "to address with tú / vosotros", "pos": "verb"},
                {"lemma": "trato", "translation": "form of address / treatment", "pos": "noun"},
                {"lemma": "respeto", "translation": "respect", "pos": "noun"},
                {"lemma": "tertulia", "translation": "informal social chat / gathering", "pos": "noun"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.04.ex01", "category": "grammar", "type": "multiple-choice", "question": "Al hablar con un grupo de amigos jóvenes en Madrid, se utiliza siempre _____.", "options": ["vosotros", "ustedes", "ellos", "nosotros"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Chicos, ¿_____ apetece ir de tapeo esta noche?", "answer": "os", "english": "Guys, do you fancy going for tapas tonight?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["En", "España", "los", "amigos", "se", "tratan", "de", "vosotros", "."], "solution": ["En", "España", "los", "amigos", "se", "tratan", "de", "vosotros", "."], "english": "In Spain friends address each other with vosotros.", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Vamos a organizar una _____ el viernes por la noche en Malasaña.", "options": ["quedada", "respeto", "trato", "tutear"], "correct": 0, "teaches": ["a2-unit33-vocab"]},
                {"id": f"a2.{unit_id}.04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Disculpen señores ancianos, ¿_____ ustedes la calle Mayor?", "answer": "conocen", "english": "Excuse me elderly gentlemen, do you know Mayor Street?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex06", "category": "grammar", "type": "matching", "pairs": [["Vosotros (amigos)", "You informal plural"], ["Ustedes (formal)", "You formal plural"], ["Ir de tapeo", "Going for tapas"], ["Colegas", "Buddies / pals"]], "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex07", "category": "listening", "type": "listening-choice", "sentence": "¡Hombre, chavales! ¿Adónde vais tan deprisa?", "options": ["Saluda a un grupo de jóvenes amigos.", "Habla con dos policías.", "Pide la cuenta en un restaurante."], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex08", "category": "listening", "type": "dictation", "sentence": "¿A vosotros os gusta la comida tradicional española?", "english": "Do you all like traditional Spanish food?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Camarero", "text": "¡Buenas! ¿Qué os pongo de beber, chicos?"}, {"speaker": "Cliente", "text": "Para nosotros dos cañas, por favor. ¿_____ tapas con la bebida?"}], "answer": "Ponéis", "options": ["Ponéis", "Ponen", "Pones", "Pongo"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Policía", "text": "Buenas noches señores. ¿Pueden _____ mostrarme sus documentos?"}, {"speaker": "Ciudadanos", "text": "Por supuesto oficial, aquí los tiene."}], "answer": "ustedes", "options": ["ustedes", "vosotros", "ellos", "nosotros"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase preguntando informalmente a tus amigos si tenéis hambre.", "answer": "Chicos, ¿tenéis hambre vosotros?"}], "teaches": ["vosotros-indicativo"]}
            ]
        },
        {
            "num": "05",
            "title": "An Evening with Friends in Madrid: Integrated Vosotros",
            "goal": "Demonstrate seamless, authentic usage of vosotros across indicative, imperative, past, and clitics in social Spanish.",
            "grammar_title": "Full Synthesis of Vosotros Forms in Peninsular Spanish",
            "grammar_slug": "vosotros-sintesis-completa",
            "grammar_text": "To sound natural and confident living or traveling in Spain, weave together all dimensions of *vosotros*:\n\n• **Greeting & invitation**: *¡Pasad, chicos! ¿Qué queréis tomar?*\n• **Inquiries**: *¿A qué hora salisteis ayer? ¿Habéis estado ya en el Retiro?*\n• **Imperatives & reflexives**: *¡Sentaos aquí! ¡Mirad qué fotos tan chulas! ¡Venid a la cocina!*\n• **Pronoun coordination**: *¿Os ha gustado la paella? Vuestra visita nos alegra un montón.*",
            "table_rows": [
                ["Presente", "¿Qué queréis hacer?", "What do you want to do?"],
                ["Imperativo", "¡Sentaos y comed!", "Sit down and eat!"],
                ["Pretérito", "¿Qué hicisteis ayer?", "What did you do yesterday?"],
                ["Pronombres", "os apetece / vuestro piso", "you fancy / your flat"]
            ],
            "examples": [
                {"spanish": "¡Chicos, venid y probad estas tapas tan ricas!", "english": "Guys, come and try these delicious tapas!"},
                {"spanish": "¿Dónde comprasteis vosotros estas entradas?", "english": "Where did you all buy these tickets?"},
                {"spanish": "¿Habéis descansado bien en vuestro hotel?", "english": "Did you rest well in your hotel?"}
            ],
            "tip": "Active practice of vosotros is the quickest way to feel truly integrated into life in Spain!",
            "vocab": [
                {"lemma": "chulo", "translation": "cool / lovely (Spain)", "pos": "adjective"},
                {"lemma": "tapeo", "translation": "tapas crawl", "pos": "noun"},
                {"lemma": "caña", "translation": "small draft beer (Spain)", "pos": "noun"},
                {"lemma": "montón", "translation": "a ton / whole lot", "pos": "noun"},
                {"lemma": "alegrar", "translation": "to make happy", "pos": "verb"},
                {"lemma": "escapada", "translation": "getaway / short trip", "pos": "noun"},
                {"lemma": "visita", "translation": "visit", "pos": "noun"},
                {"lemma": "probar", "translation": "to taste / try", "pos": "verb"},
                {"lemma": "descansar", "translation": "to rest", "pos": "verb"},
                {"lemma": "genial", "translation": "great / brilliant", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.05.ex01", "category": "grammar", "type": "multiple-choice", "question": "¡Chicos, _____ a mi piso cuando queráis!", "options": ["venid", "vengan", "ven", "venís"], "correct": 0, "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "¿A qué hora _____ de casa anoche vosotros?", "answer": "salisteis", "english": "What time did you leave home last night?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["¡", "Sentaos", "en", "el", "sofá", "y", "descansad", "!", "."], "solution": ["¡", "Sentaos", "en", "el", "sofá", "y", "descansad", "!", "."], "english": "Sit down on the couch and rest!", "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Esa chaqueta de cuero te queda súper _____.", "options": ["chula", "montón", "tapeo", "caña"], "correct": 0, "teaches": ["a2-unit33-vocab"]},
                {"id": f"a2.{unit_id}.05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Chicos, ¿ya _____ probado el jamón ibérico?", "answer": "habéis", "english": "Guys, have you already tasted the Iberian ham?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.05.ex06", "category": "grammar", "type": "matching", "pairs": [["Vosotros tenéis", "You all have"], ["¡Venid aquí!", "Come here!"], ["Fuisteis ayer", "You went yesterday"], ["Vuestro amigo", "Your friend"]], "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.05.ex07", "category": "listening", "type": "listening-choice", "sentence": "¡Pasad chicos, qué alegría verte a ti y a Carlos en Madrid!", "options": ["Les da la bienvenida a su casa con alegría.", "Se despide de ellos en la estación.", "No los reconoce."], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.05.ex08", "category": "listening", "type": "dictation", "sentence": "¿Dónde comprasteis vosotros estas camisetas tan chulas?", "english": "Where did you all buy these cool t-shirts?", "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Anfitrión", "text": "¡Chicos, no os quedéis ahí de pie! ¡_____ en el salón!"}, {"speaker": "Carlos", "text": "¡Muchas gracias, qué piso más acogedor tenéis!"}], "answer": "Sentaos", "options": ["Sentaos", "Siéntense", "Sienta", "Sentaros"], "correct": 0, "teaches": ["vosotros-imperativo"]},
                {"id": f"a2.{unit_id}.05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Elena", "text": "Chicos, ¿qué _____ hacer este fin de semana?"}, {"speaker": "Meg", "text": "Queremos ir a Segovia si hace buen tiempo."}], "answer": "pensáis", "options": ["pensáis", "piensan", "piensas", "pensamos"], "correct": 0, "teaches": ["vosotros-indicativo"]},
                {"id": f"a2.{unit_id}.05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una invitación en vosotros diciendo que paséis a tomar un café.", "answer": "Pasad a tomar un café chicos."}], "teaches": ["vosotros-imperativo"]}
            ]
        }
    ]
    
    cons_title = "Consolidation: Vosotros in Peninsular Spanish"
    cons_goal = "Demonstrate complete mastery of vosotros forms for authentic daily communication in Spain."
    cons_gr_text = "Vosotros is the heartbeat of social interaction in Spain:\n• Presente: *-áis, -éis, -ís*\n• Imperativo: infinitive minus *-r* plus *-d* (*hablad, venid*), reflexive drops *-d* (*sentaos*)\n• Pasados: *habéis hablado* (hoy), *hablasteis* (ayer)\n• Pronombres: *os* y *vuestro/a/os/as*."
    cons_table_rows = [
        ["Presente", "vosotros habláis / vivís", "You speak / live"],
        ["Imperativo", "¡hablad! / ¡sentaos!", "Speak! / Sit down!"],
        ["Perfecto", "habéis comido hoy", "You have eaten today"],
        ["Indefinido", "fuisteis / comisteis ayer", "You went / ate yesterday"]
    ]
    cons_examples = [
        {"spanish": "¡Chicos, venid a casa y tomad algo!", "english": "Guys, come home and have a drink!"},
        {"spanish": "¿Vosotros fuisteis al concierto anoche?", "english": "Did you go to the concert last night?"}
    ]
    cons_tip = "Embrace vosotros freely whenever chatting with peers, colleagues, or groups of friends across Spain."
    
    cons_exs = [
        {"id": f"a2.{unit_id}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "¿Vosotros _____ ganas de salir a dar un paseo?", "options": ["tenéis", "tienen", "tienes", "tenemos"], "correct": 0, "teaches": ["vosotros-indicativo"]},
        {"id": f"a2.{unit_id}.cons.ex02", "category": "grammar", "type": "fill-blank", "sentence": "¡Chicos, _____ aquí a ver esto!", "answer": "venid", "english": "Guys, come here to see this!", "teaches": ["vosotros-imperativo"]},
        {"id": f"a2.{unit_id}.cons.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["¿", "Qué", "hicisteis", "vosotros", "el", "sábado", "?", "."], "solution": ["¿", "Qué", "hicisteis", "vosotros", "el", "sábado", "?", "."], "english": "What did you all do on Saturday?", "teaches": ["vosotros-indicativo"]},
        {"id": f"a2.{unit_id}.cons.ex04", "category": "grammar", "type": "matching", "pairs": [["Vosotros sois", "You are (plural)"], ["¡Escuchad!", "Listen! (plural)"], ["Habéis venido", "You came (today)"], ["Vuestro coche", "Your car"]], "teaches": ["vosotros-indicativo"]},
        {"id": f"a2.{unit_id}.cons.ex05", "category": "listening", "type": "listening-choice", "sentence": "¡Pasad y sentaos donde queráis, estáis en vuestra casa!", "options": ["Les invita a entrar y sentarse con total confianza.", "Les pide que esperen fuera.", "No quiere visitas hoy."], "correct": 0, "teaches": ["vosotros-indicativo"]},
        {"id": f"a2.{unit_id}.cons.ex06", "category": "listening", "type": "dictation", "sentence": "¿A qué hora salisteis vosotros de la fiesta?", "english": "What time did you leave the party?", "teaches": ["vosotros-indicativo"]},
        {"id": f"a2.{unit_id}.cons.ex07", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Pablo", "text": "¡Hola chavales! ¿Qué tal la excursión?"}, {"speaker": "Amigos", "text": "¡Genial! ¿_____ vosotros al final el museo?"}], "answer": "Visteis", "options": ["Visteis", "Vieron", "Viste", "Vimos"], "correct": 0, "teaches": ["vosotros-indicativo"]},
        {"id": f"a2.{unit_id}.cons.ex08", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una orden afirmativa en vosotros diciendo que miréis aquí.", "answer": "Mirad aquí chicos."}], "teaches": ["vosotros-imperativo"]}
    ]
    
    story_paras = [
        "Es viernes por la noche y el madrileño barrio de Malasaña vibra con música, luces y risas en cada esquina.",
        "Carlos y Meg han quedado con sus amigos españoles Javier, Lucía y Marcos en una tradicional taberna de la plaza del Dos de Mayo.",
        "«¡Hombre, chavales! ¡Por fin habéis llegado!», exclama Javier levantándose con los brazos abiertos.",
        "«¡Pasad y sentaos aquí con nosotros!», añade Lucía sonriendo. «Os hemos guardado un sitio estupendo junto a la ventana».",
        "El camarero se acerca con una libreta y pregunta amablemente: «¡Hola chicos! ¿Qué os pongo de beber hoy?»",
        "«Ponnos unas cañas y una ración de patatas bravas bien picantes», responde Carlos sintiéndose ya totalmente como en casa.",
        "Durante toda la velada, charlan de sus viajes, de cómo pasaron el fin de semana anterior y planean una escapada a la sierra. «¡Qué bien os habéis adaptado a la vida en España!», concluye Marcos brindando por la amistad."
    ]
    
    generate_unit(
        target_dir, stem_base, unit_id, lessons_data,
        cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs,
        "La quedada de amigos en Malasaña",
        "Carlos y Meg se reúnen con sus amigos españoles en una animada taberna de Madrid, viviendo una noche de tapeo y auténtica tertulia con vosotros.",
        "Madrid", story_paras, 33
    )

def update_curriculum(path, new_units):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    existing_titles = {u["title"] for u in data}
    added = 0
    for u in new_units:
        if u["title"] not in existing_titles:
            data.append(u)
            added += 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Updated {path}: added {added} units.")

if __name__ == "__main__":
    print("Generating Unit 31 (indefinidosnegacion)...")
    build_unit_31(ES_ES)
    build_unit_31(ES_LATAM)
    
    print("Generating Unit 32 (perifrasisduracion)...")
    build_unit_32(ES_ES)
    build_unit_32(ES_LATAM)
    
    print("Generating Unit 33 (vosotrospeninsular - ES-ES only)...")
    build_unit_33(ES_ES)
    
    u31 = {
        "title": "Indefinites and Double Negation: Alguien, Nadie, Algo, Nada",
        "stems": [
            "a2-indefinidosnegacion-01",
            "a2-indefinidosnegacion-02",
            "a2-indefinidosnegacion-03",
            "a2-indefinidosnegacion-04",
            "a2-indefinidosnegacion-05",
            "a2-indefinidosnegacion-consolidation"
        ]
    }
    u32 = {
        "title": "Life in Duration and Recent Actions: Verbal Periphrases",
        "stems": [
            "a2-perifrasisduracion-01",
            "a2-perifrasisduracion-02",
            "a2-perifrasisduracion-03",
            "a2-perifrasisduracion-04",
            "a2-perifrasisduracion-05",
            "a2-perifrasisduracion-consolidation"
        ]
    }
    u33 = {
        "title": "Speaking to the Group: Vosotros in Spain",
        "stems": [
            "a2-vosotrospeninsular-01",
            "a2-vosotrospeninsular-02",
            "a2-vosotrospeninsular-03",
            "a2-vosotrospeninsular-04",
            "a2-vosotrospeninsular-05",
            "a2-vosotrospeninsular-consolidation"
        ]
    }
    
    update_curriculum(ES_ES / "curriculum/units/a2.json", [u31, u32, u33])
    update_curriculum(ES_LATAM / "curriculum/units/a2.json", [u31, u32])
    print("A2 Units 31-33 generated and wired successfully!")
