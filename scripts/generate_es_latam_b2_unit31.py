#!/usr/bin/env python3
"""
generate_es_latam_b2_unit31.py

Generates Latin American Spanish B2 Unit 31 for both tracks:
- Track 1 (Core B2): Unit 31 - Marcadores del discurso IV: Consecutivos e ilativos
  Classic: Clarice Lispector - La hora de la estrella (1977)
- Track 2 (Regional Studies): Unit 31 - Brasil III: La Amazonía, Brasilia y la geopolítica del interior
  Overview + 5 lessons + consolidation story

Strict schema conformance:
- Vocabulary: root {id, lesson, title, words: [{lemma, translation, pos}]}
- Exercises: root {lesson, exercises: [{id, type, category, teaches, ...}]}
- Grammar: root {id, title, sections: [{type: 'text'|'table'|'tip', content, rows}]}
- Lessons: root {id, title, level: 'B2', sections: [...]}
- Stories: root {id, title, level: 'B2', lesson, type, estimatedMinutes, summary, characters, paragraphs: [{type: 'narration', text}], narration: {pedagogical: {comprehensionQuestions: [...]}}}
- Story word count strictly in [650, 825] words.
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LATAM_DIR = REPO_ROOT / "content" / "es-latam"

WORD_RE = re.compile(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b")

def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))

NEW_SKILLS = {
    # Core 31 grammar skills
    "marcadores-consecutivos-formales": {
        "name": "formal consecutive discourse markers in complex sentences",
        "kind": "grammar",
        "category": "grammar"
    },
    "marcadores-consecutivos-coloquiales": {
        "name": "informal consecutive discourse markers in daily communication",
        "kind": "grammar",
        "category": "grammar"
    },
    "marcadores-causales-complejos": {
        "name": "complex causal discourse markers in formal writing",
        "kind": "grammar",
        "category": "grammar"
    },
    "marcadores-ilativos-deductivos": {
        "name": "deductive illative markers for logical argumentation",
        "kind": "grammar",
        "category": "grammar"
    },
    "marcadores-causa-efecto-subjetiva": {
        "name": "subjective cause and effect markers in natural dialogue",
        "kind": "grammar",
        "category": "grammar"
    },
    # Regional 31 grammar skills
    "interior-subordinadas-consecutivas-intensivas": {
        "name": "intensive consecutive clauses with indicative and subjunctive",
        "kind": "grammar",
        "category": "grammar"
    },
    "interior-oraciones-temporales-avanzadas": {
        "name": "advanced temporal clauses expressing simultaneous and sequential actions",
        "kind": "grammar",
        "category": "grammar"
    },
    "interior-perifrasis-obligacion-atenuada": {
        "name": "attenuated periphrases expressing duty and necessity",
        "kind": "grammar",
        "category": "grammar"
    },
    "interior-conectores-contraargumentativos-formales": {
        "name": "formal counterargument connectors in analytical discourse",
        "kind": "grammar",
        "category": "grammar"
    },
    "interior-construcciones-concesivas-subjuntivo": {
        "name": "complex concessive structures requiring the subjunctive mood",
        "kind": "grammar",
        "category": "grammar"
    },
    # Vocabulary unit themes
    "b2-31-01-vocab": {
        "name": "formal logical reasoning vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-31-02-vocab": {
        "name": "informal cause and result vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-31-03-vocab": {
        "name": "academic causality and inference vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-31-04-vocab": {
        "name": "deductive argumentation vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-31-05-vocab": {
        "name": "conversational justification and motivation vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "brasil-interior-01-vocab": {
        "name": "modernist urbanism and planned architecture vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "brasil-interior-02-vocab": {
        "name": "amazonian geography and river system vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "brasil-interior-03-vocab": {
        "name": "indigenous sovereignty and ancestral lands vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "brasil-interior-04-vocab": {
        "name": "cerrado agribusiness and ecological transition vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "brasil-interior-05-vocab": {
        "name": "diplomacy brics and south american geopolitics vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    }
}

NEW_GRAMMAR_TITLES = {
    "marcadores-consecutivos-formales": "formal consecutive discourse markers in complex sentences",
    "marcadores-consecutivos-coloquiales": "informal consecutive discourse markers in daily communication",
    "marcadores-causales-complejos": "complex causal discourse markers in formal writing",
    "marcadores-ilativos-deductivos": "deductive illative markers for logical argumentation",
    "marcadores-causa-efecto-subjetiva": "subjective cause and effect markers in natural dialogue",
    "interior-subordinadas-consecutivas-intensivas": "intensive consecutive clauses with indicative and subjunctive",
    "interior-oraciones-temporales-avanzadas": "advanced temporal clauses expressing simultaneous and sequential actions",
    "interior-perifrasis-obligacion-atenuada": "attenuated periphrases expressing duty and necessity",
    "interior-conectores-contraargumentativos-formales": "formal counterargument connectors in analytical discourse",
    "interior-construcciones-concesivas-subjuntivo": "complex concessive structures requiring the subjunctive mood"
}

def update_skill_registry():
    path = LATAM_DIR / "indexes" / "skill-registry.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_SKILLS.items():
        data["skills"][k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated skill-registry.json for Unit 31")

def update_grammar_titles():
    path = LATAM_DIR / "indexes" / "grammar-titles.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_GRAMMAR_TITLES.items():
        data[k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated grammar-titles.json for Unit 31")

# --- DATA DEFINITIONS ---

VOCAB_DATA = {
    "b2-31-01": {
        "title": "Lógica y raciocinio formal",
        "words": [
            {"lemma": "por consiguiente", "translation": "consequently", "pos": "adverb"},
            {"lemma": "por ende", "translation": "therefore / hence", "pos": "adverb"},
            {"lemma": "de ahí que", "translation": "hence / which is why (+ subj.)", "pos": "conjunction"},
            {"lemma": "corolario", "translation": "corollary", "pos": "noun"},
            {"lemma": "secuela", "translation": "aftermath / consequence", "pos": "noun"},
            {"lemma": "derivar", "translation": "to stem / to derive", "pos": "verb"},
            {"lemma": "inferencia", "translation": "inference", "pos": "noun"},
            {"lemma": "axiomático", "translation": "axiomatic / self-evident", "pos": "adjective"},
            {"lemma": "consecución", "translation": "attainment / following", "pos": "noun"},
            {"lemma": "enlace", "translation": "nexus / connection", "pos": "noun"}
        ]
    },
    "b2-31-02": {
        "title": "Causa y consecuencia coloquial",
        "words": [
            {"lemma": "así que", "translation": "so / therefore", "pos": "conjunction"},
            {"lemma": "conque", "translation": "so / then", "pos": "conjunction"},
            {"lemma": "de modo que", "translation": "so that / in such a way that", "pos": "conjunction"},
            {"lemma": "desenlace", "translation": "outcome / denouement", "pos": "noun"},
            {"lemma": "ocurrencia", "translation": "witty remark / occurrence", "pos": "noun"},
            {"lemma": "resultar", "translation": "to turn out / to result", "pos": "verb"},
            {"lemma": "repercusión", "translation": "repercussion", "pos": "noun"},
            {"lemma": "provocar", "translation": "to trigger / to provoke", "pos": "verb"},
            {"lemma": "imprevisto", "translation": "unforeseen event", "pos": "noun"},
            {"lemma": "remate", "translation": "conclusion / finishing touch", "pos": "noun"}
        ]
    },
    "b2-31-03": {
        "title": "Causalidad compleja y académica",
        "words": [
            {"lemma": "dado que", "translation": "given that", "pos": "conjunction"},
            {"lemma": "visto que", "translation": "seeing that", "pos": "conjunction"},
            {"lemma": "toda vez que", "translation": "inasmuch as / since", "pos": "conjunction"},
            {"lemma": "puesto que", "translation": "since / because", "pos": "conjunction"},
            {"lemma": "fundamento", "translation": "ground / rationale", "pos": "noun"},
            {"lemma": "etiología", "translation": "causation / etiology", "pos": "noun"},
            {"lemma": "desencadenante", "translation": "triggering factor", "pos": "noun"},
            {"lemma": "motivar", "translation": "to motivate / to prompt", "pos": "verb"},
            {"lemma": "subyacer", "translation": "to underlie", "pos": "verb"},
            {"lemma": "justificación", "translation": "justification", "pos": "noun"}
        ]
    },
    "b2-31-04": {
        "title": "Argumentación deductiva e ilativa",
        "words": [
            {"lemma": "de suerte que", "translation": "so that / with the result that", "pos": "conjunction"},
            {"lemma": "por tanto", "translation": "therefore", "pos": "conjunction"},
            {"lemma": "en consecuencia", "translation": "in consequence / accordingly", "pos": "adverb"},
            {"lemma": "silogismo", "translation": "syllogism", "pos": "noun"},
            {"lemma": "postulado", "translation": "postulate / premise", "pos": "noun"},
            {"lemma": "deducción", "translation": "deduction", "pos": "noun"},
            {"lemma": "ilación", "translation": "logical sequence / deduction", "pos": "noun"},
            {"lemma": "concluyente", "translation": "conclusive", "pos": "adjective"},
            {"lemma": "consiguiente", "translation": "ensuing / consequential", "pos": "adjective"},
            {"lemma": "establecer", "translation": "to establish", "pos": "verb"}
        ]
    },
    "b2-31-05": {
        "title": "Justificación y causa-efecto subjetiva",
        "words": [
            {"lemma": "pues", "translation": "well / since / for", "pos": "conjunction"},
            {"lemma": "es que", "translation": "the thing is that", "pos": "conjunction"},
            {"lemma": "pretexto", "translation": "pretext / excuse", "pos": "noun"},
            {"lemma": "motivo", "translation": "motive / reason", "pos": "noun"},
            {"lemma": "explicación", "translation": "explanation", "pos": "noun"},
            {"lemma": "aclaración", "translation": "clarification", "pos": "noun"},
            {"lemma": "alegar", "translation": "to plead / to allege", "pos": "verb"},
            {"lemma": "circunstancia", "translation": "circumstance", "pos": "noun"},
            {"lemma": "razón", "translation": "reason / rationality", "pos": "noun"},
            {"lemma": "convicción", "translation": "conviction", "pos": "noun"}
        ]
    },
    "b2-brasilinterior-01": {
        "title": "Brasilia y urbanismo modernista",
        "words": [
            {"lemma": "trazado", "translation": "layout / master plan", "pos": "noun"},
            {"lemma": "curvatura", "translation": "curvature", "pos": "noun"},
            {"lemma": "eje", "translation": "axis", "pos": "noun"},
            {"lemma": "hormigón", "translation": "concrete", "pos": "noun"},
            {"lemma": "monumentalidad", "translation": "monumentality", "pos": "noun"},
            {"lemma": "audacia", "translation": "boldness / audacity", "pos": "noun"},
            {"lemma": "diseñar", "translation": "to design", "pos": "verb"},
            {"lemma": "trasladar", "translation": "to relocate / to move", "pos": "verb"},
            {"lemma": "vanguardista", "translation": "avant-garde", "pos": "adjective"},
            {"lemma": "piloto", "translation": "pilot / master", "pos": "adjective"}
        ]
    },
    "b2-brasilinterior-02": {
        "title": "Geografía fluvial y selva amazónica",
        "words": [
            {"lemma": "cuenca", "translation": "river basin / watershed", "pos": "noun"},
            {"lemma": "afluente", "translation": "tributary", "pos": "noun"},
            {"lemma": "caudaloso", "translation": "mighty / high-flow", "pos": "adjective"},
            {"lemma": "navegabilidad", "translation": "navigability", "pos": "noun"},
            {"lemma": "confluencia", "translation": "confluence", "pos": "noun"},
            {"lemma": "igarapé", "translation": "amazonian creek / stream", "pos": "noun"},
            {"lemma": "selva", "translation": "rainforest / jungle", "pos": "noun"},
            {"lemma": "fluvial", "translation": "riverine / fluvial", "pos": "adjective"},
            {"lemma": "anegadizo", "translation": "floodplain / waterlogged", "pos": "adjective"},
            {"lemma": "remoto", "translation": "remote", "pos": "adjective"}
        ]
    },
    "b2-brasilinterior-03": {
        "title": "Soberanía indígena y tierras ancestrales",
        "words": [
            {"lemma": "demarcación", "translation": "demarcation / boundary marking", "pos": "noun"},
            {"lemma": "aislado", "translation": "uncontacted / isolated", "pos": "adjective"},
            {"lemma": "intangible", "translation": "intangible / inviolable", "pos": "adjective"},
            {"lemma": "invasión", "translation": "encroachment / invasion", "pos": "noun"},
            {"lemma": "salvaguarda", "translation": "safeguard", "pos": "noun"},
            {"lemma": "fiscalizar", "translation": "to inspect / to oversee", "pos": "verb"},
            {"lemma": "vulnerabilidad", "translation": "vulnerability", "pos": "noun"},
            {"lemma": "autonomía", "translation": "autonomy", "pos": "noun"},
            {"lemma": "cosmovisión", "translation": "worldview", "pos": "noun"},
            {"lemma": "protección", "translation": "protection", "pos": "noun"}
        ]
    },
    "b2-brasilinterior-04": {
        "title": "Agronegocio y transición ecológica en el Cerrado",
        "words": [
            {"lemma": "frontera agrícola", "translation": "agricultural frontier", "pos": "noun"},
            {"lemma": "deforestación", "translation": "deforestation", "pos": "noun"},
            {"lemma": "pastizal", "translation": "pasture / grassland", "pos": "noun"},
            {"lemma": "monocultivo", "translation": "monoculture", "pos": "noun"},
            {"lemma": "acuífero", "translation": "aquifer", "pos": "noun"},
            {"lemma": "erosión", "translation": "erosion", "pos": "noun"},
            {"lemma": "sostenibilidad", "translation": "sustainability", "pos": "noun"},
            {"lemma": "grano", "translation": "grain / cereal", "pos": "noun"},
            {"lemma": "devastador", "translation": "devastating", "pos": "adjective"},
            {"lemma": "preservar", "translation": "to preserve", "pos": "verb"}
        ]
    },
    "b2-brasilinterior-05": {
        "title": "Geopolítica, diplomacia y BRICS",
        "words": [
            {"lemma": "cancillería", "translation": "foreign ministry", "pos": "noun"},
            {"lemma": "multilateralismo", "translation": "multilateralism", "pos": "noun"},
            {"lemma": "hegemonía", "translation": "hegemony", "pos": "noun"},
            {"lemma": "mediación", "translation": "mediation", "pos": "noun"},
            {"lemma": "bloque", "translation": "bloc", "pos": "noun"},
            {"lemma": "liderazgo", "translation": "leadership", "pos": "noun"},
            {"lemma": "consenso", "translation": "consensus", "pos": "noun"},
            {"lemma": "soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "equilibrar", "translation": "to balance", "pos": "verb"},
            {"lemma": "estratégico", "translation": "strategic", "pos": "adjective"}
        ]
    }
}

GRAMMAR_DATA = {
    "b2-31-01-a": {
        "title": "Marcadores consecutivos formales",
        "sections": [
            {
                "type": "text",
                "content": "Los marcadores consecutivos formales como 'por consiguiente', 'por ende' y la locución conjuntiva 'de ahí que' introducen una consecuencia o deducción rigurosa a partir de premisas previas. Es fundamental señalar que 'por consiguiente' y 'por ende' operan como enlaces oracionales seguidos de modo indicativo o pausas tipográficas (comas), mientras que 'de ahí que' exige obligatoriamente el modo subjuntivo debido a su valor ponderativo y focalizador de la causa explicativa subyacente."
            },
            {
                "type": "table",
                "title": "Conectores consecutivos formales y régimen modal",
                "rows": [
                    ["No se cumplió el protocolo; por consiguiente, el experimento fue anulado.", "The protocol was not followed; consequently, the experiment was voided."],
                    ["El informe carece de datos fidedignos; por ende, carece de validez legal.", "The report lacks reliable data; hence, it lacks legal validity."],
                    ["Las lluvias destruyeron el puente, de ahí que suspendieran el tránsito vehicular.", "The rains destroyed the bridge, which is why they suspended vehicle traffic."],
                    ["Faltaron pruebas contundentes, de ahí que el juez absolviera al acusado.", "Conclusive evidence was lacking, which is why the judge acquitted the accused."]
                ]
            },
            {
                "type": "tip",
                "content": "¡Atención al régimen verbal de 'de ahí que'! Nunca uses indicativo tras esta locución: se dice 'de ahí que el gobierno tomara / haya tomado medidas', jamás 'de ahí que el gobierno tomó medidas'."
            }
        ]
    },
    "b2-31-02-a": {
        "title": "Marcadores consecutivos coloquiales e ilativos",
        "sections": [
            {
                "type": "text",
                "content": "En la comunicación oral cotidiana y en la prosa fluida, los enlaces consecutivos más recurrentes son 'así que', 'conque' y 'de modo que'. Mientras 'así que' y 'conque' señalan consecuencias inmediatas, reflexiones espontáneas o mandatos exhortativos, 'de modo que' puede alternar entre indicativo (cuando expone una consecuencia fáctica real) y subjuntivo (cuando introduce una intención, finalidad o mandato indirecto atenuado)."
            },
            {
                "type": "table",
                "title": "Usos de así que, conque y de modo que",
                "rows": [
                    ["Ya terminamos la revisión, así que podemos enviar el documento ahora mismo.", "We have already finished the review, so we can send the document right now."],
                    ["¿Conque decidiste aceptar la beca de investigación en São Paulo?", "So you decided to accept the research scholarship in São Paulo?"],
                    ["Explicó todo detalladamente, de modo que nadie tuvo dudas sobre el plan.", "He explained everything in detail, so that no one had doubts about the plan."],
                    ["Hablen más bajo, de modo que los pacientes puedan descansar tranquilos.", "Speak more quietly, so that the patients can rest peacefully."]
                ]
            },
            {
                "type": "tip",
                "content": "'Conque' se escribe en una sola palabra cuando equivale a 'así que' o 'por tanto' ('Es tarde, conque apúrate'). No lo confundas con la combinación preposición + pronombre relativo 'con que' ('el lápiz con que escribo') ni con 'con qué' interrogativo ('¿Con qué dinero vas a viajar?')."
            }
        ]
    },
    "b2-31-03-a": {
        "title": "Marcadores causales complejos",
        "sections": [
            {
                "type": "text",
                "content": "En textos ensayísticos, académicos y jurídicos, la relación causal se expresa mediante locuciones complejas de registro elevado como 'dado que', 'visto que', 'toda vez que' y 'puesto que'. Estas locuciones suelen anteponerse a la cláusula principal para enmarcar la justificación documental o fáctica que legitima la aserción posterior, rigiéndose habitualmente en modo indicativo al enunciar hechos comprobados y constatables."
            },
            {
                "type": "table",
                "title": "Locuciones causales complejas en registro formal",
                "rows": [
                    ["Dado que no existen antecedentes delictivos, se concedió la excarcelación.", "Given that there are no criminal records, release was granted."],
                    ["Visto que el tiempo apremia, procederemos a votar la resolución ministerial.", "Seeing that time is pressing, we will proceed to vote on the ministerial resolution."],
                    ["Toda vez que ambas partes llegaron a un acuerdo, se firma el acta.", "Inasmuch as both parties reached an agreement, the minute is signed."],
                    ["Puesto que conocemos las causas del fenómeno, formularemos la hipótesis.", "Since we know the causes of the phenomenon, we will formulate the hypothesis."]
                ]
            },
            {
                "type": "tip",
                "content": "La locución 'toda vez que' pertenece al lenguaje administrativo y jurisprudencial formal. En el habla corriente, suele sustituirse de forma natural por 'ya que', 'puesto que' o 'dado que'."
            }
        ]
    },
    "b2-31-04-a": {
        "title": "Marcadores ilativos y deductivos",
        "sections": [
            {
                "type": "text",
                "content": "La ilación lógica es el nexo racional que une dos juicios de modo que el segundo se deduce necesariamente del primero. Los marcadores ilativos como 'por tanto', 'en consecuencia', 'de suerte que' y el clásico 'luego' (con valor deductivo similar al latín *ergo*) estructuran silogismos y razonamientos formales rigurosos sin ambigüedad causal."
            },
            {
                "type": "table",
                "title": "Conectores ilativos y deducción racional",
                "rows": [
                    ["Todos los hombres son mortales; Sócrates es hombre; por tanto, Sócrates es mortal.", "All men are mortal; Socrates is a man; therefore, Socrates is mortal."],
                    ["Pienso, luego existo, según la máxima cartesiana clásica.", "I think, therefore I am, according to the classical Cartesian maxim."],
                    ["El caudal aumentó de manera extraordinaria; en consecuencia, se cerraron las compuertas.", "The river discharge increased extraordinarily; accordingly, the floodgates were closed."],
                    ["Rediseñaron la red hidráulica, de suerte que no volvieron a ocurrir inundaciones.", "They redesigned the hydraulic network, with the result that floods did not occur again."]
                ]
            },
            {
                "type": "tip",
                "content": "El conector 'luego' posee dos valores en español: temporal ('primero desayunamos y luego salimos') e ilativo-deductivo ('estudió con empeño, luego aprobará el examen'). En este último caso, va precedido de coma."
            }
        ]
    },
    "b2-31-05-a": {
        "title": "Causa-efecto subjetiva: justificación y énfasis",
        "sections": [
            {
                "type": "text",
                "content": "En la conversación viva y en la argumentación interpersonal, la causalidad a menudo no responde a deducciones matemáticas objetivas, sino a justificaciones subjetivas, disculpas, énfasis y motivaciones personales. El conector 'pues', la construcción causal introductoria 'es que' y el uso de 'que' explicativo permiten modular el compromiso del hablante con la justificación ofrecida."
            },
            {
                "type": "table",
                "title": "Marcadores de justificación conversacional",
                "rows": [
                    ["No fui a la reunión plenaria, pues me sentía indispuesto desde la madrugada.", "I did not go to the plenary meeting, for I had been feeling unwell since early morning."],
                    ["¿Por qué no llamaste antes? —Es que se me descargó el teléfono en el viaje.", "Why didn't you call earlier? —The thing is my phone ran out of battery on the trip."],
                    ["Ven de prisa, que ya va a comenzar la ceremonia de graduación.", "Come quickly, for the graduation ceremony is about to start."],
                    ["Aléjate del borde, que te puedes caer en el barranco rocoso.", "Step back from the edge, because you could fall into the rocky ravine."]
                ]
            },
            {
                "type": "tip",
                "content": "'Es que' siempre introduce una justificación o excusa atenuante ante una pregunta o reproche previo, suavizando la afirmación al presentar la causa como una circunstancia sobrevenida independiente de la voluntad del sujeto."
            }
        ]
    },
    "b2-brasilinterior-01-a": {
        "title": "Subordinadas consecutivas intensivas",
        "sections": [
            {
                "type": "text",
                "content": "Las oraciones subordinadas consecutivas intensivas expresan el resultado o la consecuencia directa de una cualidad o cantidad ponderada al máximo. Se estructuran mediante cuantificadores correlativos como 'tan... que', 'tanto... que', 'de tal manera / modo... que'. El verbo de la subordinada va en modo indicativo cuando la consecuencia se presenta como un hecho real y efectivo, pero pasa a subjuntivo cuando la oración principal está negada o condicionada hipotéticamente."
            },
            {
                "type": "table",
                "title": "Estructuras consecutivas intensivas",
                "rows": [
                    ["La arquitectura de Niemeyer era tan audaz que deslumbró a los críticos internacionales.", "Niemeyer's architecture was so bold that it dazzled international critics."],
                    ["Trabajaron tanto en las obras de Brasilia que levantaron la urbe en mil días.", "They worked so much on Brasilia's construction that they erected the city in a thousand days."],
                    ["Diseñó los palacios de tal manera que parecieran flotar sobre el horizonte del Cerrado.", "He designed the palaces in such a way that they appeared to float above the Cerrado horizon."],
                    ["No era tan compleja la traza que no pudiera comprenderse en un vistazo.", "The layout was not so complex that it could not be understood at a glance."]
                ]
            },
            {
                "type": "tip",
                "content": "Observa el contraste modal: 'Era tan luminoso que todos lo veían' (hecho real: indicativo) frente a 'No era tan luminoso que cegara a los transeúntes' (consecuencia negada o no verificada: subjuntivo)."
            }
        ]
    },
    "b2-brasilinterior-02-a": {
        "title": "Oraciones temporales complejas de simultaneidad y secuencia",
        "sections": [
            {
                "type": "text",
                "content": "Para narrar procesos geográficos, expediciones y dinámicas históricas fluviales, el español avanzado emplea conectores temporales de alta precisión aspectual como 'al cabo de', 'nada más + infinitivo', 'a medida que' y 'conforme'. Estas estructuras permiten distinguir la simultaneidad progresiva (*a medida que avanzaba la barcaza*) de la inmediatez secuencial absoluta (*nada más llegar a la confluencia*)."
            },
            {
                "type": "table",
                "title": "Conectores temporales de simultaneidad y sucesión",
                "rows": [
                    ["A medida que remontábamos el río Negro, el agua se tornaba más oscura y cristalina.", "As we navigated up the Negro River, the water became darker and more crystalline."],
                    ["Nada más atracar el vapor en el puerto de Manaus, los estibadores descargaron el caucho.", "As soon as the steamship docked at the port of Manaus, the stevedores unloaded the rubber."],
                    ["Al cabo de semanas de travesía por el delta de Belém, avistaron las costas del Atlántico.", "After weeks of voyage through the Belém delta, they caught sight of the Atlantic shores."],
                    ["Conforme ascendía la marea oceánica, el fenómeno de la pororoca estremecía las riberas.", "As the ocean tide rose, the pororoca tidal bore shook the riverbanks."]
                ]
            },
            {
                "type": "tip",
                "content": "'Nada más + infinitivo' es un recurso sumamente idiomático y elegante equivalente a 'en cuanto' o 'tan pronto como', con la ventaja estilística de prescindir de un verbo conjugado subordinado."
            }
        ]
    },
    "b2-brasilinterior-03-a": {
        "title": "Perífrasis de obligación y necesidad atenuada",
        "sections": [
            {
                "type": "text",
                "content": "En debates éticos e institucionales sobre soberanía y derechos territoriales, es habitual modular las exigencias y deberes normativos mediante perífrasis de obligación atenuada como 'haber de + infinitivo', 'precisar + infinitivo' y 'deber de + infinitivo' (cuando se matiza la conjetura deontológica). Frente a la contundencia de 'tener que + infinitivo', 'haber de' introduce un matiz solemne y moral ineludible."
            },
            {
                "type": "table",
                "title": "Perífrasis modales de deber y necesidad institucional",
                "rows": [
                    ["El Estado brasileño ha de respetar la intangibilidad de las tierras indígenas aisladas.", "The Brazilian State has to respect the intangibility of uncontacted indigenous lands."],
                    ["Las comunidades precisan contar con títulos de propiedad colectiva inalienables.", "The communities need to have inalienable collective property titles."],
                    ["La FUNAI ha de garantizar la fiscalización constante de las fronteras demarcadas.", "FUNAI has to guarantee constant inspection of demarcated borders."],
                    ["Hemos de preservar la diversidad etnolingüística como un patrimonio común continental.", "We must preserve ethnolinguistic diversity as a shared continental heritage."]
                ]
            },
            {
                "type": "tip",
                "content": "No confundas 'deber + infinitivo' (obligación directa: 'debes cumplir la ley') con 'deber de + infinitivo' (suposición o probabilidad: 'debe de ser muy remoto aquel afluente')."
            }
        ]
    },
    "b2-brasilinterior-04-a": {
        "title": "Conectores contraargumentativos formales",
        "sections": [
            {
                "type": "text",
                "content": "Al analizar tensiones complejas como el auge agroexportador frente a la preservación ecológica, se requieren conectores contraargumentativos de registro culto como 'empero', 'no por ello' y 'con todo'. Estos marcadores conceden validez parcial a un argumento inicial pero reorientan la fuerza conclusiva del discurso hacia la objeción prioritaria."
            },
            {
                "type": "table",
                "title": "Marcadores contraargumentativos en la prosa analítica",
                "rows": [
                    ["La soja genera divisas cruciales; empero, la deforestación del Cerrado amenaza los acuíferos.", "Soy generates crucial foreign exchange; however, Cerrado deforestation threatens aquifers."],
                    ["El país modernizó su maquinaria agrícola; no por ello cesaron los conflictos territoriales.", "The country modernized its agricultural machinery; not because of that did territorial conflicts cease."],
                    ["Las cosechas alcanzaron récords históricos; con todo, persisten graves déficits de sostenibilidad.", "Harvests reached historical records; all the same, severe sustainability deficits persist."],
                    ["Se aprobaron leyes de zonificación; empero, la fiscalización en campo sigue siendo precaria.", "Zoning laws were passed; however, field enforcement remains precarious."]
                ]
            },
            {
                "type": "tip",
                "content": "'Empero' es un arcaísmo estilístico que sobrevive en la prosa ensayística y diplomática como sinónimo elevado de 'sin embargo' o 'no obstante'. Va siempre entre comas o tras punto y coma."
            }
        ]
    },
    "b2-brasilinterior-05-a": {
        "title": "Construcciones concesivas intensivas con subjuntivo",
        "sections": [
            {
                "type": "text",
                "content": "En la argumentación geopolítica sobre el papel de potencias emergentes, las construcciones concesivas intensivas como 'por más que + subjuntivo', 'por mucho que + subjuntivo' y 'así + subjuntivo' expresan que una dificultad o presión externa es incapaz de frustrar la acción principal, subrayando la firmeza de la voluntad estratégica."
            },
            {
                "type": "table",
                "title": "Estructuras concesivas con subjuntivo en diplomacia",
                "rows": [
                    ["Por más que las potencias tradicionales presionen, el bloque de los BRICS defenderá un orden multipolar.", "However much traditional powers exert pressure, the BRICS bloc will defend a multipolar order."],
                    ["Por mucho que discrepen los negociadores, la cumbre no finalizará sin una declaración conjunta.", "However much the negotiators disagree, the summit will not end without a joint declaration."],
                    ["Así surjan crisis financieras externas, Itamaraty mantendrá sus compromisos con la integración regional.", "Even if external financial crises arise, Itamaraty will maintain its commitments to regional integration."],
                    ["Por más que se cuestione el gasto diplomático, la proyección exterior afianza la soberanía pacífica.", "However much diplomatic expenditure is questioned, foreign projection consolidates peaceful sovereignty."]
                ]
            },
            {
                "type": "tip",
                "content": "La fórmula 'así + presente o imperfecto de subjuntivo' tiene valor concesivo enfático equivalente a 'aunque' o 'incluso si' ('así llueva a cántaros, asistiremos al plenario internacional')."
            }
        ]
    }
}

STORIES_DATA = {
    "classics/b2/b2-31": {
        "id": "b2-31",
        "title": "La hora de la estrella (Clarice Lispector, 1977)",
        "level": "B2",
        "lesson": 1,
        "type": "classics",
        "estimatedMinutes": 15,
        "summary": "Exploración literaria y existencial de la célebre novela 'La hora de la estrella' de Clarice Lispector: la mediación del narrador Rodrigo S.M., la fragilidad invisible de Macabéa en Río de Janeiro, la emigración desde el Nordeste árido y la indagación filosófica sobre la causalidad, el lenguaje y la dignidad humana.",
        "characters": [
            "Clarice Lispector (autora brasileña de origen judío-ucraniano)",
            "Rodrigo S.M. (narrador ficticio atormentado por la ética de la escritura)",
            "Macabéa (mecanógrafa alagoana ingenua e invisible en Río de Janeiro)",
            "Olímpico de Jesús (novio oportunista y ambicioso)",
            "Madame Carlota (adivina que vaticina un falso destino dorado)"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el año 1977, cuando la consagrada escritora Clarice Lispector sentía la cercanía implacable del final de su existencia terrenal a causa de un cáncer terminal, concibió la que sería su obra de despedida más desgarradora, provocadora y filosóficamente desafiante: 'La hora de la estrella' ('A hora da estrela'). En primer término, la novela desconcierta al lector desde su arquitectura compositiva inicial, puesto que no presenta la trama de manera directa y convencional, sino a través de la mediación reflexiva de un narrador ficticio interpuesto, Rodrigo S.M. Este narrador, un intelectual atormentado por escrúpulos éticos y vacilaciones ontológicas, confiesa que se siente culpable por escribir desde el confort burgués sobre la desoladora indigencia de una muchacha anónima; por ende, advierte desde el preludio que su relato estará despojado de adornos retóricos superficiales para registrar con aspereza documental el misterio insondable de la subsistencia humana."
            },
            {
                "type": "narration",
                "text": "La protagonista absoluta de este drama íntimo y colectivo es Macabéa, una joven de diecinueve años oriunda del estado nororiental de Alagoas, quien forma parte de las inmensas mareas migratorias campesinas que arribaron a las barriadas periféricas de Río de Janeiro en busca de un destino menos hostil. Macabéa trabaja como una humilde mecanógrafa incompetente en una lúgubre oficina comercial del barrio de São Cristóvão; carece de formación académica elemental, padece una anemia crónica visible en sus ojeras profundas y se alimenta casi exclusivamente de perritos calientes baratos y café frío con azúcar. No obstante su extrema marginación material, Macabéa desconoce por completo su propia infelicidad: de ahí que viva en un estado de inocencia vegetal desarmante, maravillándose ante las palabras exóticas que escucha por las noches en la emisora Radio Reloj o soñando despierta con la imagen inalcanzable de la actriz Marilyn Monroe."
            },
            {
                "type": "narration",
                "text": "En el plano sentimental, Macabéa entabla un noviazgo precario y grotesco con Olímpico de Jesús, un metalúrgico paraibano dominado por una vanidad feroz y aspiraciones desmedidas de ascenso social que lo llevan a menospreciar permanentemente a la joven campesina por su torpeza verbal y su falta de malicia mundana. Por consiguiente, cuando la calculadora compañera de trabajo de Macabéa, Gloria, despliega sus encantos materiales ofreciendo un hogar burgués y banquetes familiares, Olímpico no vacila en abandonar cruelmente a Macabéa sin el menor remordimiento moral. Afligida por el desengaño pero empujada por la curiosidad ingenua, la protagonista acude al consultorio de una pintoresca cartomante llamada Madame Carlota en una favela carioca; allí, la vidente le vaticina con teatral entusiasmo que su suerte cambiará de forma súbita y que un apuesto extranjero rubio y adinerado llegará en un automóvil lujoso para desposarla y cubrirla de riquezas."
            },
            {
                "type": "narration",
                "text": "Pletórica de una felicidad radiante que jamás había experimentado en sus diecinueve años de privaciones silenciosas, Macabéa sale a la calle creyendo firmemente que su verdadera vida está a punto de comenzar bajo un cielo bienhechor. Empero, al cruzar una transitada avenida metropolitana, un reluciente automóvil Mercedes-Benz de color amarillo la atropella con violencia ciega y huye sin detenerse a socorrerla, dejándola tendida sobre el asfalto sucio de la acera. En aquel instante agónico donde el cuerpo frágil se desangra entre la multitud de curiosos indiferentes, la mecanógrafa invisible alcanza finalmente su solitaria y luminosa 'hora de la estrella': un estado de revelación mística sublime donde la muerte transforma la insignificancia cotidiana en un grito supremo de belleza, trascendencia y afirmación cósmica ante el silencio eterno del universo indiferente."
            },
            {
                "type": "narration",
                "text": "En definitiva, 'La hora de la estrella' constituye uno de los monumentos más perturbadores de la narrativa iberoamericana contemporánea, al denunciar con dolorosa lucidez cómo las grandes metrópolis devoran la vida de millones de migrantes desamparados sin concederles siquiera el derecho a poseer una voz propia. A través de la trágica odisea de Macabéa y las dudas desgarradas de Rodrigo S.M., Clarice Lispector demostró que la literatura no debe limitarse a entretener con tramas complacientes, sino que ha de interpelar la conciencia moral del lector obligándolo a mirar a los ojos de los invisibles. En última instancia, la obra enseña que toda vida humana, por insignificante o desposeída que parezca a los ojos del mundo tecnocrático, alberga en su núcleo secreto un resplandor sagrado que ningún poder terrenal puede extinguir."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Quién es el narrador que media la historia de Macabéa en 'La hora de la estrella' y qué dilema ético experimenta?",
                        "options": [
                            "Un juez militar que redacta un sumario judicial penal.",
                            "Rodrigo S.M., un intelectual que reflexiona con angustia sobre el privilegio de narrar la miseria ajena sin retórica vana.",
                            "El novio de la protagonista que escribe sus memorias en la vejez.",
                            "Un médico patólogo que investiga la causa de una epidemia hospitalaria."
                        ],
                        "correctIndex": 1,
                        "explanation": "Rodrigo S.M. es el alter ego reflexivo creado por Lispector que cuestiona la ética de la escritura ante la pobreza extrema."
                    },
                    {
                        "question": "¿De qué región de Brasil procede Macabéa y cómo es su existencia en Río de Janeiro?",
                        "options": [
                            "De las plantaciones vinícolas del sur, donde vive como hacendada acaudalada.",
                            "De Alagoas en el Nordeste, subsistiendo como mecanógrafa precaria e invisible en condiciones de extrema indigencia.",
                            "De la selva amazónica, desempeñándose como guía turística bilingüe.",
                            "De la capital Brasilia, trabajando como funcionaria de alto rango en un ministerio."
                        ],
                        "correctIndex": 1,
                        "explanation": "Macabéa encarna la migración nororiental hacia las barriadas cariocas, viviendo en la invisibilidad y privación material."
                    },
                    {
                        "question": "¿Qué significado simbólico adquiere el desenlace de la novela cuando Macabéa es arrollada por un automóvil de lujo?",
                        "options": [
                            "Un accidente intrascendente sin ninguna connotación metafórica.",
                            "Su 'hora de la estrella': el instante trágico donde la víctima invisible adquiere protagonismo y trascendencia cósmica.",
                            "La inauguración de una nueva línea de tranvías urbanos en Río de Janeiro.",
                            "El escape exitoso de la muchacha hacia un país extranjero con un magnate."
                        ],
                        "correctIndex": 1,
                        "explanation": "La colisión y agonía de Macabéa representan paradójicamente su único momento de brillo estelar y visibilidad ontológica."
                    }
                ]
            }
        }
    },
    "world/b2/b2-brasilinterior-01": {
        "id": "b2-brasilinterior-01",
        "title": "Brasilia: La utopía geométrica del Plan Piloto",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La fundación de Brasilia en 1960 como acto refundacional de la nación brasileña: la visión geopolítica de Juscelino Kubitschek, el trazado urbanístico en cruz de Lucio Costa y las curvas monumentales de hormigón armado de Oscar Niemeyer.",
        "characters": [
            "Juscelino Kubitschek (presidente impulsor del traslado de la capital)",
            "Lucio Costa (urbanista autor del Plan Piloto)",
            "Oscar Niemeyer (arquitecto de los palacios monumentales)",
            "Los 'candangos' (obreros migrantes pioneros que levantaron la ciudad)"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "El 21 de abril de 1960, en el corazón geográfico de la meseta central brasileña y en medio de la inmensidad desértica y rojiza del Cerrado, tuvo lugar uno de los acontecimientos urbanísticos y geopolíticos más audaces de la historia moderna universal: la inauguración oficial de la ciudad de Brasilia como nueva capital federal de la república. Durante más de siglo y medio, desde la independencia proclamada en 1822, estadistas y visionarios habían reclamado la necesidad imperiosa de mudar el centro del poder político lejos de la costa marítima atlántica de Río de Janeiro hacia el interior despoblado, con el fin supremo de vertebrar el territorio nacional e impulsar la colonización del vasto 'hinterland'. Fue finalmente el dinámico presidente Juscelino Kubitschek quien asumió el reto colosal bajo la consigna electrizante de lograr 'cincuenta años de progreso en cinco de gobierno', movilizando todos los recursos financieros y humanos del Estado."
            },
            {
                "type": "narration",
                "text": "La concepción espacial de la nueva metrópoli nació del talento insigne del urbanista Lucio Costa, quien ganó el concurso público internacional de 1957 con su célebre 'Plan Piloto'. Inspirado en el gesto ancestral de quien toma posesión de una tierra ignota trazando dos ejes perpendiculares que se cruzan en forma de cruz o de aeroplano en pleno vuelo, Costa organizó la vida cívica con una claridad funcional inaudita. A lo largo del Eje Monumental concentró los palacios de los poderes soberanos, los ministerios gubernamentales y los monumentos cívicos; transversalmente, a lo largo del Eje Vial curvado, distribuyó las 'Supercuadras' residenciales: módulos vecinales autónomos concebidos para albergar viviendas integradas con escuelas primarias, áreas verdes recreativas y comercios locales sin necesidad de utilizar el automóvil para las gestiones cotidianas."
            },
            {
                "type": "narration",
                "text": "Por su parte, la dimensión poética y monumental de la urbe quedó confiada a la genialidad del arquitecto Oscar Niemeyer, discípulo predilecto de Le Corbusier pero dotado de un lirismo escultórico propio e inimitable. Rechazando el ángulo recto rígido característico del racionalismo europeo tradicional, Niemeyer proclamó su devoción por la línea curva libre y sensual, inspirada en las ondulaciones de las sierras cariocas, en las nubes de la meseta y en las formas del cuerpo femenino. Obras maestras de hormigón armado como el Palacio de Planalto, el Congreso Nacional con sus cúpulas gemelas cóncava y convexa, el Supremo Tribunal Federal y la etérea Catedral Metropolitana —con sus dieciséis columnas hiperbólicas que se abren como manos orantes hacia el firmamento— consagraron a Brasilia como la cumbre arquitectónica del modernismo suramericano. Asimismo, la integración de los murales cerámicos de Athos Bulcão y el paisajismo exuberante de Roberto Burle Marx transformaron cada explanada pública en un diálogo permanente entre la abstracción geométrica y la flora tropical autóctona."
            },
            {
                "type": "narration",
                "text": "Sin embargo, aquella colosal epopeya modernista albergó también profundas contradicciones sociales y sacrificios humanos desgarradores que la historia oficial tardó en reconocer. La ciudad no fue erigida por burócratas de cuello blanco, sino por más de sesenta mil obreros desarraigados —la inmensa mayoría de ellos campesinos analfabetos procedentes del sufrido Nordeste azotado por las sequías, bautizados popularmente como 'candangos'—. Estos trabajadores laboraron día y noche bajo condiciones infrahumanas, soportando nubes de polvo calcinante y durmiendo en campamentos precarios de madera para cumplir el milagro cronológico de construir una metrópoli completa en menos de mil días. Paradójicamente, el diseño urbanístico segregó con rigor a estos constructores hacia 'ciudades satélite' periféricas desprovistas de los servicios suntuosos del Plan Piloto central."
            },
            {
                "type": "narration",
                "text": "A pesar de las críticas que señalan su excesiva dependencia del transporte automotor y la rigidez de su zonificación funcional, la Unesco declaró a Brasilia Patrimonio Cultural de la Humanidad en 1987, convirtiéndola en la única urbe edificada en el siglo veinte en ostentar semejante distinción ecuménica. En última instancia, contemplar los palacios de mármol blanco reflejándose en los espejos de agua frente al cielo azul cobalto del Cerrado constituye una experiencia estética incomparable. Brasilia demostró a la comunidad internacional que los pueblos del Sur global eran plenamente capaces de forjar una vanguardia civilizatoria propia, proyectando en el hormigón armado y en el espacio público su inquebrantable fe en el porvenir y en la soberanía de una nación continental."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál fue el objetivo geopolítico fundamental que impulsó el traslado de la capital brasileña a Brasilia en 1960?",
                        "options": [
                            "Acercar el gobierno federal a las costas de Europa para fomentar el comercio textil.",
                            "Integrar el interior continental despoblado y equilibrar el desarrollo económico lejos de la costa marítima tradicional.",
                            "Proteger a las élites coloniales de las revueltas agrarias del sur.",
                            "Construir un complejo de bases militares para vigilar las fronteras andinas."
                        ],
                        "correctIndex": 1,
                        "explanation": "El traslado al Cerrado buscó romper el atlantismo costero histórico y poblar y articular el interior geográfico del país."
                    },
                    {
                        "question": "¿Qué innovación estilística distinguió las creaciones arquitectónicas de Oscar Niemeyer en los palacios de la nueva capital?",
                        "options": [
                            "La imitación estricta de las catedrales góticas de piedra granítica.",
                            "La sustitución del ángulo recto rígido por curvas sensuales y audaces estructuras escultóricas de hormigón armado.",
                            "El uso exclusivo de maderas tropicales sin cimientos de cemento.",
                            "La reproducción exacta de los templos de la Grecia clásica."
                        ],
                        "correctIndex": 1,
                        "explanation": "Niemeyer revolucionó la arquitectura moderna utilizando hormigón armado para crear curvas poéticas inspiradas en el paisaje y la naturaleza."
                    },
                    {
                        "question": "¿Quiénes fueron los 'candangos' y qué contradicción social representaron en la construcción de Brasilia?",
                        "options": [
                            "Ingenieros extranjeros que dirigieron las obras por control remoto desde París.",
                            "Campesinos migrantes, en su mayoría nordestinos, que levantaron la urbe con enorme sacrificio pero terminaron excluidos en ciudades satélite.",
                            "Diplomáticos europeos que financiaron los gastos protocolarios.",
                            "Políticos federales que redactaron la primera constitución de la capital."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los 'candangos' fueron la mano de obra migrante que edificó la urbe en mil días pero quedó relegada a las periferias no planificadas."
                    }
                ]
            }
        }
    },
    "world/b2/b2-brasilinterior-02": {
        "id": "b2-brasilinterior-02",
        "title": "La cuenca amazónica: Manaus, Belém y la arteria fluvial continental",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La inmensidad geográfica y ecológica de la Amazonía brasileña: el río Amazonas y la confluencia de las aguas en Manaus, el auge cauchero de la Belle Époque con el Teatro Amazonas, el puerto histórico de Belém do Pará y el debate sobre la bioeconomía fluvial.",
        "characters": [
            "Barones del caucho y arquitectos europeos de la Belle Époque amazónica",
            "Pobladores ribereños, siringueros y navegantes de los barcos de línea fluvial",
            "Científicos del Instituto Nacional de Investigaciones de la Amazonía (INPA)"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Con una cuenca hidrográfica colosal que abarca más de seis millones de kilómetros cuadrados repartidos entre nueve países suramericanos, la Amazonía constituye el sistema biológico y fluvial más prodigioso del planeta Tierra. Dentro del territorio brasileño, donde se concentra más del sesenta por ciento de su superficie forestal, el río Amazonas no es un simple curso de agua, sino un auténtico mar dulce en perpetuo movimiento que vierte al océano Atlántico la quinta parte de todo el caudal fluvial del globo terráqueo. En este universo acuático y selvático exuberante, las carreteras asfaltadas ceden su protagonismo casi absoluto a los barcos de dos y tres cubiertas cargados de hamacas coloridas, los cuales surcan durante días enteros los meandros de ríos legendarios como el Solimões, el Negro, el Madeira, el Tapajós y el Xingu, constituyendo el único medio de transporte para millones de habitantes ribereños."
            },
            {
                "type": "narration",
                "text": "En el corazón mismo de este tapiz esmeralda, situada en la orilla izquierda del río Negro justo antes de su abrazo fluvial con el río Solimões, se erige la imponente metrópoli de Manaus. Es precisamente en las inmediaciones de esta ciudad donde los viajeros contemplan maravillados el fenómeno hidrológico del 'Encuentro de las Aguas': durante más de seis kilómetros, las aguas oscuras, cálidas y ácidas del río Negro y las aguas ocres, lodosas y veloces del Solimões corren paralelamente sin mezclarse en un mismo cauce, debido a sus marcadas diferencias de densidad, temperatura y velocidad de corriente, ofreciendo un espectáculo visual conmovedor donde conviven dos mundos acuáticos nítidamente diferenciados."
            },
            {
                "type": "narration",
                "text": "Entre finales del siglo diecinueve y las primeras décadas del veinte, Manaus protagonizó uno de los episodios económicos más delirantes y extravagantes de la historia moderna: la llamada fiebre del caucho ('ciclo da borracha'). Al convertirse la savia gomosa del árbol de la siringa en un insumo estratégico indispensable para la naciente industria automotriz y neumática mundial, la ciudad experimentó un enriquecimiento deslumbrante que atrajo a inversionistas internacionales y barones del látex. En aquel apogeo cosmopolita de la Belle Époque selvática, se construyó el deslumbrante Teatro Amazonas en 1896: un templo de ópera lírica edificado con mármoles importados de Carrara, cristales de Murano y una fastuosa cúpula recubierta con treinta y seis mil mosaicos esmaltados con los colores de la bandera republicana nacional, donde cantaron divas europeas como Enrico Caruso ante un público envuelto en sedas parisinas."
            },
            {
                "type": "narration",
                "text": "Hacia la desembocadura marítima, donde el gigantesco estuario fluvial abraza el océano Atlántico entre las mareas atronadoras de la pororoca y los canales de la isla de Marajó, florece la histórica ciudad de Belém do Pará. Puerta de entrada tradicional a la Amazonía desde su fundación en 1616 por los colonizadores portugueses, Belém deslumbra al visitante por su complejo arquitectónico colonial del Forte do Presépio y, sobre todo, por el legendario mercado de Ver-o-Peso: la mayor feria al aire libre de América del Sur. En sus abigarrados puestos de madera conviven las hierbas medicinales de los chamanes caboclos, los pescados gigantescos como el pirarucú y el tambaquí, las tinajas de açaí recién desgranado y el zumo embriagador del tucupí con hojas anestésicas de jambú, compendio supremo de una civilización gastronómica y botánica milenaria. Asimismo, la celebración anual del Círio de Nazaré congrega a más de dos millones de fieles en las calles de Belém, manifestando una devoción mariana entrelazada indisolublemente con los ritmos fluviales y las esperanzas colectivas del pueblo amazónico."
            },
            {
                "type": "narration",
                "text": "En el siglo veintiuno, la cuenca amazónica encara una disyuntiva histórica inaplazable entre los modelos extractivos predadores y la consolidación de una bioeconomía innovadora y respetuosa con los ciclos naturales del bosque en pie. Como advierten los investigadores del Instituto Nacional de Investigaciones de la Amazonía (INPA), talar la selva para transformarla en pastizales de ganado no solo destruye una biodiversidad farmacológica irrecuperable, sino que amenaza con desarticular los 'ríos voladores': inmensas masas de vapor transpiradas por los árboles que regulan las lluvias de todo el cono sur. Por consiguiente, proteger la integridad ecológica del bioma amazónico y valorar el saber milenario de sus comunidades ribereñas representa un deber de supervivencia no solo para Brasil, sino para la civilización humana en su conjunto."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿En qué consiste el fenómeno hidrológico del 'Encuentro de las Aguas' en las cercanías de Manaus?",
                        "options": [
                            "En la evaporación total de un afluente durante la estación seca.",
                            "En el curso paralelo sin mezclarse de las aguas oscuras del río Negro y las aguas arcillosas del Solimões debido a densidades y temperaturas disímiles.",
                            "En la congelación súbita de las aguas lodosas durante los temporales nocturnos.",
                            "En la construcción de una presa hidroeléctrica que divide el cauce en dos canales artificiales."
                        ],
                        "correctIndex": 1,
                        "explanation": "El río Negro y el Solimões fluyen juntos varios kilómetros sin combinarse debido a sus diferencias físicas y térmicas."
                    },
                    {
                        "question": "¿Qué monumento icónico simboliza el esplendor de la Belle Époque durante el ciclo del caucho en Manaus?",
                        "options": [
                            "La fortaleza de Santa Cruz de la Sierra.",
                            "El Teatro Amazonas, inaugurado en 1896 con materiales de lujo traídos íntegramente de Europa.",
                            "El acueducto de Carioca.",
                            "El Palacio de las Garzas en el delta del Orinoco."
                        ],
                        "correctIndex": 1,
                        "explanation": "El Teatro Amazonas personifica la riqueza extravagante que generó la exportación mundial del látex a fines del siglo XIX."
                    },
                    {
                        "question": "¿Qué función ecológica vital desempeñan los llamados 'ríos voladores' generados por la selva amazónica?",
                        "options": [
                            "Transportan sedimentos minerales hacia las plataformas petroleras del Atlántico norte.",
                            "Son gigantescas corrientes aéreas de vapor que transportan la humedad y regulan las precipitaciones en toda Sudamérica.",
                            "Enfrían las turbinas nucleares de las ciudades costeras.",
                            "Canalizan el vuelo migratorio de los pingüinos patagónicos hacia el trópico."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los árboles amazónicos bombean ingentes cantidades de vapor que forman ríos aéreos cruciales para el régimen de lluvias del continente."
                    }
                ]
            }
        }
    },
    "world/b2/b2-brasilinterior-03": {
        "id": "b2-brasilinterior-03",
        "title": "Soberanía indígena y la custodia de los pueblos aislados",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Los derechos ancestrales de los pueblos indígenas en Brasil: la Constitución de 1988 y la demarcación de Tierras Indígenas, el papel de la FUNAI y la política pionera de no contacto con pueblos aislados, y la figura histórica de los hermanos Villas-Bôas.",
        "characters": [
            "Orlando, Cláudio y Leonardo Villas-Bôas (indigenistas fundadores del Parque del Xingu)",
            "Líderes indígenas contemporáneos (Raoni Metuktire y Davi Kopenawa Yanomami)",
            "Técnicos de campo y agentes de la FUNAI encargados de la protección territorial"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Bajo la espesura del dosel selvático amazónico y en los confines más remotos de la cuenca continental, habitan los últimos grupos humanos del planeta que han decidido vivir en aislamiento voluntario, sin contacto permanente con la sociedad envolvente nacional. En el territorio de Brasil se tiene constancia comprobada de más de un centenar de registros de estos pueblos indígenas en aislamiento o de contacto reciente —concentrados principalmente en el valle del Yavarí, en la frontera con Perú, y en los estados de Acre, Amazonas, Rondônia y Mato Grosso—. Lejos de ser supervivencias arcaicas congeladas en el tiempo, estas comunidades representan decisiones deliberadas de repliegue defensivo adoptadas por pueblos soberanos para protegerse de las epidemias mortales de gripe y sarampión, del trabajo forzoso y de la violencia armada que sufrieron históricamente durante las sucesivas oleadas del extractivismo maderero, cauchero y mineral."
            },
            {
                "type": "narration",
                "text": "La política del Estado brasileño hacia estas poblaciones experimentó una transformación ética trascendental gracias al legado humanista de los legendarios hermanos Orlando, Cláudio y Leonardo Villas-Bôas en las décadas de 1950 y 1960. Al liderar la expedición Roncador-Xingu y convivir íntimamente con diversas etnias del Brasil central, los hermanos Villas-Bôas rompieron con la vieja ideología colonial integracionista que pretendía asimilar compulsivamente al indígena a la cultura blanca y campesina. Su denodada lucha condujo a la creación pionera en 1961 del Parque Indígena del Xingu: la primera gran reserva pluritétnica demarcada en América Latina, consagrada a garantizar la intangibilidad del territorio ancestral, la preservación de las cosmovisiones originarias y la autodeterminación cultural de los pueblos amazónicos."
            },
            {
                "type": "narration",
                "text": "Un hito jurídico de trascendencia continental se alcanzó con la promulgación de la Constitución de 1988 —la llamada 'Constitución Ciudadana'—, la cual consagró en sus artículos 231 y 232 el reconocimiento formal de los derechos originarios de los indígenas sobre las tierras que tradicionalmente ocupan. Conforme a este marco de vanguardia jurídica, las Tierras Indígenas (TI) fueron definidas como bienes de la Unión de usufructo exclusivo, inalienable e imprescriptible de las comunidades nativas. Asimismo, la Fundación Nacional de los Pueblos Indígenas (FUNAI) adoptó en 1987 la doctrina vanguardista de 'no contacto': el principio rector según el cual el Estado no debe forzar jamás el acercamiento con pueblos aislados, limitándose rigurosamente a demarcar, vigilar y proteger sus territorios contra cualquier intrusión externa invasora. Por ende, la Constitución proscribió terminantemente la remoción forzada de las comunidades nativas de sus hábitats ancestrales, garantizando que sus idiomas, costumbres y tradiciones espirituales gocen de tutela estatal preferente."
            },
            {
                "type": "narration",
                "text": "A pesar de este sólido andamiaje normativo, las Tierras Indígenas enfrentan en la actualidad presiones criminales continuas y extremadamente violentas por parte de redes ilegales de buscadores de oro ('garimpeiros'), taladores de maderas nobles y acaparadores de tierras agrícolas ('grileiros'). La dramática crisis humanitaria y sanitaria sufrida por el pueblo Yanomami en la frontera norte evidenció cómo la minería ilegal contamina los ríos con toneladas de mercurio tóxico, extermina la fauna ictícola y propaga brotes masivos de malaria y desnutrición infantil. Frente a estos atropellos, líderes indígenas de estatura internacional como el cacique Raoni Metuktire y el chamán Davi Kopenawa han alzado su voz en foros ecuménicos mundiales, recordando que los guardianes indígenas son la barrera biológica y moral más eficaz contra la destrucción climática planetaria. Asimismo, la movilización continental de la Articulación de los Pueblos Indígenas de Brasil (APIB) en Brasilia a través del histórico 'Campamento Tierra Libre' ha demostrado la pujanza política inquebrantable del movimiento nativo."
            },
            {
                "type": "narration",
                "text": "En definitiva, el reconocimiento de la soberanía y la intangibilidad de las tierras indígenas no constituye un privilegio corporativo aislado, sino una condición indispensable para el equilibrio ecológico del planeta y el honor moral de las repúblicas suramericanas. Los datos científicos satelitales son unánimes: las áreas forestales bajo custodia colectiva de los pueblos originarios registran los índices más bajos de deforestación e incendios de todo el continente. En última instancia, proteger a los pueblos aislados y respetar su derecho inalienable a existir en sus bosques ancestrales enseña a la civilización contemporánea una lección imprescindible de humildad cósmica: la demostración palmaria de que existen formas alternativas, armónicas y sabias de habitar la Tierra sin destruirla en el altar del consumo desenfrenado."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿En qué consiste el principio vanguardista de 'no contacto' aplicado por la FUNAI a los pueblos aislados?",
                        "options": [
                            "En forzar a las comunidades a trasladarse a internados en las capitales estatales.",
                            "En respetar su libre determinación de no interactuar, garantizando la protección estricta de sus tierras sin invadir su aislamiento.",
                            "En prohibirles el acceso a cualquier vacuna o atención médica incluso en emergencias territoriales.",
                            "En obligarlos a aprender portugués a través de emisiones radiales obligatorias."
                        ],
                        "correctIndex": 1,
                        "explanation": "La política de no contacto establece que el Estado debe proteger sus territorios sin interferir en su modo de vida aislado."
                    },
                    {
                        "question": "¿Cuál fue el papel histórico de los hermanos Villas-Bôas en la política indigenista brasileña?",
                        "options": [
                            "Fundaron compañías madereras para explotar los bosques vírgenes del río Madeira.",
                            "Impulsaron la creación del Parque Indígena del Xingu en 1961 promoviendo el respeto a la autodeterminación cultural indígena.",
                            "Diseñaron los planos de las fábricas textiles de São Paulo.",
                            "Redactaron los códigos mineros para autorizar la prospección de oro en reservas."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los hermanos Villas-Bôas promovieron la protección territorial comunitaria y el fin de las políticas de asimilación forzosa."
                    },
                    {
                        "question": "¿Qué estatus jurídico otorgó la Constitución de 1988 a las Tierras Indígenas en Brasil?",
                        "options": [
                            "Propiedades privadas que pueden ser embargadas y vendidas en remates bancarios.",
                            "Bienes de la Unión con usufructo exclusivo, permanente e inalienable concedido a las comunidades que las habitan.",
                            "Concesiones temporales renovables cada cinco años sujetas al pago de impuestos de timbre.",
                            "Zonas industriales libres de aranceles para corporaciones extranjeras."
                        ],
                        "correctIndex": 1,
                        "explanation": "La Constitución reconoció las tierras indígenas como territorios inalienables con usufructo exclusivo de los pueblos ancestrales."
                    }
                ]
            }
        }
    },
    "world/b2/b2-brasilinterior-04": {
        "id": "b2-brasilinterior-04",
        "title": "El Cerrado y el agronegocio: La encrucijada agroecológica",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La transformación agropecuaria del bioma del Cerrado: la sabana brasileña convertida en granero del mundo mediante la biotecnología de EMBRAPA, las tensiones entre las exportaciones récord de soja y carne y la preservación de los acuíferos y la biodiversidad.",
        "characters": [
            "Científicos e ingenieros agrónomos de EMBRAPA",
            "Productores agropecuarios tecnificados del Centro-Oeste",
            "Ecólogos y defensores de las fuentes hídricas del Cerrado"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Extendiéndose a lo largo de más de dos millones de kilómetros cuadrados en el corazón de la meseta central brasileña, el Cerrado representa la sabana tropical con mayor riqueza biológica del planeta, albergando a más de doce mil especies vegetales y cerca de mil especies de aves y mamíferos. Durante siglos, este bioma de suelos rojizos y árboles de troncos retorcidos fue considerado por los planificadores estatales como una planicie estéril y marginal, debido a la elevada acidez de su tierra y a la profunda toxicidad de sus concentraciones de aluminio natural. Sin embargo, a partir de la década de 1970, una revolución científica y biotecnológica sin precedentes protagonizada por la Empresa Brasileña de Investigación Agropecuaria (EMBRAPA) alteró radicalmente el destino productivo de la región: mediante la corrección masiva de la acidez edáfica con caliza molida y el desarrollo genético de variedades de soja adaptadas a latitudes tropicales, el Cerrado se transmutó en el mayor emporio agroexportador de América Latina."
            },
            {
                "type": "narration",
                "text": "Hoy en día, las mesetas interminables de estados como Mato Grosso, Goiás, Mato Grosso do Sul y la región agrícola de Matopiba concentran una maquinaria agroindustrial hipertecnificada que ha posicionado a Brasil como el primer productor y exportador mundial de soja en grano, carne bovina y avícola, azúcar y café, además de figurar entre los líderes globales en maíz y algodón. Cosechadoras satelitales guiadas por sistemas de navegación GPS y drones que monitorean milimétricamente la fertilización química de miles de hectáreas forman parte del paisaje cotidiano de ciudades como Sorriso o Rio Verde. Esta potencia agroexportadora genera decenas de miles de millones de dólares en divisas comerciales indispensables para la estabilidad macroeconómica nacional, abasteciendo de alimentos y proteínas esenciales a mercados gigantescos como la Unión Europea y la República Popular China."
            },
            {
                "type": "narration",
                "text": "Empero, este vertiginoso milagro agropecuario ha cobrado un precio ambiental desgarrador que amenaza con hipotecar la sustentabilidad hídrica y ecológica de todo el continente suramericano. Más de la mitad de la vegetación nativa original del Cerrado ha sido talada o fragmentada para dar paso a monocultivos intensivos y pasturas ganaderas extensivas. Los ecólogos denominan al Cerrado 'la cuna de las aguas de Brasil', puesto que en sus mesetas y acuíferos profundos —como el gigantesco Acuífero Guaraní y el Urucuia— nacen las cabeceras de ocho de las doce grandes cuencas hidrográficas del país, incluidas las de los ríos São Francisco, Tocantins-Araguaia y Paraná. La deforestación sistemática de sus raíces profundas disminuye drásticamente la capacidad de recarga de los acuíferos freáticos, desencadenando crisis hídricas graves en las grandes capitales costeras."
            },
            {
                "type": "narration",
                "text": "Asimismo, el uso indiscriminado de fertilizantes químicos y pesticidas en las planicies agropecuarias contamina los cursos de agua subterránea y pone en peligro la supervivencia de comunidades tradicionales como los 'geraizeiros', los recolectores de frutos silvestres como el pequi y el barú, y los pequeños agricultores familiares que practican un manejo diversificado y armónico del suelo. Frente a estas contradicciones, la comunidad científica insiste en que el modelo de expansión agropecuaria sobre nuevas fronteras forestales está agotado: el incremento de la producción no puede lograrse a costa de continuar arrasando la vegetación nativa, sino mediante la intensificación sostenible en tierras ya degradadas, la integración entre agricultura, ganadería y bosques (ILPF) y la bioeconomía regenerativa."
            },
            {
                "type": "narration",
                "text": "En conclusión, el dilema del Cerrado sintetiza el desafío civilizatorio cardinal del siglo veintiuno para los países emergentes: conciliar la seguridad alimentaria mundial y la generación de riqueza comercial con la preservación estricta de los ecosistemas que hacen posible la vida sobre la Tierra. Proteger lo que resta del Cerrado e impulsar su restauración ecológica no es un obstáculo para el desarrollo, sino su garantía indispensable de continuidad a largo plazo. En última instancia, una agricultura verdaderamente inteligente debe comprender que sin lluvia, sin polinizadores y sin suelo vivo no hay cosecha posible, y que la mayor riqueza de una nación no reside en los silos colmados de granos para la exportación, sino en la salud equilibrada de sus fuentes de agua y en la fertilidad generosa de su tierra madre."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué innovación científica de EMBRAPA permitió transformar el Cerrado en una potencia agropecuaria mundial?",
                        "options": [
                            "La desalinización de las aguas marinas en la costa atlántica.",
                            "La corrección de la acidez del suelo con caliza y el desarrollo de semillas de soja adaptadas al clima tropical.",
                            "La construcción de invernaderos climatizados con energía nuclear.",
                            "La importación de tractores a vapor desde Europa central."
                        ],
                        "correctIndex": 1,
                        "explanation": "El encalado para neutralizar el aluminio y la biotecnología tropical de EMBRAPA revolucionaron la agricultura del Cerrado."
                    },
                    {
                        "question": "¿Por qué los científicos denominan al bioma del Cerrado 'la cuna de las aguas' de Brasil?",
                        "options": [
                            "Porque alberga los puertos marítimos de mayor profundidad del océano Atlántico.",
                            "Porque en sus mesetas nacen las cabeceras de ocho de las principales cuencas hidrográficas de Sudamérica.",
                            "Porque es la región donde se registran los mayores glaciares andinos.",
                            "Porque concentra los mayores complejos de plantas embotelladoras de agua mineral del mundo."
                        ],
                        "correctIndex": 1,
                        "explanation": "El Cerrado alimenta las grandes cuencas fluviales suramericanas como el Amazonas, el Paraná y el São Francisco."
                    },
                    {
                        "question": "¿Cuál es la propuesta contemporánea de la ciencia para evitar la deforestación continua del Cerrado?",
                        "options": [
                            "Prohibir toda actividad agrícola y desalojar a la población del Centro-Oeste.",
                            "Aumentar la productividad en áreas ya deforestadas mediante sistemas integrados de agricultura, ganadería y bosques.",
                            "Sustituir los cultivos de cereales por la extracción exclusiva de carbón mineral.",
                            "Secar los acuíferos subterráneos para acelerar la pavimentación de carreteras."
                        ],
                        "correctIndex": 1,
                        "explanation": "La alternativa radica en la intensificación sostenible y la recuperación de pasturas degradadas sin avanzar sobre la vegetación nativa."
                    }
                ]
            }
        }
    },
    "world/b2/b2-brasilinterior-05": {
        "id": "b2-brasilinterior-05",
        "title": "Brasil en el tablero global: BRICS, Itamaraty y la multipolaridad",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La política exterior de Brasil y su proyección internacional: la prestigiosa tradición diplomática del Palacio de Itamaraty desde el Barón de Rio Branco, el rol protagónico en los BRICS y el G20, y la búsqueda de un orden multilateral más justo y equilibrado.",
        "characters": [
            "José Maria da Silva Paranhos Jr. (Barón de Rio Branco, forjador de la diplomacia brasileña)",
            "Diplomáticos de carrera del Palacio de Itamaraty",
            "Representantes de las naciones del Sur Global y delegados ante los BRICS"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Con una extensión territorial que supera los ocho millones y medio de kilómetros cuadrados, una población de más de doscientos quince millones de ciudadanos y la mayor economía de América Latina, la República Federativa de Brasil ha sido históricamente una potencia de vocación pacífica y multilateral. En el corazón de esta proyección internacional se encuentra el Ministerio de Relaciones Exteriores, conocido universalmente como 'Itamaraty'. Con sede en el elegante palacio diseñado por Oscar Niemeyer en Brasilia —adornado con jardines flotantes del paisajista Roberto Burle Marx y arcos monumentales sobre espejos de agua—, Itamaraty es reconocido unánimemente como una de las escuelas diplomáticas profesionales más rigurosas y respetadas del mundo, dotada de una cultura de Estado que trasciende los vaivenes de las alternancias partidistas electorales."
            },
            {
                "type": "narration",
                "text": "La doctrina diplomática brasileña fue forjada a comienzos del siglo veinte por su figura consular más insigne: José Maria da Silva Paranhos Jr., el legendario Barón de Rio Branco. Como ministro de Relaciones Exteriores entre 1902 y 1912, Rio Branco resolvió de manera brillante y pacífica, mediante el arbitraje jurídico internacional y negociaciones bilaterales directas, todas las complejas controversias fronterizas con las diez naciones vecinas de América del Sur, incorporando al patrimonio soberano nacional más de novecientos mil kilómetros cuadrados de territorio sin disparar un solo cañón bélico. Desde entonces, los principios cardinales de Itamaraty han sido la solución pacífica de las controversias, la no intervención en los asuntos internos de otros Estados, la autodeterminación de los pueblos y la defensa irrenunciable del multilateralismo institucional."
            },
            {
                "type": "narration",
                "text": "En el siglo veintiuno, Brasil cobró un protagonismo geopolítico estelar al participar activamente como miembro fundador en la conformación del bloque de los BRICS (Brasil, Rusia, India, China y Sudáfrica), foro que reúne a las principales economías emergentes del planeta. A través de este mecanismo de concertación y de la creación del Nuevo Banco de Desarrollo (NBD), con sede en Shanghái, la diplomacia brasileña busca contrapesar la hegemonía financiera tradicional de las instituciones de Bretton Woods, impulsando el comercio en monedas locales y canalizando inversiones multimillonarias hacia obras de infraestructura y energía limpia en el Sur Global. Asimismo, Brasil ha liderado debates decisivos en el seno del G20 y de las Naciones Unidas reclamando con firmeza la reforma estructural del Consejo de Seguridad para conceder asientos permanentes a naciones de América Latina y África."
            },
            {
                "type": "narration",
                "text": "No obstante este liderazgo ecuménico, la proyección exterior de Brasil enfrenta complejos equilibrios y dilemas estratégicos en un escenario mundial signado por la rivalidad hegemónica entre las grandes superpotencias. Por una parte, la economía brasileña mantiene vínculos comerciales simbióticos con China, su principal comprador de materias primas minerales y agropecuarias; por otra, sostiene estrechos lazos históricos, culturales y de cooperación democrática con los Estados Unidos y la Unión Europea. Frente a estas tensiones, la diplomacia de Itamaraty ha reivindicado la doctrina de la 'autonomía por la diversificación' o 'no alineamiento activo', negándose a adherir de forma subordinada a bloques ideológicos excluyentes y preservando su capacidad soberana de negociar y mediar con todos los actores de la comunidad internacional. Por añadidura, la diplomacia brasileña ha promovido iniciativas pioneras de cooperación Sur-Sur en transferencia tecnológica agropecuaria, salud pública comunitaria y energías renovables en África subsahariana y el Caribe, consolidando su prestigio de socio solidario y horizontal."
            },
            {
                "type": "narration",
                "text": "En suma, la voz de Brasil en el concierto de las naciones se erige como un puente indispensable entre el Norte desarrollado y el Sur emergente, defendiendo que la paz y el progreso universal son inalcanzables sin un orden multipolar basado en la justicia distributiva y la cooperación solidaria. Desde la preservación de la selva amazónica frente a la emergencia climática global hasta la lucha frontal contra el hambre y la pobreza endémica, Brasil demuestra que una potencia continental no necesita del poder nuclear ni de la intimidación armada para influir decisivamente en el rumbo de la humanidad. En definitiva, el mayor capital de la diplomacia brasileña reside en su autoridad moral como constructora de consensos, demostrando que el diálogo respetuoso y el derecho internacional continúan siendo las herramientas más nobles para forjar un porvenir compartido."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál fue el mayor logro histórico del Barón de Rio Branco al frente de la cancillería de Itamaraty?",
                        "options": [
                            "La invasión armada de las repúblicas vecinas durante las guerras del Pacífico.",
                            "La delimitación pacífica de todas las fronteras de Brasil mediante arbitrajes y negociaciones sin recurrir a la guerra.",
                            "La firma de tratados coloniales de protectorado con el Imperio británico.",
                            "La compra de islas en el Caribe para instalar colonias penitenciarias."
                        ],
                        "correctIndex": 1,
                        "explanation": "Rio Branco consolidó las fronteras definitivas de Brasil exclusivamente por la vía diplomática y el arbitraje."
                    },
                    {
                        "question": "¿Qué objetivo persigue Brasil al participar en el bloque de los BRICS y el Nuevo Banco de Desarrollo?",
                        "options": [
                            "Promover un orden internacional multipolar y financiar infraestructura en el Sur Global equilibrando la hegemonía occidental.",
                            "Crear una moneda de oro obligatoria para los turistas europeos.",
                            "Disolver las Naciones Unidas para sustituirlas por una asamblea militar.",
                            "Prohibir el comercio marítimo en el océano Atlántico."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los BRICS buscan democratizar la gobernanza global y proporcionar financiamiento soberano a economías emergentes."
                    },
                    {
                        "question": "¿En qué consiste la doctrina diplomática del 'no alineamiento activo' reivindicada por Itamaraty?",
                        "options": [
                            "En negarse a firmar acuerdos comerciales con países vecinos.",
                            "En mantener autonomía soberana y vínculos equilibrados con todas las potencias mundiales sin subordinarse a bloques rivales.",
                            "En retirar a todos los embajadores brasileños de los foros multilaterales.",
                            "En adoptar automáticamente la política exterior de una sola superpotencia hegemónica."
                        ],
                        "correctIndex": 1,
                        "explanation": "El no alineamiento activo permite a Brasil defender sus intereses nacionales negociando libremente con todos los actores globales."
                    }
                ]
            }
        }
    },
    "world/b2/b2-brasilinterior-consolidation": {
        "id": "b2-brasilinterior-consolidation",
        "title": "El corazón continental de Brasil y los horizontes del interior",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Síntesis reflexiva sobre el interior de Brasil: la audacia utópica de Brasilia, la majestad fluvial de la Amazonía, la protección de los pueblos indígenas aislados, el dilema ecológico del Cerrado y el papel diplomático del país en el orden multipolar.",
        "characters": [
            "Narradores y cronistas del Brasil profundo",
            "Pueblos indígenas, ribereños y constructores como protagonistas colectivos"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al contemplar la inmensidad del interior brasileño desde las alturas de la meseta central de Brasilia o desde la cubierta de un vapor fluvial que navega las aguas titánicas del río Amazonas, el viajero atento comprende que este país continental no puede ser medido con las categorías estrechas de una nación corriente. En primer término, Brasil es un cosmos geográfico y humano en perpetua construcción, donde conviven en íntima tensión las vanguardias modernistas más atrevidas y las tradiciones ancestrales más arraigadas del planeta. Es decir, internarse en el 'hinterland' no supone alejarse de la modernidad, sino descender a las raíces profundas donde se define verdaderamente la soberanía territorial, la equidad social y el destino ecológico de más de doscientos millones de habitantes que miran con orgullo hacia el futuro compartido."
            },
            {
                "type": "narration",
                "text": "En las altiplanicies del Cerrado, la silueta inconfundible de Brasilia se levanta como un manifiesto imperecedero de audacia estética y fe cívica en el porvenir colectivo. Por una parte, las curvas poéticas de Oscar Niemeyer y la geometría rigurosa del Plan Piloto de Lucio Costa demostraron al mundo que una sociedad del Sur podía imaginar una capital de vanguardia funcional; por otra parte, la memoria indeleble de los obreros 'candangos' recuerda a las generaciones presentes que ningún monumento soberano perdura si olvida la dignidad de quienes lo edificaron con sus manos laboriosas. Asimismo, en las vastas llanuras agrícolas que rodean la capital federal, la formidable potencia agroexportadora de la soja y los cereales interpela a la sociedad sobre la necesidad inaplazable de preservar las cabeceras hídricas y restaurar la biodiversidad de la sabana antes de que se extingan sus fuentes sagradas. Del mismo modo, la arquitectura monumental de Brasilia sigue interpelando a los urbanistas contemporáneos sobre los límites de la ciudad planificada y la urgencia de integrar transportes colectivos dignos y espacios peatonales para toda la ciudadanía."
            },
            {
                "type": "narration",
                "text": "Hacia el norte colosal, el reino fluvial de la Amazonía despliega su laberinto de ríos caudalosos y bosques centenarios, custodiando el mayor reservorio biológico de la Tierra. Desde la opulencia lírica del Teatro Amazonas en Manaus hasta el estallido sensorial y gastronómico del mercado de Ver-o-Peso en Belém do Pará, la civilización ribereña ha aprendido a convivir con el pulso sagrado de las crecidas y los meandros. No obstante las presiones destructivas del extractivismo depredador, la selva en pie demuestra cotidianamente su valor infinito mediante los 'ríos voladores' que alimentan las cosechas del continente y regulan el equilibrio climático mundial, ratificando que la Amazonía no es un recurso descartable, sino el corazón biológico indispensable que oxigena y refresca a toda la humanidad."
            },
            {
                "type": "narration",
                "text": "En el plano ético y humano más elevado, la defensa inquebrantable de las Tierras Indígenas y de los pueblos en aislamiento voluntario consagra el principio cardinal de la diversidad civilizatoria frente a la uniformidad colonialista. Al acatar la doctrina de no contacto y demarcar los territorios ancestrales, el Estado brasileño rinde homenaje a los guardianes originarios del bosque, reconociendo que su sabiduría milenaria no pertenece al pasado, sino que encarna la brújula ecológica más lúcida para encarar las incertidumbres del cambio climático contemporáneo. Con todo, la fiscalización de las fronteras demarcadas exige un coraje cívico permanente que impida la impunidad de las mafias madereras y mineras, garantizando la paz y la vida digna de las comunidades nativas en sus territorios inviolables. Por ende, la preservación de los saberes etnobotánicos de los ancianos y chamanes tradicionales constituye un patrimonio inmaterial invaluable que la ciencia médica contemporánea empieza apenas a comprender y valorar con admiración creciente."
            },
            {
                "type": "narration",
                "text": "En suma, la proyección de Brasil en el tablero global a través de los BRICS, de los foros multilaterales y de la centenaria tradición diplomática de Itamaraty refleja la vocación ecuménica de una nación continental que aspira a un orden internacional multipolar, pacífico y solidario. En última instancia, la verdadera grandeza de Brasil no reside en la extensión de sus fronteras terrestres ni en el poderío de sus balances comerciales, sino en la generosidad inagotable de su pueblo para soñar futuros luminosos, proteger su naturaleza deslumbrante y compartir con la comunidad de naciones una inquebrantable vocación de fraternidad, justicia cívica y concordia universal."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis territorial y humana representa el interior de Brasil explorado a lo largo de la unidad?",
                        "options": [
                            "Un enclave minero administrado por compañías foráneas sin identidad nacional.",
                            "Un espacio donde conviven la audacia modernista de Brasilia, la riqueza fluvial de la Amazonía y los dilemas ecológicos del Cerrado.",
                            "Una región completamente deshabitada que carece de ríos y recursos naturales.",
                            "Un archipiélago atlántico aislado de las dinámicas económicas de América Latina."
                        ],
                        "correctIndex": 1,
                        "explanation": "El interior sintetiza la vanguardia de Brasilia, la ecología amazónica y las tensiones del agronegocio en el Cerrado."
                    },
                    {
                        "question": "¿Por qué es crucial la preservación del bioma amazónico para el conjunto del continente americano?",
                        "options": [
                            "Porque produce los 'ríos voladores' de vapor que regulan las lluvias y estabilizan el clima en toda Sudamérica.",
                            "Porque es la única fuente de madera para la construcción de barcos transatlánticos.",
                            "Porque contiene las principales plantas de refinación nuclear del hemisferio sur.",
                            "Porque impide el flujo de los vientos alisios hacia las zonas árticas."
                        ],
                        "correctIndex": 0,
                        "explanation": "La transpiración selvática genera ríos aéreos de vapor que abastecen de lluvias vitales a toda la cuenca del Plata y el cono sur."
                    },
                    {
                        "question": "¿Qué lección ética aporta la política de protección y demarcación de Tierras Indígenas?",
                        "options": [
                            "Que las tierras comunitarias deben privatizarse para aumentar la recaudación fiscal.",
                            "Que la diversidad cultural y el respeto a los pueblos ancestrales son indispensables para la sustentabilidad del planeta.",
                            "Que los pueblos indígenas deben abandonar sus lenguas para acelerar su asimilación urbana.",
                            "Que el Estado debe permitir la minería ilegal en todas las reservas selváticas."
                        ],
                        "correctIndex": 1,
                        "explanation": "La protección indígena demuestra que las culturas originarias son las mejores guardianas de la biodiversidad planetaria."
                    }
                ]
            }
        }
    },
    "world/b2/b2-brasilinterior": {
        "id": "b2-brasilinterior",
        "title": "Brasil III: La Amazonía, Brasilia y la geopolítica del interior",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 20,
        "summary": "Compendio panorámico sobre el interior continental de Brasil: la gesta modernista y geopolítica de Brasilia, la inmensidad fluvial de la Amazonía con Manaus y Belém, la soberanía de los pueblos indígenas aislados y el principio de no contacto, la encrucijada agroecológica del Cerrado y el liderazgo de Brasil en los BRICS e Itamaraty.",
        "characters": [
            "Juscelino Kubitschek, Lucio Costa y Oscar Niemeyer",
            "Científicos del INPA y recolectores del mercado de Ver-o-Peso",
            "Hermanos Villas-Bôas y líderes indígenas contemporáneos",
            "Diplomáticos de carrera del Palacio de Itamaraty"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el vasto corazón geográfico de América del Sur, lejos de los litorales atlánticos donde comenzó la colonización europea, se extiende la masa continental más imponente, diversa y decisiva de la civilización brasileña: el interior profundo. Integrado por los biomas monumentales de la Amazonía, el Cerrado y el Pantanal, este territorio descomunal fue durante siglos una frontera esquiva y mitificada, habitada por pueblos originarios soberanos y recorrida por osadas expediciones fluviales. En el siglo veinte, la nación brasileña asumió el desafío histórico de refundar su destino geopolítico trasladando su centro gravitacional hacia la meseta central, demostrando al mundo que la integración de sus inmensidades territoriales constituía la premisa fundamental para forjar una república verdaderamente soberana, justa y equilibrada. Asimismo, la red de afluentes y humedales del Pantanal matogrossense completa este tapiz geográfico excepcional al constituir la mayor llanura inundable del planeta, refugio de jaguares, caimanes y aves migratorias que asombran a naturalistas de todos los continentes."
            },
            {
                "type": "narration",
                "text": "La manifestación más rotunda de aquella audacia soberana fue la fundación de Brasilia en 1960 bajo el liderazgo visionario de Juscelino Kubitschek. Diseñada en forma de aeroplano por el urbanista Lucio Costa en su célebre Plan Piloto y embellecida por las sensuales curvas escultóricas de hormigón armado de Oscar Niemeyer, la nueva capital federal materializó la aspiración de armonizar la vanguardia estética con la función pública republicana. No obstante la monumentalidad de sus palacios y supercuadras, la historia reconoce hoy con profunda emoción el sacrificio de los 'candangos', los campesinos migrantes nordestinos que con su sudor heroico erigieron una metrópoli completa en medio de la soledad del Cerrado en menos de mil días. Por otra parte, la plaza de los Tres Poderes resume en su trazado geométrico el equilibrio constitucional y la transparencia republicana que anhelaban los forjadores del Brasil contemporáneo."
            },
            {
                "type": "narration",
                "text": "Hacia el norte, la cuenca del río Amazonas despliega el mayor sistema de agua dulce y de selva tropical del globo terráqueo, comunicando la cordillera andina con el océano Atlántico a través de arterias fluviales colosales. Ciudades emblemáticas como Manaus —inmortalizada por el esplendor del Teatro Amazonas durante la Belle Époque de la goma elástica y el 'Encuentro de las Aguas'— y Belém do Pará, con su deslumbrante mercado botánico y gastronómico de Ver-o-Peso, evidencian la vitalidad incombustible de la cultura ribereña. Asimismo, la protección de este bioma frente a la tala destructiva resulta prioritaria para la estabilidad climática global, dado que los 'ríos voladores' que exhala el bosque regulan el régimen de lluvias en todo el cono sur de las Américas. Por consiguiente, los habitantes ribereños han desarrollado una sabiduría ecológica admirable que armoniza la recolección estacional del caucho y la castaña de Pará con el respeto reverente a los ciclos vitales de los grandes caudales."
            },
            {
                "type": "narration",
                "text": "En las profundidades de la selva y las sabanas, la custodia de las Tierras Indígenas consagra un pacto ético de rango constitucional en defensa de la vida ancestral y de los pueblos en aislamiento voluntario. Gracias a la doctrina de 'no contacto' consagrada por la FUNAI y el legado humanista del Parque Indígena del Xingu promovido por los hermanos Villas-Bôas, Brasil lidera a nivel mundial la protección territorial de comunidades que han elegido soberanamente preservar su modo de vida tradicional. Del mismo modo, en las planicies del Cerrado, la transformación agropecuaria impulsada por la biotecnología de EMBRAPA encara hoy el dilema urgente de frenar la deforestación de las cabeceras hídricas para garantizar la sustentabilidad hídrica a largo plazo."
            },
            {
                "type": "narration",
                "text": "En el escenario internacional, la proyección exterior de Brasil a través de la prestigiosa escuela diplomática de Itamaraty y su rol protagónico en los BRICS reafirman la vocación multipolar y pacífica de una potencia suramericana comprometida con el desarrollo soberano y la cooperación entre iguales. En definitiva, recorrer el interior brasileño enseña al continente entero que el progreso humano verdadero no estriba en el saqueo indiscriminado de los recursos naturales, sino en la capacidad ética y estética de edificar una civilización solidaria que sepa honrar a sus pueblos originarios, armonizar la ciencia con la naturaleza y proyectar una voz fraterna en el concierto pacífico de las naciones. Del mismo modo, la defensa inclaudicable del multilateralismo y de la paz ecuménica demuestra que el diálogo honesto y la soberanía compartida son los pilares fundamentales para edificar un siglo veintiuno más justo para todos los pueblos del orbe."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué representó geopolíticamente la fundación de Brasilia en el corazón del Cerrado en 1960?",
                        "options": [
                            "Un enclave militar fronterizo para disputar territorios con Bolivia.",
                            "El traslado refundacional del centro de poder para integrar el interior continental despoblado y equilibrar la república.",
                            "Una urbanización exclusivamente industrial para la fabricación de automóviles.",
                            "Una ciudad balnearia construida para el turismo náutico internacional."
                        ],
                        "correctIndex": 1,
                        "explanation": "Brasilia simbolizó la marcha hacia el oeste y la integración soberana del interior brasileño."
                    },
                    {
                        "question": "¿Cuál es la importancia ecológica global de la selva amazónica y sus 'ríos voladores'?",
                        "options": [
                            "Son corrientes aéreas de vapor de agua que regulan las lluvias y el equilibrio climático de todo el cono sur.",
                            "Son rutas de navegación aérea reservadas para hidroaviones de rescate militar.",
                            "Son ríos artificiales construidos para desecar los humedales del Pantanal.",
                            "Son canales de riego subterráneos que alimentan las plantaciones de café del sureste."
                        ],
                        "correctIndex": 0,
                        "explanation": "La transpiración amazónica transporta inmensas masas de vapor vitales para el ciclo hidrológico continental."
                    },
                    {
                        "question": "¿Qué principio rector guía la política de la FUNAI respecto a los pueblos indígenas en aislamiento voluntario?",
                        "options": [
                            "La asimilación lingüística forzosa en misiones religiosas.",
                            "La doctrina de 'no contacto' que garantiza la delimitación y protección estricta de sus tierras ancestrales.",
                            "La reubicación compulsiva en ciudades periféricas.",
                            "La entrega de concesiones mineras dentro de sus territorios."
                        ],
                        "correctIndex": 1,
                        "explanation": "La política de no contacto respeta la autodeterminación de los pueblos aislados protegiendo sus territorios de invasiones."
                    }
                ]
            }
        }
    }
}

EXERCISES_DATA = {
    "b2-31-01": [
        {
            "id": "b2-31-01-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["marcadores-consecutivos-formales"],
            "question": "¿Qué marcador consecutivo formal exige obligatoriamente el modo subjuntivo en la cláusula que introduce?",
            "options": [
                "Por consiguiente",
                "Por ende",
                "De ahí que",
                "En consecuencia"
            ],
            "correct": 2
        },
        {
            "id": "b2-31-01-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["marcadores-consecutivos-formales"],
            "sentence": "Las pruebas documentales no eran contundentes, de ahí que el magistrado __ la absolución del reo.",
            "answer": "decretara",
            "english": "The documentary evidence was not conclusive, which is why the magistrate ordered the defendant's acquittal."
        },
        {
            "id": "b2-31-01-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-31-01-vocab"],
            "pairs": [
                ["por consiguiente", "consequently"],
                ["por ende", "therefore / hence"],
                ["corolario", "corollary"],
                ["axiomático", "axiomatic"]
            ]
        },
        {
            "id": "b2-31-01-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cómo se puntúan generalmente marcadores oracionales como 'por consiguiente' o 'por ende' cuando inician una cláusula?",
            "options": [
                "Van siempre unidos con un guion corto.",
                "Van seguidos de una coma obligatoria que los separa del resto de la oración.",
                "Nunca llevan signos de puntuación cercanos.",
                "Se escriben siempre entre signos de interrogación."
            ],
            "correct": 1
        }
    ],
    "b2-31-02": [
        {
            "id": "b2-31-02-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["marcadores-consecutivos-coloquiales"],
            "question": "¿Cuál es la grafía correcta del conector consecutivo coloquial equivalente a 'así que'?",
            "options": [
                "Con que",
                "Con qué",
                "Conque",
                "Con qué que"
            ],
            "correct": 2
        },
        {
            "id": "b2-31-02-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["marcadores-consecutivos-coloquiales"],
            "sentence": "Ya revisamos el borrador final, __ que podemos imprimirlo ahora mismo.",
            "answer": "así",
            "english": "We have already reviewed the final draft, so we can print it right now."
        },
        {
            "id": "b2-31-02-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-31-02-vocab"],
            "pairs": [
                ["así que", "so / therefore"],
                ["conque", "so / then"],
                ["desenlace", "outcome"],
                ["repercusión", "repercussion"]
            ]
        },
        {
            "id": "b2-31-02-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué matiz modal expresa 'de modo que' cuando rige modo subjuntivo?",
            "options": [
                "Constatación de un hecho histórico pasado consumado.",
                "Finalidad, propósito o mandato indirecto atenuado.",
                "Duda epistémica absoluta sobre el pasado.",
                "Causa retrospectiva no comprobable."
            ],
            "correct": 1
        }
    ],
    "b2-31-03": [
        {
            "id": "b2-31-03-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["marcadores-causales-complejos"],
            "question": "¿Cuál de las siguientes locuciones causales complejas pertenece de manera eminente al lenguaje jurídico y administrativo formal?",
            "options": [
                "Es que",
                "Toda vez que",
                "Porque sí",
                "Como que"
            ],
            "correct": 1
        },
        {
            "id": "b2-31-03-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["marcadores-causales-complejos"],
            "sentence": "__ que el tiempo apremia, procederemos a la votación formal del dictamen.",
            "answer": "Visto",
            "english": "Seeing that time is pressing, we will proceed to the formal vote on the report."
        },
        {
            "id": "b2-31-03-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-31-03-vocab"],
            "pairs": [
                ["dado que", "given that"],
                ["toda vez que", "inasmuch as"],
                ["etiología", "causation"],
                ["subyacer", "to underlie"]
            ]
        },
        {
            "id": "b2-31-03-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué posición suelen ocupar en el periodo oracional locuciones como 'dado que' o 'visto que' en textos analíticos?",
            "options": [
                "Se sitúan frecuentemente al inicio para encuadrar la premisa que legitima la aserción principal.",
                "Solo pueden colocarse como palabra final de un párrafo.",
                "Se insertan únicamente dentro del predicado nominal.",
                "Deben acompañar siempre a un gerundio compuesto."
            ],
            "correct": 0
        }
    ],
    "b2-31-04": [
        {
            "id": "b2-31-04-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["marcadores-ilativos-deductivos"],
            "question": "En la máxima filosófica clásica 'Pienso, luego existo', ¿qué valor gramatical asume la palabra 'luego'?",
            "options": [
                "Adverbio de tiempo cronológico posterior.",
                "Conector ilativo-deductivo equivalente a 'por lo tanto'.",
                "Interjección exclamativa de asombro.",
                "Preposición de lugar equivalente a 'detrás de'."
            ],
            "correct": 1
        },
        {
            "id": "b2-31-04-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["marcadores-ilativos-deductivos"],
            "sentence": "Las pruebas experimentales arrojaron resultados idénticos; por __, la hipótesis quedó validada.",
            "answer": "tanto",
            "english": "The experimental tests yielded identical results; therefore, the hypothesis was validated."
        },
        {
            "id": "b2-31-04-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-31-04-vocab"],
            "pairs": [
                ["por tanto", "therefore"],
                ["silogismo", "syllogism"],
                ["postulado", "postulate"],
                ["concluyente", "conclusive"]
            ]
        },
        {
            "id": "b2-31-04-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué distingue a la ilación lógica de la simple sucesión cronológica de sucesos?",
            "options": [
                "La ilación establece que el segundo juicio se deduce necesariamente del primero por razonamiento.",
                "La ilación indica que ambos hechos ocurrieron en continentes diferentes.",
                "La ilación niega que exista cualquier causa física.",
                "La ilación solo se utiliza en la poesía renacentista."
            ],
            "correct": 0
        }
    ],
    "b2-31-05": [
        {
            "id": "b2-31-05-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["marcadores-causa-efecto-subjetiva"],
            "question": "¿Qué función discursiva cumple la locución 'es que' al inicio de una respuesta interpersonal?",
            "options": [
                "Expresar una orden militar terminante.",
                "Introducir una justificación, pretexto o excusa atenuante ante una pregunta o reproche previo.",
                "Formular una pregunta retórica impersonal.",
                "Indicar el inicio de un cántico litúrgico."
            ],
            "correct": 1
        },
        {
            "id": "b2-31-05-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["marcadores-causa-efecto-subjetiva"],
            "sentence": "Apúrate con la maleta, __ el tren está a punto de partir hacia el interior.",
            "answer": "que",
            "english": "Hurry up with your suitcase, for the train is about to depart for the interior."
        },
        {
            "id": "b2-31-05-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-31-05-vocab"],
            "pairs": [
                ["es que", "the thing is that"],
                ["pretexto", "pretext / excuse"],
                ["alegar", "to plead / to allege"],
                ["convicción", "conviction"]
            ]
        },
        {
            "id": "b2-31-05-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿En qué se diferencia el conector causal 'pues' de 'porque' en la prosa literaria culta?",
            "options": [
                "'Pues' nunca puede introducir una oración explicativa.",
                "'Pues' suele introducir una justificación explicativa estilísticamente más elegante y pausada.",
                "'Pues' es un anglicismo recién introducido.",
                "'Pues' obliga siempre a conjugar el verbo en futuro imperfecto."
            ],
            "correct": 1
        }
    ],
    "b2-31-consolidation": [
        {
            "id": "b2-31-con-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["marcadores-consecutivos-formales"],
            "question": "Elige la oración que respeta el régimen verbal normativo de 'de ahí que':",
            "options": [
                "El temporal derribó los postes, de ahí que la ciudad quedó a oscuras.",
                "El temporal derribó los postes, de ahí que la ciudad quedara a oscuras.",
                "El temporal derribó los postes, de ahí que la ciudad quedará a oscuras.",
                "El temporal derribó los postes, de ahí que la ciudad queda a oscuras."
            ],
            "correct": 1
        },
        {
            "id": "b2-31-con-ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["marcadores-causales-complejos"],
            "question": "¿Cuál de los siguientes marcadores causales complejos encabeza una premisa comprobada en registro formal?",
            "options": [
                "Dado que",
                "Conque",
                "Así que",
                "O sea"
            ],
            "correct": 0
        },
        {
            "id": "b2-31-con-ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["marcadores-ilativos-deductivos"],
            "sentence": "La premisa mayor y la menor son ciertas; en __, la conclusión resulta incontrovertible.",
            "answer": "consecuencia",
            "english": "The major premise and the minor premise are true; in consequence, the conclusion is incontrovertible."
        },
        {
            "id": "b2-31-con-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es el rasgo central de la novela 'La hora de la estrella' de Clarice Lispector?",
            "options": [
                "La narración de batallas navales en el Atlántico.",
                "La indagación existencial sobre la mecanógrafa Macabéa mediada por las dudas del narrador Rodrigo S.M.",
                "Un manual técnico sobre la industria textil en Río de Janeiro.",
                "Una crónica policial sobre contrabandistas de diamantes."
            ],
            "correct": 1
        }
    ],
    "b2-brasilinterior-01": [
        {
            "id": "b2-brasilinterior-01-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["interior-subordinadas-consecutivas-intensivas"],
            "question": "¿Qué conector correlativo introduce una subordinada consecutiva intensiva?",
            "options": [
                "Para que",
                "Tan... que",
                "A fin de que",
                "Antes de que"
            ],
            "correct": 1
        },
        {
            "id": "b2-brasilinterior-01-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["interior-subordinadas-consecutivas-intensivas"],
            "sentence": "Las curvas de los palacios eran __ audaces que asombraron a los urbanistas del mundo entero.",
            "answer": "tan",
            "english": "The palaces' curves were so bold that they astonished urban planners worldwide."
        },
        {
            "id": "b2-brasilinterior-01-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["brasil-interior-01-vocab"],
            "pairs": [
                ["trazado", "layout / master plan"],
                ["hormigón", "concrete"],
                ["curvatura", "curvature"],
                ["vanguardista", "avant-garde"]
            ]
        },
        {
            "id": "b2-brasilinterior-01-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Quién diseñó el trazado urbanístico del Plan Piloto de Brasilia en 1957?",
            "options": [
                "Oscar Niemeyer",
                "Lucio Costa",
                "Roberto Burle Marx",
                "Juscelino Kubitschek"
            ],
            "correct": 1
        }
    ],
    "b2-brasilinterior-02": [
        {
            "id": "b2-brasilinterior-02-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["interior-oraciones-temporales-avanzadas"],
            "question": "¿Qué construcción temporal expresa inmediatez absoluta sin necesidad de conjugar un verbo subordinado?",
            "options": [
                "A medida que",
                "Nada más + infinitivo",
                "Al cabo de",
                "Conforme"
            ],
            "correct": 1
        },
        {
            "id": "b2-brasilinterior-02-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["interior-oraciones-temporales-avanzadas"],
            "sentence": "A __ que la barcaza avanzaba por el río Negro, el cauce se ensanchaba como un océano dulce.",
            "answer": "medida",
            "english": "As the barge moved along the Negro River, the channel widened like a freshwater ocean."
        },
        {
            "id": "b2-brasilinterior-02-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["brasil-interior-02-vocab"],
            "pairs": [
                ["cuenca", "river basin"],
                ["afluente", "tributary"],
                ["caudaloso", "mighty / high-flow"],
                ["igarapé", "creek / stream"]
            ]
        },
        {
            "id": "b2-brasilinterior-02-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es la causa científica por la que el río Negro y el Solimões no se mezclan inmediatamente en Manaus?",
            "options": [
                "La existencia de un muro de contención construido en el siglo dieciocho.",
                "Diferencias notables en su densidad, temperatura y velocidad de corriente.",
                "La presencia de especies de peces incompatibles.",
                "La salinidad extrema de las aguas procedentes de los Andes."
            ],
            "correct": 1
        }
    ],
    "b2-brasilinterior-03": [
        {
            "id": "b2-brasilinterior-03-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["interior-perifrasis-obligacion-atenuada"],
            "question": "¿Qué matiz aspectual y estilístico aporta la perífrasis 'haber de + infinitivo' frente a 'tener que + infinitivo'?",
            "options": [
                "Un matiz solemne, deontológico y ético propio del discurso formal.",
                "Una duda radical sobre la existencia del sujeto.",
                "Una acción pasada que nunca llegó a verificarse.",
                "Una costumbre gastronómica familiar."
            ],
            "correct": 0
        },
        {
            "id": "b2-brasilinterior-03-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["interior-perifrasis-obligacion-atenuada"],
            "sentence": "El Estado __ de salvaguardar la intangibilidad de las tierras de los pueblos aislados.",
            "answer": "ha",
            "english": "The State has to safeguard the intangibility of the lands of uncontacted peoples."
        },
        {
            "id": "b2-brasilinterior-03-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["brasil-interior-03-vocab"],
            "pairs": [
                ["demarcación", "demarcation"],
                ["intangible", "inviolable"],
                ["salvaguarda", "safeguard"],
                ["cosmovisión", "worldview"]
            ]
        },
        {
            "id": "b2-brasilinterior-03-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué reserva emblemática crearon en 1961 los hermanos Villas-Bôas en el Brasil central?",
            "options": [
                "El Parque Nacional del Pantanal.",
                "El Parque Indígena del Xingu.",
                "La Reserva Biológica de Marajó.",
                "El Parque Histórico de los Palmares."
            ],
            "correct": 1
        }
    ],
    "b2-brasilinterior-04": [
        {
            "id": "b2-brasilinterior-04-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["interior-conectores-contraargumentativos-formales"],
            "question": "¿Cuál de los siguientes conectores contraargumentativos es un cultismo equivalente a 'sin embargo' propio del registro ensayístico?",
            "options": [
                "Pero",
                "Empero",
                "O sea",
                "Es más"
            ],
            "correct": 1
        },
        {
            "id": "b2-brasilinterior-04-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["interior-conectores-contraargumentativos-formales"],
            "sentence": "Las exportaciones de soja batieron récords históricos; con __, persisten graves alertas ecológicas.",
            "answer": "todo",
            "english": "Soybean exports broke historical records; all the same, severe ecological alerts persist."
        },
        {
            "id": "b2-brasilinterior-04-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["brasil-interior-04-vocab"],
            "pairs": [
                ["deforestación", "deforestation"],
                ["monocultivo", "monoculture"],
                ["acuífero", "aquifer"],
                ["sostenibilidad", "sustainability"]
            ]
        },
        {
            "id": "b2-brasilinterior-04-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Por qué la deforestación del Cerrado perjudica el régimen hídrico de todo Brasil?",
            "options": [
                "Porque en el Cerrado se ubican los glaciares que abastecen de hielo a los puertos.",
                "Porque sus mesetas y acuíferos profundos alimentan ocho de las doce grandes cuencas fluviales del país.",
                "Porque sus arenas volcánicas absorben el oxígeno de las nubes costeras.",
                "Porque detiene la corriente de Humboldt en el océano Pacífico."
            ],
            "correct": 1
        }
    ],
    "b2-brasilinterior-05": [
        {
            "id": "b2-brasilinterior-05-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["interior-construcciones-concesivas-subjuntivo"],
            "question": "¿Qué modo verbal exige la locución concesiva intensiva 'por más que' cuando expresa incertidumbre o firmeza ante una dificultad?",
            "options": [
                "Modo indicativo exclusivamente.",
                "Modo subjuntivo.",
                "Modo imperativo afirmativo.",
                "Forma no personal en gerundio simple."
            ],
            "correct": 1
        },
        {
            "id": "b2-brasilinterior-05-ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["interior-construcciones-concesivas-subjuntivo"],
            "sentence": "Por __ que presionen las potencias tradicionales, el bloque de los BRICS mantendrá su agenda de reformas.",
            "answer": "más",
            "english": "However much traditional powers exert pressure, the BRICS bloc will maintain its reform agenda."
        },
        {
            "id": "b2-brasilinterior-05-ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["brasil-interior-05-vocab"],
            "pairs": [
                ["cancillería", "foreign ministry"],
                ["multilateralismo", "multilateralism"],
                ["hegemonía", "hegemony"],
                ["consenso", "consensus"]
            ]
        },
        {
            "id": "b2-brasilinterior-05-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es la sede del Ministerio de Relaciones Exteriores de Brasil, famoso por su arquitectura y escuela diplomática?",
            "options": [
                "El Palacio de Carondelet",
                "El Palacio de Itamaraty",
                "El Palacio de San Martín",
                "La Casa de Nariño"
            ],
            "correct": 1
        }
    ],
    "b2-brasilinterior-consolidation": [
        {
            "id": "b2-brasilinterior-con-ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["interior-subordinadas-consecutivas-intensivas"],
            "question": "Identifica la oración con subordinada consecutiva intensiva:",
            "options": [
                "Trabajaron sin descanso para que la capital quedara inaugurada.",
                "El fervor constructor fue tan arrollador que la metrópoli se levantó en mil días.",
                "Antes de que llegara el presidente, los obreros terminaron la avenida.",
                "Aunque llovía torrencialmente, los topógrafos trazaron el eje."
            ],
            "correct": 1
        },
        {
            "id": "b2-brasilinterior-con-ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["interior-oraciones-temporales-avanzadas"],
            "question": "¿Qué valor aporta 'a medida que' en una narración histórica?",
            "options": [
                "Simultaneidad progresiva y gradual entre dos procesos en desarrollo.",
                "Causa retrospectiva negada.",
                "Condición hipotética irrealizable.",
                "Consecuencia imprevista e inmediata."
            ],
            "correct": 0
        },
        {
            "id": "b2-brasilinterior-con-ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["interior-conectores-contraargumentativos-formales"],
            "sentence": "El proyecto fue duramente criticado por los conservadores; __, la cancillería mantuvo inalterable su doctrina soberana.",
            "answer": "empero",
            "english": "The project was harshly criticized by conservatives; however, the foreign ministry kept its sovereign doctrine unaltered."
        },
        {
            "id": "b2-brasilinterior-con-ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué síntesis geopolítica define la proyección contemporánea del interior brasileño?",
            "options": [
                "La dependencia colonial respecto a las potencias del Atlántico norte.",
                "La afirmación de la soberanía territorial, la preservación ecológica y la multipolaridad global.",
                "El abandono de los compromisos multilaterales en favor de la autarquía.",
                "La militarización total de la cuenca amazónica sin control civil."
            ],
            "correct": 1
        }
    ]
}

GRAMMAR_SKILL_MAP = {
    "b2-31-01-a": "marcadores-consecutivos-formales",
    "b2-31-02-a": "marcadores-consecutivos-coloquiales",
    "b2-31-03-a": "marcadores-causales-complejos",
    "b2-31-04-a": "marcadores-ilativos-deductivos",
    "b2-31-05-a": "marcadores-causa-efecto-subjetiva",
    "b2-brasilinterior-01-a": "interior-subordinadas-consecutivas-intensivas",
    "b2-brasilinterior-02-a": "interior-oraciones-temporales-avanzadas",
    "b2-brasilinterior-03-a": "interior-perifrasis-obligacion-atenuada",
    "b2-brasilinterior-04-a": "interior-conectores-contraargumentativos-formales",
    "b2-brasilinterior-05-a": "interior-construcciones-concesivas-subjuntivo",
}

def get_vocab_id(stem: str) -> str:
    parts = stem.split("-")
    return f"vocab.b2.{parts[1]}.{parts[2]}"

def get_grammar_id(stem: str) -> str:
    skill = GRAMMAR_SKILL_MAP[stem]
    parts = stem.split("-")
    return f"grammar.b2.{parts[1]}.{parts[2]}.{skill}"

def generate_vocab_files():
    for stem, data in VOCAB_DATA.items():
        doc = {
            "id": get_vocab_id(stem),
            "lesson": stem,
            "title": data["title"],
            "words": data["words"]
        }
        path = LATAM_DIR / "vocabulary" / "b2" / f"{stem}-voc.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {path.relative_to(REPO_ROOT)}")

def generate_grammar_files():
    for stem, data in GRAMMAR_DATA.items():
        doc = {
            "id": get_grammar_id(stem),
            "title": data["title"],
            "sections": data["sections"]
        }
        path = LATAM_DIR / "grammar" / "b2" / f"{stem}-gr.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {path.relative_to(REPO_ROOT)}")

def generate_stories():
    counts = {}
    for path_rel, data in STORIES_DATA.items():
        total_text = " ".join(p["text"] for p in data["paragraphs"] if p.get("type") == "narration")
        wc = word_count(total_text)
        counts[path_rel] = wc
        print(f"stories/{path_rel}.json: {wc} words")
    
    out_of_range = {k: v for k, v in counts.items() if not (650 <= v <= 825)}
    if out_of_range:
        raise ValueError(f"Stories out of range [650, 825]: {out_of_range}")

    for path_rel, data in STORIES_DATA.items():
        path = LATAM_DIR / "stories" / f"{path_rel}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Wrote {path.relative_to(REPO_ROOT)}")

def generate_exercises():
    for stem, ex_list in EXERCISES_DATA.items():
        # Ensure ID format uses dots (stem.ex01, etc.)
        for i, ex in enumerate(ex_list, 1):
            ex["id"] = f"{stem}.ex0{i}"
        doc = {
            "lesson": stem,
            "exercises": ex_list
        }
        path = LATAM_DIR / "exercises" / "b2" / f"{stem}-ex.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {path.relative_to(REPO_ROOT)}")

def generate_lessons():
    # Core Unit 31 lessons
    core_lessons = [
        ("b2-31-01", "Marcadores consecutivos formales", "1"),
        ("b2-31-02", "Marcadores consecutivos coloquiales e ilativos", "2"),
        ("b2-31-03", "Marcadores causales complejos", "3"),
        ("b2-31-04", "Marcadores ilativos y deductivos", "4"),
        ("b2-31-05", "Causa-efecto subjetiva: justificación y énfasis", "5"),
    ]
    for stem, title, num in core_lessons:
        doc = {
            "id": f"lesson.b2.31.0{num}",
            "title": title,
            "level": "B2",
            "sections": [
                {
                    "type": "story",
                    "ref": "stories/classics/b2/b2-31.json"
                },
                {
                    "type": "grammar",
                    "ref": f"grammar/b2/{stem}-a-gr.json"
                },
                {
                    "type": "vocabulary",
                    "ref": f"vocabulary/b2/{stem}-voc.json"
                },
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b2/{stem}-ex.json",
                    "exerciseRefs": [f"{stem}.ex0{i}" for i in range(1, 5)]
                }
            ]
        }
        path = LATAM_DIR / "lessons" / "b2" / f"{stem}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {path.relative_to(REPO_ROOT)}")

    # Core consolidation
    con_stem = "b2-31-consolidation"
    doc_con = {
        "id": "lesson.b2.31.consolidation",
        "title": "Consolidation: Discourse Markers IV: Consequence & Causality",
        "level": "B2",
        "sections": [
            {
                "type": "story",
                "ref": "stories/classics/b2/b2-31.json"
            },
            {
                "type": "exercise-group",
                "title": "Review",
                "ref": f"exercises/b2/{con_stem}-ex.json",
                "exerciseRefs": [f"{con_stem}.ex0{i}" for i in range(1, 5)]
            }
        ]
    }
    path_con = LATAM_DIR / "lessons" / "b2" / f"{con_stem}.json"
    with open(path_con, "w", encoding="utf-8") as f:
        json.dump(doc_con, f, ensure_ascii=False, indent=2)
    print(f"Wrote {path_con.relative_to(REPO_ROOT)}")

    # Regional Brasil Interior lessons
    reg_lessons = [
        ("b2-brasilinterior-01", "Brasilia: La utopía geométrica del Plan Piloto", "1"),
        ("b2-brasilinterior-02", "La cuenca amazónica: Manaus, Belém y la arteria fluvial continental", "2"),
        ("b2-brasilinterior-03", "Soberanía indígena y la custodia de los pueblos aislados", "3"),
        ("b2-brasilinterior-04", "El Cerrado y el agronegocio: La encrucijada agroecológica", "4"),
        ("b2-brasilinterior-05", "Brasil en el tablero global: BRICS, Itamaraty y la multipolaridad", "5")
    ]
    for stem, title, num in reg_lessons:
        doc = {
            "id": f"lesson.b2.brasilinterior.0{num}",
            "title": title,
            "level": "B2",
            "sections": [
                {
                    "type": "story",
                    "ref": f"stories/world/b2/{stem}.json"
                },
                {
                    "type": "grammar",
                    "ref": f"grammar/b2/{stem}-a-gr.json"
                },
                {
                    "type": "vocabulary",
                    "ref": f"vocabulary/b2/{stem}-voc.json"
                },
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b2/{stem}-ex.json",
                    "exerciseRefs": [f"{stem}.ex0{i}" for i in range(1, 5)]
                }
            ]
        }
        path = LATAM_DIR / "lessons" / "b2" / f"{stem}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"Wrote {path.relative_to(REPO_ROOT)}")

    # Regional consolidation
    reg_con_stem = "b2-brasilinterior-consolidation"
    doc_reg_con = {
        "id": "lesson.b2.brasilinterior.consolidation",
        "title": "Consolidación: El corazón continental de Brasil y los horizontes del interior",
        "level": "B2",
        "sections": [
            {
                "type": "story",
                "ref": f"stories/world/b2/{reg_con_stem}.json"
            },
            {
                "type": "exercise-group",
                "title": "Review",
                "ref": f"exercises/b2/{reg_con_stem}-ex.json",
                "exerciseRefs": [f"{reg_con_stem}.ex0{i}" for i in range(1, 5)]
            }
        ]
    }
    path_reg_con = LATAM_DIR / "lessons" / "b2" / f"{reg_con_stem}.json"
    with open(path_reg_con, "w", encoding="utf-8") as f:
        json.dump(doc_reg_con, f, ensure_ascii=False, indent=2)
    print(f"Wrote {path_reg_con.relative_to(REPO_ROOT)}")

def update_curriculum_units():
    path = LATAM_DIR / "curriculum" / "units" / "b2.json"
    with open(path, "r", encoding="utf-8") as f:
        units_list = json.load(f)
    
    existing_stems = set()
    for u in units_list:
        existing_stems.update(u.get("stems", []))
    
    core_stems = [f"b2-31-0{i}" for i in range(1, 6)] + ["b2-31-consolidation"]
    reg_stems = [f"b2-brasilinterior-0{i}" for i in range(1, 6)] + ["b2-brasilinterior-consolidation"]

    if "b2-31-01" not in existing_stems:
        units_list.append({
            "title": "Discourse Markers IV: Consequence & Causality",
            "stems": core_stems,
            "track": "core"
        })
    if "b2-brasilinterior-01" not in existing_stems:
        units_list.append({
            "title": "Brazil III: Amazonia, Brasília & The Geopolitics of the Interior",
            "stems": reg_stems,
            "track": "regional"
        })

    with open(path, "w", encoding="utf-8") as f:
        json.dump(units_list, f, ensure_ascii=False, indent=2)
    print("Updated curriculum/units/b2.json with Unit 31!")

def main():
    update_skill_registry()
    update_grammar_titles()
    generate_vocab_files()
    generate_grammar_files()
    generate_stories()
    generate_exercises()
    generate_lessons()
    update_curriculum_units()
    print("Unit 31 generation complete!")

if __name__ == "__main__":
    main()
