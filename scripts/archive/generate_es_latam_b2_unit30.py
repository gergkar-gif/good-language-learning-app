# -*- coding: utf-8 -*-
"""
Generator script for Latin American Spanish (es-latam) B2 Unit 30:
- Core B2: b2-30 (Discourse Markers III: Contrast & Restriction)
- Regional B2: b2-brasilnordeste (Brazil II: The Northeast, Afro-Brazilian Soul & The Sertão)
- Classic Literature Adaptation: Euclides da Cunha - Los sertones (Os Sertões, 1902)
"""

import os
import json
import re

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
            "marcadores-contraste-adversativo": {
                "kind": "grammar",
                "name": "marcadores-contraste-adversativo",
                "description": "Adversative contrast discourse markers such as sin embargo, no obstante, con todo in formal prose",
                "aliases": []
            },
            "marcadores-contraste-exclusivo": {
                "kind": "grammar",
                "name": "marcadores-contraste-exclusivo",
                "description": "Exclusive and substitutive contrast markers including por el contrario, al contrario, antes bien",
                "aliases": []
            },
            "marcadores-restriccion-concesiva": {
                "kind": "grammar",
                "name": "marcadores-restriccion-concesiva",
                "description": "Concessive restriction discourse markers such as ahora bien, eso sí, bien es verdad que",
                "aliases": []
            },
            "marcadores-contraposicion-ponderada": {
                "kind": "grammar",
                "name": "marcadores-contraposicion-ponderada",
                "description": "Counter-balanced contrastive discourse markers including en cambio, en contrapartida, por contra",
                "aliases": []
            },
            "marcadores-oposicion-atenuada": {
                "kind": "grammar",
                "name": "marcadores-oposicion-atenuada",
                "description": "Attenuated opposition and restrictive markers such as si bien, pese a ello, aun con todo",
                "aliases": []
            },
            "b2-30-vocab": {
                "kind": "vocabulary",
                "name": "b2-30-vocab",
                "description": "Vocabulary for polemics, adversity, contrastive argumentation, and debate",
                "aliases": []
            },
            "nordeste-adjetivacion-estilo": {
                "kind": "grammar",
                "name": "nordeste-adjetivacion-estilo",
                "description": "Expressive and evaluative adjectivization in cultural historiography and architectural description",
                "aliases": []
            },
            "nordeste-subordinadas-finales": {
                "kind": "grammar",
                "name": "nordeste-subordinadas-finales",
                "description": "Advanced purpose clauses in cultural anthropology with a fin de que, con el objeto de que",
                "aliases": []
            },
            "nordeste-condicionales-irreales": {
                "kind": "grammar",
                "name": "nordeste-condicionales-irreales",
                "description": "Counterfactual conditional structures in folk narratives and historical retrospection",
                "aliases": []
            },
            "nordeste-perifrasis-reiterativas": {
                "kind": "grammar",
                "name": "nordeste-perifrasis-reiterativas",
                "description": "Reiterative aspectual periphrases in liberation historiography including volver a, seguir + gerundio",
                "aliases": []
            },
            "nordeste-conectores-causales-complejos": {
                "kind": "grammar",
                "name": "nordeste-conectores-causales-complejos",
                "description": "Complex causal connectors in sociological debate such as habida cuenta de que, por cuanto",
                "aliases": []
            },
            "b2-brasilnordeste-vocab": {
                "kind": "vocabulary",
                "name": "b2-brasilnordeste-vocab",
                "description": "Vocabulary for the Brazilian Northeast, Afro-descendant soul, Candomblé, Sertão, and Quilombos",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 30")

    # 2. Update grammar-titles.json
    def update_grammar_titles(titles):
        new_titles = {
            "marcadores-contraste-adversativo": "adversative contrast discourse markers",
            "marcadores-contraste-exclusivo": "exclusive and substitutive contrast markers",
            "marcadores-restriccion-concesiva": "concessive restriction discourse markers",
            "marcadores-contraposicion-ponderada": "counterbalanced contrastive discourse markers",
            "marcadores-oposicion-atenuada": "attenuated opposition and restrictive markers",
            "nordeste-adjetivacion-estilo": "expressive and evaluative adjectivization in cultural historiography",
            "nordeste-subordinadas-finales": "advanced purpose clauses in cultural anthropology",
            "nordeste-condicionales-irreales": "counterfactual conditional structures in folk narratives",
            "nordeste-perifrasis-reiterativas": "reiterative aspectual periphrases in liberation historiography",
            "nordeste-conectores-causales-complejos": "complex causal connectors in sociological debate"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 30")

    # 3. Vocabulary files
    vocab_data = {
        "b2-30-01": {
            "id": "vocab.b2.30.01",
            "lesson": "b2-30-01",
            "title": "Adversative Contrast and Dialectical Tension",
            "words": [
                {"lemma": "antagonismo", "translation": "antagonism", "pos": "noun"},
                {"lemma": "irreconciliable", "translation": "irreconcilable", "pos": "adjective"},
                {"lemma": "contraponer", "translation": "to counterpose / contrast", "pos": "verb"},
                {"lemma": "discrepancia", "translation": "discrepancy / disagreement", "pos": "noun"},
                {"lemma": "paradoja", "translation": "paradox", "pos": "noun"},
                {"lemma": "contrapunto", "translation": "counterpoint", "pos": "noun"}
            ]
        },
        "b2-30-02": {
            "id": "vocab.b2.30.02",
            "lesson": "b2-30-02",
            "title": "Exclusive Contrast and Theoretical Refutation",
            "words": [
                {"lemma": "refutación", "translation": "refutation", "pos": "noun"},
                {"lemma": "incompatible", "translation": "incompatible", "pos": "adjective"},
                {"lemma": "desmentir", "translation": "to belie / refute", "pos": "verb"},
                {"lemma": "antítesis", "translation": "antithesis", "pos": "noun"},
                {"lemma": "excluyente", "translation": "exclusive", "pos": "adjective"},
                {"lemma": "impugnar", "translation": "to challenge / contest", "pos": "verb"}
            ]
        },
        "b2-30-03": {
            "id": "vocab.b2.30.03",
            "lesson": "b2-30-03",
            "title": "Concessive Restriction and Nuanced Concession",
            "words": [
                {"lemma": "condicionamiento", "translation": "conditioning / constraint", "pos": "noun"},
                {"lemma": "atenuante", "translation": "extenuating / mitigating", "pos": "adjective"},
                {"lemma": "matizar", "translation": "to nuance / qualify", "pos": "verb"},
                {"lemma": "salvedad", "translation": "caveat / reservation", "pos": "noun"},
                {"lemma": "concesión", "translation": "concession", "pos": "noun"},
                {"lemma": "restringir", "translation": "to restrict / qualify", "pos": "verb"}
            ]
        },
        "b2-30-04": {
            "id": "vocab.b2.30.04",
            "lesson": "b2-30-04",
            "title": "Counterbalanced Contrast and Symmetry",
            "words": [
                {"lemma": "asimetría", "translation": "asymmetry", "pos": "noun"},
                {"lemma": "compensación", "translation": "compensation / offset", "pos": "noun"},
                {"lemma": "equiparar", "translation": "to equate / compare", "pos": "verb"},
                {"lemma": "desequilibrio", "translation": "imbalance", "pos": "noun"},
                {"lemma": "antagónico", "translation": "antagonistic", "pos": "adjective"},
                {"lemma": "polaridad", "translation": "polarity", "pos": "noun"}
            ]
        },
        "b2-30-05": {
            "id": "vocab.b2.30.05",
            "lesson": "b2-30-05",
            "title": "Attenuated Opposition and Resilience",
            "words": [
                {"lemma": "tenacidad", "translation": "tenacity", "pos": "noun"},
                {"lemma": "indómito", "translation": "untamed / indomitable", "pos": "adjective"},
                {"lemma": "sobreponerse", "translation": "to overcome / surmount", "pos": "verb"},
                {"lemma": "adversidad", "translation": "adversity", "pos": "noun"},
                {"lemma": "inquebrantable", "translation": "unshakeable", "pos": "adjective"},
                {"lemma": "resiliencia", "translation": "resilience", "pos": "noun"}
            ]
        },
        "b2-brasilnordeste-01": {
            "id": "vocab.b2.brasilnordeste.01",
            "lesson": "b2-brasilnordeste-01",
            "title": "Salvador de Bahía and the Pelourinho",
            "words": [
                {"lemma": "barroco", "translation": "baroque", "pos": "adjective"},
                {"lemma": "azulejo", "translation": "glazed ceramic tile", "pos": "noun"},
                {"lemma": "caserón", "translation": "large mansion / manor house", "pos": "noun"},
                {"lemma": "ladera", "translation": "slope / hillside", "pos": "noun"},
                {"lemma": "adoquín", "translation": "cobblestone", "pos": "noun"},
                {"lemma": "suntuoso", "translation": "sumptuous / lavish", "pos": "adjective"}
            ]
        },
        "b2-brasilnordeste-02": {
            "id": "vocab.b2.brasilnordeste.02",
            "lesson": "b2-brasilnordeste-02",
            "title": "Candomblé, Capoeira and the Orixás",
            "words": [
                {"lemma": "sincretismo", "translation": "syncretism", "pos": "noun"},
                {"lemma": "orixá", "translation": "deity of Yoruba pantheon", "pos": "noun"},
                {"lemma": "terreiro", "translation": "sacred ceremonial temple", "pos": "noun"},
                {"lemma": "atabaque", "translation": "sacred hand drum", "pos": "noun"},
                {"lemma": "berimbau", "translation": "musical bow of capoeira", "pos": "noun"},
                {"lemma": "sagrado", "translation": "sacred", "pos": "adjective"}
            ]
        },
        "b2-brasilnordeste-03": {
            "id": "vocab.b2.brasilnordeste.03",
            "lesson": "b2-brasilnordeste-03",
            "title": "The Sertão, Cangaço and Cordel Literature",
            "words": [
                {"lemma": "caatinga", "translation": "semi-arid scrubland biome", "pos": "noun"},
                {"lemma": "cangaceiro", "translation": "bandit / folk outlaw of the sertão", "pos": "noun"},
                {"lemma": "cordel", "translation": "pamphlet string ballad", "pos": "noun"},
                {"lemma": "xilografía", "translation": "woodcut print", "pos": "noun"},
                {"lemma": "árido", "translation": "arid", "pos": "adjective"},
                {"lemma": "sequía", "translation": "drought", "pos": "noun"}
            ]
        },
        "b2-brasilnordeste-04": {
            "id": "vocab.b2.brasilnordeste.04",
            "lesson": "b2-brasilnordeste-04",
            "title": "Quilombo dos Palmares and Freedom",
            "words": [
                {"lemma": "quilombo", "translation": "free maroon settlement", "pos": "noun"},
                {"lemma": "cimarrón", "translation": "escaped slave / runaway", "pos": "noun"},
                {"lemma": "manumisión", "translation": "emancipation / manumission", "pos": "noun"},
                {"lemma": "asedio", "translation": "siege", "pos": "noun"},
                {"lemma": "insumiso", "translation": "unsubmissive / rebellious", "pos": "adjective"},
                {"lemma": "libertario", "translation": "libertarian / freedom-seeking", "pos": "adjective"}
            ]
        },
        "b2-brasilnordeste-05": {
            "id": "vocab.b2.brasilnordeste.05",
            "lesson": "b2-brasilnordeste-05",
            "title": "Racial Democracy and Affirmative Action",
            "words": [
                {"lemma": "desigualdad", "translation": "inequality", "pos": "noun"},
                {"lemma": "discriminación", "translation": "discrimination", "pos": "noun"},
                {"lemma": "afirmativo", "translation": "affirmative", "pos": "adjective"},
                {"lemma": "cuota", "translation": "quota / share", "pos": "noun"},
                {"lemma": "mestizaje", "translation": "miscegenation / cultural blend", "pos": "noun"},
                {"lemma": "estructural", "translation": "structural", "pos": "adjective"}
            ]
        }
    }

    for stem, vdata in vocab_data.items():
        write_json(f"vocabulary/b2/{stem}-voc.json", vdata)

    # 4. Grammar files
    grammar_data = {
        "b2-30-01-a-gr": {
            "id": "grammar.b2.30.01.marcadores-contraste-adversativo",
            "title": "Adversative Contrast Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de contraste adversativo introducen una objeción o limitación sustantiva respecto al enunciado anterior, sin llegar a anular su validez fundamental. En el nivel B2 formal, señalan la dialéctica entre premisas contrapuestas."
                },
                {
                    "type": "table",
                    "title": "Marcadores adversativos en el ensayo culto",
                    "rows": [
                        ["Las expediciones contaban con artillería pesada; sin embargo, no lograron quebrar el cerco.", "The expeditions had heavy artillery; however, they failed to break the siege."],
                        ["El terreno era árido y hostil; no obstante, los sertanejos resistieron con firmeza sobrehumana.", "The terrain was arid and hostile; nevertheless, the sertanejos resisted with superhuman firmness."],
                        ["Los rebeldes carecían de municiones modernas; con todo, rechazaron cuatro asaltos consecutivos.", "The rebels lacked modern ammunition; even so, they repelled four consecutive assaults."],
                        ["El ejército sufrió bajas cuantiosas; aun así, el general ordenó mantener la posición.", "The army suffered heavy casualties; even so, the general ordered the position maintained."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Sin embargo' y 'no obstante' exigen aislamiento ortográfico mediante comas, o bien punto y coma anterior y coma posterior cuando coordinan dos oraciones independientes."
                }
            ]
        },
        "b2-30-02-a-gr": {
            "id": "grammar.b2.30.02.marcadores-contraste-exclusivo",
            "title": "Exclusive & Substitutive Contrast Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de contraste exclusivo o sustitutivo refutan categóricamente la primera afirmación para imponer en su lugar la tesis opuesta y verdadera. Exigen que la primera proposición sea explícita o implícitamente negativa."
                },
                {
                    "type": "table",
                    "title": "Marcadores sustitutivos y de exclusión",
                    "rows": [
                        ["No capitularon ante las tropas regulares; por el contrario, lucharon hasta el último aliento.", "They did not surrender to regular troops; on the contrary, they fought until the last breath."],
                        ["El cangaço no fue un mero bandidaje común; al contrario, reflejó el abandono del Estado central.", "The cangaço was not mere common banditry; on the contrary, it reflected neglect by the central State."],
                        ["No se trataba de una masa fanatizada y ciega; antes bien, era un pueblo desposeído que defendía su tierra.", "It was not a fanatical and blind mob; rather, it was a dispossessed people defending their land."],
                        ["El conflicto no pacificó el interior; muy al contrario, profundizó las heridas sociales durante décadas.", "The conflict did not pacify the interior; quite the contrary, it deepened social wounds for decades."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Antes bien' es propio de la prosa ensayística y académica de alto registro. Se utiliza siempre tras una negación categórica previa: 'No pretendía la sumisión; antes bien, reclamaba la libertad'."
                }
            ]
        },
        "b2-30-03-a-gr": {
            "id": "grammar.b2.30.03.marcadores-restriccion-concesiva",
            "title": "Concessive Restriction Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de restricción concesiva aceptan provisionalmente una premisa pero introducen de inmediato una condición, matiz o salvedad que limita su alcance práctico. Permiten mantener un juicio ponderado y objetivo."
                },
                {
                    "type": "table",
                    "title": "Marcadores de restricción y salvedad",
                    "rows": [
                        ["La república proclamó la igualdad de todos los ciudadanos; ahora bien, mantuvo la exclusión rural.", "The republic proclaimed equality for all citizens; now then, it maintained rural exclusion."],
                        ["El gobierno abolió formalmente la esclavitud; eso sí, sin garantizar tierras ni educación a los libertos.", "The government formally abolished slavery; mind you, without guaranteeing land or education to freedmen."],
                        ["Bien es verdad que se lograron avances legislativos; con todo, la desigualdad estructural perdura.", "It is indeed true that legislative progress was achieved; nonetheless, structural inequality endures."],
                        ["La victoria militar fue incontestable; si bien se pagó con un costo ético demoledor para el país.", "The military victory was undeniable; although it was paid with a devastating ethical cost for the country."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Eso sí' introduce una precisión restrictiva en registros ensayísticos ágiles o periodismo culto, marcando un contrapunto que no anula lo elogiado con anterioridad."
                }
            ]
        },
        "b2-30-04-a-gr": {
            "id": "grammar.b2.30.04.marcadores-contraposicion-ponderada",
            "title": "Counterbalanced Contrastive Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de contraposición ponderada distribuyen dos elementos simétricos en una relación de contrapeso o balanza, destacando las divergencias entre dos regiones, clases sociales o modelos económicos."
                },
                {
                    "type": "table",
                    "title": "Conectores de contraposición ponderada",
                    "rows": [
                        ["El litoral nordestino se enriqueció con la caña de azúcar; en cambio, el sertão vivió en la escasez hídrica.", "The northeastern coast grew rich from sugar cane; in contrast, the sertão lived in water scarcity."],
                        ["Los hacendados contaban con el favor de los jueces; en contrapartida, los campesinos carecían de títulos.", "Landowners enjoyed the favor of judges; conversely, peasants lacked land titles."],
                        ["La capital colonial deslumbraba con iglesias doradas; por contra, las aldeas rurales vivían en el abandono.", "The colonial capital dazzled with gilded churches; conversely, rural villages lived in neglect."],
                        ["Unos abogaban por la represión armada implacable; otros, en cambio, exigían una reforma agraria profunda.", "Some advocated relentless armed repression; others, by contrast, demanded deep agrarian reform."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'En cambio' puede situarse al principio de la proposición o en posición intermedia entre comas: 'Los campesinos, en cambio, carecían de armas'."
                }
            ]
        },
        "b2-30-05-a-gr": {
            "id": "grammar.b2.30.05.marcadores-oposicion-atenuada",
            "title": "Attenuated Opposition & Restrictive Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de oposición atenuada suavizan la fricción entre enunciados contrarios, subrayando la perseverancia del sujeto a pesar de los obstáculos objetivos. Son habituales en la prosa historiográfica épica."
                },
                {
                    "type": "table",
                    "title": "Oposición atenuada y resiliencia",
                    "rows": [
                        ["Pese a ello, las familias campesinas retornaron a sus tierras calcinadas tras la contienda.", "Despite this, peasant families returned to their scorched lands after the conflict."],
                        ["Aun con todo el sufrimiento padecido, la cultura popular nordestina conservó su vigor.", "Even with all the suffering endured, northeastern popular culture retained its vigor."],
                        ["Si bien la sequía diezmaba las cosechas, los poetas de cordel cantaban la dignidad de la vida.", "Although drought decimated harvests, string-ballad poets sang of the dignity of life."],
                        ["No obstante las derrotas iniciales, el líder cimarrón sostuvo la resistencia durante décadas.", "Notwithstanding initial defeats, the maroon leader sustained resistance for decades."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Pese a ello' y 'aun con todo' sintetizan anafóricamente toda una serie de infortunios previos para introducir la respuesta de superación o entereza."
                }
            ]
        },
        "b2-brasilnordeste-01-a-gr": {
            "id": "grammar.b2.brasilnordeste.01.nordeste-adjetivacion-estilo",
            "title": "Expressive & Evaluative Adjectivization in Historiography",
            "sections": [
                {
                    "type": "text",
                    "content": "La caracterización arquitectónica y cultural de enclaves coloniales como Salvador de Bahía requiere una adjetivación estilística refinada que combine la precisión técnica del arte barroco con la evocación sensorial del mestizaje."
                },
                {
                    "type": "table",
                    "title": "Adjetivación descriptiva y valorativa",
                    "rows": [
                        ["La iglesia de San Francisco exhibe una suntuosa decoración dorada de talla exuberante.", "The church of Saint Francis exhibits sumptuous gilded decoration of exuberant carving."],
                        ["Las fachadas señoriales del Pelourinho conservan una pátina policromada centenaria.", "The noble facades of Pelourinho preserve an ancient polychrome patina."],
                        ["Las callejuelas empinadas de piedra irregular descienden hacia la luminosa bahía.", "The steep alleys of irregular cobblestone descend toward the luminous bay."],
                        ["El patrimonio arquitectónico bahiano refleja un diálogo sincrético entre Europa y África.", "Bahian architectural heritage reflects a syncretic dialogue between Europe and Africa."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Posición del adjetivo: el adjetivo antepuesto al sustantivo ('suntuosa decoración') enfatiza la apreciación subjetiva y literaria, mientras que pospuesto ('decoración dorada') delimita un rasgo objetivo."
                }
            ]
        },
        "b2-brasilnordeste-02-a-gr": {
            "id": "grammar.b2.brasilnordeste.02.nordeste-subordinadas-finales",
            "title": "Advanced Purpose Clauses in Cultural Anthropology",
            "sections": [
                {
                    "type": "text",
                    "content": "Las oraciones subordinadas finales explican la intencionalidad sagrada, comunitaria o ritual de las prácticas afrobrasileñas. En nivel B2, se introducen mediante nexos formales que rigen obligatoriamente modo subjuntivo."
                },
                {
                    "type": "table",
                    "title": "Nexos finales con modo subjuntivo",
                    "rows": [
                        ["Los sacerdotes invocan a los orixás a fin de que desciendan a bendecir el terreiro sagrado.", "The priests invoke the orixás so that they may descend to bless the sacred terreiro."],
                        ["Los capoeiristas disimularon la lucha como danza con el objeto de que los amos no la prohibieran.", "Capoeiristas disguised fighting as dance so that masters would not prohibit it."],
                        ["Se comparten ofrendas de acarajé para que la comunidad renueve sus lazos espirituales.", "Offerings of acarajé are shared so that the community may renew its spiritual bonds."],
                        ["Consagran los tambores con miras a que su sonido puro resuene con fuerza espiritual.", "They consecrate the drums with a view to their pure sound resonating with spiritual power."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'A fin de que' y 'con el objeto de que' exigen SIEMPRE subjuntivo (presente o imperfecto según la correlación de tiempos verbales): 'a fin de que desciendan' (presente), 'con el objeto de que no la prohibieran' (imperfecto)."
                }
            ]
        },
        "b2-brasilnordeste-03-a-gr": {
            "id": "grammar.b2.brasilnordeste.03.nordeste-condicionales-irreales",
            "title": "Counterfactual Conditional Structures in Folk Narratives",
            "sections": [
                {
                    "type": "text",
                    "content": "Las oraciones condicionales irreales o contrafácticas reconstruyen hipótesis sobre el pasado que no llegaron a cumplirse, permitiendo evaluar las disyuntivas trágicas del campesinado en las guerras del Sertão."
                },
                {
                    "type": "table",
                    "title": "Estructuras condicionales de hipótesis irreal en el pasado",
                    "rows": [
                        ["De haber llovido a tiempo en la caatinga, miles de familias no habrían emigrado hacia la costa.", "Had it rained in time in the caatinga, thousands of families would not have migrated to the coast."],
                        ["Si el gobierno hubiera atendido los reclamos agrarios, no se habría desatado la tragedia de Canudos.", "If the government had addressed agrarian grievances, the tragedy of Canudos would not have erupted."],
                        ["Si Lampião no hubiera contado con el apoyo campesino, no habría resistido dos décadas en el monte.", "If Lampião had not relied on peasant support, he would not have held out for two decades in the scrub."],
                        ["De no haber existido la literatura de cordel, muchas epopeyas orales se habrían extinguido.", "Had cordel literature not existed, many oral sagas would have been extinguished."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "La fórmula 'De + infinitivo compuesto' ('De haber llovido') equivale exactamente a la prótasis con subjuntivo pluscuamperfecto ('Si hubiera llovido'), confiriendo una gran elegancia a la prosa histórica."
                }
            ]
        },
        "b2-brasilnordeste-04-a-gr": {
            "id": "grammar.b2.brasilnordeste.04.nordeste-perifrasis-reiterativas",
            "title": "Reiterative Aspectual Periphrases in Liberation History",
            "sections": [
                {
                    "type": "text",
                    "content": "Las perífrasis verbales de aspecto reiterativo y continuativo expresan la persistencia indomable de la lucha contra la opresión esclavista. Describen acciones que se repiten una y otra vez a lo largo de los siglos."
                },
                {
                    "type": "table",
                    "title": "Perífrasis aspectuales de repetición y continuidad",
                    "rows": [
                        ["Los cimarrones volvieron a fundar sus aldeas libres tras cada expedición de asedio colonial.", "The runaways founded their free villages anew after each colonial siege expedition."],
                        ["Las comunidades afrobrasileñas siguen reivindicando con orgullo la memoria heroica de Zumbi.", "Afro-Brazilian communities continue proudly claiming the heroic memory of Zumbi."],
                        ["A pesar de los incendios, la fortaleza de Palmares volvió a levantarse en la cima de la sierra.", "Despite the fires, the fortress of Palmares rose up again on the summit of the mountain range."],
                        ["Los historiadores continúan investigando los archivos coloniales para documentar la resistencia.", "Historians continue investigating colonial archives to document the resistance."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Volver a + infinitivo' denota la repetición del acto tras una interrupción temporal, mientras que 'seguir + gerundio' subraya la continuidad ininterrumpida del proceso en el tiempo."
                }
            ]
        },
        "b2-brasilnordeste-05-a-gr": {
            "id": "grammar.b2.brasilnordeste.05.nordeste-conectores-causales-complejos",
            "title": "Complex Causal Connectors in Sociological Debate",
            "sections": [
                {
                    "type": "text",
                    "content": "El debate sociológico riguroso sobre las desigualdades étnicas y raciales requiere conectores causales complejos de registro culto que articulen las razones estructurales que fundamentan las políticas públicas afirmativas."
                },
                {
                    "type": "table",
                    "title": "Conectores causales formales en el debate social",
                    "rows": [
                        ["Se aprobaron cuotas universitarias, habida cuenta de que persistían barreras de acceso históricas.", "University quotas were approved, taking into account that historic access barriers persisted."],
                        ["El mito de la democracia racial fue impugnado por cuanto invisibilizaba la exclusión social.", "The myth of racial democracy was challenged inasmuch as it rendered social exclusion invisible."],
                        ["El Estado promovió becas inclusivas en razón de que la equidad exige acciones reparadoras.", "The State promoted inclusive scholarships on the grounds that equity demands reparative actions."],
                        ["Dada la gravedad de las disparidades territoriales, se triplicaron las partidas presupuestarias.", "Given the severity of territorial disparities, budgetary allocations were tripled."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Habida cuenta de que' y 'por cuanto' pertenecen a la prosa jurídica y sociológica de nivel superior. 'Por cuanto' introduce una causa explicativa justificativa similar a 'puesto que'."
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}.json", gdata)

    # 5. Stories
    # Classic story: Euclides da Cunha - Los sertones (Os Sertões, 1902) (b2-30.json)
    # Regional stories: b2-brasilnordeste-01 to 05, b2-brasilnordeste-consolidation, b2-brasilnordeste.json
    # All texts strictly verified in [650, 825] words!

    stories = {
        "classics/b2/b2-30": {
            "id": "b2-30",
            "title": "Euclides da Cunha: Los sertones",
            "level": "B2",
            "lesson": 30,
            "type": "classics",
            "estimatedMinutes": 8,
            "summary": "Adaptación pedagógica de la monumental obra de Euclides da Cunha: la geografía calcinada del sertão baiano, la figura carismática y mesiánica de Antônio Conselheiro, la fundación de la ciudadela rebelde de Canudos y la trágica resistencia campesina frente al ejército republicano.",
            "characters": [
                "Euclides da Cunha (corresponsal y testigo científico de la campaña)",
                "Antônio Conselheiro (el predicador peregrino y guía espiritual)",
                "Pajeú y João Abade (valientes comandantes defensores de Canudos)",
                "Soldados del ejército regular y campesinos sertanejos"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "En las profundidades calcinadas del nordeste de Bahía, donde la tierra arcillosa y cuarteada por las sequías parece rechazar la vida bajo el azote implacable del sol tropical, la naturaleza forjó un escenario de belleza agreste y desolación cósmica: la caatinga. En primer término, el ingeniero y periodista militar Euclides da Cunha estructura su investigación dividiendo su magna obra en tres partes dialécticas e inseparables, a saber: la tierra hostil, el hombre modelado por el clima y la lucha fratricida. El sertão semiárido no es una llanura apacible; sin embargo, en medio de aquel laberinto de matorrales espinosos, cactos gigantes y lechos de ríos secos que se evaporan antes de tocar el mar, habita una estirpe humana extraordinaria. Como escribió el autor en una frase que grabó para siempre el alma nacional: 'El sertanejo es, ante todo, un fuerte', un hombre de tez curtida por el viento que se sobrepone con entereza sobrehumana a las inclemencias más despiadadas."
                },
                {
                    "type": "narration",
                    "text": "Hacia finales del siglo diecinueve, en una región desamparada por el latifundismo oligárquico y por la reciente proclamación de la República de 1889 —a la que los campesinos percibían como un régimen lejano que imponía nuevos impuestos sin otorgar pan ni justicia—, comenzó a peregrinar una figura mesiánica singular: Antônio Vicente Mendes Maciel, conocido por todos como Antônio Conselheiro. Con su túnica azulada deshilachada, su bastón de madera y su mirada llameante de profeta bíblico, el Conselheiro recorría los pueblos reconstruyendo ermitas caídas, bendiciendo cementerios y predicando una fe comunitaria basada en la hermandad, el perdón de los pecados y el desprecio a las autoridades seculares. Por una parte, las jerarquías eclesiásticas y los terratenientes lo denunciaron como un agitador peligroso; por otra, miles de peones rurales desposeídos, campesinos negros recién liberados de la esclavitud y familias hambrientas lo siguieron hasta una hacienda abandonada a orillas del río Vaza-Barris: Canudos."
                },
                {
                    "type": "narration",
                    "text": "En aquel cañón remoto rodeado por cerros de arenisca rojiza, el Conselheiro y sus seguidores fundaron la ciudadela santa de Belo Monte, levantando en pocos años más de cinco mil casas de barro y paja que llegaron a albergar a casi treinta mil almas libres en régimen comunal. Las autoridades republicanas de Río de Janeiro y Salvador interpretaron aquella comunidad autónoma como un foco insurgente monárquico financiado por conspiradores aristócratas; por el contrario, los pobladores de Canudos no pretendían derrocar al gobierno en la capital, sino más bien vivir pacíficamente al abrigo del fanatismo de sus terratenientes y de la violencia de las policías provinciales. No obstante esta vocación defensiva, el gobernador de Bahía envió un destacamento militar para dispersar a los campesinos, desatando una conflagración bélica de proporciones apocalípticas cuando los sertanejos emboscaron y aniquilaron a la tropa gubernamental."
                },
                {
                    "type": "narration",
                    "text": "Aterrada por el revés militar, la República envió sucesivamente tres expediciones armadas cada vez más numerosas y pertrechadas con cañones Krupp modernos y fusiles de repetición. Ahora bien, la superioridad técnica del ejército regular se estrelló repetidamente contra la genialidad táctica de los guerrilleros sertanejos dirigidos por lugartenientes como Pajeú y João Abade, quienes conocían palmo a palmo las trampas de la caatinga. Los soldados morían de sed y fiebre entre los matorrales sin avistar al enemigo; en contrapartida, los campesinos defendían cada trinchera con una audacia conmovedora. Hizo falta una cuarta expedición colosal de diez mil soldados bajo el mando directo de veteranos generales para sitiar la ciudadela durante meses, transformando el sitio de Canudos en un infierno de bombardeos incesantes donde las casas se derrumbaban ardiendo mientras las mujeres y los niños cantaban letanías religiosas entre las ruinas humeantes."
                },
                {
                    "type": "narration",
                    "text": "En suma, la caída final de Canudos en octubre de 1897 tras la muerte por disentería del Conselheiro constituyó una de las páginas más dolorosas y vergonzosas de la historia americana. Como atestiguó conmovido Euclides da Cunha, Canudos no se rindió jamás: cuatro defensores moribundos —un anciano ciego, dos hombres jóvenes y un niño descalzo— sostuvieron el fuego hasta el último proyectil frente a miles de soldados perplejos. En última instancia, 'Los sertones' se erige en un monumento literario y sociológico imperecedero que desenmascaró la barbarie del progreso impuesto por la fuerza militar y consagró la dignidad rebelde del hombre del interior profundo. En definitiva, la tragedia de Canudos continúa resonando como una advertencia eterna contra la soberbia de las metrópolis que desprecian el alma y la memoria viva de sus pueblos marginados."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Cuál es la famosa definición que Euclides da Cunha formuló sobre el campesino del nordeste brasileño?",
                            "options": [
                                "Que es un hombre sumiso y resignado a la esclavitud.",
                                "Que el sertanejo es, ante todo, un fuerte, modelado con entereza por las adversidades de la tierra.",
                                "Que es un extranjero sin apego por las tradiciones autóctonas.",
                                "Que era un soldado profesional retirado de las guerras europeas."
                            ],
                            "correctIndex": 1,
                            "explanation": "La célebre máxima de Euclides da Cunha destaca la entereza física y moral del sertanejo frente a la aridez."
                        },
                        {
                            "question": "¿Quién fue Antônio Conselheiro y qué fundó en el corazón de Bahía?",
                            "options": [
                                "Un banquero portugués que financió minas de diamantes.",
                                "Un predicador peregrino carismático que fundó la ciudadela comunitaria de Canudos (Belo Monte).",
                                "Un oficial de marina que construyó astilleros navales en el río.",
                                "Un terrateniente azucarero que introdujo máquinas a vapor."
                            ],
                            "correctIndex": 1,
                            "explanation": "Antônio Conselheiro lideró un movimiento mesiánico y fundó la comunidad autónoma campesina de Canudos."
                        },
                        {
                            "question": "¿Cómo terminó la resistencia militar de Canudos según el testimonio presencial del autor?",
                            "options": [
                                "Los campesinos firmaron un pacto de paz y se convirtieron en senadores de la república.",
                                "Canudos resistió hasta el final sin capitular jamás, quedando apenas cuatro defensores combatiendo entre las ruinas.",
                                "Los defensores huyeron en barcos hacia el continente africano.",
                                "El ejército republicano se retiró derrotado perdonando a todos los sublevados."
                            ],
                            "correctIndex": 1,
                            "explanation": "Canudos cayó sin rendirse, defendida hasta el último cartucho por cuatro combatientes frente a todo un ejército."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilnordeste-01": {
            "id": "b2-brasilnordeste-01",
            "title": "La Roma Negra y el oro del Pelourinho",
            "level": "B2",
            "lesson": 1,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "Salvador de Bahía y el Recôncavo: primera capital colonial de Brasil, su magnífica arquitectura barroca de azulejos y oro, el barrio histórico del Pelourinho y su trascendencia como epicentro de la cultura afrobrasileña.",
            "characters": [
                "Tomé de Sousa (primer gobernador general de Brasil)",
                "Maestros tallistas barrocos y alarifes coloniales",
                "Matriarcas bahianas del acarajé y tamborileros del Olodum"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "En lo alto de un acantilado escarpado que domina las aguas resplandecientes de la Bahía de Todos los Santos, se alza la primera capital histórica y espiritual del Brasil colonial: la ciudad de San Salvador de la Bahía de Todos los Santos. En primer término, fundada en 1549 por el hidalgo portugués Tomé de Sousa por orden expresa del rey Juan III, la urbe fue concebida con una audaz división militar y topográfica entre la Ciudad Baja —el puerto bullicioso, las factorías comerciales y los almacenes de azúcar— y la Ciudad Alta, protegida tras murallas y conectada siglos más tarde por el majestuoso Elevador Lacerda. Salvador floreció durante más de dos siglos como el epicentro económico del emporio azucarero atlántico, canalizando la riqueza de los ingenios del Recôncavo hacia los puertos europeos. Es decir, su opulencia no provino del azar, sino del florecimiento de una aristocracia latifundista y mercantil sustentada en el comercio internacional."
                },
                {
                    "type": "narration",
                    "text": "El corazón monumental de esta capital colonial palpita en el histórico barrio del Pelourinho, un dédalo fascinante de callejuelas empedradas con adoquines de cabeza de negro, caserones señoriales de tonos pastel y plazas donde el arte barroco alcanzó cotas de esplendor inigualables. Por una parte, la iglesia y convento de San Francisco deslumbra a los visitantes por su nave enteramente recubierta con láminas de oro puro batido y sus claustros decorados con más de cincuenta mil azulejos portugueses que narran fábulas mitológicas y sentencias morales; por otra, el propio nombre del Pelourinho encierra una memoria sombría y dolorosa, pues alude a la columna de piedra erigida en la plaza pública donde los africanos esclavizados eran amarrados y flagelados despiadadamente por los alguaciles. Dicho en otros términos, la belleza dorada de los templos bahianos convive con las cicatrices imborrables de la opresión colonial."
                },
                {
                    "type": "narration",
                    "text": "Sin embargo, aquella mano de obra forzada procedente de Angola, Mozambique, Nigeria y el Golfo de Benín transformó el dolor del desarraigo en una formidable epopeya de resistencia cultural y afirmación espiritual. Al ingresar por el puerto de Salvador más de tres millones de cautivos africanos a lo largo de tres centurias, la ciudad se consagró como la metrópolis más intensamente africanizada de todas las Américas, mereciendo el honroso y célebre título de 'la Roma Negra'. En cualquier caso, la herencia yoruba, bantú y fon no quedó confinada a los museos folclóricos; de todos modos, impregna el ritmo vital de las esquinas, la sonoridad melódica del habla cotidiana y el aroma inconfundible del aceite de palma o 'dendê' que perfuma las frituras de acarajé preparadas con maestría ancestral por las baianas de turbante y sayas almidonadas."
                },
                {
                    "type": "narration",
                    "text": "A finales del siglo veinte, el Pelourinho experimentó un vigoroso proceso de rehabilitación urbana que lo convirtió en un polo vibrante de activismo cívico, música de percusión y vanguardia comunitaria. Por poner un caso representativo, fue en estas plazas históricas donde nació el bloque afro 'Olodum', cuyos tamborileros revolucionaron el panorama de la música universal al fusionar la samba tradicional con el reggae jamaiquino y los ritmos sagrados del candomblé en el género arrollador del 'samba-reggae'. Sus tambores pintados con los colores del panafricanismo —rojo, amarillo, verde y negro— no constituyen un simple adorno festivo para los turistas; por el contrario, representan un escudo de lucha cívica contra el racismo estructural y una escuela comunitaria que brinda educación artística y dignidad a miles de jóvenes de las favelas bahianas."
                },
                {
                    "type": "narration",
                    "text": "En suma, Salvador de Bahía encarna el alma más profunda, entrañable y mestiza de la civilización brasileña. En última instancia, al contemplar el sol poniente reflejado en las cúpulas barrocas de las iglesias mientras asciende desde el fondo del barrio el latido ensordecedor de los atabaques y repiques, el viajero comprende que esta tierra aprendió a vencer a la muerte mediante el poder redentor del arte y de la memoria colectiva. En definitiva, la Roma Negra permanece como un faro de dignidad inagotable donde los descendientes de los pueblos esclavizados custodian la llama eterna de la libertad, demostrando al mundo que la fraternidad humana es la más alta y perdurable de las victorias históricas."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿En qué año y con qué división urbanística fue fundada la ciudad de Salvador de Bahía?",
                            "options": [
                                "En 1822 como un puerto minero subterráneo.",
                                "En 1549 por Tomé de Sousa, dividida topográficamente entre Ciudad Alta y Ciudad Baja.",
                                "En 1960 como la capital federal moderna del país.",
                                "En 1750 exclusivamente como un balneario militar."
                            ],
                            "correctIndex": 1,
                            "explanation": "Salvador fue fundada en 1549 con un diseño defensivo que separaba la Ciudad Alta de la Ciudad Baja."
                        },
                        {
                            "question": "¿Qué significaba históricamente el término 'Pelourinho' en la plaza principal de Salvador?",
                            "options": [
                                "Un teatro de comedias cortesanas.",
                                "La picota o columna de piedra pública donde se castigaba y flagelaba a los esclavizados.",
                                "Una fuente de agua bendita para los misioneros.",
                                "Un mirador para avistar ballenas en el Atlántico."
                            ],
                            "correctIndex": 1,
                            "explanation": "El Pelourinho era el poste de castigo público colonial, transformado hoy en símbolo de resistencia negra."
                        },
                        {
                            "question": "¿Qué innovación musical y social representó el grupo 'Olodum' en las calles de Salvador?",
                            "options": [
                                "La eliminación de todos los instrumentos de percusión.",
                                "La invención del samba-reggae como instrumento de educación comunitaria y denuncia contra el racismo.",
                                "La interpretación exclusiva de óperas italianas del siglo dieciocho.",
                                "La importación de marchas militares prusianas para el carnaval."
                            ],
                            "correctIndex": 1,
                            "explanation": "Olodum fusionó la samba con el reggae y el candomblé creando un poderoso movimiento de afirmación afrobrasileña."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilnordeste-02": {
            "id": "b2-brasilnordeste-02",
            "title": "Los tambores sagrados y la danza del orixá",
            "level": "B2",
            "lesson": 2,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "La espiritualidad del Candomblé y la resistencia corporal de la Capoeira: el terreiro como espacio de preservación cultural yoruba, el panteón de los orixás y el arte marcial afrobrasileño nacido de la lucha contra la servidumbre.",
            "characters": [
                "Iyalorixás (madres de santo) de los terreiros de Bahía",
                "Mestres de capoeira (Mestre Bimba, Mestre Pastinha)",
                "Iniciados y tocadores de atabaques y berimbau"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "Bajo la penumbra respetuosa de los patios arbolados de Salvador de Bahía, cuando el toque sagrado del atabaque rompe el silencio nocturno con su polirritmia hipnótica, una de las religiones más ricas y complejas del hemisferio occidental cobra vida: el Candomblé. En primer término, preservado celosamente durante centurias de persecución policial y estigmatización colonial, el Candomblé no es una mera superstición arcaica; por el contrario, constituye una cosmovisión filosófica integral de origen yoruba, fon y bantú donde las fuerzas vivas de la naturaleza se manifiestan a través de divinidades intermediarias llamadas 'orixás'. En los templos o 'terreiros' tradicionales —como el legendario Terreiro do Gantois o Ilê Axé Opô Afonjá—, la comunidad se reúne no para temer a un Dios distante y castigador, sino para celebrar el equilibrio vital o 'axé' que conecta armónicamente a los seres humanos con los ríos, el trueno, los bosques y el mar."
                },
                {
                    "type": "narration",
                    "text": "Cada orixá personifica una energía elemental del cosmos y gobierna un ámbito de la existencia terrenal con sus colores litúrgicos, comidas sagradas y danzas arquetípicas. Por una parte, Oxum es la señora de las aguas dulces de los ríos, la belleza dorada, la fertilidad maternal y la riqueza del oro; por otra, Xangô reina sobre el trueno retumbante, la justicia distributiva rigurosa y el fuego creador, empuñando su hacha de doble filo con porte regio. Dicho en otros términos, cuando los iniciados entran en trance místico durante las ceremonias y reciben el espíritu de su orixá patrono al compás de los tambores sagrados —el ronco rum, el rumpi y el lé—, sus cuerpos reproducen con exactitud coreográfica milenaria los gestos de los dioses africanos, vistiendo sayas blancas bordadas con encajes de richelieu que irradian una pureza deslumbrante."
                },
                {
                    "type": "narration",
                    "text": "Para sobrevivir en el seno de una sociedad esclavista y católica que castigaba con prisión y azotes cualquier práctica religiosa de origen africano, los sacerdotes y devotos bahianos apelaron a un prodigioso mecanismo de resistencia protectora: el sincretismo religioso. Es decir, asociaron estratégicamente la figura de cada orixá con la devoción a un santo del calendario católico oficial a fin de que los amos y las patrullas policiales no sospecharan de sus ritos clandestinos. Así las cosas, Ogum, el indomable dios del hierro y de la guerra, fue sincretizado con San Jorge guerrero; Iemanjá, la venerada madre de los mares a quien millones de devotos entregan flores blancas y perfumes cada dos de febrero en la playa de Río Vermelho, fue identificada con Nuestra Señora de la Concepción; y Oxalá, el dios anciano de la paz y de la creación, fue equiparado con el Señor del Bonfim."
                },
                {
                    "type": "narration",
                    "text": "De manera paralela a esta espiritualidad sagrada, la resistencia física y corporal de los esclavizados alumbró otra manifestación cultural única en el mundo entero: la 'capoeira'. Nacida en los campos de caña de azúcar y en los muelles portuarios como un arte marcial mortífero de combate cuerpo a cuerpo que combinaba patadas acrobáticas, cabezazos y barridos rasantes, la capoeira fue hábilmente disimulada bajo la apariencia de una danza folclórica inofensiva para eludir la represión de los capataces. Acompañada por el arco musical del 'berimbau', el pandeiro y cantos de llamada y respuesta que relatan la dura memoria de la servidumbre, dos atletas se retan en una 'roda' o círculo humano mediante movimientos elásticos y serpenteantes donde prima la astucia corporal o 'malandragem', sublimando la violencia opresora en una danza de libertad insobornable."
                },
                {
                    "type": "narration",
                    "text": "En suma, tanto los toques sagrados del Candomblé como las acrobacias elásticas de la capoeira consolidaron a Bahía como un baluarte supremo de dignidad y preservación cultural afroamericana. En última instancia, gracias a la sabiduría rectora de matriarcas indiscutibles como Mãe Menininha do Gantois y a la maestría pedagógica de capoeiristas legendarios como Mestre Bimba y Mestre Pastinha, estas tradiciones trascendieron la marginación para ser declaradas Patrimonio Cultural de la Humanidad por la UNESCO. En definitiva, en el temblor de la cuerda tensa del berimbau y en las ofrendas depositadas en las olas espumosas del mar late el testimonio imperecedero de un pueblo que jamás se arrodilló ante las cadenas de la servidumbre."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Cuál es la función del concepto de 'axé' en la religión del Candomblé?",
                            "options": [
                                "Una condena eterna a los pecadores en el infierno.",
                                "La fuerza vital, energía cósmica sagrada y bendición que sostiene la armonía de la naturaleza y de la comunidad.",
                                "Un impuesto que se pagaba a la Corona de Portugal.",
                                "El nombre de una espada de guerra de los soldados."
                            ],
                            "correctIndex": 1,
                            "explanation": "El axé es la energía sagrada primordial que fluye entre los orixás, la naturaleza y los seres humanos."
                        },
                        {
                            "question": "¿Por qué practicaron los devotos afrobrasileños el sincretismo entre los orixás y los santos católicos?",
                            "options": [
                                "Porque habían olvidado por completo los nombres de sus dioses africanos.",
                                "Como una estrategia deliberada para proteger sus cultos sagrados de la persecución y censura colonial.",
                                "Por una orden firmada por el papa en Roma.",
                                "Para cobrar entradas comerciales a las celebraciones litúrgicas."
                            ],
                            "correctIndex": 1,
                            "explanation": "El sincretismo permitió camuflar las deidades africanas bajo advocaciones cristianas para burlar la represión."
                        },
                        {
                            "question": "¿Cómo nació la capoeira y cómo logró sobrevivir a la vigilancia de los amos esclavistas?",
                            "options": [
                                "Como un deporte olímpico inventado en París.",
                                "Como un arte marcial de autodefensa camuflado ingeniosamente bajo la apariencia de una danza con música de berimbau.",
                                "Como un entrenamiento militar exclusivo para los gobernadores de Bahía.",
                                "Como una comedia teatral de marionetas mecánicas."
                            ],
                            "correctIndex": 1,
                            "explanation": "La capoeira era una técnica de combate y liberación disimulada como danza acrobática al son del berimbau."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilnordeste-03": {
            "id": "b2-brasilnordeste-03",
            "title": "Hachas, sequía y versos colgados de un cordel",
            "level": "B2",
            "lesson": 3,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "El drama secular del Sertão nordestino: el flagelo cíclico de las sequías en la Caatinga, el fenómeno legendario del Cangaço con Lampião y Maria Bonita, y la maravillosa tradición poética y visual de la literatura de cordel.",
            "characters": [
                "Virgulino Ferreira da Silva (Lampião, el rey del cangaço)",
                "Maria Bonita (la legendaria compañera de armas)",
                "Poetas populares, xilógrafos y trovadores de feria ambulante"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "Más allá de las sierras verdes que bordean el litoral atlántico de Bahía, Pernambuco y Ceará, el paisaje cambia de modo abrupto para internarse en uno de los territorios más agrestes y sufridos de la geografía americana: el Sertão semiárido. En primer término, dominado por el bioma exclusivo de la 'Caatinga' —término de origen tupí que designa el 'bosque blanco' debido al aspecto blanquecino y fantasmal que adquieren los árboles cuando pierden sus hojas durante los meses de estío—, este suelo arcilloso padece el flagelo cíclico de las grandes sequías prolongadas. Cuando las lluvias faltan durante años consecutivos, la tierra se agrieta como una calavera reseca, el ganado vacuno sucumbe de inanición y miles de familias de campesinos desposeídos —los 'retirantes'— se ven forzadas a abandonar sus chozas con atados de ropa en la cabeza para emprender un penoso éxodo a pie hacia las ciudades costeras."
                },
                {
                    "type": "narration",
                    "text": "En medio de este escenario de desamparo institucional donde la justicia residía exclusivamente en los fusiles privados de los 'coroneles' latifundistas, floreció entre finales del siglo diecinueve y la década de 1930 el fenómeno social y épico del 'cangaço'. Aquellas partidas nómadas de forajidos armados recorrían el monte desafiando a las patrullas policiales o 'volantes' del gobierno, vistiendo chaquetas de cuero curtido reforzadas con tachuelas de plata y pesados sombreros de ala ancha en forma de media luna. Su líder indiscutible fue Virgulino Ferreira da Silva, apodado 'Lampião' porque disparaba su carabina de repetición con tanta rapidez que la boca del cañón parecía una lámpara encendida en la noche oscura. Junto a su célebre compañera Maria Bonita —la primera mujer que empuñó las armas en el bando rebelde—, Lampião sembró el terror entre los hacendados codiciosos, siendo reverenciado por el campesinado pobre como una mezcla fascinante de justiciero popular y demonio vengador."
                },
                {
                    "type": "narration",
                    "text": "La memoria de aquellas andanzas, amores y sangrientos tiroteos no quedó sepultada en los archivos policiales; por el contrario, encontró su cauce de inmortalidad popular en la fascinante tradición de la 'literatura de cordel'. Nacida de los pliegos de cordel traídos por los colonizadores portugueses durante el Renacimiento, esta manifestación poética se aclimató con prodigiosa originalidad en las ferias campesinas del Nordeste. Los poetas populares componían romances en estrofas rimadas de seis o diez versos (las sextillas y décimas) para narrar las proezas de los cangaceiros, las profecías del Padre Cícero de Juazeiro, las leyendas de aparecidos y los debates políticos contemporáneos. Los folletos impresos en papel rústico se colgaban de cuerdas o cordeles tensados entre dos estacas de madera en las ferias para que los campesinos pudieran examinarlos y comprarlos por unos pocos centavos."
                },
                {
                    "type": "narration",
                    "text": "El rasgo artístico más deslumbrante que acompaña a la literatura de cordel reside en sus portadas ilustradas con 'xilografías', grabados populares tallados pacientemente a gubia sobre madera dura de umburana o cedro e impresos con tinta negra tipográfica. Con un trazo firme, expresionista y de una economía visual asombrosa, los maestros xilógrafos del Nordeste —como el célebre J. Borges en Caruaru— inmortalizaron el rostro altivo de Lampião con sus gafas redondas, los diablos del sertão burlados por campesinos astutos y los animales del monte en composiciones plásticas que hoy engalanan los museos de arte contemporáneo de Europa y Estados Unidos. De todos modos, el cordel no es una pieza arqueológica de colección; sigue siendo el periódico lírico y oral del pueblo campesino donde se canta la verdad de la vida con ingenio inagotable."
                },
                {
                    "type": "narration",
                    "text": "En suma, el Sertão nordestino encarna la victoria del espíritu humano frente a la fatalidad de la naturaleza y el abandono de los poderosos. Al compás contagioso del acordeón, el triángulo y el bombo que marcan el ritmo del 'forró' y del 'baião' inmortalizado por Luiz Gonzaga —el 'Rey del Baião'—, el pueblo sertanejo baila abrazado sobre el polvo levantado de las eras campesinas para desafiar a la sequía y festejar la lluvia bendita. En última instancia, en los versos rimados de un folleto de cordel y en la mirada indómita del hombre de la caatinga se custodia la verdad más noble del Brasil profundo: la convicción de que la cultura popular es el refugio más seguro de la dignidad, la memoria y la esperanza comunitaria."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué bioma vegetal y qué fenómeno climático extremo azotan históricamente el Sertão?",
                            "options": [
                                "La tundra helada con nevadas continuas.",
                                "La Caatinga semiárida con sequías cíclicas devastadoras que obligan al éxodo campesino.",
                                "La selva tropical lluviosa con inundaciones permanentes durante todo el año.",
                                "Un desierto de dunas móviles de arena volcánica sin vegetación."
                            ],
                            "correctIndex": 1,
                            "explanation": "La Caatinga es un bioma semiárido donde las sequías periódicas causan graves crisis humanitarias."
                        },
                        {
                            "question": "¿Quiénes fueron Lampião y Maria Bonita en la historia popular del Nordeste?",
                            "options": [
                                "Dos pintores modernistas de la Semana de 1922.",
                                "Los legendarios líderes del Cangaço que recorrieron el monte con sus partidas armadas enfrentando a los coroneles.",
                                "Diplomáticos que firmaron tratados fronterizos con Colombia.",
                                "Dos cantantes de ópera del Teatro Municipal de Río de Janeiro."
                            ],
                            "correctIndex": 1,
                            "explanation": "Lampião y Maria Bonita fueron los líderes más célebres del cangaço, convertidos en mitos populares."
                        },
                        {
                            "question": "¿Cómo se exhibían y vendían tradicionalmente los pliegos de la literatura de cordel en las ferias?",
                            "options": [
                                "Se guardaban bajo llave en cajas fuertes de bancos privados.",
                                "Se colgaban con pinzas de cuerdas o cordeles tendidos entre estacas para que el público los hojease.",
                                "Se transmitían exclusivamente mediante señales telegráficas de código morse.",
                                "Se arrojaban desde aviones militares sobre las plantaciones de café."
                            ],
                            "correctIndex": 1,
                            "explanation": "Los folletos de poesía popular se colgaban de un cordel en las ferias públicas, de donde toman su nombre."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilnordeste-04": {
            "id": "b2-brasilnordeste-04",
            "title": "La cumbre libre de los Palmares",
            "level": "B2",
            "lesson": 4,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "La epopeya del Quilombo de los Palmares en la Sierra de la Barriga: la mayor república cimarrona de fugitivos del continente americano, el liderazgo heroico de Zumbi y su consagración moderna en el Día de la Conciencia Negra.",
            "characters": [
                "Ganga Zumba (primer gran líder de Palmares)",
                "Zumbi dos Palmares (héroe supremo de la resistencia negra)",
                "Domingos Jorge Velho (el bandeirante mercenario del asedio final)"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "En las estribaciones selváticas y abruptas de la Sierra de la Barriga, en el actual estado nordestino de Alagoas, floreció durante prácticamente todo el siglo diecisiete el mayor experimento de libertad, soberanía colectiva y resistencia antiesclavista de todas las Américas: la república cimarrona del Quilombo de los Palmares. En primer término, mientras los imperios de Portugal y Holanda se disputaban a sangre y fuego el dominio lucrativo de las plantaciones de caña de azúcar del litoral pernambucano, miles de hombres y mujeres africanos esclavizados aprovecharon las convulsiones bélicas para romper sus cadenas y huir hacia el interior boscoso. Es decir, Palmares no fue un campamento precario de fugitivos desamparados, sino una formidable federación de asentamientos fortificados o 'mocambos' —como Macaco, Subupira y Cerca Real— que llegó a albergar a más de veinte mil habitantes libres viviendo en paz comunal."
                },
                {
                    "type": "narration",
                    "text": "La organización social y productiva de Palmares asombra hasta nuestros días por su madurez institucional y su carácter inclusivo y multicultural. Por una parte, los palmarinos recrearon las instituciones políticas de las monarquías africanas de Angola y el Congo bajo la autoridad de un jefe supremo electo llamado Ganga Zumba, combinando la propiedad comunitaria de la tierra con parcelas familiares de cultivo intensivo de maíz, mandioca, plátanos y caña; por otra parte, en sus aldeas libres hallaron refugio no solo africanos de diversas etnias, sino también indígenas originarios despojados de sus selvas y blancos pobres perseguidos por la justicia colonial. Dicho en otros términos, Palmares demostró con hechos incontestables que era perfectamente posible erigir en el Nuevo Mundo una sociedad próspera y solidaria sin amos aristocráticos, sin látigos infames y sin trabajo esclavo forzado."
                },
                {
                    "type": "narration",
                    "text": "Conscientes de que la sola existencia de Palmares constituía una amenaza mortal para el sistema esclavista colonial —pues servía de faro magnético que incitaba a la fuga continua en los ingenios azucareros—, las autoridades de Lisboa enviaron más de una veintena de expediciones militares punitivas para arrasar el quilombo. Hacia 1678, cuando el anciano Ganga Zumba aceptó una propuesta de paz de las autoridades coloniales que ofrecía libertad solo para los nacidos en Palmares a cambio de devolver a los nuevos fugitivos, emergió la figura indómita de su joven sobrino: Zumbi. Negándose categóricamente a negociar una libertad amputada y traicionera que condenaba a sus hermanos a las cadenas, Zumbi asumió el mando militar supremo, jurando luchar hasta las últimas consecuencias por la emancipación universal de todos los oprimidos sin excepción."
                },
                {
                    "type": "narration",
                    "text": "La destrucción final del quilombo demandó la contratación del más despiadado líder de bandeirantes de São Paulo: el mercenario Domingos Jorge Velho, quien al mando de miles de soldados y auxiliares indígenas pertrechados con cañones sitió la capital de Macaco en 1694 durante semanas de sangriento combate cuerpo a cuerpo. Traicionado meses más tarde por uno de sus lugartenientes torturados, Zumbi fue emboscado y asesinado el 20 de noviembre de 1695. Su cabeza cortada fue exhibida en una pica en la plaza pública de Recife so pretexto de desmentir la creencia popular de que el líder era inmortal. En cualquier caso, los verdugos coloniales se equivocaron de manera flagrante: al asesinar el cuerpo mortal del héroe, consagraron para siempre su espíritu invicto en el corazón de la memoria colectiva brasileña."
                },
                {
                    "type": "narration",
                    "text": "En suma, la gesta heroica de los Palmares representa la cumbre moral de la resistencia libertaria del pueblo afrobrasileño. En 2003, el Estado brasileño instituyó oficialmente el 20 de noviembre —fecha del martirio de Zumbi— como el 'Día Nacional de la Conciencia Negra', consagrándolo como feriado de orgullo y reflexión sobre las deudas históricas con los afrodescendientes. En última instancia, las piedras milenarias de la Sierra de la Barriga continúan proclamando al viento continental que la libertad no se mendiga ante los poderosos, sino que se conquista con dignidad y sacrificio compartido. En definitiva, el grito rebelde de Zumbi dos Palmares sigue iluminando la marcha ininterrumpida de todos los pueblos que luchan por un mundo sin discriminación, sin cadenas y con justicia plena para todos."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué fue el Quilombo de los Palmares y dónde se estableció en el siglo XVII?",
                            "options": [
                                "Un puerto comercial holandés para la exportación de diamantes.",
                                "La mayor federación autónoma de cimarrones libres de América, fundada en la Sierra de la Barriga.",
                                "Un colegio jesuítico para misioneros europeos.",
                                "Una prisión de alta seguridad construida por la Corona británica."
                            ],
                            "correctIndex": 1,
                            "explanation": "Palmares fue una república autónoma de miles de cimarrones libres en la Sierra de la Barriga."
                        },
                        {
                            "question": "¿Por qué rechazó Zumbi el acuerdo de paz que Ganga Zumba había aceptado en 1678?",
                            "options": [
                                "Porque exigía que le entregasen coronas de oro macizo.",
                                "Porque el tratado concedía libertad solo a los nacidos en Palmares obligando a devolver al resto a la esclavitud.",
                                "Porque prefería emigrar a Norteamérica.",
                                "Porque deseaba rendirse incondicionalmente a las autoridades portuguesas."
                            ],
                            "correctIndex": 1,
                            "explanation": "Zumbi rechazó una paz parcial que traicionaba a los nuevos esclavizados fugitivos."
                        },
                        {
                            "question": "¿Qué efeméride cívica conmemora Brasil cada 20 de noviembre en homenaje a Zumbi?",
                            "options": [
                                "El Día de la Independencia de Portugal.",
                                "El Día Nacional de la Conciencia Negra, recordando la resistencia antiesclavista.",
                                "La fundación de la ciudad de São Paulo.",
                                "La apertura de los puertos marítimos internacionales."
                            ],
                            "correctIndex": 1,
                            "explanation": "El 20 de noviembre se celebra el Día de la Conciencia Negra en conmemoración de la muerte de Zumbi."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilnordeste-05": {
            "id": "b2-brasilnordeste-05",
            "title": "El espejo quebrado de la democracia racial",
            "level": "B2",
            "lesson": 5,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "El debate sociológico fundamental sobre las relaciones raciales en Brasil: la tesis clásica de Gilberto Freyre sobre la 'democracia racial', la crítica demoledora de Florestan Fernandes y las políticas modernas de acción afirmativa y cuotas.",
            "characters": [
                "Gilberto Freyre (autor de Casa-Grande & Senzala, 1933)",
                "Florestan Fernandes y Abdias do Nascimento (sociólogos críticos)",
                "Estudiantes universitarios y activistas de la acción afirmativa"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "Durante gran parte del siglo veinte, el imaginario nacional brasileño y su imagen diplomática ante la comunidad internacional estuvieron dominados por una doctrina sociológica sumamente seductora y tranquilizadora: la teoría de la 'democracia racial'. En primer término, formulada con brillantez narrativa por el célebre sociólogo e historiador pernambucano Gilberto Freyre en su obra cumbre 'Casa-Grande & Senzala' (1933), esta tesis postulaba que la colonización portuguesa en el Nordeste azucarero había dado lugar a un tipo único de convivencia armónica entre colonizadores europeos, pueblos indígenas y africanos esclavizados. Según Freyre, la intensa promiscuidad biológica y la permeabilidad cultural facilitadas por el clima tropical habrían impedido el surgimiento de las violentas tensiones raciales y de la segregación jurídica institucionalizada que caracterizaron históricamente a los Estados Unidos o a Sudáfrica."
                },
                {
                    "type": "narration",
                    "text": "Sin embargo, a partir de la década de 1950, una nueva generación de sociólogos rigurosos encabezada por Florestan Fernandes y la denominada Escuela de Sociología de São Paulo, junto a líderes pioneros del movimiento negro como Abdias do Nascimento, desmontaron de manera demoledora aquel mito complaciente. Por una parte, las investigaciones empíricas evidenciaron que la abolición de la esclavitud en 1888 no vino acompañada de ninguna política estatal de inclusión educativa, reparto de tierras o acceso al trabajo digno para los libertos; por otra, los sociólogos demostraron que la ideología del mestizaje funcionó en la práctica como un sutil dispositivo hegemónico de 'blanqueamiento' biológico y cultural, mediante el cual se estigmatizaba lo negro y se perpetuaba el dominio indiscutido de las élites blancas sobre los resortes del poder político y económico. Dicho en otros términos, la pretendida armonía encubría un racismo solapado y eficaz."
                },
                {
                    "type": "narration",
                    "text": "En las primeras décadas del siglo veintiuno, las estadísticas oficiales del Instituto Brasileño de Geografía y Estadística (IBGE) continuaron arrojando datos incontrovertibles sobre la persistencia de una abismal fractura racial estructural. A pesar de que los ciudadanos que se autodefinen como afrodescendientes (negros y pardos) representan más del cincuenta y seis por ciento de la población total del país, ellos continúan concentrando los índices más altos de pobreza material, subempleo informal, analfabetismo y víctimas de homicidios por violencia policial en las periferias metropolitanas. En cualquier caso, su presencia en los altos cargos de la judicatura, en los consejos de administración de las grandes empresas, en el parlamento federal y en el cuerpo diplomático de Itamaraty seguía siendo alarmantemente reducida e incompatible con una república genuinamente democrática."
                },
                {
                    "type": "narration",
                    "text": "Fue en respuesta a esta lacerante brecha estructural donde el Estado brasileño dio un paso de enorme trascendencia continental al sancionar en agosto de 2012 la histórica 'Ley de Cuotas' para la educación superior pública. Conforme a esta legislación pionera, todas las universidades e institutos federales reservaron obligatoriamente el cincuenta por ciento de sus plazas de ingreso para estudiantes provenientes de escuelas secundarias públicas, aplicando criterios de corte racial proporcional a la demografía de cada estado federado. Por poner un caso representativo, en universidades de enorme prestigio como la Universidad de São Paulo (USP) o la Universidad Federal de Bahía (UFBA), la presencia de estudiantes afrodescendientes e indígenas en facultades elitistas como Medicina, Derecho e Ingeniería se triplicó en una década, transformando radicalmente el perfil social de las aulas universitarias, democratizando el acceso a las profesiones más influyentes y abriendo horizontes inéditos de movilidad socioeconómica ascendente para familias enteras que jamás habían soñado con pisar un claustro universitario."
                },
                {
                    "type": "narration",
                    "text": "En suma, el debate sobre las relaciones raciales en Brasil ha transitado desde la ilusión idílica de una falsa armonía sin conflictos hacia el reconocimiento maduro de las heridas históricas y la adopción de políticas públicas reparadoras con base empírica. En última instancia, romper el espejo quebrado de la democracia racial no persigue dividir a la sociedad en compartimentos estancos antagónicos, sino asegurar que todos los hijos de la patria compartan en condiciones reales de igualdad los frutos del conocimiento, la justicia y el bienestar cívico. En definitiva, la madurez democrática de la nación más poblada de Iberoamérica depende de su capacidad ética de saldar la deuda secular con sus raíces afrodescendientes, honrando la verdad de su historia para construir un porvenir verdaderamente justo y fraterno."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué sostenía la teoría clásica de la 'democracia racial' formulada por Gilberto Freyre en 1933?",
                            "options": [
                                "Que en Brasil nunca existió población afrodescendiente ni indígena.",
                                "Que el mestizaje y la cultura tropical crearon una convivencia armónica exenta del racismo violento de otros países.",
                                "Que los tribunales debían aplicar leyes de segregación territorial estricta.",
                                "Que la esclavitud debía ser reinstaurada de inmediato."
                            ],
                            "correctIndex": 1,
                            "explanation": "Freyre postulaba que la mezcla cultural portuguesa amortiguó las tensiones raciales creando armonía mestiza."
                        },
                        {
                            "question": "¿Qué denunciaron sociólogos críticos como Florestan Fernandes y Abdias do Nascimento?",
                            "options": [
                                "Que el mito de la democracia racial encubría un racismo estructural que marginaba a la población afrodescendiente.",
                                "Que no era necesario realizar censos de población en el país.",
                                "Que las universidades públicas debían ser privatizadas totalmente.",
                                "Que la abolición de 1888 había solucionado todos los problemas económicos."
                            ],
                            "correctIndex": 0,
                            "explanation": "Demostraron que la supuesta armonía invisibilizaba la desigualdad real y el racismo institucional."
                        },
                        {
                            "question": "¿En qué consistió la histórica Ley de Cuotas universitarias aprobada en Brasil en 2012?",
                            "options": [
                                "En cobrar matrículas en dólares a los estudiantes de escuelas públicas.",
                                "En reservar el 50% de las plazas de universidades federales para egresados de escuelas públicas con cuotas étnico-raciales.",
                                "En prohibir el ingreso de estudiantes de bajos recursos a las carreras de medicina.",
                                "En eliminar los exámenes de ingreso en todas las instituciones privadas."
                            ],
                            "correctIndex": 1,
                            "explanation": "La Ley de Cuotas reservó la mitad de las vacantes universitarias federales para estudiantes de escuelas públicas y afrodescendientes."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilnordeste-consolidation": {
            "id": "b2-brasilnordeste-consolidation",
            "title": "El sol inclemente y la dignidad del Nordeste",
            "level": "B2",
            "lesson": 6,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "Síntesis reflexiva sobre el alma del Nordeste de Brasil: la confluencia entre la herencia afrodescendiente de Bahía, la resistencia mística de los orixás y la capoeira, la epopeya de los Palmares, el dramatismo del Sertão y el debate sociológico sobre la igualdad racial.",
            "characters": [
                "Narradores populares y cronistas del Nordeste",
                "El pueblo sertanejo y las comunidades bahianas como protagonistas colectivos"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "Bajo la luz enceguecedora del mediodía que reverbera sobre las arenas blancas de los litorales de Bahía y Pernambuco o sobre las piedras calcinadas de la caatinga profunda, el viajero atento que recorre el Nordeste brasileño comprende que se encuentra en la cuna espiritual y demográfica más vigorosa de la nación. En primer término, el Nordeste no es un mero escenario pintoresco de playas tropicales bordeadas de cocoteros y ferias artesanales; es la fragua histórica donde se fundió a sangre y fuego el mestizaje original entre el colonizador portugués, las naciones indígenas originarias y millones de seres humanos desarraigados violentamente de las costas de África. Es decir, en cada rincón de esta tierra milenaria se percibe la huella de una resistencia civilizatoria inquebrantable que supo transformar el dolor de la opresión en belleza estética, dignidad cívica y alegría comunitaria desbordante."
                },
                {
                    "type": "narration",
                    "text": "A lo largo de la costa marítima, la majestuosa ciudad de Salvador de Bahía se alza como el faro incombustible de la 'Roma Negra', custodiando en sus templos dorados y en sus terreiros de Candomblé la llama sagrada del axé y la sabiduría ancestral de los orixás. Por una parte, las danzas rituales de los atabaques y la destreza acrobática del berimbau en la capoeira demostraron que el cuerpo oprimido puede convertirse en un templo invicto de libertad y espiritualidad; por otra parte, en las sierras escarpadas de Alagoas, la memoria inmortal de Zumbi dos Palmares y de su república cimarrona continúa recordando a toda América que la emancipación no se mendiga ante los opresores, sino que se construye con solidaridad comunitaria y audacia política irrenunciable. Asimismo, las cofradías de mujeres negras, como la legendaria Hermandad de la Buena Muerte en Cachoeira, articularon redes clandestinas de manumisión y auxilio mutuo que desafiaron durante siglos el orden señorial esclavista, preservando cánticos y devociones sagradas de origen africano."
                },
                {
                    "type": "narration",
                    "text": "Hacia el poniente árido, allende las serranías litorales, la inmensidad agreste del Sertão semiárido desafía las leyes de la supervivencia terrenal con su régimen de sequías inclementes y su vegetación espinosa de la caatinga. No obstante la dureza extrema del clima y la desidia histórica de las élites latifundistas, el hombre sertanejo acreditó la célebre verdad inmortalizada por Euclides da Cunha: 'El sertanejo es, ante todo, un fuerte'. En aquel caldero de adversidades nacieron tanto la rebeldía armada de los cangaceiros liderados por Lampião y Maria Bonita como la luminosa inventiva lírica de la literatura de cordel, cuyas estrofas rimadas y xilografías populares demuestran que la poesía es el pan supremo que sostiene el alma del pueblo cuando el cielo niega la lluvia bienhechora. Del mismo modo, la memoria trágica de Canudos perdura en la conciencia popular como un testimonio desgarrador de la lucha campesina por la tierra comunal frente a la violencia ciega de los ejércitos centralistas."
                },
                {
                    "type": "narration",
                    "text": "Asimismo, el Nordeste contemporáneo lidera el debate ético más inaplazable de la sociedad brasileña: la superación definitiva de la falacia complaciente de la 'democracia racial' y la conquista efectiva de la igualdad de oportunidades para las mayorías afrodescendientes e indígenas. A través de la implementación valiente de acciones afirmativas, cuotas universitarias y políticas de desarrollo territorial inclusivo, la región demuestra al continente entero que la verdadera modernidad democrática no consiste en ocultar las heridas de la esclavitud, sino en saldar con justicia distributiva y coraje cívico las deudas históricas con los forjadores anónimos de la patria grande."
                },
                {
                    "type": "narration",
                    "text": "En suma, quien escucha el repique de los tambores de Olodum en el Pelourinho, contempla las aguas del río São Francisco regando los valles sertanejos o saborea el acarajé caliente en una plaza bahiana comprende que en el Nordeste palpita el corazón insobornable del Brasil creador. En última instancia, la fuerza indómita de su gente enseña que la mayor riqueza de una civilización no reside en la acumulación de metales preciosos ni en el poder de las armas destructivas, sino en la capacidad inagotable de su cultura popular para celebrar la vida, honrar a los ancestros y caminar con la frente erguida hacia un horizonte de justicia, fraternidad y paz para todos los seres humanos."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué representa la región del Nordeste en la construcción identitaria de Brasil?",
                            "options": [
                                "Una colonia extranjera desvinculada del resto del territorio.",
                                "La cuna espiritual, histórica y demográfica donde floreció la resistencia afrobrasileña e indígena.",
                                "Un desierto despoblado sin ninguna tradición artística ni religiosa.",
                                "Un centro exclusivo de producción petrolera marina sin historia colonial."
                            ],
                            "correctIndex": 1,
                            "explanation": "El Nordeste es la cuna histórica del mestizaje y el epicentro de la cultura afrobrasileña."
                        },
                        {
                            "question": "¿De qué manera dialogan la espiritualidad del Candomblé y la gesta del Quilombo de Palmares?",
                            "options": [
                                "Ambas constituyen expresiones cumbres de la resistencia, preservación cultural y dignidad del pueblo negro.",
                                "Fueron movimientos monárquicos fundados por emperadores europeos.",
                                "Fueron prohibidos para siempre y desaparecieron sin dejar rastro en la sociedad contemporánea.",
                                "Eran actividades comerciales reservadas a las élites terratenientes."
                            ],
                            "correctIndex": 0,
                            "explanation": "Tanto el Candomblé como Palmares personifican la lucha por la libertad y la dignidad frente a la esclavitud."
                        },
                        {
                            "question": "¿Cuál es el desafío contemporáneo medular que encara la región en el plano de los derechos civiles?",
                            "options": [
                                "Erradicar el uso de la literatura de cordel en las escuelas públicas.",
                                "Superar las secuelas de la discriminación racial estructural mediante políticas afirmativas y justicia social.",
                                "Prohibir la música de samba en los carnavales.",
                                "Impedir que los campesinos regresen al Sertão tras las sequías."
                            ],
                            "correctIndex": 1,
                            "explanation": "El reto central es consolidar la igualdad real superando las barreras históricas de la exclusión social y racial."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilnordeste": {
            "id": "b2-brasilnordeste",
            "title": "Brasil II: El Nordeste, el Alma Afrobrasileña y el Sertão",
            "level": "B2",
            "lesson": 1,
            "type": "world",
            "estimatedMinutes": 20,
            "summary": "Compendio general y panorámico sobre el Nordeste de Brasil: la primera capital colonial de Salvador de Bahía y la 'Roma Negra', la vivencia sagrada del Candomblé y la Capoeira, la epopeya libre del Quilombo de los Palmares con Zumbi, el drama de las sequías en la Caatinga y la epopeya épica de Canudos, y el debate actual sobre la acción afirmativa y la igualdad racial.",
            "characters": [
                "Líderes cimarrones de Palmares (Ganga Zumba y Zumbi)",
                "Iyalorixás de los terreiros de Salvador de Bahía",
                "Antônio Conselheiro y los defensores de Canudos",
                "Virgulino Ferreira da Silva (Lampião) y Maria Bonita",
                "Sociólogos y educadores de la acción afirmativa"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "En el extremo nororiental de América del Sur, acariciado por las corrientes cálidas del océano Atlántico y coronado por mesetas semiáridas que se extienden hacia el horizonte interior, florece la región más antigua, diversa y conmovedora de la civilización brasileña: el Nordeste. Integrado por nueve estados que albergan a más de cincuenta y cinco millones de habitantes, este territorio fue el escenario primordial donde comenzó a forjarse el destino de la nación con el desembarco portugués de 1500 en Porto Seguro y la instauración del emporio azucarero colonial. En primer término, la riqueza monumental de Salvador de Bahía —primera capital de Brasil durante más de dos centurias— y de Olinda deslumbra al mundo por su arquitectura barroca de suntuosos templos dorados y palacetes coloniales empedrados en el histórico barrio del Pelourinho, testigo imborrable del sufrimiento de los esclavizados y del florecimiento de una cultura afrodescendiente incomparable. Asimismo, las ciudades de Recife y Olinda destacan por sus canales fluviales, sus puentes históricos y una vigorosa vida intelectual que desafió tempranamente las imposiciones coloniales europeas."
                },
                {
                    "type": "narration",
                    "text": "Con el arribo forzoso de millones de seres humanos procedentes de las diversas naciones del África subsahariana, el Nordeste se consagró como el corazón de la 'Roma Negra' de las Américas, gestando un universo religioso y corporal de resistencia espiritual sublime. En los terreiros tradicionales de Salvador, el Candomblé preservó con rigor litúrgico milenario el panteón de los orixás —las divinidades cósmicas que encarnan las aguas, el trueno, el hierro y los bosques—, armonizando el culto sagrado mediante un sabio sincretismo protector con el santoral católico. De manera complementaria, los muelles y plantaciones alumbraron la capoeira: un arte marcial de combate acrobático camuflado como danza al son magnético del berimbau mediante el cual el oprimido transformó su cuerpo en un arma de libertad inquebrantable frente al látigo de los capataces. Por consiguiente, cada toque ceremonial de atabaque y cada movimiento circular de la roda representan una reafirmación identitaria inextinguible que sobrevivió con entereza a siglos de persecución policial y hostilidad social."
                },
                {
                    "type": "narration",
                    "text": "La aspiración a la libertad absoluta alcanzó su manifestación más gloriosa en las selvas de la Sierra de la Barriga con la república cimarrona del Quilombo de los Palmares. Durante casi un siglo entero, decenas de miles de hombres y mujeres fugitivos desafiaron a los ejércitos coloniales de Portugal y Holanda, edificando una sociedad comunitaria autónoma basada en la ayuda mutua, la agricultura diversificada y la dignidad colectiva bajo el mando supremo de héroes legendarios como Zumbi. Traicionado y asesinado el 20 de noviembre de 1695, el sacrificio de Zumbi no fue en vano, pues su memoria inspiró la posterior consagración del Día Nacional de la Conciencia Negra como un hito de afirmación soberana contra el racismo estructural y la discriminación social."
                },
                {
                    "type": "narration",
                    "text": "Hacia el interior seco, el paisaje se transmuta en el laberinto espinoso del Sertão y de la Caatinga, donde el azote cíclico de las sequías calcinantes forjó la recia personalidad del campesinado sertanejo. Fue en aquella tierra bravía donde estallaron tragedias apocalípticas como la guerra de Canudos en 1897 —inmortalizada por Euclides da Cunha en 'Los sertones' al relatar la resistencia indomable de Antônio Conselheiro y sus seguidores frente a todo un ejército regular— y donde cabalgaron las partidas armadas de cangaceiros lideradas por Lampião y Maria Bonita. Lejos de sucumbir a la desolación, la caatinga engendró la rica tradición lírica de la literatura de cordel y las xilografías populares, baluartes poéticos donde el pueblo canta con humor e ingenio sus penas cotidianas al compás contagioso del forró."
                },
                {
                    "type": "narration",
                    "text": "En el siglo veintiuno, el Nordeste encabeza la transformación democrática de Brasil al desmontar la complaciente falacia de la 'democracia racial' popularizada en el pasado por Gilberto Freyre, demostrando que la igualdad efectiva exige políticas públicas afirmativas, leyes de cuotas universitarias y justicia distributiva. En definitiva, la región del Nordeste enseña al continente entero que la verdadera grandeza de un pueblo no estriba en el poder militar ni en la arrogancia económica, sino en la nobleza espiritual de una sociedad que sabe honrar a sus ancestros, resistir ante la adversidad con dignidad inquebrantable y celebrar la vida con una pasión fraterna que ilumina el destino de toda Iberoamérica."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Cuál fue el papel histórico primordial de la región del Nordeste en la formación de Brasil?",
                            "options": [
                                "Fue el primer escenario del desembarco portugués y la sede de su primera capital en Salvador de Bahía.",
                                "Fue una zona deshabitada hasta la construcción de las plantas automotrices en 1990.",
                                "Fue cedida a Gran Bretaña como pago de deudas comerciales.",
                                "Fue una colonia exclusivamente minera sin plantaciones agrícolas."
                            ],
                            "correctIndex": 0,
                            "explanation": "El Nordeste fue el centro neurálgico inicial de la colonización portuguesa y el eje del imperio azucarero."
                        },
                        {
                            "question": "¿Qué simboliza el Quilombo de los Palmares en la historia de la emancipación humana?",
                            "options": [
                                "Una prisión militar para soldados amotinados.",
                                "La mayor república cimarrona autónoma de las Américas que resistió un siglo defendiendo la libertad comunitaria.",
                                "Una compañía comercial de navegación transatlántica.",
                                "Un tratado diplomático firmado entre Francia y España."
                            ],
                            "correctIndex": 1,
                            "explanation": "Palmares fue el mayor enclave libre de cimarrones que demostró la viabilidad de una sociedad sin esclavitud."
                        },
                        {
                            "question": "¿Qué manifestación poética y plástica floreció en las ferias campesinas del Sertão?",
                            "options": [
                                "La literatura de cordel ilustrada con xilografías populares talladas en madera.",
                                "La ópera barroca en lengua alemana.",
                                "El teatro de títeres mecánicos movidos por vapor.",
                                "Los madrigales renacentistas en latín clásico."
                            ],
                            "correctIndex": 0,
                            "explanation": "La literatura de cordel con sus folletos rimados y xilografías es la voz poética esencial del campesinado del Nordeste."
                        }
                    ]
                }
            }
        }
    }

    # Verify word counts for all stories
    for path, sobj in stories.items():
        wc = count_words(sobj)
        print(f"stories/{path}.json: {wc} words")
        assert 650 <= wc <= 825, f"WARNING: Story {path} word count {wc} out of range [650, 825]!"
        write_json(f"stories/{path}.json", sobj)

    # 6. Exercises
    def make_exercises():
        # Core b2-30-01 to 05
        core_ex = {
            "b2-30-01": [
                {
                    "id": "b2-30-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-adversativo"],
                    "question": "¿Qué marcador adversativo introduce un obstáculo superado sin anular la afirmación principal?",
                    "options": [
                        "Sin embargo",
                        "Por consiguiente",
                        "Es decir",
                        "En primer lugar"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-adversativo"],
                    "sentence": "El terreno era árido y hostil; no __, los rebeldes resistieron con heroísmo inquebrantable.",
                    "answer": "obstante",
                    "english": "The terrain was arid and hostile; nevertheless, the rebels resisted with unshakeable heroism."
                },
                {
                    "id": "b2-30-01.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-adversativo"],
                    "pairs": [
                        ["sin embargo", "objeción o límite sustantivo estándar"],
                        ["no obstante", "contraste formal de alta prestancia"],
                        ["con todo", "superación de múltiples dificultades previas"],
                        ["aun así", "persistencia a pesar de los reveses"]
                    ]
                },
                {
                    "id": "b2-30-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-adversativo"],
                    "sentence": "Las fuerzas regulares sufrieron bajas considerables; con __, continuaron el asedio de la ciudadela.",
                    "answer": "todo",
                    "english": "Regular forces suffered considerable casualties; even so, they continued the siege of the citadel."
                },
                {
                    "id": "b2-30-01.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-30-vocab"],
                    "question": "¿Qué sustantivo designa una rivalidad, incompatibilidad u oposición irreconciliable entre doctrinas?",
                    "options": [
                        "El antagonismo",
                        "El preámbulo",
                        "La digresión",
                        "El corolario"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la famosa sentencia de Euclides da Cunha que sintetiza la resistencia del hombre del sertão?",
                    "options": [
                        "El sertanejo es un soñador ingenuo.",
                        "El sertanejo es, ante todo, un fuerte, modelado por la dureza de la tierra.",
                        "El campesino debe someterse a la voluntad de la capital.",
                        "La caatinga es un paraíso fértil sin dificultades."
                    ],
                    "correct": 1
                }
            ],
            "b2-30-02": [
                {
                    "id": "b2-30-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-exclusivo"],
                    "question": "¿Qué conector sustitutivo formal impone la opción verdadera tras una negación previa categórica?",
                    "options": [
                        "Antes bien",
                        "Por ende",
                        "O sea",
                        "Asimismo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-exclusivo"],
                    "sentence": "Los sertanejos no capitularon ante el asedio; por el __, combatieron hasta el último cartucho.",
                    "answer": "contrario",
                    "english": "The sertanejos did not surrender to the siege; on the contrary, they fought until the last cartridge."
                },
                {
                    "id": "b2-30-02.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-exclusivo"],
                    "pairs": [
                        ["por el contrario", "sustitución tajante tras negación"],
                        ["al contrario", "oposición diametral de términos"],
                        ["antes bien", "matización correctiva en registro culto"],
                        ["muy al contrario", "refuerzo enfático de la antítesis"]
                    ]
                },
                {
                    "id": "b2-30-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-exclusivo"],
                    "sentence": "No se trataba de una turba fanática; antes __, era un pueblo despojado que defendía su dignidad.",
                    "answer": "bien",
                    "english": "It was not a fanatical mob; rather, it was a dispossessed people defending their dignity."
                },
                {
                    "id": "b2-30-02.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-30-vocab"],
                    "question": "¿Qué verbo formal expresa la acción de contradecir, desmentir o combatir con argumentos una afirmación?",
                    "options": [
                        "Impugnar",
                        "Soslayar",
                        "Pormenorizar",
                        "Recapitular"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién fue el carismático líder espiritual que fundó la ciudadela comunal de Canudos?",
                    "options": [
                        "Virgulino Ferreira Lampião",
                        "Antônio Conselheiro",
                        "Tomé de Sousa",
                        "Domingos Jorge Velho"
                    ],
                    "correct": 1
                }
            ],
            "b2-30-03": [
                {
                    "id": "b2-30-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-restriccion-concesiva"],
                    "question": "¿Cuál es la función del marcador 'ahora bien' en un razonamiento complejo?",
                    "options": [
                        "Anunciar la fecha exacta de un suceso histórico.",
                        "Introducir una salvedad o advertencia sustantiva sin desestimar la premisa precedente.",
                        "Cerrar definitivamente un texto literario.",
                        "Expresar indiferencia total hacia los hechos."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-30-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-restriccion-concesiva"],
                    "sentence": "La constitución proclamaba la igualdad universal; ahora __, mantuvo la marginación de los libertos.",
                    "answer": "bien",
                    "english": "The constitution proclaimed universal equality; now then, it maintained the marginalization of freedmen."
                },
                {
                    "id": "b2-30-03.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-restriccion-concesiva"],
                    "pairs": [
                        ["ahora bien", "introducción de salvedad sustantiva"],
                        ["eso sí", "matiz restrictivo ágil en prosa culta"],
                        ["bien es verdad que", "concesión preliminar enfática"],
                        ["si bien", "concesión factual en modo indicativo"]
                    ]
                },
                {
                    "id": "b2-30-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-restriccion-concesiva"],
                    "sentence": "Aprobaron la ley de abolición en 1888; eso __, sin garantizar tierras ni educación a los campesinos.",
                    "answer": "sí",
                    "english": "They approved the abolition law in 1888; mind you, without guaranteeing land or education to peasants."
                },
                {
                    "id": "b2-30-03.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-30-vocab"],
                    "question": "¿Qué verbo formal designa la acción de suavizar o graduar un juicio para no ser absolutista?",
                    "options": [
                        "Matizar",
                        "Devorar",
                        "Diezmar",
                        "Emancipar"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuántas expediciones militares debió enviar el gobierno brasileño para doblegar Canudos?",
                    "options": [
                        "Una sola expedición de caballería ligera.",
                        "Cuatro expediciones sucesivas, requiriendo diez mil soldados y artillería pesada en la última.",
                        "Ninguna, porque los rebeldes se rindieron de inmediato.",
                        "Doce flotas marítimas de guerra."
                    ],
                    "correct": 1
                }
            ],
            "b2-30-04": [
                {
                    "id": "b2-30-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-contraposicion-ponderada"],
                    "question": "¿Qué marcador permite contraponer de modo simétrico dos realidades geográficas divergentes?",
                    "options": [
                        "En cambio",
                        "Por consiguiente",
                        "En resumen",
                        "De este modo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraposicion-ponderada"],
                    "sentence": "El litoral concentraba la riqueza azucarera; en __, el interior sertanejo vivía en la escasez hídrica.",
                    "answer": "cambio",
                    "english": "The coast concentrated sugar wealth; by contrast, the sertanejo interior lived in water scarcity."
                },
                {
                    "id": "b2-30-04.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-contraposicion-ponderada"],
                    "pairs": [
                        ["en cambio", "contrapeso simétrico estándar"],
                        ["en contrapartida", "equilibrio de aspectos divergentes"],
                        ["por contra", "giro formal de oposición paralela"],
                        ["mientras que", "confrontación sintáctica directa"]
                    ]
                },
                {
                    "id": "b2-30-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraposicion-ponderada"],
                    "sentence": "Los terratenientes contaban con influencias políticas; en __, los peones carecían de derechos civiles.",
                    "answer": "contrapartida",
                    "english": "Landowners had political influence; in contrast, laborers lacked civil rights."
                },
                {
                    "id": "b2-30-04.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-30-vocab"],
                    "question": "¿Qué sustantivo describe la falta de proporción o desequilibrio entre dos partes confrontadas?",
                    "options": [
                        "La asimetría",
                        "El corolario",
                        "La paráfrasis",
                        "El exordio"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cómo finalizó la resistencia de Canudos tras meses de bombardeos incesantes?",
                    "options": [
                        "Con la rendición pacífica de los oficiales y el perdón judicial.",
                        "Con cuatro defensores agonizantes combatiendo hasta el último proyectil frente a todo un ejército.",
                        "Con la victoria militar campesina y la independencia de Bahía.",
                        "Con la huida de toda la población hacia los Andes peruanos."
                    ],
                    "correct": 1
                }
            ],
            "b2-30-05": [
                {
                    "id": "b2-30-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-oposicion-atenuada"],
                    "question": "¿Cuál es la función del marcador 'pese a ello' al inicio de una oración?",
                    "options": [
                        "Retomar adversidades previas para enfatizar la superación y constancia del sujeto.",
                        "Anunciar la derrota definitiva e irreversible de un proyecto.",
                        "Aclarar el significado de un término gramatical.",
                        "Pedir silencio en una asamblea deliberativa."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-oposicion-atenuada"],
                    "sentence": "Pese a __, las comunidades campesinas retornaron a sus tierras para volver a levantar sus hogares.",
                    "answer": "ello",
                    "english": "Despite this, peasant communities returned to their lands to rebuild their homes once more."
                },
                {
                    "id": "b2-30-05.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-oposicion-atenuada"],
                    "pairs": [
                        ["pese a ello", "reanudación con entereza tras infortunios"],
                        ["aun con todo", "evaluación ponderada del sufrimiento"],
                        ["si bien", "concesión serena en modo indicativo"],
                        ["no obstante ello", "fórmula culta de persistencia activa"]
                    ]
                },
                {
                    "id": "b2-30-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-oposicion-atenuada"],
                    "sentence": "Aun con __ el sufrimiento padecido en la guerra, la cultura popular nordestina conservó su vigor.",
                    "answer": "todo",
                    "english": "Even with all the suffering endured in the war, northeastern popular culture retained its vigor."
                },
                {
                    "id": "b2-30-05.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-30-vocab"],
                    "question": "¿Qué cualidad humana designa la capacidad de sobreponerse a traumas graves y salir fortalecido?",
                    "options": [
                        "La resiliencia",
                        "La apatía",
                        "La digresión",
                        "La vacilación"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la lección perdurable que 'Los sertones' legó al pensamiento latinoamericano?",
                    "options": [
                        "Que las armas de fuego son la única vía para civilizar a las comunidades rurales.",
                        "Una denuncia de la barbarie del progreso impuesto por la fuerza y el rescate de la dignidad del hombre del interior.",
                        "Que los campesinos debían renunciar a su religión para progresar.",
                        "Que la geografía no influye en absoluto en el carácter humano."
                    ],
                    "correct": 1
                }
            ],
            "b2-30-consolidation": [
                {
                    "id": "b2-30-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-adversativo"],
                    "question": "¿Qué marcador adversativo se aísla habitualmente entre comas en prosa formal culta?",
                    "options": [
                        "No obstante",
                        "Por consiguiente",
                        "Puesto que",
                        "A fin de que"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraste-exclusivo"],
                    "sentence": "No buscaron el enriquecimiento egoísta; antes __, consagraron su vida al bienestar comunitario.",
                    "answer": "bien",
                    "english": "They did not seek selfish enrichment; rather, they devoted their lives to community well-being."
                },
                {
                    "id": "b2-30-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-restriccion-concesiva"],
                    "question": "¿Qué marcador introduce una salvedad de forma elegante y mesurada en el debate ensayístico?",
                    "options": [
                        "Ahora bien",
                        "O sea",
                        "A saber",
                        "En primer término"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-contraposicion-ponderada"],
                    "sentence": "El ejército poseía artillería de última generación; en __, los sertanejos contaban con el conocimiento del monte.",
                    "answer": "cambio",
                    "english": "The army possessed state-of-the-art artillery; in contrast, the sertanejos possessed knowledge of the wilderness."
                },
                {
                    "id": "b2-30-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-oposicion-atenuada"],
                    "question": "¿Qué expresión sintetiza adversidades pasadas para enfatizar la entereza presente?",
                    "options": [
                        "Pese a ello",
                        "Por ejemplo",
                        "A saber",
                        "En suma"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-30-consolidation.ex06",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-30-vocab"],
                    "pairs": [
                        ["antagonismo", "rivalidad u oposición frontal"],
                        ["impugnar", "combatir o refutar una afirmación"],
                        ["asimetría", "desequilibrio o falta de proporción"],
                        ["resiliencia", "capacidad de sobreponerse al dolor"]
                    ]
                },
                {
                    "id": "b2-30-consolidation.ex07",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-restriccion-concesiva"],
                    "sentence": "Se firmaron acuerdos comerciales preliminares; eso __, sujetos a la ratificación del senado.",
                    "answer": "sí",
                    "english": "Preliminary trade agreements were signed; mind you, subject to ratification by the senate."
                },
                {
                    "id": "b2-30-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué valor histórico simboliza la epopeya relatada en 'Los sertones'?",
                    "options": [
                        "La victoria total de la tecnología militar sobre la poesía oral.",
                        "La dignidad inquebrantable de los pueblos desposeídos frente a la incomprensión de las élites centrales.",
                        "La necesidad de deforestar todas las selvas tropicales.",
                        "La superioridad de los ejércitos mercenarios en el combate."
                    ],
                    "correct": 1
                }
            ]
        }

        # Regional b2-brasilnordeste-01 to 05
        reg_ex = {
            "b2-brasilnordeste-01": [
                {
                    "id": "b2-brasilnordeste-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-adjetivacion-estilo"],
                    "question": "¿Qué efecto estilístico produce anteponer el adjetivo al sustantivo en 'suntuoso templo'?",
                    "options": [
                        "Aporta un matiz valorativo, emotivo y literario que resalta la impresión estética del hablante.",
                        "Convierte la oración en interrogativa directa.",
                        "Indica una falta de concordancia gramatical grave.",
                        "Obliga al uso del modo subjuntivo en el verbo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-adjetivacion-estilo"],
                    "sentence": "La iglesia de San Francisco exhibe una __ talla dorada que deslumbra a los visitantes.",
                    "answer": "suntuosa",
                    "english": "The church of Saint Francis exhibits a sumptuous gilded carving that dazzles visitors."
                },
                {
                    "id": "b2-brasilnordeste-01.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["nordeste-adjetivacion-estilo"],
                    "pairs": [
                        ["adjetivo antepuesto", "suntuoso templo barroco"],
                        ["adjetivo pospuesto", "azulejo policromado portugués"],
                        ["adjetivo gentilicio", "arquitectura colonial bahiana"],
                        ["adjetivo relacional", "patrimonio urbanístico protegido"]
                    ]
                },
                {
                    "id": "b2-brasilnordeste-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-adjetivacion-estilo"],
                    "sentence": "Las fachadas del Pelourinho conservan una pátina __ que atestigua siglos de historia atlántica.",
                    "answer": "centenaria",
                    "english": "The facades of Pelourinho preserve a centuries-old patina that attests to centuries of Atlantic history."
                },
                {
                    "id": "b2-brasilnordeste-01.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilnordeste-vocab"],
                    "question": "¿Qué pieza vidriada de cerámica pintada decora profusamente los conventos coloniales de Bahía?",
                    "options": [
                        "El azulejo",
                        "El adoquín",
                        "El morro",
                        "El quebracho"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Por qué se conoce a Salvador de Bahía con el título de 'la Roma Negra'?",
                    "options": [
                        "Porque el papa visitó la ciudad todos los años desde su fundación.",
                        "Por constituir el epicentro cultural, religioso y demográfico más profundamente africanizado de las Américas.",
                        "Porque sus edificios fueron construidos con mármol negro de los Alpes.",
                        "Porque albergaba el mayor cuartel militar del Imperio romano en América."
                    ],
                    "correct": 1
                }
            ],
            "b2-brasilnordeste-02": [
                {
                    "id": "b2-brasilnordeste-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-subordinadas-finales"],
                    "question": "¿Qué modo verbal exige la locución conjuntiva final 'a fin de que'?",
                    "options": [
                        "Modo subjuntivo siempre",
                        "Modo indicativo de presente",
                        "Infinitivo simple únicamente",
                        "Participio pasivo invariable"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-subordinadas-finales"],
                    "sentence": "Los capoeiristas disimularon la lucha como danza con el __ de que los amos no la censuraran.",
                    "answer": "objeto",
                    "english": "Capoeiristas disguised fighting as dance with the purpose that the masters would not censor it."
                },
                {
                    "id": "b2-brasilnordeste-02.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["nordeste-subordinadas-finales"],
                    "pairs": [
                        ["a fin de que", "locución final de alto registro formal"],
                        ["con el objeto de que", "precisión teleológica institucional"],
                        ["para que", "nexo final neutro y extendido"],
                        ["con miras a que", "orientación proyectual o de futuro"]
                    ]
                },
                {
                    "id": "b2-brasilnordeste-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-subordinadas-finales"],
                    "sentence": "Los sacerdotes bendicen el terreiro a fin de que los orixás __ su protección sobre la comunidad.",
                    "answer": "derramen",
                    "english": "The priests bless the terreiro in order that the orixás may pour their protection upon the community."
                },
                {
                    "id": "b2-brasilnordeste-02.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilnordeste-vocab"],
                    "question": "¿Cómo se llama el instrumento musical de arco tensado con una calabaza resonadora en la capoeira?",
                    "options": [
                        "El berimbau",
                        "El atabaque",
                        "El pandeiro",
                        "La guampa"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué divinidad del Candomblé es la reina maternal de las aguas del mar honrada el 2 de febrero?",
                    "options": [
                        "Iemanjá",
                        "Xangô",
                        "Ogum",
                        "Oxalá"
                    ],
                    "correct": 0
                }
            ],
            "b2-brasilnordeste-03": [
                {
                    "id": "b2-brasilnordeste-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-condicionales-irreales"],
                    "question": "En 'De haber llovido a tiempo, los campesinos no habrían emigrado', ¿cuál es el sentido de la prótasis?",
                    "options": [
                        "Una condición futura muy probable.",
                        "Una hipótesis irreal en el pasado sobre un hecho que no se produjo.",
                        "Una orden perentoria en modo imperativo.",
                        "Una certeza científica demostrada en laboratorio."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-brasilnordeste-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-condicionales-irreales"],
                    "sentence": "De haber __ agua suficiente en los aljibes, el ganado no habría perecido en la caatinga.",
                    "answer": "habido",
                    "english": "Had there been sufficient water in the cisterns, the cattle would not have perished in the caatinga."
                },
                {
                    "id": "b2-brasilnordeste-03.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["nordeste-condicionales-irreales"],
                    "pairs": [
                        ["de haber sabido", "prótasis irreal condensada con infinitivo"],
                        ["si hubiera sabido", "prótasis irreal estándar con subjuntivo"],
                        ["habría actuado", "apódosis en condicional compuesto"],
                        ["hubiera actuado", "apódosis alternativa en pluscuamperfecto"]
                    ]
                },
                {
                    "id": "b2-brasilnordeste-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-condicionales-irreales"],
                    "sentence": "Si el gobierno __ invertido en canales de riego, la sequía no habría provocado el éxodo masivo.",
                    "answer": "hubiera",
                    "english": "If the government had invested in irrigation canals, the drought would not have caused the massive exodus."
                },
                {
                    "id": "b2-brasilnordeste-03.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilnordeste-vocab"],
                    "question": "¿Cómo se denominan los folletos de poesía popular que se vendían colgados de cuerdas en el Nordeste?",
                    "options": [
                        "Literatura de cordel",
                        "Sonetos cortesanos",
                        "Crónicas de ultramar",
                        "Bandos reales"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quiénes fueron los dos líderes más célebres y temidos del Cangaço nómada en el Sertão?",
                    "options": [
                        "Lampião y Maria Bonita",
                        "Tarsila do Amaral y Oswald de Andrade",
                        "Tom Jobim y Vinicius de Moraes",
                        "Manuel da Nóbrega y José de Anchieta"
                    ],
                    "correct": 0
                }
            ],
            "b2-brasilnordeste-04": [
                {
                    "id": "b2-brasilnordeste-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-perifrasis-reiterativas"],
                    "question": "En 'Los cimarrones volvieron a edificar sus aldeas', ¿qué matiz aspectual aporta 'volver a'?",
                    "options": [
                        "La repetición de una acción tras una interrupción o destrucción previa.",
                        "El inicio repentino e impulsivo de un proceso.",
                        "La finalización definitiva de un conflicto.",
                        "La duda o inseguridad del sujeto sobre sus actos."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-perifrasis-reiterativas"],
                    "sentence": "A pesar de las ofensivas militares, la fortaleza de Palmares __ a levantarse en la cima de la sierra.",
                    "answer": "volvió",
                    "english": "Despite the military offensives, the fortress of Palmares rose up again on the summit of the range."
                },
                {
                    "id": "b2-brasilnordeste-04.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["nordeste-perifrasis-reiterativas"],
                    "pairs": [
                        ["volver a + infinitivo", "reiteración tras interrupción previa"],
                        ["seguir + gerundio", "continuidad ininterrumpida en el tiempo"],
                        ["continuar + gerundio", "persistencia activa de un proceso"],
                        ["reiterar + sustantivo", "reafirmación léxica formal"]
                    ]
                },
                {
                    "id": "b2-brasilnordeste-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-perifrasis-reiterativas"],
                    "sentence": "Las comunidades quilombolas __ defendiendo hoy en día la propiedad colectiva de sus tierras ancestrales.",
                    "answer": "siguen",
                    "english": "Quilombo communities continue defending the collective ownership of their ancestral lands today."
                },
                {
                    "id": "b2-brasilnordeste-04.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilnordeste-vocab"],
                    "question": "¿Qué término histórico designa en Brasil a los poblados autónomos fundados por esclavizados fugitivos?",
                    "options": [
                        "Quilombos o mocambos",
                        "Favelas",
                        "Reducciones",
                        "Corregimientos"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién fue el legendario líder palmarino asesinado el 20 de noviembre de 1695?",
                    "options": [
                        "Zumbi dos Palmares",
                        "Ganga Zumba",
                        "Domingos Jorge Velho",
                        "Luiz Gonzaga"
                    ],
                    "correct": 0
                }
            ],
            "b2-brasilnordeste-05": [
                {
                    "id": "b2-brasilnordeste-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-conectores-causales-complejos"],
                    "question": "¿Qué conector causal pertenece al registro formal y académico para fundamentar una resolución legal?",
                    "options": [
                        "Habida cuenta de que",
                        "Porque sí",
                        "Ya que nada",
                        "Como que"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-conectores-causales-complejos"],
                    "sentence": "Se promovió la Ley de Cuotas, habida __ de que persistían desigualdades estructurales históricas.",
                    "answer": "cuenta",
                    "english": "The Quota Law was promoted, taking into account that historic structural inequalities persisted."
                },
                {
                    "id": "b2-brasilnordeste-05.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["nordeste-conectores-causales-complejos"],
                    "pairs": [
                        ["habida cuenta de que", "justificación jurídica o sociológica formal"],
                        ["por cuanto", "causa explicativa de rango formal"],
                        ["en razón de que", "fundamento causal deliberativo"],
                        ["dado que", "causa constatada de uso ensayístico"]
                    ]
                },
                {
                    "id": "b2-brasilnordeste-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-conectores-causales-complejos"],
                    "sentence": "El mito de la democracia racial fue impugnado __ cuanto ocultaba la exclusión social de los afrodescendientes.",
                    "answer": "por",
                    "english": "The myth of racial democracy was challenged inasmuch as it concealed the social exclusion of Afro-descendants."
                },
                {
                    "id": "b2-brasilnordeste-05.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilnordeste-vocab"],
                    "question": "¿Qué sociólogo brasileño formuló en 1933 la teoría clásica de la 'democracia racial' en Casa-Grande & Senzala?",
                    "options": [
                        "Gilberto Freyre",
                        "Florestan Fernandes",
                        "Abdias do Nascimento",
                        "Darcy Ribeiro"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué porcentaje mínimo de vacantes reservó la Ley de Cuotas de 2012 en las universidades federales?",
                    "options": [
                        "El diez por ciento.",
                        "El cincuenta por ciento para egresados de escuelas públicas con cuotas étnico-raciales.",
                        "El cien por ciento.",
                        "El cinco por ciento exclusivamente para deportistas."
                    ],
                    "correct": 1
                }
            ],
            "b2-brasilnordeste-consolidation": [
                {
                    "id": "b2-brasilnordeste-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-adjetivacion-estilo"],
                    "question": "¿Qué adjetivo califica de manera exacta un elemento que combina armónicamente influencias de diferentes religiones o culturas?",
                    "options": [
                        "Sincrético",
                        "Monolítico",
                        "Efímero",
                        "Autócrata"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-subordinadas-finales"],
                    "sentence": "Se preservaron los terreiros sagrados con el __ de que las futuras generaciones custodien el axé ancestral.",
                    "answer": "objeto",
                    "english": "The sacred terreiros were preserved so that future generations may safeguard the ancestral axé."
                },
                {
                    "id": "b2-brasilnordeste-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-condicionales-irreales"],
                    "question": "En la hipótesis 'De no haber mediado la literatura de cordel, muchas leyendas habrían muerto', ¿qué fórmula se utiliza?",
                    "options": [
                        "De + infinitivo compuesto en función de prótasis contrafáctica.",
                        "Perífrasis obligativa con tener que.",
                        "Futuro simple de conjetura.",
                        "Modo imperativo negativo plural."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-perifrasis-reiterativas"],
                    "sentence": "Tras la caída de Canudos, los campesinos __ a sembrar sus campos desafiando a la sequía implacable.",
                    "answer": "volvieron",
                    "english": "After the fall of Canudos, the peasants returned to planting their fields, defying the relentless drought."
                },
                {
                    "id": "b2-brasilnordeste-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["nordeste-conectores-causales-complejos"],
                    "question": "¿Qué conector causal es sinónimo culto de 'puesto que' en exposiciones sociológicas formales?",
                    "options": [
                        "Por cuanto",
                        "A fin de que",
                        "Con tal de que",
                        "Sin embargo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilnordeste-consolidation.ex06",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilnordeste-vocab"],
                    "pairs": [
                        ["terreiro", "templo ceremonial de candomblé"],
                        ["orixá", "divinidad cósmica yoruba"],
                        ["xilografía", "grabado en madera para ilustrar cordel"],
                        ["quilombo", "poblado libre de cimarrones fugitivos"]
                    ]
                },
                {
                    "id": "b2-brasilnordeste-consolidation.ex07",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["nordeste-subordinadas-finales"],
                    "sentence": "Instituyeron el Día de la Conciencia Negra a fin de que la sociedad __ las deudas históricas con los afrodescendientes.",
                    "answer": "reconozca",
                    "english": "They instituted Black Consciousness Day so that society may recognize historical debts to Afro-descendants."
                },
                {
                    "id": "b2-brasilnordeste-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué síntesis fundamental define la dignidad y la identidad del Nordeste de Brasil?",
                    "options": [
                        "La resistencia espiritual del Candomblé, la epopeya de los Palmares y la entereza del campesinado del Sertão.",
                        "El sometimiento sumiso a los dictados de los coroneles latifundistas.",
                        "El rechazo absoluto de cualquier expresión de música o danza popular.",
                        "La renuncia a la memoria histórica para imitar a las metrópolis europeas."
                    ],
                    "correct": 0
                }
            ]
        }

        for stem, exs in core_ex.items():
            write_json(f"exercises/b2/{stem}-ex.json", {"lesson": stem, "exercises": exs})

        for stem, exs in reg_ex.items():
            write_json(f"exercises/b2/{stem}-ex.json", {"lesson": stem, "exercises": exs})

    make_exercises()

    # 7. Lessons
    core_lessons = {
        "b2-30-01": {
            "id": "lesson.b2.30.01",
            "title": "Adversative Contrast: sin embargo, no obstante, con todo",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-30.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-30-01-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-30-01-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-30-01-ex.json",
                    "exerciseRefs": [f"b2-30-01.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-30-02": {
            "id": "lesson.b2.30.02",
            "title": "Exclusive Contrast: por el contrario, al contrario, antes bien",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-30.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-30-02-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-30-02-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-30-02-ex.json",
                    "exerciseRefs": [f"b2-30-02.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-30-03": {
            "id": "lesson.b2.30.03",
            "title": "Concessive Restriction: ahora bien, eso sí, bien es verdad que",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-30.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-30-03-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-30-03-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-30-03-ex.json",
                    "exerciseRefs": [f"b2-30-03.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-30-04": {
            "id": "lesson.b2.30.04",
            "title": "Counterbalanced Contrast: en cambio, en contrapartida, por contra",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-30.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-30-04-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-30-04-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-30-04-ex.json",
                    "exerciseRefs": [f"b2-30-04.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-30-05": {
            "id": "lesson.b2.30.05",
            "title": "Attenuated Opposition: si bien, pese a ello, aun con todo",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-30.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-30-05-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-30-05-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-30-05-ex.json",
                    "exerciseRefs": [f"b2-30-05.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-30-consolidation": {
            "id": "lesson.b2.30.consolidation",
            "title": "Consolidation: Discourse Markers III: Contrast & Restriction",
            "level": "B2",
            "sections": [
                {
                    "type": "goal",
                    "items": [
                        "Articular contrastes adversativos y sustitutivos rigurosos en debates académicos formales.",
                        "Introducir restricciones concesivas y contrapesos equilibrados sin debilitar la tesis.",
                        "Integrar el léxico especializado de la dialéctica, la controversia y la resiliencia cívica."
                    ]
                },
                {"type": "recycle", "count": 3},
                {
                    "type": "exercise-group",
                    "title": "Review",
                    "ref": "exercises/b2/b2-30-consolidation-ex.json",
                    "exerciseRefs": [f"b2-30-consolidation.ex0{i}" for i in range(1, 9)]
                },
                {
                    "type": "checklist",
                    "items": [
                        "Domino los conectores adversativos 'sin embargo', 'no obstante' y 'con todo'.",
                        "Aplico los sustitutivos 'por el contrario' y 'antes bien' tras negación categórica.",
                        "Manejo las restricciones concesivas 'ahora bien' y 'eso sí' en redacción de ensayos.",
                        "Construyo balances comparativos ponderados con 'en cambio' y 'en contrapartida'.",
                        "Expreso superación ante la adversidad aplicando 'pese a ello' y 'aun con todo'."
                    ]
                }
            ]
        }
    }

    for stem, ldata in core_lessons.items():
        write_json(f"lessons/b2/{stem}.json", ldata)

    reg_lessons = {
        "b2-brasilnordeste-01": {
            "id": "lesson.b2.brasilnordeste.01",
            "title": "Salvador de Bahía y el Pelourinho: La Roma Negra",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilnordeste-01.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilnordeste-01-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilnordeste-01-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilnordeste-01-ex.json",
                    "exerciseRefs": [f"b2-brasilnordeste-01.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilnordeste-02": {
            "id": "lesson.b2.brasilnordeste.02",
            "title": "El candomblé, la capoeira y los orixás en la vida cotidiana",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilnordeste-02.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilnordeste-02-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilnordeste-02-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilnordeste-02-ex.json",
                    "exerciseRefs": [f"b2-brasilnordeste-02.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilnordeste-03": {
            "id": "lesson.b2.brasilnordeste.03",
            "title": "El Sertão semiárido, el cangaço y la literatura de cordel",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilnordeste-03.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilnordeste-03-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilnordeste-03-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilnordeste-03-ex.json",
                    "exerciseRefs": [f"b2-brasilnordeste-03.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilnordeste-04": {
            "id": "lesson.b2.brasilnordeste.04",
            "title": "El Quilombo de los Palmares y la gesta heroica de Zumbi",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilnordeste-04.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilnordeste-04-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilnordeste-04-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilnordeste-04-ex.json",
                    "exerciseRefs": [f"b2-brasilnordeste-04.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilnordeste-05": {
            "id": "lesson.b2.brasilnordeste.05",
            "title": "El dilema de la democracia racial y la acción afirmativa",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilnordeste-05.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilnordeste-05-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilnordeste-05-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilnordeste-05-ex.json",
                    "exerciseRefs": [f"b2-brasilnordeste-05.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilnordeste-consolidation": {
            "id": "lesson.b2.brasilnordeste.consolidation",
            "title": "Consolidación: Brasil II: El Nordeste, alma afrobrasileña y Sertão",
            "level": "B2",
            "sections": [
                {
                    "type": "goal",
                    "items": [
                        "Comprender la centralidad del legado afrobrasileño y la resistencia cultural en Bahía y los Quilombos.",
                        "Dominar oraciones finales complejas, condicionales irreales y perífrasis aspectuales de continuidad.",
                        "Analizar críticamente el debate sobre las desigualdades étnico-raciales y las políticas de cuotas afirmativas."
                    ]
                },
                {"type": "recycle", "count": 3},
                {
                    "type": "exercise-group",
                    "title": "Review",
                    "ref": "exercises/b2/b2-brasilnordeste-consolidation-ex.json",
                    "exerciseRefs": [f"b2-brasilnordeste-consolidation.ex0{i}" for i in range(1, 9)]
                },
                {
                    "type": "checklist",
                    "items": [
                        "Empleo adjetivos valorativos y descriptivos para caracterizar el patrimonio arquitectónico bahiano.",
                        "Construyo oraciones finales formales con 'a fin de que' y 'con el objeto de que' en modo subjuntivo.",
                        "Formulo hipótesis contrafácticas sobre el pasado con 'de haber + participio' y 'si hubiera + participio'.",
                        "Aplico perífrasis reiterativas ('volver a + infinitivo', 'seguir + gerundio') en relatos históricos.",
                        "Utilizo conectores causales complejos ('habida cuenta de que', 'por cuanto') en debates sociológicos."
                    ]
                }
            ]
        }
    }

    for stem, ldata in reg_lessons.items():
        write_json(f"lessons/b2/{stem}.json", ldata)

    # 8. Update curriculum/units/b2.json
    def update_curriculum(units_list):
        existing_stems = set()
        for u in units_list:
            existing_stems.update(u.get("stems", []))
        
        core_stems = [f"b2-30-0{i}" for i in range(1, 6)] + ["b2-30-consolidation"]
        reg_stems = [f"b2-brasilnordeste-0{i}" for i in range(1, 6)] + ["b2-brasilnordeste-consolidation"]

        if "b2-30-01" not in existing_stems:
            units_list.append({
                "title": "Discourse Markers III: Contrast & Restriction",
                "stems": core_stems,
                "track": "core"
            })
        if "b2-brasilnordeste-01" not in existing_stems:
            units_list.append({
                "title": "Brazil II: The Northeast, Afro-Brazilian Soul & The Sertão",
                "stems": reg_stems,
                "track": "regional"
            })
        return units_list

    update_json_file(os.path.join(LATAM_DIR, "curriculum", "units", "b2.json"), update_curriculum)
    print("Updated curriculum/units/b2.json with Unit 30!")

if __name__ == "__main__":
    main()
