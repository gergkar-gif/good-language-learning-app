# -*- coding: utf-8 -*-
"""
Generate Phase 11: Spanish B1 Core Missing Grammar Additions (Units 37–40)
- Unit 37: Pretérito Perfecto de Subjuntivo (b1-37)
- Unit 38: Correlación Temporal del Subjuntivo & Estilo Indirecto (b1-38)
- Unit 39: Verbos de Cambio (b1-39)
- Unit 40: Régimen Preposicional Avanzado, Sino vs Pero, Lo Neutro (b1-40)
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

def make_lesson(lesson_id, title, goal, grammar_label, stem, vocab_ref, exercise_refs, checklist_items):
    sections = [
        {"type": "goal", "title": "Lesson Goals", "items": [goal]},
        {"type": "recycle"},
        {"type": "grammar", "ref": f"grammar/b1/{stem}-gr.json"}
    ]
    if vocab_ref:
        sections.append({"type": "vocabulary", "title": "Lesson Vocabulary", "ref": vocab_ref})
    
    if len(exercise_refs) >= 11:
        sections.extend([
            {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b1/{stem}-ex.json", "exerciseRefs": exercise_refs[0:6]},
            {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b1/{stem}-ex.json", "exerciseRefs": exercise_refs[6:8]},
            {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b1/{stem}-ex.json", "exerciseRefs": exercise_refs[8:10]},
            {"type": "exercise-group", "title": "Writing", "ref": f"exercises/b1/{stem}-ex.json", "exerciseRefs": exercise_refs[10:11]}
        ])
    else:
        sections.append({"type": "exercise-group", "title": "Review Practice", "ref": f"exercises/b1/{stem}-ex.json", "exerciseRefs": exercise_refs})
        
    sections.append({"type": "srs", "title": "Add to Review"})
    sections.append({"type": "checklist", "title": "Can you do this?", "items": checklist_items})
    
    return {
        "id": lesson_id,
        "title": title,
        "level": "B1",
        "goal": goal,
        "grammar": grammar_label,
        "metadata": {"estimatedMinutes": 20},
        "sections": sections
    }

def generate_b1_unit(target_dir, unit_num, unit_title, lessons_data, cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs):
    stem_base = f"b1-{unit_num}"
    
    for ld in lessons_data:
        stem = f"{stem_base}-{ld['num']}"
        les_id = f"lesson.b1.{unit_num}.{ld['num']}"
        
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
            f"vocabulary/b1/{stem}-voc.json",
            ex_refs,
            [f"I understand how to use {ld['grammar_title'].lower()} in real B1 contexts."]
        )
        write_json(target_dir / f"lessons/b1/{stem}.json", les_obj)
        
        clean_rows = [r[:2] for r in ld['table_rows']]
        gr_obj = {
            "id": f"grammar.b1.{unit_num}.{ld['num']}.{ld['grammar_slug']}",
            "title": ld['grammar_title'],
            "sections": [
                {"type": "text", "content": ld['grammar_text']},
                {"type": "table", "title": "Rules and Patterns", "rows": clean_rows},
                {"type": "examples", "items": ld['examples']},
                {"type": "tip", "content": ld['tip']}
            ]
        }
        write_json(target_dir / f"grammar/b1/{stem}-gr.json", gr_obj)
        
        voc_obj = {
            "id": f"vocab.b1.{unit_num}.{ld['num']}",
            "lesson": stem,
            "title": f"Vocabulary: {ld['title']}",
            "theme": f"B1 Unit {unit_num}",
            "words": ld['vocab']
        }
        write_json(target_dir / f"vocabulary/b1/{stem}-voc.json", voc_obj)
        
        ex_obj = {
            "lesson": stem,
            "exercises": ld['exs']
        }
        write_json(target_dir / f"exercises/b1/{stem}-ex.json", ex_obj)
        
    cons_stem = f"{stem_base}-consolidation"
    cons_les_id = f"lesson.b1.{unit_num}.consolidation"
    for ex in cons_exs:
        if ex.get('type') == 'dialogue-complete' and 'answer' in ex:
            del ex['answer']
    cons_refs = [ex['id'] for ex in cons_exs]
    cons_les_obj = make_lesson(cons_les_id, cons_title, cons_goal, f"b1-{unit_num} consolidación", cons_stem, None, cons_refs, ["I can confidently apply these advanced structures in communication."])
    write_json(target_dir / f"lessons/b1/{cons_stem}.json", cons_les_obj)
    
    clean_cons_rows = [r[:2] for r in cons_table_rows]
    cons_gr_obj = {
        "id": f"grammar.b1.{unit_num}.consolidation.resumen",
        "title": f"Summary: {cons_title}",
        "sections": [
            {"type": "text", "content": cons_gr_text},
            {"type": "table", "title": "Quick Reference Table", "rows": clean_cons_rows},
            {"type": "examples", "items": cons_examples},
            {"type": "tip", "content": cons_tip}
        ]
    }
    write_json(target_dir / f"grammar/b1/{cons_stem}-gr.json", cons_gr_obj)
    write_json(target_dir / f"exercises/b1/{cons_stem}-ex.json", {"lesson": cons_stem, "exercises": cons_exs})
    print(f"B1 Unit {unit_num} ({unit_title}) generated successfully in {target_dir}")

# ==========================================
# UNIT 37: Pretérito Perfecto de Subjuntivo
# ==========================================
def build_unit_37(target_dir):
    unit_num = "37"
    unit_title = "The Past in the Mind: Present Perfect Subjunctive"
    
    lessons_data = [
        {
            "num": "01",
            "title": "Formation of the Pretérito Perfecto de Subjuntivo",
            "goal": "Conjugate the present perfect subjunctive with haya, hayas, haya, hayamos, hayáis, hayan + participio.",
            "grammar_title": "Formation of the Present Perfect Subjunctive",
            "grammar_slug": "formacion-perfecto-subjuntivo",
            "grammar_text": "The **pretérito perfecto de subjuntivo** is formed by combining the present subjunctive of *haber* with the past participle:\n\n• **haber**: *haya, hayas, haya, hayamos, hayáis, hayan*\n• **participio**: *-ado* (hablado), *-ido* (vivido)\n• **Irregular participles**: *dicho, hecho, puesto, visto, escrito, vuelto, abierto, roto*.\n\nIt refers to completed past actions connected to present attitudes, feelings, or doubts.",
            "table_rows": [
                ["yo haya hablado / vivido", "I have spoken / lived"],
                ["tú hayas comido / dicho", "you have eaten / said"],
                ["él/ella haya hecho / visto", "he/she has made / seen"],
                ["nosotros hayamos salido", "we have gone out"],
                ["ellos hayan llegado", "they have arrived"]
            ],
            "examples": [
                {"spanish": "Espero que hayas tenido un buen viaje.", "english": "I hope you have had a good trip."},
                {"spanish": "Me alegro de que hayamos terminado a tiempo.", "english": "I am glad that we have finished on time."},
                {"spanish": "Dudo que hayan recibido el paquete todavía.", "english": "I doubt they have received the package yet."}
            ],
            "tip": "The participle never changes gender or number in compound tenses: always *haya llegado / hayan llegado*.",
            "vocab": [
                {"lemma": "participio", "translation": "participle", "pos": "noun"},
                {"lemma": "alegrarse", "translation": "to be glad / rejoice", "pos": "verb"},
                {"lemma": "llegada", "translation": "arrival", "pos": "noun"},
                {"lemma": "recibido", "translation": "received", "pos": "adjective"},
                {"lemma": "noticia", "translation": "news", "pos": "noun"},
                {"lemma": "comprobar", "translation": "to check / verify", "pos": "verb"},
                {"lemma": "asunto", "translation": "matter / issue", "pos": "noun"},
                {"lemma": "resultado", "translation": "result", "pos": "noun"},
                {"lemma": "logro", "translation": "achievement", "pos": "noun"},
                {"lemma": "completar", "translation": "to complete", "pos": "verb"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-01.ex01", "category": "grammar", "type": "multiple-choice", "question": "Espero que tú _____ descansado bien este fin de semana.", "options": ["hayas", "hayis", "has", "hubieras"], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Me alegro mucho de que nosotros _____ ganado el concurso.", "answer": "hayamos", "english": "I am very glad that we have won the contest.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Espero", "que", "hayas", "tenido", "un", "buen", "viaje", "."], "solution": ["Espero", "que", "hayas", "tenido", "un", "buen", "viaje", "."], "english": "I hope you have had a good trip.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Obtuvimos un excelente _____ en la evaluación final.", "options": ["resultado", "llegada", "participio", "asunto"], "correct": 0, "teaches": ["b1-unit37-vocab"]},
                {"id": f"b1-{unit_num}-01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Es fantástico que Juan _____ conseguido el trabajo.", "answer": "haya", "english": "It is fantastic that Juan has gotten the job.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex06", "category": "grammar", "type": "matching", "pairs": [["Que hayas venido", "That you have come"], ["Que hayamos visto", "That we have seen"], ["Que hayan dicho", "That they have said"], ["Que haya terminado", "That it has ended"]], "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex07", "category": "listening", "type": "listening-choice", "sentence": "Es una lástima que no hayan podido venir a la fiesta de aniversario.", "options": ["Lamenta que no hayan asistido.", "Se alegra de que hayan venido.", "Pregunta si van a venir."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex08", "category": "listening", "type": "dictation", "sentence": "Espero que hayas recibido mi mensaje a tiempo.", "english": "I hope you have received my message on time.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Ana", "text": "¡Por fin estamos en el hotel!"}, {"speaker": "Carlos", "text": "____."}], "options": ["Me alegro de que hayamos llegado bien.", "Me alegro de que llegamos ayer.", "Espero que llegábamos."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Profesor", "text": "¿Ha terminado todo el mundo el ejercicio?"}, {"speaker": "Alumnos", "text": "____."}], "options": ["Sí profesor, nos alegra que hayamos terminado.", "No profesor, nos alegra que termináramos.", "Ojalá terminamos."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase deseando que tu amigo haya tenido un buen día.", "answer": "Espero que hayas tenido un buen día."}], "teaches": ["subjuntivo-perfecto"]}
            ]
        },
        {
            "num": "02",
            "title": "Feelings and Judgments on Recent Events",
            "goal": "Express emotions, relief, and evaluations about past events using the present perfect subjunctive.",
            "grammar_title": "Feelings and Value Judgments with Past Events",
            "grammar_slug": "emociones-juicios-perfecto-subjuntivo",
            "grammar_text": "When expressing present feelings or value judgments about an action that already happened, use the present perfect subjunctive:\n\n• *Me alegro de que hayas venido.* (I am glad you came / have come.)\n• *Siento mucho que no hayas aprobado el examen.* (I am sorry you didn't pass the exam.)\n• *Es fantástico / una lástima que hayan tomado esa decisión.* (It is fantastic / a pity that they made that decision.)",
            "table_rows": [
                ["Me alegro de que...", "Me alegro de que hayas llamado."],
                ["Siento mucho que...", "Siento que no hayan venido."],
                ["Es una lástima que...", "Es una lástima que se haya roto."],
                ["Es fantástico que...", "Es fantástico que hayas vuelto."]
            ],
            "examples": [
                {"spanish": "Me parece maravilloso que hayáis encontrado esa oportunidad.", "english": "I find it wonderful that you found that opportunity."},
                {"spanish": "Siento que el concierto se haya cancelado por la lluvia.", "english": "I'm sorry the concert was cancelled because of the rain."},
                {"spanish": "Es una pena que no nos hayamos visto antes.", "english": "It's a pity we haven't seen each other sooner."}
            ],
            "tip": "Even though English often uses the simple past ('glad you came'), Spanish requires *hayas venido* because the emotion is felt now.",
            "vocab": [
                {"lemma": "maravilloso", "translation": "wonderful", "pos": "adjective"},
                {"lemma": "lástima", "translation": "pity / shame", "pos": "noun"},
                {"lemma": "oportunidad", "translation": "opportunity", "pos": "noun"},
                {"lemma": "cancelar", "translation": "to cancel", "pos": "verb"},
                {"lemma": "alivio", "translation": "relief", "pos": "noun"},
                {"lemma": "aprobar", "translation": "to pass (exam)", "pos": "verb"},
                {"lemma": "sorprendente", "translation": "surprising", "pos": "adjective"},
                {"lemma": "pena", "translation": "sorrow / pity", "pos": "noun"},
                {"lemma": "lamentar", "translation": "to regret / lament", "pos": "verb"},
                {"lemma": "reaccionar", "translation": "to react", "pos": "verb"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-02.ex01", "category": "grammar", "type": "multiple-choice", "question": "Es una pena que Pedro no _____ podido asistir a la fiesta.", "options": ["haya", "ha", "hubo", "había"], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Me alegro de que vosotros _____ aprobado todos los exámenes.", "answer": "hayáis", "english": "I am glad that you all have passed all the exams.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Siento", "mucho", "que", "te", "hayas", "lastimado", "."], "solution": ["Siento", "mucho", "que", "te", "hayas", "lastimado", "."], "english": "I am very sorry that you hurt yourself.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Fue un gran _____ saber que todos llegaron a salvo.", "options": ["alivio", "pena", "lástima", "cancelar"], "correct": 0, "teaches": ["b1-unit37-vocab"]},
                {"id": f"b1-{unit_num}-02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Es sorprendente que nadie se _____ enterado del cambio de hora.", "answer": "haya", "english": "It is surprising that nobody found out about the time change.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex06", "category": "grammar", "type": "matching", "pairs": [["Me alegro de que hayas venido", "I'm glad you came"], ["Siento que no hayas aprobado", "I'm sorry you didn't pass"], ["Es una lástima que haya llovido", "It's a pity it rained"], ["Qué alivio que hayas llamado", "What a relief you called"]], "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex07", "category": "listening", "type": "listening-choice", "sentence": "Me parece estupendo que hayan publicado tu artículo de investigación.", "options": ["Felicita por la publicación del artículo.", "Dice que el artículo tiene errores.", "Pide escribir un nuevo artículo."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex08", "category": "listening", "type": "dictation", "sentence": "Qué bien que hayamos tomado esta decisión tan acertada.", "english": "How great that we have made such a wise decision.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Marta", "text": "¡Al final conseguí las entradas para el concierto!"}, {"speaker": "David", "text": "____."}], "options": ["¡Qué alegría que las hayas conseguido!", "Qué alegría que las consigues.", "Siento que no las tengas."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Sonia", "text": "No pude entregar el informe antes de las seis."}, {"speaker": "Jefe", "text": "____."}], "options": ["Es una lástima que no hayas llegado a tiempo.", "Es una lástima que no llegas.", "Me alegro de que lo entregues."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que te alegras de que tus amigos hayan venido.", "answer": "Me alegro de que mis amigos hayan venido."}], "teaches": ["subjuntivo-perfecto"]}
            ]
        },
        {
            "num": "03",
            "title": "Doubt and Denial About Past Actions",
            "goal": "Express doubt, denial, and uncertainty about past events using no creer que, dudar que + pretérito perfecto de subjuntivo.",
            "grammar_title": "Doubt and Denial in the Past",
            "grammar_slug": "duda-negacion-perfecto-subjuntivo",
            "grammar_text": "When you doubt or deny an event that supposedly already occurred in the past, use the present perfect subjunctive:\n\n• *Dudo que hayan terminado todo el trabajo.* (I doubt they finished all the work.)\n• *No creo que Juan haya dicho semejante cosa.* (I don't think Juan said such a thing.)\n• *No es verdad que hayamos perdido los billetes.* (It's not true that we lost the tickets.)\n• *¿Crees que haya salido ya el tren?* (Do you think the train has left already?)",
            "table_rows": [
                ["No creo que...", "No creo que haya dicho eso."],
                ["Dudo que...", "Dudo que hayan terminado."],
                ["No es cierto que...", "No es cierto que hayamos perdido."],
                ["Es dudoso que...", "Es dudoso que haya ocurrido así."]
            ],
            "examples": [
                {"spanish": "No creo que hayan entendido la explicación.", "english": "I don't think they understood the explanation."},
                {"spanish": "Dudo que el tren haya llegado con puntualidad.", "english": "I doubt the train arrived on time."},
                {"spanish": "No es verdad que nos hayamos olvidado de tu cumpleaños.", "english": "It's not true that we forgot your birthday."}
            ],
            "tip": "Affirmative *creo que* takes indicative (*Creo que ha venido*), but negative *no creo que* triggers subjunctive (*No creo que haya venido*).",
            "vocab": [
                {"lemma": "dudar", "translation": "to doubt", "pos": "verb"},
                {"lemma": "cierto", "translation": "true / certain", "pos": "adjective"},
                {"lemma": "puntualidad", "translation": "punctuality", "pos": "noun"},
                {"lemma": "afirmar", "translation": "to claim / affirm", "pos": "verb"},
                {"lemma": "olvidar", "translation": "to forget", "pos": "verb"},
                {"lemma": "error", "translation": "mistake / error", "pos": "noun"},
                {"lemma": "verdad", "translation": "truth", "pos": "noun"},
                {"lemma": "explicación", "translation": "explanation", "pos": "noun"},
                {"lemma": "posible", "translation": "possible", "pos": "adjective"},
                {"lemma": "negar", "translation": "to deny", "pos": "verb"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-03.ex01", "category": "grammar", "type": "multiple-choice", "question": "No creo que ellos _____ comprendido la gravedad del asunto.", "options": ["hayan", "han", "hubieran", "habían"], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Dudo mucho que tú _____ hecho ese ejercicio solo.", "answer": "hayas", "english": "I doubt very much that you did that exercise alone.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["No", "creo", "que", "él", "haya", "dicho", "eso", "."], "solution": ["No", "creo", "que", "él", "haya", "dicho", "eso", "."], "english": "I don't think he said that.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "La _____ del tren de alta velocidad fue impecable.", "options": ["puntualidad", "error", "explicación", "negar"], "correct": 0, "teaches": ["b1-unit37-vocab"]},
                {"id": f"b1-{unit_num}-03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "No es cierto que nosotros _____ olvidado nuestra promesa.", "answer": "hayamos", "english": "It is not true that we have forgotten our promise.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex06", "category": "grammar", "type": "matching", "pairs": [["No creo que haya venido", "I don't think he came"], ["Dudo que hayan terminado", "I doubt they finished"], ["No es verdad que hayamos ido", "It's not true that we went"], ["¿Crees que haya salido?", "Do you think it has left?"]], "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex07", "category": "listening", "type": "listening-choice", "sentence": "Dudo que el director haya firmado ya el contrato definitivo.", "options": ["Duda que el contrato esté firmado.", "Afirma que el contrato está firmado.", "El contrato fue cancelado."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex08", "category": "listening", "type": "dictation", "sentence": "No creo que nadie haya visto las llaves extraviadas.", "english": "I don't think anyone has seen the lost keys.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "Dicen que el museo ya abrió sus puertas."}, {"speaker": "Beatriz", "text": "____."}], "options": ["Dudo que hayan abierto tan temprano.", "Dudo que abrieron temprano.", "Creo que hayan abierto."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Tomás", "text": "¿Es verdad que perdisteis el autobús de las diez?"}, {"speaker": "Sara", "text": "____."}], "options": ["No, no es verdad que lo hayamos perdido.", "No es verdad que lo perdimos.", "Creo que lo hayamos perdido."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que no crees que él haya terminado la tarea.", "answer": "No creo que él haya terminado la tarea."}], "teaches": ["subjuntivo-perfecto"]}
            ]
        },
        {
            "num": "04",
            "title": "Future Completion: Cuando hayamos terminado",
            "goal": "Express actions that will be completed before a future reference point using cuando / en cuanto + pretérito perfecto de subjuntivo.",
            "grammar_title": "Future Completion with Conjunctions of Time",
            "grammar_slug": "tiempo-futuro-perfecto-subjuntivo",
            "grammar_text": "The present perfect subjunctive can also refer to an action that will be completed *prior to another future event*:\n\n• **cuando**: *Te llamo cuando haya terminado de cocinar.* (I'll call you when I have finished cooking.)\n• **en cuanto / tan pronto como**: *En cuanto hayamos aterrizado, os mandaremos un mensaje.* (As soon as we have landed, we'll send you a message.)\n• **después de que**: *Saldremos después de que haya dejado de llover.* (We will go out after it has stopped raining.)",
            "table_rows": [
                ["cuando + perf. subj.", "Cuando hayas leído el libro, hablamos."],
                ["en cuanto + perf. subj.", "En cuanto haya salido el sol, saldremos."],
                ["tan pronto como...", "Tan pronto como hayamos comido, nos vamos."],
                ["después de que...", "Después de que hayas descansado, seguimos."]
            ],
            "examples": [
                {"spanish": "Te responderé en cuanto haya revisado todos los documentos.", "english": "I will answer you as soon as I have reviewed all the documents."},
                {"spanish": "Podrás salir cuando hayas ordenado tu habitación.", "english": "You will be able to go out when you have tidied your room."},
                {"spanish": "Celebraremos tan pronto como hayamos firmado el acuerdo.", "english": "We will celebrate as soon as we have signed the agreement."}
            ],
            "tip": "Think of this as the subjunctive equivalent of the future perfect: it projects forward to the moment when an action will already be done.",
            "vocab": [
                {"lemma": "en cuanto", "translation": "as soon as", "pos": "conjunction"},
                {"lemma": "tan pronto como", "translation": "as soon as", "pos": "conjunction"},
                {"lemma": "revisar", "translation": "to check / review", "pos": "verb"},
                {"lemma": "acuerdo", "translation": "agreement", "pos": "noun"},
                {"lemma": "celebrar", "translation": "to celebrate", "pos": "verb"},
                {"lemma": "ordenar", "translation": "to tidy / organize", "pos": "verb"},
                {"lemma": "firmar", "translation": "to sign", "pos": "verb"},
                {"lemma": "documento", "translation": "document", "pos": "noun"},
                {"lemma": "después de que", "translation": "after (subjunctive)", "pos": "conjunction"},
                {"lemma": "aviso", "translation": "notice / alert", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-04.ex01", "category": "grammar", "type": "multiple-choice", "question": "Avísame en cuanto _____ llegado al aeropuerto.", "options": ["hayas", "has", "habrás", "habías"], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Hablaremos del proyecto cuando nosotros _____ terminado la reunión.", "answer": "hayamos", "english": "We will talk about the project when we have finished the meeting.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Te", "llamo", "cuando", "haya", "llegado", "a", "casa", "."], "solution": ["Te", "llamo", "cuando", "haya", "llegado", "a", "casa", "."], "english": "I'll call you when I have arrived home.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Vamos a _____ el contrato mañana por la mañana.", "options": ["firmar", "revisar", "celebrar", "aviso"], "correct": 0, "teaches": ["b1-unit37-vocab"]},
                {"id": f"b1-{unit_num}-04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Iremos al parque tan pronto como _____ de llover.", "answer": "haya", "english": "We will go to the park as soon as it has stopped raining.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex06", "category": "grammar", "type": "matching", "pairs": [["Cuando hayas llegado", "When you have arrived"], ["En cuanto hayamos comido", "As soon as we have eaten"], ["Tan pronto como haya salido", "As soon as it has left"], ["Después de que hayan firmado", "After they have signed"]], "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex07", "category": "listening", "type": "listening-choice", "sentence": "Tan pronto como hayamos recibido la confirmación oficial, compraremos los pasajes.", "options": ["Comprarán los pasajes tras la confirmación.", "Ya compraron los pasajes.", "No van a comprar pasajes."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex08", "category": "listening", "type": "dictation", "sentence": "Saldremos de excursión cuando haya salido el sol.", "english": "We will go on an outing when the sun has come out.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Elena", "text": "¿Cuándo podemos revisar las cuentas?"}, {"speaker": "Marcos", "text": "____."}], "options": ["En cuanto haya terminado este informe te ayudo.", "En cuanto termino te ayudo.", "Cuando terminaré te ayudo."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Madre", "text": "¿Puedo salir con mis amigos esta tarde?"}, {"speaker": "Padre", "text": "____."}], "options": ["Sí, cuando hayas recogido tu habitación.", "Sí, cuando recogiste tu habitación.", "Sí, cuando recoges tu habitación."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que llamarás cuando hayas llegado a casa.", "answer": "Te llamaré cuando haya llegado a casa."}], "teaches": ["subjuntivo-perfecto"]}
            ]
        },
        {
            "num": "05",
            "title": "Present Subjunctive vs. Present Perfect Subjunctive",
            "goal": "Contrast the present subjunctive (hable / viva) with the present perfect subjunctive (haya hablado / haya vivido).",
            "grammar_title": "Aspect Contrast in the Subjunctive",
            "grammar_slug": "contraste-presente-perfecto-subjuntivo",
            "grammar_text": "Mastering the subjunctive at B1 requires choosing between current/future actions vs completed past actions:\n\n• **Present Subjunctive** (*hables, vengas*): Refers to simultaneous or future events:\n  *Espero que vengas a mi fiesta mañana.* (I hope you come tomorrow.)\n• **Present Perfect Subjunctive** (*hayas hablado, hayas venido*): Refers to completed events:\n  *Espero que hayas venido en metro.* (I hope you came by metro.)\n• Contrast: *Dudo que lo hagan hoy* (future action) vs. *Dudo que lo hayan hecho ya* (completed action).",
            "table_rows": [
                ["Acción presente / futura", "Espero que vengas mañana.", "Present subjunctive"],
                ["Acción ya completada", "Espero que hayas venido bien.", "Perfect subjunctive"],
                ["Duda de futuro", "Dudo que termine hoy.", "Present subjunctive"],
                ["Duda de pasado", "Dudo que haya terminado ya.", "Perfect subjunctive"]
            ],
            "examples": [
                {"spanish": "Me alegro de que estés aquí (ahora) y me alegro de que hayas venido (pasado).", "english": "I'm glad you're here (now) and I'm glad you came (past)."},
                {"spanish": "¿Crees que llueva esta tarde? vs. ¿Crees que haya llovido anoche?", "english": "Do you think it will rain this afternoon? vs. Do you think it rained last night?"},
                {"spanish": "Es una lástima que no puedan venir mañana vs. que no hayan podido venir ayer.", "english": "It's a pity they can't come tomorrow vs. that they couldn't come yesterday."}
            ],
            "tip": "Ask yourself: Is the action finished relative to now? If yes, use *haya + participio*.",
            "vocab": [
                {"lemma": "aspecto", "translation": "aspect", "pos": "noun"},
                {"lemma": "simultáneo", "translation": "simultaneous", "pos": "adjective"},
                {"lemma": "concluido", "translation": "concluded", "pos": "adjective"},
                {"lemma": "relación", "translation": "relation / relationship", "pos": "noun"},
                {"lemma": "distinguir", "translation": "to distinguish", "pos": "verb"},
                {"lemma": "matiz", "translation": "nuance", "pos": "noun"},
                {"lemma": "precisión", "translation": "precision", "pos": "noun"},
                {"lemma": "perspectiva", "translation": "perspective", "pos": "noun"},
                {"lemma": "indicar", "translation": "to indicate", "pos": "verb"},
                {"lemma": "claridad", "translation": "clarity", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-05.ex01", "category": "grammar", "type": "multiple-choice", "question": "Espero que Pedro _____ ayer todo lo necesario.", "options": ["haya comprado", "compre", "compraba", "compraría"], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Dudo que el tren _____ llegado ya a la estación.", "answer": "haya", "english": "I doubt the train has already arrived at the station.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Espero", "que", "hayan", "comprendido", "la", "diferencia", "."], "solution": ["Espero", "que", "hayan", "comprendido", "la", "diferencia", "."], "english": "I hope they understood the difference.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "El profesor explicó con gran _____ cada punto gramatical.", "options": ["claridad", "matiz", "aspecto", "relación"], "correct": 0, "teaches": ["b1-unit37-vocab"]},
                {"id": f"b1-{unit_num}-05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Me alegro de que tú _____ venido a verme hoy.", "answer": "hayas", "english": "I am glad that you came to see me today.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex06", "category": "grammar", "type": "matching", "pairs": [["Espero que venga mañana", "Present subjunctive (future)"], ["Espero que haya venido ayer", "Perfect subjunctive (past)"], ["Dudo que lo haga", "Present subjunctive"], ["Dudo que lo haya hecho", "Perfect subjunctive"]], "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex07", "category": "listening", "type": "listening-choice", "sentence": "Me alegro muchísimo de que hayáis disfrutado de vuestra estancia en la ciudad.", "options": ["Se alegra por la experiencia vivida.", "Pregunta si van a venir a la ciudad.", "No le gustó la ciudad."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex08", "category": "listening", "type": "dictation", "sentence": "Espero que no haya habido ningún malentendido.", "english": "I hope there has not been any misunderstanding.", "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Laura", "text": "¿Crees que Juan ya leyó tu mensaje?"}, {"speaker": "Felipe", "text": "____."}], "options": ["No creo que lo haya leído todavía.", "No creo que lo lee.", "Dudo que lo leerá."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Cliente", "text": "¿Cuándo estará listo el presupuesto?"}, {"speaker": "Asesor", "text": "____."}], "options": ["Se lo mandaré en cuanto lo hayamos terminado.", "Se lo mando cuando lo terminamos.", "Se lo mandé cuando lo haya terminado."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
                {"id": f"b1-{unit_num}-05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que esperas que tus amigos hayan descansado.", "answer": "Espero que mis amigos hayan descansado."}], "teaches": ["subjuntivo-perfecto"]}
            ]
        }
    ]
    
    cons_title = "Consolidation: Present Perfect Subjunctive"
    cons_goal = "Demonstrate fluid mastery of the present perfect subjunctive across feelings, doubts, and future anteriority."
    cons_gr_text = "The present perfect subjunctive (*haya hablado / vivido*) bridges present mental attitudes with completed past actions or anterior future conditions (*en cuanto haya llegado*)."
    cons_table_rows = [
        ["Forma", "haya, hayas, haya, hayamos, hayáis, hayan + participio"],
        ["Sentimientos", "Me alegro de que hayas venido"],
        ["Duda y negación", "No creo que hayan dicho la verdad"],
        ["Tiempo futuro", "Te llamo en cuanto haya terminado"]
    ]
    cons_examples = [
        {"spanish": "Me alegro de que hayamos llegado a tiempo.", "english": "I am glad we arrived on time."},
        {"spanish": "No creo que nadie haya visto las llaves.", "english": "I don't think anyone saw the keys."}
    ]
    cons_tip = "Remember: participles never inflect for gender/number in compound tenses (always haya venido, hayan venido)."
    
    cons_exs = [
        {"id": f"b1-{unit_num}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "Espero que vosotros _____ tenido un viaje agradable.", "options": ["hayáis", "hayais", "habéis", "hubierais"], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
        {"id": f"b1-{unit_num}.cons.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Me alegro de que nosotros _____ superado todos los obstáculos.", "answer": "hayamos", "english": "I am glad that we have overcome all the obstacles.", "teaches": ["subjuntivo-perfecto"]},
        {"id": f"b1-{unit_num}.cons.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Dudo", "que", "hayan", "recibido", "el", "aviso", "."], "solution": ["Dudo", "que", "hayan", "recibido", "el", "aviso", "."], "english": "I doubt they received the notice.", "teaches": ["subjuntivo-perfecto"]},
        {"id": f"b1-{unit_num}.cons.ex04", "category": "grammar", "type": "matching", "pairs": [["Que hayas venido", "That you came"], ["Que hayamos visto", "That we saw"], ["Que hayan firmado", "That they signed"], ["Que haya llovido", "That it rained"]], "teaches": ["subjuntivo-perfecto"]},
        {"id": f"b1-{unit_num}.cons.ex05", "category": "listening", "type": "listening-choice", "sentence": "Es fantástico que hayáis podido resolver el problema tan rápidamente.", "options": ["Elogia la rapidez con que resolvieron el problema.", "Se queja de la tardanza.", "No sabe si se resolvió."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
        {"id": f"b1-{unit_num}.cons.ex06", "category": "listening", "type": "dictation", "sentence": "Te llamaré en cuanto haya terminado la reunión.", "english": "I will call you as soon as I have finished the meeting.", "teaches": ["subjuntivo-perfecto"]},
        {"id": f"b1-{unit_num}.cons.ex07", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Raquel", "text": "¿Crees que ya llegó el paquete?"}, {"speaker": "Mateo", "text": "____."}], "options": ["Dudo que haya llegado todavía.", "Dudo que llegó ayer.", "Creo que haya llegado."], "correct": 0, "teaches": ["subjuntivo-perfecto"]},
        {"id": f"b1-{unit_num}.cons.ex08", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que te alegras de que todo haya salido bien.", "answer": "Me alegro de que todo haya salido bien."}], "teaches": ["subjuntivo-perfecto"]}
    ]
    
    generate_b1_unit(target_dir, unit_num, unit_title, lessons_data, cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs)

# ==========================================
# UNIT 38: Correlación Temporal & Estilo Indirecto
# ==========================================
def build_unit_38(target_dir):
    unit_num = "38"
    unit_title = "Time & Perspective: Sequence of Tenses & Reported Speech"
    
    lessons_data = [
        {
            "num": "01",
            "title": "Subjunctive Sequence of Tenses: Past Framing",
            "goal": "Apply the imperfect subjunctive when the main governing verb is in the past (pretérito indefinido, imperfecto, pluscuamperfecto).",
            "grammar_title": "Tense Sequence with Subjunctive in the Past",
            "grammar_slug": "correlacion-temporal-pasado",
            "grammar_text": "When the governing verb in the main clause is in a past tense (indefinido, imperfecto, pluscuamperfecto), the subordinate subjunctive verb shifts into the **imperfect subjunctive** (*-ra / -se*):\n\n• Present frame: *Quiero que vengas.* (Present subjunctive)\n• Past frame: *Quería que vinieras.* (Imperfect subjunctive)\n• Indefinido frame: *Me pidió que le ayudara.* (Imperfect subjunctive)\n• Condition: *Me encantaría que vinieras.* (Conditional triggers imperfect subjunctive).",
            "table_rows": [
                ["Presente -> Presente subj.", "Quiero que vengas.", "I want you to come."],
                ["Pasado -> Imperfecto subj.", "Quería que vinieras.", "I wanted you to come."],
                ["Indefinido -> Imperfecto subj.", "Me dijo que lo hiciera.", "He told me to do it."],
                ["Condicional -> Imperfecto subj.", "Me gustaría que estuvieras.", "I'd like you to be here."]
            ],
            "examples": [
                {"spanish": "Mis padres querían que yo estudiara medicina.", "english": "My parents wanted me to study medicine."},
                {"spanish": "El médico me recomendó que guardara reposo.", "english": "The doctor recommended that I get some rest."},
                {"spanish": "Me alegré mucho de que estuvieras en la ceremonia.", "english": "I was very glad that you were at the ceremony."}
            ],
            "tip": "Never mix a past main verb with a present subjunctive: say *Quería que viniera*, never *Quería que venga*.",
            "vocab": [
                {"lemma": "correlación", "translation": "sequence / correlation", "pos": "noun"},
                {"lemma": "subordinada", "translation": "subordinate clause", "pos": "noun"},
                {"lemma": "gobernar", "translation": "to govern", "pos": "verb"},
                {"lemma": "aconsejar", "translation": "to advise", "pos": "verb"},
                {"lemma": "reposo", "translation": "rest", "pos": "noun"},
                {"lemma": "ceremonia", "translation": "ceremony", "pos": "noun"},
                {"lemma": "recomendación", "translation": "recommendation", "pos": "noun"},
                {"lemma": "médico", "translation": "doctor / physician", "pos": "noun"},
                {"lemma": "exigir", "translation": "to demand / require", "pos": "verb"},
                {"lemma": "tiempo verbal", "translation": "verb tense", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-01.ex01", "category": "grammar", "type": "multiple-choice", "question": "El profesor quería que los alumnos _____ más atención en clase.", "options": ["pusieran", "pongan", "pondrían", "ponían"], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Mi madre me pidió que le _____ una carta.", "answer": "escribiera", "english": "My mother asked me to write her a letter.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Ella", "quería", "que", "yo", "fuera", "con", "ella", "."], "solution": ["Ella", "quería", "que", "yo", "fuera", "con", "ella", "."], "english": "She wanted me to go with her.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Seguimos al pie de la letra la _____ del especialista.", "options": ["recomendación", "reposo", "ceremonia", "gobernar"], "correct": 0, "teaches": ["b1-unit38-vocab"]},
                {"id": f"b1-{unit_num}-01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Nos sorprendió mucho que ellos no _____ a la reunión.", "answer": "vinieran", "english": "We were very surprised that they did not come to the meeting.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex06", "category": "grammar", "type": "matching", "pairs": [["Quiero que hables", "Present -> Present subjunctive"], ["Quería que hablaras", "Past -> Imperfect subjunctive"], ["Me pidió que fuera", "Indefinido -> Imperfect subjunctive"], ["Me gustaría que vinieras", "Conditional -> Imperfect subjunctive"]], "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex07", "category": "listening", "type": "listening-choice", "sentence": "El director exigió que todos los empleados entregaran los informes a tiempo.", "options": ["Exigió la entrega puntual de informes.", "Pidió aplazar los informes.", "No quiso leer los informes."], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex08", "category": "listening", "type": "dictation", "sentence": "Mis amigos querían que nos quedáramos más tiempo en Madrid.", "english": "My friends wanted us to stay longer in Madrid.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Pablo", "text": "¿Qué te dijo el médico ayer?"}, {"speaker": "Carlos", "text": "____."}], "options": ["Me recomendó que descansara durante una semana.", "Me recomendó que descanso.", "Me recomienda que descansaba."], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Elena", "text": "¿Por qué no compraste ese coche?"}, {"speaker": "David", "text": "____."}], "options": ["Porque mi padre no quería que gastara tanto dinero.", "Porque mi padre no quiere que gastaba.", "Porque mi padre quería que gaste."], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que tus padres querían que estudiaras más.", "answer": "Mis padres querían que yo estudiara más."}], "teaches": ["correlacion-temporal-subjuntivo"]}
            ]
        },
        {
            "num": "02",
            "title": "Reported Speech for Commands and Requests",
            "goal": "Transform direct commands and requests into reported speech using decir que, pedir que + imperfect subjunctive.",
            "grammar_title": "Reporting Commands and Requests in the Past",
            "grammar_slug": "estilo-indirecto-ordenes-peticiones",
            "grammar_text": "When transforming an imperative or a command into reported speech in the past, use **decir / pedir / ordenar que + imperfecto de subjuntivo**:\n\n• Direct command: *«¡Cierra la ventana!»*\n• Reported past: *Me dijo que cerrara la ventana.*\n• Direct request: *«Por favor, ayúdame con las maletas.»*\n• Reported past: *Me pidió que le ayudara con las maletas.*\n• Negative command: *«¡No salgas de noche!»* -> *Nos prohibió que saliéramos de noche.*",
            "table_rows": [
                ["«¡Ven aquí!»", "Me dijo que fuera allí."],
                ["«¡No toques eso!»", "Me ordenó que no tocara eso."],
                ["«Por favor, espérame.»", "Me pidió que la esperara."],
                ["«¡Estudiad mucho!»", "Nos mandó que estudiáramos mucho."]
            ],
            "examples": [
                {"spanish": "El policía me ordenó que detuviera el vehículo.", "english": "The police officer ordered me to stop the vehicle."},
                {"spanish": "El camarero nos pidió que esperáramos diez minutos.", "english": "The waiter asked us to wait ten minutes."},
                {"spanish": "La profesora nos dijo que abriéramos el libro por la página veinte.", "english": "The teacher told us to open the book to page twenty."}
            ],
            "tip": "Direct imperatives always convert to the subjunctive in reported speech. If the reporting verb is in the past, it must be the imperfect subjunctive.",
            "vocab": [
                {"lemma": "ordenar", "translation": "to order / command", "pos": "verb"},
                {"lemma": "prohibir", "translation": "to forbid / prohibit", "pos": "verb"},
                {"lemma": "petición", "translation": "request", "pos": "noun"},
                {"lemma": "orden", "translation": "command / order", "pos": "noun"},
                {"lemma": "vehículo", "translation": "vehicle", "pos": "noun"},
                {"lemma": "detener", "translation": "to stop / halt", "pos": "verb"},
                {"lemma": "mandar", "translation": "to order / send", "pos": "verb"},
                {"lemma": "rogar", "translation": "to plead / beg", "pos": "verb"},
                {"lemma": "solicitar", "translation": "to request / apply", "pos": "verb"},
                {"lemma": "instrucción", "translation": "instruction", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-02.ex01", "category": "grammar", "type": "multiple-choice", "question": "La profesora nos dijo que _____ silencio durante el examen.", "options": ["guardáramos", "guardamos", "guardemos", "guardaríamos"], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "El guía nos pidió que no nos _____ del grupo.", "answer": "separáramos", "english": "The guide asked us not to separate from the group.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Me", "dijo", "que", "cerrara", "la", "puerta", "."], "solution": ["Me", "dijo", "que", "cerrara", "la", "puerta", "."], "english": "He told me to close the door.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "El conductor tuvo que _____ el coche ante el semáforo rojo.", "options": ["detener", "ordenar", "rogar", "prohibir"], "correct": 0, "teaches": ["b1-unit38-vocab"]},
                {"id": f"b1-{unit_num}-02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "El médico me ordenó que no _____ alcohol durante el tratamiento.", "answer": "bebiera", "english": "The doctor ordered me not to drink alcohol during the treatment.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex06", "category": "grammar", "type": "matching", "pairs": [["«¡Ven!»", "Me dijo que fuera"], ["«¡Hazlo!»", "Me pidió que lo hiciera"], ["«¡No hables!»", "Me prohibió que hablara"], ["«¡Esperad!»", "Nos ordenó que esperáramos"]], "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex07", "category": "listening", "type": "listening-choice", "sentence": "El recepcionista nos rogó que no hiciéramos ruido por la noche.", "options": ["Pidió silencio durante la noche.", "Dijo que podíamos poner música.", "Se quejó del recepcionista."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex08", "category": "listening", "type": "dictation", "sentence": "Ella me pidió que le mandara la información por correo.", "english": "She asked me to send her the information by email.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿Qué te dijo el policía?"}, {"speaker": "Mateo", "text": "____."}], "options": ["Me ordenó que le mostrara el carnet de conducir.", "Me ordenó que le muestro el carnet.", "Me dice que le mostraba el carnet."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Sara", "text": "¿Qué os pidió la anfitriona?"}, {"speaker": "Invitados", "text": "____."}], "options": ["Nos pidió que nos sintiéramos como en casa.", "Nos pidió que nos sentimos en casa.", "Nos pide que nos sentáramos."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que tu amigo te pidió que le ayudaras.", "answer": "Mi amigo me pidió que le ayudara."}], "teaches": ["estilo-indirecto-ordenes"]}
            ]
        },
        {
            "num": "03",
            "title": "Reported Speech Tense Backshift: Present to Past, Future to Conditional",
            "goal": "Backshift tenses in indirect statements when reporting in the past (present -> imperfect, future -> conditional).",
            "grammar_title": "Tense Backshift in Indirect Statements",
            "grammar_slug": "estilo-indirecto-backshift-declaraciones",
            "grammar_text": "When reporting statements in a past framework (*Dijo que...*), verb tenses systematically shift back:\n\n• **Presente -> Imperfecto**: *«Tengo prisa»* -> *Dijo que tenía prisa.*\n• **Futuro -> Condicional**: *«Viajaré mañana»* -> *Dijo que viajaría al día siguiente.*\n• **Pretérito / Perfecto -> Pluscuamperfecto**: *«Ya comí» / «He comido»* -> *Dijo que ya había comido.*\n• **Time expressions also adapt**: *hoy* -> *aquel día*, *mañana* -> *al día siguiente*, *ayer* -> *el día anterior*.",
            "table_rows": [
                ["«Tengo hambre»", "Dijo que tenía hambre."],
                ["«Iré a Madrid»", "Dijo que iría a Madrid."],
                ["«Ya lo terminé»", "Dijo que ya lo había terminado."],
                ["«Lo compraré hoy»", "Dijo que lo compraría aquel día."]
            ],
            "examples": [
                {"spanish": "Carlos me aseguró que vendría a visitarnos el fin de semana.", "english": "Carlos assured me that he would come to visit us on the weekend."},
                {"spanish": "Ella dijo que estaba muy cansada para salir a cenar.", "english": "She said that she was too tired to go out for dinner."},
                {"spanish": "Los meteorólogos anunciaron que llovería durante la tarde.", "english": "The meteorologists announced that it would rain during the afternoon."}
            ],
            "tip": "The future always backshifts to the conditional: *«Llegaré a las ocho»* -> *Dijo que llegaría a las ocho*.",
            "vocab": [
                {"lemma": "asegurar", "translation": "to assure / claim", "pos": "verb"},
                {"lemma": "anunciar", "translation": "to announce", "pos": "verb"},
                {"lemma": "aquel día", "translation": "that day", "pos": "expression"},
                {"lemma": "al día siguiente", "translation": "the following day", "pos": "expression"},
                {"lemma": "el día anterior", "translation": "the day before", "pos": "expression"},
                {"lemma": "afirmación", "translation": "statement / assertion", "pos": "noun"},
                {"lemma": "declaración", "translation": "declaration", "pos": "noun"},
                {"lemma": "comentar", "translation": "to comment / mention", "pos": "verb"},
                {"lemma": "explicar", "translation": "to explain", "pos": "verb"},
                {"lemma": "posibilidad", "translation": "possibility", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-03.ex01", "category": "grammar", "type": "multiple-choice", "question": "Carlos me dijo: «Estaré en la estación a las seis». Carlos me dijo que _____ en la estación a las seis.", "options": ["estaría", "estará", "estaba", "estuviera"], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Ella me comentó que no _____ tiempo para hablar aquel día.", "answer": "tenía", "english": "She told me that she didn't have time to talk that day.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Dijo", "que", "vendría", "al", "día", "siguiente", "."], "solution": ["Dijo", "que", "vendría", "al", "día", "siguiente", "."], "english": "He said that he would come the following day.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Nos vimos en el aeropuerto justo _____ de su partida.", "options": ["el día anterior", "aquel día", "al día siguiente", "afirmación"], "correct": 0, "teaches": ["b1-unit38-vocab"]},
                {"id": f"b1-{unit_num}-03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Los directores anunciaron que la empresa _____ abrir una nueva sede.", "answer": "abriría", "english": "The directors announced that the company would open a new branch.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex06", "category": "grammar", "type": "matching", "pairs": [["«Tengo frío»", "Dijo que tenía frío"], ["«Compraré el pan»", "Dijo que compraría el pan"], ["«Ya comí»", "Dijo que ya había comido"], ["«Mañana voy»", "Dijo que iría al día siguiente"]], "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex07", "category": "listening", "type": "listening-choice", "sentence": "Marta nos aseguró que terminaría el diseño antes del viernes.", "options": ["Afirmó que completaría el diseño a tiempo.", "Dijo que no podía terminar el diseño.", "Canceló el proyecto."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex08", "category": "listening", "type": "dictation", "sentence": "Él nos dijo que compraría las entradas al día siguiente.", "english": "He told us that he would buy the tickets the following day.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Andrés", "text": "¿Qué te dijo Clara por teléfono?"}, {"speaker": "Beatriz", "text": "____."}], "options": ["Me dijo que vendría a cenar pero que tenía algo de retraso.", "Me dice que viene a cenar.", "Me dijo que vendrá mañana."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Jefe", "text": "¿Hablaste con el proveedor de Valencia?"}, {"speaker": "Secretaria", "text": "____."}], "options": ["Sí, me aseguró que enviaría los materiales hoy mismo.", "Sí, me asegura que envía los materiales.", "Sí, me dijo que envía ayer."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Transforma a estilo indirecto: «Viajaré a Madrid el lunes».", "answer": "Dijo que viajaría a Madrid el lunes."}], "teaches": ["estilo-indirecto-ordenes"]}
            ]
        },
        {
            "num": "04",
            "title": "Nuanced Reporting Verbs with Subjunctive",
            "goal": "Select and manipulate precise reporting verbs (sugerir, advertir, recomendar, exigir, proponer) that take the subjunctive.",
            "grammar_title": "Nuanced Reporting Verbs with Imperfect Subjunctive",
            "grammar_slug": "verbos-comunicacion-imperfecto-subjuntivo",
            "grammar_text": "Spanish boasts a rich variety of communication verbs that modulate authority, caution, and suggestion:\n\n• **Recomendación**: *aconsejar que, recomendar que, sugerir que* (*Me sugirió que hablara con el director*)\n• **Autoridad**: *exigir que, demandar que, imponer que* (*Nos exigió que fuéramos puntuales*)\n• **Advertencia**: *advertir que + subj.* (*Nos advirtió que no cruzáramos por allí*)\n• **Propuesta**: *proponer que* (*Propuso que hiciéramos una pausa*).",
            "table_rows": [
                ["sugerir que...", "Me sugirió que fuera al médico."],
                ["advertir que... (subj.)", "Nos advirtió que tuviéramos cuidado."],
                ["exigir que...", "El jefe exigió que llegáramos a las ocho."],
                ["proponer que...", "Propuso que cenáramos juntos."]
            ],
            "examples": [
                {"spanish": "El guía nos advirtió que tuviéramos cuidado con las piedras resbaladizas.", "english": "The guide warned us to be careful with the slippery rocks."},
                {"spanish": "El comité propuso que aplazáramos la votación hasta la semana próxima.", "english": "The committee proposed that we postpone the vote until next week."},
                {"spanish": "Mi amigo me aconsejó que no aceptara la primera oferta.", "english": "My friend advised me not to accept the first offer."}
            ],
            "tip": "*Advertir que + indicativo* reports information (*Me advirtió que llovía*), while *advertir que + subjuntivo* gives a warning command (*Me advirtió que tuviera cuidado*).",
            "vocab": [
                {"lemma": "sugerir", "translation": "to suggest", "pos": "verb"},
                {"lemma": "advertir", "translation": "to warn", "pos": "verb"},
                {"lemma": "proponer", "translation": "to propose", "pos": "verb"},
                {"lemma": "aplazar", "translation": "to postpone", "pos": "verb"},
                {"lemma": "votación", "translation": "voting / ballot", "pos": "noun"},
                {"lemma": "resbaladizo", "translation": "slippery", "pos": "adjective"},
                {"lemma": "comité", "translation": "committee", "pos": "noun"},
                {"lemma": "cuidado", "translation": "care / caution", "pos": "noun"},
                {"lemma": "prudencia", "translation": "prudence / caution", "pos": "noun"},
                {"lemma": "primer oferta", "translation": "first offer", "pos": "expression"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-04.ex01", "category": "grammar", "type": "multiple-choice", "question": "El abogado me aconsejó que no _____ ningún documento sin leerlo.", "options": ["firmara", "firmo", "firmé", "firmaría"], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "El profesor nos propuso que _____ el proyecto en grupos.", "answer": "hiciéramos", "english": "The teacher proposed that we do the project in groups.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Nos", "advirtió", "que", "tuviéramos", "mucho", "cuidado", "."], "solution": ["Nos", "advirtió", "que", "tuviéramos", "mucho", "cuidado", "."], "english": "He warned us to be very careful.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Tuvimos que caminar con extrema _____ por el suelo mojado.", "options": ["prudencia", "comité", "votación", "primer oferta"], "correct": 0, "teaches": ["b1-unit38-vocab"]},
                {"id": f"b1-{unit_num}-04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "El médico le sugirió que _____ más agua todos los días.", "answer": "bebiera", "english": "The doctor suggested that he drink more water every day.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex06", "category": "grammar", "type": "matching", "pairs": [["Aconsejar que", "To advise that"], ["Sugerir que", "To suggest that"], ["Advertir que (subj.)", "To warn that (command)"], ["Proponer que", "To propose that"]], "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex07", "category": "listening", "type": "listening-choice", "sentence": "El inspector exigió que le mostráramos todas las facturas del año pasado.", "options": ["Demandó ver todas las facturas.", "Preguntó por una factura reciente.", "Dijo que las facturas no eran necesarias."], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex08", "category": "listening", "type": "dictation", "sentence": "El guía nos sugirió que saliéramos muy temprano.", "english": "The guide suggested that we leave very early.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Valeria", "text": "¿Qué te recomendaron en la agencia de viajes?"}, {"speaker": "Ignacio", "text": "____."}], "options": ["Me recomendaron que reservara los hoteles con antelación.", "Me recomiendan que reservo con tiempo.", "Me recomendaron que reservé."], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Director", "text": "¿Qué propuso el equipo en la reunión de ayer?"}, {"speaker": "Subdirector", "text": "____."}], "options": ["Propusieron que ampliáramos el plazo de entrega.", "Propusieron que ampliamos el plazo.", "Proponen que ampliábamos el plazo."], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que el médico te aconsejó que descansaras.", "answer": "El médico me aconsejó que descansara."}], "teaches": ["correlacion-temporal-subjuntivo"]}
            ]
        },
        {
            "num": "05",
            "title": "Integrated Discourse: Temporal Harmony in Complex Narration",
            "goal": "Harmonize past indicative narratives, reported speech, and imperfect subjunctives across complex multi-clause sentences.",
            "grammar_title": "Synthesis of Temporal Harmony in Narrative Discourse",
            "grammar_slug": "armonia-temporal-discurso-complejo",
            "grammar_text": "B1 speakers articulate stories with multi-layered temporal depth:\n\n• *Ayer me encontré con Elena. Me contó que se casaría en verano y me pidió que fuera su testigo de boda.* (Past indicative -> conditional statement -> reported request with imperfect subjunctive).\n• *Aunque no quería que nos fuéramos tan pronto, tuvimos que marcharnos porque el tren salía a las diez.*",
            "table_rows": [
                ["Narración pasada", "Ayer me encontré con Elena."],
                ["Declaración de futuro", "Me contó que viajaría pronto."],
                ["Petición subordinada", "Me pidió que la acompañara."],
                ["Secuencia completa", "Dijo que vendría si no lloviera."]
            ],
            "examples": [
                {"spanish": "Me dijo que le gustaría que nos viéramos más a menudo.", "english": "He told me he would like us to see each other more often."},
                {"spanish": "El jefe nos comunicó que la empresa abriría nuevas oficinas y nos pidió que colaboráramos.", "english": "The boss told us the company would open new offices and asked us to cooperate."},
                {"spanish": "No creía que fuera posible que terminaran todo a tiempo.", "english": "I didn't believe it was possible that they would finish everything on time."}
            ],
            "tip": "Keep the chain intact: past reporting verb -> conditional or imperfect subjunctive.",
            "vocab": [
                {"lemma": "testigo", "translation": "witness", "pos": "noun"},
                {"lemma": "boda", "translation": "wedding", "pos": "noun"},
                {"lemma": "comunicar", "translation": "to communicate / inform", "pos": "verb"},
                {"lemma": "colaborar", "translation": "to cooperate / collaborate", "pos": "verb"},
                {"lemma": "a menudo", "translation": "often", "pos": "expression"},
                {"lemma": "articular", "translation": "to articulate", "pos": "verb"},
                {"lemma": "armonía", "translation": "harmony", "pos": "noun"},
                {"lemma": "multi-cláusula", "translation": "multi-clause", "pos": "noun"},
                {"lemma": "coherencia", "translation": "coherence", "pos": "noun"},
                {"lemma": "fluidez", "translation": "fluency", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-05.ex01", "category": "grammar", "type": "multiple-choice", "question": "Elena me dijo que _____ encantada de que yo fuera a su boda.", "options": ["estaría", "estará", "estuviera", "estuvo"], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "El director nos pidió que _____ con el nuevo equipo.", "answer": "colaboráramos", "english": "The director asked us to collaborate with the new team.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Me", "pidió", "que", "fuera", "su", "testigo", "."], "solution": ["Me", "pidió", "que", "fuera", "su", "testigo", "."], "english": "She asked me to be her witness.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Carlos y Lucía celebrarán su _____ en la catedral de Toledo.", "options": ["boda", "testigo", "armonía", "fluidez"], "correct": 0, "teaches": ["b1-unit38-vocab"]},
                {"id": f"b1-{unit_num}-05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Ella esperaba que nosotros _____ a visitarla más a menudo.", "answer": "fuéramos", "english": "She hoped that we would go visit her more often.", "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-05.ex06", "category": "grammar", "type": "matching", "pairs": [["Me dijo que vendría", "He said he would come"], ["Me pidió que fuera", "He asked me to go"], ["Esperaba que llamaras", "I hoped you would call"], ["Sugirió que comiéramos", "He suggested we eat"]], "teaches": ["correlacion-temporal-subjuntivo"]},
                {"id": f"b1-{unit_num}-05.ex07", "category": "listening", "type": "listening-choice", "sentence": "Ayer nos avisaron de que cancelarían el vuelo y nos pidieron que fuéramos al mostrador.", "options": ["Informaron de la cancelación y dieron una instrucción.", "El vuelo salió a tiempo.", "Llegaron sin avisar."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-05.ex08", "category": "listening", "type": "dictation", "sentence": "Mi hermano me pidió que cuidara de su perro durante el fin de semana.", "english": "My brother asked me to take care of his dog during the weekend.", "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿Hablaste con el nuevo gerente?"}, {"speaker": "Raúl", "text": "____."}], "options": ["Sí, me comunicó que cambiarían los horarios y me pidió que colaborara.", "Sí, me dice que cambia los horarios.", "Sí, me comunicó que cambia."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Marta", "text": "¿Por qué no viniste a cenar anoche?"}, {"speaker": "Sara", "text": "____."}], "options": ["Es que mi madre me rogó que me quedara en casa.", "Es que mi madre me ruega que me quedo.", "Es que mi madre me pidió que me quede."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
                {"id": f"b1-{unit_num}-05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que tu amigo te dijo que vendría más tarde.", "answer": "Mi amigo me dijo que vendría más tarde."}], "teaches": ["estilo-indirecto-ordenes"]}
            ]
        }
    ]
    
    cons_title = "Consolidation: Sequence of Tenses & Reported Speech"
    cons_goal = "Seamlessly integrate tense backshift and reported commands in narrative Spanish."
    cons_gr_text = "Mastering sequence of tenses ensures stylistic harmony: main past clauses govern imperfect subjunctives for commands/desires (*pidió que viniera*), and conditionals for future statements (*dijo que vendría*)."
    cons_table_rows = [
        ["Órdenes en pasado", "Me dijo que cerrara la puerta"],
        ["Futuro en pasado", "Aseguró que vendría mañana"],
        ["Verbos de sugerencia", "Nos aconsejó que fuéramos con cuidado"],
        ["Secuencia general", "Quería que estudiara / Me gustaría que viniera"]
    ]
    cons_examples = [
        {"spanish": "Me dijo que vendría y me pidió que lo esperara.", "english": "He told me he would come and asked me to wait for him."},
        {"spanish": "El profesor quería que entregáramos el trabajo hoy.", "english": "The teacher wanted us to hand in the assignment today."}
    ]
    cons_tip = "Maintain the past horizon: always check whether the main verb is past before deciding on the subordinate tense."
    
    cons_exs = [
        {"id": f"b1-{unit_num}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "El director me pidió que le _____ el informe financiero.", "options": ["enviara", "envíe", "enviaré", "enviaba"], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
        {"id": f"b1-{unit_num}.cons.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Carlos aseguró que _____ a la fiesta si terminaba el trabajo.", "answer": "iría", "english": "Carlos assured that he would go to the party if he finished work.", "teaches": ["estilo-indirecto-ordenes"]},
        {"id": f"b1-{unit_num}.cons.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Ella", "me", "pidió", "que", "le", "ayudara", "."], "solution": ["Ella", "me", "pidió", "que", "le", "ayudara", "."], "english": "She asked me to help her.", "teaches": ["estilo-indirecto-ordenes"]},
        {"id": f"b1-{unit_num}.cons.ex04", "category": "grammar", "type": "matching", "pairs": [["Me dijo que fuera", "He told me to go"], ["Dijo que iría", "He said he would go"], ["Quería que hablaras", "He wanted you to speak"], ["Sugirió que comiéramos", "He suggested we eat"]], "teaches": ["correlacion-temporal-subjuntivo"]},
        {"id": f"b1-{unit_num}.cons.ex05", "category": "listening", "type": "listening-choice", "sentence": "El guía nos aconsejó que lleváramos calzado cómodo para la caminata.", "options": ["Recomendó zapatos cómodos.", "Dijo que la caminata era corta.", "Pidió comprar zapatos nuevos."], "correct": 0, "teaches": ["correlacion-temporal-subjuntivo"]},
        {"id": f"b1-{unit_num}.cons.ex06", "category": "listening", "type": "dictation", "sentence": "Nos dijeron que esperaríamos unos minutos más.", "english": "They told us that we would wait a few minutes more.", "teaches": ["estilo-indirecto-ordenes"]},
        {"id": f"b1-{unit_num}.cons.ex07", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Beatriz", "text": "¿Qué te pidió tu jefe ayer?"}, {"speaker": "Antonio", "text": "____."}], "options": ["Me pidió que revisara los contratos pendientes.", "Me pidió que reviso.", "Me dice que revisara."], "correct": 0, "teaches": ["estilo-indirecto-ordenes"]},
        {"id": f"b1-{unit_num}.cons.ex08", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que tu amigo te dijo que llegaría a tiempo.", "answer": "Mi amigo me dijo que llegaría a tiempo."}], "teaches": ["estilo-indirecto-ordenes"]}
    ]
    
    generate_b1_unit(target_dir, unit_num, unit_title, lessons_data, cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs)

# ==========================================
# UNIT 39: Verbos de Cambio
# ==========================================
def build_unit_39(target_dir):
    unit_num = "39"
    unit_title = "The Nuances of Change: Spanish Verbs of Becoming"
    
    lessons_data = [
        {
            "num": "01",
            "title": "Ponerse + Adjective: Sudden & Temporary Changes",
            "goal": "Express rapid, involuntary, and reversible emotional or physical state changes with ponerse.",
            "grammar_title": "Ponerse + Adjective for Involuntary Emotional and Physical Changes",
            "grammar_slug": "ponerse-adjetivo-cambio",
            "grammar_text": "Use **ponerse + adjetivo** for changes that are rapid, involuntary, and generally temporary:\n\n• **Emotional / Mental states**: *Se puso rojo de vergüenza.* (He turned red with embarrassment.) *Me pongo nervioso al hablar en público.* (I get nervous speaking in public.)\n• **Physical conditions / Health**: *Se puso enfermo.* (He got sick.) *La sopa se puso fría.* (The soup got cold.)\n• **Appearance**: *Se puso pálido al ver el fantasma.* (He turned pale on seeing the ghost.)",
            "table_rows": [
                ["ponerse rojo", "to blush / turn red"],
                ["ponerse nervioso", "to get nervous"],
                ["ponerse enfermo / malo", "to get sick"],
                ["ponerse furioso / contento", "to become furious / happy"]
            ],
            "examples": [
                {"spanish": "Siempre me pongo nervioso antes de una entrevista de trabajo.", "english": "I always get nervous before a job interview."},
                {"spanish": "Cuando escuchó el cumplido, se puso completamente roja.", "english": "When she heard the compliment, she turned completely red."},
                {"spanish": "El niño se puso enfermo durante el fin de semana.", "english": "The child got sick during the weekend."}
            ],
            "tip": "*Ponerse* is temporary and reversible: you get nervous, but then calm down again.",
            "vocab": [
                {"lemma": "vergüenza", "translation": "embarrassment / shame", "pos": "noun"},
                {"lemma": "pálido", "translation": "pale", "pos": "adjective"},
                {"lemma": "nervioso", "translation": "nervous", "pos": "adjective"},
                {"lemma": "furioso", "translation": "furious", "pos": "adjective"},
                {"lemma": "cumplido", "translation": "compliment", "pos": "noun"},
                {"lemma": "enfermar", "translation": "to fall ill", "pos": "verb"},
                {"lemma": "contento", "translation": "happy / glad", "pos": "adjective"},
                {"lemma": "tranquilo", "translation": "calm", "pos": "adjective"},
                {"lemma": "reacción", "translation": "reaction", "pos": "noun"},
                {"lemma": "repentino", "translation": "sudden", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-01.ex01", "category": "grammar", "type": "multiple-choice", "question": "Cada vez que tiene que hablar en público, Carlos se _____ muy nervioso.", "options": ["pone", "hace", "vuelve", "queda"], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Ella se puso _____ de vergüenza al cometer el error.", "answer": "roja", "english": "She turned red with embarrassment upon making the mistake.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Me", "puse", "muy", "contento", "con", "tu", "visita", "."], "solution": ["Me", "puse", "muy", "contento", "con", "tu", "visita", "."], "english": "I became very happy with your visit.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Recibió un bonito _____ sobre su trabajo creativo.", "options": ["cumplido", "vergüenza", "pálido", "repentino"], "correct": 0, "teaches": ["b1-unit39-vocab"]},
                {"id": f"b1-{unit_num}-01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "El agua de la piscina se _____ fría por la noche.", "answer": "puso", "english": "The pool water became cold at night.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex06", "category": "grammar", "type": "matching", "pairs": [["Ponerse rojo", "To turn red / blush"], ["Ponerse nervioso", "To get nervous"], ["Ponerse enfermo", "To fall sick"], ["Ponerse contento", "To get happy"]], "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex07", "category": "listening", "type": "listening-choice", "sentence": "Al ver la factura inesperada, mi jefe se puso furioso.", "options": ["Reaccionó con enfado ante la factura.", "Pagó la factura con alegría.", "No vio la factura."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex08", "category": "listening", "type": "dictation", "sentence": "Me puse muy nervioso antes del examen oral.", "english": "I got very nervous before the oral exam.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucía", "text": "¿Por qué no saliste ayer con nosotros?"}, {"speaker": "Marcos", "text": "____."}], "options": ["Es que me puse enfermo con fiebre.", "Es que me volví enfermo.", "Es que me hice enfermo."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Profesor", "text": "¿Qué te pasó cuando te hicieron la pregunta?"}, {"speaker": "Alumno", "text": "____."}], "options": ["Me puse rojo de vergüenza porque no sabía la respuesta.", "Me quedé rojo.", "Me hice rojo."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que te pusiste muy contento con la noticia.", "answer": "Me puse muy contento con la noticia."}], "teaches": ["verbos-de-cambio"]}
            ]
        },
        {
            "num": "02",
            "title": "Quedarse: Resulting States, Loss & Disablement",
            "goal": "Express consequential states, loss, deprivation, and physical impairment using quedarse.",
            "grammar_title": "Quedarse for Resulting States, Loss, and Deprivation",
            "grammar_slug": "quedarse-adjetivo-consecuencia",
            "grammar_text": "Use **quedarse + adjetivo / participio** when a state is the direct *consequence* of a preceding event, often involving loss, surprise, or physical disablement:\n\n• **Reaction to news/shock**: *Se quedó sorprendido / boquiabierto.* (He was stunned / open-mouthed.) *Me quedé mudo.* (I was struck dumb.)\n• **Loss / Deprivation**: *Se quedó sin dinero / sin trabajo / calvo.* (He was left without money / jobless / went bald.)\n• **Physical conditions**: *Se quedó sordo / ciego.* (He went deaf / blind.)\n• **Sleep**: *Se quedó dormido en el sofá.* (He fell asleep on the couch).",
            "table_rows": [
                ["quedarse dormido", "to fall asleep"],
                ["quedarse sorprendido", "to be left surprised / stunned"],
                ["quedarse sin [algo]", "to run out of / be left without"],
                ["quedarse ciego / sordo / calvo", "to go blind / deaf / bald"]
            ],
            "examples": [
                {"spanish": "Me quedé dormido y llegué tarde a la oficina.", "english": "I overslept / fell asleep and arrived late at the office."},
                {"spanish": "Al oír la noticia, todos nos quedamos boquiabiertos.", "english": "Upon hearing the news, we were all left open-mouthed."},
                {"spanish": "Mi abuelo se quedó completamente sordo a los ochenta años.", "english": "My grandfather went completely deaf at age eighty."}
            ],
            "tip": "*Quedarse* always emphasizes the resulting aftermath of an event: *¿Cómo te quedaste? —Me quedé de piedra.*",
            "vocab": [
                {"lemma": "boquiabierto", "translation": "flabbergasted / open-mouthed", "pos": "adjective"},
                {"lemma": "calvo", "translation": "bald", "pos": "adjective"},
                {"lemma": "ciego", "translation": "blind", "pos": "adjective"},
                {"lemma": "sordo", "translation": "deaf", "pos": "adjective"},
                {"lemma": "de piedra", "translation": "stunned / petrified", "pos": "expression"},
                {"lemma": "sorprendido", "translation": "surprised", "pos": "adjective"},
                {"lemma": "pérdida", "translation": "loss", "pos": "noun"},
                {"lemma": "consecuencia", "translation": "consequence", "pos": "noun"},
                {"lemma": "quedarse sin", "translation": "to run out of / be left without", "pos": "verb"},
                {"lemma": "dormirse", "translation": "to fall asleep", "pos": "verb"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-02.ex01", "category": "grammar", "type": "multiple-choice", "question": "Estaba tan agotado que me _____ dormido en el tren.", "options": ["quedé", "puse", "hice", "volví"], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Al ver el precio del billete, nos quedamos _____ de asombro.", "answer": "boquiabiertos", "english": "Upon seeing the ticket price, we were left open-mouthed in astonishment.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Nos", "quedamos", "sin", "batería", "en", "el", "móvil", "."], "solution": ["Nos", "quedamos", "sin", "batería", "en", "el", "móvil", "."], "english": "We were left without battery on the phone.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "La empresa sufrió una grave _____ económica este trimestre.", "options": ["pérdida", "calvo", "ciego", "boquiabierto"], "correct": 0, "teaches": ["b1-unit39-vocab"]},
                {"id": f"b1-{unit_num}-02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Cuando supo el secreto, se _____ de piedra.", "answer": "quedó", "english": "When he found out the secret, he was stunned.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex06", "category": "grammar", "type": "matching", "pairs": [["Quedarse dormido", "To fall asleep / oversleep"], ["Quedarse sin blanca", "To be broke / penniless"], ["Quedarse sordo", "To go deaf"], ["Quedarse de piedra", "To be petrified / shocked"]], "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex07", "category": "listening", "type": "listening-choice", "sentence": "A mitad de la presentación nos quedamos sin conexión a internet.", "options": ["Perdieron el acceso a la red durante la charla.", "La presentación fue un éxito en línea.", "Compraron un router nuevo."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex08", "category": "listening", "type": "dictation", "sentence": "Todos nos quedamos muy sorprendidos con el resultado final.", "english": "We were all very surprised with the final result.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Elena", "text": "¿Por qué no llamaste ayer por la tarde?"}, {"speaker": "Pedro", "text": "____."}], "options": ["Es que me quedé sin batería en el teléfono.", "Es que me puse sin batería.", "Es que me volví sin batería."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Sofía", "text": "¿Cómo reaccionó tu jefe ante la renuncia?"}, {"speaker": "Javier", "text": "____."}], "options": ["Se quedó completamente boquiabierto.", "Se puso boquiabierto.", "Se hizo boquiabierto."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que te quedaste dormido viendo la película.", "answer": "Me quedé dormido viendo la película."}], "teaches": ["verbos-de-cambio"]}
            ]
        },
        {
            "num": "03",
            "title": "Volverse: Radical and Lasting Personality Shifts",
            "goal": "Describe deep, lasting, and often involuntary personality, psychological, or behavioral transformations with volverse.",
            "grammar_title": "Volverse + Adjective for Personality and Character Shifts",
            "grammar_slug": "volverse-adjetivo-personalidad",
            "grammar_text": "Use **volverse + adjetivo** for transformations in character, attitude, or psychological state that are radical and lasting:\n\n• **Personality changes**: *Se ha vuelto muy desconfiado con los años.* (He has become very distrustful over the years.) *Con la fama se volvió arrogante.* (With fame he became arrogant.)\n• **Mental state / Obsession**: *Esa música me vuelve loco.* (That music drives me crazy.) *Se volvió loco de amor.* (He went mad with love.)\n• **Difficulty/Condition**: *La situación se ha vuelto insoportable.* (The situation has become unbearable.)",
            "table_rows": [
                ["volverse loco", "to go crazy / mad"],
                ["volverse desconfiado", "to become distrustful"],
                ["volverse exigente", "to become demanding"],
                ["volverse insoportable", "to become unbearable"]
            ],
            "examples": [
                {"spanish": "Desde que ganó la lotería, se ha vuelto muy tacaño.", "english": "Ever since he won the lottery, he has become very stingy."},
                {"spanish": "Con la edad, mi abuela se volvió mucho más tolerante.", "english": "With age, my grandmother became much more tolerant."},
                {"spanish": "El tráfico en la ciudad se está volviendo imposible.", "english": "Traffic in the city is becoming impossible."}
            ],
            "tip": "*Volverse* implies a lasting change in essence or behavior, unlike the temporary nature of *ponerse*.",
            "vocab": [
                {"lemma": "desconfiado", "translation": "distrustful / suspicious", "pos": "adjective"},
                {"lemma": "arrogante", "translation": "arrogant", "pos": "adjective"},
                {"lemma": "tacaño", "translation": "stingy / cheap", "pos": "adjective"},
                {"lemma": "tolerante", "translation": "tolerant", "pos": "adjective"},
                {"lemma": "insoportable", "translation": "unbearable", "pos": "adjective"},
                {"lemma": "loco", "translation": "crazy / mad", "pos": "adjective"},
                {"lemma": "exigente", "translation": "demanding", "pos": "adjective"},
                {"lemma": "personalidad", "translation": "personality", "pos": "noun"},
                {"lemma": "carácter", "translation": "character", "pos": "noun"},
                {"lemma": "transformación", "translation": "transformation", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-03.ex01", "category": "grammar", "type": "multiple-choice", "question": "Con los años y los desengaños, Carlos se ha _____ muy desconfiado.", "options": ["vuelto", "puesto", "hecho", "quedado"], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Este ruido constante me está volviendo _____.", "answer": "loco", "english": "This constant noise is driving me crazy.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["La", "situación", "se", "volvió", "totalmente", "insoportable", "."], "solution": ["La", "situación", "se", "volvió", "totalmente", "insoportable", "."], "english": "The situation became totally unbearable.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "A pesar de su riqueza, tiene fama de ser muy _____.", "options": ["tacaño", "tolerante", "insoportable", "transformación"], "correct": 0, "teaches": ["b1-unit39-vocab"]},
                {"id": f"b1-{unit_num}-03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Desde que ascendió a director, se _____ muy distante y frío.", "answer": "volvió", "english": "Ever since he was promoted to director, he became very distant and cold.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex06", "category": "grammar", "type": "matching", "pairs": [["Volverse loco", "To go crazy"], ["Volverse tacaño", "To become stingy"], ["Volverse exigente", "To become demanding"], ["Volverse distante", "To become distant"]], "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex07", "category": "listening", "type": "listening-choice", "sentence": "No sé qué le pasa a Laura, últimamente se ha vuelto súper irritable.", "options": ["Observa un cambio duradero en su carácter.", "Dice que Laura está contenta.", "Laura no cambió en nada."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex08", "category": "listening", "type": "dictation", "sentence": "Con el paso del tiempo nos volvimos muy buenos amigos.", "english": "With the passage of time we became very good friends.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Marcos", "text": "¿Has notado algún cambio en Andrés?"}, {"speaker": "Elena", "text": "____."}], "options": ["Sí, desde que vive solo se ha vuelto muy ordenado.", "Sí, se ha puesto ordenado.", "Sí, se quedó ordenado."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Beatriz", "text": "¡Ese perro ladra sin parar toda la noche!"}, {"speaker": "David", "text": "____."}], "options": ["¡A mí también me vuelve loco ese ruido!", "A mí también me pone loco.", "A mí también me hace loco."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que con el tiempo te has vuelto más paciente.", "answer": "Con el tiempo me he vuelto más paciente."}], "teaches": ["verbos-de-cambio"]}
            ]
        },
        {
            "num": "04",
            "title": "Hacerse, Convertirse en & Llegar a ser: Effort and Culmination",
            "goal": "Express voluntary social transformation with hacerse, categorical mutation with convertirse en, and culminating career attainment with llegar a ser.",
            "grammar_title": "Hacerse, Convertirse en, and Llegar a ser",
            "grammar_slug": "hacerse-convertirse-llegar-a-ser",
            "grammar_text": "Spanish distinguishes voluntary professional, ideological, or culminating life changes:\n\n• **Hacerse + sustantivo / adjetivo**: Voluntary transformation involving effort, ideology, or passage of time: *Se hizo médico.* (He became a doctor.) *Se hizo vegetariano / budista.* (He became vegetarian / Buddhist.) *Se hace tarde.* (It's getting late.)\n• **Convertirse en + sustantivo**: Radical mutation or transformation: *La oruga se convirtió en mariposa.* (The caterpillar turned into a butterfly.) *La novela se convirtió en un superventas.* (The novel became a bestseller.)\n• **Llegar a ser**: The supreme culmination of long effort and ambition: *Tras décadas de trabajo, llegó a ser presidente de la compañía.* (After decades of work, he got to be company president.)",
            "table_rows": [
                ["hacerse médico / abogado", "to become a doctor / lawyer (effort)"],
                ["hacerse vegetariano", "to become vegetarian (ideology)"],
                ["convertirse en éxito", "to turn into a success (transformation)"],
                ["llegar a ser director", "to reach the level of director (culmination)"]
            ],
            "examples": [
                {"spanish": "Estudió durante diez años para hacerse cirujano.", "english": "He studied for ten years to become a surgeon."},
                {"spanish": "Ese pequeño pueblo costero se convirtió en un gran centro turístico.", "english": "That small coastal town turned into a major tourist center."},
                {"spanish": "Con perseverancia y talento, llegó a ser una de las científicas más respetadas.", "english": "With perseverance and talent, she came to be one of the most respected scientists."}
            ],
            "tip": "Use *convertirse en* when a noun follows indicating a complete metamorphosis, and *hacerse* for professions and personal philosophies.",
            "vocab": [
                {"lemma": "cirujano", "translation": "surgeon", "pos": "noun"},
                {"lemma": "vegetariano", "translation": "vegetarian", "pos": "adjective"},
                {"lemma": "budista", "translation": "Buddhist", "pos": "adjective"},
                {"lemma": "perseverancia", "translation": "perseverance", "pos": "noun"},
                {"lemma": "culminación", "translation": "culmination", "pos": "noun"},
                {"lemma": "mariposa", "translation": "butterfly", "pos": "noun"},
                {"lemma": "metamorfosis", "translation": "metamorphosis", "pos": "noun"},
                {"lemma": "turístico", "translation": "tourist / touristic", "pos": "adjective"},
                {"lemma": "ideología", "translation": "ideology", "pos": "noun"},
                {"lemma": "llegar a ser", "translation": "to come to be / reach", "pos": "verb"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-04.ex01", "category": "grammar", "type": "multiple-choice", "question": "Después de muchos años de estudio en la universidad, Elena se _____ abogada.", "options": ["hizo", "puso", "volvió", "quedó"], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "La pequeña empresa se convirtió _____ un gigante tecnológico.", "answer": "en", "english": "The small company turned into a tech giant.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Llegó", "a", "ser", "presidente", "de", "la", "nación", "."], "solution": ["Llegó", "a", "ser", "presidente", "de", "la", "nación", "."], "english": "He came to be president of the nation.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Gracias a su incansable _____, superó todas las barreras.", "options": ["perseverancia", "mariposa", "cirujano", "turístico"], "correct": 0, "teaches": ["b1-unit39-vocab"]},
                {"id": f"b1-{unit_num}-04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Mis primos se _____ vegetarianos por respeto a los animales.", "answer": "hicieron", "english": "My cousins became vegetarian out of respect for animals.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex06", "category": "grammar", "type": "matching", "pairs": [["Hacerse médico", "To become a doctor"], ["Convertirse en símbolo", "To turn into a symbol"], ["Llegar a ser ministro", "To reach the rank of minister"], ["Hacerse tarde", "To get late"]], "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex07", "category": "listening", "type": "listening-choice", "sentence": "Aquel invento sencillo se convirtió en una revolución mundial.", "options": ["El invento provocó una gran transformación.", "El invento no funcionó.", "Nadie conoció el invento."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex08", "category": "listening", "type": "dictation", "sentence": "Con mucho esfuerzo llegó a ser un gran pianista.", "english": "With much effort he came to be a great pianist.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿A qué se dedica tu hermano mayor ahora?"}, {"speaker": "Marta", "text": "____."}], "options": ["Se hizo arquitecto y trabaja en Sevilla.", "Se puso arquitecto.", "Se volvió arquitecto."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Raúl", "text": "¿Qué te pareció la nueva canción de la banda?"}, {"speaker": "Sara", "text": "____."}], "options": ["¡Increíble! En pocos días se convirtió en un éxito total.", "Se puso un éxito.", "Se hizo un éxito."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que tu amiga se hizo profesora de español.", "answer": "Mi amiga se hizo profesora de español."}], "teaches": ["verbos-de-cambio"]}
            ]
        },
        {
            "num": "05",
            "title": "Mastering the Spectrum of Change in Spanish",
            "goal": "Select accurately between ponerse, quedarse, volverse, hacerse, and convertirse en in real-time Spanish narratives.",
            "grammar_title": "Comparative Synthesis of Verbs of Becoming",
            "grammar_slug": "sintesis-verbos-cambio",
            "grammar_text": "Choose the right verb of change based on voluntary nature, duration, and result:\n\n• **Ponerse**: Involuntary, sudden, temporary (*Me puse furioso*).\n• **Quedarse**: Consequence, loss, surprise (*Se quedó sin blanca, se quedó dormido*).\n• **Volverse**: Lasting personality/behavioral shift (*Se volvió desconfiado*).\n• **Hacerse**: Voluntary effort, profession, ideology, time (*Se hizo médico, se hace tarde*).\n• **Convertirse en**: Total metamorphosis (*Se convirtió en oro*).\n• **Llegar a ser**: Supreme career/life culmination (*Llegó a ser líder*).",
            "table_rows": [
                ["Rápido y pasajero", "ponerse (rojo, nervioso)"],
                ["Consecuencia y pérdida", "quedarse (sin nada, dormido)"],
                ["Carácter duradero", "volverse (loco, tacaño)"],
                ["Profesión y esfuerzo", "hacerse (médico) / llegar a ser"]
            ],
            "examples": [
                {"spanish": "Al oír la noticia se puso pálido, luego se quedó en silencio y finalmente se volvió reflexivo.", "english": "On hearing the news he turned pale, then fell silent and finally became reflective."},
                {"spanish": "Estudió duro para hacerse abogada y con los años llegó a ser jueza.", "english": "She studied hard to become a lawyer and over the years came to be a judge."},
                {"spanish": "El viejo taller se convirtió en un restaurante de moda.", "english": "The old workshop turned into a trendy restaurant."}
            ],
            "tip": "Ask: Is it sudden/temporary (ponerse)? A resulting loss (quedarse)? A personality shift (volverse)? Or voluntary effort (hacerse)?",
            "vocab": [
                {"lemma": "espectro", "translation": "spectrum", "pos": "noun"},
                {"lemma": "matiz", "translation": "nuance", "pos": "noun"},
                {"lemma": "voluntario", "translation": "voluntary", "pos": "adjective"},
                {"lemma": "involuntario", "translation": "involuntary", "pos": "adjective"},
                {"lemma": "duradero", "translation": "lasting / durable", "pos": "adjective"},
                {"lemma": "pasajero", "translation": "fleeting / temporary", "pos": "adjective"},
                {"lemma": "silencio", "translation": "silence", "pos": "noun"},
                {"lemma": "reflexivo", "translation": "reflective", "pos": "adjective"},
                {"lemma": "distinguir", "translation": "to distinguish", "pos": "verb"},
                {"lemma": "maestría", "translation": "mastery", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-05.ex01", "category": "grammar", "type": "multiple-choice", "question": "Al escuchar el grito en la oscuridad, todos nos _____ helados de miedo.", "options": ["quedamos", "pusimos", "hicimos", "volvimos"], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Con los años y el trabajo duro, llegó a _____ decano de la facultad.", "answer": "ser", "english": "With the years and hard work, he came to be dean of the faculty.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Ella", "se", "puso", "roja", "de", "la", "vergüenza", "."], "solution": ["Ella", "se", "puso", "roja", "de", "la", "vergüenza", "."], "english": "She turned red with embarrassment.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Este cambio de humor no es permanente, es solo algo _____.", "options": ["pasajero", "duradero", "espectro", "maestría"], "correct": 0, "teaches": ["b1-unit39-vocab"]},
                {"id": f"b1-{unit_num}-05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Ese libro se convirtió _____ un fenómeno literario mundial.", "answer": "en", "english": "That book turned into a global literary phenomenon.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex06", "category": "grammar", "type": "matching", "pairs": [["Ponerse enfermo", "Sudden temporary state"], ["Quedarse ciego", "Consequential loss"], ["Volverse tacaño", "Personality shift"], ["Hacerse ingeniero", "Voluntary achievement"]], "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex07", "category": "listening", "type": "listening-choice", "sentence": "Al principio se puso nervioso, pero luego se quedó tranquilo y todo salió genial.", "options": ["Pasó del nerviosismo a la tranquilidad.", "Estuvo nervioso todo el tiempo.", "No quiso participar."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex08", "category": "listening", "type": "dictation", "sentence": "Con el tiempo se volvió un experto en la materia.", "english": "Over time he became an expert on the subject.", "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Andrés", "text": "¿Por qué no respondiste a mis llamadas?"}, {"speaker": "Beatriz", "text": "____."}], "options": ["Es que me quedé sin saldo y sin batería.", "Es que me volví sin saldo.", "Es que me puse sin saldo."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Javier", "text": "¿Cómo terminó la historia del antiguo convento?"}, {"speaker": "Marta", "text": "____."}], "options": ["Se convirtió en un hermoso hotel boutique.", "Se puso un hotel.", "Se hizo en un hotel."], "correct": 0, "teaches": ["verbos-de-cambio"]},
                {"id": f"b1-{unit_num}-05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que te pusiste nervioso antes de la entrevista.", "answer": "Me puse nervioso antes de la entrevista."}], "teaches": ["verbos-de-cambio"]}
            ]
        }
    ]
    
    cons_title = "Consolidation: Verbs of Becoming"
    cons_goal = "Master the five distinct Spanish verbs of change for precise characterization."
    cons_gr_text = "Spanish distinguishes verbs of change through intention, speed, and permanence:\n• Ponerse: sudden & temporary emotion/physical state\n• Quedarse: consequence, aftermath, loss\n• Volverse: radical & lasting character shift\n• Hacerse: effort, profession, ideology\n• Convertirse en: transformation into a new entity."
    cons_table_rows = [
        ["Ponerse", "Me puse alegre / rojo / enfermo"],
        ["Quedarse", "Me quedé sorprendido / sin dinero"],
        ["Volverse", "Se volvió arrogante / loco"],
        ["Hacerse / Convertirse en", "Se hizo abogado / Se convirtió en éxito"]
    ]
    cons_examples = [
        {"spanish": "Al oír la noticia se puso pálido y se quedó mudo.", "english": "On hearing the news he turned pale and was struck dumb."},
        {"spanish": "Estudió con dedicación y se hizo médico.", "english": "He studied with dedication and became a doctor."}
    ]
    cons_tip = "Avoid using *volverse* for temporary feelings: say *me puse triste*, not *me volví triste*."
    
    cons_exs = [
        {"id": f"b1-{unit_num}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "Al escuchar el trueno, el gato se _____ muy asustado.", "options": ["puso", "hizo", "volvió", "quedó"], "correct": 0, "teaches": ["verbos-de-cambio"]},
        {"id": f"b1-{unit_num}.cons.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Nos quedamos _____ de piedra al ver el resultado.", "answer": "totalmente", "english": "We were totally stunned upon seeing the result.", "teaches": ["verbos-de-cambio"]},
        {"id": f"b1-{unit_num}.cons.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Se", "hizo", "vegetariana", "por", "razones", "éticas", "."], "solution": ["Se", "hizo", "vegetariana", "por", "razones", "éticas", "."], "english": "She became vegetarian for ethical reasons.", "teaches": ["verbos-de-cambio"]},
        {"id": f"b1-{unit_num}.cons.ex04", "category": "grammar", "type": "matching", "pairs": [["Ponerse rojo", "Sudden blushing"], ["Quedarse sin saldo", "Consequential loss"], ["Volverse intolerante", "Personality shift"], ["Llegar a ser decano", "Career culmination"]], "teaches": ["verbos-de-cambio"]},
        {"id": f"b1-{unit_num}.cons.ex05", "category": "listening", "type": "listening-choice", "sentence": "Con perseverancia y pasión, la joven investigadora llegó a ser una figura clave.", "options": ["Alcanzó una posición destacada gracias a su esfuerzo.", "Abandonó la investigación.", "No tuvo éxito en su carrera."], "correct": 0, "teaches": ["verbos-de-cambio"]},
        {"id": f"b1-{unit_num}.cons.ex06", "category": "listening", "type": "dictation", "sentence": "Al terminar la fiesta nos quedamos recogiendo el salón.", "english": "When the party ended we stayed tidying the living room.", "teaches": ["verbos-de-cambio"]},
        {"id": f"b1-{unit_num}.cons.ex07", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿Por qué no vino Tomás a la cena?"}, {"speaker": "Elena", "text": "____."}], "options": ["Es que se puso enfermo a última hora.", "Es que se hizo enfermo.", "Es que se volvió enfermo."], "correct": 0, "teaches": ["verbos-de-cambio"]},
        {"id": f"b1-{unit_num}.cons.ex08", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que te pusiste muy contento con el regalo.", "answer": "Me puse muy contento con el regalo."}], "teaches": ["verbos-de-cambio"]}
    ]
    
    generate_b1_unit(target_dir, unit_num, unit_title, lessons_data, cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs)

# ==========================================
# UNIT 40: Régimen Preposicional, Sino & Lo Neutro
# ==========================================
def build_unit_40(target_dir):
    unit_num = "40"
    unit_title = "Advanced Connectors & Prepositional Regimes"
    
    lessons_data = [
        {
            "num": "01",
            "title": "Verbs with Fixed Prepositions (Régimen Preposicional)",
            "goal": "Master high-frequency Spanish verbs requiring fixed prepositions (soñar con, pensar en, contar con, depender de, insistir en, enterarse de).",
            "grammar_title": "Verbs Requiring Inherent Prepositions",
            "grammar_slug": "verbos-regimen-preposicional",
            "grammar_text": "Many essential Spanish verbs require specific prepositions that differ entirely from English equivalents:\n\n• **con**: *soñar con* (to dream of/about), *contar con* (to count on / have at disposal)\n• **en**: *pensar en* (to think about), *insistir en* (to insist on), *confiar en* (to trust in)\n• **de**: *depender de* (to depend on), *enterarse de* (to find out about), *acordarse de* (to remember)\n• **a**: *acostumbrarse a* (to get used to), *negarse a* (to refuse to).",
            "table_rows": [
                ["soñar con algo / alguien", "to dream of / about"],
                ["pensar en algo / alguien", "to think about"],
                ["contar con alguien", "to count on someone"],
                ["depender de algo", "to depend on something"]
            ],
            "examples": [
                {"spanish": "Siempre sueño con viajar por toda América Latina.", "english": "I always dream of traveling all over Latin America."},
                {"spanish": "Puedes contar conmigo para lo que necesites.", "english": "You can count on me for whatever you need."},
                {"spanish": "El éxito del proyecto depende de nuestro esfuerzo colectivo.", "english": "The success of the project depends on our collective effort."}
            ],
            "tip": "Never say *pensar de* for 'think about' (say *pensar en*). *¿Qué piensas de eso?* means 'what's your opinion of that?'.",
            "vocab": [
                {"lemma": "soñar con", "translation": "to dream of / about", "pos": "verb"},
                {"lemma": "pensar en", "translation": "to think about", "pos": "verb"},
                {"lemma": "contar con", "translation": "to count on", "pos": "verb"},
                {"lemma": "depender de", "translation": "to depend on", "pos": "verb"},
                {"lemma": "insistir en", "translation": "to insist on", "pos": "verb"},
                {"lemma": "enterarse de", "translation": "to find out about", "pos": "verb"},
                {"lemma": "confiar en", "translation": "to trust / rely on", "pos": "verb"},
                {"lemma": "negarse a", "translation": "to refuse to", "pos": "verb"},
                {"lemma": "régimen", "translation": "governing regime", "pos": "noun"},
                {"lemma": "preposición", "translation": "preposition", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-01.ex01", "category": "grammar", "type": "multiple-choice", "question": "Anoche soñé _____ que volaba sobre el océano.", "options": ["con", "de", "en", "por"], "correct": 0, "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Pienso _____ ti todos los días.", "answer": "en", "english": "I think about you every day.", "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Puedes", "contar", "con", "mi", "ayuda", "."], "solution": ["Puedes", "contar", "con", "mi", "ayuda", "."], "english": "You can count on my help.", "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Me negué rotundamente a _____ esas condiciones injustas.", "options": ["aceptar", "régimen", "preposición", "negarse a"], "correct": 0, "teaches": ["b1-unit40-vocab"]},
                {"id": f"b1-{unit_num}-01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "El resultado final depende _____ la decisión del juez.", "answer": "de", "english": "The final result depends on the judge's decision.", "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex06", "category": "grammar", "type": "matching", "pairs": [["Soñar con", "To dream of"], ["Pensar en", "To think about"], ["Contar con", "To count on"], ["Depender de", "To depend on"]], "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex07", "category": "listening", "type": "listening-choice", "sentence": "¿Te has enterado ya de la noticia de la boda de Carlos?", "options": ["Pregunta si supo de la noticia.", "Informa que no habrá boda.", "Pide invitar a Carlos."], "correct": 0, "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex08", "category": "listening", "type": "dictation", "sentence": "Insistieron en pagar la cuenta del restaurante.", "english": "They insisted on paying the restaurant bill.", "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿Puedo pedirte un favor para mañana?"}, {"speaker": "Marta", "text": "____."}], "options": ["Por supuesto, sabes que puedes contar conmigo.", "Por supuesto, puedes contar en mí.", "Sabes que dependo con ti."], "correct": 0, "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Sofía", "text": "¿Saldremos a caminar esta tarde?"}, {"speaker": "Javier", "text": "____."}], "options": ["Depende del tiempo que haga afuera.", "Depende con el tiempo.", "Sueño con el tiempo."], "correct": 0, "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que siempre piensas en tus amigos.", "answer": "Siempre pienso en mis amigos."}], "teaches": ["verbos-regimen-preposicional-avanzado"]}
            ]
        },
        {
            "num": "02",
            "title": "Adversative Contrast: Pero vs. Sino vs. Sino Que",
            "goal": "Differentiate between pero (contrast/qualification) and sino / sino que (corrective replacement after negation).",
            "grammar_title": "Contrasts: Pero, Sino, and Sino que",
            "grammar_slug": "pero-vs-sino-sino-que",
            "grammar_text": "Spanish has two distinct ways to translate 'but':\n\n• **Pero**: Adds a contrast, nuance, or limitation to a statement (positive or negative):\n  *Estudié mucho, pero no aprobé.* (I studied a lot, but didn't pass.)\n• **Sino**: Used strictly **after a negative clause** to substitute or correct an element (*not X, but rather Y*):\n  *No quiero té, sino café.* (I don't want tea, but coffee.)\n  *No es español, sino portugués.* (He is not Spanish, but Portuguese.)\n• **Sino que**: Used when the correction contains a **conjugated verb**:\n  *No fue al cine, sino que se quedó en casa estudiando.* (He didn't go to the movies, but rather stayed home studying.)",
            "table_rows": [
                ["pero (contraste general)", "Es caro, pero de buena calidad."],
                ["sino (sustitución no-verbal)", "No es rojo, sino azul."],
                ["sino que (sustitución con verbo)", "No salió, sino que durmió."],
                ["no solo... sino también...", "No solo trabaja, sino que también estudia."]
            ],
            "examples": [
                {"spanish": "No fuimos en avión, sino en tren.", "english": "We didn't go by plane, but by train."},
                {"spanish": "No perdí el documento, sino que se lo entregué al director.", "english": "I didn't lose the document, but rather handed it to the director."},
                {"spanish": "El examen era difícil, pero todos aprobamos.", "english": "The exam was difficult, but we all passed."}
            ],
            "tip": "Formula: Negative clause + noun/adj = **sino**. Negative clause + conjugated verb = **sino que**.",
            "vocab": [
                {"lemma": "sino", "translation": "but rather (after negative)", "pos": "conjunction"},
                {"lemma": "sino que", "translation": "but rather (with verb)", "pos": "conjunction"},
                {"lemma": "pero", "translation": "but (contrast)", "pos": "conjunction"},
                {"lemma": "corrección", "translation": "correction", "pos": "noun"},
                {"lemma": "adversativo", "translation": "adversative", "pos": "adjective"},
                {"lemma": "sustituir", "translation": "to substitute", "pos": "verb"},
                {"lemma": "limitar", "translation": "to limit", "pos": "verb"},
                {"lemma": "contraste", "translation": "contrast", "pos": "noun"},
                {"lemma": "afirmación", "translation": "affirmation", "pos": "noun"},
                {"lemma": "no solo", "translation": "not only", "pos": "expression"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-02.ex01", "category": "grammar", "type": "multiple-choice", "question": "No quiero agua fría, _____ un café bien caliente.", "options": ["sino", "pero", "sino que", "aunque"], "correct": 0, "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Ayer no salimos al parque, sino _____ nos quedamos en casa.", "answer": "que", "english": "Yesterday we didn't go out to the park, but rather we stayed home.", "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["No", "es", "mi", "primo", ",", "sino", "mi", "hermano", "."], "solution": ["No", "es", "mi", "primo", ",", "sino", "mi", "hermano", "."], "english": "He is not my cousin, but my brother.", "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "El profesor hizo una pequeña _____ en mi redacción.", "options": ["corrección", "contraste", "afirmación", "sino"], "correct": 0, "teaches": ["b1-unit40-vocab"]},
                {"id": f"b1-{unit_num}-02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "El piso es pequeño, _____ tiene mucha luz natural.", "answer": "pero", "english": "The apartment is small, but has a lot of natural light.", "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex06", "category": "grammar", "type": "matching", "pairs": [["No café, sino té", "Sino (noun substitution)"], ["No durmió, sino que leyó", "Sino que (verb substitution)"], ["Es caro, pero bueno", "Pero (simple contrast)"], ["No solo rico, sino sano", "No solo... sino..."]], "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex07", "category": "listening", "type": "listening-choice", "sentence": "No me molestó lo que dijo, sino el tono con el que me habló.", "options": ["Le molestó el tono, no las palabras.", "Le gustaron las palabras.", "No le importó nada."], "correct": 0, "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex08", "category": "listening", "type": "dictation", "sentence": "No compramos el coche rojo, sino el azul.", "english": "We didn't buy the red car, but the blue one.", "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿Fuiste a la fiesta de disfraces ayer?"}, {"speaker": "Marcos", "text": "____."}], "options": ["No fui a la fiesta, sino que me quedé estudiando.", "No fui, pero que me quedé.", "No fui sino estudié."], "correct": 0, "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Elena", "text": "¿Ese libro es de aventuras?"}, {"speaker": "Sara", "text": "____."}], "options": ["No es de aventuras, sino de misterio histórico.", "No es de aventuras pero de misterio.", "No es de aventuras sino que de misterio."], "correct": 0, "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que no quieres té, sino café.", "answer": "No quiero té, sino café."}], "teaches": ["sino-vs-pero"]}
            ]
        },
        {
            "num": "03",
            "title": "The Neuter Article 'Lo': Abstract Concepts",
            "goal": "Use the neuter article lo with masculine adjectives to nominalize abstract qualities (lo importante, lo bueno, lo difícil).",
            "grammar_title": "The Neuter Article Lo for Abstract Qualities",
            "grammar_slug": "lo-neutro-cualidades-abstractas",
            "grammar_text": "Spanish has no neuter nouns, but possesses the powerful neuter article **lo**. When combined with the masculine singular form of an adjective, it converts the adjective into an abstract noun meaning 'the [adjective] thing' or 'what is [adjective]':\n\n• **lo bueno**: the good thing / what is good\n• **lo malo**: the bad thing / the downside\n• **lo importante**: the important thing / what matters\n• **lo difícil**: the difficult part / what is hard\n• **lo mejor / lo peor**: the best thing / the worst thing.",
            "table_rows": [
                ["lo importante", "the important thing / what matters"],
                ["lo bueno / lo malo", "the good thing / the bad thing"],
                ["lo difícil", "the difficult part"],
                ["lo mejor / lo peor", "the best / worst thing"]
            ],
            "examples": [
                {"spanish": "Lo importante es participar y aprender de los errores.", "english": "The important thing is to participate and learn from mistakes."},
                {"spanish": "Lo bueno de vivir en el centro es que todo queda cerca.", "english": "The good thing about living downtown is that everything is close."},
                {"spanish": "Lo difícil de este idioma son las conjugaciones verbales.", "english": "The difficult part of this language is the verb conjugations."}
            ],
            "tip": "*Lo* is NEVER used before nouns (never *lo libro*). Use *lo* ONLY with adjectives, adverbs, or past participles.",
            "vocab": [
                {"lemma": "lo importante", "translation": "the important thing", "pos": "expression"},
                {"lemma": "lo bueno", "translation": "the good thing", "pos": "expression"},
                {"lemma": "lo malo", "translation": "the bad thing", "pos": "expression"},
                {"lemma": "lo difícil", "translation": "the difficult part", "pos": "expression"},
                {"lemma": "lo mejor", "translation": "the best thing", "pos": "expression"},
                {"lemma": "lo peor", "translation": "the worst thing", "pos": "expression"},
                {"lemma": "abstracto", "translation": "abstract", "pos": "adjective"},
                {"lemma": "cualidad", "translation": "quality", "pos": "noun"},
                {"lemma": "sustantivar", "translation": "to nominalize", "pos": "verb"},
                {"lemma": "ventaja", "translation": "advantage", "pos": "noun"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-03.ex01", "category": "grammar", "type": "multiple-choice", "question": "_____ importante en la vida es mantener la calma ante las dificultades.", "options": ["Lo", "El", "La", "Le"], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Lo _____ de este restaurante es su terraza con vistas al mar.", "answer": "bueno", "english": "The good thing about this restaurant is its terrace with sea views.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Lo", "difícil", "es", "empezar", "el", "proyecto", "."], "solution": ["Lo", "difícil", "es", "empezar", "el", "proyecto", "."], "english": "The difficult part is starting the project.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "Vivir cerca de la estación tiene una gran _____ para viajar.", "options": ["ventaja", "abstracto", "cualidad", "sustantivar"], "correct": 0, "teaches": ["b1-unit40-vocab"]},
                {"id": f"b1-{unit_num}-03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Lo _____ de mudarse de ciudad es tener que despedirse de los amigos.", "answer": "malo", "english": "The bad thing about moving cities is having to say goodbye to friends.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex06", "category": "grammar", "type": "matching", "pairs": [["Lo bueno", "The good thing"], ["Lo malo", "The bad thing"], ["Lo difícil", "The hard part"], ["Lo mejor", "The best thing"]], "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex07", "category": "listening", "type": "listening-choice", "sentence": "Lo interesante del debate fue la variedad de puntos de vista.", "options": ["Destaca la diversidad de opiniones en el debate.", "El debate fue aburrido.", "Nadie quiso participar."], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex08", "category": "listening", "type": "dictation", "sentence": "Lo principal es comprender las necesidades de los clientes.", "english": "The main thing is to understand the clients' needs.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Carlos", "text": "¿Qué te pareció el curso de fotografía?"}, {"speaker": "Meg", "text": "____."}], "options": ["Lo mejor fueron las salidas prácticas por la ciudad.", "El mejor fueron las salidas.", "La mejor fue las salidas."], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Profesor", "text": "¿Cuál es la clave para aprender un idioma?"}, {"speaker": "Estudiante", "text": "____."}], "options": ["Lo fundamental es practicar todos los días.", "El fundamental es practicar.", "La fundamental es practicar."], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que lo importante es ser feliz.", "answer": "Lo importante es ser feliz."}], "teaches": ["lo-neutro-abstraccion"]}
            ]
        },
        {
            "num": "04",
            "title": "Emphatic Lo: Lo + Adjective + Que (How... It Was!)",
            "goal": "Use emphatic lo + adjective/adverb + que to express intensity ('how difficult it was', 'how fast he runs').",
            "grammar_title": "Emphatic Structures with Lo + Adjective/Adverb + Que",
            "grammar_slug": "lo-enfatico-grado-intensidad",
            "grammar_text": "When expressing intensity or degree, **lo + adjetivo / adverbio + que** translates to 'how [adjective/adverb] ... is/was!':\n\n• **With adjective** (agrees in gender and number with the noun!):\n  *No sabes lo difícil que fue el examen.* (You don't know how difficult the exam was.)\n  *Mira lo contentas que están las chicas.* (Look how happy the girls are.)\n• **With adverb** (invariable):\n  *¡No te imaginas lo rápido que corre!* (You can't imagine how fast he runs!)\n  *Me sorprende lo bien que hablas español.* (I'm amazed at how well you speak Spanish.)",
            "table_rows": [
                ["lo difícil que fue", "how difficult it was"],
                ["lo contentas que están", "how happy they are (fem. pl.)"],
                ["lo bien que canta", "how well she sings"],
                ["lo rápido que pasa el tiempo", "how quickly time flies"]
            ],
            "examples": [
                {"spanish": "No te imaginas lo cansada que terminé después de la excursión.", "english": "You can't imagine how tired I ended up after the hike."},
                {"spanish": "Es increíble lo rápido que aprenden los niños pequeños.", "english": "It's incredible how fast young children learn."},
                {"spanish": "Me di cuenta de lo complicado que era resolver el enigma.", "english": "I realized how complicated it was to solve the riddle."}
            ],
            "tip": "Notice that unlike abstract *lo bueno* (always masculine singular), in emphatic *lo + adj + que*, the adjective agrees with the subject: *lo contenta que está Elena*.",
            "vocab": [
                {"lemma": "enfático", "translation": "emphatic", "pos": "adjective"},
                {"lemma": "intensidad", "translation": "intensity", "pos": "noun"},
                {"lemma": "grado", "translation": "degree / extent", "pos": "noun"},
                {"lemma": "enigma", "translation": "riddle / enigma", "pos": "noun"},
                {"lemma": "asombroso", "translation": "astonishing", "pos": "adjective"},
                {"lemma": "cansancio", "translation": "fatigue / tiredness", "pos": "noun"},
                {"lemma": "rapidez", "translation": "speed / quickness", "pos": "noun"},
                {"lemma": "imaginarse", "translation": "to imagine", "pos": "verb"},
                {"lemma": "darse cuenta de", "translation": "to realize", "pos": "verb"},
                {"lemma": "complicado", "translation": "complicated", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-04.ex01", "category": "grammar", "type": "multiple-choice", "question": "¡No te imaginas _____ cansada que estaba después de la carrera!", "options": ["lo", "la", "el", "qué"], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Es asombroso lo rápido _____ pasa el tiempo durante las vacaciones.", "answer": "que", "english": "It is astonishing how fast time flies during the holidays.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Mira", "lo", "bien", "que", "baila", "María", "."], "solution": ["Mira", "lo", "bien", "que", "baila", "María", "."], "english": "Look how well Maria dances.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "El detective resolvió el misterioso _____ en pocos días.", "options": ["enigma", "cansancio", "rapidez", "enfático"], "correct": 0, "teaches": ["b1-unit40-vocab"]},
                {"id": f"b1-{unit_num}-04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "No sabes lo _____ que fue subir hasta la cima de la montaña.", "answer": "difícil", "english": "You don't know how difficult it was to climb to the top of the mountain.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex06", "category": "grammar", "type": "matching", "pairs": [["Lo difícil que es", "How difficult it is"], ["Lo bien que tocas", "How well you play"], ["Lo rápido que corre", "How fast he runs"], ["Lo contenta que está", "How happy she is"]], "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex07", "category": "listening", "type": "listening-choice", "sentence": "Me impresionó muchísimo lo bien preparados que estaban todos los candidatos.", "options": ["Destaca la excelente preparación del grupo.", "Los candidatos no estaban preparados.", "La entrevista fue cancelada."], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex08", "category": "listening", "type": "dictation", "sentence": "No te imaginas lo difícil que fue conseguir las entradas.", "english": "You can't imagine how difficult it was to get the tickets.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Laura", "text": "¿Qué tal estuvo la prueba de acceso?"}, {"speaker": "Javier", "text": "____."}], "options": ["¡No sabes lo dura que fue la prueba física!", "No sabes la dura que fue.", "No sabes qué dura que fue."], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Madre", "text": "¿Cómo viste a los abuelos en el pueblo?"}, {"speaker": "Hijo", "text": "____."}], "options": ["¡Increíble lo contentos que se pusieron al vernos!", "Increíble los contentos que se pusieron.", "Increíble qué contentos que se pusieron."], "correct": 0, "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo: «No sabes lo bien que canta ella».", "answer": "No sabes lo bien que canta ella."}], "teaches": ["lo-neutro-abstraccion"]}
            ]
        },
        {
            "num": "05",
            "title": "Mastery of Prepositions, Nuanced Connectors and Lo",
            "goal": "Synthesize fixed prepositions, pero/sino, and the neuter article lo into cohesive advanced discourse.",
            "grammar_title": "Integrated Connectors and Prepositional Precision",
            "grammar_slug": "precision-conectores-sintesis",
            "grammar_text": "Fluency at the B1 threshold requires flawless handling of connecting tissue:\n\n• *No sueño con riquezas, sino que aspiro a vivir con tranquilidad.*\n• *Lo maravilloso de este viaje no fue el destino, sino la gente que conocimos en el camino.*\n• *Insistió en que contáramos con su ayuda, pero nos advirtió de lo complejo que sería el proceso.*",
            "table_rows": [
                ["Régimen preposicional", "soñar con / pensar en / contar con"],
                ["Oposición correctiva", "no X sino Y / no X sino que [verbo]"],
                ["Abstracción neutra", "lo importante / lo bueno / lo difícil"],
                ["Intensidad enfática", "lo bien que habla / lo difícil que fue"]
            ],
            "examples": [
                {"spanish": "Lo fascinante no fue el monumento, sino lo bien que el guía nos explicó su historia.", "english": "The fascinating thing wasn't the monument, but how well the guide explained its history."},
                {"spanish": "No dependemos de la suerte, sino que contamos con una planificación rigurosa.", "english": "We don't depend on luck, but rather count on rigorous planning."},
                {"spanish": "Pensaba en lo complicado que era, pero al final todo salió a la perfección.", "english": "I was thinking about how complicated it was, but in the end everything turned out to perfection."}
            ],
            "tip": "Combine structures smoothly: use *lo + adj* to set the topic and *sino que* to deliver the correction.",
            "vocab": [
                {"lemma": "fascinante", "translation": "fascinating", "pos": "adjective"},
                {"lemma": "riguroso", "translation": "rigorous", "pos": "adjective"},
                {"lemma": "planificación", "translation": "planning", "pos": "noun"},
                {"lemma": "perfección", "translation": "perfection", "pos": "noun"},
                {"lemma": "asociar", "translation": "to associate", "pos": "verb"},
                {"lemma": "cohesión", "translation": "cohesion", "pos": "noun"},
                {"lemma": "riqueza", "translation": "wealth / richness", "pos": "noun"},
                {"lemma": "aspirar a", "translation": "to aspire to", "pos": "verb"},
                {"lemma": "complejo", "translation": "complex", "pos": "adjective"},
                {"lemma": "fluido", "translation": "fluid", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"b1-{unit_num}-05.ex01", "category": "grammar", "type": "multiple-choice", "question": "No dependo de nadie, _____ que cuento con mi propio esfuerzo.", "options": ["sino", "pero", "sino que", "aunque"], "correct": 2, "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Siempre sueño _____ poder viajar por el espacio.", "answer": "con", "english": "I always dream of being able to travel through space.", "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Lo", "importante", "es", "aprender", "de", "los", "errores", "."], "solution": ["Lo", "importante", "es", "aprender", "de", "los", "errores", "."], "english": "The important thing is to learn from mistakes.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "La investigación requiere una metodología sumamente _____.", "options": ["rigurosa", "fascinante", "complejo", "fluido"], "correct": 0, "teaches": ["b1-unit40-vocab"]},
                {"id": f"b1-{unit_num}-05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Mira lo _____ que escribe ese autor consagrado.", "answer": "bien", "english": "Look how well that renowned author writes.", "teaches": ["lo-neutro-abstraccion"]},
                {"id": f"b1-{unit_num}-05.ex06", "category": "grammar", "type": "matching", "pairs": [["Contar con amigos", "To count on friends"], ["No té, sino café", "Sino (correction)"], ["Lo importante", "Abstract neuter"], ["Lo bien que canta", "Emphatic intensity"]], "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-05.ex07", "category": "listening", "type": "listening-choice", "sentence": "Lo asombroso de este proyecto no fue el presupuesto, sino lo rápido que se construyó.", "options": ["Destaca la velocidad de construcción por encima del presupuesto.", "Dice que el presupuesto fue muy alto.", "El proyecto tardó demasiado."], "correct": 0, "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-05.ex08", "category": "listening", "type": "dictation", "sentence": "No debemos pensar en el pasado, sino mirar hacia el futuro.", "english": "We must not think about the past, but rather look toward the future.", "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿Te molestó la crítica del profesor?"}, {"speaker": "Sara", "text": "____."}], "options": ["No me molestó la crítica, sino que me ayudó a mejorar.", "No me molestó la crítica pero que me ayudó.", "No me molestó la crítica sino me ayudó."], "correct": 0, "teaches": ["sino-vs-pero"]},
                {"id": f"b1-{unit_num}-05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Carlos", "text": "¿Con quién podemos organizar el evento de bienvenida?"}, {"speaker": "Elena", "text": "____."}], "options": ["Podemos contar con los nuevos voluntarios del equipo.", "Podemos contar de los voluntarios.", "Podemos soñar en los voluntarios."], "correct": 0, "teaches": ["verbos-regimen-preposicional-avanzado"]},
                {"id": f"b1-{unit_num}-05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo que lo importante es contar con buenos amigos.", "answer": "Lo importante es contar con buenos amigos."}], "teaches": ["verbos-regimen-preposicional-avanzado"]}
            ]
        }
    ]
    
    cons_title = "Consolidation: Advanced Connectors & Prepositions"
    cons_goal = "Demonstrate complete precision with fixed prepositional verbs, contrastive sino/pero, and neuter lo structures."
    cons_gr_text = "Mastering advanced connecting tissue in Spanish:\n• Régimen preposicional: soñar con, pensar en, contar con, depender de\n• Oposición correctiva: pero vs. sino (sustitución de palabras) vs. sino que (sustitución con verbo)\n• Lo neutro: abstracción (*lo bueno*) e intensidad enfática (*lo difícil que fue*)."
    cons_table_rows = [
        ["soñar con / pensar en", "Preposiciones fijas"],
        ["sino / sino que", "Corrección tras negación"],
        ["lo bueno / lo malo", "Cualidad abstracta"],
        ["lo bien que canta", "Grado enfático"]
    ]
    cons_examples = [
        {"spanish": "No quiero té, sino café con leche.", "english": "I don't want tea, but white coffee."},
        {"spanish": "Lo importante es que cuentes conmigo.", "english": "The important thing is that you count on me."}
    ]
    cons_tip = "Always check the verb after negation: if it's a conjugated verb, use *sino que*."
    
    cons_exs = [
        {"id": f"b1-{unit_num}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "No me quedé en la cama, _____ que salí a correr temprano.", "options": ["sino que", "pero", "sino", "aunque"], "correct": 0, "teaches": ["sino-vs-pero"]},
        {"id": f"b1-{unit_num}.cons.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Puedes contar _____ nosotros para lo que haga falta.", "answer": "con", "english": "You can count on us for whatever is needed.", "teaches": ["verbos-regimen-preposicional-avanzado"]},
        {"id": f"b1-{unit_num}.cons.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Lo", "mejor", "es", "descansar", "un", "poco", "."], "solution": ["Lo", "mejor", "es", "descansar", "un", "poco", "."], "english": "The best thing is to rest a little.", "teaches": ["lo-neutro-abstraccion"]},
        {"id": f"b1-{unit_num}.cons.ex04", "category": "grammar", "type": "matching", "pairs": [["Soñar con viajar", "Fixed preposition (con)"], ["No pan, sino arroz", "Sino (word correction)"], ["Lo importante", "Abstract neuter"], ["Lo rápido que corre", "Emphatic intensity"]], "teaches": ["verbos-regimen-preposicional-avanzado"]},
        {"id": f"b1-{unit_num}.cons.ex05", "category": "listening", "type": "listening-choice", "sentence": "No dependemos de las circunstancias externas, sino de nuestra capacidad de superación.", "options": ["Destaca la capacidad de superación personal.", "Culpa a las circunstancias.", "No quiere superarse."], "correct": 0, "teaches": ["sino-vs-pero"]},
        {"id": f"b1-{unit_num}.cons.ex06", "category": "listening", "type": "dictation", "sentence": "Lo difícil de esta lección es recordar todas las preposiciones.", "english": "The hard part of this lesson is remembering all the prepositions.", "teaches": ["lo-neutro-abstraccion"]},
        {"id": f"b1-{unit_num}.cons.ex07", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Lucas", "text": "¿En qué estás pensando?"}, {"speaker": "Beatriz", "text": "____."}], "options": ["Pienso en lo emocionante que será el viaje.", "Pienso de lo emocionante.", "Sueño de lo emocionante."], "correct": 0, "teaches": ["verbos-regimen-preposicional-avanzado"]},
        {"id": f"b1-{unit_num}.cons.ex08", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Escribe una frase diciendo: «Lo importante no es ganar, sino participar».", "answer": "Lo importante no es ganar, sino participar."}], "teaches": ["sino-vs-pero"]}
    ]
    
    generate_b1_unit(target_dir, unit_num, unit_title, lessons_data, cons_title, cons_goal, cons_gr_text, cons_table_rows, cons_examples, cons_tip, cons_exs)

def update_b1_curriculum(path, new_units):
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
    print(f"Updated {path}: added {added} B1 core units.")

if __name__ == "__main__":
    for target in [ES_ES, ES_LATAM]:
        print(f"Generating B1 Units 37-40 in {target}...")
        build_unit_37(target)
        build_unit_38(target)
        build_unit_39(target)
        build_unit_40(target)
        
    b1_units = [
        {
            "title": "The Past in the Mind: Present Perfect Subjunctive",
            "stems": [
                "b1-37-01",
                "b1-37-02",
                "b1-37-03",
                "b1-37-04",
                "b1-37-05",
                "b1-37-consolidation"
            ],
            "track": "core"
        },
        {
            "title": "Time & Perspective: Sequence of Tenses & Reported Speech",
            "stems": [
                "b1-38-01",
                "b1-38-02",
                "b1-38-03",
                "b1-38-04",
                "b1-38-05",
                "b1-38-consolidation"
            ],
            "track": "core"
        },
        {
            "title": "The Nuances of Change: Spanish Verbs of Becoming",
            "stems": [
                "b1-39-01",
                "b1-39-02",
                "b1-39-03",
                "b1-39-04",
                "b1-39-05",
                "b1-39-consolidation"
            ],
            "track": "core"
        },
        {
            "title": "Advanced Connectors & Prepositional Regimes",
            "stems": [
                "b1-40-01",
                "b1-40-02",
                "b1-40-03",
                "b1-40-04",
                "b1-40-05",
                "b1-40-consolidation"
            ],
            "track": "core"
        }
    ]
    
    update_b1_curriculum(ES_ES / "curriculum/units/b1.json", b1_units)
    update_b1_curriculum(ES_LATAM / "curriculum/units/b1.json", b1_units)
    print("Phase 11 (B1 Units 37–40) completed successfully!")
