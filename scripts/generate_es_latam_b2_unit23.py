"""Generate Latin American Spanish (es-latam) B2 Unit 23:
Core Unit 23: b2-23 (Inceptive & Iterative Periphrases)
Regional Unit 23: b2-chileextremos (Chile II: The Extreme Geographies: Atacama, Patagonia & Mapuche Wallmapu)
Classic Literature: Francisco Coloane - Cabo de Hornos (1941)
"""

import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATAM_DIR = os.path.join(BASE_DIR, "content", "es-latam")

def count_words(story_obj):
    paras = story_obj.get("narration", {}).get("paragraphs", [])
    text = " ".join(p if isinstance(p, str) else p.get("text", "") for p in paras)
    words = re.findall(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b", text)
    return len(words)

def update_json_file(filepath, updater_fn):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    data = updater_fn(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def write_json(rel_path, data):
    full_path = os.path.join(LATAM_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {os.path.relpath(full_path, BASE_DIR)}")

def main():
    # 1. Update skill-registry.json
    def update_skill_registry(registry):
        skills = registry.setdefault("skills", {})
        new_skills = {
            "perifrasis-echarse-a": {
                "kind": "grammar",
                "name": "perifrasis-echarse-a",
                "description": "Inceptive periphrasis echarse a + infinitivo for sudden emotional or physical actions",
                "aliases": []
            },
            "perifrasis-ponerse-a": {
                "kind": "grammar",
                "name": "perifrasis-ponerse-a",
                "description": "Inceptive periphrasis ponerse a + infinitivo for deliberate initiation of activities",
                "aliases": []
            },
            "perifrasis-romper-a": {
                "kind": "grammar",
                "name": "perifrasis-romper-a",
                "description": "Inceptive periphrasis romper a + infinitivo for sudden, explosive breakthroughs and outbursts",
                "aliases": []
            },
            "perifrasis-volver-a": {
                "kind": "grammar",
                "name": "perifrasis-volver-a",
                "description": "Iterative periphrasis volver a + infinitivo for repetition and resumption of processes",
                "aliases": []
            },
            "perifrasis-pasar-a": {
                "kind": "grammar",
                "name": "perifrasis-pasar-a",
                "description": "Aspectual periphrasis pasar a + infinitivo for sequential progression and agenda shifts",
                "aliases": []
            },
            "b2-unit23-vocab": {
                "kind": "vocabulary",
                "name": "b2-unit23-vocab",
                "description": "Vocabulary for inceptive and iterative actions, effort, and transitions",
                "aliases": []
            },
            "chile-atacama-astronomia": {
                "kind": "grammar",
                "name": "chile-atacama-astronomia",
                "description": "Descriptive discourse on desert astronomy and clean atmospheres",
                "aliases": []
            },
            "chile-mineria-cobre": {
                "kind": "grammar",
                "name": "chile-mineria-cobre",
                "description": "Technical discourse on open pit mining and extraction",
                "aliases": []
            },
            "chile-wallmapu-mapuche": {
                "kind": "grammar",
                "name": "chile-wallmapu-mapuche",
                "description": "Historical discourse on indigenous autonomy and cultural defense",
                "aliases": []
            },
            "chile-patagonia-glaciares": {
                "kind": "grammar",
                "name": "chile-patagonia-glaciares",
                "description": "Environmental discourse on subpolar fjords and glacial geology",
                "aliases": []
            },
            "chile-energia-austral": {
                "kind": "grammar",
                "name": "chile-energia-austral",
                "description": "Scientific discourse on green hydrogen and energy transitions",
                "aliases": []
            },
            "b2-chileextremos-vocab": {
                "kind": "vocabulary",
                "name": "b2-chileextremos-vocab",
                "description": "Vocabulary for Chilean extreme geographies, mining, cosmology, and subpolar ecology",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            if k not in skills:
                skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 23")

    # 2. Update grammar-titles.json (all lowercase words, <= 11 words, plain CEFR English)
    def update_grammar_titles(titles):
        new_titles = {
            "perifrasis-echarse-a": "inceptive periphrases with echarse a and sudden actions",
            "perifrasis-ponerse-a": "inceptive periphrases with ponerse a and deliberate actions",
            "perifrasis-romper-a": "inceptive periphrases with romper a and sudden outbursts",
            "perifrasis-volver-a": "iterative periphrases with volver a and repeated actions",
            "perifrasis-pasar-a": "transition periphrases with pasar a and sequential shifts",
            "chile-atacama-astronomia": "descriptive discourse on desert astronomy and clean atmospheres",
            "chile-mineria-cobre": "technical discourse on open pit mining and extraction",
            "chile-wallmapu-mapuche": "historical discourse on indigenous autonomy and cultural defense",
            "chile-patagonia-glaciares": "environmental discourse on subpolar fjords and glacial geology",
            "chile-energia-austral": "scientific discourse on green hydrogen and energy transitions"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 23")

    # 3. Vocabulary Files (10 files)
    vocab_data = {
        "b2-23-01": {
            "id": "vocab.b2.23.01",
            "lesson": "b2-23-01",
            "title": "Inceptive Periphrasis: Echarse a",
            "words": [
                {"lemma": "echarse a", "translation": "to burst into / to suddenly begin doing", "pos": "verb"},
                {"lemma": "súbito", "translation": "sudden / unexpected", "pos": "adjective"},
                {"lemma": "llanto", "translation": "weeping / crying", "pos": "noun"},
                {"lemma": "carcajada", "translation": "loud laugh / guffaw", "pos": "noun"},
                {"lemma": "temblor", "translation": "tremor / trembling", "pos": "noun"},
                {"lemma": "pánico", "translation": "panic", "pos": "noun"},
                {"lemma": "estampida", "translation": "stampede / sudden rush", "pos": "noun"},
                {"lemma": "arrebato", "translation": "outburst / fit of emotion", "pos": "noun"},
                {"lemma": "huida", "translation": "flight / escape", "pos": "noun"},
                {"lemma": "desbandada", "translation": "scatter / disorderly dispersion", "pos": "noun"}
            ]
        },
        "b2-23-02": {
            "id": "vocab.b2.23.02",
            "lesson": "b2-23-02",
            "title": "Inceptive Periphrasis: Ponerse a",
            "words": [
                {"lemma": "ponerse a", "translation": "to set about / to start doing deliberately", "pos": "verb"},
                {"lemma": "diligencia", "translation": "diligence / prompt dispatch", "pos": "noun"},
                {"lemma": "tesón", "translation": "tenacity / perseverance", "pos": "noun"},
                {"lemma": "deliberado", "translation": "deliberate / intentional", "pos": "adjective"},
                {"lemma": "emprender", "translation": "to undertake / to embark upon", "pos": "verb"},
                {"lemma": "redacción", "translation": "drafting / composition", "pos": "noun"},
                {"lemma": "faena", "translation": "toil / chore / labor task", "pos": "noun"},
                {"lemma": "esmero", "translation": "meticulous care / dedication", "pos": "noun"},
                {"lemma": "tarea", "translation": "task / undertaking", "pos": "noun"},
                {"lemma": "afán", "translation": "eagerness / earnest endeavor", "pos": "noun"}
            ]
        },
        "b2-23-03": {
            "id": "vocab.b2.23.03",
            "lesson": "b2-23-03",
            "title": "Inceptive Periphrasis: Romper a",
            "words": [
                {"lemma": "romper a", "translation": "to break into / to burst out doing", "pos": "verb"},
                {"lemma": "estallido", "translation": "outbreak / explosion / burst", "pos": "noun"},
                {"lemma": "brote", "translation": "outbreak / sprout / emergence", "pos": "noun"},
                {"lemma": "fragor", "translation": "clamor / din / roaring noise", "pos": "noun"},
                {"lemma": "clamor", "translation": "clamor / loud outcry", "pos": "noun"},
                {"lemma": "júbilo", "translation": "exultant joy / jubilation", "pos": "noun"},
                {"lemma": "aguacero", "translation": "downpour / sudden heavy rain", "pos": "noun"},
                {"lemma": "llamarada", "translation": "sudden blaze / flare-up", "pos": "noun"},
                {"lemma": "eclosión", "translation": "flowering / blossoming / emergence", "pos": "noun"},
                {"lemma": "trueno", "translation": "thunderclap / peal of thunder", "pos": "noun"}
            ]
        },
        "b2-23-04": {
            "id": "vocab.b2.23.04",
            "lesson": "b2-23-04",
            "title": "Iterative Periphrasis: Volver a",
            "words": [
                {"lemma": "volver a", "translation": "to do again / to repeat an action", "pos": "verb"},
                {"lemma": "reiteración", "translation": "reiteration / repetition", "pos": "noun"},
                {"lemma": "reincidencia", "translation": "relapse / recurrence", "pos": "noun"},
                {"lemma": "reanudar", "translation": "to resume / to pick up again", "pos": "verb"},
                {"lemma": "recaída", "translation": "relapse / setback", "pos": "noun"},
                {"lemma": "tentativa", "translation": "attempt / try", "pos": "noun"},
                {"lemma": "insistencia", "translation": "insistence / persistence", "pos": "noun"},
                {"lemma": "resurgimiento", "translation": "resurgence / revival", "pos": "noun"},
                {"lemma": "repetición", "translation": "repetition", "pos": "noun"},
                {"lemma": "revalidar", "translation": "to revalidate / to confirm again", "pos": "verb"}
            ]
        },
        "b2-23-05": {
            "id": "vocab.b2.23.05",
            "lesson": "b2-23-05",
            "title": "Sequential Periphrasis: Pasar a",
            "words": [
                {"lemma": "pasar a", "translation": "to move on to / to proceed to do", "pos": "verb"},
                {"lemma": "transición", "translation": "transition", "pos": "noun"},
                {"lemma": "secuencia", "translation": "sequence", "pos": "noun"},
                {"lemma": "consecutivo", "translation": "consecutive / sequential", "pos": "adjective"},
                {"lemma": "proceder", "translation": "to proceed / to carry on", "pos": "verb"},
                {"lemma": "exponer", "translation": "to state / to lay out / to expound", "pos": "verb"},
                {"lemma": "traspaso", "translation": "transfer / handover", "pos": "noun"},
                {"lemma": "subsecuente", "translation": "subsequent / following", "pos": "adjective"},
                {"lemma": "renglón", "translation": "item / line of topic / entry", "pos": "noun"},
                {"lemma": "fase", "translation": "phase / stage", "pos": "noun"}
            ]
        },
        "b2-chileextremos-01": {
            "id": "vocab.b2.chileextremos.01",
            "lesson": "b2-chileextremos-01",
            "title": "The Atacama Desert & Space Observatories",
            "words": [
                {"lemma": "diáfano", "translation": "crystal-clear / diaphanous", "pos": "adjective"},
                {"lemma": "radiotelescopio", "translation": "radio telescope", "pos": "noun"},
                {"lemma": "aridez", "translation": "aridity / extreme dryness", "pos": "noun"},
                {"lemma": "salar", "translation": "salt flat", "pos": "noun"},
                {"lemma": "astrofísica", "translation": "astrophysics", "pos": "noun"},
                {"lemma": "nitidez", "translation": "sharpness / clarity", "pos": "noun"},
                {"lemma": "constelación", "translation": "constellation", "pos": "noun"},
                {"lemma": "geoglifo", "translation": "geoglyph", "pos": "noun"},
                {"lemma": "sequedad", "translation": "dryness", "pos": "noun"},
                {"lemma": "albor", "translation": "dawn / earliest light", "pos": "noun"}
            ]
        },
        "b2-chileextremos-02": {
            "id": "vocab.b2.chileextremos.02",
            "lesson": "b2-chileextremos-02",
            "title": "Copper & Mega-Mining in the North",
            "words": [
                {"lemma": "rajo", "translation": "open pit mine quarry", "pos": "noun"},
                {"lemma": "yacimiento", "translation": "mineral deposit / orebody", "pos": "noun"},
                {"lemma": "fundición", "translation": "smelter / smelting plant", "pos": "noun"},
                {"lemma": "relave", "translation": "tailings / mining waste slurry", "pos": "noun"},
                {"lemma": "cátodo", "translation": "copper cathode", "pos": "noun"},
                {"lemma": "barretero", "translation": "miner drill operator / pickman", "pos": "noun"},
                {"lemma": "cuprífero", "translation": "copper-bearing / cupriferous", "pos": "adjective"},
                {"lemma": "ley", "translation": "mineral grade / ore concentration", "pos": "noun"},
                {"lemma": "tonelaje", "translation": "tonnage / volume mined", "pos": "noun"},
                {"lemma": "filón", "translation": "rich mineral vein / lode", "pos": "noun"}
            ]
        },
        "b2-chileextremos-03": {
            "id": "vocab.b2.chileextremos.03",
            "lesson": "b2-chileextremos-03",
            "title": "The Mapuche Nation & Wallmapu",
            "words": [
                {"lemma": "cosmovisión", "translation": "worldview / cosmovision", "pos": "noun"},
                {"lemma": "machi", "translation": "traditional Mapuche healer and spiritual authority", "pos": "noun"},
                {"lemma": "pewen", "translation": "Araucaria pine / monkey puzzle tree", "pos": "noun"},
                {"lemma": "rogativa", "translation": "ceremonial prayer / collective ritual supplication", "pos": "noun"},
                {"lemma": "plurinacional", "translation": "plurinational / multi-nation state", "pos": "adjective"},
                {"lemma": "kultrún", "translation": "sacred ceremonial Mapuche drum", "pos": "noun"},
                {"lemma": "weichafe", "translation": "Mapuche warrior / territorial defender", "pos": "noun"},
                {"lemma": "territorio", "translation": "ancestral territory / land base", "pos": "noun"},
                {"lemma": "ngillatun", "translation": "major Mapuche agricultural thanksgiving ceremony", "pos": "noun"},
                {"lemma": "identidad", "translation": "cultural identity", "pos": "noun"}
            ]
        },
        "b2-chileextremos-04": {
            "id": "vocab.b2.chileextremos.04",
            "lesson": "b2-chileextremos-04",
            "title": "Patagonian Fjords & Torres del Paine",
            "words": [
                {"lemma": "fiordo", "translation": "fjord / narrow coastal glacial inlet", "pos": "noun"},
                {"lemma": "ventisquero", "translation": "hanging glacier / snowdrift", "pos": "noun"},
                {"lemma": "morrena", "translation": "moraine / glacial debris ridge", "pos": "noun"},
                {"lemma": "témpano", "translation": "iceberg / floating ice sheet", "pos": "noun"},
                {"lemma": "estuario", "translation": "estuary", "pos": "noun"},
                {"lemma": "ventisca", "translation": "blizzard / gale wind snowstorm", "pos": "noun"},
                {"lemma": "macizo", "translation": "massif / mountain block", "pos": "noun"},
                {"lemma": "turbera", "translation": "peat bog", "pos": "noun"},
                {"lemma": "lenga", "translation": "Nothofagus pumilio / Patagonian deciduous beech", "pos": "noun"},
                {"lemma": "casquete", "translation": "ice cap / continental ice field", "pos": "noun"}
            ]
        },
        "b2-chileextremos-05": {
            "id": "vocab.b2.chileextremos.05",
            "lesson": "b2-chileextremos-05",
            "title": "Green Hydrogen & The Austral Energy Frontier",
            "words": [
                {"lemma": "electrólisis", "translation": "electrolysis", "pos": "noun"},
                {"lemma": "eólico", "translation": "wind-powered / aeolian", "pos": "adjective"},
                {"lemma": "ráfaga", "translation": "gust of wind / gale surge", "pos": "noun"},
                {"lemma": "descarbonización", "translation": "decarbonization", "pos": "noun"},
                {"lemma": "combustible", "translation": "fuel / synthetic energy carrier", "pos": "noun"},
                {"lemma": "soberanía", "translation": "sovereignty", "pos": "noun"},
                {"lemma": "ecorregión", "translation": "ecoregion", "pos": "noun"},
                {"lemma": "magallánico", "translation": "of the Magellan region / Fuegian", "pos": "adjective"},
                {"lemma": "pionero", "translation": "pioneer / groundbreaking", "pos": "adjective"},
                {"lemma": "infraestructura", "translation": "infrastructure", "pos": "noun"}
            ]
        }
    }

    for stem, vdata in vocab_data.items():
        write_json(f"vocabulary/b2/{stem}-voc.json", vdata)

    # 4. Grammar Files (10 files)
    grammar_data = {
        "b2-23-01": {
            "id": "grammar.b2.23.01.perifrasis-echarse-a",
            "title": "Perífrasis inceptivas: Echarse a + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis aspectual inceptiva *echarse a + infinitivo* focaliza el inicio abrupto, súbito e impulsivo de una acción o estado. Se combina primordialmente con verbos de reacciones emocionales incontrolables (*echarse a llorar*, *echarse a reír*, *echarse a temblar*) o con acciones físicas que denotan huida o movimiento impulsivo (*echarse a correr*, *echarse a volar*). No admite verbos que impliquen planificación minuciosa ni procesos deliberados prolongados."
                },
                {
                    "type": "table",
                    "title": "Usos representativos de Echarse a + infinitivo",
                    "rows": [
                        ["Al recibir la conmovedora noticia, la madre se echó a llorar de alivio.", "Upon receiving the moving news, the mother burst out crying with relief."],
                        ["Apenas escuchó la alarma en el muelle, el guardia se echó a correr hacia la dársena.", "As soon as he heard the alarm on the dock, the guard broke into a run toward the slipway."],
                        ["Toda la asamblea se echó a reír ante la ocurrencia del anciano marinero.", "The entire assembly burst into laughter at the old sailor's witty remark."],
                        ["Al sentir el temblor en las restingas, los petreles se echaron a volar desorientados.", "Feeling the tremor on the reefs, the petrels took to flight disoriented."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Echarse a* se reserva para impulsos espontáneos. Para tareas intelectuales o actividades laborales voluntarias debe utilizarse *ponerse a* (*se puso a redactar*, nunca *se echó a redactar*)."
                }
            ]
        },
        "b2-23-02": {
            "id": "grammar.b2.23.02.perifrasis-ponerse-a",
            "title": "Perífrasis inceptivas: Ponerse a + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis *ponerse a + infinitivo* expresa la iniciación deliberada, voluntaria y activa de una acción o labor por parte del sujeto. A diferencia de *echarse a*, denota disposición consciente y compromiso personal con una tarea (*ponerse a trabajar*, *ponerse a estudiar*, *ponerse a escribir*). Asimismo, en tercera persona puede combinarse con fenómenos meteorológicos cuando se presentan de modo inesperado (*se puso a llover*, *se puso a nevar*)."
                },
                {
                    "type": "table",
                    "title": "Usos de Ponerse a: labor voluntaria y fenómeno meteorológico",
                    "rows": [
                        ["Tras el sismo, la brigada minera se puso a despejar los accesos derrumbados.", "After the tremor, the mining crew set about clearing the collapsed access tunnels."],
                        ["Sin perder un minuto más, la geóloga se puso a examinar las muestras de cuarzo.", "Without wasting another minute, the geologist set to work examining the quartz samples."],
                        ["Hacia la medianoche, se puso a nevar copiosamente sobre los ventisqueros de Magallanes.", "Toward midnight, it began to snow heavily over the glaciers of Magallanes."],
                        ["Al clarear el día, los ingenieros se pusieron a revisar el generador eólico.", "At daybreak, the engineers set about inspecting the wind generator."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Ponerse a* requiere concentración activa y esfuerzo del agente. En contextos impersonales meteorológicos resalta el comienzo imprevisto de la precipitación."
                }
            ]
        },
        "b2-23-03": {
            "id": "grammar.b2.23.03.perifrasis-romper-a",
            "title": "Perífrasis inceptivas: Romper a + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis inceptiva *romper a + infinitivo* denota el comienzo repentino, ruidoso, violento o desbordante de una acción que quiebra un estado previo de quietud o contención. Se utiliza con un repertorio selecto de verbos que denotan expresiones vocales intensas (*romper a cantar*, *romper a gritar*, *romper a aplaudir*), fenómenos naturales tempestuosos (*romper a llover*, *romper a granizar*) o procesos de ebullición (*romper a hervir*)."
                },
                {
                    "type": "table",
                    "title": "Quiebre de contención con Romper a + infinitivo",
                    "rows": [
                        ["Al concluir la sinfonía, el auditorio rompió a aplaudir con fervor unánime.", "Upon the symphony's conclusion, the audience broke into enthusiastic, unanimous applause."],
                        ["Cuando el agua salada rompa a hervir, agregue las hierbas medicinales de la cordillera.", "When the salt water comes to a rolling boil, add the mountain medicinal herbs."],
                        ["Tras horas de silencio ominoso, las nubes del cabo rompieron a descargar granizo.", "After hours of ominous silence, the clouds over the cape broke into dumping hail."],
                        ["Al confirmarse el hallazgo de la veta mineral, los trabajadores rompieron a vitorear con júbilo.", "Upon confirmation of the mineral vein discovery, the workers broke into cheering with jubilation."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Romper a* aporta gran dramatismo y plasticidad sensorial al relato, presupone que la tensión acumulada se desata de golpe con energía sonora o física."
                }
            ]
        },
        "b2-23-04": {
            "id": "grammar.b2.23.04.perifrasis-volver-a",
            "title": "Perífrasis iterativas: Volver a + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis *volver a + infinitivo* es la construcción paradigmática en español para denotar la reiteración, la reanudación o la repetición de un evento que ya había acaecido con anterioridad. Equivale al adverbio 'nuevamente' o al prefijo 're-', pero posee una flexibilidad sintáctica y un vigor discursivo muy superiores. En contextos negativos (*no volver a + inf*), adquiere un valor prohibitivo o de resolución tajante de no reincidencia en una conducta."
                },
                {
                    "type": "table",
                    "title": "Reiteración y cese definitivo con Volver a",
                    "rows": [
                        ["El observatorio volvió a calibrar sus espejos ópticos tras el vendaval andino.", "The observatory recalibrated its optical mirrors once again after the Andean gale."],
                        ["Las comunidades han vuelto a sembrar semillas ancestrales en las terrazas de cultivo.", "The communities have resumed sowing ancestral seeds on the agricultural terraces."],
                        ["El práctico juró que no volvería a navegar ese canal sin remolcador de apoyo.", "The pilot swore he would not navigate that channel again without a tugboat escort."],
                        ["Los científicos volvieron a medir el grosor del manto de hielo en el glaciar Grey.", "The scientists measured the thickness of the ice sheet on Glacier Grey once again."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Con la negación *no volver a + inf* se formula una promesa firme de cese (*no volveré a cometer esa imprudencia*), de gran uso en registros orales y testimoniales."
                }
            ]
        },
        "b2-23-05": {
            "id": "grammar.b2.23.05.perifrasis-pasar-a",
            "title": "Perífrasis secuenciales: Pasar a + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis *pasar a + infinitivo* expresa la transición ordenada de una etapa a la siguiente en un proceso discursivo, administrativo o biográfico. En textos formales, exposiciones académicas y crónicas históricas, señala que el expositor o el sujeto deja atrás un tema previo para iniciar el tratamiento de un nuevo punto (*pasemos a examinar los resultados*, *pasó a ocupar la gerencia*). Denota secuencia lógica, jerarquía metódica y avance programado."
                },
                {
                    "type": "table",
                    "title": "Transición discursiva y progresión con Pasar a",
                    "rows": [
                        ["Habiendo presentado el marco geológico, pasemos a analizar la ley mineral del yacimiento.", "Having presented the geological framework, let us move on to analyzing the ore grade of the deposit."],
                        ["En 1971, la histórica mina de Chuquicamata pasó a ser administrada por el Estado chileno.", "In 1971, the historic Chuquicamata mine passed to being managed by the Chilean State."],
                        ["Acto seguido, la comisión técnica pasará a redactar las conclusiones del informe ambiental.", "Immediately afterward, the technical commission will proceed to draft the conclusions of the environmental report."],
                        ["A continuación, pasaremos a detallar las características del complejo eólico de Magallanes.", "Next, we will proceed to detail the features of the Magallanes wind energy complex."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Pasar a + infinitivo* funciona como un engranaje discursivo indispensable en ponencias, defensas de tesis y actas oficiales para articular la transición temática con elegancia formal."
                }
            ]
        },
        "b2-chileextremos-01": {
            "id": "grammar.b2.chileextremos.01.chile-atacama-astronomia",
            "title": "El discurso astronómico y descriptivo de la atmósfera diáfana de Atacama",
            "sections": [
                {
                    "type": "text",
                    "content": "El discurso descriptivo sobre la observación astronómica en el desierto de Atacama requiere el empleo preciso de adjetivación relacional, estructuras causales meteorológicas y perífrasis de precisión científica. Se articulan nociones de hiperaridez, ausencia de turbulencia térmica y aislamiento lumínico para fundamentar por qué el norte chileno concentra más del cincuenta por ciento de la capacidad de observación cósmica del planeta."
                },
                {
                    "type": "table",
                    "title": "Estructuras de descripción astronómica y geofísica",
                    "rows": [
                        ["Gracias a la absoluta sequedad atmosférica del llano de Chajnantor, las ondas cósmicas llegan intactas a ALMA.", "Thanks to the absolute atmospheric dryness of the Chajnantor plateau, cosmic waves reach ALMA intact."],
                        ["Los astrónomos disponen de más de trescientas noches despejadas al año en el desierto de Atacama.", "Astronomers have at their disposal more than three hundred clear nights a year in the Atacama Desert."],
                        ["El aislamiento de los centros urbanos garantiza un cielo virgen libre de toda contaminación lumínica.", "Isolation from urban centers ensures a pristine sky free of all light pollution."],
                        ["La atmósfera diáfana de Atacama permite contemplar galaxias remotas con una pureza inigualable.", "The pristine atmosphere of the Atacama Desert allows one to gaze at remote galaxies with unparalleled purity."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Combine complementos circunstanciales de causa (*merced a, gracias a, debido a*) con adjetivos de precisión física (*diáfano, límpido, milimétrico*) para lograr el registro técnico y ensayístico propio de la astronomía."
                }
            ]
        },
        "b2-chileextremos-02": {
            "id": "grammar.b2.chileextremos.02.chile-mineria-cobre",
            "title": "El discurso técnico-económico de la gran minería del cobre",
            "sections": [
                {
                    "type": "text",
                    "content": "El discurso técnico-minero en español formal combina terminología ingenieril de excavación a rajo abierto, procesos metalúrgicos de lixiviación y flotación, y marcos socioeconómicos sobre la renta de recursos no renovables. Exige exactitud sintáctica en el manejo de unidades de medida, proporciones cuantitativas y pasivas institucionales que describen la cadena de valor del cobre."
                },
                {
                    "type": "table",
                    "title": "Terminología y sintaxis de la ingeniería cuprífera",
                    "rows": [
                        ["Chuquicamata ha iniciado su transición histórica desde una faena a rajo abierto hacia la explotación subterránea.", "Chuquicamata has begun its historic transition from an open-pit operation toward underground mining."],
                        ["La minería del cobre constituye el pilar vertebrador de los ingresos fiscales y la balanza comercial de Chile.", "Copper mining forms the vertebral pillar of Chile's fiscal revenues and commercial trade balance."],
                        ["Las plantas desalinizadoras bombean agua marina hasta faenas situadas a más de tres mil metros de altitud.", "Desalination plants pump seawater up to operations situated more than three thousand meters above sea level."],
                        ["La producción de cátodos de cobre de alta pureza abastece la creciente electrificación global.", "The production of high-purity copper cathodes supplies growing global electrification."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Emplee nominalizaciones técnicas (*lixiviación, flotación, electroobtención, desalinizadora*) y pasivas con se (*se extraen millones de toneladas*) para otorgar objetividad al informe técnico."
                }
            ]
        },
        "b2-chileextremos-03": {
            "id": "grammar.b2.chileextremos.03.chile-wallmapu-mapuche",
            "title": "El discurso historiográfico y antropológico de la soberanía mapuche en el Wallmapu",
            "sections": [
                {
                    "type": "text",
                    "content": "El análisis sociopolítico e historiográfico de la nación mapuche exige un registro respetuoso y conceptualmente riguroso sobre soberanía territorial, memoria oral ancestral y pluralismo jurídico. Implica articular términos en mapuzugun integrados armónicamente en el discurso castellano formal y analizar las tensiones entre el Estado unitario y las demandas de autodeterminación territorial comunitaria."
                },
                {
                    "type": "table",
                    "title": "Integración conceptual: Cosmovisión y memoria en el Wallmapu",
                    "rows": [
                        ["Durante más de tres siglos, el río Biobío marcó la frontera de autonomía reconocida entre la corona española y el pueblo mapuche.", "For over three centuries, the Biobío River marked the recognized boundary of autonomy between the Spanish crown and the Mapuche people."],
                        ["La machi cumple un rol sagrado irremplazable como sanadora comunitaria y mediadora con las fuerzas cósmicas de la naturaleza.", "The machi fulfills an irreplaceable sacred role as community healer and mediator with natural cosmic forces."],
                        ["El pueblo mapuche reivindica la defensa integral de los bosques nativos frente al monocultivo forestal de pinos y eucaliptos.", "The Mapuche people advocate the comprehensive defense of native forests against pine and eucalyptus monoculture."],
                        ["La defensa del bosque nativo y de la memoria ancestral sostiene la dignidad indeleble del pueblo mapuche.", "The defense of native forests and ancestral memory sustains the indelible dignity of the Mapuche people."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Los vocablos del mapuzugun (*machi, pewen, kultrún, lof, Wallmapu*) se integran sin cursiva cuando forman parte del patrimonio cultural compartido y se acompañan de aposición explicativa en primera mención."
                }
            ]
        },
        "b2-chileextremos-04": {
            "id": "grammar.b2.chileextremos.04.chile-patagonia-glaciares",
            "title": "El discurso glaciológico y ecológico de los fiordos y canales patagónicos",
            "sections": [
                {
                    "type": "text",
                    "content": "El discurso sobre la Patagonia austral y los glaciares magallánicos requiere precisión en la descripción de procesos geomorfológicos, retrocesos de masas de hielo y adaptaciones biológicas al clima subpolar oceánico. Se estudian oraciones relativas explicativas y especificativas, conectores de correlación espacial y perífrasis modales para analizar el impacto del calentamiento global en las mayores reservas de agua dulce del hemisferio sur."
                },
                {
                    "type": "table",
                    "title": "Morfología glaciar y ecosistema subpolar magallánico",
                    "rows": [
                        ["Los Campos de Hielo Sur representan la tercera mayor concentración de hielo continental del planeta después de la Antártida y Groenlandia.", "The Southern Patagonian Ice Field represents the planet's third largest concentration of continental ice after Antarctica and Greenland."],
                        ["Las Torres del Paine exhiben agujas de granito esculpidas a lo largo de millones de años por la fuerza abrasiva de los hielos.", "Torres del Paine display granite spires sculpted over millions of years by the abrasive force of glaciers."],
                        ["El bosque subpolar magallánico alberga especies arbóreas capaces de soportar vientos que superan los cien kilómetros por hora.", "The Magellanic subpolar forest shelters tree species capable of withstanding winds exceeding one hundred kilometers per hour."],
                        ["El viento implacable azota los macizos patagónicos mientras los cóndores planean sobre los valles glaciares.", "The relentless wind batters the Patagonian massifs while condors glide over the glacial valleys."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Utilice términos glaciológicos precisos (*morrena, ventisquero, fiordo, témpano, casquete*) para enriquecer la descripción geográfica y ambientar relatos en paisajes subpolares."
                }
            ]
        },
        "b2-chileextremos-05": {
            "id": "grammar.b2.chileextremos.05.chile-energia-austral",
            "title": "El discurso prospectivo de la transición energética y el hidrógeno verde en Magallanes",
            "sections": [
                {
                    "type": "text",
                    "content": "El discurso prospectivo sobre la transición energética y el hidrógeno verde en la región de Magallanes conjuga variables termodinámicas, capacidad eólica excepcional y logística portuaria internacional. Se ejercitan construcciones causales y consecutivas, oraciones hipotéticas de futuro y verbos de proyección estratégica para examinar cómo la energía del viento austral puede transformar a Chile en un exportador de combustibles limpios sin emisiones de carbono."
                },
                {
                    "type": "table",
                    "title": "Prospectiva energética eólica y descarbonización",
                    "rows": [
                        ["Los vientos constantes del estrecho de Magallanes permiten generar energía eólica con un factor de planta inigualable en el planeta.", "The constant winds of the Strait of Magellan enable wind power generation with an unparalleled capacity factor on the planet."],
                        ["Mediante electrólisis alimentada por energía eólica, se disocia la molécula de agua para obtener hidrógeno verde puro.", "Through wind-powered electrolysis, the water molecule is split to obtain pure green hydrogen."],
                        ["Punta Arenas se perfila como un polo logístico clave tanto para la ciencia antártica como para el combustible naval limpio.", "Punta Arenas is shaping up as a key logistics hub for both Antarctic science and clean marine fuel."],
                        ["La fuerza del viento austral impulsa una revolución energética que promete transformar la matriz planetaria.", "The force of the southern wind drives an energy revolution that promises to transform the planetary matrix."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Articule oraciones con conectores de causa y consecuencia (*puesto que, por consiguiente, de ahí que*) para conectar las ventajas meteorológicas con los proyectos de ingeniería limpia."
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}-a-gr.json", gdata)

    # 5. Exercises Files (12 files)
    exercises_data = {
        "b2-23-01": [
            {
                "id": "b2-23-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-unit23-vocab"],
                "pairs": [
                    ["echarse a", "to burst into / to suddenly begin doing"],
                    ["súbito", "sudden / unexpected"],
                    ["carcajada", "loud laugh / guffaw"],
                    ["arrebato", "outburst / fit of emotion"]
                ]
            },
            {
                "id": "b2-23-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["perifrasis-echarse-a"],
                "sentence": "Al ver aparecer a su hermano sano y salvo, la joven se __ a llorar de emoción.",
                "answer": "echó",
                "english": "Upon seeing her brother appear safe and sound, the young woman burst into tears of emotion."
            },
            {
                "id": "b2-23-01.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["perifrasis-echarse-a"],
                "question": "¿Qué matiz semántico distingue a la perífrasis 'echarse a + infinitivo' de otras formas de comienzo?",
                "options": [
                    "Expresa el inicio súbito, involuntario o impulsivo de emociones intensas o movimientos bruscos.",
                    "Indica la planificación pausada y reflexiva de una tesis doctoral académica.",
                    "Describe la culminación definitiva y formal de un contrato comercial firmado.",
                    "Señala una acción habitual que ocurre todos los domingos por la mañana."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-01.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["perifrasis-echarse-a"],
                "tiles": ["Los", "caballos", "se", "echaron", "a", "correr", "por", "el", "valle."],
                "solution": ["Los", "caballos", "se", "echaron", "a", "correr", "por", "el", "valle."],
                "english": "The horses broke into a run across the valley."
            },
            {
                "id": "b2-23-01.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["perifrasis-echarse-a"],
                "prompt": [
                    {"speaker": "Guardaparques", "text": "¿Qué ocurrió cuando los turistas avistaron al puma andino en el sendero?"},
                    {"speaker": "Guía", "text": "Fue un susto tremendo: un grupo se quedó inmóvil y el resto..."}
                ],
                "options": [
                    "se echó a correr en estampida hacia el refugio de montaña.",
                    "se puso a calcular las coordenadas astronómicas del satélite.",
                    "volvió a terminar la redacción del manual de senderismo.",
                    "rompió a cocinar una cazuela caliente para todos los guardas."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-01.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["perifrasis-echarse-a"],
                "sentence": "Apenas escuchó la sirena del muelle, el marinero se echó a correr sin dudarlo un segundo.",
                "english": "As soon as he heard the dock siren, the sailor broke into a run without hesitating a second."
            }
        ],
        "b2-23-02": [
            {
                "id": "b2-23-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-unit23-vocab"],
                "pairs": [
                    ["ponerse a", "to set about / to start doing deliberately"],
                    ["diligencia", "diligence / prompt dispatch"],
                    ["tesón", "tenacity / perseverance"],
                    ["faena", "labor task / toil"]
                ]
            },
            {
                "id": "b2-23-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["perifrasis-ponerse-a"],
                "sentence": "Sin demorarse ni un minuto, los técnicos se __ a reparar el generador eólico.",
                "answer": "pusieron",
                "english": "Without delaying a single minute, the technicians set about repairing the wind generator."
            },
            {
                "id": "b2-23-02.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["perifrasis-ponerse-a"],
                "question": "¿En cuál de los siguientes casos es más natural emplear 'ponerse a + infinitivo'?",
                "options": [
                    "Para expresar la decisión deliberada de emprender una tarea laboriosa o intelectual.",
                    "Para denotar el pánico súbito que provoca una estampida en la oscuridad.",
                    "Para indicar que una acción se repite exactamente tres veces consecutivas.",
                    "Para marcar la conclusión irrevocable de una obra arquitectónica centenaria."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-02.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["perifrasis-ponerse-a"],
                "tiles": ["El", "ingeniero", "se", "puso", "a", "redactar", "el", "informe", "técnico."],
                "solution": ["El", "ingeniero", "se", "puso", "a", "redactar", "el", "informe", "técnico."],
                "english": "The engineer set about drafting the technical report."
            },
            {
                "id": "b2-23-02.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["perifrasis-ponerse-a"],
                "prompt": [
                    {"speaker": "Jefa de turno", "text": "¿Cuándo comenzaremos la inspección de los transformadores eléctricos?"},
                    {"speaker": "Electricista", "text": "Apenas terminemos de calibrar los multímetros..."}
                ],
                "options": [
                    "nos pondremos a revisar el cableado principal de la subestación.",
                    "nos echaremos a llorar de angustia frente al tablero central.",
                    "romperemos a cantar baladas folclóricas en la sala de mando.",
                    "volveremos a olvidar las herramientas en el taller de soldadura."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-02.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["perifrasis-ponerse-a"],
                "sentence": "Con notable tesón, la astrónoma se puso a verificar cada fotografía captada por el telescopio.",
                "english": "With notable tenacity, the astronomer set about verifying every photograph captured by the telescope."
            }
        ],
        "b2-23-03": [
            {
                "id": "b2-23-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-unit23-vocab"],
                "pairs": [
                    ["romper a", "to break into / to burst out doing"],
                    ["estallido", "outbreak / burst"],
                    ["fragor", "clamor / roaring noise"],
                    ["aguacero", "downpour / sudden heavy rain"]
                ]
            },
            {
                "id": "b2-23-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["perifrasis-romper-a"],
                "sentence": "De improviso, el cielo plomizo de la cordillera rompió a __ granizo sobre el campamento.",
                "answer": "descargar",
                "english": "Suddenly, the leaden sky of the mountain range broke into dumping hail on the camp."
            },
            {
                "id": "b2-23-03.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["perifrasis-romper-a"],
                "question": "¿Qué efecto expresivo singular aporta la perífrasis 'romper a + infinitivo'?",
                "options": [
                    "Transmite la fractura abrupta y ruidosa de un estado de contención o silencio previo.",
                    "Señala una acción continuada que se desarrolla con extrema lentitud durante décadas.",
                    "Indica una duda vacilante entre dos opciones culinarias de la comida campesina.",
                    "Expresa una orden jerárquica militar dictada formalmente por escrito."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-03.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["perifrasis-romper-a"],
                "tiles": ["El", "público", "rompió", "a", "aplaudir", "con", "auténtico", "júbilo."],
                "solution": ["El", "público", "rompió", "a", "aplaudir", "con", "auténtico", "júbilo."],
                "english": "The audience broke into applause with genuine joy."
            },
            {
                "id": "b2-23-03.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["perifrasis-romper-a"],
                "prompt": [
                    {"speaker": "Cocinero del barco", "text": "¿En qué momento exacto debemos echar los mariscos a la cazuela?"},
                    {"speaker": "Capitán", "text": "Espera un momento más; tienes que añadirlos justo cuando el caldo..."}
                ],
                "options": [
                    "rompa a hervir vigorosamente en el fogón.",
                    "se eche a llorar de frío por el viento.",
                    "se ponga a pensar en la navegación del canal.",
                    "vuelva a enfriarse bajo la escarcha marina."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-03.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["perifrasis-romper-a"],
                "sentence": "Al confirmarse el hallazgo de la veta mineral, los trabajadores rompieron a vitorear con júbilo.",
                "english": "Upon confirmation of the mineral vein discovery, the workers broke into cheering with jubilation."
            }
        ],
        "b2-23-04": [
            {
                "id": "b2-23-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-unit23-vocab"],
                "pairs": [
                    ["volver a", "to do again / to repeat an action"],
                    ["reiteración", "reiteration / repetition"],
                    ["reanudar", "to resume / to pick up again"],
                    ["tentativa", "attempt / try"]
                ]
            },
            {
                "id": "b2-23-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["perifrasis-volver-a"],
                "sentence": "Tras el temporal en el estrecho, los veleros volvieron a __ rumbo hacia el cabo de Hornos.",
                "answer": "fijar",
                "english": "After the storm in the strait, the sailboats once again set course toward Cape Horn."
            },
            {
                "id": "b2-23-04.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["perifrasis-volver-a"],
                "question": "¿Qué valor adquiere la perífrasis 'volver a + infinitivo' cuando va precedida de negación tajante?",
                "options": [
                    "Expresa la promesa o resolución terminante de no repetir jamás una acción en el futuro.",
                    "Denota que la acción se ejecutará con el doble de rapidez en el próximo intento.",
                    "Indica una duda gramatical sobre el tiempo verbal correcto del participio.",
                    "Señala que la acción ya fue realizada exitosamente por un agente anónimo."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-04.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["perifrasis-volver-a"],
                "tiles": ["Los", "científicos", "volvieron", "a", "medir", "el", "grosor", "del", "glaciar."],
                "solution": ["Los", "científicos", "volvieron", "a", "medir", "el", "grosor", "del", "glaciar."],
                "english": "The scientists measured the thickness of the glacier once again."
            },
            {
                "id": "b2-23-04.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["perifrasis-volver-a"],
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Habrá nuevas expediciones arqueológicas al desierto de Atacama este verano?"},
                    {"speaker": "Director del museo", "text": "Por supuesto, nuestro equipo multidisciplinario..."}
                ],
                "options": [
                    "volverá a excavar el sitio ceremonial de los geoglifos milenarios.",
                    "se echará a reír frente a las cerámicas prehispánicas encontradas.",
                    "romperá a llorar sin motivo antes de partir hacia el salar.",
                    "pasará a cancelar de inmediato toda investigación científica regional."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-04.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["perifrasis-volver-a"],
                "sentence": "El práctico de canales aseguró que volvería a inspeccionar la carta náutica antes de zarpar.",
                "english": "The channel pilot assured that he would inspect the nautical chart once again before setting sail."
            }
        ],
        "b2-23-05": [
            {
                "id": "b2-23-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-unit23-vocab"],
                "pairs": [
                    ["pasar a", "to move on to / to proceed to do"],
                    ["transición", "transition"],
                    ["subsecuente", "subsequent / following"],
                    ["renglón", "line of topic / item"]
                ]
            },
            {
                "id": "b2-23-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["perifrasis-pasar-a"],
                "sentence": "Habiendo concluido el balance financiero, pasemos a __ el plan de inversión sustentable.",
                "answer": "examinar",
                "english": "Having concluded the financial balance, let us move on to examining the sustainable investment plan."
            },
            {
                "id": "b2-23-05.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["perifrasis-pasar-a"],
                "question": "¿En qué contexto discursivo es especialmente idónea la perífrasis 'pasar a + infinitivo'?",
                "options": [
                    "En discursos formales, asambleas o informes para ordenar la transición lógica entre temas.",
                    "En fábulas infantiles para imitar el ladrido repentino de un perro asustado.",
                    "En mensajes informales de texto para comunicar un chiste entre amigos íntimos.",
                    "En descripciones poéticas para destacar la blancura inmóvil de las cumbres nevadas."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-05.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["perifrasis-pasar-a"],
                "tiles": ["La", "comisión", "pasó", "a", "debatir", "el", "proyecto", "de", "ley."],
                "solution": ["La", "comisión", "pasó", "a", "debatir", "el", "proyecto", "de", "ley."],
                "english": "The commission moved on to debating the draft bill."
            },
            {
                "id": "b2-23-05.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["perifrasis-pasar-a"],
                "prompt": [
                    {"speaker": "Presidente de la mesa", "text": "Si no hay más observaciones sobre el primer punto de la orden del día..."},
                    {"speaker": "Secretaria", "text": "Exactamente, señor presidente, ya podemos..."}
                ],
                "options": [
                    "pasar a discutir la asignación presupuestaria para las escuelas rurales.",
                    "echarnos a temblar de pánico ante la votación electrónica unánime.",
                    "ponernos a cantar melodías folclóricas en medio del hemiciclo parlamentario.",
                    "romper a llorar colectivamente frente a los periodistas congregados."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-05.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["perifrasis-pasar-a"],
                "sentence": "A continuación, pasaremos a detallar las características del complejo eólico de Magallanes.",
                "english": "Next, we will proceed to detail the features of the Magallanes wind energy complex."
            }
        ],
        "b2-23-consolidation": [
            {
                "id": "b2-23-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-unit23-vocab"],
                "pairs": [
                    ["echarse a", "to burst into / to suddenly begin doing"],
                    ["ponerse a", "to set about / to start doing deliberately"],
                    ["romper a", "to break into / to burst out doing"],
                    ["volver a", "to do again / to repeat an action"]
                ]
            },
            {
                "id": "b2-23-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["perifrasis-echarse-a"],
                "sentence": "Cuando el perro del barco ladró furioso, el marinero se __ a temblar por el frío y el susto.",
                "answer": "echó",
                "english": "When the ship's dog barked furiously, the sailor broke into shivering from the cold and fright."
            },
            {
                "id": "b2-23-consolidation.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["perifrasis-ponerse-a"],
                "question": "¿Qué oración refleja un uso genuino de iniciación deliberada de una tarea?",
                "options": [
                    "Al clarear el día, los buzos se pusieron a revisar las redes de pesca en el canal.",
                    "Al amanecer, la llovizna se echó a redactar un soneto barroco en las rocas.",
                    "Los vientos del cabo se volvieron a reír de las decisiones tomadas por el piloto.",
                    "El motor del barco rompió a estudiar matemáticas en la sala de máquinas."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-consolidation.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["perifrasis-romper-a"],
                "tiles": ["La", "multitud", "rompió", "a", "cantar", "el", "himno", "nacional."],
                "solution": ["La", "multitud", "rompió", "a", "cantar", "el", "himno", "nacional."],
                "english": "The crowd broke into singing the national anthem."
            },
            {
                "id": "b2-23-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["perifrasis-volver-a"],
                "sentence": "A pesar de las adversidades, la tripulación volvió a __ el mástil averiado de la balandra.",
                "answer": "levantar",
                "english": "Despite the adversities, the crew raised the sloop's damaged mast once again."
            },
            {
                "id": "b2-23-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["perifrasis-pasar-a"],
                "question": "¿Cuál es la función textual distintiva de 'pasar a + infinitivo' en exposiciones formales?",
                "options": [
                    "Articular la transición deliberada y metódica de un punto de la agenda al siguiente.",
                    "Describir la sorpresa incontrolable de un navegante ante una ballena jorobada.",
                    "Indicar que una acción se repite periódicamente todos los fines de semana.",
                    "Expresar una duda existencial sobre el significado de un vocablo náutico antiguo."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-consolidation.ex07",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["perifrasis-volver-a"],
                "prompt": [
                    {"speaker": "Viejo patrón de goleta", "text": "¿Crees que algún día el vapor reemplazará por completo la navegación a vela en el cabo?"},
                    {"speaker": "Joven marinero", "text": "Los tiempos cambian, pero mientras existan estas tempestades..."}
                ],
                "options": [
                    "volveremos a necesitar el coraje indómito de los navegantes del sur.",
                    "nos echaremos a cantar tonadas alegres en la cumbre de los témpanos.",
                    "nos pondremos a olvidar el rumbo en medio de la calma chicha.",
                    "romperemos a comprar boletos de ferrocarril a través del océano."
                ],
                "correct": 0
            },
            {
                "id": "b2-23-consolidation.ex08",
                "type": "dictation",
                "category": "listening",
                "teaches": ["perifrasis-pasar-a"],
                "sentence": "Concluido el rescate de la tripulación, las autoridades pasaron a investigar las causas del naufragio.",
                "english": "The crew's rescue concluded, the authorities moved on to investigating the causes of the shipwreck."
            }
        ],
        "b2-chileextremos-01": [
            {
                "id": "b2-chileextremos-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-chileextremos-vocab"],
                "pairs": [
                    ["diáfano", "crystal-clear / diaphanous"],
                    ["radiotelescopio", "radio telescope"],
                    ["aridez", "aridity / extreme dryness"],
                    ["salar", "salt flat"]
                ]
            },
            {
                "id": "b2-chileextremos-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["chile-atacama-astronomia"],
                "sentence": "En el llano de Chajnantor, las antenas de ALMA captan ondas milimétricas en un cielo extraordinariamente __.",
                "answer": "diáfano",
                "english": "On the Chajnantor plateau, ALMA's antennas capture millimeter waves under an extraordinarily crystal-clear sky."
            },
            {
                "id": "b2-chileextremos-01.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["chile-atacama-astronomia"],
                "question": "¿Por qué el desierto de Atacama es considerado la meca mundial de la astronomía observacional?",
                "options": [
                    "Por su extrema aridez, elevada altitud y más de trescientas noches despejadas al año sin turbulencia.",
                    "Porque cuenta con la mayor cantidad de lagos navegables de agua dulce en Sudamérica.",
                    "Por la existencia de frondosos bosques lluviosos que absorben todo el vapor circundante.",
                    "Debido a que el cielo está cubierto permanentemente por neblinas marinas que refractan la luz lunar."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-01.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["chile-atacama-astronomia"],
                "tiles": ["Los", "astrónomos", "escudriñan", "el", "origen", "del", "universo", "en", "Atacama."],
                "solution": ["Los", "astrónomos", "escudriñan", "el", "origen", "del", "universo", "en", "Atacama."],
                "english": "Astronomers scrutinize the origin of the universe in Atacama."
            },
            {
                "id": "b2-chileextremos-01.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["chile-atacama-astronomia"],
                "prompt": [
                    {"speaker": "Divulgadora científica", "text": "¿Qué ventaja tienen las antenas del observatorio ALMA a cinco mil metros de altitud?"},
                    {"speaker": "Astrofísico", "text": "A esa altura, casi todo el vapor de agua atmosférico queda por debajo de los receptores..."}
                ],
                "options": [
                    "lo que permite captar radiación milimétrica con una nitidez incomparable.",
                    "lo que obliga a suspender todas las observaciones astronómicas durante el verano.",
                    "provocando que las estrellas se oculten tras gruesas capas de hielo polar.",
                    "impidiendo que los radiotelescopios se conecten a la red eléctrica nacional."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-01.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["chile-atacama-astronomia"],
                "sentence": "La atmósfera virgen del desierto de Atacama permite contemplar galaxias remotas con una pureza inigualable.",
                "english": "The pristine atmosphere of the Atacama Desert allows one to gaze at remote galaxies with unparalleled purity."
            }
        ],
        "b2-chileextremos-02": [
            {
                "id": "b2-chileextremos-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-chileextremos-vocab"],
                "pairs": [
                    ["rajo", "open pit mine quarry"],
                    ["yacimiento", "mineral deposit / orebody"],
                    ["fundición", "smelter / smelting plant"],
                    ["cátodo", "copper cathode"]
                ]
            },
            {
                "id": "b2-chileextremos-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["chile-mineria-cobre"],
                "sentence": "La mina de Chuquicamata es célebre mundialmente por ser la excavación a __ abierto más imponente del planeta.",
                "answer": "rajo",
                "english": "The Chuquicamata mine is world-renowned for being the most imposing open-pit excavation on the planet."
            },
            {
                "id": "b2-chileextremos-02.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["chile-mineria-cobre"],
                "question": "¿Por qué al cobre se le denomina históricamente en Chile 'el sueldo de la nación'?",
                "options": [
                    "Porque genera una porción sustancial de los ingresos fiscales y apuntala la economía exterior.",
                    "Porque es el metal exclusivo con el que se acuñan las monedas de un centavo en el banco central.",
                    "Porque todos los ciudadanos chilenos reciben obligatoriamente un lingote de cobre al cumplir la mayoría de edad.",
                    "Debido a que el cobre es el único mineral que se consume como alimento en los campamentos."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-02.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["chile-mineria-cobre"],
                "tiles": ["Los", "camiones", "gigantescos", "transportan", "toneladas", "de", "roca", "mineralizada."],
                "solution": ["Los", "camiones", "gigantescos", "transportan", "toneladas", "de", "roca", "mineralizada."],
                "english": "The gigantic trucks transport tons of mineralized rock."
            },
            {
                "id": "b2-chileextremos-02.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["chile-mineria-cobre"],
                "prompt": [
                    {"speaker": "Estudiante de ingeniería", "text": "¿Cómo enfrenta la gran minería el desafío de la escasez hídrica en el norte?"},
                    {"speaker": "Metalurgista", "text": "Construyendo plantas desalinizadoras en la costa..."}
                ],
                "options": [
                    "para impulsar agua de mar tratada mediante acueductos hasta las faenas cordilleranas.",
                    "para transformar el mineral de cobre en lingotes de plomo biodegradable.",
                    "a fin de evaporar todas las reservas subterráneas de agua dulce del desierto.",
                    "con el objeto de reemplazar el cobre por carbón vegetal importado de Asia."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-02.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["chile-mineria-cobre"],
                "sentence": "La producción de cátodos de cobre de alta pureza abastece la creciente electrificación global.",
                "english": "The production of high-purity copper cathodes supplies growing global electrification."
            }
        ],
        "b2-chileextremos-03": [
            {
                "id": "b2-chileextremos-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-chileextremos-vocab"],
                "pairs": [
                    ["cosmovisión", "worldview / cosmovision"],
                    ["machi", "spiritual authority and healer"],
                    ["pewen", "Araucaria pine / monkey puzzle tree"],
                    ["kultrún", "sacred ceremonial drum"]
                ]
            },
            {
                "id": "b2-chileextremos-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["chile-wallmapu-mapuche"],
                "sentence": "Para la cosmovisión mapuche, la __ desempeña un papel insustituible en la sanación comunitaria y el equilibrio espiritual.",
                "answer": "machi",
                "english": "For the Mapuche cosmovision, the machi plays an irreplaceable role in community healing and spiritual balance."
            },
            {
                "id": "b2-chileextremos-03.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["chile-wallmapu-mapuche"],
                "question": "¿Qué hito histórico singular caracterizó la relación entre el pueblo mapuche y el imperio español durante la época colonial?",
                "options": [
                    "La celebración de parlamentos solemnes que reconocieron el río Biobío como frontera de autonomía territorial.",
                    "La rendición inmediata de todos los caciques en la primera semana de desembarco europeo.",
                    "La firma de un tratado para demoler todos los bosques de araucarias en la cordillera.",
                    "La adopción del idioma latín como lengua oficial de todas las asambleas indígenas."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-03.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["chile-wallmapu-mapuche"],
                "tiles": ["El", "sonido", "del", "kultrún", "marca", "el", "ritmo", "de", "la", "rogativa."],
                "solution": ["El", "sonido", "del", "kultrún", "marca", "el", "ritmo", "de", "la", "rogativa."],
                "english": "The sound of the sacred drum marks the rhythm of the ceremonial prayer."
            },
            {
                "id": "b2-chileextremos-03.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["chile-wallmapu-mapuche"],
                "prompt": [
                    {"speaker": "Socióloga", "text": "¿Cuáles son las demandas centrales que movilizan a las comunidades del Wallmapu en la actualidad?"},
                    {"speaker": "Dirigente mapuche", "text": "La restitución de nuestras tierras ancestrales usurpadas..."}
                ],
                "options": [
                    "y el reconocimiento pleno de nuestros derechos lingüísticos, culturales y territoriales.",
                    "y la tala obligatoria de todos los árboles sagrados de la cordillera andina.",
                    "junto a la privatización absoluta de todos los ríos y lagunas de la Araucanía.",
                    "para eliminar el uso del mapuzugun en todas las familias de las comunidades."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-03.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["chile-wallmapu-mapuche"],
                "sentence": "La defensa del bosque nativo y de la memoria ancestral sostiene la dignidad indeleble del pueblo mapuche.",
                "english": "The defense of native forests and ancestral memory sustains the indelible dignity of the Mapuche people."
            }
        ],
        "b2-chileextremos-04": [
            {
                "id": "b2-chileextremos-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-chileextremos-vocab"],
                "pairs": [
                    ["fiordo", "narrow coastal glacial inlet / fjord"],
                    ["ventisquero", "hanging glacier / snowdrift"],
                    ["témpano", "iceberg / floating ice sheet"],
                    ["morrena", "moraine / glacial debris ridge"]
                ]
            },
            {
                "id": "b2-chileextremos-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["chile-patagonia-glaciares"],
                "sentence": "Las imponentes paredes de granito de las Torres del Paine fueron modeladas por la acción milenaria de los __.",
                "answer": "glaciares",
                "english": "The imposing granite walls of Torres del Paine were sculpted by the millennial action of glaciers."
            },
            {
                "id": "b2-chileextremos-04.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["chile-patagonia-glaciares"],
                "question": "¿Qué relevancia hidrológica y planetaria poseen los Campos de Hielo Sur en el extremo austral chileno?",
                "options": [
                    "Constituyen la tercera mayor reserva mundial de hielo continental después de la Antártida y Groenlandia.",
                    "Son la principal zona de plantación de caña de azúcar y frutas tropicales del cono sur.",
                    "Albergan los volcanes submarinos más calientes del océano Atlántico norte.",
                    "Representan una cuenca sedimentaria donde el agua marina se evapora en menos de un segundo."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-04.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["chile-patagonia-glaciares"],
                "tiles": ["Los", "témpanos", "azules", "flotan", "a", "la", "deriva", "en", "el", "fiordo."],
                "solution": ["Los", "témpanos", "azules", "flotan", "a", "la", "deriva", "en", "el", "fiordo."],
                "english": "The blue icebergs float adrift in the fjord."
            },
            {
                "id": "b2-chileextremos-04.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["chile-patagonia-glaciares"],
                "prompt": [
                    {"speaker": "Bióloga marina", "text": "¿Cómo se adaptaron los antiguos pueblos canoeros como los kawésqar a este entorno extremo?"},
                    {"speaker": "Antropólogo austral", "text": "Navegaban en canozas de corteza de lenga manteniendo siempre encendida una fogata sobre arcilla..."}
                ],
                "options": [
                    "dominando un conocimiento asombroso de las mareas, los vientos y la fauna de los canales.",
                    "para quemar deliberadamente las laderas boscosas de todos los parques nacionales.",
                    "evitando consumir cualquier tipo de marisco o pescado en su dieta cotidiana.",
                    "viviendo en ciudades subterráneas excavadas en el interior de los témpanos flotantes."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-04.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["chile-patagonia-glaciares"],
                "sentence": "El viento implacable azota los macizos patagónicos mientras los cóndores planean sobre los valles glaciares.",
                "english": "The relentless wind batters the Patagonian massifs while condors glide over the glacial valleys."
            }
        ],
        "b2-chileextremos-05": [
            {
                "id": "b2-chileextremos-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-chileextremos-vocab"],
                "pairs": [
                    ["electrólisis", "electrolysis"],
                    ["eólico", "wind-powered / aeolian"],
                    ["descarbonización", "decarbonization"],
                    ["magallánico", "of the Magellan region / Fuegian"]
                ]
            },
            {
                "id": "b2-chileextremos-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["chile-energia-austral"],
                "sentence": "Gracias a sus ráfagas constantes, la región de Magallanes aprovecha la energía __ para producir hidrógeno verde.",
                "answer": "eólica",
                "english": "Thanks to its constant gusts, the Magallanes region harnesses wind energy to produce green hydrogen."
            },
            {
                "id": "b2-chileextremos-05.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["chile-energia-austral"],
                "question": "¿En qué consiste el proceso químico fundamental para la obtención del hidrógeno verde?",
                "options": [
                    "En descomponer el agua en hidrógeno y oxígeno mediante electrólisis alimentada con energías limpias.",
                    "En quemar carbón fósil de alta concentración de azufre en calderas industriales.",
                    "En destilar petróleo crudo importado de yacimientos submarinos sin refinar.",
                    "En mezclar agua dulce con ceniza volcánica caliente para generar vapor ácido."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-05.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["chile-energia-austral"],
                "tiles": ["Magallanes", "lidera", "la", "transición", "hacia", "combustibles", "limpios", "y", "renovables."],
                "solution": ["Magallanes", "lidera", "la", "transición", "hacia", "combustibles", "limpios", "y", "renovables."],
                "english": "Magallanes leads the transition toward clean and renewable fuels."
            },
            {
                "id": "b2-chileextremos-05.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["chile-energia-austral"],
                "prompt": [
                    {"speaker": "Ministro de Energía", "text": "¿Qué papel estratégico desempeña Punta Arenas en el mapa global del futuro?"},
                    {"speaker": "Delegada regional", "text": "Es la puerta de entrada logística a la Antártida y, además..."}
                ],
                "options": [
                    "el futuro puerto de abastecimiento de combustibles verdes para las flotas marítimas mundiales.",
                    "la única ciudad donde está prohibido por ley instalar generadores eólicos o solares.",
                    "un centro minero dedicado con exclusividad a la extracción de diamantes sintéticos.",
                    "una base militar sellada que no admite buques científicos ni expediciones polares."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-05.ex06",
                "type": "dictation",
                "category": "listening",
                "teaches": ["chile-energia-austral"],
                "sentence": "La fuerza del viento austral impulsa una revolución energética que promete transformar la matriz planetaria.",
                "english": "The force of the southern wind drives an energy revolution that promises to transform the planetary matrix."
            }
        ],
        "b2-chileextremos-consolidation": [
            {
                "id": "b2-chileextremos-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "teaches": ["b2-chileextremos-vocab"],
                "pairs": [
                    ["salar", "salt flat"],
                    ["rajo", "open pit mine quarry"],
                    ["machi", "spiritual authority and healer"],
                    ["fiordo", "narrow coastal glacial inlet / fjord"]
                ]
            },
            {
                "id": "b2-chileextremos-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["chile-atacama-astronomia"],
                "sentence": "La diafanidad de los cielos nortinos permite que los telescopios capturen la luz de galaxias __ con extrema precisión.",
                "answer": "remotas",
                "english": "The clarity of the northern skies allows telescopes to capture the light of remote galaxies with extreme precision."
            },
            {
                "id": "b2-chileextremos-consolidation.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["chile-mineria-cobre"],
                "question": "¿Qué desafío socioambiental enfrenta la minería del cobre en el desierto atacameño?",
                "options": [
                    "Gestionar eficientemente el agua desalinizada y minimizar el impacto sobre los ecosistemas de salares.",
                    "Evitar que las nevadas polares congelen la maquinaria en los meses de verano tropical.",
                    "Sustituir el cobre por madera de lenga patagónica en los conductores eléctricos.",
                    "Prohibir que los barcos mercantes carguen cátodos en los puertos del océano Pacífico."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-consolidation.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "teaches": ["chile-wallmapu-mapuche"],
                "tiles": ["El", "pueblo", "mapuche", "defiende", "el", "equilibrio", "sagrado", "de", "la", "tierra."],
                "solution": ["El", "pueblo", "mapuche", "defiende", "el", "equilibrio", "sagrado", "de", "la", "tierra."],
                "english": "The Mapuche people defend the sacred balance of the earth."
            },
            {
                "id": "b2-chileextremos-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "teaches": ["chile-patagonia-glaciares"],
                "sentence": "En los canales patagónicos, los ventisqueros cuelgan sobre las aguas saladas formando enormes bloques de __.",
                "answer": "hielo",
                "english": "In the Patagonian channels, hanging glaciers suspend over salt waters forming enormous blocks of ice."
            },
            {
                "id": "b2-chileextremos-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "teaches": ["chile-energia-austral"],
                "question": "¿Qué sinergia ecológica ofrece la Patagonia austral a la descarbonización mundial?",
                "options": [
                    "Convierte la formidable energía de los vientos magallánicos en hidrógeno y combustibles sintéticos limpios.",
                    "Permite construir represas hidroeléctricas gigantescas que inunden todos los parques nacionales.",
                    "Reemplaza el transporte marítimo internacional por globos aerostáticos de pasajeros.",
                    "Impide la entrada de barcos de investigación oceanográfica al estrecho de Magallanes."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-consolidation.ex07",
                "type": "dialogue-complete",
                "category": "dialogue",
                "teaches": ["chile-patagonia-glaciares"],
                "prompt": [
                    {"speaker": "Viajero", "text": "¿Cómo resumirías el carácter de las geografías extremas de Chile?"},
                    {"speaker": "Geógrafa", "text": "Es un diálogo entre contrastes monumentales: desde la aridez absoluta del norte estrellado..."}
                ],
                "options": [
                    "hasta la indómita belleza de los hielos eternos y los bosques sagrados del sur austral.",
                    "pasando por selvas caribeñas con plantaciones interminables de café y plátanos.",
                    "concluyendo en llanuras tropicales donde nunca sopla el viento ni desciende la temperatura.",
                    "demostrando que todo el territorio nacional está desprovisto de montañas y volcanes."
                ],
                "correct": 0
            },
            {
                "id": "b2-chileextremos-consolidation.ex08",
                "type": "dictation",
                "category": "listening",
                "teaches": ["chile-atacama-astronomia"],
                "sentence": "De la aridez sublime de Atacama al hielo infinito de Magallanes, Chile custodia fronteras naturales extraordinarias.",
                "english": "From the sublime aridity of Atacama to the infinite ice of Magallanes, Chile guards extraordinary natural frontiers."
            }
        ]
    }

    for stem, ex_list in exercises_data.items():
        ex_doc = {
            "lesson": stem,
            "exercises": ex_list
        }
        write_json(f"exercises/b2/{stem}-ex.json", ex_doc)

    # 6. Stories (1 Classic + 5 Regional + 1 Capstone + 1 Stitched)
    # Target: 650 to 825 words per story (audited strictly before write)

    # Classic Literature: Francisco Coloane - Cabo de Hornos (1941)
    story_core_23 = {
        "id": "b2-23",
        "title": "Cabo de Hornos: La tempestad y el coraje en los confines del mar",
        "level": "B2",
        "lesson": 23,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Una adaptación literaria de 'Cabo de Hornos' (1941), la célebre obra del narrador chileno Francisco Coloane: la travesía de una modesta balandra lobera en medio de las tempestades antárticas, las rompientes traicioneras de las islas Wollaston, el temple de los navegantes australes y la comunión trágica y heroica entre el ser humano y la bravura indómita de los mares del fin del mundo.",
        "characters": [
            "Patrón de la balandra Don Pascual",
            "Joven marinero fueguino Manuel",
            "Arponero y lobero curtido Pedro",
            "Anciano práctico de canales Don Juan"
        ],
        "narration": {
            "paragraphs": [
                "En el confín más meridional y temible del planeta habitado, donde el océano Atlántico y el océano Pacífico se estrellan en un torbellino perpetuo de corrientes heladas, vientos huracanados y rompientes asesinas, se alza el legendario promontorio del cabo de Hornos. Durante siglos, las olas ciclópeas de más de veinte metros que barren las islas Wollaston y el archipiélago de Tierra del Fuego devoraron centenares de veleros, goletas y clíperes que intentaban cruzar de un océano a otro, sembrando los fondos marinos de maderos astillados y osamentas de navegantes. En esa geografía implacable de sal, piedra y nieve, los hombres que se aventuraban por los canales no eran héroes de mármol, sino cazadores de lobos marinos, buscadores de pepitas de oro y pescadores silenciosos cuya única riqueza consistía en su temple indomable y en su respeto reverente por el mar.",
                "En la penumbra grisácea del amanecer austral, la pequeña balandra lobera *San Pedro* cabeceaba violentamente al abrigo precario de una caleta rocosa en la isla Navarino. El veterano patrón don Pascual, hombre de pocas palabras cuya piel cobriza parecía curtida por la salmuera y el viento helado, examinaba con mirada grave el horizonte sur, donde un denso telón de nubes plomizas avanzaba tapando las cumbres escarpadas. A bordo, el joven marinero fueguino Manuel y el arponero Pedro aseguraban los cabos, trincaban las barricas de grasa y alistaban los arpones para la cacería de lobos finos en las restingas exteriores. Al advertir el cambio de viento, don Pascual no dudó: ordenó levar anclas y la tripulación se puso a trabajar de inmediato con fría precisión, sabiendo que el invierno antártico no perdonaba vacilaciones.",
                "Al salir a mar abierto rumbo a la roca del Cabo, el viento suroeste sopló de golpe con la furia de un látigo de hielo. Las olas descomunales rompieron a estrellarse sobre la cubierta de proa, inundando las escotillas y haciendo gemir la arboladura de roble como si fuera a partirse en dos. En medio del fragor ensordecedor de la marejada, cuando un golpe de mar estuvo a punto de barrer al timonel por la borda, el viejo Pedro se echó a reír con una mezcla salvaje de desesperación y orgullo marinero, gritando que el cabo estaba cobrando su diezmo de sangre. Don Pascual, aferrado firmemente a la caña del timón con los nudillos blancos de tensión, mantuvo el rumbo contra viento y marea, buscando desesperadamente el paso angosto entre los farallones de piedra negra donde las olas reventaban en nubes de espuma blanca.",
                "Hacia el mediodía, un silencio repentino y fantasmal envolvió la embarcación: la balandra había penetrado en una caleta escondida entre los acantilados verticales de la roca viva, un refugio milagroso donde anidaban miles de lobos marinos de dos pelos. Sobre las piedras resbaladizas cubiertas de algas y guano, los animales bramaban con ferocidad territorial ante la llegada de los intrusos. Sin perder un instante, sabiendo que la calma chicha del ojo del temporal era fugaz, los hombres saltaron a las rocas y se pusieron a faenar con rapidez febril. La sangre caliente de los lobos teñía las pozas de agua marina mientras el viento del suroeste volvía a arreciar en las alturas de los peñones, anunciando la segunda embestida del temporal con ráfagas que superaban los ciento veinte kilómetros por hora.",
                "Con las bodegas cargadas hasta el límite con cueros salados y manteca valiosa, la *San Pedro* tuvo que enfrentar el retorno a través del tempestuoso mar de Drake. Fue una noche de angustia infinita donde el barco crujió en cada embate de las olas y los hombres, empapados hasta los huesos y temblando de fatiga, achicaban el agua de la sentina balde a balde sin permitirse un instante de descanso. En los momentos más oscuros, cuando la muerte parecía rozar el casco con sus dedos congelados, Manuel comprendió la lección que ningún libro podía enseñar: en los canales australes, el ser humano no conquista la naturaleza mediante la soberbia técnica, sino aprendiendo a doblegar su propio miedo para convivir con la inmensidad aterradora del mar.",
                "Cuando las primeras luces del alba recortaron la silueta protectora de los montes Dientes de Navarino y la balandra fondeó por fin en aguas mansas de Puerto Toro, los tripulantes contemplaron a la distancia la silueta negra y lejana del cabo de Hornos perdiéndose entre la neblina. Con *Cabo de Hornos*, Francisco Coloane legó a la literatura universal una de las epopeyas marinas más conmovedoras y verdaderas jamás escritas: un homenaje imperecedero a aquellos seres curtidos que, en los confines desolados del mundo, demostraron que el espíritu humano es capaz de desafiar las tormentas más feroces con tal de preservar su libertad, su sustento y su inquebrantable dignidad frente al abismo oceánico."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué escenario geográfico y marino sirve de marco a la narración de Francisco Coloane en 'Cabo de Hornos'?",
                        "options": [
                            "El archipiélago fueguino, las islas Wollaston y el mar de Drake en el confín meridional de Chile.",
                            "Las playas cálidas de arena blanca del mar Caribe frente a las costas de Cartagena.",
                            "Un oasis de palmeras datileras situado en medio del desierto del Sahara septentrional.",
                            "Las orillas pantanosas del río Amazonas en la frontera selvática entre Perú y Brasil."
                        ],
                        "correctIndex": 0,
                        "explanation": "La obra transcurre en las peligrosas y gélidas aguas del cabo de Hornos y Tierra del Fuego."
                    },
                    {
                        "question": "¿A qué arriesgada actividad productiva se dedicaba la tripulación de la balandra 'San Pedro'?",
                        "options": [
                            "A la cacería de lobos marinos finos en las rompientes rocosas para comerciar cueros y grasa.",
                            "Al cultivo intensivo de flores tropicales ornamentales para exportar a Europa en barricas.",
                            "Al transporte exclusivo de libros de filosofía clásica entre los puertos del mar Báltico.",
                            "A la búsqueda de restos de naves espaciales caídas en las selvas de Centroamérica."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los loberos australes cazaban lobos marinos en las restingas para extraer pieles y grasa valiosa."
                    },
                    {
                        "question": "¿Qué lección fundamental aprende el joven marinero Manuel durante la travesía en medio del temporal?",
                        "options": [
                            "Que el ser humano no vence al mar con soberbia, sino venciendo su propio miedo y respetando la fuerza indómita de la naturaleza.",
                            "Que la navegación a vela debe prohibirse de inmediato para usar únicamente botes de remo.",
                            "Que los marineros nunca deben mirar hacia el sur porque los farallones reflejan mala suerte.",
                            "Que el oro es el único valor por el que vale la pena arriesgar la vida en los canales."
                        ],
                        "correctIndex": 0,
                        "explanation": "Manuel aprende la sabiduría marinera austral basada en la humildad, el coraje y el respeto al océano."
                    }
                ]
            }
        }
    }

    # Regional Story 1: Atacama
    story_chile_01 = {
        "id": "b2-chileextremos-01",
        "title": "La ventana al infinito: El desierto de Atacama y la mirada cósmica",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre el desierto de Atacama: el lugar no polar más árido del planeta, la combinación única de sequedad extrema y altitud en el llano de Chajnantor, los grandes observatorios astronómicos internacionales como ALMA y Paranal, los enigmas arqueológicos de los geoglifos de Pintados y el florecimiento del astroturismo bajo cielos diáfanos.",
        "characters": [
            "Astrónoma chilena Valentina",
            "Ingeniero de ALMA Mateo",
            "Arqueólogo atacameño Don Tomás",
            "Guía astronómica de San Pedro Sofía"
        ],
        "narration": {
            "paragraphs": [
                "En el norte grande de Chile, extendiéndose a lo largo de más de mil kilómetros entre la costa del océano Pacífico y la muralla imponente de los Andes, se despliega el desierto de Atacama: el territorio hiperárido no polar más seco y antiguo de la Tierra. En amplias franjas de este páramo mineral de arcilla rojiza y costras de sal fósil, los registros pluviométricos confirman que no ha caído una sola gota de lluvia medible en siglos enteros. Este rigor extremo obedece a un cerco meteorológico perfecto: por el poniente, la fría corriente marina de Humboldt enfría las capas bajas de la atmósfera impidiendo la formación de nubes convectivas, mientras por el oriente, la gigantesca Cordillera de los Andes actúa como un biombo natural infranqueable que atrapa toda la humedad proveniente de la cuenca amazónica.",
                "Sin embargo, lo que a simple vista parece un desierto desprovisto de vida es en realidad uno de los laboratorios científicos y patrimoniales más fascinantes del planeta. A cinco mil metros sobre el nivel del mar, en el gélido y desolado llano de Chajnantor, opera el Atacama Large Millimeter/submillimeter Array (ALMA): el mayor observatorio astronómico terrestre jamás construido por la humanidad. Un ejército de sesenta y seis antenas parabólicas gigantescas de doce y siete metros de diámetro, construidas con fibra de carbono y movilizadas por transportadores colosales de veintiocho ruedas, funcionan al unísono como un solo telescopio virtual de dieciséis kilómetros de envergadura, escudriñando las longitudes de onda milimétricas del cosmos donde nacen las estrellas y se forman los sistemas planetarios.",
                "La elección de Atacama para instalar ALMA, así como los míticos observatorios de Paranal con su Very Large Telescope (VLT), La Silla y el futuro Extremely Large Telescope (ELT), no fue fortuita. Con más de trescientas cincuenta noches completamente despejadas al año, una atmósfera de extrema delgadez y una humedad relativa que con frecuencia desciende por debajo del dos por ciento, el cielo nocturno sobre el desierto exhibe una transparencia óptica y una ausencia de turbulencia térmica sin parangón en el hemisferio sur. Al caer el crepúsculo, cuando el sol poniente enciende los volcanes tutelares como el Licancabur y el Láscar en tonos cobrizos y violetas, la bóveda celeste se convierte en un manto sobrecogedor donde la Vía Láctea no es una tenue mancha lechosa, sino un río denso de polvo estelar y nebulosas que arroja sombras visibles sobre el suelo.",
                "Esa fascinación por los astros no comenzó con los radiotelescopios modernos. Miles de años antes de la llegada de la ciencia contemporánea, los pueblos ancestrales atacameños (licanantay) y quechuas ya contemplaban este mismo firmamento con devoción sagrada. Para ellos, las constelaciones no se dibujaban uniendo puntos brillantes de estrellas, sino interpretando las figuras oscuras dibujadas por las nubes de polvo interestelar contra el brillo de la galaxia: la llama cósmica con su cría, la serpiente sagrada y el sapo fecundador. Sobre las laderas secas de las quebradas, en sitios asombrosos como los geoglifos de Pintados y el Valle del Arcoíris, los antiguos habitantes grabaron en la roca gigantescas figuras geométricas, camélidos y chamanes que guiaban las caravanas de intercambio entre el altiplano y la costa marina.",
                "Hoy en día, junto al avance de la astrofísica de frontera que busca rastrear los orígenes del universo y posibles biofirmas en exoplanetas lejanos, el desierto vive una vibrante revolución cultural y turística. En oasis tradicionales como San Pedro de Atacama y en comunidades licanantay de Toconao y Peine, los pobladores locales han desarrollado proyectos pioneros de astroturismo y turismo comunitario, enseñando a viajeros de los cinco continentes a leer el mapa celeste con los ojos de sus abuelos y a proteger la pureza del cielo mediante normas estrictas contra la contaminación lumínica.",
                "Al contemplar el firmamento atacameño en medio del silencio absoluto de la noche, cuando el frío polar del altiplano cala los huesos y el universo entero parece descolgarse al alcance de la mano, el ser humano experimenta una conmovedora sensación de humildad y maravilla cósmica: comprende que en esta tierra árida donde el agua es el tesoro más escaso, la luz diáfana de las estrellas se convirtió en el manantial infinito que alimenta la curiosidad, la ciencia y la imaginación inmortal de toda la especie humana."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué combinación de factores climáticos y orográficos genera la hiperaridez extrema del desierto de Atacama?",
                        "options": [
                            "La corriente marina fría de Humboldt por el oeste y el biombo natural de la Cordillera de los Andes por el este.",
                            "La erupción ininterrumpida de cientos de géiseres de vapor caliente que secan la selva tropical.",
                            "La ausencia total de vientos en todo el continente sudamericano durante los doce meses del año.",
                            "La presencia de minas subterráneas de carbón que absorben toda la lluvia antes de tocar tierra."
                        ],
                        "correctIndex": 0,
                        "explanation": "La corriente fría de Humboldt y la muralla andina bloquean la humedad de ambos lados creando la hiperaridez."
                    },
                    {
                        "question": "¿Qué singular complejo científico internacional opera en el llano de Chajnantor a cinco mil metros de altitud?",
                        "options": [
                            "El radiotelescopio ALMA, compuesto por sesenta y seis antenas parabólicas de alta precisión.",
                            "Una central nuclear subterránea diseñada para calentar las aguas del lago Titicaca.",
                            "Un laboratorio botánico dedicado con exclusividad al cultivo de orquídeas acuáticas marinas.",
                            "Una base militar interoceánica construida para almacenar combustibles pesados."
                        ],
                        "correctIndex": 0,
                        "explanation": "ALMA es el mayor conjunto de radiotelescopios terrestres del planeta para observar ondas milimétricas."
                    },
                    {
                        "question": "¿Cómo interpretaban las constelaciones en el cielo nocturno los pueblos ancestrales atacameños?",
                        "options": [
                            "Identificaban figuras animales sagradas en las zonas oscuras de polvo interestelar contra el fondo galáctico.",
                            "Conectaban las estrellas para trazar retratos de reyes de la mitología griega antigua.",
                            "Pintaban con tintes vegetales las nubes bajas para iluminar los caminos nocturnos de caravanas.",
                            "Creían que las estrellas eran fósforos encendidos por los conquistadores españoles en la cordillera."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los pueblos andinos interpretaban las constelaciones oscuras (nebulosas de polvo) de la Vía Láctea."
                    }
                ]
            }
        }
    }

    # Regional Story 2: Cobre y Minería
    story_chile_02 = {
        "id": "b2-chileextremos-02",
        "title": "Las venas rojas de la montaña: Chuquicamata, el cobre y el sueldo de Chile",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la gran minería del cobre en el norte chileno: la monumental excavación a rajo abierto de Chuquicamata y el coloso subterráneo de Minera Escondida, la nacionalización histórica del cobre en 1971, los procesos tecnológicos de lixiviación y flotación, y la forja de la identidad del trabajador minero en medio de la soledad del desierto.",
        "characters": [
            "Minero barrenista Don Héctor",
            "Ingeniera metalúrgica Camila",
            "Dirigente sindical cuprífero Rodrigo",
            "Geóloga de exploración Javiera"
        ],
        "narration": {
            "paragraphs": [
                "En la meseta desértica de la región de Antofagasta, a casi tres mil metros sobre el nivel del mar y a escasos kilómetros de la ciudad de Calama, la tierra se abre en un anfiteatro ciclópeo de proporciones dantescas que sobrecoge a cualquier observador: el mineral de Chuquicamata. Con más de cinco kilómetros de longitud, tres de ancho y un kilómetro de profundidad vertical, este cráter artificial esculpido por el ingenio humano es la mayor excavación a rajo abierto del planeta. En sus bancos concéntricos escalonados en la roca viva, camiones tolva monstruosos de cuatrocientas toneladas de capacidad —cuyas ruedas duplican la estatura de un adulto— ascienden lentamente en espiral cargando mineral de roca pulverizada, semejando diminutas hormigas mecánicas operando en las entrañas mismas de la corteza terrestre.",
                "Chile es, por amplio margen geológico y productivo, el principal productor y exportador de cobre del planeta Tierra, concentrando casi un tercio de la oferta mundial del metal rojo. Desde las remotas explotaciones precolombinas donde los pueblos atacameños martillaban cobre nativo para crear hachas rituales y brazaletes funerarios, hasta el auge contemporáneo impulsado por colosos como Minera Escondida, El Teniente y Chuquicamata, la historia económica, política y social de Chile ha estado indefectiblemente soldada al destino de sus yacimientos cupríferos. Bautizado popularmente por el presidente Salvador Allende como 'el sueldo de Chile' al concretar la histórica nacionalización de la gran minería en julio de 1971 con el respaldo unánime de todo el Congreso Nacional, el cobre aporta hasta hoy los recursos fiscales indispensables para financiar la educación pública, los hospitales y las obras de infraestructura de la república.",
                "Sin embargo, extraer el cobre en medio del desierto más árido del orbe constituye una colosal hazaña de ingeniería metalúrgica y adaptación humana. Tras la fragmentación de la roca mediante tronaduras controladas con dinamita y nitrato, los bloques pasan por chancadores mecánicos que reducen la piedra al tamaño de gravilla fina. Luego, según se trate de minerales oxidados o sulfurosos, el material es sometido a complejos procesos de lixiviación ácida o a celdas de flotación espumosa donde burbujas de reactivos químicos atrapan las partículas ricas en cobre, para luego fundirlas a más de mil doscientos grados en crisoles incandescentes o refinarlas mediante electroobtención, dando origen a relucientes cátodos de cobre puro con un noventa y nueve coma noventa y nueve por ciento de pureza que viajan en trenes hacia los puertos de Antofagasta y Mejillones.",
                "Esa formidable maquinaria técnica descansa, en última instancia, sobre el sudor, la valentía y la fraternidad inquebrantable de la familia minera chilena. Durante generaciones, miles de familias vivieron en el histórico campamento de Chuquicamata, una auténtica ciudad de adobe, ladrillo y chapa construida al borde del abismo minero que albergó escuelas, teatros, pulperías y canchas de fútbol, hasta que las exigencias ambientales y la expansión de los botaderos forzaron su desalojo y traslado definitivo a Calama en 2007. En los socavones y talleres, la solidaridad forjada frente al peligro diario de los derrumbes, el polvo silicoso que amenazaba los pulmones y el frío nocturno dio nacimiento a uno de los movimientos sindicales más cultos, organizados y combativos de la historia latinoamericana.",
                "En la actualidad, la minería chilena enfrenta una profunda metamorfosis tecnológica y ecológica dictada por las urgencias del cambio climático. Con la ley del mineral en paulatino descenso tras más de un siglo de extracción continua, Chuquicamata ha inaugurado su histórica transición hacia la minería subterránea, perforando cientos de kilómetros de túneles automatizados bajo el fondo del rajo antiguo. Al mismo tiempo, las faenas mineras reemplazan el uso de aguas dulces continentales por enormes plantas desalinizadoras en la costa y abastecen sus procesos con energía solar y eólica del desierto, adaptándose a las exigencias de un mercado global que demanda un 'cobre verde' trazable y bajo en emisiones para alimentar la revolución planetaria de los vehículos eléctricos y las energías limpias.",
                "Al contemplar el rajo de Chuquicamata al atardecer, cuando las sombras azuladas invaden el fondo del abismo y las luces artificiales de las palas mecánicas comienzan a titilar como una constelación terrestre, el visitante comprende la magnitud del desafío minero: en estas rocas resecas donde la naturaleza negó el agua y los árboles, el trabajo incansable del minero chileno arrancó de las entrañas de la tierra el metal rojo que hace latir las comunicaciones, la industria y la transición energética del mundo entero."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito histórico y político transformó la administración de la gran minería del cobre en Chile en 1971?",
                        "options": [
                            "La nacionalización unánime del cobre impulsada por Salvador Allende, catalogando el mineral como 'el sueldo de Chile'.",
                            "La privatización total de todas las faenas mineras y su entrega a empresas navieras extranjeras.",
                            "El cierre definitivo de Chuquicamata por decreto presidencial para transformarla en un museo de cera.",
                            "La prohibición absoluta de exportar minerales a los países miembros de las Naciones Unidas."
                        ],
                        "correctIndex": 0,
                        "explanation": "La nacionalización del cobre en julio de 1971 declaró el mineral como recurso estratégico del Estado chileno."
                    },
                    {
                        "question": "¿Qué importante transformación productiva y tecnológica ha iniciado Chuquicamata en los últimos años?",
                        "options": [
                            "La transición de la tradicional faena a rajo abierto hacia una moderna explotación subterránea automatizada.",
                            "La inundación deliberada del cráter para convertirlo en una represa hidroeléctrica de agua dulce.",
                            "La suspensión de la extracción de cobre para dedicarse exclusivamente a la minería de salitre artificial.",
                            "El reemplazo de todos los camiones tolva por trenes impulsados enteramente a vapor de carbón mineral."
                        ],
                        "correctIndex": 0,
                        "explanation": "Chuquicamata Subterránea permite explotar reservas profundas bajo el fondo del agotado rajo abierto."
                    },
                    {
                        "question": "¿Cómo enfrenta la minería chilena contemporánea el grave problema de la escasez de agua en el desierto?",
                        "options": [
                            "Mediante la construcción de plantas desalinizadoras en la costa que bombean agua de mar hacia la cordillera.",
                            "Atrayendo nubes de lluvia desde la selva amazónica mediante cohetes con cristales de yoduro.",
                            "Comprando hielo continental derretido de los glaciares de la cordillera del Himalaya.",
                            "Prohibiendo a los trabajadores beber agua potable durante las jornadas laborales en el desierto."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las plantas desalinizadoras permiten a las mineras operar sin agotar las escasas cuencas de agua dulce del altiplano."
                    }
                ]
            }
        }
    }

    # Regional Story 3: Wallmapu
    story_chile_03 = {
        "id": "b2-chileextremos-03",
        "title": "La raíz que no cede: El Wallmapu, el pewen sagrado y la voz mapuche",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre el pueblo mapuche y su territorio ancestral del Wallmapu en el centro-sur de Chile y Argentina: la resistencia milenaria ante la conquista incaica y española, los parlamentos de la frontera en el Biobío, la cosmovisión ligada a la tierra (Ñuke Mapu) y a la araucaria (pewen), la autoridad espiritual de la machi y la demanda contemporánea por autonomía territorial y plurinacionalidad.",
        "characters": [
            "Machi Francisca Linconao",
            "Kimche o anciano sabio Don Millanao",
            "Profesora de mapuzugun Rayén",
            "Dirigente territorial Lefxaru"
        ],
        "narration": {
            "paragraphs": [
                "Al cruzar el río Biobío hacia el sur de Chile, la geografía se transforma de pronto en un territorio denso, húmedo y milenario donde los bosques nativos de coigües, robles, tepas y alerces cubren colinas onduladas y valles volcánicos vigilados por los conos nevados del Llaima, el Villarrica y el Lonquimay. Este territorio ancestral, conocido en lengua mapuzugun como el *Wallmapu*, es el hogar originario de la nación mapuche: la 'gente de la tierra' (*mapu*, tierra; *che*, gente). A diferencia de los grandes imperios precolombinos como el Azteca o el Inca, cuya estructura centralizada colapsó rápidamente tras la captura de sus gobernantes por las huestes hispanas, los mapuches carecían de una capital única o de un rey todopoderoso: su fuerza radicaba en una confederación horizontal y autónoma de comunidades familiares (*lof*) unidas por lazos de sangre, reciprocidad comunitaria y una lealtad indestructible a su tierra.",
                "Durante el siglo dieciséis, cuando las armaduras de hierro de los conquistadores españoles parecían invencibles en todo el continente americano, el pueblo mapuche protagonizó la resistencia militar más prolongada, heroica y tenaz de la historia colonial: la Guerra de Arauco. Con estrategas legendarios como Lautaro (*Leftraru*), el joven que aprendió las tácticas de caballería de los españoles siendo caballerizo de Pedro de Valdivia para luego utilizarlas magistralmente contra sus antiguos amos, y Caupolicán, las huestes mapuches frenaron en seco el avance imperial. La corona española se vio obligada a reconocer la imposibilidad de someterlos por las armas y pactó con los lonkos mapuches en solemnes parlamentos diplomáticos, como el célebre Parlamento de Quilín de 1641, donde el río Biobío quedó fijado formalmente como una frontera internacional de autonomía soberana que perduró intacta durante más de doscientos años.",
                "En el corazón espiritual de este pueblo no late la ambición de dominar la naturaleza, sino una cosmovisión holística donde el ser humano es apenas un elemento más dentro del tejido sagrado de la vida. Para la cosmovisión mapuche, la tierra (*Ñuke Mapu*) es una madre nutricia viva que no puede ser parcelada, vendida ni privatizada como una simple mercancía comercial. En las altas cumbres de la cordillera de la Costa y de los Andes florece el *pewen* o araucaria milenaria, un árbol fósil sagrado cuyos conos proporcionan el piñón, semilla rica en almidones y proteínas que salvó a las familias mapuches de la hambruna durante inviernos inclementes y que consolidó la identidad del pueblo pehuenche.",
                "En cada comunidad comunitaria, la figura tutelar y más respetada es la *machi*: mujer sabia, médica tradicional y líder espiritual que se comunica con las fuerzas protectoras de la naturaleza mediante el trance inducido por el sonido sagrado del *kultrún* —el tambor ceremonial de madera y cuero que reproduce la estructura de los cuatro cuadrantes cósmicos—. Durante la ceremonia colectiva del *ngillatun*, las familias se congregan frente al *rehue* —el tronco sagrado de canelo escalonado que conecta la tierra con el cielo— para orar por las lluvias oportunas, la fertilidad de las cosechas y la paz comunitaria, reafirmando una ética de respeto a los espíritus de los ríos, los cerros y los humedales (*menoko*).",
                "Esa autonomía soberana fue quebrantada brutalmente a fines del siglo diecinueve, cuando los ejércitos republicanos de Chile y Argentina llevaron a cabo las campañas militares denominadas eufemísticamente la 'Pacificación de la Araucanía' y la 'Campaña del Desierto'. Mediante el fuego y la bayoneta, el Estado chileno despojó a las comunidades mapuches de más del noventa y cinco por ciento de sus tierras ancestrales, arrinconando a las familias en reducciones diminutas e improductivas y entregando los valles a colonos europeos y compañías forestales. En las últimas décadas, la expansión voraz de las plantaciones industriales de pino y eucalipto —que secan las napas freáticas y acidifican el suelo— desató un profundo conflicto territorial donde las comunidades exigen la restitución de sus tierras comunales, la desmilitarización de sus valles y el reconocimiento explícito del Estado plurinacional.",
                "Al escuchar hoy el eco del kultrún en una rogativa al amanecer entre las araucarias milenarias de Curarrehue, mientras los jóvenes aprenden con orgullo el mapuzugun que sus abuelos debieron ocultar por vergüenza colonial, el observador comprende la fuerza indestructible de esta tierra: el pueblo mapuche no es un vestigio arqueológico del pasado, sino una nación viva y digna que continúa enseñando al mundo que la supervivencia de la humanidad depende de nuestra capacidad para reconciliarnos con el espíritu sagrado de la Madre Tierra."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito diplomático colonial singular fijó el Parlamento de Quilín en 1641 entre la corona española y los mapuches?",
                        "options": [
                            "Reconoció el río Biobío como una frontera de autonomía territorial mapuche que perduró más de dos siglos.",
                            "El traspaso voluntario de todas las tierras indígenas a la orden de los sacerdotes jesuitas de Roma.",
                            "La rendición incondicional de los lonkos mapuches y el destierro de sus familias hacia las islas Filipinas.",
                            "Un acuerdo para construir un ferrocarril transandino entre Valparaíso y la ciudad de Buenos Aires."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Parlamento de Quilín reconoció la frontera del Biobío y la soberanía mapuche al sur del río."
                    },
                    {
                        "question": "¿Qué rol fundamental desempeña la 'machi' en la organización social y espiritual de la comunidad mapuche?",
                        "options": [
                            "Es la máxima autoridad espiritual y sanadora que canaliza las rogativas comunitarias tocando el kultrún.",
                            "Es la capitana general encargada exclusivamente del adiestramiento militar de la caballería.",
                            "Es la jueza enviada por el gobierno de Santiago para cobrar los impuestos a la madera talada.",
                            "Es la encargada de diseñar los mapas astronómicos para los observatorios espaciales de Atacama."
                        ],
                        "correctIndex": 0,
                        "explanation": "La machi es la guía espiritual, curandera y mediadora cósmica esencial en la cosmovisión mapuche."
                    },
                    {
                        "question": "¿Qué árbol sagrado andino proporciona el piñón, alimento vital para la identidad del pueblo pehuenche?",
                        "options": [
                            "La araucaria milenaria o pewen, adaptada a resistir las nevadas en las altas cumbres volcánicas.",
                            "El eucalipto de exportación importado desde los pantanos de Australia en el siglo veinte.",
                            "El pino radiata utilizado para la fabricación de celulosa y papel comercial.",
                            "La palmera datilera cultivada en los valles templados del norte árido."
                        ],
                        "correctIndex": 0,
                        "explanation": "La araucaria o pewen es el árbol sagrado cuyo fruto (el piñón) sustenta la vida y el nombre pehuenche."
                    }
                ]
            }
        }
    }

    # Regional Story 4: Patagonia Glaciares
    story_chile_04 = {
        "id": "b2-chileextremos-04",
        "title": "El laberinto del hielo: Los canales patagónicos y las Torres del Paine",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía ecológica y geográfica por la Patagonia chilena: el laberinto de fiordos y canales tallados por glaciares, los colosales Campos de Hielo Sur, las imponentes agujas de granito de las Torres del Paine, el bosque subpolar magallánico de lengas y coigües, y la memoria de los pueblos canoeros originarios (Kawésqar y Yagán).",
        "characters": [
            "Guardaparques de Torres del Paine Ignacio",
            "Bióloga marina de fiordos Macarena",
            "Navegante de canales Don Amador",
            "Escaladora andina Valeria"
        ],
        "narration": {
            "paragraphs": [
                "En el tercio más austral del continente sudamericano, la fisonomía geográfica de Chile se fragmenta de modo prodigioso en un laberinto inextricable de miles de islas escarpadas, fiordos profundos, penínsulas deshabitadas y canales encajonados entre murallas de roca pulida por el hielo. Desde el golfo de Penas hasta el cabo de Hornos, el océano Pacífico penetra tierra adentro en angostas gargantas marinas donde desembocan gigantescas lenguas glaciares de color azul zafiro, alimentadas por la tercera mayor concentración de hielo continental del planeta Tierra después de la Antártida y Groenlandia: los colosales Campos de Hielo Sur. En este reino indómito donde el agua en estado sólido, líquido y gaseoso libra una batalla perpetua, el rugido ensordecedor del desprendimiento de un témpano de hielo sobre el agua de un fiordo quiebra el silencio de una de las geografías más prístinas y vírgenes del planeta.",
                "En el corazón continental de esta región se alza el Parque Nacional Torres del Paine, catalogado con justicia por geógrafos y viajeros de todo el orbe como la octava maravilla natural del mundo. Sobre una estepa ventosa salpicada de lagunas de aguas turquesas cargadas de sedimentos glaciares, emergen verticalmente tres monolitos ciclópeos de granito gris y oscuro que se elevan casi dos mil quinientos metros sobre el nivel del suelo como las torres de una fortaleza mitológica. Esculpidas durante millones de años por el choque tectónico y la fuerza abrasiva de glaciares colosales, las Torres y los Cuernos del Paine desafían a los vientos más huracanados del planeta, con ráfagas del oeste que barren la estepa a más de ciento cuarenta kilómetros por hora levantando remolinos de agua sobre el lago Pehoe.",
                "En las laderas protegidas de las quebradas y en las riberas de los ríos torrentosos se refugia el bosque subpolar magallánico, un ecosistema vegetal asombroso compuesto predominantemente por árboles del género *Nothofagus*, como la lenga caducifolia, el ñirre achaparrado y el coigüe de Magallanes. En los meses de otoño, las laderas montañosas estallan en una paleta cromática deslumbrante de rojos encendidos, naranjas cobrizos y amarillos dorados antes de desprender sus hojas para afrontar las tormentas de nieve del invierno. Entre las ramas cubiertas de líquenes barbudos salta el carpintero negro gigante con su penacho rojo encendido, mientras en las lomas abiertas pastan manadas de guanacos vigilantes que emiten agudos silbidos de alerta ante el menor movimiento del puma andino, el gran depredador sigiloso de la estepa.",
                "Pero la Patagonia no es solo una estampa de belleza geológica y vida silvestre; es también la patria ancestral de pueblos nómadas originarios dotados de una adaptación fisiológica y cultural milagrosa: los pueblos canoeros Kawésqar y Yagán. Durante más de seis mil años antes de la llegada de los colonizadores europeos, estas familias navegaban por los tempestuosos canales en frágiles canoas fabricadas con corteza cosida de lenga, llevando permanentemente en el centro de la embarcación una pequeña fogata encendida sobre una cama de barro para calentarse y cocinar. Desnudos o cubiertos únicamente por una pequeña piel de foca sobre los hombros, con el cuerpo untado en grasa de ballena para repeler el agua gélida, buceaban en aguas casi congeladas para recolectar centollas, erizos y cholgas, conviviendo en armonía absoluta con un medioambiente que a ojos occidentales parecía un infierno inhabitable.",
                "Trágicamente, la llegada de los navegantes europeos, los cazadores de focas británicos y los ganaderos decimonónicos a fines del siglo diecinueve desató el exterminio de estos pueblos ancestrales mediante epidemias mortales de sarampión y neumonía, envenenamientos deliberados y traslados forzados. Hoy en día, un puñado de descendientes kawésqar en Puerto Edén y yaganes en Puerto Williams mantienen viva la memoria de su lengua y de su sabiduría marina, luchando incansablemente para impedir que la expansión descontrolada de las concesiones de salmonicultura industrial contamine los fiordos vírgenes con antibióticos y desoxigene los fondos marinos de la Patagonia.",
                "Al contemplar el glaciar Grey al atardecer desde un mirador azotado por el viento, cuando los témpanos flotantes adquieren un fulgor azul eléctrico bajo las sombras crepusculares y el cóndor despliega sus alas gigantescas sobre el abismo de roca, el ser humano se siente reconciliado con la grandeza primordial del planeta: comprende que en estos confines australes donde la roca, el hielo y el viento imponen su ley soberana, la Patagonia permanece como el último templo sagrado de la naturaleza salvaje, recordándonos la obligación inaplazable de preservar intacta la belleza del mundo."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué reserva continental de agua dulce representa la mayor extensión de hielo en el hemisferio sur fuera de la Antártida?",
                        "options": [
                            "Los Campos de Hielo Sur, ubicados en los Andes patagónicos de Chile y Argentina.",
                            "Los manantiales termales del desierto de Atacama en el norte chileno.",
                            "La cuenca pantanosa del río de la Plata frente a las costas de Montevideo.",
                            "El lago Titicaca situado en la meseta del altiplano boliviano."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los Campos de Hielo Sur son la tercera masa de hielo continental del mundo tras la Antártida y Groenlandia."
                    },
                    {
                        "question": "¿Cómo sobrevivían los pueblos canoeros ancestrales como los Kawésqar y Yaganes en los canales gélidos?",
                        "options": [
                            "Navegando en canoas con una fogata sobre arcilla y untándose grasa animal para protegerse del agua helada.",
                            "Construyendo fortalezas de piedra con calefacción mediante calderas de vapor importadas.",
                            "Viviendo exclusivamente en cuevas subterráneas calientes alimentadas por volcanes activos.",
                            "Pernoctando en barcos de hierro comprados a los comerciantes de la ruta de la seda."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los nómadas canoeros usaban grasa protectora, canoas de corteza con fuego a bordo y gran pericia marina."
                    },
                    {
                        "question": "¿Qué amenaza ambiental contemporánea enfrentan los fiordos vírgenes de la Patagonia chilena?",
                        "options": [
                            "La expansión intensiva de la salmonicultura que contamina las aguas con residuos y químicos industriales.",
                            "La desertificación provocada por la tala masiva de palmeras tropicales en los glaciares.",
                            "La evaporación completa de los fiordos debido a olas de calor provenientes del Polo Norte.",
                            "La invasión de camellos del desierto del Sahara que devoran el bosque subpolar."
                        ],
                        "correctIndex": 0,
                        "explanation": "La salmonicultura industrial genera severo impacto ecológico por escapes, antibióticos y desoxigenación marina."
                    }
                ]
            }
        }
    }

    # Regional Story 5: Hidrógeno Verde
    story_chile_05 = {
        "id": "b2-chileextremos-05",
        "title": "La fragua del viento: Hidrógeno verde y la vanguardia energética en Magallanes",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la región de Magallanes y el estrecho homónimo: la capital austral Punta Arenas como puerta de entrada a la Antártida, los corredores eólicos más energéticos del planeta, la producción pionera de hidrógeno verde y combustibles sintéticos mediante electrólisis de agua de mar, y la geopolítica de la transición ecológica en el confín del mundo.",
        "characters": [
            "Ingeniero en energías renovables Sebastián",
            "Alcaldesa de Punta Arenas Doña Beatriz",
            "Científico antártico Pablo",
            "Técnica en electrólisis Daniela"
        ],
        "narration": {
            "paragraphs": [
                "A orillas del mítico Estrecho de Magallanes, la ruta marítima que descubrió en 1520 el navegante portugués al servicio de España uniendo por vez primera los dos grandes océanos del planeta, se levanta la ciudad de Punta Arenas: la metrópoli continental más austral de América. Con sus tejados de cinc pintados en alegres colores rojo, azul y verde para desafiar la melancolía del invierno polar, sus casonas de estilo neoclásico levantadas por los pioneros ganaderos decimonónicos de la lana y sus plazas arboladas donde la estatua de Hernando de Magallanes exhibe un dedo del pie reluciente por los besos de los viajeros que anhelan retornar, Punta Arenas ha sido históricamente una plaza fuerte de soberanía austral, faro de la navegación marítima y la puerta de entrada logística por excelencia para los programas científicos que operan en el continente blanco antártico.",
                "Sin embargo, el rasgo definitorio más constante y arrollador de esta geografía austral es el viento. En las planicies esteparias que bordean el estrecho y Tierra del Fuego, las masas de aire polar empujadas por las bajas presiones del océano austral barren el territorio de manera ininterrumpida a lo largo de todo el año, con velocidades medias que superan los treinta kilómetros por hora y ráfagas frecuentes de más de cien kilómetros por hora que obligan a tender pasamanos de cuerda en las calles céntricas de la ciudad para que los peatones no sean derribados durante los vendavales de primavera. Lo que durante siglos fue percibido como una aspereza climática implacable y hostil para la vida humana se ha transformado en el siglo veintiuno en el mayor tesoro estratégico de Chile y del planeta: un recurso eólico inagotable y de clase mundial.",
                "En efecto, los estudios meteorológicos internacionales han confirmado que el factor de planta eólico en Magallanes —es decir, la proporción de tiempo efectivo en que un aerogenerador produce energía eléctrica a máxima capacidad— supera el cincuenta y cinco por ciento, una cifra fenomenal que duplica el promedio de los mejores parques eólicos de Europa y Norteamérica. Esta potencia eólica extraordinaria ha convertido a la región en el epicentro de la revolución global del hidrógeno verde. Mediante complejos electrolizadores alimentados enteramente por la electricidad limpia de las turbinas eólicas, se descompone la molécula de agua desalinizada de mar para separar el hidrógeno del oxígeno sin emitir un solo gramo de dióxido de carbono a la atmósfera, generando un vector energético limpio de colosal densidad química.",
                "En las plantas piloto pioneras instaladas en las cercanías de Punta Arenas, este hidrógeno verde se combina con dióxido de carbono capturado directamente de la atmósfera o de procesos biogénicos para sintetizar e-combustibles: gasolinas y metanol sintéticos neutros en carbono que pueden emplearse directamente en motores de aviación comercial, barcos de carga interoceánicos y automóviles existentes sin necesidad de modificar su mecánica tradicional. De este modo, el combustible refinado con la fuerza de los vientos magallánicos promete descarbonizar los sectores del transporte pesado internacional más difíciles de electrificar mediante baterías convencionales, abriendo una ventana de esperanza tecnológica para contener el calentamiento global.",
                "No obstante, este promisorio horizonte industrial no está exento de complejos dilemas socioambientales y desafíos de ordenamiento territorial que movilizan a la ciudadanía magallánica. La instalación proyectada de miles de gigantescos aerogeneradores de más de doscientos metros de altura, con extensas líneas de transmisión eléctrica, puertos industriales y ductos en la estepa, plantea serios riesgos para las rutas migratorias de millones de aves australes, como el playero ártico, el chorlito de Magallanes y el amenazado canquén colorado. Comunidades locales, científicos antárticos y organizaciones conservacionistas exigen una rigurosa planificación territorial que proteja los ecosistemas de turberas —que capturan más carbono que los bosques tropicales— y garantice que el desarrollo del hidrógeno verde beneficie el bienestar y la diversificación educativa de los habitantes australes.",
                "Al contemplar las aspas monumentales de los aerogeneradores girando con cadencia majestuosa contra el cielo crepuscular del estrecho, mientras un buque rompehielos científico zarpa rumbo a las bases antárticas y el viento helado silba su tonada eterna, el observador experimenta una renovada fe en el ingenio humano: en el rincón más austral del planeta, allí donde las aguas del mundo se encuentran, la bravura indómita del viento patagónico está forjando el fuego limpio que iluminará un porvenir sustentable para todas las naciones de la Tierra."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué factor meteorológico excepcional convierte a la región de Magallanes en un polo privilegiado para la energía eólica?",
                        "options": [
                            "Vientos constantes e ininterrumpidos con factores de planta eólicos superiores al cincuenta y cinco por ciento.",
                            "La ausencia absoluta de viento que permite a los paneles solares capturar energía nocturna.",
                            "Lluvias de agua hirviendo provenientes de erupciones volcánicas submarinas en el estrecho.",
                            "Corrientes de aire caliente ecuatorial que elevan la temperatura a cuarenta grados en invierno."
                        ],
                        "correctIndex": 0,
                        "explanation": "El factor de planta eólico de Magallanes es de los más altos del mundo gracias a vientos potentes y constantes."
                    },
                    {
                        "question": "¿En qué consiste la síntesis de e-combustibles a partir del hidrógeno verde en las plantas patagónicas?",
                        "options": [
                            "En combinar hidrógeno verde con dióxido de carbono reciclado para crear combustibles líquidos neutros en carbono.",
                            "En mezclar agua de mar salada con petróleo pesado de importación para quemarlo en fogatas abiertas.",
                            "En triturar hojas de araucaria milenaria con carbón mineral para generar gas metano tóxico.",
                            "En evaporar el agua de los glaciares mediante reactores térmicos para producir vapor salino."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los e-combustibles combinan hidrógeno verde y CO2 para sustituir hidrocarburos fósiles sin emisiones netas."
                    },
                    {
                        "question": "¿Qué preocupación ambiental plantean las comunidades magallánicas ante la instalación masiva de parques eólicos?",
                        "options": [
                            "El impacto sobre las aves migratorias australes y la necesidad de proteger las turberas de la estepa.",
                            "El peligro de que los aerogeneradores detengan la rotación de la Tierra alrededor del Sol.",
                            "El temor a que las aspas de las turbinas atraigan maremotos gigantescos desde la Antártida.",
                            "La pérdida irreversible de la nieve en todas las pistas de esquí de la cordillera del Himalaya."
                        ],
                        "correctIndex": 0,
                        "explanation": "Se exige evaluar el impacto en aves migratorias y proteger las turberas que almacenan carbono."
                    }
                ]
            }
        }
    }

    # Regional Story 6: Capstone regional (Chile Extremo)
    story_chile_capstone = {
        "id": "b2-chileextremos-consolidation",
        "title": "De la aridez al hielo infinito: El mosaico de las geografías extremas de Chile",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis abarcadora de los Estudios Regionales sobre las geografías extremas de Chile: la hiperaridez y la ventana astronómica del desierto de Atacama, el titanismo minero del cobre en Chuquicamata, la cosmovisión y dignidad territorial del pueblo mapuche en el Wallmapu, el laberinto glaciar de las Torres del Paine y los fiordos patagónicos, y la revolución del hidrógeno verde en el estrecho de Magallanes.",
        "characters": [
            "Francisco Coloane",
            "Machi Francisca",
            "Minero Héctor",
            "Astrónoma Valentina"
        ],
        "narration": {
            "paragraphs": [
                "A lo largo de más de cuatro mil trescientos kilómetros de longitud vertical comprimidos entre las cumbres colosales de la cordillera andina y la inmensidad del océano Pacífico, el territorio de Chile encierra una de las sinfonías geográficas y humanas más asombrosas y extremas de la geografía planetaria. En este país largo y angosto, la naturaleza no se manifiesta en tonalidades intermedias ni en llanuras monótonas: estalla en contrastes absolutos que desafían los límites de la adaptación biológica y el ingenio de sus habitantes. Desde la sequedad mineral más implacable del planeta bajo los cielos transparentes del norte grande, pasando por los bosques sagrados templados del centro-sur, hasta desembocar en los campos de hielo continental y los fiordos laberínticos azotados por los vendavales antárticos del sur austral, Chile custodia un mosaico territorial único y conmovedor en el Cono Sur americano.",
                "En el extremo septentrional, el desierto de Atacama desafía la lógica de la vida con su hiperaridez absoluta, donde las lluvias pueden ausentarse durante siglos enteros merced a la barrera orográfica de los Andes y a la frialdad de la corriente marina de Humboldt. Pero esa misma sequedad extrema creó la ventana óptica y milimétrica más pura y diáfana del hemisferio sur, permitiendo que observatorios de vanguardia planetaria como ALMA y Paranal desentrañen los secretos del cosmos en un diálogo secular que entronca con la cosmovisión astronómica de los antiguos pueblos atacameños y quechuas. A pocos kilómetros de esos santuarios de la luz cósmica, el gigantesco anfiteatro de Chuquicamata y los yacimientos de cobre recuerdan que la riqueza geológica arrancada a las rocas del desierto es el sueldo que ha financiado el desarrollo republicano y social de la nación.",
                "Al descender hacia el sur fértil y lluvioso, el paisaje se transmuta en el sagrado territorio del *Wallmapu*, donde los volcanes coronados de nieve vigilan los bosques milenarios de araucarias (*pewen*) y robles nativos. Allí late la memoria inquebrantable de la nación mapuche, pueblo originario que defendió su soberanía y su libertad frente a las armas de la conquista hispana en la Guerra de Arauco y que hoy sostiene una lucha ejemplar por la recuperación de sus tierras ancestrales, la defensa de la Madre Tierra (*Ñuke Mapu*) frente al monocultivo forestal y el reconocimiento de su lengua y su cosmovisión espiritual guiada por el saber comunitario de la machi.",
                "Más al sur todavía, donde el continente se desmorona en miles de islas, fiordos y canales laberínticos, la Patagonia austral y los Campos de Hielo Sur exhiben la majestuosidad primordial de la era del hielo. En el Parque Nacional Torres del Paine, las agujas titánicas de granito esculpidas por glaciares colosales se levantan sobre estepas donde guanacos, zorros culpeos y cóndores conviven con el recuerdo imborrable de los pueblos canoeros Kawésqar y Yagán, navegantes ancestrales que desafiaban las aguas gélidas en frágiles canozas con una pequeña fogata encendida sobre lechos de barro, recordándonos la asombrosa plasticidad del ser humano en armonía con su entorno.",
                "Y en el confín austral de Magallanes y Tierra del Fuego, allí donde las tempestades del Cabo de Hornos cobraron durante siglos el tributo de sangre cantado por la prosa inmortal de Francisco Coloane, el viento impetuoso se ha transformado en el combustible limpio del mañana. A través de la producción pionera de hidrógeno verde y combustibles sintéticos limpios mediante energía eólica inagotable, la histórica región de Punta Arenas se proyecta al mundo no solo como la puerta de entrada logística a la Antártida, sino como el laboratorio de vanguardia de la descarbonización energética global.",
                "Al contemplar este mapa fascinante de aridez y ventisqueros, de minerales rojos y vientos boreales, el estudiante de la lengua española comprende la esencia más profunda del alma chilena: un temple forjado en la adversidad y la grandeza de los elementos, donde la palabra poética, el respeto a las raíces ancestrales y la audacia científica se funden en un horizonte común de dignidad, soberanía y comunión indestructible con la naturaleza."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis geográfica caracteriza a los dos extremos territoriales de Chile abordados en este estudio regional?",
                        "options": [
                            "El contraste absoluto entre la hiperaridez astronómica de Atacama al norte y el laberinto de hielo y viento de la Patagonia al sur.",
                            "La uniformidad de extensas selvas tropicales pantanosas que cubren todo el territorio de norte a sur.",
                            "La presencia exclusiva de playas caribeñas desprovistas de cordilleras y de glaciares.",
                            "Un archipiélago fluvial donde nunca sopla el viento ni se extraen minerales del subsuelo."
                        ],
                        "correctIndex": 0,
                        "explanation": "Chile extremo conjuga la aridez astronómica y minera de Atacama con los glaciares y vientos de la Patagonia."
                    },
                    {
                        "question": "¿Qué pueblo originario custodia la memoria ancestral y la defensa del bosque nativo en el centro-sur de Chile?",
                        "options": [
                            "El pueblo mapuche, cuya cosmovisión honra a la Ñuke Mapu y al pewen sagrado en el Wallmapu.",
                            "Los aztecas que construyeron pirámides ceremoniales a orillas del río Biobío.",
                            "Los incas que habitaron exclusivamente en los témpanos flotantes del Cabo de Hornos.",
                            "Los vikingos que fundaron puertos comerciales en los canales magallánicos en el siglo diez."
                        ],
                        "correctIndex": 0,
                        "explanation": "El pueblo mapuche habita ancestralmente el Wallmapu y defiende el equilibrio de la Ñuke Mapu."
                    },
                    {
                        "question": "¿De qué manera la región más austral de Magallanes proyecta su liderazgo en el siglo XXI?",
                        "options": [
                            "Liderando la transición energética limpia mediante la producción de hidrógeno verde impulsada por vientos eólicos.",
                            "Clausurando todas sus rutas marítimas para evitar el contacto con el resto de los continentes.",
                            "Dedicándose en exclusiva a la exportación de carbón fósil de alta emisión de carbono.",
                            "Prohibiendo la investigación científica internacional en las bases de la Antártida."
                        ],
                        "correctIndex": 0,
                        "explanation": "Magallanes aprovecha sus vientos superlativos para producir hidrógeno verde y energías limpias de exportación."
                    }
                ]
            }
        }
    }

    # Stitched unit story for Library
    story_chile_stitched = {
        "id": "b2-chileextremos",
        "title": "Chile II: Las geografías extremas: Atacama, Patagonia y Wallmapu",
        "level": "B2",
        "type": "world",
        "estimatedMinutes": 25,
        "summary": "Edición completa de la travesía por las geografías extremas de Chile: los cielos cristalinos y radiotelescopios del desierto de Atacama, la gran minería del cobre en Chuquicamata, la cosmovisión y resistencia del pueblo mapuche en el Wallmapu, los fiordos glaciares y las Torres del Paine, y la frontera del hidrógeno verde en el estrecho de Magallanes.",
        "characters": [
            "Astrónoma Valentina",
            "Minero Héctor",
            "Machi Francisca",
            "Navegante Amador",
            "Ingeniero Sebastián"
        ],
        "narration": {
            "paragraphs": (
                story_chile_01["narration"]["paragraphs"] +
                story_chile_02["narration"]["paragraphs"] +
                story_chile_03["narration"]["paragraphs"] +
                story_chile_04["narration"]["paragraphs"] +
                story_chile_05["narration"]["paragraphs"]
            )
        }
    }

    # Audit word counts of the 7 individual stories (must be between 650 and 825 words)
    stories_to_audit = [
        ("story_core_23", story_core_23),
        ("story_chile_01", story_chile_01),
        ("story_chile_02", story_chile_02),
        ("story_chile_03", story_chile_03),
        ("story_chile_04", story_chile_04),
        ("story_chile_05", story_chile_05),
        ("story_chile_capstone", story_chile_capstone)
    ]

    print("\n--- Story Word Count Audit ---")
    all_ok = True
    for name, s_obj in stories_to_audit:
        wc = count_words(s_obj)
        status = "OK (650-825)" if 650 <= wc <= 825 else f"FAILED ({wc} words, must be 650-825)"
        if not (650 <= wc <= 825):
            all_ok = False
        print(f"{name:<24}: {wc:4d} words -> {status}")

    # Helper to convert story dictionary into valid schema structure
    def to_schema_story(s, real_id=None):
        paras = s["narration"]["paragraphs"]
        questions = s["narration"]["pedagogical"]["comprehensionQuestions"]
        sid = real_id if real_id else s["id"]
        return {
            "id": sid,
            "title": s["title"],
            "level": s["level"],
            "lesson": s["lesson"],
            "type": s["type"],
            "estimatedMinutes": s.get("estimatedMinutes", 8),
            "summary": s["summary"],
            "characters": s["characters"],
            "paragraphs": [{"type": "narration", "text": p} for p in paras],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": questions
                }
            }
        }

    def to_stitched_schema(s):
        paras = s["narration"]["paragraphs"]
        return {
            "id": s["id"],
            "title": s["title"],
            "level": s["level"],
            "lesson": 1,
            "type": s["type"],
            "estimatedMinutes": s.get("estimatedMinutes", 25),
            "summary": s["summary"],
            "characters": s["characters"],
            "paragraphs": [{"type": "narration", "text": p} for p in paras]
        }

    # Write stories
    write_json("stories/classics/b2/b2-23.json", to_schema_story(story_core_23, "b2-23"))
    write_json("stories/world/b2/b2-chileextremos-01.json", to_schema_story(story_chile_01, "b2-chileextremos-01"))
    write_json("stories/world/b2/b2-chileextremos-02.json", to_schema_story(story_chile_02, "b2-chileextremos-02"))
    write_json("stories/world/b2/b2-chileextremos-03.json", to_schema_story(story_chile_03, "b2-chileextremos-03"))
    write_json("stories/world/b2/b2-chileextremos-04.json", to_schema_story(story_chile_04, "b2-chileextremos-04"))
    write_json("stories/world/b2/b2-chileextremos-05.json", to_schema_story(story_chile_05, "b2-chileextremos-05"))
    write_json("stories/world/b2/b2-chileextremos-consolidation.json", to_schema_story(story_chile_capstone, "b2-chileextremos-consolidation"))
    write_json("stories/world/b2/b2-chileextremos.json", to_stitched_schema(story_chile_stitched))

    # 7. Lessons Files (12 files)
    core_lessons_info = [
        ("b2-23-01", "lesson.b2.23.01", "Perífrasis inceptivas: Echarse a",
         "Dominar el uso de la perífrasis 'echarse a + infinitivo' para expresar el inicio súbito e impulsivo de emociones intensas o movimientos corporales.",
         "perífrasis inceptivas con echarse a y reacciones súbitas involuntarias",
         ["Identificar el valor aspectual inceptivo e involuntario de echarse a.",
          "Diferenciar echarse a de ponerse a según la deliberación del sujeto.",
          "Aplicar la construcción en narraciones dramáticas y testimonios orales."]),
        ("b2-23-02", "lesson.b2.23.02", "Perífrasis inceptivas: Ponerse a",
         "Utilizar con precisión la perífrasis 'ponerse a + infinitivo' para describir la iniciación consciente, voluntaria y dedicada de labores, tareas y estudios.",
         "perífrasis inceptivas con ponerse a y disposición voluntaria del sujeto",
         ["Comprender el matiz de esfuerzo y compromiso activo inherente a ponerse a.",
          "Distinguir el uso meteorológico de ponerse a en tercera persona.",
          "Emplear la estructura en informes técnicos y crónicas profesionales."]),
        ("b2-23-03", "lesson.b2.23.03", "Perífrasis inceptivas: Romper a",
         "Aprender el empleo estético y dramático de 'romper a + infinitivo' para expresar la eclosión ruidosa y repentina de sonidos, emociones contenidas o fenómenos climáticos.",
         "perífrasis inceptivas con romper a y quiebre de tensión o silencio",
         ["Reconocer los verbos de sonido, clima y ebullición que seleccionan romper a.",
          "Apreciar la carga de fractura de silencio y emoción acumulada en el relato.",
          "Incorporar romper a en la prosa literaria y periodística culta."]),
        ("b2-23-04", "lesson.b2.23.04", "Perífrasis iterativas: Volver a",
         "Dominar la perífrasis 'volver a + infinitivo' para denotar repetición, reanudación y compromisos de cese definitivo en enunciados negativos.",
         "perífrasis iterativas con volver a y reanudación o cese reiterativo",
         ["Articular la reiteración de acciones en diversos tiempos y modos verbales.",
          "Manejar la fuerza prohibitiva o resolutiva de no volver a + infinitivo.",
          "Comparar volver a con adverbios de repetición en el ensayo formal."]),
        ("b2-23-05", "lesson.b2.23.05", "Perífrasis secuenciales: Pasar a",
         "Utilizar 'pasar a + infinitivo' como marcador de transición discursiva y progresión metódica en exposiciones formales, actas e informes técnicos.",
         "perífrasis secuenciales con pasar a y estructuración discursiva formal",
         ["Estructurar presentaciones orales y ensayos mediante transiciones ordenadas.",
          "Describir cambios de funciones y ascensos en biografías profesionales.",
          "Garantizar la cohesión secuencial entre apartados temáticos."])
    ]

    for s, lid, tit, gol, gmr, items in core_lessons_info:
        write_json(f"lessons/b2/{s}.json", {
            "id": lid, "title": tit, "level": "B2", "goal": gol, "grammar": gmr,
            "sections": [
                {"type": "goal", "items": items},
                {"type": "recycle", "count": 3},
                {"type": "grammar", "ref": f"grammar/b2/{s}-a-gr.json"},
                {"type": "vocabulary", "ref": f"vocabulary/b2/{s}-voc.json"},
                {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex01", f"{s}.ex02", f"{s}.ex03", f"{s}.ex04"]},
                {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex05"]},
                {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex06"]}
            ]
        })

    # Core Consolidation Lesson
    write_json("lessons/b2/b2-23-consolidation.json", {
        "id": "lesson.b2.23.consolidation",
        "title": "Consolidación B2: Perífrasis aspectuales y Cabo de Hornos de Francisco Coloane",
        "level": "B2",
        "goal": "Sintetizar el dominio de las perífrasis aspectuales de inicio, esfuerzo, estallido, repetición y transición a través de Francisco Coloane.",
        "grammar": "síntesis del paradigma de perífrasis aspectuales y adaptación de Cabo de Hornos",
        "sections": [
            {"type": "goal", "items": [
                "Integrar con flexibilidad echarse a, ponerse a, romper a, volver a y pasar a.",
                "Reconocer las sutiles fronteras semánticas entre espontaneidad y deliberación.",
                "Consolidar el léxico de esfuerzo, persistencia y dinamismo narrativo austral."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/classics/b2/b2-23.json"},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-23-consolidation-ex.json", "exerciseRefs": [f"b2-23-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Distingo entre impulsos involuntarios (echarse a) e inicios deliberados (ponerse a).",
                "Domino el uso de romper a para describir quiebres sonoros y fenómenos meteorológicos.",
                "Utilizo volver a con enunciados negativos para formular resoluciones firmes de cese.",
                "Aplico pasar a para jerarquizar temas y ordenar la transición en el discurso formal.",
                "Aprecio la estética marina y el dramatismo humano en la narrativa de Francisco Coloane."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-chileextremos-01", "lesson.b2.chileextremos.01", "El desierto de Atacama: Cielos cristalinos y observatorios espaciales",
         "Explorar la geografía hiperárida de Atacama, los observatorios de astronomía de frontera como ALMA y el diálogo milenario con las cosmovisiones andinas.",
         "geografía hiperárida de Atacama, astronomía observacional y adjetivación relacional",
         ["Comprender los factores orográficos que producen la sequedad extrema atacameña.",
          "Describir el funcionamiento del radiotelescopio ALMA en el llano de Chajnantor.",
          "Analizar la lectura ancestral del firmamento por las comunidades licanantay."]),
        ("b2-chileextremos-02", "lesson.b2.chileextremos.02", "El cobre y la gran minería en Chuquicamata y Escondida",
         "Analizar la ingeniería monumental de la minería del cobre, su impacto socioeconómico en Chile y los retos ecológicos de la desalinización.",
         "ingeniería minera a rajo abierto, economía del cobre y nominalizaciones técnicas",
         ["Describir las dimensiones ciclópeas del rajo de Chuquicamata y la minería subterránea.",
          "Comprender la significación histórica de la nacionalización del cobre de 1971.",
          "Examinar los procesos metalúrgicos de lixiviación, flotación y electroobtención."]),
        ("b2-chileextremos-03", "lesson.b2.chileextremos.03", "El pueblo mapuche y la defensa del Wallmapu",
         "Conocer la historia de resistencia del pueblo mapuche, su cosmovisión arraigada a la Ñuke Mapu y sus demandas contemporáneas de autonomía y plurinacionalidad.",
         "historiografía mapuche, cosmovisión comunitaria y soberanía territorial en el Wallmapu",
         ["Analizar la frontera histórica del río Biobío fijada en los parlamentos coloniales.",
          "Comprender el rol espiritual y medicinal de la machi y el árbol sagrado pewen.",
          "Debatir sobre la restitución territorial y la preservación de los bosques nativos."]),
        ("b2-chileextremos-04", "lesson.b2.chileextremos.04", "Los canales patagónicos y las Torres del Paine",
         "Explorar los fiordos glaciares de la Patagonia austral, las formaciones geológicas de Torres del Paine y la milenaria adaptación de los pueblos canoeros.",
         "morfología glaciar patagónica, ecosistemas subpolares y memoria de los pueblos canoeros",
         ["Identificar la magnitud ecológica de los Campos de Hielo Sur y los fiordos patagónicos.",
          "Describir la flora y fauna del bosque subpolar magallánico de lengas y coigües.",
          "Honrar la memoria y la navegación de los pueblos originarios Kawésqar y Yagán."]),
        ("b2-chileextremos-05", "lesson.b2.chileextremos.05", "La revolución del hidrógeno verde y la transición energética austral",
         "Examinar el potencial eólico de Magallanes, la producción de hidrógeno verde por electrólisis y el rol de Punta Arenas como polo antártico y sustentable.",
         "energía eólica austral, electrólisis del hidrógeno verde y oraciones causales de prospectiva",
         ["Comprender la ventaja de los factores de planta eólicos superiores al 55% en Magallanes.",
          "Analizar la síntesis de e-combustibles neutros en carbono para el transporte pesado.",
          "Debatir sobre la coexistencia armónica entre parques eólicos y fauna migratoria."])
    ]

    for s, lid, tit, gol, gmr, items in reg_lessons_info:
        write_json(f"lessons/b2/{s}.json", {
            "id": lid, "title": tit, "level": "B2", "goal": gol, "grammar": gmr,
            "sections": [
                {"type": "goal", "items": items},
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": f"stories/world/b2/{s}.json"},
                {"type": "grammar", "ref": f"grammar/b2/{s}-a-gr.json"},
                {"type": "vocabulary", "ref": f"vocabulary/b2/{s}-voc.json"},
                {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex01", f"{s}.ex02", f"{s}.ex03", f"{s}.ex04"]},
                {"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex05"]},
                {"type": "exercise-group", "title": "Listening", "ref": f"exercises/b2/{s}-ex.json", "exerciseRefs": [f"{s}.ex06"]}
            ]
        })

    # Regional Consolidation Lesson
    write_json("lessons/b2/b2-chileextremos-consolidation.json", {
        "id": "lesson.b2.chileextremos.consolidation",
        "title": "Consolidación: De la aridez al hielo infinito",
        "level": "B2",
        "goal": "Sintetizar los aprendizajes sobre las geografías extremas de Chile: desde la aridez astronómica y minera de Atacama hasta los glaciares y vientos de Magallanes.",
        "grammar": "síntesis regional de las geografías extremas de Chile: de Atacama a la Patagonia austral",
        "sections": [
            {"type": "goal", "items": [
                "Integrar el conocimiento físico, histórico y cultural de los territorios extremos chilenos.",
                "Consolidar el léxico especializado de astronomía, minería, glaciología y ecología.",
                "Articular visiones críticas sobre la soberanía territorial y el porvenir energético."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b2/b2-chileextremos-consolidation.json"},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-chileextremos-consolidation-ex.json", "exerciseRefs": [f"b2-chileextremos-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo los contrastes geográficos entre el desierto de Atacama y los fiordos patagónicos.",
                "Reconozco los aportes de la cosmovisión mapuche al debate ambiental y plurinacional.",
                "Puedo explicar el funcionamiento del hidrógeno verde y la minería sustentable en Chile.",
                "Domino el vocabulario técnico de la astronomía, la ingeniería del cobre y la glaciología austral.",
                "Valoro la dignidad humana y ecológica de las comunidades que habitan los confines del Cono Sur."
            ]}
        ]
    })

    print("Completed LatAm Unit 23 (Chile Extremos) generation!")

    # 8. Update curriculum/units/b2.json
    def update_b2_units(units):
        existing_stems = set()
        for u in units:
            for s in u.get("stems", []):
                existing_stems.add(s)

        unit_core_23 = {
            "title": "Inceptive & Iterative Periphrases",
            "stems": [
                "b2-23-01",
                "b2-23-02",
                "b2-23-03",
                "b2-23-04",
                "b2-23-05",
                "b2-23-consolidation"
            ],
            "track": "core"
        }

        unit_regional_23 = {
            "title": "Chile II: The Extreme Geographies: Atacama, Patagonia & Mapuche Wallmapu",
            "stems": [
                "b2-chileextremos-01",
                "b2-chileextremos-02",
                "b2-chileextremos-03",
                "b2-chileextremos-04",
                "b2-chileextremos-05",
                "b2-chileextremos-consolidation"
            ],
            "track": "regional"
        }

        if "b2-23-01" not in existing_stems:
            units.append(unit_core_23)
        if "b2-chileextremos-01" not in existing_stems:
            units.append(unit_regional_23)
        return units

    update_json_file(os.path.join(LATAM_DIR, "curriculum", "units", "b2.json"), update_b2_units)
    print("Updated curriculum/units/b2.json with Unit 23!")

    assert all_ok, "Some stories are out of the 650-825 word count bounds!"

if __name__ == "__main__":
    main()
