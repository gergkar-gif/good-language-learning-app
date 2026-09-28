"""Generate Latin American Spanish (es-latam) B2 Unit 25:
Core Unit 25: b2-25 (Terminative & Resultative Periphrases)
Regional Unit 25: b2-argentinaregiones (Argentina II: The Pampas, Patagonia & Regional Terroirs)
Classic Literature: Ricardo Güiraldes - Don Segundo Sombra: La iniciación en las pampas y el adiós al resero (1926)
"""

import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATAM_DIR = os.path.join(BASE_DIR, "content", "es-latam")

def count_words(story_obj):
    paras = story_obj.get("paragraphs", [])
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
            "perifrasis-llegar-a-infinitivo": {
                "kind": "grammar",
                "name": "perifrasis-llegar-a-infinitivo",
                "description": "Culminative periphrasis llegar a + infinitive expressing attainment of a milestone, extreme limit, or gradual realization",
                "aliases": []
            },
            "perifrasis-dar-por-participio": {
                "kind": "grammar",
                "name": "perifrasis-dar-por-participio",
                "description": "Resultative periphrasis dar por + participle/adjective expressing definitive judgment, presupposition, or settled closure",
                "aliases": []
            },
            "b2-25-vocab": {
                "kind": "vocabulary",
                "name": "b2-25-vocab",
                "description": "Vocabulary for terminative and resultative periphrases, completion, outcomes, and transitions",
                "aliases": []
            },
            "concesivas-si-bien": {
                "kind": "grammar",
                "name": "concesivas-si-bien",
                "description": "Formal concessive clauses introduced by si bien requiring the indicative mood",
                "aliases": []
            },
            "concesivas-aun-cuando": {
                "kind": "grammar",
                "name": "concesivas-aun-cuando",
                "description": "Concessive clauses with aun cuando selecting indicative or subjunctive based on informational status and hypothesis",
                "aliases": []
            },
            "conectores-concesivos-adversativos": {
                "kind": "grammar",
                "name": "conectores-concesivos-adversativos",
                "description": "Discourse markers of concession and contrast (no obstante, si bien es cierto que, aun así) in geographical and cultural prose",
                "aliases": []
            },
            "concesivas-pese-a": {
                "kind": "grammar",
                "name": "concesivas-pese-a",
                "description": "Prepositional concessive structures with pese a followed by nouns or infinitives",
                "aliases": []
            },
            "concesivas-por-adj-que": {
                "kind": "grammar",
                "name": "concesivas-por-adj-que",
                "description": "Intensive concessive scalar constructions with por + adjective/adverb + que + subjunctive",
                "aliases": []
            },
            "b2-argentinaregiones-vocab": {
                "kind": "vocabulary",
                "name": "b2-argentinaregiones-vocab",
                "description": "Vocabulary for Argentine regional geography, pampas, viticulture, Andean northwest, and Patagonian frontier",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            if k not in skills:
                skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 25")

    # 2. Update grammar-titles.json (all lowercase words, <= 11 words, plain CEFR English, fits after 'We recommend practicing ')
    def update_grammar_titles(titles):
        new_titles = {
            "perifrasis-llegar-a-infinitivo": "culminative periphrases with llegar a plus infinitive",
            "perifrasis-dar-por-participio": "resultative periphrases with dar por plus participle",
            "concesivas-si-bien": "formal concessive clauses with si bien and the indicative",
            "concesivas-aun-cuando": "concessive clauses with aun cuando and the subjunctive",
            "conectores-concesivos-adversativos": "concessive and adversative connectors in geographical discourse",
            "concesivas-pese-a": "prepositional concessive structures with pese a and infinitive",
            "concesivas-por-adj-que": "intensive concessive structures with por plus adjective plus que"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 25")

    # 3. Vocabulary Files (10 files)
    vocab_data = {
        "b2-25-01": {
            "id": "vocab.b2.25.01",
            "lesson": "b2-25-01",
            "title": "Terminative Periphrasis: Dejar de + Infinitivo",
            "words": [
                {"lemma": "cese", "translation": "cessation / stopping", "pos": "noun"},
                {"lemma": "interrupción", "translation": "interruption / pause", "pos": "noun"},
                {"lemma": "desistimiento", "translation": "relinquishment / withdrawal", "pos": "noun"},
                {"lemma": "renuncia", "translation": "resignation / giving up", "pos": "noun"},
                {"lemma": "desapego", "translation": "detachment / letting go", "pos": "noun"},
                {"lemma": "abandono", "translation": "abandonment / giving up", "pos": "noun"},
                {"lemma": "ruptura", "translation": "rupture / severance", "pos": "noun"},
                {"lemma": "pausa", "translation": "pause / hiatus", "pos": "noun"},
                {"lemma": "claudicación", "translation": "giving in / capitulation", "pos": "noun"},
                {"lemma": "freno", "translation": "brake / curb / restraint", "pos": "noun"}
            ]
        },
        "b2-25-02": {
            "id": "vocab.b2.25.02",
            "lesson": "b2-25-02",
            "title": "Periphrases of Completion: Acabar de vs. Acabar por",
            "words": [
                {"lemma": "culminación", "translation": "culmination / completion", "pos": "noun"},
                {"lemma": "remate", "translation": "finishing touch / conclusion", "pos": "noun"},
                {"lemma": "desenlace", "translation": "outcome / unraveling", "pos": "noun"},
                {"lemma": "desembocadura", "translation": "mouth / outlet / eventual ending", "pos": "noun"},
                {"lemma": "reciente", "translation": "recent / newly done", "pos": "adjective"},
                {"lemma": "resolución", "translation": "resolution / determination", "pos": "noun"},
                {"lemma": "finiquito", "translation": "settlement / definitive ending", "pos": "noun"},
                {"lemma": "postrimería", "translation": "latter days / final phase", "pos": "noun"},
                {"lemma": "consumación", "translation": "consummation / fulfillment", "pos": "noun"},
                {"lemma": "epílogo", "translation": "epilogue / closing event", "pos": "noun"}
            ]
        },
        "b2-25-03": {
            "id": "vocab.b2.25.03",
            "lesson": "b2-25-03",
            "title": "Eventual Culmination: Terminar por + Infinitivo & Terminar + Gerundio",
            "words": [
                {"lemma": "resignación", "translation": "resignation / acceptance", "pos": "noun"},
                {"lemma": "inevitabilidad", "translation": "inevitability", "pos": "noun"},
                {"lemma": "desfecho", "translation": "final outcome / resolution", "pos": "noun"},
                {"lemma": "decantación", "translation": "gradual settling / clarifying", "pos": "noun"},
                {"lemma": "corolario", "translation": "corollary / natural result", "pos": "noun"},
                {"lemma": "secuela", "translation": "aftermath / sequel", "pos": "noun"},
                {"lemma": "saldo", "translation": "balance / net outcome", "pos": "noun"},
                {"lemma": "derivación", "translation": "derivation / offshoot", "pos": "noun"},
                {"lemma": "desahogo", "translation": "relief / emotional release", "pos": "noun"},
                {"lemma": "fatalidad", "translation": "fatality / unavoidable destiny", "pos": "noun"}
            ]
        },
        "b2-25-04": {
            "id": "vocab.b2.25.04",
            "lesson": "b2-25-04",
            "title": "Attainment & Extremes: Llegar a + Infinitivo",
            "words": [
                {"lemma": "hito", "translation": "milestone / landmark", "pos": "noun"},
                {"lemma": "apogeo", "translation": "apogee / height / peak", "pos": "noun"},
                {"lemma": "consagración", "translation": "consecration / ultimate recognition", "pos": "noun"},
                {"lemma": "alcance", "translation": "reach / scope / achievement", "pos": "noun"},
                {"lemma": "cumbre", "translation": "summit / pinnacle", "pos": "noun"},
                {"lemma": "maduración", "translation": "maturation / ripening", "pos": "noun"},
                {"lemma": "culmen", "translation": "culmination / highest point", "pos": "noun"},
                {"lemma": "trascendencia", "translation": "transcendence / profound significance", "pos": "noun"},
                {"lemma": "plenitud", "translation": "fullness / peak state", "pos": "noun"},
                {"lemma": "consecución", "translation": "attainment / achievement", "pos": "noun"}
            ]
        },
        "b2-25-05": {
            "id": "vocab.b2.25.05",
            "lesson": "b2-25-05",
            "title": "Resultative Judgments: Dar por + Participio",
            "words": [
                {"lemma": "presuposición", "translation": "presupposition / assumption", "pos": "noun"},
                {"lemma": "clausura", "translation": "closure / definitive shutting", "pos": "noun"},
                {"lemma": "estipulación", "translation": "stipulation / contractual term", "pos": "noun"},
                {"lemma": "asentimiento", "translation": "assent / agreement", "pos": "noun"},
                {"lemma": "veredicto", "translation": "verdict / formal ruling", "pos": "noun"},
                {"lemma": "liquidación", "translation": "settlement / liquidation", "pos": "noun"},
                {"lemma": "desestimación", "translation": "dismissal / rejection", "pos": "noun"},
                {"lemma": "constatación", "translation": "verification / factual confirmation", "pos": "noun"},
                {"lemma": "firmeza", "translation": "firmness / finality (legal)", "pos": "noun"},
                {"lemma": "conclusión", "translation": "conclusion / ending", "pos": "noun"}
            ]
        },
        "b2-argentinaregiones-01": {
            "id": "vocab.b2.argentinaregiones.01",
            "lesson": "b2-argentinaregiones-01",
            "title": "The Pampas & the Gaucho Heritage",
            "words": [
                {"lemma": "llanura", "translation": "plain / flat grassland", "pos": "noun"},
                {"lemma": "pampa", "translation": "pampas / fertile southern plain", "pos": "noun"},
                {"lemma": "gaucho", "translation": "gaucho / rural horseman", "pos": "noun"},
                {"lemma": "estancia", "translation": "cattle ranch / rural estate", "pos": "noun"},
                {"lemma": "arreo", "translation": "cattle drive / herding", "pos": "noun"},
                {"lemma": "doma", "translation": "horse breaking / taming", "pos": "noun"},
                {"lemma": "pajonal", "translation": "reedbed / tall grass field", "pos": "noun"},
                {"lemma": "facón", "translation": "gaucho dagger / long knife", "pos": "noun"},
                {"lemma": "payada", "translation": "improvised sung poetic duel", "pos": "noun"},
                {"lemma": "pastizal", "translation": "pasture / grazing land", "pos": "noun"}
            ]
        },
        "b2-argentinaregiones-02": {
            "id": "vocab.b2.argentinaregiones.02",
            "lesson": "b2-argentinaregiones-02",
            "title": "Mendoza: High-Altitude Oasis & Malbec Viticulture",
            "words": [
                {"lemma": "oasis", "translation": "oasis / irrigated fertile valley", "pos": "noun"},
                {"lemma": "vitivinicultura", "translation": "winemaking / viticulture", "pos": "noun"},
                {"lemma": "acequia", "translation": "irrigation ditch / canal", "pos": "noun"},
                {"lemma": "terruño", "translation": "terroir / native soil", "pos": "noun"},
                {"lemma": "cepa", "translation": "grape variety / vine stock", "pos": "noun"},
                {"lemma": "vendimia", "translation": "grape harvest festival", "pos": "noun"},
                {"lemma": "deshielo", "translation": "snowmelt / thaw", "pos": "noun"},
                {"lemma": "bodega", "translation": "winery / wine cellar", "pos": "noun"},
                {"lemma": "cuyo", "translation": "Cuyo (western Andean region)", "pos": "noun"},
                {"lemma": "aridez", "translation": "dryness / aridity", "pos": "noun"}
            ]
        },
        "b2-argentinaregiones-03": {
            "id": "vocab.b2.argentinaregiones.03",
            "lesson": "b2-argentinaregiones-03",
            "title": "Quebrada de Humahuaca & the Calchaquí Valleys",
            "words": [
                {"lemma": "quebrada", "translation": "ravine / narrow valley canyon", "pos": "noun"},
                {"lemma": "pucará", "translation": "pre-Columbian stone fortress", "pos": "noun"},
                {"lemma": "adobe", "translation": "sun-dried mud brick", "pos": "noun"},
                {"lemma": "sincretismo", "translation": "religious and cultural syncretism", "pos": "noun"},
                {"lemma": "pachamama", "translation": "Mother Earth (Andean deity)", "pos": "noun"},
                {"lemma": "cardón", "translation": "giant columnar cactus", "pos": "noun"},
                {"lemma": "copla", "translation": "traditional folk verse / ballad", "pos": "noun"},
                {"lemma": "altiplano", "translation": "high plateau", "pos": "noun"},
                {"lemma": "estratigrafía", "translation": "rock layer stratification", "pos": "noun"},
                {"lemma": "veneración", "translation": "veneration / sacred reverence", "pos": "noun"}
            ]
        },
        "b2-argentinaregiones-04": {
            "id": "vocab.b2.argentinaregiones.04",
            "lesson": "b2-argentinaregiones-04",
            "title": "Southern Patagonia: Glaciers & Welsh Colonists",
            "words": [
                {"lemma": "ventisquero", "translation": "snowfield / mountain glacier", "pos": "noun"},
                {"lemma": "glaciar", "translation": "glacier", "pos": "noun"},
                {"lemma": "estepa", "translation": "arid cold steppe", "pos": "noun"},
                {"lemma": "desprendimiento", "translation": "calving / ice detachment", "pos": "noun"},
                {"lemma": "colono", "translation": "settler / pioneer", "pos": "noun"},
                {"lemma": "desolación", "translation": "solitude / bleak expanse", "pos": "noun"},
                {"lemma": "meseta", "translation": "high windswept plateau", "pos": "noun"},
                {"lemma": "témpano", "translation": "iceberg / ice floe", "pos": "noun"},
                {"lemma": "ovino", "translation": "sheep / ovine livestock", "pos": "adjective"},
                {"lemma": "pionero", "translation": "pioneer / trail-blazer", "pos": "noun"}
            ]
        },
        "b2-argentinaregiones-05": {
            "id": "vocab.b2.argentinaregiones.05",
            "lesson": "b2-argentinaregiones-05",
            "title": "Tierra del Fuego & Ushuaia: The End of the World",
            "words": [
                {"lemma": "austral", "translation": "southern / southernmost", "pos": "adjective"},
                {"lemma": "turbera", "translation": "peat bog", "pos": "noun"},
                {"lemma": "canal", "translation": "strait / maritime channel", "pos": "noun"},
                {"lemma": "presidio", "translation": "penal colony / prison", "pos": "noun"},
                {"lemma": "antártico", "translation": "antarctic", "pos": "adjective"},
                {"lemma": "etnocidio", "translation": "ethnocide / cultural extermination", "pos": "noun"},
                {"lemma": "estrecho", "translation": "strait / narrow sea pass", "pos": "noun"},
                {"lemma": "borrasca", "translation": "subpolar storm / tempest", "pos": "noun"},
                {"lemma": "confín", "translation": "far border / outer edge", "pos": "noun"},
                {"lemma": "recalada", "translation": "port call / landfall", "pos": "noun"}
            ]
        }
    }

    for voc_stem, voc_obj in vocab_data.items():
        write_json(f"vocabulary/b2/{voc_stem}-voc.json", voc_obj)

    # 4. Grammar Files (10 files) - Valid grammar.schema.json format
    grammar_data = {
        "b2-25-01-a": {
            "id": "grammar.b2.25.01.dejar-de",
            "title": "Perífrasis terminativas: Dejar de + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis aspectual *dejar de + infinitivo* señala la cesación, interrupción o abandono voluntario de una acción previa o de un hábito arraigado. En contraste con *parar de* (que suele denotar una pausa momentánea o física), *dejar de* suele proyectarse sobre la descontinuación duradera de una conducta o estado. En contextos negativos (*no dejar de + infinitivo*), adquiere un valor ponderativo de persistencia enfática o recomendación encarecida."
                },
                {
                    "type": "table",
                    "title": "Usos y contrastes de Dejar de + infinitivo",
                    "rows": [
                        ["Al escuchar los relatos del viejo capataz, el muchacho dejó de contemplar la ciudad como su único porvenir.", "Upon hearing the old foreman's tales, the young man stopped regarding the city as his only future."],
                        ["Los pobladores de la estancia no dejaron de admirar la serenidad estoica de Don Segundo.", "The ranch dwellers did not cease to admire Don Segundo's stoic serenity."],
                        ["Tras semanas de lluvia incesante en los bañados, el arroyo pampeano dejó de amenazar las empalizadas.", "After weeks of relentless rain in the marshes, the pampas stream stopped threatening the fences."],
                        ["No dejen de avisarnos apenas el arreo cruce el vado del río Areco.", "Do not fail to let us know as soon as the cattle drive crosses the Areco river ford."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda que la combinación negativa *no dejar de + infinitivo* es muy frecuente en cartas y discursos formales para formular recomendaciones apremiantes: *No deje de consultar las fuentes notariales antes de emitir el veredicto*."
                }
            ]
        },
        "b2-25-02-a": {
            "id": "grammar.b2.25.02.acabar-de-por",
            "title": "Perífrasis de término: Acabar de vs. Acabar por + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "El verbo auxiliar *acabar* participa en dos perífrasis aspectuales de significado claramente diferenciado. *Acabar de + infinitivo* expresa pasado inmediato retrospectivo: ubica la finalización de un proceso en un instante apenas anterior al momento de referencia (*acaba de llegar* = hace un instante que llegó). Por su parte, *acabar por + infinitivo* enfatiza la resolución final o el desenlace forzoso alcanzado tras demoras, obstáculos o vacilaciones (*acabó por aceptar el acuerdo*)."
                },
                {
                    "type": "table",
                    "title": "Contraste entre Acabar de y Acabar por",
                    "rows": [
                        ["El mensajero acaba de desmontar frente a la pulpería trayendo noticias urgentes.", "The courier horseman has just dismounted in front of the tavern bringing urgent news."],
                        ["Después de resistirse toda la tarde, el potro chúcaro acabó por obedecer las riendas.", "After resisting all afternoon, the wild colt finally obeyed the reins."],
                        ["Hacía frío en la madrugada y el fogón acababa de apagarse cuando ensillaron los fletes.", "It was cold at dawn and the fire had just gone out when they saddled the horses."],
                        ["Los estancieros acabaron por acordar una tarifa común tras arduas deliberaciones.", "The ranch owners finally agreed on a common rate after arduous deliberations."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Evita combinar *acabar de + infinitivo* en valor de pasado inmediato con complementos temporales lejanos (*acabó de llegar hace cinco años* es agramatical; se debe usar el pretérito simple *llegó hace cinco años*)."
                }
            ]
        },
        "b2-25-03-a": {
            "id": "grammar.b2.25.03.terminar-por-gerundio",
            "title": "Desenlace gradual: Terminar por + infinitivo y Terminar + gerundio",
            "sections": [
                {
                    "type": "text",
                    "content": "Tanto *terminar por + infinitivo* como *terminar + gerundio* expresan la fase conclusiva de una serie de acontecimientos prolongados, con frecuencia subrayando un corolario imprevisto o sobrevenido a regañadientes. Mientras *terminar por + infinitivo* focaliza la decisión o el hecho resolutivo final (*terminó por comprender*), *terminar + gerundio* resalta el estado o la actividad en que devino el sujeto (*terminó viviendo en la soledad de los médanos*)."
                },
                {
                    "type": "table",
                    "title": "Construcciones de culminación con Terminar",
                    "rows": [
                        ["Agotado por la travesía, el jinete terminó por dormirse sobre el lomo de su caballo.", "Exhausted by the journey, the horseman finally fell asleep on the back of his horse."],
                        ["Aquel peón rebelde terminó convirtiéndose en el capataz más respetado de la comarca.", "That rebellious farmhand ended up becoming the most respected foreman in the region."],
                        ["Las tensiones entre los puesteros terminaron resolviéndose mediante el diálogo campero.", "The tensions among the outstation workers ended up being resolved through rural dialogue."],
                        ["Si continúas cabalgando de noche por el pantano, terminarás perdiendo el sendero.", "If you keep riding at night through the marsh, you will end up losing the path."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En muchos contextos narrativos, *terminar por + infinitivo* y *acabar por + infinitivo* son prácticamente equivalentes en su valor de resolución tras resistencia o dilación."
                }
            ]
        },
        "b2-25-04-a": {
            "id": "grammar.b2.25.04.llegar-a-infinitivo",
            "title": "Alcance de hitos: Llegar a + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis aspectual *llegar a + infinitivo* expresa la consecución o alcance de un límite máximo, un hito culminante o un resultado extraordinario obtenido tras un proceso gradual de desarrollo (*llegó a ser el maestro indiscutido*). En oraciones condicionales o hipotéticas, adopta un valor eventual ponderativo que evalúa la posibilidad remota de que un hecho insólito ocurra en la realidad (*si llega a suceder, actuaremos de inmediato*)."
                },
                {
                    "type": "table",
                    "title": "Valores de Llegar a + infinitivo",
                    "rows": [
                        ["Con paciencia y rigor espartano, Fabio llegó a dominar el difícil oficio de resero.", "With patience and Spartan rigor, Fabio came to master the difficult craft of cattle drover."],
                        ["Nadie en el pueblo imaginaba que aquel muchacho huérfano llegaría a heredar las ricas tierras.", "Nobody in town imagined that that orphaned boy would come to inherit the rich lands."],
                        ["Si la helada pampeana llega a extenderse hasta el amanecer, peligrarán los sembradíos.", "If the pampas frost happens to extend until dawn, the early crops will be endangered."],
                        ["La novela gauchesca de Güiraldes llegó a consagrarse como una obra maestra continental.", "Güiraldes's gauchesque novel came to be consecrated as a continental masterpiece."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En construcciones enfáticas, *llegar a + infinitivo* puede ponderar extremos de conducta insólita: *En su enojo desmedido, llegó a negarle el saludo* ('In his excessive anger, he even went so far as to deny him a greeting')."
                }
            ]
        },
        "b2-25-05-a": {
            "id": "grammar.b2.25.05.dar-por-participio",
            "title": "Juicios resultativos: Dar por + participio / adjetivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La construcción *dar por + participio* (o adjetivo) es una perífrasis resultativa de actitud epistémica en la que el sujeto considera una situación definitivamente zanjada, concluida o asumida. El participio o adjetivo concuerda obligatoriamente en género y número con el complemento directo. Entre las colocaciones de nivel B2 más arraigadas figuran *dar por sentado* (asumir como obvio), *dar por hecho* (dar por seguro por anticipado), *dar por concluido* (clausurar un procedimiento) y *dar por perdido* (asumir la pérdida irreparable)."
                },
                {
                    "type": "table",
                    "title": "Colocaciones clave con Dar por",
                    "rows": [
                        ["El juez de paz dio por concluido el inventario judicial tras revisar las escrituras.", "The justice of the peace considered the judicial inventory concluded after reviewing the deeds."],
                        ["No des por sentado que el viaje por la Patagonia austral estará exento de contratiempos.", "Do not take for granted that the trip through southern Patagonia will be free of setbacks."],
                        ["Tras días de rastreo en el monte, los gauchos dieron por perdidas las terneras.", "After days of tracking in the scrubland, the gauchos considered the calves lost."],
                        ["El capataz dio por superada la emergencia en cuanto el terraplén contuvo el arroyo.", "The foreman considered the emergency over as soon as the embankment held back the creek."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Ten presente la concordancia de género y número: *dio por terminadas las negociaciones* (femenino plural), *dio por cancelado el contrato* (masculino singular)."
                }
            ]
        },
        "b2-argentinaregiones-01-a": {
            "id": "grammar.b2.argentinaregiones.01.concesivas-si-bien",
            "title": "Concesión formal: Si bien + indicativo",
            "sections": [
                {
                    "type": "text",
                    "content": "El nexo concesivo culto *si bien* introduce una objeción o contraargumento plenamente constatado en el plano de la realidad objetiva, por lo que rige obligatoriamente el modo indicativo en español formal. A diferencia de *aunque* (que oscila entre indicativo y subjuntivo según la factualidad del obstáculo), *si bien* valida el dato como un hecho verificado para inmediatamente contraponer una afirmación de mayor peso argumentativo en la cláusula principal."
                },
                {
                    "type": "table",
                    "title": "Estructuras con Si bien en prosa ensayística",
                    "rows": [
                        ["Si bien la modernización agropecuaria transformó el paisaje pampeano, el culto al mate sigue intacto.", "Although agricultural modernization transformed the pampas landscape, the mate ritual remains intact."],
                        ["El Martín Fierro es un poema de protesta, si bien las élites lo canonizaron como epopeya nacional.", "Martín Fierro is a protest poem, although the elites canonized it as a national epic."],
                        ["Si bien los inviernos en la llanura suelen ser ventosos y crudos, el suelo conserva gran fertilidad.", "Although winters on the plain are usually windy and harsh, the soil retains great fertility."],
                        ["Los alambrados terminaron con el nomadismo gaucho, si bien la memoria del jinete libre perdura.", "Wire fences put an end to gaucho nomadism, although the memory of the free horseman endures."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Si bien* nunca rige subjuntivo en la norma culta contemporánea (*si bien sea* es incorrecto; se debe decir *si bien es* o emplear *aunque sea*)."
                }
            ]
        },
        "b2-argentinaregiones-02-a": {
            "id": "grammar.b2.argentinaregiones.02.concesivas-aun-cuando",
            "title": "Alternancia modal en concesivas: Aun cuando",
            "sections": [
                {
                    "type": "text",
                    "content": "La locución conjuntiva concesiva *aun cuando* permite graduar con precisión el estatus informativo de la objeción planteada. Cuando introduce un obstáculo constatado y verificado en la realidad por el hablante, rige modo indicativo (*aun cuando la región es árida, produce vinos notables*). Por el contrario, cuando se proyecta hacia una hipótesis incierta, un escenario futuro o una contingencia extrema desestimada, exige modo subjuntivo (*aun cuando caigan heladas tardías, el riego por aspersión protegerá los racimos*)."
                },
                {
                    "type": "table",
                    "title": "Alternancia de modo con Aun cuando",
                    "rows": [
                        ["Aun cuando el clima cuyano registra una aridez extrema, las acequias transformaron el desierto.", "Even though the Cuyo climate records extreme aridity, the acequias transformed the desert."],
                        ["Aun cuando los productores reduzcan el rendimiento por hectárea, la concentración aromática compensará el volumen.", "Even though producers may reduce yield per hectare, aromatic concentration will make up for volume."],
                        ["Los viñedos prosperan a gran altitud, aun cuando las amplitudes térmicas diarias alcancen veinte grados.", "The vineyards thrive at high altitude, even though daily temperature ranges may reach twenty degrees."],
                        ["Aun cuando la cepa Malbec sea originaria de Francia, encontró en Mendoza su máxima expresión mundial.", "Even though the Malbec variety may be native to France, it found in Mendoza its ultimate world expression."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En textos ensayísticos y de opinión de nivel B2/C1, *aun cuando* aporta un matiz más categórico e hipotético-escalar que el neutral *aunque*."
                }
            ]
        },
        "b2-argentinaregiones-03-a": {
            "id": "grammar.b2.argentinaregiones.03.conectores-concesivos-adversativos",
            "title": "Conectores contraargumentativos en la prosa geográfica",
            "sections": [
                {
                    "type": "text",
                    "content": "En la descripción y el análisis cultural de regiones andinas, los marcadores discursivos concesivos y adversativos (*si bien es cierto que*, *no obstante*, *aun así*, *con todo*) permiten balancear hechos contrastantes sin anular la tesis central. Estos conectores parentéticos guían la argumentación sopesando la conservación de tradiciones ancestrales frente a las presiones del turismo y la modernidad."
                },
                {
                    "type": "table",
                    "title": "Conectores concesivos y adversativos en contexto",
                    "rows": [
                        ["Si bien es cierto que la Quebrada de Humahuaca atrae turismo masivo, las comunidades kolla preservan sus rituales.", "While it is true that the Humahuaca Ravine attracts massive tourism, Kolla communities preserve their rituals."],
                        ["Los valles calchaquíes enfrentan aislamiento geográfico; no obstante, su riqueza cultural florece con vigor.", "The Calchaquí valleys face geographic isolation; nevertheless, their cultural richness flourishes vigorously."],
                        ["Los caminos de montaña son pedregosos y escarpados; aun así, los devotos ascienden al santuario.", "The mountain roads are stony and steep; even so, devotees climb to the sanctuary with fervor."],
                        ["El adobe colonial es vulnerable a los sismos; con todo, las antiguas capillas han desafiado los siglos.", "Colonial adobe is vulnerable to earthquakes; all the same, the ancient chapels have defied the centuries."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Puntuación formal: los conectores parentéticos como *no obstante* y *con todo* suelen aislarse mediante coma cuando inician una cláusula, o entre comas si van intercalados en medio de la oración."
                }
            ]
        },
        "b2-argentinaregiones-04-a": {
            "id": "grammar.b2.argentinaregiones.04.concesivas-pese-a",
            "title": "Concesión preposicional: Pese a + sustantivo / infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La locución preposicional *pese a* introduce estructuras concesivas directas y sintéticas sin necesidad de cláusula finita subordinada cuando va seguida de un sintagma nominal (*pese a las bajas temperaturas*) o de un infinitivo (*pese a carecer de provisiones*). Cuando se emplea con infinitivo, el sujeto del infinitivo coincide habitualmente con el sujeto gramatical de la cláusula principal."
                },
                {
                    "type": "table",
                    "title": "Estructuras con Pese a en crónicas patagónicas",
                    "rows": [
                        ["Pese a las temperaturas gélidas del invierno, el frente del glaciar Perito Moreno mantiene su avance continuo.", "In spite of the freezing winter temperatures, the Perito Moreno glacier front maintains its continuous advance."],
                        ["Los colonos galeses lograron cultivar el valle del Chubut pese a no contar con experiencia en suelos áridos.", "The Welsh settlers managed to farm the Chubut valley in spite of having no experience in arid soils."],
                        ["Pese al aislamiento absoluto de la meseta esteparia, las estancias ovinas forjaron una próspera economía.", "In spite of the absolute isolation of the steppe plateau, the sheep ranches forged a prosperous economy."],
                        ["El navío avanzó con rumbo sur pese a encontrar enormes témpanos flotantes a la entrada del fiordo.", "The vessel advanced southward in spite of encountering huge floating icebergs at the fjord entrance."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Si se desea emplear una cláusula con verbo conjugado, se utiliza la variante conjuntiva *pese a que*: rige indicativo para hechos ciertos (*pese a que soplaba viento*) y subjuntivo para hipótesis o matices evaluativos (*pese a que sople viento*)."
                }
            ]
        },
        "b2-argentinaregiones-05-a": {
            "id": "grammar.b2.argentinaregiones.05.concesivas-por-adj-que",
            "title": "Concesión intensiva: Por + adjetivo / adverbio + que + subjuntivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La estructura cuantitativo-cualitativa intensiva *por + adjetivo/adverbio + que + subjuntivo* formula una concesión de grado máximo: afirma que, sin importar cuán elevada sea la magnitud, intensidad o dificultad de una cualidad, dicha circunstancia resulta incapaz de alterar o impedir el desenlace formulado en la oración principal. El verbo de la subordinada se conjuga siempre en modo subjuntivo por tratarse de una escala hipotética o indefinida."
                },
                {
                    "type": "table",
                    "title": "Estructuras intensivas en crónicas del fin del mundo",
                    "rows": [
                        ["Por recias que sean las borrascas del cabo de Hornos, las embarcaciones científicas zarpan puntuales.", "However fierce the Cape Horn storms may be, scientific vessels set sail punctually."],
                        ["Por inhóspito que pareciera el archipiélago fueguino, los pueblos originarios convivieron en armonía con su entorno.", "However inhospitable the Fuegian archipelago might seem, native peoples lived in harmony with their environment."],
                        ["Por distante que se encuentre Ushuaia de los centros urbanos, su puerto ejerce una atracción magnética.", "However distant Ushuaia may be from urban centers, its port exerts a magnetic attraction."],
                        ["Por duras que fueran las condiciones del presidio, los penados levantaron los primeros cimientos de la ciudad.", "However harsh the prison conditions were, the convicts laid the first foundations of the city."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El adjetivo concuerda obligatoriamente en género y número con el sustantivo al que califica: *por recias que sean las tormentas* (femenino plural), *por hostil que sea el clima* (masculino singular)."
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}-gr.json", gdata)

    # 5. Stories (8 files) - EXACT story.schema.json FORMAT & STRICT 650-825 WORDS!

    story_core_25 = {
        "id": "b2-25",
        "title": "Don Segundo Sombra: La iniciación en las pampas y el adiós al resero",
        "level": "B2",
        "lesson": 25,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Una adaptación literaria de 'Don Segundo Sombra' (1926), la clásica novela gauchesca de Ricardo Güiraldes: el muchacho huérfano Fabio Cáceres abandona la rutina del pueblo para seguir al mítico resero, forjándose como jinete a través de arreos y domas en la inmensidad pampeana, hasta enfrentar el dilema de una herencia imprevista y comprender que la verdadera libertad reside en el desapego interior.",
        "characters": [
            "Fabio Cáceres",
            "Don Segundo Sombra",
            "Capataz de estancia",
            "Escribano de la capital"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el pueblo de San Antonio de Areco, la modorra provinciana parecía adormecer las voluntades y condenar las vidas a una rutina opaca y sin sorpresas. Fabio Cáceres, un muchacho criado entre tías severas que nunca le revelaron con claridad su origen ni su porvenir, vagaba por las orillas del río buscando un sentido que la estrechez del caserío le negaba sistemáticamente. Se sentía un huérfano del alma, un guacho arrojado a las márgenes del mundo adulto, hasta la noche memorable en que una figura descomunal emergió del claroscuro de la calle polvorienta. Silencioso, montado sobre un caballo zaino de porte altivo y envuelto en un poncho que desafiaba la penumbra, cruzó ante sus ojos Don Segundo Sombra. No era un paisano común; en su silueta descansaba toda la serenidad insondable, la dignidad callada y la independencia montaraz de las pampas abiertas."
            },
            {
                "type": "narration",
                "text": "Aquel encuentro fulminante transformó la existencia del muchacho. A partir de esa noche, Fabio dejó de contemplar las tabernas de mala muerte y el tedio pueblerino como su única fatalidad. Decidió abandonar el pueblo para seguir los pasos del viejo resero, resuelto a aprender los misterios de la tierra, la conducción de las tropas de ganado y el código caballeresco de la hombría gaucha. Don Segundo, parco en palabras pero generoso en saberes prácticos, aceptó la compañía del muchacho sin falsas promesas. Durante años de aprendizaje rudo y fraterno, Fabio no dejó de asombrarse ante la destreza incomparable de su maestro, quien dominaba con igual naturalidad el lazo, el cuchillo facón, la doma de potros chúcaros y el consuelo sobrio junto al fogón cuando el cansancio amenazaba con doblegar el ánimo de los peones."
            },
            {
                "type": "narration",
                "text": "La vida del arreo fue una forja implacable bajo soles abrasadores, heladas blanquecinas y tormentas pampeanas que convertían los campos en inmensos lodazales. En más de una ocasión, tras jornadas extenuantes arreando novillos ariscos que intentaban desbandarse entre las lagunas y los pajonales, el joven sintió que sus fuerzas desfallecían sin remedio. Sin embargo, antes de claudicar, acababa por encontrar en la mirada imperturbable de Don Segundo la fuerza para sostenerse en la montura. El muchacho terminó comprendiendo que el verdadero gaucho no es aquel que desafía a la naturaleza con violencia vana, sino el que sabe adaptarse a su rigor y respetar sus silencios. Fabio llegó a convertirse en un jinete respetado por veteranos troperos, capaz de cruzar vados turbulentos y velar el sueño de las haciendas bajo la inmensidad estrellada del cielo austral."
            },
            {
                "type": "narration",
                "text": "Pero el destino reservaba una prueba aún más intrincada para el joven resero. Tras años de nomadismo libre y sacrificado, llegó a la posta una carta formal enviada por un escribano de la capital. El viejo estanciero Don Fabio, a quien el muchacho había servido en su infancia sin sospechar el secreto de su sangre, acababa de morir dejándolo como único y universal heredero de una inmensa fortuna en campos y cabezas de ganado. La noticia cayó como un rayo en el campamento. De la noche a la mañana, el paisano desposeído se transformaba en señor de estancias, atrapado entre las obligaciones jurídicas, los libros contables y la vestimenta refinada de la sociedad letrada."
            },
            {
                "type": "narration",
                "text": "Fabio se rebeló íntimamente contra semejante mutación impuesta. Estuvo a punto de repudiar los títulos de propiedad, pues temía que el lujo y los alambrados acabaran por destruir la libertad conquistada en el camino. No obstante, Don Segundo le habló con la honda filosofía que da el desapego: ser libre no depende de poseer poco o mucho, sino de mantener intacta la propia rectitud interior sin dejar que las cosas materiales gobiernen el espíritu. El maestro dio por concluida su tutela formal: el discípulo ya era un hombre cabal, preparado para defender su honor en cualquier terreno. La despedida final ocurrió en lo alto de una loma al atardecer. Fabio observó cómo la figura de Don Segundo Sombra se empequeñecía lentamente en el horizonte ilimitado de la pampa, recortándose contra el ocaso como una sombra tutelar que jamás dejaría de guiar su sendero interior."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué representa la figura de Don Segundo Sombra para el joven Fabio al inicio del relato?",
                        "options": [
                            "Un capataz autoritario que lo obliga a trabajar en la estancia familiar.",
                            "Un ideal de serenidad, dignidad y libertad que lo rescata de la rutina opaca del pueblo.",
                            "Un pariente lejano que le trae noticias sobre la herencia de sus tierras.",
                            "Un forastero peligroso al que las autoridades intentan capturar en las tabernas."
                        ],
                        "correctIndex": 1,
                        "explanation": "Don Segundo encarna para Fabio la dignidad, la calma estoica y la libertad que el pueblo provinciano le negaba."
                    },
                    {
                        "question": "¿Cuál es la enseñanza central que Don Segundo transmite a Fabio respecto a la condición de gaucho?",
                        "options": [
                            "Que el verdadero gaucho debe acumular riquezas para comprar sus propias parcelas.",
                            "Que la hombría se demuestra derrotando a otros paisanos en duelos a cuchillo.",
                            "Que el valor reside en adaptarse al rigor natural y conservar la rectitud interior con desapego.",
                            "Que la vida nómada es insostenible frente al avance definitivo de los alambrados."
                        ],
                        "correctIndex": 2,
                        "explanation": "Don Segundo le enseña que la libertad y el honor residen en la fuerza moral interior y el desapego de lo material."
                    },
                    {
                        "question": "¿Qué dilema ético experimenta Fabio al descubrir que es el heredero de una gran fortuna?",
                        "options": [
                            "Teme que la propiedad y las exigencias de la vida acomodada destruyan su libertad conquistada.",
                            "Duda entre repartir el dinero entre los peones o construir un nuevo pueblo junto al río.",
                            "Planea vender todas las estancias para marcharse a vivir como forastero en Europa.",
                            "Sospecha que Don Segundo lo engañó para quedarse con una parte sustancial del ganado."
                        ],
                        "correctIndex": 0,
                        "explanation": "Fabio teme que la condición de propietario y los lazos de la vida letrada anulen la libertad espiritual conquistada como resero."
                    }
                ]
            }
        }
    }

    # Verify and write classic story
    w_count_classic = count_words(story_core_25)
    print(f"stories/classics/b2/b2-25.json: {w_count_classic} words")
    assert 650 <= w_count_classic <= 825, f"Classic story has {w_count_classic} words (must be 650-825)"
    write_json("stories/classics/b2/b2-25.json", story_core_25)

    # Regional Stories (5 lesson stories + 1 consolidation + 1 library stitched story)
    regional_story_texts = {
        "b2-argentinaregiones-01": [
            "La llanura pampeana se despliega ante los ojos del viajero como un inmenso océano verde de fertilidad asombrosa y horizonte rigurosamente rectilíneo, donde la curvatura terrestre parece la única frontera física capaz de contener la mirada. Dividida naturalmente entre la pampa húmeda oriental y la pampa seca que avanza hacia el poniente, esta formidable extensión de limos y sedimentos eólicos albergó durante siglos pastizales nativos ininterrumpidos y pastos duros, con la sola interrupción visual de algún ombú solitario recortado contra el crepúsculo. En este tapiz geográfico de escala monumental se gestó una de las epopeyas culturales más singulares y perdurables del Cono Sur: el nacimiento, apogeo y mitificación del gaucho. Jinete insuperable desde su más temprana infancia, diestro con el lazo de tientos y el cuchillo facón, el gaucho original fue el señor indiscutido de las soledades pampeanas, sobreviviendo en perfecta simbiosis con el caballo criollo y cazando las inmensas manadas de ganado cimarrón que vagaban sin marca ni dueño conocido por los campos abiertos de la cuenca del Plata.",
            "Si bien las élites letradas de Buenos Aires durante el siglo diecinueve lo retrataron a menudo con manifiesto recelo como un elemento rústico, levantisco y montaraz opuesto al progreso civilizatorio de cuño europeo, el paisano pampeano poseía un estricto código de honor basado en la lealtad fraterna, la hospitalidad incondicional ante el viajero desamparado y la defensa indoblegable de su libertad personal. Su apero y vestimenta constituían una obra maestra de adaptación funcional al medio: el poncho de vicuña o lana pesada que servía de abrigo nocturno y escudo en los lances de honor, las botas de potro y las boleadoras heredadas del contacto ancestral con las naciones indígenas pampas y querandíes. Alrededor del fogón nocturno en las pulperías de campo, mientras circulaba de mano en mano el mate amargo y chisporroteaba la leña aromática del asado a la cruz, florecía la payada: un combate poético improvisado en décimas octosilábicas donde dos cantores medían su ingenio filosófico, debatiendo sobre el destino humano, el rigor de la justicia y los pesares del hombre desposeído.",
            "La publicación en 1872 de El gaucho Martín Fierro, la inmortal obra poética concebida por José Hernández en el aislamiento de una humilde habitación de hotel, marcó un punto de inflexión trascendental en la conciencia histórica y social argentina. El poema denunciaba con elocuencia desgarradora los abusos de las levas militares forzosas que arrancaban al gaucho pacífico de su rancho y de sus hijos para confinarlo en los fortines de la frontera, utilizándolo como peón sin paga y carne de cañón frente al malón indígena. Si bien el avance inexorable de las líneas férreas británicas, la construcción de la zanja de Alsina y la introducción masiva del alambre de púas en las estancias terminaron por disolver la vida nómada tradicional, parcelando la tierra y subordinando al jinete libre al régimen del salario rural, la figura del gaucho no desapareció del corazón popular.",
            "Muy por el contrario, a medida que la Argentina moderna se transformaba en el granero agroexportador del mundo y levantaba orgullosos palacios de inspiración francesa junto a las orillas del Plata, la figura del gaucho experimentó una profunda y apasionada canonización patriótica. De paria errante, desertor perseguido y marginal por antonomasia, fue elevado por poetas e intelectuales como Leopoldo Lugones a símbolo arquetípico indiscutible de la nacionalidad, encarnando las virtudes de la generosidad desinteresada, la valentía moral y la conexión entrañable con la tierra nativa. Las grandes estancias de la provincia de Buenos Aires, de Santa Fe y de Córdoba, que introdujeron razas vacunas británicas como Aberdeen Angus y Hereford, mantuvieron vivas las faenas ecuestres tradicionales como el pilar fundamental del manejo ganadero en campo abierto.",
            "Hoy en día, las jornadas camperas de la yerra, la doma racional sin violencia y el arreo de tropas hacia los corrales conviven armoniosamente con sofisticadas tecnologías agronómicas de siembra directa y monitoreo satelital de pasturas. En localidades históricas señeras como San Antonio de Areco, la orfebrería criolla en plata cincelada a martillo, la talabartería en cuero crudo finamente trenzado y los festivales de jineteada celebran cada noviembre la Fiesta de la Tradición, recordando a las nuevas generaciones que, si bien el mundo urbano contemporáneo impone su ritmo vertiginoso, en el corazón silente y espacioso de la llanura pampeana late con fuerza la memoria inmarchitable de sus jinetes primigenios."
        ],
        "b2-argentinaregiones-02": [
            "Al pie de la formidable Cordillera de los Andes, en la histórica región occidental de Cuyo, la provincia argentina de Mendoza desafía de manera contundente toda lógica geográfica tradicional. Inserta en una franja hiperárida de pronunciada sombra orográfica donde las precipitaciones anuales rara vez superan los doscientos milímetros cúbicos y los vientos secos y cálidos como el temible Zonda descienden periódicamente desde las altas crestas cordilleranas deshidratando el ambiente, esta planicie pedregosa y polvorienta logró transformarse en una de las grandes capitales vitivinícolas del planeta. La clave de esta formidable metamorfosis territorial no reside en la abundancia de lluvias benévolas ni en un clima templado por brisas oceánicas, sino en la domesticación magistral del deshielo andino que desciende con impetuosa fuerza desde las cumbres nevadas del cerro Aconcagua y sus colosos glaciarios circundantes durante los meses de primavera y verano.",
            "Mucho antes de la llegada de las primeras expediciones colonizadoras hispánicas en el siglo dieciséis, las comunidades indígenas huarpes ya habían ideado un prodigioso y complejo sistema hidráulico de canales maestros y acequias de barro para conducir las aguas bravías de los ríos Mendoza y Tunuyán hacia los campos cultivados de algarrobo y maíz. Los conquistadores españoles adoptaron con presteza esta red milenaria de irrigación y la expandieron progresivamente a lo largo del periodo colonial, pero fue a mediados del siglo diecinueve cuando la provincia experimentó su salto cualitativo definitivo hacia la modernidad agroindustrial. En 1853, por encargo visionario de Domingo Faustino Sarmiento y del gobernador provincial Pedro Pascual Segura, el agrónomo francés Michel Aimé Pouget introdujo en Mendoza sarmientos rigurosamente seleccionados de diversas cepas nobles europeas, entre las cuales destacaba una uva tinta de origen bordelés casi relegada y olvidada en su terruño natal: el Malbec.",
            "Aun cuando en los húmedos y fríos valles franceses de Cahors y Burdeos el Malbec presentaba notorias dificultades de maduración fenólica debido a las enfermedades fúngicas recurrentes, a las heladas primaverales y a la podredumbre otoñal provocada por el exceso de humedad, en el suelo aluvial, permeable y rico en minerales calcáreos de Mendoza encontró su verdadero paraíso biológico planetario. La extraordinaria luminosidad solar que baña los faldeos andinos durante más de trescientos días al año, la pureza química indiscutible de las aguas de deshielo canalizadas por acequias arboladas y, por encima de cualquier otro factor geográfico, la marcada amplitud térmica entre el día y la noche —que puede alcanzar con facilidad los veinte grados centígrados durante los meses estivales de maduración— permitieron que la cepa desarrollara un perfil enológico sin precedentes en la historia vitivinícola mundial: taninos dulces y sumamente pulidos, una concentración antociánica profunda de color violáceo y aromas embriagadores a ciruelas maduras, higos secos, violetas silvestres y elegantes notas balsámicas y especiadas.",
            "En las últimas tres décadas, la vitivinicultura mendocina escaló con audacia hacia altitudes que los manuales tradicionales de enología del viejo mundo juzgaban incompatibles con la vid comercial de alta gama. En el célebre Valle de Uco, a cotas vertiginosas que oscilan entre los novecientos y los mil quinientos metros sobre el nivel del mar en parajes míticos como Gualtallary, Paraje Altamira o San Pablo, viñedos cultivados sobre lechos de cantos rodados cubiertos de caliche producen vinos dotados de una insólita acidez natural, frescura vibrante y tensión mineral que cosechan las más altas puntuaciones en la crítica especializada internacional. Bodegas de arquitectura bioclimática vanguardista integradas armónicamente en el imponente paisaje cordillerano combinan vasijas de hormigón crudo sin epoxi, ánforas de cerámica artesanal y barricas de roble francés de tostado sutil con sofisticados sistemas de fermentación por gravedad que preservan la pureza integral del fruto cosechado.",
            "Cada mes de marzo, la provincia entera se paraliza con devoción colectiva para celebrar la Fiesta Nacional de la Vendimia, un espectáculo de masas de magnitud colosal que fusiona teatro alegórico, coreografías folclóricas deslumbrantes y poesía popular para honrar el esfuerzo sacrificado de cosechadores, podadores, canaleros, tractoristas y enólogos de renombre. En el histórico teatro griego Frank Romero Day, ante decenas de miles de espectadores enfervorizados que colman las gradas cerro abajo bajo el límpido cielo nocturno de los Andes, mendocinos y viajeros de los cinco continentes brindan con copas colmadas de Malbec, reconociendo con profunda emoción cívica que, aun cuando el desierto aceche implacable más allá del trazado verde de las acequias, la alianza indisoluble entre la tenacidad humana y el agua pura de las cumbres consagró a este oasis como un monumento vivo al arte milenario del vino."
        ],
        "b2-argentinaregiones-03": [
            "En el extremo noroccidental de la República Argentina, en aquel territorio fascinante donde la cordillera andina se dilata en las mesetas desérticas y ventosas de la Puna, las provincias de Jujuy y Salta albergan dos paisajes geográficos y culturales de sobrecogedora monumentalidad: la Quebrada de Humahuaca y los Valles Calchaquíes. Declarada Patrimonio Cultural y Natural de la Humanidad por la UNESCO en el año 2003, la Quebrada de Humahuaca es una inmensa y profunda fractura tectónica de más de ciento cincuenta kilómetros de longitud surcada por las aguas cambiantes del río Grande, cuyas laderas desnudas exhiben una policromía geológica alucinante labrada a lo largo de millones de años de sedimentación fluvial y marina ininterrumpida. El emblemático Cerro de los Siete Colores, que custodia silencioso el milenario pueblo de Purmamarca, deslumbra a los observadores con sus franjas sedimentarias ocres, verdes, violáceas, amarillentas y rojizas superpuestas en perfecta armonía mineral, ofreciendo un lienzo natural único en el cono sur americano.",
            "Pero más allá de su magnetismo paisajístico incomparable, la comarca entera constituye el testimonio palpable de más de diez mil años de ocupación humana continuada e ininterrumpida por cazadores recolectores y agricultores tempranos. Los pueblos originarios kolla, omaguaca y tilcara domesticaron estas laderas escarpadas mucho antes de la tardía expansión del Tahuantinsuyo incaico y de la posterior y violenta irrupción de las huestes coloniales hispánicas. Vestigios arqueológicos monumentales como el Pucará de Tilcara —una imponente fortaleza defensiva de piedra erigida sobre una colina estratégica que domina el valle fluvial y rodeada de espesos bosques de cardones centenarios que se alzan como guardianes vegetales— revelan el refinado nivel de organización urbana, arquitectura militar, cerámica ritual polícroma y agricultura intensiva en andenes escalonados que caracterizaba a estas sociedades andinas originarias.",
            "Si bien es cierto que la colonización evangelizadora española impuso con rigor los dogmas de la fe católica y sembró la región de encantadoras iglesias y capillas de adobe con techos sostenidos por vigas de cardón rústico y campanarios encalados de blanco níveo, la espiritualidad indígena originaria jamás pudo ser desarraigada de la memoria comunitaria. En los valles y quebradas floreció un conmovedor y profundo sincretismo religioso en el que los santos patronos de la liturgia romana conviven de manera natural con las deidades telúricas ancestrales. El primero de agosto de cada año, al despuntar el ciclo agrario con el despertar de la tierra fértil, las familias abren hoyos ceremoniales en la tierra viva de sus patios para alimentar y sahumar a la Pachamama, la Madre Tierra, ofreciéndole hojas de coca fresca, chicha de maíz fermentada, tabaco aromático, aguardiente y viandas típicas en ferviente gratitud por su generosidad nutricia y rogando protección para el ganado y las cosechas venideras.",
            "Hacia el sur, los Valles Calchaquíes despliegan otra vertiente asombrosa del noroeste argentino entre colosales gargantas de arenisca roja y pueblos coloniales de herencia hispano-criolla intacta como Cachi, Molinos, San Carlos y Cafayate. En Cafayate, entre viñedos de extrema altura que ascienden hasta los dos mil y tres mil metros sobre el nivel del mar regados por vertientes cristalinas de montaña, se elabora el célebre vino Torrontés, una variedad blanca autóctona de perfume exuberante a jazmines, azahares y duraznos blancos que expresa con autenticidad insustituible la singularidad mineral de este terruño andino. No obstante el aislamiento secular que impusieron las intrincadas y pedregosas serranías calchaquíes, la vida comunitaria vibra con intensidad en las tradicionales peñas folclóricas, donde el redoble profundo del bombo legüero de madera de ceibo, la caja coplera y el llanto dulce del charango acompañan el canto de zambas pausadas y chacareras arrebatadoras.",
            "La existencia cotidiana en estos rincones andinos transcurre al compás de un sosiego filosófico y una dignidad ancestral que contrastan fuertemente con el desasosiego y el ruido vertiginoso de las grandes urbes modernas. Mujeres artesanas de manos curtidas por el frío y el sol de altura tejen mantas y ponchos de lana finísima de llama y vicuña en antiguos telares de madera de pie, mientras los copleros mayores entonan versos octosilábicos de honda sabiduría existencial en las celebraciones comunitarias del carnaval y los convites agrícolas. Con todo, el noroeste argentino no es una postal folclórica congelada en el tiempo ni un simple museo arqueológico al aire libre, sino una civilización viva, creativa y orgullosa que custodia la memoria profunda del continente americano frente a las incertidumbres del porvenir contemporáneo."
        ],
        "b2-argentinaregiones-04": [
            "Al sur de la cuenca del río Colorado comienza la Patagonia, un territorio de resonancias míticas y literarias cuya sola evocación remite a la inmensidad desolada, al viento implacable que no conoce tregua y a una naturaleza indómita que durante siglos representó el límite infranqueable de la geografía conocida para los navegantes europeos. En el extremo suroccidental de la provincia de Santa Cruz, abrazado por los picos andinos y bosques de lengas del Parque Nacional Los Glaciares, se encuentra una de las maravillas glaciológicas más majestuosas y dinámicas del globo terrestre: el Glaciar Perito Moreno. Alimentado por el colosal Campo de Hielo Patagónico Sur —la masa de hielo continental más extensa del hemisferio sur fuera de la plataforma antártica—, este monumental río de hielo azulado desciende lentamente desde las altas cumbres hasta desembocar en las aguas turquesas del lago Argentino.",
            "A diferencia de la inmensa mayoría de los glaciares alpinos y boreales del planeta, que sufren en la actualidad un retroceso acelerado y catastrófico como consecuencia directa del calentamiento global antropogénico, el Perito Moreno mantiene un prodigioso y fascinante equilibrio dinámico de avance continuo. Su colosal frente de hielo, que alcanza cinco kilómetros de longitud y se eleva a más de sesenta metros sobre la superficie lacustre como una muralla infranqueable, avanza con periodicidad hasta apoyarse con fuerza titánica sobre la península de Magallanes. Al represar las aguas del Brazo Rico, se genera un desnivel hídrico de varios metros cuya tremenda presión hidrostática socava los cimientos del hielo inferior hasta horadar un túnel subglaciar. Cuando la bóveda de hielo colapsa finalmente en un estruendo ensordecedor que lanza olas gigantescas y desmembra témpanos azulados que flotan a la deriva, millares de viajeros asisten sobrecogidos a uno de los espectáculos más grandiosos de la dinámica telúrica planetaria.",
            "Hacia el este de los ventisqueros cordilleranos, el paisaje se abre abruptamente en la vastedad sobrecogedora de la estepa patagónica: una meseta basáltica y pedregosa tapizada de arbustos espinosos como el coirón y la mata negra, azotada por ráfagas incesantes del cuadrante oeste que modelan las formas del terreno. En este escenario de aparente desamparo se desarrolló durante la segunda mitad del siglo diecinueve una de las empresas colonizadoras y comunitarias más singulares de la historia sudamericana. En julio de 1865, tras una extenuante y precaria travesía oceánica a bordo del velero Mimosa, arribó a las desiertas costas del Golfo Nuevo un contingente de ciento cincuenta y tres hombres, mujeres y niños galeses liderados por el reverendo Michael D. Jones y Lewis Jones, quienes buscaban afanosamente una tierra libre donde preservar su lengua materna céltica, su fe religiosa no conformista y sus tradiciones comunitarias frente a la asimilación impuesta por el Imperio Británico en Gales.",
            "Pese a carecer de víveres suficientes para afrontar el invierno, no poseer conocimientos agrícolas adaptados al rigor del desierto austral y encontrarse a miles de leguas de cualquier socorro civilizado, los colonos lograron sobrevivir y prosperar gracias a una actitud pionera de respeto intercultural ejemplar. En lugar de empuñar las armas y construir fortificaciones militares defensivas, los galeses trabaron una estrecha y leal alianza de intercambio pacífico con los pueblos originarios tehuelches, quienes les enseñaron las técnicas de rastreo, la caza del guanaco y el choique y el uso de las boleadoras en la estepa abierta. Desarrollando un audaz e innovador sistema de canales de irrigación derivados de las crecidas del río Chubut, los inmigrantes transformaron un valle semiárido en un vergel triguero que cosechó medallas de oro en ferias mundiales y sentó las bases demográficas de la provincia.",
            "En la actualidad, ciudades y poblados como Trelew, Rawson, Puerto Madryn y la idílica villa de Gaiman mantienen intacto ese patrimonio cultural bilingüe galés-argentino único en el continente. En las tradicionales casas de té de arquitectura victoriana de ladrillo visto de Gaiman, donde se sirve la auténtica torta negra galesa junto a panes caseros y mermeladas de frutos del bosque, los coros locales continúan interpretando himnos sacros en lengua galesa mientras el festival anual del Eisteddfod premia composiciones poéticas y musicales en ambos idiomas, atestiguando con elocuencia que la Patagonia austral es un territorio donde el esfuerzo solidario y la comunión entre culturas disímiles fueron capaces de florecer sobre la hostilidad del viento y la lejanía geográfica."
        ],
        "b2-argentinaregiones-05": [
            "Separada del extremo meridional del continente americano por las aguas procelosas y traicioneras del Estrecho de Magallanes, la Isla Grande de Tierra del Fuego emerge en la cartografía universal como el confín definitivo del mundo habitado, la última frontera geográfica y humana antes de las soledades heladas de la plataforma antártica. Flanqueada por las estribaciones terminales de la Cordillera de los Andes —cuyos cordones montañosos cambian aquí de orientación para correr de oeste a este antes de precipitarse en las fosas atlánticas— y por las aguas profundas del histórico Canal Beagle, la ciudad de Ushuaia se recorta con gallardía entre densos bosques magallánicos de lengas, ñires y ventisqueros colgantes, ostentando con orgullo el título universal de la ciudad más austral del planeta. Enclavada en una bahía semicircular de aguas calmas que contrasta vivamente con las tempestades oceánicas circundantes, la villa combina la arquitectura tradicional de madera y chapa acanalada con modernos miradores panorámicos que contemplan las cumbres nevadas del glaciar Martial.",
            "Sin embargo, la historia de Tierra del Fuego alberga también una de las tragedias humanas más desgarradoras y silenciadas del proceso de expansión estatal y económica decimonónico. Durante más de diez milenios, cuatro etnias originarias habitaron este archipiélago subpolar en admirable y delicado equilibrio con un medio ambiente de extrema severidad climática: los yámanas y kawésqar, nómadas canoeros que surcaban los fiordos protegidos por grasa de foca para pescar y cazar mamíferos marinos, y los selk'nam y haush, expertos cazadores pedestres que deambulaban por las estepas boscosas del norte tras las manadas de guanacos. El imponente ritual de iniciación espiritual del Hain, en el que los varones selk'nam pintaban sus cuerpos con complejos patrones geométricos de ceniza y arcilla roja para personificar a los espíritus del cosmos, constituye uno de los pináculos estéticos de la antropología simbólica americana.",
            "Por funesta paradoja histórica, la inserción de Tierra del Fuego en los circuitos de la economía capitalista agroexportadora hacia finales del siglo diecinueve provocó la aniquilación sistemática y sangrienta de estas naciones ancestrales. Las grandes sociedades explotadoras de ganado ovino alambraron la llanura esteparia y consideraron la presencia milenaria de los pueblos indígenas incompatible con la rentabilidad lanera, contratando mercenarios extranjeros y cazadores a sueldo a los que se pagaba una libra esterlina por cada par de orejas, manos cercenadas o cráneos de aborígenes asesinados. Diezmados por esta cacería atroz, por epidemias exógenas devastadoras de sarampión y viruela y por el desarraigo forzado en reducciones misionales salesianas, los pueblos fueguinos sufrieron un etnocidio demoledor cuya memoria dolorosa es hoy reivindicada con valentía cívica indeclinable por sus descendientes contemporáneos.",
            "Con el propósito prioritario de afianzar la soberanía territorial argentina en este punto geoestratégico neurálgico, el Estado nacional procedió a inicios del siglo veinte a la construcción definitiva del Presidio y Cárcel de Reincidentes de Ushuaia. Concebida como una penitenciaría de máxima seguridad para criminales célebres y disidentes políticos del régimen, fueron los propios penados quienes, en medio de inviernos feroces y condiciones inhumanas, talaron los densos bosques circundantes, operaron el legendario Tren del Fin del Mundo y edificaron con sus manos los pabellones de piedra y las primeras calles y muelles de la naciente villa austral. Clausurado el penal en 1947 por decreto humanitario, Ushuaia protagonizó una reconversión socioeconómica ejemplar gracias al régimen de exenciones fiscales, al impulso de la investigación científica marina del CADIC y a un desarrollo turístico global sostenible de alta calidad.",
            "Hoy en día, el puerto marítimo de Ushuaia bulle de dinamismo cosmopolita al consolidarse indiscutidamente como la principal base de operaciones náuticas y logísticas para más del noventa por ciento de los cruceros turísticos y expediciones científicas internacionales que navegan con rumbo sur hacia la península Antártica. Por inclementes que resulten las borrascas subpolares del pasaje de Drake y por cambiante que sea el tiempo fueguino entre celliscas repentinas y calmas luminosas, quienes surcan las aguas cristalinas del Canal Beagle contemplando los bosques costeros, las turberas fósiles de sphagnum, las colonias de pingüinos de Magallanes y las loberías de los islotes Bridges descubren conmovidos que en este rincón postrero del planeta la naturaleza conserva intacta su belleza salvaje y su sobrecogedora pureza primordial."
        ],
        "b2-argentinaregiones-consolidation": [
            "Emprender una travesía comprensiva y reflexiva por la totalidad de la geografía argentina constituye una experiencia de contrastes territoriales tan desmesurados que desafía cualquier intento de generalización simplificadora. Muy pocas naciones en el planeta concentran dentro de una misma soberanía política una diversidad de biomas tan vasta como la que media entre los valles y quebradas policromáticos del noroeste andino, el mar de pastizales infinitos de la llanura pampeana, los oasis vitivinícolas irrigados al pie de los gigantes nevados de Cuyo y las estepas gélidas azotadas por borrascas oceánicas en los confines de Tierra del Fuego. Esta gigantesca cartografía física no ha sido un mero escenario inerte para los acontecimientos humanos, sino la matriz viva que modeló economías regionales singulares, temperamentos comunitarios indoblegables y complejas expresiones culturales a lo largo de dos centurias de historia nacional republicana.",
            "En el corazón agrícola y productivo del país, la llanura pampeana forjó el mito del gaucho libre como símbolo eterno de autonomía individual, coraje moral y destreza ecuestre incomparable. Si bien la llegada del alambre de púas, el avance de las líneas férreas y la agricultura mecanizada disolvieron el nomadismo primigenio de los jinetes pampeanos transformándolos en peones asalariados o arrendatarios de chacras, el código de honor, la dignidad austera y la hospitalidad sin reservas continúan latiendo en la vida cotidiana de los pueblos de campo. El lenguaje campero, con su rico repertorio léxico sobre pelajes equinos, marcas de yerra y modismos sobrios, permea la literatura nacional y el habla urbana cotidiana. Asimismo, la ceremonia comunitaria del asado a la cruz y el tránsito incesante del mate amargo compartido trascienden las clases sociales y las barreras generacionales para erigirse en auténticos sacramentos de comunión cívica y pertenencia identitaria en todos los rincones del territorio argentino.",
            "Hacia el poniente cordillerano, la provincia de Mendoza y la región de Cuyo demuestran la victoria admirable del ingenio humano sobre la aridez más implacable del paisaje desértico. Herederos directos de las técnicas ancestrales de riego por acequias diseñadas originalmente por los pueblos huarpes, los agricultores y enólogos cuyanos supieron capturar el deshielo de los colosos andinos para alumbrar un vergel productivo de rango universal indiscutido. El cultivo heroico de la vid en los faldeos cordilleranos y la consagración internacional del Malbec de altura evidencian que, aun cuando los factores climáticos iniciales parezcan hostiles o desfavorables, la alianza armónica entre la ciencia agronómica moderna, la viticultura de precisión y la devoción entrañable al terruño es capaz de alumbrar creaciones de un refinamiento organoléptico insuperable.",
            "En las alturas septentrionales de Jujuy y Salta, la Quebrada de Humahuaca y los Valles Calchaquíes preservan la memoria profunda de las civilizaciones andinas precolombinas frente al paso de los siglos. Allí, donde los estratos minerales tiñen las serranías con los matices del arcoíris y las fortalezas de piedra del pucará vigilan los valles fluviales, la reverencia sagrada a la Pachamama no constituye un anacronismo folclórico ni una atracción exótica, sino un principio rector de reciprocidad ecológica con la Madre Tierra. El adobe cálido de las capillas coloniales, la poesía sentenciosa de las coplas populares transmitidas oralmente y el lamento emotivo de quenas, sicus y charangos recuerdan que la Argentina es también una nación indisolublemente vinculada al corazón espiritual del mundo andino sudamericano.",
            "Finalmente, en las soledades australes de la Patagonia y el archipiélago fueguino, la naturaleza despliega la grandeza sublime de los ventisqueros en continuo avance como el Perito Moreno, las mesetas esteparias colonizadas con paciencia por los pioneros galeses en el Chubut y los canales marítimos que acarician la Antártida en Ushuaia. Desde la dolorosa lección histórica del etnocidio de las naciones originarias del extremo sur hasta la pujanza científica y logística de los puertos australes contemporéneos, la geografía argentina culmina en un horizonte de reflexión y desafío colectivo. Comprender la Argentina exige, en definitiva, recorrer estos cuatro puntos cardinales sin prejuicios metropolitanos, descubriendo en cada terruño una voz inconfundible que enriquece el acervo cultural hispanoamericano. En este inmenso mapa de contrastes deslumbrantes, la verdadera riqueza de la república reside en la polifonía irrepetible de sus paisajes y en la inquebrantable dignidad de sus pueblos."
        ]
    }

    regional_titles_summaries = {
        "b2-argentinaregiones-01": (
            "La llanura pampeana y el mito del gaucho",
            "Una crónica sobre la pampa húmeda argentina: la inmensidad del horizonte pampeano, el origen y código de honor del gaucho, la payada criolla, el impacto social de 'El gaucho Martín Fierro' y la evolución de la vida rural tradicional hacia la modernidad agropecuaria.",
            ["Jinete pampeano Don Hilario", "Arriero joven Bautista", "Platero criollo Facundo", "Investigadora cultural Soledad"],
            1
        ),
        "b2-argentinaregiones-02": (
            "Mendoza y el oasis del Malbec: Vitivinicultura al pie de los Andes",
            "Un ensayo sobre la transformación agrícola de Cuyo: el aprovechamiento del deshielo andino mediante canales huarpes y acequias, la introducción del Malbec por Michel Aimé Pouget en 1853, la vitivinicultura de altura en el Valle de Uco y la Fiesta Nacional de la Vendimia.",
            ["Agrónomo mendocino Gonzalo", "Enóloga de Valle de Uco Marcela", "Canalero veterano Don Ramón", "Sommelier internacional Clara"],
            2
        ),
        "b2-argentinaregiones-03": (
            "La Quebrada de Humahuaca y los valles calchaquíes",
            "Un recorrido cultural por el noroeste argentino: la estratigrafía geológica del Cerro de los Siete Colores en Purmamarca, la fortaleza del Pucará de Tilcara, el sincretismo andino y la veneración a la Pachamama, y la música folclórica en los Valles Calchaquíes.",
            ["Coplera y tejedora kolla Doña Eusebia", "Arqueólogo andino Matías", "Luthier de bombos Don Celso", "Viticultor de Cafayate Esteban"],
            3
        ),
        "b2-argentinaregiones-04": (
            "La Patagonia austral: Glaciar Perito Moreno y los colonos galeses",
            "Una crónica de la geografía y colonización patagónica: el dinamismo del Glaciar Perito Moreno en el lago Argentino, la inmensidad de la estepa ovina, la gesta pacífica de los colonos galeses del velero Mimosa en Chubut y las tradiciones bilingües de Gaiman.",
            ["Glacióloga patagónica Valeria", "Guía de montaña Santiago", "Descendiente de colonos galeses Elen", "Estanciero de Santa Cruz Don Evaristo"],
            4
        ),
        "b2-argentinaregiones-05": (
            "Tierra del Fuego y Ushuaia: La ciudad del fin del mundo",
            "Un retrato del extremo austral del continente: el Canal Beagle y los bosques magallánicos, la memoria trágica del genocidio selk'nam y yámana, la historia del Presidio de Ushuaia y el rol estratégico de la ciudad como puerta de entrada a la Antártida.",
            ["Historiadora fueguina Laura", "Capitán de expedición antártica Bruno", "Biólogo marino del CADIC Andrés", "Descendiente selk'nam Margarita"],
            5
        ),
        "b2-argentinaregiones-consolidation": (
            "Consolidación: El vasto mapa argentino",
            "Una síntesis integradora de los contrastes geográficos y culturales de la Argentina: desde los valles prehispánicos del noroeste y el corazón pampeano del gaucho hasta los oasis vitivinícolas de Cuyo y los mares gélidos de la Patagonia y Tierra del Fuego.",
            ["Geógrafo y ensayista nacional Martín", "Historiadora regional Valentina", "Viajero y cronista Julián", "Antropóloga cultural Mariana"],
            6
        )
    }

    # Verify and write regional stories
    for stem, text_paras in regional_story_texts.items():
        rel_path = f"stories/world/b2/{stem}.json"
        title, summary, characters, lesson_num = regional_titles_summaries[stem]
        story_obj = {
            "id": stem,
            "title": title,
            "level": "B2",
            "lesson": lesson_num,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": summary,
            "characters": characters,
            "paragraphs": [{"type": "narration", "text": p} for p in text_paras],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Cuál es la tesis central que articula este texto respecto a la geografía argentina?",
                            "options": [
                                "Que el país presenta una uniformidad ecológica dominada exclusivamente por el clima pampeano.",
                                "Que la diversidad territorial forjó identidades regionales, saberes productivos y cosmovisiones singulares.",
                                "Que las regiones periféricas carecen de conexión histórica con el desarrollo cultural de la nación.",
                                "Que la influencia europea eliminó por completo los rastros de las culturas indígenas y gauchescas."
                            ],
                            "correctIndex": 1,
                            "explanation": "El texto argumenta que la vastedad territorial y sus biomas moldearon respuestas culturales y productivas singulares."
                        },
                        {
                            "question": "¿Qué factor común destaca el texto en la adaptación humana a paisajes rigurosos como Mendoza y la Patagonia?",
                            "options": [
                                "La explotación intensiva de combustibles fósiles sin considerar el equilibrio natural.",
                                "El abandono paulatino de los asentamientos rurales en favor del crecimiento de la capital.",
                                "La combinación de saberes ancestrales y comunitarios para vencer los desafíos de la aridez o el frío.",
                                "La dependencia exclusiva de subsidios estatales centralizados desde el siglo diecinueve."
                            ],
                            "correctIndex": 2,
                            "explanation": "Tanto el riego cuyano como la colonización patagónica se basaron en la cooperación y el aprovechamiento inteligente del entorno."
                        },
                        {
                            "question": "¿Cómo se describe la relación entre modernidad y tradición en las regiones analizadas?",
                            "options": [
                                "Como un diálogo fecundo donde la memoria identitaria convive con la innovación contemporánea.",
                                "Como una ruptura violenta que borró la totalidad de las prácticas culinarias y festivas del pasado.",
                                "Como un proceso fallido que aisló económicamente al interior del país del comercio mundial.",
                                "Como una asimilación forzada que subordinó todos los terruños al modelo industrial porteño."
                            ],
                            "correctIndex": 0,
                            "explanation": "El texto resalta cómo las faenas tradicionales, la viticultura y los rituales dialogan activamente con la tecnología moderna."
                        }
                    ]
                }
            }
        }

        # Check word count
        w_count = count_words(story_obj)
        print(f"{rel_path}: {w_count} words")
        assert 650 <= w_count <= 825, f"Story {rel_path} has {w_count} words (must be 650-825)"
        write_json(rel_path, story_obj)

    # Consolidated library story: b2-argentinaregiones.json (25 paragraphs from lessons 1-5)
    stitched_paragraphs = []
    for i in range(1, 6):
        stem = f"b2-argentinaregiones-0{i}"
        for p in regional_story_texts[stem]:
            stitched_paragraphs.append({"type": "narration", "text": p})

    assert len(stitched_paragraphs) == 25, f"Stitched library story must have 25 paragraphs, got {len(stitched_paragraphs)}"

    stitched_story = {
        "id": "b2-argentinaregiones",
        "title": "Argentina II: Las Pampas, la Patagonia y los Terruños Regionales",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 20,
        "summary": "Una travesía integral por los cuatro puntos cardinales del territorio argentino: las llanuras pampeanas del gaucho, los oasis vitivinícolas de Mendoza, las quebradas y pucarás del noroeste andino, los glaciares y estepas patagónicas de los galeses, y los canales y turberas australes de Tierra del Fuego.",
        "characters": [
            "Pobladores de la pampa",
            "Viticultores de Cuyo",
            "Comunidades del noroeste andino",
            "Pioneros de la Patagonia austral",
            "Habitantes de Tierra del Fuego"
        ],
        "paragraphs": stitched_paragraphs,
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué manera evolucionó la percepción del gaucho en la sociedad argentina a partir de finales del siglo XIX?",
                        "options": [
                            "Pasó de ser considerado un paria marginal a ser canonizado como símbolo patriótico de la identidad nacional.",
                            "Fue olvidado completamente tras el triunfo del ferrocarril y la agricultura mecanizada.",
                            "Se convirtió en un líder político que gobernó las principales provincias del interior.",
                            "Fue asimilado a las corrientes migratorias urbanas que poblaron los conventillos de Buenos Aires."
                        ],
                        "correctIndex": 0,
                        "explanation": "El gaucho pasó de ser perseguido y estigmatizado a consagrarse como arquetipo moral de la argentinidad."
                    },
                    {
                        "question": "¿Qué combinación de factores permitió que el Malbec alcanzara en Mendoza una calidad enológica superior a la de su región de origen?",
                        "options": [
                            "Las precipitaciones tropicales abundantes y el suelo arcilloso impermeable del valle.",
                            "La intensa luminosidad solar, el agua pura de deshielo y la gran amplitud térmica diaria.",
                            "El uso exclusivo de abonos químicos y la importación de uvas congeladas desde Europa.",
                            "El cultivo a nivel del mar protegido de las heladas andinas por bosques artificiales."
                        ],
                        "correctIndex": 1,
                        "explanation": "El sol radiante, el deshielo andino y la marcada oscilación térmica día-noche permitieron una maduración fenólica perfecta."
                    },
                    {
                        "question": "¿Cómo se manifiesta el sincretismo cultural en la Quebrada de Humahuaca y los Valles Calchaquíes?",
                        "options": [
                            "En la desaparición total de las fiestas católicas en favor de cultos prehispánicos secretos.",
                            "En la prohibición legal de hablar lenguas originarias en las ceremonias agrícolas.",
                            "En la convivencia armónica entre la devoción católica y los rituales sagrados a la Pachamama.",
                            "En la sustitución del cultivo del maíz por trigo importado de las colonias galesas."
                        ],
                        "correctIndex": 2,
                        "explanation": "Las festividades católicas y la veneración a la Madre Tierra conviven de forma integrada en las familias de la quebrada."
                    },
                    {
                        "question": "¿Cuál fue una característica distintiva del asentamiento de los colonos galeses en el valle del río Chubut?",
                        "options": [
                            "La conquista militar violenta de los territorios tehuelches mediante fortines armados.",
                            "El establecimiento de relaciones comerciales y de amistad pacífica con las comunidades indígenas tehuelches.",
                            "La dedicación exclusiva a la minería de oro en las cumbres nevadas de la cordillera.",
                            "El abandono inmediato del idioma galés para adoptar el español como única lengua oficial."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los galeses sobrevivieron y prosperaron gracias a un pacto pacífico de auxilio mutuo con los tehuelches."
                    },
                    {
                        "question": "¿Qué contradicción histórica marcó el destino de Tierra del Fuego hacia finales del siglo XIX?",
                        "options": [
                            "La prosperidad ganadera ovina se erigió sobre el trágico etnocidio de las naciones originarias selk'nam y yámana.",
                            "El descubrimiento de petróleo en Ushuaia provocó una guerra civil entre estancieros y navegantes.",
                            "La negativa del gobierno nacional a reconocer la soberanía sobre el Estrecho de Magallanes.",
                            "El fracaso rotundo del presidio militar frente a las sublevaciones constantes de los reclusos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El auge lanero motivó la persecución letal y el exterminio de las poblaciones originarias que habitaban las estepas."
                    }
                ]
            }
        }
    }
    write_json("stories/world/b2/b2-argentinaregiones.json", stitched_story)

    # 6. Exercises (12 files)
    # 6 exercises per main lesson (1 to 6), 8 per consolidation (1 to 8)
    exercise_files = {
        # Core Unit 25
        "b2-25-01-ex": {
            "lesson": "b2-25-01",
            "exercises": [
                {
                    "id": "b2-25-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["dejar-de-infinitivo"],
                    "question": "¿Qué valor aspectual aporta la perífrasis 'dejar de + infinitivo' en la oración: 'El capataz dejó de exigir faenas nocturnas tras la tormenta'?",
                    "options": [
                        "Indica el inicio repentino e impulsivo de una nueva obligación laboral.",
                        "Señala la cesación o interrupción definitiva de una conducta previa.",
                        "Expresa la reiteración insistente de una orden a lo largo de la semana.",
                        "Denota una acción que se encuentra en pleno desarrollo progresivo."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-25-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["dejar-de-infinitivo"],
                    "sentence": "Cuando comprendió los peligros del lodazal pampeano, el joven arriero __ de cabalgar a oscuras.",
                    "answer": "dejo",
                    "english": "When he understood the dangers of the pampas quagmire, the young cattle drover stopped riding in the dark."
                },
                {
                    "id": "b2-25-01.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["dejar-de-infinitivo"],
                    "question": "¿Cuál es el sentido de la construcción negativa ponderativa 'no dejar de + infinitivo' en: 'Los peones no dejaron de admirar la destreza de Don Segundo'?",
                    "options": [
                        "Equivale a una prohibición tajante impuesta por las autoridades de la estancia.",
                        "Enfatiza la persistencia continua y la certeza indiscutible de su admiración.",
                        "Sugiere que los peones olvidaron rápidamente las hazañas del veterano resero.",
                        "Expresa que la admiración se interrumpió debido a desacuerdos técnicos."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-25-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["dejar-de-infinitivo"],
                    "sentence": "Aunque el viaje por las pampas sea extenuante, no __ de avisarnos cuando lleguen a la posta.",
                    "answer": "dejen",
                    "english": "Even though the journey across the pampas may be exhausting, do not fail to let us know when you reach the staging post."
                },
                {
                    "id": "b2-25-01.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-25-vocab"],
                    "pairs": [
                        ["el cese", "the cessation / stopping"],
                        ["el desistimiento", "the relinquishment / withdrawal"],
                        ["la claudicación", "the capitulation / giving in"],
                        ["el desapego", "the detachment / letting go"]
                    ]
                },
                {
                    "id": "b2-25-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Según el relato de Ricardo Güiraldes, ¿por qué Fabio Cáceres decide abandonar su pueblo natal?",
                    "options": [
                        "Porque cometió un delito grave y huye de la justicia local.",
                        "Porque busca seguir los pasos de Don Segundo para aprender el oficio y la dignidad del gaucho.",
                        "Porque sus tías le exigieron viajar a la capital para estudiar abogacía.",
                        "Porque la sequía destruyó por completo las haciendas de su familia."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-25-02-ex": {
            "lesson": "b2-25-02",
            "exercises": [
                {
                    "id": "b2-25-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["acabar-de-infinitivo"],
                    "question": "¿Cuál es la diferencia fundamental entre 'acabar de + infinitivo' y 'acabar por + infinitivo'?",
                    "options": [
                        "'Acabar de' expresa pasado inmediato reciente, mientras 'acabar por' denota desenlace final tras demoras o vacilaciones.",
                        "'Acabar de' exige subjuntivo en todas sus formas, mientras 'acabar por' solo admite indicativo.",
                        "'Acabar por' se utiliza únicamente para el clima, mientras 'acabar de' se aplica a personas.",
                        "Ambas perífrasis son sinónimas y completamente intercambiables sin variar el matiz temporal."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-25-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["acabar-de-infinitivo"],
                    "sentence": "El jinete mensajero __ de desmontar en la pulpería trayendo noticias frescas de la estancia vecina.",
                    "answer": "acaba",
                    "english": "The courier horseman has just dismounted at the pulpería bringing fresh news from the neighboring ranch."
                },
                {
                    "id": "b2-25-02.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["terminar-por-infinitivo"],
                    "question": "¿Qué expresa la perífrasis en: 'Tras resistirse durante semanas, los estancieros acabaron por aceptar el nuevo acuerdo tarifario'?",
                    "options": [
                        "Que el acuerdo fue rechazado definitivamente por ambas partes.",
                        "Que la decisión se tomó de inmediato sin debate ni resistencia previa.",
                        "Que se llegó a ese resultado como resolución forzosa tras un prolongado conflicto.",
                        "Que el acuerdo acaba de firmarse hace escasos segundos frente al juez."
                    ],
                    "correct": 2
                },
                {
                    "id": "b2-25-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["acabar-de-infinitivo"],
                    "sentence": "Hacía frío en la madrugada y el fogón del vivac acababa __ apagarse cuando ensillaron los caballos.",
                    "answer": "de",
                    "english": "It was cold at dawn and the bivouac fire had just gone out when they saddled the horses."
                },
                {
                    "id": "b2-25-02.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-25-vocab"],
                    "pairs": [
                        ["la culminación", "the culmination / completion"],
                        ["el desenlace", "the outcome / unraveling"],
                        ["la desembocadura", "the eventual ending / outlet"],
                        ["el remate", "the finishing touch / conclusion"]
                    ]
                },
                {
                    "id": "b2-25-02.ex06",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["acabar-de-infinitivo"],
                    "question": "¿Por qué es agramatical la oración: *'Los reseros acabaron de llegar hace cuatro años a la estancia'*?",
                    "options": [
                        "Porque 'acabar de' expresa inmediatez retrospectiva y no tolera complementos temporales lejanos.",
                        "Porque el verbo 'llegar' no puede funcionar como infinitivo principal.",
                        "Porque falta la preposición 'por' antes del complemento de tiempo.",
                        "Porque los sujetos colectivos como 'reseros' exigen el verbo en singular."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-25-03-ex": {
            "lesson": "b2-25-03",
            "exercises": [
                {
                    "id": "b2-25-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["terminar-por-infinitivo"],
                    "question": "¿Qué matiz aspectual distingue a 'terminar + gerundio' en: 'Aquel joven rebelde terminó convirtiéndose en el más leal capataz'?",
                    "options": [
                        "Subraya el estado o condición resultante en que desembocó un proceso prolongado.",
                        "Señala que la acción de convertirse fue fugaz e instantánea.",
                        "Indica que el sujeto dejó de ser capataz voluntariamente.",
                        "Expresa una orden perentoria dada por el dueño de la hacienda."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-25-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["terminar-por-infinitivo"],
                    "sentence": "Después de cruzar tres ríos crecidos, la tropa de novillos __ por calmarse en las lomas secas.",
                    "answer": "termino",
                    "english": "After crossing three flooded rivers, the herd of steers finally calmed down on the dry hills."
                },
                {
                    "id": "b2-25-03.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["terminar-por-infinitivo"],
                    "question": "¿En cuál de las siguientes opciones se utiliza 'terminar por + infinitivo' con valor de desenlace forzoso o resignado?",
                    "options": [
                        "Terminamos de cenar a las ocho en el comedor principal.",
                        "El potro chúcaro terminó por doblegar su resistencia ante la destreza del domador.",
                        "Los peones terminan sus tareas cotidianas antes del crepúsculo.",
                        "El contrato terminó ayer sin que mediara renovación alguna."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-25-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["terminar-por-infinitivo"],
                    "sentence": "Si continúas galopando sin herraduras por las piedras, terminarás __ a tu caballo favorito.",
                    "answer": "lastimando",
                    "english": "If you keep galloping without horseshoes across the stones, you will end up injuring your favorite horse."
                },
                {
                    "id": "b2-25-03.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-25-vocab"],
                    "pairs": [
                        ["la resignación", "the resignation / acceptance"],
                        ["la inevitabilidad", "the inevitability"],
                        ["el corolario", "the corollary / natural result"],
                        ["la decantación", "the gradual settling / clarifying"]
                    ]
                },
                {
                    "id": "b2-25-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cómo logra Fabio Cáceres superar los momentos de extenuación durante los arreos de ganado?",
                    "options": [
                        "Amenazando a los novillos con su facón para acelerar la marcha.",
                        "Encontrando en la mirada serena e imperturbable de Don Segundo la fuerza para sostenerse en la montura.",
                        "Regresando de inmediato a San Antonio de Areco para descansar en su rancho.",
                        "Exigiendo que otros peones asuman la responsabilidad del arreo."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-25-04-ex": {
            "lesson": "b2-25-04",
            "exercises": [
                {
                    "id": "b2-25-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-llegar-a-infinitivo"],
                    "question": "¿Qué valor expresa la perífrasis 'llegar a + infinitivo' en: 'Con disciplina espartana, Fabio llegó a dominar el arte del arreo'?",
                    "options": [
                        "Indica una obligación impuesta por las leyes civiles de la provincia.",
                        "Expresa la consecución de un hito culminante tras un proceso gradual de aprendizaje.",
                        "Señala la interrupción definitiva del oficio de resero.",
                        "Denota un desplazamiento físico hacia un lugar geográfico específico."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-25-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-llegar-a-infinitivo"],
                    "sentence": "Nadie en la pulpería imaginaba que aquel muchacho huérfano __ a ser el dueño de tan ricas estancias.",
                    "answer": "llegaria",
                    "english": "Nobody at the tavern imagined that that orphaned boy would come to be the owner of such rich ranches."
                },
                {
                    "id": "b2-25-04.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-llegar-a-infinitivo"],
                    "question": "¿Cuál es la función de 'llegar a + infinitivo' en una prótasis condicional como: 'Si llega a helar esta noche, encenderemos fogatas en el huerto'?",
                    "options": [
                        "Pondera una contingencia eventual como una posibilidad remota o crucial para la toma de medidas.",
                        "Afirma con total certeza matemática que la helada ya se ha producido.",
                        "Expresa un mandato imperativo dirigido al capataz de la hacienda.",
                        "Indica el cese definitivo de las bajas temperaturas invernales."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-25-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-llegar-a-infinitivo"],
                    "sentence": "La obra cumbre de Güiraldes llegó a __ como una de las cumbres de la literatura hispánica.",
                    "answer": "consagrarse",
                    "english": "Güiraldes's masterpiece came to be consecrated as one of the peaks of Hispanic literature."
                },
                {
                    "id": "b2-25-04.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-25-vocab"],
                    "pairs": [
                        ["el apogeo", "the apogee / height / peak"],
                        ["la consagración", "the ultimate recognition / consecration"],
                        ["el hito", "the milestone / landmark"],
                        ["la plenitud", "the fullness / peak state"]
                    ]
                },
                {
                    "id": "b2-25-04.ex06",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-llegar-a-infinitivo"],
                    "question": "¿En cuál de las siguientes frases 'llegar a + infinitivo' denota un límite extremo o insólito de conducta?",
                    "options": [
                        "Llegamos a la estancia antes de que cayera la noche.",
                        "En su cólera desmedida, el patrón llegó a negarle el jornal pactado al peón.",
                        "El tren llega a destino a las cuatro en punto de la tarde.",
                        "Llegaron a un acuerdo pacífico tras varias semanas de diálogo."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-25-05-ex": {
            "lesson": "b2-25-05",
            "exercises": [
                {
                    "id": "b2-25-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-dar-por-participio"],
                    "question": "¿Qué actitud epistémica expresa 'dar por sentado' en: 'No des por sentado que el cruce del río será fácil'?",
                    "options": [
                        "Asumir algo como un hecho indudable y obvio sin haberlo comprobado plenamente.",
                        "Confirmar mediante pruebas periciales que un documento es completamente falso.",
                        "Ordenar formalmente la detención judicial de un sospechoso.",
                        "Expresar tristeza y desánimo ante una pérdida económica irreparable."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-25-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-dar-por-participio"],
                    "sentence": "El juez de paz dio por __ el inventario de las tierras tras revisar detenidamente las escrituras.",
                    "answer": "concluido",
                    "english": "The justice of the peace considered the land inventory concluded after carefully reviewing the title deeds."
                },
                {
                    "id": "b2-25-05.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-dar-por-participio"],
                    "question": "¿Cómo concuerda el participio en la perífrasis 'dar por + participio'?",
                    "options": [
                        "Permanece siempre invariable en masculino singular sin excepción alguna.",
                        "Concuerda obligatoriamente en género y número con el complemento directo de la oración.",
                        "Concuerda exclusivamente con el sujeto gramatical de la cláusula principal.",
                        "Adopta únicamente formas irregulares derivadas del latín clásico."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-25-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-dar-por-participio"],
                    "sentence": "Tras buscar sin descanso por los bañados, los peones dieron por __ a las vacas extraviadas.",
                    "answer": "perdidas",
                    "english": "After searching relentlessly through the marshes, the ranch hands considered the lost cows as gone."
                },
                {
                    "id": "b2-25-05.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-25-vocab"],
                    "pairs": [
                        ["la presuposición", "the presupposition / assumption"],
                        ["la clausura", "the closure / definitive shutting"],
                        ["el veredicto", "the verdict / formal ruling"],
                        ["la constatación", "the verification / factual confirmation"]
                    ]
                },
                {
                    "id": "b2-25-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "En el desenlace de la novela, ¿por qué Don Segundo Sombra decide marcharse de la estancia de Fabio?",
                    "options": [
                        "Porque tuvo un enfrentamiento violento con el nuevo administrador de los campos.",
                        "Porque considera que su tutela terminó y su condición de gaucho libre le impide apegarse a los bienes materiales.",
                        "Porque las autoridades de la provincia le confiscaron sus caballos de tiro.",
                        "Porque Fabio le pidió explícitamente que se fuera para poder gobernar su herencia sin testigos."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-25-consolidation-ex": {
            "lesson": "b2-25-consolidation",
            "exercises": [
                {
                    "id": "b2-25-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["dejar-de-infinitivo", "acabar-de-infinitivo"],
                    "question": "¿Qué pareja de perífrasis completa adecuadamente la oración: 'El estanciero __ de desconfiar apenas el resero __ de entregar intacto todo el ganado'?",
                    "options": [
                        "dejó / acabó de",
                        "rompió a / se puso a",
                        "echó a / anduvo por",
                        "dio por / siguió de"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-25-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["terminar-por-infinitivo"],
                    "sentence": "Aunque al principio dudaba de sus dotes de arriero, el joven terminó __ ganarse el respeto de todos.",
                    "answer": "por",
                    "english": "Although at first he doubted his skills as a cattle drover, the young man finally earned everyone's respect."
                },
                {
                    "id": "b2-25-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-llegar-a-infinitivo", "perifrasis-dar-por-participio"],
                    "question": "¿Qué expresa la secuencia: 'Nadie pensó que llegaría a heredar las tierras, pero el juez dio por concluidas las disputas familiares'?",
                    "options": [
                        "Un hito culminante e insólito seguido de una resolución judicial que zanja definitivamente un proceso.",
                        "Una prohibición legal que impide el acceso a la propiedad privada en la provincia.",
                        "Un cese momentáneo de hostilidades que se reanudará en la próxima primavera.",
                        "Una hipótesis fantástica sin base documental en el archivo de la estancia."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-25-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-dar-por-participio"],
                    "sentence": "No des por __ que el viaje por las estepas patagónicas resultará exento de contratiempos.",
                    "answer": "hecho",
                    "english": "Do not take for granted that the journey across the Patagonian steppes will be free of setbacks."
                },
                {
                    "id": "b2-25-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["dejar-de-infinitivo"],
                    "question": "¿Cuál es la interpretación correcta de: 'El viento pampeano no dejó de soplar durante tres días consecutivos'?",
                    "options": [
                        "El viento sopló de manera ininterrumpida y persistente durante todo ese período.",
                        "El viento se detuvo de repente a la primera hora del amanecer.",
                        "Hizo tanto calor que el viento apenas se sintió en las copas de los ombúes.",
                        "El viento sopló solamente de forma intermitente durante unos breves instantes."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-25-consolidation.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["acabar-de-infinitivo"],
                    "sentence": "Los peones acababan de encender el fogón cuando el trueno __ a retumbar en el horizonte pampeano.",
                    "answer": "comenzo",
                    "english": "The ranch hands had just lit the campfire when thunder began to rumble on the pampas horizon."
                },
                {
                    "id": "b2-25-consolidation.ex07",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-25-vocab"],
                    "pairs": [
                        ["el cese definitivo", "the definitive cessation"],
                        ["la culminación del proceso", "the culmination of the process"],
                        ["el desenlace forzoso", "the inevitable outcome"],
                        ["el logro del hito", "the achievement of the milestone"]
                    ]
                },
                {
                    "id": "b2-25-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es el mensaje filosófico que Don Segundo Sombra transmite a Fabio Cáceres antes de su partida final?",
                    "options": [
                        "Que la libertad interior y la rectitud moral no dependen de las posesiones materiales que se administren.",
                        "Que un verdadero gaucho debe renegar de cualquier instrucción escolar o documento legal.",
                        "Que la única forma de felicidad consiste en abandonar la patria y viajar hacia tierras lejanas.",
                        "Que el poder económico es el único instrumento legítimo para imponer justicia en las pampas."
                    ],
                    "correct": 0
                }
            ]
        },

        # Regional Unit 25 (Argentina II: b2-argentinaregiones)
        "b2-argentinaregiones-01-ex": {
            "lesson": "b2-argentinaregiones-01",
            "exercises": [
                {
                    "id": "b2-argentinaregiones-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-si-bien"],
                    "question": "¿Qué modo verbal rige obligatoriamente el conector concesivo formal 'si bien' en la prosa culta?",
                    "options": [
                        "Modo indicativo, pues introduce una objeción que se presenta como un hecho indudable y constatado.",
                        "Modo subjuntivo en todos los casos por tratarse de una cláusula concesiva.",
                        "Infinitivo compuesto precedido de preposición temporal obligatoria.",
                        "Imperativo afirmativo con pronombre enclítico adherido al final."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-si-bien"],
                    "sentence": "Si bien la llanura pampeana __ un suelo de excepcional fertilidad, exige una labor ganadera constante.",
                    "answer": "posee",
                    "english": "Although the pampas plain possesses an exceptionally fertile soil, it demands constant livestock labor."
                },
                {
                    "id": "b2-argentinaregiones-01.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-si-bien"],
                    "question": "¿Qué relación argumentativa establece 'si bien' en: 'Si bien el Martín Fierro nació como protesta social, fue canonizado como poema patrio'?",
                    "options": [
                        "Expresa una condición hipotética sin valor en el mundo real.",
                        "Concede un hecho verificado para inmediatamente contraponer una afirmación de mayor peso histórico.",
                        "Señala la causa biológica de la extinción del nomadismo gaucho.",
                        "Indica una consecuencia puramente cronológica entre dos acontecimientos desvinculados."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-argentinaregiones-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-si-bien"],
                    "sentence": "El alambrado transformó las estancias, si bien la memoria del gaucho libre __ viva en la tradición.",
                    "answer": "sigue",
                    "english": "The wire fencing transformed the ranches, although the memory of the free gaucho remains alive in tradition."
                },
                {
                    "id": "b2-argentinaregiones-01.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinaregiones-vocab"],
                    "pairs": [
                        ["la llanura pampeana", "the fertile pampas plain"],
                        ["la payada criolla", "the improvised sung poetic duel"],
                        ["el arreo de hacienda", "the cattle drive / herding"],
                        ["el facón gaucho", "the traditional gaucho dagger"]
                    ]
                },
                {
                    "id": "b2-argentinaregiones-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál fue el impacto social y literario central del poema 'El gaucho Martín Fierro' de José Hernández?",
                    "options": [
                        "Promover la llegada masiva de ferrocarriles británicos a las provincias del interior.",
                        "Denunciar los abusos de las levas militares forzosas y defender la dignidad humana del gaucho marginado.",
                        "Fomentar la emigración de los peones rurales hacia los conventillos de la capital porteña.",
                        "Exigir la prohibición definitiva del canto payadoril en las pulperías de frontera."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-argentinaregiones-02-ex": {
            "lesson": "b2-argentinaregiones-02",
            "exercises": [
                {
                    "id": "b2-argentinaregiones-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-aun-cuando"],
                    "question": "¿Cuándo exige modo subjuntivo la locución concesiva 'aun cuando'?",
                    "options": [
                        "Cuando introduce un hecho plenamente constatado en el presente del hablante.",
                        "Cuando se proyecta hacia una hipótesis incierta, un escenario futuro o una objeción desestimada por extrema.",
                        "Únicamente cuando se ubica al final de oraciones interrogativas directas.",
                        "Siempre que el verbo principal esté conjugado en pretérito indefinido."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-argentinaregiones-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-aun-cuando"],
                    "sentence": "Aun cuando las lluvias anuales __ escasas en Cuyo, el agua de deshielo asegura la irrigación de los viñedos.",
                    "answer": "son",
                    "english": "Even though annual rainfall is scarce in Cuyo, snowmelt water ensures the irrigation of the vineyards."
                },
                {
                    "id": "b2-argentinaregiones-02.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-aun-cuando"],
                    "question": "¿Por qué se utiliza el subjuntivo en: 'Aun cuando caigan heladas tardías en el Valle de Uco, los sistemas de aspersión protegerán las cepas'?",
                    "options": [
                        "Porque la helada tardía se plantea como una posibilidad contingente y futura, no como una certeza actual.",
                        "Porque el hablante desea fervientemente que las heladas destruyan la cosecha.",
                        "Porque las oraciones concesivas en Mendoza rechazan por ley el modo indicativo.",
                        "Porque el verbo 'caer' es irregular y no posee formas del modo indicativo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-aun-cuando"],
                    "sentence": "Aun cuando los costos de producción __ elevados, los bodegueros continuarán apostando por la crianza en roble.",
                    "answer": "sean",
                    "english": "Even though production costs may be high, winemakers will continue betting on aging in oak."
                },
                {
                    "id": "b2-argentinaregiones-02.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinaregiones-vocab"],
                    "pairs": [
                        ["el oasis de riego", "the irrigated valley oasis"],
                        ["la acequia milenaria", "the ancient irrigation canal"],
                        ["el terruño pedregoso", "the stony terroir / native soil"],
                        ["la fiesta de la vendimia", "the grape harvest festival"]
                    ]
                },
                {
                    "id": "b2-argentinaregiones-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién introdujo la cepa Malbec en Mendoza en 1853 y cuál fue su impacto en la región?",
                    "options": [
                        "El naturalista Charles Darwin durante su cruce de la cordillera de los Andes.",
                        "El agrónomo francés Michel Aimé Pouget, permitiendo que la uva floreciera con un perfil organoléptico superior al europeo.",
                        "El libertador José de San Martín para financiar el Ejército de los Andes.",
                        "Los misioneros jesuitas antes de su expulsión a finales del siglo dieciocho."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-argentinaregiones-03-ex": {
            "lesson": "b2-argentinaregiones-03",
            "exercises": [
                {
                    "id": "b2-argentinaregiones-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["conectores-concesivos-adversativos"],
                    "question": "¿Qué función cumple el conector 'si bien es cierto que' en la argumentación formal?",
                    "options": [
                        "Concede de manera explícita un argumento preliminar para introducir a continuación una objeción decisiva.",
                        "Niega tajantemente la veracidad de la proposición que lo precede.",
                        "Formula una pregunta retórica dirigida a los habitantes de los valles andinos.",
                        "Introduce un ejemplo aislado sin relación con la tesis del párrafo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["conectores-concesivos-adversativos"],
                    "sentence": "Los valles calchaquíes sufren un aislamiento secular; no __, su producción artesanal y enológica es reconocida mundialmente.",
                    "answer": "obstante",
                    "english": "The Calchaquí Valleys suffer centuries-old isolation; nevertheless, their artisanal and wine production is world renowned."
                },
                {
                    "id": "b2-argentinaregiones-03.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["conectores-concesivos-adversativos"],
                    "question": "¿Cómo se puntúan conectores parentéticos como 'con todo' y 'no obstante' cuando van al inicio de una oración coordinada?",
                    "options": [
                        "Se colocan entre signos de admiración para enfatizar la sorpresa.",
                        "Van seguidos obligatoriamente de una coma que los aísla del resto del enunciado.",
                        "Deben escribirse en cursiva y sin ninguna marca de puntuación posterior.",
                        "Se unen mediante guiones a la primera palabra de la cláusula subordinada."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-argentinaregiones-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["conectores-concesivos-adversativos"],
                    "sentence": "Las capillas de adobe son vulnerables a las inclemencias sísmicas; con __, han resistido varios siglos en pie.",
                    "answer": "todo",
                    "english": "The adobe chapels are vulnerable to seismic shocks; all the same, they have stood firm for several centuries."
                },
                {
                    "id": "b2-argentinaregiones-03.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinaregiones-vocab"],
                    "pairs": [
                        ["el pucará de piedra", "the pre-Columbian stone fortress"],
                        ["la devoción a la pachamama", "the devotion to Mother Earth"],
                        ["la quebrada tectónica", "the tectonic canyon / ravine"],
                        ["el cardón centenario", "the ancient columnar cactus"]
                    ]
                },
                {
                    "id": "b2-argentinaregiones-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué práctica ritual tradicional celebran las comunidades andinas del noroeste argentino cada primero de agosto?",
                    "options": [
                        "La inauguración de nuevas acequias de cemento para desviar el río Grande.",
                        "La ceremonia de la corpachada para alimentar y sahumar a la Pachamama en agradecimiento por su fertilidad.",
                        "Una carrera de caballos criollos a lo largo de las terrazas de Purmamarca.",
                        "La quema solemne de instrumentos musicales coloniales en la plaza de Tilcara."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-argentinaregiones-04-ex": {
            "lesson": "b2-argentinaregiones-04",
            "exercises": [
                {
                    "id": "b2-argentinaregiones-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-pese-a"],
                    "question": "¿Qué elemento sintáctico sigue directamente a la locución preposicional concesiva 'pese a' en: 'Pese al viento incesante, el barco zarpó'?",
                    "options": [
                        "Un sintagma nominal que sintetiza la objeción o dificultad superada.",
                        "Un verbo conjugado en imperfecto de subjuntivo con pronombre enclítico.",
                        "Una conjunción disyuntiva que abre dos alternativas excluyentes.",
                        "Un adverbio de lugar que indica la distancia hacia la costa."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-pese-a"],
                    "sentence": "Pese a las bajas temperaturas del invierno patagónico, el glaciar Perito Moreno mantiene un dinamismo __.",
                    "answer": "constante",
                    "english": "In spite of the low temperatures of the Patagonian winter, the Perito Moreno glacier maintains a constant dynamism."
                },
                {
                    "id": "b2-argentinaregiones-04.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-pese-a"],
                    "question": "¿Qué condición suele exigirse para utilizar 'pese a + infinitivo' en lugar de 'pese a que + verbo conjugado'?",
                    "options": [
                        "Que el sujeto del infinitivo coincida con el sujeto gramatical de la oración principal.",
                        "Que la oración se refiera únicamente a sucesos ocurridos en el siglo diecinueve.",
                        "Que el verbo de la cláusula principal pertenezca a la primera conjugación.",
                        "Que no existan adjetivos calificativos en el predicado."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-pese-a"],
                    "sentence": "Pese a no contar con experiencia previa en suelos áridos, los colonos galeses __ prosperar en el valle del Chubut.",
                    "answer": "lograron",
                    "english": "In spite of not having previous experience in arid soils, the Welsh settlers managed to prosper in the Chubut valley."
                },
                {
                    "id": "b2-argentinaregiones-04.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinaregiones-vocab"],
                    "pairs": [
                        ["el ventisquero andino", "the Andean snowfield glacier"],
                        ["el desprendimiento de hielo", "the ice detachment / calving"],
                        ["la estepa infinita", "the boundless cold steppe"],
                        ["la estancia ovina", "the sheep breeding ranch"]
                    ]
                },
                {
                    "id": "b2-argentinaregiones-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cómo lograron sobrevivir los primeros inmigrantes galeses que llegaron a las costas de Chubut en 1865?",
                    "options": [
                        "Comprando provisiones en las bases navales británicas de las islas Malvinas.",
                        "Estableciendo un histórico pacto de amistad y comercio pacífico con los pueblos originarios tehuelches.",
                        "Construyendo fábricas de cerveza en las orillas del lago Argentino.",
                        "Regresando de inmediato a Europa tras el primer invierno en el Mimosa."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-argentinaregiones-05-ex": {
            "lesson": "b2-argentinaregiones-05",
            "exercises": [
                {
                    "id": "b2-argentinaregiones-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-por-adj-que"],
                    "question": "¿Qué valor expresa la estructura intensiva 'por + adjetivo + que + subjuntivo' en: 'Por recias que sean las borrascas del cabo de Hornos, el barco zarpará'?",
                    "options": [
                        "Afirma una concesión escalar máxima: sin importar cuán intensas sean las tormentas, no impedirán la partida.",
                        "Indica que el barco solo zarpará si el cielo está completamente despejado y sin viento.",
                        "Expresa una causa directa por la cual la tripulación decidió cancelar la navegación.",
                        "Señala una comparación de igualdad matemática entre dos borrascas distintas."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-por-adj-que"],
                    "sentence": "Por inhóspito que __ el archipiélago fueguino, los pueblos originarios convivieron en armonía con su entorno.",
                    "answer": "fuera",
                    "english": "However inhospitable the Fuegian archipelago might have been, the native peoples lived in harmony with their environment."
                },
                {
                    "id": "b2-argentinaregiones-05.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-por-adj-que"],
                    "question": "¿Cómo debe concordar el adjetivo en construcciones como 'por + adjetivo + que + subjuntivo'?",
                    "options": [
                        "Debe concordar obligatoriamente en género y número con el sustantivo al que califica en la cláusula.",
                        "Permanece siempre en forma neutra invariable terminada en vocal o consonante.",
                        "Concuerda exclusivamente con el sujeto de la cláusula principal del enunciado.",
                        "Se convierte obligatoriamente en un adverbio terminado en el sufijo '-mente'."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-por-adj-que"],
                    "sentence": "Por distantes que se __ las costas antárticas, el puerto de Ushuaia ejerce una atracción constante.",
                    "answer": "encuentren",
                    "english": "However distant the Antarctic coasts may be, the port of Ushuaia exerts a constant attraction."
                },
                {
                    "id": "b2-argentinaregiones-05.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinaregiones-vocab"],
                    "pairs": [
                        ["el confin austral", "the southernmost border / edge"],
                        ["la turbera milenaria", "the ancient peat bog"],
                        ["el presidio historico", "the historic penal colony"],
                        ["la borrasca subpolar", "the subpolar storm / tempest"]
                    ]
                },
                {
                    "id": "b2-argentinaregiones-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué factor histórico provocó la trágica desaparición demográfica de los pueblos originarios selk'nam a finales del siglo XIX?",
                    "options": [
                        "Una erupción volcánica submarina en las aguas del Canal Beagle.",
                        "La expansión ganadera ovina y las cacerías remuneradas organizadas por estancieros y buscadores de oro.",
                        "La emigración voluntaria masiva hacia las ciudades del norte de Chile.",
                        "Un conflicto armado generalizado entre los nómadas canoeros y los cazadores de guanacos."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-argentinaregiones-consolidation-ex": {
            "lesson": "b2-argentinaregiones-consolidation",
            "exercises": [
                {
                    "id": "b2-argentinaregiones-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-si-bien", "concesivas-aun-cuando"],
                    "question": "¿Qué opción combina correctamente los modos indicativo y subjuntivo en una estructura concesiva compleja?",
                    "options": [
                        "Si bien el clima cuyano es árido, aun cuando las heladas amenacen la vid, los viñedos prosperan.",
                        "Si bien el clima cuyano sea árido, aun cuando las heladas amenazan la vid, los viñedos prosperan.",
                        "Si bien el clima cuyano fuera árido, aun cuando las heladas amenazaron la vid, los viñedos prosperan.",
                        "Si bien el clima cuyano sea árido, aun cuando las heladas amenazaren la vid, los viñedos prosperan."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-si-bien"],
                    "sentence": "Si bien la Argentina moderna __ en gran medida una sociedad urbana, las raíces del interior definen su identidad.",
                    "answer": "es",
                    "english": "Although modern Argentina is largely an urban society, the roots of the interior define its identity."
                },
                {
                    "id": "b2-argentinaregiones-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["conectores-concesivos-adversativos", "concesivas-pese-a"],
                    "question": "¿Cuál es la función sintáctica de 'pese a' en contraste con conectores coordinantes como 'no obstante'?",
                    "options": [
                        "'Pese a' es una locución preposicional que introduce sintagmas nominales o infinitivos, mientras 'no obstante' enlaza enunciados completos.",
                        "'Pese a' solo se utiliza en poesía gauchesca y 'no obstante' en documentos judiciales.",
                        "'Pese a' rige imperativo y 'no obstante' únicamente subjuntivo pretérito.",
                        "Ambos conectores son idénticos en categoría y exigen siempre punto y coma previo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["concesivas-por-adj-que"],
                    "sentence": "Por rigurosas que __ las condiciones del clima austral, los habitantes de Ushuaia defienden con fervor su terruño.",
                    "answer": "sean",
                    "english": "However harsh the conditions of the southern climate may be, the inhabitants of Ushuaia fiercely defend their homeland."
                },
                {
                    "id": "b2-argentinaregiones-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["concesivas-pese-a"],
                    "question": "¿Cuál de las siguientes oraciones utiliza 'pese a' de manera correcta y elegante en prosa formal?",
                    "options": [
                        "Pese a las distancias abismales de la Patagonia, las comunidades preservan un activo intercambio cultural.",
                        "Pese a que si llueve mucho en la cordillera, los caminos se cortan con facilidad.",
                        "Los arrieros viajaron pese a que porque no tenían otro remedio para salvar la hacienda.",
                        "Pese a muy ventoso que sea el tiempo, saldremos a caballo por los médanos."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinaregiones-consolidation.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["conectores-concesivos-adversativos"],
                    "sentence": "Las tradiciones gauchas sufrieron el impacto de la mecanización; aun __, el asado y la doma conservan su vigencia.",
                    "answer": "asi",
                    "english": "Gaucho traditions suffered the impact of mechanization; even so, the asado and horse-breaking retain their relevance."
                },
                {
                    "id": "b2-argentinaregiones-consolidation.ex07",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinaregiones-vocab"],
                    "pairs": [
                        ["el pastizal pampeano", "the pampas pasture grassland"],
                        ["la amplitud termica", "the daily temperature range"],
                        ["el sincretismo andino", "the Andean cultural syncretism"],
                        ["el frente del glaciar", "the glacier front terminus"]
                    ]
                },
                {
                    "id": "b2-argentinaregiones-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la conclusión integradora que plantea el texto de consolidación regional sobre la identidad argentina?",
                    "options": [
                        "Que la riqueza nacional radica en la polifonía de sus contrastes geográficos, desde los valles andinos hasta los hielos australes.",
                        "Que el progreso económico solo es posible si se suprimen las particularidades culturales del interior.",
                        "Que la identidad se reduce exclusivamente a las expresiones urbanas y tangueras del Río de la Plata.",
                        "Que las regiones desérticas de la Patagonia carecen de valor patrimonial frente a la fertilidad pampeana."
                    ],
                    "correct": 0
                }
            ]
        }
    }

    for ex_stem, ex_obj in exercise_files.items():
        write_json(f"exercises/b2/{ex_stem}.json", ex_obj)

    # 7. Lessons (12 files)
    # Core Lessons: b2-25
    core_lessons = [
        ("b2-25-01", "La cesación y la pausa: Dejar de + infinitivo", "b2-25-01-a-gr", "b2-25-01-voc", "b2-25-01-ex", "stories/classics/b2/b2-25.json"),
        ("b2-25-02", "Del desenlace inmediato al término forzoso: Acabar de vs. Acabar por", "b2-25-02-a-gr", "b2-25-02-voc", "b2-25-02-ex", None),
        ("b2-25-03", "La culminación del proceso: Terminar por + infinitivo y Terminar + gerundio", "b2-25-03-a-gr", "b2-25-03-voc", "b2-25-03-ex", None),
        ("b2-25-04", "El alcance de hitos y límites extremos: Llegar a + infinitivo", "b2-25-04-a-gr", "b2-25-04-voc", "b2-25-04-ex", None),
        ("b2-25-05", "Veredictos y estados concluidos: Dar por + participio", "b2-25-05-a-gr", "b2-25-05-voc", "b2-25-05-ex", None)
    ]

    for stem, title, gr_stem, voc_stem, ex_stem, story_ref in core_lessons:
        sections = []
        if story_ref:
            sections.append({"type": "story", "ref": story_ref})
        sections.append({"type": "grammar", "ref": f"grammar/b2/{gr_stem}.json"})
        sections.append({"type": "vocabulary", "ref": f"vocabulary/b2/{voc_stem}.json"})
        sections.append({"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{ex_stem}.json", "exerciseRefs": [f"{stem}.ex0{i}" for i in range(1, 7)]})

        write_json(f"lessons/b2/{stem}.json", {
            "id": f"lesson.{stem.replace('-', '.')}",
            "title": title,
            "level": "B2",
            "sections": sections
        })

    # Core Consolidation
    write_json("lessons/b2/b2-25-consolidation.json", {
        "id": "lesson.b2.25.consolidation",
        "title": "Consolidación: Perífrasis de término y resultado",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Dominar con precisión las perífrasis de fase terminativa y resultativa (dejar de, acabar de/por, terminar por, llegar a, dar por).",
                "Diferenciar matices aspectuales de inmediatez retrospectiva, culminación forzada y alcance de hitos.",
                "Integrar el vocabulario avanzado sobre transiciones, desenlaces y juicios concluidos en prosa formal."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-25-consolidation-ex.json", "exerciseRefs": [f"b2-25-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Distingo con soltura entre 'acabar de + infinitivo' (pasado inmediato) y 'acabar por + infinitivo' (desenlace final).",
                "Utilizo 'dejar de + infinitivo' tanto para la interrupción de hábitos como en fórmulas ponderativas negativas ('no dejar de').",
                "Empleo 'llegar a + infinitivo' para expresar hitos culminantes y contingencias hipotéticas relevantes.",
                "Aplico la concordancia de género y número en colocaciones con 'dar por + participio' ('dar por sentado/hecho/concluido').",
                "Analizo textos literarios gauchescos apreciando los valores aspectuales de cambio y término."
            ]}
        ]
    })

    # Regional Lessons: b2-argentinaregiones
    regional_lessons = [
        ("b2-argentinaregiones-01", "La llanura pampeana y el mito del gaucho", "b2-argentinaregiones-01-a-gr", "b2-argentinaregiones-01-voc", "b2-argentinaregiones-01-ex", "stories/world/b2/b2-argentinaregiones-01.json"),
        ("b2-argentinaregiones-02", "Mendoza y el oasis del Malbec: Vitivinicultura al pie de los Andes", "b2-argentinaregiones-02-a-gr", "b2-argentinaregiones-02-voc", "b2-argentinaregiones-02-ex", "stories/world/b2/b2-argentinaregiones-02.json"),
        ("b2-argentinaregiones-03", "La Quebrada de Humahuaca y los valles calchaquíes", "b2-argentinaregiones-03-a-gr", "b2-argentinaregiones-03-voc", "b2-argentinaregiones-03-ex", "stories/world/b2/b2-argentinaregiones-03.json"),
        ("b2-argentinaregiones-04", "La Patagonia austral: Glaciar Perito Moreno y los colonos galeses", "b2-argentinaregiones-04-a-gr", "b2-argentinaregiones-04-voc", "b2-argentinaregiones-04-ex", "stories/world/b2/b2-argentinaregiones-04.json"),
        ("b2-argentinaregiones-05", "Tierra del Fuego y Ushuaia: La ciudad del fin del mundo", "b2-argentinaregiones-05-a-gr", "b2-argentinaregiones-05-voc", "b2-argentinaregiones-05-ex", "stories/world/b2/b2-argentinaregiones-05.json")
    ]

    for stem, title, gr_stem, voc_stem, ex_stem, story_ref in regional_lessons:
        write_json(f"lessons/b2/{stem}.json", {
            "id": f"lesson.{stem.replace('-', '.')}",
            "title": title,
            "level": "B2",
            "sections": [
                {"type": "story", "ref": story_ref},
                {"type": "grammar", "ref": f"grammar/b2/{gr_stem}.json"},
                {"type": "vocabulary", "ref": f"vocabulary/b2/{voc_stem}.json"},
                {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{ex_stem}.json", "exerciseRefs": [f"{stem}.ex0{i}" for i in range(1, 7)]}
            ]
        })

    # Regional Consolidation
    write_json("lessons/b2/b2-argentinaregiones-consolidation.json", {
        "id": "lesson.b2.argentinaregiones.consolidation",
        "title": "Consolidación: El vasto mapa argentino",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Integrar la visión geográfica, humana y cultural de los diversos terruños y regiones argentinas.",
                "Consolidar el léxico especializado de la pampa, la vitivinicultura andina, el noroeste prehispánico y la Patagonia austral.",
                "Dominar el repertorio de estructuras concesivas cultas (si bien, aun cuando, conectores parentéticos, pese a, por + adj + que)."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b2/b2-argentinaregiones-consolidation.json"},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-argentinaregiones-consolidation-ex.json", "exerciseRefs": [f"b2-argentinaregiones-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Reconozco la trascendencia del mito gaucho y su evolución poética desde el Martín Fierro.",
                "Comprendo la ingeniería hidráulica de las acequias mendocinas y el éxito del Malbec de altura.",
                "Identifico la riqueza geológica y el sincretismo andino de la Quebrada de Humahuaca y los Valles Calchaquíes.",
                "Analizo la dinámica glaciológica del Perito Moreno y la gesta comunitaria de los colonos galeses en Chubut.",
                "Comprendo el drama histórico de los pueblos fueguinos y el rol estratégico de Ushuaia como enclave antártico.",
                "Aplico con precisión las diferentes estructuras concesivas según el grado de factualidad e hipótesis requeridos."
            ]}
        ]
    })

    # 8. Update content/es-latam/curriculum/units/b2.json
    def update_curriculum_units(units):
        existing_titles = {u.get("title") for u in units}
        new_units = [
            {
                "title": "Terminative & Resultative Periphrases",
                "stems": [
                    "b2-25-01",
                    "b2-25-02",
                    "b2-25-03",
                    "b2-25-04",
                    "b2-25-05",
                    "b2-25-consolidation"
                ],
                "track": "core"
            },
            {
                "title": "Argentina II: The Pampas, Patagonia & Regional Terroirs",
                "stems": [
                    "b2-argentinaregiones-01",
                    "b2-argentinaregiones-02",
                    "b2-argentinaregiones-03",
                    "b2-argentinaregiones-04",
                    "b2-argentinaregiones-05",
                    "b2-argentinaregiones-consolidation"
                ],
                "track": "regional"
            }
        ]
        for nu in new_units:
            if nu["title"] not in existing_titles:
                units.append(nu)
        return units

    update_json_file(os.path.join(LATAM_DIR, "curriculum", "units", "b2.json"), update_curriculum_units)
    print("Updated curriculum/units/b2.json with Unit 25!")

if __name__ == "__main__":
    main()
