# -*- coding: utf-8 -*-
"""
Fixes scripts/generate_es_latam_b2_unit28.py:
1. vocab lesson -> stem ('b2-28-01', etc.)
2. exercise lesson -> stem ('b2-28-01', etc.)
3. grammar text/tip -> content
4. grammar table -> 2 columns [spanish, english], title instead of headers
5. includes refined story texts
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
            "marcadores-ordenacion": {
                "kind": "grammar",
                "name": "marcadores-ordenacion",
                "description": "Discourse markers of ordering and enumeration such as en primer lugar, en segundo término, por último in formal registers",
                "aliases": []
            },
            "marcadores-digresion": {
                "kind": "grammar",
                "name": "marcadores-digresion",
                "description": "Markers of digression and incidental commentary including por cierto, a propósito, dicho sea de paso",
                "aliases": []
            },
            "marcadores-continuidad": {
                "kind": "grammar",
                "name": "marcadores-continuidad",
                "description": "Markers of thematic progression and transition such as pues bien, dicho esto, así las cosas",
                "aliases": []
            },
            "marcadores-distribucion": {
                "kind": "grammar",
                "name": "marcadores-distribucion",
                "description": "Distributive discourse markers including por una parte... por otra, ya... ya, bien... bien",
                "aliases": []
            },
            "marcadores-conclusion": {
                "kind": "grammar",
                "name": "marcadores-conclusion",
                "description": "Concluding and summative discourse markers such as en suma, en definitiva, en última instancia",
                "aliases": []
            },
            "b2-28-vocab": {
                "kind": "vocabulary",
                "name": "b2-28-vocab",
                "description": "Vocabulary for discourse structure, oratorical sequencing, debate, and argumentation",
                "aliases": []
            },
            "paraguay-contacto-linguistico": {
                "kind": "grammar",
                "name": "paraguay-contacto-linguistico",
                "description": "Linguistic contact features and lexical calques in Paraguayan Spanish and Guaraní bilingualism",
                "aliases": []
            },
            "paraguay-concesivas-avanzadas": {
                "kind": "grammar",
                "name": "paraguay-concesivas-avanzadas",
                "description": "Advanced concessive clauses in historical analysis with por más que, si bien, aun cuando, pese a que",
                "aliases": []
            },
            "paraguay-voz-pasiva-estilo": {
                "kind": "grammar",
                "name": "paraguay-voz-pasiva-estilo",
                "description": "Stylistic passive structures in historiographical discourse including passive with ser, reflexive passive, and impersonal se",
                "aliases": []
            },
            "paraguay-adverbiales-lugar": {
                "kind": "grammar",
                "name": "paraguay-adverbiales-lugar",
                "description": "Complex locative adverbials in descriptive prose such as tierra adentro, río abajo, en los confines de",
                "aliases": []
            },
            "paraguay-subordinadas-adjetivas": {
                "kind": "grammar",
                "name": "paraguay-subordinadas-adjetivas",
                "description": "Relative clauses with complex prepositions in cultural writing including mediante el cual, en virtud de los cuales",
                "aliases": []
            },
            "b2-paraguay-vocab": {
                "kind": "vocabulary",
                "name": "b2-paraguay-vocab",
                "description": "Vocabulary for Paraguayan culture, Guaraní bilingualism, Jesuit missions, Chaco wilderness, and folklore",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 28")

    # 2. Update grammar-titles.json
    def update_grammar_titles(titles):
        new_titles = {
            "marcadores-ordenacion": "discourse markers of ordering and enumeration",
            "marcadores-digresion": "markers of digression and incidental commentary",
            "marcadores-continuidad": "markers of thematic progression and transition",
            "marcadores-distribucion": "distributive discourse markers",
            "marcadores-conclusion": "concluding and summative discourse markers",
            "paraguay-contacto-linguistico": "linguistic contact features and lexical calques",
            "paraguay-concesivas-avanzadas": "advanced concessive clauses in historical analysis",
            "paraguay-voz-pasiva-estilo": "stylistic passive structures in historiographical discourse",
            "paraguay-adverbiales-lugar": "complex locative adverbials in descriptive prose",
            "paraguay-subordinadas-adjetivas": "relative clauses with complex prepositions in cultural writing"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 28")

    # 3. Vocabulary files
    vocab_data = {
        "b2-28-01": {
            "id": "vocab.b2.28.01",
            "lesson": "b2-28-01",
            "title": "Discourse Ordering and Sequencing",
            "words": [
                {"lemma": "preámbulo", "translation": "preamble", "pos": "noun"},
                {"lemma": "epílogo", "translation": "epilogue", "pos": "noun"},
                {"lemma": "sucinto", "translation": "succinct", "pos": "adjective"},
                {"lemma": "dilucidar", "translation": "to elucidate", "pos": "verb"},
                {"lemma": "pormenorizar", "translation": "to detail / itemize", "pos": "verb"},
                {"lemma": "postrimería", "translation": "final period / closing stage", "pos": "noun"}
            ]
        },
        "b2-28-02": {
            "id": "vocab.b2.28.02",
            "lesson": "b2-28-02",
            "title": "Digression and Incidental Commentary",
            "words": [
                {"lemma": "digresión", "translation": "digression", "pos": "noun"},
                {"lemma": "paréntesis", "translation": "parenthesis / interlude", "pos": "noun"},
                {"lemma": "inciso", "translation": "clause / incidental remark", "pos": "noun"},
                {"lemma": "soslayar", "translation": "to sidestep / skirt", "pos": "verb"},
                {"lemma": "tangencial", "translation": "tangential", "pos": "adjective"},
                {"lemma": "apostilla", "translation": "marginal note / gloss", "pos": "noun"}
            ]
        },
        "b2-28-03": {
            "id": "vocab.b2.28.03",
            "lesson": "b2-28-03",
            "title": "Continuity and Thematic Transition",
            "words": [
                {"lemma": "hilo conductor", "translation": "common thread / guiding theme", "pos": "noun"},
                {"lemma": "articulación", "translation": "linkage / structuring", "pos": "noun"},
                {"lemma": "hilvanar", "translation": "to link together / weave", "pos": "verb"},
                {"lemma": "encadenamiento", "translation": "concatenation / sequencing", "pos": "noun"},
                {"lemma": "transición", "translation": "transition", "pos": "noun"},
                {"lemma": "cohesión", "translation": "cohesion", "pos": "noun"}
            ]
        },
        "b2-28-04": {
            "id": "vocab.b2.28.04",
            "lesson": "b2-28-04",
            "title": "Distribution and Parallel Arguments",
            "words": [
                {"lemma": "dicotomía", "translation": "dichotomy", "pos": "noun"},
                {"lemma": "disyuntiva", "translation": "dilemma / alternative", "pos": "noun"},
                {"lemma": "paralelismo", "translation": "parallelism", "pos": "noun"},
                {"lemma": "contrapartida", "translation": "counterpart / offset", "pos": "noun"},
                {"lemma": "bifurcación", "translation": "branching / bifurcation", "pos": "noun"},
                {"lemma": "antítesis", "translation": "antithesis", "pos": "noun"}
            ]
        },
        "b2-28-05": {
            "id": "vocab.b2.28.05",
            "lesson": "b2-28-05",
            "title": "Synthesis and Concluding Evaluation",
            "words": [
                {"lemma": "recapitulación", "translation": "recapitulation", "pos": "noun"},
                {"lemma": "corolario", "translation": "corollary", "pos": "noun"},
                {"lemma": "desenlace", "translation": "outcome / denouement", "pos": "noun"},
                {"lemma": "sintetizar", "translation": "to synthesize", "pos": "verb"},
                {"lemma": "concluyente", "translation": "conclusive", "pos": "adjective"},
                {"lemma": "balance", "translation": "overall assessment / balance", "pos": "noun"}
            ]
        },
        "b2-paraguay-01": {
            "id": "vocab.b2.paraguay.01",
            "lesson": "b2-paraguay-01",
            "title": "Guaraní Bilingualism and Jopara",
            "words": [
                {"lemma": "bilingüismo", "translation": "bilingualism", "pos": "noun"},
                {"lemma": "sustrato", "translation": "substratum", "pos": "noun"},
                {"lemma": "calco", "translation": "loan translation / calque", "pos": "noun"},
                {"lemma": "diglosia", "translation": "diglossia", "pos": "noun"},
                {"lemma": "lengua materna", "translation": "mother tongue", "pos": "noun"},
                {"lemma": "autóctono", "translation": "autochthonous / indigenous", "pos": "adjective"}
            ]
        },
        "b2-paraguay-02": {
            "id": "vocab.b2.paraguay.02",
            "lesson": "b2-paraguay-02",
            "title": "Jesuit Reductions and Indigenous Baroque",
            "words": [
                {"lemma": "reducción", "translation": "Jesuit mission settlement", "pos": "noun"},
                {"lemma": "barroco", "translation": "baroque", "pos": "adjective"},
                {"lemma": "cantería", "translation": "stonework / masonry", "pos": "noun"},
                {"lemma": "partitura", "translation": "musical score", "pos": "noun"},
                {"lemma": "tallista", "translation": "woodcarver / sculptor", "pos": "noun"},
                {"lemma": "vestigio", "translation": "vestige / trace", "pos": "noun"}
            ]
        },
        "b2-paraguay-03": {
            "id": "vocab.b2.paraguay.03",
            "lesson": "b2-paraguay-03",
            "title": "War of the Triple Alliance and Resilience",
            "words": [
                {"lemma": "devastación", "translation": "devastation", "pos": "noun"},
                {"lemma": "diezmar", "translation": "to decimate", "pos": "verb"},
                {"lemma": "reconstrucción", "translation": "reconstruction", "pos": "noun"},
                {"lemma": "abnegación", "translation": "selflessness / sacrifice", "pos": "noun"},
                {"lemma": "epopeya", "translation": "epic / saga", "pos": "noun"},
                {"lemma": "diezmado", "translation": "decimated", "pos": "adjective"}
            ]
        },
        "b2-paraguay-04": {
            "id": "vocab.b2.paraguay.04",
            "lesson": "b2-paraguay-04",
            "title": "The Wild Landscape of the Gran Chaco",
            "words": [
                {"lemma": "quebracho", "translation": "quebracho hardwood tree", "pos": "noun"},
                {"lemma": "tanino", "translation": "tannin", "pos": "noun"},
                {"lemma": "inóspito", "translation": "inhospitable", "pos": "adjective"},
                {"lemma": "palmar", "translation": "palm grove", "pos": "noun"},
                {"lemma": "monte", "translation": "scrubland / wilderness", "pos": "noun"},
                {"lemma": "aridez", "translation": "aridity", "pos": "noun"}
            ]
        },
        "b2-paraguay-05": {
            "id": "vocab.b2.paraguay.05",
            "lesson": "b2-paraguay-05",
            "title": "Guarania, Paraguayan Harp and Tereré",
            "words": [
                {"lemma": "guarania", "translation": "guarania musical genre", "pos": "noun"},
                {"lemma": "arpa", "translation": "harp", "pos": "noun"},
                {"lemma": "guampa", "translation": "horn cup for tereré", "pos": "noun"},
                {"lemma": "bombilla", "translation": "metal straw with filter", "pos": "noun"},
                {"lemma": "yerbatero", "translation": "herbalist / yerba worker", "pos": "noun"},
                {"lemma": "cadencia", "translation": "cadence / rhythm", "pos": "noun"}
            ]
        }
    }

    for stem, vdata in vocab_data.items():
        write_json(f"vocabulary/b2/{stem}-voc.json", vdata)

    # 4. Grammar files
    grammar_data = {
        "b2-28-01-a-gr": {
            "id": "grammar.b2.28.01.marcadores-ordenacion",
            "title": "Discourse Markers of Ordering & Enumeration",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de ordenación organizan las partes de un discurso o texto escrito en una secuencia lógica y cronológica. En registros formales de nivel B2, permiten articular conferencias, artículos de opinión y ensayos académicos sin recurrir a enumeraciones elementales."
                },
                {
                    "type": "table",
                    "title": "Marcadores de ordenación en contexto",
                    "rows": [
                        ["En primer término, conviene delimitar los antecedentes jurídicos del conflicto.", "In the first place, it is advisable to define the legal background of the conflict."],
                        ["Acto seguido, analizaremos los efectos socioeconómicos en la población rural.", "Immediately afterwards, we will analyze the socioeconomic effects on the rural population."],
                        ["Por una parte, la modernización tecnológica favorece la conectividad regional.", "On the one hand, technological modernization favors regional connectivity."],
                        ["Por último, examinaremos las recomendaciones de política pública internacional.", "Lastly, we will examine the recommendations of international public policy."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Regla de puntuación: todos los marcadores ordenadores se aíslan mediante comas cuando inician un período o frase: 'En primer término, debemos considerar...', 'Por último, cabe subrayar...'"
                }
            ]
        },
        "b2-28-02-a-gr": {
            "id": "grammar.b2.28.02.marcadores-digresion",
            "title": "Discourse Markers of Digression & Incidental Remarks",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de digresión introducen un comentario lateral, una precisión secundaria o una observación tangencial que se desvía momentáneamente del hilo conductor principal del texto sin que se pierda la cohesión global."
                },
                {
                    "type": "table",
                    "title": "Marcadores de digresión en prosa formal",
                    "rows": [
                        ["El proyecto fue aprobado en mayo; por cierto, con el apoyo de todas las bancadas.", "The project was approved in May; by the way, with the support of all factions."],
                        ["A propósito de la reforma tributaria, los gremios presentaron una contrapropuesta.", "Speaking of tax reform, the labor unions presented a counterproposal."],
                        ["El informe omite, dicho sea de paso, el impacto sobre las comunidades ribereñas.", "The report omits, by the way, the impact on riverside communities."],
                        ["Conviene señalar, entre paréntesis, que la vigencia del tratado expira en 2030.", "It is worth pointing out, parenthetically, that the treaty expires in 2030."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Evita el abuso de digresiones en textos ensayísticos: 'dicho sea de paso' debe emplearse de forma mesurada para enriquecer el argumento sin dispersar la atención del lector."
                }
            ]
        },
        "b2-28-03-a-gr": {
            "id": "grammar.b2.28.03.marcadores-continuidad",
            "title": "Discourse Markers of Continuity & Thematic Transition",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de continuidad y progresión temática aseguran que el discurso avance fluidamente entre un punto ya establecido y el siguiente razonamiento deductivo o explicativo. Señalan la reanudación del argumento central o una reformulación estratégica."
                },
                {
                    "type": "table",
                    "title": "Marcadores de progresión y transición",
                    "rows": [
                        ["Pues bien, examinadas las pruebas periciales, el tribunal absolvió al inculpado.", "Now then, having examined the expert evidence, the court acquitted the defendant."],
                        ["Dicho esto, no debemos soslayar las dificultades presupuestarias que persisten.", "Having said this, we must not sidestep the budgetary difficulties that remain."],
                        ["Así las cosas, el parlamento se vio forzado a negociar un texto de consenso.", "As things stood, parliament was forced to negotiate a consensus text."],
                        ["Ahora bien, la viabilidad financiera exige un estricto control de gasto público.", "Now, financial viability demands strict control of public spending."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Pues bien' y 'así las cosas' exigen coma inmediatamente posterior. Marcan una pausa deliberada en la que el orador o ensayista evalúa el escenario construido antes de dar el siguiente paso."
                }
            ]
        },
        "b2-28-04-a-gr": {
            "id": "grammar.b2.28.04.marcadores-distribucion",
            "title": "Distributive Discourse Markers & Parallel Argumentation",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores distributivos estructuran dos o más proposiciones paralelas que se contrastan, complementan o alternan de modo simétrico. Exigen un riguroso equilibrio sintáctico entre los dos miembros coordinados."
                },
                {
                    "type": "table",
                    "title": "Estructuras correlativas distributivas",
                    "rows": [
                        ["Por una parte, la apertura atrae inversiones; por otra, tensiona el empleo local.", "On the one hand, openness attracts investments; on the other, it strains local jobs."],
                        ["Por un lado, se alaba la agilidad; por otro, se teme la falta de garantías legales.", "On the one hand, speed is praised; on the other, lack of legal guarantees is feared."],
                        ["Ya por falta de recursos, ya por desidia burocrática, la obra quedó inconclusa.", "Whether from lack of resources or bureaucratic apathy, the work remained unfinished."],
                        ["Ora con vehemencia retórica, ora con silencios elocuentes, conmovió al auditorio.", "Now with rhetorical vehemence, now with eloquent silences, he moved the audience."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Correlación estricta: si abres con 'por una parte', debes cerrar con 'por otra' (o 'por otra parte'). Mezclar 'por un lado... por otra parte' se considera descuido estilístico en nivel B2/C1."
                }
            ]
        },
        "b2-28-05-a-gr": {
            "id": "grammar.b2.28.05.marcadores-conclusion",
            "title": "Discourse Markers of Synthesis & Conclusion",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de conclusión y recapitulación cierran el razonamiento condensando las premisas desarrolladas. Permiten formular el balance final, la tesis resolutiva o el corolario teórico de una investigación."
                },
                {
                    "type": "table",
                    "title": "Marcadores de conclusión y balance",
                    "rows": [
                        ["En suma, el programa logró mitigar la deserción escolar en las áreas rurales.", "In short, the program managed to mitigate school dropout in rural areas."],
                        ["En definitiva, la soberanía reside en la voluntad del pueblo soberano.", "Ultimately, sovereignty resides in the will of the sovereign people."],
                        ["En última instancia, el éxito de la democracia depende de sus instituciones.", "In the final analysis, the success of democracy depends on its institutions."],
                        ["A fin de cuentas, los resultados electorales reflejaron el malestar ciudadano.", "At the end of the day, the election results reflected civic discontent."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'En última instancia' denota el fundamento último, aquello que no admite ulterior discusión o reducción; es el marcador preferido en la argumentación filosófica, jurídica y política."
                }
            ]
        },
        "b2-paraguay-01-a-gr": {
            "id": "grammar.b2.paraguay.01.paraguay-contacto-linguistico",
            "title": "Linguistic Contact Features & Lexical Calques in Paraguay",
            "sections": [
                {
                    "type": "text",
                    "content": "El español paraguayo se distingue por una prolongada e intensa convivencia con el guaraní, lengua hablada por la inmensa mayoría de la población. Este contacto secular genera calcos semánticos y partículas discursivas que conviven con la norma culta panhispánica."
                },
                {
                    "type": "table",
                    "title": "Fenómenos de contacto español-guaraní",
                    "rows": [
                        ["Venína un ratito a ver este informe sobre las misiones.", "Come here please for a moment to see this report on the missions."],
                        ["Dijo que iba a pagar la deuda ayer, gua'u.", "He said he was going to pay the debt yesterday, as if."],
                        ["Llovió demasiado mucho en la cordillera durante la tormenta.", "It rained immensely in the mountain range during the storm."],
                        ["Al arpa paraguaya le afinaron con esmero tradicional para el concierto.", "They tuned the Paraguayan harp with traditional care for the concert."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En el registro formal escrito (ensayos, literatura culta de Augusto Roa Bastos), estos rasgos se emplean como recurso expresivo deliberado para impregnar el texto de la cosmovisión y el ritmo del guaraní."
                }
            ]
        },
        "b2-paraguay-02-a-gr": {
            "id": "grammar.b2.paraguay.02.paraguay-concesivas-avanzadas",
            "title": "Advanced Concessive Clauses in Historical Analysis",
            "sections": [
                {
                    "type": "text",
                    "content": "El análisis historiográfico requiere contraponer obstáculos objetivos a logros consumados. Las oraciones subordinadas concesivas avanzadas permiten articular esta dialéctica mediante alternancias de indicativo y subjuntivo."
                },
                {
                    "type": "table",
                    "title": "Nexos concesivos avanzados en contexto histórico",
                    "rows": [
                        ["Por más que las misiones sufrieran asedios, sus templos perduraron.", "No matter how much the missions suffered sieges, their temples endured."],
                        ["Si bien los jesuitas fueron expulsados en 1767, su música barroca arraigó.", "Although the Jesuits were expelled in 1767, their baroque music took root."],
                        ["Aun cuando faltaran recursos modernos, los artesanos guaraníes tallaron la piedra.", "Even though modern resources were lacking, Guaraní artisans carved the stone."],
                        ["Pese a que la selva avanzó sobre las ruinas, las naves siguen en pie.", "Despite the jungle advancing over the ruins, the naves remain standing."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda: 'si bien' se construye siempre con modo indicativo en prosa formal: 'Si bien la contienda fue atroz, la nación se reconstruyó' (NUNCA: *si bien fuera atroz)."
                }
            ]
        },
        "b2-paraguay-03-a-gr": {
            "id": "grammar.b2.paraguay.03.paraguay-voz-pasiva-estilo",
            "title": "Stylistic Passive Structures in Historiographical Discourse",
            "sections": [
                {
                    "type": "text",
                    "content": "La prosa historiográfica de nivel B2 recurre a la voz pasiva perifrástica ('ser' + participio) y a la pasiva refleja ('se' + verbo en tercera persona) para conferir solemnidad, enfatizar el objeto de la acción o velar el agente causal."
                },
                {
                    "type": "table",
                    "title": "Estructuras pasivas en la narración histórica",
                    "rows": [
                        ["La soberanía patria fue defendida con heroísmo indecible en Cerro Corá.", "Homeland sovereignty was defended with unspeakable heroism at Cerro Corá."],
                        ["Se fundaron hospitales de campaña gracias a la abnegación de las mujeres.", "Field hospitals were founded thanks to the selflessness of the women."],
                        ["Se combatió sin descanso a lo largo de las trincheras del río Aquidabán.", "Fighting took place tirelessly along the trenches of the Aquidabán River."],
                        ["Quedó diezmada la población masculina tras un lustro de asedio.", "The male population ended up decimated after five years of siege."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Concordancia de la pasiva refleja: si el sujeto paciente es plural, el verbo DEBE concordar en plural: 'Se fundaron hospitales' (correcto), no *'Se fundó hospitales'."
                }
            ]
        },
        "b2-paraguay-04-a-gr": {
            "id": "grammar.b2.paraguay.04.paraguay-adverbiales-lugar",
            "title": "Complex Locative Adverbials in Descriptive Prose",
            "sections": [
                {
                    "type": "text",
                    "content": "La descripción geográfica y paisajística de regiones agrestes como el Gran Chaco se enriquece mediante locuciones adverbiales espaciales que sitúan los elementos en el horizonte, transmitiendo lejanía, inmensidad o confinamiento."
                },
                {
                    "type": "table",
                    "title": "Locuciones espaciales en la prosa geográfica",
                    "rows": [
                        ["Avanzaron cien leguas tierra adentro sorteando matorrales espinosos.", "They advanced a hundred leagues inland dodging thorny scrubland."],
                        ["Navegaron río abajo hacia la confluencia del Pilcomayo y el Paraguay.", "They sailed downriver toward the confluence of the Pilcomayo and the Paraguay."],
                        ["Se refugiaron en los confines del monte, donde la vegetación es impenetrable.", "They took refuge in the confines of the scrub, where vegetation is impenetrable."],
                        ["El bosque de quebracho se extendía a lo largo y ancho de la llanura.", "The quebracho forest stretched across the length and breadth of the plain."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Evita construcciones redundantes: 'tierra adentro' no lleva preposición 'hacia' antes si el verbo ya implica movimiento ('se internaron tierra adentro')."
                }
            ]
        },
        "b2-paraguay-05-a-gr": {
            "id": "grammar.b2.paraguay.05.paraguay-subordinadas-adjetivas",
            "title": "Relative Clauses with Complex Prepositions in Cultural Writing",
            "sections": [
                {
                    "type": "text",
                    "content": "En el ensayo cultural de nivel B2, las proposiciones subordinadas adjetivas o de relativo con preposición compleja ('mediante el cual', 'en virtud del cual', 'a través de los que') otorgan prestancia y precisión a la caracterización de rituales artísticos y colectivos."
                },
                {
                    "type": "table",
                    "title": "Subordinadas adjetivas relativas complejas",
                    "rows": [
                        ["El tereré es un rito comunitario mediante el cual se forjan lazos de hermandad.", "Tereré is a community ritual through which bonds of brotherhood are forged."],
                        ["La guarania es el cauce poético a través del cual el pueblo canta su nostalgia.", "The guarania is the poetic channel through which the people sing their nostalgia."],
                        ["Creó cánones armónicos en virtud de los cuales el arpa adquirió renombre mundial.", "He created harmonic canons by virtue of which the harp acquired global renown."],
                        ["Siguen un protocolo secular con arreglo al cual se ceba y comparte la guampa.", "They follow a secular protocol in accordance with which the guampa is poured and shared."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El relativo compuesto debe concordar estrictamente en género y número con su antecedente: 'las melodías (femenino plural) mediante las cuales...', 'el instrumento (masculino singular) a través del cual...'"
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}.json", gdata)

    # 5. Exercises
    def make_exercises():
        # Core b2-28-01 to 05
        core_ex = {
            "b2-28-01": [
                {
                    "id": "b2-28-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-ordenacion"],
                    "question": "¿Cuál es la función del marcador 'en primer término' en un discurso formal?",
                    "options": [
                        "Concluir definitivamente la exposición tras sopesar los argumentos.",
                        "Introducir el punto de partida o la primera consideración de una serie ordenada.",
                        "Expresar una duda irresoluble sobre los hechos relatados.",
                        "Pedir disculpas por un error involuntario en el texto."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-ordenacion"],
                    "sentence": "En primer lugar, delimitaremos el marco conceptual; en segundo __, examinaremos los datos empíricos.",
                    "answer": "término",
                    "english": "In the first place, we will delimit the conceptual framework; in the second place, we will examine the empirical data."
                },
                {
                    "id": "b2-28-01.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-ordenacion"],
                    "pairs": [
                        ["en primer lugar", "apertura de serie enumerativa"],
                        ["acto seguido", "continuación cronológica inmediata"],
                        ["por último", "clausura de la enumeración"],
                        ["para empezar", "introducción inicial del tema"]
                    ]
                },
                {
                    "id": "b2-28-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-ordenacion"],
                    "sentence": "Por __ parte, la propuesta reduce costos; por otra, genera incertidumbre laboral.",
                    "answer": "una",
                    "english": "On the one hand, the proposal reduces costs; on the other, it creates labor uncertainty."
                },
                {
                    "id": "b2-28-01.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-28-vocab"],
                    "question": "¿Qué sustantivo designa la parte final o etapa de cierre de un período o época histórica?",
                    "options": [
                        "El preámbulo",
                        "La postrimería",
                        "El exordio",
                        "La coyuntura"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué motivó a Gaspar Mora a aislarse en el monte de Itapé según el relato?",
                    "options": [
                        "El deseo de escapar de sus deudas bancarias.",
                        "El descubrimiento de que padecía lepra y la voluntad de consagrar su destierro a tallar el dolor de su pueblo.",
                        "Una orden judicial del gobernador militar de la provincia.",
                        "La búsqueda de yacimientos de oro en la sierra."
                    ],
                    "correct": 1
                }
            ],
            "b2-28-02": [
                {
                    "id": "b2-28-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-digresion"],
                    "question": "¿Qué marcador permite incorporar un comentario accesorio sin que sea el eje del razonamiento principal?",
                    "options": [
                        "En consecuencia",
                        "Dicho sea de paso",
                        "Por consiguiente",
                        "Habida cuenta de"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-digresion"],
                    "sentence": "El ministro defendió el presupuesto; por __, anunció una partida especial para educación rural.",
                    "answer": "cierto",
                    "english": "The minister defended the budget; by the way, he announced a special fund for rural education."
                },
                {
                    "id": "b2-28-02.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-digresion"],
                    "pairs": [
                        ["a propósito", "vinculación con asunto conexo"],
                        ["dicho sea de paso", "comentario incidental o accesorio"],
                        ["entre paréntesis", "pausa explícita de aclaración"],
                        ["por cierto", "evocación oportuna de un dato"]
                    ]
                },
                {
                    "id": "b2-28-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-digresion"],
                    "sentence": "A __ de la reforma agraria, varios parlamentarios visitaron las cooperativas del interior.",
                    "answer": "propósito",
                    "english": "Speaking of agrarian reform, several parliamentarians visited the cooperatives in the interior."
                },
                {
                    "id": "b2-28-02.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-28-vocab"],
                    "question": "¿Qué verbo formal expresa la acción de esquivar o eludir una dificultad o tema espinoso?",
                    "options": [
                        "Pormenorizar",
                        "Soslayar",
                        "Dilucidar",
                        "Recapitular"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Por qué los campesinos se negaron a colocar el Cristo de Gaspar Mora en el templo parroquial?",
                    "options": [
                        "Porque la estatua era demasiado pesada para transportarla.",
                        "Porque querían que la imagen perteneciera al pueblo y permaneciera libre en la cima del cerro desafiando a las autoridades.",
                        "Porque el obispo les exigía pagar un tributo de oro.",
                        "Porque preferían venderla a un coleccionista extranjero."
                    ],
                    "correct": 1
                }
            ],
            "b2-28-03": [
                {
                    "id": "b2-28-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-continuidad"],
                    "question": "¿Cuál es la función textual del marcador 'dicho esto'?",
                    "options": [
                        "Invalidar retroactivamente todas las afirmaciones anteriores.",
                        "Asumir lo planteado previamente y pasar al siguiente punto introduciendo una salvedad o contrapunto.",
                        "Indicar el final abrupto de una conferencia.",
                        "Citar textualmente a un autor clásico."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-continuidad"],
                    "sentence": "Pues __, analizadas las consecuencias del tratado, procede debatir sus implicancias fiscales.",
                    "answer": "bien",
                    "english": "Now then, having analyzed the consequences of the treaty, it is appropriate to debate its fiscal implications."
                },
                {
                    "id": "b2-28-03.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-continuidad"],
                    "pairs": [
                        ["pues bien", "reanudación o paso al siguiente razonamiento"],
                        ["dicho esto", "transición con contrapunto matizado"],
                        ["así las cosas", "evaluación del estado de la cuestión"],
                        ["ahora bien", "introducción de objeción sustantiva"]
                    ]
                },
                {
                    "id": "b2-28-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-continuidad"],
                    "sentence": "Así las __, la asamblea decidió suspender la votación hasta recibir el dictamen pericial.",
                    "answer": "cosas",
                    "english": "As things stood, the assembly decided to suspend the vote until receiving the expert opinion."
                },
                {
                    "id": "b2-28-03.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-28-vocab"],
                    "question": "¿Qué expresión designa el elemento vertebrador o idea central que une las partes de un discurso?",
                    "options": [
                        "El hilo conductor",
                        "El inciso lateral",
                        "La bifurcación",
                        "El corolario"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-28-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿A qué prueba extrema se enfrenta Cristóbal Jara en las arenas del Chaco?",
                    "options": [
                        "A defender una fortaleza fluvial desarmado.",
                        "A conducir un camión cisterna con agua vital bajo fuego enemigo para salvar a un destacamento agonizante.",
                        "A cruzar nadando el río Paraguay en plena noche.",
                        "A redactar un armisticio con los comandantes bolivianos."
                    ],
                    "correct": 1
                }
            ],
            "b2-28-04": [
                {
                    "id": "b2-28-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-distribucion"],
                    "question": "¿Qué pareja de marcadores distributivos pertenece al registro ensayístico y literario más formal?",
                    "options": [
                        "O sea... es decir",
                        "Ora... ora",
                        "Por lo tanto... en consecuencia",
                        "Así que... de modo que"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-distribucion"],
                    "sentence": "Por un lado, la medida estimula el consumo; por __ lado, puede acelerar el ritmo inflacionario.",
                    "answer": "otro",
                    "english": "On the one hand, the measure stimulates consumption; on the other hand, it may accelerate the rate of inflation."
                },
                {
                    "id": "b2-28-04.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-distribucion"],
                    "pairs": [
                        ["por un lado... por otro", "distribución bimembre analítica"],
                        ["ya... ya", "alternancia simétrica culta"],
                        ["bien... bien", "distribución de opciones equivalentes"],
                        ["ora... ora", "alternancia retórica clásica"]
                    ]
                },
                {
                    "id": "b2-28-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-distribucion"],
                    "sentence": "Ya por timidez, __ por prudencia diplomática, el delegado optó por guardar silencio.",
                    "answer": "ya",
                    "english": "Whether out of shyness or out of diplomatic prudence, the delegate chose to remain silent."
                },
                {
                    "id": "b2-28-04.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-28-vocab"],
                    "question": "¿Qué término formal designa la división o bifurcación de un concepto en dos posturas opuestas?",
                    "options": [
                        "Dicotomía",
                        "Apostilla",
                        "Preámbulo",
                        "Paréntesis"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-28-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué dimensión trascendente adquiere la travesía del camión aguatero en la novela?",
                    "options": [
                        "Una demostración de velocidad automovilística para vender motores.",
                        "Una consagración del sacrificio solidario entre hermanos de infortunio frente a la indiferencia del poder.",
                        "Un simple paseo rutinario sin consecuencias personales.",
                        "Una maniobra de escape cobarde hacia la frontera argentina."
                    ],
                    "correct": 1
                }
            ],
            "b2-28-05": [
                {
                    "id": "b2-28-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-conclusion"],
                    "question": "¿Qué marcador de cierre connota el principio irreductible o la causa última de una argumentación?",
                    "options": [
                        "Para empezar",
                        "En última instancia",
                        "A propósito",
                        "Por cierto"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-conclusion"],
                    "sentence": "En __, los resultados del estudio confirman plenamente la hipótesis inicial de los investigadores.",
                    "answer": "suma",
                    "english": "In short, the results of the study fully confirm the researchers' initial hypothesis."
                },
                {
                    "id": "b2-28-05.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-conclusion"],
                    "pairs": [
                        ["en suma", "recapitulación sintética condensada"],
                        ["en definitiva", "resolución categórica concluyente"],
                        ["en última instancia", "fundamento irreductible o causa esencial"],
                        ["a fin de cuentas", "balance pragmático del desenlace"]
                    ]
                },
                {
                    "id": "b2-28-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-conclusion"],
                    "sentence": "En __, la estabilidad democrática exige el fortalecimiento continuo de las instituciones republicanas.",
                    "answer": "definitiva",
                    "english": "Ultimately, democratic stability demands the continuous strengthening of republican institutions."
                },
                {
                    "id": "b2-28-05.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-28-vocab"],
                    "question": "¿Qué sustantivo formal se refiere a la proposición que se deduce de lo demostrado con anterioridad?",
                    "options": [
                        "El corolario",
                        "El exordio",
                        "El inciso",
                        "La digresión"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-28-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la lección humanista que Roa Bastos transmite mediante el dolor de su tierra?",
                    "options": [
                        "Que la resignación absoluta es la única virtud verdadera.",
                        "Que la dignidad humana se levanta en la solidaridad fraterna compartida por los desposeídos.",
                        "Que el progreso depende únicamente de la compra de armamentos modernos.",
                        "Que la memoria histórica debe borrarse para evitar el sufrimiento."
                    ],
                    "correct": 1
                }
            ],
            "b2-28-consolidation": [
                {
                    "id": "b2-28-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-ordenacion"],
                    "question": "Identifica la opción donde el marcador ordenador esté correctamente puntuado en apertura de párrafo:",
                    "options": [
                        "En primer término debemos analizar el impacto ambiental.",
                        "En primer término, debemos analizar el impacto ambiental.",
                        "En primer término; debemos analizar el impacto ambiental.",
                        "En primer término: debemos analizar el impacto ambiental."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-digresion"],
                    "sentence": "Conviene recordar, dicho sea de __, que los plazos de apelación vencen el próximo viernes.",
                    "answer": "paso",
                    "english": "It is worth remembering, by the way, that the appeal deadlines expire next Friday."
                },
                {
                    "id": "b2-28-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-continuidad"],
                    "question": "¿Qué marcador indica que se evalúa el estado actual de los hechos antes de continuar?",
                    "options": [
                        "En cambio",
                        "Así las cosas",
                        "Sin embargo",
                        "Por consiguiente"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-28-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-distribucion"],
                    "sentence": "Por una parte, la propuesta es atractiva; por __ parte, los riesgos financieros son inasumibles.",
                    "answer": "otra",
                    "english": "On the one hand, the proposal is attractive; on the other hand, the financial risks are unacceptable."
                },
                {
                    "id": "b2-28-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-conclusion"],
                    "question": "¿Cuál es el marcador más adecuado para enunciar el fundamento ético irreductible de un ensayo?",
                    "options": [
                        "En última instancia",
                        "A propósito",
                        "Por cierto",
                        "En primer lugar"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-28-consolidation.ex06",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-28-vocab"],
                    "pairs": [
                        ["preámbulo", "introducción formal o exordio"],
                        ["soslayar", "eludir o evitar una dificultad"],
                        ["dicotomía", "división en dos posturas opuestas"],
                        ["corolario", "proposición deducida de lo previo"]
                    ]
                },
                {
                    "id": "b2-28-consolidation.ex07",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-conclusion"],
                    "sentence": "En __, podemos afirmar que el congreso alcanzó con éxito todos sus objetivos pedagógicos.",
                    "answer": "suma",
                    "english": "In short, we can state that the conference successfully achieved all its pedagogical objectives."
                },
                {
                    "id": "b2-28-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué elemento unifica simbólicamente la resistencia campesina en la obra de Augusto Roa Bastos?",
                    "options": [
                        "Un estandarte militar importado de Madrid.",
                        "El Cristo tallado en guayacán por el leproso Gaspar Mora en el cerro de Itapé.",
                        "Un libro de leyes comerciales del siglo dieciocho.",
                        "Una campana de bronce donada por el párroco."
                    ],
                    "correct": 1
                }
            ]
        }

        # Regional b2-paraguay-01 to 05
        reg_ex = {
            "b2-paraguay-01": [
                {
                    "id": "b2-paraguay-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-contacto-linguistico"],
                    "question": "¿Qué función cumple el sufijo enfático '-na' heredado del guaraní en el habla paraguaya?",
                    "options": [
                        "Negar rotundamente una orden judicial.",
                        "Atenuar un mandato o expresar un ruego cordial ('venína' = 'ven, por favor').",
                        "Indicar el tiempo pasado de los verbos irregulares.",
                        "Marcar el género femenino de los sustantivos abstractos."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-contacto-linguistico"],
                    "sentence": "En el mercado de Asunción, la mezcla espontánea de guaraní y español se conoce como __.",
                    "answer": "jopara",
                    "english": "In the Asunción market, the spontaneous blend of Guaraní and Spanish is known as jopara."
                },
                {
                    "id": "b2-paraguay-01.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["paraguay-contacto-linguistico"],
                    "pairs": [
                        ["-na", "atenuación de ruego o súplica cordial"],
                        ["gua'u", "marcador de ironía o fingimiento"],
                        ["demasiado mucho", "calco intensificador de hetáiterei"],
                        ["jopara", "código mixto bilingüe urbano"]
                    ]
                },
                {
                    "id": "b2-paraguay-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-contacto-linguistico"],
                    "sentence": "Dijo que vendría temprano, __; todos sabían que se quedaría descansando.",
                    "answer": "gua'u",
                    "english": "He said he would come early, as if; everyone knew he would stay resting."
                },
                {
                    "id": "b2-paraguay-01.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-paraguay-vocab"],
                    "question": "¿Qué concepto lingüístico alude a la influencia de una lengua originaria sobre otra recién adquirida?",
                    "options": [
                        "El sustrato lingüístico",
                        "La entonación modal",
                        "El pleonasmo sintáctico",
                        "La cacofonía léxica"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-paraguay-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la trascendencia de la Constitución Nacional de 1992 para la lengua guaraní?",
                    "options": [
                        "Prohibió su enseñanza en centros universitarios públicos.",
                        "La declaró lengua oficial de la república en igualdad jurídica con el castellano.",
                        "Estableció que solo los ancianos rurales podían hablarla.",
                        "Ordenó traducir todas las leyes exclusivamente al latín eclesiástico."
                    ],
                    "correct": 1
                }
            ],
            "b2-paraguay-02": [
                {
                    "id": "b2-paraguay-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-concesivas-avanzadas"],
                    "question": "¿Qué modo verbal debe seguir obligatoriamente al nexo concesivo culto 'si bien'?",
                    "options": [
                        "Subjuntivo imperativo",
                        "Indicativo",
                        "Infinitivo compuesto",
                        "Gerundio continuo"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-concesivas-avanzadas"],
                    "sentence": "Si __ las misiones sufrieron el expolio colonial, su legado artístico perdura en la memoria.",
                    "answer": "bien",
                    "english": "Although the missions suffered colonial plundering, their artistic legacy endures in memory."
                },
                {
                    "id": "b2-paraguay-02.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["paraguay-concesivas-avanzadas"],
                    "pairs": [
                        ["si bien", "concesión en indicativo de hecho comprobado"],
                        ["por más que", "concesión enfática con subjuntivo o indicativo"],
                        ["aun cuando", "concesión extrema en subjuntivo hipotético"],
                        ["pese a que", "concesión formal de amplio uso ensayístico"]
                    ]
                },
                {
                    "id": "b2-paraguay-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-concesivas-avanzadas"],
                    "sentence": "Aun __ faltaran herramientas modernas, los tallistas guaraníes erigieron catedrales colosales.",
                    "answer": "cuando",
                    "english": "Even though modern tools were lacking, Guaraní carvers erected colossal cathedrals."
                },
                {
                    "id": "b2-paraguay-02.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-paraguay-vocab"],
                    "question": "¿Cómo se llamaba el poblado comunal autónomo fundado por los jesuitas para los indígenas?",
                    "options": [
                        "El latifundio",
                        "La reducción",
                        "El feudo",
                        "El corregimiento"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué célebre compositor toscano compuso música sacra barroca interpretada por los guaraníes?",
                    "options": [
                        "Antonio Vivaldi",
                        "Domenico Zipoli",
                        "Claudio Monteverdi",
                        "Arcangelo Corelli"
                    ],
                    "correct": 1
                }
            ],
            "b2-paraguay-03": [
                {
                    "id": "b2-paraguay-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-voz-pasiva-estilo"],
                    "question": "En la oración 'Se fundaron hospitales comunitarios', ¿cuál es la estructura sintáctica empleada?",
                    "options": [
                        "Pasiva refleja con concordancia de sujeto paciente en plural.",
                        "Voz pasiva perifrástica con complemento agente expreso.",
                        "Impersonal refleja con objeto directo invariable.",
                        "Oración transitiva activa regular."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-paraguay-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-voz-pasiva-estilo"],
                    "sentence": "La soberanía nacional __ defendida con heroísmo indómito por soldados y campesinos en Humaitá.",
                    "answer": "fue",
                    "english": "National sovereignty was defended with untamed heroism by soldiers and peasants at Humaitá."
                },
                {
                    "id": "b2-paraguay-03.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["paraguay-voz-pasiva-estilo"],
                    "pairs": [
                        ["pasiva con ser", "fue defendida la trinchera"],
                        ["pasiva refleja", "se reconstruyeron los pueblos"],
                        ["impersonal con se", "se combatió sin descanso"],
                        ["participio adjetivo", "población diezmada por la peste"]
                    ]
                },
                {
                    "id": "b2-paraguay-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-voz-pasiva-estilo"],
                    "sentence": "Se __ numerosas trincheras a lo largo de las riberas del río para detener a la escuadra acorazada.",
                    "answer": "cavaron",
                    "english": "Numerous trenches were dug along the river banks to stop the ironclad fleet."
                },
                {
                    "id": "b2-paraguay-03.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-paraguay-vocab"],
                    "question": "¿Qué verbo formal designa la aniquilación o reducción drástica de una población o tropa militar?",
                    "options": [
                        "Diezmar",
                        "Emancipar",
                        "Reivindicar",
                        "Recaudar"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-paraguay-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quiénes fueron 'Las Residentas' en la memoria histórica del Paraguay?",
                    "options": [
                        "Enfermeras extranjeras contratadas por el gobierno imperial brasileño.",
                        "Las mujeres paraguayas que sostuvieron al ejército y reconstruyeron la nación con su trabajo agrario.",
                        "Escritoras que fundaron el primer diario impreso en idioma guaraní.",
                        "Militares veteranas de la guerra de independencia."
                    ],
                    "correct": 1
                }
            ],
            "b2-paraguay-04": [
                {
                    "id": "b2-paraguay-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-adverbiales-lugar"],
                    "question": "¿Qué locución locativa expresa desplazamiento hacia el interior de un territorio agreste o continental?",
                    "options": [
                        "Mar adentro",
                        "Tierra adentro",
                        "Cuesta abajo",
                        "De par en par"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-adverbiales-lugar"],
                    "sentence": "Los exploradores navegaron río __ buscando la confluencia con el Pilcomayo.",
                    "answer": "abajo",
                    "english": "The explorers navigated downriver looking for the confluence with the Pilcomayo."
                },
                {
                    "id": "b2-paraguay-04.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["paraguay-adverbiales-lugar"],
                    "pairs": [
                        ["tierra adentro", "penetración hacia el interior territorial"],
                        ["río abajo", "navegación en el sentido de la corriente"],
                        ["en los confines de", "límite extremo o remoto de una región"],
                        ["a lo largo y ancho de", "cobertura completa de un espacio geográfico"]
                    ]
                },
                {
                    "id": "b2-paraguay-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-adverbiales-lugar"],
                    "sentence": "En los __ del Gran Chaco, habitan comunidades indígenas en armonía con el monte.",
                    "answer": "confines",
                    "english": "In the confines of the Gran Chaco, indigenous communities live in harmony with the wilderness."
                },
                {
                    "id": "b2-paraguay-04.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-paraguay-vocab"],
                    "question": "¿Qué sustancia química extraída del quebracho colorado fue esencial para el curtido de cueros?",
                    "options": [
                        "El caucho",
                        "El tanino",
                        "El salitre",
                        "El guano"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué ciudad es el epicentro agroindustrial cooperativo fundado por menonitas en el Chaco central?",
                    "options": [
                        "Encarnación",
                        "Filadelfia",
                        "Villarrica",
                        "Concepción"
                    ],
                    "correct": 1
                }
            ],
            "b2-paraguay-05": [
                {
                    "id": "b2-paraguay-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-subordinadas-adjetivas"],
                    "question": "En 'El tereré es un rito comunitario mediante el cual se forjan amistades', ¿cuál es el relativo complejo?",
                    "options": [
                        "Donde",
                        "Mediante el cual",
                        "Cuyo valor",
                        "Cualquiera que"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-subordinadas-adjetivas"],
                    "sentence": "La guarania es el género poético a __ del cual José Asunción Flores inmortalizó el alma de su pueblo.",
                    "answer": "través",
                    "english": "The guarania is the poetic genre through which José Asunción Flores immortalized his people's soul."
                },
                {
                    "id": "b2-paraguay-05.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["paraguay-subordinadas-adjetivas"],
                    "pairs": [
                        ["mediante el cual", "mecanismo o instrumento mediador"],
                        ["en virtud de la cual", "fundamento o causa normativa"],
                        ["a través de los que", "vía o canal de manifestación"],
                        ["con arreglo al cual", "pauta o criterio rector"]
                    ]
                },
                {
                    "id": "b2-paraguay-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-subordinadas-adjetivas"],
                    "sentence": "Aprobaron normas en __ de las cuales se protege el conocimiento botánico de las yuyeras tradicionales.",
                    "answer": "virtud",
                    "english": "They approved regulations by virtue of which the botanical knowledge of traditional herbalists is protected."
                },
                {
                    "id": "b2-paraguay-05.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-paraguay-vocab"],
                    "question": "¿Cómo se llama el vaso tradicional elaborado con cuerno de vaca o madera para beber tereré?",
                    "options": [
                        "La guampa",
                        "El porongo",
                        "La bota",
                        "El cántaro"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-paraguay-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién fue el genial creador del ritmo de la guarania en 1925?",
                    "options": [
                        "Agustín Pío Barrios",
                        "José Asunción Flores",
                        "Félix Pérez Cardozo",
                        "Herminio Giménez"
                    ],
                    "correct": 1
                }
            ],
            "b2-paraguay-consolidation": [
                {
                    "id": "b2-paraguay-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-contacto-linguistico"],
                    "question": "¿Qué rasgo caracteriza el contacto del español con el guaraní en Paraguay?",
                    "options": [
                        "La desaparición absoluta de cualquier vocabulario precolombino.",
                        "El empleo de préstamos, calcos expresivos y partículas atenuadoras en el marco del jopara cotidiano.",
                        "La sustitución de todos los verbos en pasado por participios italianos.",
                        "La prohibición de usar pronombres personales en público."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-concesivas-avanzadas"],
                    "sentence": "Por __ que arreciaran los bombardeos enemigos, las fortalezas de Humaitá no capitularon de inmediato.",
                    "answer": "más",
                    "english": "No matter how much the enemy bombardments raged, the fortresses of Humaitá did not surrender immediately."
                },
                {
                    "id": "b2-paraguay-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-voz-pasiva-estilo"],
                    "question": "¿Qué construcción pasiva es típica del registro historiográfico formal solemne?",
                    "options": [
                        "La pasiva perifrástica con el verbo ser y participio concordado.",
                        "La perífrasis de gerundio continuo con estar.",
                        "El futuro perifrástico de duda con ir a.",
                        "La interjección enfática exclamativa."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-paraguay-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-adverbiales-lugar"],
                    "sentence": "Se internaron tierra __ sorteando pantanales y matorrales espinosos durante semanas.",
                    "answer": "adentro",
                    "english": "They penetrated inland dodging marshes and thorny scrubland for weeks."
                },
                {
                    "id": "b2-paraguay-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["paraguay-subordinadas-adjetivas"],
                    "question": "¿Cuál es la forma correcta con relativo complejo para complementar el sustantivo 'las pautas'?",
                    "options": [
                        "Con arreglo al cual",
                        "Con arreglo a las cuales",
                        "Con arreglo a los cuales",
                        "Con arreglo de que"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-paraguay-consolidation.ex06",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-paraguay-vocab"],
                    "pairs": [
                        ["jopara", "habla mixta guaraní-castellano"],
                        ["reducción", "pueblo misional jesuítico"],
                        ["guampa", "recipiente para beber tereré"],
                        ["pohã ñana", "hierbas medicinales tradicionales"]
                    ]
                },
                {
                    "id": "b2-paraguay-consolidation.ex07",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["paraguay-subordinadas-adjetivas"],
                    "sentence": "Diseñaron un tratado mediante el __ se garantiza la protección del patrimonio cultural e inmaterial.",
                    "answer": "cual",
                    "english": "They designed a treaty through which the protection of cultural and intangible heritage is guaranteed."
                },
                {
                    "id": "b2-paraguay-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué valor humano fundamental transmite el ritual cotidiano del tereré en el pueblo paraguayo?",
                    "options": [
                        "La supremacía económica sobre los países vecinos.",
                        "La fraternidad comunitaria, la pausa reflexiva y la hospitalidad sin distinción de clases sociales.",
                        "La obligación de aislarse del contacto con amigos y familiares.",
                        "El desinterés absoluto por el cuidado de la salud física."
                    ],
                    "correct": 1
                }
            ]
        }

        for stem, exs in core_ex.items():
            write_json(f"exercises/b2/{stem}-ex.json", {"lesson": stem, "exercises": exs})

        for stem, exs in reg_ex.items():
            write_json(f"exercises/b2/{stem}-ex.json", {"lesson": stem, "exercises": exs})

    make_exercises()

    # 6. Stories (ensure refreshed from disk/verified files)
    print("Stories are already created and verified.")

    # 7. Lessons
    core_lessons = {
        "b2-28-01": {
            "id": "lesson.b2.28.01",
            "title": "Discourse Ordering: en primer término, acto seguido, por último",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-28.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-28-01-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-28-01-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-28-01-ex.json",
                    "exerciseRefs": [f"b2-28-01.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-28-02": {
            "id": "lesson.b2.28.02",
            "title": "Digression & Remarks: dicho sea de paso, por cierto, a propósito",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-28.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-28-02-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-28-02-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-28-02-ex.json",
                    "exerciseRefs": [f"b2-28-02.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-28-03": {
            "id": "lesson.b2.28.03",
            "title": "Continuity & Transition: pues bien, dicho esto, así las cosas",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-28.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-28-03-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-28-03-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-28-03-ex.json",
                    "exerciseRefs": [f"b2-28-03.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-28-04": {
            "id": "lesson.b2.28.04",
            "title": "Distribution & Parallelism: por una parte... por otra, ya... ya",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-28.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-28-04-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-28-04-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-28-04-ex.json",
                    "exerciseRefs": [f"b2-28-04.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-28-05": {
            "id": "lesson.b2.28.05",
            "title": "Conclusion & Synthesis: en suma, en definitiva, en última instancia",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-28.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-28-05-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-28-05-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-28-05-ex.json",
                    "exerciseRefs": [f"b2-28-05.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-28-consolidation": {
            "id": "lesson.b2.28.consolidation",
            "title": "Consolidation: Discourse Markers I: Structuring & Sequencing",
            "level": "B2",
            "sections": [
                {
                    "type": "goal",
                    "items": [
                        "Articular textos expositivos y ensayísticos mediante marcadores de ordenación rigurosos.",
                        "Introducir digresiones y matices contextuales sin quebrantar la cohesión argumentativa.",
                        "Sintetizar razonamientos complejos aplicando marcadores de conclusión de registro culto B2."
                    ]
                },
                {"type": "recycle", "count": 3},
                {
                    "type": "exercise-group",
                    "title": "Review",
                    "ref": "exercises/b2/b2-28-consolidation-ex.json",
                    "exerciseRefs": [f"b2-28-consolidation.ex0{i}" for i in range(1, 9)]
                },
                {
                    "type": "checklist",
                    "items": [
                        "Domino los marcadores de apertura, progresión y clausura enumerativa (en primer término, por último).",
                        "Uso oportunamente marcadores de digresión (dicho sea de paso, por cierto, a propósito).",
                        "Estructuro transiciones y contrapuntos formales con 'pues bien', 'dicho esto' y 'así las cosas'.",
                        "Mantengo la correlación exacta en estructuras distributivas (por una parte... por otra, ya... ya).",
                        "Corono argumentaciones académicas con 'en suma', 'en definitiva' y 'en última instancia'."
                    ]
                }
            ]
        }
    }

    for stem, ldata in core_lessons.items():
        write_json(f"lessons/b2/{stem}.json", ldata)

    reg_lessons = {
        "b2-paraguay-01": {
            "id": "lesson.b2.paraguay.01",
            "title": "Bilingüismo guaraní y jopara: El alma de una nación",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-paraguay-01.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-paraguay-01-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-paraguay-01-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-paraguay-01-ex.json",
                    "exerciseRefs": [f"b2-paraguay-01.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-paraguay-02": {
            "id": "lesson.b2.paraguay.02",
            "title": "Reducciones jesuíticas: Barroco guaraní y utopía comunal",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-paraguay-02.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-paraguay-02-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-paraguay-02-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-paraguay-02-ex.json",
                    "exerciseRefs": [f"b2-paraguay-02.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-paraguay-03": {
            "id": "lesson.b2.paraguay.03",
            "title": "La Guerra de la Triple Alianza y el renacer de Las Residentas",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-paraguay-03.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-paraguay-03-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-paraguay-03-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-paraguay-03-ex.json",
                    "exerciseRefs": [f"b2-paraguay-03.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-paraguay-04": {
            "id": "lesson.b2.paraguay.04",
            "title": "El Gran Chaco: Quebrachales, menonitas y pueblos originarios",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-paraguay-04.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-paraguay-04-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-paraguay-04-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-paraguay-04-ex.json",
                    "exerciseRefs": [f"b2-paraguay-04.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-paraguay-05": {
            "id": "lesson.b2.paraguay.05",
            "title": "Tradición e identidad: El tereré de pohã ñana y la guarania",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-paraguay-05.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-paraguay-05-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-paraguay-05-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-paraguay-05-ex.json",
                    "exerciseRefs": [f"b2-paraguay-05.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-paraguay-consolidation": {
            "id": "lesson.b2.paraguay.consolidation",
            "title": "Consolidación: Paraguay, bilingüismo guaraní, misiones y el Chaco",
            "level": "B2",
            "sections": [
                {
                    "type": "goal",
                    "items": [
                        "Comprender la dimensión cultural y lingüística del bilingüismo oficial y el jopara en Paraguay.",
                        "Manejar estructuras concesivas y pasivas formales en el análisis historiográfico de la cuenca del Plata.",
                        "Dominar locuciones adverbiales de lugar y subordinadas relativas complejas en la prosa cultural."
                    ]
                },
                {"type": "recycle", "count": 3},
                {
                    "type": "exercise-group",
                    "title": "Review",
                    "ref": "exercises/b2/b2-paraguay-consolidation-ex.json",
                    "exerciseRefs": [f"b2-paraguay-consolidation.ex0{i}" for i in range(1, 9)]
                },
                {
                    "type": "checklist",
                    "items": [
                        "Reconozco los calcos y partículas modales del contacto español-guaraní en registros descriptivos.",
                        "Construyo oraciones concesivas complejas con 'si bien' (indicativo), 'por más que' y 'aun cuando'.",
                        "Aplico con rigor la pasiva perifrástica y la pasiva refleja en textos historiográficos sobre la Guerra Grande.",
                        "Utilizo locuciones adverbiales locativas como 'tierra adentro', 'río abajo' y 'en los confines de'.",
                        "Formulo relativas con preposiciones compuestas ('mediante el cual', 'en virtud de los cuales')."
                    ]
                }
            ]
        }
    }

    for stem, ldata in reg_lessons.items():
        write_json(f"lessons/b2/{stem}.json", ldata)

if __name__ == "__main__":
    main()
