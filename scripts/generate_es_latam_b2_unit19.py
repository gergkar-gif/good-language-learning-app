#!/usr/bin/env python3
"""
Generate Latin American Spanish (es-latam) B2 Unit 19:
- Core Unit 19: The Passive with 'Se' (La pasiva refleja y sus límites)
  Classic literature: Mario Vargas Llosa - La ciudad y los perros (1963)
- Regional Unit 19: Peru II: The Pacific Coast, Lima & The Gastronomic Vanguard (b2-perucosta)
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
    c_unit = "b2-19"
    r_unit = "b2-perucosta"

    c1, c2, c3, c4, c5, l6_con = [f"{c_unit}-0{i}" for i in range(1, 6)] + [f"{c_unit}-consolidation"]
    r1, r2, r3, r4, r5, r6_con = [f"{r_unit}-0{i}" for i in range(1, 6)] + [f"{r_unit}-consolidation"]

    # -------------------------------------------------------------------------
    # 0. UPDATE REGISTRY & GRAMMAR TITLES
    # -------------------------------------------------------------------------
    reg_path = LATAM_DIR / "indexes" / "skill-registry.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    skills = registry.setdefault("skills", {})

    new_skills = {
        "b2-19-vocab": {"kind": "vocabulary", "level": "B2"},
        "pasiva-refleja-concordancia": {"kind": "grammar", "level": "B2"},
        "se-pasivo-vs-impersonal": {"kind": "grammar", "level": "B2"},
        "pasiva-refleja-restricciones-agente": {"kind": "grammar", "level": "B2"},
        "se-institucional-juridico": {"kind": "grammar", "level": "B2"},
        "desambiguacion-valores-se": {"kind": "grammar", "level": "B2"},
        "sintesis-pasiva-refleja": {"kind": "grammar", "level": "B2"},
        "b2-perucosta-vocab": {"kind": "vocabulary", "level": "B2"},
        "peru-costa-corriente-humboldt": {"kind": "grammar", "level": "B2"},
        "peru-lima-virreinal-balcones": {"kind": "grammar", "level": "B2"},
        "peru-afroperuano-chincha-cajon": {"kind": "grammar", "level": "B2"},
        "peru-gastronomia-nikkei-chifa": {"kind": "grammar", "level": "B2"},
        "peru-iquitos-caucho-amazonia": {"kind": "grammar", "level": "B2"},
        "peru-costa-sintesis-regional": {"kind": "grammar", "level": "B2"}
    }

    for k, v in new_skills.items():
        skills[k] = v

    reg_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated skill-registry.json for Unit 19")

    gt_path = LATAM_DIR / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))

    new_titles = {
        "pasiva-refleja-concordancia": "passive reflex constructions with singular and plural agreement",
        "se-pasivo-vs-impersonal": "distinguishing reflexive passive from impersonal se constructions",
        "pasiva-refleja-restricciones-agente": "semantic constraints and agent omission in reflexive passives",
        "se-institucional-juridico": "impersonal se in formal juridical and institutional registers",
        "desambiguacion-valores-se": "pragmatic disambiguation of reflexive reciprocal and passive se",
        "sintesis-pasiva-refleja": "synthesis of reflexive passive and impersonal se structures",
        "peru-costa-corriente-humboldt": "humboldt marine current and coastal desert ecology in peru",
        "peru-lima-virreinal-balcones": "viceregal architecture and latticed balconies of colonial lima",
        "peru-afroperuano-chincha-cajon": "afro-peruvian cultural heritage and cajon percussion rhythms",
        "peru-gastronomia-nikkei-chifa": "peruvian culinary diplomacy and chifa and nikkei fusion traditions",
        "peru-iquitos-caucho-amazonia": "iquitos rubber boom history and peruvian amazon waterways",
        "peru-costa-sintesis-regional": "synthesis of coastal peruvian history gastronomy and geography"
    }

    for k, v in new_titles.items():
        gt[k] = v

    gt_path.write_text(json.dumps(gt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json for Unit 19")

    # -------------------------------------------------------------------------
    # 1. VOCABULARY FILES (5 Core + 5 Regional)
    # -------------------------------------------------------------------------
    core_vocabs = [
        (c1, "b2-19-01-voc", "La concordancia en la pasiva refleja", [
            {"lemma": "acuerdo", "translation": "agreement / formal treaty", "pos": "noun"},
            {"lemma": "estipulación", "translation": "stipulation / contractual term", "pos": "noun"},
            {"lemma": "promulgar", "translation": "to promulgate / to enact officially", "pos": "verb"},
            {"lemma": "disponer", "translation": "to dispose / to decree", "pos": "verb"},
            {"lemma": "concordante", "translation": "concordant / in grammatical agreement", "pos": "adjective"},
            {"lemma": "paciente", "translation": "patient / receiver of action in passive", "pos": "adjective"}
        ]),
        (c2, "b2-19-02-voc", "Pasiva refleja frente a impersonal con se", [
            {"lemma": "damnificado", "translation": "victim / casualty / affected person", "pos": "noun"},
            {"lemma": "postulante", "translation": "applicant / candidate", "pos": "noun"},
            {"lemma": "atender", "translation": "to assist / to attend to", "pos": "verb"},
            {"lemma": "condecorar", "translation": "to decorate / to award honors to", "pos": "verb"},
            {"lemma": "indiferenciado", "translation": "undifferentiated / generalized", "pos": "adjective"},
            {"lemma": "animado", "translation": "animate / human referent", "pos": "adjective"}
        ]),
        (c3, "b2-19-03-voc", "Agentividad implícita y restricciones de agente", [
            {"lemma": "agente", "translation": "agent / initiator of action", "pos": "noun"},
            {"lemma": "omisión", "translation": "omission / deliberate withholding", "pos": "noun"},
            {"lemma": "vetar", "translation": "to veto / to prohibit officially", "pos": "verb"},
            {"lemma": "demoler", "translation": "to demolish / to tear down", "pos": "verb"},
            {"lemma": "incompatible", "translation": "incompatible / grammatically discordant", "pos": "adjective"},
            {"lemma": "tácito", "translation": "tacit / implicit", "pos": "adjective"}
        ]),
        (c4, "b2-19-04-voc", "El se institucional y jurídico", [
            {"lemma": "decreto", "translation": "decree / executive order", "pos": "noun"},
            {"lemma": "resolución", "translation": "resolution / judicial ruling", "pos": "noun"},
            {"lemma": "notificar", "translation": "to serve notice / to notify formally", "pos": "verb"},
            {"lemma": "sancionar", "translation": "to enact / to sanction legally", "pos": "verb"},
            {"lemma": "vinculante", "translation": "binding / legally enforceable", "pos": "adjective"},
            {"lemma": "fehaciente", "translation": "irrefutable / providing authentic proof", "pos": "adjective"}
        ]),
        (c5, "b2-19-05-voc", "Desambiguación de los valores de se", [
            {"lemma": "ambigüedad", "translation": "ambiguity / dual interpretation", "pos": "noun"},
            {"lemma": "reciprocidad", "translation": "reciprocity / mutual action", "pos": "noun"},
            {"lemma": "difundir", "translation": "to broadcast / to disseminate widely", "pos": "verb"},
            {"lemma": "interceptar", "translation": "to intercept / to stop mid-transit", "pos": "verb"},
            {"lemma": "equívoco", "translation": "misleading / ambiguous", "pos": "adjective"},
            {"lemma": "reflejo", "translation": "reflexive / mirrored", "pos": "adjective"}
        ])
    ]

    for stem, vid, vtitle, words in core_vocabs:
        write_json(f"vocabulary/b2/{vid}.json", {
            "id": f"vocab.b2.19.{stem[-2:]}",
            "lesson": stem,
            "title": vtitle,
            "theme": "the passive with se and formal impersonality",
            "words": words
        })

    reg_vocabs = [
        (r1, "b2-perucosta-01-voc", "El desierto costero y la corriente de Humboldt", [
            {"lemma": "afloramiento", "translation": "upwelling of deep nutrient-rich water", "pos": "noun"},
            {"lemma": "garúa", "translation": "dense coastal fog and drizzle of Lima", "pos": "noun"},
            {"lemma": "anchoveta", "translation": "Peruvian anchoveta fish species", "pos": "noun"},
            {"lemma": "cardumen", "translation": "shoal / dense school of fish", "pos": "noun"},
            {"lemma": "árido", "translation": "hyper-arid / waterless", "pos": "adjective"},
            {"lemma": "litoral", "translation": "coastal / littoral marine zone", "pos": "adjective"}
        ]),
        (r2, "b2-perucosta-02-voc", "Lima virreinal y los balcones de celosía", [
            {"lemma": "celosía", "translation": "wooden lattice balcony screen", "pos": "noun"},
            {"lemma": "virreinato", "translation": "viceroyalty / colonial administrative territory", "pos": "noun"},
            {"lemma": "palaciego", "translation": "palatial / stately viceregal", "pos": "adjective"},
            {"lemma": "señorío", "translation": "nobility / stately aristocratic elegance", "pos": "noun"},
            {"lemma": "enrejar", "translation": "to enclose with latticework or iron grilles", "pos": "verb"},
            {"lemma": "conventual", "translation": "conventual / relating to monasteries", "pos": "adjective"}
        ]),
        (r3, "b2-perucosta-03-voc", "La herencia afroperuana de Chincha y el cajón", [
            {"lemma": "cajón", "translation": "box drum instrument invented by Afro-Peruvians", "pos": "noun"},
            {"lemma": "décima", "translation": "ten-line poetic stanza sung or recited", "pos": "noun"},
            {"lemma": "zapateo", "translation": "rhythmic tap footwork of Afro-Peruvian dance", "pos": "noun"},
            {"lemma": "festejo", "translation": "joyous celebratory Afro-Peruvian musical genre", "pos": "noun"},
            {"lemma": "sincopado", "translation": "syncopated / complex rhythmic off-beat", "pos": "adjective"},
            {"lemma": "cimarrón", "translation": "runaway enslaved person / freedom fighter", "pos": "noun"}
        ]),
        (r4, "b2-perucosta-04-voc", "La revolución gastronómica y las fusiones nikkei y chifa", [
            {"lemma": "cebiche", "translation": "raw fish cured in fresh lime juice and chili", "pos": "noun"},
            {"lemma": "tiradito", "translation": "sashimi-style raw fish without raw onion", "pos": "noun"},
            {"lemma": "chifa", "translation": "Cantonese-Peruvian culinary fusion tradition", "pos": "noun"},
            {"lemma": "nikkei", "translation": "Japanese-Peruvian culinary fusion style", "pos": "adjective"},
            {"lemma": "marinar", "translation": "to marinade / to cure fish in citrus acid", "pos": "verb"},
            {"lemma": "biodiversidad", "translation": "biodiversity of ecosystems and native crops", "pos": "noun"}
        ]),
        (r5, "b2-perucosta-05-voc", "Iquitos y el auge cauchero en la Amazonia fluvial", [
            {"lemma": "caucho", "translation": "natural rubber latex extracted from trees", "pos": "noun"},
            {"lemma": "embarcación", "translation": "river vessel / boat navigate Amazon waters", "pos": "noun"},
            {"lemma": "siringuero", "translation": "rubber tapper worker in rainforest", "pos": "noun"},
            {"lemma": "aislamiento", "translation": "geographic isolation without highway access", "pos": "noun"},
            {"lemma": "fluvial", "translation": "fluvial / relating to river systems", "pos": "adjective"},
            {"lemma": "exuberante", "translation": "exuberant / lushly fertile jungle vegetation", "pos": "adjective"}
        ])
    ]

    for stem, vid, vtitle, words in reg_vocabs:
        write_json(f"vocabulary/b2/{vid}.json", {
            "id": f"vocab.b2.perucosta.{stem[-2:]}",
            "lesson": stem,
            "title": vtitle,
            "theme": "peruvian coastal geography history culture and gastronomy",
            "words": words
        })


    # -------------------------------------------------------------------------
    # 2. GRAMMAR FILES (5 Core + 5 Regional, none for consolidation)
    # -------------------------------------------------------------------------
    core_grammars = [
        (c1, "grammar.b2.19.01.pasiva-refleja-concordancia", "Pasiva refleja básica y concordancia de número",
         "La **pasiva refleja** se construye con el pronombre **se** y una forma verbal en tercera persona (singular o plural) que concuerda obligatoriamente con el sujeto paciente pospuesto o antepuesto.\n\nA diferencia de las oraciones activas o impersonales, en la pasiva refleja el elemento nominal no funciona como objeto directo sino como auténtico **sujeto sintáctico**: *Se firmó el acuerdo bilateral* (singular) frente a *Se firmaron los acuerdos de paz* (plural).",
         "Ejemplos de concordancia de número en pasiva refleja",
         [["Se firmó el acuerdo bilateral.", "The bilateral agreement was signed."],
          ["Se firmaron los acuerdos de paz.", "The peace agreements were signed."],
          ["Se clausuró la sesión plenaria.", "The plenary session was adjourned."],
          ["Se clausuraron las sesiones legislativas.", "The legislative sessions were adjourned."],
          ["Se publicó la resolución ministerial.", "The ministerial resolution was published."],
          ["Se publicaron los decretos supremos.", "The supreme decrees were published."]],
         "La concordancia en plural es obligatoria cuando el sujeto paciente es plural: decir *'se firmó los acuerdos'* constituye un error de discordancia en el registro formal escrito."),

        (c2, "grammar.b2.19.02.se-pasivo-vs-impersonal", "Diferenciación: pasiva refleja vs se impersonal",
         "La distinción entre la **pasiva refleja** y la **oración impersonal con se** radica en la naturaleza del argumento verbal y la presencia de la preposición **a**.\n\nCuando el verbo transitivo se refiere a personas determinadas individualizadas mediante la marca acusativa **a**, la construcción es estrictamente **impersonal** y el verbo permanece invariable en tercera persona del singular: *Se atendió a los damnificados*. En cambio, con entidades inanimadas o cosas sin preposición, opera la pasiva refleja con concordancia plural: *Se atendieron los reclamos*.",
         "Contraste entre impersonal con 'a' y pasiva refleja",
         [["Se atendió a los damnificados en el refugio.", "The disaster victims were assisted at the shelter (impersonal)."],
          ["Se atendieron las solicitudes de auxilio.", "The assistance requests were attended to (passive reflex)."],
          ["Se condecoró a las científicas peruanas.", "The Peruvian female scientists were decorated (impersonal)."],
          ["Se condecoraron los méritos académicos.", "The academic merits were decorated (passive reflex)."],
          ["Se examinó a los postulantes.", "The applicants were examined (impersonal)."],
          ["Se examinaron los expedientes de admisión.", "The admission files were examined (passive reflex)."]],
         "Con referentes humanos precedidos de 'a', nunca pluralices el verbo (*'se atendieron a los heridos'* es agramatical en la norma culta panhispánica)."),

        (c3, "grammar.b2.19.03.pasiva-refleja-restricciones-agente", "Restricciones de agentividad en la pasiva refleja",
         "La pasiva refleja presupone siempre la existencia de un **agente humano tácito** que realiza la acción de forma voluntaria, pero su función discursiva primordial es ocultar o desdibujar a ese agente.\n\nPor esa razón, la pasiva refleja rechaza casi sistemáticamente el **complemento agente explícito** introducido por *por*: construcciones como *'??Se cancelaron los vuelos por la aerolínea'* resultan forzadas o incorrectas. Si se desea explicitar el ejecutor, el español prefiere la voz activa (*La aerolínea canceló los vuelos*) o la pasiva analítica (*Los vuelos fueron cancelados por la aerolínea*).",
         "Alternativas para expresar u omitir el agente",
         [["Se demolieron los edificios antiguos.", "The old buildings were demolished (agent omitted, natural)."],
          ["Los edificios fueron demolidos por el municipio.", "The buildings were demolished by the municipality (analytical passive)."],
          ["Se cancelaron las transferencias bancarias.", "The bank transfers were cancelled (natural agentless passive)."],
          ["El banco canceló las transferencias.", "The bank cancelled the transfers (active voice)."],
          ["Se promulgaron tres leyes orgánicas.", "Three organic laws were promulgated (natural legislative passive)."],
          ["El congreso promulgó tres leyes orgánicas.", "Congress promulgated three organic laws (active voice)."]],
         "Utiliza la pasiva refleja cuando el agente sea irrelevante, obvio, desconocido o cuando busques conferir distancia objetiva al enunciado."),

        (c4, "grammar.b2.19.04.se-institucional-juridico", "El se en el discurso administrativo y legal",
         "En el estilo forense, judicial y administrativo, las construcciones con **se** desempeñan un papel central para dotar a las resoluciones, edictos y contratos de un tono de **autoridad despersonalizada e imparcialidad legal**.\n\nFórmulas performativas consagradas como *se resuelve*, *se dispone*, *se ordena* o *se hace constar* transforman la voluntad de magistrados y funcionarios en mandatos objetivos emanados del ordenamiento jurídico del Estado.",
         "Fórmulas consagradas del registro jurídico-institucional",
         [["Se hace constar que el acusado declaró sin coacción.", "It is recorded that the defendant testified without coercion."],
          ["Se resuelve otorgar la personería jurídica solicitada.", "It is resolved to grant the requested legal status."],
          ["Se previene a las partes sobre los plazos procesales.", "The parties are cautioned regarding procedural deadlines."],
          ["Se dispone la publicación inmediata en el diario oficial.", "Immediate publication in the official gazette is ordered."],
          ["Se ordena la apertura del proceso sancionador.", "The opening of the sanctioning process is ordered."],
          ["Se deja constancia en el acta notarial.", "It is placed on record in the notarial act."]],
         "Observa que tras *se dispone* o *se resuelve* puede seguir una proposición sustantiva con *que + subjuntivo* o una cláusula de infinitivo según el carácter preceptivo de la norma."),

        (c5, "grammar.b2.19.05.desambiguacion-valores-se", "Desambiguación pragmática de las funciones de se",
         "El pronombre **se** en español es altamente polisémico: puede desempeñar funciones reflexivas (*se cuida*), recíprocas (*se saludan*), incoativas/pronominales (*se durmió*) o pasivo-impersonales (*se vende*).\n\nPara desambiguar oraciones potencialmente confusas con sujetos plurales animados (*Los ministros se respetan*), el contexto pragmático y el uso de marcadores explícitos (*mutuamente*, *el uno al otro*) resultan decisivos para distinguir la reciprocidad de la voz pasiva.",
         "Desambiguación de los distintos valores sintácticos de 'se'",
         [["Los ministros se saludaron cordialmente.", "The ministers greeted each other (reciprocal reading)."],
          ["Se vendieron todos los boletos del concierto.", "All concert tickets were sold (reflexive passive reading)."],
          ["El candidato se preparó meticulosamente para el debate.", "The candidate prepared himself meticulously (reflexive reading)."],
          ["Se vive con tranquilidad en este valle andino.", "One lives peacefully in this Andean valley (impersonal reading)."],
          ["El tratado se ratificó por unanimidad.", "The treaty was ratified unanimously (reflexive passive reading)."],
          ["Los líderes se comprometieron ante la ciudadanía.", "The leaders committed themselves before the citizenry (pronominal reading)."]],
         "Cuando el sujeto es inanimado plural, la interpretación pasiva refleja es la predominante; con sujetos humanos plurales, la interpretación por defecto suele ser la recíproca.")
    ]

    for stem, gid, title, text_content, tbl_title, rows, tip_content in core_grammars:
        write_json(f"grammar/b2/{stem}-a-gr.json", {
            "id": gid,
            "title": title,
            "sections": [
                {"type": "text", "content": text_content},
                {"type": "table", "title": tbl_title, "rows": rows},
                {"type": "tip", "content": tip_content}
            ]
        })

    reg_grammars = [
        (r1, "grammar.b2.perucosta.01.corriente-humboldt-costa", "La corriente marina de Humboldt y el mar peruano",
         "La **corriente de Humboldt** o corriente del Perú es un flujo oceánico frío de procedencia subantártica que recorre el litoral pacífico suramericano. El fenómeno del **afloramiento costero** eleva nutrientes minerales de las fosas profundas a la superficie, fertilizando una descomunal biomasa marina dominada por la anchoveta.\n\nSimultáneamente, la baja temperatura del agua marina enfría la atmósfera inferior y genera una inversión térmica que suprime las precipitaciones en la costa, creando el árido desierto costero y la persistente niebla invernal limeña llamada **garúa**.",
         "Dinámica oceanográfica y climática de la corriente de Humboldt",
         [["La corriente de Humboldt enfría el litoral peruano.", "The Humboldt Current cools the Peruvian coastline."],
          ["El afloramiento costero eleva nutrientes minerales.", "Coastal upwelling brings up deep mineral nutrients."],
          ["La garúa cubre a Lima durante el invierno austral.", "Dense coastal drizzle covers Lima during the austral winter."],
          ["El desierto costero alberga valles agrícolas fértiles.", "The coastal desert harbors fertile agricultural valleys."],
          ["La anchoveta sustenta la cadena trófica pelágica.", "The anchoveta sustains the pelagic food web."],
          ["Las islas guaneras acumularon fertilizante milenario.", "The guano islands accumulated millennia of fertilizer."]],
         "La inversión térmica impide que el aire húmedo ascienda para formar nubes de tormenta; por ello, la costa peruana registra una de las menores tasas de pluviosidad del planeta."),

        (r2, "grammar.b2.perucosta.02.lima-virreinal-balcones", "Urbanismo virreinal y los balcones de celosía de Lima",
         "Fundada en 1535 por Francisco Pizarro sobre los dominios indígenas del valle del Rímac, Lima se erigió durante casi tres siglos en la fastuosa **Ciudad de los Reyes**, capital política, militar y religiosa del virreinato más opulento de América del Sur.\n\nSu rasgo arquitectónico más emblemático son los **balcones voladizos de celosía** tallados en cedro y roble, de clara filiación mudéjar. Estas celosías permitían a las familias observar las procesiones y el trajín callejero sin ser vistas, y sirvieron de cobijo al fascinante mito social de la **tapada limeña**.",
         "Elementos del urbanismo y la arquitectura virreinal limeña",
         [["Los balcones de celosía adornan el centro limeño.", "Latticed balconies adorn the downtown historic center of Lima."],
          ["La tapada limeña preservaba su anonimato social.", "The tapada limeña preserved her social anonymity with her veil."],
          ["El convento de San Francisco custodia extensas catacumbas.", "The convent of San Francisco holds extensive catacombs."],
          ["La Plaza Mayor fue el epicentro del poder virreinal.", "The Plaza Mayor was the epicenter of viceregal power."],
          ["El damero de Pizarro articuló la traza urbana de la ciudad.", "Pizarro's grid plan articulated the urban layout of the city."],
          ["Santa Rosa de Lima encarnó la mística ascética americana.", "Saint Rose of Lima embodied American ascetic mysticism."]],
         "Los balcones limeños fueron declarados Patrimonio de la Humanidad por la UNESCO como parte integral del Centro Histórico de Lima."),

        (r3, "grammar.b2.perucosta.03.afroperuano-chincha-cajon", "Patrimonio afroperuano: Chincha, el cajón y la décima",
         "Las poblaciones de origen africano introducidas en las haciendas azucareras y algodoneras de la costa central y sur (Chincha, Cañete, Zaña) enriquecieron decisivamente la identidad peruana a través de la resistencia de los **cimarrones** y la creación musical.\n\nPrivados de sus tambores ancestrales, los músicos afroperuanos inventaron el **cajón** a partir de cajas de madera de embalaje. En el ámbito lírico, la apropiación de la **décima espinela** por poetas insignes como Nicomedes y Victoria Santa Cruz transformó la estrofa clásica en una trinchera contra el racismo y en un canto de dignidad continental.",
         "Manifestaciones de la cultura afroperuana",
         [["El cajón peruano nació del ingenio de los cimarrones.", "The Peruvian cajon was born from the ingenuity of runaways."],
          ["Nicomedes Santa Cruz dignificó la décima de pie quebrado.", "Nicomedes Santa Cruz elevated the rhymed decima verse."],
          ["El festejo y el landó despliegan polirritmias africanas.", "Festejo and landó unfold African polyrhythms."],
          ["El zapateo criollo resuena en las fiestas de El Carmen.", "Criollo zapateo footwork echoes in the festivals of El Carmen."],
          ["La quijada de burro complementa el compás percusivo.", "The donkey jawbone complements the percussive beat."],
          ["Victoria Santa Cruz reivindicó el orgullo identitario negro.", "Victoria Santa Cruz championed black identity pride."]],
         "En 1977, el guitarrista Paco de Lucía descubrió el cajón en Lima y lo incorporó al flamenco, proyectando la creación afroperuana a los auditorios del mundo entero."),

        (r4, "grammar.b2.perucosta.04.gastronomia-nikkei-chifa", "Diplomacia culinaria: cebiche, chifa y fusión nikkei",
         "La gastronomía peruana contemporánea constituye un extraordinario fenómeno de **diplomacia cultural y cohesión social**, resultado de siglos de encuentro entre la biodiversidad andino-amazónica, la generosidad marina de Humboldt y sucesivas oleadas migratorias.\n\nEl **cebiche**, declarado Patrimonio Inmaterial de la Humanidad por la UNESCO, conjuga técnicas prehispánicas de maceración con cítricos mediterráneos. A ello se suman el **chifa** (fusión cantonesa nacida en el siglo XIX) y la cocina **nikkei** (fusión japonesa que revolucionó los cortes de pescado fresco con ají y jengibre).",
         "Conceptos clave de la cocina mestiza peruana",
         [["El cebiche conjuga pescado fresco, limón sutil y ají.", "Cebiche combines fresh fish, subtle Key lime, and chili pepper."],
          ["El chifa fusionó técnicas cantonesas con insumos locales.", "Chifa fused Cantonese wok techniques with local ingredients."],
          ["La cocina nikkei aportó cortes de sashimi y precisión.", "Nikkei cuisine contributed sashimi cuts and aesthetic precision."],
          ["La gastronomía opera como un factor de orgullo identitario.", "Gastronomy functions as a core factor of national pride."],
          ["El tiradito prescinde de cebolla y resalta la leche de tigre.", "Tiradito dispenses with onion and highlights the tiger's milk."],
          ["El lomo saltado amalgama el wok chino y la papa peruana.", "Lomo saltado blends the Chinese wok and the Peruvian potato."]],
         "La gastronomía ha funcionado en el Perú como un territorio de reconciliación democrática donde confluyen todas las clases sociales y regiones del país."),

        (r5, "grammar.b2.perucosta.05.iquitos-caucho-amazonia", "Iquitos y el auge del caucho en la cuenca amazónica",
         "Ubicada en el departamento de Loreto, a orillas del río Amazonas, **Iquitos** es la mayor metrópoli del mundo continental inaccesible por red de carreteras. Su comunicación depende exclusivamente de la navegación fluvial y el transporte aéreo.\n\nEntre 1880 y 1914, la ciudad vivió el delirio económico de la **fiebre del caucho**, marcada por una opulencia extravagante (mansiones con azulejos europeos y la **Casa de Fierro** atribuida a los talleres de Eiffel) y por la brutal explotación de comunidades indígenas amazónicas, cuya memoria y arte sagrado de **kené** resurgen hoy con orgullo.",
         "Aspectos históricos y territoriales de Iquitos y la Amazonia",
         [["Iquitos se erige como la capital fluvial de la Amazonia.", "Iquitos stands as the river capital of the Peruvian Amazon."],
          ["El ciclo del caucho generó fortunas y abusos laborales.", "The rubber boom generated massive fortunes and labor abuses."],
          ["La Casa de Fierro fue diseñada por el taller de Eiffel.", "The Iron House was designed in Eiffel's Parisian workshop."],
          ["El arte shipibo plasma la geometría sagrada del kené.", "Shipibo art depicts the sacred geometric patterns of kené."],
          ["El río Amazonas nace de la unión del Marañón y Ucayali.", "The Amazon River is born from the union of Marañón and Ucayali."],
          ["Iquitos depende vitalmente del transporte fluvial y aéreo.", "Iquitos vitally depends on fluvial and air transport."]],
         "El arte kené del pueblo Shipibo-Konibo fue declarado Patrimonio Cultural de la Nación por plasmar la cosmovisión y los cantos curativos de la selva viva.")
    ]

    for stem, gid, title, text_content, tbl_title, rows, tip_content in reg_grammars:
        write_json(f"grammar/b2/{stem}-a-gr.json", {
            "id": gid,
            "title": title,
            "sections": [
                {"type": "text", "content": text_content},
                {"type": "table", "title": tbl_title, "rows": rows},
                {"type": "tip", "content": tip_content}
            ]
        })

    # -------------------------------------------------------------------------
    # 3. EXERCISE FILES (6 Core + 6 Regional)
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
                    ["acuerdo", "bilateral signed pact"],
                    ["estipulación", "contractual clause"],
                    ["promulgar", "to officially enact"],
                    ["concordante", "grammatically matching in number"]
                ],
                "teaches": ["b2-19-vocab"]
            },
            {
                "id": f"{c1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ayer se __ los acuerdos de cooperación binacional en el palacio de gobierno. (firmar)",
                "answer": "firmaron",
                "english": "Yesterday the binational cooperation agreements were signed in the government palace.",
                "teaches": ["pasiva-refleja-concordancia"]
            },
            {
                "id": f"{c1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué es incorrecto decir '*Se aprobó los decretos supremos' en español formal?",
                "options": [
                    "Porque 'los decretos supremos' es el sujeto paciente plural y exige verbo en plural: 'se aprobaron'.",
                    "Porque el pronombre 'se' solo puede utilizarse con verbos intransitivos.",
                    "Porque los decretos deben llevar obligatoriamente la preposición 'a'.",
                    "Porque el verbo aprobar no admite construcciones pasivas en ningún caso."
                ],
                "correct": 0,
                "teaches": ["pasiva-refleja-concordancia"]
            },
            {
                "id": f"{c1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "publicaron", "los", "resultados", "oficiales", "del", "censo", "nacional."],
                "solution": ["Se", "publicaron", "los", "resultados", "oficiales", "del", "censo", "nacional."],
                "english": "The official results of the national census were published.",
                "teaches": ["pasiva-refleja-concordancia"]
            },
            {
                "id": f"{c1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Periodista", "text": "¿Qué decisiones se tomaron en el congreso extraordinario de ministros?"},
                    {"speaker": "Portavoz", "text": "Durante la sesión, _____ las nuevas directrices de inversión pública."}
                ],
                "options": [
                    "se consensuaron",
                    "se consensuó",
                    "consensuaron a",
                    "se consensuaban a"
                ],
                "correct": 0,
                "teaches": ["pasiva-refleja-concordancia"]
            },
            {
                "id": f"{c1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se redactaron minuciosamente todas las cláusulas del tratado comercial.",
                "english": "All clauses of the trade treaty were meticulously drafted.",
                "teaches": ["pasiva-refleja-concordancia"]
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
                    ["damnificado", "disaster victim"],
                    ["postulante", "exam candidate"],
                    ["atender", "to give formal care to"],
                    ["condecorar", "to award medal or honor"]
                ],
                "teaches": ["b2-19-vocab"]
            },
            {
                "id": f"{c2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En el hospital militar se __ a los soldados heridos durante el operativo. (atender)",
                "answer": "atendió",
                "english": "In the military hospital the wounded soldiers were cared for during the operation.",
                "teaches": ["se-pasivo-vs-impersonal"]
            },
            {
                "id": f"{c2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la diferencia sintáctica entre 'Se condecoró a los médicos' y 'Se construyeron los hospitales'?",
                "options": [
                    "La primera es impersonal con 'a' (verbo singular); la segunda es pasiva refleja con sujeto paciente plural.",
                    "Ambas son pasivas analíticas con complemento agente implícito.",
                    "La primera tiene sujeto paciente plural y la segunda es puramente reflexiva.",
                    "No hay diferencia sintáctica alguna, ambas son intercambiables en plural."
                ],
                "correct": 0,
                "teaches": ["se-pasivo-vs-impersonal"]
            },
            {
                "id": f"{c2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "premió", "a", "los", "mejores", "escritores", "del", "certamen."],
                "solution": ["Se", "premió", "a", "los", "mejores", "escritores", "del", "certamen."],
                "english": "The best writers of the contest were awarded.",
                "teaches": ["se-pasivo-vs-impersonal"]
            },
            {
                "id": f"{c2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Fiscal", "text": "¿Cómo procedió la policía tras la denuncia por estafa financiera?"},
                    {"speaker": "Abogada", "text": "Inmediatamente _____ a los principales directivos de la entidad."}
                ],
                "options": [
                    "se interrogó",
                    "se interrogaron",
                    "se interrogan a",
                    "interrogaron de"
                ],
                "correct": 0,
                "teaches": ["se-pasivo-vs-impersonal"]
            },
            {
                "id": f"{c2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se protegió a los testigos protegidos durante todo el juicio oral.",
                "english": "The protected witnesses were protected throughout the oral trial.",
                "teaches": ["se-pasivo-vs-impersonal"]
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
                    ["omisión", "deliberate withholding"],
                    ["vetar", "to officially veto"],
                    ["demoler", "to tear down structurally"],
                    ["tácito", "implied without words"]
                ],
                "teaches": ["b2-19-vocab"]
            },
            {
                "id": f"{c3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Por orden judicial se __ los pabellones en ruinas del viejo penal. (demoler)",
                "answer": "demolieron",
                "english": "By court order the ruined wings of the old penitentiary were demolished.",
                "teaches": ["pasiva-refleja-restricciones-agente"]
            },
            {
                "id": f"{c3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la oración '??Se cancelaron los vuelos por la aerolínea' resulta forzada o anómala en español culto?",
                "options": [
                    "Porque la pasiva refleja rechaza típicamente complementos agentes explícitos con 'por'; se prefiere la pasiva perifrástica.",
                    "Porque los vuelos no pueden ser cancelados por entidades jurídicas.",
                    "Porque el verbo cancelar solo puede usarse en voz activa.",
                    "Porque la preposición 'por' únicamente indica causa climática."
                ],
                "correct": 0,
                "teaches": ["pasiva-refleja-restricciones-agente"]
            },
            {
                "id": f"{c3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "suspendieron", "las", "garantías", "constitucionales", "durante", "la", "crisis."],
                "solution": ["Se", "suspendieron", "las", "garantías", "constitucionales", "durante", "la", "crisis."],
                "english": "Constitutional guarantees were suspended during the crisis.",
                "teaches": ["pasiva-refleja-restricciones-agente"]
            },
            {
                "id": f"{c3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministro", "text": "¿Qué medida se adoptó respecto a las obras inconclusas?"},
                    {"speaker": "Director", "text": "Tras la auditoría, _____ rescindir todos los contratos lesivos."}
                ],
                "options": [
                    "se determinó",
                    "se determinaron",
                    "se determinan a",
                    "determinaron por"
                ],
                "correct": 0,
                "teaches": ["pasiva-refleja-restricciones-agente"]
            },
            {
                "id": f"{c3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se desestimaron las impugnaciones por falta de pruebas concluyentes.",
                "english": "The challenges were dismissed for lack of conclusive evidence.",
                "teaches": ["pasiva-refleja-restricciones-agente"]
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
                    ["decreto", "official executive mandate"],
                    ["resolución", "formal administrative order"],
                    ["notificar", "to formally serve legal notice"],
                    ["fehaciente", "irrefutably proven"]
                ],
                "teaches": ["b2-19-vocab"]
            },
            {
                "id": f"{c4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En el artículo segundo se __ la creación de la reserva ecológica nacional. (disponer)",
                "answer": "dispone",
                "english": "In article second the creation of the national ecological reserve is decreed.",
                "teaches": ["se-institucional-juridico"]
            },
            {
                "id": f"{c4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué efecto pragmático produce la fórmula 'Se hace saber a las partes' en los documentos notariales?",
                "options": [
                    "Confiere autoridad formal despersonalizada e imparcialidad legal emanada de la institución.",
                    "Indica que el notario desconoce la identidad de los demandantes.",
                    "Expresa una opinión meramente subjetiva y provisional.",
                    "Obliga a suspender de inmediato el procedimiento administrativo."
                ],
                "correct": 0,
                "teaches": ["se-institucional-juridico"]
            },
            {
                "id": f"{c4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "ordena", "la", "inmediata", "ejecución", "de", "la", "sentencia."],
                "solution": ["Se", "ordena", "la", "inmediata", "ejecución", "de", "la", "sentencia."],
                "english": "The immediate execution of the ruling is ordered.",
                "teaches": ["se-institucional-juridico"]
            },
            {
                "id": f"{c4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Secretario", "text": "¿En qué términos quedó redactado el dictamen final?"},
                    {"speaker": "Relator", "text": "En el considerando primero _____ que las partes cumplieron los plazos."}
                ],
                "options": [
                    "se deja constancia de",
                    "se dejan constancia a",
                    "deja constancia de que",
                    "se dejaron de"
                ],
                "correct": 0,
                "teaches": ["se-institucional-juridico"]
            },
            {
                "id": f"{c4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se resuelve declarar infundada la apelación presentada por la defensa.",
                "english": "It is resolved to declare unfounded the appeal filed by the defense.",
                "teaches": ["se-institucional-juridico"]
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
                    ["ambigüedad", "double meaning"],
                    ["reciprocidad", "mutual exchange"],
                    ["difundir", "to spread news widely"],
                    ["equívoco", "easily misunderstood"]
                ],
                "teaches": ["b2-19-vocab"]
            },
            {
                "id": f"{c5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Durante la madrugada se __ los informes confidenciales en las redes. (filtrar)",
                "answer": "filtraron",
                "english": "During the early morning the confidential reports were leaked on social networks.",
                "teaches": ["desambiguacion-valores-se"]
            },
            {
                "id": f"{c5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la frase 'Los senadores se respetan', ¿cuál es la interpretación más habitual según la pragmática?",
                "options": [
                    "Recíproca: los senadores se respetan mutuamente entre sí.",
                    "Pasiva refleja: los senadores son respetados por la ciudadanía.",
                    "Impersonal absoluta: se respeta a todo el senado.",
                    "Reflexiva estricta: cada senador se respeta solo a sí mismo."
                ],
                "correct": 0,
                "teaches": ["desambiguacion-valores-se"]
            },
            {
                "id": f"{c5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "esclarecieron", "los", "hechos", "tras", "una", "exhaustiva", "indagación."],
                "solution": ["Se", "esclarecieron", "los", "hechos", "tras", "una", "exhaustiva", "indagación."],
                "english": "The facts were clarified after an exhaustive inquiry.",
                "teaches": ["desambiguacion-valores-se"]
            },
            {
                "id": f"{c5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Investigador", "text": "¿Qué ocurrió cuando colapsó el servidor bancario?"},
                    {"speaker": "Perito", "text": "Afortunadamente _____ copias de seguridad de todas las transacciones."}
                ],
                "options": [
                    "se habían generado",
                    "se había generado a",
                    "habían generado a",
                    "se generaban con"
                ],
                "correct": 0,
                "teaches": ["desambiguacion-valores-se"]
            },
            {
                "id": f"{c5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se descubrieron valiosos manuscritos coloniales en el archivo histórico.",
                "english": "Valuable colonial manuscripts were discovered in the historical archive.",
                "teaches": ["desambiguacion-valores-se"]
            }
        ]
    })

    # Core Consolidation
    write_json(f"exercises/b2/{l6_con}-ex.json", {
        "lesson": l6_con,
        "exercises": [
            {
                "id": f"{l6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["promulgar", "to officially enact laws"],
                    ["damnificado", "disaster victim"],
                    ["demoler", "to tear down structures"],
                    ["vinculante", "legally binding mandate"]
                ],
                "teaches": ["b2-19-vocab"]
            },
            {
                "id": f"{c_unit}-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En el internado militar se __ normas implacables de disciplina y silencio. (imponer)",
                "answer": "imponían",
                "english": "In the military boarding school relentless rules of discipline and silence were imposed.",
                "teaches": ["sintesis-pasiva-refleja"]
            },
            {
                "id": f"{c_unit}-consolidation.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la novela La ciudad y los perros, ¿qué función cumple la impersonalidad en el código de honor de los cadetes?",
                "options": [
                    "Refleja una ley tribal no escrita donde 'se delata' o 'se calla' bajo amenaza de castigo colectivo.",
                    "Demuestra que los cadetes desconocían el idioma castellano formal.",
                    "Indica que el colegio carecía de autoridades y reglamentos oficiales.",
                    "Demuestra que todos los estudiantes eran pacíficos y amables."
                ],
                "correct": 0,
                "teaches": ["sintesis-pasiva-refleja"]
            },
            {
                "id": f"{c_unit}-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Tras el robo del examen de química, se __ con rigor a todos los cadetes sospechosos. (interrogar)",
                "answer": "interrogó",
                "english": "After the theft of the chemistry exam, all suspected cadets were rigorously interrogated.",
                "teaches": ["se-pasivo-vs-impersonal"]
            },
            {
                "id": f"{c_unit}-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Se", "establecieron", "sanciones", "severas", "para", "los", "infractores."],
                "solution": ["Se", "establecieron", "sanciones", "severas", "para", "los", "infractores."],
                "english": "Severe penalties were established for violators.",
                "teaches": ["sintesis-pasiva-refleja"]
            },
            {
                "id": f"{c_unit}-consolidation.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Teniente Gamboa", "text": "¿Se sabe con certeza quién disparó el fusil durante las maniobras?"},
                    {"speaker": "Cadete Alberto", "text": "Mi teniente, entre los cadetes _____ la verdad por miedo a represalias."}
                ],
                "options": [
                    "se oculta",
                    "se ocultan a",
                    "ocultan de",
                    "se ocultaban a"
                ],
                "correct": 0,
                "teaches": ["sintesis-pasiva-refleja"]
            },
            {
                "id": f"{c_unit}-consolidation.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "Se archivó el expediente disciplinario para salvar el prestigio de la institución.",
                "english": "The disciplinary file was shelved to save the institution's prestige.",
                "teaches": ["sintesis-pasiva-refleja"]
            },
            {
                "id": f"{c_unit}-consolidation.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la regla fundamental para elegir entre 'se atendió a las víctimas' y 'se atendieron los reclamos'?",
                "options": [
                    "Con personas introducidas por 'a' va en singular impersonal; con cosas sin preposición va en plural como pasiva refleja.",
                    "Las personas siempre exigen verbo en plural y las cosas siempre en singular.",
                    "Ambas frases deben llevar el verbo obligatoriamente en plural.",
                    "La preposición 'a' solo se usa con sujetos inanimados."
                ],
                "correct": 0,
                "teaches": ["se-pasivo-vs-impersonal"]
            }
        ]
    })

    # Regional 1 (Humboldt & Coast)
    write_json(f"exercises/b2/{r1}-ex.json", {
        "lesson": r1,
        "exercises": [
            {
                "id": f"{r1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["afloramiento", "nutrient-rich upwelling"],
                    ["garúa", "dense winter coastal mist"],
                    ["anchoveta", "Peruvian forage fish"],
                    ["litoral", "coastal shoreline zone"]
                ],
                "teaches": ["b2-perucosta-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las aguas frías de la corriente de __ ascienden frente a las costas del Perú ricas en plancton. (Humboldt)",
                "answer": "Humboldt",
                "english": "The cold waters of the Humboldt Current rise off the coast of Peru rich in plankton.",
                "teaches": ["peru-costa-corriente-humboldt"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué fenómeno climático singular causa la corriente de Humboldt en la costa central peruana?",
                "options": [
                    "Impide la formación de lluvias torrenciales y genera una persistente niebla invernal llamada garúa.",
                    "Provoca tifones tropicales continuos durante todos los meses del año.",
                    "Congela las bahías marítimas convirtiéndolas en glaciares flotantes.",
                    "Transforma el desierto costero en una selva tropical húmeda."
                ],
                "correct": 0,
                "teaches": ["peru-costa-corriente-humboldt"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "mar", "peruano", "posee", "una", "de", "las", "mayores", "biomasas", "marinas."],
                "solution": ["El", "mar", "peruano", "posee", "una", "de", "las", "mayores", "biomasas", "marinas."],
                "english": "The Peruvian sea possesses one of the greatest marine biomasses.",
                "teaches": ["peru-costa-corriente-humboldt"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Bióloga", "text": "¿Por qué es tan prolífica la pesca de anchoveta en el mar de Grau?"},
                    {"speaker": "Oceanógrafo", "text": "Porque el afloramiento costero de nutrientes minerales _____ una cadena trófica colosal."}
                ],
                "options": [
                    "sustenta de manera continua",
                    "sustentan con frialdad",
                    "sustentaban a",
                    "habrían sustentado"
                ],
                "correct": 0,
                "teaches": ["peru-costa-corriente-humboldt"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La corriente fría de Humboldt define el clima hiperárido de la faja costera peruana.",
                "english": "The cold Humboldt Current defines the hyper-arid climate of the Peruvian coastal strip.",
                "teaches": ["peru-costa-corriente-humboldt"]
            }
        ]
    })

    # Regional 2 (Lima Virreinal)
    write_json(f"exercises/b2/{r2}-ex.json", {
        "lesson": r2,
        "exercises": [
            {
                "id": f"{r2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["celosía", "latticed wooden balcony screen"],
                    ["virreinato", "colonial viceroyalty seat"],
                    ["señorío", "stately noble elegance"],
                    ["conventual", "monastic religious architecture"]
                ],
                "teaches": ["b2-perucosta-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Los balcones de __ son el elemento arquitectónico más distintivo del centro histórico de Lima. (celosía)",
                "answer": "celosía",
                "english": "Latticed balconies are the most distinctive architectural feature of Lima's historic center.",
                "teaches": ["peru-lima-virreinal-balcones"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Quiénes eran las célebres 'tapadas limeñas' en la sociedad virreinal?",
                "options": [
                    "Mujeres que cubrían su rostro con mantón de seda dejando un solo ojo visible para circular con libertad anónima.",
                    "Monjas de clausura que jamás salían de las catacumbas franciscanas.",
                    "Comerciantes extranjeras dedicadas a la venta de telas orientales.",
                    "Soldaderas que custodiaban las murallas de la ciudad colonial."
                ],
                "correct": 0,
                "teaches": ["peru-lima-virreinal-balcones"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Lima", "fue", "fundada", "en", "1535", "como", "la", "Ciudad", "de", "los", "Reyes."],
                "solution": ["Lima", "fue", "fundada", "en", "1535", "como", "la", "Ciudad", "de", "los", "Reyes."],
                "english": "Lima was founded in 1535 as the City of Kings.",
                "teaches": ["peru-lima-virreinal-balcones"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Turista", "text": "¿Qué función cumplían las catacumbas bajo la iglesia de San Francisco?"},
                    {"speaker": "Guía", "text": "Durante siglos _____ como el principal camposanto subterráneo de la ciudad virreinal."}
                ],
                "options": [
                    "funcionaron",
                    "funcionó a",
                    "funcionaban con",
                    "habrían funcionado a"
                ],
                "correct": 0,
                "teaches": ["peru-lima-virreinal-balcones"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los balcones voladizos de cedro permitían contemplar las procesiones sin ser visto.",
                "english": "The cantilevered cedar balconies allowed one to watch processions without being seen.",
                "teaches": ["peru-lima-virreinal-balcones"]
            }
        ]
    })

    # Regional 3 (Afroperuano)
    write_json(f"exercises/b2/{r3}-ex.json", {
        "lesson": r3,
        "exercises": [
            {
                "id": f"{r3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["cajón", "Afro-Peruvian wooden box drum"],
                    ["décima", "ten-verse rhymed poem"],
                    ["zapateo", "rhythmic percussive tap dancing"],
                    ["cimarrón", "escaped enslaved rebel"]
                ],
                "teaches": ["b2-perucosta-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El distrito de El Carmen en la provincia de __ es el corazón de la cultura afroperuana. (Chincha)",
                "answer": "Chincha",
                "english": "The district of El Carmen in the province of Chincha is the heart of Afro-Peruvian culture.",
                "teaches": ["peru-afroperuano-chincha-cajon"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál fue la trascendencia del poeta Nicomedes Santa Cruz en la cultura hispanoamericana?",
                "options": [
                    "Rescató y revitalizó la décima de pie quebrado para denunciar el racismo y celebrar la raíz afrodescendiente.",
                    "Fue el compositor del himno nacional republicano del Perú.",
                    "Escribió tratados de botánica sobre los algodonales costeños.",
                    "Diseñó los primeros planos de los ferrocarriles andinos."
                ],
                "correct": 0,
                "teaches": ["peru-afroperuano-chincha-cajon"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "cajón", "peruano", "es", "el", "alma", "rítmica", "de", "la", "música", "criolla."],
                "solution": ["El", "cajón", "peruano", "es", "el", "alma", "rítmica", "de", "la", "música", "criolla."],
                "english": "The Peruvian cajon is the rhythmic soul of criollo music.",
                "teaches": ["peru-afroperuano-chincha-cajon"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Músico", "text": "¿Cómo se incorporó el cajón peruano a la música flamenca en España?"},
                    {"speaker": "Musicóloga", "text": "Fue descubierto en Lima por Paco de Lucía, quien _____ en sus giras mundiales."}
                ],
                "options": [
                    "lo adoptó con entusiasmo",
                    "adoptaron a él",
                    "se adoptó de",
                    "lo habían adoptado a"
                ],
                "correct": 0,
                "teaches": ["peru-afroperuano-chincha-cajon"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La marinera y el festejo combinan elegancia criolla con síncopas de raíz africana.",
                "english": "The marinera and festejo combine criollo elegance with African-rooted syncopations.",
                "teaches": ["peru-afroperuano-chincha-cajon"]
            }
        ]
    })

    # Regional 4 (Gastronomía)
    write_json(f"exercises/b2/{r4}-ex.json", {
        "lesson": r4,
        "exercises": [
            {
                "id": f"{r4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["cebiche", "lime-cured fresh raw fish"],
                    ["tiradito", "sashimi-cut fish without raw onion"],
                    ["chifa", "Cantonese-Peruvian wok cuisine"],
                    ["nikkei", "Japanese-Peruvian fusion artistry"]
                ],
                "teaches": ["b2-perucosta-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La UNESCO declaró al __ tradicional peruano como Patrimonio Cultural Inmaterial de la Humanidad. (cebiche)",
                "answer": "cebiche",
                "english": "UNESCO declared traditional Peruvian cebiche as Intangible Cultural Heritage of Humanity.",
                "teaches": ["peru-gastronomia-nikkei-chifa"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué singularidad histórica define la cocina 'chifa' en la sociedad peruana?",
                "options": [
                    "Nació de los inmigrantes cantoneses en el siglo XIX adaptando ingredientes chinos a productos peruanos.",
                    "Fue importada de Francia durante la corte de los reyes borbones.",
                    "Es una dieta exclusiva de pescadores prehispánicos del norte.",
                    "Surgió en las misiones jesuíticas de la selva amazónica."
                ],
                "correct": 0,
                "teaches": ["peru-gastronomia-nikkei-chifa"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "cocina", "peruana", "es", "el", "resultado", "de", "siglos", "de", "mestizaje."],
                "solution": ["La", "cocina", "peruana", "es", "el", "resultado", "de", "siglos", "de", "mestizaje."],
                "english": "Peruvian cuisine is the result of centuries of cultural fusion.",
                "teaches": ["peru-gastronomia-nikkei-chifa"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Crítico", "text": "¿En qué se diferencia el tiradito del cebiche clásico?"},
                    {"speaker": "Chef", "text": "El tiradito lleva cortes finos estilo sashimi y prescinde de cebolla, _____ de crema de ají."}
                ],
                "options": [
                    "acompañado",
                    "acompañando a",
                    "se acompaña",
                    "habiendo acompañado"
                ],
                "correct": 0,
                "teaches": ["peru-gastronomia-nikkei-chifa"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La biodiversidad marina y andina convirtió a Lima en la capital gastronómica continental.",
                "english": "Marine and Andean biodiversity turned Lima into the continental gastronomic capital.",
                "teaches": ["peru-gastronomia-nikkei-chifa"]
            }
        ]
    })

    # Regional 5 (Iquitos y Amazonia)
    write_json(f"exercises/b2/{r5}-ex.json", {
        "lesson": r5,
        "exercises": [
            {
                "id": f"{r5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["caucho", "latex from Amazonian trees"],
                    ["siringuero", "forest rubber tapper"],
                    ["fluvial", "river-navigable system"],
                    ["aislamiento", "isolation without highway access"]
                ],
                "teaches": ["b2-perucosta-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La ciudad de __ es la metrópoli continental más poblada del mundo sin conexión por carretera. (Iquitos)",
                "answer": "Iquitos",
                "english": "The city of Iquitos is the world's most populous continental metropolis without road connection.",
                "teaches": ["peru-iquitos-caucho-amazonia"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué monumento arquitectónico en Iquitos testimonia la desmedida opulencia del auge del caucho?",
                "options": [
                    "La Casa de Fierro, atribuida a los talleres parisinos de Gustave Eiffel y ensamblada en plena selva.",
                    "Un anfiteatro romano de mármol de Carrara traído en barcazas.",
                    "Una pirámide de cristal inspirada en el Museo del Louvre.",
                    "Un rascacielos de cincuenta pisos construido con maderas preciosas."
                ],
                "correct": 0,
                "teaches": ["peru-iquitos-caucho-amazonia"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "río", "Amazonas", "nace", "en", "las", "cumbres", "andinas", "del", "Perú."],
                "solution": ["El", "río", "Amazonas", "nace", "en", "las", "cumbres", "andinas", "del", "Perú."],
                "english": "The Amazon River is born in the Andean peaks of Peru.",
                "teaches": ["peru-iquitos-caucho-amazonia"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Antropóloga", "text": "¿Qué expresa la compleja iconografía geométrica del kené en el pueblo shipibo?"},
                    {"speaker": "Artista", "text": "Representa las visiones de plantas maestras y los senderos fluviales que _____ el cosmos selvático."}
                ],
                "options": [
                    "interconectan",
                    "interconecta a",
                    "se interconectan de",
                    "habían interconectado a"
                ],
                "correct": 0,
                "teaches": ["peru-iquitos-caucho-amazonia"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Iquitos vive en íntima simbiosis con los caudales crecientes y vaciantes del río Amazonas.",
                "english": "Iquitos lives in intimate symbiosis with the rising and falling waters of the Amazon River.",
                "teaches": ["peru-iquitos-caucho-amazonia"]
            }
        ]
    })

    # Regional Consolidation
    write_json(f"exercises/b2/{r6_con}-ex.json", {
        "lesson": r6_con,
        "exercises": [
            {
                "id": f"{r6_con}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["garúa", "grey coastal winter mist"],
                    ["celosía", "latticed balcony carved in cedar"],
                    ["cajón", "resonant wooden box drum"],
                    ["cebiche", "fresh fish cured with citrus"]
                ],
                "teaches": ["b2-perucosta-vocab"]
            },
            {
                "id": f"{r6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El mar peruano debe su extraordinaria abundancia biológica al __ de aguas profundas. (afloramiento)",
                "answer": "afloramiento",
                "english": "The Peruvian sea owes its extraordinary biological abundance to the upwelling of deep waters.",
                "teaches": ["peru-costa-corriente-humboldt"]
            },
            {
                "id": f"{r6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué rasgo arquitectónico virreinal concedió a Lima el apelativo de la 'ciudad de los balcones'?",
                "options": [
                    "Cientos de balcones voladizos de celosía mudéjar tallados en madera de cedro.",
                    "Balcones de hierro forjado traídos exclusivamente de los palacios de Versalles.",
                    "Miradores de cristal flotante inspirados en la arquitectura holandesa.",
                    "Terrazas al aire libre decoradas únicamente con columnas de mármol blanco."
                ],
                "correct": 0,
                "teaches": ["peru-lima-virreinal-balcones"]
            },
            {
                "id": f"{r6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El poeta afroperuano Nicomedes Santa Cruz popularizó la __ como expresión lírica y social. (décima)",
                "answer": "décima",
                "english": "Afro-Peruvian poet Nicomedes Santa Cruz popularized the decima as a lyrical and social expression.",
                "teaches": ["peru-afroperuano-chincha-cajon"]
            },
            {
                "id": f"{r6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿De qué manera la gastronomía contemporánea ha forjado un consenso identitario en el Perú moderno?",
                "options": [
                    "Ha convertido el orgullo por la biodiversidad y el mestizaje culinario en un símbolo unificador de ciudadanía.",
                    "Ha eliminado por completo el consumo de carnes y pescados en todo el país.",
                    "Obliga a todas las familias a comer exclusivamente en restaurantes de alta cocina.",
                    "Ha reemplazado a todos los idiomas originarios por manuales de hostelería."
                ],
                "correct": 0,
                "teaches": ["peru-gastronomia-nikkei-chifa"]
            },
            {
                "id": f"{r6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Iquitos", "mantiene", "su", "vida", "social", "articulada", "en", "torno", "al", "río."],
                "solution": ["Iquitos", "mantiene", "su", "vida", "social", "articulada", "en", "torno", "al", "río."],
                "english": "Iquitos maintains its social life organized around the river.",
                "teaches": ["peru-iquitos-caucho-amazonia"]
            },
            {
                "id": f"{r6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La costa peruana amalgama el rigor del desierto con la infinita generosidad del océano Pacífico.",
                "english": "The Peruvian coast blends the harshness of the desert with the infinite generosity of the Pacific Ocean.",
                "teaches": ["peru-costa-sintesis-regional"]
            },
            {
                "id": f"{r6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la principal vía de abastecimiento y comunicación para la ciudad amazónica de Iquitos?",
                "options": [
                    "El transporte fluvial por el río Amazonas y los vuelos comerciales, ya que carece de carreteras terrestres.",
                    "Una autopista pavimentada de cuatro carriles que cruza los Andes directamente.",
                    "Un tren de alta velocidad que conecta la selva con la costa de Lima.",
                    "Un sistema de teleféricos interprovinciales suspendidos sobre las copas de los árboles."
                ],
                "correct": 0,
                "teaches": ["peru-iquitos-caucho-amazonia"]
            }
        ]
    })

    # -------------------------------------------------------------------------
    # 4. STORIES (1 Core Classic + 5 Regional Lessons + 1 Regional Capstone)
    # Strictly audited between 650 and 825 words
    # -------------------------------------------------------------------------
    # Story Core 19: Mario Vargas Llosa - La ciudad y los perros (1963)
    story_core_19 = {
        "id": "b2-19",
        "title": "La ciudad y los perros: El código de silencio en el Leoncio Prado",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de la célebre novela de Mario Vargas Llosa: la disciplina militar asfixiante del Colegio Militar Leoncio Prado en Lima, el robo clandestino de un examen de química por 'el Círculo', la delación desesperada del Esclavo, el misterioso disparo mortal en las maniobras y el silencio corporativo impuesto por los oficiales para salvaguardar el prestigio institucional.",
        "characters": [
            "Cadete Alberto Fernández ('el Poeta')",
            "Cadete Jaguar",
            "Cadete Ricardo Arana ('el Esclavo')",
            "Teniente Gamboa",
            "Coronel director"
        ],
        "narration": {
            "paragraphs": [
                "Bajo el cielo encapotado y plomizo de Lima, donde la niebla húmeda se confunde con el salitre del océano Pacífico, el Colegio Militar Leoncio Prado se alzaba en el distrito de La Perla como un microcosmos brutal de toda la sociedad peruana. Tras sus altos muros de ladrillo y rejas de hierro, centenares de adolescentes procedentes de las clases aristocráticas de Miraflores, las barriadas pobres del Rímac y las provincias andinas convivían sometidos a una disciplina militar implacable. En aquel recinto carcelario, se aprendía rápidamente que la debilidad no se perdonaba: los alumnos del último año bautizaban cruelmente a los recién llegados como 'perros', imponiéndoles ritos de sumisión, novatadas violentas y castigos humillantes diseñados para forjar una masculinidad tosca y despiadada.",
                "Para sobrevivir a los abusos y burlar el estricto reglamento interno, se organizaban cofradías clandestinas regidas por códigos implacables. La más temida de ellas era 'el Círculo', una banda secreta capitaneada por el Jaguar, un cadete silencioso, atlético y de mirada gélida que dominaba los dormitorios mediante la ley de los puños. Una noche fría y neblinosa, se ejecutó una audaz operación prohibida: el Círculo rompió el cristal de un ventanal del laboratorio y se sustrajo el examen oficial de química que se aplicaría al día siguiente. Sin embargo, al descubrirse el vidrio astillado, las autoridades militares reaccionaron con indignación draconiana: se suspendieron de inmediato las salidas de fin de semana para toda la sección y se decretó un encierro indefinido hasta que apareciera el culpable.",
                "El confinamiento prolongado resultó devastador para Ricardo Arana, apodado con desprecio 'el Esclavo' por su carácter tímido, su fragilidad física y su incapacidad visceral para responder a los golpes. Desesperado por obtener el pase de salida que le permitiría visitar a Teresa, una vecina de barrio a quien amaba en secreto desde la infancia, el Esclavo tomó una decisión trágica y suicida: acudió al despacho de los oficiales y denunció en secreto a Cava, el cadete serrano que había ejecutado materialmente el robo del examen. Pocas horas después, Cava fue degradado en público ante el batallón formado y expulsado del colegio en medio de la ignominia general. En el cuartel, la delación representaba el pecado supremo: se juró venganza inmediata en los pasillos nocturnos.",
                "La venganza no tardó en consumarse con frialdad letal. Durante unos ejercicios tácticos con fusiles y munición real en el descampado pedregoso de la pampa de Amancayes, una detonación imprevista retumbó en medio de la humareda de los disparos. El Esclavo cayó desplomado sobre el polvo con una herida de bala en la cabeza. Los partes médicos iniciales determinaron que se trataba de un accidente fortuito provocado por la propia negligencia del cadete al tropezar con su arma. No obstante, el cadete Alberto Fernández, conocido como 'el Poeta' por redactar cartas de amor y novelitas eróticas a cambio de cigarrillos, sabía que el Esclavo jamás se habría disparado a sí mismo: se sospechaba con certeza moral que el Jaguar había aprovechado el fragor del combate simulado para liquidar al delator.",
                "Consumido por el remordimiento y el horror, Alberto acudió ante el teniente Gamboa, el único oficial recto y riguroso que creía en la justicia militar más allá de los favoritismos. Conmovido por el testimonio del cadete, Gamboa inició una exhaustiva investigación interna y encerró al Jaguar en el calabozo preventivo. Pero cuando las pesquisas amenazaron con desvelar ante la opinión pública que en el prestigioso colegio militar se traficaba alcohol, se jugaba a los dados y se cometían asesinatos por venganza, la jerarquía superior intervino con contundencia. El coronel director ordenó archivar de inmediato el sumario: se alegó que no existían pruebas concluyentes y que el prestigio sagrado del ejército no podía ser mancillado por los rumores de unos muchachos indisciplinados.",
                "Para silenciar definitivamente el escándalo, se amenazó a Alberto con revelar ante su familia las cartas pornográficas que él mismo había escrito, obligándolo a retractarse y firmar su silencio cómplice. Por su parte, el honesto teniente Gamboa fue sancionado con un traslado forzoso a una guarnición remota en las punas heladas de la sierra sur. Al finalizar el año lectivo, los cadetes se graduaron y se dispersaron por la inmensa urbe de Lima como si nada hubiera ocurrido. El Jaguar regresó a su barrio prometiendo redimirse, mientras Alberto se preparaba para viajar a estudiar al extranjero, olvidando las pesadillas del internado. La novela de Vargas Llosa denunciaba así cómo las instituciones autoritarias imponen el silencio colectivo para encubrir la violencia, dejando a los individuos atrapados en una telaraña de hipocresía social."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué Ricardo Arana, 'el Esclavo', decidió romper el código de silencio y delatar el robo del examen?",
                        "options": [
                            "Porque estaba desesperado por salir de franco el fin de semana para visitar a su amada Teresa.",
                            "Porque el coronel le prometió un ascenso inmediato al rango de brigadier mayor.",
                            "Porque deseaba expulsar a su enemigo el Jaguar para asumir el mando del Círculo.",
                            "Porque los oficiales lo descubrieron con las copias del examen bajo su almohada."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Esclavo estaba confinado indefinidamente y delató a Cava para conseguir el pase de salida y ver a Teresa."
                    },
                    {
                        "question": "¿Cómo reaccionaron las altas autoridades del colegio militar ante la investigación iniciada por el teniente Gamboa?",
                        "options": [
                            "Archivaron el caso para salvaguardar el prestigio del ejército y castigaron a Gamboa trasladándolo a la sierra.",
                            "Felicitaron a Gamboa públicamente y llevaron al Jaguar a un consejo de guerra televisado.",
                            "Cerraron el colegio militar de forma definitiva demoliendo sus instalaciones.",
                            "Nombraron a Alberto como nuevo director administrativo del colegio."
                        ],
                        "correctIndex": 0,
                        "explanation": "El coronel archivó el sumario para proteger la imagen institucional y sancionó al teniente Gamboa enviándolo a una guarnición remota."
                    },
                    {
                        "question": "¿Qué representa el Colegio Militar Leoncio Prado en la novela de Mario Vargas Llosa?",
                        "options": [
                            "Un microcosmos de la sociedad peruana donde chocan distintas clases sociales bajo un régimen autoritario.",
                            "Una academia deportiva de verano donde solo se practicaba natación competitiva.",
                            "Un internado religioso fundado exclusivamente para la formación de futuros sacerdotes.",
                            "Una colonia agrícola extranjera situada en las selvas de la frontera oriental."
                        ],
                        "correctIndex": 0,
                        "explanation": "El colegio funciona como metáfora de la sociedad peruana, donde conviven jóvenes de todas las clases bajo violencia y jerarquía institucional."
                    }
                ]
            }
        }
    }

    # Regional Story 1: Corriente de Humboldt y costa
    story_peru_01 = {
        "id": "b2-peruandino-01", # Will be mapped to b2-perucosta-01
        "title": "El mar de Humboldt: El río frío que fecunda el desierto peruano",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía oceanográfica y geográfica por el litoral peruano: el flujo polar de la corriente de Humboldt, el afloramiento costero de nutrientes minerales, la inmensa biomasa de la anchoveta, las islas guaneras de Chincha, el enigma del desierto hiperárido y la garúa invernal que baña la ciudad de Lima.",
        "characters": [
            "Oceanógrafa Carola Medina",
            "Capitán pesquero Don Lucho",
            "Guardaparque de Paracas Marcial",
            "Biólogo marino Andrés"
        ],
        "narration": {
            "paragraphs": [
                "A bordo de la moderna embarcación científica que zarpa antes del amanecer desde la bahía del Callao, el océano Pacífico se presenta como un manto espeso de aguas verde esmeralda cubierto por una densa neblina lechosa. El termómetro sumergido en el agua marca apenas catorce grados centígrados, una temperatura asombrosamente gélida para una latitud intertropical donde teóricamente deberían reinar mares cálidos y arrecifes de coral. La responsable directa de esta paradoja planetaria es la corriente de Humboldt o del Perú: un colosal río submarino de aguas antárticas que remonta las costas de Chile y Perú a lo largo de miles de kilómetros, descubierto y medido científicamente por el sabio naturalista prusiano Alexander von Humboldt durante su histórica expedición de 1802 frente a las playas de Lima e impulsado por la rotación terrestre y los vientos alisios del sureste.",
                "Cuando estos constantes vientos costeros empujan las capas de agua superficial hacia mar adentro, se desencadena el fenómeno hidrográfico más prolífico del globo terráqueo: el afloramiento costero o surgencia marina. Desde las profundidades abisales y oscuras de la fosa peruano-chilena, aguas frías saturadas de nitratos, fosfatos y silicatos ascienden ininterrumpidamente hacia la superficie iluminada por el sol. Esta inagotable sopa mineral fertiliza una explosión incalculable de fitoplancton microscópico, que tiñe las aguas de tonalidades verdosas y sustenta a millonarias colonias de zooplancton, conformando la base alimenticia de la cadena trófica marina más densa, rica y productiva de todo el planeta.",
                "En el corazón de este prodigio biológico nada la anchoveta peruana (*Engraulis ringens*), un pequeño pez plateado que no supera los quince centímetros de longitud pero cuya abundancia desafía la imaginación de los biólogos marinos. Cardúmenes descomunales que se extienden por decenas de kilómetros cuadrados navegan por el litoral, alimentando no solo a ballenas jorobadas, delfines mulares, lobos marinos de chusco y pingüinos de Humboldt en las islas Ballestas y la reserva de Paracas, sino también a millones de aves guaneras como el guanay, el piquero y el pelícano alcatraz, cuyas deyecciones milenarias acumularon sobre las islas de Chincha gigantescas montañas de guano que en el siglo XIX financiaron la economía republicana del Perú.",
                "Sin embargo, la corriente de Humboldt no solo gobierna la vida en el océano, sino que esculpe de manera radical el paisaje terrestre del litoral. Al enfriar drásticamente las capas inferiores de la atmósfera marina, el agua fría impide la evaporación masiva y la formación de nubes de tormenta convectivas. Como consecuencia directa de este fenómeno de inversión térmica, no llueve casi jamás sobre la angosta franja costera peruana, dando origen a uno de los desiertos costeros más áridos y desolados del mundo, interrumpido únicamente por cincuenta y tres valles fluviales que descienden velozmente desde las cumbres de los Andes.",
                "Durante los meses del invierno austral, entre mayo y octubre, la humedad marina condensada queda atrapada bajo la capa de inversión térmica a menos de quinientos metros de altitud, cubriendo la ciudad de Lima y los acantilados de la Costa Verde con una llovizna microscópica e incesante conocida popularmente como 'garúa'. Esta niebla fría transforma el cielo limeño en el célebre 'cielo color panza de burro' descrito por cronistas virreinales, humedeciendo las lomas costeras de Lachay y Amancaes donde florecen milagrosamente vergeles vegetales efímeros de flores amarillas en medio de la desolación de las arenas desérticas.",
                "El mar de Grau, bautizado así en honor al héroe naval Miguel Grau Seminario, representa la mayor reserva de proteínas marinas de América del Sur y una arteria económica primordial para miles de familias de pescadores artesanales e industriales. No obstante, este ecosistema hiperproductivo enfrenta hoy la amenaza cíclica de El Niño: un calentamiento anómalo de las aguas superficiales que debilita el afloramiento, desplaza a los cardúmenes de anchoveta hacia el sur y desencadena destructivas lluvias aluviales en el desierto. Preservar el equilibrio de esta corriente polar frente a la sobrepesca y el calentamiento global constituye una responsabilidad ecológica de trascendencia continental."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué proceso oceanográfico explica la extraordinaria abundancia de fitoplancton en el litoral peruano?",
                        "options": [
                            "El afloramiento costero de aguas profundas frías cargadas de nitratos, fosfatos y sales minerales.",
                            "El calentamiento volcánico submarino procedente de géiseres en la fosa oceánica.",
                            "La descarga masiva de fertilizantes químicos industriales desde los barcos mercantes.",
                            "La ausencia total de corrientes marinas y la inmovilidad absoluta del agua."
                        ],
                        "correctIndex": 0,
                        "explanation": "El afloramiento eleva aguas abisales frías ricas en nutrientes minerales que alimentan al fitoplancton microscópico."
                    },
                    {
                        "question": "¿Por qué la corriente fría de Humboldt impide la lluvia regular en la costa desértica del Perú?",
                        "options": [
                            "Porque enfría las capas bajas de la atmósfera generando inversión térmica que evita la formación de nubes de lluvia.",
                            "Porque absorbe toda la humedad del viento desviándola directamente hacia el océano Atlántico.",
                            "Porque los vientos alisios soplan exclusivamente desde el polo sur hacia la Antártida.",
                            "Porque el agua salada disuelve las nubes en cuanto intentan ingresar al continente."
                        ],
                        "correctIndex": 0,
                        "explanation": "El enfriamiento del aire marino genera inversión térmica, impidiendo la convección y las precipitaciones regulares en la costa."
                    },
                    {
                        "question": "¿Qué alteración climática provoca el fenómeno de El Niño en el ecosistema marino de la costa peruana?",
                        "options": [
                            "Calienta las aguas superficiales, debilitando el afloramiento y desplazando los cardúmenes de anchoveta.",
                            "Congela por completo los puertos pesqueros impidiendo la navegación de las lanchas.",
                            "Seca el océano Pacífico transformándolo en una salina durante varios meses.",
                            "Atrae millones de pingüinos polares hacia las playas turísticas de Lima."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Niño introduce aguas cálidas tropicales que suprimen la surgencia de nutrientes y dispersan a la anchoveta."
                    }
                ]
            }
        }
    }

    # Regional Story 2: Lima virreinal y balcones
    story_peru_02 = {
        "id": "b2-peruandino-02", # Will be mapped to b2-perucosta-02
        "title": "La Ciudad de los Reyes: Balcones de celosía, conventos y tapadas",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica histórica por el damero de Pizarro y la Lima virreinal: la fundación en 1535 a orillas del río Rímac, la opulencia de la corte virreinal, el diseño mudéjar de los balcones voladizos de celosía, las catacumbas de San Francisco, la devoción a Santa Rosa de Lima y el mito fascinante de la tapada limeña.",
        "characters": [
            "Cronista don Sebastián de Aliaga",
            "Doña Francisca de Zúñiga (la Tapada)",
            "Fray Bartolomé del convento de San Francisco",
            "Restauradora Mariana"
        ],
        "narration": {
            "paragraphs": [
                "El 18 de enero de 1535, en una llanura árida cercana al mar y regada por las milenarias acequias del río Rímac, el conquistador Francisco Pizarro fundó solemnemente la capital del virreinato con el nombre oficial de Ciudad de los Reyes, en homenaje a los Reyes Magos de la Epifanía. Erigida sobre el palacio y los dominios del curaca indígena Taulichusco y trazada con tiralíneas en un damero perfecto de ciento diecisiete manzanas cuadradas, Lima se convirtió durante casi tres siglos en la sede gubernamental, judicial, militar y eclesiástica más opulenta de todo el imperio español en América del Sur. Desde su palacio virreinal partían las órdenes y decretos que regían los destinos de un territorio colosal que se extendía desde las selvas de Panamá hasta los estrechos patagónicos de Tierra del Fuego.",
                "En esta capital cortesana donde el oro y la plata de los Andes se transmutaban en suntuosidad palaciega, la arquitectura civil y religiosa desarrolló una personalidad inconfundible. Las residencias de la nobleza criolla se organizaban alrededor de amplios patios empedrados con mosaicos sevillanos, caballerizas señoriales y portadas monumentales de piedra labrada. Pero el elemento visual que consagró a Lima como una urbe de fábula fueron sus balcones voladizos de madera. Tallados primorosamente en cedro nicaragüense y roble por carpinteros moriscos y mestizos, estos balcones cerrados con celosías geométricas de influencia mudéjar sobresalían sobre las estrechas calles coloniales, permitiendo la ventilación cruzada y resguardando a los moradores del sol.",
                "Los balcones no eran simples apéndices decorativos: constituían el escenario privilegiado de la vida social y el espionaje urbano. Protegidas tras las tupidas mallas de celosía que dejaban pasar la luz pero impedían ver hacia el interior, las familias aristocráticas observaban sin ser advertidas el desfile incesante de carruajes dorados, pregones de vendedores ambulantes y solemnes procesiones religiosas como la del Señor de los Milagros. Los balcones funcionaban como ojos invisibles desde donde se tejían intrigas políticas, alianzas matrimoniales y romances secretos en una sociedad rígidamente vigilada por el Tribunal del Santo Oficio de la Inquisición.",
                "En este ambiente de vigilancia y ceremonia cortesana surgió una de las figuras más enigmáticas y transgresoras de la historia urbana americana: la tapada limeña, inmortalizada en las sátiras y relatos de Ricardo Palma en sus *Tradiciones peruanas*. Vistiendo una falda ajustada a la cintura llamada saya y un manto de seda negra que cubría por completo la cabeza y los hombros dejando al descubierto un único ojo centelleante, las mujeres limeñas de todas las clases sociales lograron una libertad de movimiento inusitada. Bajo el anonimato perfecto que les confería el disfraz, la tapada podía pasear sola por las plazas, coquetear con pretendientes desconocidos, burlarse de los magistrados y opinar de política sin temor a ser reconocida o censurada por sus padres o esposos.",
                "Al mismo tiempo, la fe católica moldeaba el corazón espiritual de la urbe con una intensidad fervorosa. En los claustros mudéjares del Convento de San Francisco, con sus zócalos de azulejos sevillanos de 1620 y su fastuosa biblioteca de pergaminos antiguos, se construyó una vasta red de catacumbas subterráneas abovedadas que sirvió como el camposanto principal de la ciudad hasta principios del siglo XIX. Decenas de miles de osamentas colocadas en patrones geométricos dentro de criptas de cal y canto atestiguan hoy la familiaridad devota con la que los limeños convivían con la memoria de la muerte y la esperanza de la salvación eterna.",
                "En este mismo suelo floreció la devoción a Santa Rosa de Lima (1586-1617), la primera santa canonizada de América, célebre por su austeridad mística, sus curaciones milagrosas y su solidaridad incansable con los enfermos e indígenas desamparados. Al recorrer hoy el Jirón de la Unión y contemplar los balcones restaurados de la Casa de Torre Tagle y el Palacio de Osambela, el viajero percibe que Lima guarda en sus celosías de madera la memoria de una época donde la devoción ascética, el boato virreinal y la picardía criolla forjaron el señorío eterno de la Ciudad de los Reyes."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál era la ventaja social fundamental que el traje de 'la tapada limeña' brindaba a las mujeres virreinales?",
                        "options": [
                            "Les otorgaba anonimato total mediante un manto que dejaba un solo ojo libre, permitiéndoles circular y expresarse sin tutela.",
                            "Les permitía ingresar como oficiales al ejército virreinal sin ser detectadas.",
                            "Las protegía del frío ártico durante los meses del verano costero.",
                            "Era el uniforme obligatorio dictado por la Inquisición para todas las damas nobles."
                        ],
                        "correctIndex": 0,
                        "explanation": "La saya y el manto que dejaba un único ojo visible garantizaba anonimato, otorgando a las mujeres libertad e independencia inusuales."
                    },
                    {
                        "question": "¿Qué función práctica y social cumplían los balcones de celosía tallada en las calles de la Lima colonial?",
                        "options": [
                            "Permitían ventilar las casas y observar la vida pública sin ser visto desde la calle, preservando la intimidad familiar.",
                            "Servían exclusivamente como puestos de guardia militar para disparar cañones durante asaltos piratas.",
                            "Eran almacenes exteriores donde se colgaban las piezas de carne salada para que se secaran al sol.",
                            "Funcionaban como celdas de castigo para los esclavos cimarrones capturados."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las celosías mudéjares facilitaban la ventilación y permitían a los habitantes vigilar el espacio público con privacidad."
                    },
                    {
                        "question": "¿Qué monumento religioso de Lima alberga un vasto complejo de catacumbas subterráneas coloniales?",
                        "options": [
                            "El Convento y Basílica de San Francisco.",
                            "La Fortaleza del Real Felipe en el Callao.",
                            "El Palacio de Gobierno en la Plaza Mayor.",
                            "El Teatro Municipal de Lima."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las catacumbas bajo el Convento de San Francisco funcionaron como el camposanto subterráneo de la ciudad hasta inicios del siglo XIX."
                    }
                ]
            }
        }
    }

    # Regional Story 3: Herencia afroperuana y Chincha
    story_peru_03 = {
        "id": "b2-peruandino-03", # Will be mapped to b2-perucosta-03
        "title": "El latido negro de la costa: Chincha, el cajón y la décima",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una inmersión cultural y musical en la herencia afroperuana: las haciendas algodoneras y azucareras de Chincha y Cañete, la resistencia de los cimarrones, el nacimiento del cajón peruano como instrumento de percusión libertaria, la danza del festejo y el landó, y la inmortal poesía en décimas de Nicomedes Santa Cruz.",
        "characters": [
            "Don Amador Ballumbrosio",
            "Poeta Nicomedes Santa Cruz",
            "Coreógrafa Victoria Santa Cruz",
            "Joven cajonero Miguel"
        ],
        "narration": {
            "paragraphs": [
                "Al sur de Lima, donde el desierto costero es acariciado por los vientos marinos de la bahía de Pisco, se extiende el valle de Chincha y el entrañable distrito de El Carmen. En este rincón bendecido por el sol, el aroma a sopa seca y carapulcra con chancho flota en el aire de las cocinas campesinas, mientras desde el patio sombreado de haciendas solariegas como San José —célebre por sus extensas catacumbas subterráneas donde se recluía a los cautivos— comienza a brotar un ritmo sincopado, grave y vibrante que parece surgir de las entrañas mismas de la tierra. Es el golpe de una palma morena sobre una caja de madera de cedro: el sonido inconfundible del cajón peruano, el instrumento emblemático que convirtió el dolor de la esclavitud en un canto inextinguible de orgullo, libertad y resistencia cultural.",
                "Durante los siglos de la dominación colonial y las primeras décadas republicanas, decenas de miles de africanos esclavizados, procedentes de las costas de Angola, Congo, Guinea y Mozambique, fueron desembarcados en el Callao para trabajar forzadamente en las extensas haciendas azucareras, algodoneras y vitivinícolas de la costa central y norteña. Despojados de su lengua originaria y de sus tambores rituales de piel de cabra, prohibidos taxativamente por los capataces por considerarlos diabólicos o inductores de rebeliones armadas, los trabajadores afroperuanos no renunciaron a su memoria sonora. Con ingenio indomable, transformaron las sencillas cajas rectangulares destinadas al transporte de pescado seco y frutos en cajas de resonancia rítmica.",
                "Sentándose a horcajadas sobre la madera y golpeando con las manos desnudas la cara delantera mientras regulaban los tonos graves en el centro y los agudos secos en el borde superior, los músicos negros crearon el cajón. Acompañado de la quijada de burro desecada cuyas piezas dentales vibran al ser golpeadas y de la cajita de madera con tapa basculante, este instrumento polifacético, capaz de replicar la complejidad polirrítmica de los cultos ancestrales africanos, se convirtió en el corazón palpitante del festejo alegre y sensual, del elegante landó de cadencia melancólica, del ágil zapateo criollo y de la marinera limeña. Siglos más tarde, el virtuoso guitarrista español Paco de Lucía quedaría fascinado por la precisión percusiva del instrumento durante una recepción diplomática en Lima en 1977, adoptándolo de inmediato para el flamenco contemporáneo e inmortalizando al cajón en los escenarios mundiales.",
                "Pero la rebelión afroperuana no solo se expresó con las manos sobre la madera, sino también con la palabra poética más afilada. En las campiñas costeras floreció el arte oral de la décima espinela, una estrofa poética de diez versos octosílabos con rima consonante heredada del Siglo de Oro español que las comunidades negras se apropiaron con maestría para cultivar el contrapunto lírico y cantar a sus antepasados cimarrones: aquellos esclavos prófugos que escapaban hacia los bosques de cañaverales para fundar palenques libres en las quebradas desérticas.",
                "La cumbre de esta dignidad poética cristalizó en el siglo XX a través de la obra monumental de Nicomedes Santa Cruz (1925-1992). Periodista, poeta e investigador infatigable, Nicomedes rescató la décima de los círculos campesinos marginados y la elevó a la categoría de literatura mayor continental, denunciando el racismo estructural, narrando la epopeya de los barrios criollos de Lima y tejiendo lazos de solidaridad panafricana con sus versos inmortales de *Cumanana*. Junto a él, su hermana Victoria Santa Cruz estremeció las conciencias con su célebre poema coreográfico *¡Me gritaron negra!*, una lección sublime sobre cómo transformar la herida del insulto racista en un grito libertario de autoestima y afirmación identitaria.",
                "En las celebraciones de la Virgen del Carmen en Chincha, la familia Ballumbrosio, custodios de una dinastía de violinistas y cajoneros prodigiosos liderada por el patriarca Don Amador, continúa congregando a multitudes para zapatear al compás del atajo de negritos. Al escuchar el retumbar del cajón y las décimas recitadas con altivez frente al mar Pacífico, se comprende que la identidad peruana no se explica sin la huella indeleble de sus pueblos negros, cuya alegría desafiante y maestría rítmica continúan enriqueciendo el patrimonio espiritual del planeta."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿De qué manera ingeniosa surgió el cajón peruano entre los trabajadores afrodescendientes esclavizados en la costa?",
                        "options": [
                            "Al prohibírseles sus tambores ancestrales de cuero, utilizaron cajas de madera de embalaje para recrear sus polirritmias.",
                            "Fue inventado por un fabricante de pianos alemán que abrió una tienda en el puerto del Callao.",
                            "Se construyó a partir de los mástiles de madera recuperados de los barcos de guerra coloniales.",
                            "Fue un obsequio protocolar traído por marineros mercantes desde las islas Filipinas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Ante la prohibición de sus tambores africanos, los esclavos emplearon cajones de embalaje de madera como instrumentos de percusión."
                    },
                    {
                        "question": "¿Qué guitarrista español de renombre mundial adoptó el cajón peruano tras una gira por Lima en 1977?",
                        "options": [
                            "Paco de Lucía.",
                            "Andrés Segovia.",
                            "Carlos Santana.",
                            "Vicente Amigo."
                        ],
                        "correctIndex": 0,
                        "explanation": "Paco de Lucía descubrió el cajón en Lima en 1977 y lo integró definitivamente al género flamenco en todo el mundo."
                    },
                    {
                        "question": "¿Cuál fue el mensaje central del célebre poema escénico '¡Me gritaron negra!' de Victoria Santa Cruz?",
                        "options": [
                            "La superación del dolor del insulto racista para transformarlo en una afirmación orgullosa y consciente de su identidad afrodescendiente.",
                            "Un llamado a abandonar el Perú y emigrar hacia los países del norte de Europa.",
                            "Una protesta contra los altos impuestos cobrados por el municipio de Lima a los teatros.",
                            "Una alabanza a las técnicas de pintura al óleo enseñadas en las academias virreinales."
                        ],
                        "correctIndex": 0,
                        "explanation": "Victoria Santa Cruz convirtió la agresión racista vivida en la infancia en un himno de autoafirmación y orgullo identitario."
                    }
                ]
            }
        }
    }

    # Regional Story 4: Gastronomía
    story_peru_04 = {
        "id": "b2-peruandino-04", # Will be mapped to b2-perucosta-04
        "title": "La revolución en el plato: Cebiche, fusión nikkei y diplomacia del sabor",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la explosión culinaria peruana: el cebiche tradicional declarado Patrimonio de la Humanidad por la UNESCO, la frescura del limón sutil y el ají limo, el nacimiento del chifa con la migración cantonesa del siglo XIX, la sofisticación del tiradito nikkei y el papel de la gastronomía como motor de orgullo y reconciliación nacional.",
        "characters": [
            "Chef Gastón",
            "Maestro de cocina nikkei Humberto Sato",
            "Cebichero Don Augusto",
            "Agricultora de ajíes doña Juana"
        ],
        "narration": {
            "paragraphs": [
                "Al filo del mediodía en una bulliciosa cebichería del muelle pesquero de Chorrillos, los comensales aguardan con mirada anhelante mientras el cocinero ejecuta un ritual que combina la precisión de un cirujano con la pasión de un alquimista. Sobre una tabla de madera limpia, filetea dados uniformes de corvina fresca capturada apenas tres horas antes en el océano Pacífico. Vierte sobre el pescado sal marina gruesa, una lluvia de cebolla roja cortada en pluma fina, un puñado de cilantro picado y rodajas de ají limo aromático. Finalmente, exprime al instante varios limones sutiles recién cosechados en los valles del norte: en cuestión de segundos, el jugo cítrico interactúa con las proteínas del pescado tiñendo el líquido de una emulsión blancuzca, lechosa y vibrante bautizada popularmente como 'leche de tigre'.",
                "El cebiche peruano, declarado por la UNESCO en 2023 como Patrimonio Cultural Inmaterial de la Humanidad, es la síntesis perfecta del encuentro milenario entre el mar y la tierra. Mucho antes de la llegada de los europeos, los pescadores de las culturas Moche y Chimú ya maceraban el pescado fresco con jugos fermentados de tumbo, una fruta ácida de la selva alta, o con chicha de maíz. La posterior incorporación de la cebolla y los cítricos mediterráneos por los conquistadores españoles, combinada con la generosidad de los ajíes nativos como el limo y el amarillo, forjó un plato universal que en cada caleta costeña se sirve tradicionalmente escoltado por trozos de camote dulce cocido y granos crujientes de choclo o maíz tostado (cancha).",
                "Sin embargo, la cocina peruana contemporánea no se explica únicamente por sus raíces prehispánicas y coloniales, sino por su extraordinaria capacidad para abrazar y reinterpretar las oleadas migratorias que arribaron a sus costas durante los siglos XIX y XX. A mediados del siglo XIX, miles de trabajadores chinos procedentes de la región de Cantón llegaron al Perú para laborar en las islas guaneras y las haciendas algodoneras bajo contratos draconianos de servidumbre ('culíes'). Al culminar sus contratos de endeudamiento, muchos se instalaron en el corazón comercial de Lima fundando pequeños comedores que el pueblo bautizó como *chifas* (derivado de la expresión cantonesa *chi fan*, que significa 'comer arroz').",
                "En los woks ardientes de los chifas limeños, las técnicas de salteado a fuego vivo se fusionaron con la cebolla roja, el ají amarillo y las carnes peruanas, alumbrando obras maestras cotidianas como el lomo saltado, el arroz chaufa y la sopa wantán. Paralelamente, la llegada de migrantes japoneses a partir de 1899 aportó una segunda revolución estética: la cocina *nikkei*. Maestros legendarios como Minoru Kunigami y Humberto Sato revolucionaron la mirada criolla sobre los recursos marinos, acortando los tiempos de maceración del cebiche —que antaño se dejaba reposar durante horas hasta cocerse en exceso— y creando el *tiradito*: láminas delicadas de pescado crudo cortadas como sashimi japonés, sin cebolla, marinadas en salsas emulsionadas de ají amarillo y jengibre.",
                "En las últimas dos décadas, esta confluencia de tradiciones dio origen a lo que analistas internacionales denominan el 'milagro gastronómico peruano'. Liderada por cocineros innovadores como Gastón Acurio, Virgilio Martínez y Mitsuharu Tsumura, la gastronomía trascendió el ámbito de los restaurantes para convertirse en una poderosa herramienta de diplomacia cultural, turismo internacional y cohesión social. En un país históricamente fragmentado por tensiones geográficas y sociales, la mesa compartida funcionó como un territorio neutral de reconciliación colectiva, donde todos los peruanos se reconocían orgullosamente en la excelencia de sus sabores.",
                "En las ferias gastronómicas internacionales como Mistura y en los mercados populares de abastos, la cocina peruana demuestra que su mayor fortaleza radica en la biodiversidad de sus materias primas y en el respeto por los pequeños agricultores y pescadores artesanales. Al degustar un tiradito nikkei, una causa limeña de papa amarilla o un tacu-tacu con mariscos frente al mar de Grau, el comensal comprende que la cocina en el Perú no es una simple manifestación culinaria: es un testimonio conmovedor de cómo la diversidad cultural puede dialogar en armonía para enriquecer la mesa de toda la humanidad."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué distinción técnica y visual caracteriza al 'tiradito' de influencia nikkei frente al cebiche tradicional?",
                        "options": [
                            "Se corta en láminas finas estilo sashimi japonés, prescinde de cebolla y se baña con emulsiones de ají y cítricos al momento.",
                            "Se cocina en un horno de leña durante varias horas con abundante queso derretido.",
                            "Lleva pescado ahumado importado de los mares nórdicos servido con fideos de arroz.",
                            "Se elabora exclusivamente con frutas tropicales dulces sin sal ni picante."
                        ],
                        "correctIndex": 0,
                        "explanation": "El tiradito adopta el corte japonés del sashimi, no utiliza cebolla y se adereza con una crema de ají al momento."
                    },
                    {
                        "question": "¿De qué término de la lengua cantonesa se origina el nombre popular de los restaurantes 'chifa' en el Perú?",
                        "options": [
                            "De la frase 'chi fan', que significa literalmente 'comer arroz' en dialecto cantonés.",
                            "Del apellido del primer embajador imperial chino en la ciudad de Lima.",
                            "Del nombre de una especia picante originaria de la provincia de Sichuan.",
                            "De una palabra quechua que designaba a las ollas de barro para cocinar sopas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Chifa proviene del cantonés 'chi fan' (comer arroz), término que usaban los cocineros para llamar a comer a los comensales."
                    },
                    {
                        "question": "¿Qué papel sociopolítico desempeñó la revolución gastronómica en el Perú durante las últimas dos décadas?",
                        "options": [
                            "Actuó como motor de orgullo identitario y cohesión social unificando a diversos sectores del país en torno a su cocina.",
                            "Provocó la prohibición de todos los productos alimenticios importados del exterior.",
                            "Obligó al Estado a sustituir la moneda nacional por bonos canjeables en restaurantes.",
                            "Eliminó la agricultura tradicional en favor de la producción de alimentos artificiales sintéticos."
                        ],
                        "correctIndex": 0,
                        "explanation": "La gastronomía se transformó en un símbolo de orgullo patrio y encuentro social que ayudó a integrar culturalmente a la nación."
                    }
                ]
            }
        }
    }

    # Regional Story 5: Iquitos y Amazonia
    story_peru_05 = {
        "id": "b2-peruandino-05", # Will be mapped to b2-perucosta-05
        "title": "Iquitos: La isla continental de la selva y el espejismo del caucho",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía fluvial por la Amazonia peruana: la ciudad de Iquitos como metrópoli sin carreteras, el nacimiento del río Amazonas en la confluencia del Marañón y el Ucayali, la época dorada y brutal de la fiebre del caucho, la arquitectura europea de la Casa de Fierro y la resistencia del arte indígena shipibo-konibo con sus trazos sagrados de kené.",
        "characters": [
            "Navegante fluvial Don Manuel",
            "Historiadora amazónica Rosa",
            "Artesana shipiba Olinda Silvano",
            "Joven naturalista Carlos"
        ],
        "narration": {
            "paragraphs": [
                "Para llegar a Iquitos, la ciudad de casi medio millón de habitantes situada en el departamento de Loreto, ningún vehículo terrestre puede encender sus motores en la costa o en los Andes: sencillamente no existen carreteras que crucen la inmensidad verde de la llanura amazónica. Conectada con el resto del planeta únicamente por vía aérea o a través de singladuras fluviales de varios días por las aguas caudalosas del río Amazonas, Iquitos es la mayor urbe del mundo continental inaccesible por carretera. Rodeada por los ríos Nanay, Itaya y el coloso Amazonas, la ciudad late con un calor húmedo e hipnótico, donde el zumbido de millares de mototaxis se mezcla con el canto de aves tropicales y el olor a pescado de río ahumado en las esquinas de Belén.",
                "A menos de cien kilómetros al sur de Iquitos, en la reserva nacional Pacaya Samiria, se produce el nacimiento hidrológico oficial del río más largo y caudaloso de la Tierra: la unión solemne de las aguas barrosas y torrentosas del río Marañón con las corrientes serenas del río Ucayali, ambas alimentadas por el deshielo de los glaciares andinos a miles de kilómetros de distancia. En este laberinto fluvial de aguas negras y blancas habitan delfines rosados, nutrias gigantes, manatíes y paiches gigantescos de tres metros de longitud, mientras las comunidades ribereñas adaptan sus casas sobre pilotes de madera de capirona para resistir las subidas cíclicas del río durante la temporada de lluvias.",
                "Sin embargo, el destino urbano de Iquitos cambió radicalmente a finales del siglo XIX con el estallido de la 'fiebre del caucho' (1880-1914). El descubrimiento del proceso de vulcanización por Charles Goodyear y la demanda voraz de neumáticos para las nacientes industrias del automóvil y la bicicleta en Europa y Estados Unidos transformaron al látex de los árboles de la selva (*Hevea brasiliensis*) en el 'oro blanco' de la Amazonia. En pocos años, una modesta aldea de misioneros y pescadores se convirtió en un emporio comercial de opulencia desmedida, donde los magnates caucheros o 'barones del caucho' amasaron fortunas fabulosas exportando miles de toneladas de resina desde su puerto fluvial con destino a los mercados de Londres y Nueva York.",
                "La opulencia de aquella época dorada dejó una impronta arquitectónica estrafalaria y deslumbrante en plena selva virgen. Los barones construyeron mansiones palaciegas revestidas con azulejos portugueses pintados a mano, instalaron farolas de gas importadas de Inglaterra y enviaban su ropa sucia a lavar en barcos de vapor hasta París. El hito supremo de este delirio modernista fue la legendaria Casa de Fierro, diseñada por los talleres parisinos de Gustave Eiffel y exhibida en la Exposición Universal de París de 1889: comprada por un magnate cauchero, la estructura prefabricada de láminas de hierro forjado fue transportada en barcazas a través del Atlántico y ensamblada tornillo a tornillo en la Plaza de Armas de Iquitos, donde todavía asombra a los visitantes.",
                "Pero detrás de aquel espejismo de lujo y ópera europea latía una tragedia humanitaria atroz. Para extraer el caucho en los bosques más recónditos de la cuenca del río Putumayo, corporaciones inescrupulosas como la Peruvian Amazon Company del sanguinario Julio César Arana sometieron a decenas de miles de indígenas witotos, boras y ocainas a un régimen de esclavitud brutal, torturas y trabajo forzado mediante el sistema de endeudamiento artificial. Este holocausto selvático, denunciado ante el parlamento británico en 1912 por el cónsul Roger Casement, diezmó a poblaciones ancestrales enteras antes de que el contrabando de semillas de caucho a Malasia provocara el colapso definitivo del monopolio amazónico.",
                "Hoy, Iquitos renace abrazando su verdadera identidad amazónica y reivindicando el arte y la sabiduría de sus pueblos originarios. En el barrio de Cantagallo y en las comunidades del río Ucayali, maestras como Olinda Silvano despliegan la belleza geométrica del *kené*: un arte pictórico sagrado del pueblo Shipibo-Konibo donde mujeres sabias trazan con tintes naturales de barro y cortezas de caoba intrincados laberintos que representan las constelaciones, los ríos y los cantos chamánicos del bosque. Iquitos demuestra que la selva viva no es un recurso extractivo inagotable, sino un santuario sagrado cuya supervivencia depende del respeto irrestricto por los pueblos que la han protegido durante milenios."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál es la singularidad geográfica que define el acceso a la ciudad de Iquitos frente a otras urbes de su tamaño en el mundo?",
                        "options": [
                            "Es la mayor metrópoli continental del planeta sin conexión por carretera, accesible solo por río o por avión.",
                            "Está situada en una isla flotante de totora en el centro de un cráter volcánico activo.",
                            "Solo puede visitarse en trineos durante los meses de invierno por el congelamiento del río.",
                            "Fue construida bajo tierra en cavernas de piedra para evitar la luz solar."
                        ],
                        "correctIndex": 0,
                        "explanation": "Iquitos es la mayor ciudad del mundo continental sin acceso por carretera: solo se llega por avión o navegando los ríos."
                    },
                    {
                        "question": "¿Qué monumento histórico prefabricado en París fue traído por piezas y ensamblado en la Plaza de Armas de Iquitos durante el auge del caucho?",
                        "options": [
                            "La Casa de Fierro, atribuida a los talleres del célebre ingeniero francés Gustave Eiffel.",
                            "Una réplica exacta del Arco de Triunfo de mármol de Normandía.",
                            "Un campanario de madera de pino fabricado en los talleres de la corte vienesa.",
                            "Una estación de metro subterráneo con vagones de madera importados de Londres."
                        ],
                        "correctIndex": 0,
                        "explanation": "La Casa de Fierro, diseñada en los talleres de Eiffel y exhibida en París en 1889, fue montada con planchas de hierro en Iquitos."
                    },
                    {
                        "question": "¿Qué representa el arte tradicional del 'kené' en la cosmovisión del pueblo indígena Shipibo-Konibo?",
                        "options": [
                            "Laberintos geométricos sagrados que plasman las constelaciones, las rutas fluviales y los cantos curativos chamánicos.",
                            "Códigos numéricos para calcular el precio del caucho y la madera de exportación.",
                            "Mapas militares para organizar incursiones de conquista sobre pueblos vecinos.",
                            "Dibujos cómicos creados para entretener a los turistas en los paseos en canoa."
                        ],
                        "correctIndex": 0,
                        "explanation": "El kené es un diseño geométrico sagrado shipibo que visualiza la energía de plantas maestras, constelaciones y cantos de curación."
                    }
                ]
            }
        }
    }

    # Regional Story 6: Capstone regional (El mar de Grau, el desierto y la Lima diversa)
    story_peru_capstone = {
        "id": "b2-perucosta-consolidation",
        "title": "La costa fecunda: El abrazo del desierto, el océano y la Lima mestiza",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis panorámica de los Estudios Regionales sobre el litoral y la cuenca fluvial peruana: la riqueza marina de la corriente de Humboldt, la herencia señorial de los balcones y conventos de la Lima virreinal, la resistencia poética y musical de las comunidades afroperuanas de Chincha, la vanguardia gastronómica nikkei y chifa, y la integración amazónica desde Iquitos.",
        "characters": [
            "Nicomedes Santa Cruz",
            "Doña Rosa de Lima",
            "Maestro Humberto Sato",
            "Artesana Olinda Silvano"
        ],
        "narration": {
            "paragraphs": [
                "A lo largo de más de tres mil kilómetros de litoral bañados por el océano Pacífico, la costa peruana se extiende como una de las geografías más singulares, contrastantes y fascinantes de todo el planeta Tierra. Flanqueada al oriente por la muralla colosal de la cordillera de los Andes y acariciada al poniente por las aguas gélidas de la corriente de Humboldt, esta angosta faja territorial desafía todas las leyes convencionales del clima: en ella coexisten la aridez hiperárida de dunas desérticas inmensas con la biomasa marina más densa y prolífica del globo, forjando un escenario donde la tenacidad humana demostró desde tiempos inmemoriales que la escasez de agua no es una condena, sino un estímulo permanente para la creatividad civilizatoria.",
                "En el mar de Grau, el milagroso fenómeno del afloramiento costero de nutrientes minerales transforma el océano en una cantera inagotable de vida que sustenta a gigantescos cardúmenes de anchoveta y a millones de aves guaneras, cuyas deyecciones enriquecieron el suelo agrícola de medio mundo durante el siglo XIX. Esta generosidad marina fertiliza también a los más de cincuenta valles aluviales que serpentean por la pampa desértica, donde los antiguos pobladores de Paracas, Nasca y Chimú construyeron canales de irrigación subterráneos y trazaron sobre las planicies petroglifos astronómicos que continúan desafiando el enigma del tiempo.",
                "En el corazón geográfico y político de este litoral árido resplandece la metrópoli de Lima, fundada en 1535 como la Ciudad de los Reyes. Durante el virreinato, la capital peruana articuló el poderío administrativo y eclesiástico de América del Sur entre el incienso de sus catedrales barrocas, las criptas secretas de las catacumbas franciscanas y los refinados balcones voladizos de celosía tallada en cedro. Detrás de esas celosías mudéjares, las célebres tapadas limeñas conquistaron un espacio insólito de anonimato y libertad de pensamiento, mientras santos de conmovedora devoción como Santa Rosa y San Martín de Porres sembraban las semillas de una espiritualidad mestiza y solidaria.",
                "Hacia el sur, en los fértiles valles algodoneros de Chincha y Cañete, la memoria ancestral de los pueblos afroperuanos convirtió el desgarro de la esclavitud en un patrimonio musical que asombra al mundo. Al reinventar cajas de embalaje para crear el cajón peruano y al cultivar con altivez las décimas de pie quebrado inmortalizadas por Nicomedes y Victoria Santa Cruz, las comunidades morenas dotaron a la identidad criolla de su latido rítmico más apasionado, demostrando que la cultura popular es el arma suprema para derrotar la opresión y dignificar la memoria de los cimarrones.",
                "Esa misma vocación mestiza e integradora protagonizó en las últimas décadas una auténtica revolución en el plato. Al conjugar la frescura marina del cebiche tradicional con el legado cantonés del chifa y la precisión milimétrica del tiradito nikkei, la gastronomía peruana se consagró como un fenómeno cultural de resonancia planetaria y, al mismo tiempo, como un territorio de reconciliación nacional donde la diversidad de ingredientes andinos, costeños y selváticos simboliza la unidad de un país que celebra con orgullo su mestizaje infinito.",
                "Y más allá de la muralla andina, en la llanura inaccesible por carretera donde nace el río Amazonas, la ciudad fluvial de Iquitos enlaza el destino de la costa con el corazón latente de la Amazonia. Desde el espejismo opulento de la fiebre del caucho y la Casa de Fierro hasta los trazos sagrados del kené shipibo que representan la armonía de la selva virgen, Iquitos recuerda que el Perú no termina en el litoral, sino que dialoga íntimamente con los bosques y los ríos que nutren el pulmón ecológico del continente.",
                "Al contemplar la trayectoria inmemorial de la costa peruana, el viajero comprende que su grandeza no reside en la uniformidad de un paisaje, sino en la maravillosa convivencia de sus contrastes. En este territorio donde el desierto abraza al mar frío y donde los pregones coloniales se funden con los acordes del cajón y las humaredas perfumadas del lomo saltado, el Perú contemporáneo proyecta hacia el futuro una lección de dignidad inagotable: que la verdadera riqueza de las naciones brota del encuentro generoso, fraterno y creativo entre todos sus pueblos."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué dos fuerzas geográficas determinan el carácter árido pero hiperproductivo de la costa peruana?",
                        "options": [
                            "La cordillera de los Andes que frena las lluvias orientales y la corriente fría de Humboldt que genera surgencia marina.",
                            "Los glaciares del Caribe y los vientos alisios provenientes del Polo Norte.",
                            "Los tifones ecuatoriales y las selvas pantanosas de manglares continuos.",
                            "Las mareas volcánicas subterráneas y las dunas de sal del Altiplano."
                        ],
                        "correctIndex": 0,
                        "explanation": "La barrera andina y la corriente polar de Humboldt crean el desierto costero y simultáneamente la biomasa marina más rica del planeta."
                    },
                    {
                        "question": "¿De qué manera la herencia afroperuana y las migraciones asiáticas transformaron la identidad de la costa peruana?",
                        "options": [
                            "Aportaron el ritmo del cajón, la poesía de la décima y la revolución culinaria del chifa y la cocina nikkei.",
                            "Obligaron a la población a abandonar el idioma castellano en favor del latín medieval.",
                            "Sustituyeron todas las iglesias coloniales por fábricas de ensamblaje textil industrial.",
                            "Prohibieron la pesca marina estableciendo una economía puramente ganadera."
                        ],
                        "correctIndex": 0,
                        "explanation": "Los afroperuanos aportaron el cajón y la décima, mientras las migraciones cantonesa y japonesa crearon el chifa y la fusión nikkei."
                    },
                    {
                        "question": "¿Cuál es el valor simbólico de la gastronomía contemporánea en la sociedad peruana del siglo XXI?",
                        "options": [
                            "Constituye un factor aglutinador de orgullo identitario que une a diversos sectores del país a través de la diversidad de sus platos.",
                            "Es una actividad económica menor que solo interesa a los turistas extranjeros en los hoteles de lujo.",
                            "Ha provocado el cierre de todos los mercados populares tradicionales de las ciudades.",
                            "Es una réplica estricta de los menús de la realeza europea sin aportes autóctonos."
                        ],
                        "correctIndex": 0,
                        "explanation": "La gastronomía se erige como emblema de orgullo nacional y espacio de encuentro democrático y armónico entre culturas."
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
    write_json(f"stories/classics/b2/{c_unit}.json", to_schema_story(story_core_19))
    # Regional lesson stories:
    write_json(f"stories/world/b2/{r1}.json", to_schema_story(story_peru_01, r1))
    write_json(f"stories/world/b2/{r2}.json", to_schema_story(story_peru_02, r2))
    write_json(f"stories/world/b2/{r3}.json", to_schema_story(story_peru_03, r3))
    write_json(f"stories/world/b2/{r4}.json", to_schema_story(story_peru_04, r4))
    write_json(f"stories/world/b2/{r5}.json", to_schema_story(story_peru_05, r5))
    write_json(f"stories/world/b2/{r6_con}.json", to_schema_story(story_peru_capstone, r6_con))
    write_json(f"stories/world/b2/{r_unit}.json", to_schema_story(story_peru_capstone, r_unit))

    # -------------------------------------------------------------------------
    # 5. LESSON FILES (6 Core + 6 Regional)
    # -------------------------------------------------------------------------
    core_lessons_info = [
        ("b2-19-01", "lesson.b2.19.01", "Pasiva refleja básica y concordancia de número",
         "Master basic passive reflex constructions with 'se' and ensure strict subject-verb number agreement with postposed plural patients.",
         "pasiva refleja básica y concordancia estricta de número con el sujeto paciente",
         ["Formulate passive reflex sentences with 'se' and third-person verbs.", "Ensure mandatory plural agreement when the passive subject is plural (se firmaron los acuerdos).", "Differentiate passive patients from direct objects."]),
        ("b2-19-02", "lesson.b2.19.02", "Pasiva refleja frente a impersonal con se",
         "Distinguish reflexive passives with plural inanimate subjects from strictly impersonal 'se' clauses introducing animate patients with 'a'.",
         "distinción entre pasiva refleja e impersonalidad sintáctica con se y marca de acusativo 'a'",
         ["Apply invariant singular verb agreement in impersonal clauses with personal 'a' (se atendió a las víctimas).", "Contrast inanimate reflexive passives with human impersonal structures.", "Avoid erroneous pluralization in impersonal human clauses (*se atendieron a las víctimas)."]),
        ("b2-19-03", "lesson.b2.19.03", "Restricciones de agentividad en la pasiva refleja",
         "Examine semantic agency constraints and agent omission in reflexive passive clauses versus analytical passives.",
         "restricciones de agentividad implícita y omisión del complemento agente en la pasiva refleja",
         ["Recognize why reflexive passives reject overt agent complements with 'por'.", "Select between reflexive passives (agentless) and analytical passives (overt agent).", "Deploy natural journalistic and institutional prose without awkward agent phrases."]),
        ("b2-19-04", "lesson.b2.19.04", "El se en el discurso administrativo y legal",
         "Deploy the impersonal and reflexive 'se' in decrees, judicial rulings, minutes, and administrative edicts.",
         "uso de la pasiva refleja e impersonal en registros jurídicos, administrativos y notariales",
         ["Formulate performative legal resolutions using 'se dispone', 'se resuelve', and 'se notifica'.", "Confer formal institutional objectivity to executive decrees and official communiqués.", "Structure solemn legislative clauses adhering to legal drafting house style."]),
        ("b2-19-05", "lesson.b2.19.05", "Desambiguación pragmática de las funciones de se",
         "Disambiguate among reflexive, reciprocal, inchoative, and passive meanings of the multi-functional pronoun 'se'.",
         "desambiguación contextual y pragmática de los valores reflexivo, recíproco y pasivo de se",
         ["Distinguish reciprocal interpretations from passive reflexives in plural animated contexts.", "Differentiate pronominal aspectual nuances from true passive structures.", "Analyze ambiguous sentences and restructure them for crystal-clear clarity."])
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
        "id": "lesson.b2.19.consolidation",
        "title": "Consolidación B2: Pasiva refleja e impersonalidad en La ciudad y los perros",
        "level": "B2",
        "goal": "Synthesize reflexive passive and impersonal 'se' structures through Mario Vargas Llosa's military academy masterpiece La ciudad y los perros.",
        "grammar": "síntesis de voz pasiva refleja, impersonalidad con se y adaptación de La ciudad y los perros",
        "sections": [
            {"type": "goal", "items": [
                "Master the distinction between plural reflexive passives and singular animate impersonals.",
                "Deploy institutional and journalistic 'se' constructions with stylistic precision.",
                "Analyze institutional authoritarianism, omertà, and social hypocrisy in Vargas Llosa's novel."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{l6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Aplico la concordancia de número en la pasiva refleja con sujetos pacientes plurales.",
                "Mantengo el verbo en singular cuando el objeto humano lleva la preposición 'a'.",
                "Evito la inclusión forzada de complementos agentes con 'por' en pasivas reflejas.",
                "Desambiguo con soltura los distintos valores pragmáticos del pronombre 'se'."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-perucosta-01", "lesson.b2.perucosta.01", "El desierto costero y la corriente de Humboldt",
         "Explore the marine geography of the Humboldt Current, upwelling ecology, and coastal hyper-aridity.",
         "oceanografía de la corriente de Humboldt, afloramiento marino y clima desértico costero",
         ["Analyze the physical upwelling mechanism of deep nutrient-rich Antarctic waters.", "Examine the role of the thermal inversion layer in generating the Lima winter garúa.", "Deploy marine biology, fishery, and climatic vocabulary (afloramiento, garúa, anchoveta, biomasa)."]),
        ("b2-perucosta-02", "lesson.b2.perucosta.02", "Lima virreinal: Balcones de celosía y señorío",
         "Investigate the viceregal architecture of Lima, Mudejar latticed balconies, and the tapada limeña phenomenon.",
         "urbanismo colonial de Lima, balcones voladizos de celosía mudéjar y sociedad virreinal",
         ["Analyze the architectural palimpsest of the City of Kings founded in 1535.", "Explore the unique social anonymity and freedom exercised by the tapadas limeñas.", "Deploy colonial history, viceregal aristocracy, and architecture vocabulary (celosía, virreinato, señorío, conventual)."]),
        ("b2-perucosta-03", "lesson.b2.perucosta.03", "La herencia afroperuana: Chincha, el cajón y la décima",
         "Examine Afro-Peruvian history in Chincha, the creation of the cajón box drum, and Nicomedes Santa Cruz's poetry.",
         "historia afroperuana, etnomusicología del cajón y poesía en décimas de Nicomedes Santa Cruz",
         ["Trace the historical creation of the cajón from wooden crates by enslaved coastal workers.", "Analyze the lyrical and social power of the décima espinela and Afro-descendant dignity.", "Deploy musicological, percussion, and oral literature vocabulary (cajón, décima, zapateo, festejo)."]),
        ("b2-perucosta-04", "lesson.b2.perucosta.04", "La revolución gastronómica: Cebiche, chifa y fusión nikkei",
         "Analyze contemporary Peruvian culinary diplomacy, UNESCO-recognized cebiche, and chifa and nikkei fusions.",
         "sociología gastronómica peruana, patrimonio inmaterial del cebiche y mestizaje culinario chifa y nikkei",
         ["Analyze traditional cebiche preparation with lime, chili, and fresh marine catch.", "Explore the historical origins of Cantonese chifa and Japanese nikkei innovations.", "Deploy culinary arts, fusion gastronomy, and cultural diplomacy vocabulary (cebiche, tiradito, chifa, nikkei)."]),
        ("b2-perucosta-05", "lesson.b2.perucosta.05", "Iquitos y el ciclo del caucho en la cuenca amazónica",
         "Explore the history of Iquitos as the world's largest roadless continental city, the rubber boom, and Shipibo art.",
         "historia de la Amazonia peruana, ciclo extractivo del caucho y cosmología del kené shipibo",
         ["Explore the unique geographic isolation and Amazon river hub status of Iquitos.", "Analyze the economic wealth and human rights tragedy of the 19th-century rubber boom.", "Deploy Amazonian geography, fluvial transport, and indigenous art vocabulary (caucho, fluvial, siringuero, kené)."])
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
        "id": "lesson.b2.perucosta.consolidation",
        "title": "Consolidación Regional: El mar de Grau, el desierto y la Lima diversa",
        "level": "B2",
        "goal": "Consolidate regional studies on coastal Peru: Humboldt marine ecology, viceregal Lima, Afro-Peruvian Chincha, gastronomic diplomacy, and Amazonian Iquitos.",
        "grammar": "síntesis de estudios regionales de la costa y oriente peruano: Humboldt, Lima virreinal, afroperuanidad y gastronomía",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize marine hydrology, Humboldt upwelling, and coastal desert ecology.",
                "Appreciate the viceregal architecture of Lima and Afro-Peruvian musical contributions.",
                "Reflect on the unifying power of Peruvian gastronomy and Amazonian river navigation."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r6_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{r6_con}-ex.json", "exerciseRefs": [f"{r6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la influencia de la corriente de Humboldt en el desierto costero peruano.",
                "Reconozco el valor patrimonial de los balcones de celosía y las tapadas de Lima.",
                "Valoro el aporte fundacional del cajón y la décima afroperuana.",
                "Explico la trascendencia de las fusiones nikkei y chifa en la cocina mundial.",
                "Entiendo el aislamiento fluvial y el pasado histórico de la ciudad de Iquitos."
            ]}
        ]
    })

    print("Completed LatAm Unit 19 (Peru Costa) generation!")

    # -------------------------------------------------------------------------
    # 6. UPDATE CURRICULUM UNITS (b2.json)
    # -------------------------------------------------------------------------
    b2_units_path = LATAM_DIR / "curriculum" / "units" / "b2.json"
    b2_units = json.loads(b2_units_path.read_text(encoding="utf-8"))
    
    # Check if Unit 19 entries already exist
    has_core_19 = any(u.get("title") == "The Passive with 'Se'" for u in b2_units)
    has_reg_19 = any(u.get("title") == "Peru II: The Pacific Coast, Lima & The Gastronomic Vanguard" for u in b2_units)
    
    if not has_core_19:
        b2_units.append({
            "title": "The Passive with 'Se'",
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
    if not has_reg_19:
        b2_units.append({
            "title": "Peru II: The Pacific Coast, Lima & The Gastronomic Vanguard",
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
    print("Updated curriculum/units/b2.json with Unit 19!")

    # -------------------------------------------------------------------------
    # 7. Word Count Audit for Stories
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_19", story_core_19),
        ("story_peru_01", story_peru_01),
        ("story_peru_02", story_peru_02),
        ("story_peru_03", story_peru_03),
        ("story_peru_04", story_peru_04),
        ("story_peru_05", story_peru_05),
        ("story_peru_capstone", story_peru_capstone)
    ]
    print("\n--- Story Word Count Audit ---")
    all_ok = True
    for name, s in stories_to_audit:
        full_text = " ".join(s["narration"]["paragraphs"])
        wc = count_words(full_text)
        status = "OK (650-825)" if 650 <= wc <= 825 else f"FAILED ({wc} words, must be 650-825)"
        print(f"{name:22}: {wc:4} words -> {status}")
        if not (650 <= wc <= 825):
            all_ok = False

    assert all_ok, "Some stories are out of the 650-825 word count bounds!"

if __name__ == "__main__":
    main()
