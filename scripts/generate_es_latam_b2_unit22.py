#!/usr/bin/env python3
"""
Generate Latin American Spanish (es-latam) B2 Unit 22:
- Core Unit 22: Verbs of Becoming & Transformation (Verbos de cambio y transformación)
  Classic literature: Baldomero Lillo - Sub terra (Relato: El chiflón del diablo) (1904)
- Regional Unit 22: Chile I: The Central Valley, Valparaíso & The Great Poets (b2-chilecentro)
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LATAM_DIR = ROOT / "content" / "es-latam"

def count_words(text):
    return len(re.findall(r'[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ]+', text))

def write_json(rel_path, data):
    p = LATAM_DIR / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {p.relative_to(ROOT)}")

def main():
    c_unit = "b2-22"
    r_unit = "b2-chilecentro"

    c1, c2, c3, c4, c5, l6_con = [f"{c_unit}-0{i}" for i in range(1, 6)] + [f"{c_unit}-consolidation"]
    r1, r2, r3, r4, r5, r6_con = [f"{r_unit}-0{i}" for i in range(1, 6)] + [f"{r_unit}-consolidation"]

    # -------------------------------------------------------------------------
    # 0. UPDATE REGISTRY & GRAMMAR TITLES
    # -------------------------------------------------------------------------
    reg_path = LATAM_DIR / "indexes" / "skill-registry.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    skills = registry.setdefault("skills", {})

    new_skills = {
        "b2-22-vocab": {"kind": "vocabulary", "level": "B2"},
        "verbos-cambio-ponerse-quedarse": {"kind": "grammar", "level": "B2"},
        "verbos-cambio-hacerse-volverse": {"kind": "grammar", "level": "B2"},
        "verbos-cambio-convertirse-transformarse": {"kind": "grammar", "level": "B2"},
        "verbos-cambio-llegar-a-ser": {"kind": "grammar", "level": "B2"},
        "seleccion-estilistica-verbos-cambio": {"kind": "grammar", "level": "B2"},
        "sintesis-verbos-de-cambio": {"kind": "grammar", "level": "B2"},
        "b2-chilecentro-vocab": {"kind": "vocabulary", "level": "B2"},
        "chile-vallecentral-geografia-clima": {"kind": "grammar", "level": "B2"},
        "chile-valparaiso-puerto-patrimonio": {"kind": "grammar", "level": "B2"},
        "chile-mistral-neruda-poesia": {"kind": "grammar", "level": "B2"},
        "chile-moneda-golpe-memoria": {"kind": "grammar", "level": "B2"},
        "chile-transicion-estallido-ciudadania": {"kind": "grammar", "level": "B2"},
        "chile-centro-sintesis-regional": {"kind": "grammar", "level": "B2"}
    }

    for k, v in new_skills.items():
        skills[k] = v

    reg_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated skill-registry.json for Unit 22")

    gt_path = LATAM_DIR / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))

    new_titles = {
        "verbos-cambio-ponerse-quedarse": "verbs of becoming expressing temporary state or reaction",
        "verbos-cambio-hacerse-volverse": "verbs of becoming expressing gradual or involuntary transformation",
        "verbos-cambio-convertirse-transformarse": "verbs of radical conversion and category transformation",
        "verbos-cambio-llegar-a-ser": "verbs of culmination achievement and progressive arrival",
        "seleccion-estilistica-verbos-cambio": "stylistic selection and nuance in verbs of change",
        "sintesis-verbos-de-cambio": "synthesis of verbs of transformation and becoming",
        "chile-vallecentral-geografia-clima": "narrative aspect and imperfective backgrounding in central valley geography",
        "chile-valparaiso-puerto-patrimonio": "spatial and relative structures in port architecture and bohemian urbanism",
        "chile-mistral-neruda-poesia": "poetic modality and evaluative structures in great literary legacies",
        "chile-moneda-golpe-memoria": "retrospective temporal sequencing in pivotal historical trauma",
        "chile-transicion-estallido-ciudadania": "discourse connectors of opposition and cause in modern civic mobilizations",
        "chile-centro-sintesis-regional": "advanced discourse synthesis in central chilean poetry and history"
    }

    for k, v in new_titles.items():
        gt[k] = v

    gt_path.write_text(json.dumps(gt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json for Unit 22")

    # -------------------------------------------------------------------------
    # 1. VOCABULARY FILES (10 files)
    # -------------------------------------------------------------------------
    vocab_data = {
        f"{c_unit}-01": {
            "id": "vocab.b2.22.01",
            "lesson": f"{c_unit}-01",
            "title": "Cambios transitorios, reacciones y estados resultantes",
            "words": [
                {"lemma": "ponerse", "translation": "to become (sudden, emotional, temporary)", "pos": "verb"},
                {"lemma": "quedarse", "translation": "to end up, be left in state", "pos": "verb"},
                {"lemma": "mutabilidad", "translation": "mutability / changeability", "pos": "noun"},
                {"lemma": "transitorio", "translation": "transitory / temporary", "pos": "adjective"},
                {"lemma": "enrojecer", "translation": "to blush / turn red", "pos": "verb"},
                {"lemma": "desconcierto", "translation": "bewilderment / confusion", "pos": "noun"},
                {"lemma": "ensombrecer", "translation": "to overshadow / darken mood", "pos": "verb"},
                {"lemma": "aturdimiento", "translation": "daze / numbness", "pos": "noun"},
                {"lemma": "perplejo", "translation": "perplexed / baffled", "pos": "adjective"}
            ]
        },
        f"{c_unit}-02": {
            "id": "vocab.b2.22.02",
            "lesson": f"{c_unit}-02",
            "title": "Transformaciones graduales, ideológicas y de carácter",
            "words": [
                {"lemma": "volverse", "translation": "to become (involuntary, lasting character shift)", "pos": "verb"},
                {"lemma": "hacerse", "translation": "to become (voluntary, ideological, profession)", "pos": "verb"},
                {"lemma": "paulatino", "translation": "gradual / step by step", "pos": "adjective"},
                {"lemma": "involuntario", "translation": "involuntary", "pos": "adjective"},
                {"lemma": "idiosincrasia", "translation": "idiosyncrasy / distinctive character", "pos": "noun"},
                {"lemma": "escéptico", "translation": "skeptical", "pos": "adjective"},
                {"lemma": "arraigo", "translation": "deep rootedness / attachment", "pos": "noun"},
                {"lemma": "intransigente", "translation": "uncompromising / intransigent", "pos": "adjective"},
                {"lemma": "militancia", "translation": "political activism / membership", "pos": "noun"}
            ]
        },
        f"{c_unit}-03": {
            "id": "vocab.b2.22.03",
            "lesson": f"{c_unit}-03",
            "title": "Metamorfosis radical y cambio de naturaleza",
            "words": [
                {"lemma": "convertirse", "translation": "to turn into / become (radical shift)", "pos": "verb"},
                {"lemma": "transformarse", "translation": "to transform into", "pos": "verb"},
                {"lemma": "metamorfosis", "translation": "metamorphosis", "pos": "noun"},
                {"lemma": "conversión", "translation": "conversion / change of nature", "pos": "noun"},
                {"lemma": "mutación", "translation": "mutation / structural change", "pos": "noun"},
                {"lemma": "reconfigurar", "translation": "to reconfigure / reshape", "pos": "verb"},
                {"lemma": "paradigma", "translation": "paradigm", "pos": "noun"},
                {"lemma": "transmutar", "translation": "to transmute", "pos": "verb"},
                {"lemma": "trascendencia", "translation": "transcendence / historical scope", "pos": "noun"}
            ]
        },
        f"{c_unit}-04": {
            "id": "vocab.b2.22.04",
            "lesson": f"{c_unit}-04",
            "title": "Culminación, trayectoria y logro progresivo",
            "words": [
                {"lemma": "llegar a ser", "translation": "to eventually become through effort", "pos": "verb"},
                {"lemma": "culminación", "translation": "culmination / pinnacle", "pos": "noun"},
                {"lemma": "consagración", "translation": "definitive recognition / triumph", "pos": "noun"},
                {"lemma": "trayectoria", "translation": "career trajectory / path", "pos": "noun"},
                {"lemma": "empeño", "translation": "tenacious effort / determination", "pos": "noun"},
                {"lemma": "perseverancia", "translation": "perseverance", "pos": "noun"},
                {"lemma": "cúspide", "translation": "peak / summit", "pos": "noun"},
                {"lemma": "itinerario", "translation": "itinerary / development path", "pos": "noun"},
                {"lemma": "advenir", "translation": "to come about / arrive", "pos": "verb"}
            ]
        },
        f"{c_unit}-05": {
            "id": "vocab.b2.22.05",
            "lesson": f"{c_unit}-05",
            "title": "Precisión semántica y selección estilística de cambio",
            "words": [
                {"lemma": "matiz", "translation": "nuance / shade of meaning", "pos": "noun"},
                {"lemma": "semántica", "translation": "semantics", "pos": "noun"},
                {"lemma": "estilística", "translation": "stylistics", "pos": "noun"},
                {"lemma": "connotación", "translation": "connotation", "pos": "noun"},
                {"lemma": "ponderación", "translation": "deliberate weighing / evaluation", "pos": "noun"},
                {"lemma": "fluidez", "translation": "fluency / prose rhythm", "pos": "noun"},
                {"lemma": "expresividad", "translation": "expressiveness", "pos": "noun"},
                {"lemma": "pasar a", "translation": "to transition into being", "pos": "verb"},
                {"lemma": "desembocar", "translation": "to lead into / culminate in", "pos": "verb"}
            ]
        },
        f"{r_unit}-01": {
            "id": "vocab.b2.chilecentro.01",
            "lesson": f"{r_unit}-01",
            "title": "El Valle Central, los Andes y el clima mediterráneo",
            "words": [
                {"lemma": "cordillera", "translation": "mountain range", "pos": "noun"},
                {"lemma": "cuenca", "translation": "river basin / watershed valley", "pos": "noun"},
                {"lemma": "inversión", "translation": "thermal inversion", "pos": "noun"},
                {"lemma": "precipitación", "translation": "precipitation / rainfall", "pos": "noun"},
                {"lemma": "viñedo", "translation": "vineyard", "pos": "noun"},
                {"lemma": "rancagüino", "translation": "from Rancagua / Central Valley", "pos": "adjective"},
                {"lemma": "esmog", "translation": "smog / urban haze", "pos": "noun"},
                {"lemma": "mapocho", "translation": "Mapocho river of Santiago", "pos": "noun"},
                {"lemma": "mediterráneo", "translation": "Mediterranean climate", "pos": "adjective"}
            ]
        },
        f"{r_unit}-02": {
            "id": "vocab.b2.chilecentro.02",
            "lesson": f"{r_unit}-02",
            "title": "Valparaíso: Funiculares, cerros y bohemia portuaria",
            "words": [
                {"lemma": "funicular", "translation": "funicular railway / hillside lift", "pos": "noun"},
                {"lemma": "anfiteatro", "translation": "natural amphitheater port", "pos": "noun"},
                {"lemma": "bohemia", "translation": "bohemian lifestyle or quarter", "pos": "noun"},
                {"lemma": "porteño", "translation": "inhabitant of Valparaíso port", "pos": "noun"},
                {"lemma": "cerro", "translation": "inhabited hill of Valparaíso", "pos": "noun"},
                {"lemma": "caleta", "translation": "cove / traditional fishing inlet", "pos": "noun"},
                {"lemma": "ascensor", "translation": "hill elevator of Valparaíso", "pos": "noun"},
                {"lemma": "quebrada", "translation": "ravine / gully", "pos": "noun"},
                {"lemma": "mirador", "translation": "viewpoint / scenic overlook", "pos": "noun"}
            ]
        },
        f"{r_unit}-03": {
            "id": "vocab.b2.chilecentro.03",
            "lesson": f"{r_unit}-03",
            "title": "Gabriela Mistral y Pablo Neruda: La patria poética",
            "words": [
                {"lemma": "laureado", "translation": "laureate / Nobel winner", "pos": "adjective"},
                {"lemma": "lírica", "translation": "lyric poetry", "pos": "noun"},
                {"lemma": "pedagogía", "translation": "pedagogy / teaching philosophy", "pos": "noun"},
                {"lemma": "ruralidad", "translation": "rural life / rurality", "pos": "noun"},
                {"lemma": "caracola", "translation": "seashell", "pos": "noun"},
                {"lemma": "marítimo", "translation": "maritime / oceanic", "pos": "adjective"},
                {"lemma": "elquino", "translation": "from Elqui valley", "pos": "adjective"},
                {"lemma": "oda", "translation": "ode", "pos": "noun"},
                {"lemma": "estrofa", "translation": "poetic stanza", "pos": "noun"}
            ]
        },
        f"{r_unit}-04": {
            "id": "vocab.b2.chilecentro.04",
            "lesson": f"{r_unit}-04",
            "title": "El 11 de septiembre de 1973 y la memoria democrática",
            "words": [
                {"lemma": "quiebre", "translation": "rupture / institutional breakdown", "pos": "noun"},
                {"lemma": "bombardeo", "translation": "aerial bombing", "pos": "noun"},
                {"lemma": "dictadura", "translation": "dictatorship", "pos": "noun"},
                {"lemma": "clandestinidad", "translation": "underground resistance / secrecy", "pos": "noun"},
                {"lemma": "resistencia", "translation": "resistance", "pos": "noun"},
                {"lemma": "trovador", "translation": "folk singer / troubadour", "pos": "noun"},
                {"lemma": "memorial", "translation": "memorial monument", "pos": "noun"},
                {"lemma": "desaparecido", "translation": "disappeared person", "pos": "noun"},
                {"lemma": "inmolación", "translation": "sacrifice / martyrdom", "pos": "noun"}
            ]
        },
        f"{r_unit}-05": {
            "id": "vocab.b2.chilecentro.05",
            "lesson": f"{r_unit}-05",
            "title": "La transición democrática y el estallido social",
            "words": [
                {"lemma": "plebiscito", "translation": "plebiscite / direct popular vote", "pos": "noun"},
                {"lemma": "estallido", "translation": "social outburst / uprising", "pos": "noun"},
                {"lemma": "democracia", "translation": "democracy", "pos": "noun"},
                {"lemma": "constituyente", "translation": "constitutional delegate", "pos": "noun"},
                {"lemma": "desigualdad", "translation": "inequality", "pos": "noun"},
                {"lemma": "movilización", "translation": "civic mobilization", "pos": "noun"},
                {"lemma": "cabildo", "translation": "citizens' open town meeting", "pos": "noun"},
                {"lemma": "cacerolazo", "translation": "pot-banging protest", "pos": "noun"},
                {"lemma": "reivindicación", "translation": "social demand / claim", "pos": "noun"}
            ]
        }
    }

    for lid, vdata in vocab_data.items():
        write_json(f"vocabulary/b2/{lid}-voc.json", vdata)

    # -------------------------------------------------------------------------
    # 2. GRAMMAR FILES (10 files)
    # -------------------------------------------------------------------------
    grammar_data = {
        f"{c_unit}-01": {
            "id": f"grammar.b2.22.01.verbos-cambio-ponerse-quedarse",
            "title": "Los verbos de cambio ponerse y quedarse: reacciones y estados resultantes",
            "sections": [
                {
                    "type": "text",
                    "content": "En el sistema de los verbos de cambio o devenir en español, *ponerse* y *quedarse* expresan transiciones de estado asociadas a consecuencias físicas, anímicas o circunstanciales. *Ponerse* denota una alteración involuntaria, súbita y generalmente transitoria en el estado de ánimo, la salud o el aspecto físico (*se puso furiosa*, *se puso pálido*). En contraste, *quedarse* resalta el estado final o resultante en que permanece el sujeto tras un suceso imprevisto o irreversible (*se quedó sin palabras*, *se quedó ciego*)."
                },
                {
                    "type": "table",
                    "title": "Contraste funcional: Ponerse vs Quedarse",
                    "rows": [
                        ["Al escuchar la sentencia, el acusado se puso lívido.", "Upon hearing the sentence, the defendant turned pale."],
                        ["La diplomática se puso nerviosa durante el debate televisivo.", "The diplomat became nervous during the televised debate."],
                        ["Tras el terremoto, miles de familias se quedaron sin hogar.", "After the earthquake, thousands of families were left homeless."],
                        ["El público se quedó boquiabierto ante la elocuencia de la oradora.", "The audience was left agape at the speaker's eloquence."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Ponerse* se combina fundamentalmente con adjetivos de emoción o aspecto (*triste, contento, rojo, enfermo*). *Quedarse* se construye con adjetivos que expresan pérdida o secuela física/psicológica (*sordo, viudo, perplejo, absorto*)."
                }
            ]
        },
        f"{c_unit}-02": {
            "id": f"grammar.b2.22.02.verbos-cambio-hacerse-volverse",
            "title": "Los verbos de cambio hacerse y volverse: voluntad frente a cambio de carácter",
            "sections": [
                {
                    "type": "text",
                    "content": "*Hacerse* y *volverse* describen transformaciones profundas y duraderas, pero divergen en la intervención de la voluntad del sujeto. *Hacerse* implica un proceso voluntario o una evolución paulatina vinculada a la profesión, la religión, la ideología o el paso natural del tiempo (*se hizo abogado*, *se hizo vegetariano*, *se hace tarde*). Por el contrario, *volverse* expresa un cambio radical e involuntario en el carácter, la personalidad o la conducta de alguien, con frecuencia de signo negativo o inesperado (*se volvió desconfiado*, *se volvió intolerante*)."
                },
                {
                    "type": "table",
                    "title": "Contraste: Hacerse (voluntario/paulatino) vs Volverse (involuntario/carácter)",
                    "rows": [
                        ["Tras años de estudio nocturno, se hizo diplomática de carrera.", "After years of evening study, she became a career diplomat."],
                        ["Con el paso de los años, el poeta se hizo muy devoto.", "With the passing of the years, the poet became very devout."],
                        ["El veterano se volvió hosco y solitario tras la guerra.", "The veteran became sullen and reclusive after the war."],
                        ["La situación económica se volvió insostenible para el comercio.", "The economic situation became unsustainable for trade."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Para cambios involuntarios de personalidad use *volverse* (*se volvió arrogante*). Evite emplear *hacerse* con defectos o trastornos involuntarios (*no se dice *se hizo loco*, sino *se volvió loco*)."
                }
            ]
        },
        f"{c_unit}-03": {
            "id": f"grammar.b2.22.03.verbos-cambio-convertirse-transformarse",
            "title": "Convertirse en y transformarse en: metamorfosis radical y cambio de categoría",
            "sections": [
                {
                    "type": "text",
                    "content": "Las perífrasis reflexivas con preposición *convertirse en* y *transformarse en* indican una metamorfosis sustancial o un cambio categorial profundo donde una entidad pasa a ser algo por completo diferente. A diferencia de los otros verbos de cambio que admiten adjetivos directos, *convertirse en* y *transformarse en* rigen necesariamente un sintagma nominal introducido por la preposición *en* (*el puerto se convirtió en una metrópoli*, *la protesta se transformó en un estallido social*)."
                },
                {
                    "type": "table",
                    "title": "Régimen preposicional y alcance de Convertirse en / Transformarse en",
                    "rows": [
                        ["Valparaíso se convirtió en el principal emporio comercial del Pacífico sur.", "Valparaíso became the main commercial emporium of the South Pacific."],
                        ["La pequeña caleta de pescadores se transformó en un balneario cosmopolita.", "The small fishing cove transformed into a cosmopolitan seaside resort."],
                        ["El poema lírico se convirtió en el himno de los trabajadores mineros.", "The lyric poem became the anthem of the mining workers."],
                        ["La crisis institucional se transformó en una oportunidad constituyente.", "The institutional crisis transformed into a constitutional opportunity."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerde siempre la preposición *en*: es agramatical decir '*se convirtió un líder'*; la construcción normativa exige invariablemente '*se convirtió en un líder*'."
                }
            ]
        },
        f"{c_unit}-04": {
            "id": f"grammar.b2.22.04.verbos-cambio-llegar-a-ser",
            "title": "La perífrasis llegar a ser: culminación de un proceso y reconocimiento",
            "sections": [
                {
                    "type": "text",
                    "content": "La locución *llegar a ser* representa la culminación exitosa de una prolongada trayectoria vital, profesional o artística marcada por el esfuerzo continuado, la perseverancia y la superación de obstáculos. Implica una valoración altamente positiva o de notable trascendencia histórica, situando al sujeto en una cúspide o posición relevante (*Gabriela Mistral llegó a ser la primera latinoamericana en ganar el Premio Nobel de Literatura*)."
                },
                {
                    "type": "table",
                    "title": "Usos de Llegar a ser como culminación de trayectoria",
                    "rows": [
                        ["Aquella humilde maestra rural llegó a ser una figura intelectual ecuménica.", "That humble rural schoolteacher eventually became an ecumenical intellectual figure."],
                        ["Con tenacidad inquebrantable, el dirigente sindical llegó a ser presidente.", "With unbreakable tenacity, the union leader eventually became president."],
                        ["Esa obra novelística llegó a ser el clásico indiscutible del realismo social.", "That novelistic work eventually became the unquestioned classic of social realism."],
                        ["El carbón de Lota llegó a ser el combustible fundamental de la armada nacional.", "The coal of Lota eventually became the fundamental fuel of the national navy."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Llegar a ser* resalta el largo proceso de ascenso y el mérito acumulado. No se emplea para cambios instantáneos o accidentales."
                }
            ]
        },
        f"{c_unit}-05": {
            "id": f"grammar.b2.22.05.seleccion-estilistica-verbos-cambio",
            "title": "Criterios estilísticos y matices semánticos en los verbos de devenir",
            "sections": [
                {
                    "type": "text",
                    "content": "El dominio de los verbos de devenir en el nivel B2 superior reside en seleccionar con precisión el matiz adecuado entre *ponerse, quedarse, volverse, hacerse, convertirse en, transformarse en* y *llegar a ser*. A ellos se suman opciones de registro culto como *pasar a ser* (transición funcional) o verbos derivados que condensan el cambio en una sola palabra léxica (*enriquecerse, empobrecerse, enmudecer, palidecer*)."
                },
                {
                    "type": "table",
                    "title": "Matices semánticos en los verbos de transformación",
                    "rows": [
                        ["Se puso furioso / Palideció al oír la noticia.", "Temporary physical/emotional reaction."],
                        ["Se quedó sin empleo tras el cierre del yacimiento.", "Resultant state of deprivation or outcome."],
                        ["Se volvió taciturno con el paso de los años.", "Involuntary permanent shift in temperament."],
                        ["Se hizo militante por convicción política.", "Voluntary ideological or professional adoption."],
                        ["Se convirtió en la capital cultural del país.", "Radical transformation into a new category."],
                        ["Llegó a ser una gloria de las letras hispánicas.", "Culmination of lifelong endeavor and recognition."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Para enriquecer su estilo, combine los verbos perifrásticos de cambio con verbos derivados directos (*se puso rojo* -> *enrojeció*; *se hizo rico* -> *se enriqueció*)."
                }
            ]
        },
        f"{r_unit}-01": {
            "id": f"grammar.b2.chilecentro.01.chile-vallecentral-geografia-clima",
            "title": "El relato geográfico del Valle Central: aspecto narrativo e inversión térmica",
            "sections": [
                {
                    "type": "text",
                    "content": "La descripción del relieve chileno central —enmarcado entre la imponente Cordillera de los Andes y la Cordillera de la Costa— requiere articular descripciones panorámicas con pretérito imperfecto para el marco espacial y pretérito indefinido para los hitos orográficos y fundacionales. El régimen de clima mediterráneo, las cuencas fértiles regadas por los deshielos del río Mapocho y del Maipo y el fenómeno invernal de la inversión térmica configuran el hábitat donde reside más del setenta por ciento de la población del país."
                },
                {
                    "type": "table",
                    "title": "Estructuras descriptivas del paisaje altoandino y central",
                    "rows": [
                        ["Mientras la cordillera nevada dominaba el horizonte, la cuenca albergaba viñedos prósperos.", "While the snowy range dominated the horizon, the basin harbored prosperous vineyards."],
                        ["En invierno el aire frío quedaba atrapado, provocando una densa inversión térmica.", "In winter the cold air remained trapped, causing a dense thermal inversion."],
                        ["Los agricultores canalizaron las aguas glaciares; así transformaron la llanura en un vergel.", "Farmers channeled glacial waters; thus they transformed the plain into an orchard."],
                        ["La cordillera de la Costa impedía el paso directo de las brisas oceánicas hacia Santiago.", "The Coastal range prevented the direct passage of oceanic breezes into Santiago."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En la prosa geográfica chilena, la alternancia entre el imperfecto de fondo (*dominaba, albergaba*) y el indefinido de evento (*canalizaron, fundaron*) otorga relieve y profundidad temporal al texto."
                }
            ]
        },
        f"{r_unit}-02": {
            "id": f"grammar.b2.chilecentro.02.chile-valparaiso-puerto-patrimonio",
            "title": "Estructuras espaciales y de relativo en la arquitectura vertical de Valparaíso",
            "sections": [
                {
                    "type": "text",
                    "content": "La topografía escarpada de Valparaíso, declarada Patrimonio de la Humanidad por la UNESCO, exige el uso de cláusulas de relativo complejas con preposiciones locativas (*en cuyos cerros*, *por donde trepan los funiculares*, *desde cuyos miradores*) para capturar la distribución vertical de sus barrios, sus coloridas casas de chapa ondulada colgadas de las laderas y la intensa bohemia portuaria."
                },
                {
                    "type": "table",
                    "title": "Oraciones de relativo complejas y subordinación espacial",
                    "rows": [
                        ["Los cerros Alegre y Concepción, en cuyas laderas serpentean pasajes peatonales, deslumbran al viajero.", "Cerro Alegre and Concepción, on whose slopes pedestrian passages wind, dazzle the traveler."],
                        ["Los antiguos funiculares de madera, mediante los cuales los vecinos vencían los abismos, siguen operativos.", "The old wooden funiculars, by means of which neighbors conquered precipices, remain operational."],
                        ["El puerto, a cuyos muelles arribaban veleros de todos los océanos, forjó una cultura cosmopolita.", "The port, at whose docks sailing ships from all oceans arrived, forged a cosmopolitan culture."],
                        ["Es una bahía anfiteatral donde la arquitectura espontánea desafía las leyes de la gravedad.", "It is an amphitheater bay where spontaneous architecture defies the laws of gravity."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El empleo del relativo posesivo *cuyo* precedido de preposición locativa (*en cuyos cerros, a cuyos pies*) dota a las crónicas urbanas de elegancia clásica y precisión descriptiva."
                }
            ]
        },
        f"{r_unit}-03": {
            "id": f"grammar.b2.chilecentro.03.chile-mistral-neruda-poesia",
            "title": "Modalidad lírica y valoración estética en el legado de Mistral y Neruda",
            "sections": [
                {
                    "type": "text",
                    "content": "Chile es universalmente reconocido como la 'tierra de poetas' gracias a sus dos premios Nobel de Literatura: Gabriela Mistral (1945) y Pablo Neruda (1971). El análisis de sus poéticas despliega estructuras de valoración modal (*resulta conmovedor constatar*, *es admirable cómo*), contrastando el arraigo telúrico y pedagógico de la maestra del valle del Elqui con la exuberancia cósmica, marina y política del cantor de Isla Negra."
                },
                {
                    "type": "table",
                    "title": "Estructuras de valoración modal y contraste poético",
                    "rows": [
                        ["Resulta conmovedor constatar cómo Mistral aunó la defensa del niño campesino con la lírica universal.", "It is moving to verify how Mistral united the defense of the peasant child with universal lyrics."],
                        ["Es innegable que Neruda transformó la lengua castellana con sus Odas elementales y el Canto General.", "It is undeniable that Neruda transformed the Spanish language with his Elemental Odes and Canto General."],
                        ["Mientras Gabriela buscaba la pureza austera del valle, Pablo dialogaba con el rugido del mar.", "While Gabriela sought the austere purity of the valley, Pablo dialogued with the roar of the sea."],
                        ["Ambos laureados demostraron que la poesía puede convertirse en la voz moral de los oprimidos.", "Both laureates demonstrated that poetry can become the moral voice of the oppressed."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Las matrices de certeza objetiva (*es innegable que*) seleccionan indicativo, mientras que las de valoración subjetiva o recomendación estética rigen subjuntivo (*conviene que el lector descubra*)."
                }
            ]
        },
        f"{r_unit}-04": {
            "id": f"grammar.b2.chilecentro.04.chile-moneda-golpe-memoria",
            "title": "Secuenciación temporal y correlación verbal en la memoria del 11 de septiembre",
            "sections": [
                {
                    "type": "text",
                    "content": "La narración del golpe de Estado del 11 de septiembre de 1973 en el Palacio de La Moneda y el posterior quebrantamiento de la institucionalidad republicana chilena recurre a una rigurosa secuenciación temporal retrospectiva. El uso coordinado del pluscuamperfecto de indicativo (*habían cercado*), el pretérito indefinido (*asaltaron, transmitió*) y construcciones temporales con *al + infinitivo* o *tan pronto como* articulan la reconstrucción de aquella jornada histórica."
                },
                {
                    "type": "table",
                    "title": "Correlación de tiempos pasados en la narración histórica",
                    "rows": [
                        ["Al despuntar el alba, los tanques militares ya habían rodeado la sede del gobierno.", "At daybreak, military tanks had already surrounded the seat of government."],
                        ["Tan pronto como los aviones bombardearon La Moneda, la democracia republicana quedó suspendida.", "As soon as aircraft bombed La Moneda, republican democracy remained suspended."],
                        ["Salvador Allende pronunció su último discurso antes de que se cortaran las transmisiones radiales.", "Salvador Allende delivered his final speech before radio transmissions were cut off (subj)."],
                        ["La memoria colectiva custodió las canciones de Víctor Jara a pesar de la censura dictatorial.", "Collective memory safeguarded Víctor Jara's songs despite dictatorial censorship."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En la subordinación temporal con *antes de que*, el verbo subordinado se conjuga invariablemente en modo subjuntivo (*antes de que se cortaran las transmisiones*), incluso en contextos de pasado fáctico."
                }
            ]
        },
        f"{r_unit}-05": {
            "id": f"grammar.b2.chilecentro.05.chile-transicion-estallido-ciudadania",
            "title": "Conectores de contraste y causalidad en los debates sociopolíticos chilenos",
            "sections": [
                {
                    "type": "text",
                    "content": "El examen de la trayectoria contemporánea de Chile —desde el triunfo democrático del 'No' en el plebiscito de 1988 hasta el 'estallido social' de octubre de 2019 y los procesos constituyentes— emplea conectores discursivos de causa, oposición y consecuencia. Nexos como *si bien*, *no obstante*, *a raíz de*, *por consiguiente* y *de ahí que* permiten sopesar la modernización económica frente a la persistencia de desigualdades estructurales."
                },
                {
                    "type": "table",
                    "title": "Conectores de ponderación sociopolítica en el Chile contemporáneo",
                    "rows": [
                        ["Si bien la economía creció de forma sostenida, la desigualdad social generó hondo malestar.", "Although the economy grew steadily, social inequality generated deep discontent."],
                        ["No obstante los avances institucionales, las demandas ciudadanas desbordaron a los partidos.", "Notwithstanding institutional advances, citizens' demands overwhelmed traditional parties."],
                        ["A raíz de las multitudinarias protestas, las fuerzas políticas convocaron a un plebiscito constituyente.", "In the wake of massive protests, political forces convened a constitutional plebiscite."],
                        ["El costo de la vida era agobiante; de ahí que millones de personas salieran a marchar en paz.", "The cost of living was crushing; hence millions of people went out to march peacefully (subj)."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerde que el conector consecutivo de valor explicativo *de ahí que* rige siempre modo subjuntivo en español culto (*de ahí que salieran a marchar*)."
                }
            ]
        }
    }

    for lid, gdata in grammar_data.items():
        write_json(f"grammar/b2/{lid}-a-gr.json", gdata)

    # -------------------------------------------------------------------------
    # 3. EXERCISE FILES (12 files, 76 exercises)
    # -------------------------------------------------------------------------
    # Core 1
    write_json(f"exercises/b2/{c1}-ex.json", {
        "lesson": c1,
        "exercises": [
            {
                "id": f"{c1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["ponerse", "to become emotionally or temporarily"],
                    ["quedarse", "to end up in a lasting resulting state"],
                    ["mutabilidad", "quality of being subject to change"],
                    ["desconcierto", "state of perplexity or confusion"]
                ],
                "teaches": ["b2-22-vocab"]
            },
            {
                "id": f"{c1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Al enterarse de la dimisión del ministro, el vocero se __ pálido de desconcierto. (puso)",
                "answer": "puso",
                "english": "Upon learning of the minister's resignation, the spokesperson turned pale with bewilderment.",
                "teaches": ["verbos-cambio-ponerse-quedarse"]
            },
            {
                "id": f"{c1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué se utiliza 'quedarse' en 'Tras la inundación, cientos de familias se quedaron sin hogar'?",
                "options": [
                    "Porque expresa un estado resultante involuntario de privación o secuela duradera.",
                    "Porque describe una decisión voluntaria tomada de común acuerdo entre vecinos.",
                    "Porque el verbo quedarse solo se conjuga en pretérito perfecto compuesto.",
                    "Porque se trata de una acción temporal que desaparece en cuestión de minutos."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-ponerse-quedarse"]
            },
            {
                "id": f"{c1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "actriz", "se", "puso", "nerviosa", "ante", "las", "cámaras."],
                "solution": ["La", "actriz", "se", "puso", "nerviosa", "ante", "las", "cámaras."],
                "english": "The actress became nervous in front of the cameras.",
                "teaches": ["verbos-cambio-ponerse-quedarse"]
            },
            {
                "id": f"{c1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diputado", "text": "¿Cómo reaccionó la audiencia ante las cifras del déficit?"},
                    {"speaker": "Asesora", "text": "Todos los presentes _____ atónitos al comprobar la magnitud del desfalco."}
                ],
                "options": [
                    "se quedaron",
                    "se pusieron a",
                    "quedándose",
                    "fueron puestos"
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-ponerse-quedarse"]
            },
            {
                "id": f"{c1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El testigo se quedó perplejo al reconocer el arma en el tribunal.",
                "english": "The witness was left perplexed upon recognizing the weapon in court.",
                "teaches": ["verbos-cambio-ponerse-quedarse"]
            }
        ]
    })

    # Core 2
    write_json(f"exercises/b2/{c2}-ex.json", {
        "lesson": c2,
        "exercises": [
            {
                "id": f"{c2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["volverse", "to undergo involuntary character change"],
                    ["hacerse", "to adopt identity or profession intentionally"],
                    ["paulatino", "occurring step by step or gradually"],
                    ["escéptico", "inclined to doubt or question assertions"]
                ],
                "teaches": ["b2-22-vocab"]
            },
            {
                "id": f"{c2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Con el paso de los años, el fiscal se __ sumamente desconfiado de las presiones políticas. (volvió)",
                "answer": "volvió",
                "english": "With the passing of the years, the prosecutor became extremely distrustful of political pressures.",
                "teaches": ["verbos-cambio-hacerse-volverse"]
            },
            {
                "id": f"{c2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿En cuál de las siguientes oraciones es normativamente obligatorio emplear 'hacerse' en vez de 'volverse'?",
                "options": [
                    "Tras culminar sus estudios universitarios, ella se hizo abogada laboralista.",
                    "Después del accidente ferroviario, el maquinista se hizo sumamente miedoso.",
                    "El tiempo atmosférico se hizo nublado en apenas cinco minutos.",
                    "Al escuchar la noticia falsa, el público se hizo furioso de inmediato."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-hacerse-volverse"]
            },
            {
                "id": f"{c2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "dirigente", "se", "hizo", "militante", "por", "firme", "convicción."],
                "solution": ["El", "dirigente", "se", "hizo", "militante", "por", "firme", "convicción."],
                "english": "The leader became a party member out of firm conviction.",
                "teaches": ["verbos-cambio-hacerse-volverse"]
            },
            {
                "id": f"{c2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Por qué cambió tanto la actitud del novelista hacia la crítica?"},
                    {"speaker": "Editor", "text": "A raíz de las polémicas injustas, _____ muy escéptico y solitario."}
                ],
                "options": [
                    "se volvió",
                    "se hizo",
                    "se convirtió",
                    "quedose"
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-hacerse-volverse"]
            },
            {
                "id": f"{c2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El antiguo militar se hizo pacifista tras presenciar los horrores del combate.",
                "english": "The former military officer became a pacifist after witnessing the horrors of combat.",
                "teaches": ["verbos-cambio-hacerse-volverse"]
            }
        ]
    })

    # Core 3
    write_json(f"exercises/b2/{c3}-ex.json", {
        "lesson": c3,
        "exercises": [
            {
                "id": f"{c3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["convertirse", "to turn into something new categorically"],
                    ["metamorfosis", "profound structural transformation"],
                    ["paradigma", "accepted model or conceptual framework"],
                    ["transmutar", "to change from one nature into another"]
                ],
                "teaches": ["b2-22-vocab"]
            },
            {
                "id": f"{c3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La humilde caleta de pescadores se convirtió __ un próspero polo turístico internacional. (en)",
                "answer": "en",
                "english": "The humble fishing cove turned into a prosperous international tourist hub.",
                "teaches": ["verbos-cambio-convertirse-transformarse"]
            },
            {
                "id": f"{c3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué exigencia sintáctica distingue a 'convertirse en' de otros verbos de cambio?",
                "options": [
                    "Rige obligatoriamente la preposición 'en' seguida de un sintagma nominal categorial.",
                    "Solo puede conjugarse en primera persona del plural del presente indicativo.",
                    "Exige siempre un adjetivo calificativo sin ninguna preposición intermedia.",
                    "No admite sujetos inanimados ni colectivos bajo ninguna circunstancia."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-convertirse-transformarse"]
            },
            {
                "id": f"{c3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "puerto", "se", "transformó", "en", "el", "epicentro", "comercial."],
                "solution": ["El", "puerto", "se", "transformó", "en", "el", "epicentro", "comercial."],
                "english": "The port transformed into the commercial epicenter.",
                "teaches": ["verbos-cambio-convertirse-transformarse"]
            },
            {
                "id": f"{c3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora", "text": "¿Cómo influyó el ferrocarril en el desarrollo de la comarca?"},
                    {"speaker": "Geógrafo", "text": "La llegada del tren hizo que la aldea _____ en una ciudad pujante."}
                ],
                "options": [
                    "se convirtiera",
                    "se hiciera a",
                    "se pusiera en",
                    "volviérase"
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-convertirse-transformarse"]
            },
            {
                "id": f"{c3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El antiguo teatro de madera se transformó en un centro cultural comunitario.",
                "english": "The old wooden theater transformed into a community cultural center.",
                "teaches": ["verbos-cambio-convertirse-transformarse"]
            }
        ]
    })

    # Core 4
    write_json(f"exercises/b2/{c4}-ex.json", {
        "lesson": c4,
        "exercises": [
            {
                "id": f"{c4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["llegar a ser", "to become through effort and progression"],
                    ["culminación", "final peak of a historical process"],
                    ["consagración", "definitive official recognition"],
                    ["trayectoria", "course of career or human progression"]
                ],
                "teaches": ["b2-22-vocab"]
            },
            {
                "id": f"{c4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Tras décadas de magisterio rural, Gabriela Mistral llegó a __ la primera Nobel de América Latina. (ser)",
                "answer": "ser",
                "english": "After decades of rural teaching, Gabriela Mistral eventually became Latin America's first Nobel laureate.",
                "teaches": ["verbos-cambio-llegar-a-ser"]
            },
            {
                "id": f"{c4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué dimensión pragmática aporta la perífrasis 'llegar a ser' frente a un simple verbo copulativo?",
                "options": [
                    "Subraya el largo proceso de esfuerzo, mérito y perseverancia que culmina en un logro trascendente.",
                    "Indica una casualidad fortuita ocurrida sin intervención de la voluntad personal.",
                    "Expresa una orden perentoria dictada por una autoridad académica.",
                    "Señala que el resultado fue decepcionante o de poca duración en el tiempo."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-llegar-a-ser"]
            },
            {
                "id": f"{c4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Con", "tenacidad", "aquel", "joven", "llegó", "a", "ser", "rector."],
                "solution": ["Con", "tenacidad", "aquel", "joven", "llegó", "a", "ser", "rector."],
                "english": "With tenacity that young man eventually became university president.",
                "teaches": ["verbos-cambio-llegar-a-ser"]
            },
            {
                "id": f"{c4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Estudiante", "text": "¿Esperaba el novelista alcanzar tal prestigio internacional?"},
                    {"speaker": "Catedrática", "text": "Jamás lo imaginó en sus inicios, pero con los años _____ una voz universal."}
                ],
                "options": [
                    "llegó a ser",
                    "se puso a ser",
                    "quedó siendo de",
                    "hízose por"
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-llegar-a-ser"]
            },
            {
                "id": f"{c4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La obra de Baldomero Lillo llegó a ser la cumbre del realismo minero chileno.",
                "english": "Baldomero Lillo's work eventually became the peak of Chilean mining realism.",
                "teaches": ["verbos-cambio-llegar-a-ser"]
            }
        ]
    })

    # Core 5
    write_json(f"exercises/b2/{c5}-ex.json", {
        "lesson": c5,
        "exercises": [
            {
                "id": f"{c5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["semántica", "study of linguistic meaning"],
                    ["estilística", "art of expressive textual choices"],
                    ["ponderación", "balanced evaluation of nuances"],
                    ["fluidez", "smooth natural flow of prose"]
                ],
                "teaches": ["b2-22-vocab"]
            },
            {
                "id": f"{c5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El antiguo mineral de carbón pasó a __ un monumento patrimonial protegido por el estado. (ser)",
                "answer": "ser",
                "english": "The former coal mine transitioned into being a heritage monument protected by the state.",
                "teaches": ["seleccion-estilistica-verbos-cambio"]
            },
            {
                "id": f"{c5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la opción estilísticamente más elegante para condensar 'El cielo se puso oscuro súbitamente'?",
                "options": [
                    "El cielo se ensombreció de manera repentina.",
                    "El cielo se hizo muy oscuro de repente.",
                    "El cielo se volvió oscurecido sin aviso.",
                    "El cielo llegó a ser una cosa muy oscura."
                ],
                "correct": 0,
                "teaches": ["seleccion-estilistica-verbos-cambio"]
            },
            {
                "id": f"{c5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "propuesta", "pasó", "a", "ser", "la", "prioridad", "legislativa."],
                "solution": ["La", "propuesta", "pasó", "a", "ser", "la", "prioridad", "legislativa."],
                "english": "The proposal transitioned into being the legislative priority.",
                "teaches": ["seleccion-estilistica-verbos-cambio"]
            },
            {
                "id": f"{c5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítico", "text": "¿Qué verbo de cambio refleja mejor la consagración del pintor?"},
                    {"speaker": "Curadora", "text": "Sin duda 'llegó a ser maestro', porque resalta el mérito acumulado de su vida."}
                ],
                "options": [
                    "llegó a ser maestro",
                    "se puso maestro",
                    "quedó en maestro",
                    "volviose maestro"
                ],
                "correct": 0,
                "teaches": ["seleccion-estilistica-verbos-cambio"]
            },
            {
                "id": f"{c5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La concertación de fuerzas políticas desembocó en un acuerdo constituyente histórico.",
                "english": "The consensus of political forces culminated in a historic constitutional agreement.",
                "teaches": ["seleccion-estilistica-verbos-cambio"]
            }
        ]
    })

    # Core Consolidation
    write_json(f"exercises/b2/{c_unit}-consolidation-ex.json", {
        "lesson": f"{c_unit}-consolidation",
        "exercises": [
            {
                "id": f"{c_unit}-con.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["enmudecer", "to become speechless or silent"],
                    ["enriquecerse", "to acquire wealth or intellectual depth"],
                    ["reconfigurar", "to alter structural arrangement"],
                    ["consagración", "definitive triumph and public acclaim"]
                ],
                "teaches": ["b2-22-vocab"]
            },
            {
                "id": f"{c_unit}-con.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Al contemplar el derrumbe en la galería, la madre del minero se __ sin aliento. (quedó)",
                "answer": "quedó",
                "english": "Upon beholding the cave-in in the shaft, the miner's mother was left breathless.",
                "teaches": ["verbos-cambio-ponerse-quedarse"]
            },
            {
                "id": f"{c_unit}-con.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué verbo de cambio expresa una transformación radical de categoría con régimen preposicional obligatorio?",
                "options": [
                    "Convertirse en, porque rige siempre la preposición 'en' seguida de un sustantivo.",
                    "Ponerse, porque solo admite participios verbales terminados en -ado e -ido.",
                    "Hacerse, porque no tolera sustantivos ideológicos ni religiosos.",
                    "Llegar a ser, porque exige un complemento circunstancial de tiempo pretérito."
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-convertirse-transformarse"]
            },
            {
                "id": f"{c_unit}-con.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Con", "esfuerzo", "constante", "llegó", "a", "ser", "un", "referente."],
                "solution": ["Con", "esfuerzo", "constante", "llegó", "a", "ser", "un", "referente."],
                "english": "With constant effort he eventually became an authority.",
                "teaches": ["sintesis-verbos-de-cambio"]
            },
            {
                "id": f"{c_unit}-con.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Profesor", "text": "¿Por qué el joven obrero decidió estudiar derecho?"},
                    {"speaker": "Compañera", "text": "Quería _____ abogado para defender a sus hermanos de los abusos patronales."}
                ],
                "options": [
                    "hacerse",
                    "volverse",
                    "ponerse",
                    "quedarse"
                ],
                "correct": 0,
                "teaches": ["verbos-cambio-hacerse-volverse"]
            },
            {
                "id": f"{c_unit}-con.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El relato minero se convirtió en el grito de protesta de toda una generación.",
                "english": "The mining tale turned into the outcry of an entire generation.",
                "teaches": ["sintesis-verbos-de-cambio"]
            },
            {
                "id": f"{c_unit}-con.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué dimensión social denuncia Baldomero Lillo en 'El chiflón del diablo'?",
                "options": [
                    "La deshumanización patronal que sacrificaba vidas obreras en galerías inseguras por codicia de carbón.",
                    "El encarecimiento de los billetes de tren entre las ciudades de Santiago y Concepción.",
                    "La rivalidad deportiva entre los equipos de fútbol de los puertos carboníferos.",
                    "La falta de bibliotecas públicas en los pueblos rurales del valle central."
                ],
                "correct": 0
            },
            {
                "id": f"{c_unit}-con.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la correspondencia funcional correcta en el sistema de verbos de devenir?",
                "options": [
                    "Ponerse (transitorio físico/anímico), volverse (carácter involuntario), hacerse (voluntario/tiempo), convertirse en (metamorfosis categorial).",
                    "Ponerse (profesión definitiva), volverse (metamorfosis categorial con en), hacerse (secuela irreversible de salud).",
                    "Convertirse en (emoción momentánea), quedarse (ascenso meritorio paulatino), llegar a ser (accidente transitorio).",
                    "Todos los verbos de cambio son sinónimos absolutos y pueden permutarse libremente sin alterar el sentido."
                ],
                "correct": 0,
                "teaches": ["sintesis-verbos-de-cambio"]
            }
        ]
    })

    # Regional 1
    write_json(f"exercises/b2/{r1}-ex.json", {
        "lesson": r1,
        "exercises": [
            {
                "id": f"{r1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["cuenca", "valley enclosed by mountain ranges"],
                    ["inversión", "atmospheric trapping of cold air layer"],
                    ["viñedo", "plantation of grapevines for wine"],
                    ["mediterráneo", "warm dry summer and mild wet winter climate"]
                ],
                "teaches": ["b2-chilecentro-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En los meses de invierno el aire frío __ atrapado en la cuenca de Santiago. (quedaba)",
                "answer": "quedaba",
                "english": "In winter months, cold air remained trapped in the Santiago basin.",
                "teaches": ["chile-vallecentral-geografia-clima"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el pretérito imperfecto es predominante al describir la cuenca del Valle Central chileno?",
                "options": [
                    "Porque establece el marco paisajístico y las condiciones climáticas continuas de fondo.",
                    "Porque los Andes chilenos ya no existen en la geografía contemporánea.",
                    "Porque el pretérito imperfecto es el único tiempo verbal permitido en textos ecológicos.",
                    "Porque describe una acción puntual que ocurrió una sola vez en el siglo dieciséis."
                ],
                "correct": 0,
                "teaches": ["chile-vallecentral-geografia-clima"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "ríos", "glaciares", "regaban", "las", "fértiles", "tierras", "agrícolas."],
                "solution": ["Los", "ríos", "glaciares", "regaban", "las", "fértiles", "tierras", "agrícolas."],
                "english": "Glacial rivers irrigated the fertile agricultural lands.",
                "teaches": ["chile-vallecentral-geografia-clima"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Agrónoma", "text": "¿Por qué el Valle Central es tan propicio para la vitivinicultura?"},
                    {"speaker": "Climatólogo", "text": "Porque la oscilación térmica diurna y los suelos sedimentarios _____ condiciones inmejorables."}
                ],
                "options": [
                    "brindaban",
                    "brinden",
                    "habían brindado a",
                    "brindaron de"
                ],
                "correct": 0,
                "teaches": ["chile-vallecentral-geografia-clima"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La cordillera de la Costa modera el impacto directo de las brisas del océano Pacífico.",
                "english": "The Coastal range moderates the direct impact of Pacific ocean breezes.",
                "teaches": ["chile-vallecentral-geografia-clima"]
            }
        ]
    })

    # Regional 2
    write_json(f"exercises/b2/{r2}-ex.json", {
        "lesson": r2,
        "exercises": [
            {
                "id": f"{r2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["funicular", "cable railway ascending steep hillsides"],
                    ["anfiteatro", "natural semi-circular bay structure"],
                    ["porteño", "inhabitant or cultural aspect of Valparaíso"],
                    ["quebrada", "deep coastal ravine dividing urban hills"]
                ],
                "teaches": ["b2-chilecentro-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los cerros Alegre y Concepción, en __ laderas trepan los funiculares, son patrimonio mundial. (cuyas)",
                "answer": "cuyas",
                "english": "Cerro Alegre and Concepción, on whose slopes funiculars climb, are world heritage.",
                "teaches": ["chile-valparaiso-puerto-patrimonio"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Con qué concuerda el pronombre relativo 'cuyos' en 'El puerto a cuyos miradores acuden los artistas'?",
                "options": [
                    "Con el sustantivo plural masculino 'miradores' que le sigue inmediatamente.",
                    "Con el sustantivo antecedente 'puerto' que aparece antes de la preposición.",
                    "Siempre en singular neutro por regla de cortesía gramatical.",
                    "Con el sujeto implícito 'los artistas' que realiza la acción de acudir."
                ],
                "correct": 0,
                "teaches": ["chile-valparaiso-puerto-patrimonio"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "funiculares", "comunican", "el", "plano", "con", "los", "cerros."],
                "solution": ["Los", "funiculares", "comunican", "el", "plano", "con", "los", "cerros."],
                "english": "The funiculars connect the flat city with the hills.",
                "teaches": ["chile-valparaiso-puerto-patrimonio"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Arquitecto", "text": "¿Qué singulariza el trazado urbano de Valparaíso?"},
                    {"speaker": "Guía", "text": "Es una ciudad anfiteatral _____ escaleras desafían la verticalidad de la roca."}
                ],
                "options": [
                    "cuyas",
                    "cuyo",
                    "en cuyos",
                    "donde que"
                ],
                "correct": 0,
                "teaches": ["chile-valparaiso-puerto-patrimonio"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Valparaíso despliega casas de chapa policromada colgadas sobre el abismo del Pacífico.",
                "english": "Valparaíso displays polychrome corrugated iron houses hanging over the Pacific abyss.",
                "teaches": ["chile-valparaiso-puerto-patrimonio"]
            }
        ]
    })

    # Regional 3
    write_json(f"exercises/b2/{r3}-ex.json", {
        "lesson": r3,
        "exercises": [
            {
                "id": f"{r3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["laureado", "distinguished with supreme award"],
                    ["lírica", "poetic verse expressing profound emotion"],
                    ["ruralidad", "cultural essence of peasant countryside"],
                    ["oda", "lyric poem celebrating elemental reality"]
                ],
                "teaches": ["b2-chilecentro-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Resulta conmovedor constatar que la poesía de Mistral __ la voz moral de los desposeídos. (fue)",
                "answer": "fue",
                "english": "It is moving to verify that Mistral's poetry was the moral voice of the dispossessed.",
                "teaches": ["chile-mistral-neruda-poesia"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo verbal debe seleccionarse tras la matriz de certeza 'Es innegable que...' en el análisis poético?",
                "options": [
                    "Modo indicativo, porque constata una realidad empírica o juicio incontrovertible.",
                    "Modo subjuntivo, porque la poesía es siempre un terreno de opinión subjetiva.",
                    "Modo imperativo directo en tercera persona del plural.",
                    "Infinitivo simple obligatorio sin posibilidad de conjugación finita."
                ],
                "correct": 0,
                "teaches": ["chile-mistral-neruda-poesia"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Ambos", "poetas", "hicieron", "resonar", "la", "voz", "de", "Chile."],
                "solution": ["Ambos", "poetas", "hicieron", "resonar", "la", "voz", "de", "Chile."],
                "english": "Both poets made the voice of Chile resound.",
                "teaches": ["chile-mistral-neruda-poesia"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Profesora", "text": "¿Cómo se vincula Neruda con el paisaje costero de Isla Negra?"},
                    {"speaker": "Poeta", "text": "Es evidente que el rumor de las olas _____ cada verso de su obra tardía."}
                ],
                "options": [
                    "inspiró",
                    "inspire",
                    "inspirara",
                    "inspirando a"
                ],
                "correct": 0,
                "teaches": ["chile-mistral-neruda-poesia"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Gabriela Mistral fue la primera escritora de América Latina distinguida con el Premio Nobel.",
                "english": "Gabriela Mistral was the first Latin American female writer honored with the Nobel Prize.",
                "teaches": ["chile-mistral-neruda-poesia"]
            }
        ]
    })

    # Regional 4
    write_json(f"exercises/b2/{r4}-ex.json", {
        "lesson": r4,
        "exercises": [
            {
                "id": f"{r4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["quiebre", "abrupt institutional constitutional rupture"],
                    ["bombardeo", "destructive aerial air attack"],
                    ["trovador", "poet musician singing social truths"],
                    ["inmolación", "supreme sacrifice for moral principles"]
                ],
                "teaches": ["b2-chilecentro-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Al despuntar el alba, los blindados militares ya habían __ el Palacio de La Moneda. (rodeado)",
                "answer": "rodeado",
                "english": "At daybreak, military armored vehicles had already surrounded the La Moneda Palace.",
                "teaches": ["chile-moneda-golpe-memoria"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo exige la locución 'antes de que' en 'El presidente habló antes de que los cazabombarderos atacaran'?",
                "options": [
                    "Modo subjuntivo siempre, con independencia de que el hecho sea histórico y consumado.",
                    "Modo indicativo obligatorio cuando se alude a acontecimientos ya pasados.",
                    "Condicional simple para expresar duda temporal sobre los hechos.",
                    "Imperativo para conmemorar solemnemente a las víctimas de la tragedia."
                ],
                "correct": 0,
                "teaches": ["chile-moneda-golpe-memoria"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "música", "de", "Víctor", "Jara", "pervivió", "en", "la", "clandestinidad."],
                "solution": ["La", "música", "de", "Víctor", "Jara", "pervivió", "en", "la", "clandestinidad."],
                "english": "Víctor Jara's music survived in the underground.",
                "teaches": ["chile-moneda-golpe-memoria"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Cuándo se consumó el quebrantamiento de la república democrática?"},
                    {"speaker": "Investigadora", "text": "Tan pronto como los tanques _____ contra la sede del poder ejecutivo."}
                ],
                "options": [
                    "dispararon",
                    "dispararan",
                    "disparaban a",
                    "disparen"
                ],
                "correct": 0,
                "teaches": ["chile-moneda-golpe-memoria"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las canciones de la Nueva Canción Chilena desafiaron el silencio impuesto por la censura.",
                "english": "Songs of the Chilean New Song movement defied the silence imposed by censorship.",
                "teaches": ["chile-moneda-golpe-memoria"]
            }
        ]
    })

    # Regional 5
    write_json(f"exercises/b2/{r5}-ex.json", {
        "lesson": r5,
        "exercises": [
            {
                "id": f"{r5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["plebiscito", "direct popular vote deciding state course"],
                    ["estallido", "sudden widespread social civic protest"],
                    ["cacerolazo", "banging pots and pans as popular protest"],
                    ["reivindicación", "assertion of socioeconomic public demand"]
                ],
                "teaches": ["b2-chilecentro-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las pensiones y la salud eran precarias; de ahí que la ciudadanía __ a protestar en masa. (saliera)",
                "answer": "saliera",
                "english": "Pensions and healthcare were precarious; hence citizens went out to protest en masse.",
                "teaches": ["chile-transicion-estallido-ciudadania"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el conector consecutivo 'de ahí que' rige modo subjuntivo en la prosa culta?",
                "options": [
                    "Porque presenta la consecuencia como una explicación o derivación lógica indiscutible del hecho previo.",
                    "Porque expresa que la acción principal no llegó a suceder en la realidad fáctica.",
                    "Porque es un arcaísmo medieval que carece de uso en el periodismo actual.",
                    "Porque solo se utiliza en oraciones interrogativas directas de tono solemne."
                ],
                "correct": 0,
                "teaches": ["chile-transicion-estallido-ciudadania"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "raíz", "del", "estallido", "se", "convocó", "el", "plebiscito."],
                "solution": ["A", "raíz", "del", "estallido", "se", "convocó", "el", "plebiscito."],
                "english": "In the wake of the uprising, the plebiscite was convened.",
                "teaches": ["chile-transicion-estallido-ciudadania"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sociólogo", "text": "¿Cómo se explica la profundidad del estallido social de 2019?"},
                    {"speaker": "Politóloga", "text": "Si bien el país creció económicamente, la desigualdad _____ una fractura profunda."}
                ],
                "options": [
                    "engendró",
                    "engendre",
                    "engendrara a",
                    "engendrando"
                ],
                "correct": 0,
                "teaches": ["chile-transicion-estallido-ciudadania"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Millones de chilenos marcharon pacíficamente exigiendo un nuevo pacto constitucional solidario.",
                "english": "Millions of Chileans marched peacefully demanding a new solidarity-based constitutional pact.",
                "teaches": ["chile-transicion-estallido-ciudadania"]
            }
        ]
    })

    # Regional Consolidation
    write_json(f"exercises/b2/{r_unit}-consolidation-ex.json", {
        "lesson": f"{r_unit}-consolidation",
        "exercises": [
            {
                "id": f"{r_unit}-con.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["funicular", "hillside cable lift in Valparaíso"],
                    ["cuenca", "valley surrounded by cordillera peaks"],
                    ["laureado", "author awarded the Nobel prize"],
                    ["cacerolazo", "rhythmic pot banging protest"]
                ],
                "teaches": ["b2-chilecentro-vocab"]
            },
            {
                "id": f"{r_unit}-con.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La ciudad portuaria, en __ cerros cuelgan casas de colores, abraza la inmensidad del océano. (cuyos)",
                "answer": "cuyos",
                "english": "The port city, on whose hills hang colorful houses, embraces the vastness of the ocean.",
                "teaches": ["chile-valparaiso-puerto-patrimonio"]
            },
            {
                "id": f"{r_unit}-con.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué conector introduce adecuadamente el contraste en 'Si bien hubo logros macroeconómicos, ___ persistieron hondas brechas salariales'?",
                "options": [
                    "no obstante",
                    "por ende",
                    "dado que",
                    "de modo que"
                ],
                "correct": 0,
                "teaches": ["chile-transicion-estallido-ciudadania"]
            },
            {
                "id": f"{r_unit}-con.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "versos", "de", "Mistral", "dignificaron", "la", "tierra", "campesina."],
                "solution": ["Los", "versos", "de", "Mistral", "dignificaron", "la", "tierra", "campesina."],
                "english": "Mistral's verses dignified the peasant earth.",
                "teaches": ["chile-mistral-neruda-poesia"]
            },
            {
                "id": f"{r_unit}-con.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora", "text": "¿Por qué la transición chilena fue tan compleja y pactada?"},
                    {"speaker": "Analista", "text": "A raíz de las restricciones constitucionales, las reformas _____ lentas y difíciles."}
                ],
                "options": [
                    "fueron",
                    "fueran",
                    "hayan sido",
                    "siendo de"
                ],
                "correct": 0,
                "teaches": ["chile-transicion-estallido-ciudadania"]
            },
            {
                "id": f"{r_unit}-con.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Chile conjuga la solemnidad andina con la fuerza libertaria de sus puertos y grandes poetas.",
                "english": "Chile combines Andean solemnity with the liberating force of its ports and great poets.",
                "teaches": ["chile-centro-sintesis-regional"]
            },
            {
                "id": f"{r_unit}-con.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué síntesis define la identidad sociocultural del Chile central según el estudio regional?",
                "options": [
                    "La fecundidad del Valle Central, el laberinto cosmopolita de Valparaíso y la voz poética y cívica de su pueblo.",
                    "El aislamiento absoluto en medio de selvas impenetrables desprovistas de caminos o ciudades.",
                    "La adopción del idioma inglés como lengua oficial exclusiva en todos los colegios y puertos.",
                    "La desaparición total de las tradiciones vitivinícolas tras el terremoto de 1960."
                ],
                "correct": 0
            },
            {
                "id": f"{r_unit}-con.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura verbal articula con mayor precisión un hito de culminación histórica en Chile central?",
                "options": [
                    "La perífrasis llegar a ser combinada con sintagma nominal de reconocimiento universal.",
                    "El uso exclusivo del gerundio simple sin verbo auxiliar que lo sostenga.",
                    "La repetición enfática del adverbio 'siempre' al comienzo de cada cláusula.",
                    "La subordinación condicional irreal referida a escenarios futuros inciertos."
                ],
                "correct": 0,
                "teaches": ["chile-centro-sintesis-regional"]
            }
        ]
    })

    # -------------------------------------------------------------------------
    # 4. STORIES (7 stories: 1 classic adaptation, 6 regional stories)
    # -------------------------------------------------------------------------

    # Classic Story: Baldomero Lillo - Sub terra (El chiflón del diablo)
    story_core_22 = {
        "id": "b2-22",
        "title": "El abismo del carbón: El chiflón del diablo y el grito de Lota",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Una adaptación literaria de 'El chiflón del diablo', obra cumbre de 'Sub terra' (1904) del maestro chileno Baldomero Lillo: en las minas submarinas de carbón de Lota, el joven minero Cabeza de Cobre es forzado a trabajar en la galería más letal del yacimiento, donde la codicia patronal, la oscuridad asfixiante y el amor desgarrado de una madre desembocan en una tragedia inolvidable.",
        "characters": [
            "Joven minero Cabeza de Cobre",
            "Madre María de los Ángeles",
            "Capataz despótico de la mina",
            "Compañero barretero Pedro"
        ],
        "narration": {
            "paragraphs": [
                "En la costa gris y batida por las olas del golfo de Arauco, donde el océano Pacífico ruge con furia incansable contra los acantilados de piedra pizarra, se alzaban las fauces colosales de las minas de carbón de Lota. A fines del siglo diecinueve, la prosperidad industrial de la república chilena y el vapor que movía a los ferrocarriles y buques de guerra dependían de las entrañas negras de aquel yacimiento subterráneo que se internaba kilómetros enteros bajo el lecho marino. En la superficie, los parques señoriales de la familia Cousiño lucían fuentes de hierro fundido y palacios de mármol; pero en el fondo de la tierra, a centenares de metros bajo el agua salada, miles de barreteros descalzos y niños enganchados consumían sus vidas en galerías sofocantes donde el aire viciado olía a azufre y a humedad sepulcral.",
                "Entre aquellos condenados de la roca destacaba un muchacho de apenas veinte años a quien todos llamaban con cariño 'Cabeza de Cobre', a causa de su espesa cabellera rojiza y su temperamento leal. Huérfano de padre —un viejo barretero que había muerto años atrás sepultado por un derrumbe—, el joven sostenía con su magro jornal a su anciana madre, María de los Ángeles, y a dos hermanos pequeños. Aquella mañana aciaga, al presentarse en la boca del pique para iniciar su turno, el capataz de la mina lo apartó de su cuadrilla habitual con una sonrisa despectiva y le notificó una orden inapelable: debía trasladarse de inmediato a trabajar en 'El chiflón del diablo'.",
                "Un estremecimiento de pavor helado recorrió el cuerpo de los mineros que escucharon la disposición. El Chiflón del diablo no era una galería cualquiera: era un conducto angosto, traicionero y vertical, famoso por sus constantes desprendimientos de roca y sus emanaciones invisibles de gas grisú. La empresa, en su implacable afán de lucro, se negaba a invertir en maderamen para apuntalar los techos agrietados de aquel socavón maldito, prefiriendo enviar allí a los obreros más pobres o a los castigados por reclamar mejores pagas. Sabedor de que rechazar la orden significaba la expulsión inmediata de la choza comunal y la condena a morir de hambre en las colinas, Cabeza de Cobre agachó la frente, apretó los labios y descendió amarrado a la jaula metálica que crujía en la oscuridad del abismo.",
                "En la choza de barro y tablas del campamento minero, el corazón de María de los Ángeles presintió la tragedia con la certeza infalible de las madres del carbón. Al enterarse por los vecinos de que su hijo había sido enviado al Chiflón, la anciana arrojó el mandil, atravesó corriendo los senderos polvorientos y llegó descalza a la explanada del pique principal. Justo en ese instante, un estruendo sordo y subterráneo sacudió las colinas de Lota: la tierra tembló bajo sus pies, una bocanada espesa de humo negro brotó por la boca del pozo y la campana de alarma comenzó a repicar con su tañido fúnebre. Un derrumbe masivo había sepultado la fatídica galería.",
                "Durante horas de angustia insoportable, entre el llanto desgarrador de decenas de mujeres que clamaban por sus deudos frente a los cordones de la policía armada, la jaula del ascensor subió lentamente desde las profundidades cargando una camilla cubierta por mantas ensangrentadas. Cuando los camilleros destaparon el rostro pálido y sereno del muchacho, cuya cabellera cobriza relucía bajo el sol mortecino, la anciana no gritó ni maldijo a los capataces. Acarició la frente fría de su único amparo terrenal, contempló el abismo insondable del pique que le había arrebatado a su esposo y a su hijo, y en un rapto de dolor absoluto, se arrojó al fondo negro del pozo para unirse eternamente a sus muertos.",
                "Con *Sub terra*, Baldomero Lillo desgarró el velo de la hipocresía aristocrática chilena, convirtiendo el dolor mudo del minero en una epopeya de denuncia social imperecedera. Al evocar hoy la tragedia del Chiflón del diablo, la memoria nacional recuerda con veneración a aquellos mártires de la roca, cuya sangre derramada en las profundidades marinas iluminó el camino hacia la conquista irrenunciable de la justicia, el respeto al trabajo y la dignidad humana en el corazón de Chile."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué la galería 'El chiflón del diablo' era temida por todos los mineros del carbón de Lota?",
                        "options": [
                            "Porque era un socavón sumamente inestable y peligroso donde la empresa no apuntalaba los techos para ahorrar costos.",
                            "Porque albergaba manantiales de agua hirviendo que inundaban constantemente los túneles.",
                            "Porque era el lugar exclusivo donde los ingenieros europeos guardaban su instrumental científico.",
                            "Porque la entrada a la galería estaba prohibida para todos los ciudadanos nacidos en Chile."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Chiflón del diablo carecía de vigas de seguridad y registraba derrumbes mortales frecuentes."
                    },
                    {
                        "question": "¿Qué motivo obligó al joven 'Cabeza de Cobre' a aceptar el peligroso traslado al Chiflón?",
                        "options": [
                            "La necesidad apremiante de no ser despedido para poder sustentar a su anciana madre y a sus hermanos.",
                            "El deseo de ganar una medalla deportiva concedida por el sindicato de barreteros.",
                            "Una promesa religiosa formulada durante las fiestas de fin de año en la catedral.",
                            "El anhelo de estudiar ingeniería de minas en una universidad del extranjero."
                        ],
                        "correctIndex": 0,
                        "explanation": "El minero aceptó el riesgo mortal para no perder su salario y evitar el desalojo de su familia."
                    },
                    {
                        "question": "¿Cómo culmina la trágica historia tras confirmarse la muerte del joven obrero en el derrumbe?",
                        "options": [
                            "Su madre María de los Ángeles, enloquecida por el dolor, se arroja al abismo del pozo para morir con él.",
                            "Los trabajadores incendian las oficinas de la empresa y huyen en barcas hacia la Argentina.",
                            "El capataz de la mina renuncia a su puesto y funda una escuela nocturna para niños pobres.",
                            "El gobierno decreta el cierre definitivo de todas las minas de carbón del golfo de Arauco."
                        ],
                        "correctIndex": 0,
                        "explanation": "La madre se suicida arrojándose al pique del pozo ante el dolor insoportable de perder a su hijo."
                    }
                ]
            }
        }
    }

    # Regional Story 1: Valle Central
    story_chile_01 = {
        "id": "b2-chilecentro-01",
        "title": "El valle entre dos cordilleras: Santiago, el Mapocho y la cuenca fértil",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía geográfica y ecológica por el Valle Central de Chile: la cuenca de Santiago flanqueada por los colosos nevados de los Andes y la Cordillera de la Costa, la memoria fluvial del río Mapocho, el clima mediterráneo templado que sustenta la agricultura y vitivinicultura de exportación, y el desafío contemporáneo de la inversión térmica y el esmog urbano.",
        "characters": [
            "Geógrafo santiaguino Francisco",
            "Viticultora del valle del Maipo Andrea",
            "Ambientalista urbana Camila",
            "Anciano agricultor de Rancagua Don Pedro"
        ],
        "narration": {
            "paragraphs": [
                "En el corazón geográfico y demográfico de Chile, aprisionado entre dos gigantescas murallas orográficas de piedra y nieve, se despliega el Valle Central: una cuenca tectónica fértil y luminosa donde late el núcleo productivo, político e histórico de la nación. Al este, la Cordillera de los Andes se alza como un coloso titánico cuyas cumbres de hielo eterno, como el cerro El Plomo a más de cinco mil cuatrocientos metros de altitud, resplandecen bajo el cielo diáfano de la mañana, mientras al oeste, la más baja pero escarpada Cordillera de la Costa actúa como un biombo natural que frena el ingreso directo de la humedad marina. En este estrecho corredor intermontano que se prolonga cientos de kilómetros hacia el sur, el clima mediterráneo de veranos cálidos y secos e inviernos templados y lluviosos creó uno de los ecosistemas agrícolas más benignos y codiciados del continente.",
                "En el fondo de la cuenca principal, custodiada por los cerros tutelares Santa Lucía (Huelén) y San Cristóbal, se expande la gran metrópoli de Santiago, una ciudad de casi siete millones de habitantes fundada en 1541 por Pedro de Valdivia sobre un antiguo asentamiento administrativo incaico. Cruzando la urbe de este a oeste discurre el histórico río Mapocho, cuyas aguas parduzcas alimentadas por los deshielos cordilleranos fueron durante siglos la fuente primordial de regadío y supervivencia urbana, pero también de temibles riadas torrenciales que inundaban periódicamente los barrios coloniales de La Chimba, obligando a las autoridades virreinales a erigir los célebres tajamares de cal y canto para proteger a la población ribereña. Hoy en día, el centro histórico alrededor de la Plaza de Armas y el bullicioso Mercado Central conserva las huellas de esa herencia colonial y republicana que amalgamó la cultura hispana con las raíces indígenas.",
                "Más allá del perímetro urbano, el Valle Central se convierte en un vergel productivo sin parangón en América del Sur. En las ricas tierras sedimentarias regadas por las cuencas de los ríos Maipo, Cachapoal y Tinguiririca, los campos agrícolas producen cosechas excepcionales de frutas de exportación como cerezas, duraznos, ciruelas, manzanas y uvas de mesa. Es aquí donde florecen los prestigiosos viñedos chilenos, cuyas cepas nobles de Cabernet Sauvignon, Carménère y Syrah se benefician de la marcada oscilación térmica entre el día y la noche, generando vinos de renombre planetario que conquistan las mesas más exigentes de Europa, Asia y Norteamérica. En estos campos laboriosos perduran las tradiciones del huaso chileno con su manta tejida al telar y su chupalla de paja, celebrando cada otoño la fiesta comunitaria de la vendimia en medio del regocijo popular.",
                "Sin embargo, la particular conformación topográfica de la cuenca santiaguina encierra una severa paradoja ambiental. Durante los meses fríos del invierno, cuando las altas presiones bloquean la circulación de los vientos y la Cordillera de la Costa impide el desalojo del aire estancado, se produce el fenómeno de la inversión térmica: una capa de aire caliente en altura sella la cuenca como una tapa hermética, atrapando a nivel del suelo los humos industriales, las emisiones vehiculares y el polvo en suspensión, generando episodios críticos de esmog que ponen en jaque la salud respiratoria de los ciudadanos y exigen permanentes alertas ambientales.",
                "Frente a este desafío ecológico, Santiago y las ciudades del valle central han emprendido una profunda transformación sostenible. La recuperación paulatina de las riberas del río Mapocho mediante parques urbanos lineales, la electrificación masiva de la flota de transporte público metropolitano —la más grande del mundo fuera de China— y la protección estricta de las quebradas precordilleranas cubiertas por el milenario bosque esclerófilo de peumos, quillayes y boldos demuestran la voluntad de armonizar el crecimiento metropolitano con el respeto al entorno natural.",
                "Al contemplar el Valle Central al caer la tarde, cuando la cordillera andina se tiñe de un fulgor rosado y violeta bautizado poéticamente como el 'alboradazo', el viajero comprende la magia singular de esta geografía: un territorio fértil y laborioso donde la nieve de las cumbres alimenta la vida de los valles, recordándole al ser humano que el progreso solo es verdadero cuando honra la generosidad de la tierra que lo sustenta."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué dos cadenas montañosas delimitan geográficamente el Valle Central de Chile?",
                        "options": [
                            "La Cordillera de los Andes al este y la Cordillera de la Costa al oeste.",
                            "La cordillera del Himalaya y los montes Urales septentrionales.",
                            "La sierra de la Macarena y el escudo de las Guayanas.",
                            "Los Pirineos occidentales y la meseta del altiplano boliviano."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Valle Central chileno es una depresión intermedia flanqueada por los Andes y la Cordillera de la Costa."
                    },
                    {
                        "question": "¿En qué consiste el fenómeno meteorológico de la 'inversión térmica' que afecta a la cuenca de Santiago en invierno?",
                        "options": [
                            "Una capa de aire caliente en altura atrapa el aire frío y la contaminación en el fondo de la cuenca como una tapa.",
                            "Lluvias torrenciales de nieve salada que congelan instantáneamente los ríos de la precordillera.",
                            "La evaporación completa de las aguas del río Mapocho debido a erupciones volcánicas submarinas.",
                            "La llegada de vientos alisios que transforman el clima templado en una selva tropical lluviosa."
                        ],
                        "correctIndex": 0,
                        "explanation": "La inversión térmica impide la dispersión vertical de los contaminantes en la cuenca cerrada de Santiago."
                    },
                    {
                        "question": "¿Qué factor climático favorece la producción vitivinícola de calidad mundial en los valles del Maipo y Cachapoal?",
                        "options": [
                            "El clima mediterráneo templado combinado con una marcada oscilación térmica entre el día y la noche.",
                            "La comercialización de fertilizantes artificiales de contrabando en los puertos.",
                            "Las heladas polares constantes que impiden el crecimiento de hojas en las parras.",
                            "La cercanía con yacimientos de carbón mineral que calientan artificialmente las raíces."
                        ],
                        "correctIndex": 0,
                        "explanation": "El clima mediterráneo y la amplitud térmica diaria garantizan uvas ricas en azúcares y aromas complejos."
                    }
                ]
            }
        }
    }

    # Regional Story 2: Valparaíso
    story_chile_02 = {
        "id": "b2-chilecentro-02",
        "title": "El anfiteatro del viento: Valparaíso, funiculares y memorias portuarias",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre Valparaíso, la mítica 'Joya del Pacífico': su topografía vertical de más de cuarenta cerros que descienden en cascada hacia el océano, el apogeo comercial decimonónico como escala obligada del cabo de Hornos, la arquitectura pintoresca de madera y chapa ondulada, los centenarios ascensores funiculares y la bohemia poética que sedujo a Pablo Neruda.",
        "characters": [
            "Viejo mecánico de ascensor Don Horacio",
            "Pintor muralista porteño Sebastián",
            "Historiadora de Valparaíso Marcela",
            "Poeta bohemio de cerro Alegre Lucas"
        ],
        "narration": {
            "paragraphs": [
                "Pocas ciudades en el mundo desafían las leyes de la geometría y la gravedad con la audacia poética de Valparaíso. Recostada sobre una bahía semicircular del océano Pacífico que semeja un gigantesco anfiteatro natural, la ciudad portuaria se despliega no sobre llanuras amables, sino trepando verticalmente por las laderas escarpadas de más de cuarenta cerros habitados. Desde las cumbres de cerro Alegre, cerro Concepción, Bellavista, Artillería y Playa Ancha, una cascada vertiginosa de casas multicolores construidas en maderas nativas de roble y alerce y revestidas de chapa ondulada de zinc cuelga sobre los acantilados marinos, comunicada por un laberinto inextricable de escaleras empinadas, pasajes empedrados, callejones sinuosos y miradores ventosos que miran extasiados hacia la inmensidad plateada del mar.",
                "Durante el siglo diecinueve y hasta la apertura del Canal de Panamá en 1914, Valparaíso fue el emporio comercial y marítimo más codiciado y cosmopolita de América del Sur. Todos los veleros y vapores que doblaban el tormentoso cabo de Hornos hacían escala obligada en sus muelles para reabastecerse de víveres, reparar averías y comerciar con el trigo del valle central y el salitre del desierto norteño. En sus tabernas del barrio puerto, en su Bolsa de Comercio y en sus clubes señoriales convivían marineros ingleses, comerciantes alemanes, banqueros franceses, tipógrafos españoles e inmigrantes croatas junto a estibadores chilenos, legando a la ciudad un patrimonio arquitectónico singular donde los balcones victorianos dialogan con la arquitectura popular espontánea de los cerros.",
                "Para vencer el abismo cotidiano entre el 'plan' comercial costero y las viviendas familiares encaramadas en las cumbres, a partir de 1883 la ingeniería porteña concibió una solución emblemática: la red de ascensores funiculares de tracción por cables. Con sus cabinas de madera crujiente que ascienden con lentitud solemne por rieles empinados de hierro apoyados en pilares de piedra, ascensores históricos como El Peral, Polanco, Reina Victoria, Barón, San Agustín y Concepción se transformaron en el sistema de transporte vertical más pintoresco del mundo y en el alma móvil de la identidad urbana porteña, permitiendo a generaciones de vecinos subir diariamente cargando canastas colmadas de pescado fresco, verduras aromáticas traídas de las chacras y crujientes marraquetas calientes recién salidas del horno comunal.",
                "Esa atmósfera melancólica, bohemia y rebelde cautivó a poetas, pintores y músicos de todas las épocas. El propio Pablo Neruda, fascinado por el viento salino y los navíos errantes, construyó en el cerro Bellavista su célebre residencia 'La Sebastiana': una torre laberíntica de cinco pisos con ventanales circulares que parecían ojos de buey de barco, desde donde el poeta contemplaba las luces titilantes del puerto en la noche, coleccionaba mascarones de proa antiguos, catalejos dorados y botellas con barcos en miniatura, despidiendo el año viendo los fuegos artificiales estallando sobre las aguas mansas de la bahía porteña.",
                "Declarada Patrimonio de la Humanidad por la UNESCO en 2003, Valparaíso enfrenta hoy el reto de preservar su fragilidad material frente a los voraces incendios que bajan periódicamente por sus quebradas boscosas y al deterioro del paso del tiempo. Sin embargo, en cada rincón de sus cerros florece la resistencia creadora: jóvenes artistas han convertido los muros descascarados en lienzos de arte urbano al aire libre con murales deslumbrantes que narran la memoria obrera y las leyendas del mar, mientras los cafetines tradicionales, los almacenes de barrio y las peñas folclóricas mantienen viva la llama de la bohemia porteña al son de cuecas bravas y boleros desgarrados que resuenan entre las sombras de la noche.",
                "Al descender al anochecer por una escalera alumbrada por faroles amarillos, mientras la sirena de un buque mercante saluda a la distancia y el viento del océano agita las chapas de las techumbres, el visitante comprende la sentencia inolvidable de los poetas: Valparaíso no es una ciudad para ser explicada por la razón cartesiana, sino un puerto mágico que se ama con el corazón arrebatado, colgado eternamente entre el cielo de los cerros y el abismo azul del mar."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito geopolítico internacional en 1914 alteró el rol hegemónico de Valparaíso como emporio comercial marítimo?",
                        "options": [
                            "La apertura del Canal de Panamá, que eliminó la necesidad de doblar el cabo de Hornos para cruzar de océano a océano.",
                            "La erupción simultánea de todos los volcanes de la cordillera de la Costa.",
                            "La firma de un tratado que prohibió a los barcos extranjeros atracar en puertos del Pacífico.",
                            "La invención del avión de pasajeros que reemplazó a todos los buques de carga en un año."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Canal de Panamá desvió las rutas mundiales que antes hacían escala obligada en Valparaíso."
                    },
                    {
                        "question": "¿Qué solución de transporte urbano crearon los ingenieros porteños a fines del siglo XIX para unir el plan con los cerros?",
                        "options": [
                            "Los ascensores funiculares de madera que trepan por rieles sobre las pendientes de los cerros.",
                            "Una red de túneles subterráneos excavados enteramente bajo el agua del mar.",
                            "Globos aerostáticos impulsados por viento que transportaban a los vecinos entre cerros.",
                            "Líneas de tranvías magnéticos de alta velocidad importados de Japón."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los ascensores funiculares son el medio histórico de transporte vertical que comunica el plan con las cumbres."
                    },
                    {
                        "question": "¿Cómo se llamaba la emblemática casa que Pablo Neruda construyó en el cerro Bellavista de Valparaíso?",
                        "options": [
                            "La Sebastiana, diseñada con ventanales panorámicos y forma de barco.",
                            "La Chascona, ubicada en el desierto de Atacama.",
                            "Isla Negra, levantada en medio de las minas de Lota.",
                            "El Mirador del Carbón, situada junto a los muelles comerciales."
                        ],
                        "correctIndex": 0,
                        "explanation": "La Sebastiana es la mítica casa de Neruda en el cerro Bellavista que domina la bahía de Valparaíso."
                    }
                ]
            }
        }
    }

    # Regional Story 3: Mistral y Neruda
    story_chile_03 = {
        "id": "b2-chilecentro-03",
        "title": "La palabra iluminada: Gabriela Mistral, Pablo Neruda y el alma de Chile",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Un ensayo biográfico y lírico sobre las dos cumbres universales de la literatura chilena y latinoamericana: Gabriela Mistral (Lucila Godoy Alcayaga), maestra rural del valle del Elqui y primera Nobel del continente (1945), defensora de la infancia y los pueblos originarios; y Pablo Neruda (Neftalí Reyes), el torrente lírico de Isla Negra y Nobel en 1971, cantor de la materia, el amor y las luchas populares.",
        "characters": [
            "Poeta e investigadora literaria Paulina",
            "Catedrático de literatura chilena Gonzalo",
            "Maestra rural de Vicuña doña Elena",
            "Pescador de Isla Negra don Juvenal"
        ],
        "narration": {
            "paragraphs": [
                "Pocos países en el mundo han visto su alma nacional esculpida por la poesía con tanta hondura y fecundidad como Chile. Designada universalmente como 'tierra de poetas', la patria austral ostenta el privilegio singular de haber dado al siglo veinte a dos de las voces líricas más poderosas, universales y disímiles de la literatura hispánica: Gabriela Mistral y Pablo Neruda. Ambos laureados con el Premio Nobel de Literatura —Mistral en 1945, marcando el hito de ser la primera escritora de América Latina en recibirlo, y Neruda en 1971—, forjaron con sus versos una cartografía espiritual donde la geografía indómita de los Andes y del mar se entrelaza con el clamor moral de la dignidad humana.",
                "Nacida en 1889 en el pequeño pueblo de Vicuña en el árido y luminoso valle del Elqui bajo el nombre de Lucila Godoy Alcayaga, Gabriela Mistral creció en medio de la soledad agreste de las viñas de pisco y los cerros secos. Maestra rural autodidacta desde su adolescencia, enseñó a leer a niños campesinos y descalzos en escuelas humildes de La Serena, Traiguén y Punta Arenas, colaborando más tarde en México con José Vasconcelos en la trascendental reforma educativa popular de esa nación hermana. Su poesía, inaugurada con la desgarradora intensidad de los *Sonetos de la muerte* y consagrada en volúmenes como *Desolación*, *Tala* y *Lagar*, trasciende el lamento personal para convertirse en una plegaria cósmica por los desposeídos, una defensa radical de los derechos de la infancia, una exaltación de la herencia indígena y una meditación dolorosa sobre la maternidad y el desarraigo del exilio diplomático.",
                "En las antípodas estilísticas y vivenciales de la mesura franciscana de Mistral floreció el torrente volcánico y desbordante de Pablo Neruda (nacido en Parral en 1904 como Neftalí Reyes Basoalto). Criado en las lluvias torrenciales y los bosques milenarios de la frontera de Temuco, Neruda revolucionó la lírica castellana a los veinte años con *Veinte poemas de amor y una canción desesperada*, el libro de poesía más leído y memorizado en lengua española. Más tarde, testigo directo del dolor de la Guerra Civil Española donde editó *España en el corazón* impreso por soldados en el frente de batalla, y de la persecución política en su propia tierra, su voz maduró en la cumbre monumental del *Canto General*, donde reconstruyó la epopeya histórica de todo el continente americano desde sus raíces precolombinas hasta las luchas mineras de su tiempo.",
                "En su refugio marino de Isla Negra, una colina rocosa frente al rugido implacable del Pacífico sur, Neruda coleccionaba mascarones de proa de antiguos navíos, caracolas marinas gigantescas, botellas con barcos de madera y mapas antiguos, dialogando a diario con las olas espumosas. Allí compuso sus célebres *Odas elementales*, poemas de una asombrosa sencillez formal y pureza rítmica dedicados no a grandes héroes ni a batallas heroicas, sino a los objetos cotidianos y humildes de la existencia humana: el pan, la cebolla, el aire, el cobre, el vino y los zapatos viejos.",
                "A pesar de sus diferencias de temperamento y cosmovisión política, Mistral y Neruda compartieron un compromiso ético inquebrantable con la emancipación de su pueblo. Gabriela, con su prosa ensayística visionaria que anticipó el ecofeminismo y la integración panamericana; Pablo, con su oratoria combativa que defendió a los obreros del salitre y los trabajadores del carbón desde su escaño senatorial, demostraron que la alta literatura en América Latina no es un adorno aristocrático para salones burgueses, sino un escudo de fuego contra la injusticia.",
                "Al visitar la tumba sencilla de Gabriela Mistral en Montegrande entre los viñedos soleados del Elqui, o al contemplar la sepultura de Neruda junto a su amada Matilde Urrutia sobre las rocas azotadas por la espuma en Isla Negra, el viajero comprende la lección suprema de los grandes bardos chilenos: la palabra poética no muere con el paso de las estaciones, sino que permanece latiendo eternamente en la memoria de un pueblo que aprendió a cantar su dolor y su esperanza bajo la luz infinita de las estrellas australes."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito histórico continental protagonizó Gabriela Mistral en el año 1945?",
                        "options": [
                            "Fue la primera personalidad literaria de América Latina en recibir el Premio Nobel de Literatura.",
                            "Fue elegida presidenta constitucional de la República de Chile en comicios universales.",
                            "Fundó la primera universidad politécnica estatal de la región austral.",
                            "Dirigió la expedición científica que descubrió las ruinas submarinas de Valparaíso."
                        ],
                        "correctIndex": 0,
                        "explanation": "Gabriela Mistral marcó un hito al ganar el primer Premio Nobel literario para América Latina en 1945."
                    },
                    {
                        "question": "¿Qué temas singulares abordó Pablo Neruda en sus célebres 'Odas elementales'?",
                        "options": [
                            "Celebró objetos cotidianos y humildes como el pan, la cebolla, el aire y el vino con lenguaje accesible.",
                            "Redactó manuales técnicos de navegación a vela para barcos mercantes británicos.",
                            "Escribió tratados de derecho penal militar para la armada nacional.",
                            "Compuso himnos religiosos exclusivamente dedicados a emperadores romanos antiguos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las Odas elementales exaltan la dignidad poética de las cosas sencillas de la vida diaria."
                    },
                    {
                        "question": "¿Qué rasgo común unió el magisterio ético de Gabriela Mistral y de Pablo Neruda?",
                        "options": [
                            "Un compromiso inquebrantable con los derechos humanos, la infancia y la dignidad de los sectores postergados.",
                            "La decisión de renunciar a la lengua española para escribir únicamente en latín clásico.",
                            "El apoyo incondicional a los monopolios salitreros extranjeros en el norte del país.",
                            "El rechazo a cualquier tipo de educación pública en las comunidades rurales campesinas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Ambos poetas emplearon su prestigio mundial para abogar por la justicia social y la educación popular."
                    }
                ]
            }
        }
    }

    # Regional Story 4: 11 de Septiembre
    story_chile_04 = {
        "id": "b2-chilecentro-04",
        "title": "El día que quebró la historia: El Palacio de La Moneda y el canto que no calla",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica histórica sobre el golpe de Estado del 11 de septiembre de 1973 en Chile: el asedio y bombardeo aéreo del Palacio de La Moneda, las últimas palabras de Salvador Allende al pueblo a través de Radio Magallanes, la represión feroz en el Estadio Nacional, el martirio de Víctor Jara y la preservación clandestina de la memoria democrática.",
        "characters": [
            "Periodista de Radio Magallanes",
            "Músico de la Nueva Canción Chilena",
            "Fotógrafo documental de Santiago",
            "Abogada de derechos humanos Carmen"
        ],
        "narration": {
            "paragraphs": [
                "La mañana del martes 11 de septiembre de 1973 amaneció en la capital chilena con una quietud espectral y amenazante bajo un cielo plomizo que presagiaba la tormenta política más desgarradora del siglo. En el Palacio de La Moneda, la señorial mansión de arquitectura neoclásica del siglo dieciocho que albergaba la presidencia de la república en el corazón urbano de Santiago, el mandatario socialista Salvador Allende ingresaba a su despacho antes de las ocho de la mañana. Horas antes, las tropas de la Armada se habían sublevado en el puerto de Valparaíso, y en cuestión de minutos los regimientos blindados del Ejército tomaron las esquinas céntricas, desconectaron las emisoras de radio leales al gobierno y rodearon la sede del poder ejecutivo con tanques, tanquetas y francotiradores apostados en los tejados de los ministerios circundantes.",
                "A las nueve y diez de la mañana, mientras los disparos de fusilería retumbaban contra las gruesas paredes de adobe y cal de La Moneda, Allende se dirigió por última vez al pueblo chileno a través de la única línea telefónica que permanecía enlazada con la combativa Radio Magallanes. En un discurso histórico improvisado con serenidad sobrecogedora y firmeza indestructible, el presidente proclamó que pagaría con su vida la lealtad del pueblo, negándose a renunciar ante los golpistas y profetizando con fe inquebrantable que, más temprano que tarde, 'se abrirán las grandes alamedas por donde pase el hombre libre, para construir una sociedad mejor'. Minutos después de emitirse el mensaje, la antena de la radioemisora fue ametrallada y silenciada.",
                "Poco antes del mediodía tuvo lugar la escena más dantesca y traumática en los dos siglos de historia republicana de Chile: dos aviones cazabombarderos Hawker Hunter de la Fuerza Aérea sobrevolaron a baja altura la plaza de la Constitución y lanzaron cohetes de alta precisión contra el palacio presidencial. En segundos, las columnas de fuego y humo negro envolvieron los salones de gobierno, los techos se desplomaron en llamas y el presidente Allende cayó muerto en el salón Independencia antes de que la infantería asaltara las ruinas humeantes, dando inicio a diecisiete años de cruenta dictadura militar encabezada por el general Augusto Pinochet.",
                "La maquinaria represiva del régimen se desplegó de inmediato con ferocidad implacable en todo el territorio nacional. Miles de obreros fabriles, estudiantes universitarios, campesinos y funcionarios de izquierda fueron detenidos en allanamientos masivos y concentrados en campos improvisados como el Estadio Chile y el Estadio Nacional. Entre los prisioneros se encontraba el querido cantor popular y director de teatro Víctor Jara, alma insustituible de la Nueva Canción Chilena. Sometido a brutales torturas donde sus verdugos le quebraron las manos para burlarse de su guitarra, Víctor escribió en un pedazo de papel clandestino su último poema testimonial —*Somos cinco mil aquí en esta pequeña parte de la ciudad*— antes de ser acribillado a tiros en los sótanos del recinto.",
                "A pesar de los bandos militares que prohibieron los partidos, clausuraron el parlamento y quemaron libros en las plazas públicas, el canto y la memoria no pudieron ser borrados de la historia. En la clandestinidad de las poblaciones obreras como La Victoria y La Legua, en los talleres de la Vicaría de la Solidaridad donde mujeres valientes bordaban en arpillera los nombres de sus familiares detenidos desaparecidos, y en los escenarios del exilio europeo y latinoamericano donde grupos como Inti-Illimani y Quilapayún alzaron su voz con charangos y quenas, la dignidad democrática resistió sin doblegarse.",
                "Medio siglo después de aquel quiebre trágico, al caminar por la plaza de la Constitución frente a la estatua de Salvador Allende que mira hacia las grandes alamedas de Santiago, o al visitar el Memorial de los Derechos Humanos en el Cementerio General y recintos recuperados como Villa Grimaldi y Londres 38, la sociedad chilena honra a sus mártires con una convicción indeleble: que la democracia, la memoria y la justicia no son dones fortuitos, sino conquistas sagradas que deben defenderse a diario para que nunca más la bota de la intolerancia vuelva a pisotear la patria."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿A través de qué medio de comunicación transmitió Salvador Allende su célebre discurso final el 11 de septiembre de 1973?",
                        "options": [
                            "A través de Radio Magallanes, enlazada por teléfono desde su despacho en el palacio en llamas.",
                            "Mediante un mensaje satelital emitido por la cadena de televisión británica BBC.",
                            "En una conferencia de prensa convocada en el aeropuerto internacional de Pudahuel.",
                            "Por medio de un telegrama impreso repartido por los carteros del centro de Santiago."
                        ],
                        "correctIndex": 0,
                        "explanation": "Allende habló a la nación a través de Radio Magallanes minutos antes del bombardeo a La Moneda."
                    },
                    {
                        "question": "¿Qué artista y trovador de la Nueva Canción Chilena fue detenido y asesinado en el Estadio Chile tras el golpe militar?",
                        "options": [
                            "Víctor Jara, prolífico cantor popular y director teatral que compuso poemas hasta su muerte.",
                            "El poeta barroco Alonso de Ercilla y Zúñiga.",
                            "El pintor muralista mexicano Diego Rivera.",
                            "El director de cine italiano Federico Fellini."
                        ],
                        "correctIndex": 0,
                        "explanation": "Víctor Jara fue torturado y asesinado en el Estadio Chile, convirtiéndose en símbolo de la resistencia cultural."
                    },
                    {
                        "question": "¿Qué manifestación textil artesanal crearon las mujeres chilenas para denunciar la desaparición de sus familiares?",
                        "options": [
                            "Las arpilleras bordadas con retazos de tela que representaban las violaciones a los derechos humanos.",
                            "Banderas de seda blanca bordadas con hilos de oro para las ceremonias de los cuarteles militares.",
                            "Veleros de mimbre flotantes que se enviaban por el océano Pacífico hacia la Antártida.",
                            "Ponchos impermeables de cuero para los oficiales de aduanas en los pasos cordilleranos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las arpilleras fueron tapices artesanales bordados por madres y esposas para denunciar las desapariciones."
                    }
                ]
            }
        }
    }

    # Regional Story 5: Transición y Estallido
    story_chile_05 = {
        "id": "b2-chilecentro-05",
        "title": "La primavera rebelde: Del plebiscito del 88 al despertar de la Plaza Dignidad",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la evolución sociopolítica chilena de las últimas tres décadas: la histórica victoria del 'No' en el plebiscito de 1988 con la franja del arcoíris, la transición democrática tutelada y el auge macroeconómico neoliberal, el malestar acumulado por las pensiones y la educación, el 'estallido social' de octubre de 2019 en Plaza Baquedano (Plaza Dignidad) y la encrucijada constituyente.",
        "characters": [
            "Estudiante secundaria manifestante Sofía",
            "Economista de la Concertación Don Manuel",
            "Jubilada profesora marchante Señora Irene",
            "Periodista de prensa independiente Matías"
        ],
        "narration": {
            "paragraphs": [
                "El 5 de octubre de 1988, Chile vivió una jornada de heroísmo cívico y valentía electoral que asombró a la comunidad internacional. Tras quince años de dictadura feroz, el pueblo chileno concurrió masivamente a las urnas para responder con un lápiz grafito a un dilema existencial: si el general Augusto Pinochet continuaría en el poder por ocho años más o si se convocaría a elecciones presidenciales abiertas. Pese a las amenazas del aparato estatal y el miedo acumulado en los hogares, la franja televisiva opositora, encabezada por el esperanzador arcoíris multicolor de la campaña del 'No' y la pegajosa canción 'Chile, la alegría ya viene', derrotó democráticamente al régimen con un contundente cincuenta y seis por ciento de los votos, abriendo las puertas a la recuperación de la institucionalidad republicana.",
                "En marzo de 1990 asumió la presidencia Patricio Aylwin, inaugurando el ciclo de gobiernos de la Concertación de Partidos por la Democracia. Durante las siguientes tres décadas, Chile experimentó una era de extraordinaria estabilidad política y expansión macroeconómica: la pobreza extrema se redujo de más del cuarenta por ciento a un dígito, se modernizaron las autopistas y puertos, y el país fue catalogado por los organismos multilaterales como el 'oasis' y el modelo de éxito indiscutible de América Latina. Sin embargo, aquel crecimiento descansaba sobre los cimientos inmutables de la Constitución de 1980 y un modelo neoliberal radical que privatizó el agua, la salud, la educación y los fondos de pensiones (las AFP), creando una sociedad de altísima segregación territorial y endeudamiento familiar crónico.",
                "El 18 de octubre de 2019, la aparente serenidad del oasis se quebró con la fuerza de un terremoto social. Lo que comenzó como una protesta estudiantil secundaria de evasión masiva del torniquete en el metro de Santiago por un aumento de treinta pesos en el pasaje escolar derivó en cuestión de horas en el mayor levantamiento ciudadano en la historia contemporánea de Chile: el 'estallido social'. Bajo la consigna unánime de '¡No son treinta pesos, son treinta años!', millones de trabajadores, jubilados, jóvenes y familias enteras coparon las calles del país golpeando cacerolas, denunciando que mientras las grandes empresas se coludían para fijar precios abusivos de medicamentos y pollos, los ancianos recibían pensiones miserables que no alcanzaban para cubrir los servicios básicos.",
                "El epicentro de aquella marejada ciudadana fue la céntrica Plaza Baquedano de Santiago, rebautizada popularmente por los manifestantes como 'Plaza Dignidad'. El 25 de octubre, más de un millón doscientas mil personas marcharon pacíficamente en una postal conmovedora donde ondeaban banderas chilenas, emblemas del pueblo mapuche y carteles que exigían una salud digna y educación gratuita. Aunque la represión de las fuerzas policiales dejó un saldo doloroso de cientos de jóvenes con traumas oculares por perdigones y denuncias de excesos de fuerza, la energía popular resultó incontenible para el sistema político tradicional.",
                "Para canalizar la crisis por vías pacíficas y democráticas, en la madrugada del 15 de noviembre de 2019 las principales fuerzas políticas firmaron el histórico 'Acuerdo por la Paz Social y la Nueva Constitución'. Un año después, en un plebiscito nacional inolvidable, casi el ochenta por ciento de los chilenos aprobó enterrar definitivamente la carta fundamental de la dictadura mediante una asamblea constituyente paritaria y con escaños reservados para pueblos originarios, iniciando un complejo e intenso proceso de deliberación ciudadana sobre las bases del futuro común.",
                "Al contemplar hoy el horizonte del Chile contemporáneo, el observador percibe la madurez profunda de un pueblo que aprendió que el desarrollo económico es insostenible si no va de la mano con la cohesión social y el respeto irrestricto a los derechos de las mayorías. En la memoria viva de la Plaza Dignidad y en el debate democrático constante late la certeza de que el porvenir se construye con la participación consciente de toda la ciudadanía, confirmando que la primavera de la justicia siempre florece cuando una nación decide ser dueña de su propio destino."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué hito electoral pacífico marcó el principio del fin de la dictadura militar chilena en 1988?",
                        "options": [
                            "La victoria de la opción 'No' en el plebiscito nacional con la campaña del arcoíris multicolor.",
                            "Un golpe de estado parlamentario que destituyó al gabinete ministerial en pleno.",
                            "La invasión de tropas aliadas de cascos azules autorizada por las Naciones Unidas.",
                            "La suspensión definitiva de la moneda nacional y la adopción del marco alemán."
                        ],
                        "correctIndex": 0,
                        "explanation": "El triunfo del 'No' en el plebiscito del 5 de octubre de 1988 abrió el camino hacia la democracia."
                    },
                    {
                        "question": "¿Qué consigna popular sintetizó el profundo malestar ciudadano que detonó el estallido social de octubre de 2019?",
                        "options": [
                            "'¡No son treinta pesos, son treinta años!', denunciando décadas de desigualdad estructural privatizada.",
                            "'¡Queremos que los teléfonos celulares sean gratuitos para todos los turistas extranjeros!'.",
                            "'¡Exigimos trasladar la capital de la república a las islas de la Antártida!'.",
                            "'¡Prohibamos los trenes de carga para usar únicamente carretas de bueyes coloniales!'."
                        ],
                        "correctIndex": 0,
                        "explanation": "La consigna expresó que el alza del metro fue solo la gota que colmó el vaso tras décadas de abusos sociales."
                    },
                    {
                        "question": "¿Cuál fue la salida institucional acordada por las fuerzas políticas para resolver democráticamente la crisis del estallido social?",
                        "options": [
                            "La convocatoria a un plebiscito para redactar una nueva Constitución Política del Estado.",
                            "La disolución de todas las universidades del país y el cierre de las fronteras aéreas.",
                            "La entrega del control del cobre a consorcios privados sin pagar impuestos.",
                            "La prórroga indefinida del estado de sitio sin elecciones por dos décadas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Acuerdo por la Paz de noviembre de 2019 encauzó la demanda ciudadana en un proceso constituyente democrático."
                    }
                ]
            }
        }
    }

    # Regional Story 6: Capstone regional (Chile Central)
    story_chile_capstone = {
        "id": "b2-chilecentro-consolidation",
        "title": "El corazón del Valle Central: Poesía, mar y dignidad en el Chile central",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis abarcadora de los Estudios Regionales sobre el Chile central: la geografía fértil del Valle Central enmarcada por los Andes y la costa, la arquitectura anfiteatral y los funiculares de Valparaíso, el magisterio poético ecuménico de Gabriela Mistral y Pablo Neruda, la memoria democrática de La Moneda y el horizonte ciudadano forjado desde el plebiscito del 88 hasta el estallido social.",
        "characters": [
            "Salvador Allende",
            "Gabriela Mistral",
            "Pablo Neruda",
            "Pueblo porteño y santiaguino"
        ],
        "narration": {
            "paragraphs": [
                "En el corazón geográfico y espiritual del Cono Sur americano, el territorio de Chile central se alza como un crisol extraordinario donde la majestad imponente de la naturaleza dialoga íntimamente con la palabra poética, la vocación marítima y una inquebrantable conciencia cívica. Flanqueado al oriente por las murallas colosales de la Cordillera de los Andes y al poniente por la Cordillera de la Costa, el Valle Central demostró a lo largo de cinco siglos que la fertilidad de sus tierras regadas por aguas glaciares y la templanza de su clima mediterráneo son el lecho nutricio donde germinó la identidad republicana más vigorosa y compleja de la patria chilena.",
                "En el regazo de esta cuenca fértil se levanta Santiago, la gran metrópoli donde el río Mapocho sigue recordando su curso histórico mientras rascacielos modernos se recortan contra el telón de fondo de los ventisqueros andinos y los cerros tutelares Santa Lucía y San Cristóbal. Hacia el sur de la cuenca, en los fértiles valles del Maipo, Cachapoal y Colchagua, los viñedos centenarios transforman el sol templado en caldos de reconocimiento internacional, mientras la cultura campesina del huaso tradicional mantiene viva la cueca campesina, el apego a la tierra fecunda y los lazos de cooperación comunitaria que forjaron el temple laborioso y hospitalario de su gente en cada faena rural.",
                "Siguiendo el curso de las brisas oceánicas hacia el poniente, la costa revela su joya más deslumbrante y melancólica: la bahía anfiteatral de Valparaíso. Con sus más de cuarenta cerros salpicados de casas de chapa policromada colgadas sobre el abismo y sus centenarios ascensores funiculares de madera que trepan con cadencia de carillón, el mítico puerto cosmopolita custodia la memoria de los veleros que doblaban el cabo de Hornos y el alma bohemia de los estibadores, poetas, músicos y marineros del mundo que dejaron su impronta imborrable en cada rincón, mirador y pasaje empinado frente al Pacífico inmenso.",
                "En esa misma geografía marina y montañosa floreció la palabra inmortal de sus dos Premios Nobel: Gabriela Mistral y Pablo Neruda. Desde el valle árido del Elqui hasta los roquedales rumorosos de Isla Negra, Gabriela y Pablo demostraron a la humanidad entera que la poesía en Chile no es un ejercicio formalista para élites letradas, sino la voz moral de los niños campesinos, el canto apasionado al trabajo obrero, la comunión con las materias cotidianas y la defensa irrenunciable de los pueblos postergados de América.",
                "Esa fuerza moral fue sometida a su prueba más desgarradora el 11 de septiembre de 1973 en las llamas del Palacio de La Moneda. Pero ni el bombardeo aéreo a la casa de gobierno, ni el martirio de Salvador Allende y Víctor Jara, ni los diecisiete años de dictadura militar pudieron quebrar la raíz democrática de la nación. En la clandestinidad de las poblaciones, en los telares de las arpilleras y en la resistencia del canto popular con charangos y guitarras se incubó la histórica victoria del 'No' en el plebiscito de 1988, devolviendo la patria a los caminos de la soberanía republicana.",
                "Y en octubre de 2019, cuando las alamedas de Santiago y la emblemática Plaza Dignidad se colmaron con más de un millón de personas que salieron a golpear cacerolas exigiendo un nuevo pacto de justicia, salud digna y educación compartida, el pueblo chileno confirmó que su historia no está congelada en manuales escolares, sino viva y palpitante en el reclamo soberano de sus derechos comunes y de una nueva carta constitucional verdaderamente ciudadana.",
                "Al contemplar hoy el horizonte del Chile central al atardecer, cuando la cordillera andina se ilumina con su fulgor púrpura y las luces de los cerros de Valparaíso comienzan a titilar sobre el Pacífico, el viajero comprende la grandeza indeleble de esta tierra: un país donde el barroco del mar, el dolor de la historia y el fuego de la poesía se entrelazan en un himno indestructible de esperanza, fraternidad y dignidad humana que continúa inspirando al mundo entero."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis geográfica, cultural e histórica singulariza al Chile central en América del Sur?",
                        "options": [
                            "La fertilidad del Valle Central, los cerros poéticos de Valparaíso y la memoria cívica de lucha por la dignidad democrática.",
                            "Un archipiélago polar desprovisto de vegetación donde no existe historia literaria conservada.",
                            "Una selva amazónica pantanosa dominada exclusivamente por el cultivo del café y el caucho.",
                            "Un desierto salino sin ciudades ni acceso a las costas del océano Pacífico."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Chile central reúne la agricultura del valle, la bohemia portuaria de Valparaíso y el legado de grandes poetas y luchas cívicas."
                    },
                    {
                        "question": "¿De qué manera la literatura (Mistral, Neruda, Lillo) dialoga con la historia social del país?",
                        "options": [
                            "Dando voz poética a las demandas de justicia, al dolor de los mineros y a la defensa de los derechos humanos y campesinos.",
                            "Promoviendo exclusivamente la compra de títulos nobiliarios europeos para los políticos locales.",
                            "Eliminando cualquier mención a la geografía chilena para imitar novelas policiales extranjeras.",
                            "Prohibiendo la lectura en las escuelas rurales para evitar el debate político."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los grandes autores chilenos enraizaron su obra en las luchas sociales y la dignidad de los trabajadores y campesinos."
                    },
                    {
                        "question": "¿Qué continuidad histórica une la resistencia de La Moneda en 1973 con las movilizaciones de octubre de 2019?",
                        "options": [
                            "La búsqueda irrenunciable del pueblo chileno por construir una sociedad libre, justa y democrática a través de la soberanía popular.",
                            "La decisión de clausurar el sistema escolar para que los jóvenes no aprendan historia contemporánea.",
                            "La exigencia de restablecer la monarquía hispánica colonial como único sistema de gobierno.",
                            "La orden de destruir todos los funiculares de Valparaíso por considerarlos obsoletos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Ambos momentos históricos encarnan el anhelo del pueblo por justicia social y autodeterminación democrática."
                    }
                ]
            }
        }
    }

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

    # Write stories
    # Core classic story:
    write_json(f"stories/classics/b2/{c_unit}.json", to_schema_story(story_core_22))
    # Regional lesson stories:
    write_json(f"stories/world/b2/{r1}.json", to_schema_story(story_chile_01, r1))
    write_json(f"stories/world/b2/{r2}.json", to_schema_story(story_chile_02, r2))
    write_json(f"stories/world/b2/{r3}.json", to_schema_story(story_chile_03, r3))
    write_json(f"stories/world/b2/{r4}.json", to_schema_story(story_chile_04, r4))
    write_json(f"stories/world/b2/{r5}.json", to_schema_story(story_chile_05, r5))
    write_json(f"stories/world/b2/{r6_con}.json", to_schema_story(story_chile_capstone, r6_con))
    write_json(f"stories/world/b2/{r_unit}.json", to_schema_story(story_chile_capstone, r_unit))

    # -------------------------------------------------------------------------
    # 5. LESSON FILES (6 Core + 6 Regional)
    # -------------------------------------------------------------------------
    core_lessons_info = [
        ("b2-22-01", "lesson.b2.22.01", "Los verbos de cambio ponerse y quedarse",
         "Master verbs of becoming 'ponerse' and 'quedarse' to express sudden emotional reactions and resulting states.",
         "verbos de cambio ponerse y quedarse: reacciones anímicas y estados resultantes",
         ["Deploy 'ponerse' with emotional and physical adjectives for temporary reactions.", "Utilize 'quedarse' to emphasize the final resulting condition or deprivation.", "Distinguish between voluntary decisions and involuntary states."]),
        ("b2-22-02", "lesson.b2.22.02", "Los verbos de cambio hacerse y volverse",
         "Deploy 'hacerse' for voluntary professional/ideological changes and 'volverse' for involuntary character shifts.",
         "verbos de cambio hacerse y volverse: voluntad frente a cambio involuntario de carácter",
         ["Select 'hacerse' for gradual or voluntary ideological and career developments.", "Apply 'volverse' for permanent involuntary transformations in temperament.", "Avoid using 'hacerse' with involuntary psychological disorders."]),
        ("b2-22-03", "lesson.b2.22.03", "Convertirse en y transformarse en: metamorfosis radical",
         "Master 'convertirse en' and 'transformarse en' for categorical metamorphosis and profound structural change.",
         "convertirse en y transformarse en: metamorfosis categorial y régimen preposicional",
         ["Enforce the mandatory preposition 'en' before noun phrases.", "Describe radical societal, urban, and historical conversions.", "Distinguish categorical noun transformations from adjectival states."]),
        ("b2-22-04", "lesson.b2.22.04", "La perífrasis llegar a ser: culminación de un proceso",
         "Deploy the periphrasis 'llegar a ser' to capture the culmination of prolonged endeavor and public recognition.",
         "perífrasis llegar a ser: culminación de trayectoria vital y logro histórico",
         ["Highlight long-term effort and perseverance culminating in prominent status.", "Apply 'llegar a ser' in biographical and artistic historical portraits.", "Avoid using 'llegar a ser' for sudden accidental occurrences."]),
        ("b2-22-05", "lesson.b2.22.05", "Selección estilística y matices en los verbos de cambio",
         "Select with stylistic mastery among all verbs of becoming and integrate derived lexical change verbs in formal prose.",
         "criterios de selección estilística y alternancia léxica en los verbos de devenir",
         ["Evaluate semantic nuances across the entire paradigm of becoming verbs.", "Integrate synthetic derived verbs (enrojecer, empobrecerse, ensombrecer) for concision.", "Produce balanced and nuanced analytical prose following CEFR B2 house style."])
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
    write_json(f"lessons/b2/{l6_con}.json", {
        "id": "lesson.b2.22.consolidation",
        "title": "Consolidación B2: Verbos de cambio y Sub terra de Baldomero Lillo",
        "level": "B2",
        "goal": "Synthesize verbs of becoming and transformation through Baldomero Lillo's Chilean mining classic El chiflón del diablo.",
        "grammar": "síntesis del paradigma de verbos de cambio y adaptación de Sub terra",
        "sections": [
            {"type": "goal", "items": [
                "Master functional distinctions between ponerse, quedarse, volverse, and hacerse.",
                "Deploy convertirse en and llegar a ser with correct syntax and register in formal prose.",
                "Analyze the human tragedy and social denunciation of the Lota coal miners in Chilean realism."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{c_unit}-con.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Distingo entre cambios transitorios (ponerse) y estados resultantes (quedarse).",
                "Utilizo 'hacerse' para evoluciones voluntarias y 'volverse' para cambios de carácter.",
                "Construyo correctamente 'convertirse en' con la preposición 'en' y sintagma nominal.",
                "Aplico 'llegar a ser' para resaltar el mérito acumulado de una trayectoria vital.",
                "Selecciono con fluidez y variedad léxica los verbos de devenir en la prosa ensayística."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-chilecentro-01", "lesson.b2.chilecentro.01", "El Valle Central, los Andes nevados y el clima mediterráneo",
         "Explore the physical geography of Chile's Central Valley, Andean glacial hydrology, and Mediterranean climate.",
         "geografía del Valle Central, clima mediterráneo y aspecto imperfectivo en la narración",
         ["Analyze the physical relief between the Andes and Coastal ranges.", "Deploy imperfective aspect in spatial and climatic descriptions.", "Deploy valley geography, thermal inversion, and viticulture vocabulary (cuenca, inversión, viñedo, mediterráneo)."]),
        ("b2-chilecentro-02", "lesson.b2.chilecentro.02", "Valparaíso: Funiculares, cerros y bohemia portuaria",
         "Investigate the steep urban topography of Valparaíso, 19th-century maritime commerce, and historic funicular lifts.",
         "urbanismo vertical de Valparaíso, funiculares y oraciones de relativo locativo con cuyo",
         ["Analyze the amphitheater bay topography and hillside architecture.", "Deploy complex relative clauses with 'cuyo' in spatial urban narratives.", "Deploy port architecture, funicular lifts, and bohemian identity vocabulary (funicular, anfiteatro, bohemia, cerro)."]),
        ("b2-chilecentro-03", "lesson.b2.chilecentro.03", "Gabriela Mistral y Pablo Neruda: La patria en la poesía",
         "Explore the literary and moral legacies of Chile's two Nobel laureates, Gabriela Mistral and Pablo Neruda.",
         "análisis lírico comparativo, valoración estética y matrices de certeza frente a subjuntivo",
         ["Analyze Mistral's rural pedagogical roots in the Elqui Valley and defense of children.", "Examine Neruda's oceanic poetry at Isla Negra and celebration of elemental things.", "Deploy poetic analysis, rurality, and lyric vocabulary (laureado, lírica, ruralidad, oda)."]),
        ("b2-chilecentro-04", "lesson.b2.chilecentro.04", "El 11 de septiembre de 1973 y el Palacio de La Moneda",
         "Analyze the military coup of September 11, 1973, the bombardment of La Moneda, and the defense of democratic memory.",
         "secuenciación temporal retrospectiva, correlación de pasados y subordinación temporal con antes de que",
         ["Trace the historical sequence of the 1973 coup d'état at La Moneda.", "Deploy past temporal correlations and subjunctive selection after 'antes de que'.", "Deploy democratic memory, political resistance, and folk music vocabulary (quiebre, bombardeo, trovador, memorial)."]),
        ("b2-chilecentro-05", "lesson.b2.chilecentro.05", "La transición a la democracia y el estallido social de 2019",
         "Examine the 1988 'No' plebiscite, the democratic transition, economic growth, and the 2019 social uprising.",
         "debate sociopolítico chileno, marcadores contraargumentativos y conectores consecutivos",
         ["Analyze the historic victory of the 'No' plebiscite and return to democracy.", "Deploy discourse connectors (si bien, no obstante, de ahí que) in development debates.", "Deploy civic protest, plebiscite, and constitutional assembly vocabulary (plebiscito, estallido, cacerolazo, cabildo)."])
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
    write_json(f"lessons/b2/{r6_con}.json", {
        "id": "lesson.b2.chilecentro.consolidation",
        "title": "Consolidación Regional: Palabra y memoria en el Valle Central",
        "level": "B2",
        "goal": "Consolidate regional studies on central Chile: Central Valley ecology, Valparaíso heritage, Mistral and Neruda poetry, La Moneda memory, and 2019 civic mobilization.",
        "grammar": "síntesis de estudios regionales del Chile central: geografía, Valparaíso, poesía de Nobel y memoria democrática",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize Central Valley agricultural hydrology, port architecture, and funicular heritage.",
                "Appreciate the universal lyric voices of Gabriela Mistral and Pablo Neruda.",
                "Reflect on Chilean democratic resilience from 1973 to the constitutional crossroads."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r6_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{r6_con}-ex.json", "exerciseRefs": [f"{r_unit}-con.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la geografía del Valle Central y el clima mediterráneo entre dos cordilleras.",
                "Reconozco el valor patrimonial y los funiculares de la bahía anfiteatral de Valparaíso.",
                "Valoro la trascendencia lírica y ética de Gabriela Mistral y Pablo Neruda.",
                "Analizo el impacto histórico del quiebre democrático de 1973 y la defensa de la memoria.",
                "Explico la trayectoria cívica desde el plebiscito del 88 hasta el estallido social de 2019."
            ]}
        ]
    })

    print("Completed LatAm Unit 22 (Chile Centro) generation!")

    # -------------------------------------------------------------------------
    # 6. UPDATE CURRICULUM UNITS (b2.json)
    # -------------------------------------------------------------------------
    b2_units_path = LATAM_DIR / "curriculum" / "units" / "b2.json"
    b2_units = json.loads(b2_units_path.read_text(encoding="utf-8"))

    has_core_22 = any(u.get("title") == "Verbs of Becoming & Transformation" for u in b2_units)
    has_reg_22 = any(u.get("title") == "Chile I: The Central Valley, Valparaíso & The Great Poets" for u in b2_units)

    if not has_core_22:
        b2_units.append({
            "title": "Verbs of Becoming & Transformation",
            "stems": [
                f"{c_unit}-01",
                f"{c_unit}-02",
                f"{c_unit}-03",
                f"{c_unit}-04",
                f"{c_unit}-05",
                f"{c_unit}-consolidation"
            ],
            "track": "core"
        })
    if not has_reg_22:
        b2_units.append({
            "title": "Chile I: The Central Valley, Valparaíso & The Great Poets",
            "stems": [
                f"{r_unit}-01",
                f"{r_unit}-02",
                f"{r_unit}-03",
                f"{r_unit}-04",
                f"{r_unit}-05",
                f"{r_unit}-consolidation"
            ],
            "track": "regional"
        })

    b2_units_path.write_text(json.dumps(b2_units, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated curriculum/units/b2.json with Unit 22!")

    # -------------------------------------------------------------------------
    # 7. AUDIT STORY WORD COUNTS (Strict 650 - 825 words)
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_22", story_core_22),
        ("story_chile_01", story_chile_01),
        ("story_chile_02", story_chile_02),
        ("story_chile_03", story_chile_03),
        ("story_chile_04", story_chile_04),
        ("story_chile_05", story_chile_05),
        ("story_chile_capstone", story_chile_capstone)
    ]

    print("\n--- Story Word Count Audit ---")
    all_ok = True
    for name, s in stories_to_audit:
        full_text = " ".join(s["narration"]["paragraphs"])
        wc = count_words(full_text)
        status = "OK (650-825)" if 650 <= wc <= 825 else f"FAILED ({wc} words, must be 650-825)"
        if not (650 <= wc <= 825):
            all_ok = False
        print(f"{name:<24}: {wc:4d} words -> {status}")

    assert all_ok, "Some stories are out of the 650-825 word count bounds!"

if __name__ == "__main__":
    main()
