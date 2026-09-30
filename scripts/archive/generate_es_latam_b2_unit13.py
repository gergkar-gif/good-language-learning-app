#!/usr/bin/env python3
"""
Generator for Spanish (LatAm) B2 Pair 13:
  - Core Unit 13: Relative Clauses with Unidentified Antecedents (b2-13)
  - Regional Unit 13: Colombia I: The Andean Core, Coffee & Realism (b2-colombiaandina)
"""

import json
from pathlib import Path
from b2_latam_helpers import write_json, make_lesson, make_consolidation_lesson

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "content" / "es-latam"

def count_words(story_data):
    total = 0
    for p in story_data.get("paragraphs", []):
        total += len(p.get("text", "").split())
    return total

def run():
    # -------------------------------------------------------------------------
    # SKILL REGISTRY & GRAMMAR TITLES
    # -------------------------------------------------------------------------
    skill_reg_path = BASE / "indexes" / "skill-registry.json"
    with open(skill_reg_path, "r", encoding="utf-8") as f:
        skill_reg = json.load(f)

    new_skills = {
        "b2-unit13-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "institutional search profiles, candidate specifications, and qualification criteria"
        },
        "relativas-antecedente-inespecifico": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "relative clauses with non-specific or hypothetical antecedents"
        },
        "relativas-antecedente-negativo": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "relative clauses with negative or non-existent antecedents"
        },
        "relativas-modo-indicativo-subjuntivo": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "mood selection in restrictive relative clauses based on specificity"
        },
        "relativas-preposicionales-subjuntivo": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "prepositional relative clauses with subjunctive"
        },
        "relativas-criterios-institucionales": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "institutional selection criteria with generalizing relative clauses"
        },
        "b2-colombiaandina-vocab": {
            "kind": "vocabulary",
            "level": "B2",
            "tier": 2,
            "theme": "colombian geography, paramo ecosystems, bogota urban culture, medellin innovation, and coffee heritage"
        },
        "colombia-cordilleras-paramos": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "colombian paramo ecosystems and mountain geography"
        },
        "colombia-bogota-atenas-debate": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "bogota civic discourse and urban mobility"
        },
        "colombia-medellin-innovacion-social": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "medellin social innovation and urban transformation"
        },
        "colombia-eje-cafetero-patrimonio": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "colombian coffee cultural landscape and traditions"
        },
        "colombia-garcia-marquez-realismo": {
            "kind": "grammar",
            "level": "B2",
            "tier": 2,
            "theme": "garcia marquez and magical realism in context"
        }
    }
    skill_reg["skills"].update(new_skills)
    with open(skill_reg_path, "w", encoding="utf-8") as f:
        json.dump(skill_reg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated skill-registry.json for Unit 13")

    grammar_titles_path = BASE / "indexes" / "grammar-titles.json"
    with open(grammar_titles_path, "r", encoding="utf-8") as f:
        grammar_titles = json.load(f)

    new_titles = {
        "relativas-antecedente-inespecifico": "relative clauses with non-specific antecedents",
        "relativas-antecedente-negativo": "relative clauses with negative antecedents",
        "relativas-modo-indicativo-subjuntivo": "indicative vs subjunctive in relative clauses",
        "relativas-preposicionales-subjuntivo": "prepositional relative clauses with subjunctive",
        "relativas-criterios-institucionales": "institutional criteria and qualifying relative clauses",
        "colombia-cordilleras-paramos": "colombian paramo ecosystems and mountain geography",
        "colombia-bogota-atenas-debate": "bogota civic discourse and urban mobility",
        "colombia-medellin-innovacion-social": "medellin social innovation and urban transformation",
        "colombia-eje-cafetero-patrimonio": "colombian coffee cultural landscape and traditions",
        "colombia-garcia-marquez-realismo": "garcia marquez and magical realism in context"
    }
    grammar_titles.update(new_titles)
    with open(grammar_titles_path, "w", encoding="utf-8") as f:
        json.dump(grammar_titles, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated grammar-titles.json for Unit 13")

    # =========================================================================
    # CORE UNIT 13: RELATIVE CLAUSES WITH UNIDENTIFIED ANTECEDENTS (b2-13)
    # =========================================================================

    # Lesson 1: b2-13-01
    c1 = "b2-13-01"
    write_json(f"vocabulary/b2/{c1}-voc.json", {
        "id": "vocab.b2.13.01",
        "lesson": c1,
        "title": "Búsqueda de perfiles y requisitos profesionales",
        "theme": "Criterios de selección, convocatorias laborales y competencias requeridas",
        "words": [
            {"lemma": "postulante", "translation": "applicant, candidate", "pos": "noun"},
            {"lemma": "requisito", "translation": "requirement, prerequisite", "pos": "noun"},
            {"lemma": "competencia", "translation": "competence, skill", "pos": "noun"},
            {"lemma": "idoneidad", "translation": "suitability, fitness", "pos": "noun"},
            {"lemma": "convocatoria", "translation": "call for applications, open competition", "pos": "noun"},
            {"lemma": "desempeñar", "translation": "to carry out, to discharge", "pos": "verb"},
            {"lemma": "acreditar", "translation": "to certify, to prove credentials", "pos": "verb"},
            {"lemma": "riguroso", "translation": "rigorous, strict", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c1}-a-gr.json", {
        "id": "grammar.b2.13.01.relativas-antecedente-inespecifico",
        "title": "Oraciones relativas con antecedente no específico o hipotético",
        "sections": [
            {
                "type": "text",
                "title": "El subjuntivo en la caracterización de entidades no identificadas",
                "content": "En español B2, cuando el antecedente de una oración de relativo es una entidad indeterminada, desconocida o hipotética cuya existencia real no se presupone en el mundo del emisor, el verbo subordinado adopta obligatoriamente el modo subjuntivo ('Buscamos un investigador que tenga experiencia en bioética', 'Se requiere una plataforma que procese datos en tiempo real')."
            },
            {
                "type": "table",
                "title": "Estructuras de relativo con antecedente inespecífico",
                "rows": [
                    ["Necesitamos un perito...", "...que comprenda la legislación ambiental."],
                    ["Buscan una solución...", "...que minimice el impacto fiscal negativo."],
                    ["Contratarán a alguien...", "...que hable varios idiomas indígenas andinos."],
                    ["Diseñaremos un plan...", "...que articule a los ministerios involucrados."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c1}-ex.json", {
        "lesson": c1,
        "exercises": [
            {
                "id": f"{c1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el postulante", "applicant, candidate"],
                    ["la idoneidad", "suitability, fitness"],
                    ["la convocatoria", "call for applications"],
                    ["desempeñar", "to carry out, to discharge"]
                ],
                "teaches": ["b2-unit13-vocab"]
            },
            {
                "id": f"{c1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La comisión necesita redactar un informe que __ fielmente los hallazgos de campo. (reflejar)",
                "answer": "refleje",
                "english": "The commission needs to draft a report that faithfully reflects the field findings.",
                "teaches": ["relativas-antecedente-inespecifico"]
            },
            {
                "id": f"{c1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué enunciado exige modo subjuntivo por tener un antecedente inespecífico o hipotético?",
                "options": [
                    "Buscamos a un consultor que conozca la normativa aduanera andina.",
                    "Contratamos al consultor que conoce la normativa aduanera andina.",
                    "Trabajamos con el equipo que gestiona los fondos públicos descentralizados."
                ],
                "correct": 0,
                "teaches": ["relativas-antecedente-inespecifico"]
            },
            {
                "id": f"{c1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Requerimos", "un", "auditor", "que", "acredite", "experiencia", "en", "proyectos", "multilaterales."],
                "solution": ["Requerimos", "un", "auditor", "que", "acredite", "experiencia", "en", "proyectos", "multilaterales."],
                "english": "We require an auditor who certifies experience in multilateral projects.",
                "teaches": ["relativas-antecedente-inespecifico"]
            },
            {
                "id": f"{c1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Directora de RRHH", "text": "Debemos publicar la vacante antes del viernes. ¿Qué perfil propones para liderar el proyecto andino?"},
                    {"speaker": "Coordinador", "text": "_____"},
                    {"speaker": "Directora de RRHH", "text": "Me parece un criterio impecable; redactemos la convocatoria con ese requisito."}
                ],
                "options": [
                    "Sugiero que busquemos a alguien que tenga solvencia técnica y haya coordinado equipos interculturales.",
                    "El archivo central abre de lunes a viernes a las nueve de la mañana.",
                    "Los pasajes aéreos a Bogotá fueron adquiridos el mes pasado."
                ],
                "correct": 0,
                "teaches": ["relativas-antecedente-inespecifico"]
            },
            {
                "id": f"{c1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Es indispensable seleccionar un postulante que demuestre probada idoneidad moral.",
                "english": "It is essential to select an applicant who demonstrates proven moral suitability.",
                "teaches": ["relativas-antecedente-inespecifico"]
            }
        ]
    })

    write_json(f"lessons/b2/{c1}.json", make_lesson(
        stem=c1,
        unit_num=13,
        title="Búsqueda de perfiles y antecedentes inespecíficos",
        goal="Master the use of the subjunctive in relative clauses describing non-specific or hypothetical entities.",
        grammar_desc="oraciones de relativo con antecedente inespecífico o hipotético en subjuntivo",
        grammar_ref=f"grammar/b2/{c1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c1}-voc.json",
        ex_ref=f"exercises/b2/{c1}-ex.json",
        ex_ids=[f"{c1}.ex01", f"{c1}.ex02", f"{c1}.ex03", f"{c1}.ex04", f"{c1}.ex05", f"{c1}.ex06"],
        goals=[
            "Identify when an antecedent lacks real-world specificity.",
            "Formulate professional requirements and job profiles using the subjunctive.",
            "Distinguish between hypothetical candidates and known individuals."
        ]
    ))

    # Lesson 2: b2-13-02
    c2 = "b2-13-02"
    write_json(f"vocabulary/b2/{c2}-voc.json", {
        "id": "vocab.b2.13.02",
        "lesson": c2,
        "title": "Verificación empírica y ausencia de antecedentes",
        "theme": "Léxico de auditoría, refutación categórica y comprobación fáctica",
        "words": [
            {"lemma": "inexistencia", "translation": "non-existence", "pos": "noun"},
            {"lemma": "hallazgo", "translation": "finding, discovery", "pos": "noun"},
            {"lemma": "indicio", "translation": "indication, clue, evidence", "pos": "noun"},
            {"lemma": "vacío", "translation": "void, gap, loophole", "pos": "noun"},
            {"lemma": "corroborar", "translation": "to corroborate, to confirm", "pos": "verb"},
            {"lemma": "desmentir", "translation": "to deny, to refute", "pos": "verb"},
            {"lemma": "infundado", "translation": "unfounded, baseless", "pos": "adjective"},
            {"lemma": "categórico", "translation": "categorical, unequivocal", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c2}-a-gr.json", {
        "id": "grammar.b2.13.02.relativas-antecedente-negativo",
        "title": "Oraciones relativas con antecedente negativo o inexistente",
        "sections": [
            {
                "type": "text",
                "title": "Subjuntivo ante la negación explícita de la existencia",
                "content": "Cuando la cláusula principal niega la existencia del antecedente mediante cuantificadores negativos ('nadie', 'nada', 'ninguno/a', 'ningún lugar', 'en modo alguno'), la cláusula adjetiva subordinada exige invariablemente el modo subjuntivo ('No hay nadie que pueda impugnar el resultado', 'No encontramos ningún documento que avale esa pretensión')."
            },
            {
                "type": "table",
                "title": "Antecedentes negativos y subordinadas en subjuntivo",
                "rows": [
                    ["No hay nadie...", "...que conozca los pormenores del contrato."],
                    ["No existe ningún indicio...", "...que justifique una investigación penal."],
                    ["No encontramos nada...", "...que contradiga el testimonio oficial."],
                    ["No queda lugar alguno...", "...adonde podamos recurrir en apelación."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c2}-ex.json", {
        "lesson": c2,
        "exercises": [
            {
                "id": f"{c2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el hallazgo", "finding, discovery"],
                    ["el indicio", "indication, clue, evidence"],
                    ["corroborar", "to corroborate, to confirm"],
                    ["categórico", "categorical, unequivocal"]
                ],
                "teaches": ["b2-unit13-vocab"]
            },
            {
                "id": f"{c2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En los archivos no queda ningún registro que __ la entrega de los fondos. (acreditar)",
                "answer": "acredite",
                "english": "In the archives there remains no record that certifies the delivery of the funds.",
                "teaches": ["relativas-antecedente-negativo"]
            },
            {
                "id": f"{c2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué opción contiene una oración subordinada adjetiva con antecedente negativo correcto?",
                "options": [
                    "No encontramos ningún peritaje que respalde la tesis de la defensa.",
                    "No encontramos ningún peritaje que respalda la tesis de la defensa.",
                    "No existe prueba alguna que demuestra su culpabilidad penal."
                ],
                "correct": 0,
                "teaches": ["relativas-antecedente-negativo"]
            },
            {
                "id": f"{c2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "hay", "ninguna", "cláusula", "que", "invalide", "los", "acuerdos", "firmados."],
                "solution": ["No", "hay", "ninguna", "cláusula", "que", "invalide", "los", "acuerdos", "firmados."],
                "english": "There is no clause that invalidates the signed agreements.",
                "teaches": ["relativas-antecedente-negativo"]
            },
            {
                "id": f"{c2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Ha descubierto la fiscalía algún testimonio comprometedor contra la junta?"},
                    {"speaker": "Portavoz judicial", "text": "_____"},
                    {"speaker": "Periodista", "text": "Queda clara entonces la postura oficial respecto a la investigación."}
                ],
                "options": [
                    "Hasta el momento no disponemos de ningún indicio testimonial que vincule a los miembros de la junta.",
                    "El tribunal supremo sesiona en el palacio de justicia cada martes por la tarde.",
                    "Los diarios nacionales publicaron reportajes sobre el comercio fluvial."
                ],
                "correct": 0,
                "teaches": ["relativas-antecedente-negativo"]
            },
            {
                "id": f"{c2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "No existe ningún argumento fáctico que desmienta los hallazgos de la auditoría.",
                "english": "There is no factual argument that refutes the audit's findings.",
                "teaches": ["relativas-antecedente-negativo"]
            }
        ]
    })

    write_json(f"lessons/b2/{c2}.json", make_lesson(
        stem=c2,
        unit_num=13,
        title="Antecedentes negativos e inexistencia categórica",
        goal="Express non-existence, absence, and refutation using negative antecedents with subjunctive relative clauses.",
        grammar_desc="oraciones de relativo con antecedentes negativos (nadie, nada, ninguno) y modo subjuntivo",
        grammar_ref=f"grammar/b2/{c2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c2}-voc.json",
        ex_ref=f"exercises/b2/{c2}-ex.json",
        ex_ids=[f"{c2}.ex01", f"{c2}.ex02", f"{c2}.ex03", f"{c2}.ex04", f"{c2}.ex05", f"{c2}.ex06"],
        goals=[
            "Construct relative sentences with 'nadie', 'nada', and 'ninguno'.",
            "Articulate rigorous refutations and audit statements in professional contexts.",
            "Distinguish affirmative specificity from negative non-existence."
        ]
    ))

    # Lesson 3: b2-13-03
    c3 = "b2-13-03"
    write_json(f"vocabulary/b2/{c3}-voc.json", {
        "id": "vocab.b2.13.03",
        "lesson": c3,
        "title": "Identificación de fuentes y entidades concretas",
        "theme": "Léxico de peritaje, contrastación epistémica y certidumbre factual",
        "words": [
            {"lemma": "fuente", "translation": "source, informant", "pos": "noun"},
            {"lemma": "entidad", "translation": "entity, agency", "pos": "noun"},
            {"lemma": "testigo", "translation": "witness", "pos": "noun"},
            {"lemma": "certeza", "translation": "certainty, certitude", "pos": "noun"},
            {"lemma": "constatar", "translation": "to verify, to ascertain", "pos": "verb"},
            {"lemma": "individualizar", "translation": "to single out, to individualize", "pos": "verb"},
            {"lemma": "fidedigno", "translation": "reliable, trustworthy", "pos": "adjective"},
            {"lemma": "concreto", "translation": "concrete, specific", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c3}-a-gr.json", {
        "id": "grammar.b2.13.03.relativas-modo-indicativo-subjuntivo",
        "title": "Contraste de modo en relativas: Indicativo (específico) vs Subjuntivo (inespecífico)",
        "sections": [
            {
                "type": "text",
                "title": "La alternancia modal como marcador de identificación epistémica",
                "content": "La elección entre indicativo y subjuntivo en oraciones adjetivas no depende meramente del verbo principal, sino de si el hablante tiene en mente un referente concreto e individualizado en el mundo real (indicativo) o si busca, postula o desconoce al individuo que cumple esas propiedades (subjuntivo)."
            },
            {
                "type": "table",
                "title": "Contraste modal según la especificidad del referente",
                "rows": [
                    ["Conozco a un perito que habla quechua.", "Referente concreto y verificado (indicativo)"],
                    ["Busco a un perito que hable quechua.", "Perfil abstracto o desconocido (subjuntivo)"],
                    ["Tengo un informe que explica el déficit.", "Documento en mano ya existente (indicativo)"],
                    ["Necesito un informe que explique el déficit.", "Requerimiento hipotético formulado (subjuntivo)"]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c3}-ex.json", {
        "lesson": c3,
        "exercises": [
            {
                "id": f"{c3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la certeza", "certainty, certitude"],
                    ["el testigo", "witness"],
                    ["constatar", "to verify, to ascertain"],
                    ["fidedigno", "reliable, trustworthy"]
                ],
                "teaches": ["b2-unit13-vocab"]
            },
            {
                "id": f"{c3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Aquí tengo en mis manos el expediente que __ la procedencia legal de las tierras. (demostrar)",
                "answer": "demuestra",
                "english": "Here in my hands I have the dossier that demonstrates the legal provenance of the lands.",
                "teaches": ["relativas-modo-indicativo-subjuntivo"]
            },
            {
                "id": f"{c3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál enunciado afirma con certeza la existencia real de un individuo específico?",
                "options": [
                    "Trabajo con una analista que domina las finanzas públicas andinas.",
                    "Busco a una analista que domine las finanzas públicas andinas.",
                    "Ojalá tengamos una analista que domine las finanzas públicas andinas."
                ],
                "correct": 0,
                "teaches": ["relativas-modo-indicativo-subjuntivo"]
            },
            {
                "id": f"{c3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Contamos", "con", "un", "protocolo", "que", "garantiza", "la", "cadena", "de", "custodia."],
                "solution": ["Contamos", "con", "un", "protocolo", "que", "garantiza", "la", "cadena", "de", "custodia."],
                "english": "We count on a protocol that guarantees the chain of custody.",
                "teaches": ["relativas-modo-indicativo-subjuntivo"]
            },
            {
                "id": f"{c3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministro", "text": "¿Ya se eligió el consorcio para la infraestructura vial?"},
                    {"speaker": "Viceministro", "text": "_____"},
                    {"speaker": "Ministro", "text": "De acuerdo; no adjudicaremos la obra hasta tener garantías plenas."}
                ],
                "options": [
                    "Estamos esperando una propuesta que cumpla con las exigencias, ya que la actual no satisface los estándares.",
                    "La carretera pavimentada conecta la capital con los puertos fluviales del norte.",
                    "Los camiones de carga circulan principalmente durante el horario nocturno."
                ],
                "correct": 0,
                "teaches": ["relativas-modo-indicativo-subjuntivo"]
            },
            {
                "id": f"{c3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Conozco personalmente al perito que redactó las conclusiones del caso.",
                "english": "I personally know the expert who drafted the conclusions of the case.",
                "teaches": ["relativas-modo-indicativo-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{c3}.json", make_lesson(
        stem=c3,
        unit_num=13,
        title="Alternancia modal: Lo concreto frente a lo hipotético",
        goal="Master the nuanced contrast between indicative (specific real entities) and subjunctive (hypothetical, searched entities) in relative clauses.",
        grammar_desc="contraste de modo indicativo y subjuntivo en oraciones de relativo según la especificidad del antecedente",
        grammar_ref=f"grammar/b2/{c3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c3}-voc.json",
        ex_ref=f"exercises/b2/{c3}-ex.json",
        ex_ids=[f"{c3}.ex01", f"{c3}.ex02", f"{c3}.ex03", f"{c3}.ex04", f"{c3}.ex05", f"{c3}.ex06"],
        goals=[
            "Distinguish between specific concrete entities and idealized search criteria.",
            "Use indicative to assert verified facts and subjunctive to formulate expectations.",
            "Navigate nuanced register shifts in legal and journalistic prose."
        ]
    ))

    # Lesson 4: b2-13-04
    c4 = "b2-13-04"
    write_json(f"vocabulary/b2/{c4}-voc.json", {
        "id": "vocab.b2.13.04",
        "lesson": c4,
        "title": "Instrumentos normativos y canales de interlocución",
        "theme": "Mecanismos institucionales, vías de mediación y recursos legales",
        "words": [
            {"lemma": "interlocutor", "translation": "interlocutor, dialogue partner", "pos": "noun"},
            {"lemma": "mecanismo", "translation": "mechanism, framework", "pos": "noun"},
            {"lemma": "vía", "translation": "avenue, channel, pathway", "pos": "noun"},
            {"lemma": "instancia", "translation": "authority, body, forum", "pos": "noun"},
            {"lemma": "recurrir", "translation": "to resort to, to appeal", "pos": "verb"},
            {"lemma": "canalizar", "translation": "to channel, to streamline", "pos": "verb"},
            {"lemma": "vinculante", "translation": "binding, enforceable", "pos": "adjective"},
            {"lemma": "viable", "translation": "viable, workable", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c4}-a-gr.json", {
        "id": "grammar.b2.13.04.relativas-preposicionales-subjuntivo",
        "title": "Oraciones relativas con preposición y modo subjuntivo",
        "sections": [
            {
                "type": "text",
                "title": "Sintaxis de relativos preposicionales con antecedentes hipotéticos",
                "content": "Las oraciones relativas precedidas de preposición ('a quien', 'con el cual', 'en la que', 'por el que') también seleccionan subjuntivo cuando su antecedente es inespecífico, negativo o prospectivo. Estas estructuras son fundamentales en el discurso institucional y diplomático para definir canales, mediadores o condiciones operativas ideales."
            },
            {
                "type": "table",
                "title": "Estructuras relativas con preposición",
                "rows": [
                    ["con quien / con el que", "Buscamos un líder con quien se pueda pactar la tregua."],
                    ["mediante el cual / por el cual", "Urge un mecanismo por el cual se diriman disputas."],
                    ["a quien / a los que", "No encontramos a nadie a quien confiarle el archivo."],
                    ["en donde / en el que", "Diseñarán un espacio en el que converjan ambas partes."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c4}-ex.json", {
        "lesson": c4,
        "exercises": [
            {
                "id": f"{c4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el interlocutor", "dialogue partner"],
                    ["el mecanismo", "framework, mechanism"],
                    ["canalizar", "to channel, to streamline"],
                    ["vinculante", "binding, enforceable"]
                ],
                "teaches": ["b2-unit13-vocab"]
            },
            {
                "id": f"{c4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Se requiere un marco legal mediante el cual se __ los derechos territoriales comunitarios. (proteger)",
                "answer": "protejan",
                "english": "A legal framework is required through which community territorial rights are protected.",
                "teaches": ["relativas-preposicionales-subjuntivo"]
            },
            {
                "id": f"{c4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la formulación más adecuada en un marco de mediación pacífica?",
                "options": [
                    "Necesitamos una mesa de diálogo en la que participen todos los sectores afectados.",
                    "Necesitamos una mesa de diálogo en la que participan todos los sectores afectados.",
                    "No hay ningún canal formal por el cual se tramita la apelación."
                ],
                "correct": 0,
                "teaches": ["relativas-preposicionales-subjuntivo"]
            },
            {
                "id": f"{c4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["No", "hallamos", "a", "nadie", "con", "quien", "pudiéramos", "establecer", "comunicación", "segura."],
                "solution": ["No", "hallamos", "a", "nadie", "con", "quien", "pudiéramos", "establecer", "comunicación", "segura."],
                "english": "We found no one with whom we could establish secure communication.",
                "teaches": ["relativas-preposicionales-subjuntivo"]
            },
            {
                "id": f"{c4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Comisionado", "text": "Las partes reclaman garantías de cumplimiento. ¿Cómo resolvemos esa desconfianza?"},
                    {"speaker": "Asesora jurídica", "text": "_____"},
                    {"speaker": "Comisionado", "text": "Excelente iniciativa; dotará de legitimidad internacional al proceso."}
                ],
                "options": [
                    "Propondré la creación de una veeduría internacional a la que ambas delegaciones rindan cuentas periódicas.",
                    "Las actas de la reunión anterior fueron archivadas en el servidor digital.",
                    "El café colombiano se exporta principalmente a través de puertos caribeños."
                ],
                "correct": 0,
                "teaches": ["relativas-preposicionales-subjuntivo"]
            },
            {
                "id": f"{c4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Debemos convenir un protocolo bajo el cual se canalicen las reclamaciones urgentes.",
                "english": "We must agree upon a protocol under which urgent claims are channeled.",
                "teaches": ["relativas-preposicionales-subjuntivo"]
            }
        ]
    })

    write_json(f"lessons/b2/{c4}.json", make_lesson(
        stem=c4,
        unit_num=13,
        title="Relativas preposicionales y canales institucionales",
        goal="Construct complex prepositional relative clauses with subjunctive to establish prospective procedures and institutional channels.",
        grammar_desc="relativas preposicionales complejas (con quien, mediante el cual, en el que) con subjuntivo",
        grammar_ref=f"grammar/b2/{c4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c4}-voc.json",
        ex_ref=f"exercises/b2/{c4}-ex.json",
        ex_ids=[f"{c4}.ex01", f"{c4}.ex02", f"{c4}.ex03", f"{c4}.ex04", f"{c4}.ex05", f"{c4}.ex06"],
        goals=[
            "Deploy prepositions with relative pronouns ('mediante el cual', 'con quien', 'en el que').",
            "Specify non-existent or idealized mechanisms in institutional debate.",
            "Enhance syntactical variety and formal cohesion."
        ]
    ))

    # Lesson 5: b2-13-05
    c5 = "b2-13-05"
    write_json(f"vocabulary/b2/{c5}-voc.json", {
        "id": "vocab.b2.13.05",
        "lesson": c5,
        "title": "Criterios institucionales y cláusulas estatutarias",
        "theme": "Léxico de estatutos, convocatorias públicas y pliegos de condiciones",
        "words": [
            {"lemma": "postulación", "translation": "application, candidacy", "pos": "noun"},
            {"lemma": "pliego", "translation": "specifications sheet, tender conditions", "pos": "noun"},
            {"lemma": "estatuto", "translation": "statute, by-law", "pos": "noun"},
            {"lemma": "baremo", "translation": "scoring scale, grading scale", "pos": "noun"},
            {"lemma": "incurrir", "translation": "to incur, to fall into", "pos": "verb"},
            {"lemma": "subsanar", "translation": "to rectify, to remedy", "pos": "verb"},
            {"lemma": "taxativo", "translation": "exhaustive, imperative, non-negotiable", "pos": "adjective"},
            {"lemma": "excluyente", "translation": "exclusive, disqualifying", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{c5}-a-gr.json", {
        "id": "grammar.b2.13.05.relativas-criterios-institucionales",
        "title": "Relativas generalizadoras y criterios de idoneidad institucional",
        "sections": [
            {
                "type": "text",
                "title": "El subjuntivo en pliegos, estatutos y normas generales",
                "content": "En textos normativos, convocatorias públicas y códigos deontológicos, las oraciones relativas encabezadas por cuantificadores distributivos o universales ('todo aquel que', 'cualquier persona que', 'quienesquiera que', 'aquel postulante que') emplean sistemáticamente el subjuntivo para establecer una norma abstracta aplicable a cualquier sujeto futuro que reúna tales condiciones."
            },
            {
                "type": "table",
                "title": "Cláusulas generalizadoras en textos estatutarios",
                "rows": [
                    ["Cualquier aspirante que...", "...que falsee sus datos será descalificado."],
                    ["Todo aquel que...", "...que aspire a la vocalía debe carecer de sanciones."],
                    ["Quienquiera que...", "...que asuma la dirección deberá rendir fianza."],
                    ["Aquellas empresas que...", "...que no acrediten solvencia quedarán excluidas."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{c5}-ex.json", {
        "lesson": c5,
        "exercises": [
            {
                "id": f"{c5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el pliego", "tender conditions, specifications"],
                    ["el estatuto", "by-law, statute"],
                    ["subsanar", "to rectify, to remedy"],
                    ["taxativo", "exhaustive, non-negotiable"]
                ],
                "teaches": ["b2-unit13-vocab"]
            },
            {
                "id": f"{c5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Todo postulante que no __ los errores formales dentro del plazo perderá el derecho a examen. (subsanar)",
                "answer": "subsane",
                "english": "Any applicant who does not remedy formal errors within the deadline will forfeit the right to be examined.",
                "teaches": ["relativas-criterios-institucionales"]
            },
            {
                "id": f"{c5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la redacción estatutaria correcta con relativo generalizador?",
                "options": [
                    "Cualquier miembro de la junta que incurra en conflicto de intereses deberá abstenerse de votar.",
                    "Cualquier miembro de la junta que incurre en conflicto de intereses debe abstenerse de votar.",
                    "Todo aquel que postula a la licitación presentó su propuesta ayer por la tarde."
                ],
                "correct": 0,
                "teaches": ["relativas-criterios-institucionales"]
            },
            {
                "id": f"{c5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Serán", "admitidos", "aquellos", "candidatos", "que", "hayan", "completado", "el", "registro."],
                "solution": ["Serán", "admitidos", "aquellos", "candidatos", "que", "hayan", "completado", "el", "registro."],
                "english": "Those candidates who have completed the registration will be admitted.",
                "teaches": ["relativas-criterios-institucionales"]
            },
            {
                "id": f"{c5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Vocal técnico", "text": "Tenemos postulaciones incompletas. ¿Cómo definimos el criterio en el acta?"},
                    {"speaker": "Secretario general", "text": "_____"},
                    {"speaker": "Vocal técnico", "text": "Correcto; así garantizamos la igualdad de condiciones entre oferentes."}
                ],
                "options": [
                    "El texto del acta debe consignar que todo aquel que no presente las certificaciones originales será descalificado.",
                    "La sala de reuniones dispone de proyectores multimedia y conexión inalámbrica.",
                    "El informe anual de gestión financiera se imprimirá en papel reciclado."
                ],
                "correct": 0,
                "teaches": ["relativas-criterios-institucionales"]
            },
            {
                "id": f"{c5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Quedarán automáticamente excluidos aquellos oferentes que incumplan los requerimientos técnicos mínimos.",
                "english": "Those bidders who fail to meet the minimum technical requirements will be automatically excluded.",
                "teaches": ["relativas-criterios-institucionales"]
            }
        ]
    })

    write_json(f"lessons/b2/{c5}.json", make_lesson(
        stem=c5,
        unit_num=13,
        title="Criterios institucionales y cláusulas generalizadoras",
        goal="Apply the subjunctive in generalizing relative clauses ('cualquiera que', 'todo aquel que') within institutional statutes and regulatory texts.",
        grammar_desc="relativas generalizadoras y distributivas en textos normativos con modo subjuntivo",
        grammar_ref=f"grammar/b2/{c5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{c5}-voc.json",
        ex_ref=f"exercises/b2/{c5}-ex.json",
        ex_ids=[f"{c5}.ex01", f"{c5}.ex02", f"{c5}.ex03", f"{c5}.ex04", f"{c5}.ex05", f"{c5}.ex06"],
        goals=[
            "Draft statutory rules and tender requirements with precision.",
            "Master distributive antecedents ('todo aquel que', 'cualquier persona que').",
            "Synthesize formal rights, obligations, and disqualification criteria."
        ]
    ))

    # Consolidation Unit 13 (Core): b2-13-consolidation
    c_con = "b2-13-consolidation"
    write_json(f"exercises/b2/{c_con}-ex.json", {
        "lesson": c_con,
        "exercises": [
            {
                "id": f"{c_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la idoneidad", "fitness, suitability"],
                    ["el pliego", "tender conditions, specifications"],
                    ["constatar", "to verify, to ascertain"],
                    ["taxativo", "exhaustive, non-negotiable"]
                ],
                "teaches": ["b2-unit13-vocab"]
            },
            {
                "id": f"{c_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el enunciado 'Buscamos una solución que satisfaga a ambas partes' requiere subjuntivo?",
                "options": [
                    "Porque el antecedente 'una solución' es inespecífico y su existencia real aún no está verificada.",
                    "Porque el verbo 'buscar' exige siempre infinitivo con cambio de sujeto.",
                    "Porque se trata de una narración de hechos históricos ya consumados en el pasado."
                ],
                "correct": 0,
                "teaches": ["relativas-antecedente-inespecifico"]
            },
            {
                "id": f"{c_con}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "No hubo en el expediente ningún testimonio que __ las denuncias de corrupción. (avalar)",
                "answer": "avalara",
                "english": "There was no testimony in the case file that supported the corruption allegations.",
                "teaches": ["relativas-antecedente-negativo"]
            },
            {
                "id": f"{c_con}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Cualquiera", "que", "vulnerase", "el", "orden", "constitucional", "sería", "llevado", "a", "juicio."],
                "solution": ["Cualquiera", "que", "vulnerase", "el", "orden", "constitucional", "sería", "llevado", "a", "juicio."],
                "english": "Anyone who violated the constitutional order would be brought to trial.",
                "teaches": ["relativas-criterios-institucionales"]
            },
            {
                "id": f"{c_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la diferencia entre 'Tengo un perito que conoce el caso' y 'Busco un perito que conozca el caso'?",
                "options": [
                    "La primera señala a un individuo específico real (indicativo); la segunda postula un perfil buscado (subjuntivo).",
                    "Ambas frases son intercambiables y expresan exactamente la misma certidumbre empírica.",
                    "La segunda frase es un error gramatical que debe corregirse con tiempo condicional."
                ],
                "correct": 0,
                "teaches": ["relativas-modo-indicativo-subjuntivo"]
            },
            {
                "id": f"{c_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Presidente del tribunal", "text": "¿Qué dictamen procede con los aspirantes que no acreditaron el título de posgrado?"},
                    {"speaker": "Secretaria técnica", "text": "_____"},
                    {"speaker": "Presidente del tribunal", "text": "Se aplicará entonces la exclusión sin excepciones."}
                ],
                "options": [
                    "Conforme al reglamento, todo aquel que no acredite la titulación requerida queda excluido del concurso de méritos.",
                    "El salón de audiencias fue remodelado con maderas nobles de la cordillera.",
                    "Los magistrados almuerzan puntualmente a la una de la tarde."
                ],
                "correct": 0,
                "teaches": ["relativas-criterios-institucionales"]
            },
            {
                "id": f"{c_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "No admitiremos ninguna propuesta que comprometa la soberanía ecológica de los páramos.",
                "english": "We will not admit any proposal that compromises the ecological sovereignty of the paramos.",
                "teaches": ["relativas-antecedente-negativo"]
            },
            {
                "id": f"{c_con}.ex08",
                "type": "sentence-builder",
                "category": "writing",
                "tiles": ["Conviene", "establecer", "un", "medio", "por", "el", "cual", "se", "atiendan", "las", "víctimas."],
                "solution": ["Conviene", "establecer", "un", "medio", "por", "el", "cual", "se", "atiendan", "las", "víctimas."],
                "english": "It is advisable to establish a means through which the victims are attended to.",
                "teaches": ["relativas-preposicionales-subjuntivo"]
            }
        ]
    })

    # Classic Story for Unit 13: Gabriel García Márquez - Cien años de soledad
    story_core_13 = {
        "id": "b2-13",
        "title": "Gabriel García Márquez: Cien años de soledad",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de nivel B2 de Cien años de soledad de Gabriel García Márquez: la mítica fundación de Macondo por José Arcadio Buendía y Úrsula Iguarán, la llegada periódica de los gitanos con los inventos de Melquíades y la búsqueda incesante de un horizonte que desentrañara los enigmas del cosmos y la soledad humana.",
        "characters": [
            "José Arcadio Buendía",
            "Úrsula Iguarán",
            "Melquíades",
            "Aureliano Buendía"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella remota tarde en que su padre lo llevó a conocer el hielo. Macondo era entonces una aldea de veinte casas de barro y cañabrava, construidas a la orilla de un río de aguas diáfanas que se precipitaban por un lecho de piedras pulidas, blancas y enormes como huevos prehistóricos. El mundo era tan reciente que muchas cosas carecían de nombre, y para mencionarlas había que señalarlas con el dedo. En aquella planicie aislada por pantanos impenetrables y serranías abruptas, el patriarca José Arcadio Buendía soñaba con fundar una civilización ilustrada que no dependiera de los errores del pasado y en la que ningún habitante fuera despojado de su dignidad ni de su sosiego terrenal."
            },
            {
                "type": "narration",
                "text": "Todos los años, por el mes de marzo, una familia de gitanos desarrapados plantaba su carpa cerca de la aldea, y con un gran alboroto de pitos y timbales daba a conocer los nuevos inventos. Primero llevaron el imán. Un gitano corpulento, de barba montaraz y manos de gorrión, que se presentó con el nombre de Melquíades, hizo una truculenta demostración pública de lo que él mismo llamaba la octava maravilla de los alquimistas de Macedonia. Fue de casa en casa arrastrando dos lingotes metálicos, y todo el mundo se espantó al ver que los calderos, las pailas, las tenazas y los anafes se caían de su sitio, y las maderas crujían por la desesperación de los clavos y los tornillos que pugnaban por desenclavarse. José Arcadio Buendía, cuya desaforada imaginación iba siempre más lejos que el ingenio de la naturaleza, creyó que era posible servirse de aquella invención para desentrañar el oro de la tierra profunda."
            },
            {
                "type": "narration",
                "text": "Úrsula Iguarán, su juiciosa y tenaz consorte, no pudo evitar que su marido trocara los ahorros familiares por aquellos hierros imantados que solo sirvieron para desenterrar una armadura del siglo quince con los huesos de un guerrero español en su interior. Poco después, los gitanos volvieron con un catalejo y una lupa gigantesca, divulgando que los sabios de Ámsterdam habían concebido un artefacto mediante el cual se pudiera concentrar el poder solar como arma bélica. Fascinado por las posibilidades científicas de la óptica, José Arcadio Buendía se encerró durante meses en un rincón sombrío del patio, experimentando con rayos solares sobre su propio cuerpo y sobre pieles secas de ganado, convencido de que hallaría una fórmula matemática que transformara a Macondo en el epicentro de la sabiduría universal."
            },
            {
                "type": "narration",
                "text": "Cuando los gitanos trajeron finalmente el bloque de hielo, guardado en un cofre de madera forrado de paja en medio del calor tórrido de la ciénaga, José Arcadio Buendía pagó cinco reales para que sus hijos palparan aquel prodigio transparente. Al apoyar la palma sobre la superficie helada, declaró con el corazón henchido de júbilo que aquel era el diamante más grande de la tierra. Aquella curiosidad desmedida, no obstante, derivó con los años en una obsesión solitaria. Buscó con desesperación una ruta marítima que comunicara a la aldea con el resto del mundo civilizado, convencido de que la península de la Guajira o el mar Caribe debían encontrarse a pocas jornadas de marcha. Guiando a un puñado de hombres decididos a través de ciénagas humeantes y bosques tupidos donde no penetraba la luz del cielo, solo halló, encallado entre orquídeas y enredaderas a doce kilómetros de la costa, el esqueleto carcomido de un galeón español coronado de laureles."
            },
            {
                "type": "narration",
                "text": "Aquel hallazgo del galeón extraviado en la maleza confirmó ante sus ojos la dimensión circular y fantástica de su destino. Melquíades regresó años más tarde envejecido y sabio, portando pergaminos cifrados en sánscrito que predecían la historia entera de la estirpe Buendía con cien años de antelación. En aquel laboratorio atestado de probetas, alambiques y mercurio hirviente, José Arcadio Buendía comenzó a perder los límites entre la vigilia y la quimera. Conversaba largamente con el fantasma de Prudencio Aguilar, el rival a quien había atravesado la garganta con una lanza en su juventud remota y cuya sombra errante buscaba consuelo en la casa familiar lavándose las heridas con agua de albahaca."
            },
            {
                "type": "narration",
                "text": "La lucidez del patriarca se quebró de manera definitiva una madrugada de marzo en que descubrió que el tiempo no avanzaba en línea recta, sino que daba vueltas en redondo sobre sí mismo. Atado por su familia al tronco de un corpulento castaño en el patio central para evitar que destrozara los enseres domésticos, José Arcadio Buendía permaneció durante años en un diálogo silencioso con las lluvias y los pájaros, balbuceando frases en un latín impecable que nadie comprendía. Su tragedia condensó la parábola de toda una estirpe condenada a cien años de soledad: una familia titánica que buscó incansablemente el saber y la justicia en un territorio mágico donde la realidad más cruda y el ensueño más prodigioso caminaban entrelazados."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué fascinaban a José Arcadio Buendía los inventos que traían los gitanos de Melquíades a Macondo?",
                        "options": [
                            "Porque creía que a través de ellos encontraría claves científicas y riquezas para situar a Macondo en el centro del conocimiento universal.",
                            "Porque deseaba comercializarlos en las ciudades costeras del Caribe para enriquecerse rápidamente.",
                            "Porque pretendía organizar un ejército regular para conquistar las tierras del interior andino.",
                            "Porque era incapaz de trabajar en la agricultura y prefería entretener a los niños del pueblo."
                        ],
                        "correctIndex": 0,
                        "explanation": "El texto resalta la desaforada imaginación de José Arcadio Buendía y su afán por emplear los inventos para descubrir riquezas y conectar a Macondo con la ciencia y la sabiduría universal."
                    },
                    {
                        "question": "¿Qué descubrieron José Arcadio Buendía y sus acompañantes durante la expedición en busca de una salida al mar?",
                        "options": [
                            "El esqueleto carcomido de un antiguo galeón español encallado en medio de la densa selva.",
                            "Un puerto mercantil próspero habitado por comerciantes extranjeros.",
                            "Una mina inagotable de oro y diamantes custodiada por tribus originarias.",
                            "El campamento abandonado de los alquimistas holandeses."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 describe que tras cruzar selvas tupidas hallaron, a doce kilómetros de la costa entre orquídeas y maleza, el esqueleto carcomido de un galeón español."
                    },
                    {
                        "question": "¿Cuál es el sentido simbólico del destino final de José Arcadio Buendía atado al castaño?",
                        "options": [
                            "Refleja la caída en la obsesión solitaria y la concepción circular del tiempo que marcaría a toda la estirpe de Macondo.",
                            "Demuestra que los habitantes del pueblo se rebelaron contra su autoridad fundacional.",
                            "Evidencia que fue castigado por las autoridades coloniales debido a sus experimentos de alquimia.",
                            "Indica que decidió voluntariamente convertirse en monje eremita."
                        ],
                        "correctIndex": 0,
                        "explanation": "El último párrafo ilustra cómo su locura, el descubrimiento de que el tiempo gira en redondo y su encierro bajo el castaño simbolizan la soledad trágica y circular de la familia Buendía."
                    }
                ]
            }
        }
    }
    write_json(f"stories/classics/b2/{c_con.replace('-consolidation', '')}.json", story_core_13)

    write_json(f"lessons/b2/{c_con}.json", make_consolidation_lesson(
        stem=c_con,
        unit_num=13,
        title="Consolidación: Criterios, perfiles y la búsqueda de horizontes",
        goal="Consolidate upper-intermediate mastery of relative clauses with unidentified, negative, and generalizing antecedents in institutional and literary registers.",
        grammar_desc="repaso integral de oraciones de relativo en subjuntivo con antecedentes hipotéticos, negativos y estatutarios",
        ex_ref=f"exercises/b2/{c_con}-ex.json",
        ex_ids=[f"{c_con}.ex01", f"{c_con}.ex02", f"{c_con}.ex03", f"{c_con}.ex04", f"{c_con}.ex05", f"{c_con}.ex06", f"{c_con}.ex07", f"{c_con}.ex08"],
        goals=[
            "Synthesize indicative vs subjunctive selection in relative clauses with full confidence.",
            "Formulate categorical denials and institutional prerequisites using negative and generalizing pronouns.",
            "Analyze literary and legal excerpts reflecting hypothetical criteria and human searches."
        ],
        checklist_items=[
            "Diferencio con precisión entre antecedentes específicos (indicativo) e hipotéticos (subjuntivo).",
            "Uso el subjuntivo ante antecedentes negativos como 'nadie', 'nada' o 'ningún'.",
            "Construyo relativas preposicionales formales ('en el cual', 'con quien').",
            "Redacto cláusulas generalizadoras y estatutarias ('cualquiera que', 'todo aquel que')."
        ],
        story_ref=f"stories/classics/b2/{c_con.replace('-consolidation', '')}.json"
    ))
    print("Completed Core Unit 13 generation!")

    # =========================================================================
    # REGIONAL UNIT 13: COLOMBIA I: THE ANDEAN CORE, COFFEE & REALISM (b2-colombiaandina)
    # =========================================================================

    # Lesson 1: b2-colombiaandina-01
    r1 = "b2-colombiaandina-01"
    write_json(f"vocabulary/b2/{r1}-voc.json", {
        "id": "vocab.b2.colombiaandina.01",
        "lesson": r1,
        "title": "Geografía fractal, cordilleras y fábricas de agua",
        "theme": "Topografía andina, pisos térmicos, páramos y endemismos colombianos",
        "words": [
            {"lemma": "páramo", "translation": "paramo, high-altitude Andean moorland", "pos": "noun"},
            {"lemma": "frailejón", "translation": "espeletia, frailejon (water-capturing Andean plant)", "pos": "noun"},
            {"lemma": "cordillera", "translation": "mountain range", "pos": "noun"},
            {"lemma": "cuenca", "translation": "river basin, watershed", "pos": "noun"},
            {"lemma": "macizo", "translation": "mountain massif", "pos": "noun"},
            {"lemma": "represar", "translation": "to dam, to hold back water", "pos": "verb"},
            {"lemma": "abrupto", "translation": "abrupt, steep, rugged", "pos": "adjective"},
            {"lemma": "endémico", "translation": "endemic, native exclusively", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r1}-a-gr.json", {
        "id": "grammar.b2.colombiaandina.01.colombia-cordilleras-paramos",
        "title": "La geografía fractal andina y los páramos colombianos",
        "sections": [
            {
                "type": "text",
                "title": "Discurso biogeográfico y ecología de alta montaña",
                "content": "La descripción del territorio colombiano en nivel B2 integra una visión fractal de sus tres ramales andinos (Occidental, Central y Oriental) que nacen en el Macizo Colombiano. El registro analítico combina oraciones adjetivas y construcciones de finalidad para explicar cómo los páramos actúan como 'fábricas de agua' que abastecen a más del setenta por ciento de la población del país."
            },
            {
                "type": "table",
                "title": "Topografía andina y funciones ecosistémicas",
                "rows": [
                    ["Páramo de Sumapaz", "Ecosistema que capta la humedad de las nubes."],
                    ["Frailejones (Espeletia)", "Plantas que retienen el agua para los valles."],
                    ["Macizo Colombiano", "Punto orográfico del cual brotan los mayores ríos."],
                    ["Cañón del Chicamocha", "Accidente abrupto que modela microclimas áridos."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{r1}-ex.json", {
        "lesson": r1,
        "exercises": [
            {
                "id": f"{r1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el páramo", "high-altitude Andean moorland"],
                    ["el frailejón", "water-capturing Andean plant"],
                    ["el macizo", "mountain massif"],
                    ["abrupto", "steep, rugged"]
                ],
                "teaches": ["b2-colombiaandina-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El frailejón es una planta emblemática que __ apenas un centímetro por año en las cumbres andinas. (crecer)",
                "answer": "crece",
                "english": "The frailejon is an emblematic plant that grows barely one centimeter per year in the Andean peaks.",
                "teaches": ["colombia-cordilleras-paramos"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué afirmación describe con precisión sintáctica la función de los páramos colombianos?",
                "options": [
                    "Colombia alberga más de la mitad de los páramos del planeta, los cuales son ecosistemas que abastecen de agua a las principales metrópolis andinas.",
                    "Los páramos colombianos son lugares que no tienen ninguna importancia para el abastecimiento hídrico.",
                    "El río Magdalena nace en el páramo sin que nadie sepa su origen geográfico exacto."
                ],
                "correct": 0,
                "teaches": ["colombia-cordilleras-paramos"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "Macizo", "Colombiano", "es", "la", "estrella", "fluvial", "donde", "nacen", "los", "grandes", "ríos."],
                "solution": ["El", "Macizo", "Colombiano", "es", "la", "estrella", "fluvial", "donde", "nacen", "los", "grandes", "ríos."],
                "english": "The Colombian Massif is the fluvial star where the great rivers are born.",
                "teaches": ["colombia-cordilleras-paramos"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Bióloga suiza", "text": "¿Por qué Colombia posee una diversidad biológica tan desproporcionada respecto a su extensión territorial?"},
                    {"speaker": "Geógrafo andino", "text": "_____"},
                    {"speaker": "Bióloga suiza", "text": "Eso explica la extraordinaria abundancia de especies de aves y orquídeas."}
                ],
                "options": [
                    "Se debe a que las tres cordilleras generan un mosaico fractal de pisos térmicos que alberga microclimas y endemismos únicos en cada valle.",
                    "El transporte marítimo conecta a los archipiélagos caribeños con las Antillas Menores.",
                    "Los cultivos de banano se concentran en las planicies del golfo de Urabá."
                ],
                "correct": 0,
                "teaches": ["colombia-cordilleras-paramos"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los páramos capturan la niebla condensada y regulan el caudal de las cuencas interandinas.",
                "english": "The paramos capture condensed fog and regulate the volume of inter-Andean basins.",
                "teaches": ["colombia-cordilleras-paramos"]
            }
        ]
    })

    story_col_01 = {
        "id": "b2-colombiaandina-01",
        "title": "Las tres cordilleras y los guardianes de la niebla",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica geográfica y ecológica de nivel B2 sobre la orografía fractal de Colombia: la división de los Andes en tres ramales en el Macizo Colombiano, los páramos de Chingaza y Sumapaz como fábricas de agua y el rol sagrado de los frailejones en la preservación del equilibrio hídrico continental.",
        "characters": [
            "Felipe Montoya",
            "Marta Cifuentes",
            "Don Rogelio"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Pocos territorios en el planeta exhiben una complejidad geográfica tan sobrecogedora como la que configura la columna vertebral de Colombia. Al penetrar desde el sur continental tras recorrer miles de leguas por Sudamérica, la monumental cordillera de los Andes tropieza con el Macizo Colombiano —también llamado por los lugareños el Nudo de Almaguer— y se fractura como una gigantesca mano abierta en tres ramales paralelos e independientes: la cordillera Occidental, la cordillera Central y la cordillera Oriental. Esta trinidad montañosa esculpe una geografía fractal de profundos cañones interandinos, valles fértiles y altiplanos escarpados que históricamente determinaron el relativo aislamiento entre regiones, forjando identidades culturales profundamente singulares, acentos inconfundibles y un mosaico biológico de una riqueza enteramente insospechada en la cuenca del Cauca y el Magdalena."
            },
            {
                "type": "narration",
                "text": "Entre las cumbres nebulosas de estas cordilleras, por encima de los tres mil metros sobre el nivel del mar, florece el ecosistema más estratégico, frágil y singular de los Andes septentrionales: el páramo. Colombia concentra con orgullo más del cincuenta por ciento de los páramos de todo el globo terráqueo, destacándose colosos como el páramo de Sumapaz —el más extenso y misterioso de la Tierra— y el complejo de Chingaza, cuyas lagunas glaciares abastecen de agua potable de altísima pureza al ochenta por ciento de los millones de habitantes de la capital bogotana. En estos parajes de silencios sobrecogedores y vientos cortantes, el frío perpetuo convive con una radiación solar implacable que obliga a la vegetación nativa a desarrollar adaptaciones fisiológicas extraordinarias para sobrevivir."
            },
            {
                "type": "narration",
                "text": "El protagonista indiscutible de este santuario nuboso es el frailejón, planta del género Espeletia cuyas hojas gruesas, lanudas y aterciopeladas forman una roseta perfecta diseñada evolutivamente para atrapar la niebla húmeda que asciende incansablemente desde la inmensa cuenca amazónica y el valle del río Magdalena. Cada frailejón es un organismo prodigioso que crece a un ritmo parsimonioso de apenas un centímetro al año, acumulando en su tallo resinoso y en el denso colchón de musgos esponjosos miles de litros de agua dulce que luego son liberados con asombrosa regularidad hacia las quebradas y los ríos tributarios. Caminar por estos valles poblados de siluetas erguidas y coronadas de amarillo evoca la imagen poética de monjes encapuchados que custodian en silencio el secreto milenario de la vida en las alturas."
            },
            {
                "type": "narration",
                "text": "Felipe Montoya, un hidrólogo oriundo de Manizales con dos décadas de experiencia en aforos cordilleranos, y Marta Cifuentes, una botánica de la Universidad Nacional especializada en criptógamas andinas, ascienden al páramo de Chingaza durante una jornada de medición del estrés hídrico estacional. Acompañados por Don Rogelio, un campesino guardaparques que conoce cada recodo de turbera y cada risco desde su más tierna infancia, los investigadores constatan cómo las fluctuaciones térmicas extremas —que pueden oscilar desde varios grados bajo cero en la madrugada hasta más de veinte grados al mediodía bajo un cielo despejado— ponen a prueba la formidable resiliencia de este regulador térmico del continente."
            },
            {
                "type": "narration",
                "text": "'La gente en las grandes urbes que abre el grifo cada mañana con naturalidad ignora a menudo que esa agua cristalina no proviene de una fábrica ni de un simple embalse de cemento, sino de las hojas velludas de estos frailejones centenarios que desafían la ventisca y la intemperie', reflexiona Felipe mientras instala un pluviómetro digital cerca de una laguna de origen glaciar. Don Rogelio asiente con gravedad campesina, recordando que para las antiguas civilizaciones muiscas estas lagunas de altura constituían el útero sagrado del cosmos, el santuario reverenciado de donde emergió la diosa Bachué con un niño en brazos para poblar el mundo terrenal con su linaje humano antes de transformarse en serpiente sagrada."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el frágil equilibrio de estos páramos enfrenta amenazas contemporáneas severas que no admiten dilaciones. El avance descontrolado de la frontera agrícola, el pastoreo intensivo de ganado de altura y los proyectos de megaminería que pretenden horadar los yacimientos de oro y carbón en las faldas cordilleranas han encendido las alarmas de las comunidades científicas, campesinas e indígenas. Defender las tres cordilleras y sus fábricas de agua representa hoy en Colombia no solo una causa ambiental ineludible, sino una condición de supervivencia elemental para las futuras generaciones, sellando un pacto ético con la niebla que nutre el porvenir de la patria."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cómo se describe la división orográfica de los Andes al ingresar a territorio colombiano?",
                        "options": [
                            "Se divide en tres ramales montañosos paralelos —Occidental, Central y Oriental— a partir del Macizo Colombiano.",
                            "Se extingue en una sola cordillera baja que rodea la selva amazónica.",
                            "Forma una meseta desértica uniforme que cruza el país de este a oeste.",
                            "Se sumerge bajo el océano Pacífico sin formar valles interandinos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 detalla que la cordillera se fractura como una mano abierta en tres ramales paralelos e independientes al chocar con el Macizo Colombiano."
                    },
                    {
                        "question": "¿Cuál es la función ecológica fundamental del frailejón descrita en el relato?",
                        "options": [
                            "Atrapar la humedad de la niebla con sus hojas aterciopeladas y liberar agua dulce de forma continua hacia las cuencas fluviales.",
                            "Generar calor geotérmico para elevar la temperatura de las lagunas de origen glaciar.",
                            "Proporcionar madera resistente para la construcción de viviendas en los altiplanos.",
                            "Servir de alimento exclusivo para las aves migratorias procedentes del Caribe."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 explica que el frailejón atrapa la niebla con sus hojas velludas y acumula miles de litros que nutren las quebradas y ríos."
                    },
                    {
                        "question": "¿Qué significado cultural y ancestral tenían las lagunas de páramo para el pueblo muisca según Don Rogelio?",
                        "options": [
                            "Eran consideradas el útero sagrado de donde emergió la diosa Bachué para poblar la tierra.",
                            "Eran depósitos comerciales donde se almacenaban los granos de maíz cosechados.",
                            "Eran fortalezas militares donde se repelían las invasiones de las tribus del litoral.",
                            "Eran canteras de piedras para esculpir herramientas agrícolas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 menciona que para los muiscas estas lagunas de altura eran el útero sagrado del cosmos del que emergió Bachué."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r1}.json", story_col_01)

    write_json(f"lessons/b2/{r1}.json", make_lesson(
        stem=r1,
        unit_num=13,
        title="Las tres cordilleras y la geografía fractal colombiana",
        goal="Analyze Colombia's tri-cordillera geography, paramo ecosystems, and high-altitude water sources using biogeographical terminology.",
        grammar_desc="discurso biogeográfico andino y oraciones de relieve topográfico",
        grammar_ref=f"grammar/b2/{r1}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r1}-voc.json",
        ex_ref=f"exercises/b2/{r1}-ex.json",
        ex_ids=[f"{r1}.ex01", f"{r1}.ex02", f"{r1}.ex03", f"{r1}.ex04", f"{r1}.ex05", f"{r1}.ex06"],
        goals=[
            "Describe the three Andean cordilleras and the Colombian Massif.",
            "Explain the hydrologic function of paramos and frailejones.",
            "Deploy geographical and conservation vocabulary with grammatical precision."
        ],
        story_ref=f"stories/world/b2/{r1}.json"
    ))

    # Lesson 2: b2-colombiaandina-02
    r2 = "b2-colombiaandina-02"
    write_json(f"vocabulary/b2/{r2}-voc.json", {
        "id": "vocab.b2.colombiaandina.02",
        "lesson": r2,
        "title": "Bogotá: Cultura ciudadana, movilidad y vida urbana",
        "theme": "Urbanismo bogotano, ciclovía, debate intelectual y convivencia metropolitana",
        "words": [
            {"lemma": "altiplano", "translation": "high plateau, savanna", "pos": "noun"},
            {"lemma": "ciclovía", "translation": "bike path, open-street cycling network", "pos": "noun"},
            {"lemma": "convivencia", "translation": "coexistence, civic harmony", "pos": "noun"},
            {"lemma": "tertulia", "translation": "intellectual gathering, literary circle", "pos": "noun"},
            {"lemma": "descongestionar", "translation": "to decongest, to ease traffic", "pos": "verb"},
            {"lemma": "transitar", "translation": "to travel through, to walk/drive through", "pos": "verb"},
            {"lemma": "multitudinario", "translation": "massive, crowded", "pos": "adjective"},
            {"lemma": "cosmopolita", "translation": "cosmopolitan", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r2}-a-gr.json", {
        "id": "grammar.b2.colombiaandina.02.colombia-bogota-atenas-debate",
        "title": "Bogotá: Ciudadanía, debate público y movilidad urbana",
        "sections": [
            {
                "type": "text",
                "title": "El ensayo sociopolítico y el análisis de políticas urbanas",
                "content": "El examen de la capital colombiana —situada a 2.600 metros de altitud en la Sabana de Bogotá— articula la histórica reputación de la ciudad como centro de universidades y debates cívicos con los desafíos de la movilidad contemporánea (TransMilenio, ciclorrutas, metro). Se utilizan oraciones de relativo para ponderar los aciertos y dilemas de la cultura ciudadana."
            },
            {
                "type": "table",
                "title": "Estructuras de análisis sociourbano bogotano",
                "rows": [
                    ["Cultura ciudadana", "Un modelo en el que la pedagogía primó sobre la sanción."],
                    ["Movilidad y ciclovía", "Un sistema pionero que reduce la huella de carbono."],
                    ["Vida intelectual", "Una capital cuyas librerías y cafés acogen el debate."],
                    ["Cerros tutelares", "Miradores naturales desde los cuales se domina la sabana."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{r2}-ex.json", {
        "lesson": r2,
        "exercises": [
            {
                "id": f"{r2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el altiplano", "high plateau, savanna"],
                    ["la ciclovía", "open-street cycling network"],
                    ["la tertulia", "intellectual gathering"],
                    ["descongestionar", "to ease traffic, to decongest"]
                ],
                "teaches": ["b2-colombiaandina-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La capital colombiana cuenta con una tradición letrada que le __ históricamente el apodo de la Atenas suramericana. (valer)",
                "answer": "valió",
                "english": "The Colombian capital possesses a literate tradition that historically earned it the moniker of the South American Athens.",
                "teaches": ["colombia-bogota-atenas-debate"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué oración analiza la Ciclovía bogotana con propiedad sintáctica?",
                "options": [
                    "La Ciclovía de Bogotá es un programa pionero en el que millones de ciudadanos se apropian pacíficamente del espacio vial cada domingo.",
                    "La Ciclovía es un proyecto vial que nadie en Bogotá utiliza los fines de semana.",
                    "El TransMilenio reemplazó completamente a las bicicletas en los años noventa."
                ],
                "correct": 0,
                "teaches": ["colombia-bogota-atenas-debate"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "cerros", "orientales", "son", "los", "muros", "verdes", "que", "custodian", "a", "Bogotá."],
                "solution": ["Los", "cerros", "orientales", "son", "los", "muros", "verdes", "que", "custodian", "a", "Bogotá."],
                "english": "The eastern hills are the green walls that guard Bogotá.",
                "teaches": ["colombia-bogota-atenas-debate"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Urbanista mexicano", "text": "¿Qué lecciones dejó el célebre experimento de cultura ciudadana en la Bogotá de los años noventa?"},
                    {"speaker": "Socióloga colombiana", "text": "_____"},
                    {"speaker": "Urbanista mexicano", "text": "Un precedente fundamental para humanizar las metrópolis latinoamericanas."}
                ],
                "options": [
                    "Demostró que el cambio cívico es sostenible cuando se emplean recursos pedagógicos y símbolos colectivos que apelan al respeto mutuo.",
                    "La Plaza de Mercado de Paloquemao recibe flores frescas desde la madrugada.",
                    "El teleférico de Monserrate fue construido por ingenieros suizos en el siglo veinte."
                ],
                "correct": 0,
                "teaches": ["colombia-bogota-atenas-debate"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El debate público en Bogotá refleja la polifonía de una metrópoli moldeada por la migración interna.",
                "english": "Public debate in Bogotá reflects the polyphony of a metropolis shaped by internal migration.",
                "teaches": ["colombia-bogota-atenas-debate"]
            }
        ]
    })

    story_col_02 = {
        "id": "b2-colombiaandina-02",
        "title": "Bogotá: La sabana letrada y la reinvención cívica",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica urbana y sociológica de nivel B2 sobre Bogotá: la vida en la meseta andina a 2.600 metros de altura, la herencia ilustrada de la Atenas suramericana, la revolución cívica de la Ciclovía y los desafíos contemporáneos de movilidad y equidad en el corazón político del país.",
        "characters": [
            "Camila Restrepo",
            "Julián Pardo",
            "Profesor Salcedo"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Asentada a dos mil seiscientos metros sobre el nivel del mar en una inmensa altiplanicie coronada por los cerros tutelares de Monserrate y Guadalupe, Bogotá despliega una personalidad urbana insólita y fascinante en el panorama latinoamericano. Lejos de la sensualidad cálida y festiva de las costas caribeñas, la capital colombiana late bajo una luz plateada, un cielo frecuentemente encapotado y un aire frío de montaña que históricamente templó el carácter sobrio, formal y profundamente reflexivo de sus habitantes. Ya en el siglo XIX, los diplomáticos y viajeros europeos quedaron pasmados ante la proliferación de imprentas, colegios mayores, academias de la lengua y tertulias literarias que florecían en el céntrico barrio colonial de La Candelaria, bautizando a la urbe andina con el honroso y solemne título de la 'Atenas suramericana'."
            },
            {
                "type": "narration",
                "text": "Esa devoción por la palabra escrita, la sutileza jurídica y el debate filosófico coexistió siempre con profundas tensiones sociales y violentas fracturas históricas que marcaron a fuego el destino nacional. El trágico 'Bogotazo' del 9 de abril de 1948, desatado tras el magnicidio en plena carrera séptima del caudillo popular Jorge Eliécer Gaitán, redujo a cenizas buena parte del casco histórico y catapultó una explosión demográfica sin precedentes. A lo largo de las décadas posteriores, oleadas masivas de familias campesinas desterradas por la violencia partidista en los campos llegaron a la sabana en busca de refugio, dignidad y porvenir, transformando una austera ciudad letrada de medio millón de personas en una metrópoli vibrante, diversa, caótica y desbordante de más de ocho millones de almas procedentes de todos los confines de la república."
            },
            {
                "type": "narration",
                "text": "Fue a mediados de los años noventa cuando Bogotá protagonizó uno de los experimentos de gobernanza democrática y transformación cívica más comentados y emulados del urbanismo contemporáneo. Bajo liderazgos audaces y heterodoxos como el del matemático y filósofo Antanas Mockus, la administración distrital apostó resueltamente por la 'cultura ciudadana': mimos artísticos en los cruces peatonales para regular el caótico tráfico vehicular, tarjetas de cartulina con pulgares arriba o abajo empuñadas por los transeúntes y una pedagogía colectiva que priorizó la fuerza de la moral y el acuerdo mutuo sobre la sanción policial coercitiva. Simultáneamente, la ciudad rediseñó el espacio público, priorizando anchas alamedas peatonales, una extensa red de ciclorrutas y el sistema masivo de autobuses de tránsito rápido TransMilenio."
            },
            {
                "type": "narration",
                "text": "Cada domingo por la mañana, la capital experimenta un rito multitudinario de convivencia pacífica que asombra invariablemente a propios y extraños: la tradicional Ciclovía de Bogotá. Más de ciento veinte kilómetros de autopistas y avenidas arteriales son cerrados al tráfico motorizado para el disfrute exclusivo de más de un millón y medio de ciclistas, patinadores, familias y peatones de todos los estratos socioeconómicos. En ese asfalto liberado del humo de los motores, el ejecutivo corporativo y el obrero de construcción pedalean codo a codo frente al verdor majestuoso de los cerros orientales, degustando jugos de mandarina recién exprimidos, obleas con arequipe y mazorcas tiernas asadas al carbón en carretillas populares."
            },
            {
                "type": "narration",
                "text": "Camila Restrepo, una arquitecta urbanista formada en la Universidad de los Andes, y Julián Pardo, gestor cultural de la Red de Bibliotecas Públicas en la imponente sede Virgilio Barco, conversan animadamente con el profesor Salcedo mientras contemplan la panorámica urbana desde el mirador del Chorro de Quevedo. El profesor, veterano testigo de las mutaciones de la ciudad, reflexiona sobre el carácter hospitalario de los bogotanos: 'Bogotá es una urbe que nunca te pregunta de dónde vienes ni te cierra las puertas; acoge a gentes del Pacífico afrocolombiano, de las sabanas ganaderas, de los valles cafeteros y del sur indígena. Cada comunidad aporta su propia cadencia, convirtiendo a esta meseta en el verdadero crisol y termómetro de la nacionalidad'."
            },
            {
                "type": "narration",
                "text": "A pesar de sus formidables logros cívicos, Bogotá lidia hoy con los dolores de crecimiento propios de una megaciudad andina en transición: la saturación vehicular, la histórica postergación de una red de metro pesado y las persistentes brechas de segregación espacial entre el norte acomodado y el sur periférico. No obstante, en sus cafés centenarios donde aún se discute de política y poesía, en las concurridas ferias internacionales del libro y en las marchas de una juventud que reclama justicia ambiental, late con fuerza incombustible la convicción de que la palabra argumentada y el espacio compartido siguen siendo los mayores tesoros de la capital."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué Bogotá fue apodada en el siglo XIX como la 'Atenas suramericana'?",
                        "options": [
                            "Por la gran cantidad de imprentas, bibliotecas, academias y tertulias intelectuales que florecían en su seno.",
                            "Por haber sido fundada por colonos griegos que introdujeron la arquitectura clásica.",
                            "Por sus victorias militares en las guerras independentistas continentales.",
                            "Por ser la sede de los primeros juegos olímpicos andinos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 explica que los visitantes extranjeros admiraban la proliferación de imprentas, tertulias literarias y academias en La Candelaria, bautizándola así."
                    },
                    {
                        "question": "¿En qué consistió la estrategia de 'cultura ciudadana' implementada en los años noventa en la capital?",
                        "options": [
                            "En una pedagogía cívica innovadora con mimos callejeros y acuerdos colectivos para fomentar el respeto sin recurrir a la mera coerción.",
                            "En imponer toques de queda militares estrictos en todas las avenidas principales.",
                            "En prohibir el uso de automóviles particulares durante los días laborables.",
                            "En privatizar los parques públicos y demoler el centro colonial de La Candelaria."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 describe cómo Antanas Mockus empleó mimos, tarjetas cívicas y pedagogía colectiva para priorizar los acuerdos morales sobre la coerción."
                    },
                    {
                        "question": "¿Qué representa la Ciclovía dominical para la dinámica social de Bogotá?",
                        "options": [
                            "Un espacio integrador de convivencia ciudadana donde personas de todos los sectores sociales comparten el asfalto liberado de vehículos.",
                            "Una competencia deportiva profesional regulada por la federación ciclista internacional.",
                            "Una manifestación de protesta sindical contra el transporte colectivo.",
                            "Un mercado informal exclusivo para la venta de repuestos mecánicos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 subraya que la Ciclovía cierra más de 120 km de vías para que millones de personas de todos los estratos socioeconómicos compartan el espacio pacíficamente."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r2}.json", story_col_02)

    write_json(f"lessons/b2/{r2}.json", make_lesson(
        stem=r2,
        unit_num=13,
        title="Bogotá: Atenas suramericana, TransMilenio y debate público",
        goal="Explore Bogotá's intellectual heritage, civic culture transformations, and urban transit dilemmas through formal sociological discourse.",
        grammar_desc="análisis de políticas cívicas y discurso sociológico urbano",
        grammar_ref=f"grammar/b2/{r2}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r2}-voc.json",
        ex_ref=f"exercises/b2/{r2}-ex.json",
        ex_ids=[f"{r2}.ex01", f"{r2}.ex02", f"{r2}.ex03", f"{r2}.ex04", f"{r2}.ex05", f"{r2}.ex06"],
        goals=[
            "Trace Bogotá's evolution from the 19th-century intellectual hub to a sprawling metropolis.",
            "Understand civic culture innovations (Mockus, Ciclovía, BRT TransMilenio).",
            "Express complex assessments of urban equity and public mobility."
        ],
        story_ref=f"stories/world/b2/{r2}.json"
    ))

    # Lesson 3: b2-colombiaandina-03
    r3 = "b2-colombiaandina-03"
    write_json(f"vocabulary/b2/{r3}-voc.json", {
        "id": "vocab.b2.colombiaandina.03",
        "lesson": r3,
        "title": "Medellín: Resiliencia paisa, urbanismo social e innovación",
        "theme": "Transformación de Medellín, Metrocable, Comuna 13, cultura paisa y emprendimiento",
        "words": [
            {"lemma": "paisa", "translation": "paisa (native of Antioquia/Coffee Axis region)", "pos": "noun"},
            {"lemma": "resiliencia", "translation": "resilience", "pos": "noun"},
            {"lemma": "comuna", "translation": "urban district, commune, hillside neighborhood", "pos": "noun"},
            {"lemma": "metrocable", "translation": "cable-car mass transit system", "pos": "noun"},
            {"lemma": "emprendimiento", "translation": "entrepreneurship, initiative", "pos": "noun"},
            {"lemma": "integrar", "translation": "to integrate, to bring together", "pos": "verb"},
            {"lemma": "emblemático", "translation": "emblematic, iconic", "pos": "adjective"},
            {"lemma": "pujante", "translation": "thriving, dynamic, enterprising", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r3}-a-gr.json", {
        "id": "grammar.b2.colombiaandina.03.colombia-medellin-innovacion-social",
        "title": "Medellín: Innovación social, urbanismo y resiliencia comunitaria",
        "sections": [
            {
                "type": "text",
                "title": "El urbanismo social como respuesta a la violencia histórica",
                "content": "El análisis de Medellín en nivel B2 estudia el tránsito de la ciudad más violenta del mundo en los años ochenta y noventa a un referente global de innovación urbana. Se analizan estructuras de relativo que califican la integración del transporte público (Metrocable, escaleras eléctricas de la Comuna 13) con la arquitectura pública (parques biblioteca) y el arraigo cultural paisa."
            },
            {
                "type": "table",
                "title": "Innovaciones del urbanismo social en Medellín",
                "rows": [
                    ["Metrocable", "Medio de transporte mediante el cual se conectaron las laderas."],
                    ["Parques Biblioteca", "Espacios públicos en los que la comunidad recuperó la dignidad."],
                    ["Escaleras de la Comuna 13", "Infraestructura que reemplazó a cientos de escalones."],
                    ["Identidad paisa", "Pobladores cuya pujanza impulsó la industria regional."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{r3}-ex.json", {
        "lesson": r3,
        "exercises": [
            {
                "id": f"{r3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el paisa", "native of Antioquia/Coffee Axis"],
                    ["la resiliencia", "resilience"],
                    ["el emprendimiento", "initiative, entrepreneurship"],
                    ["pujante", "thriving, dynamic, enterprising"]
                ],
                "teaches": ["b2-colombiaandina-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Metrocable fue el primer sistema de teleférico en el mundo que se __ al transporte público masivo. (incorporar)",
                "answer": "incorporó",
                "english": "The Metrocable was the first cable car system in the world that was incorporated into mass transit.",
                "teaches": ["colombia-medellin-innovacion-social"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué enunciado expresa con exactitud el principio rector del 'urbanismo social' en Medellín?",
                "options": [
                    "Consistió en construir las obras públicas más bellas en los barrios que habían sufrido la mayor exclusión y violencia.",
                    "Prohibió la construcción de viviendas populares en las pendientes del valle de Aburrá.",
                    "Priorizó la inversión estatal exclusivamente en el distrito financiero del sur."
                ],
                "correct": 0,
                "teaches": ["colombia-medellin-innovacion-social"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "pujanza", "paisa", "es", "un", "rasgo", "que", "impulsa", "la", "innovación", "empresarial."],
                "solution": ["La", "pujanza", "paisa", "es", "un", "rasgo", "que", "impulsa", "la", "innovación", "empresarial."],
                "english": "Paisa industriousness is a trait that drives business innovation.",
                "teaches": ["colombia-medellin-innovacion-social"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista alemán", "text": "¿Cómo logró Medellín superar las alarmantes tasas de homicidio de los años noventa?"},
                    {"speaker": "Líder comunitario", "text": "_____"},
                    {"speaker": "Periodista alemán", "text": "Una demostración conmovedora del poder sanador de la inversión social."}
                ],
                "options": [
                    "Fue un esfuerzo conjunto en el que la inversión pública llegó con dignidad a sitios adonde el Estado nunca antes había hecho presencia.",
                    "El servicio de metro cuenta con dos líneas principales que cruzan el valle de norte a sur.",
                    "La feria de las flores se celebra anualmente durante el mes de agosto con desfiles de silleteros."
                ],
                "correct": 0,
                "teaches": ["colombia-medellin-innovacion-social"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El arte urbano y el hip hop transformaron el dolor de la Comuna 13 en memoria viva.",
                "english": "Urban art and hip hop transformed the pain of Comuna 13 into living memory.",
                "teaches": ["colombia-medellin-innovacion-social"]
            }
        ]
    })

    story_col_03 = {
        "id": "b2-colombiaandina-03",
        "title": "Medellín: La metamorfosis de la ciudad de la eterna primavera",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica sociourbana de nivel B2 sobre la resiliencia de Medellín y la cultura paisa: el trauma de los años del narcotráfico, el pionero urbanismo social que llevó teleféricos y bibliotecas monumentales a las laderas marginadas, y el renacer cultural de la Comuna 13 a través de los murales y el arte juvenil.",
        "characters": [
            "Mateo Henao",
            "Doña Luz Marina",
            "Yeison 'K-libre'"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Encajonada en el verde y angosto valle de Aburrá, custodiada por cumbres andinas que parecen tocar las nubes, Medellín gozó durante décadas del apelativo seductor de la 'ciudad de la eterna primavera'. Su clima excepcionalmente templado, la exuberancia de sus jardines en flor y la proverbial vocación laboriosa de los paisas —como se conoce popularmente a los nativos de Antioquia y el Eje Cafetero— cimentaron a lo largo del siglo XX una próspera sociedad industrial volcada a la manufactura textil, la metalmecánica y el comercio regional. Sin embargo, hacia finales de la década de 1980 y los albores de los noventa, la irrupción implacable del cartel del narcotráfico, los sangrientos atentados con carros bomba y la guerra territorial entre bandas paramilitares y milicias sumieron a la capital antioqueña en una espiral trágica que la situó como la urbe más violenta del mundo."
            },
            {
                "type": "narration",
                "text": "Aquella catástrofe social y humanitaria amenazó con fracturar irreversiblemente el tejido comunitario y despojar de esperanza a generaciones enteras de jóvenes. Las populosas comunas que trepaban de manera desordenada por las faldas empinadas del valle crecieron en medio del abandono institucional, privadas de vías de acceso seguras, escuelas dignas o centros culturales. No obstante, en lugar de claudicar ante la barbarie, la sociedad civil organizada, las universidades, los colectivos juveniles, el empresariado comprometido y sucesivas administraciones municipales concertaron un pacto cívico audaz fundamentado en una premisa ética revolucionaria: el 'urbanismo social'. El axioma era contundente y conmovedor: las obras públicas más bellas y las inversiones más generosas debían destinarse a los vecindarios más pobres y lacerados por el conflicto."
            },
            {
                "type": "narration",
                "text": "El emblema indiscutible de esa audacia fue el sistema Metrocable, inaugurado en 2004 en la ladera nororiental de la ciudad como extensión del metro elevado. Por primera vez en la historia del transporte masivo en el mundo, la tecnología de las cabinas de teleférico de montaña fue adaptada para el servicio público cotidiano en barriadas populares de topografía intrincada. Decenas de miles de trabajadores de barrios como Santo Domingo Savio y Popular 1 comenzaron a surcar los aires por encima de los tejados de cinc, reduciendo trayectos extenuantes de más de dos horas a escasos quince minutos de viaje digno y seguro. En torno a las estaciones de cable se erigieron los emblemáticos 'parques biblioteca', complejos arquitectónicos de diseño vanguardista concebidos como templos cívicos de lectura, aprendizaje tecnológico y encuentro vecinal."
            },
            {
                "type": "narration",
                "text": "En la ladera occidental del valle, la Comuna 13 protagonizó una gesta de resiliencia cultural aún más asombrosa. Tras haber padecido años de zozobra bajo el dominio de grupos armados irregulares y el trauma de intervenciones militares sangrientas como la Operación Orión en 2002, los jóvenes del territorio decidieron responder a las balas con pinceles, micrófonos y pasos de baile. La instalación en 2011 de seis tramos dobles de escaleras eléctricas al aire libre —hito de ingeniería urbana que sustituyó a más de trescientos cincuenta escalones de cemento resbaladizo— devolvió la movilidad a los ancianos y sirvió como catalizador para un renacimiento artístico que asombró a la comunidad internacional."
            },
            {
                "type": "narration",
                "text": "En la actualidad, Mateo Henao, sociólogo de la Universidad de Antioquia, recorre junto a delegaciones internacionales los pasajes multicolores del sector de Las Independencias. Mientras Doña Luz Marina atiende a los transeúntes ofreciéndoles empanadas crujientes y café recién colado, Yeison, un joven rapero apodado 'K-libre', interpreta vibrantes rimas sobre memoria y reconciliación frente a un inmenso mural donde una niña sonriente suelta mariposas amarillas al viento. 'En estas paredes no ocultamos las cicatrices de la guerra; las pintamos con colores vivos para que nadie en Colombia olvide lo que costó recuperar la tranquilidad', manifiesta Yeison con orgullo campesino y urbano."
            },
            {
                "type": "narration",
                "text": "Medellín no ha resuelto de manera definitiva todos sus dilemas de equidad ni ha erradicado por completo los desafíos de la delincuencia organizada que todavía presiona a ciertos sectores vulnerables. Sin embargo, su capacidad sobrehumana para transformar el dolor en innovación social, su vigorosa apuesta por distritos de ciencia y tecnología como Ruta N y la calidez incondicional de su gente demuestran que la mayor grandeza de la cultura paisa no radica únicamente en su pujanza mercantil, sino en su inagotable voluntad de renacer de las cenizas para edificar un porvenir de dignidad y esperanza compartida."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál fue el principio rector del 'urbanismo social' implementado en Medellín tras la crisis de violencia?",
                        "options": [
                            "Construir las obras públicas más bellas y vanguardistas en los barrios más marginados y vulnerables de la ciudad.",
                            "Trasladar a toda la población de las laderas hacia campamentos agrícolas fuera del valle.",
                            "Demoler los barrios populares para reemplazarlos exclusivamente por complejos de apartamentos privados.",
                            "Militarizar permanentemente las colinas sin realizar inversiones en transporte o educación."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 expone la premisa del urbanismo social: los edificios más hermosos y las mejores infraestructuras debían construirse en las zonas más golpeadas por la exclusión."
                    },
                    {
                        "question": "¿Qué innovación tecnológica global representó el sistema Metrocable de Medellín inaugurado en 2004?",
                        "options": [
                            "Fue la primera adaptación en el mundo de teleféricos de montaña para el transporte público masivo urbano en barriadas populares.",
                            "Fue el primer tren subterráneo automatizado propulsado por hidrógeno verde en América del Sur.",
                            "Fue una flota de helicópteros subsidiados para transportar trabajadores textiles.",
                            "Fue un canal acuático artificial excavado a lo largo de las pendientes del valle de Aburrá."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 3 resalta que por primera vez en el mundo las cabinas de teleférico se adaptaron para el transporte público masivo de barriadas empinadas."
                    },
                    {
                        "question": "¿De qué manera la comunidad juvenil de la Comuna 13 canalizó la memoria histórica de su territorio?",
                        "options": [
                            "A través del muralismo, el rap y las expresiones artísticas urbanas que transformaron el dolor colectivo en testimonio y esperanza.",
                            "Mediante la clausura de las escuelas para dedicarse exclusivamente al comercio informal.",
                            "Creando partidos políticos clandestinos para impugnar las obras públicas de la alcaldía.",
                            "Abandonando el barrio en masa para radicarse en otras regiones de Colombia."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 y 5 detallan cómo los jóvenes canalizaron su experiencia a través del hip hop y los murales para narrar su memoria viva y educar a las nuevas generaciones."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r3}.json", story_col_03)

    write_json(f"lessons/b2/{r3}.json", make_lesson(
        stem=r3,
        unit_num=13,
        title="Medellín y el Paisa: De la crisis a la innovación social",
        goal="Examine Medellín's transformation from violence to a global beacon of social urbanism, cable-transit integration, and paisa entrepreneurial resilience.",
        grammar_desc="narrativa de resiliencia comunitaria y urbanismo social",
        grammar_ref=f"grammar/b2/{r3}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r3}-voc.json",
        ex_ref=f"exercises/b2/{r3}-ex.json",
        ex_ids=[f"{r3}.ex01", f"{r3}.ex02", f"{r3}.ex03", f"{r3}.ex04", f"{r3}.ex05", f"{r3}.ex06"],
        goals=[
            "Analyze the causes and architectural solutions of Medellín's social urbanism.",
            "Understand the impact of Metrocable and hillside public escalators in Comuna 13.",
            "Characterize the cultural and entrepreneurial values of the Paisa identity."
        ],
        story_ref=f"stories/world/b2/{r3}.json"
    ))

    # Lesson 4: b2-colombiaandina-04
    r4 = "b2-colombiaandina-04"
    write_json(f"vocabulary/b2/{r4}-voc.json", {
        "id": "vocab.b2.colombiaandina.04",
        "lesson": r4,
        "title": "El Eje Cafetero: Patrimonio de la humanidad y tradición cafetera",
        "theme": "Cultura cafetera, bahareque, chivas, recolección manual y palma de cera",
        "words": [
            {"lemma": "cafetal", "translation": "coffee plantation, coffee field", "pos": "noun"},
            {"lemma": "bahareque", "translation": "bahareque (traditional wattle-and-daub / bamboo architecture)", "pos": "noun"},
            {"lemma": "chiva", "translation": "chiva (colorful open-sided wooden mountain bus)", "pos": "noun"},
            {"lemma": "recolector", "translation": "coffee picker, harvester", "pos": "noun"},
            {"lemma": "despulpar", "translation": "to pulp (strip coffee cherry pulp from bean)", "pos": "verb"},
            {"lemma": "secar", "translation": "to dry, to cure beans in the sun", "pos": "verb"},
            {"lemma": "ondulado", "translation": "rolling, undulating, hilly", "pos": "adjective"},
            {"lemma": "artesanal", "translation": "artisanal, traditional handcrafted", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r4}-a-gr.json", {
        "id": "grammar.b2.colombiaandina.04.colombia-eje-cafetero-patrimonio",
        "title": "El Eje Cafetero: Paisaje Cultural Patrimonio de la Humanidad",
        "sections": [
            {
                "type": "text",
                "title": "El lenguaje agronómico y la valoración del patrimonio vivo",
                "content": "La descripción del Paisaje Cultural Cafetero de Colombia (declarado patrimonio de la humanidad por la UNESCO en 2011) abarca los departamentos de Caldas, Quindío, Risaralda y el norte del Valle del Cauca. En nivel B2, se despliegan oraciones descriptivas complejas y oraciones de relativo para detallar las técnicas de cultivo en laderas empinadas, la arquitectura de bahareque y guadua, y la icónica palma de cera del Valle de Cocora."
            },
            {
                "type": "table",
                "title": "Patrimonio cultural y arquitectónico cafetero",
                "rows": [
                    ["Recolección manual", "Selección grano a grano que garantiza la calidad arábica."],
                    ["Arquitectura de bahareque", "Haciendas cuyas paredes de guadua resisten los sismos."],
                    ["Chiva o bus escalera", "Vehículo tradicional en el que viajan campesinos y cosechas."],
                    ["Palma de cera del Quindío", "Árbol nacional que supera los sesenta metros de altitud."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{r4}-ex.json", {
        "lesson": r4,
        "exercises": [
            {
                "id": f"{r4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el cafetal", "coffee plantation"],
                    ["el bahareque", "wattle-and-daub bamboo architecture"],
                    ["la chiva", "open-sided wooden bus"],
                    ["artesanal", "handcrafted, traditional"]
                ],
                "teaches": ["b2-colombiaandina-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La arquitectura tradicional de las haciendas utiliza la guadua, una especie de bambú que __ elasticidad ante los terremotos. (proporcionar)",
                "answer": "proporciona",
                "english": "Traditional hacienda architecture uses guadua, a bamboo species that provides elasticity against earthquakes.",
                "teaches": ["colombia-eje-cafetero-patrimonio"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo singular distingue al Paisaje Cultural Cafetero reconocido por la UNESCO?",
                "options": [
                    "Es un paisaje productivo vivo donde el esfuerzo humano y la topografía escarpada crearon una tradición cafetera y arquitectónica única.",
                    "Es una llanura desértica donde el café se recoge exclusivamente con maquinaria industrial pesada.",
                    "Es un parque temático artificial construido para el turismo sin actividad agrícola real."
                ],
                "correct": 0,
                "teaches": ["colombia-eje-cafetero-patrimonio"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Las", "palmas", "de", "cera", "gigantescas", "se", "elevan", "entre", "la", "neblina", "andina."],
                "solution": ["Las", "palmas", "de", "cera", "gigantescas", "se", "elevan", "entre", "la", "neblina", "andina."],
                "english": "The gigantic wax palms rise amidst the Andean mist.",
                "teaches": ["colombia-eje-cafetero-patrimonio"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Sommelier de café", "text": "¿A qué se debe el prestigio internacional del café colombiano frente al de otras latitudes?"},
                    {"speaker": "Agrónoma del Quindío", "text": "_____"},
                    {"speaker": "Sommelier de café", "text": "Un perfil de taza incomparable por su limpieza y notas florales."}
                ],
                "options": [
                    "A que cultivamos exclusivamente la variedad arábica en laderas empinadas, lo que exige una recolección manual que evita dañar los granos verdes.",
                    "Las fincas cafeteras cuentan con piscinas recreativas para los turistas extranjeros.",
                    "El puerto de Buenaventura moviliza contenedores marítimos hacia los mercados asiáticos."
                ],
                "correct": 0,
                "teaches": ["colombia-eje-cafetero-patrimonio"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los recolectores seleccionan únicamente las cerezas maduras para garantizar la suavidad de la taza.",
                "english": "The pickers select only the ripe cherries to guarantee the cup's smoothness.",
                "teaches": ["colombia-eje-cafetero-patrimonio"]
            }
        ]
    })

    story_col_04 = {
        "id": "b2-colombiaandina-04",
        "title": "El Eje Cafetero: El aroma de las laderas y las palmas gigantes",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Crónica cultural y sensorial de nivel B2 sobre el Paisaje Cultural Cafetero de Colombia: la vida en las fincas de Caldas y Quindío, el arte minucioso de la recolección manual de café arábico suave, la arquitectura de bahareque y guadua, y la imponencia solemne de las palmas de cera en el Valle de Cocora.",
        "characters": [
            "Don Bernardo Echeverri",
            "Carolina Duque",
            "Santiago"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al coronar el legendario Alto de La Línea en la cordillera Central y descender hacia la cuenca fértil del río Cauca, la vista se sumerge en un mar interminable de colinas onduladas pintadas de infinitas gamas de verde esmeralda. Nos encontramos en el corazón geográfico del Eje Cafetero colombiano, territorio integrado por los departamentos de Caldas, Risaralda y Quindío, junto a municipios del norte del Valle del Cauca, cuya fisonomía deslumbrante fue consagrada por la UNESCO en 2011 en la lista del Patrimonio Mundial bajo el título de 'Paisaje Cultural Cafetero'. Aquí, la topografía quebrada de los Andes se fusionó durante más de un siglo con el tesón incansable de familias campesinas para forjar una cultura productiva de una nobleza y armonía paisajística sin paralelo."
            },
            {
                "type": "narration",
                "text": "A diferencia de las inmensas llanuras mecanizadas de otros grandes productores del orbe como Brasil o Vietnam, el café en Colombia se siembra y cosecha casi exclusivamente en laderas empinadas de entre cuarenta y sesenta grados de pendiente, a altitudes privilegiadas que van de los mil doscientos a los dos mil metros sobre el nivel del mar. Estas condiciones microclimáticas de nubosidad moderada, lluvias generosas y suelos volcánicos ricos en cenizas y minerales exigen un cuidado enteramente artesanal. Los caficultores colombianos cultivan exclusivamente la especie *Coffea arabica*, apreciada universalmente por su aroma envolvente, su acidez limpia y equilibrada y su suavidad gustativa, lo que consagró a la nación andina como el principal exportador del mejor café arábico lavado del mundo."
            },
            {
                "type": "narration",
                "text": "En la finca 'La Primavera', encaramada en las vertientes brumosas del municipio de Chinchiná, Don Bernardo Echeverri inicia su jornada cotidiana mucho antes del clarear del alba. Ataviado con su poncho de algodón blanco sobre el hombro, su sombrero aguadeño de fina paja toquilla y su carriel de cuero vacuno con múltiples bolsillos secretos, Don Bernardo supervisa a la cuadrilla de recolectores. Con sus canastos de mimbre o plástico trenzado sujetos con correas a la cintura, hombres y mujeres se adentran en los cafetales realizando el minucioso 'pascón' o cosecha selectiva, desprendiendo con las yemas de los dedos únicamente las cerezas que lucen un rojo carmesí perfecto y dejando madurar los granos verdes para semanas venideras."
            },
            {
                "type": "narration",
                "text": "El alma identitaria de este paisaje cultural se manifiesta igualmente en su arquitectura vernácula, conocida como el 'bahareque de guadua'. En poblados pintorescos y bien conservados como Salento, Filandia, Pijao o Salamina, las casonas tradicionales lucen balcones de maderas nativas primorosamente talladas y pintadas con esmaltes de vivos colores primarios —amarillos relucientes, azules turquesa, verdes esmeralda y rojos vivos— bajo aleros volados que resguardan las fachadas de los aguaceros andinos. El armazón interior de estas edificaciones utiliza la guadua (*Guadua angustifolia*), un bambú gigante de portentosa flexibilidad que permitió a los pueblos cafeteros resistir durante más de un siglo intensos sismos tectónicos sin desplomarse."
            },
            {
                "type": "narration",
                "text": "Unos pocos kilómetros cordillera arriba, en el deslumbrante Valle de Cocora a las puertas del Parque Nacional Natural Los Nevados, Carolina Duque guía a su sobrino Santiago a través de un paraje que parece extraído de un lienzo fantástico. Entre la densa niebla que desciende de los glaciares coronados de nieve emergen las siluetas esbeltas y solemnes de la palma de cera del Quindío (*Ceroxylon quindiuense*), árbol nacional de la República de Colombia. Estas palmas gigantescas, capaces de elevarse hasta sesenta metros del suelo y de vivir más de dos siglos, desafían el viento helado como columnas vivas, brindando refugio indispensable al loro coroniazul y a una rica variedad de colibríes andinos."
            },
            {
                "type": "narration",
                "text": "Al declinar la tarde, una chiva o 'bus escalera' —camión artesanal de madera decorado con complejas grecas geométricas polícromas— se detiene ruidosamente en la plaza empedrada de Salento cargada de bultos de café pergamino, racimos de plátano dominico y campesinos que se disponen a saborear un humeante 'tinto' en los cafés de la plaza. En ese trago reconfortante servido en taza de loza se sintetiza la memoria viva de una comarca que supo transformar el rigor de la montaña en aroma, patrimonio y hospitalidad para el disfrute de la humanidad entera."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué el cultivo de café en el Eje Cafetero colombiano requiere una recolección manual grano a grano?",
                        "options": [
                            "Debido a las pendientes escarpadas de las laderas andinas y a la necesidad de cosechar únicamente las cerezas arábicas en su punto óptimo de maduración.",
                            "Porque las leyes ambientales prohíben la entrada de cualquier tipo de herramienta metálica a las fincas.",
                            "Porque los frutos maduran todos en un solo día del año y se estropean al contacto con maquinaria.",
                            "Para evitar que las plantas de café crezcan por encima de los diez metros de altura."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 y 3 explican que la topografía empinada impide la mecanización y exige recolectar manualmente solo las cerezas maduras para garantizar la calidad del arábico suave."
                    },
                    {
                        "question": "¿Qué propiedades estructurales destaca el texto sobre el bahareque de guadua en la arquitectura cafetera tradicional?",
                        "options": [
                            "Su elasticidad y resistencia sismorresistente frente a los terremotos gracias a la flexibilidad del bambú nativo.",
                            "Su capacidad para aislar las viviendas de las altas temperaturas del desierto.",
                            "Que es un material pétreo impenetrable utilizado para construir fortalezas militares.",
                            "Que permite edificar rascacielos de más de cuarenta pisos en las zonas montañosas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 subraya que la guadua es un bambú nativo de extraordinaria flexibilidad estructural que permite a las casas resistir sismos sin colapsar."
                    },
                    {
                        "question": "¿Qué singularidad botánica distingue a la palma de cera en el Valle de Cocora?",
                        "options": [
                            "Es el árbol nacional de Colombia y la palma más alta del planeta, alcanzando hasta sesenta metros de altitud.",
                            "Es una planta carnívora gigante que habita en las cuevas de los nevados.",
                            "Produce granos de café de color azul oscuro durante la temporada invernal.",
                            "Es un arbusto rastrero que se extiende únicamente a ras de suelo en las orillas de los ríos."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 describe a la palma de cera como el árbol nacional que supera los sesenta metros de altura y vive más de dos siglos."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r4}.json", story_col_04)

    write_json(f"lessons/b2/{r4}.json", make_lesson(
        stem=r4,
        unit_num=13,
        title="El Eje Cafetero y el paisaje cultural patrimonio",
        goal="Discover the UNESCO Coffee Cultural Landscape, traditional bahareque architecture, manual harvesting, and the Cocora Valley wax palms.",
        grammar_desc="discurso etnobotánico, agronómico y valoración del patrimonio cultural",
        grammar_ref=f"grammar/b2/{r4}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r4}-voc.json",
        ex_ref=f"exercises/b2/{r4}-ex.json",
        ex_ids=[f"{r4}.ex01", f"{r4}.ex02", f"{r4}.ex03", f"{r4}.ex04", f"{r4}.ex05", f"{r4}.ex06"],
        goals=[
            "Understand why Colombian Arabica coffee is hand-picked on steep slopes.",
            "Analyze traditional bahareque and guadua earthquake-resistant architecture.",
            "Describe the botanical wonder of the Quindío wax palms in Cocora Valley."
        ],
        story_ref=f"stories/world/b2/{r4}.json"
    ))

    # Lesson 5: b2-colombiaandina-05
    r5 = "b2-colombiaandina-05"
    write_json(f"vocabulary/b2/{r5}-voc.json", {
        "id": "vocab.b2.colombiaandina.05",
        "lesson": r5,
        "title": "Gabriel García Márquez: Realismo Mágico y verdad histórica",
        "theme": "Crítica literaria, realismo mágico, Macondo, periodismo y memoria colectiva",
        "words": [
            {"lemma": "verosimilitud", "translation": "verisimilitude, credibility", "pos": "noun"},
            {"lemma": "hipérbole", "translation": "hyperbole, exaggeration", "pos": "noun"},
            {"lemma": "masacre", "translation": "massacre, slaughter", "pos": "noun"},
            {"lemma": "estirpe", "translation": "lineage, stock, descent", "pos": "noun"},
            {"lemma": "desmitificar", "translation": "to demystify", "pos": "verb"},
            {"lemma": "transmutar", "translation": "to transmute, to transform", "pos": "verb"},
            {"lemma": "desmesurado", "translation": "disproportionate, boundless, immeasurable", "pos": "adjective"},
            {"lemma": "mitológico", "translation": "mythological", "pos": "adjective"}
        ]
    })

    write_json(f"grammar/b2/{r5}-a-gr.json", {
        "id": "grammar.b2.colombiaandina.05.colombia-garcia-marquez-realismo",
        "title": "Gabriel García Márquez: El Realismo Mágico como testimonio social",
        "sections": [
            {
                "type": "text",
                "title": "Análisis literario y mediación testimonial en la prosa de Gabo",
                "content": "El estudio de la obra de Gabriel García Márquez en nivel B2 trasciende la etiqueta folclórica del Realismo Mágico para examinarlo como un método estético y testimonial arraigado en la realidad colombiana. Se analizan estructuras de relativo que conectan los hechos históricos (la masacre de las bananeras de 1928, las guerras civiles del siglo XIX) con la transmutación mítica de Macondo."
            },
            {
                "type": "table",
                "title": "Dimensiones críticas del Realismo Mágico",
                "rows": [
                    ["Oficio periodístico", "Práctica en la que Gabo aprendió a verificar la verdad."],
                    ["Masacre de las bananeras", "Episodio histórico que el poder oficial intentó borrar."],
                    ["Tono de la narración", "Voz que relata lo prodigioso con rostro impasible."],
                    ["Soledad colectiva", "Condición trágica que condena a estirpes enteras."]
                ]
            }
        ]
    })

    write_json(f"exercises/b2/{r5}-ex.json", {
        "lesson": r5,
        "exercises": [
            {
                "id": f"{r5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["la verosimilitud", "verisimilitude, credibility"],
                    ["la hipérbole", "hyperbole, exaggeration"],
                    ["la estirpe", "lineage, stock, descent"],
                    ["desmesurado", "boundless, disproportionate"]
                ],
                "teaches": ["b2-colombiaandina-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "García Márquez afirmó que no había en sus novelas una sola línea que no __ su origen en un hecho real. (tener)",
                "answer": "tuviera",
                "english": "García Márquez affirmed that there was not in his novels a single line that did not have its origin in a real fact.",
                "teaches": ["colombia-garcia-marquez-realismo"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la interpretación crítica más rigurosa sobre el Realismo Mágico en García Márquez?",
                "options": [
                    "No es una simple evasión fantástica, sino un lente estético que revela la desmesurada y trágica realidad latinoamericana.",
                    "Es un artificio puramente comercial diseñado sin ninguna vinculación con la historia ni los conflictos de Colombia.",
                    "Es una recopilación de leyendas infantiles desconectada de la denuncia social."
                ],
                "correct": 0,
                "teaches": ["colombia-garcia-marquez-realismo"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Su", "abuela", "le", "contaba", "las", "cosas", "más", "fantásticas", "con", "rostro", "imperturbable."],
                "solution": ["Su", "abuela", "le", "contaba", "las", "cosas", "más", "fantásticas", "con", "rostro", "imperturbable."],
                "english": "His grandmother told him the most fantastic things with an imperturbable face.",
                "teaches": ["colombia-garcia-marquez-realismo"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Estudiante de letras", "text": "¿Por qué el episodio del tren bananero en Cien años de soledad genera tanto debate historiográfico?"},
                    {"speaker": "Catedrático", "text": "_____"},
                    {"speaker": "Estudiante de letras", "text": "Una demostración magistral de cómo la literatura rescata la memoria pisoteada."}
                ],
                "options": [
                    "Porque Gabo recurrió a una hipérbole trágica mediante la cual rescató del olvido una matanza obrera real que los partes oficiales negaban.",
                    "Las compañías bananeras exportaban frutas a través de vapores fluviales en el río Magdalena.",
                    "El tren de pasajeros circulaba dos veces por semana entre Santa Marta y Aracataca."
                ],
                "correct": 0,
                "teaches": ["colombia-garcia-marquez-realismo"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Macondo no es un lugar geográfico, sino un estado del alma compartido por todos los pueblos de nuestra América.",
                "english": "Macondo is not a geographical place, but a state of the soul shared by all the peoples of our America.",
                "teaches": ["colombia-garcia-marquez-realismo"]
            }
        ]
    })

    story_col_05 = {
        "id": "b2-colombiaandina-05",
        "title": "Gabo: El periodismo de la desmesura y el espejo de Macondo",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Ensayo literario y biográfico de nivel B2 sobre Gabriel García Márquez: sus raíces en Aracataca, la herencia oral de sus abuelos, el rigor de su oficio periodístico en El Espectador y cómo el Realismo Mágico se convirtió en una herramienta de denuncia social frente a las tragedias históricas de Colombia.",
        "characters": [
            "Gabriel García Márquez",
            "Tranquilina Iguarán",
            "Coronel Nicolás Márquez"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Cuando en octubre de 1982 la Academia Sueca otorgó el Premio Nobel de Literatura a Gabriel García Márquez por 'sus novelas e historias cortas en las que lo fantástico y lo real se combinan en un rico mundo de imaginación compuesta que refleja la vida y los conflictos de un continente', el gran narrador colombiano pronunció en Estocolmo un discurso de aceptación inolvidable titulado 'La soledad de América Latina'. En aquellas páginas encendidas, Gabo no se regodeó en exotismos turísticos ni en fantasías folclóricas confortables; denunció con valentía a dictadores sangrientos, ríos desbordados de cadáveres por la violencia política, guerras civiles despiadadas y millones de seres humanos arrojados al desamparo. Para él, la realidad desmesurada de nuestra historia superaba con creces a cualquier invención literaria que un escritor pudiera concebir."
            },
            {
                "type": "narration",
                "text": "Las raíces profundas de esa mirada estética y política se hundían en la vieja casona de paredes agrietadas de Aracataca, un pequeño municipio de la zona bananera del Magdalena donde el futuro escritor transcurrió su infancia al cuidado de sus abuelos maternos. Su abuelo, el coronel Nicolás Ricardo Márquez, veterano de la Guerra de los Mil Días, solía llevar al pequeño de la mano para relatarle sin tapujos la verdad sobre los abusos de las compañías transnacionales y la brutalidad de las guerras fratricidas, inculcándole la convicción inquebrantable de que la dignidad humana jamás puede ser silenciada por el poder. Al mismo tiempo, su abuela, doña Tranquilina Iguarán, poblaba las noches infantiles con relatos de fantasmas familiares, presagios misteriosos y sucesos sobrenaturales que narraba con un rostro imperturbable, como si los milagros formaran parte corriente de la rutina hogareña."
            },
            {
                "type": "narration",
                "text": "De esa doble vertiente formativa —la severa memoria histórica del abuelo militar y la certidumbre mágica de la abuela narradora— nació el tono inconfundible de su creación literaria. No obstante, el crisol que pulió su prosa precisa y su implacable ética de observación no fue la academia ni los cenáculos bohemios, sino el ejercicio incansable del periodismo de a pie. En las salas de redacción calurosas y desordenadas de diarios como *El Universal* de Cartagena, *El Heraldo* de Barranquilla y de manera estelar *El Espectador* de Bogotá, Gabo aprendió a reportear en la calle, a contrastar versiones testimoniales y a desconfiar metódicamente de los comunicados emitidos por los gobiernos de turno."
            },
            {
                "type": "narration",
                "text": "Su monumental reportaje investigativo por entregas *Relato de un náufrago*, publicado con gran repercusión popular en 1955 en las páginas de *El Espectador*, evidenció que el periodismo riguroso armado de tensión narrativa era capaz de hacer tambalear a una dictadura militar. Al desmentir la versión oficial del régimen del general Gustavo Rojas Pinilla y comprobar que el marinero Luis Alejandro Velasco no había caído al mar por una supuesta tormenta, sino debido a un cargamento desmesurado de contrabando mal estibado en la cubierta del buque de guerra, el joven cronista enfureció a las autoridades castrenses, viéndose compelido a iniciar un largo y fructífero exilio en suelo europeo."
            },
            {
                "type": "narration",
                "text": "Años después, cuando en una modesta casa del barrio de San Ángel en la Ciudad de México redactó febrilmente a lo largo de dieciocho meses las páginas inmortales de *Cien años de soledad*, García Márquez volcó toda esa sabiduría testimonial en la epopeya de Macondo. En el trágico episodio de la masacre de las bananeras de 1928, donde tres mil trabajadores huelguistas son ametrallados en la plaza de la estación y transportados en un tren silencioso para ser arrojados al mar como racimos de fruta podrida, Gabo erigió una metáfora desgarradora sobre la desmemoria histórica inducida por el Estado, encarnada en los ciudadanos aterrorizados que repiten mecánicamente que en el pueblo no ha ocurrido absolutamente nada."
            },
            {
                "type": "narration",
                "text": "El Realismo Mágico, por tanto, constituyó para García Márquez una herramienta de resistencia moral y de lucidez política: una vía estética para nombrar las heridas no cerradas de Colombia, devolver la palabra a las víctimas del olvido oficial y proclamar ante el mundo que las estirpes condenadas a cien años de despojo tienen el derecho irrenunciable a una segunda oportunidad sobre la tierra. Su obra perdura como un faro ético que recuerda a las nuevas generaciones que la mayor hazaña del arte es transformar la memoria del sufrimiento en esperanza colectiva y dignidad perdurable."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué dos influencias familiares primordiales surgió el tono narrativo de García Márquez según el texto?",
                        "options": [
                            "De la memoria histórica y política de su abuelo el coronel, y de los relatos mágicos narrados con rostro impávido por su abuela Tranquilina.",
                            "De las lecciones de latín que recibió de sacerdotes franceses en un convento andino.",
                            "De los manuales de navegación marítima de su padre y las canciones de marineros caribeños.",
                            "De los tratados de economía que estudió en las universidades europeas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 2 y 3 explican que combinó la memoria histórica y ética de su abuelo Nicolás con las leyendas mágicas contadas con naturalidad por su abuela Tranquilina."
                    },
                    {
                        "question": "¿Qué consecuencias políticas generó la publicación del reportaje *Relato de un náufrago* en 1955?",
                        "options": [
                            "Desmintió la versión oficial de la dictadura militar al revelar que el naufragio se debió a un cargamento de contrabando, obligando a Gabo al exilio.",
                            "Provocó la caída inmediata de todas las empresas bananeras extranjeras en el Caribe.",
                            "Hizo que la Academia Sueca le otorgara el Premio Nobel de Periodismo.",
                            "Obligó al cierre definitivo de la fábrica textil de Medellín donde trabajaba el marinero."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 relata que el reportaje demostró que no hubo tormenta sino contrabando mal estibado, lo que molestó a la dictadura y forzó su salida a Europa."
                    },
                    {
                        "question": "¿Qué denuncia fundamental encierra el episodio de la masacre de las bananeras en *Cien años de soledad*?",
                        "options": [
                            "Denuncia la matanza histórica de obreros en 1928 y el intento del poder político de borrar el crimen mediante la desmemoria colectiva inducida.",
                            "Critica que los trabajadores no estuvieran suficientemente capacitados para operar la maquinaria ferroviaria.",
                            "Muestra que los huelguistas habían abandonado sus puestos para celebrar una fiesta religiosa.",
                            "Sugiere que las plantaciones bananeras debían reemplazarse por minas de esmeraldas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 5 analiza cómo el episodio revela el horror de la masacre real de 1928 y la desmemoria impuesta por el discurso oficial que negaba la tragedia."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{r5}.json", story_col_05)

    write_json(f"lessons/b2/{r5}.json", make_lesson(
        stem=r5,
        unit_num=13,
        title="Gabriel García Márquez y el Realismo Mágico como lente social",
        goal="Analyze García Márquez's literary legacy, journalistic roots, and the use of Magical Realism to address historical memory and social injustice in Colombia.",
        grammar_desc="crítica literaria, mediación testimonial y narrativa del realismo mágico",
        grammar_ref=f"grammar/b2/{r5}-a-gr.json",
        vocab_ref=f"vocabulary/b2/{r5}-voc.json",
        ex_ref=f"exercises/b2/{r5}-ex.json",
        ex_ids=[f"{r5}.ex01", f"{r5}.ex02", f"{r5}.ex03", f"{r5}.ex04", f"{r5}.ex05", f"{r5}.ex06"],
        goals=[
            "Trace Gabo's upbringing in Aracataca and his journalistic career.",
            "Deconstruct the social critique behind the banana massacre in Macondo.",
            "Synthesize literary and political discourse at an advanced B2 level."
        ],
        story_ref=f"stories/world/b2/{r5}.json"
    ))

    # Regional Consolidation: b2-colombiaandina-consolidation
    rc_con = "b2-colombiaandina-consolidation"
    write_json(f"exercises/b2/{rc_con}-ex.json", {
        "lesson": rc_con,
        "exercises": [
            {
                "id": f"{rc_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["el frailejón", "high-altitude Andean water plant"],
                    ["el bahareque", "wattle-and-daub bamboo structure"],
                    ["la resiliencia", "resilience, capacity to recover"],
                    ["la verosimilitud", "verisimilitude, credibility"]
                ],
                "teaches": ["b2-colombiaandina-vocab"]
            },
            {
                "id": f"{rc_con}.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué elemento unifica la geografía, el urbanismo y la cultura del corazón andino colombiano?",
                "options": [
                    "La capacidad de las comunidades para transformar una topografía abrupta y desafiante en un crisol de innovación social, patrimonio y memoria viva.",
                    "La uniformidad de un clima desértico que homogeneizó las costumbres en todo el país.",
                    "La sumisión absoluta a los dictados de monopolios extranjeros."
                ],
                "correct": 0,
                "teaches": ["colombia-cordilleras-paramos"]
            },
            {
                "id": f"{rc_con}.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Paisaje Cultural Cafetero es un modelo en el que la familia campesina __ tradiciones centenarias en laderas escarpadas. (preservar)",
                "answer": "preserva",
                "english": "The Coffee Cultural Landscape is a model in which the peasant family preserves century-old traditions on steep slopes.",
                "teaches": ["colombia-eje-cafetero-patrimonio"]
            },
            {
                "id": f"{rc_con}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "inversión", "social", "transformó", "barrios", "que", "habían", "sufrido", "la", "violencia."],
                "solution": ["La", "inversión", "social", "transformó", "barrios", "que", "habían", "sufrido", "la", "violencia."],
                "english": "Social investment transformed neighborhoods that had suffered violence.",
                "teaches": ["colombia-medellin-innovacion-social"]
            },
            {
                "id": f"{rc_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el Realismo Mágico en la narrativa de García Márquez?",
                "options": [
                    "Nombrar las heridas históricas y devolver la voz a las víctimas mediante una poética de la desmesura.",
                    "Entretener al público con cuentos de hadas ajenos a la realidad social colombiana.",
                    "Promocionar el cultivo intensivo de frutas tropicales en el extranjero."
                ],
                "correct": 0,
                "teaches": ["colombia-garcia-marquez-realismo"]
            },
            {
                "id": f"{rc_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Cuál es la mayor lección que ofrece la región andina colombiana al mundo contemporáneo?"},
                    {"speaker": "Antropóloga", "text": "_____"},
                    {"speaker": "Historiador", "text": "Una síntesis formidable de dignidad y esperanza compartida."}
                ],
                "options": [
                    "Haber demostrado que no existe abismo geográfico ni herida histórica que las comunidades no puedan superar mediante el arte, la educación y la solidaridad.",
                    "El cultivo de café arábico lavado requiere suelos volcánicos fértiles.",
                    "Las flotas de transporte intermunicipal operan desde terminales terrestres."
                ],
                "correct": 0,
                "teaches": ["colombia-medellin-innovacion-social"]
            },
            {
                "id": f"{rc_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "De los páramos nubosos a las tertulias bogotanas, Colombia conjuga naturaleza indómita y resiliencia creadora.",
                "english": "From cloudy paramos to Bogotan intellectual circles, Colombia combines untamed nature and creative resilience.",
                "teaches": ["colombia-cordilleras-paramos"]
            },
            {
                "id": f"{rc_con}.ex08",
                "type": "sentence-builder",
                "category": "writing",
                "tiles": ["Macondo", "reveló", "al", "mundo", "la", "desmesurada", "y", "mágica", "realidad", "latinoamericana."],
                "solution": ["Macondo", "reveló", "al", "mundo", "la", "desmesurada", "y", "mágica", "realidad", "latinoamericana."],
                "english": "Macondo revealed to the world the disproportionate and magical Latin American reality.",
                "teaches": ["colombia-garcia-marquez-realismo"]
            }
        ]
    })

    story_col_capstone = {
        "id": "b2-colombiaandina-consolidation",
        "title": "La espina dorsal andina: Polifonía, aroma y memoria",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Gran crónica de consolidación de nivel B2 sobre el corazón andino de Colombia: la odisea geográfica de sus tres cordilleras, la vitalidad cívica de la sabana bogotana, la lección de resiliencia social de Medellín, la nobleza del trabajo cafetero en las laderas y la resonancia universal de García Márquez en la conciencia colectiva.",
        "characters": [
            "Elena Arismendi",
            "Carlos Benavides"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Recorrer el corazón andino de Colombia supone descifrar una de las geografías humanas más fascinantes, abruptas y complejas de todo el continente americano. Cuando los primeros pobladores contemplaron la colosal muralla de cumbres que se elevaba desafiante desde las llanuras amazónicas y las cuencas litorales, comprendieron de inmediato que aquel territorio no admitía simplificaciones ni complacencias superficiales. Al fracturarse en tres cordilleras soberbias a partir del Macizo Colombiano, los Andes forzaron a cada pueblo a inventarse su propio modo de habitar las nubes, tallando caminos de herradura sobre desfiladeros vertiginosos y transformando el aislamiento geográfico en un formidable estímulo para la creatividad artística, la solidaridad comunitaria y la tenacidad cívica."
            },
            {
                "type": "narration",
                "text": "En las cumbres intocadas de los páramos de Chingaza y Sumapaz, el prodigio silencioso del agua cristalina nos recuerda a diario que la subsistencia de millones de compatriotas depende de la extrema fragilidad de un ecosistema que captura con paciencia la humedad de las nieblas andinas. Allí, donde los frailejones centenarios se yerguen como venerables monjes vegetales que apenas crecen un centímetro cada doce meses, las antiguas memorias muiscas parecen custodiar todavía el equilibrio hídrico de la nación. Proteger estos páramos frente a las presiones del extractivismo minero y las perturbaciones climáticas se ha consolidado como el mayor imperativo ético de una sociedad que reconoce en sus fuentes de agua el patrimonio más sagrado de su porvenir colectivo."
            },
            {
                "type": "narration",
                "text": "Descendiendo a la inmensa altiplanicie de la Sabana, Bogotá acoge ese torrente hídrico y vital para transformarlo en pensamiento crítico, debate universitario y polifonía ciudadana. La legendaria 'Atenas suramericana' de antaño ya no es el reducto reservado a una élite de gramáticos y letrados aislados en salones coloniales, sino una metrópoli poliédrica, dinámica y cosmopolita que aprendió a construirse sobre pactos de convivencia cívica, ciclovías multitudinarias y bibliotecas públicas abiertas a todos los sectores. En sus barrios confluyen las voces afro del litoral pacífico, el acento montañés de Boyacá y Santander y la alegría desbordante del Caribe, convirtiendo a la sabana en el verdadero condensador de las esperanzas nacionales."
            },
            {
                "type": "narration",
                "text": "Más al occidente, superando el cañón majestuoso del río Magdalena, el valle de Aburrá ofrece el testimonio elocuente de la metamorfosis urbana y social de Medellín. La que fuera en los años más sombríos del narcotráfico la ciudad más asolada por la violencia enseñó al mundo entero que el antídoto más eficaz contra la exclusión reside en el urbanismo social con rostro humano. Al articular cabinas de Metrocable y escaleras mecánicas en las pendientes escarpadas de la Comuna 13, la comunidad antioqueña demostró con creces que la belleza arquitectónica y la inversión estatal deben llegar primero a los más vulnerables, permitiendo que los murales comunitarios y el hip hop juvenil desarmen el miedo y siembren reconciliación."
            },
            {
                "type": "narration",
                "text": "Ese mismo espíritu industrioso y laborioso brilla con luz propia en las vertientes esmeralda del Eje Cafetero, donde el cultivo del café arábico suave lavado en laderas casi verticales consolidó una cultura campesina admirada universalmente como Patrimonio de la Humanidad por la UNESCO. Entre casonas tradicionales de bahareque y guadua adornadas con maderas multicolores y los senderos del Valle de Cocora escoltados por las monumentales palmas de cera que tocan el cielo andino, la recolección manual grano a grano representa un ritual de dignidad campesina que colma de aroma y reconocimiento a la patria entera ante los mercados del mundo."
            },
            {
                "type": "narration",
                "text": "Y tutelando toda esta epopeya de cicatrices superadas y sueños comunitarios, la figura universal de Gabriel García Márquez proyecta la luz de su sabiduría sobre la conciencia colectiva colombiana. Mediante el mito imperecedero de Macondo y la potencia de su prosa realista y mágica, Gabo entregó a la humanidad el espejo donde América Latina se reconoce en toda su desmesura trágica y su hermosura indomable, recordando que ninguna estirpe, por duras que hayan sido sus pruebas históricas, está condenada para siempre a la soledad. En esa certidumbre luminosa forjada en las cordilleras late hoy, con fuerza inquebrantable, el corazón andino de Colombia."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué manera el texto sintetiza la relación entre la geografía montañosa de Colombia y el carácter de sus pueblos?",
                        "options": [
                            "La fragmentación en tres cordilleras impulsó a las comunidades a desarrollar una singular capacidad de adaptación, creatividad y solidaridad cívica.",
                            "El relieve montañoso impidió permanentemente el desarrollo económico de las regiones del interior.",
                            "Las cordilleras forzaron a la población a abandonar los valles para radicarse exclusivamente en las islas del Caribe.",
                            "La topografía obligó al Estado a centralizar todos los recursos en una sola provincia costera."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 1 sostiene que la trinidad montañosa convirtió el aislamiento geográfico en un incentivo para la creatividad, la resiliencia y la tenacidad comunitaria."
                    },
                    {
                        "question": "¿Qué lección urbana global destaca la crónica a partir de la experiencia de Medellín y la Comuna 13?",
                        "options": [
                            "Que la inclusión social, el transporte público vanguardista y la cultura barrial pueden revertir décadas de violencia y marginación.",
                            "Que las ciudades andinas deben prohibir la construcción de viviendas en las pendientes del valle.",
                            "Que la inversión pública debe concentrarse únicamente en los distritos financieros de la urbe formal.",
                            "Que los teleféricos solo son viables en estaciones invernales de esquí."
                        ],
                        "correctIndex": 0,
                        "explanation": "El párrafo 4 remarca que llevar Metrocable y escaleras mecánicas a las laderas demostró que la inversión social de calidad puede transformar barrios vulnerables."
                    },
                    {
                        "question": "¿Cuál es el mensaje ético final que rescata el ensayo sobre la obra de Gabriel García Márquez?",
                        "options": [
                            "Que ninguna estirpe o pueblo, por más golpeado que haya sido por la violencia, está condenado para siempre a la soledad y la desesperanza.",
                            "Que la literatura debe evitar hablar de hechos históricos dolorosos para no desalentar a los lectores.",
                            "Que Macondo debe ser reconstruido como un parque de atracciones en la costa atlántica.",
                            "Que el Realismo Mágico es una fantasía ajena a los problemas de América Latina."
                        ],
                        "correctIndex": 0,
                        "explanation": "El último párrafo enfatiza que el legado de Gabo es el derecho inalienable de las comunidades a una segunda oportunidad de justicia y fraternidad frente a la soledad histórica."
                    }
                ]
            }
        }
    }
    write_json(f"stories/world/b2/{rc_con}.json", story_col_capstone)
    write_json("stories/world/b2/b2-colombiaandina.json", story_col_capstone)

    write_json(f"lessons/b2/{rc_con}.json", make_consolidation_lesson(
        stem=rc_con,
        unit_num=13,
        title="Consolidación: La espina dorsal andina y el alma colombiana",
        goal="Consolidate communicative and cultural mastery of the Colombian Andean region, integrating cordillera geography, civic debate, social urbanism, coffee heritage, and literary realism.",
        grammar_desc="repaso integral del discurso biogeográfico, social y literario del corazón andino colombiano",
        ex_ref=f"exercises/b2/{rc_con}-ex.json",
        ex_ids=[f"{rc_con}.ex01", f"{rc_con}.ex02", f"{rc_con}.ex03", f"{rc_con}.ex04", f"{rc_con}.ex05", f"{rc_con}.ex06", f"{rc_con}.ex07", f"{rc_con}.ex08"],
        goals=[
            "Synthesize geographical, social, and literary dimensions of Colombia's Andean core.",
            "Demonstrate fluency in complex relative clauses and formal socio-cultural registers.",
            "Articulate nuanced perspectives on Latin American resilience, urban transformation, and cultural memory."
        ],
        checklist_items=[
            "Comprendo la geografía fractal de las tres cordilleras y la función ecológica de los páramos.",
            "Analizo la evolución cívica de Bogotá y el impacto del urbanismo social en Medellín.",
            "Valoro la tradición del Paisaje Cultural Cafetero y la arquitectura de bahareque.",
            "Interpreto la dimensión testimonial y política del Realismo Mágico en García Márquez."
        ],
        story_ref=f"stories/world/b2/{rc_con}.json"
    ))
    print("Completed LatAm Unit 13 (Colombia Andina) generation!")

    # -------------------------------------------------------------------------
    # UPDATE CURRICULUM UNITS B2
    # -------------------------------------------------------------------------
    b2_units_path = BASE / "curriculum" / "units" / "b2.json"
    with open(b2_units_path, "r", encoding="utf-8") as f:
        b2_units = json.load(f)

    has_u13_core = any(u.get("title") == "Relative Clauses with Unidentified Antecedents" for u in b2_units)
    has_u13_reg = any(u.get("title") == "Colombia I: The Andean Core, Coffee & Realism" for u in b2_units)

    if not has_u13_core:
        b2_units.append({
            "title": "Relative Clauses with Unidentified Antecedents",
            "stems": [
                "b2-13-01",
                "b2-13-02",
                "b2-13-03",
                "b2-13-04",
                "b2-13-05",
                "b2-13-consolidation"
            ],
            "track": "core"
        })

    if not has_u13_reg:
        b2_units.append({
            "title": "Colombia I: The Andean Core, Coffee & Realism",
            "stems": [
                "b2-colombiaandina-01",
                "b2-colombiaandina-02",
                "b2-colombiaandina-03",
                "b2-colombiaandina-04",
                "b2-colombiaandina-05",
                "b2-colombiaandina-consolidation"
            ],
            "track": "latam"
        })

    with open(b2_units_path, "w", encoding="utf-8") as f:
        json.dump(b2_units, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Updated curriculum/units/b2.json with Unit 13!")

    # -------------------------------------------------------------------------
    # WORD COUNT AUDIT
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_13", story_core_13),
        ("story_col_01", story_col_01),
        ("story_col_02", story_col_02),
        ("story_col_03", story_col_03),
        ("story_col_04", story_col_04),
        ("story_col_05", story_col_05),
        ("story_col_capstone", story_col_capstone)
    ]
    print("\n--- Story Word Count Audit ---")
    all_ok = True
    for name, s in stories_to_audit:
        wc = count_words(s)
        status = "OK (650-825)" if 650 <= wc <= 825 else "OUT OF RANGE"
        if "OUT" in status:
            all_ok = False
        print(f"{name:20}: {wc:4} words -> {status}")
    if not all_ok:
        raise ValueError("Some stories failed the word count requirement (650-825 words)!")

if __name__ == "__main__":
    run()
