#!/usr/bin/env python3
"""
generate_es_latam_b2_unit32.py

Generates Latin American Spanish B2 Unit 32 for both tracks:
- Track 1 (Core B2): Unit 32 - Subordinación adverbial I: Concesivas avanzadas y modales
  Classic: Rómulo Gallegos - Canaima (1935)
- Track 2 (Regional Studies): Unit 32 - Amazonía Pancontinental: La cuenca compartida y el bioma sin fronteras
  Overview + 5 lessons + consolidation story

Strict schema conformance:
- Vocabulary: root {id: 'vocab.b2.32.01', lesson: 'b2-32-01', title, words: [{lemma, translation, pos}]}
- Exercises: root {lesson: 'b2-32-01', exercises: [{id: 'b2-32-01.ex01', type, category, teaches, ...}]}
- Grammar: root {id: 'grammar.b2.32.01.<skill>', title, sections: [{type: 'text'|'table'|'tip', content, rows}]}
- Lessons: root {id: 'lesson.b2.32.01', title, level: 'B2', sections: [...]}
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
    # Core 32 grammar skills
    "concesivas-intensivas-cuantificadas": {
        "name": "intensive quantified concessive clauses with subjunctive",
        "kind": "grammar",
        "category": "grammar"
    },
    "concesivas-riesgo-contingencia": {
        "name": "concessive clauses expressing risk contingency and outcome",
        "kind": "grammar",
        "category": "grammar"
    },
    "concesivas-redundantes-duplicadas": {
        "name": "reduplicative concessive clauses expressing unconditional actions",
        "kind": "grammar",
        "category": "grammar"
    },
    "modales-correlativas-avanzadas": {
        "name": "advanced manner clauses of conformity and correspondence",
        "kind": "grammar",
        "category": "grammar"
    },
    "modales-hipoteticas-comparativas": {
        "name": "hypothetical comparative manner clauses with subjunctive",
        "kind": "grammar",
        "category": "grammar"
    },
    # Regional 32 grammar skills
    "amazonia-oraciones-finales-institucionales": {
        "name": "institutional purpose clauses in international diplomacy agreements",
        "kind": "grammar",
        "category": "grammar"
    },
    "amazonia-relativas-locativas-complejas": {
        "name": "complex locative relative clauses with subjunctive mood",
        "kind": "grammar",
        "category": "grammar"
    },
    "amazonia-causales-explicativas-continuativas": {
        "name": "formal continuative causal clauses in scientific reports",
        "kind": "grammar",
        "category": "grammar"
    },
    "amazonia-perifrasis-probabilidad-retrospectiva": {
        "name": "retrospective probability periphrases in historical investigations",
        "kind": "grammar",
        "category": "grammar"
    },
    "amazonia-condicionales-mixtas-complejas": {
        "name": "mixed complex conditional sentences across temporal frames",
        "kind": "grammar",
        "category": "grammar"
    },
    # Vocabulary unit themes
    "b2-32-01-vocab": {
        "name": "tenacity and adversity vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-32-02-vocab": {
        "name": "risk and uncertainty vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-32-03-vocab": {
        "name": "unwavering determination vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-32-04-vocab": {
        "name": "regulatory conformity vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "b2-32-05-vocab": {
        "name": "hypothetical similes and appearances vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "amazonia-pan-01-vocab": {
        "name": "panamazonian diplomacy and treaty vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "amazonia-pan-02-vocab": {
        "name": "porous borders and transboundary peoples vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "amazonia-pan-03-vocab": {
        "name": "flying rivers and continental hydrology vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "amazonia-pan-04-vocab": {
        "name": "environmental enforcement and mercury pollution vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    },
    "amazonia-pan-05-vocab": {
        "name": "bioeconomy and standing forest medicine vocabulary",
        "kind": "vocabulary",
        "category": "vocabulary"
    }
}

NEW_GRAMMAR_TITLES = {
    "concesivas-intensivas-cuantificadas": "intensive quantified concessive clauses with subjunctive",
    "concesivas-riesgo-contingencia": "concessive clauses expressing risk contingency and outcome",
    "concesivas-redundantes-duplicadas": "reduplicative concessive clauses expressing unconditional actions",
    "modales-correlativas-avanzadas": "advanced manner clauses of conformity and correspondence",
    "modales-hipoteticas-comparativas": "hypothetical comparative manner clauses with subjunctive",
    "amazonia-oraciones-finales-institucionales": "institutional purpose clauses in international diplomacy agreements",
    "amazonia-relativas-locativas-complejas": "complex locative relative clauses with subjunctive mood",
    "amazonia-causales-explicativas-continuativas": "formal continuative causal clauses in scientific reports",
    "amazonia-perifrasis-probabilidad-retrospectiva": "retrospective probability periphrases in historical investigations",
    "amazonia-condicionales-mixtas-complejas": "mixed complex conditional sentences across temporal frames"
}

def update_skill_registry():
    path = LATAM_DIR / "indexes" / "skill-registry.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_SKILLS.items():
        data["skills"][k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated skill-registry.json for Unit 32")

def update_grammar_titles():
    path = LATAM_DIR / "indexes" / "grammar-titles.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in NEW_GRAMMAR_TITLES.items():
        data[k] = v
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated grammar-titles.json for Unit 32")

VOCAB_DATA = {
    "b2-32-01": {
        "title": "Tenacidad y resistencia ante la adversidad",
        "words": [
            {"lemma": "por más que", "translation": "no matter how much (+ subj.)", "pos": "conjunction"},
            {"lemma": "por mucho que", "translation": "however much (+ subj.)", "pos": "conjunction"},
            {"lemma": "tenacidad", "translation": "tenacity / perseverance", "pos": "noun"},
            {"lemma": "indómito", "translation": "untamed / indomitable", "pos": "adjective"},
            {"lemma": "adversidad", "translation": "adversity", "pos": "noun"},
            {"lemma": "empeño", "translation": "determination / endeavor", "pos": "noun"},
            {"lemma": "claudicar", "translation": "to give in / to yield", "pos": "verb"},
            {"lemma": "inquebrantable", "translation": "unshakeable", "pos": "adjective"},
            {"lemma": "sobreponerse", "translation": "to overcome / to prevail", "pos": "verb"},
            {"lemma": "arduo", "translation": "arduous", "pos": "adjective"}
        ]
    },
    "b2-32-02": {
        "title": "Riesgo, audacia e incertidumbre",
        "words": [
            {"lemma": "aun a riesgo de que", "translation": "even at the risk of (+ subj.)", "pos": "conjunction"},
            {"lemma": "con todo y que", "translation": "even with the fact that", "pos": "conjunction"},
            {"lemma": "contingencia", "translation": "contingency", "pos": "noun"},
            {"lemma": "temeridad", "translation": "recklessness / daring", "pos": "noun"},
            {"lemma": "azaroso", "translation": "eventful / hazardous", "pos": "adjective"},
            {"lemma": "arrojo", "translation": "boldness / courage", "pos": "noun"},
            {"lemma": "arriesgar", "translation": "to risk / to venture", "pos": "verb"},
            {"lemma": "incertidumbre", "translation": "uncertainty", "pos": "noun"},
            {"lemma": "desafío", "translation": "challenge / defiance", "pos": "noun"},
            {"lemma": "intrépido", "translation": "intrepid / fearless", "pos": "adjective"}
        ]
    },
    "b2-32-03": {
        "title": "Determinación y reduplicación concesiva",
        "words": [
            {"lemma": "cueste lo que cueste", "translation": "whatever it takes / cost what it may", "pos": "expression"},
            {"lemma": "pase lo que pase", "translation": "come what may / whatever happens", "pos": "expression"},
            {"lemma": "haga lo que haga", "translation": "whatever he/she does", "pos": "expression"},
            {"lemma": "resolución", "translation": "resolve / resolution", "pos": "noun"},
            {"lemma": "firmeza", "translation": "firmness / steadfastness", "pos": "noun"},
            {"lemma": "compromiso", "translation": "commitment", "pos": "noun"},
            {"lemma": "invariable", "translation": "invariable / steady", "pos": "adjective"},
            {"lemma": "perseguir", "translation": "to pursue / to seek", "pos": "verb"},
            {"lemma": "meta", "translation": "goal / target", "pos": "noun"},
            {"lemma": "incondicional", "translation": "unconditional", "pos": "adjective"}
        ]
    },
    "b2-32-04": {
        "title": "Normativa, conformidad y preceptos modales",
        "words": [
            {"lemma": "según y conforme", "translation": "according as / depending on", "pos": "conjunction"},
            {"lemma": "a tenor de", "translation": "in accordance with / to the effect that", "pos": "preposition"},
            {"lemma": "con arreglo a", "translation": "in accordance with / pursuant to", "pos": "preposition"},
            {"lemma": "conformidad", "translation": "conformity / agreement", "pos": "noun"},
            {"lemma": "estatuto", "translation": "statute / bylaw", "pos": "noun"},
            {"lemma": "normativo", "translation": "regulatory / normative", "pos": "adjective"},
            {"lemma": "estipular", "translation": "to stipulate", "pos": "verb"},
            {"lemma": "prescripción", "translation": "prescription / legal rule", "pos": "noun"},
            {"lemma": "dictamen", "translation": "opinion / ruling", "pos": "noun"},
            {"lemma": "alinear", "translation": "to align", "pos": "verb"}
        ]
    },
    "b2-32-05": {
        "title": "Símiles, apariencias e hipótesis modales",
        "words": [
            {"lemma": "como si", "translation": "as if (+ subj.)", "pos": "conjunction"},
            {"lemma": "cual si", "translation": "as though / just as if (+ subj.)", "pos": "conjunction"},
            {"lemma": "similitud", "translation": "similarity / likeness", "pos": "noun"},
            {"lemma": "apariencia", "translation": "appearance / semblance", "pos": "noun"},
            {"lemma": "fingir", "translation": "to feign / to pretend", "pos": "verb"},
            {"lemma": "ilusorio", "translation": "illusory", "pos": "adjective"},
            {"lemma": "semejanza", "translation": "resemblance", "pos": "noun"},
            {"lemma": "espejismo", "translation": "mirage / illusion", "pos": "noun"},
            {"lemma": "aparente", "translation": "apparent / seeming", "pos": "adjective"},
            {"lemma": "evocar", "translation": "to evoke", "pos": "verb"}
        ]
    },
    "b2-amazoniapan-01": {
        "title": "Gobernanza panamazónica y tratados",
        "words": [
            {"lemma": "en aras de", "translation": "for the sake of / in order to (+ inf./que)", "pos": "preposition"},
            {"lemma": "a efectos de que", "translation": "with the aim that (+ subj.)", "pos": "conjunction"},
            {"lemma": "tratado", "translation": "treaty", "pos": "noun"},
            {"lemma": "multilateral", "translation": "multilateral", "pos": "adjective"},
            {"lemma": "soberanía", "translation": "sovereignty", "pos": "noun"},
            {"lemma": "cooperación", "translation": "cooperation", "pos": "noun"},
            {"lemma": "declaración", "translation": "declaration", "pos": "noun"},
            {"lemma": "ratificar", "translation": "to ratify", "pos": "verb"},
            {"lemma": "convergencia", "translation": "convergence", "pos": "noun"},
            {"lemma": "vincular", "translation": "to bind / to link", "pos": "verb"}
        ]
    },
    "b2-amazoniapan-02": {
        "title": "Fronteras porosas y pueblos transfronterizos",
        "words": [
            {"lemma": "allí donde", "translation": "where / wherever", "pos": "conjunction"},
            {"lemma": "adondequiera que", "translation": "wherever (+ subj.)", "pos": "conjunction"},
            {"lemma": "poroso", "translation": "porous / permeable", "pos": "adjective"},
            {"lemma": "transfronterizo", "translation": "cross-border / transboundary", "pos": "adjective"},
            {"lemma": "fluvial", "translation": "riverine / fluvial", "pos": "adjective"},
            {"lemma": "itinerancia", "translation": "itinerancy / roaming", "pos": "noun"},
            {"lemma": "territorialidad", "translation": "territoriality", "pos": "noun"},
            {"lemma": "confluir", "translation": "to converge / to meet", "pos": "verb"},
            {"lemma": "vecindad", "translation": "neighborhood / proximity", "pos": "noun"},
            {"lemma": "hito", "translation": "boundary stone / milestone", "pos": "noun"}
        ]
    },
    "b2-amazoniapan-03": {
        "title": "Ríos voladores e hidrología continental",
        "words": [
            {"lemma": "habida cuenta de que", "translation": "taking into account that", "pos": "conjunction"},
            {"lemma": "por cuanto", "translation": "inasmuch as / whereas", "pos": "conjunction"},
            {"lemma": "evapotranspiración", "translation": "evapotranspiration", "pos": "noun"},
            {"lemma": "humedad", "translation": "moisture / humidity", "pos": "noun"},
            {"lemma": "precipitación", "translation": "rainfall / precipitation", "pos": "noun"},
            {"lemma": "caudal", "translation": "river flow / discharge", "pos": "noun"},
            {"lemma": "estacionalidad", "translation": "seasonality", "pos": "noun"},
            {"lemma": "amortiguar", "translation": "to buffer / to cushion", "pos": "verb"},
            {"lemma": "régimen", "translation": "regime / pattern", "pos": "noun"},
            {"lemma": "bioma", "translation": "biome", "pos": "noun"}
        ]
    },
    "b2-amazoniapan-04": {
        "title": "Fiscalización ambiental y contaminación minera",
        "words": [
            {"lemma": "deber de haber", "translation": "must have (+ past participle)", "pos": "verb"},
            {"lemma": "venir a", "translation": "to come to / to amount to (+ inf.)", "pos": "verb"},
            {"lemma": "mercurio", "translation": "mercury", "pos": "noun"},
            {"lemma": "toxicidad", "translation": "toxicity", "pos": "noun"},
            {"lemma": "dragado", "translation": "dredging", "pos": "noun"},
            {"lemma": "decomiso", "translation": "seizure / confiscation", "pos": "noun"},
            {"lemma": "fiscalizar", "translation": "to inspect / to monitor", "pos": "verb"},
            {"lemma": "impunidad", "translation": "impunity", "pos": "noun"},
            {"lemma": "contaminar", "translation": "to pollute / to contaminate", "pos": "verb"},
            {"lemma": "clandestino", "translation": "clandestine / illegal", "pos": "adjective"}
        ]
    },
    "b2-amazoniapan-05": {
        "title": "Bioeconomía y farmacopea del bosque en pie",
        "words": [
            {"lemma": "de haber sabido", "translation": "had one known", "pos": "expression"},
            {"lemma": "farmacopea", "translation": "pharmacopeia", "pos": "noun"},
            {"lemma": "regenerativo", "translation": "regenerative", "pos": "adjective"},
            {"lemma": "recolección", "translation": "harvesting / gathering", "pos": "noun"},
            {"lemma": "biomolécula", "translation": "biomolecule", "pos": "noun"},
            {"lemma": "patente", "translation": "patent", "pos": "noun"},
            {"lemma": "biopiratería", "translation": "biopiracy", "pos": "noun"},
            {"lemma": "aprovechamiento", "translation": "sustainable use / exploitation", "pos": "noun"},
            {"lemma": "ancestral", "translation": "ancestral", "pos": "adjective"},
            {"lemma": "endémico", "translation": "endemic", "pos": "adjective"}
        ]
    }
}

GRAMMAR_DATA = {
    "b2-32-01-a": {
        "title": "Concesivas intensivas cuantificadas",
        "sections": [
            {
                "type": "text",
                "content": "Las oraciones concesivas intensivas cuantificadas formadas por 'por más que + verbo' y 'por mucho que + verbo' (o la variante adjetival 'por muy + adjetivo + que + subjuntivo') expresan que, por grande o extrema que sea la magnitud de la acción o cualidad descrita en la prótasis, esta resulta incapaz de impedir o desvirtuar lo afirmado en la cláusula principal. Cuando la acción se proyecta hacia el futuro, expresa hipótesis o alude a hechos no verificados por el hablante, rige invariablemente el modo subjuntivo."
            },
            {
                "type": "table",
                "title": "Estructuras concesivas intensivas cuantificadas",
                "rows": [
                    ["Por más que insistan los intermediarios, no venderé la concesión forestal.", "No matter how much the brokers insist, I will not sell the timber concession."],
                    ["Por mucho que cueste la expedición, llegaremos a las fuentes del Orinoco.", "However much the expedition costs, we will reach the sources of the Orinoco."],
                    ["Por muy caudaloso que sea el raudal, los balseros cruzarán el desfiladero.", "However high-flowing the rapid may be, the rafters will cross the gorge."],
                    ["Por más que intentó ocultar su fatiga, el explorador cayó exhausto en la ribera.", "No matter how much he tried to hide his fatigue, the explorer collapsed exhausted on the bank."]
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que si el hecho es un dato fáctico constatado del pasado que el hablante no cuestiona, puede aparecer con indicativo ('por más que llovió, logramos terminar'). Sin embargo, en el estilo argumentativo B2 formal predomina el subjuntivo para ponderar la dificultad como irrelevante."
            }
        ]
    },
    "b2-32-02-a": {
        "title": "Concesivas de riesgo y contingencia",
        "sections": [
            {
                "type": "text",
                "content": "Para expresar que una decisión se asume con plena conciencia del peligro o de consecuencias desfavorables inminentes, el español formal recurre a locuciones concesivas complejas como 'aun a riesgo de que + subjuntivo' y 'con todo y que'. Mientras que 'aun a riesgo de que' enfatiza la contingencia peligrosa y exige subjuntivo, 'con todo y que' admite indicativo cuando enuncia un obstáculo fáctico real que no logra frenar la acción."
            },
            {
                "type": "table",
                "title": "Conectores concesivos de riesgo y contingencia",
                "rows": [
                    ["Continuaron navegando el caño, aun a riesgo de que la corriente destrozara la canoa.", "They continued navigating the creek, even at the risk of the current wrecking the canoe."],
                    ["El fiscal denunció la tala clandestina, aun a riesgo de que sufriera represalias armadas.", "The prosecutor denounced illegal logging, even at the risk of suffering armed retaliation."],
                    ["Con todo y que los caminos estaban anegados, el convoy de auxilio llegó a la aldea.", "Even with the fact that the roads were waterlogged, the relief convoy reached the village."],
                    ["Con todo y que no tenían mapas satelitales, los baquianos guiaron la marcha con éxito.", "Even though they lacked satellite maps, the bush guides led the march successfully."]
                ]
            },
            {
                "type": "tip",
                "content": "'Aun a riesgo de que' rige obligatoriamente subjuntivo porque la consecuencia temida se concibe como una eventualidad posible o contingente, no como un hecho ya consumado."
            }
        ]
    },
    "b2-32-03-a": {
        "title": "Concesivas reduplicativas y de indiferencia",
        "sections": [
            {
                "type": "text",
                "content": "Las cláusulas concesivas reduplicadas son construcciones idiomáticas de gran vigor enfático que expresan la determinación absoluta del sujeto ante cualquier circunstancia imaginable. Se estructuran mediante la repetición de un mismo verbo en subjuntivo unido por un pronombre o relativo indefinido: 'haga lo que haga', 'cueste lo que cueste', 'pase lo que pase', 'venga quien venga', o mediante la alternancia disyuntiva 'quiera o no quiera'."
            },
            {
                "type": "table",
                "title": "Estructuras reduplicativas de indiferencia y determinación",
                "rows": [
                    ["Cueste lo que cueste, preservaremos la reserva biológica intacta para el porvenir.", "Whatever it takes, we will preserve the biological reserve intact for the future."],
                    ["Pase lo que pase durante la asamblea, los delegados indígenas mantendrán su postura común.", "Come what may during the assembly, the indigenous delegates will keep their joint stance."],
                    ["Diga lo que diga la prensa sensacionalista, el tratado limítrofe es plenamente legítimo.", "Whatever the sensationalist press says, the boundary treaty is fully legitimate."],
                    ["Quiera o no quiera la empresa minera, la consulta previa vinculante habrá de celebrarse.", "Whether the mining company wants to or not, binding prior consultation will have to take place."]
                ]
            },
            {
                "type": "tip",
                "content": "En estas fórmulas el primer verbo puede ir en subjuntivo presente o imperfecto dependiendo del anclaje temporal ('costara lo que costara, estaban decididos a salvar el bosque')."
            }
        ]
    },
    "b2-32-04-a": {
        "title": "Subordinadas modales correlativas avanzadas",
        "sections": [
            {
                "type": "text",
                "content": "En el registro formal, diplomático y legal, la manera o el modo en que se ejecuta una acción se subordina mediante nexos conjuntivos complejos como 'según y conforme', 'a tenor de' y 'con arreglo a'. Estas locuciones vinculan la acción rectora con directrices, pautas o preceptos normativos preestablecidos, rigiéndose en indicativo cuando constatan pautas reales o en subjuntivo cuando la pauta es contingente o futura."
            },
            {
                "type": "table",
                "title": "Nexos modales de conformidad y correspondencia",
                "rows": [
                    ["Procederemos a demarcar la frontera según y conforme lo estipulan los protocolos de paz.", "We will proceed to demarcate the border according as the peace protocols stipulate."],
                    ["A tenor de lo establecido en el tratado de la OTCA, los ocho países vigilarán la deforestación.", "In accordance with what is established in the ACTO treaty, the eight countries will monitor deforestation."],
                    ["Actuaron con arreglo a las directrices de la fiscalía especializada en delitos ambientales.", "They acted pursuant to the guidelines of the special prosecution office for environmental crimes."],
                    ["Se resolverá la controversia según y conforme dictaminen los jueces del tribunal arbitral.", "The dispute will be resolved according as the judges of the arbitral tribunal rule."]
                ]
            },
            {
                "type": "tip",
                "content": "'A tenor de' es una locución prepositiva culta sumamente valorada en textos jurídicos y análisis de políticas públicas para citar cláusulas y mandatos normativos."
            }
        ]
    },
    "b2-32-05-a": {
        "title": "Subordinadas modales hipotéticas con subjuntivo",
        "sections": [
            {
                "type": "text",
                "content": "Las oraciones modales hipotéticas introducidas por 'como si' y su variante lírica o arcaizante 'cual si' comparan una acción real con una circunstancia imaginaria, simulada o contrafáctica. Por su naturaleza intrínsecamente irreal o fingida, estas locuciones exigen de forma rigurosa los tiempos del subjuntivo del eje del pasado: pretérito imperfecto (para simultaneidad con la acción principal) o pluscuamperfecto (para anterioridad)."
            },
            {
                "type": "table",
                "title": "Estructuras modales hipotéticas con como si y cual si",
                "rows": [
                    ["Hablaba de la selva como si la conociera desde antes de nacer.", "He spoke of the jungle as if he had known it before being born."],
                    ["El cauce rugía en la noche cual si fuera un monstruo mitológico al acecho.", "The river roared in the night as though it were an ambushing mythological monster."],
                    ["Gastaba los caudales del caucho como si las riquezas nunca fueran a terminarse.", "He squandered the rubber revenues as if the wealth were never going to end."],
                    ["Los taladores huyeron del campamento cual si hubieran visto una aparición espectral.", "The loggers fled the camp as though they had seen a spectral apparition."]
                ]
            },
            {
                "type": "tip",
                "content": "Nunca uses presente de subjuntivo tras 'como si': decir *como si tenga* o *como si sea* es un error normativo grave. Debe ser siempre 'como si tuviera' o 'como si fuera'."
            }
        ]
    },
    "b2-amazoniapan-01-a": {
        "title": "Oraciones finales en diplomacia ambiental",
        "sections": [
            {
                "type": "text",
                "content": "En la redacción de acuerdos multilaterales y cumbres internacionales, la finalidad institucional se formula mediante locuciones de registro solemne como 'en aras de que + subjuntivo', 'a efectos de que + subjuntivo' y 'con miras a que + subjuntivo'. Estas construcciones elevan el tono discursivo por encima del común 'para que', proyectando el propósito soberano de las partes firmantes."
            },
            {
                "type": "table",
                "title": "Locuciones finales institucionales",
                "rows": [
                    ["Los presidentes suscribieron la Declaración de Belém en aras de que se detenga el punto de no retorno.", "The presidents signed the Belém Declaration in order that the tipping point be halted."],
                    ["Se crea una comisión binacional a efectos de que los guardaparques coordinen patrullajes conjuntos.", "A binational commission is created with the aim that park rangers coordinate joint patrols."],
                    ["Compartirán datos satelitales con miras a que la fiscalización forestal resulte implacable.", "They will share satellite data with the aim that forest monitoring proves relentless."],
                    ["Modificaron el reglamento en aras de que las comunidades nativas tengan voto vinculante.", "They amended the regulation in order that native communities hold a binding vote."]
                ]
            },
            {
                "type": "tip",
                "content": "Tanto 'en aras de' como 'a efectos de' admiten infinitivo cuando el sujeto de la cláusula principal y subordinada coincide ('actuaron en aras de preservar la paz'). Cuando introducen un sujeto diferente con 'que', exigen subjuntivo."
            }
        ]
    },
    "b2-amazoniapan-02-a": {
        "title": "Relativas locativas complejas",
        "sections": [
            {
                "type": "text",
                "content": "Para describir territorios porosos y la movilidad de comunidades nómadas o transfronterizas en la Amazonía, el español avanzado utiliza relativas locativas como 'allí donde', 'adondequiera que + subjuntivo' y 'por doquier que'. Estas estructuras expresan indeterminación espacial y universalidad territorial sin sujeción a fronteras cartográficas convencionales."
            },
            {
                "type": "table",
                "title": "Cláusulas relativas locativas de espacio indefinido",
                "rows": [
                    ["Los pueblos indígenas cruzan los ríos allí donde las corrientes forman vados seguros.", "Indigenous peoples cross the rivers wherever the currents form safe shallows."],
                    ["Adondequiera que viajen los cazadores nómadas, reconocen los árboles sagrados de su linaje.", "Wherever the nomadic hunters travel, they recognize the sacred trees of their lineage."],
                    ["Allí donde confluían las tres fronteras, los comerciantes intercambiaban víveres y canoas.", "Where the three borders converged, merchants traded provisions and canoes."],
                    ["Adondequiera que penetren los científicos del herbario, descubren especies vegetales inéditas.", "Wherever the herbarium scientists penetrate, they discover unprecedented plant species."]
                ]
            },
            {
                "type": "tip",
                "content": "'Adondequiera' se escribe en una sola palabra cuando es adverbio relativo indefinido seguido de 'que' y subjuntivo. No debe confundirse con 'a donde quiera' (preposición + adverbio interrogativo + verbo querer)."
            }
        ]
    },
    "b2-amazoniapan-03-a": {
        "title": "Causales explicativas continuativas",
        "sections": [
            {
                "type": "text",
                "content": "En la exposición científica sobre macrobiomas y ciclos meteorológicos, la causa no se presenta como una simple justificación cotidiana, sino como un argumento fundado mediante conectores explicativos formales como 'habida cuenta de que' y 'por cuanto'. Estos marcadores introducen una causa demostrada y suficiente que legitima deducciones científicas de gran escala."
            },
            {
                "type": "table",
                "title": "Conectores causales explicativos en informes científicos",
                "rows": [
                    ["Las lluvias en el sur dependen del bioma, habida cuenta de que los árboles evaporan miles de millones de toneladas de agua.", "Rains in the south depend on the biome, taking into account that trees evaporate billions of tons of water."],
                    ["Se debe proteger la cabecera andina, por cuanto allí se originan los sedimentos vitales de la llanura.", "The Andean headwaters must be protected, inasmuch as the vital sediments of the plain originate there."],
                    ["El calentamiento se acelerará, habida cuenta de que la selva degradada pierde su capacidad de sumidero.", "Warming will accelerate, taking into account that the degraded forest loses its sink capacity."],
                    ["El proyecto fue respaldado unánimemente, por cuanto reunía las máximas garantías de sostenibilidad.", "The project was unanimously supported, inasmuch as it met the highest sustainability guarantees."]
                ]
            },
            {
                "type": "tip",
                "content": "'Por cuanto' es una locución causal culta propia de dictámenes técnicos y tratados doctrinales. Equivale a 'dado que' o 'puesto que', pero con un valor fundamentador más solemne."
            }
        ]
    },
    "b2-amazoniapan-04-a": {
        "title": "Perífrasis de probabilidad y conjetura retrospectiva",
        "sections": [
            {
                "type": "text",
                "content": "Al analizar indicios de actividades delictivas encubiertas o impactos ecológicos del pasado reciente, es preceptivo matizar las afirmaciones mediante perífrasis de conjetura y probabilidad compuesta como 'deber de haber + participio' y la perífrasis aproximativa 'venir a + infinitivo'. Estas fórmulas permiten al redactor emitir juicios fundados sin incurrir en temeridad fáctica."
            },
            {
                "type": "table",
                "title": "Perífrasis de hipótesis y aproximación analítica",
                "rows": [
                    ["Los dragados ilegales deben de haber operado durante meses sin ser detectados por los radares.", "The illegal dredging operations must have operated for months without being detected by radar."],
                    ["La concentración de mercurio en el cauce viene a superar en diez veces el límite tolerable.", "The mercury concentration in the riverbed comes to exceed the tolerable limit tenfold."],
                    ["Las balsas mineras debieron de haber zarpado antes de que amaneciera sobre el río Caquetá.", "The mining rafts must have set sail before dawn broke over the Caquetá River."],
                    ["El costo de restaurar las riberas degradadas viene a representar una suma astronómica.", "The cost of restoring the degraded banks comes to represent an astronomical sum."]
                ]
            },
            {
                "type": "tip",
                "content": "Recuerda que la norma culta prescribe 'deber de + infinitivo' para expresar conjetura o suposición ('debe de haber llovido anoche'), reservando 'deber + infinitivo' sin preposición para la obligación moral o legal."
            }
        ]
    },
    "b2-amazoniapan-05-a": {
        "title": "Condicionales mixtas complejas",
        "sections": [
            {
                "type": "text",
                "content": "Las oraciones condicionales mixtas complejas combinan marcos temporales disímiles entre la prótasis y la apódosis: habitualmente una condición irreal en el pasado (prótasis con pluscuamperfecto de subjuntivo: 'si hubiéramos sabido') combinada con una consecuencia duradera en el presente (apódosis con condicional simple: 'hoy tendríamos'). Son indispensables para evaluar el impacto a largo plazo de decisiones históricas y ecológicas."
            },
            {
                "type": "table",
                "title": "Estructuras condicionales mixtas en análisis prospectivo",
                "rows": [
                    ["Si se hubiera valorado la farmacopea ancestral hace décadas, hoy la Amazonía lideraría la biotecnología médica mundial.", "If ancestral pharmacopeia had been valued decades ago, today Amazonia would lead global medical biotechnology."],
                    ["De haber frenado la tala en el siglo pasado, no padeceríamos ahora estas sequías extremas en la cuenca.", "Had logging been stopped in the last century, we would not suffer these extreme droughts in the basin now."],
                    ["Si los Estados hubieran coordinado su legislación ambiental, las mafias no operarían con tanta impunidad fronteriza.", "If States had coordinated their environmental legislation, mafias would not operate with such border impunity."],
                    ["De no haber existido el Tratado de Cooperación Amazónica, el bioma carecería hoy de un marco de defensa común.", "Had the Amazonian Cooperation Treaty not existed, the biome would lack a common defense framework today."]
                ]
            },
            {
                "type": "tip",
                "content": "La fórmula 'De + infinitivo compuesto' ('De haber frenado') es un sustituto estilísticamente refinado de 'Si hubiera frenado', sumamente común en la prosa ensayística y académica avanzada."
            }
        ]
    }
}

STORIES_DATA = {
    "classics/b2/b2-32": {
        "id": "b2-32",
        "title": "Canaima (Rómulo Gallegos, 1935)",
        "level": "B2",
        "lesson": 1,
        "type": "classics",
        "estimatedMinutes": 15,
        "summary": "Estudio literario y ontológico de la novela 'Canaima' de Rómulo Gallegos: la odisea de Marcos Vargas en la selva del Orinoco y la Amazonía venezolana, el mito del espíritu maligno de la selva virgen, el drama de los caucheros y la dialéctica entre la fuerza ciega de la naturaleza y la voluntad humana.",
        "characters": [
            "Marcos Vargas (protagonista temerario dominado por la sed de aventura salvaje)",
            "Cholo Parima y los capataces de las cuadrillas caucheras",
            "Gabriel Ureña (amigo intelectual de Marcos)",
            "Los indios pemones y los espíritus de la selva (Canaima como fuerza primordial)"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Publicada en Barcelona en 1935, en pleno exilio voluntario durante la tiranía gomecista, 'Canaima' representa una de las cumbres narrativas más intensas, sombrías y poéticamente deslumbrantes del gran escritor y estadista venezolano Rómulo Gallegos. Tras haber retratado la llanura bravía en 'Doña Bárbara' y la costa abrasada en 'Cantaclaro', Gallegos penetró en este relato en las profundidades telúricas de la Guayana venezolana y los confines fluviales de la cuenca amazónica, donde los ríos Orinoco, Caroní, Caura y Ventuari desgarran la tierra virgen entre tepuyes milenarios. En este escenario titánico no impera la ley civil republicana ni el sosiego de la urbe letrada, sino la presencia sobrecogedora de Canaima: el espíritu terrible, multiforme e implacable de la naturaleza virgen, personificación mística del caos, la ferocidad ciega y la fascinación fatal que devora la cordura de los hombres que osan profanar sus secretos vegetales."
            },
            {
                "type": "narration",
                "text": "El protagonista de esta epopeya selvática es Marcos Vargas, un joven de Ciudad Bolívar dotado de una fortaleza física extraordinaria, un temperamento indómito y una sed insaciable de acción tempestuosa que rechaza la vida sedentaria del comercio familiar. Deslumbrado por los relatos de los navegantes fluviales y aventureros que remontan las corrientes misteriosas del Yuruari y el Cuyuní, Marcos decide internarse en la selva profunda para trabajar en la extracción del caucho y la balata. Por más que sus parientes y amigos sensatos como Gabriel Ureña le advierten que la selva es un abismo verde sin retorno que aniquila la piedad humana, el joven avanza con temerario arrojo, convencido de que su voluntad de hierro es capaz de subyugar cualquier obstáculo orográfico o embestida del destino adverso."
            },
            {
                "type": "narration",
                "text": "Al ingresar en el universo asfixiante de los campamentos caucheros ('purgueros'), Marcos descubre la verdadera faz del extractivismo selvático: un régimen atroz de servidumbre por deudas, violencia brutal y degradación moral donde los capataces armados como el temible Cholo Parima tiranizan a peones e indígenas desamparados. Aun a riesgo de que los sicarios del latifundio cauchero le tiendan emboscadas mortales en las trochas anegadas, Marcos Vargas se rebela con furia indomable contra la injusticia reinante, enfrentándose a balazos y a filo de machete contra los matones del monopolio comercial. En cada duelo a muerte y en cada encrucijada peligrosa, el protagonista siente que una fuerza oscura y telúrica se apodera de sus sentidos, transformándolo progresivamente: cual si fuera un elemento más de la tormenta tropical, la violencia salvaje de Canaima penetra en sus venas y desafía su conciencia civilizada."
            },
            {
                "type": "narration",
                "text": "No obstante sus victorias iniciales y su fama legendaria de hombre invencible a lo largo de las riberas del Orinoco, Marcos Vargas comprende al cabo de años de lucha errante que la selva no puede ser doblegada mediante el odio ni la violencia armada ciega. La naturaleza virgen no se somete a la soberbia del conquistador individualista: los árboles gigantescos, las ciénagas ponzoñosas y las fiebres palúdicas terminan aislando al héroe en un laberinto espiritual impenetrable. En un gesto supremo de desprendimiento y renuncia a las ambiciones del mundo exterior, Marcos se despoja de sus arreos mercantiles y se interna para siempre entre las comunidades indígenas del río Cuyuní, uniéndose en matrimonio sagrado con una doncella pemón y fundiéndose en el anonimato sagrado de la floresta como un habitante armónico del bosque ancestral."
            },
            {
                "type": "narration",
                "text": "El desenlace magistral de la novela arroja un rayo de esperanza civilizatoria hacia el porvenir de la patria grande: años más tarde, el hijo mestizo de Marcos Vargas es enviado a Caracas para educarse bajo la tutela de Gabriel Ureña, portando en su sangre la conjunción creadora entre la energía cósmica de la selva virgen y la luz del conocimiento humanista republicano. En definitiva, 'Canaima' trasciende los moldes de la novela de aventuras para erigirse en un tratado ontológico sobre el destino de América: la certidumbre de que nuestro continente solo hallará su plenitud cuando aprenda a convivir con su naturaleza colosal sin saquearla ni destruirla, armonizando el coraje indómito del habitante del bosque con la justicia, la ciencia y la dignidad fraterna que demanda el siglo de las luces."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué simboliza la figura mítica de 'Canaima' en la novela homónima de Rómulo Gallegos?",
                        "options": [
                            "Un buque de vapor fluvial que transporta minerales hacia el mar Caribe.",
                            "El espíritu terrible y despiadado de la selva virgen, fuerza ciega y primordial que desafía la voluntad humana.",
                            "Un tratado comercial firmado entre Venezuela y el Imperio británico.",
                            "La capital administrativa de una provincia minera en los Andes."
                        ],
                        "correctIndex": 1,
                        "explanation": "Canaima es la divinidad mítica indígena que encarna las fuerzas desatadas de la selva y el caos telúrico."
                    },
                    {
                        "question": "¿Cuál es la actitud de Marcos Vargas al ingresar a la explotación cauchera en la Guayana venezolana?",
                        "options": [
                            "Sumisión absoluta a las órdenes de los capataces extranjeros.",
                            "Rebeldía indómita frente a la explotación inhumana y fascinación por la violencia cósmica de la selva.",
                            "Desinterés total y regreso inmediato a su hogar en Ciudad Bolívar.",
                            "Organización de una compañía bancaria para especular con el precio del oro."
                        ],
                        "correctIndex": 1,
                        "explanation": "Marcos desafía la tiranía de los purgueros con coraje indómito, sintiéndose atraído por la furia de la selva."
                    },
                    {
                        "question": "¿Cómo culmina la trayectoria vital de Marcos Vargas y qué representa su hijo mestizo al final de la obra?",
                        "options": [
                            "Muere ejecutado en un presidio militar de la costa.",
                            "Se asimila a una comunidad indígena pemón, y su hijo viaja a educarse como síntesis entre la fuerza natural y la civilización.",
                            "Huye a Europa con un tesoro de diamantes extraídos del Caroní.",
                            "Se convierte en presidente de la república tras una revolución armada."
                        ],
                        "correctIndex": 1,
                        "explanation": "Marcos se integra en la armonía indígena, y su hijo mestizo simboliza la síntesis futura entre selva y cultura republicana."
                    }
                ]
            }
        }
    },
    "world/b2/b2-amazoniapan-01": {
        "id": "b2-amazoniapan-01",
        "title": "La cuenca de las ocho naciones: La OTCA y la Declaración de Belém",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La cooperación interestatal en la cuenca amazónica: la Organización del Tratado de Cooperación Amazónica (OTCA) con sede en Brasilia, los ocho países firmantes y el hito histórico de la Cumbre de Belém de 2023 para evitar el punto de no retorno climático.",
        "characters": [
            "Jefes de Estado de las ocho naciones amazónicas",
            "Diplomáticos y científicos de la Secretaría Permanente de la OTCA",
            "Portavoces de la Coordinadora de las Organizaciones Indígenas de la Cuenca Amazónica (COICA)"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Con una extensión territorial que rebasa los siete millones de kilómetros cuadrados en el corazón del continente suramericano, la cuenca del río Amazonas no pertenece en exclusividad a una sola república soberana, sino que constituye un patrimonio ecológico indivisible compartido por ocho naciones soberanas: Bolivia, Brasil, Colombia, Ecuador, Guyana, Perú, Surinam y Venezuela (junto al territorio ultramarino de la Guayana Francesa). Reconociendo que ningún Estado aislado, por poderoso o extenso que sea, puede garantizar por sí solo la integridad biológica y climática de semejante coloso planetario, los gobiernos de la región suscribieron el 3 de julio de 1978 el histórico Tratado de Cooperación Amazónica (TCA), instrumento multilateral pionero que dio nacimiento institucional a la Organización del Tratado de Cooperación Amazónica (OTCA), con secretaría permanente establecida en Brasilia. Asimismo, la cuenca alberga a cerca de cincuenta millones de seres humanos pertenecientes a diversas etnias originarias, comunidades afrodescendientes y colonos ribereños que dependen de sus aguas para la navegación y la alimentación diaria."
            },
            {
                "type": "narration",
                "text": "Durante décadas, la labor diplomática de la OTCA estuvo constreñida por tensiones geopolíticas bilaterales, desconfianzas territoriales heredadas del pasado colonial y prioridades de desarrollo asimétricas entre los países miembros. Sin embargo, la aceleración vertiginosa del cambio climático global y las alertas inequívocas de la comunidad científica internacional provocaron un viraje estratégico decisivo en el siglo veintiuno. Investigadores de renombre mundial advirtieron que la Amazonía se aproximaba peligrosamente al denominado 'punto de no retorno' ('tipping point'): un umbral catastrófico de deforestación acumulada (situado entre el veinte y el veinticinco por ciento de su cobertura original) a partir del cual el ciclo de lluvias colapsaría de forma irreversible, transformando vastas extensiones de selva tropical en sabanas secas degradadas. Por consiguiente, los modelos climatológicos más sofisticados corroboran que cruzar este umbral desataría incendios espontáneos incontrolables en el dosel y privaría de precipitaciones vitales a las principales urbes del continente."
            },
            {
                "type": "narration",
                "text": "Fue en respuesta a esta amenaza existencial donde los mandatarios de los ocho países amazónicos se congregaron en agosto de 2023 en la ciudad brasileña de Belém do Pará para celebrar la histórica IV Cumbre Amazónica. El fruto de aquellas deliberaciones de alto nivel fue la adopción formal de la 'Declaración de Belém': un exhaustivo programa de acción de ciento trece puntos consensuados en aras de que los Estados articulen políticas públicas conjuntas de fiscalización satelital, combate implacable contra el crimen organizado transnacional y erradicación total de la minería ilegal y la deforestación no autorizada. Asimismo, la declaración ratificó la necesidad imperiosa de promover una bioeconomía soberana basada en los productos forestales no maderables y el conocimiento ancestral. Por añadidura, el documento sentó las bases para la creación del Centro de Cooperación Policial Internacional en Manaus y del Panel Técnico-Científico Intergubernamental de la Amazonía, inspirado en el modelo del IPCC."
            },
            {
                "type": "narration",
                "text": "Un elemento cualitativo de enorme trascendencia política en Belém fue la participación activa y protagónica de la sociedad civil organizada y de las federaciones indígenas de la cuenca, articuladas a través de la Coordinadora de las Organizaciones Indígenas de la Cuenca Amazónica (COICA). En los multitudinarios 'Diálogos Amazónicos' previos a la cita presidencial, más de veinticinco mil delegados campesinos, científicos, ribereños y guardianes nativos exigieron con firmeza que los acuerdos intergubernamentales no quedaran confinados a meras declaraciones retóricas bienintencionadas, reclamando que se garantice la titulación colectiva inmediata de cien millones de hectáreas de territorios indígenas pendientes de demarcación legal en los ocho países firmantes."
            },
            {
                "type": "narration",
                "text": "En conclusión, la gobernanza panamazónica liderada por la OTCA y revitalizada por el espíritu de Belém demuestra que la cooperación multilateral suramericana es el único camino viable para salvaguardar el mayor pulmón hídrico del planeta. En última instancia, la defensa de la Amazonía trasciende las fronteras nacionales y las diferencias ideológicas coyunturales de los gobiernos de turno: exige concebir a la cuenca como un organismo vivo único e indivisible cuya salud depende de la solidaridad de sus pueblos. Al asumir este compromiso histórico ante la comunidad internacional, las ocho naciones amazónicas reafirman que la soberanía verdadera no consiste en destruir los bosques para enriquecer a monopolios efímeros, sino en custodiar la vida para las generaciones venideras de toda la humanidad."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué organismo intergubernamental reúne a los ocho países de la cuenca amazónica y dónde tiene su sede permanente?",
                        "options": [
                            "La Comunidad Andina de Naciones (CAN), con sede en Lima.",
                            "La Organización del Tratado de Cooperación Amazónica (OTCA), con secretaría permanente en Brasilia.",
                            "La Comisión Económica para América Latina (CEPAL), con sede en Santiago de Chile.",
                            "El Parlamento del Mercosur, con sede en Montevideo."
                        ],
                        "correctIndex": 1,
                        "explanation": "La OTCA es el único organismo multilateral panamazónico y su secretaría permanente opera en Brasilia."
                    },
                    {
                        "question": "¿En qué consiste el 'punto de no retorno' ecológico advertido por los científicos en la selva amazónica?",
                        "options": [
                            "En la inundación permanente de todas las ciudades costeras del Pacífico.",
                            "En un umbral de deforestación acumulada tras el cual la selva colapsa de forma irreversible convirtiéndose en sabana seca.",
                            "En el enfriamiento súbito del océano Atlántico que detiene las tormentas tropicales.",
                            "En la congelación de las aguas del río Amazonas durante el solsticio de verano."
                        ],
                        "correctIndex": 1,
                        "explanation": "El punto de no retorno implica la pérdida de la capacidad autorregenerativa del bosque con savanización irreversible."
                    },
                    {
                        "question": "¿Cuál fue el objetivo central consagrado en la Declaración de Belém suscrita en agosto de 2023?",
                        "options": [
                            "Privatizar la navegación fluvial en todos los afluentes de la cuenca.",
                            "Articular políticas conjuntas contra la deforestación ilegal, la minería ilícita y promover la bioeconomía inclusiva.",
                            "Construir una carretera asfaltada que una directamente Caracas con La Paz atravesando los parques naturales.",
                            "Prohibir el uso de energías renovables en las reservas forestales."
                        ],
                        "correctIndex": 1,
                        "explanation": "La Declaración de Belém consensuó medidas conjuntas de fiscalización forestal y bioeconomía para evitar el colapso amazónico."
                    }
                ]
            }
        }
    },
    "world/b2/b2-amazoniapan-02": {
        "id": "b2-amazoniapan-02",
        "title": "Pueblos transfronterizos y naciones sin fronteras: El trapecio amazónico",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La porosidad fronteriza y la interculturalidad fluvial en el Trapecio Amazónico: la confluencia urbana de Leticia (Colombia), Tabatinga (Brasil) y Santa Rosa (Perú), y la soberanía ancestral de pueblos binacionales como los Ticunas y Yanomamis.",
        "characters": [
            "Pobladores y comerciantes de la triple frontera (Leticia, Tabatinga y Santa Rosa)",
            "Líderes indígenas del pueblo Ticuna (Magüta) y chamanes Yanomami",
            "Guardaparques y agentes de aduana de los tres países ribereños"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el remoto vértice donde coinciden las soberanías territoriales de Colombia, Brasil y Perú, a miles de kilómetros de las capitales andinas o de las urbes atlánticas, la frontera cartográfica trazada por los tratados diplomáticos pierde su rigidez geométrica para dar paso a una de las dinámicas de convivencia humana más fascinantes del planeta: el Trapecio Amazónico. En este enclave fluvial único, las ciudades de Leticia (en el departamento colombiano de Amazonas) y Tabatinga (en el estado brasileño de Amazonas) forman una conurbación urbana perfectamente continua y abierta, donde los ciudadanos cruzan de un país a otro simplemente atravesando una avenida pavimentada, sin puestos de control militar ni vallas de contención aduanera, mientras que la pequeña isla peruana de Santa Rosa de Yavarí saluda desde la orilla opuesta del gran río entre barcazas de madera y lanchas rápidas."
            },
            {
                "type": "narration",
                "text": "En este crisol cosmopolita y selvático florece una identidad fronteriza fluida y espontánea que los sociólogos y lingüistas denominan con admiración 'fronteriza' o 'portuñol amazónico'. Los pobladores locales transitan con naturalidad asombrosa entre el español y el portugués en una misma frase al comprar frutas en el mercado público, escuchar emisoras radiales de samba y vallenato o realizar transacciones comerciales indistintamente en pesos colombianos, reales brasileños o soles peruanos. Lejos de constituir un foco de hostilidad o conflicto militar entre las tres repúblicas hermanas, esta vecindad porosa demuestra que los ríos no dividen a las sociedades ribereñas, sino que operan como magnéticas avenidas de encuentro cultural, comercio solidario y enriquecimiento mutuo. De igual manera, las escuelas binacionales y los centros de salud ribereños atienden a pacientes de ambas márgenes fluviales sin exigir visados restrictivos, consolidando una red comunitaria de auxilio recíproco que desafía cualquier pretensión de aislamiento burocrático."
            },
            {
                "type": "narration",
                "text": "Mucho más allá del entramado urbano contemporáneo, la verdadera profundidad humana del bioma radica en la existencia milenaria de pueblos originarios transfronterizos cuyas cosmovisiones y lazos de parentesco preceden por siglos a la demarcación de los Estados republicanos modernos. El pueblo Ticuna (o Magüta), que cuenta con más de sesenta mil integrantes repartidos entre las riberas fluviales de Brasil, Colombia y Perú, constituye la nación indígena más numerosa de la Amazonía compartida. Para los ancianos y sabios ticunas, el río Amazonas y los bosques no son líneas divisorias de soberanía estatal ajena, sino su hogar común e indivisible, articulado por clanes totémicos que se visitan mutuamente para celebrar las ceremonias sagradas de la pubertad femenina (la fiesta de la 'pelazón') sin importar qué bandera ondee en el puerto. Del mismo modo, los caciques coordinan asambleas periódicas para consensuar normas de pesca artesanal y vedas estacionales en las lagunas de varzea, salvaguardando la reproducción del pirarucú y otras especies ictiológicas indispensables para la supervivencia comunitaria."
            },
            {
                "type": "narration",
                "text": "Una realidad análoga se vive en las serranías septentrionales de la Sierra de Parima, en la frontera montañosa y selvática que separa a Venezuela de Brasil, territorio ancestral del pueblo Yanomami. Con una población cercana a los treinta y ocho mil habitantes distribuidos en aldeas comunales circulares ('shabonos') a ambos lados de la divisoria de aguas, los Yanomamis han resistido durante siglos el asedio exterior preservando una lengua milenaria y una concepción cósmica donde la selva ('urihi a') es concebida como un ser viviente que respira, siente y sufre. Cuando los mineros ilegales de oro ('garimpeiros') invaden los ríos con maquinaria pesada y mercurio, las enfermedades y la violencia contaminan indistintamente los valles a ambos lados de la frontera, demostrando que la vulnerabilidad y la lucha de los pueblos originarios son compartidas."
            },
            {
                "type": "narration",
                "text": "En definitiva, los pueblos transfronterizos y las ciudades fluviales del Trapecio Amazónico interpelan profundamente los conceptos tradicionales de soberanía territorial excluyente y frontera securitizada heredados de la Europa decimonónica. Al demostrar que es posible convivir en paz, compartir recursos vitales y preservar identidades ancestrales más allá de los pasaportes y los sellos aduaneros, estas comunidades enseñan a América del Sur una lección luminosa de integración genuina. En última instancia, la Amazonía sin fronteras recuerda que la verdadera fraternidad continental no se firma en salones dorados de cancillerías lejanas, sino que se forja día a día en las canoas que cruzan las aguas libres, uniendo a pueblos que reconocen en la selva a su madre protectora común."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuáles son las tres poblaciones urbanas que conforman la triple frontera en el Trapecio Amazónico?",
                        "options": [
                            "Iquitos, Puerto Maldonado y Riberalta.",
                            "Leticia (Colombia), Tabatinga (Brasil) y Santa Rosa (Perú).",
                            "Cucui, San Carlos de Río Negro y Mitú.",
                            "Manaus, Belém y Santarém."
                        ],
                        "correctIndex": 1,
                        "explanation": "Leticia, Tabatinga y Santa Rosa de Yavarí forman el enclave urbano neurálgico de la triple frontera."
                    },
                    {
                        "question": "¿Qué pueblo originario es el más numeroso de la Amazonía compartida entre Brasil, Colombia y Perú?",
                        "options": [
                            "Los mapuches.",
                            "Los ticunas (Magüta), con más de sesenta mil personas unidas por clanes y parentesco común.",
                            "Los guaraníes del Chaco.",
                            "Los diaguitas de las estepas andinas."
                        ],
                        "correctIndex": 1,
                        "explanation": "El pueblo Ticuna habita históricamente el trapecio fluvial a ambos lados de las tres fronteras nacionales."
                    },
                    {
                        "question": "¿Qué amenaza crítica comparten los Yanomamis en la frontera selvática entre Venezuela y Brasil?",
                        "options": [
                            "La invasión de mineros ilegales de oro que contaminan los ríos con mercurio y propagan epidemias mortales.",
                            "La falta de transporte aéreo supersónico hacia las capitales.",
                            "La salinización de los pozos de agua potable por mareas oceánicas.",
                            "La congelación de los bosques durante los inviernos polares."
                        ],
                        "correctIndex": 0,
                        "explanation": "La minería ilegal de oro ('garimpo') contamina con mercurio y desata crisis sanitarias en el territorio Yanomami binacional."
                    }
                ]
            }
        }
    },
    "world/b2/b2-amazoniapan-03": {
        "id": "b2-amazoniapan-03",
        "title": "Ríos voladores y el pulso hidrológico continental",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "El ciclo del agua panamazónico y los 'ríos voladores': cómo la evapotranspiración de cuatrocientos mil millones de árboles bombea ingentes masas aéreas de humedad que chocan contra la cordillera de los Andes y riegan la producción agrícola de todo el cono sur.",
        "characters": [
            "Antonio Nobre (científico brasileño pionero en la teoría de los ríos voladores)",
            "Meteorólogos e hidrólogos del Centro de Ciencia del Sistema Terrestre",
            "Agricultores de la cuenca del Plata beneficiarios de las lluvias amazónicas"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Bajo la mirada superficial de un observador desacostumbrado, el río Amazonas parecería ser el único gran cauce por donde circula el agua dulce de América del Sur. Sin embargo, la ciencia meteorológica contemporánea ha demostrado que sobre las copas esmeraldas de los cuatrocientos mil millones de árboles que pueblan la floresta amazónica discurre un caudal invisible aún más prodigioso y vital para la supervivencia del continente: los llamados 'ríos voladores' ('rios voadores'). Este fenómeno hidrológico colosal consiste en descomunales corrientes atmosféricas de vapor de agua bombeadas activamente hacia la troposfera por la selva en pie, las cuales transportan diariamente una cantidad de humedad que rivaliza o incluso supera los doscientos mil metros cúbicos por segundo que vierte el río Amazonas al océano Atlántico."
            },
            {
                "type": "narration",
                "text": "El funcionamiento físico de este mecanismo biológico extraordinario fue explicado magistralmente por científicos de vanguardia como el investigador brasileño Antonio Nobre a través de la teoría de la 'bomba biótica'. En primer término, las hojas de un solo árbol maduro de gran porte pueden transpirar más de mil litros de agua al día hacia la atmósfera mediante el proceso de evapotranspiración vegetal. Al ascender esta ingente masa de vapor y condensarse en nubes bajas, se genera una caída drástica de la presión atmosférica local que funciona como una formidable bomba aspirante natural: esta succión atrae con fuerza constante las masas de aire húmedo procedentes del océano Atlántico tropical hacia el interior continental, impidiendo que el corazón de Suramérica se convierta en un desierto estéril como ocurre en otras latitudes del planeta."
            },
            {
                "type": "narration",
                "text": "Una vez en el aire, estos gigantescos ríos aéreos de vapor avanzan arrastrados por los vientos alisios hacia el oeste continental hasta encontrarse de frente con la monumental muralla geológica de la cordillera de los Andes. Incapaces de superar las cumbres nevadas de más de cinco mil metros de altitud que forman el espinazo montañoso de Colombia, Ecuador y Perú, las nubes amazónicas son desviadas magistralmente hacia el sur, serpenteando por los valles andino-amazónicos de Bolivia, Paraguay, el centro y sureste de Brasil, el norte de Argentina y Uruguay. Es precisamente esta humedad reconducida la que desencadena las lluvias bienhechoras que llenan los embalses hidroeléctricos de São Paulo y nutren las llanuras agrícolas más fértiles de la cuenca del Plata. Asimismo, las represas colosales como Itaipú en la frontera brasileño-paraguaya y Yacyretá entre Argentina y Paraguay dependen críticamente de los caudales sostenidos que este ciclo aéreo vierte sobre las cuencas altas de los ríos Paraná y Paraguay durante los meses estivales."
            },
            {
                "type": "narration",
                "text": "Por consiguiente, la prosperidad agroalimentaria, energética e industrial de potencias del cono sur como Argentina, Uruguay o el sur brasileño depende indisolublemente de la preservación estricta de la selva amazónica ubicada a miles de kilómetros de distancia. Si la tala rasa y los incendios continúan desforestando las cuencas de los ríos Tapajós, Xingu y Madeira, la bomba biótica se debilitará hasta apagarse por completo: sin árboles no hay transpiración, sin transpiración no hay ríos aéreos, y sin ríos aéreos las pampas trigueras y los maizales del sur sufrirán sequías crónicas catastróficas que paralizarán la producción alimentaria de millones de personas y desatarán crisis energéticas sin precedentes. Por ende, fenómenos meteorológicos extremos como El Niño ven agravados sus impactos cuando coinciden con temporadas de quemas intensas en Rondônia y Mato Grosso, alterando los patrones de circulación monzónica y amenazando la seguridad hídrica de capitales metropolitanas como Asunción, Montevideo y Buenos Aires."
            },
            {
                "type": "narration",
                "text": "En suma, la revelación científica de los ríos voladores destruye definitivamente la ilusión provinciana de que la Amazonía es un territorio ajeno que compete únicamente a los pobladores de la selva o a los guardaparques estatales. Todos los habitantes de América del Sur, desde el ganadero de la pampa húmeda argentina hasta el habitante de una metrópoli andina, beben del agua y se alimentan de las cosechas que el bosque tropical amazónico exhala hacia el cielo con su aliento generoso. En última instancia, proteger la Amazonía es proteger el agua de nuestros propios grifos y el pan de nuestras propias mesas, ratificando la verdad ecológica más bella y sagrada de la naturaleza: que en nuestro continente todo está profundamente entretejido en una sola y misma respiración cósmica."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿En qué consiste el fenómeno meteorológico e hidrológico de los 'ríos voladores' en América del Sur?",
                        "options": [
                            "En naves espaciales que rocían agua salada sobre los desiertos costeros.",
                            "En gigantescas corrientes aéreas de vapor de agua bombeadas por la evapotranspiración de los árboles amazónicos.",
                            "En acueductos artificiales de aluminio construidos sobre los árboles de la selva.",
                            "En ríos subterráneos de lava volcánica que fluyen bajo los Andes."
                        ],
                        "correctIndex": 1,
                        "explanation": "Los ríos voladores son inmensas masas de vapor transpiradas por la selva que transportan humedad vital por todo el continente."
                    },
                    {
                        "question": "¿Qué papel decisivo desempeña la cordillera de los Andes en el curso de los ríos aéreos de vapor?",
                        "options": [
                            "Absorbe toda la humedad transformándola en rocas calizas.",
                            "Actúa como una barrera natural que frena las nubes y las desvía hacia el sur, irrigando la cuenca del Plata.",
                            "Permite el paso directo de las nubes hacia las islas del océano Pacífico tropical.",
                            "Calienta las corrientes de aire disipando las lluvias en cuestión de minutos."
                        ],
                        "correctIndex": 1,
                        "explanation": "La muralla andina bloquea el avance al oeste y redirige la humedad amazónica hacia el centro y cono sur de Sudamérica."
                    },
                    {
                        "question": "¿Qué consecuencia directa provocaría la destrucción de la selva amazónica en la agricultura del cono sur?",
                        "options": [
                            "Un aumento descontrolado de las cosechas de algodón en la Patagonia.",
                            "El debilitamiento de la bomba biótica con sequías crónicas y pérdida masiva de cosechas agrícolas y energía.",
                            "La proliferación de glaciares en las llanuras pampeanas.",
                            "La sustitución inmediata de las lluvias por agua marina dulce."
                        ],
                        "correctIndex": 1,
                        "explanation": "Sin la evapotranspiración del bosque, cesan las lluvias en el cono sur, provocando sequías agrícolas catastróficas."
                    }
                ]
            }
        }
    },
    "world/b2/b2-amazoniapan-04": {
        "id": "b2-amazoniapan-04",
        "title": "Minería ilegal, mercurio y la defensa de las cuencas binacionales",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "El drama del crimen ambiental transnacional en las cuencas amazónicas: la minería aluvial de oro con dragas clandestinas, la contaminación por mercurio tóxico en ríos binacionales como el Caquetá, Putumayo y Madre de Dios, y los operativos militares conjuntos.",
        "characters": [
            "Fiscales de delitos ambientales y oficiales de guardacostas fluviales",
            "Biólogos y toxicólogos que miden la bioacumulación de metales pesados",
            "Comunidades ribereñas e indígenas afectadas por la contaminación del agua"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A lo largo de miles de kilómetros de meandros fluviales donde las fronteras de Bolivia, Brasil, Colombia, Ecuador y Perú se confunden entre el follaje espeso de la selva virgen, una de las actividades delictivas más lucrativas, destructivas y letales de la actualidad prolifera en la clandestinidad: la minería aluvial ilegal de oro. Equipadas con gigantescas dragas flotantes con motores diésel de gran potencia, motobombas de aspiración continua y retroexcavadoras que remueven miles de toneladas de sedimentos por hora, redes criminales transnacionales devastan los lechos de ríos emblemáticos como el Madre de Dios en Perú, el Caquetá y Putumayo en Colombia, y el Tapajós y Yanomami en Brasil, dejando a su paso inmensos cráteres de barro muerto y desolación biológica absoluta. Aunado a ello, las orillas deforestadas por el dragado aluvial pierden la protección radicular de los árboles de ribera, desencadenando procesos erosivos violentos que colmatan de arenas estériles los cauces de navegación fluvial ancestral y sepultan las zonas de desove de peces autóctonos."
            },
            {
                "type": "narration",
                "text": "Sin embargo, el impacto ecológico más aterrador e insidioso de esta fiebre del oro clandestina radica en el uso masivo y descontrolado del mercurio líquido ('azogue'), reactivo químico indispensable para amalgamar y separar las partículas microscópicas de oro de las arenas fluviales. Según estimaciones coincidentes de organismos toxicológicos internacionales, por cada kilogramo de oro refinado en las balsas ilegales, se vierten al medio acuático entre dos y tres kilogramos de mercurio puro. Al entrar en contacto con las bacterias anaeróbicas de los fondos fluviales, este metal pesado se transmuta en metilmercurio: una neurotoxina extremadamente virulenta y liposoluble que no se degrada con el paso del tiempo, sino que se bioacumula y biomagnifica exponencialmente a través de la cadena alimentaria acuática."
            },
            {
                "type": "narration",
                "text": "Las primeras y más trágicas víctimas de este envenenamiento invisible son las comunidades indígenas y ribereñas que dependen casi exclusivamente de la pesca fluvial para su subsistencia proteica cotidiana. Peces carnívoros de gran consumo familiar como el bagre rayado, la mota y el piraíba concentran niveles de metilmercurio que duplican o triplican los límites máximos recomendados por la Organización Mundial de la Salud (OMS). Los estudios clínicos realizados en aldeas del río Caquetá y del valle de Madre de Dios revelaron datos escalofriantes: concentraciones alarmantes de mercurio en el cabello de mujeres lactantes y niños pequeños, asociadas a malformaciones congénitas, daños neurológicos irreversibles, temblores motores crónicos, ceguera parcial y pérdidas graves del desarrollo cognitivo infantil. A su vez, las postas médicas rurales carecen a menudo de los equipos analíticos y quelantes necesarios para diagnosticar y tratar oportunamente estas intoxicaciones masivas, dejando a las familias nativas en un estado de desprotección sanitaria angustiosa frente a los estragos silenciosos del metal pesado."
            },
            {
                "type": "narration",
                "text": "Frente a una criminalidad transnacional que aprovecha las fronteras porosas para evadir la justicia —trasladando las dragas mecánicas de una margen nacional a otra en cuestión de horas según la presencia de las patrullas policiales—, los Estados de la región han debido coordinar operativos binacionales de interdicción armada de gran escala. Operaciones conjuntas como las ejecutadas entre las fuerzas armadas de Colombia y Brasil a lo largo del río Puré permitieron dinamitar y destruir decenas de barcazas mineras clandestinas e incautar toneladas de mercurio importado de contrabando. Empero, los fiscales especializados coinciden en que la mera destrucción física de maquinaria resulta insuficiente si no se persiguen los flujos financieros ilícitos y las joyerías internacionales que lavan el oro manchado de sangre en los mercados de Zúrich, Londres y Nueva York."
            },
            {
                "type": "narration",
                "text": "En conclusión, el combate frontal contra la minería aluvial ilegal y la contaminación por mercurio no es un simple asunto de policía aduanera, sino una batalla decisiva en defensa de la salud pública, la soberanía de los pueblos amazónicos y los derechos inalienables de la naturaleza. Los ríos suramericanos no pueden continuar siendo cloacas tóxicas sacrificadas en el altar de la codicia financiera transnacional. En última instancia, recuperar la pureza cristalina de los caudales binacionales y restaurar las cuencas degradadas constituye un imperativo ético irrenunciable que une a todas las naciones del bioma en un mismo juramento de justicia ecológica, dignidad cívica y preservación de la vida humana para los siglos por venir."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué es tan peligroso el mercurio utilizado en la minería aluvial ilegal de oro?",
                        "options": [
                            "Porque se evapora y congela el aire tropical circundante.",
                            "Porque se transforma en metilmercurio en el agua, bioacumulándose en los peces y causando daños neurológicos irreversibles en humanos.",
                            "Porque atrae a los caimanes hacia las zonas recreativas urbanas.",
                            "Porque acelera el crecimiento de vegetación desértica en los bosques."
                        ],
                        "correctIndex": 1,
                        "explanation": "El metilmercurio se acumula en la cadena trófica provocando gravísimos daños neurotóxicos y malformaciones en la población."
                    },
                    {
                        "question": "¿De qué manera burlan las redes de minería ilegal el control estatal en los ríos amazónicos?",
                        "options": [
                            "Compran submarinos atómicos en ferias internacionales.",
                            "Mueven sus dragas flotantes de una margen nacional a otra aprovechando la frontera fluvial porosa y desprovista de vigilancia permanente.",
                            "Se disfrazan de diplomáticos de embajadas europeas.",
                            "Ocultan sus motores dentro de troncos de madera tallada a mano."
                        ],
                        "correctIndex": 1,
                        "explanation": "Las mafias aprovechan los límites fronterizos para evadir la jurisdicción policial cambiando de país al cruzar el río."
                    },
                    {
                        "question": "¿Qué medida estructural reclaman los fiscales ambientales más allá de la destrucción física de las dragas?",
                        "options": [
                            "Permitir el libre comercio de mercurio sin restricciones.",
                            "Rastrear y desarticular las redes financieras internacionales y joyerías que compran y lavan el oro ilegal en mercados mundiales.",
                            "Prohibir el uso de canoas a las comunidades indígenas ancestrales.",
                            "Construir muros de cemento a lo largo de todos los ríos amazónicos."
                        ],
                        "correctIndex": 1,
                        "explanation": "La lucha contra la minería ilegal requiere golpear la cadena de lavado financiero internacional del oro ilícito."
                    }
                ]
            }
        }
    },
    "world/b2/b2-amazoniapan-05": {
        "id": "b2-amazoniapan-05",
        "title": "Bioeconomía y farmacopea del bosque en pie: El futuro regenerativo",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "La alternativa económica sostenible para la Amazonía: la bioeconomía del bosque en pie frente al extractivismo depredador, la farmacopea ancestral de los pueblos indígenas, la recolección comunitaria de açaí, castaña y copoazú, y la lucha contra la biopiratería internacional.",
        "characters": [
            "Biotecnólogos y farmacólogos de institutos amazónicos de investigación",
            "Recolectores y cooperativistas de productos forestales no maderables",
            "Chamanes y médicos tradicionales guardianes de la sabiduría botánica"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Durante siglos, la lógica económica hegemónica impuesta por el modelo extractivista colonial y poscolonial concibió a la selva amazónica como un obstáculo estéril que debía ser 'desbrozado', talado y quemado para dar paso a actividades productivas convencionales como la ganadería vacuna extensiva, la agricultura de monocultivo o la explotación minera. Sin embargo, los más lúcidos centros de investigación científica del continente y las comunidades originarias han demostrado de forma concluyente que la selva viva y en pie alberga una riqueza biológica, genética y terapéutica infinitamente superior a cualquier dividendo a corto plazo generado por su destrucción. Esta certeza es el fundamento ético de la 'bioeconomía del bosque en pie': un paradigma socioeconómico regenerativo que persigue generar bienestar humano e innovación científica respetando escrupulosamente los ciclos vitales del bioma."
            },
            {
                "type": "narration",
                "text": "En el corazón de esta bioeconomía innovadora se encuentra la inagotable farmacopea vegetal amazónica, preservada durante milenios por el saber empírico de chamanes, taitas y médicos tradicionales de más de cuatrocientas naciones indígenas. Sustancias legendarias como el curare —utilizado ancestralmente por los cazadores para emponzoñar cerbatanas y transformado por la medicina moderna en anestésicos musculares indispensables para la cirugía quirúrgica cardiovascular— o la corteza de la quina, de donde se extrajo la quinina que salvó a millones de seres humanos de la malaria, evidencian el potencial farmacológico del bosque. Hoy en día, extractos de plantas prodigiosas como la uña de gato (antinflamatoria e inmunoestimulante) o la sangre de drago (cicatrizante epitelial) revolucionan los laboratorios farmacéuticos mundiales. Incluso preparados sagrados y enteógenos milenarios como la ayahuasca o yagé, empleados en ceremonias de sanación psicosomática comunitaria, atraen hoy a científicos internacionales interesados en comprender los mecanismos neuroquímicos de la dimetiltriptamina en la regeneración neuronal y el tratamiento de traumas psicológicos severos."
            },
            {
                "type": "narration",
                "text": "Asimismo, las cadenas de valor basadas en los productos forestales no maderables (PFNM) han demostrado su enorme viabilidad comercial al empoderar a decenas de miles de familias campesinas y recolectoras en Brasil, Bolivia y Perú. Frutos tropicales de excepcionales propiedades nutricionales como el açaí, el copoazú, el camu-camu (con concentraciones de vitamina C cincuenta veces superiores a las de la naranja) y la nuez o castaña de Pará generan economías comunitarias prósperas sin necesidad de talar un solo árbol centenario. Al organizarse en cooperativas autogestionadas con certificación agroecológica y comercio justo, los pobladores locales se convierten en los defensores más celosos y eficaces de sus reservas extractivas frente al avance de los madereros ilegales. Por otra parte, la industrialización sostenible de aceites esenciales extraídos de la andiroba y del copaiba abastece a cosméticas verdes internacionales, asegurando ingresos estables y justos a cooperativas de mujeres recolectoras que reinvierten sus ganancias en escuelas primarias y dispensarios locales."
            },
            {
                "type": "narration",
                "text": "Empero, el florecimiento de esta bioeconomía del conocimiento enfrenta un desafío jurídico y ético inaplazable en el plano internacional: la erradicación de la biopiratería transnacional. Durante décadas, corporaciones biotecnológicas y farmacéuticas de países del Norte global han patentado de forma fraudulenta moléculas y principios activos derivados del saber ancestral indígena sin solicitar consentimiento previo informado ni compartir de forma equitativa los cuantiosos beneficios económicos derivados de su comercialización. Frente a este despojo neocolonial, el Protocolo de Nagoya sobre acceso a los recursos genéticos y las legislaciones de propiedad intelectual colectiva de la cuenca amazónica exigen el reconocimiento soberano de los pueblos como legítimos creadores y custodios de su patrimonio biológico milenario."
            },
            {
                "type": "narration",
                "text": "En conclusión, el dilema de la Amazonía en el siglo veintiuno no estriba en elegir entre la miseria material de la inacción o la devastación destructiva de la selva: radica en edificar una economía del conocimiento verde que dialogue en pie de igualdad con la sabiduría ancestral de sus pobladores. Una hectárea de selva biodiversa en pie vale mucho más para el futuro de la humanidad que mil hectáreas de pastizales degradados para el ganado. En última instancia, la bioeconomía amazónica enseña al planeta que la verdadera modernidad no consiste en dominar y destruir la naturaleza con soberbia tecnológica, sino en aprender a leer sus secretos sagrados con veneración, gratitud y reverencia, transformando el saber en vida y esperanza para todo el género humano."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿En qué postulado ético y económico se fundamenta la 'bioeconomía del bosque en pie'?",
                        "options": [
                            "En talar la selva rápidamente para construir fábricas de plástico en la ribera.",
                            "En que la selva viva genera una riqueza biológica, científica y comunitaria superior y sostenible frente al extractivismo depredador.",
                            "En exportar toda la madera tropical sin procesar hacia los mercados asiáticos.",
                            "En desecar los humedales fluviales para facilitar el paso de ferrocarriles pesados."
                        ],
                        "correctIndex": 1,
                        "explanation": "La bioeconomía demuestra que los productos forestales no maderables y el bosque vivo generan mayor valor que la deforestación."
                    },
                    {
                        "question": "¿Qué fruto amazónico destaca por contener concentraciones de vitamina C hasta cincuenta veces más altas que la naranja?",
                        "options": [
                            "El camu-camu.",
                            "El plátano verde.",
                            "El maíz morado.",
                            "La aceituna de botija."
                        ],
                        "correctIndex": 0,
                        "explanation": "El camu-camu es célebre en la nutrición global por su altísimo contenido natural de ácido ascórbico."
                    },
                    {
                        "question": "¿Qué práctica ilícita busca erradicar el Protocolo de Nagoya en relación con los saberes indígenas?",
                        "options": [
                            "La navegación de canoas de madera en lagos comunitarios.",
                            "La biopiratería o apropiación comercial y patentamiento no autorizado de conocimientos ancestrales por corporaciones foráneas.",
                            "La reforestación de riberas fluviales con especies autóctonas.",
                            "La enseñanza de lenguas originarias en escuelas bilingües rurales."
                        ],
                        "correctIndex": 1,
                        "explanation": "El Protocolo de Nagoya protege a los pueblos originarios contra el patentamiento indebido y el saqueo de su patrimonio genético."
                    }
                ]
            }
        }
    },
    "world/b2/b2-amazoniapan-consolidation": {
        "id": "b2-amazoniapan-consolidation",
        "title": "La selva indivisible: El corazón biológico de la Patria Grande",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Síntesis reflexiva sobre la Amazonía Pancontinental: la cuenca de las ocho naciones, la OTCA, los ríos voladores, la resistencia indígena transfronteriza y la bioeconomía del bosque en pie.",
        "characters": [
            "Narradores y cronistas del bioma amazónico",
            "Pueblos indígenas, científicos y navegantes fluviales como protagonistas colectivos"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Al contemplar desde el aire la inmensidad infinita del manto verde amazónico, surcado por los meandros dorados de ríos titánicos que serpentean sin atender a las líneas ficticias de los mapas diplomáticos, el observador sensible comprende que se encuentra ante el santuario biológico más deslumbrante y vulnerable de la Tierra. En primer término, la Amazonía no es un conjunto inconexo de departamentos o provincias periféricas gobernadas desde capitales andinas o atlánticas lejanas; es un solo ser viviente continuo, una patria continental indivisible cuyo pulso regula el clima, el agua y la fertilidad de todo el hemisferio sur. Es decir, internarse en sus laberintos fluviales no supone descender al salvajismo primitivo, sino elevarse hacia la vanguardia ecológica más lúcida que la civilización contemporánea necesita con desesperada urgencia para salvar su propio porvenir. Por añadidura, la masa vegetal continua actúa como un gigantesco regulador térmico del planeta, cuya evaporación masiva amortigua las olas de calor extremo y disipa perturbaciones climáticas severas que de otro modo castigarían con mayor virulencia a todo el cono sur."
            },
            {
                "type": "narration",
                "text": "A través de la arquitectura institucional de la OTCA y el hito ecuménico de la Declaración de Belém de 2023, las ocho naciones de la cuenca han asumido el reto inaplazable de superar siglos de fragmentación y desconfianza para edificar una gobernanza ambiental común. Por una parte, la ciencia de los ríos voladores ha demostrado de forma incontrovertible que las lluvias de Buenos Aires, de São Paulo o de Montevideo nacen de la transpiración de los árboles amazónicos; por otra, los pueblos transfronterizos como los Ticunas y los Yanomamis recuerdan cotidianamente a los Estados que la verdadera soberanía habita en el respeto a las raíces ancestrales y en la preservación sagrada del bosque vivo frente a la codicia destructiva del extractivismo ilícito."
            },
            {
                "type": "narration",
                "text": "Asimismo, el combate sin tregua contra la minería aluvial ilegal y la contaminación por mercurio en cuencas binacionales como el Caquetá, el Putumayo y Madre de Dios evidencia que el crimen ambiental es una hidra transnacional que solo puede ser vencida mediante la solidaridad operativa y el coraje ético compartido. Frente a las dragas clandestinas que envenenan los ríos y amenazan el desarrollo de las generaciones infantiles, los pueblos ribereños alzan su voz reclamando una justicia implacable que no se detenga ante los señores de la guerra ni ante los lavadores financieros del oro ilícito en las plazas bursátiles del hemisferio norte. Del mismo modo, la titulación colectiva de las tierras ancestrales emerge como el baluarte más seguro y eficaz para blindar el territorio contra las invasiones de madereros y acaparadores de tierras."
            },
            {
                "type": "narration",
                "text": "En el horizonte del siglo veintiuno, la bioeconomía regenerativa del bosque en pie y el rescate de la farmacopea originaria trazan el camino luminoso hacia un modelo de desarrollo que no exige destruir la selva para generar riqueza y empleo digno. Al transformar frutos milagrosos como el açaí, el camu-camu y la castaña de Pará en motores de prosperidad comunitaria con valor agregado científico, los pobladores amazónicos demuestran al mundo que la economía más avanzada no es la que devasta los ecosistemas con retroexcavadoras, sino la que sabe descifrar con reverencia el código biológico del bosque y armonizar el laboratorio con la memoria milenaria de los ancianos y chamanes. Del mismo modo, la diversificación productiva mediante sistemas agroforestales regenerativos demuestra que la conservación estricta y el desarrollo económico no son términos antagónicos, sino dos vertientes indisociables de una misma soberanía alimentaria para los pueblos de la floresta."
            },
            {
                "type": "narration",
                "text": "En suma, quien escucha el susurro de la lluvia sobre el dosel selvático en Leticia, navega las corrientes majestuosas del río Negro en Manaus o contempla las nieblas eternas de los tepuyes guayaneses comprende que en la Amazonía late el corazón indomable de la humanidad entera. En última instancia, la defensa de la cuenca compartida enseña al continente americano que nuestra verdadera grandeza no se mide por la cantidad de árboles talados ni por las toneladas de oro extraídas a sangre y fuego, sino por nuestra capacidad colectiva de convivir en armonía con la Madre Tierra, honrar a los guardianes originarios del bosque y custodiar la maravilla de la vida para todas las generaciones que heredarán este planeta sagrado."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué se define a la Amazonía como un santuario biológico continental indivisible?",
                        "options": [
                            "Porque es una península rocosa rodeada de glaciares andinos.",
                            "Porque constituye un único macroecosistema cuyas lluvias, biodiversidad y ríos regulan el equilibrio ecológico de todo el continente suramericano.",
                            "Porque está gobernada en su totalidad por una sola empresa naviera privada.",
                            "Porque es un desierto arenoso sin presencia de ríos navegables."
                        ],
                        "correctIndex": 1,
                        "explanation": "La Amazonía es un sistema vivo continuo que articula el clima y el agua de toda la masa continental suramericana."
                    },
                    {
                        "question": "¿Qué alianza estratégica representa la OTCA revitalizada por la Cumbre de Belém de 2023?",
                        "options": [
                            "Un pacto militar defensivo para comprar armas nucleares en Europa.",
                            "La unión diplomática y científica de las ocho naciones amazónicas para evitar el colapso del bioma y promover la bioeconomía.",
                            "Una compañía petrolera binacional entre Guyana y Surinam.",
                            "Un acuerdo para privatizar las reservas de agua dulce de la selva."
                        ],
                        "correctIndex": 1,
                        "explanation": "La OTCA coordina las políticas de Estado de los ocho países en favor de la preservación forestal y la bioeconomía."
                    },
                    {
                        "question": "¿Qué lección fundamental aporta la bioeconomía del bosque en pie a la humanidad?",
                        "options": [
                            "Que la única forma de progresar es acelerar la tala rasa para plantaciones de soja.",
                            "Que es posible generar bienestar y avance científico respetando los ciclos del bosque y valorando los saberes ancestrales sin destruir la naturaleza.",
                            "Que los pueblos indígenas deben abandonar sus territorios selváticos para vivir en megalópolis costeras.",
                            "Que las medicinas sintéticas son incompatibles con cualquier planta vegetal."
                        ],
                        "correctIndex": 1,
                        "explanation": "La bioeconomía demuestra que la selva viva genera mayor riqueza sostenible que la deforestación extractivista."
                    }
                ]
            }
        }
    },
    "world/b2/b2-amazoniapan": {
        "id": "b2-amazoniapan",
        "title": "Amazonía Pancontinental: La cuenca compartida y el bioma sin fronteras",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 20,
        "summary": "Compendio general y panorámico sobre la Amazonía Pancontinental: la cuenca compartida por ocho naciones y la labor de la OTCA, los ríos voladores y el ciclo hidrológico continental, la porosidad fronteriza del Trapecio Amazónico, la resistencia de pueblos transfronterizos como Ticunas y Yanomamis, la lucha contra la minería de mercurio y el futuro de la bioeconomía.",
        "characters": [
            "Líderes de las ocho naciones amazónicas (OTCA)",
            "Chamanes y médicos tradicionales Ticuna y Yanomami",
            "Científicos del clima y defensores de los ríos voladores",
            "Cooperativistas y recolectores del bosque en pie"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "En el corazón geográfico del continente suramericano, acariciada por las brisas cálidas del océano Atlántico y contenida al occidente por la mole colosal de los Andes, se extiende la llanura selvática más portentosa, biodiversa y determinante de la biosfera planetaria: la Amazonía Pancontinental. Abarcando una superficie descomunal superior a los siete millones de kilómetros cuadrados repartidos entre ocho repúblicas soberanas —Bolivia, Brasil, Colombia, Ecuador, Guyana, Perú, Surinam y Venezuela— más la Guayana Francesa, este territorio no es un mero mosaico de parcelas cartográficas divididas por mojones fronterizos; es un organismo vivo indivisible, un océano dulce en constante transpiración donde el agua, la fauna y los pueblos originarios desafían cotidianamente las barreras aduaneras de los Estados nacionales. Aunado a ello, la confluencia entre los valles andinos y la llanura amazónica crea un gradiente de pisos altitudinales de biodiversidad incomparable, albergando especies endémicas de orquídeas, aves y anfibios que no existen en ninguna otra región del globo terráqueo."
            },
            {
                "type": "narration",
                "text": "La arquitectura política de este patrimonio común se encarna en la Organización del Tratado de Cooperación Amazónica (OTCA), cuya secretaría en Brasilia articula la voluntad concertada de las ocho naciones desde 1978. Tras décadas de aproximaciones cautelosas, la adopción formal de la histórica Declaración de Belém en agosto de 2023 marcó un hito de convergencia soberana sin precedentes: por primera vez en la historia contemporánea, los jefes de Estado proclamaron el compromiso unánime de actuar de manera mancomunada para impedir que el bioma alcance el irreversible 'punto de no retorno' climático. Asimismo, la cumbre reconoció que la soberanía territorial no se defiende con discursos aislacionistas, sino coordinando patrullajes conjuntos contra la deforestación y escuchando a las federaciones indígenas de la COICA. Asimismo, los mandatarios acordaron la creación de un fondo financiero soberano para financiar proyectos de transición ecológica justa y la instauración de una red de monitoreo satelital integrada para interceptar en tiempo real alertas de tala ilegal e incendios no autorizados."
            },
            {
                "type": "narration",
                "text": "En el plano hidrológico y atmosférico, la selva en pie demuestra su protagonismo ecuménico a través de los extraordinarios 'ríos voladores': monumentales corrientes aéreas de vapor impulsadas por la evapotranspiración de cuatrocientos mil millones de árboles que transportan ingentes masas de humedad hacia los Andes y el cono sur. Es esta formidable bomba biótica la que alimenta las lluvias que colman los embalses hidroeléctricos y riegan los campos de cultivo más productivos de Argentina, Paraguay, Uruguay y el sur brasileño. Por consiguiente, talar la floresta no supone únicamente empobrecer a las comunidades ribereñas locales, sino secar las fuentes de agua y los alimentos de cientos de millones de latinoamericanos que dependen indirectamente del aliento vegetal de la floresta."
            },
            {
                "type": "narration",
                "text": "En los enclaves fluviales como el Trapecio Amazónico —donde las ciudades hermanas de Leticia en Colombia, Tabatinga en Brasil y Santa Rosa en Perú conviven en una simbiosis cotidiana pacífica y abierta—, la vecindad porosa demuestra que los ríos son arterias fraternas de integración cultural. Pueblos originarios milenarios como los Ticunas y los Yanomamis custodian sus territorios binacionales con heroica dignidad, haciendo frente a los embates devastadores de la minería ilegal de oro y al envenenamiento criminal de los caudales con mercurio. Con todo, la defensa inquebrantable de sus saberes etnobotánicos y la consolidación de cooperativas de bioeconomía basadas en el açaí, el camu-camu y la castaña demuestran que el aprovechamiento sostenible del bosque en pie es infinitamente más próspero que el extractivismo voraz. Por consiguiente, los guardaparques binacionales y los monitores indígenas de ribera articulan brigadas mixtas de vigilancia para salvaguardar las reservas de biosfera, protegiendo tanto los sitios sagrados de las etnias originarias como las cabeceras de cuenca indispensables para el abastecimiento de agua dulce."
            },
            {
                "type": "narration",
                "text": "En conclusión, la Amazonía Pancontinental enseña al mundo entero que el porvenir de la civilización humana depende de nuestra capacidad ética para armonizar el conocimiento científico de vanguardia con la sabiduría sagrada de los pueblos ancestrales que habitan la selva virgen. Proteger la integridad de la cuenca compartida no es una concesión retórica ni un lujo conservacionista descartable, sino la garantía ineludible de continuidad para la vida sobre nuestro planeta. Al asumir unidos este mandato histórico imperecedero, los pueblos del continente afirman con orgullo que en la floresta viva palpita la promesa más bella de un futuro solidario, justo y fraterno para toda la humanidad."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuántas naciones soberanas integran la cuenca amazónica representada en la OTCA?",
                        "options": [
                            "Tres naciones andinas exclusivamente.",
                            "Ocho naciones: Bolivia, Brasil, Colombia, Ecuador, Guyana, Perú, Surinam y Venezuela.",
                            "Dieciocho naciones de todo el continente americano.",
                            "Dos países costeros del océano Atlántico."
                        ],
                        "correctIndex": 1,
                        "explanation": "La cuenca amazónica está compartida por ocho países soberanos articulados institucionalmente en la OTCA."
                    },
                    {
                        "question": "¿Cómo influyen los 'ríos voladores' amazónicos en la economía del cono sur de Sudamérica?",
                        "options": [
                            "Permiten el tráfico de barcos pesados entre los puertos del Pacífico.",
                            "Transportan inmensas masas aéreas de humedad que generan las lluvias necesarias para la agricultura y la hidroelectricidad del sur.",
                            "Enfrían las turbinas de gas en las refinerías petroleras.",
                            "Impiden la formación de vientos en el océano Atlántico."
                        ],
                        "correctIndex": 1,
                        "explanation": "La transpiración selvática genera lluvias cruciales para la agricultura y energía del centro y sur de Sudamérica."
                    },
                    {
                        "question": "¿Qué alternativa sostenible defiende el paradigma de la 'bioeconomía del bosque en pie'?",
                        "options": [
                            "Talar toda la madera para convertir la selva en una zona de pastizales ganaderos.",
                            "Aprovechar los productos forestales no maderables y el conocimiento biotecnológico manteniendo la selva viva e intacta.",
                            "Desecar los ríos fronterizos para construir autopistas de peaje.",
                            "Expulsar a las comunidades indígenas hacia las ciudades costeras."
                        ],
                        "correctIndex": 1,
                        "explanation": "La bioeconomía demuestra que la selva viva genera prosperidad comunitaria y farmacológica superior a la deforestación."
                    }
                ]
            }
        }
    }
}

EXERCISES_DATA = {
    "b2-32-01": [
        {
            "id": "b2-32-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["concesivas-intensivas-cuantificadas"],
            "question": "¿Qué modo verbal exige la locución 'por más que' cuando expresa una dificultad hipotética o proyectada al futuro?",
            "options": [
                "Modo indicativo",
                "Modo subjuntivo",
                "Modo imperativo",
                "Infinitivo simple"
            ],
            "correct": 1
        },
        {
            "id": "b2-32-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["concesivas-intensivas-cuantificadas"],
            "sentence": "Por __ que insistan los compradores, no venderemos las tierras comunitarias.",
            "answer": "mucho",
            "english": "However much the buyers insist, we will not sell the community lands."
        },
        {
            "id": "b2-32-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-32-01-vocab"],
            "pairs": [
                ["por más que", "no matter how much"],
                ["tenacidad", "tenacity"],
                ["indómito", "untamed"],
                ["arduo", "arduous"]
            ]
        },
        {
            "id": "b2-32-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué matiz pragmático aporta la estructura 'por muy + adjetivo + que + subjuntivo'?",
            "options": [
                "Pondera una cualidad en grado extremo declarándola incapaz de frustrar la acción principal.",
                "Niega que la cualidad haya existido alguna vez.",
                "Indica una duda absoluta sobre el sujeto del predicado.",
                "Expresa el resultado final de un cálculo matemático."
            ],
            "correct": 0
        }
    ],
    "b2-32-02": [
        {
            "id": "b2-32-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["concesivas-riesgo-contingencia"],
            "question": "¿Cuál es el régimen verbal normativo de la locución concesiva 'aun a riesgo de que'?",
            "options": [
                "Modo indicativo obligatorio.",
                "Modo subjuntivo obligatorio, al expresar contingencia o peligro no consumado.",
                "Condicional compuesto exclusivamente.",
                "Gerundio compuesto."
            ],
            "correct": 1
        },
        {
            "id": "b2-32-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["concesivas-riesgo-contingencia"],
            "sentence": "Los expedicionarios cruzaron el caudal, aun a riesgo de que la corriente __ la embarcación.",
            "answer": "volcara",
            "english": "The expedition members crossed the river, even at the risk of the current overturning the vessel."
        },
        {
            "id": "b2-32-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-32-02-vocab"],
            "pairs": [
                ["aun a riesgo de que", "even at the risk of"],
                ["contingencia", "contingency"],
                ["temeridad", "recklessness"],
                ["intrépido", "intrepid"]
            ]
        },
        {
            "id": "b2-32-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿En qué se diferencia 'con todo y que' de 'aun a riesgo de que'?",
            "options": [
                "'Con todo y que' constata un obstáculo fáctico real, admitiendo comúnmente el indicativo.",
                "'Con todo y que' solo se usa en el lenguaje epistolar diplomático.",
                "'Con todo y que' exige imperativo en la prótasis.",
                "'Con todo y que' es un anglicismo recién introducido."
            ],
            "correct": 0
        }
    ],
    "b2-32-03": [
        {
            "id": "b2-32-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["concesivas-redundantes-duplicadas"],
            "question": "¿Qué caracteriza a las concesivas reduplicadas como 'haga lo que haga' o 'cueste lo que cueste'?",
            "options": [
                "La repetición del mismo verbo en modo subjuntivo unido por un relativo indefinido para expresar determinación absoluta.",
                "El uso exclusivo de verbos impersonales en pasado.",
                "La obligación de colocar una negación doble.",
                "La necesidad de conjugar el verbo en futuro de subjuntivo."
            ],
            "correct": 0
        },
        {
            "id": "b2-32-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["concesivas-redundantes-duplicadas"],
            "sentence": "Pase lo que __, los delegados defenderán la intangibilidad del territorio ancestral.",
            "answer": "pase",
            "english": "Come what may, the delegates will defend the inviolability of ancestral territory."
        },
        {
            "id": "b2-32-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-32-03-vocab"],
            "pairs": [
                ["cueste lo que cueste", "whatever it takes"],
                ["pase lo que pase", "come what may"],
                ["resolución", "resolve"],
                ["inquebrantable", "unshakeable"]
            ]
        },
        {
            "id": "b2-32-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué tiempo verbal asume la reduplicación concesiva en relatos ambientados en el pasado?",
            "options": [
                "Pretérito perfecto compuesto de indicativo.",
                "Pretérito imperfecto de subjuntivo (por ejemplo: 'dijera lo que dijera').",
                "Infinitivo simple exclusivamente.",
                "Condicional compuesto."
            ],
            "correct": 1
        }
    ],
    "b2-32-04": [
        {
            "id": "b2-32-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["modales-correlativas-avanzadas"],
            "question": "¿Cuál de las siguientes locuciones prepositivas de registro formal equivale a 'conforme a' o 'de acuerdo con'?",
            "options": [
                "A tenor de",
                "Por si acaso",
                "De cara a",
                "A expensas de"
            ],
            "correct": 0
        },
        {
            "id": "b2-32-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["modales-correlativas-avanzadas"],
            "sentence": "Los guardaparques actuaron con __ a las directrices vigentes de la fiscalía ambiental.",
            "answer": "arreglo",
            "english": "The park rangers acted pursuant to the prevailing guidelines of the environmental prosecution office."
        },
        {
            "id": "b2-32-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-32-04-vocab"],
            "pairs": [
                ["a tenor de", "in accordance with"],
                ["con arreglo a", "pursuant to"],
                ["estatuto", "statute"],
                ["dictamen", "ruling / opinion"]
            ]
        },
        {
            "id": "b2-32-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿En qué textos es especialmente idóneo el empleo de 'según y conforme'?",
            "options": [
                "En textos jurídicos, protocolarios y administrativos de alta prestancia.",
                "En mensajes publicitarios para niños.",
                "En recetarios de cocina rápida.",
                "En cómics humorísticos juveniles."
            ],
            "correct": 0
        }
    ],
    "b2-32-05": [
        {
            "id": "b2-32-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["modales-hipoteticas-comparativas"],
            "question": "¿Qué tiempo verbal debe usarse obligatoriamente tras la locución comparativa irreal 'como si'?",
            "options": [
                "Presente de subjuntivo",
                "Pretérito imperfecto o pluscuamperfecto de subjuntivo",
                "Futuro de indicativo",
                "Presente de indicativo"
            ],
            "correct": 1
        },
        {
            "id": "b2-32-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["modales-hipoteticas-comparativas"],
            "sentence": "El río rugía en la espesura cual __ fuera una bestia mítica acechando en las sombras.",
            "answer": "si",
            "english": "The river roared in the thickness as though it were a mythical beast lurking in the shadows."
        },
        {
            "id": "b2-32-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["b2-32-05-vocab"],
            "pairs": [
                ["como si", "as if"],
                ["cual si", "as though"],
                ["ilusorio", "illusory"],
                ["espejismo", "mirage"]
            ]
        },
        {
            "id": "b2-32-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Por qué es incorrecto decir en español culto '*habla como si sepa la verdad*'?",
            "options": [
                "Porque 'como si' exige siempre tiempos de subjuntivo del eje del pasado ('supiera' o 'hubiera sabido') al denotar irrealidad o simulación.",
                "Porque el verbo saber no tiene subjuntivo.",
                "Porque 'como si' solo puede ir con indicativo.",
                "Porque debe llevar la preposición de delante."
            ],
            "correct": 0
        }
    ],
    "b2-32-consolidation": [
        {
            "id": "b2-32-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["concesivas-intensivas-cuantificadas"],
            "question": "Selecciona la oración redactada con pulcritud normativa concesiva intensiva:",
            "options": [
                "Por más que reclaman, nadie los escucha nunca.",
                "Por más que reclamen los infractores, la sanción ambiental será ratificada.",
                "Por más qué reclamen los infractores, la multa sigue en pie.",
                "Por más de que reclamen, no cambiará la norma."
            ],
            "correct": 1
        },
        {
            "id": "b2-32-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["modales-hipoteticas-comparativas"],
            "question": "¿Qué oración contiene una cláusula modal hipotética correctamente formulada?",
            "options": [
                "Caminaba por la trocha como si no tuviera miedo a las fieras.",
                "Caminaba por la trocha como si no tiene miedo a las fieras.",
                "Caminaba por la trocha como si no tenga miedo a las fieras.",
                "Caminaba por la trocha como si no tendrá miedo a las fieras."
            ],
            "correct": 0
        },
        {
            "id": "b2-32-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["concesivas-redundantes-duplicadas"],
            "sentence": "Haga lo que __ la compañía maderera, la comunidad no abandonará sus tierras ancestrales.",
            "answer": "haga",
            "english": "Whatever the timber company does, the community will not abandon its ancestral lands."
        },
        {
            "id": "b2-32-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es el tema ontológico central de la novela 'Canaima' de Rómulo Gallegos?",
            "options": [
                "La vida apacible de los pescadores caribeños.",
                "El duelo entre la voluntad humana indómita y la fuerza arrolladora y salvaje de la selva virgen.",
                "La construcción del ferrocarril en los valles del café.",
                "La emigración europea hacia las estancias pampeanas."
            ],
            "correct": 1
        }
    ],
    "b2-amazoniapan-01": [
        {
            "id": "b2-amazoniapan-01.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["amazonia-oraciones-finales-institucionales"],
            "question": "¿Qué locución final de registro diplomático institucional rige modo subjuntivo?",
            "options": [
                "En aras de que",
                "A causa de",
                "Gracias a que",
                "Dado que"
            ],
            "correct": 0
        },
        {
            "id": "b2-amazoniapan-01.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["amazonia-oraciones-finales-institucionales"],
            "sentence": "Se creó el comité binacional a __ de que los guardaparques coordinen patrullajes conjuntos.",
            "answer": "efectos",
            "english": "The binational committee was created with the aim that park rangers coordinate joint patrols."
        },
        {
            "id": "b2-amazoniapan-01.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["amazonia-pan-01-vocab"],
            "pairs": [
                ["en aras de", "for the sake of"],
                ["a efectos de que", "with the aim that"],
                ["multilateral", "multilateral"],
                ["ratificar", "to ratify"]
            ]
        },
        {
            "id": "b2-amazoniapan-01.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es la sede permanente de la Secretaría de la OTCA (Organización del Tratado de Cooperación Amazónica)?",
            "options": [
                "Leticia",
                "Brasilia",
                "Iquitos",
                "Georgetown"
            ],
            "correct": 1
        }
    ],
    "b2-amazoniapan-02": [
        {
            "id": "b2-amazoniapan-02.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["amazonia-relativas-locativas-complejas"],
            "question": "¿Qué nexo relativo locativo compuesto introduce una ubicación indeterminada rigiendo subjuntivo?",
            "options": [
                "Allí donde",
                "Adondequiera que",
                "En donde",
                "Desde donde"
            ],
            "correct": 1
        },
        {
            "id": "b2-amazoniapan-02.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["amazonia-relativas-locativas-complejas"],
            "sentence": "Adondequiera que __ los cazadores nómadas, reconocen los árboles sagrados de su linaje.",
            "answer": "viajen",
            "english": "Wherever the nomadic hunters travel, they recognize the sacred trees of their lineage."
        },
        {
            "id": "b2-amazoniapan-02.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["amazonia-pan-02-vocab"],
            "pairs": [
                ["adondequiera que", "wherever"],
                ["poroso", "porous"],
                ["transfronterizo", "cross-border"],
                ["territorialidad", "territoriality"]
            ]
        },
        {
            "id": "b2-amazoniapan-02.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué ciudades forman la triple frontera fluvial en el Trapecio Amazónico?",
            "options": [
                "Leticia, Tabatinga y Santa Rosa de Yavarí.",
                "Manaus, Santarém y Belém.",
                "Puerto Maldonado, Cobija y Guayaramerín.",
                "Mitú, San Gabriel da Cachoeira y Maroa."
            ],
            "correct": 0
        }
    ],
    "b2-amazoniapan-03": [
        {
            "id": "b2-amazoniapan-03.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["amazonia-causales-explicativas-continuativas"],
            "question": "¿Cuál de las siguientes locuciones causales explicativas continuativas es propia de informes científicos?",
            "options": [
                "Habida cuenta de que",
                "Porque sí",
                "Es que",
                "A ver si"
            ],
            "correct": 0
        },
        {
            "id": "b2-amazoniapan-03.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["amazonia-causales-explicativas-continuativas"],
            "sentence": "Se debe proteger la cabecera andina, por __ allí se originan los sedimentos vitales del río.",
            "answer": "cuanto",
            "english": "The Andean headwaters must be protected, inasmuch as the river's vital sediments originate there."
        },
        {
            "id": "b2-amazoniapan-03.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["amazonia-pan-03-vocab"],
            "pairs": [
                ["habida cuenta de que", "taking into account that"],
                ["por cuanto", "inasmuch as"],
                ["evapotranspiración", "evapotranspiration"],
                ["caudal", "river flow / discharge"]
            ]
        },
        {
            "id": "b2-amazoniapan-03.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Hacia dónde desvía la cordillera de los Andes las masas de vapor de los ríos voladores amazónicos?",
            "options": [
                "Hacia el océano Ártico.",
                "Hacia el sur, regando las regiones agrícolas de la cuenca del Plata.",
                "Hacia el desierto de Atacama en Chile.",
                "Hacia las islas Galápagos."
            ],
            "correct": 1
        }
    ],
    "b2-amazoniapan-04": [
        {
            "id": "b2-amazoniapan-04.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["amazonia-perifrasis-probabilidad-retrospectiva"],
            "question": "¿Qué construcción modal formula una conjetura o hipótesis retrospectiva sobre el pasado?",
            "options": [
                "Deber de haber + participio",
                "Tener que + infinitivo",
                "Haber de + infinitivo",
                "Estar por + infinitivo"
            ],
            "correct": 0
        },
        {
            "id": "b2-amazoniapan-04.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["amazonia-perifrasis-probabilidad-retrospectiva"],
            "sentence": "Las dragas clandestinas deben de __ operado durante semanas en el lecho del río Caquetá.",
            "answer": "haber",
            "english": "The illegal dredging operations must have operated for weeks in the Caquetá riverbed."
        },
        {
            "id": "b2-amazoniapan-04.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["amazonia-pan-04-vocab"],
            "pairs": [
                ["deber de haber", "must have"],
                ["mercurio", "mercury"],
                ["dragado", "dredging"],
                ["impunidad", "impunity"]
            ]
        },
        {
            "id": "b2-amazoniapan-04.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Cuál es la consecuencia más grave del mercurio vertido por la minería ilegal en las cuencas fluviales?",
            "options": [
                "La bioacumulación de metilmercurio en los peces y graves afecciones neurológicas en las poblaciones humanas.",
                "La disminución de la velocidad del viento en la copa de los árboles.",
                "El teñido de las aguas de color azul brillante.",
                "La cristalización de las rocas graníticas del lecho."
            ],
            "correct": 0
        }
    ],
    "b2-amazoniapan-05": [
        {
            "id": "b2-amazoniapan-05.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["amazonia-condicionales-mixtas-complejas"],
            "question": "¿Qué combinación temporal caracteriza a las condicionales mixtas complejas en análisis prospectivo?",
            "options": [
                "Condición en pasado (pluscuamperfecto de subjuntivo) y consecuencia en presente (condicional simple).",
                "Presente de indicativo y futuro imperfecto.",
                "Pretérito perfecto de subjuntivo e imperativo afirmativo.",
                "Dos verbos conjugados en copretérito de indicativo."
            ],
            "correct": 0
        },
        {
            "id": "b2-amazoniapan-05.ex02",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["amazonia-condicionales-mixtas-complejas"],
            "sentence": "De haber protegido la farmacopea ancestral hace décadas, hoy la región __ la biotecnología médica global.",
            "answer": "lideraría",
            "english": "Had ancestral pharmacopeia been protected decades ago, today the region would lead global medical biotechnology."
        },
        {
            "id": "b2-amazoniapan-05.ex03",
            "type": "matching",
            "category": "vocabulary",
            "teaches": ["amazonia-pan-05-vocab"],
            "pairs": [
                ["farmacopea", "pharmacopeia"],
                ["biopiratería", "biopiracy"],
                ["regenerativo", "regenerative"],
                ["ancestral", "ancestral"]
            ]
        },
        {
            "id": "b2-amazoniapan-05.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué tratado internacional protege a las comunidades indígenas contra la biopiratería de sus recursos genéticos?",
            "options": [
                "El Protocolo de Nagoya",
                "El Tratado de Versalles",
                "El Pacto de Varsovia",
                "La Carta de Jamaica"
            ],
            "correct": 0
        }
    ],
    "b2-amazoniapan-consolidation": [
        {
            "id": "b2-amazoniapan-consolidation.ex01",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["amazonia-oraciones-finales-institucionales"],
            "question": "Identifica la oración con locución final diplomática institucional correcta:",
            "options": [
                "Firmaron el protocolo en aras de que se garantice la intangibilidad del bosque.",
                "Firmaron el protocolo a causa de que se garantice la intangibilidad del bosque.",
                "Firmaron el protocolo gracias a que se garantice la intangibilidad del bosque.",
                "Firmaron el protocolo según que se garantice la intangibilidad del bosque."
            ],
            "correct": 0
        },
        {
            "id": "b2-amazoniapan-consolidation.ex02",
            "type": "multiple-choice",
            "category": "grammar",
            "teaches": ["amazonia-condicionales-mixtas-complejas"],
            "question": "¿Cuál es la estructura condicional mixta que vincula una hipótesis pasada con una situación actual?",
            "options": [
                "De haber frenado la deforestación en el siglo pasado, no padeceríamos ahora estas sequías.",
                "Si frenamos la deforestación, no padeceremos sequías.",
                "Si frenábamos la deforestación, no padecíamos sequías.",
                "Como frenamos la deforestación, no padecemos sequías."
            ],
            "correct": 0
        },
        {
            "id": "b2-amazoniapan-consolidation.ex03",
            "type": "fill-blank",
            "category": "grammar",
            "teaches": ["amazonia-relativas-locativas-complejas"],
            "sentence": "Adondequiera que __ las brigadas de guardaparques, encuentran vestigios de campamentos taladores.",
            "answer": "vayan",
            "english": "Wherever the park ranger squads go, they find traces of logging camps."
        },
        {
            "id": "b2-amazoniapan-consolidation.ex04",
            "type": "multiple-choice",
            "category": "reading",
            "question": "¿Qué síntesis ecológica consagra a la Amazonía como patrimonio continental indivisible?",
            "options": [
                "La extracción ilimitada de hidrocarburos pesados en el delta.",
                "La integración de la cuenca hídrica, la interdependencia de los ríos voladores y el liderazgo de los pueblos ancestrales en la bioeconomía.",
                "La canalización artificial de todos los ríos para regar plantaciones costeras.",
                "El abandono de los compromisos multilaterales en favor de la deforestación masiva."
            ],
            "correct": 1
        }
    ]
}

GRAMMAR_SKILL_MAP = {
    "b2-32-01-a": "concesivas-intensivas-cuantificadas",
    "b2-32-02-a": "concesivas-riesgo-contingencia",
    "b2-32-03-a": "concesivas-redundantes-duplicadas",
    "b2-32-04-a": "modales-correlativas-avanzadas",
    "b2-32-05-a": "modales-hipoteticas-comparativas",
    "b2-amazoniapan-01-a": "amazonia-oraciones-finales-institucionales",
    "b2-amazoniapan-02-a": "amazonia-relativas-locativas-complejas",
    "b2-amazoniapan-03-a": "amazonia-causales-explicativas-continuativas",
    "b2-amazoniapan-04-a": "amazonia-perifrasis-probabilidad-retrospectiva",
    "b2-amazoniapan-05-a": "amazonia-condicionales-mixtas-complejas",
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
    # Core Unit 32 lessons
    core_lessons = [
        ("b2-32-01", "Concesivas intensivas cuantificadas", "1"),
        ("b2-32-02", "Concesivas de riesgo y contingencia", "2"),
        ("b2-32-03", "Concesivas reduplicativas y de indiferencia", "3"),
        ("b2-32-04", "Subordinadas modales correlativas avanzadas", "4"),
        ("b2-32-05", "Subordinadas modales hipotéticas con subjuntivo", "5"),
    ]
    for stem, title, num in core_lessons:
        doc = {
            "id": f"lesson.b2.32.0{num}",
            "title": title,
            "level": "B2",
            "sections": [
                {
                    "type": "story",
                    "ref": "stories/classics/b2/b2-32.json"
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
    con_stem = "b2-32-consolidation"
    doc_con = {
        "id": "lesson.b2.32.consolidation",
        "title": "Consolidation: Advanced Concessive & Manner Clauses",
        "level": "B2",
        "sections": [
            {
                "type": "story",
                "ref": "stories/classics/b2/b2-32.json"
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

    # Regional Amazonía Pancontinental lessons
    reg_lessons = [
        ("b2-amazoniapan-01", "La cuenca de las ocho naciones: La OTCA y la Declaración de Belém", "1"),
        ("b2-amazoniapan-02", "Pueblos transfronterizos y naciones sin fronteras: El trapecio amazónico", "2"),
        ("b2-amazoniapan-03", "Ríos voladores y el pulso hidrológico continental", "3"),
        ("b2-amazoniapan-04", "Minería ilegal, mercurio y la defensa de las cuencas binacionales", "4"),
        ("b2-amazoniapan-05", "Bioeconomía y farmacopea del bosque en pie: El futuro regenerativo", "5")
    ]
    for stem, title, num in reg_lessons:
        doc = {
            "id": f"lesson.b2.amazoniapan.0{num}",
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
    reg_con_stem = "b2-amazoniapan-consolidation"
    doc_reg_con = {
        "id": "lesson.b2.amazoniapan.consolidation",
        "title": "Consolidación: La selva indivisible: El corazón biológico de la Patria Grande",
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
    
    core_stems = [f"b2-32-0{i}" for i in range(1, 6)] + ["b2-32-consolidation"]
    reg_stems = [f"b2-amazoniapan-0{i}" for i in range(1, 6)] + ["b2-amazoniapan-consolidation"]

    if "b2-32-01" not in existing_stems:
        units_list.append({
            "title": "Subordinación adverbial I: Concesivas avanzadas y modales",
            "stems": core_stems,
            "track": "core"
        })
    if "b2-amazoniapan-01" not in existing_stems:
        units_list.append({
            "title": "Amazonía Pancontinental: La cuenca compartida y el bioma sin fronteras",
            "stems": reg_stems,
            "track": "regional"
        })

    with open(path, "w", encoding="utf-8") as f:
        json.dump(units_list, f, ensure_ascii=False, indent=2)
    print("Updated curriculum/units/b2.json with Unit 32!")

def main():
    update_skill_registry()
    update_grammar_titles()
    generate_vocab_files()
    generate_grammar_files()
    generate_stories()
    generate_exercises()
    generate_lessons()
    update_curriculum_units()
    print("Unit 32 generation complete!")

if __name__ == "__main__":
    main()
