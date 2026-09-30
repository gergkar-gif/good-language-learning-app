#!/usr/bin/env python3
"""
Generate Latin American Spanish (es-latam) B2 Unit 21:
- Core Unit 21: Impersonality & Strategic Distance (Impersonalidad sintáctica y distancia enunciativa)
  Classic literature: Augusto Céspedes - Sangre de mestizos (Relato: El pozo) (1936)
- Regional Unit 21: Bolivia II: The Lowlands, Eastern Amazonia & The Lithium Frontier (b2-boliviaoriente)
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
    c_unit = "b2-21"
    r_unit = "b2-boliviaoriente"

    c1, c2, c3, c4, c5, l6_con = [f"{c_unit}-0{i}" for i in range(1, 6)] + [f"{c_unit}-consolidation"]
    r1, r2, r3, r4, r5, r6_con = [f"{r_unit}-0{i}" for i in range(1, 6)] + [f"{r_unit}-consolidation"]

    # -------------------------------------------------------------------------
    # 0. UPDATE REGISTRY & GRAMMAR TITLES
    # -------------------------------------------------------------------------
    reg_path = LATAM_DIR / "indexes" / "skill-registry.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    skills = registry.setdefault("skills", {})

    new_skills = {
        "b2-21-vocab": {"kind": "vocabulary", "level": "B2"},
        "impersonal-tercera-plural-uno": {"kind": "grammar", "level": "B2"},
        "se-impersonal-avanzado": {"kind": "grammar", "level": "B2"},
        "nominalizacion-despersonalizacion": {"kind": "grammar", "level": "B2"},
        "verbos-impersonales-evaluativos": {"kind": "grammar", "level": "B2"},
        "distanciamiento-epistemico-atenuacion": {"kind": "grammar", "level": "B2"},
        "sintesis-impersonalidad-distancia": {"kind": "grammar", "level": "B2"},
        "b2-boliviaoriente-vocab": {"kind": "vocabulary", "level": "B2"},
        "bolivia-chiquitos-misiones-selva": {"kind": "grammar", "level": "B2"},
        "bolivia-santacruz-agroindustria-camba": {"kind": "grammar", "level": "B2"},
        "bolivia-uyuni-litio-geopolitica": {"kind": "grammar", "level": "B2"},
        "bolivia-guerra-chaco-nacionalismo": {"kind": "grammar", "level": "B2"},
        "bolivia-carnaval-oruro-folclore": {"kind": "grammar", "level": "B2"},
        "bolivia-oriente-sintesis-regional": {"kind": "grammar", "level": "B2"}
    }

    for k, v in new_skills.items():
        skills[k] = v

    reg_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated skill-registry.json for Unit 21")

    gt_path = LATAM_DIR / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))

    new_titles = {
        "impersonal-tercera-plural-uno": "third-person plural impersonals and indefinite uno",
        "se-impersonal-avanzado": "advanced impersonal se constructions",
        "nominalizacion-despersonalizacion": "nominalization for depersonalization and agency omission",
        "verbos-impersonales-evaluativos": "evaluative impersonal verbs in formal register",
        "distanciamiento-epistemico-atenuacion": "epistemic hedging and strategic distance",
        "sintesis-impersonalidad-distancia": "synthesis of impersonality and strategic distance",
        "bolivia-chiquitos-misiones-selva": "discourse connectors of cause and consequence in missionary history",
        "bolivia-santacruz-agroindustria-camba": "adversative and concessive markers in regional identity debates",
        "bolivia-uyuni-litio-geopolitica": "periphrases of probability and conjecture in natural resource discourse",
        "bolivia-guerra-chaco-nacionalismo": "retrospective conditional constructions in historical analysis",
        "bolivia-carnaval-oruro-folclore": "descriptive complex subordination in living folkloric traditions",
        "bolivia-oriente-sintesis-regional": "advanced discourse synthesis in lowlands and mineral horizons"
    }

    for k, v in new_titles.items():
        gt[k] = v

    gt_path.write_text(json.dumps(gt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json for Unit 21")

    # -------------------------------------------------------------------------
    # 1. VOCABULARY FILES (10 files)
    # -------------------------------------------------------------------------
    vocab_data = {
        f"{c_unit}-01": {
            "id": "vocab.b2.21.01",
            "lesson": f"{c_unit}-01",
            "title": "La impersonalidad y la generalización enunciativa",
            "words": [
                {"lemma": "enunciador", "translation": "speaker / enunciator", "pos": "noun"},
                {"lemma": "colectividad", "translation": "community / collectivity", "pos": "noun"},
                {"lemma": "trasfondo", "translation": "background / underlying context", "pos": "noun"},
                {"lemma": "anonimato", "translation": "anonymity", "pos": "noun"},
                {"lemma": "distanciamiento", "translation": "distancing / detachment", "pos": "noun"},
                {"lemma": "indefinido", "translation": "indefinite / unspecified", "pos": "adjective"},
                {"lemma": "desdibujar", "translation": "to blur / obscure", "pos": "verb"},
                {"lemma": "rumor", "translation": "rumor / hearsay", "pos": "noun"},
                {"lemma": "generalización", "translation": "generalization", "pos": "noun"}
            ]
        },
        f"{c_unit}-02": {
            "id": "vocab.b2.21.02",
            "lesson": f"{c_unit}-02",
            "title": "El 'se' impersonal y la gestión institucional",
            "words": [
                {"lemma": "intransitividad", "translation": "intransitivity", "pos": "noun"},
                {"lemma": "destinatario", "translation": "recipient / addressee", "pos": "noun"},
                {"lemma": "delegación", "translation": "delegation / branch", "pos": "noun"},
                {"lemma": "convocatoria", "translation": "official call / notice", "pos": "noun"},
                {"lemma": "estatuto", "translation": "statute / bylaw", "pos": "noun"},
                {"lemma": "normativa", "translation": "regulations / rules", "pos": "noun"},
                {"lemma": "protocolo", "translation": "protocol / procedure", "pos": "noun"},
                {"lemma": "despersonalizar", "translation": "to depersonalize", "pos": "verb"},
                {"lemma": "tramitación", "translation": "processing / procedure", "pos": "noun"}
            ]
        },
        f"{c_unit}-03": {
            "id": "vocab.b2.21.03",
            "lesson": f"{c_unit}-03",
            "title": "La nominalización y la concisión ensayística",
            "words": [
                {"lemma": "nominalización", "translation": "nominalization", "pos": "noun"},
                {"lemma": "promulgación", "translation": "enactment / promulgation", "pos": "noun"},
                {"lemma": "erradicación", "translation": "eradication", "pos": "noun"},
                {"lemma": "desestimación", "translation": "dismissal / rejection", "pos": "noun"},
                {"lemma": "subsanación", "translation": "remedying / correction", "pos": "noun"},
                {"lemma": "reestructuración", "translation": "restructuring", "pos": "noun"},
                {"lemma": "viabilidad", "translation": "viability / feasibility", "pos": "noun"},
                {"lemma": "implementación", "translation": "implementation", "pos": "noun"},
                {"lemma": "adjudicación", "translation": "allocation / awarding", "pos": "noun"}
            ]
        },
        f"{c_unit}-04": {
            "id": "vocab.b2.21.04",
            "lesson": f"{c_unit}-04",
            "title": "Verbos de necesidad y evaluación institucional",
            "words": [
                {"lemma": "incumbir", "translation": "to fall on / be the duty of", "pos": "verb"},
                {"lemma": "atañer", "translation": "to concern / relate to", "pos": "verb"},
                {"lemma": "constar", "translation": "to be registered / be clear", "pos": "verb"},
                {"lemma": "competer", "translation": "to be within one's remit", "pos": "verb"},
                {"lemma": "convenir", "translation": "to be advisable / suit", "pos": "verb"},
                {"lemma": "imperar", "translation": "to prevail / reign", "pos": "verb"},
                {"lemma": "urgencia", "translation": "urgency / emergency", "pos": "noun"},
                {"lemma": "pertinencia", "translation": "relevance / appropriateness", "pos": "noun"},
                {"lemma": "procedencia", "translation": "origin / admissibility", "pos": "noun"}
            ]
        },
        f"{c_unit}-05": {
            "id": "vocab.b2.21.05",
            "lesson": f"{c_unit}-05",
            "title": "Atenuación epistémica y cautela diplomática",
            "words": [
                {"lemma": "atenuación", "translation": "hedging / attenuation", "pos": "noun"},
                {"lemma": "presunción", "translation": "presumption / assumption", "pos": "noun"},
                {"lemma": "inferencia", "translation": "inference / deduction", "pos": "noun"},
                {"lemma": "conjetura", "translation": "conjecture / guess", "pos": "noun"},
                {"lemma": "cautela", "translation": "caution / prudence", "pos": "noun"},
                {"lemma": "plausibilidad", "translation": "plausibility", "pos": "noun"},
                {"lemma": "escepticismo", "translation": "skepticism", "pos": "noun"},
                {"lemma": "aserto", "translation": "assertion / claim", "pos": "noun"},
                {"lemma": "matiz", "translation": "nuance / shade", "pos": "noun"}
            ]
        },
        f"{r_unit}-01": {
            "id": "vocab.b2.boliviaoriente.01",
            "lesson": f"{r_unit}-01",
            "title": "Los llanos de Chiquitos y la herencia misional",
            "words": [
                {"lemma": "sabana", "translation": "savannah / grassland", "pos": "noun"},
                {"lemma": "serranía", "translation": "mountain ridge / highlands", "pos": "noun"},
                {"lemma": "chiquitanía", "translation": "Chiquitania region", "pos": "noun"},
                {"lemma": "oratorio", "translation": "oratorio / musical chapel", "pos": "noun"},
                {"lemma": "barroco", "translation": "baroque", "pos": "adjective"},
                {"lemma": "fresqueado", "translation": "fresco painting", "pos": "noun"},
                {"lemma": "espesura", "translation": "thicket / dense woods", "pos": "noun"},
                {"lemma": "reducción", "translation": "mission settlement / reduction", "pos": "noun"},
                {"lemma": "biodiversidad", "translation": "biodiversity", "pos": "noun"}
            ]
        },
        f"{r_unit}-02": {
            "id": "vocab.b2.boliviaoriente.02",
            "lesson": f"{r_unit}-02",
            "title": "Santa Cruz de la Sierra y la pujanza agroindustrial",
            "words": [
                {"lemma": "agroindustria", "translation": "agribusiness", "pos": "noun"},
                {"lemma": "camba", "translation": "lowland Bolivian / camba", "pos": "noun"},
                {"lemma": "oleaginosa", "translation": "oilseed crop / soy", "pos": "noun"},
                {"lemma": "desmonte", "translation": "land clearing / deforestation", "pos": "noun"},
                {"lemma": "hacienda", "translation": "estate / ranch", "pos": "noun"},
                {"lemma": "zafra", "translation": "harvest / sugar season", "pos": "noun"},
                {"lemma": "metrópoli", "translation": "metropolis", "pos": "noun"},
                {"lemma": "pujanza", "translation": "dynamism / economic strength", "pos": "noun"},
                {"lemma": "expansión", "translation": "expansion / growth", "pos": "noun"}
            ]
        },
        f"{r_unit}-03": {
            "id": "vocab.b2.boliviaoriente.03",
            "lesson": f"{r_unit}-03",
            "title": "El Salar de Uyuni y la encrucijada del litio",
            "words": [
                {"lemma": "salmuera", "translation": "brine", "pos": "noun"},
                {"lemma": "costra", "translation": "crust / salt layer", "pos": "noun"},
                {"lemma": "litio", "translation": "lithium", "pos": "noun"},
                {"lemma": "batería", "translation": "battery / accumulator", "pos": "noun"},
                {"lemma": "endorreico", "translation": "endorheic / closed basin", "pos": "adjective"},
                {"lemma": "evaporación", "translation": "evaporation", "pos": "noun"},
                {"lemma": "transición", "translation": "energy transition", "pos": "noun"},
                {"lemma": "yacimiento", "translation": "mineral deposit / field", "pos": "noun"},
                {"lemma": "geopolítica", "translation": "geopolitics", "pos": "noun"}
            ]
        },
        f"{r_unit}-04": {
            "id": "vocab.b2.boliviaoriente.04",
            "lesson": f"{r_unit}-04",
            "title": "La Guerra del Chaco y la forja de la memoria",
            "words": [
                {"lemma": "matorral", "translation": "scrubland / brush", "pos": "noun"},
                {"lemma": "sed", "translation": "thirst / dehydration", "pos": "noun"},
                {"lemma": "alambrada", "translation": "barbed wire fence", "pos": "noun"},
                {"lemma": "trinchera", "translation": "trench", "pos": "noun"},
                {"lemma": "beligerante", "translation": "belligerent / combatant", "pos": "noun"},
                {"lemma": "armisticio", "translation": "armistice / truce", "pos": "noun"},
                {"lemma": "fraternidad", "translation": "brotherhood / solidarity", "pos": "noun"},
                {"lemma": "desolación", "translation": "desolation / grief", "pos": "noun"},
                {"lemma": "veterano", "translation": "veteran", "pos": "noun"}
            ]
        },
        f"{r_unit}-05": {
            "id": "vocab.b2.boliviaoriente.05",
            "lesson": f"{r_unit}-05",
            "title": "El Carnaval de Oruro y la devoción danzada",
            "words": [
                {"lemma": "diablada", "translation": "diablada dance", "pos": "noun"},
                {"lemma": "morenada", "translation": "morenada dance", "pos": "noun"},
                {"lemma": "socavón", "translation": "mine tunnel / shaft", "pos": "noun"},
                {"lemma": "careta", "translation": "mask / ceremonial face", "pos": "noun"},
                {"lemma": "devoción", "translation": "devotion / piety", "pos": "noun"},
                {"lemma": "comparsa", "translation": "carnival troupe / ensemble", "pos": "noun"},
                {"lemma": "matraca", "translation": "rattle / noisemaker", "pos": "noun"},
                {"lemma": "bordado", "translation": "embroidery", "pos": "noun"},
                {"lemma": "sincretismo", "translation": "syncretism / cultural fusion", "pos": "noun"}
            ]
        }
    }

    for lid, vdata in vocab_data.items():
        write_json(f"vocabulary/b2/{lid}-voc.json", vdata)

    # -------------------------------------------------------------------------
    # 2. GRAMMAR FILES (10 files: 5 core, 5 regional - none for consolidation)
    # -------------------------------------------------------------------------
    grammar_data = {
        f"{c_unit}-01": {
            "id": f"grammar.b2.21.01.impersonal-tercera-plural-uno",
            "title": "La tercera persona del plural impersonal y el pronombre indefinido uno",
            "sections": [
                {
                    "type": "text",
                    "content": "En el registro formal y periodístico del español de América, existen diversas estrategias para desdibujar al agente de la acción cuando este es desconocido, irrelevante o se desea mantener en el anonimato. La tercera persona del plural sin sujeto expreso (*dicen que*, *comentan que*, *llaman a la puerta*) atribuye la acción a un colectivo indeterminado, mientras que el pronombre indefinido *uno / una* generaliza la experiencia humana proyectándola desde una perspectiva subjetiva pero compartible."
                },
                {
                    "type": "table",
                    "title": "Estrategias de impersonalidad y generalización",
                    "rows": [
                        ["Dicen que la delegación llegará mañana al mediodía.", "They say that the delegation will arrive tomorrow at noon."],
                        ["Tocan a la puerta a horas intempestivas.", "Someone is knocking at the door at unearthly hours."],
                        ["Cuando uno asume un cargo público, debe esperar escrutinio.", "When one assumes public office, one must expect scrutiny."],
                        ["En situaciones de crisis, una no sabe qué decisión tomar.", "In crisis situations, one (fem.) does not know what decision to take."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En la prosa académica estricta se prefiere la pasiva refleja o las nominalizaciones frente a *uno*, ya que este último conserva cierta cercanía conversacional. En América Latina, *uno* concuerda siempre en tercera persona singular con el verbo."
                }
            ]
        },
        f"{c_unit}-02": {
            "id": f"grammar.b2.21.02.se-impersonal-avanzado",
            "title": "El se impersonal avanzado y sus contrastes con la pasiva refleja",
            "sections": [
                {
                    "type": "text",
                    "content": "La partícula *se* permite construir oraciones estrictamente impersonales (sin sujeto gramatical alguno) tanto con verbos intransitivos (*se vive bien aquí*, *se trabaja hasta tarde*) como con verbos transitivos que llevan objeto directo de persona introducido por la preposición *a* (*se convocó a los ministros*, *se premió a las científicas*). Esta estructura se distingue tajantemente de la pasiva refleja (*se aprobaron las leyes*), donde el sintagma nominal concuerda en número con el verbo."
                },
                {
                    "type": "table",
                    "title": "Contraste: Se impersonal vs Pasiva refleja",
                    "rows": [
                        ["Se atendió a los damnificados con prontitud.", "The victims were assisted promptly (impersonal se + prep a)."],
                        ["Se premió a las mejores investigadoras del país.", "The best female researchers in the country were awarded."],
                        ["Se firmaron los tratados de cooperación bilateral.", "The bilateral cooperation treaties were signed (passive se + plural)."],
                        ["Se debate con serenidad en el consejo directivo.", "There is serene debate in the executive board (intransitive impersonal)."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Si el objeto es de persona y lleva preposición *a*, el verbo permanece rigurosamente en singular: *se entrevistó a los diplomáticos* (nunca *se entrevistaron a los diplomáticos*)."
                }
            ]
        },
        f"{c_unit}-03": {
            "id": f"grammar.b2.21.03.nominalizacion-despersonalizacion",
            "title": "La nominalización como recurso de despersonalización y concisión",
            "sections": [
                {
                    "type": "text",
                    "content": "La nominalización consiste en transformar un verbo o una cláusula entera en un sintagma nominal (*promulgar la ley* -> *la promulgación de la ley*; *destruir los bosques* -> *la destrucción de los bosques*). En el ensayo, los informes jurídicos y los editoriales periodísticos, este mecanismo permite omitir por completo a los causantes de una acción, condensar información densa y dotar al texto de un tono desapasionado y analítico."
                },
                {
                    "type": "table",
                    "title": "Transformación de cláusulas verbales en sintagmas nominalizados",
                    "rows": [
                        ["El gobierno promulgó el decreto de emergencia.", "La promulgación del decreto de emergencia calmó los mercados."],
                        ["La empresa reestructuró sus pasivos financieros.", "La reestructuración de los pasivos financieros facilitó el crédito."],
                        ["El tribunal desestimó la demanda por vicios formales.", "La desestimación de la demanda por vicios formales cerró el caso."],
                        ["Las brigadas erradicaron la plaga agrícola.", "La erradicación de la plaga agrícola garantizó la exportación."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Aunque la nominalización aporta rigor y distancia enunciativa, el abuso excesivo de sustantivos abstractos encadenados puede entorpecer la fluidez del texto. Combínala armónicamente con verbos precisos."
                }
            ]
        },
        f"{c_unit}-04": {
            "id": f"grammar.b2.21.04.verbos-impersonales-evaluativos",
            "title": "Verbos impersonales evaluativos y de necesidad institucional",
            "sections": [
                {
                    "type": "text",
                    "content": "Ciertos verbos terciopersonales actúan en construcciones impersonales para señalar necesidad, pertinencia, incumbencia o constatación fáctica. Verbos como *convenir*, *urgir*, *constar*, *atañer* e *incumbir* rigen oraciones subordinadas que seleccionan indicativo o subjuntivo según la naturaleza semántica de la matriz: certeza fáctica (*consta que + indicativo*) frente a valoración o directriz institucional (*conviene que / urge que + subjuntivo*)."
                },
                {
                    "type": "table",
                    "title": "Matrices impersonales de evaluación y selección de modo",
                    "rows": [
                        ["Conviene que el directorio evalúe el informe técnico.", "It is advisable that the board evaluate the technical report (subj)."],
                        ["Urge que se tomen medidas cautelares en la frontera.", "It is urgent that precautionary measures be taken at the border (subj)."],
                        ["Consta en actas que los comisionados votaron a favor.", "It is recorded in minutes that the commissioners voted in favor (ind)."],
                        ["Incumbe a las autoridades velar por la transparencia.", "It is incumbent upon the authorities to safeguard transparency (inf)."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Consta que* expresa evidencia probada e incontrovertible, por lo que exige modo indicativo. En cambio, *urge que* y *conviene que* conllevan una directriz o deseo institucional, exigiendo invariablemente subjuntivo."
                }
            ]
        },
        f"{c_unit}-05": {
            "id": f"grammar.b2.21.05.distanciamiento-epistemico-atenuacion",
            "title": "Distanciamiento epistémico y fórmulas de atenuación asertiva",
            "sections": [
                {
                    "type": "text",
                    "content": "En la redacción diplomática, pericial y académica avanzada, la aserción tajante se sustituye a menudo por fórmulas de atenuación o *hedging*. Estas estructuras permiten al autor modular su grado de compromiso con la verdad de una afirmación, manifestando cautela metodológica o cortesía discursiva mediante el condicional simple (*cabría inferir*, *se presumiría*), la pasiva de percepción (*parece desprenderse*) o adverbios de aproximación modal (*presumiblemente*, *en principio*)."
                },
                {
                    "type": "table",
                    "title": "Fórmulas de atenuación epistémica en la prosa crítica",
                    "rows": [
                        ["Cabría inferir que las partes alcanzaron un principio de acuerdo.", "One might infer that the parties reached an agreement in principle."],
                        ["De los datos disponibles parece desprenderse una tendencia positiva.", "From the available data a positive trend seems to emerge."],
                        ["Se presumiría que los desembolsos se realizaron conforme a ley.", "It would be presumed that the disbursements were made according to law."],
                        ["Resulta razonable suponer que habrá ajustes presupuestarios.", "It is reasonable to assume that there will be budgetary adjustments."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El uso del condicional de modestia (*cabría señalar*, *valdría la pena matizar*) es el estándar de oro en las reseñas académicas y ensayos latinoamericanos de nivel C1/B2 superior para polemizar con elegancia sin confrontación directa."
                }
            ]
        },
        f"{r_unit}-01": {
            "id": f"grammar.b2.boliviaoriente.01.conectores-causales-consecutivos",
            "title": "Conectores discursivos de causa y consecuencia en la prosa histórica",
            "sections": [
                {
                    "type": "text",
                    "content": "La narración sobre las misiones jesuíticas de Chiquitos y la colonización de las selvas orientales bolivianas exige conectar hechos remotos mediante conectores causales y consecutivos de registro formal. Nexos como *habida cuenta de que*, *dado que*, *por ende*, *por consiguiente* y *de modo que* permiten articular explicaciones históricas rigurosas sobre la supervivencia de este patrimonio barroco único."
                },
                {
                    "type": "table",
                    "title": "Conectores de causalidad y consecutividad histórica",
                    "rows": [
                        ["Habida cuenta de su aislamiento geográfico, los templos no fueron saqueados.", "Taking into account their geographical isolation, the temples were not looted."],
                        ["Los indígenas asimilaron el violín; por ende, conservaron las partituras.", "The indigenous people assimilated the violin; therefore, they preserved the scores."],
                        ["Dado que no se impuso una sustitución forzosa, floreció el barroco mestizo.", "Given that forced substitution was not imposed, mestizo baroque flourished."],
                        ["Las reducciones mantuvieron autonomía, de modo que sus tradiciones pervivieron.", "The missions retained autonomy, so that their traditions survived."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Habida cuenta de que* y *dado que* encabezan causas objetivas previas. En cambio, *por ende* y *por consiguiente* introducen deducciones o consecuencias lógicas directas en la oración siguiente."
                }
            ]
        },
        f"{r_unit}-02": {
            "id": f"grammar.b2.boliviaoriente.02.conectores-contraargumentativos-oriente",
            "title": "Marcadores contraargumentativos y concesivos en debates sociopolíticos",
            "sections": [
                {
                    "type": "text",
                    "content": "El análisis de las tensiones regionales entre el oriente agroindustrial cruceño (la cultura *camba*) y el occidente andino (la cultura *colla*) requiere un manejo sobrio de conectores contraargumentativos. Nexos como *no obstante*, *ahora bien*, *si bien es cierto que*, *en contrapartida* y *antes bien* permiten ponderar posturas divergentes sobre el modelo productivo, la autonomía departamental y la unidad del Estado."
                },
                {
                    "type": "table",
                    "title": "Marcadores de contraste y ponderación regional",
                    "rows": [
                        ["Santa Cruz lidera el PIB agrícola; no obstante, enfrenta críticas ambientales.", "Santa Cruz leads the agricultural GDP; nevertheless, it faces environmental critique."],
                        ["Si bien el desmonte genera divisas, amenaza la biodiversidad amazónica.", "Although deforestation generates foreign currency, it threatens Amazonian biodiversity."],
                        ["El occidente prioriza la reciprocidad comunal; en contrapartida, el oriente apuesta por el mercado.", "The west prioritizes communal reciprocity; in contrast, the east bets on the market."],
                        ["No se trata de un conflicto étnico; antes bien, refleja visiones de desarrollo.", "It is not an ethnic conflict; rather, it reflects contrasting visions of development."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Antes bien* introduce una corrección rectificativa que sustituye una premisa errónea por la correcta ('no X; antes bien, Y'). *En contrapartida* presenta un aspecto simétrico pero opuesto en una comparación equilibrada."
                }
            ]
        },
        f"{r_unit}-03": {
            "id": f"grammar.b2.boliviaoriente.03.perifrasis-probabilidad-conjetura",
            "title": "Perífrasis de probabilidad y conjetura en el discurso sobre recursos",
            "sections": [
                {
                    "type": "text",
                    "content": "Al debatir sobre las reservas de litio del Salar de Uyuni y el futuro de la transición energética global, los análisis técnicos emplean frecuentemente perífrasis modales de conjetura y probabilidad. Destacan *deber de + infinitivo* (conjetura basada en indicios), *venir a + infinitivo* (aproximación o estimación cuantitativa) y construcciones con *poder que + subjuntivo*."
                },
                {
                    "type": "table",
                    "title": "Perífrasis de conjetura y estimación técnica",
                    "rows": [
                        ["El Salar de Uyuni debe de albergar más de veinte millones de toneladas de litio.", "The Uyuni Salt Flat must harbor over twenty million tons of lithium (conjecture)."],
                        ["La industrialización estatal viene a representar un desafío tecnológico colosal.", "State industrialization comes to represent a colossal technological challenge."],
                        ["Puede que las inversiones conjuntas aceleren la producción de cátodos.", "It may be that joint investments accelerate cathode production (subj)."],
                        ["El costo de extracción debe de oscilar según la tecnología empleada.", "The extraction cost must fluctuate according to the technology employed."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda la distinción normativa fundamental: *deber + infinitivo* expresa obligación moral o legal (*el Estado debe proteger el salar*), mientras que *deber de + infinitivo* expresa suposición o probabilidad (*debe de ser el mayor salar del mundo*)."
                }
            ]
        },
        f"{r_unit}-04": {
            "id": f"grammar.b2.boliviaoriente.04.oraciones-condicionales-retrospectivas",
            "title": "Estructuras condicionales retrospectivas en el análisis histórico",
            "sections": [
                {
                    "type": "text",
                    "content": "El examen historiográfico de la Guerra del Chaco (1932–1935) recurre a esquemas condicionales retrospectivos o contrafácticos para evaluar decisiones estratégicas, desenlaces territoriales y el despertar de la conciencia social de los combatientes. El patrón *si + pluscuamperfecto de subjuntivo + condicional compuesto* se combina con la reducción preposicional de hipótesis (*de haber mediado...*, *de haberse sabido...*)."
                },
                {
                    "type": "table",
                    "title": "Estructuras condicionales y contrafácticas en la historia",
                    "rows": [
                        ["Si no hubiera mediado la escasez de agua, la resistencia de Boquerón habría durado más.", "If water scarcity had not intervened, the resistance at Boquerón would have lasted longer."],
                        ["De haberse conocido la verdadera geología petrolífera, no se habría librado la guerra.", "Had the true petroleum geology been known, the war would not have been fought."],
                        ["Si los soldados de distintas regiones no hubieran compartido la trinchera, la revolución del 52 habría tardado décadas.", "Had soldiers from different regions not shared the trench, the '52 revolution would have taken decades."],
                        ["De haber existido caminos transitables, el abastecimiento habría sido eficiente.", "Had passable roads existed, logistics would have been efficient."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "La fórmula *de + infinitivo compuesto* (*de haber sabido*, *de haberse firmado*) es muy frecuente en la historiografía académica latinoamericana para condensar elegantes oraciones condicionales irreales pasadas."
                }
            ]
        },
        f"{r_unit}-05": {
            "id": f"grammar.b2.boliviaoriente.05.subordinadas-descriptivas-folclore",
            "title": "Subordinación descriptiva compleja en la narrativa etnográfica",
            "sections": [
                {
                    "type": "text",
                    "content": "La crónica etnográfica sobre el Carnaval de Oruro —Obra Maestra del Patrimonio Oral e Intangible de la Humanidad— despliega oraciones de relativo complejas con preposiciones compuestas (*a cuyos pies*, *en cuyas máscaras*, *al compás de cuyos sones*) y subordinadas participiales para recrear la exuberancia sensorial y el sincretismo espiritual de la Diablada y la Morenada."
                },
                {
                    "type": "table",
                    "title": "Relativos con preposición y subordinación multisensorial",
                    "rows": [
                        ["El santuario del Socavón, a cuyos pies danzan miles de devotos, resplandece de cirios.", "The Socavón sanctuary, at whose feet thousands of devotees dance, shines with candles."],
                        ["Los diablos y arcángeles, en cuyas máscaras brillan espejos y dragones, bajan en tropel.", "The devils and archangels, on whose masks mirrors and dragons glitter, descend in hordes."],
                        ["Las comparsas de morenos avanzan al compás de cuyas matracas retumba la plaza.", "The troupes of morenos advance to the rhythm of whose noisemakers the square resounds."],
                        ["Es un rito milenario mediante el cual la fe católica y la Pachamama se entrelazan.", "It is an ancient ritual through which Catholic faith and Pachamama intertwine."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El pronombre relativo posesivo *cuyo/cuya/cuyos/cuyas* concuerda siempre en género y número con el sustantivo que le sigue (el objeto poseído), nunca con su antecedente: *los danzantes, cuyas máscaras...*; *el templo, a cuyos pies...*."
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
                    ["enunciador", "speaker or producer of utterance"],
                    ["colectividad", "community or collective body"],
                    ["trasfondo", "background or underlying context"],
                    ["anonimato", "state of remaining unnamed"]
                ],
                "teaches": ["b2-21-vocab"]
            },
            {
                "id": f"{c1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En situaciones de emergencia institucional, __ no puede perder la serenidad. (uno)",
                "answer": "uno",
                "english": "In institutional emergency situations, one cannot lose serenity.",
                "teaches": ["impersonal-tercera-plural-uno"]
            },
            {
                "id": f"{c1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué efecto comunicativo produce la tercera persona del plural en 'Comentan que renegociarán el contrato'?",
                "options": [
                    "Atribuye el rumor a una fuente indeterminada eludiendo la responsabilidad del hablante.",
                    "Señala a tres negociadores específicos que firmaron el documento público.",
                    "Expresa una orden perentoria dirigida a los directores de la empresa.",
                    "Describe un hecho pasado consumado que no admite rectificación alguna."
                ],
                "correct": 0,
                "teaches": ["impersonal-tercera-plural-uno"]
            },
            {
                "id": f"{c1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Dicen", "que", "la", "comisión", "arribará", "esta", "tarde."],
                "solution": ["Dicen", "que", "la", "comisión", "arribará", "esta", "tarde."],
                "english": "They say that the committee will arrive this afternoon.",
                "teaches": ["impersonal-tercera-plural-uno"]
            },
            {
                "id": f"{c1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Quién filtró las conclusiones preliminares del informe pericial?"},
                    {"speaker": "Vocero", "text": "En los pasillos _____ que provino de un asesor externo independiente."}
                ],
                "options": [
                    "comentan",
                    "comenta uno",
                    "están comentado",
                    "se comente"
                ],
                "correct": 0,
                "teaches": ["impersonal-tercera-plural-uno"]
            },
            {
                "id": f"{c1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Tocan a la puerta a horas imprevistas durante la madrugada.",
                "english": "Someone is knocking at the door at unforeseen hours during dawn.",
                "teaches": ["impersonal-tercera-plural-uno"]
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
                    ["destinatario", "recipient of official notice"],
                    ["normativa", "regulatory body of rules"],
                    ["protocolo", "established formal procedure"],
                    ["tramitación", "administrative processing"]
                ],
                "teaches": ["b2-21-vocab"]
            },
            {
                "id": f"{c2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la sesión extraordinaria se __ a los peritos extranjeros con deferencia. (recibió)",
                "answer": "recibió",
                "english": "In the extraordinary session, foreign experts were received with deference.",
                "teaches": ["se-impersonal-avanzado"]
            },
            {
                "id": f"{c2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué es agramatical en la norma culta decir '*Se condecoraron a las maestras ilustres'?",
                "options": [
                    "Porque al haber preposición 'a' de persona, el sintagma es objeto directo y el verbo impersonal debe ir en singular.",
                    "Porque las maestras no pueden recibir condecoraciones estatales sin previa ley del congreso.",
                    "Porque el verbo condecorar exige conjugarse siempre en tiempo presente de subjuntivo.",
                    "Porque falta añadir un complemento agente obligatorio introducido por la preposición por."
                ],
                "correct": 0,
                "teaches": ["se-impersonal-avanzado"]
            },
            {
                "id": f"{c2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "atendió", "a", "los", "damnificados", "en", "el", "hospital."],
                "solution": ["Se", "atendió", "a", "los", "damnificados", "en", "el", "hospital."],
                "english": "The victims were assisted in the hospital.",
                "teaches": ["se-impersonal-avanzado"]
            },
            {
                "id": f"{c2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Abogada", "text": "¿Cómo procedió el tribunal con los testigos convocados?"},
                    {"speaker": "Secretario", "text": "Durante la mañana _____ a cada testigo en audiencia reservada."}
                ],
                "options": [
                    "se interrogó",
                    "se interrogaron",
                    "fueron interrogado",
                    "se interroga a"
                ],
                "correct": 0,
                "teaches": ["se-impersonal-avanzado"]
            },
            {
                "id": f"{c2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se convocó a los ministros para evaluar la emergencia climática.",
                "english": "The ministers were summoned to evaluate the climate emergency.",
                "teaches": ["se-impersonal-avanzado"]
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
                    ["promulgación", "official enactment of statute"],
                    ["erradicación", "complete removal or destruction"],
                    ["subsanación", "formal correction of flaws"],
                    ["adjudicación", "official granting of contract"]
                ],
                "teaches": ["b2-21-vocab"]
            },
            {
                "id": f"{c3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La __ del decreto supremo restableció la calma en los mercados financieros. (promulgación)",
                "answer": "promulgación",
                "english": "The enactment of the supreme decree restored calm in the financial markets.",
                "teaches": ["nominalizacion-despersonalizacion"]
            },
            {
                "id": f"{c3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la principal ventaja estilística de la nominalización en el ensayo académico?",
                "options": [
                    "Permite condensar procesos complejos despersonalizando al agente y otorgando densidad teórica.",
                    "Multiplica el número de páginas de un manuscrito sin necesidad de aportar datos empíricos.",
                    "Sustituye la necesidad de consultar bibliografía de autores contemporáneos.",
                    "Garantiza que el texto pueda traducirse automáticamente a lenguas germánicas."
                ],
                "correct": 0,
                "teaches": ["nominalizacion-despersonalizacion"]
            },
            {
                "id": f"{c3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "desestimación", "del", "recurso", "cerró", "el", "litigio", "judicial."],
                "solution": ["La", "desestimación", "del", "recurso", "cerró", "el", "litigio", "judicial."],
                "english": "The dismissal of the appeal closed the legal litigation.",
                "teaches": ["nominalizacion-despersonalizacion"]
            },
            {
                "id": f"{c3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Auditor", "text": "¿Por qué demoró tanto el desembolso de los fondos de inversión?"},
                    {"speaker": "Gerenta", "text": "La _____ de las observaciones contables tomó más de tres meses."}
                ],
                "options": [
                    "subsanación",
                    "subsanar",
                    "subsanado",
                    "subsana"
                ],
                "correct": 0,
                "teaches": ["nominalizacion-despersonalizacion"]
            },
            {
                "id": f"{c3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La reestructuración de la deuda pública facilitó nuevos créditos multilaterales.",
                "english": "The restructuring of public debt facilitated new multilateral credits.",
                "teaches": ["nominalizacion-despersonalizacion"]
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
                    ["incumbir", "to fall upon as formal duty"],
                    ["atañer", "to concern or have relevance to"],
                    ["constar", "to be recorded as verified fact"],
                    ["imperar", "to reign or prevail as condition"]
                ],
                "teaches": ["b2-21-vocab"]
            },
            {
                "id": f"{c4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Consta en actas que los comisionados __ por unanimidad a favor del dictamen. (votaron)",
                "answer": "votaron",
                "english": "It is recorded in minutes that the commissioners voted unanimously in favor of the report.",
                "teaches": ["verbos-impersonales-evaluativos"]
            },
            {
                "id": f"{c4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la matriz impersonal 'Urge que...' rige obligatoriamente modo subjuntivo?",
                "options": [
                    "Porque introduce una directriz, mandato o necesidad institucional apremiante que aún no se consuma.",
                    "Porque describe una acción que ya ocurrió en el pasado bajo supervisión judicial.",
                    "Porque expresa una duda subjetiva sobre la existencia de los funcionarios encargados.",
                    "Porque el verbo urgir solo existe en lengua española en tiempos compuestos."
                ],
                "correct": 0,
                "teaches": ["verbos-impersonales-evaluativos"]
            },
            {
                "id": f"{c4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Conviene", "que", "el", "directorio", "revise", "el", "balance", "anual."],
                "solution": ["Conviene", "que", "el", "directorio", "revise", "el", "balance", "anual."],
                "english": "It is advisable that the board review the annual balance sheet.",
                "teaches": ["verbos-impersonales-evaluativos"]
            },
            {
                "id": f"{c4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Senador", "text": "¿A qué institución le corresponde fiscalizar estos comicios?"},
                    {"speaker": "Jurista", "text": "Incumbe al órgano electoral autónomo _____ las garantías del proceso."}
                ],
                "options": [
                    "precautelar",
                    "precautela",
                    "precautelaran",
                    "precautelando"
                ],
                "correct": 0,
                "teaches": ["verbos-impersonales-evaluativos"]
            },
            {
                "id": f"{c4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Urge que se tomen medidas cautelares para proteger el patrimonio arqueológico.",
                "english": "It is urgent that precautionary measures be taken to protect archaeological heritage.",
                "teaches": ["verbos-impersonales-evaluativos"]
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
                    ["atenuación", "hedging or discursive softening"],
                    ["presunción", "assumption based on probability"],
                    ["inferencia", "logical deduction from data"],
                    ["cautela", "prudence and analytical care"]
                ],
                "teaches": ["b2-21-vocab"]
            },
            {
                "id": f"{c5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A la luz de los antecedentes periciales, __ inferir una tendencia favorable. (cabría)",
                "answer": "cabría",
                "english": "In light of forensic background events, one might infer a favorable trend.",
                "teaches": ["distanciamiento-epistemico-atenuacion"]
            },
            {
                "id": f"{c5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el condicional de modestia en 'Cabría presumir que las partes concertaron un armisticio'?",
                "options": [
                    "Atenúa la aserción expresando cautela epistémica para modular la responsabilidad del analista.",
                    "Expresa un reproche furioso por la falta de información disponible en el frente.",
                    "Obliga a los embajadores a firmar el tratado antes del anochecer.",
                    "Indica una certeza incontrovertible que no tolera ninguna objeción metodológica."
                ],
                "correct": 0,
                "teaches": ["distanciamiento-epistemico-atenuacion"]
            },
            {
                "id": f"{c5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["De", "las", "cifras", "parece", "desprenderse", "un", "crecimiento", "constante."],
                "solution": ["De", "las", "cifras", "parece", "desprenderse", "un", "crecimiento", "constante."],
                "english": "From the figures a steady growth seems to emerge.",
                "teaches": ["distanciamiento-epistemico-atenuacion"]
            },
            {
                "id": f"{c5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diplomática", "text": "¿Es posible afirmar que el acuerdo comercial entrará en vigencia pronto?"},
                    {"speaker": "Canciller", "text": "Resulta prudente matizar; _____ que aún quedan anexos técnicos por dirimir."}
                ],
                "options": [
                    "se presumiría",
                    "se presume a",
                    "presumiéndose",
                    "es presumir"
                ],
                "correct": 0,
                "teaches": ["distanciamiento-epistemico-atenuacion"]
            },
            {
                "id": f"{c5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Cabría conjeturar que las reformas tributarias tendrán un efecto distributivo equilibrado.",
                "english": "One might conjecture that tax reforms will have a balanced distributive effect.",
                "teaches": ["distanciamiento-epistemico-atenuacion"]
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
                    ["plausibilidad", "quality of being credible"],
                    ["desestimación", "formal rejection of lawsuit"],
                    ["subsanación", "remedying of legal flaws"],
                    ["aserto", "affirmative proposition or claim"]
                ],
                "teaches": ["b2-21-vocab"]
            },
            {
                "id": f"{c_unit}-con.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la cumbre internacional se __ a las delegaciones con honores de estado. (agasajó)",
                "answer": "agasajó",
                "english": "At the international summit, the delegations were entertained with state honors.",
                "teaches": ["se-impersonal-avanzado"]
            },
            {
                "id": f"{c_unit}-con.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál de las siguientes transformaciones nominalizadas aporta mayor concisión formal?",
                "options": [
                    "La promulgación de la ley minera aceleró las inversiones productivas.",
                    "El hecho de que promulgaran la ley minera causó que se invirtiera más.",
                    "Cuando el parlamento promulgó la ley, las inversiones comenzaron a subir.",
                    "Promulgar leyes es algo que el parlamento siempre hace con mucha rapidez."
                ],
                "correct": 0,
                "teaches": ["nominalizacion-despersonalizacion"]
            },
            {
                "id": f"{c_unit}-con.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "procedió", "a", "la", "revisión", "de", "las", "actas", "oficiales."],
                "solution": ["Se", "procedió", "a", "la", "revisión", "de", "las", "actas", "oficiales."],
                "english": "They proceeded to the review of the official minutes.",
                "teaches": ["sintesis-impersonalidad-distancia"]
            },
            {
                "id": f"{c_unit}-con.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministro", "text": "¿Consta en el expediente la ratificación del protocolo?"},
                    {"speaker": "Secretaria", "text": "Sí, señor ministro; _____ fehacientemente que fue depositado a tiempo."}
                ],
                "options": [
                    "consta",
                    "conste",
                    "constara",
                    "esté constando"
                ],
                "correct": 0,
                "teaches": ["verbos-impersonales-evaluativos"]
            },
            {
                "id": f"{c_unit}-con.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Cabría inferir que las reformas institucionales fortalecerán la transparencia pública.",
                "english": "One might infer that institutional reforms will strengthen public transparency.",
                "teaches": ["distanciamiento-epistemico-atenuacion"]
            },
            {
                "id": f"{c_unit}-con.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué valor confiere la despersonalización y el distanciamiento enunciativo a la prosa ensayística?",
                "options": [
                    "Permite fundamentar las conclusiones en la consistencia de los argumentos y las pruebas objetivas.",
                    "Oculta la identidad del autor para evitar responsabilidades civiles ante los tribunales.",
                    "Garantiza que el texto sea aceptado sin revisión por las editoriales universitarias.",
                    "Aumenta la longitud de los párrafos para cumplir con normas de extensión académica."
                ],
                "correct": 0
            },
            {
                "id": f"{c_unit}-con.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la combinatoria sintáctica idónea para expresar distanciamiento en un dictamen pericial?",
                "options": [
                    "Amalgamar impersonales terciopersonales, nominalizaciones desagentivadas y condicionales de atenuación.",
                    "Utilizar exclusivamente la primera persona del singular acompañada de adjetivos superlativos.",
                    "Redactar oraciones imperativas directas dirigidas a la autoridad judicial.",
                    "Evitar el uso de verbos transitivos en todo el cuerpo del documento."
                ],
                "correct": 0,
                "teaches": ["sintesis-impersonalidad-distancia"]
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
                    ["Chiquitanía", "tropical savannah and dry forest region"],
                    ["oratorio", "musical chapel or sacred composition"],
                    ["barroco", "elaborate mestizo artistic style"],
                    ["espesura", "dense forest thicket"]
                ],
                "teaches": ["b2-boliviaoriente-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los cabildos indígenas conservaron los archivos musicales; por __, las partituras pervivieron. (ende)",
                "answer": "ende",
                "english": "Indigenous town councils preserved the musical archives; therefore, the scores survived.",
                "teaches": ["bolivia-chiquitos-misiones-selva"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué conector causal de registro culto encabeza adecuadamente '___ las misiones se hallaban aisladas de los centros mineros, sus templos no fueron desmantelados'?",
                "options": [
                    "Habida cuenta de que",
                    "Por consiguiente",
                    "De modo que",
                    "Por ende"
                ],
                "correct": 0,
                "teaches": ["bolivia-chiquitos-misiones-selva"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Dado", "que", "hubo", "cuidado", "comunitario", "sobrevivió", "el", "barroco."],
                "solution": ["Dado", "que", "hubo", "cuidado", "comunitario", "sobrevivió", "el", "barroco."],
                "english": "Given that there was communal care, baroque survived.",
                "teaches": ["bolivia-chiquitos-misiones-selva"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Musicóloga", "text": "¿Cómo llegaron estas sonatas barrocas intactas hasta el siglo veintiuno?"},
                    {"speaker": "Luthier", "text": "Los músicos del cabildo las transcribieron fielmente; _____ se conservaron miles de partituras."}
                ],
                "options": [
                    "por ende",
                    "antes bien",
                    "no obstante",
                    "si bien"
                ],
                "correct": 0,
                "teaches": ["bolivia-chiquitos-misiones-selva"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las misiones jesuíticas de Chiquitos custodian templos barrocos de madera tallada.",
                "english": "The Jesuit missions of Chiquitos safeguard baroque temples of carved wood.",
                "teaches": ["bolivia-chiquitos-misiones-selva"]
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
                    ["camba", "identity of Bolivian lowlands"],
                    ["agroindustria", "large scale agricultural business"],
                    ["desmonte", "clearing of forest land"],
                    ["pujanza", "dynamic economic vigor"]
                ],
                "teaches": ["b2-boliviaoriente-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La producción agrícola genera divisas; no __, los desmontes acelerados amenazan la biodiversidad. (obstante)",
                "answer": "obstante",
                "english": "Agricultural production generates foreign exchange; nevertheless, accelerated land clearing threatens biodiversity.",
                "teaches": ["bolivia-santacruz-agroindustria-camba"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué matiz semántico aporta la locución 'en contrapartida' al contrastar las economías andina y oriental?",
                "options": [
                    "Introduce un contrapeso equilibrado entre dos modelos productivos complementarios.",
                    "Indica una consecuencia desastrosa inevitable para la agricultura campesina.",
                    "Niega que exista alguna actividad comercial fuera de las ciudades capitales.",
                    "Expresa una orden judicial de clausura para las haciendas ganaderas."
                ],
                "correct": 0,
                "teaches": ["bolivia-santacruz-agroindustria-camba"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Si", "bien", "hay", "prosperidad", "surgen", "desafíos", "ambientales."],
                "solution": ["Si", "bien", "hay", "prosperidad", "surgen", "desafíos", "ambientales."],
                "english": "Although there is prosperity, environmental challenges arise.",
                "teaches": ["bolivia-santacruz-agroindustria-camba"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Socióloga", "text": "¿Es la tensión regional un obstáculo insalvable para el país?"},
                    {"speaker": "Economista", "text": "No se trata de una ruptura irreversible; _____ expresa modelos de desarrollo complementarios."}
                ],
                "options": [
                    "antes bien",
                    "por ende",
                    "dado que",
                    "de modo que"
                ],
                "correct": 0,
                "teaches": ["bolivia-santacruz-agroindustria-camba"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Santa Cruz de la Sierra se consolidó como el motor agropecuario de Bolivia.",
                "english": "Santa Cruz de la Sierra established itself as the agricultural engine of Bolivia.",
                "teaches": ["bolivia-santacruz-agroindustria-camba"]
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
                    ["salmuera", "mineral rich concentrated salt solution"],
                    ["litio", "lightweight alkali metal for batteries"],
                    ["endorreico", "closed drainage basin without sea outlet"],
                    ["geopolítica", "geographical influence on power politics"]
                ],
                "teaches": ["b2-boliviaoriente-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El Salar de Uyuni debe __ albergar más de veinte millones de toneladas de litio. (de)",
                "answer": "de",
                "english": "The Uyuni Salt Flat must harbor over twenty million tons of lithium.",
                "teaches": ["bolivia-uyuni-litio-geopolitica"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la diferencia normativa entre 'debe industrializar' y 'debe de contener'?",
                "options": [
                    "'Debe' indica obligación o imperativo moral; 'debe de' expresa conjetura o probabilidad fundada en indicios.",
                    "'Debe' expresa una probabilidad lejana; 'debe de' impone un mandato legal del poder ejecutivo.",
                    "Ambas fórmulas son idénticas y pueden intercambiarse sin alterar el significado en ningún caso.",
                    "Ninguna de las dos perífrasis es admitida por las academias de la lengua en registros cultos."
                ],
                "correct": 0,
                "teaches": ["bolivia-uyuni-litio-geopolitica"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "planta", "piloto", "viene", "a", "representar", "un", "hito", "estratégico."],
                "solution": ["La", "planta", "piloto", "viene", "a", "representar", "un", "hito", "estratégico."],
                "english": "The pilot plant comes to represent a strategic milestone.",
                "teaches": ["bolivia-uyuni-litio-geopolitica"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ingeniero", "text": "¿Es factible implementar la extracción directa sin agotar los acuíferos?"},
                    {"speaker": "Científica", "text": "Puede que esa tecnología _____ el consumo hídrico de manera significativa."}
                ],
                "options": [
                    "reduzca",
                    "reduce",
                    "reduciría",
                    "haya reducido a"
                ],
                "correct": 0,
                "teaches": ["bolivia-uyuni-litio-geopolitica"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El Salar de Uyuni es el espejo natural más extenso del planeta.",
                "english": "The Uyuni Salt Flat is the most extensive natural mirror on the planet.",
                "teaches": ["bolivia-uyuni-litio-geopolitica"]
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
                    ["matorral", "dry thorny scrub vegetation"],
                    ["trinchera", "defensive military earth excavation"],
                    ["armisticio", "formal agreement to cease hostilities"],
                    ["fraternidad", "brotherhood forged in common hardship"]
                ],
                "teaches": ["b2-boliviaoriente-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "De __ mediado agua potable en el fortín, la resistencia de Boquerón habría durado más. (haber)",
                "answer": "haber",
                "english": "Had drinking water intervened in the fort, the resistance at Boquerón would have lasted longer.",
                "teaches": ["bolivia-guerra-chaco-nacionalismo"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué esquema condicional retrospectivo evalúa rigurosamente una hipótesis sobre la Guerra del Chaco?",
                "options": [
                    "Si los monopolios foráneos no hubieran presionado a los gobiernos, la guerra no se habría desatado.",
                    "Si los monopolios no presionan a los gobiernos, la guerra no se desata en el futuro.",
                    "De no presionar los monopolios, la guerra no se desataría en estos momentos.",
                    "Por haber presionado los monopolios, la guerra se desató el siglo pasado."
                ],
                "correct": 0,
                "teaches": ["bolivia-guerra-chaco-nacionalismo"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["De", "haberse", "evitado", "la", "guerra", "habrían", "salvado", "vidas."],
                "solution": ["De", "haberse", "evitado", "la", "guerra", "habrían", "salvado", "vidas."],
                "english": "Had the war been avoided, lives would have been saved.",
                "teaches": ["bolivia-guerra-chaco-nacionalismo"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Habría triunfado la revolución de 1952 sin la experiencia del Chaco?"},
                    {"speaker": "Profesor", "text": "Si los combatientes no hubieran convivido en las trincheras, no _____ la conciencia nacional."}
                ],
                "options": [
                    "habría despertado",
                    "despertaría",
                    "hubiera de despertar",
                    "despierta"
                ],
                "correct": 0,
                "teaches": ["bolivia-guerra-chaco-nacionalismo"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "En las arenas del Chaco los soldados forjaron una fraternidad inquebrantable.",
                "english": "In the sands of the Chaco, the soldiers forged an unbreakable brotherhood.",
                "teaches": ["bolivia-guerra-chaco-nacionalismo"]
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
                    ["diablada", "dramatic masked dance of good and evil"],
                    ["morenada", "dance honoring Afro-Bolivian historical roots"],
                    ["matraca", "wooden rattle carried by moreno dancers"],
                    ["sincretismo", "blending of Catholic and Andean beliefs"]
                ],
                "teaches": ["b2-boliviaoriente-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La Virgen del Socavón, a __ devoción bailan miles de mineros, es la patrona de Oruro. (cuya)",
                "answer": "cuya",
                "english": "The Virgin of the Socavón, to whose devotion thousands of miners dance, is the patroness of Oruro.",
                "teaches": ["bolivia-carnaval-oruro-folclore"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Con qué elemento debe concordar en género y número el pronombre relativo posesivo 'cuyo'?",
                "options": [
                    "Siempre con el sustantivo que le sigue inmediatamente (el término poseído), nunca con el antecedente.",
                    "Siempre con el sustantivo antecedente que aparece antes de la coma o preposición.",
                    "Siempre en masculino singular por ser una partícula invariable en lengua formal.",
                    "Con el sujeto gramatical de la oración principal independientemente de su posición."
                ],
                "correct": 0,
                "teaches": ["bolivia-carnaval-oruro-folclore"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "danzantes", "cuyas", "caretas", "relucen", "desfilan", "por", "horas."],
                "solution": ["Los", "danzantes", "cuyas", "caretas", "relucen", "desfilan", "por", "horas."],
                "english": "The dancers whose masks glitter parade for hours.",
                "teaches": ["bolivia-carnaval-oruro-folclore"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Turista", "text": "¿Qué representan las bandas de música que acompañan a las fraternidades?"},
                    {"speaker": "Guía", "text": "Son conjuntos orureños al compás de _____ sones retumba toda la avenida cívica."}
                ],
                "options": [
                    "cuyos",
                    "cuyas",
                    "cuyo",
                    "cuya"
                ],
                "correct": 0,
                "teaches": ["bolivia-carnaval-oruro-folclore"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El Carnaval de Oruro fue proclamado obra maestra del patrimonio oral de la humanidad.",
                "english": "The Carnival of Oruro was proclaimed a masterpiece of the oral heritage of humanity.",
                "teaches": ["bolivia-carnaval-oruro-folclore"]
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
                    ["zafra", "sugar cane harvest period"],
                    ["camba", "inhabitant of the eastern lowlands"],
                    ["salmuera", "lithium bearing mineral brine"],
                    ["trinchera", "defensive trench of Chaco War"]
                ],
                "teaches": ["b2-boliviaoriente-vocab"]
            },
            {
                "id": f"{r_unit}-con.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los templos misionales conservaron sus archivos; por __, la música sacra llegó viva a nuestros días. (ende)",
                "answer": "ende",
                "english": "The missionary temples preserved their archives; therefore, sacred music reached our days alive.",
                "teaches": ["bolivia-chiquitos-misiones-selva"]
            },
            {
                "id": f"{r_unit}-con.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función cumple el conector 'no obstante' al analizar el despegue económico cruceño?",
                "options": [
                    "Introduce un contraste o contraargumento fundamental respecto a los impactos ambientales del desmonte.",
                    "Indica una consecuencia matemática previsible sobre los precios mundiales de la soya.",
                    "Ordena cronológicamente los decretos coloniales que fundaron las reducciones jesuíticas.",
                    "Expresa una orden perentoria dirigida a los exportadores de carne bovina."
                ],
                "correct": 0,
                "teaches": ["bolivia-santacruz-agroindustria-camba"]
            },
            {
                "id": f"{r_unit}-con.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["De", "haberse", "conocido", "el", "terreno", "habrían", "trazado", "otra", "ruta."],
                "solution": ["De", "haberse", "conocido", "el", "terreno", "habrían", "trazado", "otra", "ruta."],
                "english": "Had the terrain been known, they would have traced another route.",
                "teaches": ["bolivia-guerra-chaco-nacionalismo"]
            },
            {
                "id": f"{r_unit}-con.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Geólogo", "text": "¿Es posible cuantificar con exactitud el litio de Uyuni?"},
                    {"speaker": "Ministra", "text": "Las salmueras _____ albergar más de veintiún millones de toneladas métricas."}
                ],
                "options": [
                    "deben de",
                    "deben a",
                    "debieron que",
                    "debiendo"
                ],
                "correct": 0,
                "teaches": ["bolivia-uyuni-litio-geopolitica"]
            },
            {
                "id": f"{r_unit}-con.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Bolivia integra las alturas andinas con la inmensidad fértil de las llanuras orientales.",
                "english": "Bolivia integrates the Andean heights with the fertile vastness of the eastern lowlands.",
                "teaches": ["bolivia-oriente-sintesis-regional"]
            },
            {
                "id": f"{r_unit}-con.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "¿Qué síntesis territorial y cultural define a la Bolivia del siglo XXI según el estudio regional?",
                "options": [
                    "La integración complementaria entre la memoria y cosmovisión andina y el dinamismo productivo de las tierras bajas.",
                    "La fragmentación inevitable del territorio nacional en cuatro estados soberanos separados.",
                    "El abandono de todas las actividades agrícolas para concentrarse en la minería tradicional de plata.",
                    "La clausura definitiva de todos los festivales de música sacra en la Chiquitanía."
                ],
                "correct": 0
            },
            {
                "id": f"{r_unit}-con.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué estructura sintáctica permite entrelazar antecedentes sagrados con descripciones etnográficas solemnes?",
                "options": [
                    "Cláusulas de relativo complejo con el pronombre posesivo cuyo precedido de locuciones prepositivas.",
                    "Oraciones subordinadas adverbiales de tiempo introducidas exclusivamente por 'en cuanto'.",
                    "Oraciones interrogativas directas seguidas de signos de exclamación enfáticos.",
                    "Sintagmas nominales aislados sin ningún tipo de núcleo verbal o concordancia de género."
                ],
                "correct": 0,
                "teaches": ["bolivia-carnaval-oruro-folclore"]
            }
        ]
    })

    # -------------------------------------------------------------------------
    # 4. STORIES (7 stories: 1 classic adaptation, 6 regional stories)
    # -------------------------------------------------------------------------

    # Classic Story: Augusto Céspedes - Sangre de mestizos (El pozo)
    story_core_21 = {
        "id": "b2-21",
        "title": "El pozo en el infierno verde: Voces y agonía en el Chaco Boreal",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Una adaptación literaria de 'El pozo', relato cumbre del libro 'Sangre de mestizos' (1936) del maestro boliviano Augusto Céspedes: un pelotón de soldados excava obsesivamente un pozo en la aridez implacable del Chaco durante la guerra con Paraguay, descubriendo en el fondo de la tierra la desolación, la fraternidad de la sed y el despertar de una nueva conciencia nacional.",
        "characters": [
            "Suboficial narrador Miguel Navarro",
            "Soldado quechua Pedraza",
            "Zapador potosino Chacón",
            "Capitán de regimiento"
        ],
        "narration": {
            "paragraphs": [
                "En el corazón calcinado del Chaco Boreal, donde la línea del horizonte se disuelve en una reverberación asfixiante de polvo y salitrales secos, el calor no es una circunstancia atmosférica: es una condena corpórea implacable. En el verano de 1933, nuestro destacamento de zapadores del ejército boliviano recibió una orden terminante que sonaba a delirio o a milagro: excavar un pozo en medio del matorral espinoso, en un punto ciego donde la sed diezmaba a los regimientos con mayor ferocidad que las ametralladoras del ejército paraguayo. Entre las ramas espinosas del quebracho y los cactus achatados, el polvo blancuzco flotaba en el aire inmóvil como ceniza volcánica, adhiriéndose a las gargantas secas y a los labios agrietados de los soldados.",
                "Durante semanas interminables que parecían fundirse en un solo mediodía perpetuo, el barreno y la pala se convirtieron en nuestras únicas armas. El soldado Pedraza, un campesino quechua de las laderas de Tarata que jamás había visto una llanura sin cerros, hundía el pico con una furia mecánica en la tierra compacta y arcillosa. Cada palada extraída era devuelta a la superficie con sogas de cuero desgastadas por el zapador Chacón, un minero potosino acostumbrado a la noche fría de los socavones de estaño que ahora sudaba a borbotones a cincuenta grados a la sombra. A medida que el túnel vertical descendía metro a metro hacia las entrañas de la tierra, la atmósfera en el fondo se volvía espesa, tibia y pegajosa como la respiración de un animal subterráneo.",
                "Diez metros, veinte metros, treinta metros. Al alcanzar los cuarenta metros de profundidad en aquel cilindro oscuro, la obsesión colectiva por el agua adquirió dimensiones místicas y desgarradoras. Nadie hablaba ya de la patria, ni de los discursos patrioteros de los políticos de La Paz, ni del petróleo invisible que decían que dormía bajo el subsuelo. Toda la existencia de cincuenta hombres se reducía al anhelo desesperado de una gota de humedad, a una mancha de barro fresco que anunciara la llegada de la napa freática. Cuando un soldado bajaba amarrado a la cuerda, los que aguardaban arriba escrutaban con ojos afiebrados el fondo del abismo, aguardando el grito salvador que trajera la resurrección.",
                "Sin embargo, el fondo del pozo devolvía invariablemente el mismo veredicto despiadado: polvo seco, arena calcinada, tierra estéril y sorda que se desgranaba entre los dedos como harina caliente. En el fondo de aquel tubo de sombras, los soldados experimentaban un vértigo inverso: el cielo del Chaco se reducía a un diminuto círculo de luz lejana y cruel, tan inaccesible como la lluvia que se negaba a caer sobre los matorrales. Fue en ese confinamiento subterráneo donde el minero potosino y el campesino cochabambino comprendieron, sin necesidad de proclamas académicas, que compartían una misma condición de desamparo frente a una oficialidad lejana y a unas oligarquías que los habían arrojado a matarse entre hermanos desposeídos.",
                "A mediados de julio, cuando la profundidad del pozo superaba los cuarenta y cinco metros y el agua continuaba siendo una quimera esquiva, sonó la alarma en la trinchera exterior: una patrulla enemiga avanzaba entre los algarrobales. El pozo que debía salvar nuestras vidas con su frescura líquida se transformó entonces en una fosa de combate. En torno a su boca de arcilla reseca se libró una escaramuza violenta y ciega. Al caer la tarde, con varios compañeros caídos sobre la tierra removida, el silencio retornó al matorral. El pozo yacía abierto como una gigantesca herida en la costra del desierto, mudo testigo de una tragedia absurda.",
                "Años más tarde, al recordar aquel infierno verde, comprendimos que en el fondo de ese pozo sin agua no hallamos manantiales subterráneos, pero desenterramos algo más hondo y duradero: la conciencia compartida de una nación mestiza e indígena que, unida por el dolor de la sed y el barro, decidió no volver a agachar la cabeza ante sus antiguos verdugos. En la memoria indeleble de los sobrevivientes, la imagen de aquel pozo seco perdura como el testimonio supremo de una fraternidad forjada en la desolación más absoluta."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál era la misión primordial asignada al destacamento de zapadores en el relato 'El pozo' de Augusto Céspedes?",
                        "options": [
                            "Excavar desesperadamente un pozo en el Chaco en busca de agua para salvar a las tropas de la sed implacable.",
                            "Construir un puente colgante sobre las aguas caudalosas del río Pilcomayo.",
                            "Tender una línea de telégrafo que comunicara el frente con el palacio presidencial de La Paz.",
                            "Desactivar las minas terrestres sembradas por la aviación enemiga en las serranías."
                        ],
                        "correctIndex": 0,
                        "explanation": "El relato narra la agónica odisea de un pelotón que cava un pozo profundo en el desierto para hallar agua."
                    },
                    {
                        "question": "¿Qué revelación social experimentan los soldados de distintas regiones en el fondo del pozo?",
                        "options": [
                            "Descubren su fraternidad como mestizos e indígenas desamparados frente al abandono de las élites oligárquicas.",
                            "Deciden desertar del ejército para fundar una compañía comercial en territorio argentino.",
                            "Comprueban que el subsuelo del Chaco está repleto de lingotes de plata colonial.",
                            "Se enfrentan entre sí por disputas regionales entre quechuas y aymaras."
                        ],
                        "correctIndex": 0,
                        "explanation": "El sufrimiento compartido de la sed derriba los prejuicios regionales y despierta la conciencia nacional boliviana."
                    },
                    {
                        "question": "¿En qué se transforma trágicamente el pozo al aproximarse una patrulla enemiga?",
                        "options": [
                            "En una trinchera defensiva y fosa de combate donde varios soldados pierden la vida.",
                            "En un refugio subterráneo donde los combatientes organizan un banquete de despedida.",
                            "En una trampa de agua que ahoga por accidente a los exploradores adversarios.",
                            "En un depósito secreto para almacenar armamento pesado de artillería."
                        ],
                        "correctIndex": 0,
                        "explanation": "El pozo seco se convierte en escenario de combate y fosa para los combatientes caídos en la escaramuza."
                    }
                ]
            }
        }
    }

    # Regional Story 1: Chiquitanía y misiones
    story_bolivia_01 = {
        "id": "b2-boliviaoriente-01",
        "title": "El secreto de Chiquitos: Barroco mestizo en la espesura del bosque seco",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía cultural por las misiones jesuíticas de la Chiquitanía boliviana: los templos monumentales de madera tallada en medio del bosque seco tropical, la conservación milagrosa de miles de partituras de música barroca sacra por los cabildos indígenas, la pervivencia del violín y el modelo de autogestión comunitaria tras la expulsión colonial.",
        "characters": [
            "Maestro luthier Don Carlos",
            "Musicóloga e investigadora Silvia",
            "Cacique del cabildo indígena de San Javier",
            "Joven violinista chiquitana Marcela"
        ],
        "narration": {
            "paragraphs": [
                "Al este del río Grande, en un territorio de transición ecológica donde los últimos contrafuertes andinos dan paso a la vasta planicie del bosque seco chiquitano, se despliega uno de los enclaves culturales más asombrosos del continente americano: las misiones jesuíticas de Chiquitos. Mientras en el resto de América del Sur las célebres reducciones coloniales fueron arrasadas tras la expulsión de la Compañía de Jesús en 1767 por orden del rey Carlos III, los templos de San Javier, Concepción, San Miguel, San Rafael, Santa Ana y San José permanecieron intactos. En medio de sabanas calurosas y serranías cubiertas de vegetación espesa, estas majestuosas construcciones de tres naves sostenidas por gigantescas columnas salomónicas de madera de cuchi y tajibo continúan latiendo como santuarios vivos de fe comunitaria.",
                "El secreto de esta prodigiosa supervivencia histórica no radica en decretos gubernamentales ni en la intervención de ejércitos protectores, sino en la entereza moral de los propios pueblos originarios chiquitanos. Tras la intempestiva partida de los misioneros jesuitas en el siglo dieciocho, las familias indígenas no abandonaron los pueblos ni permitieron que la selva devorara los templos. Organizadas a través de sus cabildos comunales tradicionales, las autoridades originarias asumieron la tutela directa de los edificios de adobe y madera policromada, barriendo a diario los pisos de ladrillo cocido, retocando los frescos vegetales con pigmentos naturales extraídos de cortezas de árboles y custodiando con celo sagrado los ornamentos litúrgicos frente a la codicia de hacendados y buscadores de oro.",
                "A comienzos de la década de 1970, durante las obras de restauración arquitectónica dirigidas por el visionario arquitecto suizo Hans Roth, tuvo lugar un hallazgo musicológico sin parangón en el mundo: en los desvanes y armarios cerrados de los templos de San Rafael y Concepción aparecieron más de diez mil hojas de partituras de música barroca de los siglos diecisiete y dieciocho. Obras maestras de compositores barrocos europeos como Domenico Zipoli, intercaladas con misas polifónicas, sonatas y motetes anónimos compuestos por músicos indígenas en latín y en lenguas chiquitana y moxeña, habían sido pacientemente transcritas, encuadernadas en cuero de vaca y ejecutadas domingo tras domingo por orquestas locales durante dos centurias enteras de silencio administrativo.",
                "En el taller de carpintería comunal de Concepción, el maestro luthier Don Carlos cepilla con amorosa cadencia una tabla de cedro amazónico para dar forma a un nuevo violín. A su lado, su nieta Marcela tensa las cuerdas del instrumento y ensaya las notas cristalinas de un concierto barroco que resuena bajo el artesonado de vigas talladas. En Chiquitos, el violín no es un objeto europeo foráneo traído por conquistadores lejanos, sino una voz ancestral asimilada por el alma indígena: un puente místico que une el rezo cristiano con el canto sagrado de las aves de la selva y la memoria inmarcesible de los antepasados del monte.",
                "Cada dos años, la región celebra el prestigioso Festival Internacional de Música Renacentista y Barroca Americana 'Misiones de Chiquitos', congregando a ensambles y coros de los cinco continentes que viajan por caminos de tierra colorada para tocar junto a las orquestas juveniles locales. Sentado en las bancas de madera olorosa de la nave central mientras los coros polifónicos se elevan hacia el cielo tropical, el viajero comprende la dimensión profunda de este milagro: Chiquitos demostró que el verdadero patrimonio no se conserva congelado en vitrinas de museos extranjeros, sino palpitando en el corazón de un pueblo digno que hizo de la belleza su mayor escudo de libertad.",
                "Al caer el sol sobre las techumbres de teja y los campanarios de madera de San Javier, el repique solemne de las campanas convoca a la oración comunitaria. En la penumbra dorada del templo, entre querubines mestizos tallados con rasgos indígenas y columnas que parecen danzar en la penumbra, resuena la certeza de que en este rincón de Bolivia la historia no fue una herida de olvido, sino una melodía ininterrumpida de resistencia, esperanza y armonía espiritual. Es el legado imperecedero de un pueblo que supo hermanar la fe, el arte y la naturaleza en un canto colectivo de perdurable vigencia."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál fue el factor determinante que permitió la preservación intacta de las misiones de Chiquitos tras 1767?",
                        "options": [
                            "La organización de los cabildos indígenas locales que asumieron la custodia y mantenimiento diario de los templos.",
                            "La protección armada brindada por barcos de guerra apostados en las bahías del océano.",
                            "Un decreto papal que convirtió a la región en una zona militar neutral e inaccesible.",
                            "El traslado forzoso de todos los edificios a las ciudades de Sucre y Potosí."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los cabildos indígenas chiquitanos asumieron con devoción la tutela material y espiritual de sus templos."
                    },
                    {
                        "question": "¿Qué extraordinario descubrimiento musicológico se produjo durante las restauraciones dirigidas por Hans Roth?",
                        "options": [
                            "El hallazgo de más de diez mil páginas de partituras barrocas conservadas y ejecutadas por músicos originarios.",
                            "Una colección de discos de vinilo grabados en Europa durante la Segunda Guerra Mundial.",
                            "Pinturas renacentistas originales firmadas por el maestro italiano Leonardo da Vinci.",
                            "Cofres repletos de monedas de oro procedentes del imperio incaico."
                        ],
                        "correctIndex": 0,
                        "explanation": "Se descubrió el archivo de música barroca sacra indígena más vasto y mejor conservado del planeta."
                    },
                    {
                        "question": "¿Qué significado cultural tiene el violín para las comunidades contemporáneas de la Chiquitanía?",
                        "options": [
                            "Es considerado una voz ancestral plenamente apropiada que entrelaza la devoción y la memoria del pueblo.",
                            "Es un artículo de lujo destinado exclusivamente a la exportación a coleccionistas privados.",
                            "Un instrumento reservado únicamente para actos diplomáticos entre presidentes.",
                            "Una herramienta de castigo utilizada en las antiguas escuelas misionales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El violín es un símbolo de identidad y resistencia espiritual integrado en la vida comunitaria chiquitana."
                    }
                ]
            }
        }
    }

    # Regional Story 2: Santa Cruz y el oriente agroindustrial
    story_bolivia_02 = {
        "id": "b2-boliviaoriente-02",
        "title": "La capital de las llanuras: Santa Cruz, la identidad camba y la frontera agrícola",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la explosión urbana, económica y demográfica de Santa Cruz de la Sierra: de pueblo aislado en las sabanas orientales al corazón agroindustrial, energético y metropolitano de Bolivia, el orgullo de la identidad cultural camba, el debate ambiental en torno al avance de la frontera agrícola y la dialéctica nacional con el occidente andino.",
        "characters": [
            "Empresario agropecuario Don Rogelio",
            "Bióloga conservacionista Mariana",
            "Migrante quechua comerciante doña Gregoria",
            "Sociólogo cruceño Alejandro"
        ],
        "narration": {
            "paragraphs": [
                "Hasta mediados del siglo veinte, Santa Cruz de la Sierra era poco más que un pueblo apacible y provinciano recostado sobre las arenas del río Piraí, donde las carretas de bueyes surcaban calles de arena cálida bajo la sombra generosa de los toborochis en flor. Comunicada con el resto del país únicamente por sendas precarias de herradura que se anegaban con las lluvias torrenciales del verano tropical, la ciudad vivía al ritmo lento de las tertulias vespertinas y el mate tibio. Aquel aislamiento secular forjó un temperamento autosuficiente y solidario entre las familias pioneras, acostumbradas a resolver sus necesidades colectivas mediante el trabajo comunitario y la ayuda mutua. Sin embargo, la revolución de 1952, la inauguración de la carretera asfaltada hacia Cochabamba y la política estatal de 'marcha hacia el oriente' desataron una de las transformaciones sociourbanas más vertiginosas y expansivas de América del Sur.",
                "En el lapso de seis décadas, aquella aldea colonial de casas de adobe y galerías con horcones de madera tallada se transfiguró en una metrópoli moderna de más de dos millones de habitantes, organizada en un trazado circular de grandes avenidas concéntricas denominadas anillos. Respaldada por la fertilidad excepcional de las llanuras orientales, Santa Cruz se erigió en el indiscutible motor económico y agropecuario de Bolivia: sus campos de cultivo tecnificados producen más del setenta por ciento de los alimentos del país, liderando las exportaciones de soya, sorgo, maíz, caña de azúcar, carne bovina y derivados lácteos, además de consolidarse como un nodo financiero, petroquímico y logístico internacional.",
                "Este impetuoso dinamismo material forjó una marcada identidad cultural: la conciencia 'camba'. Enraizada en el mestizaje temprano entre conquistadores andaluces e indígenas chané y guaraníes, la cultura camba se define por la franqueza desenvuelta en el trato interpersonal, el orgullo por la tierra generosa, la pasión por la música de chovena y taquirari, y una concepción del progreso basada en la iniciativa privada y la libertad de empresa. Frente al centralismo político tradicional radicado en La Paz, la sociedad cruceña canalizó históricamente sus demandas a través de sus comités cívicos y la lucha por las regalías petroleras y las autonomías departamentales, reivindicando un modelo de descentralización que reconfiguró el mapa del poder estatal. Estas conquistas cívicas consolidaron un pacto social entre sectores empresariales, cooperativas de servicios públicos y sindicatos gremiales que confirieron estabilidad institucional a la expansión económica del oriente.",
                "No obstante, este deslumbrante crecimiento agroexportador enfrenta crecientes dilemas ecológicos y sociales. El avance agresivo de la frontera agrícola sobre los bosques vírgenes de la Chiquitanía y la cuenca amazónica ha provocado incendios forestales recurrentes que devoran millones de hectáreas de biodiversidad única, desatando alarmas entre ambientalistas como la bióloga Mariana. Al mismo tiempo, el magnetismo económico de la urbe atrajo a centenares de miles de migrantes quechuas y aymaras procedentes del altiplano y los valles andinos, quienes levantaron populosos distritos comerciales como el Plan Tres Mil, tejiendo un mestizaje urbano cosmopolita donde las polleras tradicionales conviven armónicamente con los sombreros de sao.",
                "Santa Cruz de la Sierra encarna hoy el rostro moderno, vibrante y tensionado de la Bolivia del porvenir, donde la tradición hospitalaria se conjuga a diario con los desafíos de una metrópoli global en constante reinvención. En sus bulevares arbolados donde rascacielos vanguardistas de vidrio espejado se alzan junto a puestos callejeros de cuñapé y majadito humeante, confluyen las energías productivas de todo un país que busca encontrar un punto de equilibrio entre el crecimiento económico, la preservación ecológica y la convivencia multicultural.",
                "Al contemplar el bullicio creador de las avenidas cruceñas al caer la tarde, cuando la brisa cálida alivia el bochorno diurno y el cielo se tiñe de tonos violetas y bermellones, el observador percibe que en este cruce de caminos tropicales late una verdad incontrovertible: la grandeza de Bolivia no radica en la hegemonía de una sola región sobre otra, sino en el abrazo fraterno y complementario entre la meseta andina y la llanura fecunda del oriente."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué acontecimientos históricos marcaron el despegue económico y demográfico de Santa Cruz de la Sierra a mediados del siglo XX?",
                        "options": [
                            "La revolución de 1952, la apertura de la carretera a Cochabamba y la política estatal de marcha al oriente.",
                            "La invasión de corsarios ingleses que desembarcaron en las playas fluviales del río Grande.",
                            "La construcción de un ferrocarril directo hacia las costas del océano Ártico.",
                            "La decisión del gobierno colonial de nombrar a la ciudad como sede única de la Real Audiencia."
                        ],
                        "correctIndex": 0,
                        "explanation": "La conexión vial en la década de 1950 y la política de diversificación productiva detonaron el auge cruceño."
                    },
                    {
                        "question": "¿Qué porcentaje aproximado de los alimentos de Bolivia se producen en los llanos del departamento de Santa Cruz?",
                        "options": [
                            "Más del setenta por ciento del total nacional de productos agroalimentarios.",
                            "Menos del cinco por ciento debido a las heladas constantes del invierno.",
                            "Aproximadamente el veinte por ciento concentrado exclusivamente en la pesca.",
                            "El cien por ciento de los granos pero nada de carne vacuna ni lácteos."
                        ],
                        "correctIndex": 0,
                        "explanation": "Santa Cruz produce más del 70% de los alimentos de Bolivia gracias a su tecnificación agropecuaria."
                    },
                    {
                        "question": "¿Cuál es uno de los principales desafíos socioambientales generados por la expansión de la frontera agrícola cruceña?",
                        "options": [
                            "Los incendios forestales recurrentes y la pérdida de bosques nativos por el desmonte agroindustrial.",
                            "La escasez absoluta de lluvia que transformó las tierras bajas en un desierto polar.",
                            "El abandono de los cultivos debido a la emigración masiva de campesinos a Europa.",
                            "La falta de fertilizantes minerales en los suelos sedimentarios del oriente."
                        ],
                        "correctIndex": 0,
                        "explanation": "El desmonte para cultivos de soya y ganadería genera graves incendios forestales y pérdida de biodiversidad."
                    }
                ]
            }
        }
    }

    # Regional Story 3: Salar de Uyuni y litio
    story_bolivia_03 = {
        "id": "b2-boliviaoriente-03",
        "title": "El desierto de sal: Uyuni, el oro blanco y la encrucijada del litio",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una expedición geográfica, científica y geopolítica al Salar de Uyuni: el mar blanco de diez mil kilómetros cuadrados formado por antiguos lagos prehistóricos, la extracción tradicional de sal, las mayores reservas probadas de litio del planeta en las salmueras profundas y el reto histórico de la industrialización soberana ante la transición energética global.",
        "characters": [
            "Ingeniero químico boliviano Efraín",
            "Trabajador salinero de Colchani Don Tomás",
            "Especialista en transición energética Laura",
            "Líder comunitaria quechua Doña Asunción"
        ],
        "narration": {
            "paragraphs": [
                "En el sudoeste del territorio boliviano, a más de 3.650 metros sobre el nivel del mar en el departamento de Potosí, la corteza terrestre se transforma en una visión deslumbrante que desconcierta los sentidos: el Salar de Uyuni. Con una superficie colosal que sobrepasa los diez mil quinientos kilómetros cuadrados, este inmenso océano fosilizado de sal es la planicie continua más extensa, blanca y plana del planeta Tierra. Formado a lo largo de decenas de miles de años tras la evaporación paulatina de los gigantescos lagos prehistóricos Minchin y Tauca, el salar presenta una costra superficial de sal de varios metros de grosor estructurada en perfectos polígonos geométricos que parecen trazados por la mano de un geómetra cósmico.",
                "Durante la estación seca del invierno andino, el aire gélido y diáfano permite divisar volcanes sagrados como el Tunupa a más de ochenta kilómetros de distancia con una nitidez sobrecogedora, mientras la radiación solar reverbera sobre la superficie con una luminosidad cegadora. En cambio, durante las semanas lluviosas del verano, una fina capa de agua de pocos centímetros cubre la costra salina, convirtiendo al salar en el espejo natural más grande del mundo: una superficie reflectante perfecta donde el cielo, las nubes algodonosas y las estrellas nocturnas se reflejan con tal fidelidad óptica que caminar por el salar produce la embriagadora sensación de flotar en medio del infinito celestial. Científicos de agencias espaciales de todo el mundo aprovechan esta planicie desprovista de desniveles para calibrar con máxima precisión los altímetros láser de los satélites en órbita terrestre.",
                "En los márgenes del salar, en aldeas tradicionales como Colchani, generaciones enteras de familias campesinas quechuas han vivido del trabajo paciente de cosechar sal. Don Tomás amontona la sal húmeda con palas de madera en pequeñas pirámides cónicas para que escurra el agua bajo el sol implacable, cargando luego los bloques en camiones para yodarla y distribuirla en los mercados del país. Sin embargo, en las últimas dos décadas el interés del planeta entero dejó de mirar la sal superficial para concentrarse obsesivamente en las salmueras líquidas que yacen atrapadas en las profundidades porosas del lecho salino.",
                "Esas salmueras subterráneas albergan la mayor concentración de litio conocida sobre la faz de la Tierra: más de veintiún millones de toneladas métricas de este metal blando, liviano y altamente electroquímico, indispensable para la fabricación de baterías de iones de litio que alimentan desde teléfonos inteligentes hasta flotas de vehículos eléctricos. En el umbral de la descarbonización del transporte mundial para mitigar la catástrofe del cambio climático, Bolivia se encontró repentinamente situada en el epicentro geopolítico del llamado 'triángulo del litio', que conforma junto a los salares de Atacama en Chile y del Hombre Muerto en Argentina.",
                "Consciente de las amargas lecciones de la historia colonial y republicana —donde la plata de Potosí enriqueció a las cortes europeas y el estaño engrosó las arcas de barones mineros privados dejando solo miseria y silicosis en las comunidades locales—, el Estado boliviano adoptó una política de control soberano estricto. A través de la empresa pública Yacimientos de Litio Bolivianos (YLB), el país se propuso no limitarse a la simple exportación primaria de carbonato de litio a granel, sino dominar la cadena tecnológica integral: desde la extracción directa con tecnologías que minimicen el consumo de agua dulce hasta la producción local de cátodos y celdas de baterías con socios internacionales bajo esquema mixto. Esta estrategia de industrialización integral aspira a posicionar a Bolivia no como un mero proveedor de materia prima para industrias foráneas, sino como un actor científico con voz propia en la vanguardia energética suramericana.",
                "Al contemplar la inmensidad blanca de Uyuni bajo el resplandor cobrizo del ocaso, cuando el viento helado barre los cristales de sal, el observador comprende la magnitud histórica del desafío: el desierto blanco de Potosí no es solo una maravilla natural de belleza inigualable, sino la gran prueba de fuego donde Bolivia se juega la oportunidad histórica de transformar sus riquezas naturales en progreso científico, justicia social y soberanía duradera para las futuras generaciones."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cómo se originó geológicamente la majestuosa planicie del Salar de Uyuni?",
                        "options": [
                            "Por la evaporación paulatina de antiguos lagos prehistóricos (Minchin y Tauca) a lo largo de miles de años.",
                            "Por la caída de un meteorito helado que cubrió la meseta andina de salitre.",
                            "Por la inundación artificial de minas subterráneas de carbón durante el siglo diecinueve.",
                            "Por el desbordamiento de las aguas del océano Atlántico sobre la cordillera."
                        ],
                        "correctIndex": 0,
                        "explanation": "El salar se formó por la desecación milenaria de grandes lagos interiores prehistóricos."
                    },
                    {
                        "question": "¿Qué fenómeno óptico espectacular ocurre en el Salar de Uyuni durante la temporada de lluvias en verano?",
                        "options": [
                            "Una capa de agua cubre la sal convirtiéndolo en un gigantesco espejo natural que refleja el cielo.",
                            "El salar se torna de color verde esmeralda y comienza a hervir a altas temperaturas.",
                            "Se abren cavernas profundas por donde circulan submarinos turísticos.",
                            "La sal se derrite por completo transformándose en barro oscuro impracticable."
                        ],
                        "correctIndex": 0,
                        "explanation": "El agua superficial genera un reflejo perfecto del firmamento, creando el espejo natural más grande del planeta."
                    },
                    {
                        "question": "¿Cuál es la premisa estratégica de Bolivia respecto a la industrialización de sus reservas de litio?",
                        "options": [
                            "Mantener el control soberano estatal y desarrollar la cadena de valor tecnológico (baterías y cátodos) en territorio patrio.",
                            "Ceder las salmueras en concesión perpetua y gratuita a consorcios privados extranjeros.",
                            "Prohibir el uso del litio en vehículos eléctricos para proteger el uso de combustibles fósiles.",
                            "Exportar exclusivamente sal común de cocina y desechar las salmueras ricas en minerales."
                        ],
                        "correctIndex": 0,
                        "explanation": "Bolivia busca evitar el extractivismo primario desarrollando tecnología e industrialización con soberanía estatal."
                    }
                ]
            }
        }
    }

    # Regional Story 4: Guerra del Chaco
    story_bolivia_04 = {
        "id": "b2-boliviaoriente-04",
        "title": "El pozo y la trinchera: La Guerra del Chaco y el despertar de una nación",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la Guerra del Chaco (1932-1935) entre Bolivia y Paraguay: el conflicto bélico más devastador de Sudamérica en el siglo XX en el infierno seco del Chaco Boreal, la manipulación geopolítica de intereses petroleros foráneos, el martirio de la sed y el nacimiento de la Generación del 35 que desencadenó la Revolución Nacional de 1952.",
        "characters": [
            "Historiador militar boliviano Ramiro",
            "Veterano de Boquerón Don Sixto",
            "Enfermera de la Cruz Roja Carmen",
            "Joven estudiante paceño Gonzalo"
        ],
        "narration": {
            "paragraphs": [
                "Entre 1932 y 1935, en el corazón árido y sofocante de América del Sur, Bolivia y Paraguay se desangraron en el conflicto armado internacional más violento, mortífero y traumático librado en el continente a lo largo del siglo veinte: la Guerra del Chaco. Sobre un escenario de más de doscientos cincuenta mil kilómetros cuadrados de planicies espinosas, matorrales achaparrados y arenales calcinados conocido como el Chaco Boreal, más de cien mil vidas jóvenes se extinguieron en trincheras sofocantes donde la artillería pesada, los nidos de ametralladoras y la guerra química se combinaron con un adversario natural infinitamente más implacable y temido que las balas enemigas: la sed absoluta.",
                "Las causas profundas de la contienda entrelazaron disputas limítrofes nunca resueltas desde la época colonial con la codicia de poderosos monopolios energéticos internacionales. Azuzados por la sospecha —más tarde desmentida por los peritajes geológicos de la época— de que bajo el suelo inhóspito del Chaco dormían fabulosos yacimientos de petróleo, los gobiernos de La Paz y Asunción fueron empujados al enfrentamiento bélico bajo la sombra de la rivalidad entre gigantes corporativos extranjeros como la Standard Oil norteamericana y la Royal Dutch Shell británica, convirtiendo a dos pueblos hermanos y empobrecidos en peones sacrificables de una ajedrez geopolítico foráneo. Las cancillerías de ambos países, subordinadas a presiones financieras externas, desoyeron las advertencias diplomáticas regionales que instaban a una solución arbitral pacífica.",
                "Para el soldado boliviano, la guerra representó un choque biogeográfico demoledor. Reclutados por la fuerza en las gélidas comunidades indígenas del altiplano a cuatro mil metros de altitud, decenas de miles de conscriptos aymaras y quechuas fueron transportados en vagones de carga y camiones polvorientos hacia un territorio tórrido a nivel del mar, donde las temperaturas superaban los cuarenta y cinco grados a la sombra y los mosquitos transmitían la malaria y la disentería. En batallas épicas y desgarradoras como la defensa heroica del fortín Boquerón, donde seiscientos soldados resistieron durante veintiún días el asedio de catorce mil combatientes enemigos, el grito desgarrado de '¡Agua!' resonaba en las noches como un réquiem universal.",
                "Sin embargo, en medio de la carnicería absurda de las alambradas de púas de Nanawa y Campo Vía, aconteció un milagro sociológico que cambió para siempre el destino político de Bolivia. En la estrechez claustrofóbica de la trinchera, el indígena aymara que solo hablaba su lengua ancestral compartió el último sorbo de orina o de agua podrida con el minero comunista de Huanuni y el joven universitario letrado de la clase media de Sucre. Al mirarse en los ojos afiebrados del compañero de desdicha, todos comprendieron con fulgurante lucidez que eran hijos de una misma patria secuestrada por una oligarquía terrateniente y minera que los despreciaba.",
                "De aquel crisol de dolor y ceniza emergió la célebre 'Generación del Chaco' o Generación del 35. Al firmarse el protocolo de paz en Buenos Aires en junio de 1935, los soldados retornaron a sus comunidades y ciudades no como súbditos sumisos, sino como ciudadanos conscientes de su fuerza histórica. Escritores como Augusto Céspedes (*Sangre de mestizos*) y Jesús Lara (*Repete*) narraron el martirio de la tropa, mientras jóvenes oficiales como Germán Busch y Gualberto Villarroel impulsaron las primeras medidas de nacionalismo económico y reconocimiento social del trabajo minero e indígena. En las aulas universitarias y en los sindicatos fabriles floreció un debate apasionado que sentó las bases conceptuales para recuperar los recursos naturales estratégicos en favor de las mayorías desposeídas.",
                "Apenas diecisiete años después del cese de hostilidades en el Chaco, aquellos mismos excombatientes y sus hijos protagonizaron en abril de 1952 la Revolución Nacional boliviana: una gesta que nacionalizó las grandes minas de estaño, decretó la reforma agraria liquidando el pongueaje feudal e instauró el sufragio universal para indígenas y mujeres. Al recorrer hoy los silenciosos fortines del Chaco donde las cruces de madera blanca se alzan entre los matorrales, el viajero rinde tributo a aquellos mártires de la sed, cuya inmolación dolorosa despertó de su letargo a la nación para alumbrar el siglo de la dignidad popular."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué rivalidad corporativa internacional atizó el conflicto bélico por el control del Chaco Boreal?",
                        "options": [
                            "La supuesta existencia de petróleo y la pugna entre consorcios extranjeros como Standard Oil y Shell.",
                            "La competencia entre empresas azucareras por monopolizar la exportación de ron al Caribe.",
                            "El control de los derechos de transmisión televisiva de eventos deportivos continentales.",
                            "La disputa entre compañías navieras por construir un canal interoceánico en la selva."
                        ],
                        "correctIndex": 0,
                        "explanation": "El conflicto estuvo impulsado por intereses geopolíticos y la sospecha de yacimientos petrolíferos estratégicos."
                    },
                    {
                        "question": "¿Por qué la batalla de Boquerón (1932) se convirtió en un hito de memoria heroica para Bolivia?",
                        "options": [
                            "Porque seiscientos soldados resistieron sitiados durante semanas frente a un ejército numéricamente muy superior.",
                            "Porque fue la primera batalla de la historia humana donde se utilizaron cohetes espaciales teledirigidos.",
                            "Porque se firmó un tratado de paz definitivo en menos de veinticuatro horas de combate.",
                            "Porque los soldados descubrieron un lago subterráneo que abasteció a toda la región del Chaco."
                        ],
                        "correctIndex": 0,
                        "explanation": "La defensa de Boquerón fue una gesta de resistencia extrema contra fuerzas enemigas abrumadoras."
                    },
                    {
                        "question": "¿Qué trascendencia histórica tuvo la llamada 'Generación del Chaco' para el porvenir boliviano?",
                        "options": [
                            "Forjó la conciencia social y antimperialista que desembocó en la Revolución Nacional de 1952 y la reforma agraria.",
                            "Provocó la desaparición de todos los partidos políticos y la adopción de una monarquía parlamentaria.",
                            "Inició una política de aislamiento internacional que cerró las fronteras del país por medio siglo.",
                            "Obligó a todos los ciudadanos a trasladarse a vivir a las zonas desérticas del Chaco."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los veteranos del Chaco encabezaron la revolución del 52 que abolió el latifundismo y concedió el voto universal."
                    }
                ]
            }
        }
    }

    # Regional Story 5: Carnaval de Oruro
    story_bolivia_05 = {
        "id": "b2-boliviaoriente-05",
        "title": "La danza de la redención: Diablos, arcángeles y fe en el Carnaval de Oruro",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una inmersión etnográfica y multisensorial en el fastuoso Carnaval de Oruro, Obra Maestra del Patrimonio Oral e Intangible de la Humanidad: la peregrinación danzada hacia el santuario de la Virgen del Socavón, el simbolismo sincrético de la Diablada donde el Arcángel San Miguel vence a los demonios mineros, la resonancia de las matracas de la Morenada y el arte ancestral de los mascareros.",
        "characters": [
            "Maestro mascarero Don Zenón",
            "Danzante de la Diablada Gonzalo",
            "Músico de banda de bronces Efraín",
            "Devota orureña Doña Maruja"
        ],
        "narration": {
            "paragraphs": [
                "A tres mil setecientos metros de altitud, sobre las faldas minerales de los cerros Pie de Gallo y San Felipe en la altiplanicie minera de Bolivia, la ciudad de Oruro se transforma cada febrero en el escenario del espectáculo de devoción popular, coreografía y arte tradicional más deslumbrante de América: el fastuoso Carnaval de Oruro. Proclamado en 2001 por la UNESCO como Obra Maestra del Patrimonio Oral e Intangible de la Humanidad, este acontecimiento multitudinario no es una simple fiesta mundana de disfraces y jolgorio efímero, sino una gigantesca peregrinación danzada donde más de cincuenta mil devotos y quince mil músicos consagran su cuerpo y su aliento a los pies de la sagrada Virgen de la Candelaria, conocida con fervor como la Virgen del Socavón.",
                "Durante el sábado de peregrinación, la ciudad amanece sacudida por el estruendo coordinado de centenares de tubas, trompetas, platillos y bombos de las monumentales bandas de bronce, cuyos uniformes relucen con botones dorados bajo el sol limpio de la puna. A lo largo de una ruta serpenteante de más de cuatro kilómetros que asciende desde la avenida Bolívar hasta el santuario del cerro, cincuenta y dos fraternidades folclóricas desfilan durante veinte horas continuas sin interrupción. Cada danzante ha formulado una promesa solemne de bailar durante tres años consecutivos por fe a la Virgen, soportando el cansancio físico extremo y el peso de atuendos que superan con frecuencia los treinta kilos de brocados, cuentas de vidrio y láminas de metal repujado.",
                "La cumbre estética y conceptual del carnaval es la Diablada, una danza que sintetiza de forma magistral el choque y la fusión entre la teología moral cristiana y la cosmovisión subterránea andina. Al frente de la comparsa avanza el Arcángel San Miguel, blandiendo una espada flamígera de plata y un escudo protector con el que somete a las huestes infernales. Detrás danzan en tropel Lucifer, Satanás y la Diablesa o China Supay, escoltados por una multitud de diablos menores cuyas descomunales máscaras de yeso y hojalata presentan ojos saltones de vidrio iluminados con focos incandescentes, dientes amenazantes de jaguar y cornamentas retorcidas sobre las que reptan serpientes y sapos esculpidos.",
                "Sin embargo, para el minero orureño, ese diablo enmascarado no es el demonio bíblico del castigo eterno, sino 'El Tío': la deidad tutelar de las profundidades de la tierra que reina en los socavones mineros, dueño de las vetas de estaño y protector contra los derrumbes en la oscuridad de las galerías subterráneas. Al ingresar bailando al santuario y caer de rodillas en lágrimas ante el altar iluminado por millares de cirios encendidos, los diablos se despojan de sus caretas en señal de sumisión y agradecimiento, demostrando que en los Andes la fe católica y la reverencia a la Pachamama no se destruyen mutuamente, sino que conviven en un abrazo cósmico indisoluble.",
                "Junto a la Diablada retumba la Morenada, cuya cadencia pesada y cadenciosa rinde homenaje a los esclavos africanos traídos en la época virreinal para trabajar en las minas y cecas monetarias. Al compás del sonido seco y metálico de centenares de matracas de madera con formas de barcos y peces tallados, los morenos avanzan con majestuosos trajes cónicos de terciopelo bordados con hilos de oro y plata que simulan barriles de carga, coronados por cascos emplumados que ondean al viento frío de la meseta. La coreografía acompasada transmite con sobrecogedora fuerza la dignidad de los afrobolivianos y su aporte insustituible a la matriz cultural de la nación.",
                "En los talleres de la calle La Paz, maestros artesanos y mascareros como Don Zenón dedican el año entero a modelar en arcilla y cartón las caretas sagradas, transmitiendo secretos de fundición y policromía de padres a hijos. En cada puntada de hilo brillante y en cada nota que brota de los bronces orureños vibra la identidad indestructible de un pueblo que convirtió el trabajo minero, el dolor histórico y la devoción religiosa en un himno inmortal de luz, color y resistencia cultural que conmueve al mundo entero y renueva cada año el pacto sagrado entre el ser humano, la fe y la generosa tierra andina."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué distinción otorgó la UNESCO al Carnaval de Oruro en el año 2001?",
                        "options": [
                            "Lo proclamó Obra Maestra del Patrimonio Oral e Intangible de la Humanidad.",
                            "Lo declaró Parque Nacional Ecológico bajo protección militar estricta.",
                            "Lo nombró Capital Gastronómica de la cocina molecular del Cono Sur.",
                            "Le concedió el premio internacional a la mejor red de transporte ferroviario."
                        ],
                        "correctIndex": 0,
                        "explanation": "La UNESCO reconoció el carnaval como una de las máximas expresiones de patrimonio inmaterial de la humanidad."
                    },
                    {
                        "question": "¿Cuál es la devoción central que motiva la peregrinación danzada de más de cincuenta mil personas en Oruro?",
                        "options": [
                            "La promesa de fe a la Virgen del Socavón (Virgen de la Candelaria), protectora de los mineros.",
                            "El agradecimiento a los directores de los bancos comerciales de la ciudad.",
                            "La celebración anual por la inauguración de una represa hidroeléctrica.",
                            "El homenaje póstumo a los generales victoriosos de la Guerra del Pacífico."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los danzantes bailan por devoción religiosa prometiendo tres años de danza a la Virgen del Socavón."
                    },
                    {
                        "question": "¿Qué doble significado religioso y cosmológico encierra la figura del diablo en la danza de la Diablada?",
                        "options": [
                            "Encarna el demonio moral católico vencido por San Miguel, pero también a 'El Tío', deidad protectora del subsuelo minero.",
                            "Representa a un pirata europeo que navega por el lago Poopó buscando tesoros.",
                            "Es un personaje satírico inventado para promocionar obras de teatro infantil en los colegios.",
                            "Simboliza a los recaudadores de impuestos de la corona española durante el virreinato."
                        ],
                        "correctIndex": 0,
                        "explanation": "La Diablada funde el mito católico de San Miguel con el culto minero andino a El Tío de los socavones."
                    }
                ]
            }
        }
    }

    # Regional Story 6: Capstone regional (Bolivia Oriente & minerals of future)
    story_bolivia_capstone = {
        "id": "b2-boliviaoriente-consolidation",
        "title": "Tierras bajas, salar y memoria: El mosaico integral de la Bolivia oriental",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis abarcadora de los Estudios Regionales de Bolivia II: el barroco vivo de las misiones jesuíticas de Chiquitos, el liderazgo agroindustrial y cívico de Santa Cruz de la Sierra, el desafío geopolítico del litio en el Salar de Uyuni, la memoria nacional de la Guerra del Chaco y la majestuosidad folclórica del Carnaval de Oruro.",
        "characters": [
            "Hans Roth",
            "Augusto Céspedes",
            "Virgen del Socavón",
            "Pueblo chiquitano y camba"
        ],
        "narration": {
            "paragraphs": [
                "Cuando la mirada geográfica e histórica abraza la totalidad del territorio boliviano, se descubre una verdad deslumbrante: Bolivia no es únicamente la imponente meseta andina de cumbres nevadas y socavones de plata, sino también la exuberante inmensidad de sus tierras bajas, sus llanuras tropicales y sus salares infinitos. Desde los bosques secos de la Chiquitanía hasta la frontera calurosa del Chaco Boreal y los horizontes blancos de Uyuni, la Bolivia oriental y sus salares representan la fuerza productiva, la memoria épica y la encrucijada estratégica donde el país proyecta su destino soberano en el siglo veintiuno.",
                "En la espesura de la Chiquitanía, los templos misionales de madera tallada erigidos en el siglo dieciocho se alzan como un monumento viviente al mestizaje creador. Allí donde los misioneros jesuitas trajeron el violín y la polifonía sacra, las comunidades indígenas chiquitanas custodiaron con heroica lealtad más de diez mil páginas de partituras barrocas tras la expulsión colonial, demostrando que la cultura no muere cuando el pueblo asume su tutela espiritual. Hoy, el sonido de los violines tallados en cedro sigue flotando sobre los campanarios de madera, proclamando que la dignidad y la belleza son capaces de vencer el olvido histórico.",
                "Esa misma vitalidad florece con fuerza volcánica en Santa Cruz de la Sierra, la gran capital económica de las llanuras orientales. Transformada en medio siglo en una metrópoli pujante de más de dos millones de habitantes, Santa Cruz se convirtió en el granero agroalimentario de Bolivia, produciendo el sustento diario de la nación y encabezando las exportaciones agroindustriales. Con su indiscutible identidad camba, abierta a la iniciativa privada y a la autonomía departamental, la urbe se convirtió también en el crisol de un nuevo mestizaje donde millones de compatriotas de origen andino integran sus esperanzas de progreso en un diálogo cosmopolita y laborioso. Esta sinergia productiva demuestra que las diferencias geográficas no son barreras insalvables, sino motores de innovación y complementariedad cotidiana.",
                "Hacia el sudoeste, en el desierto blanco de Uyuni, la geografía deposita en manos bolivianas la mayor reserva de litio del planeta. En ese mar de sal de diez mil kilómetros cuadrados formado por antiguos lagos prehistóricos, el país enfrenta el reto de transformar la bendición mineral en soberanía tecnológica real. A través de la empresa estatal YLB y la industrialización local de baterías, Bolivia busca romper definitivamente el ciclo colonial del extractivismo primario, exigiendo que las riquezas de la tierra se traduzcan en bienestar social, educación científica y respeto ambiental para las comunidades campesinas.",
                "Esta conciencia contemporánea de autodeterminación fue templada con sangre y dolor en las arenas ardientes de la Guerra del Chaco. En aquellas trincheras donde la sed fue el enemigo supremo y los monopolios petroleros extranjeros dictaron órdenes insidiosas, el campesino quechua, el minero aymara y el estudiante cruceño se reconocieron por primera vez como hermanos de un mismo destino. De ese martirio colectivo nació la Generación del Chaco y la Revolución de 1952, demoliendo las viejas estructuras feudales y abriendo las puertas de la ciudadanía universal.",
                "Y en Oruro, al pie de los cerros mineros, esa memoria de lucha y devoción estalla cada año en la magnificencia del Carnaval. Cuando los diablos se arrodillan ante la Virgen del Socavón y los morenos hacen retumbar sus matracas de madera, el sincretismo andino proclama su triunfo supremo: la fe católica y el culto a la Pachamama se entrelazan en una danza inmortal que celebra la redención del trabajo y la belleza indestructible del alma popular. Es la consagración festiva de una espiritualidad mestiza que no olvida sus raíces subterráneas mientras eleva su plegaria al cielo infinito de los Andes.",
                "Al contemplar este vasto mosaico boliviano, el viajero comprende que la verdadera grandeza del país radica en la armonía de sus contrastes. En la unión fecunda entre la roca andina y el río amazónico, entre la memoria del socavón y la espiga de la llanura, Bolivia camina hacia su futuro guiada por la luz soberana de sus pueblos, demostrando al mundo que la justicia, la cultura y la libertad florecen cuando una nación respeta todas sus raíces."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis geográfica y económica define el papel de las tierras bajas de Santa Cruz en Bolivia?",
                        "options": [
                            "Constituyen el motor agroalimentario del país produciendo más del setenta por ciento de los alimentos nacionales.",
                            "Son un territorio desértico despoblado sin actividad productiva relevante.",
                            "Albergan las únicas fábricas de aviones de pasajeros del continente americano.",
                            "Se dedican exclusivamente a la minería subterránea de carbón de piedra."
                        ],
                        "correctIndex": 0,
                        "explanation": "Santa Cruz de la Sierra y sus llanuras aportan más del 70% de la producción agroalimentaria boliviana."
                    },
                    {
                        "question": "¿Cómo se vincula el Salar de Uyuni con la soberanía económica de Bolivia en el siglo XXI?",
                        "options": [
                            "Mediante el desafío de industrializar el litio localmente en baterías evitando el viejo modelo extractivista colonial.",
                            "Mediante la venta de la totalidad del salar a bancos extranjeros para pagar la deuda externa.",
                            "A través de la desecación artificial de todos los ríos amazónicos para ampliar el salar.",
                            "Prohibiendo la extracción de cualquier mineral para destinar la zona únicamente a competencias automovilísticas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Uyuni encarna el reto de industrializar con valor agregado nacional las mayores reservas de litio del planeta."
                    },
                    {
                        "question": "¿De qué manera el Carnaval de Oruro expresa la síntesis espiritual de la historia boliviana?",
                        "options": [
                            "Amalgamando la devoción católica mariana con las divinidades andinas mineras (El Tío y la Pachamama) en una danza multitudinaria.",
                            "Eliminando por completo todas las tradiciones autóctonas para adoptar bailes europeos del siglo diecinueve.",
                            "Celebrando exclusivamente las victorias militares de las guerras civiles decimonónicas.",
                            "Sustituyendo los instrumentos musicales tradicionales por computadoras electrónicas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Carnaval de Oruro es el máximo exponente del sincretismo entre el catolicismo y la cosmovisión andina."
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

    # Write classic story
    write_json(f"stories/classics/b2/{c_unit}.json", to_schema_story(story_core_21))

    # Write regional stories
    write_json(f"stories/world/b2/{r1}.json", to_schema_story(story_bolivia_01, r1))
    write_json(f"stories/world/b2/{r2}.json", to_schema_story(story_bolivia_02, r2))
    write_json(f"stories/world/b2/{r3}.json", to_schema_story(story_bolivia_03, r3))
    write_json(f"stories/world/b2/{r4}.json", to_schema_story(story_bolivia_04, r4))
    write_json(f"stories/world/b2/{r5}.json", to_schema_story(story_bolivia_05, r5))
    write_json(f"stories/world/b2/{r6_con}.json", to_schema_story(story_bolivia_capstone, r6_con))
    write_json(f"stories/world/b2/{r_unit}.json", to_schema_story(story_bolivia_capstone, r_unit))

    # -------------------------------------------------------------------------
    # 5. LESSON FILES (6 Core + 6 Regional)
    # -------------------------------------------------------------------------
    core_lessons_info = [
        ("b2-21-01", "lesson.b2.21.01", "La tercera persona impersonal y el indefinido uno",
         "Master third-person plural impersonals and indefinite 'uno' to obscure agency and formulate shared human principles.",
         "tercera persona plural impersonal y pronombre indefinido uno",
         ["Deploy plural third-person verbs without explicit subject to communicate rumors or general talk.", "Utilize indefinite 'uno' to project generalized experience in thoughtful discourse.", "Avoid conversational 'uno' in strict academic prose favoring nominalizations."]),
        ("b2-21-02", "lesson.b2.21.02", "El se impersonal avanzado y la gestión institucional",
         "Deploy advanced impersonal 'se' with intransitive verbs and transitive verbs taking personal 'a', distinguishing it from reflexive passive.",
         "se impersonal con intransitivos y objeto de persona con a frente a pasiva refleja",
         ["Construct impersonal 'se' with personal 'a' and invariable singular verb.", "Differentiate impersonal 'se' from agreement-requiring reflexive passive.", "Master impersonal formulas in administrative notices and institutional summaries."]),
        ("b2-21-03", "lesson.b2.21.03", "La nominalización y la concisión ensayística",
         "Deploy syntactic nominalization to transform verbal clauses into dense noun phrases, omitting agents and heightening formality.",
         "nominalización desagentivadora y condensación informativa en la prosa ensayística",
         ["Transform verbal clauses into abstract nouns ending in -ción and -miento.", "Omit circumstantial human agents to achieve objective scientific tone.", "Balance nominal density to prevent stylistic opacity in formal critique."]),
        ("b2-21-04", "lesson.b2.21.04", "Verbos de necesidad y evaluación institucional",
         "Deploy impersonal evaluative and necessity verbs (convenir, urgir, constar, atañer, incumbir) with appropriate mood selection.",
         "verbos terciopersonales de valoración y necesidad: alternancia indicativo y subjuntivo",
         ["Select indicative mood after factive certainty matrices like 'consta que'.", "Enforce subjunctive mood after institutional directives like 'urge que' and 'conviene que'.", "Delimit administrative jurisdictions using 'atañer a' and 'incumbir a'."]),
        ("b2-21-05", "lesson.b2.21.05", "Atenuación epistémica y cautela diplomática",
         "Master hedging devices, epistemic conditional formulas, and perception passives for nuanced academic and diplomatic analysis.",
         "fórmulas de atenuación asertiva, condicional de modestia y distanciamiento epistémico",
         ["Apply the conditional of modesty (cabría inferir, se presumiría) to modulate claims.", "Employ perception passives like 'parece desprenderse' in data analysis.", "Express methodological caution and respectful disagreement without polemical confrontation."])
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
        "id": "lesson.b2.21.consolidation",
        "title": "Consolidación B2: Impersonalidad y El pozo de Augusto Céspedes",
        "level": "B2",
        "goal": "Synthesize syntactic impersonality, nominalization, and epistemic hedging through Augusto Céspedes's Chaco War masterpiece El pozo.",
        "grammar": "síntesis de impersonalidad sintáctica, nominalización y adaptación de Sangre de mestizos",
        "sections": [
            {"type": "goal", "items": [
                "Master impersonal 'se' and third-person plural generalizations in formal registers.",
                "Deploy nominalizations and evaluative impersonal matrices with correct mood selection.",
                "Analyze the fraternal awakening and existential tragedy of the Chaco War in Bolivian literature."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{c_unit}-con.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Utilizo adecuadamente la tercera persona plural impersonal y el indefinido 'uno'.",
                "Construyo oraciones impersonales con 'se' distinguiéndolas de la pasiva refleja.",
                "Aplico nominalizaciones precisas para despersonalizar textos analíticos.",
                "Selecciono el modo verbal correcto tras verbos impersonales como 'constar' y 'urgir'.",
                "Modulo mis afirmaciones con fórmulas de atenuación epistémica en condicional."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-boliviaoriente-01", "lesson.b2.boliviaoriente.01", "Los llanos de Chiquitos y las misiones jesuíticas",
         "Explore the Chiquitania savannahs, Jesuit mission wooden architecture, and living baroque musical archives.",
         "historia misional de Chiquitos, conectores causales-consecutivos y archivo musical barroco",
         ["Analyze the historical survival of the Chiquitos Jesuit mission churches.", "Deploy causal and consecutive discourse markers (habida cuenta de que, por ende) in historiographical prose.", "Deploy savannah ecology, mission history, and baroque music vocabulary (Chiquitanía, oratorio, barroco, espesura)."]),
        ("b2-boliviaoriente-02", "lesson.b2.boliviaoriente.02", "Santa Cruz de la Sierra y la pujanza agroindustrial",
         "Investigate the modern expansion of Santa Cruz, camba regional identity, agribusiness boom, and ecological dilemmas.",
         "economía agropecuaria cruceña, identidad cultural camba y marcadores contraargumentativos",
         ["Analyze Santa Cruz's role as the agroindustrial motor of Bolivia.", "Deploy adversative and concessive discourse markers (no obstante, antes bien, en contrapartida) in development debates.", "Deploy agribusiness, urban expansion, and regional identity vocabulary (agroindustria, camba, desmonte, pujanza)."]),
        ("b2-boliviaoriente-03", "lesson.b2.boliviaoriente.03", "El Salar de Uyuni y la encrucijada del litio",
         "Explore the Salar de Uyuni, prehistoric lake geology, lithium reserves, and sovereign energy transition challenges.",
         "geología del Salar de Uyuni, salmueras de litio y perífrasis de conjetura y probabilidad",
         ["Analyze the geological formation and optical mirror phenomenon of the Salar de Uyuni.", "Deploy probability periphrases (deber de + inf, venir a + inf) in technical resource evaluation.", "Deploy mineral brine, clean energy transition, and lithium extraction vocabulary (salmuera, litio, endorreico, geopolítica)."]),
        ("b2-boliviaoriente-04", "lesson.b2.boliviaoriente.04", "La Guerra del Chaco y la forja de la memoria nacional",
         "Analyze the Chaco War (1932-1935), trench warfare in the arid desert, oil geopolitics, and the Generation of 1935.",
         "historiografía de la Guerra del Chaco, estructuras condicionales contrafácticas y conciencia nacional",
         ["Trace the geopolitical causes and human tragedy of the Chaco War.", "Deploy retrospective counterfactual conditionals (de haber + participio, si hubiera... habría) in historical analysis.", "Deploy military history, trench warfare, and nationalist awakening vocabulary (matorral, trinchera, armisticio, fraternidad)."]),
        ("b2-boliviaoriente-05", "lesson.b2.boliviaoriente.05", "El Carnaval de Oruro y la devoción danzada",
         "Explore the UNESCO Masterpiece Carnival of Oruro, the Diablada syncretism, Virgen del Socavón, and Morenada dances.",
         "etnografía del Carnaval de Oruro, sincretismo andino y oraciones de relativo complejo con cuyo",
         ["Analyze the syncretic fusion between Catholic Marian devotion and Andean mineral deities.", "Deploy complex relative clauses with 'cuyo' in multisensory ethnographic narrative.", "Deploy folkloric dance, artisanal embroidery, and ritual festival vocabulary (diablada, morenada, matraca, sincretismo)."])
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
        "id": "lesson.b2.boliviaoriente.consolidation",
        "title": "Consolidación Regional: Tierras bajas, salar y memoria oriental",
        "level": "B2",
        "goal": "Consolidate regional studies on lowland Bolivia: Chiquitania missions, Santa Cruz agribusiness, Uyuni lithium, Chaco War, and Oruro Carnival.",
        "grammar": "síntesis de estudios regionales de la Bolivia oriental: Chiquitos, Santa Cruz, Uyuni, Chaco y Oruro",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize the cultural wealth of Jesuit mission baroque and Cruceño agroindustrial dynamism.",
                "Appreciate the geopolitical and technological stakes of the lithium frontier in Uyuni.",
                "Reflect on the historical turning points of the Chaco War and the living folk syncretism of Oruro."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r6_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{r6_con}-ex.json", "exerciseRefs": [f"{r_unit}-con.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la supervivencia única del barroco misional en los llanos de Chiquitos.",
                "Reconozco el liderazgo productivo de Santa Cruz y los debates ambientales de la frontera agrícola.",
                "Explico la trascendencia geopolítica del litio en el Salar de Uyuni y la transición energética.",
                "Valoro el impacto de la Guerra del Chaco en la forja de la conciencia nacional y la revolución del 52.",
                "Aprecio la riqueza simbólica y devocional del Carnaval de Oruro como patrimonio de la humanidad."
            ]}
        ]
    })

    print("Completed LatAm Unit 21 (Bolivia Oriente) generation!")

    # -------------------------------------------------------------------------
    # 6. UPDATE CURRICULUM UNITS (b2.json)
    # -------------------------------------------------------------------------
    b2_units_path = LATAM_DIR / "curriculum" / "units" / "b2.json"
    b2_units = json.loads(b2_units_path.read_text(encoding="utf-8"))

    has_core_21 = any(u.get("title") == "Impersonality & Strategic Distance" for u in b2_units)
    has_reg_21 = any(u.get("title") == "Bolivia II: The Lowlands, Eastern Amazonia & The Lithium Frontier" for u in b2_units)

    if not has_core_21:
        b2_units.append({
            "title": "Impersonality & Strategic Distance",
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
    if not has_reg_21:
        b2_units.append({
            "title": "Bolivia II: The Lowlands, Eastern Amazonia & The Lithium Frontier",
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
    print("Updated curriculum/units/b2.json with Unit 21!")

    # -------------------------------------------------------------------------
    # 7. AUDIT STORY WORD COUNTS (Strict 650 - 825 words)
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_21", story_core_21),
        ("story_bolivia_01", story_bolivia_01),
        ("story_bolivia_02", story_bolivia_02),
        ("story_bolivia_03", story_bolivia_03),
        ("story_bolivia_04", story_bolivia_04),
        ("story_bolivia_05", story_bolivia_05),
        ("story_bolivia_capstone", story_bolivia_capstone)
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
