"""
Generator script for Latin American Spanish (es-latam) B2 Unit 27:
- Core B2: b2-27 (Advanced Prepositional Regimes & Prepositional Locutions)
- Regional B2: b2-uruguay (Uruguay: Secularism, Candombe & Progressive Institutions)
- Classic Literature Adaptation: Horacio Quiroga - Anaconda (1921)
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
LATAM_DIR = os.path.join(CONTENT_DIR, "es-latam")

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
            "locuciones-prepositivas-causa-origen": {
                "kind": "grammar",
                "name": "locuciones-prepositivas-causa-origen",
                "description": "Causal and originary prepositional locutions such as a raíz de, en virtud de, con motivo de in formal prose",
                "aliases": []
            },
            "locuciones-prepositivas-conformidad-criterio": {
                "kind": "grammar",
                "name": "locuciones-prepositivas-conformidad-criterio",
                "description": "Conformity and normative prepositional locutions including conforme a, de acuerdo con, con arreglo a, a tenor de",
                "aliases": []
            },
            "locuciones-prepositivas-finalidad-sacrificio": {
                "kind": "grammar",
                "name": "locuciones-prepositivas-finalidad-sacrificio",
                "description": "Teleological and sacrifice prepositional locutions such as en aras de, con miras a, a costa de, en pos de",
                "aliases": []
            },
            "locuciones-prepositivas-pretexto-salvedad": {
                "kind": "grammar",
                "name": "locuciones-prepositivas-pretexto-salvedad",
                "description": "Pretextual, delimiting, and restrictive locutions including so pretexto de, a juicio de, sin perjuicio de, al margen de",
                "aliases": []
            },
            "regimen-preposicional-verbos-avanzados": {
                "kind": "grammar",
                "name": "regimen-preposicional-verbos-avanzados",
                "description": "Advanced verb prepositional rection in analytical prose such as supeditar a, derivar en, estribar en, versar sobre, abogar por",
                "aliases": []
            },
            "b2-27-vocab": {
                "kind": "vocabulary",
                "name": "b2-27-vocab",
                "description": "Vocabulary for prepositional regimes, judicial phrasing, normative discourse, and administrative governance",
                "aliases": []
            },
            "b2-uruguay-vocab": {
                "kind": "vocabulary",
                "name": "b2-uruguay-vocab",
                "description": "Vocabulary for Uruguayan history, batllismo, candombe, civic secularism, and institutional democracy",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            if k not in skills:
                skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 27")

    # 2. Update grammar-titles.json
    def update_grammar_titles(titles):
        new_titles = {
            "locuciones-prepositivas-causa-origen": "causal prepositional locutions",
            "locuciones-prepositivas-conformidad-criterio": "prepositional locutions of conformity and criteria",
            "locuciones-prepositivas-finalidad-sacrificio": "purpose and sacrifice prepositional locutions",
            "locuciones-prepositivas-pretexto-salvedad": "pretext and restrictive prepositional locutions",
            "regimen-preposicional-verbos-avanzados": "advanced verb prepositional rections"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 27")

    # 3. Vocabulary Files (10 files)
    vocab_files = {
        "b2-27-01": {
            "id": "vocab.b2.27.01",
            "lesson": "b2-27-01",
            "title": "Causal & Origin Locutions: a raíz de, en virtud de",
            "words": [
                {"lemma": "a raíz de", "translation": "as a result of / following", "pos": "preposition"},
                {"lemma": "en virtud de", "translation": "by virtue of / pursuant to", "pos": "preposition"},
                {"lemma": "con motivo de", "translation": "on the occasion of / because of", "pos": "preposition"},
                {"lemma": "propiciar", "translation": "to foster / to promote", "pos": "verb"},
                {"lemma": "desencadenar", "translation": "to trigger / to unleash", "pos": "verb"},
                {"lemma": "precepto", "translation": "precept / mandate", "pos": "noun"},
                {"lemma": "emanar", "translation": "to emanate / to stem from", "pos": "verb"},
                {"lemma": "coyuntura", "translation": "conjuncture / situational context", "pos": "noun"},
                {"lemma": "fundamento", "translation": "foundation / legal basis", "pos": "noun"},
                {"lemma": "atribución", "translation": "power / authority / attribution", "pos": "noun"}
            ]
        },
        "b2-27-02": {
            "id": "vocab.b2.27.02",
            "lesson": "b2-27-02",
            "title": "Conformity & Normative Locutions: conforme a, de acuerdo con",
            "words": [
                {"lemma": "conforme a", "translation": "in accordance with / according to", "pos": "preposition"},
                {"lemma": "de acuerdo con", "translation": "in accordance with / according to", "pos": "preposition"},
                {"lemma": "con arreglo a", "translation": "in compliance with / pursuant to", "pos": "preposition"},
                {"lemma": "a tenor de", "translation": "according to the wording of / in light of", "pos": "preposition"},
                {"lemma": "estipulación", "translation": "stipulation / contractual clause", "pos": "noun"},
                {"lemma": "disposición", "translation": "provision / decree / disposition", "pos": "noun"},
                {"lemma": "supeditar", "translation": "to condition / to make subject to", "pos": "verb"},
                {"lemma": "acatar", "translation": "to abide by / to comply with", "pos": "verb"},
                {"lemma": "ordenanza", "translation": "ordinance / municipal regulation", "pos": "noun"},
                {"lemma": "dictamen", "translation": "official opinion / ruling", "pos": "noun"}
            ]
        },
        "b2-27-03": {
            "id": "vocab.b2.27.03",
            "lesson": "b2-27-03",
            "title": "Purpose & Sacrifice Locutions: en aras de, a costa de",
            "words": [
                {"lemma": "en aras de", "translation": "for the sake of / in pursuit of", "pos": "preposition"},
                {"lemma": "con miras a", "translation": "with a view to / aiming at", "pos": "preposition"},
                {"lemma": "a costa de", "translation": "at the expense of / at the cost of", "pos": "preposition"},
                {"lemma": "en pos de", "translation": "in pursuit of / striving towards", "pos": "preposition"},
                {"lemma": "sacrificio", "translation": "sacrifice", "pos": "noun"},
                {"lemma": "abnegación", "translation": "selflessness / self-sacrifice", "pos": "noun"},
                {"lemma": "consecución", "translation": "attainment / achievement", "pos": "noun"},
                {"lemma": "menoscabar", "translation": "to undermine / to impair", "pos": "verb"},
                {"lemma": "perjuicio", "translation": "detriment / harm / prejudice", "pos": "noun"},
                {"lemma": "claudicación", "translation": "giving up / surrendering", "pos": "noun"}
            ]
        },
        "b2-27-04": {
            "id": "vocab.b2.27.04",
            "lesson": "b2-27-04",
            "title": "Pretext & Restrictive Locutions: so pretexto de, a juicio de",
            "words": [
                {"lemma": "so pretexto de", "translation": "under the pretext of", "pos": "preposition"},
                {"lemma": "a juicio de", "translation": "in the opinion of / according to", "pos": "preposition"},
                {"lemma": "sin perjuicio de", "translation": "without prejudice to / notwithstanding", "pos": "preposition"},
                {"lemma": "al margen de", "translation": "apart from / outside of", "pos": "preposition"},
                {"lemma": "salvedad", "translation": "proviso / reservation / qualification", "pos": "noun"},
                {"lemma": "pretexto", "translation": "pretext / excuse", "pos": "noun"},
                {"lemma": "subterfugio", "translation": "subterfuge / evasion", "pos": "noun"},
                {"lemma": "soslayar", "translation": "to bypass / to avoid / to skirt", "pos": "verb"},
                {"lemma": "coartada", "translation": "alibi / pretext", "pos": "noun"},
                {"lemma": "arbitrariedad", "translation": "arbitrariness / abuse of power", "pos": "noun"}
            ]
        },
        "b2-27-05": {
            "id": "vocab.b2.27.05",
            "lesson": "b2-27-05",
            "title": "Advanced Verb Prepositional Regimes: estribar en, derivar en",
            "words": [
                {"lemma": "estribar en", "translation": "to lie in / to consist in", "pos": "verb"},
                {"lemma": "derivar en", "translation": "to lead to / to result in", "pos": "verb"},
                {"lemma": "versar sobre", "translation": "to deal with / to be about", "pos": "verb"},
                {"lemma": "abogar por", "translation": "to advocate for / to champion", "pos": "verb"},
                {"lemma": "arraigar en", "translation": "to take root in", "pos": "verb"},
                {"lemma": "incurrir en", "translation": "to incur / to fall into", "pos": "verb"},
                {"lemma": "coincidir en", "translation": "to agree on / to concur in", "pos": "verb"},
                {"lemma": "disentir de", "translation": "to disagree with / to dissent from", "pos": "verb"},
                {"lemma": "radicar en", "translation": "to lie in / to be based on", "pos": "verb"},
                {"lemma": "supeditar a", "translation": "to subordinate to / to condition upon", "pos": "verb"}
            ]
        },
        "b2-uruguay-01": {
            "id": "vocab.b2.uruguay.01",
            "lesson": "b2-uruguay-01",
            "title": "El batllismo y el Estado de bienestar",
            "words": [
                {"lemma": "batllismo", "translation": "Batllism (Uruguayan social reformism)", "pos": "noun"},
                {"lemma": "laicidad", "translation": "secularism / lay statehood", "pos": "noun"},
                {"lemma": "secularización", "translation": "secularization", "pos": "noun"},
                {"lemma": "vanguardia", "translation": "vanguard / forefront", "pos": "noun"},
                {"lemma": "estatización", "translation": "state nationalization", "pos": "noun"},
                {"lemma": "reformismo", "translation": "reformism", "pos": "noun"},
                {"lemma": "proteccionismo", "translation": "protectionism", "pos": "noun"},
                {"lemma": "institucionalidad", "translation": "institutional framework", "pos": "noun"},
                {"lemma": "vareliano", "translation": "Varelian (pertaining to Jose Pedro Varela)", "pos": "adjective"},
                {"lemma": "cogobierno", "translation": "co-governance (in universities)", "pos": "noun"}
            ]
        },
        "b2-uruguay-02": {
            "id": "vocab.b2.uruguay.02",
            "lesson": "b2-uruguay-02",
            "title": "Candombe, comparsas y el Barrio Sur",
            "words": [
                {"lemma": "candombe", "translation": "candombe rhythm and culture", "pos": "noun"},
                {"lemma": "comparsa", "translation": "carnival drum and dance troupe", "pos": "noun"},
                {"lemma": "tamborilero", "translation": "drummer", "pos": "noun"},
                {"lemma": "conventillo", "translation": "tenement house / communal courtyard", "pos": "noun"},
                {"lemma": "lonja", "translation": "drum skin / leather head", "pos": "noun"},
                {"lemma": "repique", "translation": "repique (high-pitched solo drum)", "pos": "noun"},
                {"lemma": "chico", "translation": "chico drum (metronomic high drum)", "pos": "noun"},
                {"lemma": "piano", "translation": "piano drum (deep bass drum)", "pos": "noun"},
                {"lemma": "ancestralidad", "translation": "ancestral heritage", "pos": "noun"},
                {"lemma": "llamada", "translation": "Llamadas parade (drum call)", "pos": "noun"}
            ]
        },
        "b2-uruguay-03": {
            "id": "vocab.b2.uruguay.03",
            "lesson": "b2-uruguay-03",
            "title": "La dictadura y el plebiscito del NO de 1980",
            "words": [
                {"lemma": "plebiscito", "translation": "plebiscite / referendum", "pos": "noun"},
                {"lemma": "disolución", "translation": "dissolution", "pos": "noun"},
                {"lemma": "insurgencia", "translation": "insurgency", "pos": "noun"},
                {"lemma": "clandestinidad", "translation": "clandestinity / secrecy", "pos": "noun"},
                {"lemma": "proscripción", "translation": "banning / proscription", "pos": "noun"},
                {"lemma": "consenso", "translation": "consensus", "pos": "noun"},
                {"lemma": "penitenciaría", "translation": "penitentiary / prison", "pos": "noun"},
                {"lemma": "transición", "translation": "transition", "pos": "noun"},
                {"lemma": "resistencia", "translation": "resistance", "pos": "noun"},
                {"lemma": "escrutinio", "translation": "scrutiny / ballot count", "pos": "noun"}
            ]
        },
        "b2-uruguay-04": {
            "id": "vocab.b2.uruguay.04",
            "lesson": "b2-uruguay-04",
            "title": "Vanguardia de derechos y agenda verde",
            "words": [
                {"lemma": "descarbonización", "translation": "decarbonization", "pos": "noun"},
                {"lemma": "matriz", "translation": "matrix / structural grid", "pos": "noun"},
                {"lemma": "regulación", "translation": "regulation", "pos": "noun"},
                {"lemma": "sostenibilidad", "translation": "sustainability", "pos": "noun"},
                {"lemma": "trazabilidad", "translation": "traceability", "pos": "noun"},
                {"lemma": "cooperativa", "translation": "cooperative", "pos": "noun"},
                {"lemma": "fotovoltaico", "translation": "photovoltaic / solar", "pos": "adjective"},
                {"lemma": "autocultivo", "translation": "home cultivation", "pos": "noun"},
                {"lemma": "alfabetización", "translation": "literacy / learning", "pos": "noun"},
                {"lemma": "biomasa", "translation": "biomass", "pos": "noun"}
            ]
        },
        "b2-uruguay-05": {
            "id": "vocab.b2.uruguay.05",
            "lesson": "b2-uruguay-05",
            "title": "Montevideo, la rambla y la convivencia",
            "words": [
                {"lemma": "rambla", "translation": "coastal promenade (Rambla)", "pos": "noun"},
                {"lemma": "termo", "translation": "thermos flask", "pos": "noun"},
                {"lemma": "cebar", "translation": "to brew / to pour mate", "pos": "verb"},
                {"lemma": "oriental", "translation": "Uruguayan / from the Eastern Bank", "pos": "adjective"},
                {"lemma": "tablado", "translation": "carnival neighborhood stage", "pos": "noun"},
                {"lemma": "murga", "translation": "murga (musical theater troupe)", "pos": "noun"},
                {"lemma": "sosiego", "translation": "tranquility / serenity / calm", "pos": "noun"},
                {"lemma": "convivencia", "translation": "coexistence / civility", "pos": "noun"},
                {"lemma": "cuplé", "translation": "couplet / satirical theatrical song", "pos": "noun"},
                {"lemma": "llaneza", "translation": "plainness / unpretentiousness", "pos": "noun"}
            ]
        }
    }

    for stem, vdata in vocab_files.items():
        write_json(f"vocabulary/b2/{stem}-voc.json", vdata)

    # 4. Grammar Files (10 files) - ROOT: only id, title, sections
    grammar_data = {
        "b2-27-01-a": {
            "id": "grammar.b2.27.01.locuciones-causa-origen",
            "title": "Locuciones prepositivas de causa y origen: a raíz de, en virtud de, con motivo de",
            "sections": [
                {
                    "type": "text",
                    "content": "En la prosa formal, analítica y jurídica del nivel B2, las causas no se limitan a conjunciones simples como *porque* o *ya que*. Las **locuciones prepositivas de causa y origen** permiten precisar con elegancia el fundamento institucional, la coyuntura desencadenante o el marco normativo que origina un acontecimiento.\n\n* **A raíz de**: Señala el origen temporal y causal inmediato de un hecho (equivalente a *como consecuencia directa de* o *a partir de*).\n* **En virtud de**: Expresa la causa formal, la legitimidad jurídica o la potestad en la que se fundamenta una acción (equivalente a *con base en* o *por la fuerza de*).\n* **Con motivo de**: Indica la ocasión o el acontecimiento motivador que propicia un evento (equivalente a *en conmemoración de* o *con ocasión de*)."
                },
                {
                    "type": "table",
                    "title": "Usos de locuciones causales y de origen",
                    "rows": [
                        ["A raíz de la crisis bancaria, el Parlamento aprobó una estricta regulación financiera.", "Following the banking crisis, Parliament approved strict financial regulation."],
                        ["En virtud de las atribuciones constitucionales, el presidente promulgó la ley de laicidad.", "By virtue of constitutional powers, the president promulgated the secularism law."],
                        ["Con motivo del bicentenario de la independencia, se inauguraron parques eólicos en el interior.", "On the occasion of the bicentennial of independence, wind farms were inaugurated in the interior."],
                        ["A raíz de los reclamos sindicales, se instituyó la jornada laboral de ocho horas.", "As a direct result of union demands, the eight-hour workday was instituted."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*En virtud de* rige siempre sustantivos o sintagmas nominales de carácter abstracto o normativo (*en virtud de la ley*, *en virtud de sus méritos*), mientras que *a raíz de* suele vincularse a hechos fácticos o crisis coyunturales."
                }
            ]
        },
        "b2-27-02-a": {
            "id": "grammar.b2.27.02.locuciones-conformidad-criterio",
            "title": "Locuciones prepositivas de conformidad y criterio: conforme a, de acuerdo con, con arreglo a, a tenor de",
            "sections": [
                {
                    "type": "text",
                    "content": "Para estructurar argumentaciones rigurosas, dictámenes institucionales y análisis comparados, el español culto recurre a locuciones que expresan conformidad con una norma, un pacto o una fuente documental autorizada.\n\n* **Conforme a**: Establece adecuación estricta a una norma, directriz o expectativa reglamentaria (*conforme a la ley*, *conforme a derecho*).\n* **De acuerdo con**: Cita una fuente de autoridad o señala consentimiento recíproco (*de acuerdo con los datos*, *de acuerdo con el ministro*).\n* **Con arreglo a**: Enfatiza el cumplimiento metódico y ordenado de un procedimiento prescrito (*con arreglo a las ordenanzas*).\n* **A tenor de**: Introduce una valoración basada en el contenido literal o el espíritu de un texto o testimonio (*a tenor de lo dispuesto*, *a tenor de sus palabras*)."
                },
                {
                    "type": "table",
                    "title": "Modelos de conformidad y criterio normativo",
                    "rows": [
                        ["El divorcio por la sola voluntad de la mujer se tramitó conforme a la legislación civil pionera.", "Divorce by the sole will of the woman was processed in accordance with pioneering civil legislation."],
                        ["De acuerdo con el informe de la universidad, la matriz energética es plenamente renovable.", "According to the university report, the energy matrix is fully renewable."],
                        ["Las compensaciones a los trabajadores se abonaron con arreglo a los estatutos vigentes.", "Worker compensations were paid in compliance with the current statutes."],
                        ["A tenor de los resultados del plebiscito, la ciudadanía rechazó el proyecto autoritario.", "In light of the plebiscite results, the citizenry rejected the authoritarian project."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Evite la incorrección ultraculta de acuerdo a cuando se refiera a personas o normas en prosa formal; la norma culta panhispánica prefiere invariablemente *de acuerdo con* o *conforme a*."
                }
            ]
        },
        "b2-27-03-a": {
            "id": "grammar.b2.27.03.locuciones-finalidad-sacrificio",
            "title": "Locuciones prepositivas de finalidad y sacrificio: en aras de, con miras a, a costa de, en pos de",
            "sections": [
                {
                    "type": "text",
                    "content": "El discurso político, ético y filosófico del Cono Sur emplea con frecuencia locuciones que sopesan el fin perseguido frente al costo humano, social o material requerido para alcanzarlo.\n\n* **En aras de**: Expresa una subordinación deliberada o un sacrificio noble en favor de un bien superior considerado digno de veneración (*en aras de la paz*, *en aras del consenso*).\n* **Con miras a**: Señala una orientación estratégica o un propósito planificado a mediano y largo plazo (*con miras a modernizar el país*).\n* **A costa de**: Expresa perjuicio, merma o sacrificio gravoso asumido para lograr un resultado (*a costa de su propia salud*, *a costa de las libertades*).\n* **En pos de**: Manifiesta un anhelo idealista, una búsqueda perseverante o un movimiento hacia una meta sublime (*en pos de la justicia*)."
                },
                {
                    "type": "table",
                    "title": "Finalidad, estrategia y balance de costos",
                    "rows": [
                        ["Los partidos tradicionales postergaron sus rencillas en aras de la gobernabilidad democrática.", "Traditional parties postponed their quarrels for the sake of democratic governability."],
                        ["Se invirtió fuertemente en educación pública con miras a reducir las brechas sociales.", "Heavy investment was made in public education with a view to reducing social gaps."],
                        ["La junta militar intentó imponer estabilidad macroeconómica a costa del terror y la censura.", "The military junta attempted to impose macroeconomic stability at the cost of terror and censorship."],
                        ["Las organizaciones de derechos humanos marcharon en pos de la verdad y la memoria colectiva.", "Human rights organizations marched in pursuit of truth and collective memory."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*En aras de* exige siempre una noción valorada positivamente como destino del sacrificio (*en aras de la concordia*, jamás en aras de la inflación)."
                }
            ]
        },
        "b2-27-04-a": {
            "id": "grammar.b2.27.04.locuciones-pretexto-salvedad",
            "title": "Locuciones prepositivas de pretexto y salvedad: so pretexto de, a juicio de, sin perjuicio de, al margen de",
            "sections": [
                {
                    "type": "text",
                    "content": "Para matizar afirmaciones, denunciar pretextos espurios o formular reservas jurídicas precisas, el registro B2 avanzado se vale de locuciones de delimitación y excepción.\n\n* **So pretexto de**: Denuncia una justificación aparente o falaz utilizada para encubrir la verdadera motivación (*so pretexto de seguridad nacional*).\n* **A juicio de**: Introduce el criterio pericial, doctrinal o subjetivo de una autoridad consultada (*a juicio de los juristas*).\n* **Sin perjuicio de**: Establece una salvedad que preserva intacto otro derecho, disposición o competencia complementaria (*sin perjuicio de las sanciones penales*).\n* **Al margen de**: Delimita el campo de análisis dejando de lado elementos secundarios o periféricos (*al margen de consideraciones partidistas*)."
                },
                {
                    "type": "table",
                    "title": "Delimitación, reservas y denuncias argumentativas",
                    "rows": [
                        ["So pretexto de combatir el caos social, la dictadura suprimió las libertades individuales.", "Under the pretext of fighting social chaos, the dictatorship suppressed individual liberties."],
                        ["A juicio del comité asesor, el plan de energía eólica superó todas las expectativas.", "In the advisory committee's opinion, the wind energy plan exceeded all expectations."],
                        ["Se promulgó el estatuto laboral, sin perjuicio de futuras mejoras acordadas en paritarias.", "The labor statute was enacted, without prejudice to future improvements agreed upon in collective bargaining."],
                        ["Al margen de su filiación política, los ciudadanos acudieron a votar por la defensa republicana.", "Regardless of their political affiliation, citizens turned out to vote for republican defense."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "La preposición arcaica *so* se conserva casi exclusivamente fosilizada en locuciones como *so pretexto de* y *so pena de*. No admite intercalar artículos (*so el pretexto* es incorrecto)."
                }
            ]
        },
        "b2-27-05-a": {
            "id": "grammar.b2.27.05.regimen-verbos-avanzados",
            "title": "Régimen preposicional de verbos analíticos avanzados: estribar en, derivar en, versar sobre, abogar por",
            "sections": [
                {
                    "type": "text",
                    "content": "El dominio del estilo ensayístico y del debate público en América Latina requiere precisión en el régimen preposicional obligatorio que demandan ciertos verbos de alta densidad conceptual. Modificar la preposición altera o destruye el sentido oracional.\n\n* **Estribar en**: Radicar o fundarse esencialmente en algo (*el éxito estriba en el diálogo constante*).\n* **Derivar en**: Desembocar o transformarse en una consecuencia determinada (*la huelga derivó en la caída del gabinete*).\n* **Versar sobre**: Tratar o tener como materia temática un asunto (*el debate versó sobre la despenalización*).\n* **Abogar por**: Defender activamente una causa, principio o derecho colectivo (*Uruguay aboga por el multilateralismo*).\n* **Supeditar a**: Condicionar la validez o ejecución de un acto a una circunstancia previa (*supeditaron la inversión al aval ambiental*)."
                },
                {
                    "type": "table",
                    "title": "Verbos analíticos y sus regímenes preposicionales",
                    "rows": [
                        ["La singularidad de la democracia uruguaya estriba en la cercanía entre gobernantes y ciudadanos.", "The uniqueness of Uruguayan democracy lies in the closeness between leaders and citizens."],
                        ["El debate cívico sobre la regulación del cannabis derivó en un modelo internacional de salud pública.", "The civic debate on cannabis regulation resulted in an international public health model."],
                        ["Las sesiones parlamentarias versaron sobre la ampliación de licencias parentales compartidas.", "Parliamentary sessions dealt with the expansion of shared parental leaves."],
                        ["Los activistas y juristas abogan por la preservación de los archivos de la memoria histórica.", "Activists and legal experts advocate for the preservation of historical memory archives."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Confundir *derivar en* (desembocar en) con *derivar de* (provenir de) es un error frecuente. Observe la dirección: *la propuesta deriva de un estudio técnico* (origen), pero *el desacuerdo derivó en una consulta popular* (resultado)."
                }
            ]
        },
        "b2-uruguay-01-a": {
            "id": "grammar.b2.uruguay.01.batllismo-causalidad",
            "title": "El batllismo y el Estado de bienestar: Causalidad y fundamentación con locuciones prepositivas",
            "sections": [
                {
                    "type": "text",
                    "content": "A comienzos del siglo XX, el presidente José Batlle y Ordóñez impulsó una profunda transformación que convirtió a Uruguay en un Estado de bienestar modelo y en la sociedad más secularizada de América Latina. Analizar este proceso histórico demanda el empleo de locuciones causales y normativas precisas como *en virtud de*, *a raíz de* y *con motivo de*.\n\nEl batllismo nacionalizó servicios estratégicos (bancos, seguros, ferrocarriles y energía eléctrica) y estableció la jornada laboral de ocho horas en 1915, mucho antes que la mayoría de los países europeos. Asimismo, en virtud de una concepción laica intransigente, se secularizó el calendario oficial: la Semana Santa pasó a denominarse oficialmente *Semana de Turismo*, la Navidad fue declarada *Día de la Familia*, y los crucifijos fueron retirados de los hospitales públicos."
                },
                {
                    "type": "table",
                    "title": "Locuciones causales aplicadas a la historia institucional uruguaya",
                    "rows": [
                        ["En virtud de las leyes de 1913, Uruguay consagró el divorcio por la sola voluntad de la mujer.", "By virtue of the laws of 1913, Uruguay enshrined divorce by the woman's sole will."],
                        ["A raíz de la visión laicista del Estado, se eliminó la enseñanza religiosa obligatoria en escuelas públicas.", "Following the state's secular vision, compulsory religious instruction in public schools was eliminated."],
                        ["Con motivo de la celebración del centenario en 1930, se construyó el Estadio Centenario en Montevideo.", "On the occasion of the centenary celebration in 1930, the Centenario Stadium was built in Montevideo."],
                        ["En virtud del pacto social batllista, las clases medias accedieron a una universidad pública gratuita y cogobernada.", "By virtue of the Batllist social pact, the middle classes accessed a free, co-governed public university."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Utilice *en virtud de* cuando justifique una medida que se apoya en una facultad legal, un decreto o un principio ético consagrado en la arquitectura institucional."
                }
            ]
        },
        "b2-uruguay-02-a": {
            "id": "grammar.b2.uruguay.02.candombe-finalidad",
            "title": "Candombe, comparsas y resistencia comunitaria: Locuciones de finalidad y sacrificio",
            "sections": [
                {
                    "type": "text",
                    "content": "El candombe uruguayo, declarado Patrimonio Cultural Inmaterial de la Humanidad por la UNESCO, es el latido sonoro y espiritual de la comunidad afrouruguaya. Forjado en los conventillos de Barrio Sur y Palermo (como el célebre Medio Mundo y Ansina), el candombe representa una conmovedora historia de resiliencia cultural en la que el tambor fue el instrumento de salvaguarda comunitaria.\n\nPara expresar la entrega de los tamborileros y la defensa de la memoria ancestral frente al racismo estructural y los desalojos dictatoriales, se utilizan locuciones de finalidad y sacrificio como *en aras de*, *en pos de* y *a costa de*."
                },
                {
                    "type": "table",
                    "title": "Locuciones de finalidad y sacrificio en la cultura del candombe",
                    "rows": [
                        ["Las familias afrodescendientes preservaron sus toques sagrados en aras de la identidad comunitaria.", "Afro-descendant families preserved their sacred rhythms for the sake of community identity."],
                        ["Los tamborileros marcharon por la calle Isla de Flores en pos del reconocimiento de sus raíces.", "Drummers marched down Isla de Flores Street in pursuit of recognition for their roots."],
                        ["La especulación inmobiliaria demolió conventillos históricos a costa del desarraigo barrial.", "Real estate speculation demolished historic tenement houses at the cost of neighborhood uprooting."],
                        ["Las comparsas ensayan todo el año con miras a deslumbrar en el concurso de las Llamadas.", "The comparsas rehearse all year with a view to dazzling in the Llamadas contest."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "La cuerda de candombe consta de tres tambores fundamentales afinados mediante calor de leña: el *piano* (grave y conductor), el *chico* (agudo y métrico) y el *repique* (improvisador y sincopado)."
                }
            ]
        },
        "b2-uruguay-03-a": {
            "id": "grammar.b2.uruguay.03.plebiscito-pretexto",
            "title": "El plebiscito de 1980 y la resistencia cívica: Locuciones de pretexto y delimitación",
            "sections": [
                {
                    "type": "text",
                    "content": "Durante la dictadura cívico-militar que gobernó Uruguay entre 1973 y 1985, el régimen intentó legitimar su permanencia indefinida mediante un plebiscito constitucional en noviembre de 1980. Convocado en un clima de censura férrea, prisión masiva de opositores y proscripción política de los principales líderes, los militares confiaban en obtener una victoria fácil.\n\nSin embargo, el pueblo uruguayo protagonizó una hazaña cívica sin precedentes: el NO triunfó con casi el 57% de los sufragios, asestando un golpe mortal al proyecto dictatorial. Para narrar este proceso con rigor analítico, es indispensable emplear locuciones de pretexto y salvedad como *so pretexto de*, *a juicio de*, *sin perjuicio de* y *al margen de*."
                },
                {
                    "type": "table",
                    "title": "Pretexto, salvaguarda y criterio cívico en el relato histórico",
                    "rows": [
                        ["So pretexto de salvaguardar la soberanía, la dictadura intervino la Universidad de la República.", "Under the pretext of safeguarding sovereignty, the dictatorship intervened the University of the Republic."],
                        ["A juicio de los analistas internacionales, la derrota militar en las urnas selló el fin de la dictadura.", "In international analysts' opinion, the military defeat at the ballot box sealed the end of the dictatorship."],
                        ["Los ciudadanos votaron con valentía, sin perjuicio de las amenazas veladas del mando militar.", "Citizens voted with courage, without prejudice to the veiled threats of the military command."],
                        ["Al margen del cerco mediático oficialista, las revistas clandestinas difundieron las razones del NO.", "Outside of the pro-government media blackout, clandestine magazines spread the reasons for the NO."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerde que *sin perjuicio de* indica que una condición o derecho se mantiene plenamente válido a pesar de lo que se exponga a continuación (*sin perjuicio de las restricciones*, se mantuvo el espíritu democrático)."
                }
            ]
        },
        "b2-uruguay-04-a": {
            "id": "grammar.b2.uruguay.04.vanguardia-conformidad",
            "title": "Vanguardia de derechos y transición verde: Locuciones de conformidad y criterio",
            "sections": [
                {
                    "type": "text",
                    "content": "En el siglo XXI, Uruguay consolidó su reputación como laboratorio de vanguardia social y ambiental a escala global. Fue el primer país del planeta en regular integralmente el mercado del cannabis con fines médicos, industriales y recreativos (2013), aprobó el matrimonio igualitario y despenalizó la interrupción voluntaria del embarazo, todo ello sustentado en un amplio debate parlamentario y ciudadano.\n\nEn paralelo, el país transformó radicalmente su matriz energética: hoy más del 95% de su electricidad proviene de fuentes renovables (hidroeléctrica, eólica, biomasa y solar). Describir estos hitos contemporáneos requiere dominar locuciones de conformidad como *conforme a*, *de acuerdo con*, *con arreglo a* y *a tenor de*."
                },
                {
                    "type": "table",
                    "title": "Conformidad legal y criterios científicos de vanguardia",
                    "rows": [
                        ["La venta de cannabis en farmacias se organiza conforme a estrictos protocolos sanitarios del IRCCA.", "The sale of cannabis in pharmacies is organized according to strict sanitary protocols of the IRCCA."],
                        ["De acuerdo con los organismos ambientales, la matriz energética uruguaya es un modelo de descarbonización.", "According to environmental agencies, the Uruguayan energy matrix is a model of decarbonization."],
                        ["Las parejas del mismo sexo acceden a la adopción civil con arreglo a la ley de matrimonio igualitario.", "Same-sex couples access civil adoption in compliance with the marriage equality law."],
                        ["A tenor de las mediciones de calidad de vida, Uruguay lidera los índices de desarrollo humano en la región.", "In light of quality of life measurements, Uruguay leads human development indices in the region."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En la prosa técnica y jurídica uruguaya, *con arreglo a* se emplea preferentemente para aludir a ordenanzas técnicas, cálculos arancelarios y protocolos de inspección pública."
                }
            ]
        },
        "b2-uruguay-05-a": {
            "id": "grammar.b2.uruguay.05.rambla-regimen-verbal",
            "title": "Montevideo, la rambla y la identidad oriental: Regímenes preposicionales de convivencia",
            "sections": [
                {
                    "type": "text",
                    "content": "La vida cotidiana en Uruguay se caracteriza por un ritmo sosegado, una escala humana y un profundo apego a la convivencia republicana. El símbolo supremo de esta idiosincrasia es el mate amargo, llevado con el termo bajo el brazo en cualquier ámbito: en el trabajo, en la parada del autobús o caminando por los más de veinte kilómetros de la rambla de Montevideo frente a las aguas mansas del Río de la Plata.\n\nPara articular reflexiones ensayísticas sobre la sociabilidad uruguaya, las murgas del carnaval más largo del mundo y la modestia de sus líderes cívicos, se emplean verbos de régimen preposicional obligatorio como *estribar en*, *versar sobre*, *abogar por* y *derivar en*."
                },
                {
                    "type": "table",
                    "title": "Verbos de régimen preposicional en el ensayo sociológico",
                    "rows": [
                        ["El encanto de Montevideo estriba en la armonía entre su rambla abierta y su arquitectura histórica.", "Montevideo's charm lies in the harmony between its open promenade and historic architecture."],
                        ["Los cuplés de las murgas barriales versan sobre las contradicciones de la política cotidiana.", "The couplets of neighborhood murgas deal with the contradictions of daily politics."],
                        ["La ciudadanía oriental aboga por una sociedad tolerante donde nadie sea más que nadie.", "The Uruguayan citizenry advocates for a tolerant society where no one is above anyone else."],
                        ["Las discusiones de café sobre fútbol y política suelen derivar en un apretón de manos fraterno.", "Cafe discussions about soccer and politics usually result in a fraternal handshake."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "La expresión popular uruguaya naides es más que naides sintetiza el credo republicano y antiautoritario atribuido a José Gervasio Artigas, prócer de la independencia oriental."
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}-gr.json", gdata)

    # 5. Stories (8 files) - EXACT story.schema.json FORMAT & STRICT 650-825 WORDS!

    story_core_27 = {
        "id": "b2-27",
        "title": "Anaconda: La rebelión de la selva y el congreso de las víboras",
        "level": "B2",
        "lesson": 27,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Una adaptación literaria de 'Anaconda' (1921), la obra cumbre del escritor uruguayo Horacio Quiroga: en la espesura del Alto Paraná, las serpientes convocan a un congreso de emergencia ante el avance implacable del ser humano con sus expediciones científicas y sueros antiofídicos, debatiendo entre la guerra abierta o la tregua en un conmovedor choque entre instinto, cálculo y destino.",
        "characters": [
            "Lanceolata (Yarará)",
            "Anaconda",
            "Cruzada",
            "Coralina",
            "Los hombres del campamento"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En lo más recóndito de la selva misionera, a orillas de las aguas rojizas del Alto Paraná, una inquietud desconocida quebró el silencio milenario de las criaturas rastreras. El hombre, aquel enemigo implacable y bípedo al que la fauna veneraba con pavor reverente, había instalado un campamento científico en el borde mismo de los esteros. No se trataba de cazadores furtivos en pos de pieles o plumas, sino de médicos y naturalistas equipados con carpas de lona blanca, caballos inmunes y recipientes de vidrio destinados a la extracción masiva de veneno para elaborar sueros antiofídicos. A raíz de este avance metódico que amenazaba con aniquilar a las especies autóctonas, Lanceolata —una yarará soberbia de metro y medio, rápida como el rayo y consciente de su estirpe venenosa— convocó con urgencia a todas las familias de reptiles a un congreso solemne en la caverna del peñasco."
            },
            {
                "type": "narration",
                "text": "Conforme a los viejos códigos de la selva que proscribían las querellas intestinas durante las treguas mayores, acudieron a la cita las más temibles habitantes del sotobosque: las yararacusús de escamas oscuras, las víboras de la cruz de mirada fría, las pequeñas corales con sus anillos concéntricos brillantes y, finalmente, deslizándose con majestuosa lentitud por entre las lianas, Anaconda, la gigantesca constrictora de diez metros que no poseía veneno pero gobernaba los ríos en virtud de su fuerza muscular descomunal. Las discusiones iniciales versaron sobre la estrategia que debía adoptarse frente a los invasores: mientras Lanceolata abogaba por una ofensiva frontal e inmediata para diezmar a los científicos en sus catres antes del amanecer, Anaconda aconsejó prudencia táctica, advirtiendo que el poder del hombre estribaba en su cerebro coordinado y en sus artificios de fuego contra los cuales la ferocidad ciega resultaba inútil."
            },
            {
                "type": "narration",
                "text": "'¿Acaso hemos de entregarnos sin combatir en aras de una sumisión indigna?', increpó Lanceolata irguiendo su cuello triangular en señal de desafío. 'So pretexto de investigar nuestras costumbres, esos seres de dos patas nos capturan con horquillas de hierro, encierran a nuestras hermanas en cajones estrechos y nos ordeñan las glándulas como si fuéramos ganado servil. Debemos atacarlos esta misma noche, al margen de cualquier temor supersticioso'. Las víboras venenosas ovacionaron el plan de la yarará, dispuestas a inmolarse si fuera preciso con miras a expulsar a la colonia humana. Anaconda, sin embargo, contempló la asamblea con melancolía filosófica; comprendía que el triunfo efímero de una picadura nocturna derivaría forzosamente en una represalia implacable: el desmonte con fuego y la deforestación total de su hábitat primitivo a costa de la vida de toda la comunidad vegetal y animal."
            },
            {
                "type": "narration",
                "text": "Aquella misma madrugada, la vanguardia reptiliana avanzó silenciosa por los matorrales empapados de rocío, infiltrándose bajo las lonas del campamento dormido. Cruzada y Coralina lograron penetrar en las habitaciones de madera, buscando los tobillos desnudos de los científicos. Pero el hombre, prevenido por la experiencia zoológica, había colocado telas metálicas en las aberturas y lámparas de carburo que iluminaban los senderos. Al sonar la alarma, estallaron los disparos de escopeta y los garrotazos certeros. Lanceolata combatió con desesperada valentía, mordiendo repetidamente las polainas de cuero endurecido de los peones hasta que un impacto fatal le quebró el espinazo. Las pocas serpientes sobrevivientes huyeron despavoridas hacia el río, dejando tras de sí un reguero de desolación que confirmó la profecía de Anaconda."
            },
            {
                "type": "narration",
                "text": "Al clarear el día, Anaconda decidió presentarse sola ante el campamento en un postrer acto de dignidad soberana, buscando atraer la atención de los hombres para permitir que los restos dispersos del congreso alcanzaran las profundidades inexpugnables del monte. Enredada valientemente en las empalizadas del corral, la gran serpiente asfixió a dos perros de guardia antes de ser acorralada con lazos corredizos y barras de hierro. Los investigadores la contemplaron con asombro reverente, reconociendo en la anatomía colosal de la bestia la belleza sublime de una naturaleza que se negaba a doblegarse ante el imperio de las máquinas y el desmonte industrial."
            },
            {
                "type": "narration",
                "text": "Encerrada en una jaula espaciosa a la espera de su traslado a los laboratorios de Buenos Aires, Anaconda observó por última vez el cauce turbulento del río Paraná y las copas infinitas de la selva virgen donde había reinado libremente. Comprendió entonces que la tragedia de las criaturas del monte no estribaba en la falta de coraje o de veneno letal, sino en la inexorable marcha de una civilización que devoraba el misterio del mundo silvestre en pos del dominio técnico. Y con la mirada fija en el horizonte verde, cerró los ojos con el sosiego aristocrático de los reyes vencidos que conservan intacto su señorío interior."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál es la causa primordial que motiva a Lanceolata a convocar al congreso de las serpientes?",
                        "options": [
                            "La escasez imprevista de alimento en las orillas del río Paraná.",
                            "La invasión de científicos humanos que capturan víboras para elaborar sueros antiofídicos.",
                            "Una disputa territorial ancestral entre las víboras venenosas y las constrictoras.",
                            "La crecida destructiva de las aguas del río que anegó las madrigueras."
                        ],
                        "correctIndex": 1,
                        "explanation": "El campamento científico representa una amenaza sistemática que extrae veneno y altera el equilibrio de la selva."
                    },
                    {
                        "question": "¿En qué estriba la diferencia fundamental de postura entre Lanceolata y Anaconda?",
                        "options": [
                            "Lanceolata aboga por un ataque frontal inmediato, mientras Anaconda advierte sobre las fatales consecuencias de la represalia humana.",
                            "Lanceolata propone aliarse con los hombres, mientras Anaconda desea destruir el campamento con sus músculos.",
                            "Lanceolata rehúsa combatir por miedo al agua, mientras Anaconda exige cruzar el río a nado.",
                            "Lanceolata quiere huir a las montañas, mientras Anaconda insiste en esconderse en las carpas humanas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Lanceolata representa la agresividad instintiva del veneno, mientras Anaconda aporta una lucidez estratégica que anticipa el desmonte."
                    },
                    {
                        "question": "¿Qué reflexión final sobre la civilización y la selva encarna el destino de Anaconda al final del relato?",
                        "options": [
                            "Que las herramientas humanas son inferiores al poder de las fieras salvajes.",
                            "Que la modernidad y el avance tecnológico avanzan inexorablemente sobre los misterios de la naturaleza virgen.",
                            "Que las víboras debieron haber aprendido a hablar para negociar un tratado comercial.",
                            "Que la selva volverá a recuperar sus límites en pocos días sin dejar rastro del hombre."
                        ],
                        "correctIndex": 1,
                        "explanation": "Anaconda asume con dignidad aristocrática la derrota ante una civilización técnica que devora el mundo silvestre."
                    }
                ]
            }
        }
    }

    w_count_classic = count_words(story_core_27)
    print(f"stories/classics/b2/b2-27.json: {w_count_classic} words")
    assert 650 <= w_count_classic <= 825, f"Classic story has {w_count_classic} words (must be 650-825)"
    write_json("stories/classics/b2/b2-27.json", story_core_27)

    # Regional Stories (5 lesson stories + 1 consolidation + 1 library stitched story)
    regional_story_texts = {
        "b2-uruguay-01": [
            "A comienzos del siglo veinte, mientras la mayor parte de las repúblicas hispanoamericanas debatían su destino institucional entre regímenes caudillistas autoritarios, monopolios latifundistas y la tutela hegemónica de la Iglesia católica sobre la vida civil y familiar, la República Oriental del Uruguay protagonizó una singular revolución pacífica de vanguardia institucional. Bajo el liderazgo visionario y reformista de José Batlle y Ordóñez, dos veces presidente de la república (1903–1907 y 1911–1915), el país sentó las bases doctrinarias del 'batllismo': un modelo socialdemócrata y solidario que forjó el primer Estado de bienestar integral del continente americano. A raíz de este impulso democratizador extraordinariamente audaz, Uruguay transformó sus estructuras económicas mediante la nacionalización temprana de servicios y empresas estratégicas en los sectores de la energía eléctrica, los bancos comerciales, las compañías de seguros y las redes de ferrocarriles, impidiendo de forma deliberada que el capital especulativo foráneo subordinara el interés colectivo soberano a sus propios dividendos.",
            "En el plano de las relaciones del trabajo, el reformismo batllista inauguró una legislación social de vanguardia continental al sancionar en noviembre de 1915 la histórica ley de ocho horas de trabajo diario y fijar el descanso semanal obligatorio para los obreros industriales y dependientes de comercio, convirtiendo a los asalariados uruguayos en ciudadanos plenos con tiempo digno para la educación, el descanso y la recreación familiar mucho antes de que conquistas análogas se alcanzaran en la mayoría de los países de Europa occidental. Asimismo, en virtud de un compromiso ético inquebrantable con la emancipación femenina, Uruguay aprobó en 1907 la ley de divorcio civil y, pocos años más tarde en 1913, consagró la histórica figura del divorcio por la sola voluntad de la mujer, un avance jurídico inédito en el derecho comparado global que protegió a miles de ciudadanas del despotismo conyugal sin exigirles la humillante justificación de causales íntimas en tribunales patriarcales.",
            "De manera paralela a estas transformaciones socioeconómicas, Batlle y Ordóñez impulsó un riguroso proceso de secularización institucional que arraigó de manera definitiva en el alma de la sociedad oriental. So pretexto de neutralidad cívica, muchos Estados contemporáneos mantenían fueros eclesiásticos privilegiados; Uruguay, en cambio, separó tajantemente la Iglesia del Estado en su Constitución de 1917, retiró los crucifijos de todos los hospitales públicos y eliminó por completo la enseñanza religiosa en los centros educativos estatales. Con asombrosa audacia pedagógica y simbólica, el calendario oficial sustituyó los nombres devocionales católicos por designaciones cívicas universales: la Semana Santa fue rebautizada oficialmente como 'Semana de Turismo', el Día de la Virgen se transformó en 'Día de las Playas', y la tradicional Navidad pasó a celebrarse formalmente en el registro civil como el 'Día de la Familia'.",
            "La educación pública gratuita, obligatoria y estrictamente laica se erigió en el pilar supremo de la integración comunitaria oriental y en la garantía de la concordia cívica. A través de la reforma escolar inspirada inicialmente por el pedagogo José Pedro Varela en el siglo diecinueve y perfeccionada por los sucesivos gobiernos batllistas, los hijos de los grandes terratenientes acomodados, los descendientes de peones rurales y los hijos de los humildes inmigrantes italianos, españoles y suizos compartieron las mismas aulas públicas vistiendo la emblemática túnica blanca con moña azul sobre el pecho. Esta formidable democratización escolar propició una movilidad social ascendente extraordinaria y consagró a la histórica Universidad de la República (UdelaR) como una institución gratuita, autónoma y cogobernada donde la investigación científica y el pensamiento humanístico florecieron al abrigo de cualquier dogma religioso o imposición autoritaria.",
            "Hoy en día, el legado civilizatorio del batllismo continúa operando como el marco de referencia identitario insustituible sobre el cual la sociedad uruguaya edifica y renueva pacíficamente sus consensos políticos. Si bien los debates contemporáneos versan sobre los nuevos desafíos de la productividad en la era digital, la apertura comercial y la sostenibilidad fiscal del sistema previsional, el principio batllista fundamental según el cual el Estado tiene la obligación moral indeclinable de proteger a los más débiles y asegurar la igualdad de oportunidades se mantiene incólume en la conciencia ciudadana, demostrando que la fe republicana en la justicia distributiva es la más noble y perdurable de las virtudes colectivas orientales."
        ],
        "b2-uruguay-02": [
            "Al caer la tarde en los legendarios barrios montevideanos de Sur y Palermo, cuando el aire costero y salobre refresca las calles adoquinadas cercanas a la rambla, un murmullo sordo de madera y calor anticipa uno de los rituales culturales y espirituales más fascinantes del Cono Sur: el templado de los tambores de candombe. Nacido a finales del siglo dieciocho en el seno de las diversas 'naciones' africanas esclavizadas en la bahía de Montevideo —congoleños, angoleños, bantúes, mozambiqueños y mandingas—, el candombe trascendió el dolor indecible de la opresión colonial y la trata de personas para erigirse en un formidable bastión de resistencia espiritual, alegría comunitaria y afirmación identitaria de la población afrouruguaya, mereciendo su consagración por la UNESCO en 2009 como Patrimonio Cultural Inmaterial de la Humanidad.",
            "El corazón geográfico y afectivo de esta cultura de matriz africana palpitó históricamente en los míticos 'conventillos', aquellas viviendas colectivas de patio central abierto, barandas de madera y habitaciones contiguas donde decenas de familias trabajadoras afrodescendientes compartían la vida cotidiana, las penas y las celebraciones. Espacios legendarios e irrepetibles como el Conventillo Medio Mundo en la calle Cuareim 1080 o el conventillo Ansina en Palermo funcionaron como verdaderas incubadoras artísticas donde las 'abuelas' afrouruguayas preservaron las memorias orales de África y donde los tamborileros crearon el toque polirrítmico sincopado que hoy define a las comparsas. Trágicamente, a fines de los años setenta, la dictadura cívico-militar ordenó el desalojo forzoso y la demolición con topadoras de ambos conventillos so pretexto de higiene urbana y renovación inmobiliaria, dispersando a sus habitantes hacia la periferia en un intento deliberado y clasista de quebrar el tejido social de la comunidad negra.",
            "No obstante la violencia del desarraigo físico y el dolor de la expulsión territorial, el candombe demostró una resiliencia comunitaria indoblegable que ninguna maquinaria castrense pudo sofocar jamás. La orquesta fundamental del candombe está integrada por tres tambores de duelas de madera y lonja de cuero vacuno: el 'piano', el tambor más grande y de sonido más grave que marca el latido del suelo y guía con autoridad el rumbo rítmico; el 'chico', el más pequeño y agudo que sostiene con precisión métrica implacable el pulso acelerado; y el 'repique', el tambor intermedio que dialoga con virtuosismo sincopado improvisando frases, repiqueteos y contratiempos electrizantes. Antes de salir a marchar por el asfalto, los tamborileros encienden pequeñas fogatas con maderas secas en el cordón de la acera para templar las lonjas al calor del fuego vivo, logrando una afinación aguda y resonante que hace vibrar el pecho de quienes asisten al llamado ancestral.",
            "Cada año, en las noches templadas de febrero durante el Carnaval montevideano —reconocido como el más extenso y participativo del planeta entero, con más de cuarenta días ininterrumpidos de festejos—, la ciudad se paraliza ante el majestuoso 'Desfile de las Llamadas'. Decenas de comparsas tradicionales o 'sociedades de negros y lubolos' recorren la histórica calle Isla de Flores al ritmo ensordecedor y magnético de más de dos mil tamborileros marchando al unísono con balanceo cadencioso. El cortejo festivo lo encabezan figuras arquetípicas llenas de sabiduría ancestral: el 'Gramillero', el anciano curandero de barba blanca, levita y bastón que danza con pasitos temblorosos y cura los males con hierbas medicinales; la 'Mama Vieja', matriarca bondadosa de abanico, saya y vestido de volantes que irradia dignidad y protección maternal; el 'Escobero', acróbata sagrado que abre paso al compás con malabares prodigiosos de su escobilla mágica; y las deslumbrantes vedettes y bailarinas que despliegan su sensualidad festiva.",
            "Más allá de su deslumbrante despliegue coreográfico, poético y sonoro en el carnaval, el candombe representa hoy en día un canal irrenunciable de movilización cívica y debate político contra el racismo estructural, la discriminación soterrada y la marginación histórica que aún afecta a los afrodescendientes en el mercado laboral y universitario uruguayo. En cada golpe seco de la madera con el palo y en cada caricia de la palma abierta sobre el parche caliente, las nuevas generaciones de tamborileros renuevan su pacto sagrado con los ancestros esclavizados, demostrando que el candombe no es una pieza arqueológica de museo folclórico, sino un corazón palpitante de dignidad, hermandad y resistencia libertaria que abraza a todo el pueblo oriental en una misma comunión sonora."
        ],
        "b2-uruguay-03": [
            "A finales de la década de 1960, el mítico sosiego republicano de la denominada 'Suiza de América' comenzó a fracturarse de manera alarmante bajo el impacto combinado de un estancamiento económico crónico, una inflación desbocada y la creciente polarización política continental azuzada por las tensiones geopolíticas de la Guerra Fría. La irrupción de la guerrilla urbana del Movimiento de Liberación Nacional (MLN-Tupamaros) y la consiguiente escalada de medidas prontas de seguridad decretadas por el gobierno derivaron en una asfixiante militarización del espacio público. El 27 de junio de 1973, en estrecha connivencia con el propio presidente constitucional Juan María Bordaberry, los altos mandos de las fuerzas armadas disolvieron el Parlamento de la república e instauraron en el Uruguay una feroz y prolongada dictadura cívico-militar que se extendió durante doce oscuros años, quebrando medio siglo ininterrumpido de ejemplar institucionalidad democrática.",
            "La respuesta del combativo movimiento obrero uruguayo ante la consumación del golpe de Estado fue inmediata, unánime y de una valentía cívica ejemplar: la Convención Nacional de Trabajadores (CNT) decretó de inmediato una histórica huelga general con ocupación pacífica de fábricas, refinerías, talleres y centros de estudio que paralizó el país durante quince días heroicos bajo el constante asedio represivo militar. Desarticulada la resistencia civil inicial tras sangrientas persecuciones, la dictadura instauró un régimen de terrorismo de Estado sistemático que convirtió a Uruguay en el país con la mayor cantidad de presos políticos per cápita del mundo entero: uno de cada quinientos ciudadanos pasó por celdas clandestinas de tortura o cárceles militares como el siniestro Penal de Libertad para hombres o Punta de Rieles para mujeres. El plan represivo se coordinó a nivel continental en el marco del criminal Plan Cóndor, secuestrando, torturando y desapareciendo a casi doscientos militantes sociales y políticos orientales.",
            "En noviembre de 1980, envalentonada por el control monopolístico y férreo de los medios de comunicación y por el encarcelamiento, destierro o proscripción política de los principales líderes de la oposición, la junta militar creyó llegado el momento propicio de legitimar su dominio perpetuo mediante una reforma constitucional autoritaria que pretendía subordinar para siempre los poderes civiles a un Consejo de Seguridad Nacional tutelado por generales. Confiados en una victoria aplastante facilitada por la censura, los jerarcas castrenses convocaron a un plebiscito obligatorio el 30 de noviembre de 1980, prohibiendo cualquier campaña opositora en la radio y la televisión abiertas. Sin embargo, en la clandestinidad de los talleres fabriles, en las tertulias familiares en voz baja y a través de publicaciones independientes heroicas, el pueblo uruguayo articuló una resistencia silenciosa pero inquebrantable.",
            "El desenlace del plebiscito constituyó un hito cívico histórico sin precedentes en América Latina: contra todos los pronósticos oficiales y desafiando el miedo paralizante de una década de represión, casi el 57% de los ciudadanos acudió a las urnas para votar valientemente por la papeleta del NO, propinando una derrota humillante e inapelable al proyecto constitucional totalitario de las fuerzas armadas. Aquel NO rotundo y pacífico resonó en el continente entero como la demostración palmaria de que la vocación democrática de una ciudadanía culta y educada no se compra con propaganda ni se apaga con intimidaciones castrenses. La derrota en las urnas forzó a los mandos militares a abrir un proceso de transición negociada que culminó en las elecciones generales de noviembre de 1984 y en la definitiva restitución del Estado de derecho el 1 de marzo de 1985 con la asunción del presidente Julio María Sanguinetti.",
            "El plebiscito de 1980 y la ejemplar salida democrática consolidaron en el imaginario colectivo oriental la convicción inquebrantable de que el sufragio universal libre y las urnas transparentes son el escudo supremo de la república. A pesar de los intensos debates posteriores sobre la ley de caducidad de la pretensión punitiva del Estado y las dolorosas deudas pendientes en la identificación de los restos de los detenidos desaparecidos —reivindicada incansablemente cada 20 de mayo en la multitudinaria Marcha del Silencio por la avenida 18 de Julio en Montevideo—, Uruguay demostró al mundo entero que la memoria cívica, la perseverancia pacífica y el pacto constitucional democrático son virtudes capaces de doblegar a la más cerrada de las tiranías militares."
        ],
        "b2-uruguay-04": [
            "En las primeras décadas del siglo veintiuno, mientras buena parte del escenario internacional transitaba por el auge de discursos polarizantes, tensiones sociales y retrocesos en materias civiles, Uruguay sorprendió nuevamente a la comunidad internacional al consagrarse como un audaz laboratorio social y un referente mundial de vanguardia en derechos ciudadanos, inclusión digital y sostenibilidad ecológica. Fiel a su centenaria tradición batllista de secularismo institucional, respeto irrestricto a las libertades y protección a las minorías postergadas, el país aprobó entre 2012 y 2013 un paquete legislativo de transformación humanista integral: la despenalización de la interrupción voluntaria del embarazo, la sanción del matrimonio igualitario con derecho pleno de adopción para parejas del mismo sexo, y la ley pionera de regulación estatal integral del mercado de cannabis con fines medicinales, industriales y recreativos.",
            "La histórica regulación del cannabis, impulsada decididamente durante la presidencia del veterano líder social y exguerrillero José 'Pepe' Mujica, rompió de cuajo con el paradigma punitivo y fracasado de la llamada 'guerra contra las drogas' para adoptar un enfoque pragmático de salud pública, derechos individuales y combate inteligente al crimen organizado. Conforme a esta normativa estricta tutelada y fiscalizada por el Instituto de Regulación y Control del Cannabis (IRCCA), el Estado uruguayo autorizó tres vías legales de acceso controlado a la sustancia: el autocultivo doméstico registrado de hasta seis plantas hembras por hogar, los clubes cannábicos cooperativos de membresía limitada y la adquisición fiscalizada de variedades estandarizadas en farmacias comerciales habilitadas. Este modelo pionero atrajo el interés de científicos, sociólogos, criminólogos y gobiernos de todos los continentes, demostrando con hechos empíricos que arrebatar el negocio ilícito al narcotráfico mediante la regulación estatal reduce la violencia urbana, desmantela redes clandestinas y garantiza la trazabilidad sanitaria de los consumidores.",
            "De manera simultánea a esta vanguardia en libertades individuales y derechos civiles, Uruguay ejecutó una de las transformaciones ambientales más espectaculares y veloces del planeta: la descarbonización casi total de su matriz eléctrica nacional. En el lapso de apenas una década, gracias a un consenso multipartidario de largo plazo suscrito en 2010 que trascendió las disputas partidarias coyunturales y los cambios de signo político en el gobierno, el país invirtió fuertemente en infraestructura renovable, instalando decenas de parques eólicos modernos a lo largo de sus cuchillas serranas, plantas solares fotovoltaicas y centrales térmicas alimentadas con biomasa forestal e hidroeléctrica. Como resultado de esta política pública visionaria, Uruguay genera hoy de forma sostenida entre el 95% y el 98% de su electricidad a partir de fuentes limpias y renovables, convirtiéndose en el segundo país del mundo con mayor penetración relativa de energía eólica en su red eléctrica y exportando excedentes limpios a países vecinos como Argentina y Brasil.",
            "En el ámbito pedagógico y de inclusión digital, el país lideró una experiencia de alfabetización tecnológica escolar inédita en el mundo: el Plan Ceibal, instaurado en 2007 durante el primer mandato presidencial del oncólogo Tabaré Vázquez. Inspirado en el principio universalista de que la equidad social exige acceso democrático a las herramientas del conocimiento, el Estado uruguayo entregó gratuitamente una computadora portátil con conexión inalámbrica a internet a cada estudiante y docente de todas las escuelas públicas del territorio nacional. Esta temprana alfabetización digital universal cerró brechas socioeconómicas históricas entre la capital y el interior rural, permitiendo al sistema educativo uruguayo responder con asombrosa solvencia pedagógica a crisis sanitarias globales y posicionando al país como un polo de innovación y exportación de software de alta gama en el Cono Sur.",
            "Esta formidable confluencia entre derechos cívicos avanzados, transición energética limpia y equidad digital confirma que la escala territorial y demográfica reducida de Uruguay —con apenas tres millones y medio de habitantes— constituye su mayor fortaleza estratégica. Lejos de ser una limitación insuperable, su escala humana facilita la cohesión social, la deliberación democrática pacífica y la adopción de políticas públicas audaces con base empírica, refrendando el estatus de la república oriental como un faro de sensatez humanista, audacia legislativa y progreso social en un planeta necesitado de modelos de convivencia inspiradores que demuestren la viabilidad de un desarrollo ético y sostenible."
        ],
        "b2-uruguay-05": [
            "Para quien desembarca por primera vez en Montevideo o recorre los pequeños pueblos del interior uruguayo a orillas del río Uruguay o del río Negro, el impacto inicial suele ser de una serenidad desacostumbrada. A escasas millas náuticas del ritmo febril y vertiginoso de Buenos Aires, la capital uruguaya parece respirar con una cadencia pausada y humana, donde la prisa cotidiana se disuelve en una cortesía reposada y donde el trato cotidiano entre vecinos, comerciantes y transeúntes se rige por un escrupuloso respeto mutuo. El corazón visual y afectivo de este sosiego oriental es la majestuosa rambla montevideana, una franja peatonal costera de más de veintidós kilómetros ininterrumpidos que abraza las aguas amarronadas y salobres del Río de la Plata desde la histórica Ciudad Vieja hasta el barrio señorial de Carrasco, funcionando como un inmenso balcón cívico abierto a todos los ciudadanos.",
            "A lo largo de esa inmensa balconada cívica frente al horizonte fluvial, se despliega a diario el ritual identitario más transversal y ecuménico de la nación oriental: la liturgia del mate. A diferencia de otras regiones del Cono Sur donde el mate se consume sentado en la intimidad hogareña o en círculos compartidos en una mesa de campo, el uruguayo lleva su termo de acero inoxidable encajado con naturalidad bajo el brazo izquierdo y sostiene la calabaza con la bombilla en la mano derecha dondequiera que vaya: caminando por la rambla al atardecer, viajando en autobús urbano hacia la universidad, trabajando en una oficina pública o haciendo cola pacientemente en una dependencia bancaria. El mate amargo de yerba pura sin palo no es un mero estimulante diurético; es un apéndice corporal, un compañero existencial y una contraseña tácita de pertenencia comunitaria que desdibuja todas las jerarquías de clase social y hermana a los orientales en una misma pausa reflexiva.",
            "Otro pilar insustituible de la sociabilidad oriental florece durante las noches estivales de febrero en los 'tablados' de barrio, los escenarios populares levantados en clubes de fútbol infantil, plazas públicas o sedes vecinales para albergar las presentaciones del Carnaval más largo del mundo. Allí brilla la 'murga' uruguaya, un género coral y teatral incomparable que combina la polifonía de trece voces potentes vestidas con trajes fastuosos y rostros pintados, el repique sincopado del bombo, los platillos y el redoblante, y letras cargadas de una lúcida e implacable sátira política y social. Sobre las tablas de madera, la murga pasa revista a los yerros del gobierno, fustiga la hipocresía de los poderosos y canta con poesía desgarradora a los amores perdidos y a la nostalgia barrial, operando como un formidable tribunal ético popular al que ningún dirigente político escapa con indiferencia.",
            "Esta singular convivencia armónica estriba en un rasgo sociológico medular del alma colectiva oriental: una profunda aversión a la ostentación y un arraigado credo igualitario que desconfía visceralmente de los liderazgos providenciales, caudillescos o arrogantes. En el Uruguay, los expresidentes de la república caminan por las ferias vecinales sin guardaespaldas armados, hacen la compra en la verdulería del barrio y conversan amablemente con ciudadanos que votaron a partidos contrarios en las elecciones anteriores. Esa cercanía republicana y esa sencillez en el ejercicio del poder público —que figuras de proyección universal como José Mujica proyectaron ante la fascinación del mundo— no son una pose electoral calculada, sino la encarnación viva de la histórica máxima artiguista: 'Naides es más que naides'.",
            "Así, entre el termo bajo el brazo, la brisa fresca del río en la rambla, el eco lejano de los tambores de candombe en el Barrio Sur y la conversación serena en los viejos cafés montevideanos, el pueblo oriental conserva el tesoro más preciado de la modernidad: la capacidad de edificar una sociedad culta, próspera y tolerante sin renunciar a la lentitud humana, al sosiego espiritual y a la fraterna convivencia cívica que hacen de esta tierra un refugio inestimable de cordura republicana frente a las tempestades y las urgencias del mundo contemporáneo."
        ],
        "b2-uruguay-consolidation": [
            "Examinar la trayectoria histórica, institucional y cultural de la República Oriental del Uruguay a la luz de los complejos dilemas del siglo veintiuno equivale a redescubrir una excepcionalidad democrática de trascendencia universal e incalculable valor ético. En un continente americano marcado con frecuencia por crisis recurrentes de gobernabilidad, abismos de desigualdad distributiva y virulencias polarizantes, este pequeño país de tres millones y medio de habitantes ha sabido cimentar una arquitectura comunitaria singular y pacífica, caracterizada por la fortaleza de sus partidos políticos históricos, la temprana secularización de su espacio público, la vanguardia en derechos civiles y una ejemplar cultura de cercanía republicana que prioriza el sosiego cívico y la templanza sobre cualquier mesianismo autoritario.",
            "El batllismo fundacional impulsado por José Batlle y Ordóñez a principios del siglo veinte no fue una mera corriente política coyuntural, sino una matriz filosófica perdurable que enseñó al pueblo oriental a confiar en el Estado como el escudo supremo de los desposeídos y el árbitro ético de la convivencia colectiva. La temprana conquista de la jornada laboral de ocho horas, el divorcio civil por la sola voluntad de la mujer, la educación pública universal y gratuita inspirada en el ideario pedagógico de José Pedro Varela y la estricta laicidad de Estado que retiró la tutela dogmática de las instituciones públicas configuraron una ciudadanía ilustrada, crítica, participativa y profundamente consciente de sus derechos inalienables frente a cualquier arbitrariedad del poder civil, patronal o religioso.",
            "Esa sólida conciencia cívica demostró su temple heroico en los momentos más oscuros de la patria, cuando la dictadura cívico-militar de 1973 pretendió asfixiar las libertades constitucionales bajo el terror de Estado, la tortura sistemática y el encarcelamiento masivo de opositores. El glorioso NO ciudadano en el plebiscito constitucional de noviembre de 1980 —una hazaña electoral irrepetible donde un pueblo desarmado derrotó a los fusiles en las urnas sin recurrir a la violencia— ratificó que las instituciones libres y el sufragio universal son patrimonios irrenunciables del alma oriental. Asimismo, la persistente demanda de Memoria, Verdad y Justicia que cada año colma pacíficamente las calles en la Marcha del Silencio recuerda que ninguna estabilidad democrática puede considerarse plena mientras persistan deudas morales con las víctimas del autoritarismo.",
            "En el plano de las identidades vivas y las sensibilidades compartidas, el pulso afrouruguayo del candombe y la poesía crítica de las murgas barriales demuestran que la cultura popular oriental no es un adorno folclórico decorativo, sino un canal vital de deliberación comunitaria, resistencia afectiva y celebración festiva donde convergen todas las generaciones de vecinos en los tablados populares de cada rincón del país. En estrecha armonía con esta herencia comunitaria, la sociedad uruguaya contemporánea ha sabido situarse a la vanguardia mundial mediante la regulación pionera del mercado de cannabis, la aprobación del matrimonio igualitario, la inclusión digital universal del Plan Ceibal en cada escuela pública y una transición energética ejemplar que abastece al país casi en su totalidad con fuentes limpias y renovables, demostrando que la audacia ética y la sostenibilidad ecológica son plenamente compatibles con la moderación y el sosiego republicano.",
            "Uruguay se revela, en conclusión, como una patria donde la convivencia armónica no se impone por decreto ni por la fuerza, sino que se construye pacientemente día a día en la conversación pausada de café, en el paseo compartido por la rambla de Montevideo con el termo bajo el brazo y en el arraigado principio ético de que nadie es superior a nadie por cuna, rango o fortuna personal. Comprender la experiencia uruguaya exige valorar el poder transformador de las instituciones transparentes, el respeto irrestricto por las normas acordadas y la templanza republicana, confirmando ante la mirada atenta de la comunidad internacional que la verdadera grandeza histórica de un pueblo no se mide por la inmensidad de su territorio geográfico ni por su arsenal militar, sino por la nobleza, la madurez y la generosidad cívica de su pacto democrático compartido ante los complejos desafíos del porvenir."
        ]
    }

    regional_titles_summaries = {
        "b2-uruguay-01": (
            "El batllismo y el Estado de bienestar: La temprana modernidad institucional",
            "Un ensayo sobre la presidencia de José Batlle y Ordóñez: la legislación laboral pionera, el divorcio por la sola voluntad de la mujer, la laicidad de Estado y la gratuidad de la enseñanza pública.",
            ["Historiador del batllismo Gonzalo", "Docente de escuela pública Mariana", "Abogado laboralista Don Ignacio", "Estudiante de ciencias políticas Camila"],
            1
        ),
        "b2-uruguay-02": (
            "Candombe, comparsas y el Barrio Sur: La raíz afrouruguaya y las Llamadas",
            "Una crónica cultural sobre el candombe montevideano: los tambores chico, repique y piano, los míticos conventillos Medio Mundo y Ansina, el desfile de las Llamadas y la resistencia negra.",
            ["Tamborilero y luthier de lonjas Don Heber", "Vedette de comparsa tradicional Laura", "Investigadora del patrimonio afrouruguayo Natalia", "Joven escobero de comparsa Matías"],
            2
        ),
        "b2-uruguay-03": (
            "La dictadura militar (1973–1985) y la gesta democrática del plebiscito de 1980",
            "Una memoria histórica sobre la disolución del parlamento, la huelga general obrera, el penal de Libertad y el histórico triunfo del NO en el plebiscito de 1980 que aceleró la vuelta a la democracia.",
            ["Militante sindical de la huelga de 1973 Don Walter", "Expreso político del penal de Libertad Esteban", "Periodista y cronista del plebiscito del NO Lucía", "Abogada de derechos humanos Mariana"],
            3
        ),
        "b2-uruguay-04": (
            "Vanguardia cívica y agenda de derechos: Cannabis, matrimonio y matriz verde",
            "Un análisis del modelo uruguayo en el siglo XXI: la regulación estatal del cannabis, el matrimonio igualitario, la inclusión digital del Plan Ceibal y la descarbonización casi total de la matriz eléctrica.",
            ["Bioquímica y reguladora del IRCCA Valeria", "Ingeniero en energías renovables Bruno", "Docente de informática del Plan Ceibal Julián", "Activista de derechos cívicos y diversidad Florencia"],
            4
        ),
        "b2-uruguay-05": (
            "Montevideo, la rambla y la identidad oriental: Mate, tranquilidad y convivencia",
            "Un retrato de la idiosincrasia uruguaya: el ritual del mate con termo bajo el brazo, el sosiego costero de la rambla de Montevideo, las murgas del Carnaval y la ética republicana de la cercanía.",
            ["Vecino y habitué de la rambla Don Alcides", "Directora y letrista de murga barrial Romina", "Sociólogo de la convivencia oriental Santiago", "Paseante y feriante de Tristán Narvaja Soledad"],
            5
        ),
        "b2-uruguay-consolidation": (
            "Consolidación: El pacto cívico y la convivencia oriental",
            "Una síntesis integral de los pilares democráticos y culturales de Uruguay: el legado batllista, la resistencia cívica del NO, el ritmo del candombe y la vanguardia institucional del nuevo siglo.",
            ["Ensayista y politólogo oriental Bautista", "Historiadora de las instituciones Laura", "Sociólogo del espacio público Sebastián", "Docente universitaria Mercedes"],
            6
        )
    }

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
                            "question": "¿Cuál es la premisa central que define la identidad sociopolítica de Uruguay según el texto?",
                            "options": [
                                "La primacía del autoritarismo militar sobre la voluntad popular.",
                                "La sólida construcción de un Estado de bienestar laico, la convivencia republicana y la defensa pacífica de las libertades.",
                                "El rechazo absoluto a cualquier tipo de reforma legislativa o avance de derechos.",
                                "La subordinación total de la economía a las decisiones de las potencias extranjeras."
                            ],
                            "correctIndex": 1,
                            "explanation": "El texto resalta el modelo batllista, la laicidad, la convivencia igualitaria y la resistencia pacífica en las urnas."
                        },
                        {
                            "question": "¿Qué episodio histórico evidenció la inquebrantable vocación democrática del pueblo uruguayo en el siglo XX?",
                            "options": [
                                "La firma de tratados comerciales secretos durante la década del cincuenta.",
                                "El triunfo rotundo del NO en el plebiscito de 1980 convocado por la dictadura militar.",
                                "La disolución de los clubes deportivos en los barrios tradicionales.",
                                "La cancelación definitiva del Carnaval montevideano por decreto municipal."
                            ],
                            "correctIndex": 1,
                            "explanation": "El 30 de noviembre de 1980 el 57% de la ciudadanía votó NO al proyecto constitucional autoritario de las fuerzas armadas."
                        },
                        {
                            "question": "¿Qué manifestación cultural o cotidiana encarna el sentido de igualdad y encuentro de la sociedad uruguaya?",
                            "options": [
                                "El uso exclusivo de carruajes importados en las avenidas residenciales.",
                                "El ritual cotidiano del mate en la rambla de Montevideo y el toque comunitario del candombe y las murgas.",
                                "La obligatoriedad de vestir uniforme militar en los eventos públicos cívicos.",
                                "El aislamiento estricto de las familias en barrios cerrados sin contacto con la calle."
                            ],
                            "correctIndex": 1,
                            "explanation": "El mate compartido frente al río y las comparsas de candombe en el espacio público simbolizan la integración sin jerarquías."
                        }
                    ]
                }
            }
        }

        w_count = count_words(story_obj)
        print(f"{rel_path}: {w_count} words")
        assert 650 <= w_count <= 825, f"Story {rel_path} has {w_count} words (must be 650-825)"
        write_json(rel_path, story_obj)

    # Consolidated library story: b2-uruguay.json (25 paragraphs from lessons 1-5)
    stitched_paragraphs = []
    for i in range(1, 6):
        stem = f"b2-uruguay-0{i}"
        for p in regional_story_texts[stem]:
            stitched_paragraphs.append({"type": "narration", "text": p})

    assert len(stitched_paragraphs) == 25, f"Stitched library story must have 25 paragraphs, got {len(stitched_paragraphs)}"

    stitched_story = {
        "id": "b2-uruguay",
        "title": "Uruguay: Secularismo, Candombe, Institucionalidad y Convivencia",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 20,
        "summary": "Un compendio integral sobre la singular experiencia republicana y cultural del Uruguay: el Estado de bienestar y la laicidad batllista, el candombe de Barrio Sur y Palermo como raíz afrouruguaya, la resistencia cívica del plebiscito del NO en 1980, la vanguardia mundial en regulación del cannabis y energías limpias, y la serena convivencia cotidiana del mate en la rambla montevideana.",
        "characters": [
            "Pioneros del reformismo batllista y educadores varelianos",
            "Tamborileros, matriarcas y bailarines del candombe tradicional",
            "Luchadores sociales y ciudadanos del histórico plebiscito de 1980",
            "Científicos, legisladores y promotores de la agenda verde",
            "Vecinos, murguistas y paseantes de la rambla de Montevideo"
        ],
        "paragraphs": stitched_paragraphs,
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué rasgo caracterizó las reformas institucionales de José Batlle y Ordóñez a comienzos del siglo XX?",
                        "options": [
                            "La privatización inmediata de todos los recursos naturales y ferrocarriles.",
                            "La creación del primer Estado de bienestar americano con jornada laboral de ocho horas, divorcio femenino y laicidad estricta.",
                            "La imposición de la religión obligatoria en todas las universidades públicas.",
                            "La supresión definitiva de los sindicatos y de los partidos de oposición."
                        ],
                        "correctIndex": 1,
                        "explanation": "El batllismo sentó las bases de un Estado de bienestar modelo con avanzada legislación social y secularización profunda."
                    },
                    {
                        "question": "¿Cómo se preservó la cultura afrouruguaya del candombe tras los desalojos de los conventillos durante la dictadura?",
                        "options": [
                            "A través de la resistencia comunitaria en los toques de comparsas de Barrio Sur y Palermo y el desfile de las Llamadas.",
                            "Abandonando por completo el uso de tambores de madera y cuero de lonja.",
                            "Trasladando las sedes de las comparsas exclusivamente a clubes de lujo en el extranjero.",
                            "Sustituyendo los ritmos africanos por danzas cortesanas europeas tradicionales."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los tamborileros mantuvieron vivos los toques de piano, chico y repique templados al fuego, resistiendo al desarraigo."
                    },
                    {
                        "question": "¿Qué logro internacional contemporáneo destaca a Uruguay en materia de sostenibilidad ecológica?",
                        "options": [
                            "La construcción masiva de reactores nucleares de alta potencia en la costa fluvial.",
                            "La generación de entre el 95% y el 98% de su electricidad mediante fuentes limpias y renovables como el viento y el agua.",
                            "La prohibición absoluta del uso de computadoras en las aulas escolares públicas.",
                            "La venta exclusiva de automóviles movilizados a carbón mineral en Montevideo."
                        ],
                        "correctIndex": 1,
                        "explanation": "Uruguay transformó su matriz eléctrica logrando una descarbonización casi total sustentada en energía eólica, biomasa e hidroeléctrica."
                    }
                ]
            }
        }
    }
    write_json("stories/world/b2/b2-uruguay.json", stitched_story)

    # 6. Exercises (12 files)
    exercise_files = {
        # Core Unit 27
        "b2-27-01-ex": {
            "lesson": "b2-27-01",
            "exercises": [
                {
                    "id": "b2-27-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "question": "¿Qué locución prepositiva completa adecuadamente la oración expresando origen causal directo?",
                    "options": [
                        "A raíz de las nuevas investigaciones, el tribunal reabrió la causa penal.",
                        "So pretexto de las nuevas investigaciones, el tribunal reabrió la causa penal.",
                        "Con miras a las nuevas investigaciones, el tribunal reabrió la causa penal.",
                        "Al margen de las nuevas investigaciones, el tribunal reabrió la causa penal."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "sentence": "En __ de las potestades conferidas por la Constitución, el ministro promulgó la ley.",
                    "answer": "virtud",
                    "english": "By virtue of the powers conferred by the Constitution, the minister promulgated the law."
                },
                {
                    "id": "b2-27-01.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "question": "¿Cuál de las siguientes frases introduce formalmente un acontecimiento conmemorativo?",
                    "options": [
                        "Con motivo del centenario constitucional, se inauguró el archivo nacional.",
                        "En pos del centenario constitucional, se inauguró el archivo nacional.",
                        "A costa del centenario constitucional, se inauguró el archivo nacional.",
                        "Conforme de centenario constitucional, se inauguró el archivo nacional."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "sentence": "A __ de los reclamos sindicales, se instituyó la jornada laboral de ocho horas.",
                    "answer": "raíz",
                    "english": "As a direct result of union demands, the eight-hour workday was instituted."
                },
                {
                    "id": "b2-27-01.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-27-vocab"],
                    "pairs": [
                        ["a raíz de", "as a result of / following"],
                        ["en virtud de", "by virtue of / pursuant to"],
                        ["la coyuntura", "the situational context"],
                        ["el precepto legal", "the legal precept / mandate"]
                    ]
                },
                {
                    "id": "b2-27-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "En 'Anaconda' de Horacio Quiroga, ¿cuál es la causa inmediata que motiva a Lanceolata a convocar el congreso?",
                    "options": [
                        "La crecida destructiva de las aguas del río Paraná.",
                        "La instalación del campamento científico humano para extraer veneno.",
                        "Una rebelión interna de las víboras constrictoras del monte.",
                        "La sequía extrema que afectó a la fauna del sotobosque."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-27-02-ex": {
            "lesson": "b2-27-02",
            "exercises": [
                {
                    "id": "b2-27-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "question": "¿Cuál es la expresión canónica recomendada en registro formal para citar conformidad con una norma?",
                    "options": [
                        "Los magistrados resolvieron la controversia conforme a derecho.",
                        "Los magistrados resolvieron la controversia de acuerdo a derecho.",
                        "Los magistrados resolvieron la controversia con arreglo de derecho.",
                        "Los magistrados resolvieron la controversia a tenor con derecho."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "sentence": "De acuerdo __ las estadísticas oficiales, la inflación disminuyó de manera sostenida.",
                    "answer": "con",
                    "english": "According to official statistics, inflation decreased steadily."
                },
                {
                    "id": "b2-27-02.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "question": "¿Qué locución prepositiva denota adecuación al contenido literal de un texto o testimonio?",
                    "options": [
                        "A tenor de las declaraciones de los testigos, no hubo negligencia oficial.",
                        "En pos de las declaraciones de los testigos, no hubo negligencia oficial.",
                        "A costa de las declaraciones de los testigos, no hubo negligencia oficial.",
                        "So pretexto de las declaraciones de los testigos, no hubo negligencia oficial."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "sentence": "Se liquidaron las compensaciones con __ a los estatutos vigentes de la institución.",
                    "answer": "arreglo",
                    "english": "Compensations were settled in compliance with the institution's current statutes."
                },
                {
                    "id": "b2-27-02.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-27-vocab"],
                    "pairs": [
                        ["conforme a", "in accordance with / according to"],
                        ["la estipulación", "the contractual stipulation"],
                        ["supeditar", "to condition / to make subject to"],
                        ["acatar", "to abide by / to comply with"]
                    ]
                },
                {
                    "id": "b2-27-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "En el relato de Quiroga, ¿por qué asisten las víboras al congreso convocado por Lanceolata?",
                    "options": [
                        "Porque los códigos ancestrales de la selva proscriben querellas durante treguas mayores.",
                        "Porque deseaban entregarse pacíficamente a los científicos del campamento.",
                        "Porque el fuego del campamento había destruido todas sus madrigueras.",
                        "Porque Anaconda las amenazó con expulsarlas del cauce del río."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-27-03-ex": {
            "lesson": "b2-27-03",
            "exercises": [
                {
                    "id": "b2-27-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "question": "¿Qué locución prepositiva expresa una subordinación o sacrificio noble en favor de un bien superior?",
                    "options": [
                        "Renunciaron a privilegios individuales en aras del bienestar colectivo.",
                        "Renunciaron a privilegios individuales a costa del bienestar colectivo.",
                        "Renunciaron a privilegios individuales so pretexto del bienestar colectivo.",
                        "Renunciaron a privilegios individuales al margen del bienestar colectivo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "sentence": "No se puede obtener crecimiento económico a __ de los derechos laborales fundamentales.",
                    "answer": "costa",
                    "english": "Economic growth cannot be achieved at the expense of fundamental labor rights."
                },
                {
                    "id": "b2-27-03.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "question": "¿Cuál de las siguientes frases expresa una meta planificada a mediano plazo?",
                    "options": [
                        "Diseñaron un plan integral con miras a la descarbonización energética del país.",
                        "Diseñaron un plan integral a tenor de la descarbonización energética del país.",
                        "Diseñaron un plan integral so pretexto de la descarbonización energética del país.",
                        "Diseñaron un plan integral en virtud de la descarbonización energética del país."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "sentence": "Las organizaciones marcharon unidas en __ de la justicia social y la memoria histórica.",
                    "answer": "pos",
                    "english": "The organizations marched united in pursuit of social justice and historical memory."
                },
                {
                    "id": "b2-27-03.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-27-vocab"],
                    "pairs": [
                        ["en aras de", "for the sake of / in pursuit of"],
                        ["a costa de", "at the expense of / at the cost of"],
                        ["la abnegación", "the selflessness / self-sacrifice"],
                        ["menoscabar", "to undermine / to impair"]
                    ]
                },
                {
                    "id": "b2-27-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "En 'Anaconda', ¿qué advierte la gran constrictora sobre el costo de un ataque precipitado contra los hombres?",
                    "options": [
                        "Que derivaría en una represalia humana con desmonte y fuego a costa del hábitat selvático.",
                        "Que los hombres aprenderían a nadar y conquistarían el fondo del río.",
                        "Que las víboras venenosas perderían su reputación ante los demás animales.",
                        "Que el veneno se agotaría para siempre en todas las generaciones futuras."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-27-04-ex": {
            "lesson": "b2-27-04",
            "exercises": [
                {
                    "id": "b2-27-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "question": "¿Qué locución denuncia de manera explícita un motivo aparente o coartada falaz?",
                    "options": [
                        "So pretexto de mantener el orden, clausuraron periódicos independientes.",
                        "Conforme a mantener el orden, clausuraron periódicos independientes.",
                        "En aras de mantener el orden, clausuraron periódicos independientes.",
                        "De acuerdo con mantener el orden, clausuraron periódicos independientes."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "sentence": "Se sancionó la falta administrativa, sin __ de las acciones penales que procedan.",
                    "answer": "perjuicio",
                    "english": "The administrative offense was sanctioned, without prejudice to any criminal actions that may apply."
                },
                {
                    "id": "b2-27-04.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "question": "¿Qué opción introduce el criterio pericial de una autoridad consultada?",
                    "options": [
                        "A juicio de los constitucionalistas, el decreto transgrede normas superiores.",
                        "En pos de los constitucionalistas, el decreto transgrede normas superiores.",
                        "A costa de los constitucionalistas, el decreto transgrede normas superiores.",
                        "Conforme con los constitucionalistas, el decreto transgrede normas superiores."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "sentence": "Al __ de las discrepancias políticas, la salud pública fue priorizada por todos.",
                    "answer": "margen",
                    "english": "Apart from political disagreements, public health was prioritized by everyone."
                },
                {
                    "id": "b2-27-04.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-27-vocab"],
                    "pairs": [
                        ["so pretexto de", "under the pretext of"],
                        ["sin perjuicio de", "without prejudice to / notwithstanding"],
                        ["la salvedad", "the proviso / reservation"],
                        ["el subterfugio", "the subterfuge / evasion"]
                    ]
                },
                {
                    "id": "b2-27-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "En el relato de Quiroga, ¿cómo describe Lanceolata las capturas de serpientes por parte de los científicos?",
                    "options": [
                        "Como un secuestro servil so pretexto de investigar sus hábitos zoológicos.",
                        "Como una colaboración voluntaria para mejorar la medicina del monte.",
                        "Como una invitación honorable a formar parte de una expedición mundial.",
                        "Como un tributo religioso exigido por los dioses de la selva."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-27-05-ex": {
            "lesson": "b2-27-05",
            "exercises": [
                {
                    "id": "b2-27-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "question": "¿Qué preposición rige el verbo analítico 'estribar' en la prosa culta formal?",
                    "options": [
                        "La fortaleza del sistema estriba en la confianza mutua entre ciudadanos.",
                        "La fortaleza del sistema estriba con la confianza mutua entre ciudadanos.",
                        "La fortaleza del sistema estriba de la confianza mutua entre ciudadanos.",
                        "La fortaleza del sistema estriba por la confianza mutua entre ciudadanos."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "Las negociaciones parlamentarias derivaron __ un histórico acuerdo multipartidario.",
                    "answer": "en",
                    "english": "The parliamentary negotiations resulted in a historic multi-party agreement."
                },
                {
                    "id": "b2-27-05.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "question": "¿Qué verbo con régimen preposicional significa tener como materia temática un asunto?",
                    "options": [
                        "La conferencia versó sobre la historia de la laicidad republicana.",
                        "La conferencia abogó sobre la historia de la laicidad republicana.",
                        "La conferencia estribó sobre la historia de la laicidad republicana.",
                        "La conferencia derivó sobre la historia de la laicidad republicana."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "La delegación diplomática abogó __ el respeto al derecho internacional humanitario.",
                    "answer": "por",
                    "english": "The diplomatic delegation advocated for respect for international humanitarian law."
                },
                {
                    "id": "b2-27-05.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-27-vocab"],
                    "pairs": [
                        ["estribar en", "to lie in / to consist in"],
                        ["derivar en", "to lead to / to result in"],
                        ["versar sobre", "to deal with / to be about"],
                        ["abogar por", "to advocate for / to champion"]
                    ]
                },
                {
                    "id": "b2-27-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Al final del relato de Quiroga, ¿en qué concluye Anaconda que estriba la tragedia de las fieras del monte?",
                    "options": [
                        "En el implacable avance técnico de una civilización que devora el misterio de la naturaleza.",
                        "En la traición de las serpientes venenosas que abandonaron la lucha.",
                        "En la falta de lluvias que debilitó las corrientes de los ríos selváticos.",
                        "En la incapacidad de comunicarse telepáticamente con los científicos."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-27-consolidation-ex": {
            "lesson": "b2-27-consolidation",
            "exercises": [
                {
                    "id": "b2-27-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "question": "¿Qué enunciado integra con precisión normativa la locución causal formal?",
                    "options": [
                        "En virtud del dictamen vinculante, el comité procedió a revisar las credenciales.",
                        "En virtud al dictamen vinculante, el comité procedió a revisar las credenciales.",
                        "A raíz con el dictamen vinculante, el comité procedió a revisar las credenciales.",
                        "Conforme de dictamen vinculante, el comité procedió a revisar las credenciales."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "sentence": "Se liquidaron los haberes con __ a las ordenanzas vigentes de la administración.",
                    "answer": "arreglo",
                    "english": "Salaries were settled in compliance with current administration ordinances."
                },
                {
                    "id": "b2-27-consolidation.ex03",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "La singularidad del modelo democrático estriba __ la confianza cívica entre sus ciudadanos.",
                    "answer": "en",
                    "english": "The uniqueness of the democratic model lies in civic trust among its citizens."
                },
                {
                    "id": "b2-27-consolidation.ex04",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "question": "¿Qué opción formula un sacrificio legítimo en favor de un bien superior?",
                    "options": [
                        "Ambas partes flexibilizaron sus posturas en aras de asegurar la paz republicana.",
                        "Ambas partes flexibilizaron sus posturas a costa de asegurar la paz republicana.",
                        "Ambas partes flexibilizaron sus posturas so pretexto de asegurar la paz republicana.",
                        "Ambas partes flexibilizaron sus posturas al margen de asegurar la paz republicana."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "question": "¿Cuál de las siguientes oraciones utiliza una locución de pretexto de forma sintácticamente intachable?",
                    "options": [
                        "So pretexto de seguridad nacional, se suspendieron ilegítimamente las garantías cívicas.",
                        "So el pretexto de seguridad nacional, se suspendieron ilegítimamente las garantías cívicas.",
                        "Bajo pretexto a seguridad nacional, se suspendieron ilegítimamente las garantías cívicas.",
                        "En pretexto de seguridad nacional, se suspendieron ilegítimamente las garantías cívicas."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-27-consolidation.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "Los representantes diplomáticos abogaron __ una solución negociada y multilateral.",
                    "answer": "por",
                    "english": "The diplomatic representatives advocated for a negotiated, multilateral solution."
                },
                {
                    "id": "b2-27-consolidation.ex07",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-27-vocab"],
                    "pairs": [
                        ["el precepto", "the precept / legal mandate"],
                        ["el subterfugio", "the subterfuge / evasion"],
                        ["la salvedad", "the proviso / reservation"],
                        ["versar sobre", "to deal with / to be about"]
                    ]
                },
                {
                    "id": "b2-27-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué síntesis filosófica plantea 'Anaconda' sobre el encuentro entre la selva y la técnica humana?",
                    "options": [
                        "La confrontación trágica entre el instinto primario silvestre y el cálculo dominador de la civilización.",
                        "La victoria definitiva de los animales que logran erradicar a la especie humana del continente.",
                        "La domesticación pacífica de todas las especies de serpientes para el trabajo agrícola.",
                        "La demostración de que el veneno ofídico carece de cualquier aplicación científica útil."
                    ],
                    "correct": 0
                }
            ]
        },

        # Regional Unit: b2-uruguay
        "b2-uruguay-01-ex": {
            "lesson": "b2-uruguay-01",
            "exercises": [
                {
                    "id": "b2-uruguay-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "question": "¿Qué locución prepositiva complementa con propiedad la afirmación sobre las reformas batllistas?",
                    "options": [
                        "En virtud de las leyes de 1913, Uruguay consagró el divorcio por la sola voluntad de la mujer.",
                        "So pretexto de las leyes de 1913, Uruguay consagró el divorcio por la sola voluntad de la mujer.",
                        "A costa de las leyes de 1913, Uruguay consagró el divorcio por la sola voluntad de la mujer.",
                        "Al margen de las leyes de 1913, Uruguay consagró el divorcio por la sola voluntad de la mujer."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "sentence": "A __ de la reforma de Varela, la escuela pública se consagró como obligatoria y gratuita.",
                    "answer": "raíz",
                    "english": "Following Varela's reform, public school was established as compulsory and free."
                },
                {
                    "id": "b2-uruguay-01.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "question": "¿Cómo se denominó oficialmente la Semana Santa en Uruguay tras la secularización batllista?",
                    "options": [
                        "Con motivo de la laicidad estatal, pasó a llamarse oficialmente Semana de Turismo.",
                        "Con motivo de la laicidad estatal, pasó a llamarse oficialmente Semana Santa Mayor.",
                        "Con motivo de la laicidad estatal, pasó a llamarse oficialmente Semana del Santo Sepulcro.",
                        "Con motivo de la laicidad estatal, pasó a llamarse oficialmente Semana Episcopal."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "sentence": "En __ de la Constitución de 1917, se consumó la separación entre la Iglesia y el Estado.",
                    "answer": "virtud",
                    "english": "By virtue of the 1917 Constitution, the separation between Church and State was finalized."
                },
                {
                    "id": "b2-uruguay-01.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-uruguay-vocab"],
                    "pairs": [
                        ["el batllismo", "Uruguayan welfare state reformism"],
                        ["la laicidad", "secularism / lay statehood"],
                        ["la estatización", "state nationalization of services"],
                        ["el cogobierno", "co-governance in public universities"]
                    ]
                },
                {
                    "id": "b2-uruguay-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué rasgo singular distinguió a la ley de divorcio aprobada en Uruguay en 1913?",
                    "options": [
                        "Que permitió la disolución del matrimonio por la sola voluntad de la mujer sin alegar causales.",
                        "Que exigió el permiso obligatorio de las autoridades eclesiásticas vaticanas.",
                        "Que impidió a las mujeres conservar la custodia de sus hijos en cualquier circunstancia.",
                        "Que solo tuvo vigencia en las zonas rurales del norte del país."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-uruguay-02-ex": {
            "lesson": "b2-uruguay-02",
            "exercises": [
                {
                    "id": "b2-uruguay-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "question": "¿Qué locución prepositiva resalta la entrega comunitaria de los afrouruguayos por su identidad?",
                    "options": [
                        "Las familias afrouruguayas preservaron sus toques ancestrales en aras de la dignidad colectiva.",
                        "Las familias afrouruguayas preservaron sus toques ancestrales a costa de la dignidad colectiva.",
                        "Las familias afrouruguayas preservaron sus toques ancestrales so pretexto de la dignidad colectiva.",
                        "Las familias afrouruguayas preservaron sus toques ancestrales al margen de la dignidad colectiva."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "sentence": "Las comparsas marchan por la calle Isla de Flores en __ del reconocimiento de sus raíces.",
                    "answer": "pos",
                    "english": "The comparsas march down Isla de Flores Street in pursuit of the recognition of their roots."
                },
                {
                    "id": "b2-uruguay-02.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "question": "¿Cuál de las siguientes frases expresa la preparación orientada al concurso de Carnaval?",
                    "options": [
                        "Las cuerdas de tambores ensayan con miras a deslumbrar en el Desfile de las Llamadas.",
                        "Las cuerdas de tambores ensayan a costa de deslumbrar en el Desfile de las Llamadas.",
                        "Las cuerdas de tambores ensayan a tenor de deslumbrar en el Desfile de las Llamadas.",
                        "Las cuerdas de tambores ensayan so pretexto de deslumbrar en el Desfile de las Llamadas."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "sentence": "La especulación inmobiliaria demolió conventillos históricos a __ del desarraigo vecinal.",
                    "answer": "costa",
                    "english": "Real estate speculation demolished historic tenement houses at the cost of neighborhood uprooting."
                },
                {
                    "id": "b2-uruguay-02.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-uruguay-vocab"],
                    "pairs": [
                        ["el tamborilero", "the candombe drummer"],
                        ["la lonja", "the drum skin / leather head"],
                        ["el repique", "the improvisational high drum"],
                        ["el conventillo", "the historic tenement house"]
                    ]
                },
                {
                    "id": "b2-uruguay-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Por qué los tamborileros de candombe encienden pequeñas fogatas en las aceras antes de tocar?",
                    "options": [
                        "Para calentar y templar las lonjas de cuero vacuno al calor directo del fuego.",
                        "Para quemar las partituras musicales e improvisar de memoria.",
                        "Para iluminar el camino ante la falta de alumbrado público municipal.",
                        "Para ahuyentar a las comparsas rivales que marchan en sentido contrario."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-uruguay-03-ex": {
            "lesson": "b2-uruguay-03",
            "exercises": [
                {
                    "id": "b2-uruguay-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "question": "¿Qué locución denuncia la excusa falaz utilizada por los golpistas en 1973?",
                    "options": [
                        "So pretexto de restablecer la seguridad, la dictadura disolvió las cámaras legislativas.",
                        "Conforme a restablecer la seguridad, la dictadura disolvió las cámaras legislativas.",
                        "En aras de restablecer la seguridad, la dictadura disolvió las cámaras legislativas.",
                        "De acuerdo con restablecer la seguridad, la dictadura disolvió las cámaras legislativas."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "sentence": "A __ de los analistas políticos, el triunfo del NO en 1980 precipitó el fin del régimen militar.",
                    "answer": "juicio",
                    "english": "In the opinion of political analysts, the triumph of the NO in 1980 hastened the end of the military regime."
                },
                {
                    "id": "b2-uruguay-03.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "question": "¿Qué enunciado expresa una salvedad que mantuvo viva la dignidad electoral a pesar de las amenazas?",
                    "options": [
                        "Los ciudadanos votaron con valentía, sin perjuicio de las amenazas veladas de la junta.",
                        "Los ciudadanos votaron con valentía, con motivo de las amenazas veladas de la junta.",
                        "Los ciudadanos votaron con valentía, a costa de las amenazas veladas de la junta.",
                        "Los ciudadanos votaron con valentía, con arreglo a las amenazas veladas de la junta."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "sentence": "Al __ del monopolio mediático estatal, la resistencia ciudadana circuló de boca en boca.",
                    "answer": "margen",
                    "english": "Apart from the state media monopoly, citizen resistance circulated by word of mouth."
                },
                {
                    "id": "b2-uruguay-03.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-uruguay-vocab"],
                    "pairs": [
                        ["el plebiscito", "the constitutional referendum"],
                        ["la proscripción", "the political banning"],
                        ["la clandestinidad", "the secrecy / clandestinity"],
                        ["la penitenciaría", "the military prison / penitentiary"]
                    ]
                },
                {
                    "id": "b2-uruguay-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál fue el resultado trascendental del plebiscito constitucional uruguayo del 30 de noviembre de 1980?",
                    "options": [
                        "El triunfo del NO con casi el 57% de los votos que derrotó el proyecto constitucional militar.",
                        "La aprobación unánime de la reforma propuesta por los comandantes generales.",
                        "La suspensión definitiva de los comicios por falta de votantes en las urnas.",
                        "El nombramiento perpetuo del presidente de facto como monarca constitucional."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-uruguay-04-ex": {
            "lesson": "b2-uruguay-04",
            "exercises": [
                {
                    "id": "b2-uruguay-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "question": "¿Qué locución de conformidad encaja adecuadamente para citar los protocolos del cannabis?",
                    "options": [
                        "La distribución en farmacias se realiza conforme a los protocolos sanitarios del IRCCA.",
                        "La distribución en farmacias se realiza conforme de los protocolos sanitarios del IRCCA.",
                        "La distribución en farmacias se realiza a tenor con los protocolos sanitarios del IRCCA.",
                        "La distribución en farmacias se realiza en arreglo a los protocolos sanitarios del IRCCA."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "sentence": "De acuerdo __ los informes técnicos, Uruguay genera más del noventa y cinco por ciento de energía limpia.",
                    "answer": "con",
                    "english": "According to technical reports, Uruguay generates more than ninety-five percent of clean energy."
                },
                {
                    "id": "b2-uruguay-04.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "question": "¿Qué enunciado expresa apego reglamentario en materia de matrimonio igualitario?",
                    "options": [
                        "Las parejas homoparentales adoptan con arreglo a la ley civil vigente.",
                        "Las parejas homoparentales adoptan a tenor con la ley civil vigente.",
                        "Las parejas homoparentales adoptan en regla a la ley civil vigente.",
                        "Las parejas homoparentales adoptan con acuerdo de la ley civil vigente."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "sentence": "A __ de los índices internacionales, el Plan Ceibal redujo sustancialmente la brecha digital.",
                    "answer": "tenor",
                    "english": "In light of international indices, Plan Ceibal substantially reduced the digital divide."
                },
                {
                    "id": "b2-uruguay-04.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-uruguay-vocab"],
                    "pairs": [
                        ["la descarbonización", "the energy decarbonization"],
                        ["la matriz eléctrica", "the electric power grid"],
                        ["el autocultivo", "the registered home growing"],
                        ["la sostenibilidad", "the ecological sustainability"]
                    ]
                },
                {
                    "id": "b2-uruguay-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿En qué consistió la iniciativa pionera del Plan Ceibal instaurado en Uruguay en 2007?",
                    "options": [
                        "En entregar una computadora portátil gratuita con internet a cada alumno y docente de escuela pública.",
                        "En cobrar un impuesto especial a las familias que utilizaban teléfonos inteligentes.",
                        "En prohibir la enseñanza de programación informática en la educación primaria.",
                        "En vender computadoras usadas exclusivamente a empresas privadas extranjeras."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-uruguay-05-ex": {
            "lesson": "b2-uruguay-05",
            "exercises": [
                {
                    "id": "b2-uruguay-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "question": "¿Qué preposición rige el verbo 'estribar' al analizar la vida barrial uruguaya?",
                    "options": [
                        "El encanto de Montevideo estriba en su rambla abierta y en su ritmo pausado.",
                        "El encanto de Montevideo estriba con su rambla abierta y en su ritmo pausado.",
                        "El encanto de Montevideo estriba de su rambla abierta y en su ritmo pausado.",
                        "El encanto de Montevideo estriba por su rambla abierta y en su ritmo pausado."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "Las letras de la murga uruguaya en el tablado versan __ la realidad social y política.",
                    "answer": "sobre",
                    "english": "The lyrics of the Uruguayan murga on the neighborhood stage deal with social and political reality."
                },
                {
                    "id": "b2-uruguay-05.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "question": "¿Qué opción formula la defensa cívica de la tolerancia sin estridencias?",
                    "options": [
                        "La sociedad oriental aboga por una convivencia fraterna y dialogante.",
                        "La sociedad oriental aboga en una convivencia fraterna y dialogante.",
                        "La sociedad oriental aboga con una convivencia fraterna y dialogante.",
                        "La sociedad oriental aboga sobre una convivencia fraterna y dialogante."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "Las discusiones acaloradas de café sobre fútbol suelen derivar __ una charla afectuosa.",
                    "answer": "en",
                    "english": "Heated cafe discussions about soccer usually result in an affectionate chat."
                },
                {
                    "id": "b2-uruguay-05.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-uruguay-vocab"],
                    "pairs": [
                        ["la rambla", "the coastal riverfront promenade"],
                        ["el termo", "the stainless steel thermos flask"],
                        ["el tablado", "the neighborhood carnival stage"],
                        ["la murga", "the satirical musical theater troupe"]
                    ]
                },
                {
                    "id": "b2-uruguay-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué costumbre cotidiana describe la singularidad del mate en la cultura uruguaya frente a otros países?",
                    "options": [
                        "Llevar el termo bajo el brazo caminando por la calle, la rambla o el autobús urbano.",
                        "Consumir mate exclusivamente en ceremonias religiosas secretas a medianoche.",
                        "Mezclar el agua del termo con jugos de frutas cítricas azucaradas.",
                        "Prohibir el consumo de mate fuera de los restaurantes de lujo."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-uruguay-consolidation-ex": {
            "lesson": "b2-uruguay-consolidation",
            "exercises": [
                {
                    "id": "b2-uruguay-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-causa-origen"],
                    "question": "¿Qué enunciado combina correctamente una locución causal con un régimen preposicional formal?",
                    "options": [
                        "En virtud de su tradición cívica, Uruguay aboga por el respeto al derecho internacional.",
                        "En virtud a su tradición cívica, Uruguay aboga de el respeto al derecho internacional.",
                        "A raíz con su tradición cívica, Uruguay aboga en el respeto al derecho internacional.",
                        "Conforme de su tradición cívica, Uruguay aboga sobre el respeto al derecho internacional."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-finalidad-sacrificio"],
                    "sentence": "Los partidos sellaron un pacto de Estado en __ de la descarbonización energética del país.",
                    "answer": "aras",
                    "english": "The parties sealed a state pact for the sake of the country's energy decarbonization."
                },
                {
                    "id": "b2-uruguay-consolidation.ex03",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "La singularidad de la república oriental estriba __ su apego irrenunciable a la convivencia laica.",
                    "answer": "en",
                    "english": "The uniqueness of the eastern republic lies in its unwavering adherence to secular coexistence."
                },
                {
                    "id": "b2-uruguay-consolidation.ex04",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-conformidad-criterio"],
                    "question": "¿Qué opción cita adecuadamente los resultados del plebiscito de 1980?",
                    "options": [
                        "A tenor de los escrutinios finales, el NO triunfó con casi el 57% de los sufragios.",
                        "A tenor con los escrutinios finales, el NO triunfó con casi el 57% de los sufragios.",
                        "En tenor a los escrutinios finales, el NO triunfó con casi el 57% de los sufragios.",
                        "Con tenor de los escrutinios finales, el NO triunfó con casi el 57% de los sufragios."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["locuciones-prepositivas-pretexto-salvedad"],
                    "question": "¿Cuál de las siguientes frases denuncia una justificación autoritaria falsa?",
                    "options": [
                        "So pretexto de seguridad nacional, se pretendió perpetuar la tutela castrense sobre el Estado.",
                        "En aras de seguridad nacional, se pretendió perpetuar la tutela castrense sobre el Estado.",
                        "Conforme a seguridad nacional, se pretendió perpetuar la tutela castrense sobre el Estado.",
                        "De acuerdo con seguridad nacional, se pretendió perpetuar la tutela castrense sobre el Estado."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-uruguay-consolidation.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["regimen-preposicional-verbos-avanzados"],
                    "sentence": "Los debates ciudadanos versaron __ la ampliación de licencias parentales compartidas.",
                    "answer": "sobre",
                    "english": "Citizen debates dealt with the expansion of shared parental leaves."
                },
                {
                    "id": "b2-uruguay-consolidation.ex07",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-uruguay-vocab"],
                    "pairs": [
                        ["el sosiego cívico", "the civic tranquility / calm"],
                        ["la llamada ancestral", "the ancestral drum call"],
                        ["la matriz renovable", "the renewable energy grid"],
                        ["la llaneza republicana", "the republican unpretentiousness / modesty"]
                    ]
                },
                {
                    "id": "b2-uruguay-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la lección suprema que proyecta la experiencia democrática uruguaya ante la comunidad internacional?",
                    "options": [
                        "Que la verdadera grandeza histórica reside en la solidez de las instituciones y la convivencia pacífica.",
                        "Que los países pequeños deben supeditar su legislación a las decisiones de grandes potencias militares.",
                        "Que las reformas de derechos individuales son incompatibles con la estabilidad económica.",
                        "Que la laicidad estatal destruye las tradiciones populares barriales como el Carnaval."
                    ],
                    "correct": 0
                }
            ]
        }
    }

    for ex_stem, ex_obj in exercise_files.items():
        write_json(f"exercises/b2/{ex_stem}.json", ex_obj)

    # 7. Lessons (12 files)
    # Core Lessons: b2-27
    core_lessons = [
        ("b2-27-01", "Causal & Origin Locutions: a raíz de, en virtud de, con motivo de", "b2-27-01-a-gr", "b2-27-01-voc", "b2-27-01-ex", "stories/classics/b2/b2-27.json"),
        ("b2-27-02", "Conformity & Normative Locutions: conforme a, de acuerdo con, con arreglo a", "b2-27-02-a-gr", "b2-27-02-voc", "b2-27-02-ex", None),
        ("b2-27-03", "Purpose & Sacrifice Locutions: en aras de, con miras a, a costa de", "b2-27-03-a-gr", "b2-27-03-voc", "b2-27-03-ex", None),
        ("b2-27-04", "Pretext & Restrictive Locutions: so pretexto de, a juicio de, sin perjuicio de", "b2-27-04-a-gr", "b2-27-04-voc", "b2-27-04-ex", None),
        ("b2-27-05", "Advanced Verb Prepositional Regimes: estribar en, derivar en, versar sobre", "b2-27-05-a-gr", "b2-27-05-voc", "b2-27-05-ex", None)
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
    write_json("lessons/b2/b2-27-consolidation.json", {
        "id": "lesson.b2.27.consolidation",
        "title": "Consolidation: Advanced Prepositional Regimes & Prepositional Locutions",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Dominar las locuciones prepositivas de causa, conformidad, finalidad y pretexto en prosa formal B2.",
                "Aplicar con precisión los regímenes preposicionales obligatorios de verbos analíticos avanzados.",
                "Integrar el léxico especializado de la fundamentación jurídica, la normativa y el ensayo reflexivo."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-27-consolidation-ex.json", "exerciseRefs": [f"b2-27-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Distingo con rigor entre 'a raíz de' (hecho desencadenante) y 'en virtud de' (autoridad o potestad legal).",
                "Empleo 'conforme a', 'de acuerdo con' y 'con arreglo a' para fundamentar dictámenes y apego a normas.",
                "Sopeso fines y sacrificios mediante 'en aras de' (bien noble) y 'a costa de' (perjuicio gravoso).",
                "Denuncio justificaciones falaces mediante 'so pretexto de' y formulo salvedades con 'sin perjuicio de'.",
                "Domino los regímenes preposicionales de 'estribar en', 'derivar en', 'versar sobre' y 'abogar por'."
            ]}
        ]
    })

    # Regional Lessons: b2-uruguay
    regional_lessons = [
        ("b2-uruguay-01", "El batllismo y el Estado de bienestar: Modernidad institucional", "b2-uruguay-01-a-gr", "b2-uruguay-01-voc", "b2-uruguay-01-ex", "stories/world/b2/b2-uruguay-01.json"),
        ("b2-uruguay-02", "Candombe, comparsas y el Barrio Sur: La raíz afrouruguaya", "b2-uruguay-02-a-gr", "b2-uruguay-02-voc", "b2-uruguay-02-ex", "stories/world/b2/b2-uruguay-02.json"),
        ("b2-uruguay-03", "La dictadura cívico-militar y el plebiscito del NO de 1980", "b2-uruguay-03-a-gr", "b2-uruguay-03-voc", "b2-uruguay-03-ex", "stories/world/b2/b2-uruguay-03.json"),
        ("b2-uruguay-04", "Vanguardia de derechos y agenda verde: Cannabis, matrimonio y matriz limpia", "b2-uruguay-04-a-gr", "b2-uruguay-04-voc", "b2-uruguay-04-ex", "stories/world/b2/b2-uruguay-04.json"),
        ("b2-uruguay-05", "Montevideo, la rambla y la identidad oriental: Mate, tranquilidad y convivencia", "b2-uruguay-05-a-gr", "b2-uruguay-05-voc", "b2-uruguay-05-ex", "stories/world/b2/b2-uruguay-05.json")
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
    write_json("lessons/b2/b2-uruguay-consolidation.json", {
        "id": "lesson.b2.uruguay.consolidation",
        "title": "Consolidación: El pacto cívico y la convivencia oriental",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Integrar la perspectiva histórica, institucional y cultural de la singularidad democrática uruguaya.",
                "Consolidar el léxico del batllismo, el candombe, la resistencia cívica y la transición energética.",
                "Dominar el uso de locuciones prepositivas complejas y regímenes verbales en el ensayo sociológico."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b2/b2-uruguay-consolidation.json"},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-uruguay-consolidation-ex.json", "exerciseRefs": [f"b2-uruguay-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la trascendencia del modelo batllista en la creación del Estado de bienestar y la laicidad.",
                "Reconozco el valor espiritual e identitario del candombe como patrimonio inmaterial afrouruguayo.",
                "Valoro la hazaña cívica del plebiscito constitucional de 1980 en la recuperación democrática.",
                "Analizo la vanguardia uruguaya en derechos civiles, Plan Ceibal y descarbonización energética.",
                "Aprecio la liturgia del mate en la rambla montevideana y el credo igualitario de cercanía republicana.",
                "Aplico con precisión las locuciones 'en virtud de', 'conforme a', 'en aras de' y 'so pretexto de'."
            ]}
        ]
    })

    # 8. Update content/es-latam/curriculum/units/b2.json
    def update_curriculum_units(units):
        existing_titles = {u.get("title") for u in units}
        new_units = [
            {
                "title": "Advanced Prepositional Regimes & Prepositional Locutions",
                "stems": [
                    "b2-27-01",
                    "b2-27-02",
                    "b2-27-03",
                    "b2-27-04",
                    "b2-27-05",
                    "b2-27-consolidation"
                ],
                "track": "core"
            },
            {
                "title": "Uruguay: Secularism, Candombe & Progressive Institutions",
                "stems": [
                    "b2-uruguay-01",
                    "b2-uruguay-02",
                    "b2-uruguay-03",
                    "b2-uruguay-04",
                    "b2-uruguay-05",
                    "b2-uruguay-consolidation"
                ],
                "track": "regional"
            }
        ]
        for nu in new_units:
            if nu["title"] not in existing_titles:
                units.append(nu)
        return units

    update_json_file(os.path.join(LATAM_DIR, "curriculum", "units", "b2.json"), update_curriculum_units)
    print("Updated curriculum/units/b2.json with Unit 27!")

if __name__ == "__main__":
    main()
