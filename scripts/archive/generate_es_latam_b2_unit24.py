"""Generate Latin American Spanish (es-latam) B2 Unit 24:
Core Unit 24: b2-24 (Durative & Progressive Periphrases)
Regional Unit 24: b2-argentinaba (Argentina I: Buenos Aires, Tango & Porteño Culture)
Classic Literature: Roberto Arlt - El juguete rabioso: La noche porteña y la invención en los arrabales (1926)
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
            "perifrasis-andar-gerundio": {
                "kind": "grammar",
                "name": "perifrasis-andar-gerundio",
                "description": "Progressive periphrasis andar + gerundio expressing dispersed, restless, or erratic ongoing activity",
                "aliases": []
            },
            "perifrasis-venir-gerundio": {
                "kind": "grammar",
                "name": "perifrasis-venir-gerundio",
                "description": "Cumulative progressive periphrasis venir + gerundio expressing actions accumulating from past to present",
                "aliases": []
            },
            "b2-24-vocab": {
                "kind": "vocabulary",
                "name": "b2-24-vocab",
                "description": "Vocabulary for progressive and durative periphrases, temporal continuity, and persistence",
                "aliases": []
            },
            "locuciones-prepositivas-espaciales": {
                "kind": "grammar",
                "name": "locuciones-prepositivas-espaciales",
                "description": "Spatial and locative prepositional locutions in urban and architectural descriptions",
                "aliases": []
            },
            "voseo-rioplatense-reconocimiento": {
                "kind": "grammar",
                "name": "voseo-rioplatense-reconocimiento",
                "description": "Recognition and comprehension of Rioplatense voseo verb forms and pronominal paradigms",
                "aliases": []
            },
            "participios-absolutos-narrativos": {
                "kind": "grammar",
                "name": "participios-absolutos-narrativos",
                "description": "Absolute participial clauses functioning as temporal and circumstantial background in narrative prose",
                "aliases": []
            },
            "marcadores-reflexion-intelectual": {
                "kind": "grammar",
                "name": "marcadores-reflexion-intelectual",
                "description": "Discourse markers of intellectual reflection, analytical distancing, and conceptual precision",
                "aliases": []
            },
            "estructuras-conjeturales-metafisicas": {
                "kind": "grammar",
                "name": "estructuras-conjeturales-metafisicas",
                "description": "Conjectural and metaphysical comparison structures in fantastic and philosophical literature",
                "aliases": []
            },
            "b2-argentinaba-vocab": {
                "kind": "vocabulary",
                "name": "b2-argentinaba-vocab",
                "description": "Vocabulary for Buenos Aires, tango, immigrant heritage, psychoanalysis, and Argentine fantastic literature",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            if k not in skills:
                skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 24")

    # 2. Update grammar-titles.json (all lowercase words, <= 11 words, plain CEFR English, fits after 'We recommend practicing ')
    def update_grammar_titles(titles):
        new_titles = {
            "perifrasis-andar-gerundio": "the progressive periphrasis andar plus gerund",
            "perifrasis-venir-gerundio": "the cumulative progressive periphrasis venir plus gerund",
            "locuciones-prepositivas-espaciales": "spatial prepositional phrases in urban descriptions",
            "voseo-rioplatense-reconocimiento": "recognizing rioplatense voseo in spoken and literary discourse",
            "participios-absolutos-narrativos": "absolute participial clauses in narrative prose",
            "marcadores-reflexion-intelectual": "discourse markers of reflection and critical analysis",
            "estructuras-conjeturales-metafisicas": "conjectural and metaphysical structures in literary prose"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 24")

    # 3. Vocabulary Files (10 files)
    vocab_data = {
        "b2-24-01": {
            "id": "vocab.b2.24.01",
            "lesson": "b2-24-01",
            "title": "Durative Periphrasis: Llevar + Gerundio",
            "words": [
                {"lemma": "llevar", "translation": "to have been doing (duration)", "pos": "verb"},
                {"lemma": "trayectoria", "translation": "trajectory / track record", "pos": "noun"},
                {"lemma": "andadura", "translation": "walk / journey / course of time", "pos": "noun"},
                {"lemma": "continuidad", "translation": "continuity", "pos": "noun"},
                {"lemma": "ininterrumpido", "translation": "uninterrupted", "pos": "adjective"},
                {"lemma": "acúmulo", "translation": "accumulation", "pos": "noun"},
                {"lemma": "prolongado", "translation": "prolonged / extended", "pos": "adjective"},
                {"lemma": "permanencia", "translation": "stay / permanence", "pos": "noun"},
                {"lemma": "constancia", "translation": "perseverance / steady effort", "pos": "noun"},
                {"lemma": "decurso", "translation": "course / lapse of time", "pos": "noun"}
            ]
        },
        "b2-24-02": {
            "id": "vocab.b2.24.02",
            "lesson": "b2-24-02",
            "title": "Durative Periphrasis: Seguir + Gerundio",
            "words": [
                {"lemma": "seguir", "translation": "to continue / to keep on doing", "pos": "verb"},
                {"lemma": "persistencia", "translation": "persistence", "pos": "noun"},
                {"lemma": "obstinación", "translation": "obstinacy / stubbornness", "pos": "noun"},
                {"lemma": "vigencia", "translation": "validity / current relevance", "pos": "noun"},
                {"lemma": "inalterable", "translation": "unalterable / unchanging", "pos": "adjective"},
                {"lemma": "firmeza", "translation": "firmness / steadfastness", "pos": "noun"},
                {"lemma": "perdurabilidad", "translation": "durability / endurance", "pos": "noun"},
                {"lemma": "latente", "translation": "latent / dormant", "pos": "adjective"},
                {"lemma": "empeño", "translation": "determination / tenacity", "pos": "noun"},
                {"lemma": "constante", "translation": "constant / unwavering", "pos": "adjective"}
            ]
        },
        "b2-24-03": {
            "id": "vocab.b2.24.03",
            "lesson": "b2-24-03",
            "title": "Progressive Periphrasis: Ir + Gerundio",
            "words": [
                {"lemma": "ir", "translation": "to do gradually / step by step", "pos": "verb"},
                {"lemma": "paulatino", "translation": "gradual / step-by-step", "pos": "adjective"},
                {"lemma": "gradual", "translation": "gradual", "pos": "adjective"},
                {"lemma": "despliegue", "translation": "unfolding / rollout", "pos": "noun"},
                {"lemma": "afianzamiento", "translation": "consolidation / strengthening", "pos": "noun"},
                {"lemma": "maduración", "translation": "maturation / ripening", "pos": "noun"},
                {"lemma": "progresión", "translation": "progression", "pos": "noun"},
                {"lemma": "asentamiento", "translation": "settling / establishing", "pos": "noun"},
                {"lemma": "desenlace", "translation": "unraveling / outcome", "pos": "noun"},
                {"lemma": "decantación", "translation": "settling down / distillation", "pos": "noun"}
            ]
        },
        "b2-24-04": {
            "id": "vocab.b2.24.04",
            "lesson": "b2-24-04",
            "title": "Progressive Periphrasis: Andar + Gerundio",
            "words": [
                {"lemma": "andar", "translation": "to go around doing / to be roaming about", "pos": "verb"},
                {"lemma": "errante", "translation": "wandering / roving", "pos": "adjective"},
                {"lemma": "desasosiego", "translation": "restlessness / uneasiness", "pos": "noun"},
                {"lemma": "inquietud", "translation": "restlessness / concern", "pos": "noun"},
                {"lemma": "disperso", "translation": "dispersed / scattered", "pos": "adjective"},
                {"lemma": "merodear", "translation": "to prowl / to loiter about", "pos": "verb"},
                {"lemma": "rondar", "translation": "to hover around / to haunt", "pos": "verb"},
                {"lemma": "rumor", "translation": "rumor / murmur", "pos": "noun"},
                {"lemma": "trajín", "translation": "bustle / coming and going", "pos": "noun"},
                {"lemma": "deriva", "translation": "drift / wandering course", "pos": "noun"}
            ]
        },
        "b2-24-05": {
            "id": "vocab.b2.24.05",
            "lesson": "b2-24-05",
            "title": "Cumulative Periphrasis: Venir + Gerundio",
            "words": [
                {"lemma": "venir", "translation": "to have been developing (historically)", "pos": "verb"},
                {"lemma": "acumulativo", "translation": "cumulative", "pos": "adjective"},
                {"lemma": "gestación", "translation": "gestation / genesis", "pos": "noun"},
                {"lemma": "precedente", "translation": "precedent", "pos": "noun"},
                {"lemma": "secuela", "translation": "consequence / aftermath", "pos": "noun"},
                {"lemma": "sedimentación", "translation": "sedimentation / gradual buildup", "pos": "noun"},
                {"lemma": "reiteración", "translation": "repetition / reiteration", "pos": "noun"},
                {"lemma": "herencia", "translation": "legacy / inheritance", "pos": "noun"},
                {"lemma": "transcurso", "translation": "lapse / course of time", "pos": "noun"},
                {"lemma": "continuo", "translation": "continuum / continuous flow", "pos": "noun"}
            ]
        },
        "b2-argentinaba-01": {
            "id": "vocab.b2.argentinaba.01",
            "lesson": "b2-argentinaba-01",
            "title": "The Río de la Plata & Porteño Urbanism",
            "words": [
                {"lemma": "estuario", "translation": "estuary", "pos": "noun"},
                {"lemma": "trazado", "translation": "layout / urban grid", "pos": "noun"},
                {"lemma": "dársena", "translation": "dock / harbor basin", "pos": "noun"},
                {"lemma": "barranca", "translation": "ravine / riverside slope", "pos": "noun"},
                {"lemma": "bulevar", "translation": "boulevard", "pos": "noun"},
                {"lemma": "arbolado", "translation": "tree-lined / grove", "pos": "adjective"},
                {"lemma": "riachuelo", "translation": "creek / meandering urban river", "pos": "noun"},
                {"lemma": "puerto", "translation": "port / harbor", "pos": "noun"},
                {"lemma": "avenida", "translation": "broad avenue", "pos": "noun"},
                {"lemma": "palacete", "translation": "mansion / small palace", "pos": "noun"}
            ]
        },
        "b2-argentinaba-02": {
            "id": "vocab.b2.argentinaba.02",
            "lesson": "b2-argentinaba-02",
            "title": "The Great Immigrant Wave & Cocoliche",
            "words": [
                {"lemma": "conventillo", "translation": "tenement boarding house", "pos": "noun"},
                {"lemma": "inquilinato", "translation": "tenement housing system", "pos": "noun"},
                {"lemma": "cocoliche", "translation": "Italian-Spanish immigrant hybrid dialect", "pos": "noun"},
                {"lemma": "crisol", "translation": "melting pot / crucible", "pos": "noun"},
                {"lemma": "chapa", "translation": "corrugated sheet metal", "pos": "noun"},
                {"lemma": "colectividad", "translation": "immigrant community / diaspora group", "pos": "noun"},
                {"lemma": "arribo", "translation": "arrival / landing", "pos": "noun"},
                {"lemma": "mestizaje", "translation": "cultural fusion / blending", "pos": "noun"},
                {"lemma": "hacinamiento", "translation": "overcrowding", "pos": "noun"},
                {"lemma": "afincarse", "translation": "to settle down / to establish roots", "pos": "verb"}
            ]
        },
        "b2-argentinaba-03": {
            "id": "vocab.b2.argentinaba.03",
            "lesson": "b2-argentinaba-03",
            "title": "Tango, Arrabales & Lunfardo",
            "words": [
                {"lemma": "arrabal", "translation": "outskirts / suburban underworld quarter", "pos": "noun"},
                {"lemma": "bandoneón", "translation": "bandoneon accordion", "pos": "noun"},
                {"lemma": "lunfardo", "translation": "Buenos Aires slang argot", "pos": "noun"},
                {"lemma": "compadrito", "translation": "dandy tango tough guy / street swaggerer", "pos": "noun"},
                {"lemma": "milonga", "translation": "tango dance hall / musical rhythm", "pos": "noun"},
                {"lemma": "fuelle", "translation": "bellows / bandoneon (slang)", "pos": "noun"},
                {"lemma": "síncopa", "translation": "syncopation", "pos": "noun"},
                {"lemma": "melancolía", "translation": "melancholy", "pos": "noun"},
                {"lemma": "farol", "translation": "street lamp / lantern", "pos": "noun"},
                {"lemma": "cadencia", "translation": "cadence / rhythmic swing", "pos": "noun"}
            ]
        },
        "b2-argentinaba-04": {
            "id": "vocab.b2.argentinaba.04",
            "lesson": "b2-argentinaba-04",
            "title": "Psychoanalysis, Cafés & Bookstores",
            "words": [
                {"lemma": "psicoanálisis", "translation": "psychoanalysis", "pos": "noun"},
                {"lemma": "diván", "translation": "psychoanalytic couch / divan", "pos": "noun"},
                {"lemma": "tertulia", "translation": "literary gathering / café discussion group", "pos": "noun"},
                {"lemma": "introspección", "translation": "introspection", "pos": "noun"},
                {"lemma": "cafetín", "translation": "traditional small Buenos Aires café", "pos": "noun"},
                {"lemma": "intelectualidad", "translation": "intellectual circle", "pos": "noun"},
                {"lemma": "librería", "translation": "bookshop", "pos": "noun"},
                {"lemma": "inconsciente", "translation": "unconscious mind", "pos": "noun"},
                {"lemma": "bohemia", "translation": "bohemian lifestyle / artistic circle", "pos": "noun"},
                {"lemma": "nocturnidad", "translation": "nightlife / nocturnal culture", "pos": "noun"}
            ]
        },
        "b2-argentinaba-05": {
            "id": "vocab.b2.argentinaba.05",
            "lesson": "b2-argentinaba-05",
            "title": "Borges, Cortázar & Fantastic Literature",
            "words": [
                {"lemma": "laberinto", "translation": "labyrinth / maze", "pos": "noun"},
                {"lemma": "metafísica", "translation": "metaphysics", "pos": "noun"},
                {"lemma": "espejo", "translation": "mirror", "pos": "noun"},
                {"lemma": "infinito", "translation": "infinity / endlessness", "pos": "noun"},
                {"lemma": "azar", "translation": "chance / fate", "pos": "noun"},
                {"lemma": "conjetura", "translation": "conjecture / theoretical surmise", "pos": "noun"},
                {"lemma": "bifurcación", "translation": "bifurcation / branching path", "pos": "noun"},
                {"lemma": "cronopio", "translation": "playful nonconformist character (Cortázar)", "pos": "noun"},
                {"lemma": "fantástico", "translation": "fantastic / uncanny", "pos": "adjective"},
                {"lemma": "paradoja", "translation": "paradox", "pos": "noun"}
            ]
        }
    }

    for stem, vdata in vocab_data.items():
        write_json(f"vocabulary/b2/{stem}-voc.json", vdata)

    # 4. Grammar Files (10 files)
    grammar_data = {
        "b2-24-01": {
            "id": "grammar.b2.24.01.llevar-gerundio",
            "title": "Perífrasis durativas: Llevar + gerundio",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis aspectual *llevar + gerundio* cuantifica la duración temporal ininterrumpida de una acción o estado que comenzó en el pasado y continúa vigente en el momento de referencia. Exige obligatoriamente la expresión de un complemento temporal (*dos semanas*, *décadas*, *mucho tiempo*). A diferencia de *hace... que*, *llevar + gerundio* pone el foco sintáctico en la persistencia activa del sujeto durante todo ese intervalo acumulado."
                },
                {
                    "type": "table",
                    "title": "Estructura y contrastes de Llevar + gerundio",
                    "rows": [
                        ["Llevo tres años investigando la arquitectura de los conventillos porteños.", "I have been researching the architecture of Buenos Aires tenements for three years."],
                        ["Los arqueólogos urbanos llevaban meses excavando las márgenes del Riachuelo.", "The urban archaeologists had been excavating the banks of the Riachuelo for months."],
                        ["¿Cuánto tiempo llevás viviendo en el barrio de San Telmo?", "How long have you been living in the San Telmo neighborhood?"],
                        ["Llevamos semanas debatiendo la vigencia del psicoanálisis en la cultura popular.", "We have been debating the relevance of psychoanalysis in popular culture for weeks."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Para la negación de acciones prolongadas, se emplea frecuentemente la estructura alternativa *llevar + sin + infinitivo*: *Lleva tres meses sin ensayar con la orquesta típica* ('He has gone three months without rehearsing with the tango orchestra')."
                }
            ]
        },
        "b2-24-02": {
            "id": "grammar.b2.24.02.seguir-gerundio",
            "title": "Perífrasis de continuidad: Seguir + gerundio",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis *seguir + gerundio* (junto con su variante más formal *continuar + gerundio*) focaliza el mantenimiento de una acción o estado frente a posibles obstáculos, interrupciones o la expectativa contraria de cese. Señala que las circunstancias no han alterado el curso del acontecimiento. Se opone directamente a *dejar de + infinitivo*."
                },
                {
                    "type": "table",
                    "title": "Usos de Seguir + gerundio",
                    "rows": [
                        ["A pesar de las transformaciones modernas, la milonga sigue convocando a jóvenes y veteranos.", "Despite modern transformations, the milonga continues to bring together youths and veterans."],
                        ["Los historiadores siguen debatiendo el origen exacto del término lunfardo.", "Historians keep debating the exact origin of the term lunfardo."],
                        ["Aunque el café cerró temporalmente, sus antiguos clientes siguieron reuniéndose en la esquina.", "Although the café closed temporarily, its former patrons kept meeting on the corner."],
                        ["La obra de Borges sigue cautivando por su deslumbrante precisión metafísica.", "Borges's work continues to captivate through its dazzling metaphysical precision."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En registros cultos, *continuar + gerundio* aporta un tono más solemne y formal que *seguir + gerundio*, especialmente en ensayos historiográficos o discursos académicos."
                }
            ]
        },
        "b2-24-03": {
            "id": "grammar.b2.24.03.perifrasis-ir-gerundio",
            "title": "Perífrasis progresivas: Ir + gerundio",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis *ir + gerundio* expresa una acción que progresa de forma paulatina, acumulativa y gradual, paso a paso, orientada hacia una culminación o desarrollo sucesivo. No denota mera continuidad estática, sino una evolución incremental que avanza fase por fase en el tiempo."
                },
                {
                    "type": "table",
                    "title": "Ejemplos de Ir + gerundio",
                    "rows": [
                        ["Con la llegada de cada barco, la ciudad se fue transformando en una colmena cosmopolita.", "With the arrival of each ship, the city gradually transformed into a cosmopolitan beehive."],
                        ["Los acordes del bandoneón van ganando intensidad a medida que avanza la pieza.", "The bandoneon chords gradually gain intensity as the piece progresses."],
                        ["Vamos comprendiendo la complejidad urbanística de Buenos Aires al recorrer sus bulevares.", "We are gradually understanding Buenos Aires's urban complexity as we traverse its boulevards."],
                        ["Las antiguas disputas teóricas se fueron disolviendo con el paso de las generaciones.", "The old theoretical disputes gradually dissolved with the passing of generations."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Se asocia de manera natural con marcadores de gradualidad como *poco a poco*, *paulatinamente*, *paso a paso* y *a medida que*."
                }
            ]
        },
        "b2-24-04": {
            "id": "grammar.b2.24.04.perifrasis-andar-gerundio",
            "title": "Perífrasis progresivas: Andar + gerundio",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis *andar + gerundio* denota una acción reiterada, dispersa, errática o sin un rumbo fijo, desarrollada en diversos momentos o lugares. Con frecuencia introduce un matiz de inquietud, reproche o informalidad coloquial en el discurso, sugiriendo que el sujeto se halla desasosegado o vagando en su tarea."
                },
                {
                    "type": "table",
                    "title": "Ejemplos de Andar + gerundio",
                    "rows": [
                        ["El cronista anda buscando testimonios orales por los viejos bodegones de Boedo.", "The chronicler is going around looking for oral testimonies in the old taverns of Boedo."],
                        ["Andan diciendo en el barrio que la vieja librería va a transformarse en un centro cultural.", "People around the neighborhood are going around saying that the old bookstore will become a cultural center."],
                        ["Silvio anda ideando inventos mecánicos en su humilde taller de Flores.", "Silvio is going around devising mechanical inventions in his humble Flores workshop."],
                        ["Los inspectores anduvieron revisando las condiciones de habitabilidad en los conventillos.", "The inspectors went around inspecting the living conditions in the tenement houses."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "No confundas *ir + gerundio* (proceso ordenado y paulatino hacia una meta) con *andar + gerundio* (proceso intermitente, desordenado, disperso o errático)."
                }
            ]
        },
        "b2-24-05": {
            "id": "grammar.b2.24.05.perifrasis-venir-gerundio",
            "title": "Perífrasis acumulativas: Venir + gerundio",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis *venir + gerundio* describe una acción que se originó en un punto temporal pretérito y se ha venido desarrollando, acumulando o repitiendo de manera ininterrumpida o recurrente hasta alcanzar el presente de la enunciación. Enfatiza el espesor histórico, la trayectoria previa y el peso acumulativo del proceso."
                },
                {
                    "type": "table",
                    "title": "Ejemplos de Venir + gerundio",
                    "rows": [
                        ["Los sociólogos vienen advirtiendo sobre las profundas huellas identitarias de la inmigración masiva.", "Sociologists have long been warning about the deep identity marks left by mass immigration."],
                        ["Desde principios del siglo XX, el tango viene expresando las nostalgias del desarraigo rioplatense.", "Since the beginning of the 20th century, tango has been expressing the nostalgia of River Plate uprooting."],
                        ["Esta editorial independiente viene publicando joyas del pensamiento filosófico latinoamericano.", "This independent publishing house has been publishing gems of Latin American philosophical thought."],
                        ["Vengo sosteniendo que Buenos Aires es una ciudad que se piensa a sí misma a través de sus cafés.", "I have been maintaining that Buenos Aires is a city that contemplates itself through its cafés."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Frente a *llevar + gerundio* (que enfatiza el cómputo exacto de tiempo), *venir + gerundio* subraya la persistencia histórica y la gestación acumulativa que desemboca en la situación actual."
                }
            ]
        },
        "b2-argentinaba-01": {
            "id": "grammar.b2.argentinaba.01.locuciones-prepositivas-espaciales",
            "title": "Locuciones prepositivas espaciales en la descripción urbana",
            "sections": [
                {
                    "type": "text",
                    "content": "Las descripciones urbanísticas y arquitectónicas formales recurren a locuciones prepositivas espaciales complejas (*a lo largo de*, *a orillas de*, *en torno a*, *frente a*, *al borde de*, *en las inmediaciones de*) para situar con precisión geométrica y visual los elementos del paisaje metropolitano."
                },
                {
                    "type": "table",
                    "title": "Locuciones espaciales representativas",
                    "rows": [
                        ["A lo largo de la Avenida de Mayo se yerguen imponentes fachadas de inspiración parisina y madrileña.", "Along Avenida de Mayo stand imposing facades of Parisian and Madrid inspiration."],
                        ["A orillas del Río de la Plata, la ciudad se expandió ganando tierras al estuario.", "On the shores of the Río de la Plata, the city expanded by reclaiming land from the estuary."],
                        ["En torno a la Plaza de Mayo converge la memoria política y fundacional de la República.", "Around Plaza de Mayo converges the political and foundational memory of the Republic."],
                        ["Frente al muelle de Puerto Madero, los antiguos silos de grano se transformaron en lofts modernos.", "In front of the Puerto Madero dock, the old grain silos were transformed into modern lofts."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Estas locuciones sustituyen con elegancia construcciones más simples como *cerca de* o *al lado de*, dotando al texto de una perspectiva topográfica formal propia del registro B2/C1."
                }
            ]
        },
        "b2-argentinaba-02": {
            "id": "grammar.b2.argentinaba.02.voseo-rioplatense-reconocimiento",
            "title": "Reconocimiento y comprensión del voseo rioplatense",
            "sections": [
                {
                    "type": "text",
                    "content": "En la región rioplatense (Argentina y Uruguay), el pronombre de segunda persona del singular informal es *vos*, acompañado de una conjugación verbal paradigmática monosilábica o aguda con acento en la última sílaba: *vos tenés*, *vos sos*, *vos sabés*, *vos podés*, *vos venís*. En imperativo afirmativo, pierde la 'd' final del antiguo plural: *mirá*, *decime*, *pensá*, *acercate*."
                },
                {
                    "type": "table",
                    "title": "Paradigma verbal del Voseo Rioplatense",
                    "rows": [
                        ["Presente de indicativo: Vos tenés la llave del taller / Vos sabés cómo resolverlo.", "Present indicative: You have the shop key / You know how to solve it."],
                        ["Imperativo afirmativo: Vení para acá / Decime la verdad sin rodeos.", "Affirmative imperative: Come over here / Tell me the truth plainly."],
                        ["Pronombre y preposición: Esto es para vos / Confío plenamente en vos.", "Prepositional pronoun: This is for you / I trust you fully."],
                        ["Subjuntivo (alternancia): Espero que tengas / tengás paciencia con el trámite.", "Subjunctive (alternation): I hope you have patience with the procedure."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El voseo es la norma de prestigio oral en toda la sociedad argentina. Para el estudiante de nivel B2, el objetivo primordial es reconocerlo fluidamente tanto en la literatura porteña como en el cine y la interacción cotidiana."
                }
            ]
        },
        "b2-argentinaba-03": {
            "id": "grammar.b2.argentinaba.03.participios-absolutos-narrativos",
            "title": "Construcciones de participio absoluto en el relato literario",
            "sections": [
                {
                    "type": "text",
                    "content": "Las cláusulas de participio absoluto constituyen una herramienta estilística avanzada en la prosa narrativa. El participio concuerda en género y número con un sustantivo propio y encabeza la cláusula subordinada circunstancial, funcionando como trasfondo temporal, causal o concesivo sin necesidad de nexos explícitos."
                },
                {
                    "type": "table",
                    "title": "Ejemplos de Participios Absolutos",
                    "rows": [
                        ["Concluida la milonga, las parejas se dispersaron en la bruma de la madrugada.", "Once the milonga concluded, the couples dispersed into the early morning mist."],
                        ["Afinado el fuelle del bandoneón, el maestro arrancó con los primeros compases del tango.", "With the bellows of the bandoneon tuned, the maestro launched into the first bars of the tango."],
                        ["Despejadas las dudas sobre la autoría, el manuscrito fue catalogado en la biblioteca nacional.", "Once doubts regarding authorship were cleared, the manuscript was cataloged in the national library."],
                        ["Llegados los inmigrantes al puerto, iniciaba el riguroso examen sanitario.", "Having the immigrants arrived at the port, the rigorous health inspection would begin."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Observa el orden sintáctico habitual: el participio precede al sustantivo con el que concuerda (*Agotadas las entradas, se suspendió la función*)."
                }
            ]
        },
        "b2-argentinaba-04": {
            "id": "grammar.b2.argentinaba.04.marcadores-reflexion-intelectual",
            "title": "Marcadores de reflexión y análisis crítico en el ensayo",
            "sections": [
                {
                    "type": "text",
                    "content": "En la tradición ensayística y psicoanalítica porteña, la argumentación descansa en marcadores discursivos que introducen consideraciones críticas, matizaciones y valoraciones analíticas: *cabe señalar que*, *es menester destacar*, *en lo que atañe a*, *resulta evidente que*, *convendría matizar que*."
                },
                {
                    "type": "table",
                    "title": "Marcadores analíticos en contexto",
                    "rows": [
                        ["Cabe señalar que la fascinación por el psicoanálisis en Buenos Aires arraiga en una profunda pulsión reflexiva.", "It is worth noting that the fascination with psychoanalysis in Buenos Aires is rooted in a deep reflective drive."],
                        ["En lo que atañe a la cultura del cafetín, este funcionó históricamente como ágora cívica y salón de debates.", "As far as café culture is concerned, it historically functioned as a civic agora and debate salon."],
                        ["Resulta evidente que la tertulia literaria moldó la fisonomía intelectual de la calle Corrientes.", "It is evident that the literary salon shaped the intellectual character of Corrientes Street."],
                        ["Convendría matizar que no toda introspección porteña responde a la melancolía del tango.", "It would be worth qualifying that not all porteño introspection responds to tango melancholy."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Estas fórmulas permiten presentar juicios críticos con rigor académico y distanciamiento analítico, evitando afirmaciones tajantes o excesivamente subjetivas."
                }
            ]
        },
        "b2-argentinaba-05": {
            "id": "grammar.b2.argentinaba.05.estructuras-conjeturales-metafisicas",
            "title": "Estructuras conjeturales y metafísicas en la literatura fantástica",
            "sections": [
                {
                    "type": "text",
                    "content": "La literatura fantástica rioplatense (Borges, Cortázar, Bioy Casares) emplea complejas estructuras conjeturales para difuminar los límites entre realidad, sueño, memoria y laberinto. Destacan construcciones comparativo-hipotéticas con *como si + imperfecto/pluscuamperfecto de subjuntivo*, locuciones de probabilidad conjetural (*cabría inferir que*, *pareciera ser que*) y oraciones modales de apariencia."
                },
                {
                    "type": "table",
                    "title": "Estructuras conjeturales en la ficción metafísica",
                    "rows": [
                        ["El protagonista contemplaba el sótano como si en ese punto microscópico convergiera el universo entero.", "The protagonist contemplated the cellar as if the entire universe converged in that microscopic point."],
                        ["Cabría inferir que el laberinto no era de piedra sino de líneas trazadas por el destino.", "One might infer that the labyrinth was not made of stone but of lines drawn by fate."],
                        ["Pareciera ser que los espejos duplican no solo los rostros, sino también las angustias del infinito.", "It would seem that mirrors duplicate not only faces, but also the anxieties of infinity."],
                        ["Avanzaba por la biblioteca como si cada libro ya hubiera sido leído en una vida pretérita.", "He advanced through the library as if every book had already been read in a past life."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda que tras *como si* la norma culta exige siempre subjuntivo: imperfecto para simultaneidad o posterioridad (*como si supiera*), y pluscuamperfecto para anterioridad (*como si hubiera existido*)."
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}-a-gr.json", gdata)

    # 5. Stories (8 files) - EXACT ROOT-LEVEL PARAGRAPHS SCHEMA & STRICT 650-825 WORDS!

    story_core_24 = {
        "id": "b2-24",
        "title": "El juguete rabioso: La noche porteña y la invención en los arrabales",
        "level": "B2",
        "lesson": 24,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Una adaptación literaria de 'El juguete rabioso' (1926), la clásica novela de Roberto Arlt: los anhelos juveniles de Silvio Astier en el barrio de Flores, la tensión entre la vocación de inventor y la miseria urbana, el deambular nocturno por los cafetines y librerías de lance, y el desgarrador dilema ético que culmina en la traición al Rengo como una oscura afirmación de su propia fatalidad.",
        "characters": [
            "Silvio Astier",
            "Madre de Silvio",
            "El Rengo",
            "Comerciante de Belgrano"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "La ciudad de Buenos Aires crecía hacia los cuatro rumbos como una colmena desbordada por el vapor de las locomotoras, el rumor incesante de las imprentas y el trajín de miles de recién llegados que buscaban su destino entre callejones de barro y avenidas recién trazadas. En aquel arrabal brumoso de Flores, Silvio Astier llevaba meses alimentando un sueño desmesurado que lo apartaba de las mezquindades de la vida cotidiana: ansiaba convertirse en un inventor insigne, en un demiurgo capaz de doblegar las leyes de la física mediante la audacia del ingenio. En su pequeño cuarto atestado de engranajes oxidados, libros de química deshojados y frascos de reactivos comprados con monedas escasas, la penumbra apenas retrocedía ante la débil llama de un mechero de gas."
            },
            {
                "type": "narration",
                "text": "Su madre, mujer de ademanes fatigosos y ojos oscurecidos por las privaciones del conventillo, lo contemplaba desde el umbral con una mezcla de piedad y reproche. Le recordaba que los años de juventud pasaban de prisa y que el pan no se ganaba descifrando esquemas fantásticos en la soledad de la noche. Sin embargo, Silvio seguía sosteniendo que la verdadera grandeza residía en trascender la mediocridad impuesta por la miseria urbana. En los momentos de mayor agobio, cuando la falta de recursos paralizaba sus experimentos, su espíritu no se resignaba; por el contrario, su mente se fue acostumbrando a concebir artefactos mecánicos extraordinarios: un cañón de señales para barcos en peligro, una ganzúa electromagnética y una máquina para escribir señales en las nubes."
            },
            {
                "type": "narration",
                "text": "Durante las tardes lluviosas, cuando el fango del arrabal hacía impracticable cualquier paseo largo, Silvio andaba recorriendo las librerías de lance de la calle Corrientes y los mostradores de los prestamistas en busca de manuales de mecánica aplicada. El joven observaba a la multitud abigarrada de dependientes, inmigrantes italianos, poetas bohemios y estafadores de poca monta que pululaban bajo los toldos mojados. Sentía que una fuerza subterránea y violenta latía en el pavimento húmedo de la metrópolis. Los intelectuales consagrados venían proclamando desde los periódicos elegantes el advenimiento de una edad dorada para la República, pero Silvio contemplaba la otra cara de la moneda: la dureza de las pensiones clandestinas, el desamparo de los adolescentes sin oficio y la humillación diaria del empleo servil."
            },
            {
                "type": "narration",
                "text": "Una noche de invierno, desesperado por conseguir capital para patentar un invento que juzgaba revolucionario, Silvio se reunió con el Rengo, un compadrito taciturno y cojo que frecuentaba las tabernas de los muelles. El hombre lo escuchó mientras bebían aguardiente en un bodegón donde el humo del tabaco se mezclaba con el aliento áspero de los estibadores. El Rengo le propuso un golpe audaz: saquear la caja fuerte de un comerciante adinerado que guardaba sus ganancias en una casa desguarnecida de Belgrano. Durante varias jornadas, Silvio anduvo sopesando el dilema moral con angustia punzante. Sabía que cruzar esa frontera implicaba renunciar a sus ideales de redención por la ciencia y sumergirse definitivamente en el fango de la delincuencia arrabalera."
            },
            {
                "type": "narration",
                "text": "La noche señalada para el asalto, la ciudad parecía una trampa geométrica tendida bajo un cielo encapotado. El viento frío del Río de la Plata soplaba sobre los techos de zinc, levantando torbellinos de ceniza y hojas secas. Al aproximarse a la mansión silenciosa, Silvio comprendió que la fatalidad no se resolvía mediante el delito vulgar, sino a través de un acto más desgarrador y desconcertante. De manera imprevista, resolvió delatar al Rengo ante el dueño de la casa y las autoridades policiales. Aquella traición no nacía de la virtud cívica ni del miedo al presidio, sino de un impulso sombrío y luciferino: el deseo de comprobar hasta qué abismo de soledad y desprecio podía descender su propia alma en una urbe despiadada que devoraba las ilusiones de sus hijos."
            },
            {
                "type": "narration",
                "text": "Al amanecer, mientras el Rengo era conducido engrillado por los agentes policiales bajo una llovizna helada, Silvio caminó sin rumbo hacia las dársenas del puerto, sintiendo en el pecho una extraña y amarga serenidad. En *El juguete rabioso*, Roberto Arlt supo plasmar la desesperación existencial de una generación atrapada entre los deslumbrantes espejismos de la modernización tecnológica y la crudeza de la exclusión social. La figura de Silvio Astier perdura en la literatura hispanoamericana como el testimonio implacable de un alma herida que, en medio de la niebla porteña, prefirió consumirse en su propio fuego antes que capitular ante la monotonía servil del mundo de los hombres sensatos."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál era el anhelo fundamental que Silvio Astier perseguía en su modesto cuarto de Flores?",
                        "options": [
                            "Convertirse en un inventor ilustre capaz de superar la mediocridad cotidiana mediante el ingenio científico.",
                            "Acumular suficiente capital para comprar tierras ganaderas en la provincia de Buenos Aires.",
                            "Heredar el negocio textil de su familia en Génova y regresar a Europa en el primer vapor transatlántico.",
                            "Aprender a tocar el bandoneón para ingresar en una orquesta típica de tango en los cabarets céntricos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Silvio sueña obsesivamente con consagrarse como inventor e ingeniero creador de artefactos extraordinarios."
                    },
                    {
                        "question": "¿Qué contradicción observaba Silvio entre los discursos oficiales y la realidad cotidiana de la urbe?",
                        "options": [
                            "Los periódicos pregonaban una edad dorada mientras él constataba la dureza de las pensiones y la miseria urbana.",
                            "El gobierno obligaba a todos los jóvenes a emigrar al campo a pesar del auge de las fábricas porteñas.",
                            "Las autoridades prohibían la venta de libros científicos y clausuraban los institutos técnicos de enseñanza.",
                            "La policía impedía que los barcos descargaran mercancías en las dársenas de Puerto Madero."
                        ],
                        "correctIndex": 0,
                        "explanation": "Silvio percibe el abismo entre la retórica optimista de la élite y la miseria descarnada de los arrabales."
                    },
                    {
                        "question": "¿Por qué motivo crucial resolvió Silvio delatar al Rengo antes de cometer el asalto planificado?",
                        "options": [
                            "Por un impulso sombrío de comprobar hasta qué abismo de soledad y desprecio podía descender su propia alma.",
                            "Porque el comerciante asaltado le ofreció una generosa recompensa monetaria para abrir su propio taller mecánico.",
                            "Debido a que su madre le rogó entre lágrimas que no manchara el honor honrado de la familia obrera.",
                            "Para evitar que la policía descubriera que él no tenía documentos de identidad argentinos válidos."
                        ],
                        "correctIndex": 0,
                        "explanation": "La traición de Silvio es un acto existencial gratuito y autodestructivo, característico del universo de Arlt."
                    }
                ]
            }
        }
    }

    story_chile_01 = {
        "id": "b2-argentinaba-01",
        "title": "El Río de la Plata y el trazado de la reina del Plata",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la evolución urbanística y geográfica de Buenos Aires: la relación histórica y esquiva con el inmenso estuario del Río de la Plata, el trazado monumental de la Avenida de Mayo y la Avenida 9 de Julio, los contrastes entre las márgenes del Riachuelo y los parques de Carlos Thays, y la reconversión vanguardista de las dársenas de Puerto Madero.",
        "characters": [
            "Urbanista e historiador porteño Hernán",
            "Arquitecta restauradora Camila",
            "Capitán de remolcador fluvial Don Vicente",
            "Paseante e investigadora Lucía"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "El Río de la Plata se despliega ante la mirada del viajero no como un cauce fluvial tradicional, sino como una inmensa llanura líquida de tonos leonados y horizontes abiertos que se confunde con el mar infinito. Desde la segunda fundación de la ciudad por Juan de Garay en 1580 sobre una modesta barranca ribereña, Buenos Aires mantuvo una relación compleja, esquiva y fascinante con este estuario colosal. Durante siglos coloniales, la urbe permaneció de espaldas a sus aguas barrosas debido a la escasa profundidad de las costas, que forzaba a los navíos transatlánticos a fondear a leguas de distancia mientras carretas de ruedas descomunales transportaban pasajeros y mercancías a través del lodazal."
            },
            {
                "type": "narration",
                "text": "Con la llegada del auge agroexportador a finales del siglo XIX, la élite gobernante decidió transformar radicalmente aquel fondeadero precario en una metrópolis deslumbrante que emulara el refinamiento urbanístico de París y Londres. Ingenieros y planificadores trazaron avenidas grandiosas cortando la cuadrícula hispánica tradicional: la emblemática Avenida de Mayo unió la histórica Plaza de Mayo con el majestuoso Congreso Nacional, flanqueada por cúpulas art nouveau, palacetes academicistas y farolas de hierro forjado. Paralelamente, la Avenida 9 de Julio se proyectó como la arteria más ancha del mundo, derribando manzanas enteras para dotar a la capital de una escala monumental que reflejara el optimismo de una nación en plena bonanza cerealera y ganadera."
            },
            {
                "type": "narration",
                "text": "A lo largo de la costa sur, el meandro fangoso del Riachuelo definió el perfil proletario e industrial de la ciudad. En sus márgenes creció el barrio de La Boca, donde los barcos mercantes descargaban carbón, madera y contingentes incesantes de familias italianas en medio de talleres navales y saladeros. En contraste, hacia el norte ribereño, los parques diseñados por el paisajista francés Carlos Thays modelaron Palermo y Recoleta mediante bosques de tipas centenarias, jacarandás en flor y lagos artificiales que ofrecían sombra y esparcimiento aristocrático. La topografía suave de las barrancas fue aprovechada con maestría para levantar residencias palaciegas que contemplaban la desembocadura fluvial con el señorío indiscutible de la belle époque sudamericana."
            },
            {
                "type": "narration",
                "text": "El gran dilema portuario culminó con la construcción de Puerto Madero, un ambicioso sistema de cuatro dársenas rectangulares cerradas por esclusas que proyectó el comerciante Eduardo Madero con financiamiento británico. No obstante, el vertiginoso crecimiento del tonelaje de los buques modernos convirtió las dársenas en estructuras obsoletas al cabo de pocas décadas, forzando la apertura de Puerto Nuevo más al norte. Abandonados durante casi todo el siglo XX, aquellos docks de ladrillo rojo inglés y silos graneleros renacieron en la década de 1990 gracias a una de las intervenciones de reconversión urbana más exitosas del continente, transformándose en un distrito exclusivo de rascacielos acristalados, gastronomía refinada y paseos peatonales ribereños."
            },
            {
                "type": "narration",
                "text": "Hoy en día, la Reina del Plata dialoga de manera renovada con su estuario ancestral a través de la Costanera Norte y las reservas ecológicas ganadas al río mediante el relleno planificado de escombros urbanos. En ese humedal silvestre que creció espontáneamente junto a los rascacielos, conviven garzas moras, sauces criollos y cisnes de cuello negro a escasos metros del bullicio automovilístico. La urbe exhibe con orgullo su condición de palimpsesto arquitectónico: la traza colonial de San Telmo convive armoniosamente con los bulevares neoclásicos, las torres de vanguardia y los viejos muelles portuarios. Caminar por sus riberas permite constatar que Buenos Aires no es simplemente una capital sudamericana, sino una civilización cosmopolita nacida del barro pampeano y abierta para siempre a los vientos oceánicos del mundo entero."
            },
            {
                "type": "narration",
                "text": "Esa impronta de grandiosidad y nostalgia fluvial imprime a la metrópolis su pulso inconfundible y su magnetismo inagotable. En cada atardecer ribereño, cuando la brisa fresca del sudeste refresca el asfalto caliente y las aguas cobrizas reflejan los destellos de las farolas centenarias, el habitante de Buenos Aires experimenta la certeza íntima de pertenecer a una urbe única, nacida de la audacia humana en los confines del océano y forjada con la tenacidad inquebrantable de quienes la soñaron eterna, libre y generosa frente al horizonte infinito del gran río color de león."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué motivo la Buenos Aires colonial vivió durante siglos de espaldas al Río de la Plata?",
                        "options": [
                            "Por la escasa profundidad de las costas fangosas que impedía el atraque directo de navíos de gran calado.",
                            "Debido a decretos virreinales que prohibían estrictamente contemplar las aguas por razones religiosas.",
                            "Porque el agua del estuario contenía minerales venenosos que corroían el casco de madera de las naves.",
                            "Por la existencia ininterrumpida de piratas holandeses que bombardeaban la costa desde el mar abierto."
                        ],
                        "correctIndex": 0,
                        "explanation": "El fondo playo y lodoso forzaba a los barcos a fondear lejos y usar carretas para transbordar cargas."
                    },
                    {
                        "question": "¿Qué intervenciones urbanísticas definieron la monumentalidad de la ciudad a finales del siglo XIX?",
                        "options": [
                            "La apertura de la Avenida de Mayo, el diseño de la Avenida 9 de Julio y los parques arbolados de Carlos Thays.",
                            "La demolición completa de todas las iglesias coloniales para construir fábricas de pólvora y aceros.",
                            "La construcción de una muralla defensiva de piedra granítica que rodeaba la cuadrícula fundacional.",
                            "El traslado forzoso de la sede de gobierno a una isla artificial en medio del Río de la Plata."
                        ],
                        "correctIndex": 0,
                        "explanation": "La apertura de grandes avenidas y bulevares parisinos reflejó el esplendor de la época agroexportadora."
                    },
                    {
                        "question": "¿De qué manera renació el área portuaria de Puerto Madero tras décadas de abandono industrial?",
                        "options": [
                            "Mediante un ambicioso proyecto de reconversión que recicló los docks de ladrillo en un distrito gastronómico y cultural.",
                            "Fue inundada deliberadamente para crear un parque temático dedicado a la pesca deportiva.",
                            "Se transformó en un arsenal militar exclusivo para el atraque de submarinos nucleares internacionales.",
                            "Fue demolida en su totalidad para instalar huertos comunitarios de producción hortícola intensiva."
                        ],
                        "correctIndex": 0,
                        "explanation": "Puerto Madero fue refuncionalizado en los años noventa como un moderno polo de viviendas, oficinas y gastronomía."
                    }
                ]
            }
        }
    }

    story_chile_02 = {
        "id": "b2-argentinaba-02",
        "title": "La gran ola inmigratoria: Italianos, españoles y el cocoliche",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una investigación histórica sobre la inmensa corriente inmigratoria que transformó la Argentina entre 1880 y 1920: el desembarco en el Hotel de Inmigrantes, la vida cotidiana y el hacinamiento en los conventillos de La Boca, el nacimiento del cocoliche y las mutuales obreras de socorro mutuo que forjaron la identidad popular rioplatense.",
        "characters": [
            "Inmigrante genovés Giuseppe",
            "Lavandera y líder comunitaria María",
            "Médico del Hotel de Inmigrantes Dr. Álvarez",
            "Joven cronista barrial Lisandro"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Entre 1880 y las primeras décadas del siglo XX, la República Argentina experimentó uno de los fenómenos de transformación demográfica más intensos y masivos de la historia moderna universal. Amparados por el precepto constitucional de albergar a todos los hombres de buena voluntad que quisieran habitar el suelo patrio, más de cuatro millones de extranjeros desembarcaron en las dársenas porteñas procedentes de aldeas italianas del Piamonte, Liguria, Calabria y Sicilia, junto a campesinos gallegos, andaluces, vascos, asquenazíes y sirio-libaneses. Para la inmensa mayoría, la primera morada en tierra americana fue el monumental Hotel de Inmigrantes, complejo estatal erigido junto al puerto donde recibían alojamiento gratuito, exámenes médicos y orientación laboral inicial."
            },
            {
                "type": "narration",
                "text": "La falta de viviendas individuales y los elevados costos del suelo urbano empujaron a las familias obreras hacia los conventillos: viejas casonas señoriales abandonadas por las familias patricias tras la epidemia de fiebre amarilla de 1871, o precarias edificaciones construidas con maderas de desecho y chapas de zinc acanaladas en el barrio de La Boca. En aquellas viviendas colectivas, decenas de núcleos familiares compartían un único patio central de baldosas gastadas, piletas comunes para el lavado de ropa y un solo retrete para cincuenta habitantes. Cada pequeña pieza alquilada albergaba a padres, hijos y parientes en condiciones de severo hacinamiento, pero también propiciaba una convivencia comunitaria fecunda e irrepetible donde se mezclaban olores de polenta, puchero y panes recién horneados al calor de fogones compartidos."
            },
            {
                "type": "narration",
                "text": "En ese crisol de patios ruidosos surgió una singular hibridación lingüística bautizada como cocoliche: una jerga de transición que mezclaba dialectos peninsulares italianos (genovés, napolitano, véneto, calabrés) con el castellano criollo rioplatense. Los inmigrantes de primera generación, deseosos de integrarse laboralmente pero aferrados a sus giros nativos, deformaban la fonética española introduciendo vocablos itálicos como *laburar* (trabajar), *mufa* (mala suerte), *mina* (mujer), *pibe* (muchacho), *morfar* (comer) o *festichola* (fiesta). Aunque las clases acomodadas y los sainetes teatrales satirizaron al cocoliche como una aberración cómica del lenguaje, este fenómeno sentó las bases emocionales y léxicas que más tarde nutrirían con fuerza inusitada al lunfardo porteño."
            },
            {
                "type": "narration",
                "text": "Lejos de replegarse en la pasividad o la resignación silenciosa, la masa inmigrante desplegó un extraordinario tejido de solidaridad colectiva para resistir la precariedad de los primeros años. Fundaron mutuales de socorro mutuo que garantizaban atención médica y sepelio digno, hospitales comunitarios de vanguardia como el Hospital Italiano y el Hospital Español, círculos obreros de orientación socialista o anarquista y sociedades recreativas donde se entonaban canzonettas napolitanas al compás de acordeones y guitarras. Las célebres huelgas de inquilinos de 1907, lideradas con coraje por mujeres armadas con escobas en los conventillos de Balvanera y La Boca para frenar los abusos en los alquileres, evidenciaron que aquellos trabajadores no se concebían como huéspedes transitorios, sino como ciudadanos conscientes de sus derechos laborales y de su dignidad social."
            },
            {
                "type": "narration",
                "text": "Hacia 1914, más de la mitad de los habitantes de Buenos Aires había nacido en el extranjero, sellando para siempre la fisonomía cultural, gastronómica y gestual de la argentinidad. La pasión por la pasta dominical amasada en familia, la costumbre compartida del asado al aire libre, la gesticulación expresiva de las manos al hablar y una melancólica nostalgia por la patria lejana se integraron indisolublemente en el ser porteño. Aquella ola inmigratoria colosal no solo pobló una nación en plena expansión territorial, sino que inventó una identidad híbrida, abierta y plural que continúa siendo el rasgo distintivo de la sociedad rioplatense contemporánea."
            },
            {
                "type": "narration",
                "text": "Al cruzar hoy las calles empedradas de San Telmo o contemplar las fachadas policromadas de Caminito en La Boca, el eco de aquellas lenguas mezcladas parece flotar aún entre los balcones floridos y los patios soleados. La memoria de aquellos millones de abuelos que cruzaron el Atlántico con una maleta de cartón y el corazón colmado de esperanzas sigue latiendo con fuerza inextinguible en cada mesa familiar, donde una fuente humeante de tallarines renueva el pacto secular entre las raíces del viejo continente y la infinita generosidad de la tierra americana."
            },
            {
                "type": "narration",
                "text": "Comprender la Buenos Aires moderna resulta inconcebible sin reconocer la gesta silenciosa de aquellos hombres y mujeres que levantaron una metrópolis desde el barro de las dársenas. En sus sacrificios anónimos, en sus huelgas por un jornal justo y en su capacidad para fundar hogares en medio de la adversidad, germinó la energía democrática y la inagotable vocación de futuro que distingue para siempre al espíritu rioplatense."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué papel desempeñó el Hotel de Inmigrantes en la recepción de los recién llegados a Buenos Aires?",
                        "options": [
                            "Brindaba alojamiento gratuito temporal, revisión sanitaria y mediación para conseguir los primeros empleos.",
                            "Funcionaba como cárcel militar donde se retenía indefinidamente a los sospechosos de filiación anarquista.",
                            "Era un exclusivo hotel de lujo reservado para diplomáticos y banqueros europeos de alto rango.",
                            "Constituía una escuela de idiomas obligatoria donde se prohibía hablar dialectos extranjeros durante tres años."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Hotel de Inmigrantes ofrecía albergue, comidas y colocación laboral a los recién desembarcados."
                    },
                    {
                        "question": "¿Cuáles eran las características habitacionales y sociales de los conventillos tradicionales?",
                        "options": [
                            "Viviendas colectivas con severo hacinamiento donde numerosas familias compartían patio central y servicios básicos.",
                            "Modernos bloques de apartamentos individuales con calefacción central y jardines privados para cada obrero.",
                            "Cabañas aisladas construidas en las islas vírgenes del delta del Paraná para prevenir epidemias.",
                            "Mansiones suburbanas de estilo normando destinadas exclusivamente a familias de origen anglosajón."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los conventillos albergaban a decenas de familias humildes en habitaciones diminutas en torno a un patio común."
                    },
                    {
                        "question": "¿Cómo surgió el cocoliche y qué influencia posterior tuvo en el habla popular rioplatense?",
                        "options": [
                            "Surgió como dialecto híbrido italo-criollo en los conventillos y aportó numerosos giros y préstamos al lunfardo.",
                            "Fue inventado artificialmente por una comisión de filólogos para erradicar las lenguas indígenas del norte.",
                            "Nació como un código secreto de marineros alemanes para contrabandear telas finas en el puerto de La Boca.",
                            "Era la lengua litúrgica exclusiva utilizada en los sermones de la catedral metropolitana de Buenos Aires."
                        ],
                        "correctIndex": 0,
                        "explanation": "El cocoliche nació espontáneamente de la mezcla del italiano con el español y nutrió al habla porteña."
                    }
                ]
            }
        }
    }

    story_chile_03 = {
        "id": "b2-argentinaba-03",
        "title": "El tango: De los arrabales marginales a los salones del mundo",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la historia social del tango: su nacimiento en los prostíbulos y arrabales del puerto, la incorporación trascendental del bandoneón, el impacto de Carlos Gardel y las letras filosóficas del lunfardo, y la revolución vanguardista de Astor Piazzolla hasta su consagración como patrimonio inmaterial de la humanidad.",
        "characters": [
            "Bandoneonista veterano Don Osvaldo",
            "Cantora de milonga Milena",
            "Letrista y poeta de cafetín Julián",
            "Joven bailarina de conservatorio Florencia"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En las últimas décadas del siglo XIX, en los suburbios polvorientos donde la pampa abierta comenzaba a rozar los arrabales marginales de Buenos Aires y Montevideo, nació una criatura musical híbrida, provocadora y desgarrada: el tango. En los prostíbulos de orillas del Riachuelo, en las fondas donde se cruzaban gauchos desarraigados, marineros extranjeros, criollos orilleros y afrodescendientes que conservaban el pulso rítmico del candombe, surgió esta danza de abrazos estrechos y pasos quebrados. Inicialmente interpretado con flauta, violín y guitarra, el tango era considerado por la oligarquía porteña como una danza obscena, pecaminosa y reservada con exclusividad a los sectores más bajos del hampa urbana."
            },
            {
                "type": "narration",
                "text": "La incorporación decisiva del bandoneón —un instrumento de fuelle de origen alemán concebido originalmente para interpretar corales religiosos en parroquias rurales sin órgano— transformó de raíz la sustancia tímbrica y espiritual del género. Con sus quejidos metálicos, sus silencios dramáticos y sus notas arrastradas con dolorosa lentitud, el fuelle dotó al tango de una melancolía metafísica inigualable. Aquel ritmo alegre y prostibulario de los orígenes derivó hacia una contemplación trágica sobre el paso implacable del tiempo, el desengaño amoroso, la traición de los amigos y la nostalgia irremediable por el barrio de la infancia que la piqueta del progreso comenzaba a demoler sin compasión."
            },
            {
                "type": "narration",
                "text": "El punto de inflexión definitivo ocurrió con la aparición estelar de Carlos Gardel, 'El Zorzal Criollo', quien en 1917 grabó *Mi noche triste* de Pascual Contursi, inaugurando la era dorada del tango-canción. Con su voz de barítono brillante, su sonrisa magnética y una elegancia insuperable en escena, Gardel llevó el tango desde los cafetines humildes de la calle Corrientes hasta los salones dorados de París, Madrid y Nueva York. La consagración europea operó un milagro sociológico instantáneo: la alta burguesía argentina, que antes lo despreciaba por considerarlo una indecencia de compadritos y malandras, se apresuró a adoptarlo con fervor como el máximo símbolo del orgullo y la distinción nacional en el mundo entero."
            },
            {
                "type": "narration",
                "text": "Acompañando a las composiciones musicales floreció el lunfardo, argot callejero nutrido de giros carcelarios, préstamos del dialecto genovés y deformaciones silábicas como el vesre: *gotán* por tango, *feca* por café. Letristas magistrales de la talla de Enrique Santos Discépolo, Homero Manzi y Cátulo Castillo elevaron la poesía tanguera a la categoría de alta literatura filosófica popular. Tangos memorables como *Cambalache*, *Sur* o *Yira, yira* articularon una radiografía implacable sobre las paradojas morales del siglo XX, denunciando la hipocresía social y dibujando la geografía sentimental de esquinas con farol y noches de cafetín donde se ahogaban las penas con grapa barata."
            },
            {
                "type": "narration",
                "text": "Décadas más tarde, Astor Piazzolla revolucionó los cimientos del género al fusionar la tradición tanguera con la música clásica contemporánea de Igor Stravinski y las síncopas vanguardistas del jazz moderno. Pese a la encarnizada resistencia de los puristas conservadores que negaban con vehemencia que sus suites instrumentales fueran auténtico tango, Piazzolla proyectó la música porteña hacia una dimensión cosmopolita insospechada en los grandes teatros de concierto de Europa y Japón. Declarado Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO en 2009, el tango continúa palpitando hoy en las milongas nocturnas de San Telmo y Almagro como un lenguaje universal del cuerpo, donde dos extraños se abrazan para resistir la soledad del mundo contemporáneo."
            },
            {
                "type": "narration",
                "text": "Cuando en el silencio de una pista oscurecida se escuchan las primeras notas quejumbrosas del fuelle y los bailarines inician su marcha cadenciosa, el tiempo parece suspenderse en un instante mágico de comunión estética. En ese diálogo silencioso de miradas cómplices y pasos compaseados, el tango demuestra que la belleza más sublime no nace de la dicha complaciente, sino del dolor transfigurado por el arte en una melodía inmortal que consuela las heridas secretas y universales de la condición humana."
            },
            {
                "type": "narration",
                "text": "Por todo ello, el tango no es simplemente un género de baile o una partitura musical nostálgica, sino una concepción filosófica de la existencia. En cada tango se resume la aventura del náufrago urbano que, despojado de certidumbres en la gran metrópolis, encuentra en el abrazo protector de la milonga y en los acordes solemnes del bandoneón la fuerza trascendente para seguir caminando con dignidad en medio de la noche."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿En qué espacios marginales nació originariamente el tango y qué instrumentos lo interpretaban?",
                        "options": [
                            "En prostíbulos y arrabales orilleros del Riachuelo, interpretado con flauta, violín y guitarra.",
                            "En los salones aristocráticos de la ópera de Recoleta, interpretado con grandes arpas y cornos franceses.",
                            "En las capillas jesuíticas del interior cordobés, cantado exclusivamente a capela por coros litúrgicos.",
                            "En los campamentos mineros de los Andes, interpretado con bombos legüeros y quenas de caña hueca."
                        ],
                        "correctIndex": 0,
                        "explanation": "El tango brotó en el bajo fondo y prostíbulos suburbanos antes de adoptar el bandoneón."
                    },
                    {
                        "question": "¿Qué transformación sonora y emocional provocó la introducción del bandoneón en el tango?",
                        "options": [
                            "Dotó al género de una densidad tímbrica lúgubre y una melancolía metafísica profunda.",
                            "Convirtió al tango en una marcha militar apresurada para desfiles castrenses patrióticos.",
                            "Hizo que la música sonara idéntica a los valses vieneses de Johann Strauss en las cortes palaciegas.",
                            "Eliminó por completo la necesidad de melodía al limitarse a emitir ruidos de percusión metálica."
                        ],
                        "correctIndex": 0,
                        "explanation": "El bandoneón ralentizó el compás y cargó al tango de una melancolía desgarrada y nostálgica."
                    },
                    {
                        "question": "¿Por qué la consagración internacional de Carlos Gardel alteró la percepción de las élites argentinas sobre el género?",
                        "options": [
                            "Porque el éxito arrollador de Gardel en París legitimó socialmente al tango como emblema de prestigio nacional.",
                            "Porque Gardel prohibió a los obreros y compadritos volver a bailar en las milongas populares.",
                            "Debido a que el cantante se convirtió en ministro de finanzas y expropió todas las salas de baile.",
                            "Porque Gardel tradujo todas las canciones al francés obligando a cantar únicamente en ese idioma."
                        ],
                        "correctIndex": 0,
                        "explanation": "El triunfo en Europa hizo que la alta sociedad argentina adoptara el tango como símbolo de identidad patria."
                    }
                ]
            }
        }
    }

    story_chile_04 = {
        "id": "b2-argentinaba-04",
        "title": "La pasión por el psicoanálisis, los cafés y las librerías",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Un ensayo sociocultural sobre las tres grandes pasiones de la vida cotidiana porteña: el fenómeno único del psicoanálisis como práctica de masas, la liturgia cívica de los cafés tradicionales en tertulias sin prisas, y la vibrante noche intelectual de la calle Corrientes y la mítica librería El Ateneo Grand Splendid.",
        "characters": [
            "Psicoanalista lacaniana Dra. Inés",
            "Mozo del Café Tortoni Don Rodolfo",
            "Librero de lance de Corrientes Norberto",
            "Estudiante de filosofía Martín"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Buenos Aires ostenta un récord singular en las estadísticas sociológicas mundiales: es la urbe con la mayor concentración de psicoanalistas per cápita y una de las capitales con mayor densidad de librerías y teatros del planeta. Para el ciudadano porteño, acudir regularmente al diván no constituye un estigma reservado a patologías extremas, sino una práctica cotidiana de higiene mental, autoconocimiento y exploración existencial. Las teorías pioneras de Sigmund Freud y más tarde las elaboradas revisiones estructurales de Jacques Lacan permearen de tal forma el tejido social que términos clínicos como *inconsciente*, *acto fallido*, *pulsión*, *angustia* y *catarsis* forman parte habitual de cualquier charla informal entre amigos en una mesa de café."
            },
            {
                "type": "narration",
                "text": "Esta vocación casi obsesiva por el autoexamen y la deliberación crítica encuentra su escenario predilecto en la red inagotable de cafés tradicionales que puntean la geografía metropolitana. Establecimientos legendarios como el Café Tortoni en la Avenida de Mayo, Las Violetas en Almagro, La Biela en Recoleta o La Giralda en la calle Corrientes funcionan como verdaderas ágoras cívicas y salones de tertulia permanente. Frente a un pocillo de café servido con un vaso pequeño de soda y dos medialunas de manteca, escritores consagrados, estudiantes universitarios y transeúntes solitarios pasan horas enteras leyendo, redactando borradores o debatiendo acaloradamente sobre política, fútbol y dilemas éticos sin que ningún camarero los apresure a abandonar la mesa."
            },
            {
                "type": "narration",
                "text": "La noche porteña tiene su epicentro intelectual sobre la mítica Avenida Corrientes, arteria cosmopolita que 'nunca duerme' y que conecta la vorágine financiera del centro con los arrabales bohemios. A lo largo de sus aceras iluminadas por marquesinas de neón, decenas de librerías de saldo y novedades mantienen abiertas sus puertas hasta altas horas de la madrugada. Es una estampa habitual observar a decenas de lectores hojeando volúmenes de ensayo filosófico, novelas de ficción y cuadernos de poesía a las dos de la mañana, antes de cruzar la calzada para saborear una porción de pizza al molde con moscato en templos gastronómicos populares como Güerrín o Los Inmortales."
            },
            {
                "type": "narration",
                "text": "Entre los templos dedicados al libro descuella El Ateneo Grand Splendid, situado en el elegante barrio de Recoleta y catalogado internacionalmente como una de las librerías más hermosas del mundo. Instalada en un majestuoso teatro de comienzos del siglo XX que conservó intacta su cúpula pintada con alegorías sobre la paz tras la Gran Guerra, sus palcos dorados originales y su telón de terciopelo encarnado, la tienda permite a los visitantes sentarse en el antiguo escenario —reconvertido en un acogedor salón de té— para hojear textos rodeados por millares de estantes colmados de literatura universal en un ambiente de reverente silencio arquitectónico."
            },
            {
                "type": "narration",
                "text": "Esta imbricación entre el diván psicoanalítico, la mesa de café y la librería abierta hasta el amanecer evidencia una sociedad que se rehúsa categóricamente a la banalidad y al silencio reflexivo. En un país sacudido periódicamente por crisis económicas recurrentes, incertidumbres institucionales y fracturas políticas agudas, la palabra dialogada y la introspección teórica se erigen en trincheras de resistencia cívica fundamental. El habitante de Buenos Aires charla interminablemente no para evadir la realidad cotidiana, sino para desentrañar sus laberintos íntimos y encontrar en el lenguaje compartido un asidero donde afirmar su identidad colectiva."
            },
            {
                "type": "narration",
                "text": "Esa búsqueda constante de sentido a través del verbo compartido convierte a la capital argentina en una inmensa terapia comunitaria a cielo abierto. Entre sorbos de café humeante y páginas de libros recién comprados, la mente porteña descifra sus angustias y sus esperanzas con una lucidez insobornable, demostrando que mientras persistan un libro abierto y un interlocutor dispuesto al debate honesto, ningún laberinto existencial resultará completamente insondable ni ninguna herida espiritual carecerá de alivio."
            },
            {
                "type": "narration",
                "text": "En definitiva, el amor porteño por el pensamiento crítico, la psicoterapia y las páginas impresas constituye un pacto de honor con la inteligencia. En una época dominada por la prisa digital y el consumo efímero, Buenos Aires preserva con orgullo el arte sagrado de sentarse a conversar, reflexionar y soñar despierto a la luz cálida de una lámpara de cafetín."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué singularidad ostenta Buenos Aires en relación con la práctica y divulgación del psicoanálisis?",
                        "options": [
                            "Posee la mayor tasa mundial de terapeutas por habitante y su vocabulario forma parte del habla cotidiana.",
                            "Es la única ciudad del mundo donde el psicoanálisis está penado por leyes constitucionales estrictas.",
                            "Solo los miembros del parlamento tienen derecho legal a asistir a sesiones de terapia psicoanalítica.",
                            "Las sesiones terapéuticas son obligatorias por ley para poder contraer matrimonio civil en el registro."
                        ],
                        "correctIndex": 0,
                        "explanation": "Buenos Aires es mundialmente conocida por su densidad psicoanalítica y la naturalidad con que se practica."
                    },
                    {
                        "question": "¿Cuál es el rol cultural y cívico que desempeñan los cafés tradicionales en la vida cotidiana porteña?",
                        "options": [
                            "Operan como ágoras de deliberación democrática, lectura pausada y debate político y existencial.",
                            "Son comedores industriales donde los clientes deben comer de pie y retirarse en menos de diez minutos.",
                            "Funcionan exclusivamente como oficinas de cambio de divisas y casas de apuestas clandestinas.",
                            "Son centros de silencio riguroso donde está terminantemente prohibido conversar o sostener reuniones."
                        ],
                        "correctIndex": 0,
                        "explanation": "El cafetín porteño es una institución cívica de tertulia, literatura y permanencia sin apremios."
                    },
                    {
                        "question": "¿Qué características arquitectónicas convierten a El Ateneo Grand Splendid en una librería célebre en todo el mundo?",
                        "options": [
                            "Ocupa un antiguo teatro con palcos dorados, cúpula con frescos alegóricos y un escenario adaptado como café.",
                            "Fue excavada íntegramente en cavernas submarinas bajo las aguas turbias del Río de la Plata.",
                            "Está construida únicamente con madera reciclada de barcos pesqueros naufragados en el estrecho de Magallanes.",
                            "Consiste en una torre de cristal ultramoderna de ochenta pisos sin paredes interiores ni estantes."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Ateneo Grand Splendid conserva el esplendor teatral del antiguo Grand Splendid de 1919."
                    }
                ]
            }
        }
    }

    story_chile_05 = {
        "id": "b2-argentinaba-05",
        "title": "Jorge Luis Borges, Julio Cortázar y la literatura fantástica",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Un estudio crítico sobre los dos pilares de la literatura fantástica y metafísica argentina: la poética borgesiana de los laberintos, los espejos, el infinito y 'El Aleph', junto a la revolución lúdica, existencial y subversiva de Julio Cortázar en relatos como 'Casa tomada' y su obra cumbre 'Rayuela'.",
        "characters": [
            "Catedrático de letras rioplatenses Dr. Valenzuela",
            "Ensayista y crítica literaria Estela",
            "Joven narrador borgesiano Ignacio",
            "Lectora cortazariana y editora Mariana"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Pocas ciudades del mundo han sido recreadas con tanta hondura mitológica y rigor estético como Buenos Aires a través de la obra monumental de sus dos máximos artífices literarios: Jorge Luis Borges y Julio Cortázar. Para Borges, la metrópolis rioplatense no era un simple decorado geográfico ni un mero testimonio costumbrista, sino una sustancia ontológica que oscilaba permanentemente entre la memoria histórica y la ensoñación metafísica. En cuentos fundacionales como *El Aleph*, sitúa en el modesto sótano de una vieja casona de la calle Garay el punto prodigioso donde coinciden, sin superponerse, todos los lugares del cosmos contemplados desde todos los ángulos del infinito."
            },
            {
                "type": "narration",
                "text": "El universo borgesiano se articula en torno a laberintos inextricables, espejos que multiplican el horror del infinito, bibliotecas colosales que contienen todos los libros posibles y tigres que acechan en la penumbra de los sueños. Maestro absoluto de la concisión sintáctica y del distanciamiento irónico, Borges subvirtió los géneros tradicionales al convertir la erudición apócrifa, las reseñas de libros imaginarios y las paradojas teológicas en piezas maestras de la ficción contemporánea. Bajo su pluma exquisita, las desoladas esquinas de arrabal donde los compadritos dirimían duelos a cuchillo se transfiguraron en arquetipos universales sobre el honor, el coraje y la fatalidad del tiempo."
            },
            {
                "type": "narration",
                "text": "Por su parte, Julio Cortázar exploró con maestría inigualable la otra vertiente de la literatura fantástica: la irrupción repentina de lo insólito y perturbador en el corazón de la cotidianidad urbana más apacible. En relatos extraordinarios como *Casa tomada*, una fuerza invisible y misteriosa expulsa paulatinamente a dos hermanos de su señorial mansión familiar; en *Axolotl*, la contemplación hipnótica de un anfibio en un acuario parisino desemboca en la transmigración de la conciencia del observador al interior del animal. Cortázar demostró que el misterio no precisa de castillos góticos ni apariciones espectrales, sino que aguarda agazapado en el reverso de una rutina doméstica o en un vagón de metro."
            },
            {
                "type": "narration",
                "text": "Con la publicación en 1963 de su obra cumbre, *Rayuela*, Cortázar propuso una auténtica revolución formal que desarticuló la lectura lineal tradicional. Estructurada como un artefacto lúdico que puede leerse siguiendo múltiples itinerarios propuestos por el propio autor, la novela tiende un puente existencial entre el París bohemio de los clubes de jazz y el Buenos Aires melancólico de las pensiones y los hospitales psiquiátricos. Sus personajes emblemáticos, como Horacio Oliveira y La Maga, encarnaron la búsqueda desesperada de un sentido vital al margen de las convenciones burguesas y la rigidez del pensamiento racionalista occidental."
            },
            {
                "type": "narration",
                "text": "Tanto Borges como Cortázar, acompañados por figuras indispensables como Adolfo Bioy Casares y Silvina Ocampo, consolidaron la literatura fantástica rioplatense como un faro de autonomía estética de proyección ecuménica sin precedentes. Sus relatos no buscan el mero entretenimiento evasivo, sino que interpelan al lector sobre la consistencia ilusoria de la realidad, los enigmas de la percepción humana y el poder mágico de la palabra escrita. Al internarse en sus páginas, el lector descubre que Buenos Aires es, ante todo, un vasto laberinto de tinta y memoria que continúa reinventándose cada vez que un libro se abre."
            },
            {
                "type": "narration",
                "text": "Esa herencia intelectual desafía continuamente la imaginación de quienes caminan hoy por las calles arboladas de Palermo, Constitución o Balvanera. Cada zaguán sombrío parece ocultar un secreto metafísico insondable y cada rayuela trazada con tiza en la acera invita a saltar de la tierra al cielo, recordando a los caminantes que la verdadera patria del escritor rioplatense es el territorio infinito y libre de la literatura universal."
            },
            {
                "type": "narration",
                "text": "Así, la capital argentina pervive en la imaginación del mundo como un mapa soñado donde convergen la memoria de los arrabales populares y las más altas cumbres de la especulación metafísica. En cada verso de Borges y en cada juego narrativo de Cortázar, la ciudad se renueva eternamente como un misterio fascinante donde la realidad cotidiana se disuelve para dar paso a la magia inagotable del arte literario, permitiendo que cada lector se reconozca como un viajero perpetuo entre el asombro y la lucidez."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué manera sitúa Jorge Luis Borges el prodigio de 'El Aleph' en el contexto urbano de Buenos Aires?",
                        "options": [
                            "Lo ubica en el sótano de una modesta vivienda de la calle Garay como vórtice donde converge el cosmos entero.",
                            "En la cúspide del Obelisco de la Avenida 9 de Julio durante un eclipse solar anunciado por astrónomos.",
                            "En la bodega de un barco de carga anclado en la dársena norte del puerto de ultramar.",
                            "En la caja fuerte blindada del Banco Central custodiada por guardias armados y sensores infrarrojos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Borges sitúa el Aleph en el sótano de la casa de Carlos Argentino Daneri en la calle Garay."
                    },
                    {
                        "question": "¿Cómo concibe Julio Cortázar lo fantástico en sus narraciones breves?",
                        "options": [
                            "Como una grieta perturbadora que irrumpe de improviso en el seno de la cotidianidad doméstica más corriente.",
                            "A través de relatos históricos estrictamente documentados sobre las batallas navales de la independencia.",
                            "Mediante el uso exclusivo de monstruos mitológicos gigantescos tomados de la epopeya clásica griega.",
                            "Como tratados científicos sobre botánica amazónica sin elementos imaginarios ni metáforas poéticas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Para Cortázar, lo fantástico no es sobrenatural externo, sino una alteración repentina de lo cotidiano."
                    },
                    {
                        "question": "¿Qué innovación estructural fundamental propuso Cortázar a los lectores con la publicación de 'Rayuela'?",
                        "options": [
                            "Una estructura de novela múltiple y lúdica que admite diversos órdenes de lectura y capítulos prescindibles.",
                            "La obligación legal de leer la obra de atrás hacia adelante en voz alta ante un tribunal judicial.",
                            "Un texto compuesto exclusivamente de diagramas matemáticos y fórmulas químicas sin palabras en prosa.",
                            "Un volumen que contenía páginas en blanco para que cada lector redactara su propia biografía infantil."
                        ],
                        "correctIndex": 0,
                        "explanation": "Rayuela es una 'antinovela' o contranovela abierta con un tablero de dirección para múltiples lecturas."
                    }
                ]
            }
        }
    }

    story_chile_capstone = {
        "id": "b2-argentinaba-consolidation",
        "title": "El laberinto porteño: Síntesis de una metrópolis infinita",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis abarcadora de Buenos Aires: la impronta fundacional del Río de la Plata y las avenidas monumentales, la gesta colectiva de los conventillos y el cocoliche, la filosofía sentimental del tango y el bandoneón, el ritual cotidiano del psicoanálisis y las librerías nocturnas, y la inmortalidad metafísica legada por Borges y Cortázar.",
        "characters": [
            "Cronista mayor de la ciudad Don Horacio",
            "Socióloga urbana Florencia",
            "Músico de tango y compositor Andrés",
            "Bibliófila y ensayista Carolina"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Buenos Aires se erige sobre la margen occidental del Río de la Plata como una urbe de geometrías complejas, donde la nostalgia pampeana se funde con los anhelos cosmopolitas de una metrópolis que siempre soñó con ser el espejo austral de Europa. Su fisonomía no responde a un trazado monolítico, sino a la superposición apasionada de mareas migratorias, debates intelectuales y revoluciones estéticas que fueron sedimentando una personalidad intransferible. Desde los palacetes de Recoleta hasta los conventillos de zinc de La Boca, cada rincón porteño testimonia la obstinada voluntad de sus habitantes por inventar una voz propia en el cruce de todos los caminos del mundo."
            },
            {
                "type": "narration",
                "text": "La memoria fluvial del estuario condicionó los primeros siglos de aislamiento colonial, pero fue la gigantesca ola inmigratoria de entresiglos la que transformó definitivamente el alma de la urbe. Italianos de todas las provincias peninsulares, campesinos españoles, judíos asquenazíes y colectividades de Oriente Medio aportaron su fuerza laboral, sus penurias cotidianas y sus lenguajes híbridos en el crisol de los conventillos. De aquel roce constante y desgarrador nació el cocoliche y floreció el lunfardo, enriqueciendo el caudal del idioma castellano con una sonoridad picante y expresiva que pronto hallaría su cauce inmortal en los compases del tango."
            },
            {
                "type": "narration",
                "text": "El bandoneón, con su lamento arrastrado y su cadencia sincopada, se convirtió en el órgano emocional de la ciudad. Carlos Gardel dotó a la canción arrabalera de prestancia mundial, mientras letristas como Discépolo plasmaron una filosofía del desencanto que aún interpela las contradicciones humanas más dolorosas. Más tarde, la genialidad vanguardista de Astor Piazzolla desbordó las fronteras del género, fusionando la melancolía del puerto con las armonías contemporáneas de la música docta y el pulso libre del jazz. En las pistas de las milongas, el abrazo apretado sigue siendo el ritual donde la soledad individual se disuelve en el compás de dos cuerpos que caminan juntos."
            },
            {
                "type": "narration",
                "text": "Paralelamente, la capital desarrolló una pulsión reflexiva única manifestada en su devoción por el psicoanálisis, la bohemia de sus cafetines históricos y la vigencia asombrosa de sus librerías nocturnas. Sobre la calle Corrientes o bajo las molduras doradas de El Ateneo Grand Splendid, la palabra hablada y escrita se erige en una liturgia civil indispensable para el ciudadano común. El porteño se piensa, se interroga y se cuestiona incansablemente frente a una taza de café, convencido de que la introspección teórica, la ironía lúcida y el debate apasionado constituyen la herramienta más noble para resistir las zozobras materiales y el vértigo abrumador de la modernidad."
            },
            {
                "type": "narration",
                "text": "En la cúspide de este universo brilla la literatura fantástica de Jorge Luis Borges y Julio Cortázar, quienes transformaron la topografía rioplatense en un territorio metafísico de laberintos, espejos y rayuelas infinitas. Comprender Buenos Aires exige recorrer sus calles como quien descifra un libro infinito: cada esquina encierra una biblioteca secreta, un fuelle que suspira en la penumbra o un diván donde se desanudan los misterios del alma. La Reina del Plata permanece así como un laberinto acogedor e inagotable, donde la melancolía del pasado alimenta sin cesar la fecunda creatividad del porvenir."
            },
            {
                "type": "narration",
                "text": "Caminar por Buenos Aires en el silencio de la medianoche, cuando el viento del río acaricia los plátanos añosos y las luces de los cafetines titilan en la penumbra, es comprender que las ciudades verdaderas no se miden por sus dimensiones geográficas, sino por la intensidad apasionada con que sus pueblos aman, sueñan, recuerdan y transforman sus nostalgias más hondas en monumentos eternos de la cultura universal."
            },
            {
                "type": "narration",
                "text": "Ese es el legado imperecedero de la gran metrópolis austral: una ciudad que aprendió a convertir sus crisis en poesía viva, sus inmigraciones en crisol fecundo de identidades y sus noches de café en un diálogo interminable con el infinito. Quien se adentra en su dédalo de avenidas monumentales y arrabales silenciosos ya no puede contemplar el mundo del mismo modo, porque Buenos Aires enseña con ternura y coraje que en cada esquina solitaria late siempre la promesa intacta de una nueva, generosa y deslumbrante invención humana."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué manera moldearon las sucesivas olas inmigratorias el lenguaje y la identidad cultural de Buenos Aires?",
                        "options": [
                            "Aportaron una rica hibridación lingüística con el cocoliche y el lunfardo, modelando el habla popular y el tango.",
                            "Impusieron el aprendizaje forzoso del latín clásico en todas las escuelas y juzgados municipales.",
                            "Obligaron a la población criolla a abandonar por completo las costumbres rioplatenses del mate y el asado.",
                            "Hicieron que la ciudad perdiera su carácter portuario para convertirse en una aldea exclusivamente agraria."
                        ],
                        "correctIndex": 0,
                        "explanation": "La inmigración enriqueció el español con dialectos italianos y lunfardo, creando una cultura híbrida única."
                    },
                    {
                        "question": "¿Qué evolución artística experimentó el tango desde sus orígenes marginales hasta las innovaciones de Astor Piazzolla?",
                        "options": [
                            "Transitó desde los prostíbulos orilleros y el auge gardeliano hasta la sofisticada fusión clásica y jazzística piazzolliana.",
                            "Comenzó como una danza de corte imperial en Viena y terminó como una marcha militar rural en la Patagonia.",
                            "Fue prohibido permanentemente en toda América del Sur por considerarse perjudicial para la salud pública.",
                            "Se transformó en un género exclusivo de flauta dulce sin acompañamiento instrumental ni letra poética."
                        ],
                        "correctIndex": 0,
                        "explanation": "El tango evolucionó de danza orillera prostibularia a género refinado, popular y vanguardista universal."
                    },
                    {
                        "question": "¿Por qué se afirma que la literatura y el debate intelectual convierten a Buenos Aires en un territorio metafísico?",
                        "options": [
                            "Porque autores como Borges y Cortázar transfiguraron la topografía urbana en laberintos filosóficos y reflexivos.",
                            "Debido a que todos los habitantes de la ciudad son graduados con títulos doctorales en matemáticas avanzadas.",
                            "Porque las leyes municipales obligan a cada ciudadano a escribir un libro de versos antes de cumplir treinta años.",
                            "Porque la ciudad fue construida sobre pirámides astronómicas similares a las de Teotihuacan o Egipto."
                        ],
                        "correctIndex": 0,
                        "explanation": "Borges y Cortázar otorgaron a Buenos Aires una dimensión mítica y metafísica de validez ecuménica."
                    }
                ]
            }
        }
    }

    # Consolidated 25-paragraph Library reading (b2-argentinaba.json)
    story_library = {
        "id": "b2-argentinaba",
        "title": "Retrato integral de Buenos Aires: Río, tango, inmigración y literatura",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 25,
        "summary": "Compendio completo de los cinco estudios sobre Buenos Aires: la evolución urbanística junto al Río de la Plata, la epopeya de la inmigración masiva y el cocoliche, la gestación del tango y el lunfardo, el papel civil del psicoanálisis, los cafetines y librerías, y la trascendencia universal de la literatura de Borges y Cortázar.",
        "characters": [
            "Narrador y cronista general de Buenos Aires",
            "Inmigrantes, músicos, psicoanalistas y escritores porteños"
        ],
        "paragraphs": story_chile_01["paragraphs"][:5] + \
                      story_chile_02["paragraphs"][:5] + \
                      story_chile_03["paragraphs"][:5] + \
                      story_chile_04["paragraphs"][:5] + \
                      story_chile_05["paragraphs"][:5],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cómo influyó la relación contradictoria con el Río de la Plata en la evolución urbanística y portuaria de Buenos Aires?",
                        "options": [
                            "Forzó un paso gradual desde el aislamiento colonial hasta la creación y reconversión moderna de Puerto Madero.",
                            "Obligó a trasladar la capital hacia la cordillera de los Andes durante todo el siglo diecinueve.",
                            "Provocó la desaparición de todas las zonas residenciales al sur del Riachuelo por inundaciones permanentes.",
                            "Impidió que la ciudad recibiera barcos de vapor transatlánticos hasta comienzos del siglo veintiuno."
                        ],
                        "correctIndex": 0,
                        "explanation": "Buenos Aires superó sus barreras portuarias iniciales mediante ambiciosas obras que hoy son distritos modernos."
                    },
                    {
                        "question": "¿Qué papel cumplieron los conventillos y las mutuales obreras en la integración de las colectividades inmigrantes?",
                        "options": [
                            "Fueron el crisol social donde convivieron diversas nacionalidades y surgieron redes solidarias de defensa obrera.",
                            "Sirvieron como escuelas militares donde los extranjeros recibían entrenamiento de combate naval.",
                            "Eran prisiones de alta seguridad donde los recién llegados cumplían cuarentenas de varios años.",
                            "Funcionaban como fábricas estatales de pólvora donde solo trabajaban artesanos genoveses solteros."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los conventillos y mutuales forjaron los lazos comunitarios y la identidad de la clase trabajadora porteña."
                    },
                    {
                        "question": "¿Qué elementos poéticos y musicales hicieron del tango y de la literatura fantástica los dos grandes emblemas universales porteños?",
                        "options": [
                            "La transfiguración estética de la melancolía, el desarraigo, el honor y los misterios metafísicos del tiempo.",
                            "Su devoción exclusiva por ensalzar los tratados comerciales de exportación de cueros pampeanos.",
                            "El uso obligatorio de himnos patrióticos en lengua guaraní para acompañar las ceremonias cívicas.",
                            "La imitación exacta de las comedias musicales británicas sin ningún elemento cultural latinoamericano."
                        ],
                        "correctIndex": 0,
                        "explanation": "Tanto el tango como la literatura borgesiana convirtieron las vivencias porteñas en arquetipos universales."
                    }
                ]
            }
        }
    }

    stories_to_write = [
        ("stories/classics/b2/b2-24.json", story_core_24),
        ("stories/world/b2/b2-argentinaba-01.json", story_chile_01),
        ("stories/world/b2/b2-argentinaba-02.json", story_chile_02),
        ("stories/world/b2/b2-argentinaba-03.json", story_chile_03),
        ("stories/world/b2/b2-argentinaba-04.json", story_chile_04),
        ("stories/world/b2/b2-argentinaba-05.json", story_chile_05),
        ("stories/world/b2/b2-argentinaba-consolidation.json", story_chile_capstone),
        ("stories/world/b2/b2-argentinaba.json", story_library)
    ]

    all_ok = True
    for path, s in stories_to_write:
        wc = count_words(s)
        if "b2-argentinaba.json" not in path:
            print(f"{path}: {wc} words")
            if not (650 <= wc <= 825):
                print(f"ERROR: {path} word count {wc} out of range [650, 825]!")
                all_ok = False
        write_json(path, s)

    # 6. Exercises (12 files: 10 main x 6 exercises + 2 consolidation x 8 exercises = 76 exercises)
    # Exercise Metadata rules:
    # - category: vocabulary | grammar | reading | dialogue | writing | listening
    # - teaches: canonical skill slug from skill-registry.json
    # - category vocabulary -> teaches b2-24-vocab or b2-argentinaba-vocab
    # - category grammar -> teaches grammar skill
    # - dictation -> sentence
    # - multiple-choice -> correct: 0 (NO explanation, NO correctIndex)
    # - fill-blank -> sentence: "... __ ...", answer: "...", english: "..."
    # - sentence-builder -> tiles, solution, english
    # - dialogue-complete -> prompt: [{"speaker": "...", "text": "..."}], options, correct: 0
    # - matching -> pairs: [[es, en], ...]

    # b2-24-01-ex.json (llevar + gerundio)
    write_json("exercises/b2/b2-24-01-ex.json", {
        "lesson": "b2-24-01",
        "exercises": [
            {
                "id": "b2-24-01.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz aspectual primordial aporta la perífrasis 'llevar + gerundio'?",
                "options": [
                    "Cuantifica la duración temporal acumulada de una acción iniciada en el pasado que sigue vigente.",
                    "Indica el cese definitivo e irreversible de una actividad profesional prolongada.",
                    "Expresa una acción repentina e involuntaria motivada por el miedo o el asombro.",
                    "Describe un hábito futuro que comenzará tras cumplir un requisito previo."
                ],
                "correct": 0,
                "teaches": ["llevar-gerundio"]
            },
            {
                "id": "b2-24-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los investigadores porteños __ meses analizando los planos originales de los primeros conventillos de La Boca.",
                "answer": "llevan",
                "english": "The Buenos Aires researchers have been analyzing the original plans of the first La Boca tenements for months.",
                "teaches": ["llevar-gerundio"]
            },
            {
                "id": "b2-24-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Llevábamos", "tres", "años", "viviendo", "en", "San Telmo", "cuando", "abrieron", "el", "taller."],
                "solution": ["Llevábamos", "tres", "años", "viviendo", "en", "San Telmo", "cuando", "abrieron", "el", "taller."],
                "english": "We had been living in San Telmo for three years when they opened the workshop.",
                "teaches": ["llevar-gerundio"]
            },
            {
                "id": "b2-24-01.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["trayectoria", "track record / trajectory"],
                    ["andadura", "journey / course of time"],
                    ["ininterrumpido", "uninterrupted"],
                    ["permanencia", "permanence / stay"],
                    ["constancia", "perseverance / steady effort"]
                ],
                "teaches": ["b2-24-vocab"]
            },
            {
                "id": "b2-24-01.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Martín", "text": "¿Cuánto tiempo hace que trabajás en este archivo histórico?"},
                    {"speaker": "Valeria", "text": "La verdad es que ya __ casi una década ordenando estos legajos."}
                ],
                "options": [
                    "llevo",
                    "rompo a",
                    "vuelvo a",
                    "pongo a"
                ],
                "correct": 0,
                "teaches": ["llevar-gerundio"]
            },
            {
                "id": "b2-24-01.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El maestro de tango lleva más de cuarenta años perfeccionando su estilo en los salones de baile.",
                "english": "The tango master has been perfecting his style in dance halls for more than forty years.",
                "teaches": ["llevar-gerundio"]
            }
        ]
    })

    # b2-24-02-ex.json (seguir + gerundio)
    write_json("exercises/b2/b2-24-02-ex.json", {
        "lesson": "b2-24-02",
        "exercises": [
            {
                "id": "b2-24-02.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la función semántica de 'seguir + gerundio' frente a 'dejar de + infinitivo'?",
                "options": [
                    "Focaliza la continuidad inalterada de una acción frente a obstáculos o expectativas de cese.",
                    "Expresa el inicio fulminante y sorpresivo de una emoción intensa.",
                    "Indica la conclusión fortuita y no planificada de un proceso complejo.",
                    "Manifiesta la repetición cíclica de una acción tras haber sido interrumpida."
                ],
                "correct": 0,
                "teaches": ["seguir-gerundio"]
            },
            {
                "id": "b2-24-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A pesar de las transformaciones modernas de la ciudad, las viejas milongas __ reuniendo a cientos de apasionados.",
                "answer": "siguen",
                "english": "Despite modern transformations of the city, the old milongas keep bringing together hundreds of enthusiasts.",
                "teaches": ["seguir-gerundio"]
            },
            {
                "id": "b2-24-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "músicos", "siguieron", "ensayando", "la", "pieza", "a", "pesar", "del", "corte", "eléctrico."],
                "solution": ["Los", "músicos", "siguieron", "ensayando", "la", "pieza", "a", "pesar", "del", "corte", "eléctrico."],
                "english": "The musicians kept rehearsing the piece despite the power outage.",
                "teaches": ["seguir-gerundio"]
            },
            {
                "id": "b2-24-02.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["persistencia", "persistence"],
                    ["obstinación", "obstinacy / stubbornness"],
                    ["vigencia", "validity / current relevance"],
                    ["perdurabilidad", "durability / endurance"],
                    ["inalterable", "unalterable / unchanging"]
                ],
                "teaches": ["b2-24-vocab"]
            },
            {
                "id": "b2-24-02.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Federico", "text": "¿No pensaron en clausurar la imprenta tras la crisis del papel?"},
                    {"speaker": "Clara", "text": "Al contrario, nosotros __ imprimiendo obras independientes con el mismo empeño."}
                ],
                "options": [
                    "seguimos",
                    "rompemos a",
                    "echamos a",
                    "pasamos a"
                ],
                "correct": 0,
                "teaches": ["seguir-gerundio"]
            },
            {
                "id": "b2-24-02.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Aunque pasen las décadas, la poesía de Manzi sigue emocionando por su honda melancolía.",
                "english": "Even though decades go by, Manzi's poetry continues to move people with its deep melancholy.",
                "teaches": ["seguir-gerundio"]
            }
        ]
    })

    # b2-24-03-ex.json (ir + gerundio)
    write_json("exercises/b2/b2-24-03-ex.json", {
        "lesson": "b2-24-03",
        "exercises": [
            {
                "id": "b2-24-03.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué diferencia específica presenta 'ir + gerundio' frente a 'estar + gerundio'?",
                "options": [
                    "Expresa un desarrollo paulatino, incremental y paso a paso hacia una culminación.",
                    "Describe una acción estática que ocurre simultáneamente a otra sin progreso alguno.",
                    "Indica una orden perentoria que el interlocutor debe cumplir de inmediato.",
                    "Señala la culminación violenta y accidental de un suceso inesperado."
                ],
                "correct": 0,
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": "b2-24-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Con el arribo de cada oleada de familias, el barrio se __ transformando en un polo comercial cosmopolita.",
                "answer": "fue",
                "english": "With the arrival of each wave of families, the neighborhood was gradually transforming into a cosmopolitan commercial hub.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": "b2-24-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Poco", "a", "poco", "vamos", "comprendiendo", "la", "complejidad", "sociológica", "del", "puerto."],
                "solution": ["Poco", "a", "poco", "vamos", "comprendiendo", "la", "complejidad", "sociológica", "del", "puerto."],
                "english": "Little by little, we are gradually understanding the sociological complexity of the port.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": "b2-24-03.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["paulatino", "gradual / step-by-step"],
                    ["despliegue", "unfolding / rollout"],
                    ["afianzamiento", "consolidation / strengthening"],
                    ["maduración", "maturation / ripening"],
                    ["decantación", "distillation / settling down"]
                ],
                "teaches": ["b2-24-vocab"]
            },
            {
                "id": "b2-24-03.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Horacio", "text": "¿Cómo evoluciona la restauración de las cúpulas históricas?"},
                    {"speaker": "Beatriz", "text": "Los arquitectos __ recuperando los detalles originales fachada por fachada."}
                ],
                "options": [
                    "van",
                    "andan",
                    "echan a",
                    "rompen a"
                ],
                "correct": 0,
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": "b2-24-03.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las diferencias estéticas entre ambas corrientes poéticas se fueron atenuando con los años.",
                "english": "The aesthetic differences between both poetic movements gradually softened over the years.",
                "teaches": ["perifrasis-ir-gerundio"]
            }
        ]
    })

    # b2-24-04-ex.json (andar + gerundio)
    write_json("exercises/b2/b2-24-04-ex.json", {
        "lesson": "b2-24-04",
        "exercises": [
            {
                "id": "b2-24-04.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo característico distingue a la perífrasis 'andar + gerundio'?",
                "options": [
                    "Describe una actividad dispersa, errática, itinerante o no sujeta a un plan estricto.",
                    "Indica una progresión matemática perfectamente secuencial y acumulativa.",
                    "Denota una acción que concluye bruscamente antes de alcanzar su meta.",
                    "Expresa una orden solemne emitida por una autoridad eclesiástica o jurídica."
                ],
                "correct": 0,
                "teaches": ["perifrasis-andar-gerundio"]
            },
            {
                "id": "b2-24-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El cronista porteño __ buscando testimonios orales por los cafetines más escondidos de Boedo.",
                "answer": "anda",
                "english": "The Buenos Aires chronicler is going around looking for oral testimonies in the most hidden little cafés of Boedo.",
                "teaches": ["perifrasis-andar-gerundio"]
            },
            {
                "id": "b2-24-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "vecinos", "andan", "diciendo", "que", "abrirán", "un", "nuevo", "centro", "cultural."],
                "solution": ["Los", "vecinos", "andan", "diciendo", "que", "abrirán", "un", "nuevo", "centro", "cultural."],
                "english": "The neighbors are going around saying that they will open a new cultural center.",
                "teaches": ["perifrasis-andar-gerundio"]
            },
            {
                "id": "b2-24-04.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["errante", "wandering / roving"],
                    ["desasosiego", "restlessness / uneasiness"],
                    ["merodear", "to prowl / to loiter about"],
                    ["trajín", "bustle / coming and going"],
                    ["deriva", "drift / wandering course"]
                ],
                "teaches": ["b2-24-vocab"]
            },
            {
                "id": "b2-24-04.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Ernesto", "text": "¿Supiste algo de Silvio en estos últimos días?"},
                    {"speaker": "Lucía", "text": "Sí, me contaron que __ tramando otro invento insólito en su taller."}
                ],
                "options": [
                    "anda",
                    "rompe a",
                    "lleva a",
                    "pasa a"
                ],
                "correct": 0,
                "teaches": ["perifrasis-andar-gerundio"]
            },
            {
                "id": "b2-24-04.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "No andes divulgando sospechas infundadas antes de revisar los documentos oficiales.",
                "english": "Do not go around spreading unfounded suspicions before reviewing the official documents.",
                "teaches": ["perifrasis-andar-gerundio"]
            }
        ]
    })

    # b2-24-05-ex.json (venir + gerundio)
    write_json("exercises/b2/b2-24-05-ex.json", {
        "lesson": "b2-24-05",
        "exercises": [
            {
                "id": "b2-24-05.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué énfasis aporta 'venir + gerundio' en el discurso histórico y ensayístico?",
                "options": [
                    "Subraya la trayectoria acumulativa y continuada de un proceso desde el pasado hasta el presente.",
                    "Indica que el sujeto está a punto de emprender un viaje físico hacia su lugar natal.",
                    "Expresa una duda epistemológica sobre la veracidad de testimonios antiguos.",
                    "Señala la culminación repentina de una disputa comercial tras una mediación."
                ],
                "correct": 0,
                "teaches": ["perifrasis-venir-gerundio"]
            },
            {
                "id": "b2-24-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los sociólogos rioplatenses __ advirtiendo sobre las secuelas emocionales de las crisis recurrentes.",
                "answer": "vienen",
                "english": "River Plate sociologists have been warning about the emotional aftermath of recurrent crises.",
                "teaches": ["perifrasis-venir-gerundio"]
            },
            {
                "id": "b2-24-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Esta", "editorial", "viene", "publicando", "obras", "filosóficas", "fundamentales", "desde", "hace", "décadas."],
                "solution": ["Esta", "editorial", "viene", "publicando", "obras", "filosóficas", "fundamentales", "desde", "hace", "décadas."],
                "english": "This publishing house has been publishing fundamental philosophical works for decades.",
                "teaches": ["perifrasis-venir-gerundio"]
            },
            {
                "id": "b2-24-05.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["acumulativo", "cumulative"],
                    ["gestación", "gestation / genesis"],
                    ["sedimentación", "gradual buildup / sedimentation"],
                    ["reiteración", "repetition / reiteration"],
                    ["continuo", "continuum / continuous flow"]
                ],
                "teaches": ["b2-24-vocab"]
            },
            {
                "id": "b2-24-05.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Santiago", "text": "¿Desde cuándo se debate la reapertura de ese mítico teatro?"},
                    {"speaker": "Mariana", "text": "Los vecinos y artistas lo __ reclamando desde hace más de quince años."}
                ],
                "options": [
                    "vienen",
                    "echan a",
                    "rompen a",
                    "pasan a"
                ],
                "correct": 0,
                "teaches": ["perifrasis-venir-gerundio"]
            },
            {
                "id": "b2-24-05.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El historiador viene sosteniendo que la identidad urbana de Buenos Aires nació en los conventillos.",
                "english": "The historian has been maintaining that the urban identity of Buenos Aires was born in the tenements.",
                "teaches": ["perifrasis-venir-gerundio"]
            }
        ]
    })

    # b2-24-consolidation-ex.json (8 exercises: integration of periphrases)
    write_json("exercises/b2/b2-24-consolidation-ex.json", {
        "lesson": "b2-24-consolidation",
        "exercises": [
            {
                "id": "b2-24-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué perífrasis durativa expresa un avance gradual y escalonado hacia una meta?",
                "options": [
                    "Ir + gerundio",
                    "Andar + gerundio",
                    "Echarse a + infinitivo",
                    "Romper a + infinitivo"
                ],
                "correct": 0,
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": "b2-24-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Aunque algunos críticos pronosticaban su desaparición, las orquestas típicas __ interpretando tango clásico.",
                "answer": "siguen",
                "english": "Although some critics predicted their disappearance, typical orchestras keep performing classic tango.",
                "teaches": ["seguir-gerundio"]
            },
            {
                "id": "b2-24-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "vecinos", "llevaban", "meses", "reclamando", "la", "preservación", "del", "viejo", "cine."],
                "solution": ["Los", "vecinos", "llevaban", "meses", "reclamando", "la", "preservación", "del", "viejo", "cine."],
                "english": "The neighbors had been demanding the preservation of the old cinema for months.",
                "teaches": ["llevar-gerundio"]
            },
            {
                "id": "b2-24-consolidation.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["continuidad", "continuity"],
                    ["latente", "latent / dormant"],
                    ["progresión", "progression"],
                    ["desasosiego", "restlessness / uneasiness"],
                    ["sedimentación", "gradual buildup / sedimentation"]
                ],
                "teaches": ["b2-24-vocab"]
            },
            {
                "id": "b2-24-consolidation.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Esteban", "text": "¿Qué te pareció el artículo sobre Roberto Arlt?"},
                    {"speaker": "Camila", "text": "Brillante; el autor __ explorando esas paradojas existenciales desde hace años."}
                ],
                "options": [
                    "viene",
                    "rompe a",
                    "echa a",
                    "pasa a"
                ],
                "correct": 0,
                "teaches": ["perifrasis-venir-gerundio"]
            },
            {
                "id": "b2-24-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz pragmático introduce frecuentemente 'andar + gerundio' en la interacción oral?",
                "options": [
                    "Inquietud, reproche o dispersión en la realización de una tarea.",
                    "Certeza científica respaldada por experimentos contrastados.",
                    "Obligación legal impuesta por una corte suprema.",
                    "Aceptación sumisa de un veredicto desfavorable."
                ],
                "correct": 0,
                "teaches": ["perifrasis-andar-gerundio"]
            },
            {
                "id": "b2-24-consolidation.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "A lo largo de las décadas, la metrópolis fue transformando sus márgenes portuarios en modernos distritos culturales.",
                "english": "Over the decades, the metropolis was gradually transforming its port waterfronts into modern cultural districts.",
                "teaches": ["perifrasis-ir-gerundio"]
            },
            {
                "id": "b2-24-consolidation.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "¿Por qué __ diciendo falsedades sobre el proyecto editorial en lugar de informarte adecuadamente?",
                "answer": "andás",
                "english": "Why are you going around saying falsehoods about the publishing project instead of properly informing yourself?",
                "teaches": ["perifrasis-andar-gerundio"]
            }
        ]
    })

    # Regional exercises: b2-argentinaba
    # b2-argentinaba-01-ex.json (locuciones prepositivas espaciales)
    write_json("exercises/b2/b2-argentinaba-01-ex.json", {
        "lesson": "b2-argentinaba-01",
        "exercises": [
            {
                "id": "b2-argentinaba-01.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué locución prepositiva espacial denota extensión continua y paralela a un eje urbano?",
                "options": [
                    "A lo largo de",
                    "A expensas de",
                    "En aras de",
                    "A falta de"
                ],
                "correct": 0,
                "teaches": ["locuciones-prepositivas-espaciales"]
            },
            {
                "id": "b2-argentinaba-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "__ del Río de la Plata se extendían primitivos bañados y pajonales antes del trazado de los bulevares.",
                "answer": "A orillas",
                "english": "On the shores of the Río de la Plata extended primitive wetlands and reedbeds before the laying out of the boulevards.",
                "teaches": ["locuciones-prepositivas-espaciales"]
            },
            {
                "id": "b2-argentinaba-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["En", "torno", "a", "la", "Plaza", "de", "Mayo", "convergen", "los", "edificios", "institucionales."],
                "solution": ["En", "torno", "a", "la", "Plaza", "de", "Mayo", "convergen", "los", "edificios", "institucionales."],
                "english": "Around Plaza de Mayo converge the institutional buildings.",
                "teaches": ["locuciones-prepositivas-espaciales"]
            },
            {
                "id": "b2-argentinaba-01.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["estuario", "estuary"],
                    ["trazado", "layout / urban grid"],
                    ["dársena", "dock / harbor basin"],
                    ["barranca", "ravine / riverside slope"],
                    ["arbolado", "tree-lined / grove"]
                ],
                "teaches": ["b2-argentinaba-vocab"]
            },
            {
                "id": "b2-argentinaba-01.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Guía", "text": "¿Hacia dónde se orientan los docks reformados de Puerto Madero?"},
                    {"speaker": "Visitante", "text": "Se sitúan exactamente __ antiguo canal de navegación del puerto."}
                ],
                "options": [
                    "frente al",
                    "a despecho del",
                    "en pos del",
                    "por mor del"
                ],
                "correct": 0,
                "teaches": ["locuciones-prepositivas-espaciales"]
            },
            {
                "id": "b2-argentinaba-01.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "A lo largo de la Avenida de Mayo se aprecian fachadas majestuosas con cúpulas art nouveau.",
                "english": "Along Avenida de Mayo one can appreciate majestic facades with art nouveau domes.",
                "teaches": ["locuciones-prepositivas-espaciales"]
            }
        ]
    })

    # b2-argentinaba-02-ex.json (voseo rioplatense)
    write_json("exercises/b2/b2-argentinaba-02-ex.json", {
        "lesson": "b2-argentinaba-02",
        "exercises": [
            {
                "id": "b2-argentinaba-02.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la forma verbal correcta del voseo rioplatense para el presente de indicativo del verbo 'saber'?",
                "options": [
                    "Vos sabés",
                    "Vos sabes",
                    "Vos sabís",
                    "Vos sepás"
                ],
                "correct": 0,
                "teaches": ["voseo-rioplatense-reconocimiento"]
            },
            {
                "id": "b2-argentinaba-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Si querés comprender la historia de los inmigrantes en La Boca, __ al antiguo conventillo de la calle Garibaldi.",
                "answer": "andá",
                "english": "If you want to understand the history of immigrants in La Boca, go to the old tenement on Garibaldi Street.",
                "teaches": ["voseo-rioplatense-reconocimiento"]
            },
            {
                "id": "b2-argentinaba-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Decime", "la", "verdad", "sobre", "las", "condiciones", "en", "el", "inquilinato."],
                "solution": ["Decime", "la", "verdad", "sobre", "las", "condiciones", "en", "el", "inquilinato."],
                "english": "Tell me the truth about the conditions in the tenement house.",
                "teaches": ["voseo-rioplatense-reconocimiento"]
            },
            {
                "id": "b2-argentinaba-02.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["conventillo", "tenement boarding house"],
                    ["cocoliche", "Italian-Spanish immigrant hybrid dialect"],
                    ["inquilinato", "tenement housing system"],
                    ["crisol", "melting pot / crucible"],
                    ["chapa", "corrugated sheet metal"]
                ],
                "teaches": ["b2-argentinaba-vocab"]
            },
            {
                "id": "b2-argentinaba-02.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Mateo", "text": "¿Tenés tiempo de revisar los documentos de desembarco de mi abuelo?"},
                    {"speaker": "Sofía", "text": "Claro, pasámelos ahora mismo; __ que me apasiona la historia familiar."}
                ],
                "options": [
                    "vos sabés",
                    "tú sabes",
                    "usted sabe",
                    "vosotros sabéis"
                ],
                "correct": 0,
                "teaches": ["voseo-rioplatense-reconocimiento"]
            },
            {
                "id": "b2-argentinaba-02.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Mirá con atención las cartas que los obreros enviaban a sus familias en Génova y Nápoles.",
                "english": "Look carefully at the letters that the workers sent to their families in Genoa and Naples.",
                "teaches": ["voseo-rioplatense-reconocimiento"]
            }
        ]
    })

    # b2-argentinaba-03-ex.json (participios absolutos narrativos)
    write_json("exercises/b2/b2-argentinaba-03-ex.json", {
        "lesson": "b2-argentinaba-03",
        "exercises": [
            {
                "id": "b2-argentinaba-03.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la estructura sintáctica de una cláusula de participio absoluto en el relato literario?",
                "options": [
                    "El participio encabeza la cláusula y concuerda en género y número con su propio sustantivo.",
                    "El verbo conjugado en subjuntivo exige un conector subordinante causal obligatorio.",
                    "El participio permanece invariable en masculino singular independientemente del sujeto.",
                    "Se forma exclusivamente con verbos auxiliares modales en tiempo condicional."
                ],
                "correct": 0,
                "teaches": ["participios-absolutos-narrativos"]
            },
            {
                "id": "b2-argentinaba-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "__ los acordes finales del bandoneón, los bailarines permanecieron inmóviles bajo el foco tenue.",
                "answer": "Extinguidos",
                "english": "Once the final chords of the bandoneon were extinguished, the dancers remained motionless under the dim spotlight.",
                "teaches": ["participios-absolutos-narrativos"]
            },
            {
                "id": "b2-argentinaba-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Concluida", "la", "milonga", "los", "músicos", "guardaron", "los", "bandoneones", "en", "sus", "fundas."],
                "solution": ["Concluida", "la", "milonga", "los", "músicos", "guardaron", "los", "bandoneones", "en", "sus", "fundas."],
                "english": "The milonga concluded, the musicians stored the bandoneons in their cases.",
                "teaches": ["participios-absolutos-narrativos"]
            },
            {
                "id": "b2-argentinaba-03.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["arrabal", "outskirts / suburban underworld quarter"],
                    ["bandoneón", "bandoneon accordion"],
                    ["lunfardo", "Buenos Aires slang argot"],
                    ["compadrito", "dandy tango tough guy / street swaggerer"],
                    ["fuelle", "bellows / bandoneon (slang)"]
                ],
                "teaches": ["b2-argentinaba-vocab"]
            },
            {
                "id": "b2-argentinaba-03.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Locutor", "text": "¿Cuándo se autorizó la gira internacional de la orquesta típica?"},
                    {"speaker": "Historiador", "text": "__ las diferencias contractuales, el elenco partió rumbo a París."}
                ],
                "options": [
                    "Subsanadas",
                    "A pesar de",
                    "Dado que",
                    "Por cuanto"
                ],
                "correct": 0,
                "teaches": ["participios-absolutos-narrativos"]
            },
            {
                "id": "b2-argentinaba-03.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Afinado el fuelle del bandoneón, el maestro arrancó con los primeros compases del tango.",
                "english": "With the bellows of the bandoneon tuned, the maestro launched into the first bars of the tango.",
                "teaches": ["participios-absolutos-narrativos"]
            }
        ]
    })

    # b2-argentinaba-04-ex.json (marcadores de reflexión intelectual)
    write_json("exercises/b2/b2-argentinaba-04-ex.json", {
        "lesson": "b2-argentinaba-04",
        "exercises": [
            {
                "id": "b2-argentinaba-04.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué marcador discursivo es más idóneo para introducir una consideración analítica destacada en un ensayo?",
                "options": [
                    "Cabe señalar que",
                    "O sea que",
                    "Total que",
                    "De buenas a primeras"
                ],
                "correct": 0,
                "teaches": ["marcadores-reflexion-intelectual"]
            },
            {
                "id": "b2-argentinaba-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "__ destacar que la tertulia de cafetín cumplió el rol de una verdadera asamblea cívica en la metrópolis.",
                "answer": "Es menester",
                "english": "It is necessary to highlight that the café salon fulfilled the role of a true civic assembly in the metropolis.",
                "teaches": ["marcadores-reflexion-intelectual"]
            },
            {
                "id": "b2-argentinaba-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["En", "lo", "que", "atañe", "al", "psicoanálisis", "Buenos", "Aires", "posee", "una", "vitalidad", "incomparable."],
                "solution": ["En", "lo", "que", "atañe", "al", "psicoanálisis", "Buenos", "Aires", "posee", "una", "vitalidad", "incomparable."],
                "english": "As far as psychoanalysis is concerned, Buenos Aires possesses an incomparable vitality.",
                "teaches": ["marcadores-reflexion-intelectual"]
            },
            {
                "id": "b2-argentinaba-04.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["psicoanálisis", "psychoanalysis"],
                    ["tertulia", "literary gathering / café discussion group"],
                    ["diván", "psychoanalytic couch / divan"],
                    ["cafetín", "traditional small Buenos Aires café"],
                    ["introspección", "introspection"]
                ],
                "teaches": ["b2-argentinaba-vocab"]
            },
            {
                "id": "b2-argentinaba-04.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Profesor", "text": "¿Toda la literatura nocturna de Corrientes responde a la evasión bohemia?"},
                    {"speaker": "Alumna", "text": "No exactamente; __ que muchos autores producían allí su crítica social más rigurosa."}
                ],
                "options": [
                    "convendría matizar",
                    "sale sobrando",
                    "da lo mismo",
                    "se viene abajo"
                ],
                "correct": 0,
                "teaches": ["marcadores-reflexion-intelectual"]
            },
            {
                "id": "b2-argentinaba-04.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Resulta evidente que el debate filosófico nocturno moldeó la identidad intelectual de la ciudad.",
                "english": "It is evident that nocturnal philosophical debate shaped the intellectual identity of the city.",
                "teaches": ["marcadores-reflexion-intelectual"]
            }
        ]
    })

    # b2-argentinaba-05-ex.json (estructuras conjeturales metafísicas)
    write_json("exercises/b2/b2-argentinaba-05-ex.json", {
        "lesson": "b2-argentinaba-05",
        "exercises": [
            {
                "id": "b2-argentinaba-05.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué modo y tiempo verbal exige la conjunción hipotética-comparativa 'como si'?",
                "options": [
                    "Subjuntivo (imperfecto o pluscuamperfecto)",
                    "Indicativo (presente o pretérito indefinido)",
                    "Condicional simple o compuesto",
                    "Infinitivo compuesto con preposición"
                ],
                "correct": 0,
                "teaches": ["estructuras-conjeturales-metafisicas"]
            },
            {
                "id": "b2-argentinaba-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Borges contemplaba los espejos del zaguán como si en su azogue se __ multiplicado el infinito.",
                "answer": "hubiera",
                "english": "Borges contemplated the hallway mirrors as if infinity had been multiplied in their quicksilver.",
                "teaches": ["estructuras-conjeturales-metafisicas"]
            },
            {
                "id": "b2-argentinaba-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Cabría", "conjeturar", "que", "el", "laberinto", "era", "una", "metáfora", "del", "tiempo."],
                "solution": ["Cabría", "conjeturar", "que", "el", "laberinto", "era", "una", "metáfora", "del", "tiempo."],
                "english": "One might conjecture that the labyrinth was a metaphor for time.",
                "teaches": ["estructuras-conjeturales-metafisicas"]
            },
            {
                "id": "b2-argentinaba-05.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["laberinto", "labyrinth / maze"],
                    ["metafísica", "metaphysics"],
                    ["bifurcación", "bifurcation / branching path"],
                    ["azar", "chance / fate"],
                    ["cronopio", "playful nonconformist character (Cortázar)"]
                ],
                "teaches": ["b2-argentinaba-vocab"]
            },
            {
                "id": "b2-argentinaba-05.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Crítico", "text": "¿Cómo describe el narrador la vivencia del tiempo en Rayuela?"},
                    {"speaker": "Ensayista", "text": "El protagonista recorre París __ los instantes no obedecieran al orden cronológico."}
                ],
                "options": [
                    "como si",
                    "en tanto que",
                    "a condición de que",
                    "por temor a que"
                ],
                "correct": 0,
                "teaches": ["estructuras-conjeturales-metafisicas"]
            },
            {
                "id": "b2-argentinaba-05.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Pareciera ser que los relatos de Borges desafían para siempre nuestra noción de realidad.",
                "english": "It would seem that Borges's stories challenge our notion of reality forever.",
                "teaches": ["estructuras-conjeturales-metafisicas"]
            }
        ]
    })

    # b2-argentinaba-consolidation-ex.json (8 exercises: integration of regional topics)
    write_json("exercises/b2/b2-argentinaba-consolidation-ex.json", {
        "lesson": "b2-argentinaba-consolidation",
        "exercises": [
            {
                "id": "b2-argentinaba-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo sintáctico caracteriza a las construcciones de participio absoluto en descripciones literarias?",
                "options": [
                    "Aparecen separadas por comas, concuerdan con su propio sustantivo y prescinden de nexo subordinante.",
                    "Requieren invariablemente la presencia de un pronombre relativo explicativo.",
                    "Deben conjugarse siempre en tiempo presente del modo subjuntivo.",
                    "Sustituyen obligatoriamente a todas las oraciones concesivas con 'aunque'."
                ],
                "correct": 0,
                "teaches": ["participios-absolutos-narrativos"]
            },
            {
                "id": "b2-argentinaba-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Caminaba por la Costanera Norte __ las olas del Río de la Plata le susurraran historias del antiguo puerto.",
                "answer": "como si",
                "english": "He walked along the Costanera Norte as if the waves of the Río de la Plata were whispering stories of the ancient port to him.",
                "teaches": ["estructuras-conjeturales-metafisicas"]
            },
            {
                "id": "b2-argentinaba-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "lo", "largo", "del", "Riachuelo", "se", "afincaron", "los", "primeros", "inmigrantes", "genoveses."],
                "solution": ["A", "lo", "largo", "del", "Riachuelo", "se", "afincaron", "los", "primeros", "inmigrantes", "genoveses."],
                "english": "Along the Riachuelo settled the first Genoese immigrants.",
                "teaches": ["locuciones-prepositivas-espaciales"]
            },
            {
                "id": "b2-argentinaba-consolidation.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["conventillo", "tenement boarding house"],
                    ["bandoneón", "bandoneon accordion"],
                    ["cocoliche", "Italian-Spanish immigrant hybrid dialect"],
                    ["tertulia", "literary gathering / café discussion group"],
                    ["laberinto", "labyrinth / maze"]
                ],
                "teaches": ["b2-argentinaba-vocab"]
            },
            {
                "id": "b2-argentinaba-consolidation.ex05",
                "type": "dialogue-complete",
                "category": "grammar",
                "prompt": [
                    {"speaker": "Turista", "text": "¿Cómo puedo llegar a la librería El Ateneo Grand Splendid?"},
                    {"speaker": "Porteño", "text": "__ por Santa Fe unas cuatro cuadras y la vas a ver enseguida sobre mano derecha."}
                ],
                "options": [
                    "Caminá",
                    "Camines",
                    "Caminarías",
                    "Caminaste"
                ],
                "correct": 0,
                "teaches": ["voseo-rioplatense-reconocimiento"]
            },
            {
                "id": "b2-argentinaba-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el marcador 'cabe señalar que' en un texto argumentativo formal?",
                "options": [
                    "Introduce una observación analítica relevante con rigor crítico y distanciamiento.",
                    "Expresa un desacuerdo violento e irreparable entre los interlocutores.",
                    "Pide disculpas formales por un error ortográfico en el manuscrito.",
                    "Concluye abruptamente una disertación sin admitir preguntas del auditorio."
                ],
                "correct": 0,
                "teaches": ["marcadores-reflexion-intelectual"]
            },
            {
                "id": "b2-argentinaba-consolidation.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Concluida la función de ópera, el público colmaba las mesas del café para debatir la interpretación.",
                "english": "The opera performance concluded, the audience filled the café tables to debate the interpretation.",
                "teaches": ["participios-absolutos-narrativos"]
            },
            {
                "id": "b2-argentinaba-consolidation.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "__ inferir que la identidad porteña se cimentó sobre la confluencia fecunda de múltiples tradiciones inmigrantes.",
                "answer": "Cabría",
                "english": "One might infer that porteño identity was built upon the fruitful confluence of multiple immigrant traditions.",
                "teaches": ["estructuras-conjeturales-metafisicas"]
            }
        ]
    })

    # 7. Lessons (12 files)
    # Core Lessons
    core_lessons = [
        ("b2-24-01", "Durative Periphrasis: Llevar + Gerundio", "b2-24-01-a-gr", "b2-24-01-voc", "b2-24-01-ex"),
        ("b2-24-02", "Continuity Periphrasis: Seguir + Gerundio", "b2-24-02-a-gr", "b2-24-02-voc", "b2-24-02-ex"),
        ("b2-24-03", "Progressive Periphrasis: Ir + Gerundio", "b2-24-03-a-gr", "b2-24-03-voc", "b2-24-03-ex"),
        ("b2-24-04", "Progressive Periphrasis: Andar + Gerundio", "b2-24-04-a-gr", "b2-24-04-voc", "b2-24-04-ex"),
        ("b2-24-05", "Cumulative Periphrasis: Venir + Gerundio", "b2-24-05-a-gr", "b2-24-05-voc", "b2-24-05-ex")
    ]

    for stem, title, gr_stem, voc_stem, ex_stem in core_lessons:
        write_json(f"lessons/b2/{stem}.json", {
            "id": f"lesson.{stem.replace('-', '.')}",
            "title": title,
            "level": "B2",
            "sections": [
                {"type": "grammar", "ref": f"grammar/b2/{gr_stem}.json"},
                {"type": "vocabulary", "ref": f"vocabulary/b2/{voc_stem}.json"},
                {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{ex_stem}.json", "exerciseRefs": [f"{stem}.ex0{i}" for i in range(1, 7)]}
            ]
        })

    # Core Consolidation
    write_json("lessons/b2/b2-24-consolidation.json", {
        "id": "lesson.b2.24.consolidation",
        "title": "Consolidación: Perífrasis durativas y de continuidad",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Dominar los contrastes aspectuales de las perífrasis durativas (llevar, seguir, ir, andar, venir + gerundio).",
                "Integrar el léxico formal de continuidad, persistencia, gradualidad y decurso temporal.",
                "Analizar textos literarios complejos a partir de la adaptación de Roberto Arlt."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/classics/b2/b2-24.json"},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-24-consolidation-ex.json", "exerciseRefs": [f"b2-24-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Distingo con precisión los valores de llevar, seguir, ir, andar y venir con gerundio.",
                "Puedo expresar duración ininterrumpida y persistencia activa con soltura en registro formal.",
                "Comprendo la prosa psicológica y social de la novela clásica porteña de Roberto Arlt.",
                "Utilizo adecuadamente el vocabulario sobre trayectorias, afianzamiento y procesos acumulativos.",
                "Aplico matices aspectuales sutiles en la argumentación escrita de nivel B2."
            ]}
        ]
    })

    # Regional Lessons: b2-argentinaba
    regional_lessons = [
        ("b2-argentinaba-01", "El Río de la Plata y el trazado de la reina del Plata", "b2-argentinaba-01-a-gr", "b2-argentinaba-01-voc", "b2-argentinaba-01-ex", "stories/world/b2/b2-argentinaba-01.json"),
        ("b2-argentinaba-02", "La gran ola inmigratoria: Italianos, españoles y el cocoliche", "b2-argentinaba-02-a-gr", "b2-argentinaba-02-voc", "b2-argentinaba-02-ex", "stories/world/b2/b2-argentinaba-02.json"),
        ("b2-argentinaba-03", "El tango: De los arrabales marginales a los salones del mundo", "b2-argentinaba-03-a-gr", "b2-argentinaba-03-voc", "b2-argentinaba-03-ex", "stories/world/b2/b2-argentinaba-03.json"),
        ("b2-argentinaba-04", "La pasión por el psicoanálisis, los cafés y las librerías", "b2-argentinaba-04-a-gr", "b2-argentinaba-04-voc", "b2-argentinaba-04-ex", "stories/world/b2/b2-argentinaba-04.json"),
        ("b2-argentinaba-05", "Jorge Luis Borges, Julio Cortázar y la literatura fantástica", "b2-argentinaba-05-a-gr", "b2-argentinaba-05-voc", "b2-argentinaba-05-ex", "stories/world/b2/b2-argentinaba-05.json")
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
    write_json("lessons/b2/b2-argentinaba-consolidation.json", {
        "id": "lesson.b2.argentinaba.consolidation",
        "title": "Consolidación: El laberinto porteño",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Integrar la visión histórica, urbana y cultural de Buenos Aires como metrópolis cosmopolita.",
                "Consolidar el léxico especializado del tango, la inmigración, el psicoanálisis y la literatura fantástica.",
                "Articular análisis críticos sobre la identidad porteña, el voseo y las vanguardias estéticas."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b2/b2-argentinaba-consolidation.json"},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-argentinaba-consolidation-ex.json", "exerciseRefs": [f"b2-argentinaba-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la evolución urbanística de Buenos Aires desde el estuario hasta Puerto Madero.",
                "Reconozco el impacto cultural y lingüístico de la inmigración masiva y el cocoliche.",
                "Analizo la trascendencia del tango y la poesía lunfarda en la identidad argentina.",
                "Identifico el papel del psicoanálisis, los cafetines históricos y las librerías en la vida cívica.",
                "Interpreto con soltura las estructuras conjeturales y metafísicas de Borges y Cortázar."
            ]}
        ]
    })

    print("Completed LatAm Unit 24 (Argentina I: Buenos Aires) generation!")

    # 8. Update curriculum/units/b2.json
    def update_b2_units(units):
        existing_stems = set()
        for u in units:
            for s in u.get("stems", []):
                existing_stems.add(s)

        unit_core_24 = {
            "title": "Durative & Progressive Periphrases",
            "stems": [
                "b2-24-01",
                "b2-24-02",
                "b2-24-03",
                "b2-24-04",
                "b2-24-05",
                "b2-24-consolidation"
            ],
            "track": "core"
        }

        unit_regional_24 = {
            "title": "Argentina I: Buenos Aires, Tango & Porteño Culture",
            "stems": [
                "b2-argentinaba-01",
                "b2-argentinaba-02",
                "b2-argentinaba-03",
                "b2-argentinaba-04",
                "b2-argentinaba-05",
                "b2-argentinaba-consolidation"
            ],
            "track": "regional"
        }

        if "b2-24-01" not in existing_stems:
            units.append(unit_core_24)
        if "b2-argentinaba-01" not in existing_stems:
            units.append(unit_regional_24)
        return units

    update_json_file(os.path.join(LATAM_DIR, "curriculum", "units", "b2.json"), update_b2_units)
    print("Updated curriculum/units/b2.json with Unit 24!")

    assert all_ok, "Some stories are out of the 650-825 word count bounds!"

if __name__ == "__main__":
    main()
