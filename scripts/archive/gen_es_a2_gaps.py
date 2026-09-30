# -*- coding: utf-8 -*-
"""
Generate Phase 10: Spanish A2 Core Additions (Units 30–33)
Remediates critical CEFR gaps:
- Unit 30: Prepositions in Action: Por vs. Para (unit.a2.porpara)
- Unit 31: Indefinites & Double Negation: Alguien, Nadie, Algo, Nada (unit.a2.indefinidosnegacion)
- Unit 32: Life in Duration & Recent Actions: Verbal Periphrases (unit.a2.perifrasisduracion)
- Unit 33: Speaking to the Group: Vosotros in Spain (unit.a2.vosotrospeninsular) - Peninsular Spanish
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

# ==========================================
# UNIT 30: Por vs. Para (unit.a2.porpara)
# ==========================================
def build_unit_30(target_dir):
    stem_base = "a2-porpara"
    unit_id = "porpara"
    
    lessons_data = [
        {
            "num": "01",
            "title": "The Realm of Para: Purpose, Recipient & Destination",
            "goal": "Express the purpose of an action, the intended recipient of an object, and final destinations with para.",
            "grammar_title": "The Preposition Para: Purpose and Recipient",
            "grammar_slug": "para-destino",
            "grammar_text": "Use **para** when pointing toward an aim, a destination, or a recipient:\n\n1. **Purpose / Goal** (`para + infinitivo`): *Estudio español para viajar por el mundo.*\n2. **Recipient**: *Este libro es para Elena.*\n3. **Destination**: *Mañana salgo para Valencia.*",
            "table_rows": [
                ["para + infinitivo", "Estudio para aprobar el examen."],
                ["para + persona", "Compré un regalo para mi madre."],
                ["para + lugar", "El tren para Barcelona sale a las diez."]
            ],
            "examples": [
                {"spanish": "Trabajo duro para comprar una casa.", "english": "I work hard to buy a house."},
                {"spanish": "¿Tienes una carta para mí?", "english": "Do you have a letter for me?"},
                {"spanish": "Salimos para el aeropuerto ahora mismo.", "english": "We are leaving for the airport right now."}
            ],
            "tip": "Think of *para* as an arrow: it always aims forward at a goal, a recipient, or an end destination.",
            "vocab": [
                {"lemma": "meta", "translation": "goal / target", "pos": "noun"},
                {"lemma": "destino", "translation": "destination", "pos": "noun"},
                {"lemma": "destinatario", "translation": "recipient", "pos": "noun"},
                {"lemma": "regalo", "translation": "gift / present", "pos": "noun"},
                {"lemma": "objetivo", "translation": "objective", "pos": "noun"},
                {"lemma": "entregar", "translation": "to hand over / deliver", "pos": "verb"},
                {"lemma": "preparar", "translation": "to prepare", "pos": "verb"},
                {"lemma": "salir para", "translation": "to leave for", "pos": "expression"},
                {"lemma": "para siempre", "translation": "forever", "pos": "expression"},
                {"lemma": "útil", "translation": "useful", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.01.ex01", "category": "grammar", "type": "multiple-choice", "question": "Estudio todos los días _____ aprender español.", "options": ["para", "por", "de", "con"], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Este paquete urgente es _____ el director.", "answer": "para", "english": "This urgent parcel is for the director.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["El", "tren", "sale", "para", "Madrid", "."], "solution": ["El", "tren", "sale", "para", "Madrid", "."], "english": "The train leaves for Madrid.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "¿Quién es el _____ del paquete postal?", "options": ["destinatario", "objetivo", "regalo", "destino"], "correct": 0, "teaches": ["a2-unit30-vocab"]},
                {"id": f"a2.{unit_id}.01.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Ahorro dinero _____ viajar en verano.", "answer": "para", "english": "I save money to travel in summer.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex06", "category": "grammar", "type": "matching", "pairs": [["Para viajar", "To travel"], ["Para ti", "For you"], ["Para Madrid", "Bound for Madrid"], ["Para siempre", "Forever"]], "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex07", "category": "listening", "type": "listening-choice", "sentence": "Necesito una mesa para cuatro personas, por favor.", "options": ["Mesa para cuatro personas.", "Mesa para dos personas.", "Mesa para seis personas."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex08", "category": "listening", "type": "dictation", "sentence": "Este regalo es para mi hermano.", "english": "This gift is for my brother.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Meg", "text": "Carlos, ¿para qué compraste esa guía de viaje?"}, {"speaker": "Carlos", "text": "_____"}], "options": ["Para conocer mejor los museos de la ciudad.", "Por conocer los museos de la ciudad.", "De conocer los museos de la ciudad."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Recepcionista", "text": "¿Para quién es la reserva de la habitación?"}, {"speaker": "Carlos", "text": "_____"}], "options": ["Para Carlos Ruiz y su familia.", "Por Carlos Ruiz y su familia.", "De Carlos Ruiz y su familia."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.01.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Say: I study Spanish to speak with my friends.", "answer": "Estudio español para hablar con mis amigos."}, {"prompt": "Say: This present is for my mother.", "answer": "Este regalo es para mi madre."}], "teaches": ["por-vs-para"]}
            ],
            "check": ["I can use 'para' to express purpose and goals.", "I can use 'para' to indicate recipients and travel destinations."]
        },
        {
            "num": "02",
            "title": "The Realm of Por: Cause, Motive & Means",
            "goal": "Explain the reasons, causes, and means of transport or communication using por.",
            "grammar_title": "The Preposition Por: Reason and Means",
            "grammar_slug": "por-causa-medio",
            "grammar_text": "Use **por** when looking back at a cause, a reason, or the vehicle/medium through which something happens:\n\n1. **Cause / Reason**: *El vuelo se retrasó por la tormenta.*\n2. **Means / Channel**: *Te envié el documento por correo electrónico.*\n3. **Motive / On behalf of**: *Hizo todo eso por su familia.*",
            "table_rows": [
                ["por + sustantivo (causa)", "Llegamos tarde por el tráfico."],
                ["por teléfono / internet", "Hablamos por teléfono ayer."],
                ["por casualidad / por ejemplo", "Nos vimos por casualidad en el metro."]
            ],
            "examples": [
                {"spanish": "No pudimos salir por la lluvia intensa.", "english": "We could not go out because of the heavy rain."},
                {"spanish": "Prefiero comunicarme por mensaje.", "english": "I prefer to communicate by text message."},
                {"spanish": "Gracias por tu gran ayuda.", "english": "Thank you for your great help."}
            ],
            "tip": "Think of *por* as looking backward at the source: 'because of', 'through', or 'by means of'.",
            "vocab": [
                {"lemma": "motivo", "translation": "motive / reason", "pos": "noun"},
                {"lemma": "culpa", "translation": "fault / blame", "pos": "noun"},
                {"lemma": "teléfono", "translation": "telephone", "pos": "noun"},
                {"lemma": "correo", "translation": "mail / email", "pos": "noun"},
                {"lemma": "internet", "translation": "internet", "pos": "noun"},
                {"lemma": "tráfico", "translation": "traffic", "pos": "noun"},
                {"lemma": "lluvia", "translation": "rain", "pos": "noun"},
                {"lemma": "por casualidad", "translation": "by chance", "pos": "expression"},
                {"lemma": "por ejemplo", "translation": "for example", "pos": "expression"},
                {"lemma": "enviar por", "translation": "to send by", "pos": "expression"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.02.ex01", "category": "grammar", "type": "multiple-choice", "question": "Llegamos tarde _____ culpa del tráfico.", "options": ["por", "para", "a", "en"], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Te envié los billetes _____ correo electrónico.", "answer": "por", "english": "I sent you the tickets by email.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Hablamos", "por", "teléfono", "anoche", "."], "solution": ["Hablamos", "por", "teléfono", "anoche", "."], "english": "We spoke on the phone last night.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "No pudimos aterrizar por culpa del mal _____.", "options": ["tráfico", "motivo", "correo", "teléfono"], "correct": 0, "teaches": ["a2-unit30-vocab"]},
                {"id": f"a2.{unit_id}.02.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Muchas gracias _____ tu amable invitación.", "answer": "por", "english": "Thank you very much for your kind invitation.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex06", "category": "grammar", "type": "matching", "pairs": [["Por la lluvia", "Because of the rain"], ["Por avión", "By plane"], ["Por teléfono", "By phone"], ["Por casualidad", "By chance"]], "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex07", "category": "listening", "type": "listening-choice", "sentence": "El tren se detuvo por una avería en la vía.", "options": ["Por una avería en la vía.", "Por el mal tiempo en la vía.", "Por una huelga de trenes."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex08", "category": "listening", "type": "dictation", "sentence": "Lo encontré por casualidad en el centro.", "english": "I found it by chance in the city centre.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Carlos", "text": "¿Por qué no viniste a clase ayer por la tarde?"}, {"speaker": "Meg", "text": "_____"}], "options": ["Por un fuerte dolor de cabeza.", "Para un fuerte dolor de cabeza.", "Con un fuerte dolor de cabeza."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Meg", "text": "¿Cómo compraste las entradas para el concierto?"}, {"speaker": "Carlos", "text": "_____"}], "options": ["Las compré por internet hace dos días.", "Las compré para internet hace dos días.", "Las compré a internet hace dos días."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.02.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Say: I didn't go out because of the rain.", "answer": "No salí por la lluvia."}, {"prompt": "Say: I spoke with Carlos by phone.", "answer": "Hablé con Carlos por teléfono."}], "teaches": ["por-vs-para"]}
            ],
            "check": ["I can use 'por' to give reasons and causes.", "I can use 'por' to describe means of transport and communication."]
        },
        {
            "num": "03",
            "title": "Time and Space: Deadlines vs. Duration and Path",
            "goal": "Contrast time deadlines (para) with duration (por), and spatial destination (para) with movement through space (por).",
            "grammar_title": "Por and Para in Time and Space",
            "grammar_slug": "por-para-tiempo-espacio",
            "grammar_text": "Time and space highlight the classic contrast between **por** and **para**:\n\n1. **Time Deadline** (*para*): *El informe es para el lunes.* (Due by Monday)\n2. **Time Duration** (*por*): *Estudié por tres horas.* (Duration of 3 hours)\n3. **Time of day** (*por*): *por la mañana, por la tarde, por la noche*\n4. **Motion through a place** (*por*): *Caminamos por el parque.* (Through / around the park)\n5. **Motion toward a place** (*para*): *Vamos para casa.* (Heading home)",
            "table_rows": [
                ["para el lunes / mañana", "La tarea es para mañana."],
                ["por dos horas / días", "Esperamos por dos horas en la estación."],
                ["por la mañana / tarde", "Hago ejercicio por la mañana."],
                ["por la calle / el parque", "Paseamos por el centro histórico."]
            ],
            "examples": [
                {"spanish": "Necesito el coche listo para el viernes.", "english": "I need the car ready by Friday."},
                {"spanish": "Vivieron en Valencia por un año.", "english": "They lived in Valencia for a year."},
                {"spanish": "El gato escapó por la ventana.", "english": "The cat escaped through the window."}
            ],
            "tip": "*Para* sets a cutoff point or final stop; *por* covers the duration elapsed or the area traveled through.",
            "vocab": [
                {"lemma": "plazo", "translation": "deadline / term", "pos": "noun"},
                {"lemma": "parque", "translation": "park", "pos": "noun"},
                {"lemma": "calle", "translation": "street", "pos": "noun"},
                {"lemma": "centro", "translation": "downtown / center", "pos": "noun"},
                {"lemma": "pasear", "translation": "to stroll / walk", "pos": "verb"},
                {"lemma": "caminar", "translation": "to walk", "pos": "verb"},
                {"lemma": "ventana", "translation": "window", "pos": "noun"},
                {"lemma": "para el lunes", "translation": "by Monday", "pos": "expression"},
                {"lemma": "por la tarde", "translation": "in the afternoon", "pos": "expression"},
                {"lemma": "a tiempo", "translation": "on time", "pos": "expression"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.03.ex01", "category": "grammar", "type": "multiple-choice", "question": "Debemos entregar el trabajo _____ el viernes por la mañana.", "options": ["para", "por", "de", "en"], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Ayer dimos un paseo _____ el parque del Retiro.", "answer": "por", "english": "Yesterday we took a walk through the Retiro park.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["El", "tren", "va", "para", "Sevilla", "."], "solution": ["El", "tren", "va", "para", "Sevilla", "."], "english": "The train is heading toward Seville.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "El _____ de entrega del proyecto termina el jueves.", "options": ["plazo", "parque", "centro", "pasear"], "correct": 0, "teaches": ["a2-unit30-vocab"]},
                {"id": f"a2.{unit_id}.03.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Estudiamos en la biblioteca _____ tres horas seguidas.", "answer": "por", "english": "We studied in the library for three hours straight.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex06", "category": "grammar", "type": "matching", "pairs": [["Para mañana", "By tomorrow"], ["Por la noche", "At night"], ["Por el centro", "Around downtown"], ["Por la tarde", "In the afternoon"]], "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex07", "category": "listening", "type": "listening-choice", "sentence": "Salimos a correr por la playa todos los días.", "options": ["Correr por la playa.", "Correr para la playa.", "Correr en la pista."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex08", "category": "listening", "type": "dictation", "sentence": "La reserva es para el próximo sábado.", "english": "The reservation is for next Saturday.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Profesor", "text": "¿Para cuándo es el ensayo de literatura?"}, {"speaker": "Carlos", "text": "_____"}], "options": ["Es para el próximo martes.", "Es por el próximo martes.", "Es en el próximo martes."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Turista", "text": "¿Por dónde se va a la Plaza Mayor?"}, {"speaker": "Guía", "text": "_____"}], "options": ["Siga recto por esta calle comercial.", "Vaya para esta calle comercial.", "Doble de esta calle comercial."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.03.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Say: I must finish the report by tomorrow.", "answer": "Debo terminar el informe para mañana."}, {"prompt": "Say: We walked through the city center.", "answer": "Caminamos por el centro de la ciudad."}], "teaches": ["por-vs-para"]}
            ],
            "check": ["I can use 'para' for deadlines and cut-off dates.", "I can use 'por' for duration and movement through spaces."]
        },
        {
            "num": "04",
            "title": "Exchanges, Prices & Gratitude",
            "goal": "Use por for financial exchanges, prices, bartering, and saying thanks.",
            "grammar_title": "Por for Exchanges, Prices and Thanks",
            "grammar_slug": "por-intercambio-precio",
            "grammar_text": "Whenever one thing replaces or buys another, Spanish uses **por**:\n\n1. **Financial Exchange / Cost**: *Compré este libro por quince euros.*\n2. **Substitution / In place of**: *Trabajo hoy por mi compañero enfermo.*\n3. **Expressions of Gratitude**: *Muchas gracias por todo.* / *Disculpa por la molestia.*\n4. Contrast with beneficiary (*para*): *Compré el libro por 15 € (precio) para mi hermana (destinataria).* ",
            "table_rows": [
                ["pagar / comprar por X euros", "Lo compré por diez euros."],
                ["gracias por + sust./inf.", "Gracias por venir a verme."],
                ["cambiar A por B", "Cambié la camisa por otra talla."]
            ],
            "examples": [
                {"spanish": "Te doy mi postre por tu manzana.", "english": "I'll give you my dessert for your apple."},
                {"spanish": "Pagué treinta euros por la cena.", "english": "I paid thirty euros for the dinner."},
                {"spanish": "Gracias por invitarme a tu casa.", "english": "Thank you for inviting me to your home."}
            ],
            "tip": "If money, items, or favors are swapped, *por* mediates the exchange.",
            "vocab": [
                {"lemma": "precio", "translation": "price", "pos": "noun"},
                {"lemma": "cambiar", "translation": "to change / exchange", "pos": "verb"},
                {"lemma": "pagar", "translation": "to pay", "pos": "verb"},
                {"lemma": "costar", "translation": "to cost", "pos": "verb"},
                {"lemma": "propina", "translation": "tip / gratuity", "pos": "noun"},
                {"lemma": "ayuda", "translation": "help", "pos": "noun"},
                {"lemma": "favor", "translation": "favor", "pos": "noun"},
                {"lemma": "gracias por", "translation": "thanks for", "pos": "expression"},
                {"lemma": "a cambio de", "translation": "in exchange for", "pos": "expression"},
                {"lemma": "barato", "translation": "cheap", "pos": "adjective"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.04.ex01", "category": "grammar", "type": "multiple-choice", "question": "Compré esta chaqueta de cuero _____ cincuenta euros en las rebajas.", "options": ["por", "para", "de", "con"], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Muchísimas gracias _____ ayudarme con las maletas.", "answer": "por", "english": "Thank you very much for helping me with the suitcases.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Cambié", "el", "billete", "por", "otro", "."], "solution": ["Cambié", "el", "billete", "por", "otro", "."], "english": "I exchanged the ticket for another one.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "El camarero fue muy amable y dejamos una buena _____.", "options": ["propina", "ayuda", "precio", "favor"], "correct": 0, "teaches": ["a2-unit30-vocab"]},
                {"id": f"a2.{unit_id}.04.ex05", "category": "grammar", "type": "fill-blank", "sentence": "Compré estas flores _____ el cumpleaños de mi madre.", "answer": "para", "english": "I bought these flowers for my mother's birthday.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex06", "category": "grammar", "type": "matching", "pairs": [["Por veinte euros", "For twenty euros"], ["Gracias por llamar", "Thanks for calling"], ["Para mi amigo", "For my friend"], ["Cambiar por", "To exchange for"]], "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex07", "category": "listening", "type": "listening-choice", "sentence": "¿Me puedes cambiar este billete de cincuenta por dos de veinte y uno de diez?", "options": ["Cambiar un billete de cincuenta.", "Pagar cincuenta euros.", "Comprar un billete de diez."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex08", "category": "listening", "type": "dictation", "sentence": "Perdona por llegar tarde a la cita.", "english": "Sorry for arriving late to the appointment.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Cliente", "text": "¿Cuánto pagaste por esa bicicleta de segunda mano?"}, {"speaker": "Vendedor", "text": "_____"}], "options": ["Pagué solo cien euros por ella.", "Pagué para cien euros por ella.", "Pagué de cien euros por ella."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Amiga", "text": "¡Qué tarta más rica trajiste a la fiesta!"}, {"speaker": "Meg", "text": "_____"}], "options": ["Gracias por invitarme a merendar.", "Gracias para invitarme a merendar.", "Gracias a invitarme a merendar."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.04.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Say: I paid twenty euros for the dinner.", "answer": "Pagué veinte euros por la cena."}, {"prompt": "Say: Thanks for the gift.", "answer": "Gracias por el regalo."}], "teaches": ["por-vs-para"]}
            ],
            "check": ["I can use 'por' for prices, sales, and exchanges.", "I can use 'por' when thanking or apologizing to someone."]
        },
        {
            "num": "05",
            "title": "Por vs. Para in Context: Travel and Decisions",
            "goal": "Integrate por and para seamlessly in travel planning, personal decisions, and narrative storytelling.",
            "grammar_title": "Comprehensive Por vs. Para Mastery",
            "grammar_slug": "por-vs-para-integrado",
            "grammar_text": "Putting the complete system together:\n\n• **PARA**: Objective, Recipient, Deadline, Destination, Opinion (*para mí*).\n• **POR**: Cause, Means, Time of day, Duration, Path through space, Price, Exchange, Gratitude.\n\nCompare: *Salgo para Madrid (destino) por la mañana (tiempo) por tren (medio) para ver a mi tía (propósito).*",
            "table_rows": [
                ["destino vs. trayecto", "Voy para Valencia / Camino por la playa."],
                ["plazo vs. duración", "Es para el martes / Me quedé por dos días."],
                ["destinatario vs. causa", "Es para ti / Lo hice por ti (por tu bien)."]
            ],
            "examples": [
                {"spanish": "Para mí, viajar en tren es la mejor opción.", "english": "In my opinion, traveling by train is the best option."},
                {"spanish": "Caminamos por la Gran Vía para llegar al teatro.", "english": "We walked along Gran Vía to get to the theater."},
                {"spanish": "Tengo que preparar la maleta para salir temprano.", "english": "I have to pack my suitcase to leave early."}
            ],
            "tip": "Memorize the sentence: *Viajo para aprender, pago por viajar y camino por la ciudad.*",
            "vocab": [
                {"lemma": "decisión", "translation": "decision", "pos": "noun"},
                {"lemma": "viaje", "translation": "trip / journey", "pos": "noun"},
                {"lemma": "maleta", "translation": "suitcase", "pos": "noun"},
                {"lemma": "camino", "translation": "path / way", "pos": "noun"},
                {"lemma": "estación", "translation": "station", "pos": "noun"},
                {"lemma": "prisa", "translation": "hurry / rush", "pos": "noun"},
                {"lemma": "horario", "translation": "timetable / schedule", "pos": "noun"},
                {"lemma": "para mí", "translation": "in my opinion / for me", "pos": "expression"},
                {"lemma": "tener prisa", "translation": "to be in a hurry", "pos": "expression"},
                {"lemma": "de camino", "translation": "on the way", "pos": "expression"}
            ],
            "exs": [
                {"id": f"a2.{unit_id}.05.ex01", "category": "grammar", "type": "multiple-choice", "question": "_____ mí, la paella valenciana es el mejor plato español.", "options": ["Para", "Por", "De", "A"], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex02", "category": "grammar", "type": "fill-blank", "sentence": "Fuimos a la estación _____ comprar los billetes para Sevilla.", "answer": "para", "english": "We went to the station to buy the tickets for Seville.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex03", "category": "grammar", "type": "sentence-builder", "tiles": ["Paseamos", "por", "el", "barrio", "antiguo", "."], "solution": ["Paseamos", "por", "el", "barrio", "antiguo", "."], "english": "We strolled through the old quarter.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex04", "category": "vocabulary", "type": "multiple-choice", "question": "No puedo hablar ahora porque tengo mucha _____.", "options": ["prisa", "maleta", "decisión", "estación"], "correct": 0, "teaches": ["a2-unit30-vocab"]},
                {"id": f"a2.{unit_id}.05.ex05", "category": "grammar", "type": "fill-blank", "sentence": "El autobús no pudo pasar _____ las obras en la avenida.", "answer": "por", "english": "The bus could not pass because of roadworks on the avenue.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex06", "category": "grammar", "type": "matching", "pairs": [["Para mí", "In my opinion"], ["Por la tarde", "In the afternoon"], ["Para viajar", "In order to travel"], ["Por el centro", "Through downtown"]], "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex07", "category": "listening", "type": "listening-choice", "sentence": "Reservé una mesa para dos personas por teléfono.", "options": ["Mesa para dos por teléfono.", "Mesa para cuatro por teléfono.", "Mesa para dos en el restaurante."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex08", "category": "listening", "type": "dictation", "sentence": "Salimos temprano para evitar el tráfico.", "english": "We left early in order to avoid the traffic.", "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex09", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Guía", "text": "¿Tienen alguna pregunta sobre la ruta del viaje?"}, {"speaker": "Meg", "text": "_____"}], "options": ["¿Cuánto tiempo caminaremos por la montaña?", "¿Para cuándo caminaremos por la montaña?", "¿Por dónde salimos para la montaña?"], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex10", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Carlos", "text": "Meg, ¿está lista tu maleta para el viaje?"}, {"speaker": "Meg", "text": "_____"}], "options": ["Sí, ya tengo todo preparado para mañana.", "Sí, tengo todo preparado por mañana.", "Sí, tengo todo preparado a mañana."], "correct": 0, "teaches": ["por-vs-para"]},
                {"id": f"a2.{unit_id}.05.ex11", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Say: In my opinion, Spain is ideal for traveling.", "answer": "Para mí, España es un país ideal para viajar."}, {"prompt": "Say: We walked through the old town in the afternoon.", "answer": "Paseamos por el casco antiguo por la tarde."}], "teaches": ["por-vs-para"]}
            ],
            "check": ["I can contrast 'por' and 'para' confidently in full sentences.", "I can express personal opinions using 'para mí'."]
        }
    ]
    
    cons_exs = [
        {"id": f"a2.{unit_id}.cons.ex01", "category": "grammar", "type": "multiple-choice", "question": "Estudio español _____ encontrar un buen trabajo.", "options": ["para", "por", "de", "en"], "correct": 0, "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex02", "category": "grammar", "type": "multiple-choice", "question": "No fuimos al concierto _____ culpa de la lluvia.", "options": ["por", "para", "a", "con"], "correct": 0, "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex03", "category": "grammar", "type": "fill-blank", "sentence": "Este paquete es _____ mi abuela.", "answer": "para", "english": "This parcel is for my grandmother.", "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex04", "category": "grammar", "type": "fill-blank", "sentence": "Pagamos quince euros _____ el menú del día.", "answer": "por", "english": "We paid fifteen euros for the set menu.", "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex05", "category": "grammar", "type": "sentence-builder", "tiles": ["Caminamos", "por", "el", "parque", "."], "solution": ["Caminamos", "por", "el", "parque", "."], "english": "We walked through the park.", "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex06", "category": "grammar", "type": "fill-blank", "sentence": "La tarea es _____ el próximo lunes.", "answer": "para", "english": "The homework is for next Monday.", "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex07", "category": "grammar", "type": "multiple-choice", "question": "Te envié las fotos _____ correo electrónico.", "options": ["por", "para", "en", "con"], "correct": 0, "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex08", "category": "grammar", "type": "fill-blank", "sentence": "Muchas gracias _____ tu gran ayuda.", "answer": "por", "english": "Thank you very much for your great help.", "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex09", "category": "vocabulary", "type": "matching", "pairs": [["Para mí", "In my opinion"], ["Por la mañana", "In the morning"], ["Por casualidad", "By chance"], ["Para siempre", "Forever"]], "teaches": ["a2-unit30-vocab"]},
        {"id": f"a2.{unit_id}.cons.ex10", "category": "listening", "type": "listening-choice", "sentence": "El tren para Barcelona sale por la vía tres.", "options": ["Sale hacia Barcelona por la vía 3.", "Llega de Barcelona a la vía 3.", "Sale para Sevilla por la vía 2."], "correct": 0, "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex11", "category": "listening", "type": "dictation", "sentence": "Lo compramos por internet para ahorrar dinero.", "english": "We bought it online in order to save money.", "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex12", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Elena", "text": "¿Para cuándo necesitas el informe completo?"}, {"speaker": "Carlos", "text": "_____"}], "options": ["Lo necesito para mañana por la tarde.", "Lo necesito por mañana por la tarde.", "Lo necesito de mañana por la tarde."], "correct": 0, "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex13", "category": "dialogue", "type": "dialogue-complete", "prompt": [{"speaker": "Pablo", "text": "¿Por qué decidiste estudiar español?"}, {"speaker": "Meg", "text": "_____"}], "options": ["Para poder trabajar en España en el futuro.", "Por poder trabajar en España en el futuro.", "De poder trabajar en España en el futuro."], "correct": 0, "teaches": ["por-vs-para"]},
        {"id": f"a2.{unit_id}.cons.ex14", "category": "writing", "type": "structured-writing", "template": [{"prompt": "Say: I am leaving for Seville in the morning.", "answer": "Salgo para Sevilla por la mañana."}, {"prompt": "Say: We traveled by train through Andalusia.", "answer": "Viajamos por tren por Andalucía."}], "teaches": ["por-vs-para"]}
    ]
    
    for ld in lessons_data:
        stem = f"{stem_base}-{ld['num']}"
        les_id = f"lesson.a2.{unit_id}.{ld['num']}"
        ex_refs = [ex['id'] for ex in ld['exs']]
        
        les_obj = make_lesson(les_id, ld['title'], ld['goal'], "por vs para", stem, f"vocabulary/a2/{stem}-voc.json", ex_refs, ld['check'])
        write_json(target_dir / f"lessons/a2/{stem}.json", les_obj)
        
        gr_obj = {
            "id": f"grammar.a2.{unit_id}.{ld['num']}.{ld['grammar_slug']}",
            "title": ld['grammar_title'],
            "sections": [
                {"type": "text", "content": ld['grammar_text']},
                {"type": "table", "title": "Key Patterns", "rows": ld['table_rows']},
                {"type": "examples", "items": ld['examples']},
                {"type": "tip", "content": ld['tip']}
            ]
        }
        write_json(target_dir / f"grammar/a2/{stem}-gr.json", gr_obj)
        
        voc_obj = {
            "id": f"vocab.a2.{unit_id}.{ld['num']}",
            "lesson": stem,
            "title": f"Vocabulary: {ld['title']}",
            "theme": "prepositions and travel",
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
    cons_refs = [ex['id'] for ex in cons_exs]
    cons_les_obj = make_lesson(cons_les_id, "Consolidation: Por vs. Para", "Consolidate your mastery of por and para across all core contexts.", "por vs para consolidación", cons_stem, None, cons_refs, ["I can confidently distinguish between por and para in everyday speech and writing."])
    write_json(target_dir / f"lessons/a2/{cons_stem}.json", cons_les_obj)
    
    cons_gr_obj = {
        "id": f"grammar.a2.{unit_id}.consolidation.resumen",
        "title": "Summary of Por vs. Para",
        "sections": [
            {"type": "text", "content": "Mastering **por** and **para** comes down to direction of attention:\n\n• **PARA** points forward: purpose (*para aprender*), destination (*para Madrid*), recipient (*para ti*), deadline (*para el viernes*), and personal evaluation (*para mí*).\n\n• **POR** looks back or surrounds: cause/motive (*por la lluvia*), means/transport (*por tren*), time of day (*por la tarde*), duration (*por tres horas*), path (*por la calle*), exchange/cost (*por diez euros*), and gratitude (*gracias por*)."},
            {"type": "table", "title": "Complete Quick Reference", "rows": [
                ["Finalidad / Destino", "Estudio para aprender / Salgo para Sevilla"],
                ["Causa / Medio", "No salí por la lluvia / Te llamo por teléfono"],
                ["Plazo vs. Duración", "Para el lunes / Por dos semanas"],
                ["Precio / Intercambio", "Lo compré por 20 € / Gracias por todo"]
            ]},
            {"type": "examples", "items": [
                {"spanish": "Para mí, caminar por el centro es un placer.", "english": "For me, walking around downtown is a pleasure."},
                {"spanish": "Compré flores por cinco euros para mi amiga.", "english": "I bought flowers for five euros for my friend."}
            ]},
            {"type": "tip", "content": "When in doubt, ask yourself: Is it an objective/deadline (para) or a reason/path (por)?"}
        ]
    }
    write_json(target_dir / f"grammar/a2/{cons_stem}-gr.json", cons_gr_obj)
    write_json(target_dir / f"exercises/a2/{cons_stem}-ex.json", {"lesson": cons_stem, "exercises": cons_exs})
    
    story_paras = [
        "Meg y Carlos reciben una llamada urgente de su amiga Elena desde la oficina central en Madrid.",
        "«Necesito un favor enorme», dice Elena con tono de prisa. «Tengo un paquete de documentos para el notario que debe entregarse hoy antes de las cinco de la tarde».",
        "«No te preocupes, Elena», responde Carlos sonriendo. «Nosotros nos encargamos de llevarlo para que llegues a tiempo a tu reunión».",
        "Salen rápidamente del apartamento y caminan por las concurridas calles de Malasaña hacia la Gran Vía.",
        "Por el camino, cruzan por la Plaza de España y toman el metro para evitar el tráfico de la tarde.",
        "Llegan al despacho del notario a las cuatro y media. «¡Llegamos a tiempo!», exclama Meg aliviada al entregar el paquete para el abogado.",
        "Más tarde, Elena les escribe un mensaje lleno de agradecimiento: «¡Muchísimas gracias por vuestra ayuda! La próxima cena corre por mi cuenta»."
    ]
    story_obj = make_story(f"a2-original-{unit_id}", "El encargo urgente en Madrid", "Meg y Carlos deben entregar un paquete urgente por el centro de Madrid antes de las cinco de la tarde.", "Madrid", ["por vs para", "preposiciones"], ["tráfico", "viaje", "ciudad"], story_paras, 30)
    write_json(target_dir / f"stories/original/a2/a2-{unit_id}.json", story_obj)
    print(f"Unit 30 ({unit_id}) generated successfully in {target_dir}")

build_unit_30(ES_ES)
build_unit_30(ES_LATAM)
