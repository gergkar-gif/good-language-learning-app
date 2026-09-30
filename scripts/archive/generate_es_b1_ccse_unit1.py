#!/usr/bin/env python3
"""Generate Spain CCSE Unit 1: La Constitución Española de 1978 (content/es-es, B1, track: cultura).

Follows the full 3-pillar standard (matching Hungarian Citizenship & LatAm tracks):
- 5 per-lesson companion World Stories + 1 combined unit story in stories/world/b1/
  with TRIH narrative style, narration metadata, and 3 comprehension questions each.
- 5 Vocabulary files (8 words each = 40 words total).
- 5 Grammar files with text, examples, and tip sections.
- 5 Exercise files (9 exercises each = 45 lesson exercises).
- 1 Consolidation Exercise file (18 exercises).
- 6 full Lesson files (goal, recycle, story, vocabulary, grammar, exercise-group, srs, checklist).
"""

import json
import os
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


def build_unit_1():
    # Remove old legacy b1-ccse-constitucion-* files if present
    for folder in ["lessons/b1", "vocabulary/b1", "grammar/b1", "exercises/b1"]:
        dir_path = ROOT / "content/es-es" / folder
        if dir_path.exists():
            for old_file in dir_path.glob("b1-ccse-constitucion*"):
                old_file.unlink()
                print(f"Removed legacy file {old_file.relative_to(ROOT)}")

    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.constitucion.01",
        "lesson": "b1-constitucion-01",
        "title": "El referéndum de 1978 y la soberanía nacional",
        "theme": "La Constitución Española",
        "words": [
            {"lemma": "la soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "el referéndum", "translation": "referendum", "pos": "noun"},
            {"lemma": "ratificar", "translation": "to ratify", "pos": "verb"},
            {"lemma": "emanar", "translation": "to emanate, originate from", "pos": "verb"},
            {"lemma": "el consenso", "translation": "consensus", "pos": "noun"},
            {"lemma": "entrar en vigor", "translation": "to enter into force, take effect", "pos": "expression"},
            {"lemma": "el boletín oficial", "translation": "official state gazette", "pos": "expression"},
            {"lemma": "el Estado de Derecho", "translation": "rule of law, state under the rule of law", "pos": "expression"}
        ]
    }
    write_json("content/es-es/vocabulary/b1/b1-constitucion-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.constitucion.02",
        "lesson": "b1-constitucion-02",
        "title": "La monarquía parlamentaria y la separación de poderes",
        "theme": "La Constitución Española",
        "words": [
            {"lemma": "la monarquía parlamentaria", "translation": "parliamentary monarchy", "pos": "expression"},
            {"lemma": "la jefatura del Estado", "translation": "headship of State", "pos": "expression"},
            {"lemma": "arbitrar", "translation": "to arbitrate", "pos": "verb"},
            {"lemma": "moderar", "translation": "to moderate", "pos": "verb"},
            {"lemma": "sancionar", "translation": "to sanction, give royal assent", "pos": "verb"},
            {"lemma": "promulgar", "translation": "to promulgate, enact", "pos": "verb"},
            {"lemma": "la separación de poderes", "translation": "separation of powers", "pos": "expression"},
            {"lemma": "la permanencia", "translation": "permanence, continuity", "pos": "noun"}
        ]
    }
    write_json("content/es-es/vocabulary/b1/b1-constitucion-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.constitucion.03",
        "lesson": "b1-constitucion-03",
        "title": "Valores superiores, lenguas oficiales y símbolos",
        "theme": "La Constitución Española",
        "words": [
            {"lemma": "el pluralismo político", "translation": "political pluralism", "pos": "expression"},
            {"lemma": "el ordenamiento jurídico", "translation": "legal system, legal order", "pos": "expression"},
            {"lemma": "cooficial", "translation": "co-official", "pos": "adjective"},
            {"lemma": "el patrimonio cultural", "translation": "cultural heritage", "pos": "expression"},
            {"lemma": "la franja", "translation": "stripe, band (of a flag)", "pos": "noun"},
            {"lemma": "la anchura", "translation": "width", "pos": "noun"},
            {"lemma": "el deber", "translation": "duty, obligation", "pos": "noun"},
            {"lemma": "propugnar", "translation": "to advocate, uphold", "pos": "verb"}
        ]
    }
    write_json("content/es-es/vocabulary/b1/b1-constitucion-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.constitucion.04",
        "lesson": "b1-constitucion-04",
        "title": "Estructura y reforma de la Constitución",
        "theme": "La Constitución Española",
        "words": [
            {"lemma": "el preámbulo", "translation": "preamble", "pos": "noun"},
            {"lemma": "la disposición", "translation": "provision, disposition", "pos": "noun"},
            {"lemma": "la reforma constitucional", "translation": "constitutional reform, amendment", "pos": "expression"},
            {"lemma": "la mayoría cualificada", "translation": "qualified supermajority", "pos": "expression"},
            {"lemma": "el sufragio", "translation": "suffrage, right to vote", "pos": "noun"},
            {"lemma": "la estabilidad presupuestaria", "translation": "budgetary stability", "pos": "expression"},
            {"lemma": "la discapacidad", "translation": "disability", "pos": "noun"},
            {"lemma": "la dignidad", "translation": "dignity", "pos": "noun"}
        ]
    }
    write_json("content/es-es/vocabulary/b1/b1-constitucion-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.constitucion.05",
        "lesson": "b1-constitucion-05",
        "title": "El Estado de las Autonomías y la solidaridad territorial",
        "theme": "La Constitución Española",
        "words": [
            {"lemma": "indisoluble", "translation": "indissoluble", "pos": "adjective"},
            {"lemma": "la autonomía", "translation": "autonomy, self-government", "pos": "noun"},
            {"lemma": "la solidaridad", "translation": "solidarity", "pos": "noun"},
            {"lemma": "el estatuto de autonomía", "translation": "statute of autonomy", "pos": "expression"},
            {"lemma": "el municipio", "translation": "municipality", "pos": "noun"},
            {"lemma": "la provincia", "translation": "province", "pos": "noun"},
            {"lemma": "la competencia", "translation": "jurisdiction, power, competence", "pos": "noun"},
            {"lemma": "descentralizar", "translation": "to decentralize", "pos": "verb"}
        ]
    }
    write_json("content/es-es/vocabulary/b1/b1-constitucion-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.constitucion.01.se-pasiva-constitucional",
        "title": "Pasiva refleja con «se» en textos constitucionales",
        "sections": [
            {
                "type": "text",
                "content": "En el lenguaje jurídico y en el examen CCSE es muy frecuente emplear estructuras con *se* (*se constituye*, *se aprobó*, *se publicó*) para expresar normas y hechos institucionales de forma objetiva, donde lo esencial es la ley o la institución misma. El verbo concuerda en número (singular o plural) con el sujeto paciente."
            },
            {
                "type": "examples",
                "items": [
                    {
                        "spanish": "España se constituye en un Estado social y democrático de Derecho.",
                        "english": "Spain is constituted as a social and democratic State under the rule of law."
                    },
                    {
                        "spanish": "La Constitución Española se aprobó en referéndum el 6 de diciembre de 1978.",
                        "english": "The Spanish Constitution was approved by referendum on December 6, 1978."
                    },
                    {
                        "spanish": "Las leyes se publican en el Boletín Oficial del Estado para que entren en vigor.",
                        "english": "Laws are published in the Official State Gazette in order to enter into force."
                    },
                    {
                        "spanish": "En las elecciones de 1977 se eligieron las Cortes que redactaron el texto constitucional.",
                        "english": "In the 1977 elections, the Cortes that drafted the constitutional text were elected."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "Fíjate en la concordancia: si el elemento nombrado es singular (*la Constitución*), usamos el verbo en singular (*se aprobó*); si es plural (*las leyes*), el verbo va en plural (*se publican*)."
            }
        ]
    }
    write_json("content/es-es/grammar/b1/b1-constitucion-01-se-pasiva-constitucional-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.constitucion.02.corresponde-a-infinitivo",
        "title": "Atribuir funciones institucionales: «corresponder a + infinitivo»",
        "sections": [
            {
                "type": "text",
                "content": "Para describir qué órgano del Estado tiene cada competencia según la Constitución, el español administrativo utiliza la estructura *A [órgano] le/les corresponde + infinitivo*. Es una construcción equivalente a *to be the responsibility/duty of* en inglés."
            },
            {
                "type": "examples",
                "items": [
                    {
                        "spanish": "Al Rey le corresponde sancionar y promulgar las leyes aprobadas por el Parlamento.",
                        "english": "It falls to the King to sanction and promulgate the laws passed by Parliament."
                    },
                    {
                        "spanish": "A las Cortes Generales les corresponde ejercer la potestad legislativa del Estado.",
                        "english": "It belongs to the Cortes Generales to exercise the legislative power of the State."
                    },
                    {
                        "spanish": "Al Gobierno le corresponde dirigir la política interior y exterior de España.",
                        "english": "It is the Government's responsibility to direct Spain's domestic and foreign policy."
                    },
                    {
                        "spanish": "A los jueces y magistrados les corresponde administrar la justicia en nombre del Rey.",
                        "english": "It falls to judges and magistrates to administer justice in the name of the King."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "Usa el pronombre indirecto singular *le* cuando la institución es singular (*al Rey le corresponde*) y plural *les* cuando es plural (*a las Cortes les corresponde*)."
            }
        ]
    }
    write_json("content/es-es/grammar/b1/b1-constitucion-02-corresponde-a-infinitivo-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.constitucion.03.el-deber-de-y-el-derecho-a",
        "title": "Derechos y deberes: «el deber de» vs. «el derecho a»",
        "sections": [
            {
                "type": "text",
                "content": "El artículo 3 de la Constitución distingue con gran precisión entre las obligaciones y las garantías ciudadanas mediante dos preposiciones fijas: *tener el deber de + infinitivo* (obligación legal) y *tener el derecho a + infinitivo o sustantivo* (libertad garantizada)."
            },
            {
                "type": "examples",
                "items": [
                    {
                        "spanish": "Todos los españoles tienen el deber de conocer el castellano y el derecho a usarlo.",
                        "english": "All Spaniards have the duty to know Castilian Spanish and the right to use it."
                    },
                    {
                        "spanish": "Los ciudadanos tienen el derecho a participar en los asuntos públicos.",
                        "english": "Citizens have the right to participate in public affairs."
                    },
                    {
                        "spanish": "Los poderes públicos tienen el deber de proteger el patrimonio lingüístico y cultural.",
                        "english": "Public authorities have the duty to protect linguistic and cultural heritage."
                    },
                    {
                        "spanish": "Nadie puede ser discriminado en el ejercicio de su derecho a la igualdad ante la ley.",
                        "english": "No one may be discriminated against in the exercise of their right to equality before the law."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda la pareja de preposiciones para el examen CCSE: *deber DE* (conocerla) y *derecho A* (usarla)."
            }
        ]
    }
    write_json("content/es-es/grammar/b1/b1-constitucion-03-el-deber-de-y-el-derecho-a-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.constitucion.04.para-que-subjuntivo-reforma",
        "title": "Finalidad legislativa: «para que + presente o imperfecto de subjuntivo»",
        "sections": [
            {
                "type": "text",
                "content": "Cuando explicamos el propósito de una reforma constitucional o de un requisito legal con cambio de sujeto, empleamos *para que* seguido de subjuntivo: presente de subjuntivo si nos referimos a una norma vigente hoy, o imperfecto de subjuntivo (*pudieran*, *garantizara*) si narramos una reforma histórica."
            },
            {
                "type": "examples",
                "items": [
                    {
                        "spanish": "En 1992 se reformó el artículo 13.2 para que los ciudadanos europeos pudieran ser elegidos en elecciones municipales.",
                        "english": "In 1992, Article 13.2 was amended so that European citizens could stand for election in municipal elections."
                    },
                    {
                        "spanish": "La Constitución exige mayorías cualificadas para que ninguna reforma se apruebe sin un amplio consenso.",
                        "english": "The Constitution requires qualified majorities so that no reform is passed without broad consensus."
                    },
                    {
                        "spanish": "En 2024 se modificó el artículo 49 para que el texto constitucional reflejara la dignidad de las personas con discapacidad.",
                        "english": "In 2024, Article 49 was amended so that the constitutional text would reflect the dignity of persons with disabilities."
                    },
                    {
                        "spanish": "El referéndum se convoca para que la ciudadanía ratifique directamente los cambios esenciales.",
                        "english": "A referendum is called so that the citizenry directly ratifies essential changes."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "Si el verbo principal está en pasado (*se reformó*, *se modificó*), el verbo detrás de *para que* va en imperfecto de subjuntivo (*pudieran*, *reflejara*)."
            }
        ]
    }
    write_json("content/es-es/grammar/b1/b1-constitucion-04-para-que-subjuntivo-reforma-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.constitucion.05.si-bien-concesivas",
        "title": "Concesión formal: «si bien» para equilibrar unidad y autonomía",
        "sections": [
            {
                "type": "text",
                "content": "El diseño territorial español combina dos principios complementarios: unidad estatal y descentralización autonómica. En el registro culto y constitucional, el conector *si bien* (seguido de indicativo) permite contrastar dos realidades verdaderas con elegancia, equivalente a *while it is true that / although*."
            },
            {
                "type": "examples",
                "items": [
                    {
                        "spanish": "Si bien la Constitución se fundamenta en la unidad de España, garantiza plenamente el derecho a la autonomía.",
                        "english": "While the Constitution is founded on the unity of Spain, it fully guarantees the right to autonomy."
                    },
                    {
                        "spanish": "Cada comunidad tiene su propio Estatuto, si bien todas deben respetar el principio de solidaridad.",
                        "english": "Each community has its own Statute, although all must respect the principle of solidarity."
                    },
                    {
                        "spanish": "Si bien Ceuta y Melilla no son comunidades autónomas, cuentan con estatutos de ciudades autónomas.",
                        "english": "While Ceuta and Melilla are not autonomous communities, they have statutes as autonomous cities."
                    },
                    {
                        "spanish": "Las comunidades gestionan la sanidad y la educación, si bien el Estado conserva competencias exclusivas.",
                        "english": "Communities manage healthcare and education, while the State retains exclusive powers."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "A diferencia de *aunque* (que puede llevar indicativo o subjuntivo), *si bien* introduce siempre un hecho real y comprobado, por lo que va seguido de indicativo."
            }
        ]
    }
    write_json("content/es-es/grammar/b1/b1-constitucion-05-si-bien-concesivas-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 lesson stories + 1 combined story)
    # -------------------------------------------------------------------------
    p_01 = [
        {"type": "narration", "text": "Madrid, otoño de 1978. Tras casi cuatro décadas de dictadura franquista, España vivía un momento decisivo de su historia contemporánea: construir en paz una democracia para todos."},
        {"type": "narration", "text": "Siete diputados de ideologías muy distintas, conocidos como los «padres de la Constitución», trabajaron durante meses buscando el consenso para redactar una ley fundamental que no excluyera a nadie."},
        {"type": "narration", "text": "El texto fue aprobado primero por las Cortes Generales el 31 de octubre de 1978. Pocas semanas después, el 6 de diciembre de 1978, el pueblo español acudió a las urnas y ratificó la Constitución en referéndum con una amplísima mayoría."},
        {"type": "narration", "text": "El rey Juan Carlos I sancionó la Carta Magna el 27 de diciembre y, finalmente, el texto entró en vigor el 29 de diciembre de 1978 al publicarse en el Boletín Oficial del Estado (BOE)."},
        {"type": "narration", "text": "Su primer artículo proclamaba una transformación histórica: España se constituye en un Estado social y democrático de Derecho, y la soberanía nacional reside en el pueblo español, del que emanan todos los poderes del Estado."}
    ]
    story_01 = {
        "id": "story.b1.constitucion.01",
        "title": "El referéndum de 1978 y la soberanía nacional",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "How the seven 'Fathers of the Constitution' forged consensus in 1978, leading to the historic December 6 referendum and the proclamation that national sovereignty resides in the Spanish people.",
        "characters": [],
        "location": "Madrid, Congreso de los Diputados",
        "grammar": ["se-pasiva-constitucional"],
        "vocabularyTopics": ["La Constitución de 1978", "Soberanía nacional"],
        "paragraphs": p_01,
        "narration": make_narration(
            p_01,
            ["se-pasiva-constitucional"],
            [
                {"lemma": "soberanía", "pos": "noun", "cefr": "B1", "gloss": "sovereignty"},
                {"lemma": "referéndum", "pos": "noun", "cefr": "B1", "gloss": "referendum"},
                {"lemma": "consenso", "pos": "noun", "cefr": "B1", "gloss": "consensus"}
            ],
            [
                {
                    "question": "¿En qué fecha ratificó el pueblo español la Constitución en referéndum?",
                    "options": [
                        "El 6 de diciembre de 1978",
                        "El 31 de octubre de 1975",
                        "El 12 de octubre de 1978",
                        "El 29 de diciembre de 1982"
                    ],
                    "correctIndex": 0,
                    "explanation": "El pueblo español ratificó la Constitución mediante referéndum el 6 de diciembre de 1978, fecha en la que se celebra el Día de la Constitución."
                },
                {
                    "question": "Según el artículo 1.2 de la Constitución, ¿en quién reside la soberanía nacional?",
                    "options": [
                        "En el pueblo español, del que emanan los poderes del Estado",
                        "Exclusivamente en el Gobierno y los ministros",
                        "En el Tribunal Constitucional",
                        "En la Corona y el Senado"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 1.2 establece que la soberanía nacional reside en el pueblo español."
                },
                {
                    "question": "¿Cuándo entró oficialmente en vigor la Constitución Española?",
                    "options": [
                        "El 29 de diciembre de 1978, con su publicación en el Boletín Oficial del Estado (BOE)",
                        "El mismo día de las elecciones de 1977",
                        "El 1 de enero de 1979 tras un decreto real",
                        "Antes de ser votada por las Cortes Generales"
                    ],
                    "correctIndex": 0,
                    "explanation": "Tras ser sancionada el 27 de diciembre, entró en vigor el 29 de diciembre de 1978 al publicarse en el BOE."
                }
            ]
        )
    }
    write_json("content/es-es/stories/world/b1/b1-constitucion-01-origenes.json", story_01)

    p_02 = [
        {"type": "narration", "text": "Una de las cuestiones más delicadas de la Transición fue definir cómo convivirían la tradición histórica de la Corona y la plena democracia moderna."},
        {"type": "narration", "text": "El artículo 1.3 de la Constitución dio la respuesta precisa: la forma política del Estado español es la monarquía parlamentaria."},
        {"type": "narration", "text": "En este sistema, el Rey es el Jefe del Estado y símbolo de su unidad y permanencia, pero no dirige la política nacional: como resume el principio clásico del constitucionalismo europeo, «el Rey reina, pero no gobierna»."},
        {"type": "narration", "text": "Al monarca le corresponde arbitrar y moderar el funcionamiento regular de las instituciones, así como sancionar y promulgar las leyes que aprueban los representantes de los ciudadanos."},
        {"type": "narration", "text": "Para evitar cualquier abuso de autoridad, la Constitución consagra la separación de tres poderes independientes: el poder legislativo en las Cortes Generales, el poder ejecutivo en el Gobierno y el poder judicial en los jueces y magistrados."}
    ]
    story_02 = {
        "id": "story.b1.constitucion.02",
        "title": "La monarquía parlamentaria y la separación de poderes",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Why Spain's political form is a parliamentary monarchy where the King is Head of State and symbol of unity, while legislative, executive, and judicial powers remain strictly separated.",
        "characters": [],
        "location": "Madrid, Palacio de las Cortes",
        "grammar": ["corresponde-a-infinitivo"],
        "vocabularyTopics": ["Monarquía parlamentaria", "Separación de poderes"],
        "paragraphs": p_02,
        "narration": make_narration(
            p_02,
            ["corresponde-a-infinitivo"],
            [
                {"lemma": "monarquía parlamentaria", "pos": "expression", "cefr": "B1", "gloss": "parliamentary monarchy"},
                {"lemma": "arbitrar", "pos": "verb", "cefr": "B1", "gloss": "to arbitrate"},
                {"lemma": "sancionar", "pos": "verb", "cefr": "B1", "gloss": "to sanction"}
            ],
            [
                {
                    "question": "¿Cuál es la forma política del Estado español según el artículo 1.3 de la Constitución?",
                    "options": [
                        "La monarquía parlamentaria",
                        "La república federal",
                        "La monarquía absoluta",
                        "La confederación autonómica"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 1.3 establece que la forma política del Estado español es la monarquía parlamentaria."
                },
                {
                    "question": "¿Qué papel desempeña el Rey según la Constitución?",
                    "options": [
                        "Es el Jefe del Estado, símbolo de su unidad y permanencia, y arbitra y modera las instituciones",
                        "Dirige el poder ejecutivo y redacta los presupuestos del Estado",
                        "Preside el Tribunal Constitucional y dicta sentencias judiciales",
                        "Aprueba en solitario las leyes sin intervención de las Cortes"
                    ],
                    "correctIndex": 0,
                    "explanation": "El Rey ostenta la Jefatura del Estado y representa la unidad y permanencia del país, sin ejercer el poder ejecutivo ni el legislativo."
                },
                {
                    "question": "¿Cómo se dividen los tres poderes del Estado en la Constitución Española?",
                    "options": [
                        "Legislativo (Cortes Generales), ejecutivo (Gobierno) y judicial (jueces y magistrados)",
                        "Estatal, autonómico y municipal",
                        "Militar, civil y eclesiástico",
                        "Real, senatorial y ministerial"
                    ],
                    "correctIndex": 0,
                    "explanation": "La separación de poderes atribuye la potestad legislativa a las Cortes, la ejecutiva al Gobierno y la judicial a los jueces y magistrados."
                }
            ]
        )
    }
    write_json("content/es-es/stories/world/b1/b1-constitucion-02-monarquia.json", story_02)

    p_03 = [
        {"type": "narration", "text": "Una Constitución no es solo un reglamento de instituciones: es también una declaración de valores y un espejo de la pluralidad cultural del país."},
        {"type": "narration", "text": "Desde su primer artículo, España propugna como valores superiores de su ordenamiento jurídico cuatro pilares fundamentales: la libertad, la justicia, la igualdad y el pluralismo político."},
        {"type": "narration", "text": "En el artículo 3, la Constitución establece que el castellano es la lengua española oficial del Estado, y añade que todos los españoles tienen el deber de conocerla y el derecho a usarla."},
        {"type": "narration", "text": "Al mismo tiempo, reconoce que las demás lenguas españolas —como el catalán, el gallego, el euskera o el valenciano— son también oficiales en sus respectivas comunidades autónomas y constituyen un patrimonio cultural que será objeto de especial respeto y protección."},
        {"type": "narration", "text": "Por último, los artículos 4 y 5 fijan los símbolos comunes: la bandera formada por tres franjas horizontales —roja, amarilla y roja, siendo la amarilla de doble anchura que cada una de las rojas— y la capital del Estado en la villa de Madrid."}
    ]
    story_03 = {
        "id": "story.b1.constitucion.03",
        "title": "Valores superiores, lenguas oficiales y símbolos",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The four supreme values of Spain's legal order (liberty, justice, equality, political pluralism), the status of Castilian and the co-official languages, the flag's proportions, and Madrid as capital.",
        "characters": [],
        "location": "España",
        "grammar": ["el-deber-de-y-el-derecho-a"],
        "vocabularyTopics": ["Valores superiores", "Lenguas cooficiales", "Bandera de España"],
        "paragraphs": p_03,
        "narration": make_narration(
            p_03,
            ["el-deber-de-y-el-derecho-a"],
            [
                {"lemma": "pluralismo político", "pos": "expression", "cefr": "B1", "gloss": "political pluralism"},
                {"lemma": "cooficial", "pos": "adjective", "cefr": "B1", "gloss": "co-official"},
                {"lemma": "franja", "pos": "noun", "cefr": "B1", "gloss": "stripe"}
            ],
            [
                {
                    "question": "¿Cuáles son los cuatro valores superiores del ordenamiento jurídico español según el artículo 1.1?",
                    "options": [
                        "La libertad, la justicia, la igualdad y el pluralismo político",
                        "El trabajo, la propiedad, la seguridad y el comercio",
                        "La tradición, la jerarquía, el orden y la soberanía",
                        "La solidaridad, el ahorro, la defensa y la diplomacia"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 1.1 propugna como valores superiores la libertad, la justicia, la igualdad y el pluralismo político."
                },
                {
                    "question": "¿Qué dispone el artículo 3 de la Constitución respecto al castellano?",
                    "options": [
                        "Es la lengua oficial del Estado; todos los españoles tienen el deber de conocerla y el derecho a usarla",
                        "Es la única lengua permitida en todo el territorio nacional",
                        "Su conocimiento es opcional según la comunidad autónoma",
                        "Solo es oficial en las instituciones europeas"
                    ],
                    "correctIndex": 0,
                    "explanation": "El castellano es la lengua española oficial del Estado, con el deber de conocerla y el derecho a usarla, junto a las lenguas cooficiales en sus comunidades."
                },
                {
                    "question": "¿Cómo son las tres franjas horizontales de la bandera de España según el artículo 4.1?",
                    "options": [
                        "Roja, amarilla y roja, siendo la amarilla de doble anchura que cada una de las rojas",
                        "Tres franjas de idéntica anchura: roja, blanca y amarilla",
                        "Amarilla, roja y amarilla en sentido vertical",
                        "Dos franjas horizontales de igual tamaño, roja y amarilla"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 4.1 define la bandera con tres franjas horizontales (roja, amarilla y roja), siendo la amarilla de doble anchura que cada una de las rojas."
                }
            ]
        )
    }
    write_json("content/es-es/stories/world/b1/b1-constitucion-03-valores.json", story_03)

    p_04 = [
        {"type": "narration", "text": "¿Cómo está organizado el texto de la Constitución Española? La Carta Magna consta exactamente de 169 artículos, precedidos por un Preámbulo solemne y repartidos entre un Título Preliminar y diez Títulos numerados."},
        {"type": "narration", "text": "El Título I, el más extenso de todos, está dedicado a los derechos y deberes fundamentales de las personas, mientras que los demás títulos regulan la Corona, las Cortes, el Gobierno, el Poder Judicial, la economía, las autonomías y el Tribunal Constitucional."},
        {"type": "narration", "text": "Los redactores de 1978 diseñaron una Constitución rígida en su Título X, exigiendo mayorías cualificadas de tres quintos o dos tercios de las cámaras para que ninguna mayoría pasajera pudiera alterar las reglas del juego sin un amplio acuerdo."},
        {"type": "narration", "text": "Por esa razón, en casi medio siglo de democracia la Constitución solo se ha reformado en tres ocasiones puntuales: en 1992, para que los ciudadanos de la Unión Europea pudieran ser votados en las elecciones municipales tras el Tratado de Maastricht; en 2011, para consagrar en el artículo 135 el principio de estabilidad presupuestaria."},
        {"type": "narration", "text": "La tercera reforma tuvo lugar en enero de 2024, cuando las Cortes actualizaron el artículo 49 para eliminar el término «disminuidos» y reforzar la plena inclusión, autonomía y dignidad de las personas con discapacidad."}
    ]
    story_04 = {
        "id": "story.b1.constitucion.04",
        "title": "Estructura y reforma de la Constitución",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The architecture of the 169 articles across the Preliminary Title and ten Titles, and the three historic constitutional amendments of 1992, 2011, and 2024.",
        "characters": [],
        "location": "Madrid",
        "grammar": ["para-que-subjuntivo-reforma"],
        "vocabularyTopics": ["Estructura constitucional", "Reformas de 1992, 2011 y 2024"],
        "paragraphs": p_04,
        "narration": make_narration(
            p_04,
            ["para-que-subjuntivo-reforma"],
            [
                {"lemma": "preámbulo", "pos": "noun", "cefr": "B1", "gloss": "preamble"},
                {"lemma": "reforma constitucional", "pos": "expression", "cefr": "B1", "gloss": "constitutional reform"},
                {"lemma": "mayoría cualificada", "pos": "expression", "cefr": "B1", "gloss": "qualified majority"}
            ],
            [
                {
                    "question": "¿Cuántos artículos tiene la Constitución Española de 1978?",
                    "options": [
                        "169 artículos",
                        "50 artículos",
                        "350 artículos",
                        "17 artículos"
                    ],
                    "correctIndex": 0,
                    "explanation": "La Constitución Española consta de 169 artículos distribuidos en un Título Preliminar y diez Títulos."
                },
                {
                    "question": "¿Por qué se reformó por primera vez la Constitución en 1992?",
                    "options": [
                        "Para permitir el sufragio pasivo de los ciudadanos de la Unión Europea en las elecciones municipales (Tratado de Maastricht)",
                        "Para cambiar la capital del Estado a otra ciudad",
                        "Para suprimir el Senado y crear una sola cámara",
                        "Para introducir el euro como moneda oficial antes de 1995"
                    ],
                    "correctIndex": 0,
                    "explanation": "La reforma de 1992 modificó el artículo 13.2 para adaptarlo al Tratado de Maastricht."
                },
                {
                    "question": "¿Qué aspecto renovó la tercera reforma constitucional aprobada en 2024?",
                    "options": [
                        "Modificó el artículo 49 para reforzar los derechos y la dignidad de las personas con discapacidad",
                        "Cambió la duración del mandato parlamentario a seis años",
                        "Modificó los colores de la bandera nacional",
                        "Redujo el número de comunidades autónomas"
                    ],
                    "correctIndex": 0,
                    "explanation": "En 2024 se reformó el artículo 49, sustituyendo la palabra «disminuidos» por «personas con discapacidad»."
                }
            ]
        )
    }
    write_json("content/es-es/stories/world/b1/b1-constitucion-04-reforma.json", story_04)

    p_05 = [
        {"type": "narration", "text": "¿Cómo organizar un país con una profunda diversidad histórica, geográfica y lingüística sin romper su cohesión? Ese fue el gran reto territorial que resolvieron el artículo 2 y el Título VIII de la Constitución."},
        {"type": "narration", "text": "El artículo 2 establece que la Constitución se fundamenta en la indisoluble unidad de la Nación española y, en la misma frase, reconoce y garantiza el derecho a la autonomía de las nacionalidades y regiones que la integran y la solidaridad entre todas ellas."},
        {"type": "narration", "text": "A partir de este principio nació el llamado Estado de las Autonomías: el territorio español se organiza en municipios, en provincias y en diecisiete comunidades autónomas, además de las dos ciudades autónomas de Ceuta y Melilla en el norte de África."},
        {"type": "narration", "text": "Cada comunidad autónoma se rige por su norma institucional básica, el Estatuto de Autonomía, que es aprobado como ley orgánica por las Cortes Generales y define sus instituciones propias y sus competencias."},
        {"type": "narration", "text": "Si bien las comunidades autónomas gestionan servicios esenciales para la vida diaria como la sanidad y la educación, el principio constitucional de solidaridad prohíbe cualquier privilegio económico o social entre los españoles de distintos territorios."}
    ]
    story_05 = {
        "id": "story.b1.constitucion.05",
        "title": "El Estado de las Autonomías y la solidaridad territorial",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "How Article 2 and Title VIII balance the indissoluble unity of the Spanish Nation with the right to autonomy of its 17 Autonomous Communities and 2 Autonomous Cities.",
        "characters": [],
        "location": "España, 17 Comunidades Autónomas",
        "grammar": ["si-bien-concesivas"],
        "vocabularyTopics": ["Estado de las Autonomías", "Estatuto de Autonomía", "Solidaridad territorial"],
        "paragraphs": p_05,
        "narration": make_narration(
            p_05,
            ["si-bien-concesivas"],
            [
                {"lemma": "autonomía", "pos": "noun", "cefr": "B1", "gloss": "autonomy"},
                {"lemma": "solidaridad", "pos": "noun", "cefr": "B1", "gloss": "solidarity"},
                {"lemma": "estatuto de autonomía", "pos": "expression", "cefr": "B1", "gloss": "statute of autonomy"}
            ],
            [
                {
                    "question": "¿Qué tres principios une el artículo 2 de la Constitución Española?",
                    "options": [
                        "La unidad de la Nación española, el derecho a la autonomía de nacionalidades y regiones, y la solidaridad entre todas ellas",
                        "La independencia fiscal de cada provincia, la centralización total y las aduanas interiores",
                        "El sistema federal presidencialista y la soberanía de cada municipio",
                        "La división del territorio únicamente en regiones militares"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 2 articula la unidad de la Nación, el derecho a la autonomía y la solidaridad interterritorial."
                },
                {
                    "question": "¿Cómo se organiza territorialmente el Estado según el Título VIII de la Constitución?",
                    "options": [
                        "En municipios, en provincias y en las comunidades autónomas que se constituyan (17 comunidades y 2 ciudades autónomas)",
                        "En departamentos federales y cantones",
                        "Solamente en cincuenta provincias sin gobiernos regionales",
                        "En cuatro reinos históricos sin municipios"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 137 (Título VIII) dispone que el Estado se organiza territorialmente en municipios, provincias y comunidades autónomas."
                },
                {
                    "question": "¿Cuál es la norma institucional básica de cada comunidad autónoma?",
                    "options": [
                        "El Estatuto de Autonomía",
                        "El Reglamento Municipal",
                        "El Decreto Provincial",
                        "El Tratado Regional"
                    ],
                    "correctIndex": 0,
                    "explanation": "Según el artículo 147 de la Constitución, los Estatutos son la norma institucional básica de cada comunidad autónoma."
                }
            ]
        )
    }
    write_json("content/es-es/stories/world/b1/b1-constitucion-05-autonomias.json", story_05)

    p_comb = [
        {"type": "narration", "text": "Aprobada por las Cortes el 31 de octubre de 1978, ratificada en referéndum por los ciudadanos el 6 de diciembre y en vigor desde su publicación en el BOE el 29 de diciembre de 1978, la Constitución Española constituye a España en un Estado social y democrático de Derecho cuya soberanía nacional reside en el pueblo español."},
        {"type": "narration", "text": "Su artículo 1.3 define la monarquía parlamentaria como forma política del Estado: el Rey es el Jefe del Estado y símbolo de su unidad y permanencia, mientras el poder se divide entre las Cortes Generales (legislativo), el Gobierno (ejecutivo) y los jueces y magistrados (judicial)."},
        {"type": "narration", "text": "El ordenamiento jurídico propugna cuatro valores superiores —libertad, justicia, igualdad y pluralismo político—, declara oficial el castellano en todo el Estado junto a las lenguas cooficiales en sus comunidades, describe la bandera rojigualda y fija la capital en Madrid."},
        {"type": "narration", "text": "Compuesta por 169 artículos en un Título Preliminar y diez Títulos, la Constitución requiere mayorías cualificadas para su reforma y solo se ha modificado en tres ocasiones: 1992 (sufragio municipal europeo), 2011 (estabilidad presupuestaria) y 2024 (derechos de las personas con discapacidad)."},
        {"type": "narration", "text": "Por último, el artículo 2 y el Título VIII articulan el Estado de las Autonomías: diecisiete comunidades autónomas y las dos ciudades autónomas de Ceuta y Melilla, regidas por sus Estatutos de Autonomía bajo los principios de unidad y solidaridad."}
    ]
    story_combined = {
        "id": "story.b1.constitucion",
        "title": "La Constitución Española de 1978",
        "level": "B1",
        "order": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Complete overview of the 1978 Spanish Constitution for the CCSE exam: its birth in the Transition referendum, parliamentary monarchy, fundamental values, oficial languages, structure, reforms, and the State of Autonomies.",
        "characters": [],
        "location": "España",
        "grammar": [
            "se-pasiva-constitucional",
            "corresponde-a-infinitivo",
            "el-deber-de-y-el-derecho-a",
            "para-que-subjuntivo-reforma",
            "si-bien-concesivas"
        ],
        "vocabularyTopics": [
            "La Constitución Española de 1978",
            "Monarquía parlamentaria",
            "Valores superiores y símbolos",
            "Reforma constitucional",
            "Estado de las Autonomías"
        ],
        "paragraphs": p_comb,
        "narration": make_narration(
            p_comb,
            ["se-pasiva-constitucional", "corresponde-a-infinitivo"],
            [
                {"lemma": "soberanía", "pos": "noun", "cefr": "B1", "gloss": "sovereignty"},
                {"lemma": "monarquía parlamentaria", "pos": "expression", "cefr": "B1", "gloss": "parliamentary monarchy"},
                {"lemma": "estatuto de autonomía", "pos": "expression", "cefr": "B1", "gloss": "statute of autonomy"}
            ],
            [
                {
                    "question": "¿Cómo define el artículo 1 de la Constitución al Estado español y su forma política?",
                    "options": [
                        "Un Estado social y democrático de Derecho cuya forma política es la monarquía parlamentaria",
                        "Una república parlamentaria centralizada",
                        "Una confederación de estados soberanos",
                        "Una monarquía constitucional sin parlamento"
                    ],
                    "correctIndex": 0,
                    "explanation": "El artículo 1 define a España como Estado social y democrático de Derecho (1.1) y su forma política como monarquía parlamentaria (1.3)."
                },
                {
                    "question": "¿Cuántos artículos componen la Constitución y cuántas veces ha sido reformada?",
                    "options": [
                        "Tiene 169 artículos y ha sido reformada tres veces (1992, 2011 y 2024)",
                        "Tiene 100 artículos y nunca ha sido reformada",
                        "Tiene 250 artículos y se reforma cada cuatro años",
                        "Tiene 169 artículos y ha sido reformada diez veces"
                    ],
                    "correctIndex": 0,
                    "explanation": "Consta de 169 artículos y ha experimentado tres reformas puntuales: en 1992, 2011 y 2024."
                },
                {
                    "question": "¿Cuántas comunidades y ciudades autónomas integran la organización territorial de España?",
                    "options": [
                        "17 comunidades autónomas y 2 ciudades autónomas (Ceuta y Melilla)",
                        "15 comunidades autónomas y 3 ciudades autónomas",
                        "19 comunidades autónomas sin ciudades autónomas",
                        "50 comunidades autónomas"
                    ],
                    "correctIndex": 0,
                    "explanation": "España se organiza en 17 comunidades autónomas y 2 ciudades autónomas (Ceuta y Melilla)."
                }
            ]
        )
    }
    write_json("content/es-es/stories/world/b1/b1-constitucion.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (5 lessons x 9 exercises + 1 consolidation x 18 exercises)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-constitucion-01",
        "exercises": [
            {
                "id": "b1-constitucion-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la soberanía", "sovereignty"],
                    ["el referéndum", "referendum"],
                    ["ratificar", "to ratify"],
                    ["emanar", "to emanate, originate from"]
                ]
            },
            {
                "id": "b1-constitucion-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el consenso", "consensus"],
                    ["entrar en vigor", "to enter into force"],
                    ["el boletín oficial", "official state gazette"],
                    ["el Estado de Derecho", "rule of law"]
                ]
            },
            {
                "id": "b1-constitucion-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿En qué fecha ratificaron los españoles en referéndum la Constitución de 1978?",
                "options": [
                    "El 6 de diciembre de 1978.",
                    "El 12 de octubre de 1978.",
                    "El 23 de febrero de 1981."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-01.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según el artículo 1.2 de la Constitución Española, ¿dónde reside la soberanía nacional?",
                "options": [
                    "En el pueblo español, del que emanan los poderes del Estado.",
                    "En el Gobierno de la Nación y el Consejo de Ministros.",
                    "En el Tribunal Supremo y el Consejo General del Poder Judicial."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-01.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "España ___ constituye en un Estado social y democrático de Derecho. (se)",
                "answer": "se",
                "teaches": ["se-pasiva-constitucional"],
                "english": "Spain is constituted as a social and democratic State under the rule of law."
            },
            {
                "id": "b1-constitucion-01.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cuándo entró en vigor la Constitución Española?",
                "options": [
                    "El 29 de diciembre de 1978, el día de su publicación en el Boletín Oficial del Estado (BOE).",
                    "El 31 de octubre de 1978, antes del referéndum nacional.",
                    "El 1 de enero de 1986, con la entrada en la Comunidad Europea."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-01.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": [
                    "La", "soberanía", "nacional", "reside", "en", "el", "pueblo", "español."
                ],
                "solution": [
                    "La", "soberanía", "nacional", "reside", "en", "el", "pueblo", "español."
                ],
                "english": "National sovereignty resides in the Spanish people.",
                "teaches": ["se-pasiva-constitucional"]
            },
            {
                "id": "b1-constitucion-01.ex07",
                "type": "dialogue-complete",
                "category": "reading",
                "prompt": [
                    {"speaker": "Elena", "text": "¿Por qué es festivo en toda España el 6 de diciembre?"},
                    {"speaker": "Marco", "text": "_____"}
                ],
                "options": [
                    "Porque ese día de 1978 el pueblo español ratificó la Constitución mediante referéndum.",
                    "Porque ese día se celebraron las primeras elecciones municipales de la historia.",
                    "Porque ese día España firmó su adhesión a la Unión Europea."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-01.ex08",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "La Constitución entró en vigor el 29 de diciembre de 1978 tras publicarse en el Boletín Oficial del Estado.",
                "options": [
                    "The Constitution entered into force on December 29, 1978 after being published in the Official State Gazette.",
                    "The Constitution was rejected in the December 1978 national referendum.",
                    "The Constitution was drafted without the participation of Parliament."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/es-es/exercises/b1/b1-constitucion-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-constitucion-02",
        "exercises": [
            {
                "id": "b1-constitucion-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la monarquía parlamentaria", "parliamentary monarchy"],
                    ["la jefatura del Estado", "headship of State"],
                    ["arbitrar", "to arbitrate"],
                    ["moderar", "to moderate"]
                ]
            },
            {
                "id": "b1-constitucion-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["sancionar", "to sanction (laws)"],
                    ["promulgar", "to promulgate, enact"],
                    ["la separación de poderes", "separation of powers"],
                    ["la permanencia", "permanence, continuity"]
                ]
            },
            {
                "id": "b1-constitucion-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cuál es la forma política del Estado español según la Constitución?",
                "options": [
                    "La monarquía parlamentaria.",
                    "La república federal.",
                    "La monarquía absoluta."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-02.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Quién es el Jefe del Estado y símbolo de su unidad y permanencia?",
                "options": [
                    "El Rey.",
                    "El Presidente del Gobierno.",
                    "El Presidente del Congreso de los Diputados."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-02.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Al Rey le ___ sancionar y promulgar las leyes aprobadas por las Cortes. (corresponder)",
                "answer": "corresponde",
                "teaches": ["corresponde-a-infinitivo"],
                "english": "It falls to the King to sanction and promulgate the laws passed by the Cortes."
            },
            {
                "id": "b1-constitucion-02.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué institución ejerce la potestad legislativa del Estado en España?",
                "options": [
                    "Las Cortes Generales (Congreso de los Diputados y Senado).",
                    "El Consejo General del Poder Judicial.",
                    "El Consejo de Estado."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-02.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": [
                    "La", "forma", "política", "del", "Estado", "español", "es", "la", "monarquía", "parlamentaria."
                ],
                "solution": [
                    "La", "forma", "política", "del", "Estado", "español", "es", "la", "monarquía", "parlamentaria."
                ],
                "english": "The political form of the Spanish State is the parliamentary monarchy.",
                "teaches": ["corresponde-a-infinitivo"]
            },
            {
                "id": "b1-constitucion-02.ex07",
                "type": "dialogue-complete",
                "category": "reading",
                "prompt": [
                    {"speaker": "Lucía", "text": "¿Significa la monarquía parlamentaria que el Rey dirige el Gobierno?"},
                    {"speaker": "David", "text": "_____"}
                ],
                "options": [
                    "No, el Rey es el Jefe del Estado y arbitra las instituciones, pero el poder ejecutivo lo dirige el Gobierno.",
                    "Sí, el Rey nombra libremente a los jueces y redacta todas las leyes.",
                    "Sí, el Rey preside cada semana el Consejo de Ministros y vota en el Congreso."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-02.ex08",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "El Rey es el Jefe del Estado, símbolo de su unidad y permanencia, y arbitra el funcionamiento regular de las instituciones.",
                "options": [
                    "The King is the Head of State, symbol of its unity and permanence, and arbitrates the regular functioning of the institutions.",
                    "The Prime Minister is the Head of State and commands the judicial branch.",
                    "The Senate exercises executive power and appoints the monarch."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/es-es/exercises/b1/b1-constitucion-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-constitucion-03",
        "exercises": [
            {
                "id": "b1-constitucion-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el pluralismo político", "political pluralism"],
                    ["el ordenamiento jurídico", "legal order"],
                    ["cooficial", "co-official"],
                    ["el patrimonio cultural", "cultural heritage"]
                ]
            },
            {
                "id": "b1-constitucion-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la franja", "stripe, band"],
                    ["la anchura", "width"],
                    ["el deber", "duty, obligation"],
                    ["propugnar", "to advocate, uphold"]
                ]
            },
            {
                "id": "b1-constitucion-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cuáles son los valores superiores del ordenamiento jurídico que propugna España según el artículo 1.1?",
                "options": [
                    "La libertad, la justicia, la igualdad y el pluralismo político.",
                    "La unidad, la jerarquía, la disciplina y el comercio.",
                    "La competencia económica, la seguridad y el bipartidismo."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-03.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Según el artículo 3 de la Constitución, ¿qué relación tienen los españoles con el castellano?",
                "options": [
                    "Todos los españoles tienen el deber de conocerlo y el derecho a usarlo.",
                    "Su uso es obligatorio únicamente en la capital del Estado.",
                    "Tienen el derecho de conocerlo, pero ningún deber constitucional."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-03.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Todos los españoles tienen el deber ___ conocer la lengua oficial y el derecho a usarla. (de)",
                "answer": "de",
                "teaches": ["el-deber-de-y-el-derecho-a"],
                "english": "All Spaniards have the duty to know the official language and the right to use it."
            },
            {
                "id": "b1-constitucion-03.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cómo es la franja amarilla de la bandera de España según el artículo 4.1?",
                "options": [
                    "Es de doble anchura que cada una de las dos franjas rojas.",
                    "Tiene exactamente la misma anchura que las franjas rojas.",
                    "Es la mitad de estrecha que las franjas rojas."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-03.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": [
                    "La", "capital", "del", "Estado", "es", "la", "villa", "de", "Madrid."
                ],
                "solution": [
                    "La", "capital", "del", "Estado", "es", "la", "villa", "de", "Madrid."
                ],
                "english": "The capital of the State is the town of Madrid.",
                "teaches": ["el-deber-de-y-el-derecho-a"]
            },
            {
                "id": "b1-constitucion-03.ex07",
                "type": "dialogue-complete",
                "category": "reading",
                "prompt": [
                    {"speaker": "Clara", "text": "¿Son oficiales en toda España lenguas como el catalán, el gallego o el euskera?"},
                    {"speaker": "Jorge", "text": "_____"}
                ],
                "options": [
                    "Son también oficiales en sus respectivas comunidades autónomas, de acuerdo con sus Estatutos.",
                    "No, la Constitución prohíbe que las comunidades autónomas tengan lenguas cooficiales.",
                    "Sí, son obligatorias en las diecisiete comunidades autónomas por igual."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-03.ex08",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "España propugna como valores superiores de su ordenamiento jurídico la libertad, la justicia, la igualdad y el pluralismo político.",
                "options": [
                    "Spain upholds as supreme values of its legal order liberty, justice, equality, and political pluralism.",
                    "Spain establishes a single political party and abolishes regional languages.",
                    "The Spanish flag consists of three vertical stripes of equal width."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/es-es/exercises/b1/b1-constitucion-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-constitucion-04",
        "exercises": [
            {
                "id": "b1-constitucion-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el preámbulo", "preamble"],
                    ["la disposición", "provision, disposition"],
                    ["la reforma constitucional", "constitutional reform"],
                    ["la mayoría cualificada", "qualified supermajority"]
                ]
            },
            {
                "id": "b1-constitucion-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el sufragio", "suffrage, right to vote"],
                    ["la estabilidad presupuestaria", "budgetary stability"],
                    ["la discapacidad", "disability"],
                    ["la dignidad", "dignity"]
                ]
            },
            {
                "id": "b1-constitucion-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿De cuántos artículos consta la Constitución Española de 1978?",
                "options": [
                    "De 169 artículos.",
                    "De 120 artículos.",
                    "De 210 artículos."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-04.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué regula el Título I de la Constitución Española?",
                "options": [
                    "Los derechos y deberes fundamentales.",
                    "La organización de los municipios y las provincias.",
                    "El procedimiento de reforma constitucional."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-04.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En 1992 se reformó el artículo 13.2 para que los ciudadanos europeos ___ ser elegidos en elecciones municipales. (poder, imperfecto de subjuntivo)",
                "answer": "pudieran",
                "teaches": ["para-que-subjuntivo-reforma"],
                "english": "In 1992, Article 13.2 was amended so that European citizens could stand for election in municipal elections."
            },
            {
                "id": "b1-constitucion-04.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cuántas veces se ha reformado la Constitución Española desde 1978?",
                "options": [
                    "Tres veces: en 1992, en 2011 y en 2024.",
                    "Ninguna vez, porque la Constitución prohíbe cualquier reforma.",
                    "Más de quince veces, una en cada legislatura."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-04.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": [
                    "La", "Constitución", "exige", "mayorías", "cualificadas", "para", "que", "exista", "consenso."
                ],
                "solution": [
                    "La", "Constitución", "exige", "mayorías", "cualificadas", "para", "que", "exista", "consenso."
                ],
                "english": "The Constitution requires qualified majorities so that consensus exists.",
                "teaches": ["para-que-subjuntivo-reforma"]
            },
            {
                "id": "b1-constitucion-04.ex07",
                "type": "dialogue-complete",
                "category": "reading",
                "prompt": [
                    {"speaker": "Ana", "text": "¿Qué cambio introdujo la reforma constitucional de enero de 2024 en el artículo 49?"},
                    {"speaker": "Pablo", "text": "_____"}
                ],
                "options": [
                    "Sustituyó el término «disminuidos» por «personas con discapacidad» y reforzó la protección de sus derechos y su dignidad.",
                    "Aumentó el número de diputados del Congreso a quinientos.",
                    "Estableció la obligatoriedad del voto en las elecciones generales."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-04.ex08",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "La Constitución consta de ciento sesenta y nueve artículos repartidos en un Título Preliminar y diez Títulos.",
                "options": [
                    "The Constitution consists of 169 articles distributed across a Preliminary Title and ten Titles.",
                    "The Constitution has fifty articles and has been reformed every year since 1978.",
                    "Title X regulates the royal family rather than constitutional reform."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/es-es/exercises/b1/b1-constitucion-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-constitucion-05",
        "exercises": [
            {
                "id": "b1-constitucion-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["indisoluble", "indissoluble"],
                    ["la autonomía", "autonomy"],
                    ["la solidaridad", "solidarity"],
                    ["el estatuto de autonomía", "statute of autonomy"]
                ]
            },
            {
                "id": "b1-constitucion-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el municipio", "municipality"],
                    ["la provincia", "province"],
                    ["la competencia", "jurisdiction, competence"],
                    ["descentralizar", "to decentralize"]
                ]
            },
            {
                "id": "b1-constitucion-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cómo se organiza territorialmente el Estado español según el artículo 137 (Título VIII)?",
                "options": [
                    "En municipios, en provincias y en las comunidades autónomas que se constituyan.",
                    "Únicamente en departamentos centrales dirigidos desde Madrid.",
                    "En estados federales soberanos con ejército propio."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cuál es la norma institucional básica de cada comunidad autónoma?",
                "options": [
                    "El Estatuto de Autonomía.",
                    "La Ordenanza Municipal.",
                    "El Código Civil Provincial."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-05.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "___ bien la Constitución se fundamenta en la unidad de España, garantiza el derecho a la autonomía. (si)",
                "answer": "Si",
                "teaches": ["si-bien-concesivas"],
                "english": "While the Constitution is founded on the unity of Spain, it guarantees the right to autonomy."
            },
            {
                "id": "b1-constitucion-05.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Cuántas comunidades autónomas y ciudades autónomas forman España?",
                "options": [
                    "17 comunidades autónomas y 2 ciudades autónomas (Ceuta y Melilla).",
                    "15 comunidades autónomas y 4 ciudades autónomas.",
                    "19 comunidades autónomas y ninguna ciudad autónoma."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-05.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": [
                    "La", "Constitución", "garantiza", "la", "solidaridad", "entre", "todas", "las", "nacionalidades", "y", "regiones."
                ],
                "solution": [
                    "La", "Constitución", "garantiza", "la", "solidaridad", "entre", "todas", "las", "nacionalidades", "y", "regiones."
                ],
                "english": "The Constitution guarantees solidarity among all nationalities and regions.",
                "teaches": ["si-bien-concesivas"]
            },
            {
                "id": "b1-constitucion-05.ex07",
                "type": "dialogue-complete",
                "category": "reading",
                "prompt": [
                    {"speaker": "Marta", "text": "¿Pueden los Estatutos de Autonomía establecer privilegios económicos de unas comunidades sobre otras?"},
                    {"speaker": "Raúl", "text": "_____"}
                ],
                "options": [
                    "No, la Constitución garantiza el principio de solidaridad y prohíbe privilegios económicos o sociales entre comunidades.",
                    "Sí, las comunidades más ricas están exentas de contribuir al presupuesto estatal.",
                    "Sí, cada provincia puede fijar aduanas y aranceles frente a las provincias vecinas."
                ],
                "correct": 0
            },
            {
                "id": "b1-constitucion-05.ex08",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "El Estatuto de Autonomía es la norma institucional básica de cada comunidad autónoma, aprobada como ley orgánica por las Cortes Generales.",
                "options": [
                    "The Statute of Autonomy is the basic institutional norm of each autonomous community, passed as an organic law by the Cortes Generales.",
                    "Each municipality drafts its own constitution independent of the Cortes Generales.",
                    "Ceuta and Melilla do not belong to the Spanish constitutional system."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/es-es/exercises/b1/b1-constitucion-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-constitucion-consolidation",
        "exercises": [
            {
                "id": "b1-constitucion-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la soberanía", "sovereignty"],
                    ["el referéndum", "referendum"],
                    ["la monarquía parlamentaria", "parliamentary monarchy"],
                    ["sancionar", "to sanction (laws)"],
                    ["el pluralismo político", "political pluralism"],
                    ["cooficial", "co-official"],
                    ["la mayoría cualificada", "qualified supermajority"],
                    ["el estatuto de autonomía", "statute of autonomy"]
                ],
                "teaches": ["vocabulary-constitucion"]
            },
            {
                "id": "b1-constitucion-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración emplea correctamente la pasiva refleja con «se» según el artículo 1.1?",
                "options": [
                    "España se constituye en un Estado social y democrático de Derecho.",
                    "España constituyen en un Estado social y democrático.",
                    "Las leyes se aprobó ayer en el Boletín Oficial."
                ],
                "correct": 0,
                "teaches": ["se-pasiva-constitucional"]
            },
            {
                "id": "b1-constitucion-consolidation.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura expresa correctamente las competencias constitucionales del Rey?",
                "options": [
                    "Al Rey le corresponde sancionar y promulgar las leyes.",
                    "Al Rey les corresponden sancionar las leyes.",
                    "El Rey corresponde de sancionar las leyes."
                ],
                "correct": 0,
                "teaches": ["corresponde-a-infinitivo"]
            },
            {
                "id": "b1-constitucion-consolidation.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué combinación de preposiciones recoge el artículo 3 sobre el castellano?",
                "options": [
                    "Todos los españoles tienen el deber de conocerla y el derecho a usarla.",
                    "Todos los españoles tienen el deber a conocerla y el derecho de usarla.",
                    "Todos los españoles tienen el deber por conocerla y el derecho en usarla."
                ],
                "correct": 0,
                "teaches": ["el-deber-de-y-el-derecho-a"]
            },
            {
                "id": "b1-constitucion-consolidation.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué conector concesivo formal equilibra la unidad estatal y la autonomía territorial?",
                "options": [
                    "Si bien la Constitución se fundamenta en la unidad de España, garantiza el derecho a la autonomía.",
                    "Para que la Constitución se fundamenta en la unidad, garantiza la autonomía.",
                    "A menos que la Constitución garantiza la autonomía, existe unidad."
                ],
                "correct": 0,
                "teaches": ["si-bien-concesivas"]
            },
            {
                "id": "b1-constitucion-consolidation.ex06",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La Constitución Española ___ aprobó en referéndum el 6 de diciembre de 1978. (se)",
                "answer": "se",
                "teaches": ["se-pasiva-constitucional"],
                "english": "The Spanish Constitution was approved by referendum on December 6, 1978."
            },
            {
                "id": "b1-constitucion-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A las Cortes Generales ___ corresponde ejercer la potestad legislativa del Estado. (les)",
                "answer": "les",
                "teaches": ["corresponde-a-infinitivo"],
                "english": "It belongs to the Cortes Generales to exercise the legislative power of the State."
            },
            {
                "id": "b1-constitucion-consolidation.ex08",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En 2024 se modificó el artículo 49 para que el texto ___ la dignidad de las personas con discapacidad. (reflejar, imperfecto de subjuntivo)",
                "answer": "reflejara",
                "teaches": ["para-que-subjuntivo-reforma"],
                "english": "In 2024, Article 49 was amended so that the text would reflect the dignity of persons with disabilities."
            },
            {
                "id": "b1-constitucion-consolidation.ex09",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": [
                    "Todos", "los", "españoles", "tienen", "el", "deber", "de", "conocerla", "y", "el", "derecho", "a", "usarla."
                ],
                "solution": [
                    "Todos", "los", "españoles", "tienen", "el", "deber", "de", "conocerla", "y", "el", "derecho", "a", "usarla."
                ],
                "english": "All Spaniards have the duty to know it and the right to use it.",
                "teaches": ["el-deber-de-y-el-derecho-a"]
            },
            {
                "id": "b1-constitucion-consolidation.ex10",
                "type": "sentence-order",
                "category": "grammar",
                "sentences": [
                    "Las Cortes Generales aprobaron el texto el 31 de octubre de 1978. [The Cortes Generales approved the text on October 31, 1978.]",
                    "El pueblo español ratificó la Constitución en referéndum el 6 de diciembre. [The Spanish people ratified the Constitution in a referendum on December 6.]",
                    "Finalmente, la Constitución entró en vigor el 29 de diciembre al publicarse en el BOE. [Finally, the Constitution entered into force on December 29 upon publication in the BOE.]"
                ],
                "solution": [0, 1, 2],
                "teaches": ["se-pasiva-constitucional"]
            },
            {
                "id": "b1-constitucion-consolidation.ex11",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Qué preguntas sobre el artículo 1 suelen aparecer en el examen CCSE?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "Que España es un Estado social y democrático de Derecho, la soberanía reside en el pueblo y su forma política es la monarquía parlamentaria.",
                    "Que España es una república federal donde la soberanía reside en el Senado.",
                    "Que la Constitución fue aprobada en 1986 sin referéndum ciudadano."
                ],
                "correct": 0,
                "teaches": ["corresponde-a-infinitivo"]
            },
            {
                "id": "b1-constitucion-consolidation.ex12",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "La bandera de España está formada por tres franjas horizontales, roja, amarilla y roja, siendo la amarilla de doble anchura que cada una de las rojas.",
                "options": [
                    "The flag of Spain consists of three horizontal stripes, red, yellow, and red, the yellow one being twice as wide as each red one.",
                    "The flag of Spain has two vertical stripes of equal width.",
                    "The capital of Spain is established by municipal decree rather than the Constitution."
                ],
                "correct": 0,
                "teaches": ["el-deber-de-y-el-derecho-a"]
            },
            {
                "id": "b1-constitucion-consolidation.ex13",
                "type": "listening-choice",
                "category": "listening",
                "sentence": "La Constitución se fundamenta en la indisoluble unidad de la Nación española y garantiza el derecho a la autonomía y la solidaridad entre todas las regiones.",
                "options": [
                    "The Constitution is based on the indissoluble unity of the Spanish Nation and guarantees the right to autonomy and solidarity among all regions.",
                    "The Constitution abolishes all autonomous communities and provinces.",
                    "Only three regions in Spain have a Statute of Autonomy."
                ],
                "correct": 0,
                "teaches": ["si-bien-concesivas"]
            },
            {
                "id": "b1-constitucion-consolidation.ex14",
                "type": "dictation",
                "category": "listening",
                "sentence": "La soberanía nacional reside en el pueblo español.",
                "teaches": ["se-pasiva-constitucional"],
                "english": "National sovereignty resides in the Spanish people."
            },
            {
                "id": "b1-constitucion-consolidation.ex15",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica la forma política del Estado español y el papel del Rey según el artículo 1.3 y el Título II. [Explain the political form of the Spanish State and the role of the King.]",
                        "answer": "La forma política del Estado español es la monarquía parlamentaria, en la que el Rey es el Jefe del Estado y símbolo de su unidad y permanencia."
                    }
                ],
                "teaches": ["corresponde-a-infinitivo"]
            },
            {
                "id": "b1-constitucion-consolidation.ex16",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Resume qué establece el artículo 3 sobre el castellano y las demás lenguas españolas. [Summarise what Article 3 establishes regarding Castilian and the other Spanish languages.]",
                        "answer": "El castellano es la lengua española oficial del Estado, todos tienen el deber de conocerla y el derecho a usarla, y las demás lenguas españolas son también oficiales en sus respectivas comunidades autónomas."
                    }
                ],
                "teaches": ["el-deber-de-y-el-derecho-a"]
            },
            {
                "id": "b1-constitucion-consolidation.ex17",
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explica cómo se organiza territorialmente España y qué función cumplen los Estatutos de Autonomía. [Explain how Spain is territorially organised and what role the Statutes of Autonomy play.]",
                        "answer": "España se organiza en municipios, provincias, diecisiete comunidades autónomas y dos ciudades autónomas, y el Estatuto de Autonomía es la norma institucional básica de cada comunidad."
                    }
                ],
                "teaches": ["si-bien-concesivas"]
            },
            {
                "id": "b1-constitucion-consolidation.ex18",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "A", "text": "¿Por qué se dice que la Constitución de 1978 es una Constitución rígida?"},
                    {"speaker": "B", "text": "_____"}
                ],
                "options": [
                    "Porque exige mayorías cualificadas para que cualquier reforma cuente con un amplio consenso parlamentario.",
                    "Porque puede modificarse por simple decreto de un alcalde.",
                    "Porque no contiene ningún artículo sobre derechos fundamentales."
                ],
                "correct": 0,
                "teaches": ["para-que-subjuntivo-reforma"]
            }
        ]
    }
    write_json("content/es-es/exercises/b1/b1-constitucion-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (5 topical lessons + 1 consolidation lesson)
    # -------------------------------------------------------------------------
    lessons_spec = [
        {
            "num": "01",
            "title": "El referéndum de 1978 y la soberanía nacional",
            "goal": "Explicar cómo se aprobó y entró en vigor la Constitución de 1978 y por qué la soberanía nacional reside en el pueblo español.",
            "grammar": "Pasiva refleja con «se»",
            "story_ref": "stories/world/b1/b1-constitucion-01-origenes.json",
            "vocab_ref": "vocabulary/b1/b1-constitucion-01-voc.json",
            "grammar_ref": "grammar/b1/b1-constitucion-01-se-pasiva-constitucional-gr.json",
            "ex_ref": "exercises/b1/b1-constitucion-01-ex.json",
            "goals": [
                "Identify key dates of the 1978 Constitution: December 6 referendum and December 29 entry into force in the BOE.",
                "State that Spain is constituted as a social and democratic State under the rule of law (Article 1.1).",
                "Explain that national sovereignty resides in the Spanish people, from whom all State powers emanate (Article 1.2).",
                "Use impersonal and passive 'se' constructions in constitutional Spanish."
            ]
        },
        {
            "num": "02",
            "title": "La monarquía parlamentaria y la separación de poderes",
            "goal": "Identificar la monarquía parlamentaria como forma política del Estado, el papel del Rey y la división de los tres poderes.",
            "grammar": "corresponder a + infinitivo",
            "story_ref": "stories/world/b1/b1-constitucion-02-monarquia.json",
            "vocab_ref": "vocabulary/b1/b1-constitucion-02-voc.json",
            "grammar_ref": "grammar/b1/b1-constitucion-02-corresponde-a-infinitivo-gr.json",
            "ex_ref": "exercises/b1/b1-constitucion-02-ex.json",
            "goals": [
                "State that the political form of the Spanish State is the parliamentary monarchy (Article 1.3).",
                "Explain the role of the King as Head of State and symbol of unity and permanence.",
                "Distinguish the legislative (Cortes Generales), executive (Government), and judicial (judges and magistrates) branches.",
                "Use 'corresponder a + infinitivo' to attribute constitutional powers."
            ]
        },
        {
            "num": "03",
            "title": "Valores superiores, lenguas oficiales y símbolos",
            "goal": "Reconocer los cuatro valores superiores del ordenamiento jurídico, el régimen constitucional de las lenguas españolas, la bandera y la capital.",
            "grammar": "el deber de vs. el derecho a",
            "story_ref": "stories/world/b1/b1-constitucion-03-valores.json",
            "vocab_ref": "vocabulary/b1/b1-constitucion-03-voc.json",
            "grammar_ref": "grammar/b1/b1-constitucion-03-el-deber-de-y-el-derecho-a-gr.json",
            "ex_ref": "exercises/b1/b1-constitucion-03-ex.json",
            "goals": [
                "Name the four supreme values of Spain's legal order: liberty, justice, equality, and political pluralism.",
                "Explain Article 3: the duty to know Castilian, the right to use it, and the co-official status of Spain's other languages.",
                "Describe the proportions of the Spanish flag (Article 4) and identify Madrid as the capital (Article 5).",
                "Contrast 'el deber de + infinitivo' with 'el derecho a + infinitivo'."
            ]
        },
        {
            "num": "04",
            "title": "Estructura y reforma de la Constitución",
            "goal": "Conocer la estructura de los 169 artículos de la Constitución y las tres reformas constitucionales de 1992, 2011 y 2024.",
            "grammar": "para que + subjuntivo",
            "story_ref": "stories/world/b1/b1-constitucion-04-reforma.json",
            "vocab_ref": "vocabulary/b1/b1-constitucion-04-voc.json",
            "grammar_ref": "grammar/b1/b1-constitucion-04-para-que-subjuntivo-reforma-gr.json",
            "ex_ref": "exercises/b1/b1-constitucion-04-ex.json",
            "goals": [
                "State that the 1978 Constitution consists of a Preamble, a Preliminary Title, 10 Titles, and 169 articles.",
                "Identify Title I as the section regulating fundamental rights and public liberties.",
                "Explain the three constitutional reforms in democratic Spain: 1992 (Maastricht municipal suffrage), 2011 (Article 135), and 2024 (Article 49).",
                "Use 'para que + subjunctive' to explain the purpose of legal reforms."
            ]
        },
        {
            "num": "05",
            "title": "El Estado de las Autonomías y la solidaridad territorial",
            "goal": "Comprender la organización territorial de España en municipios, provincias, 17 comunidades autónomas y 2 ciudades autónomas.",
            "grammar": "Concesivas formales con «si bien»",
            "story_ref": "stories/world/b1/b1-constitucion-05-autonomias.json",
            "vocab_ref": "vocabulary/b1/b1-constitucion-05-voc.json",
            "grammar_ref": "grammar/b1/b1-constitucion-05-si-bien-concesivas-gr.json",
            "ex_ref": "exercises/b1/b1-constitucion-05-ex.json",
            "goals": [
                "Explain how Article 2 combines the unity of the Spanish Nation with the right to autonomy and solidarity among regions.",
                "Describe Spain's territorial organization into municipalities, provinces, 17 Autonomous Communities, and 2 Autonomous Cities (Ceuta and Melilla).",
                "Define the Statute of Autonomy as the basic institutional norm of each Autonomous Community.",
                "Use 'si bien' + indicative to express formal concession."
            ]
        }
    ]

    for spec in lessons_spec:
        num = spec["num"]
        stem = f"b1-constitucion-{num}"
        lesson_data = {
            "id": f"lesson.b1.constitucion.{num}",
            "title": spec["title"],
            "level": "B1",
            "goal": spec["goal"],
            "grammar": spec["grammar"],
            "sections": [
                {
                    "type": "goal",
                    "items": spec["goals"]
                },
                {
                    "type": "recycle",
                    "count": 3
                },
                {
                    "type": "story",
                    "ref": spec["story_ref"]
                },
                {
                    "type": "vocabulary",
                    "ref": spec["vocab_ref"]
                },
                {
                    "type": "grammar",
                    "ref": spec["grammar_ref"]
                },
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": spec["ex_ref"],
                    "exerciseRefs": [
                        f"{stem}.ex01",
                        f"{stem}.ex01b",
                        f"{stem}.ex02",
                        f"{stem}.ex03",
                        f"{stem}.ex04",
                        f"{stem}.ex05",
                        f"{stem}.ex06",
                        f"{stem}.ex07",
                        f"{stem}.ex08"
                    ]
                },
                {
                    "type": "srs"
                },
                {
                    "type": "checklist",
                    "items": [f"I can {g[0].lower() + g[1:]}" for g in spec["goals"]]
                }
            ]
        }
        # The track's first lesson opens with a welcome screen explaining
        # what the Cultura y Ciudadanía track is and how it relates to Core.
        if num == "01":
            lesson_data["sections"].insert(0, {
                "type": "intro",
                "title": "Welcome to Cultura y Ciudadanía",
                "body": [
                    "This is a 36-unit track about Spain itself: how the state works, the rights and duties of the people who live there, its geography and regions, its history, and its culture and everyday life. It follows the topics of the *CCSE*, the test on the constitution and Spanish society that the Instituto Cervantes sets for people applying for Spanish nationality.",
                    "Every lesson is built around a story: a real episode told as a narrative, not a list of facts to memorise. The words you need come from that story, and so does one B1 grammar point, practised on the same topic. Each unit has five lessons, then a consolidation lesson that ties them together.",
                    "This track runs alongside Core Spanish, not instead of it. It doesn't gate your level test, but it assumes you're working through B1 Core grammar at the same time, and every word you learn here goes into the same review deck.",
                    "To be clear about one thing: this track teaches the CCSE topics in Spanish at B1. It isn't an official preparation course. The real exam's questions come from the Instituto Cervantes' own published materials, so study those as well before you sit it.",
                    "Okay, let's start where modern Spain starts: 1978."
                ]
            })
        write_json(f"content/es-es/lessons/b1/{stem}.json", lesson_data)

    consolidation_lesson = {
        "id": "lesson.b1.constitucion.consolidation",
        "title": "Repaso y Simulacro: La Constitución de 1978",
        "level": "B1",
        "goal": "Consolidar los principios, derechos, símbolos, reformas y organización territorial de la Constitución Española de 1978 para el examen CCSE.",
        "grammar": "Consolidación de estructuras constitucionales y jurídicas",
        "sections": [
            {
                "type": "goal",
                "items": [
                    "Consolidate key CCSE exam facts on the approval, sovereignty, and parliamentary monarchy of the 1978 Constitution.",
                    "Review vocabulary for constitutional values, official languages, symbols, and territorial organization.",
                    "Practice impersonal 'se', 'corresponder a', 'el deber de / el derecho a', 'para que + subjunctive', and 'si bien'.",
                    "Synthesize how the 169 articles, 3 reforms, and Statutes of Autonomy structure modern democratic Spain."
                ]
            },
            {
                "type": "recycle",
                "count": 3
            },
            {
                "type": "exercise-group",
                "title": "Review",
                "ref": "exercises/b1/b1-constitucion-consolidation-ex.json",
                "exerciseRefs": [
                    f"b1-constitucion-consolidation.ex{i:02d}" for i in range(1, 19)
                ]
            },
            {
                "type": "checklist",
                "items": [
                    "I can consolidate key CCSE exam facts on the approval, sovereignty, and parliamentary monarchy of the 1978 Constitution.",
                    "I can review vocabulary for constitutional values, official languages, symbols, and territorial organization.",
                    "I can practice impersonal 'se', 'corresponder a', 'el deber de / el derecho a', 'para que + subjunctive', and 'si bien'.",
                    "I can synthesize how the 169 articles, 3 reforms, and Statutes of Autonomy structure modern democratic Spain."
                ]
            }
        ]
    }
    write_json("content/es-es/lessons/b1/b1-constitucion-consolidation.json", consolidation_lesson)

    # -------------------------------------------------------------------------
    # 6. Update curriculum/units/b1.json for Unit 1
    # -------------------------------------------------------------------------
    units_path = ROOT / "content/es-es/curriculum/units/b1.json"
    units_data = json.loads(units_path.read_text(encoding="utf-8"))
    for u in units_data:
        if u.get("track") == "cultura" and "Constitución" in u.get("title", ""):
            u["stems"] = [
                "b1-constitucion-01",
                "b1-constitucion-02",
                "b1-constitucion-03",
                "b1-constitucion-04",
                "b1-constitucion-05",
                "b1-constitucion-consolidation"
            ]
            break
    write_json("content/es-es/curriculum/units/b1.json", units_data)


if __name__ == "__main__":
    build_unit_1()
