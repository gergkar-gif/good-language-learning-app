#!/usr/bin/env python3
"""
Generate Latin American Spanish (es-latam) B2 Unit 20:
- Core Unit 20: Analytical & Resultative Passives (Voz pasiva analítica y pasiva de estado)
  Classic literature: Alcides Arguedas - Raza de bronce (1919)
- Regional Unit 20: Bolivia I: The High Altiplano, Potosí & The Indigenous Majority State (b2-boliviaaltiplano)
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
    c_unit = "b2-20"
    r_unit = "b2-boliviaaltiplano"

    c1, c2, c3, c4, c5, l6_con = [f"{c_unit}-0{i}" for i in range(1, 6)] + [f"{c_unit}-consolidation"]
    r1, r2, r3, r4, r5, r6_con = [f"{r_unit}-0{i}" for i in range(1, 6)] + [f"{r_unit}-consolidation"]

    # -------------------------------------------------------------------------
    # 0. UPDATE REGISTRY & GRAMMAR TITLES
    # -------------------------------------------------------------------------
    reg_path = LATAM_DIR / "indexes" / "skill-registry.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    skills = registry.setdefault("skills", {})

    new_skills = {
        "b2-20-vocab": {"kind": "vocabulary", "level": "B2"},
        "pasiva-analitica-ser-participio": {"kind": "grammar", "level": "B2"},
        "pasiva-complemento-agente-por": {"kind": "grammar", "level": "B2"},
        "pasiva-estado-estar-participio": {"kind": "grammar", "level": "B2"},
        "participios-irregulares-dobles": {"kind": "grammar", "level": "B2"},
        "seleccion-estilistica-pasivas": {"kind": "grammar", "level": "B2"},
        "sintesis-pasivas-analitica-estado": {"kind": "grammar", "level": "B2"},
        "b2-boliviaaltiplano-vocab": {"kind": "vocabulary", "level": "B2"},
        "bolivia-altiplano-titicaca-geografia": {"kind": "grammar", "level": "B2"},
        "bolivia-potosi-cerro-rico-plata": {"kind": "grammar", "level": "B2"},
        "bolivia-lapaz-elalto-cholets-cholitas": {"kind": "grammar", "level": "B2"},
        "bolivia-coca-acullico-cosmovision": {"kind": "grammar", "level": "B2"},
        "bolivia-estado-plurinacional-constitucion": {"kind": "grammar", "level": "B2"},
        "bolivia-altiplano-sintesis-regional": {"kind": "grammar", "level": "B2"}
    }

    for k, v in new_skills.items():
        skills[k] = v

    reg_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated skill-registry.json for Unit 20")

    gt_path = LATAM_DIR / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))

    new_titles = {
        "pasiva-analitica-ser-participio": "analytical passive with ser and participle agreement in formal registers",
        "pasiva-complemento-agente-por": "agentive complements with por in analytical passive sentences",
        "pasiva-estado-estar-participio": "resultative state passive with estar and past participles",
        "participios-irregulares-dobles": "irregular and double past participles in passive constructions",
        "seleccion-estilistica-pasivas": "stylistic selection among analytical resultative and reflexive passives",
        "sintesis-pasivas-analitica-estado": "synthesis of analytical and resultative passive structures",
        "bolivia-altiplano-titicaca-geografia": "high altiplano geography and lake titicaca sacred ecosystems",
        "bolivia-potosi-cerro-rico-plata": "cerro rico silver mining history and colonial economy of potosi",
        "bolivia-lapaz-elalto-cholets-cholitas": "neo-andean architecture and aymara identity in la paz and el alto",
        "bolivia-coca-acullico-cosmovision": "ancestral sacred coca leaf rituals and cultural worldview in bolivia",
        "bolivia-estado-plurinacional-constitucion": "plurinational constitutional state and indigenous legal rights in bolivia",
        "bolivia-altiplano-sintesis-regional": "synthesis of bolivian high altiplano history culture and society"
    }

    for k, v in new_titles.items():
        gt[k] = v

    gt_path.write_text(json.dumps(gt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json for Unit 20")

    # -------------------------------------------------------------------------
    # 1. VOCABULARY FILES (5 Core + 5 Regional)
    # -------------------------------------------------------------------------
    core_vocabs = [
        (c1, "b2-20-01-voc", "La pasiva analítica y concordancia del participio", [
            {"lemma": "erigir", "translation": "to erect / to construct monumentally", "pos": "verb"},
            {"lemma": "redactar", "translation": "to draft / to write formal text", "pos": "verb"},
            {"lemma": "monumento", "translation": "monument / historic memorial structure", "pos": "noun"},
            {"lemma": "tratado", "translation": "international formal treaty", "pos": "noun"},
            {"lemma": "paciente", "translation": "syntactic patient receiving action", "pos": "adjective"},
            {"lemma": "inaugurado", "translation": "inaugurated / officially opened", "pos": "adjective"}
        ]),
        (c2, "b2-20-02-voc", "El complemento agente con por", [
            {"lemma": "promotor", "translation": "promoter / initiator of an undertaking", "pos": "noun"},
            {"lemma": "artífice", "translation": "architect / primary author of an outcome", "pos": "noun"},
            {"lemma": "sancionar", "translation": "to pass legislation / to impose legal sanction", "pos": "verb"},
            {"lemma": "auspiciar", "translation": "to sponsor / to patronize formally", "pos": "verb"},
            {"lemma": "unánime", "translation": "unanimous in agreement", "pos": "adjective"},
            {"lemma": "deliberado", "translation": "deliberate / consciously intentional", "pos": "adjective"}
        ]),
        (c3, "b2-20-03-voc", "La pasiva de estado con estar y participio", [
            {"lemma": "estado", "translation": "state / resultant condition", "pos": "noun"},
            {"lemma": "desenlace", "translation": "outcome / denouement of events", "pos": "noun"},
            {"lemma": "clausurar", "translation": "to seal off / to close permanently", "pos": "verb"},
            {"lemma": "devastar", "translation": "to lay waste / to devastate thoroughly", "pos": "verb"},
            {"lemma": "resuelto", "translation": "resolved / settled conclusively", "pos": "adjective"},
            {"lemma": "consumado", "translation": "consummated / fully completed", "pos": "adjective"}
        ]),
        (c4, "b2-20-04-voc", "Participios irregulares y formas dobles", [
            {"lemma": "electo", "translation": "elected official awaiting inauguration", "pos": "adjective"},
            {"lemma": "impreso", "translation": "printed / published in hard copy", "pos": "adjective"},
            {"lemma": "proveer", "translation": "to provide / to supply essential resources", "pos": "verb"},
            {"lemma": "reparto", "translation": "distribution / allotment of shares", "pos": "noun"},
            {"lemma": "suplente", "translation": "substitute / deputy alternate", "pos": "noun"},
            {"lemma": "confeso", "translation": "self-confessed / admitted culpability", "pos": "adjective"}
        ]),
        (c5, "b2-20-05-voc", "Selección estilística entre pasivas", [
            {"lemma": "estilo", "translation": "style / prose register register", "pos": "noun"},
            {"lemma": "ponderación", "translation": "weighing of alternatives / deliberation", "pos": "noun"},
            {"lemma": "alternar", "translation": "to alternate between syntactic forms", "pos": "verb"},
            {"lemma": "despersonalizar", "translation": "to depersonalize prose for objectivity", "pos": "verb"},
            {"lemma": "discursivo", "translation": "discursive / textual", "pos": "adjective"},
            {"lemma": "sucinto", "translation": "succinct / concise and precise", "pos": "adjective"}
        ])
    ]

    for stem, vid, vtitle, words in core_vocabs:
        write_json(f"vocabulary/b2/{vid}.json", {
            "id": f"vocab.b2.20.{stem[-2:]}",
            "lesson": stem,
            "title": vtitle,
            "theme": "analytical and resultative passives in formal spanish",
            "words": words
        })

    reg_vocabs = [
        (r1, "b2-boliviaaltiplano-01-voc", "El altiplano a cuatro mil metros y el lago Titicaca", [
            {"lemma": "altiplano", "translation": "high plateau highland basin", "pos": "noun"},
            {"lemma": "totora", "translation": "aquatic reed used for floating islands and boats", "pos": "noun"},
            {"lemma": "bofedal", "translation": "high-altitude peat wetland ecosystem", "pos": "noun"},
            {"lemma": "embarcación", "translation": "traditional reed watercraft", "pos": "noun"},
            {"lemma": "gélido", "translation": "frigid / biting high-altitude cold", "pos": "adjective"},
            {"lemma": "ancestral", "translation": "ancestral / immemorial millenary heritage", "pos": "adjective"}
        ]),
        (r2, "b2-boliviaaltiplano-02-voc", "El Cerro Rico de Potosí y la plata virreinal", [
            {"lemma": "socavón", "translation": "subterranean mine tunnel or shaft", "pos": "noun"},
            {"lemma": "mita", "translation": "rotational forced mining labor levy", "pos": "noun"},
            {"lemma": "plata", "translation": "silver bullion extracted from ore", "pos": "noun"},
            {"lemma": "minero", "translation": "subterranean mine worker", "pos": "noun"},
            {"lemma": "metalúrgico", "translation": "metallurgical / ore smelting", "pos": "adjective"},
            {"lemma": "suntuoso", "translation": "sumptuous / opulent baroque splendor", "pos": "adjective"}
        ]),
        (r3, "b2-boliviaaltiplano-03-voc", "La Paz y El Alto: Cholitas y cholets neoandinos", [
            {"lemma": "cholet", "translation": "neo-Andean colorful mansion of El Alto", "pos": "noun"},
            {"lemma": "cholita", "translation": "Aymara indigenous woman with bowler hat and pollera", "pos": "noun"},
            {"lemma": "pollera", "translation": "voluminous layered traditional skirt", "pos": "noun"},
            {"lemma": "teleférico", "translation": "urban aerial cable car transit network", "pos": "noun"},
            {"lemma": "vanguardista", "translation": "avant-garde / boldly innovative", "pos": "adjective"},
            {"lemma": "abrupto", "translation": "precipitous / deeply canyoned mountain topography", "pos": "adjective"}
        ]),
        (r4, "b2-boliviaaltiplano-04-voc", "La hoja de coca: Cosmovisión y acullico", [
            {"lemma": "acullico", "translation": "sacred ritual chewing of coca leaf wad", "pos": "noun"},
            {"lemma": "chuspa", "translation": "woven Andean pouch for carrying coca leaves", "pos": "noun"},
            {"lemma": "challa", "translation": "reciprocal libation offering to Pachamama", "pos": "noun"},
            {"lemma": "alcaloide", "translation": "medicinal organic alkaloid compound", "pos": "noun"},
            {"lemma": "sagrado", "translation": "sacred / venerated in Andean worldview", "pos": "adjective"},
            {"lemma": "energizante", "translation": "energizing / combatting fatigue and altitude sickness", "pos": "adjective"}
        ]),
        (r5, "b2-boliviaaltiplano-05-voc", "El Estado Plurinacional y la refundación constitucional", [
            {"lemma": "wiphala", "translation": "square seven-colored indigenous Andean emblem flag", "pos": "noun"},
            {"lemma": "plurinacionalidad", "translation": "constitutional recognition of multiple indigenous nations", "pos": "noun"},
            {"lemma": "asamblea", "translation": "constitutional constituent assembly", "pos": "noun"},
            {"lemma": "descolonización", "translation": "decolonization of state and cultural institutions", "pos": "noun"},
            {"lemma": "originario", "translation": "native / native indigenous inhabitant", "pos": "adjective"},
            {"lemma": "comunitario", "translation": "communal / collective indigenous governance", "pos": "adjective"}
        ])
    ]

    for stem, vid, vtitle, words in reg_vocabs:
        write_json(f"vocabulary/b2/{vid}.json", {
            "id": f"vocab.b2.boliviaaltiplano.{stem[-2:]}",
            "lesson": stem,
            "title": vtitle,
            "theme": "bolivian high altiplano geography mining indigenous culture and statecraft",
            "words": words
        })

    # -------------------------------------------------------------------------
    # 2. GRAMMAR FILES (5 Core + 5 Regional, none for consolidation)
    # -------------------------------------------------------------------------
    core_grammars = [
        (c1, "grammar.b2.20.01.pasiva-analitica-ser-participio", "Voz pasiva analítica con ser y participio",
         "La **voz pasiva analítica** o de acción se forma con el verbo auxiliar **ser** conjugado en el tiempo correspondiente seguido del **participio del verbo principal**, el cual concuerda obligatoriamente en género y número con el sujeto paciente.\n\nEsta estructura focaliza el proceso dinámico experimentado por el sujeto: *El puente fue erigido por los ingenieros*, *Las actas fueron redactadas por el secretario*. Se utiliza profusamente en textos históricos, periodísticos y jurídicos para enfatizar al paciente de la acción.",
         "Concordancia de género y número en la pasiva con ser",
         [["El monumento fue erigido en la plaza mayor.", "The monument was erected in the main square."],
          ["La constitución fue promulgada en el congreso.", "The constitution was promulgated in congress."],
          ["Los tratados fueron suscritos por los presidentes.", "The treaties were signed by the presidents."],
          ["Las resoluciones fueron redactadas con rigor.", "The resolutions were drafted with rigor."],
          ["El edificio histórico fue restaurado por artesanos.", "The historic building was restored by craftspeople."],
          ["Las murallas fueron derribadas durante el asedio.", "The defensive walls were torn down during the siege."]],
         "Recuerda que el participio pasivo con 'ser' varía siempre en género y número: *fue redactad-o*, *fue redactad-a*, *fueron redactad-os*, *fueron redactad-as*."),

        (c2, "grammar.b2.20.02.pasiva-complemento-agente-por", "El complemento agente introducido por por",
         "En la pasiva analítica, el ejecutor de la acción se expresa mediante el **complemento agente**, introducido casi invariablemente por la preposición **por** (y excepcionalmente por *de* con verbos de afección o conocimiento: *ser temido de todos*).\n\nEl complemento agente se explicita cuando la identidad del causante aporta información informativa o jurídica indispensable: *La ley fue vetada por el poder ejecutivo*. Si el agente es genérico o irrelevante, suele omitirse o reemplazarse por una pasiva refleja.",
         "Uso y función del complemento agente con por",
         [["El decreto fue rubricado por el presidente.", "The decree was signed by the president."],
          ["Las tierras fueron defendidas por los comuneros.", "The lands were defended by the communal villagers."],
          ["El concierto fue auspiciado por el ministerio.", "The concert was sponsored by the ministry."],
          ["La propuesta fue aprobada por votación unánime.", "The proposal was approved by unanimous vote."],
          ["La novela fue aclamada por la crítica internacional.", "The novel was acclaimed by international critics."],
          ["El proyecto fue respaldado por las asambleas locales.", "The project was backed by the local assemblies."]],
         "Evita usar 'por' cuando se trate de un medio instrumental en lugar de un agente humano consciente: no digas *'fue destruido por un martillo'*, sino *'con un martillo'*."),

        (c3, "grammar.b2.20.03.pasiva-estado-estar-participio", "La pasiva de estado con estar y participio",
         "A diferencia de la pasiva con *ser* (que denota una acción o acontecimiento en desarrollo), la **pasiva de estado o resultativa** con **estar + participio** describe el estado o resultado estático alcanzado tras la culminación de un proceso previo.\n\nContrasta: *La puerta fue cerrada a medianoche* (acción puntual ejecutada por alguien) frente a *La puerta estaba cerrada cuando llegamos* (estado descriptivo visible).",
         "Contraste entre pasiva de acción (ser) y pasiva de estado (estar)",
         [["El informe fue concluido anoche.", "The report was concluded last night (action)."],
          ["El informe ya está concluido.", "The report is already concluded (resultant state)."],
          ["Las minas fueron clausuradas por el gobierno.", "The mines were shut down by the government (action)."],
          ["Las minas están clausuradas desde enero.", "The mines have been shut down since January (state)."],
          ["El conflicto fue resuelto mediante diálogo.", "The conflict was resolved through dialogue (action)."],
          ["El conflicto está totalmente resuelto.", "The conflict is completely resolved (state)."]],
         "En la pasiva de estado con 'estar', el complemento agente con 'por' rara vez aparece, ya que la atención se focaliza enteramente en la condición estática del sujeto."),

        (c4, "grammar.b2.20.04.participios-irregulares-dobles", "Participios irregulares y formas dobles en español",
         "Determinados verbos españoles disponen de **dos formas de participio**: una regular terminada en *-ado/-ido* y otra irregular heredada del latín (*elegido/electo*, *imprimido/impreso*, *proveído/provisto*, *soltado/suelto*).\n\nEn la lengua culta contemporánea, las formas regulares se emplean preferentemente en los tiempos compuestos (*ha elegido*), mientras que las formas irregulares actúan predominantemente como adjetivos o en pasivas de estado (*el presidente electo*, *los libros están impresos*). Con *imprimir*, *freír* y *proveer*, ambas formas son válidas en la pasiva analítica.",
         "Distribución de participios dobles regulares e irregulares",
         [["El informe ha sido imprimido / impreso.", "The report has been printed (both valid with ser)."],
          ["El texto ya está impreso en papel vitela.", "The text is already printed on vellum paper (adjective/state)."],
          ["El congreso ha elegido a los nuevos magistrados.", "Congress has elected the new magistrates (compound tense)."],
          ["Los magistrados electos asumirán el cargo.", "The elected magistrates will take office (adjective)."],
          ["El pueblo ha sido provisto de víveres.", "The village has been supplied with foodstuffs."],
          ["El almacén está bien provisto para el invierno.", "The storehouse is well supplied for the winter."]],
         "Con verbos como *atender* y *despertar*, solo la forma regular es auténtico participio verbal (*ha atendido*, *ha despertado*); las formas *atento* y *despierto* son adjetivos independientes."),

        (c5, "grammar.b2.20.05.seleccion-estilistica-pasivas", "Selección estilística entre pasivas en la prosa formal",
         "El redactor de nivel B2 debe saber seleccionar con criterio estilístico entre la **pasiva refleja** (*se firmó el pacto*), la **pasiva analítica** (*el pacto fue firmado por los delegados*) y la **pasiva de estado** (*el pacto está firmado*).\n\nLa pasiva analítica es idónea para crónicas históricas con agente explícito; la pasiva refleja aporta fluidez al estilo periodístico despersonalizado; y la pasiva de estado fija la situación final de un proceso institucional.",
         "Criterios de adecuación estilística en la prosa formal",
         [["Se promulgaron tres leyes prioritarias.", "Three priority laws were promulgated (reflexive passive, agentless fluid)."],
          ["Las leyes fueron promulgadas por el presidente.", "The laws were promulgated by the president (analytical passive with agent)."],
          ["Las leyes ya están promulgadas en la gaceta.", "The laws are already promulgated in the gazette (resultant state)."],
          ["Se clausuraron los socavones clandestinos.", "Clandestine mine shafts were closed (fluid institutional summary)."],
          ["Los socavones fueron clausurados por la policía.", "The mine shafts were closed by the police (specific event chronicle)."],
          ["Los accesos están clausurados con sellos oficiales.", "Access points are sealed with official stamps (current condition)."]],
         "Evita sobrecargar un mismo párrafo con sucesivas pasivas analíticas con 'ser'; alterna con pasivas reflejas y construcciones activas para dinamizar la lectura.")
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
        (r1, "grammar.b2.boliviaaltiplano.01.bolivia-altiplano-titicaca-geografia", "Geografía del altiplano y el lago sagrado Titicaca",
         "El **altiplano andino** es una colosal meseta intermontana situada a más de 3.800 metros sobre el nivel del mar entre las cordilleras Occidental y Real de los Andes bolivianos. Su clima extremo combina radiación solar intensa con noches gélidas bajo cero.\n\nEn su seno reposa el **lago Titicaca**, el cuerpo de agua navegable más alto del planeta. Considerado por las civilizaciones tiwanaku e inca como la cuna sagrada de los dioses solares, el lago alberga islas de totora flotantes, bofedales de pastoreo para llamas y alpacas, y una milenaria tradición de navegación en caballitos de totora.",
         "Rasgos geomorfológicos y culturales del altiplano y Titicaca",
         [["El altiplano se extiende a casi cuatro mil metros de altitud.", "The high plateau extends at almost four thousand meters of altitude."],
          ["El lago Titicaca regula térmicamente las heladas de la meseta.", "Lake Titicaca thermally moderates plateau frosts."],
          ["Las islas flotantes son construidas con cañas de totora.", "The floating islands are built with totora reed roots."],
          ["Los bofedales sustentan el pastoreo de camélidos andinos.", "Peat wetlands sustain the grazing of Andean camelids."],
          ["La Isla del Sol fue el santuario primordial del Tawantinsuyu.", "The Island of the Sun was the primary sanctuary of Tawantinsuyu."],
          ["El pueblo aymara mantiene viva su lengua y cosmovisión lacustre.", "The Aymara people keep alive their lacustrine language and worldview."]],
         "El efecto termorregulador de la inmensa masa de agua del Titicaca permite el cultivo de papa, quinua, habas y cebada en una altitud donde de otro modo la agricultura sería inviable."),

        (r2, "grammar.b2.boliviaaltiplano.02.bolivia-potosi-cerro-rico-plata", "El Cerro Rico de Potosí y la economía minera virreinal",
         "Descubierto en 1545, el **Cerro Rico de Potosí** (*Sumaj Orcko*) albergó la veta de plata más descomunal y concentrada de la historia de la humanidad, dando origen a la célebre expresión *'valer un Potosí'* para describir riquezas incalculables.\n\nA sus faldas creció la Villa Imperial de Potosí, una metrópoli barroca de conventos e iglesias suntuosas que en el siglo XVII superó en población a Londres y París. Su opulencia descansó sobre la **mita minera**: un sistema de trabajo forzado que cobró millares de vidas indígenas en los oscuros socavones, donde hasta hoy los mineros rinden culto devoto a **El Tío**, dios protector del inframundo.",
         "Historia minera y legado patrimonial de Potosí",
         [["El Cerro Rico abasteció de plata a los imperios europeos.", "The Cerro Rico supplied silver to European empires."],
          ["La mita colonial reclutaba anualmente a miles de mitayos.", "The colonial mita recruited thousands of forced laborers annually."],
          ["La Casa de la Moneda acuñó los reales de a ocho mundiales.", "The Royal Mint minted the worldwide pieces of eight silver coins."],
          ["El Tío custodia los filones minerales en los socavones profundos.", "El Tío guards the mineral veins in the deep mine tunnels."],
          ["Potosí fue declarada Patrimonio de la Humanidad por la UNESCO.", "Potosí was declared a World Heritage Site by UNESCO."],
          ["La economía virreinal articuló rutas desde el Alto Perú hasta Sevilla.", "The viceregal economy linked trade routes from Upper Peru to Seville."]],
         "La Casa de la Moneda de Potosí conserva intactas las colosales maquinarias de madera de roble movidas por tracción animal para laminar los lingotes de plata."),

        (r3, "grammar.b2.boliviaaltiplano.03.bolivia-lapaz-elalto-cholets-cholitas", "La Paz y El Alto: Cholitas y arquitectura neoandina cholet",
         "El área metropolitana paceña presenta uno de los contrastes topográficos y sociales más impactantes de América: en la hoyada profunda descansa **La Paz** (3.600 m), mientras en la planicie superior se expande **El Alto** (4.100 m), la metrópoli aymara más poblada y vibrante del continente.\n\nAmbas urbes están conectadas por la red de **teleféricos urbanos** más extensa del mundo. En El Alto florece la vanguardia arquitectónica de los **cholets**, fastuosas mansiones policromáticas diseñadas por Freddy Mamani con motivos geométricos tiwanakotas, reflejo del empoderamiento económico de la burguesía aymara y de las orgullosas **cholitas**.",
         "Vanguardia urbana y reivindicación identitaria en La Paz y El Alto",
         [["La red de teleféricos enlaza la hoyada paceña con El Alto.", "The cable car network links the La Paz canyon with El Alto."],
          ["Los cholets integran iconografía tiwanakota y colores vivos.", "Cholets integrate Tiwanaku iconography and vibrant colors."],
          ["La cholita boliviana viste pollera plisada y sombrero borsalino.", "The Bolivian cholita wears a pleated pollera and bowler hat."],
          ["El Alto se erige como el corazón del poder popular aymara.", "El Alto stands as the heart of Aymara popular power."],
          ["La arquitectura neoandina resignifica el paisaje altiplánico.", "Neo-Andean architecture resignifies the high plateau landscape."],
          ["Las mujeres de pollera conquistaron las universidades y el parlamento.", "Indigenous women in polleras conquered universities and parliament."]],
         "Las cholitas bolivianas han roto barreras históricas de discriminación, destacando hoy como empresarias, abogadas, ministras de Estado, periodistas y escaladoras de alta montaña."),

        (r4, "grammar.b2.boliviaaltiplano.04.bolivia-coca-acullico-cosmovision", "La sagrada hoja de coca: Cosmovisión y acullico",
         "Para los pueblos aymara y quechua de Bolivia, la **hoja de coca** (*Erythroxylum coca*) es una planta sagrada (*inalmama*) venerada como un puente espiritual con la Pachamama y los Apus desde hace más de tres milenios.\n\nLa práctica ancestral del **acullico** (el pijcheo o masticación ritual de las hojas secas con caliza o ceniza) mitiga la fatiga, el hambre y el mal de montaña (*soroche*), aportando minerales y vitaminas esenciales. La Constitución de 2009 protege a la coca en su estado natural como patrimonio cultural y factor de cohesión social, defendiendo la premisa fundamental: *'la coca no es cocaína'*.",
         "Significado cultural, medicinal y social de la hoja de coca",
         [["El acullico alivia la fatiga física y el mal de altura.", "The acullico chew relieves physical fatigue and altitude sickness."],
          ["La coca es empleada en la challa y los rituales sagrados.", "Coca is used in challa libations and sacred Andean rituals."],
          ["Las hojas de coca contienen nutrientes minerales y alcaloides.", "Coca leaves contain mineral nutrients and natural alkaloids."],
          ["Los sabios yatiris leen el porvenir en las hojas extendidas.", "Aymara yatiri healers read the future in the spread leaves."],
          ["La Constitución boliviana protege la coca como patrimonio originario.", "The Bolivian constitution protects coca as indigenous heritage."],
          ["El sindicato cocalero defendió la soberanía agraria campesina.", "The coca growers' union defended peasant agrarian sovereignty."]],
         "En 2013, Bolivia logró que la Organización de las Naciones Unidas reconociera formalmente la reserva que permite el acullico tradicional dentro de su territorio soberano."),

        (r5, "grammar.b2.boliviaaltiplano.05.bolivia-estado-plurinacional-constitucion", "El Estado Plurinacional y la refundación constitucional",
         "La promulgación de la **Constitución Política del Estado de 2009** refundó a la República de Bolivia como un **Estado Unitario Social de Derecho Plurinacional Comunitario**, reconociendo formalmente la preexistencia colonial de treinta y seis naciones y pueblos indígena originario campesinos.\n\nLa carta magna consagró la **Wiphala** como símbolo patrio oficial junto a la tricolor, reconoció la justicia indígena originaria campesina en igualdad de jerarquía con la justicia ordinaria estatal, y adoptó el principio ético-moral del **Suma Qamaña** (el 'Vivir Bien' aymara).",
         "Pilares del Estado Plurinacional de Bolivia",
         [["La Constitución reconoce a treinta y seis naciones originarias.", "The Constitution recognizes thirty-six native indigenous nations."],
          ["La Wiphala simboliza la igualdad y complementariedad cósmica.", "The Wiphala symbolizes cosmic equality and complementarity."],
          ["La justicia indígena comunitaria posee igual rango que la ordinaria.", "Indigenous community justice possesses equal rank to ordinary justice."],
          ["El Vivir Bien orienta el modelo de desarrollo descolonizador.", "Living Well guides the decolonizing model of development."],
          ["Las lenguas originarias gozan de estatus oficial en el Estado.", "Indigenous languages enjoy official status within the State."],
          ["La democracia comunitaria complementa el voto representativo.", "Community democracy complements representative voting."]],
         "El concepto de 'Vivir Bien' (Suma Qamaña en aymara, Sumak Kawsay en quechua) prioriza la armonía biocéntrica con la Madre Tierra por encima del crecimiento económico ilimitado.")
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
                    ["erigir", "to build monumental structure"],
                    ["redactar", "to compose formal prose"],
                    ["tratado", "signed diplomatic pact"],
                    ["inaugurado", "officially opened to public"]
                ],
                "teaches": ["b2-20-vocab"]
            },
            {
                "id": f"{c1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las actas fundacionales de la república fueron __ por los diputados constituyentes. (redactar)",
                "answer": "redactadas",
                "english": "The founding acts of the republic were drafted by the constituent deputies.",
                "teaches": ["pasiva-analitica-ser-participio"]
            },
            {
                "id": f"{c1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué el participio en la pasiva analítica 'Las leyes fueron promulgadas' lleva desinencia femenina plural?",
                "options": [
                    "Porque en la pasiva con ser el participio concuerda estrictamente en género y número con el sujeto paciente.",
                    "Porque el verbo ser siempre impone terminación femenina a los participios.",
                    "Porque las leyes son objetos que carecen de género gramatical.",
                    "Porque la concordancia en género solo es obligatoria en tiempo presente."
                ],
                "correct": 0,
                "teaches": ["pasiva-analitica-ser-participio"]
            },
            {
                "id": f"{c1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "templo", "colonial", "fue", "erigido", "sobre", "cimientos", "incaicos."],
                "solution": ["El", "templo", "colonial", "fue", "erigido", "sobre", "cimientos", "incaicos."],
                "english": "The colonial temple was erected over Inca foundations.",
                "teaches": ["pasiva-analitica-ser-participio"]
            },
            {
                "id": f"{c1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiador", "text": "¿Cuándo se inauguraron las obras del ferrocarril andino?"},
                    {"speaker": "Archivera", "text": "Los primeros tramos _____ en agosto de mil novecientos trece."}
                ],
                "options": [
                    "fueron inaugurados",
                    "fue inaugurado",
                    "fueron inauguradas",
                    "se inauguró a"
                ],
                "correct": 0,
                "teaches": ["pasiva-analitica-ser-participio"]
            },
            {
                "id": f"{c1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Todas las cláusulas del tratado fueron ratificadas por el congreso.",
                "english": "All clauses of the treaty were ratified by congress.",
                "teaches": ["pasiva-analitica-ser-participio"]
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
                    ["artífice", "primary author of outcome"],
                    ["auspiciar", "to sponsor formally"],
                    ["unánime", "in full total agreement"],
                    ["deliberado", "done with clear intent"]
                ],
                "teaches": ["b2-20-vocab"]
            },
            {
                "id": f"{c2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La reforma constitucional fue aprobada __ una abrumadora mayoría de los congresistas. (por)",
                "answer": "por",
                "english": "The constitutional reform was approved by an overwhelming majority of congress members.",
                "teaches": ["pasiva-complemento-agente-por"]
            },
            {
                "id": f"{c2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿En qué circunstancias es indispensable incluir el complemento agente con 'por' en una oración pasiva analítica?",
                "options": [
                    "Cuando la identidad específica del causante o ejecutor aporta información jurídica, histórica o narrativa fundamental.",
                    "Siempre, ya que ninguna oración pasiva puede existir sin complemento agente explícito.",
                    "Únicamente cuando el sujeto paciente sea una persona viva.",
                    "Solo cuando el verbo esté conjugado en modo subjuntivo."
                ],
                "correct": 0,
                "teaches": ["pasiva-complemento-agente-por"]
            },
            {
                "id": f"{c2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "resolución", "fue", "rubricada", "por", "el", "ministro", "de", "justicia."],
                "solution": ["La", "resolución", "fue", "rubricada", "por", "el", "ministro", "de", "justicia."],
                "english": "The resolution was signed by the minister of justice.",
                "teaches": ["pasiva-complemento-agente-por"]
            },
            {
                "id": f"{c2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Diputado", "text": "¿Quién redactó la ponencia final del proyecto minero?"},
                    {"speaker": "Relator", "text": "El documento _____ los miembros de la comisión técnica independiente."}
                ],
                "options": [
                    "fue elaborado por",
                    "estuvo elaborado de",
                    "se elaboró para",
                    "fueron elaborados con"
                ],
                "correct": 0,
                "teaches": ["pasiva-complemento-agente-por"]
            },
            {
                "id": f"{c2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Los derechos comunitarios fueron respaldados por la corte suprema de justicia.",
                "english": "Community rights were backed by the supreme court of justice.",
                "teaches": ["pasiva-complemento-agente-por"]
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
                    ["desenlace", "final outcome of plot"],
                    ["clausurar", "to seal or close down"],
                    ["devastar", "to lay waste to area"],
                    ["consumado", "fully carried out"]
                ],
                "teaches": ["b2-20-vocab"]
            },
            {
                "id": f"{c3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Cuando los peritos llegaron al yacimiento, los accesos principales ya __ clausurados con bloques de hormigón. (estar)",
                "answer": "estaban",
                "english": "When the inspectors arrived at the site, the main accesses were already sealed with concrete blocks.",
                "teaches": ["pasiva-estado-estar-participio"]
            },
            {
                "id": f"{c3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la diferencia semántica fundamental entre 'El puente fue destruido' y 'El puente está destruido'?",
                "options": [
                    "La primera describe la acción o acontecimiento violento; la segunda describe el estado resultante presente.",
                    "La primera es incorrecta en español y la segunda es la única aceptada por la academia.",
                    "La primera indica que el puente aún funciona y la segunda que está en obras.",
                    "Ambas expresan exactamente lo mismo sin ningún matiz temporal o aspectual."
                ],
                "correct": 0,
                "teaches": ["pasiva-estado-estar-participio"]
            },
            {
                "id": f"{c3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "socavones", "antiguos", "están", "inundados", "por", "las", "aguas", "subterráneas."],
                "solution": ["Los", "socavones", "antiguos", "están", "inundados", "por", "las", "aguas", "subterráneas."],
                "english": "The old mine shafts are flooded by subterranean waters.",
                "teaches": ["pasiva-estado-estar-participio"]
            },
            {
                "id": f"{c3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Auditor", "text": "¿En qué condición encontramos el archivo histórico de la gobernación?"},
                    {"speaker": "Archivero", "text": "Los expedientes más valiosos _____ en cajas ignífugas bajo llave."}
                ],
                "options": [
                    "están preservados",
                    "fueron preservando",
                    "están preservando a",
                    "habían sido de"
                ],
                "correct": 0,
                "teaches": ["pasiva-estado-estar-participio"]
            },
            {
                "id": f"{c3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las fronteras interprovinciales permanecen cerradas por orden sanitaria.",
                "english": "Interprovincial borders remain closed by sanitary order.",
                "teaches": ["pasiva-estado-estar-participio"]
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
                    ["electo", "elected official awaiting office"],
                    ["impreso", "published hard copy text"],
                    ["proveer", "to supply essentials"],
                    ["confeso", "admitted guilty culprit"]
                ],
                "teaches": ["b2-20-vocab"]
            },
            {
                "id": f"{c4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El presidente __ asumirá el mando supremo ante la asamblea legislativa en agosto. (electo)",
                "answer": "electo",
                "english": "The president-elect will assume supreme command before the legislative assembly in August.",
                "teaches": ["participios-irregulares-dobles"]
            },
            {
                "id": f"{c4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuáles son las dos formas de participio válidas para el verbo 'imprimir' en la pasiva con ser?",
                "options": [
                    "Tanto 'imprimido' como 'impreso' son formas plenamente válidas como participio verbal.",
                    "Únicamente 'imprimido', ya que 'impreso' es un error vulgar.",
                    "Únicamente 'impreso', porque la forma regular desapareció en el siglo dieciocho.",
                    "Ninguna, el verbo imprimir carece de voz pasiva en español."
                ],
                "correct": 0,
                "teaches": ["participios-irregulares-dobles"]
            },
            {
                "id": f"{c4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "manifiestos", "fueron", "impresos", "en", "imprentas", "clandestinas."],
                "solution": ["Los", "manifiestos", "fueron", "impresos", "en", "imprentas", "clandestinas."],
                "english": "The manifestos were printed in clandestine printing presses.",
                "teaches": ["participios-irregulares-dobles"]
            },
            {
                "id": f"{c4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Ministra", "text": "¿Se distribuyó el material de auxilio a las comunidades damnificadas?"},
                    {"speaker": "Director", "text": "Sí, todos los albergues _____ de agua potable y mantas de lana."}
                ],
                "options": [
                    "han sido provistos",
                    "han sido electos",
                    "están imprimiendo",
                    "fueron confesos"
                ],
                "correct": 0,
                "teaches": ["participios-irregulares-dobles"]
            },
            {
                "id": f"{c4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "Las autoridades electas juraron defender la constitución del estado plurinacional.",
                "english": "The elected authorities swore to defend the constitution of the plurinational state.",
                "teaches": ["participios-irregulares-dobles"]
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
                    ["ponderación", "careful evaluation of terms"],
                    ["alternar", "to switch between structures"],
                    ["despersonalizar", "to make objective in tone"],
                    ["sucinto", "brief and tightly phrased"]
                ],
                "teaches": ["b2-20-vocab"]
            },
            {
                "id": f"{c5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la crónica histórica se prefiere la pasiva __ cuando el agente humano debe explicitarse con rigor. (analítica)",
                "answer": "analítica",
                "english": "In historical chronicles the analytical passive is preferred when the human agent must be explicitly stated.",
                "teaches": ["seleccion-estilistica-pasivas"]
            },
            {
                "id": f"{c5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué un exceso reiterado de pasivas analíticas con 'ser' empobrece la prosa en español?",
                "options": [
                    "Porque calca la sintaxis germánica o anglosajona, restando agilidad natural al ritmo del español culto.",
                    "Porque las pasivas con ser están prohibidas en todos los tratados académicos.",
                    "Porque el verbo ser solo puede utilizarse dos veces por página en español.",
                    "Porque los participios pierden su significado cuando se repiten en plural."
                ],
                "correct": 0,
                "teaches": ["seleccion-estilistica-pasivas"]
            },
            {
                "id": f"{c5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "documento", "histórico", "fue", "custodiado", "por", "los", "ancianos."],
                "solution": ["El", "documento", "histórico", "fue", "custodiado", "por", "los", "ancianos."],
                "english": "The historical document was guarded by the elders.",
                "teaches": ["seleccion-estilistica-pasivas"]
            },
            {
                "id": f"{c5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Editor", "text": "¿Cómo redactamos la nota sobre los nuevos acuerdos agrícolas?"},
                    {"speaker": "Redactora", "text": "Podemos escribir: '_____ tras intensas deliberaciones comunitarias'."}
                ],
                "options": [
                    "Se suscribieron los acuerdos",
                    "Fue suscrito a los acuerdos",
                    "Estuvieron suscribiendo de",
                    "Se suscribió por los acuerdos"
                ],
                "correct": 0,
                "teaches": ["seleccion-estilistica-pasivas"]
            },
            {
                "id": f"{c5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La alternancia entre pasiva refleja y analítica dota de elegancia a la prosa.",
                "english": "Alternating between reflexive and analytical passives endows prose with elegance.",
                "teaches": ["seleccion-estilistica-pasivas"]
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
                    ["erigir", "to erect monument"],
                    ["artífice", "principal author of act"],
                    ["electo", "chosen official awaiting office"],
                    ["devastar", "to lay waste utterly"]
                ],
                "teaches": ["b2-20-vocab"]
            },
            {
                "id": f"{l6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "En la novela Raza de bronce, las tierras de los comuneros aymaras fueron __ por el codicioso hacendado Pantoja. (usurpar)",
                "answer": "usurpadas",
                "english": "In the novel Raza de bronce, the lands of the Aymara villagers were usurped by the greedy landowner Pantoja.",
                "teaches": ["sintesis-pasivas-analitica-estado"]
            },
            {
                "id": f"{l6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "En la obra de Alcides Arguedas, ¿cómo se describe el desenlace trágico de la comunidad de Kohahuyo?",
                "options": [
                    "Tras el asesinato de la joven Wata Wara por los patrones, los comuneros se sublevan y la hacienda es consumida por el fuego vengador.",
                    "Los campesinos deciden vender voluntariamente sus bofedales para trasladarse a vivir a París.",
                    "El terrateniente divide pacíficamente sus tierras entre los ancianos en un banquete festivo.",
                    "Llega una expedición arqueológica que desentierra tesoros de oro salvando a todos."
                ],
                "correct": 0,
                "teaches": ["sintesis-pasivas-analitica-estado"]
            },
            {
                "id": f"{l6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Al final del relato, las casas patronales ya __ completamente consumidas por las llamas. (estar)",
                "answer": "estaban",
                "english": "At the end of the story, the manor houses were already completely consumed by the flames.",
                "teaches": ["pasiva-estado-estar-participio"]
            },
            {
                "id": f"{l6_con}.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Los", "comuneros", "fueron", "empujados", "a", "la", "rebelión", "por", "la", "injusticia."],
                "solution": ["Los", "comuneros", "fueron", "empujados", "a", "la", "rebelión", "por", "la", "injusticia."],
                "english": "The communal villagers were pushed into rebellion by injustice.",
                "teaches": ["sintesis-pasivas-analitica-estado"]
            },
            {
                "id": f"{l6_con}.ex06",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Agapito Choque", "text": "¿Qué suerte corrió la caravana que descendió a los yungas cálidos?"},
                    {"speaker": "Cachapa", "text": "Muchos compañeros _____ por las fiebres tropicales y el agotamiento del viaje."}
                ],
                "options": [
                    "fueron diezmados",
                    "fueron diezmadas",
                    "estuvieron diezmando a",
                    "se diezmó con"
                ],
                "correct": 0,
                "teaches": ["sintesis-pasivas-analitica-estado"]
            },
            {
                "id": f"{l6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "La dignidad de la raza indígena fue defendida con heroísmo frente al despojo feudal.",
                "english": "The dignity of the indigenous race was defended with heroism against feudal dispossession.",
                "teaches": ["sintesis-pasivas-analitica-estado"]
            },
            {
                "id": f"{l6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la regla fundamental para concordar el participio en la pasiva con 'ser' frente a los tiempos compuestos con 'haber'?",
                "options": [
                    "Con 'ser' el participio concuerda en género y número con el sujeto paciente; con 'haber' el participio es invariable terminado en -o.",
                    "Con 'ser' el participio termina siempre en -o; con 'haber' concuerda con el objeto directo.",
                    "Ambos auxiliares exigen concordancia obligatoria en género y número.",
                    "Ninguno de los dos auxiliares permite variación en género y número."
                ],
                "correct": 0,
                "teaches": ["sintesis-pasivas-analitica-estado"]
            }
        ]
    })

    # Regional 1 (Altiplano y Titicaca)
    write_json(f"exercises/b2/{r1}-ex.json", {
        "lesson": r1,
        "exercises": [
            {
                "id": f"{r1}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["altiplano", "high intermontane plateau"],
                    ["totora", "sturdy aquatic reed"],
                    ["bofedal", "high-altitude peat wetland"],
                    ["gélido", "bitingly frigid cold"]
                ],
                "teaches": ["b2-boliviaaltiplano-vocab"]
            },
            {
                "id": f"{r1}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El lago __ es el lago navegable más alto del mundo a más de tres mil ochocientos metros. (Titicaca)",
                "answer": "Titicaca",
                "english": "Lake Titicaca is the highest navigable lake in the world at over three thousand eight hundred meters.",
                "teaches": ["bolivia-altiplano-titicaca-geografia"]
            },
            {
                "id": f"{r1}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué función climática vital cumple el lago Titicaca para las comunidades agrícolas del altiplano?",
                "options": [
                    "Actúa como un inmenso termorregulador que modera las heladas nocturnas permitiendo el cultivo de tubérculos y cereales.",
                    "Provoca olas gigantescas que impiden cualquier tipo de asentamiento humano ribereño.",
                    "Calienta el agua hasta transformarla en vapor termal durante todo el año.",
                    "Deseca los valles vecinos impidiendo el crecimiento de pastizales para camélidos."
                ],
                "correct": 0,
                "teaches": ["bolivia-altiplano-titicaca-geografia"]
            },
            {
                "id": f"{r1}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "Isla", "del", "Sol", "fue", "venerada", "como", "la", "cuna", "mítica", "solar."],
                "solution": ["La", "Isla", "del", "Sol", "fue", "venerada", "como", "la", "cuna", "mítica", "solar."],
                "english": "The Island of the Sun was venerated as the mythical solar cradle.",
                "teaches": ["bolivia-altiplano-titicaca-geografia"]
            },
            {
                "id": f"{r1}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Turista", "text": "¿Con qué material ancestral construyen los pescadores sus balsas en el Titicaca?"},
                    {"speaker": "Guía aymara", "text": "Las embarcaciones tradicionales _____ con tallos secos de caña de totora trenzada."}
                ],
                "options": [
                    "son elaboradas",
                    "fueron elaborando a",
                    "está elaborada",
                    "se elaboraban de"
                ],
                "correct": 0,
                "teaches": ["bolivia-altiplano-titicaca-geografia"]
            },
            {
                "id": f"{r1}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El altiplano boliviano despliega un horizonte infinito custodiado por la Cordillera Real.",
                "english": "The Bolivian high plateau unfolds an infinite horizon guarded by the Cordillera Real.",
                "teaches": ["bolivia-altiplano-titicaca-geografia"]
            }
        ]
    })

    # Regional 2 (Potosí y Cerro Rico)
    write_json(f"exercises/b2/{r2}-ex.json", {
        "lesson": r2,
        "exercises": [
            {
                "id": f"{r2}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["socavón", "deep subterranean mine gallery"],
                    ["mita", "forced rotational mining labor"],
                    ["plata", "precious extracted silver ore"],
                    ["suntuoso", "lavishly opulent and ornate"]
                ],
                "teaches": ["b2-boliviaaltiplano-vocab"]
            },
            {
                "id": f"{r2}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El cerro sagrado de __ albergó la mayor concentración de plata conocida en la historia. (Potosí)",
                "answer": "Potosí",
                "english": "The sacred mountain of Potosí harbored the largest concentration of silver known in history.",
                "teaches": ["bolivia-potosi-cerro-rico-plata"]
            },
            {
                "id": f"{r2}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Quién es la deidad sincrética conocida como 'El Tío' en las minas de Potosí?",
                "options": [
                    "El señor y protector del inframundo minero a quien se rinde culto con ofrendas de alcohol, coca y cigarrillos en el socavón.",
                    "El apodo del primer virrey español que visitó las galerías subterráneas.",
                    "Un santo católico canonizado exclusivamente para la protección de los ingenieros.",
                    "El nombre del principal río subterráneo que inundaba las minas."
                ],
                "correct": 0,
                "teaches": ["bolivia-potosi-cerro-rico-plata"]
            },
            {
                "id": f"{r2}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "Casa", "de", "la", "Moneda", "fue", "fundada", "en", "la", "Villa", "Imperial."],
                "solution": ["La", "Casa", "de", "la", "Moneda", "fue", "fundada", "en", "la", "Villa", "Imperial."],
                "english": "The Royal Mint was founded in the Imperial Villa.",
                "teaches": ["bolivia-potosi-cerro-rico-plata"]
            },
            {
                "id": f"{r2}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Historiadora", "text": "¿Qué moneda acuñada en Potosí se convirtió en la primera divisa global?"},
                    {"speaker": "Numismático", "text": "El célebre 'real de a ocho' _____ por comerciantes de Europa, Asia y las Américas."}
                ],
                "options": [
                    "fue aceptado universalmente",
                    "estuvo aceptando a",
                    "se aceptó con",
                    "fueron aceptados de"
                ],
                "correct": 0,
                "teaches": ["bolivia-potosi-cerro-rico-plata"]
            },
            {
                "id": f"{r2}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La plata extraída de Potosí financió el comercio transoceánico durante tres centurias.",
                "english": "The silver extracted from Potosí financed transoceanic commerce for three centuries.",
                "teaches": ["bolivia-potosi-cerro-rico-plata"]
            }
        ]
    })

    # Regional 3 (La Paz y El Alto)
    write_json(f"exercises/b2/{r3}-ex.json", {
        "lesson": r3,
        "exercises": [
            {
                "id": f"{r3}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["cholet", "colorful neo-Andean mansion"],
                    ["cholita", "proud Aymara indigenous woman"],
                    ["pollera", "pleated multi-layered traditional skirt"],
                    ["teleférico", "urban aerial cable car system"]
                ],
                "teaches": ["b2-boliviaaltiplano-vocab"]
            },
            {
                "id": f"{r3}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La red de transporte por cable urbano más extensa y moderna del mundo es el __ de La Paz y El Alto. (teleférico)",
                "answer": "teleférico",
                "english": "The world's most extensive and modern urban cable transit network is the cable car of La Paz and El Alto.",
                "teaches": ["bolivia-lapaz-elalto-cholets-cholitas"]
            },
            {
                "id": f"{r3}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué singularidad estética define a la arquitectura de los 'cholets' creada por Freddy Mamani en El Alto?",
                "options": [
                    "Edificios de múltiples pisos con fachadas polícromas inspiradas en los textiles y la iconografía geométrica de Tiwanaku.",
                    "Imitaciones exactas de castillos medievales góticos con puentes levadizos.",
                    "Construcciones subterráneas de barro sin ventanas para aislarse del frío.",
                    "Casas de madera idénticas a los chalés alpinos suizos."
                ],
                "correct": 0,
                "teaches": ["bolivia-lapaz-elalto-cholets-cholitas"]
            },
            {
                "id": f"{r3}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Las", "cholitas", "alteñas", "conquistaron", "nuevos", "espacios", "sociales", "y", "políticos."],
                "solution": ["Las", "cholitas", "alteñas", "conquistaron", "nuevos", "espacios", "sociales", "y", "políticos."],
                "english": "Aymara women from El Alto conquered new social and political spaces.",
                "teaches": ["bolivia-lapaz-elalto-cholets-cholitas"]
            },
            {
                "id": f"{r3}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Urbanista", "text": "¿Cómo transformó el teleférico la movilidad entre La Paz y El Alto?"},
                    {"speaker": "Socióloga", "text": "Los tiempos de desplazamiento _____ drásticamente, democratizando el acceso urbano."}
                ],
                "options": [
                    "fueron reducidos",
                    "fueron reducidas",
                    "estuvo reducido",
                    "se redujo a"
                ],
                "correct": 0,
                "teaches": ["bolivia-lapaz-elalto-cholets-cholitas"]
            },
            {
                "id": f"{r3}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La ciudad de El Alto refleja el vigor económico y la autoafirmación aymara contemporánea.",
                "english": "The city of El Alto reflects the economic vigor and contemporary Aymara self-affirmation.",
                "teaches": ["bolivia-lapaz-elalto-cholets-cholitas"]
            }
        ]
    })

    # Regional 4 (Hoja de Coca)
    write_json(f"exercises/b2/{r4}-ex.json", {
        "lesson": r4,
        "exercises": [
            {
                "id": f"{r4}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["acullico", "sacred chewing of coca leaves"],
                    ["chuspa", "woven pouch for sacred leaves"],
                    ["challa", "reciprocal libation to Pachamama"],
                    ["alcaloide", "natural beneficial chemical compound"]
                ],
                "teaches": ["b2-boliviaaltiplano-vocab"]
            },
            {
                "id": f"{r4}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El ritual andino de masticar hojas de coca con ceniza o caliza se denomina __. (acullico)",
                "answer": "acullico",
                "english": "The Andean ritual of chewing coca leaves with ash or limestone is called acullico.",
                "teaches": ["bolivia-coca-acullico-cosmovision"]
            },
            {
                "id": f"{r4}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Cuál es la premisa cultural y diplomática defendida por el Estado boliviano sobre la hoja de coca?",
                "options": [
                    "Que 'la hoja de coca no es cocaína', defendiendo su valor sagrado, nutricional y medicinal ancestral.",
                    "Que la coca debe ser erradicada por completo de todos los valles andinos.",
                    "Que las hojas solo pueden ser consumidas por turistas extranjeros en infusiones.",
                    "Que la coca es una planta traída recientemente desde otros continentes."
                ],
                "correct": 0,
                "teaches": ["bolivia-coca-acullico-cosmovision"]
            },
            {
                "id": f"{r4}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "hoja", "de", "coca", "es", "venerada", "como", "un", "símbolo", "de", "resistencia."],
                "solution": ["La", "hoja", "de", "coca", "es", "venerada", "como", "un", "símbolo", "de", "resistencia."],
                "english": "The coca leaf is venerated as a symbol of resistance.",
                "teaches": ["bolivia-coca-acullico-cosmovision"]
            },
            {
                "id": f"{r4}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Médica", "text": "¿Qué propiedades fisiológicas aporta el acullico tradicional a gran altitud?"},
                    {"speaker": "Antropólogo", "text": "Los nutrientes y alcaloides naturales _____ para optimizar la oxigenación celular."}
                ],
                "options": [
                    "son asimilados",
                    "fueron asimiladas",
                    "está asimilando",
                    "se asimilaba de"
                ],
                "correct": 0,
                "teaches": ["bolivia-coca-acullico-cosmovision"]
            },
            {
                "id": f"{r4}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "La práctica milenaria del acullico fue reconocida por las Naciones Unidas en dos mil trece.",
                "english": "The millenary practice of acullico was recognized by the United Nations in 2013.",
                "teaches": ["bolivia-coca-acullico-cosmovision"]
            }
        ]
    })

    # Regional 5 (Estado Plurinacional)
    write_json(f"exercises/b2/{r5}-ex.json", {
        "lesson": r5,
        "exercises": [
            {
                "id": f"{r5}.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["wiphala", "square multi-colored indigenous flag"],
                    ["plurinacionalidad", "coexistence of indigenous nations in state"],
                    ["asamblea", "constituent constitutional body"],
                    ["descolonización", "structural dismantling of colonial hierarchies"]
                ],
                "teaches": ["b2-boliviaaltiplano-vocab"]
            },
            {
                "id": f"{r5}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "La bandera ajedrezada de cuarenta y nueve cuadrantes que simboliza la complementariedad andina es la __. (Wiphala)",
                "answer": "Wiphala",
                "english": "The checkered flag of forty-nine squares symbolizing Andean complementarity is the Wiphala.",
                "teaches": ["bolivia-estado-plurinacional-constitucion"]
            },
            {
                "id": f"{r5}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué hito jurídico consagra la Constitución de Bolivia de 2009 respecto a las naciones originarias?",
                "options": [
                    "Reconoce formalmente a 36 pueblos originarios y otorga a la justicia comunitaria igual rango que la ordinaria.",
                    "Prohíbe el uso de todas las lenguas originarias en los tribunales de justicia.",
                    "Disuelve las comunidades campesinas transformándolas en empresas privadas.",
                    "Establece una monarquía constitucional hereditaria presidida por un virrey."
                ],
                "correct": 0,
                "teaches": ["bolivia-estado-plurinacional-constitucion"]
            },
            {
                "id": f"{r5}.ex04",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["La", "nueva", "carta", "magna", "fue", "aprobada", "por", "referéndum", "popular."],
                "solution": ["La", "nueva", "carta", "magna", "fue", "aprobada", "por", "referéndum", "popular."],
                "english": "The new constitution was approved by popular referendum.",
                "teaches": ["bolivia-estado-plurinacional-constitucion"]
            },
            {
                "id": f"{r5}.ex05",
                "type": "dialogue-complete",
                "category": "dialogue",
                "prompt": [
                    {"speaker": "Jurista", "text": "¿En qué consiste el principio ético constitucional del Suma Qamaña?"},
                    {"speaker": "Amauta", "text": "El concepto de 'Vivir Bien' _____ como una búsqueda de armonía entre comunidad y Madre Tierra."}
                ],
                "options": [
                    "fue concebido",
                    "fueron concebidos",
                    "estuvo concibiendo",
                    "se concebía de"
                ],
                "correct": 0,
                "teaches": ["bolivia-estado-plurinacional-constitucion"]
            },
            {
                "id": f"{r5}.ex06",
                "type": "dictation",
                "category": "listening",
                "sentence": "El Estado Plurinacional garantiza el pluralismo jurídico y la autodeterminación comunitaria.",
                "english": "The Plurinational State guarantees legal pluralism and community self-determination.",
                "teaches": ["bolivia-estado-plurinacional-constitucion"]
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
                    ["altiplano", "high plateau lake basin"],
                    ["socavón", "subterranean mine tunnel"],
                    ["cholet", "vibrant neo-Andean mansion"],
                    ["wiphala", "seven-colored indigenous emblem"]
                ],
                "teaches": ["b2-boliviaaltiplano-vocab"]
            },
            {
                "id": f"{r6_con}.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Las riquezas de plata del Cerro Rico fueron __ con la sangre de generaciones de mitayos andinos. (extraer)",
                "answer": "extraídas",
                "english": "The silver riches of Cerro Rico were extracted with the blood of generations of Andean forced laborers.",
                "teaches": ["bolivia-potosi-cerro-rico-plata"]
            },
            {
                "id": f"{r6_con}.ex03",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Qué simboliza el teleférico urbano más alto del mundo que une La Paz con El Alto?",
                "options": [
                    "La integración social y física entre la hoyada metropolitana y la planicie andina aymara.",
                    "Un parque temático de diversiones para turistas extranjeros de lujo.",
                    "Un sistema de transporte militar de emergencia sin acceso para civiles.",
                    "Una línea de tren subterráneo construida con túneles de hormigón."
                ],
                "correct": 0,
                "teaches": ["bolivia-lapaz-elalto-cholets-cholitas"]
            },
            {
                "id": f"{r6_con}.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "El principio ético del 'Vivir Bien' en lengua aymara se denomina Suma __. (Qamaña)",
                "answer": "Qamaña",
                "english": "The ethical principle of 'Living Well' in the Aymara language is called Suma Qamaña.",
                "teaches": ["bolivia-estado-plurinacional-constitucion"]
            },
            {
                "id": f"{r6_con}.ex05",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿Por qué la hoja de coca es considerada un pilar de la identidad andina boliviana?",
                "options": [
                    "Porque representa un elemento espiritual de reciprocidad comunal y medicina tradicional contra el mal de altura.",
                    "Porque es el único cultivo permitido en las llanuras tropicales amazónicas.",
                    "Porque se utiliza exclusivamente para la fabricación de productos plásticos sintéticos.",
                    "Porque fue declarada moneda obligatoria de curso legal en todo el país."
                ],
                "correct": 0,
                "teaches": ["bolivia-coca-acullico-cosmovision"]
            },
            {
                "id": f"{r6_con}.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Bolivia", "fue", "refundada", "como", "un", "Estado", "Plurinacional", "y", "descolonizado."],
                "solution": ["Bolivia", "fue", "refundada", "como", "un", "Estado", "Plurinacional", "y", "descolonizado."],
                "english": "Bolivia was refounded as a Plurinational and decolonized State.",
                "teaches": ["bolivia-estado-plurinacional-constitucion"]
            },
            {
                "id": f"{r6_con}.ex07",
                "type": "dictation",
                "category": "listening",
                "sentence": "El lago Titicaca custodia las memorias sagradas de las naciones aymara y quechua.",
                "english": "Lake Titicaca guards the sacred memories of the Aymara and Quechua nations.",
                "teaches": ["bolivia-altiplano-titicaca-geografia"]
            },
            {
                "id": f"{r6_con}.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "¿De qué manera la arquitectura de los cholets expresa la emancipación social de la burguesía aymara?",
                "options": [
                    "Visibiliza el éxito económico y el orgullo identitario combinando iconografía ancestral con diseño futurista.",
                    "Oculta la identidad de sus dueños bajo fachadas de imitación europea clásica.",
                    "Sustituye todas las viviendas unifamiliares por cuarteles militares comunales.",
                    "Es una imposición obligatoria del gobierno central para uniformar las calles."
                ],
                "correct": 0,
                "teaches": ["bolivia-lapaz-elalto-cholets-cholitas"]
            }
        ]
    })

    # -------------------------------------------------------------------------
    # 4. STORIES (1 Core Classic + 5 Regional Lessons + 1 Regional Capstone)
    # Strictly audited between 650 and 825 words
    # -------------------------------------------------------------------------
    # Story Core 20: Alcides Arguedas - Raza de bronce (1919)
    story_core_20 = {
        "id": "b2-20",
        "title": "Raza de bronce: La epopeya trágica de Kohahuyo y la furia del altiplano",
        "level": "B2",
        "lesson": 6,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Adaptación literaria de la obra fundacional del indigenismo boliviano de Alcides Arguedas: la comunidad aymara de Kohahuyo a orillas del lago Titicaca, el penoso viaje de los comuneros a través de los desfiladeros andinos hacia los yungas cálidos, el abuso despótico del hacendado Pantoja, el ultraje a Wata Wara y la rebelión justiciera de la estirpe de bronce.",
        "characters": [
            "Agapito Choque (sabio anciano aymara)",
            "Cachapa (joven pescador de totora)",
            "Wata Wara (pastora aymara)",
            "Hacendado don Fernando Pantoja",
            "Mayordomo Troche"
        ],
        "narration": {
            "paragraphs": [
                "A orillas de las aguas azules y gélidas del lago Titicaca, bajo la mirada imperturbable de los nevados de la Cordillera Real que recortan sus aristas de hielo contra el firmamento andino, la milenaria comunidad aymara de Kohahuyo desarrollaba su existencia en un diálogo permanente con la tierra. En esta agreste meseta donde el viento de la puna azota los pastizales de ichu y los bofedales verdosos, los comuneros pastoreaban sus rebaños de llamas y cultivaban sus parcelas de papa y quinua, atados a los ciclos solares mediante la devoción profunda a la Pachamama. Sin embargo, sobre aquella armonía ancestral pesaba la sombra implacable del feudalismo republicano: la hacienda vecina, usurpada gradualmente a los campesinos mediante escrituras fraudulentas, era gobernada con mano de hierro por don Fernando Pantoja, un terrateniente despótico que consideraba a los indígenas meras bestias de carga obligadas a la servidumbre perpetua.",
                "Un día aciago, la tranquilidad de Kohahuyo fue quebrantada por una orden terminante del patrón. Se exigió que una comitiva de comuneros emprendiera una expedición suicida: debían descender desde las alturas heladas de cuatro mil metros hacia los valles tropicales y húmedos de los Yungas para comprar y transportar sobre sus espaldas decenas de quintales de semillas y productos agrícolas. Liderada por el respetado anciano Agapito Choque y por el joven pescador Cachapa —prometido de la hermosa doncella Wata Wara—, la caravana de mitayos emprendió la marcha. El periplo fue una pesadilla dantesca: los abismos rocosos cobraron la vida de hombres y mulas que se despeñaron en los precipicios, mientras en las tierras bajas el paludismo y las fiebres malignas diezmaron a los sobrevivientes, regresando al altiplano un puñado de espectros hambrientos y quebrantados por el sufrimiento.",
                "Pero el dolor más lacerante aguardaba a Cachapa en su propio suelo natal. Durante los meses de forzosa ausencia de los hombres jóvenes, el abuso patronal se había desbordado sin contención legal alguna. Wata Wara, cuya belleza ingenua y mirada luminosa despertaban la codicia de los capataces, fue perseguida en los roquedales solitarios mientras pastoreaba sus ovejas. Pantoja y sus secuaces, envalentonados por la embriaguez y la absoluta impunidad de su condición aristocrática, consumaron un crimen atroz: la joven pastora fue asaltada, ultrajada salvajemente y su cuerpo sin vida fue abandonado entre los pajonales fríos de la quebrada para encubrir la felonía.",
                "El hallazgo del cadáver destrozado de Wata Wara desató un cataclismo en el alma colectiva de la comunidad. El llanto silencioso de las ancianas y la desesperación enloquecida de Cachapa se transformaron en un relámpago de dignidad inextinguible. Agapito Choque convocó a un consejo secreto de emergencia en las cavernas sagradas del cerro: por primera vez en generaciones, los ancianos no aconsejaron la resignación piadosa ni el repliegue sumiso. En la noche cerrada del altiplano, el sonido sordo, ronco y estremecedor de los *pututus* —los ancestrales cuernos marinos de guerra de los incas— comenzó a retumbar de cumbre en cumbre, quebrando el silencio secular de la noche andina.",
                "Desde todas las quebradas, caseríos y ayllus lacustres, millares de hombres y mujeres de la 'raza de bronce' convergieron en silencio hacia la casa de la hacienda patronal, armados con hondas, piedras, palos y teas encendidas. Sitiados tras sus gruesos muros de adobe y rejas coloniales, Pantoja y sus mayordomos abrieron fuego desesperadamente con sus fusiles de cacería, pero la marea humana, impulsada por siglos de agravios contenidos y el clamor irrenunciable de justicia, resultó incontenible. Las puertas de roble fueron derribadas a golpes de ariete, los disparos fueron sofocados por una lluvia torrencial de peñascos y las llamas purificadoras envolvieron las habitaciones señoriales y los graneros patronales en un voraz incendio que iluminó las cumbres nevadas del Illampu.",
                "Al despuntar el alba sobre las aguas sagradas del Titicaca, las cenizas humeantes de la hacienda proclamaban el despertar irrevocable de un pueblo que jamás volvería a arrodillarse. La novela de Alcides Arguedas inmortalizó así el drama social de los Andes bolivianos, demostrando que detrás de la aparente pasividad del hombre originario late una fuerza geológica invencible, templada como el bronce, capaz de levantarse como una tempestad para reconquistar su libertad, su tierra y su destino soberano en la historia de América."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué misión mortífera impuso el hacendado Pantoja a los comuneros aymaras de Kohahuyo?",
                        "options": [
                            "Descender a pie hacia los valles tropicales de los Yungas para transportar pesadas cargas de semillas sufriendo fiebres y abismos.",
                            "Navegar en canoas hasta las costas de California para comprar oro en las minas.",
                            "Construir un palacio de mármol blanco traído exclusivamente desde las canteras de Italia.",
                            "Sembrar uvas francesas en las cumbres nevadas del monte Illampu."
                        ],
                        "correctIndex": 0,
                        "explanation": "Pantoja forzó a la comitiva a un extenuante viaje a los Yungas donde muchos murieron por fiebres y despeñamientos."
                    },
                    {
                        "question": "¿Qué trágico acontecimiento desató la sublevación general de los comuneros contra la hacienda patronal?",
                        "options": [
                            "El ultraje y asesinato de la joven pastora Wata Wara a manos de Pantoja y sus capataces durante la ausencia de los hombres.",
                            "La subida de impuestos aduaneros decretada por el ministerio de hacienda en La Paz.",
                            "La llegada de una plaga de langostas que devoró los campos de quinua de la cuenca lacustre.",
                            "El rechazo del obispo a consagrar la nueva capilla católica de la comunidad."
                        ],
                        "correctIndex": 0,
                        "explanation": "El ultraje y crimen de Wata Wara colmó la paciencia comunal, desatando el llamado a las armas con los pututus."
                    },
                    {
                        "question": "¿Qué instrumento ancestral andino se empleó para convocar a la rebelión indígena de Kohahuyo en la noche?",
                        "options": [
                            "El pututu, una trompeta o caracol marino que emite un bramido sordo de largo alcance.",
                            "Campanas de bronce importadas de los campanarios de Sevilla.",
                            "Tambores metálicos de marcha militar francesa.",
                            "Señales de telégrafo eléctrico instaladas a lo largo de la ribera del lago."
                        ],
                        "correctIndex": 0,
                        "explanation": "El sonido telúrico del pututu resonó de cerro en cerro para congregar a los ayllus aymaras en armas."
                    }
                ]
            }
        }
    }

    # Regional Story 1: Altiplano y Titicaca
    story_bolivia_01 = {
        "id": "b2-boliviaaltiplano-01",
        "title": "El espejo del cielo: El altiplano a cuatro mil metros y el lago Titicaca",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía geográfica y espiritual por la inmensidad del altiplano boliviano: la meseta a cuatro mil metros de altitud custodiada por la Cordillera Real, las aguas sagradas del lago Titicaca como cuna civilizatoria de los incas, la navegación milenaria en balsas de totora y la vida comunal aymara en los bofedales andinos.",
        "characters": [
            "Amauta Esteban Quispe",
            "Pescador lacustre Don Paulino",
            "Geóloga Laura Alarcón",
            "Tejedora aymara Doña Gregoria"
        ],
        "narration": {
            "paragraphs": [
                "A casi cuatro mil metros sobre el nivel del mar, en el corazón geográfico de los Andes suramericanos, el altiplano boliviano se abre ante los ojos del viajero como una meseta titánica de luz diáfana e infinita donde la tierra parece tocar de manera directa la bóveda azul del cielo. Enmarcada al oeste por los conos volcánicos de la cordillera Occidental y al este por las aristas nevadas del Illimani, el Huayna Potosí y el Illampu en la majestuosa Cordillera Real, esta inmensa cuenca endorreica presenta un clima de contrastes implacables: la radiación solar quema la piel durante el día con una intensidad cegadora, mientras al caer la tarde las temperaturas se desploman bajo cero grados centígrados, cubriendo de escarcha cristalina los extensos pajonales de ichu. En este vasto horizonte silencioso, las comunidades aymaras han desarrollado a lo largo de siglos una profunda sabiduría de adaptación bioclimática, interpretando los ciclos astronómicos y la dirección de las nubes para anticipar las lluvias y organizar las siembras comunales.",
                "En medio de esta estepa gélida resplandece la joya hídrica indiscutible del continente: el lago Titicaca, el cuerpo de agua navegable más alto del planeta, que abarca más de ocho mil quinientos kilómetros cuadrados entre Bolivia y Perú. Lejos de ser un simple accidente geográfico, el Titicaca constituye el corazón térmico y biológico de toda la región: su inmensa masa de agua dulce absorbe el calor solar diurno y lo libera lentamente durante la noche, creando un microclima atemperado único que reduce las heladas destructivas y permite a las comunidades campesinas cultivar papas nativas, ocas, habas, cebada y quinua en una altitud donde cualquier otra agricultura del mundo resultaría inviable.",
                "Para la cosmovisión de las civilizaciones originarias, el Titicaca es la cuna sagrada del universo. Según las crónicas andinas, de las profundidades del lago emergieron Manco Cápac y Mama Ocllo, enviados por el dios Sol (Inti) para fundar el imperio del Tawantinsuyu. En la mítica Isla del Sol, accesible tras navegar por el estrecho de Tiquina, se conservan templos de piedra labrada, terrazas agrícolas escalonadas y la roca sagrada de las tres fuentes de agua pura donde los peregrinos andinos rendían culto a los orígenes del mundo mucho antes de la llegada de las carabelas hispanas.",
                "A orillas del lago y en las bahías de Huatajata y Copacabana, la vida humana se articula en íntima simbiosis con la totora (*Schoenoplectus californicus*), una caña acuática resistente y flexible que crece en espesos bosques lacustres llamados totorales. Don Paulino Esteban, maestro artesano que construyó balsas para expediciones transoceánicas internacionales, corta los tallos dorados con su hoz, los deja secar al sol y los ensambla en apretados haces atados con cuerdas vegetales. Estas ligeras embarcaciones no solo han surcado las olas frías del lago durante milenios facilitando la pesca de bogas y karachis, sino que sus raíces forman la base flotante de islas artificiales habitadas por familias aymaras y uros. La cosecha de la totora sigue protocolos estrictos de manejo ecológico transmitidos de generación en generación, asegurando que los humedales conserven su capacidad regenerativa frente a las sequías estacionales.",
                "Más allá de las riberas lacustres, el paisaje altiplánico está salpicado por los bofedales: humedales altoandinos de turberas donde las aguas de deshielo glaciar afloran a la superficie creando oasis de vegetación esponjosa y tierna. En estos bofedales pastan apaciblemente manadas de llamas y alpacas, cuya lana fina y abrigada es esquilada por mujeres como doña Gregoria para tejer los tradicionales ponchos y aguayos multicolores que resguardan a sus familias de los vientos helados de la meseta.",
                "El altiplano boliviano enseña a la humanidad que la adversidad climática y la falta de oxígeno no son obstáculos insuperables cuando una sociedad comprende las leyes de la naturaleza y vive en armonía con su entorno. Al contemplar el atardecer sobre el Titicaca, cuando las aguas reflejan las cumbres nevadas teñidas de púrpura y oro, el viajero comprende por qué este santuario de piedra, paja y agua continúa siendo considerado por millones de personas como el altar eterno de la dignidad andina."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Por qué el lago Titicaca es considerado el motor vital para la agricultura en el altiplano boliviano?",
                        "options": [
                            "Porque actúa como un termorregulador que almacena calor solar y mitiga las heladas nocturnas en la meseta.",
                            "Porque sus aguas saladas se utilizan como abono químico para la exportación de flores exóticas.",
                            "Porque genera lluvias torrenciales diarias que transforman el altiplano en un bosque tropical.",
                            "Porque desvía los vientos fríos del polo norte impidiendo que lleguen a América del Sur."
                        ],
                        "correctIndex": 0,
                        "explanation": "La enorme masa de agua del lago regula la temperatura nocturna, permitiendo el cultivo de alimentos a gran altitud."
                    },
                    {
                        "question": "¿Qué material vegetal acuático es esencial para la construcción de balsas e islas flotantes en el lago Titicaca?",
                        "options": [
                            "La totora, una caña acuática fibrosa, liviana y muy resistente.",
                            "La madera de pino importada de los bosques septentrionales.",
                            "Las hojas secas de palma aceitera amazónica.",
                            "Las ramas espinosas de los cactus del desierto costero."
                        ],
                        "correctIndex": 0,
                        "explanation": "La totora es la caña acuática que sustenta la navegación ancestral y las viviendas flotantes en el lago."
                    },
                    {
                        "question": "¿Qué importancia espiritual e histórica tiene la Isla del Sol en la cosmovisión andina?",
                        "options": [
                            "Es venerada como la cuna sagrada del universo de donde emergieron los fundadores del imperio incaico.",
                            "Fue el primer puerto comercial fundado por los conquistadores españoles en el siglo dieciséis.",
                            "Es un yacimiento petrolífero protegido por el ejército boliviano.",
                            "Albergó el observatorio astronómico construido por científicos europeos durante la Ilustración."
                        ],
                        "correctIndex": 0,
                        "explanation": "La Isla del Sol es el santuario primordial andino considerado el origen mítico de Manco Cápac y Mama Ocllo."
                    }
                ]
            }
        }
    }

    # Regional Story 2: Potosí y Cerro Rico
    story_bolivia_02 = {
        "id": "b2-boliviaaltiplano-02",
        "title": "La montaña de plata: El Cerro Rico de Potosí y la sombra de la mita",
        "level": "B2",
        "lesson": 2,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica histórica y humana en la Villa Imperial de Potosí: el hallazgo en 1545 de la mayor veta de plata del planeta en el Cerro Rico (Sumaj Orcko), la opulencia desenfrenada de la corte colonial, la tragedia humana de la mita minera, el templo numismático de la Casa de la Moneda y el culto sincrético a El Tío en los socavones.",
        "characters": [
            "Minero don Dionisio",
            "Historiadora potosina Jimena",
            "Numismático de la Casa de la Moneda",
            "Guía de socavón Juan Carlos"
        ],
        "narration": {
            "paragraphs": [
                "Al pie de una montaña piramidal de tonos rojizos y ocres que se recorta a más de cuatro mil metros de altitud contra el cielo frío de los Andes, se alza la legendaria ciudad de Potosí. En 1545, cuando el pastor indígena Diego Huallpa encendió una fogata para protegerse del viento helado y descubrió al amanecer hilos de plata pura derretida que brillaban en la roca, comenzó uno de los capítulos más deslumbrantes y trágicos de la historia económica universal. La montaña, conocida en lengua quechua como *Sumaj Orcko* (el 'Cerro Hermoso'), encerraba en su interior la concentración de mineral de plata más vasta, pura y rica jamás descubierta sobre la faz de la Tierra. Durante los primeros años de explotación a cielo abierto, los cronistas virreinales aseguraban que la plata afloraba a flor de tierra en planchas tan puras que bastaba cincelarlas con herramientas elementales para llenar arcones enteros de metal precioso.",
                "En pocas décadas, la modesta aldea minera se transformó en la Villa Imperial de Carlos V, una metrópoli de opulencia delirante que hacia 1650 albergaba a más de ciento sesenta mil habitantes, superando en población y suntuosidad a ciudades como Madrid, París y Londres. Alrededor de sus treinta y seis iglesias barrocas ricamente adornadas con retablos de pan de oro, aristócratas y capitanes de minas competían en banquetes pantagruélicos, vestían sedas flamencas y calzaban herraduras de plata a sus corceles, dando nacimiento en el idioma castellano a la universal locución 'vale un Potosí' para designar a cualquier bien de valor inestimable.",
                "Sin embargo, aquel derroche de riqueza sin precedentes tuvo un costo humano devastador. Para mantener activas las fundiciones y extraer el mineral de las profundidades de la montaña, el virrey Francisco de Toledo institucionalizó en 1572 la mita minera: un sistema coercitivo de trabajo rotativo forzado que obligaba anualmente a más de trece mil indígenas varones de dieciséis provincias del Alto Perú a internarse en las entrañas de la tierra. Sometidos a jornadas asfixiantes en galerías sofocantes donde respiraban polvo de sílice y gases tóxicos, miles de mitayos perecieron en los socavones víctimas de derrumbes, agotamiento y silicosis pulmonar. La conscripción forzosa despobló comarcas agrícolas enteras a lo largo de centenares de leguas, transformando para siempre la geografía demográfica y productiva de los valles andinos.",
                "En el corazón urbano de Potosí se levanta aún hoy la Real Casa de la Moneda, una fortaleza arquitectónica que ocupa una manzana entera y que fue el motor financiero del imperio español. En sus amplias salas de techos de cedro se conservan intactas las gigantescas máquinas laminadoras de madera de roble traídas desde España, cuyos engranajes eran movidos por recuas de mulas para aplanar los lingotes de plata y acuñar los famosos 'reales de a ocho' o columnarios: monedas que circularon como divisa de cambio universal desde los mercados de Sevilla y Ámsterdam hasta los puertos del imperio chino. Cada moneda acuñada llevaba estampada la marca inconfundible de la ceca potosina, garantizando su aceptación inmediata en las transacciones más exigentes de la banca internacional de la época.",
                "En la actualidad, el Cerro Rico sigue horadado por centenares de kilómetros de túneles donde laboran miles de mineros organizados en cooperativas tradicionales. Al ingresar al socavón, los trabajadores descienden a un inframundo dominado por el calor, el polvo y la oscuridad, pero antes de empuñar el barreno y la dinamita cumplen con un ritual inquebrantable: visitar la gruta de 'El Tío', la imagen barroca y sincrética de una divinidad con cuernos esculpida en arcilla roja que reina en las entrañas de la montaña. Los mineros adornan el cuello de El Tío con serpentinas, encienden cigarrillos en su boca y derraman chorros de alcohol puro sobre sus rodillas pidiendo permiso y protección para hallar vetas ricas y salir ilesos del socavón.",
                "Declarada Patrimonio de la Humanidad por la UNESCO, Potosí es un testigo monumental de las paradojas de la historia: una montaña que alimentó la expansión del capitalismo global y vistió de gloria a reyes lejanos, mientras en sus entrañas de roca custodia la memoria imborrable del sufrimiento y la tenacidad indestructible del pueblo minero andino."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué célebre expresión del idioma español se originó a partir de la inmensa riqueza argentífera de Potosí?",
                        "options": [
                            "'Vale un Potosí', empleada para designar que algo posee un valor incalculable o extraordinario.",
                            "'Estar en las nubes', para señalar la gran altitud de las ciudades andinas.",
                            "'Costar un ojo de la cara', referida al precio de los billetes de tren.",
                            "'Oro parece, plata no es', utilizada en las adivinanzas infantiles coloniales."
                        ],
                        "correctIndex": 0,
                        "explanation": "La riqueza descomunal del Cerro Rico dio origen a la locución 'vale un Potosí' para indicar valor supremo."
                    },
                    {
                        "question": "¿En qué consistía el sistema de la 'mita' minera instaurado por el virrey Toledo en 1572?",
                        "options": [
                            "En un tributo de trabajo forzado y rotativo obligatorio que reclutaba miles de indígenas para extraer mineral en los socavones.",
                            "En un festival de danza folclórica celebrado anualmente en la plaza mayor.",
                            "En un impuesto pagado exclusivamente con productos textiles de lana de alpaca.",
                            "En la entrega gratuita de tierras agrícolas a los mineros más veteranos."
                        ],
                        "correctIndex": 0,
                        "explanation": "La mita colonial obligaba a miles de indígenas a trabajar forzosamente en condiciones infrahumanas dentro de las minas."
                    },
                    {
                        "question": "¿Qué divinidad tutelar del inframundo custodian y veneran los mineros en los socavones del Cerro Rico?",
                        "options": [
                            "El Tío, a quien ofrecen alcohol, tabaco y hojas de coca para pedir protección contra derrumbes y hallar vetas.",
                            "El dios griego Poseidón para evitar inundaciones subterráneas.",
                            "Una estatua ecuestre del rey Carlos V colocada en la entrada de las galerías.",
                            "Un dragón de bronce fabricado por los comerciantes de la ruta de la seda."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Tío es la deidad protectora de las profundidades mineras a la que se rinde culto diario con ofrendas rituales."
                    }
                ]
            }
        }
    }

    # Regional Story 3: La Paz y El Alto
    story_bolivia_03 = {
        "id": "b2-boliviaaltiplano-03",
        "title": "La hoyada y la cumbre: Cholitas, cholets y la vanguardia aymara",
        "level": "B2",
        "lesson": 3,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una travesía urbana y sociológica por la conurbación de La Paz y El Alto: el contraste entre la cuenca profunda del cañón paceño y la planicie rebelde a más de cuatro mil metros, la democratización del espacio urbano mediante los teleféricos aéreos, la revolución arquitectónica neoandina de los cholets de Freddy Mamani y el orgullo imparable de las cholitas aymaras.",
        "characters": [
            "Arquitecto Freddy Mamani",
            "Cholita empresaria Doña Remedios",
            "Ingeniero de Mi Teleférico Carlos",
            "Joven estudiante alteño Jhonny"
        ],
        "narration": {
            "paragraphs": [
                "Pocas postales urbanas en el mundo provocan un estremecimiento tan profundo como asomarse desde el borde del altiplano hacia la hoyada de La Paz. En el fondo de un gigantesco cañón de arenisca arcillosa labrado por el río Choqueyapu a 3.600 metros de altitud, la sede de gobierno boliviana se despliega en una cascada de rascacielos modernos y barrios residenciales coronados por el coloso nevado del Illimani, cuyos tres picos de hielo eterno resplandecen como un guardián telúrico. Pero al elevar la mirada hacia la planicie superior, a 4.100 metros sobre el nivel del mar, se extiende El Alto: la ciudad más joven, populosa y rebelde de Bolivia, una metrópoli de casi un millón de habitantes predominantemente aymaras que en cuatro décadas pasó de ser una barriada periférica a convertirse en el corazón palpitante del poder político, comercial y social del país.",
                "Durante décadas, la abrupta topografía que separa a ambas urbes representó una frontera física y de clase casi infranqueable, donde descender o ascender por autopistas serpenteantes tomaba horas de caótico tráfico vehicular. Sin embargo, en 2014 esa fractura geográfica fue vencida por una proeza de ingeniería civil: la red de Mi Teleférico, el sistema de transporte por cable aéreo urbano más extenso, alto y moderno del planeta. Con más de treinta kilómetros de líneas codificadas en colores vistosos que sobrevuelan los techos de la urbe, miles de trabajadores, estudiantes y comerciantes viajan hoy en cabinas silenciosas suspendidas sobre el abismo en cuestión de minutos, transformando un servicio de transporte masivo en un símbolo democratizador de integración ciudadana. Con una puntualidad rigurosa y vistas panorámicas incomparables, el teleférico ha superado no solo las barreras orográficas más extremas, sino también los prejuicios clasistas que históricamente dividían a la urbe administrativa de la meseta obrera.",
                "En las anchas avenidas de El Alto, este vigor económico de la floreciente burguesía comercial aymara encontró su más deslumbrante manifestación visual: la arquitectura neoandina, conocida popularmente como los *cholets* (término que fusiona las palabras *cholo* y *chalé*). Creados por el audaz arquitecto autodidacta Freddy Mamani, estos edificios monumentales de hasta siete pisos desafían la monocromía grisácea del altiplano con fachadas de vidrios reflectantes y motivos geométricos policromáticos en verde esmeralda, naranja encendido y azul cobalto, inspirados directamente en la iconografía de los tejidos ceremoniales y las ruinas milenarias de Tiwanaku.",
                "Un cholet no es una simple residencia familiar: es un complejo social integral diseñado para la celebración comunitaria. En la planta baja alberga galerías comerciales; en los pisos intermedios, suntuosos salones de fiesta adornados con centenares de luces led y columnas monumentales donde se celebran bodas y bautizos al compás de orquestas folclóricas de morenada; y en la cúspide del edificio, coronando la estructura, se alza un chalé unifamiliar de dos plantas con techo a dos aguas donde residen los propietarios, contemplando la inmensidad del altiplano desde las alturas.",
                "En el centro de esta vibrante transformación social brillan las mujeres aymaras: las célebres cholitas paceñas y alteñas. Portando con altivez sus voluminosas polleras plisadas de seda, sus mantas abrigadas de vicuña prendidas con broches de oro macizo y sus tradicionales sombreros borsalinos de fieltro negro o café colocados con coquetería sobre largas trenzas azabache, las cholitas han quebrado de forma irreversible décadas de racismo y discriminación colonial. Antaño marginadas de las instituciones formales, hoy las mujeres de pollera dominan los mercados mayoristas, ejercen como abogadas en los tribunales, debaten como diputadas en la asamblea legislativa, conducen programas televisivos y escalan cumbres nevadas de seis mil metros de altitud. Destaca en este movimiento la hazaña deportiva de las cholitas escaladoras, quienes han coronado los picos más escarpados de los Andes vistiendo sus tradicionales faldas plisadas como emblema de resistencia física y afirmación cultural.",
                "La conurbación de La Paz y El Alto confirma que la modernidad en los Andes no exige la renuncia a la herencia indígena, sino todo lo contrario: una audaz resignificación del pasado milenario. En el sobrevuelo silencioso del teleférico, entre los destellos dorados de los cholets y el paso firme de las cholitas, late la certeza de que el pueblo aymara es el arquitecto indiscutible de su propio futuro."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué récord de infraestructura de transporte ostenta el sistema 'Mi Teleférico' de La Paz y El Alto?",
                        "options": [
                            "Es la red de transporte público por cable urbano más extensa, alta y moderna del planeta.",
                            "Es la única línea férrea subterránea construida enteramente bajo agua salada.",
                            "Es el teleférico más veloz del mundo diseñado exclusivamente para trenes de carga pesada.",
                            "Es una atracción turística que funciona únicamente durante las vacaciones de verano."
                        ],
                        "correctIndex": 0,
                        "explanation": "Mi Teleférico une La Paz y El Alto con más de 30 kilómetros de cables aéreos como transporte masivo regular."
                    },
                    {
                        "question": "¿En qué fuentes estéticas se inspira el arquitecto Freddy Mamani para diseñar los 'cholets' neoandinos de El Alto?",
                        "options": [
                            "En la iconografía geométrica de Tiwanaku y los colores vivos de los textiles y aguayos aymaras.",
                            "En las mansiones de madera victorianas del sur de los Estados Unidos.",
                            "En los tratados de arquitectura clasicista renacentista de Roma.",
                            "En los modelos de rascacielos minimalistas monocromáticos de Japón."
                        ],
                        "correctIndex": 0,
                        "explanation": "Mamani fusiona motivos tiwanakotas y colores intensos de textiles andinos en las fachadas de los cholets."
                    },
                    {
                        "question": "¿Cómo se manifiesta la reivindicación de las 'cholitas' aymaras en la sociedad boliviana contemporánea?",
                        "options": [
                            "Visten con orgullo su indumentaria tradicional mientras ocupan espacios de liderazgo en la economía, la justicia y la política.",
                            "Han abandonado por completo sus polleras tradicionales para vestir trajes occidentales de oficina.",
                            "Viven en aislamiento voluntario en comunidades campesinas remotas sin pisar las ciudades.",
                            "Tienen prohibido estudiar en las universidades estatales o participar en elecciones públicas."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las cholitas conquistaron universidades, parlamentos y empresas portando con dignidad sus polleras y sombreros."
                    }
                ]
            }
        }
    }

    # Regional Story 4: Hoja de Coca
    story_bolivia_04 = {
        "id": "b2-boliviaaltiplano-04",
        "title": "La hoja milenaria: Cosmovisión, acullico y la dignidad de la coca",
        "level": "B2",
        "lesson": 4,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la trascendencia cultural, médica y política de la hoja de coca en Bolivia: el ritual ancestral del acullico o masticado ritual, el uso en la challa y las ofrendas a la Pachamama, la resistencia de los sindicatos campesinos de los Yungas y el Chapare, y la victoria diplomática que consagró el principio de que 'la coca no es cocaína'.",
        "characters": [
            "Yatiri Don Mamani",
            "Dirigente cocalera Doña Leonor",
            "Médico etnofarmacólogo Álvaro",
            "Joven campesino Zenón"
        ],
        "narration": {
            "paragraphs": [
                "En el amanecer helado de una cumbre altiplánica donde el viento silba entre los roquedales, un anciano sabio aymara o *yatiri* abre con manos pausadas su *chuspa*, una pequeña bolsa de lana de vicuña tejida con motivos solares. De su interior extrae un puñado de hojas verdes ovaladas y secas, seleccionando con reverencia las piezas enteras y perfectas. Antes de iniciar la jornada de trabajo o emprender una decisión comunal de trascendencia, el anciano eleva las hojas hacia el sol naciente, sopla tres veces en dirección a los cuatro puntos cardinales pidiendo permiso a los Apus tutelares y realiza la *challa*: el agradecimiento recíproco a la Pachamama que sustenta la vida. Es el prólogo sagrado del *acullico*, la práctica milenaria de mascar la hoja de coca que ha nutrido el espíritu y el cuerpo de las civilizaciones andinas durante más de tres mil años.",
                "El acullico —conocido también como *pijcheo* en los valles quechuas— no es un acto vulgar de consumo recreativo, sino un ritual medicinal y social cargado de profundo simbolismo comunitario. El usuario introduce cuidadosamente una a una las hojas secas en el carrillo de la mejilla, formando un bolo compacto que se humedece con saliva sin ser masticado ni tragado. Para activar los catorce alcaloides naturales que contiene la planta, se añade una pizca de *llipta*, una pasta dulce elaborada con ceniza vegetal de quinua y cáscara de plátano rica en carbonato de calcio. La infusión natural que se desprende lentamente alivia de inmediato la fatiga del trabajo físico extenuante, amortigua los dolores del hambre en la montaña y combate con eficacia comprobada el mal de altura o *soroche*. En las asambleas comunales del altiplano y los valles, el acto de compartir coca de una chuspa común sella pactos de palabra, resuelve desacuerdos vecinales y refrenda compromisos matrimoniales bajo un principio rector de confianza mutua.",
                "Etnofarmacólogos de todo el mundo han constatado que la hoja de coca en su estado natural es un prodigio nutricional: posee concentraciones excepcionales de calcio, hierro, fósforo, vitamina A y riboflavina, superando los valores de muchos cereales y vegetales de consumo masivo. La planta actúa además como un regulador metabólico natural de comprobada eficacia, aportando energía constante sin generar dependencia física ni alteraciones psicológicas adversas. Sin embargo, a lo largo del siglo XX, esta planta sagrada fue objeto de un estigma internacional feroz y desproporcionado, promovido por convenciones internacionales antidrogas que la equipararon falsamente con la cocaína, ignorando que para elaborar un solo gramo del narcótico refinado se requieren procesos químicos industriales que destruyen por completo las propiedades benéficas de la hoja natural.",
                "En las décadas de 1980 y 1990, esta criminalización extranjera desató la violencia en los valles subtropicales de los Yungas de La Paz y el trópico de Cochabamba (el Chapare), donde miles de familias campesinas dependían del cultivo tradicional de la coca para sobrevivir. Bajo la imposición de programas de erradicación forzada militarizada financiados por potencias extranjeras, los campesinos sufrieron represión y encarcelamientos masivos. Fue en esas trincheras de resistencia agraria donde germinaron los sindicatos cocaleros, forjando un movimiento social e indígena de una cohesión inédita que transformó el panorama político de Bolivia bajo una consigna inquebrantable: 'La coca no es cocaína; la coca es cultura, medicina y soberanía nacional'.",
                "El triunfo de esta lucha popular cristalizó en la Constitución Política del Estado de 2009, cuyo artículo 384 declara solemnemente a la coca como patrimonio cultural, recurso natural renovable de la biodiversidad de Bolivia y factor de cohesión social, garantizando su producción, comercialización y consumo tradicional. Cuatro años más tarde, en 2013, la diplomacia boliviana protagonizó una victoria histórica en la sede de las Naciones Unidas en Viena: tras años de debates científicos, la comunidad internacional aceptó la reserva soberana que despenalizó el acullico tradicional dentro del territorio boliviano.",
                "Hoy, la coca se industrializa legalmente en refrescos, licores, harinas alimenticias, infusiones medicinales, pomadas analgésicas y cosméticos que se comercializan en todo el país. Al compartir unas hojas verdes en un velorio, en una asamblea comunal o en la cumbre de un nevado, los bolivianos celebran la victoria de la sabiduría ancestral sobre el prejuicio colonial, confirmando que la sagrada hoja de coca continuará latiendo como el corazón verde e inmarcesible de los Andes."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué función cumple la 'llipta' (pasta de ceniza alcalina) durante el ritual tradicional del acullico?",
                        "options": [
                            "Aporta un medio alcalino que activa los nutrientes y alcaloides naturales presentes en las hojas secas de coca.",
                            "Endulza el agua de los ríos para facilitar la pesca de truchas.",
                            "Sirve como tinte para teñir las lanas de vicuña de color negro oscuro.",
                            "Es un pegamento vegetal para sellar las bolsas de cuero donde se guardan las hojas."
                        ],
                        "correctIndex": 0,
                        "explanation": "La llipta alcaliniza la saliva, permitiendo la absorción paulatina de los nutrientes y alcaloides de la coca."
                    },
                    {
                        "question": "¿Cuál fue el argumento central defendido por Bolivia ante las Naciones Unidas para despenalizar el acullico en 2013?",
                        "options": [
                            "Demostrar que la hoja en estado natural es una práctica milenaria alimenticia y cultural que no debe confundirse con la cocaína.",
                            "Solicitar que la cocaína se declare medicamento obligatorio en los hospitales de todo el mundo.",
                            "Proponer la sustitución del café y el té por bebidas alcohólicas fermentadas.",
                            "Renunciar a todos los tratados comerciales internacionales para aislar al país."
                        ],
                        "correctIndex": 0,
                        "explanation": "Bolivia demostró científicamente que el acullico tradicional es inocuo y constituye un derecho cultural inalienable."
                    },
                    {
                        "question": "¿En qué artículo de la Constitución boliviana de 2009 se protege a la hoja de coca como patrimonio cultural?",
                        "options": [
                            "En el artículo 384, que la consagra como recurso natural y factor de cohesión social.",
                            "En el preámbulo militar sobre el servicio de defensa de fronteras.",
                            "En una disposición transitoria que ordenaba su erradicación en diez años.",
                            "En un anexo secreto firmado exclusivamente por embajadores extranjeros."
                        ],
                        "correctIndex": 0,
                        "explanation": "El artículo 384 de la Constitución de 2009 protege a la hoja de coca como patrimonio del Estado y de los pueblos."
                    }
                ]
            }
        }
    }

    # Regional Story 5: Estado Plurinacional
    story_bolivia_05 = {
        "id": "b2-boliviaaltiplano-05",
        "title": "La refundación de la patria: Treinta y seis naciones y la luz de la Wiphala",
        "level": "B2",
        "lesson": 5,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una crónica sobre la refundación institucional y descolonizadora de Bolivia: la Asamblea Constituyente de Sucre de 2006 a 2008, la promulgación de la Constitución Política del Estado de 2009, el reconocimiento de treinta y seis naciones originarias, la entronización de la Wiphala como emblema patrio y el horizonte ético del Suma Qamaña o Vivir Bien.",
        "characters": [
            "Constituyente aymara Silvia Lazarte",
            "Jurista constitucionalista René",
            "Dirigente guaraní Marcial",
            "Joven abogada quechua Lucía"
        ],
        "narration": {
            "paragraphs": [
                "El 7 de febrero de 2009, en una plaza de El Alto colmada por decenas de miles de indígenas, campesinos, obreros y estudiantes que agitaban banderas tricolores y un mar resplandeciente de cuadrantes multicolores de la Wiphala, Bolivia vivió el momento de refundación institucional más trascendental de sus dos siglos de vida republicana. Tras meses de intensos y apasionados debates en la histórica ciudad colonial de Sucre, una Asamblea Constituyente presidida por primera vez en la historia por una mujer indígena campesina, la líder quechua Silvia Lazarte, entregaba al pueblo la nueva Constitución Política del Estado, aprobada por una abrumadora mayoría ciudadana en referéndum nacional. Nacía oficialmente el Estado Plurinacional de Bolivia, dejando atrás el viejo modelo de república monocultural y excluyente que durante casi dos centurias había gobernado a espaldas de su mayoría social originaria.",
                "El corazón conceptual de esta transformación radica en el principio de la plurinacionalidad. La nueva carta magna reconoce explícitamente la preexistencia colonial de treinta y seis naciones y pueblos indígena originario campesinos —desde las populosas naciones aymara y quechua de la cordillera andina hasta los pueblos guaraní, chiquitano, moxeño, chimán y ayoreo de las llanuras orientales y la selva amazónica—. Lejos de fragmentar el país, el texto constitucional articula la unidad nacional sobre la base del respeto irrestricto a la diversidad cultural, consagrando a los treinta y seis idiomas originarios como lenguas oficiales del Estado junto al castellano, y obligando a los funcionarios públicos a comunicarse en al menos una lengua nativa de su región. Esta transformación educativa y cultural fomenta la revalorización de los saberes médicos ancestrales, los calendarios agrícolas originarios y las formas comunitarias de deliberación democrática en todos los niveles del sistema escolar público.",
                "Uno de los avances jurídicos más revolucionarios del modelo plurinacional fue la consagración del pluralismo jurídico de igual jerarquía. La constitución reconoció que la justicia indígena originaria campesina —impartida por las autoridades tradicionales de los ayllus y comunidades mediante el consenso, la conciliación comunitaria y la reparación del daño moral o material— posee idéntico rango y validez constitucional que la justicia ordinaria administrada por los tribunales del Estado. Este reconocimiento puso fin a siglos en los que los sistemas ancestrales de resolución de conflictos eran tildados despectivamente de salvajes o ilegales por las élites urbanas.",
                "Símbolo indiscutible de este amanecer descolonizador fue la entronización oficial de la Wiphala como símbolo patrio del Estado, obligatoria en todos los edificios públicos y ceremonias diplomáticas junto a la bandera roja, amarilla y verde. Con sus cuarenta y nueve cuadrantes repartidos en siete colores del arcoíris dispuestos en diagonal, la Wiphala no es una simple bandera: es un ideograma cósmico y matemático que representa la dualidad complementaria (*chacha-warmi*), la solidaridad comunitaria, la defensa de la Madre Tierra y la armonía biocéntrica entre todos los seres vivos del universo. Cada uno de sus siete colores encierra un significado filosófico preciso: desde la energía y la tierra fértil hasta la administración comunitaria, la ciencia y la soberanía del pensamiento colectivo.",
                "Asimismo, la carta magna incorporó como principios ético-morales rectores de la sociedad preceptos milenarios de la filosofía andina y amazónica: el *ama suwa* (no seas ladrón), *ama llulla* (no seas mentiroso) y *ama qhilla* (no seas flojo), complementados por el horizonte civilizatorio supremo del *Suma Qamaña* (el 'Vivir Bien' aymara) y el *Ñandereko* (la 'vida armoniosa' guaraní). Estos principios postulan que el verdadero desarrollo de una sociedad no se mide por la acumulación egoísta de bienes materiales ni por la depredación ilimitada de los recursos naturales, sino por la capacidad colectiva de convivir en paz comunitaria, dignidad compartida y reverencia por la Pachamama.",
                "El Estado Plurinacional de Bolivia ha demostrado al mundo entero que la descolonización de las instituciones no es una utopía inalcanzable, sino una realidad palpable construida con valentía democrática. Al ondear la Wiphala sobre las cumbres nevadas y en los valles amazónicos, la patria de Tupac Katari y Bartolina Sisa proclama con orgullo su verdad luminosa: que solo reconociendo todas las raíces de un pueblo puede florecer un destino de justicia, fraternidad e igualdad para todos los seres humanos."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Quién presidió la histórica Asamblea Constituyente que redactó la nueva Constitución de Bolivia entre 2006 y 2008?",
                        "options": [
                            "Silvia Lazarte, líder indígena quechua y campesina de amplia trayectoria comunitaria.",
                            "Un magistrado enviado por la corte internacional de La Haya.",
                            "El embajador de las Naciones Unidas acreditado en La Paz.",
                            "El decano de la facultad de derecho de la Universidad de Harvard."
                        ],
                        "correctIndex": 0,
                        "explanation": "Silvia Lazarte marcó un hito histórico al presidir la asamblea constituyente que fundó el Estado Plurinacional."
                    },
                    {
                        "question": "¿Qué implica la consagración constitucional del 'pluralismo jurídico' en el Estado Plurinacional de Bolivia?",
                        "options": [
                            "Que la justicia indígena comunitaria posee igual jerarquía y valor legal que la justicia ordinaria del Estado.",
                            "Que las leyes se redactan exclusivamente en idioma latín para todos los tribunales.",
                            "Que se eliminan los juzgados civiles permitiendo únicamente juicios militares.",
                            "Que las sentencias deben ser ratificadas por cortes extranjeras para tener validez."
                        ],
                        "correctIndex": 0,
                        "explanation": "El pluralismo jurídico reconoce la misma jerarquía constitucional a la justicia comunitaria originaria y a la ordinaria."
                    },
                    {
                        "question": "¿Cuál es la premisa fundamental del paradigma del 'Vivir Bien' (Suma Qamaña) adoptado en la Constitución?",
                        "options": [
                            "Priorizar la armonía con la comunidad y la Madre Tierra frente al consumismo y la acumulación material ilimitada.",
                            "Promover la industrialización pesada sin considerar el impacto ecológico en los bosques.",
                            "Eliminar todos los intercambios comerciales con los países vecinos de América del Sur.",
                            "Fomentar la competencia económica individualista desregulada en todas las áreas de la sociedad."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Vivir Bien plantea un modelo de desarrollo biocéntrico en armonía social y respeto absoluto a la Pachamama."
                    }
                ]
            }
        }
    }

    # Regional Story 6: Capstone regional (El guardián de las alturas y la Bolivia andina)
    story_bolivia_capstone = {
        "id": "b2-boliviaaltiplano-consolidation",
        "title": "El corazón de bronce: Altura, memoria y soberanía en la Bolivia plurinacional",
        "level": "B2",
        "lesson": 6,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "Una síntesis panorámica de los Estudios Regionales sobre el altiplano y la Bolivia andina: el lago Titicaca y la termorregulación lacustre, el Cerro Rico de Potosí y la historia minera de la plata, la vanguardia arquitectónica de los cholets y el poder de las cholitas en La Paz y El Alto, la dignidad ancestral de la hoja de coca y la refundación constitucional del Estado Plurinacional.",
        "characters": [
            "Tupac Katari",
            "Bartolina Sisa",
            "Silvia Lazarte",
            "Freddy Mamani"
        ],
        "narration": {
            "paragraphs": [
                "En la cima del continente suramericano, donde el aire puro y enrarecido exige respirar con la lentitud solemne de las cumbres nevadas, el altiplano de Bolivia se alza como una de las geografías más imponentes, espirituales y complejas del mundo contemporáneo. Custodiada por los macizos colosales del Illimani, el Sajama y el Huayna Potosí, esta meseta intermontana a cuatro mil metros de altitud demostró a lo largo de milenios que la dureza de las heladas y la aridez del clima no son barreras para el florecimiento humano, sino el crisol donde se templó una civilización comunitaria de inquebrantable entereza moral: la estirpe andina de la raza de bronce. En este territorio indómito de horizontes diáfanos, la memoria histórica no es una reliquia inerte guardada en museos, sino una fuerza viva que nutre las aspiraciones contemporáneas de autodeterminación y justicia social de millones de ciudadanos.",
                "En el regazo del altiplano, las aguas azul cobalto del lago Titicaca continúan actuando como el gran corazón termorregulador que permite la vida en las alturas. Desde las orillas donde florecen los totorales y bavegan las balsas trenzadas a mano hasta las escalinatas sagradas de la Isla del Sol, el Titicaca custodia el mito fundacional de los hijos del sol y mantiene vivo el lazo de reciprocidad que une a los ayllus aymaras y quechuas con las fuerzas sagradas de la naturaleza y los pastizales de los bofedales.",
                "Hacia el sur, recortándose contra el cielo de la puna, el Cerro Rico de Potosí recuerda al mundo las contradicciones más profundas de la historia humana. La montaña que alimentó la opulencia de la corte colonial y acuñó los reales de a ocho que circularon por los cinco continentes fue también el escenario de la mita minera y del dolor indecible de millones de mitayos. Hoy, en los socavones oscuros donde los mineros rinden ofrendas de alcohol y coca a El Tío para proteger sus vidas, Potosí se erige como un monumento vivo al trabajo, la memoria obrera y la tenacidad inquebrantable de sus pueblos.",
                "En la cuenca vertiginosa de La Paz y en la combativa planicie superior de El Alto, esa memoria ancestral dialoga en igualdad de condiciones con la vanguardia del siglo XXI. Enlazadas por la red de teleféricos urbanos más extensa del planeta, las ciudades presencian el florecimiento de los cholets de Freddy Mamani, cuyas fachadas polícromas inspiradas en los textiles de Tiwanaku proclaman el empoderamiento económico de una burguesía aymara orgullosa de sus raíces. Y en las calles y universidades, las cholitas bolivianas, con sus polleras plisadas y sombreros borsalinos, encarnan la victoria definitiva sobre la discriminación colonial, demostrando que la dignidad no se negocia. Esta ebullición cultural alteña demuestra que la identidad andina es capaz de asimilar las innovaciones tecnológicas globales sin perder un ápice de su autenticidad ni de su compromiso con la comunidad de origen.",
                "Esa misma dignidad late en la defensa incondicional de la sagrada hoja de coca. Mediante la práctica milenaria del acullico, compartida en asambleas comunitarias y jornadas de trabajo, la sociedad boliviana demostró ante los organismos internacionales que la coca es alimento, medicina y patrimonio cultural, desterrando el estigma foráneo bajo la consigna de que la coca en su estado natural representa la soberanía y la autodeterminación de los pueblos originarios.",
                "Todo este caudal milenario confluyó en la refundación democrática del Estado Plurinacional en 2009. Al consagrar a treinta y seis naciones originarias en pie de igualdad, reconocer la justicia indígena comunitaria y adoptar la Wiphala como símbolo patrio de hermandad y equilibrio cósmico, Bolivia propuso al mundo entero el paradigma civilizatorio del Suma Qamaña o Vivir Bien: una concepción del progreso donde la armonía con la Pachamama y la solidaridad comunitaria se sitúan por encima de la acumulación material depredadora.",
                "Al contemplar la trayectoria inmemorial de la Bolivia andina, el viajero comprende que su mayor tesoro no reposa en las vetas de plata del cerro ni en las salmueras de litio del salar, sino en el alma invencible de su gente. En este suelo donde el pasado sagrado guía los pasos del porvenir soberano, los pueblos del altiplano continúan enseñando a la humanidad que la verdadera libertad brota de la tierra, se defiende con valentía y florece eternamente bajo los colores luminosos de la Wiphala."
            ],
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué síntesis geográfica y cultural define la singularidad del altiplano boliviano en América del Sur?",
                        "options": [
                            "Una meseta a cuatro mil metros donde el lago Titicaca, la historia minera de Potosí y la cultura aymara forjaron una identidad comunitaria invencible.",
                            "Un archipiélago de islas desiertas donde no existe población permanente ni agricultura.",
                            "Una selva tropical pantanosa dominada exclusivamente por plantaciones de caña de azúcar.",
                            "Un valle costero árido sin montañas ni tradiciones indígenas conservadas."
                        ],
                        "correctIndex": 0,
                        "explanation": "El altiplano boliviano amalgama la termorregulación de Titicaca, la historia de Potosí y el vigor de las naciones aymara y quechua."
                    },
                    {
                        "question": "¿De qué manera el paradigma del 'Suma Qamaña' (Vivir Bien) cuestiona los modelos tradicionales de desarrollo?",
                        "options": [
                            "Plantea que el bienestar radica en la armonía biocéntrica con la Madre Tierra y la comunidad, no en la acumulación material egoísta.",
                            "Obliga a todas las industrias a utilizar carbón mineral como única fuente de energía.",
                            "Prohíbe el uso de la electricidad y de cualquier avance tecnológico moderno.",
                            "Promueve la privatización de todos los recursos hídricos en favor de empresas multinacionales."
                        ],
                        "correctIndex": 0,
                        "explanation": "El Suma Qamaña postula un equilibrio armónico biocéntrico con la naturaleza y la comunidad por encima del extractivismo depredador."
                    },
                    {
                        "question": "¿Qué papel desempeñaron las mujeres indígenas (cholitas y constituyentes como Silvia Lazarte) en la Bolivia del siglo XXI?",
                        "options": [
                            "Lideraron la descolonización institucional, presidieron la Asamblea Constituyente y conquistaron espacios de poder político y profesional.",
                            "Fueron relegadas exclusivamente a labores domésticas sin participación en los debates públicos.",
                            "Abandonaron sus atuendos ancestrales para integrarse a órdenes religiosas de clausura.",
                            "Se trasladaron a vivir al extranjero sin intervenir en la redacción de la nueva constitución."
                        ],
                        "correctIndex": 0,
                        "explanation": "Las mujeres indígenas protagonizaron la refundación plurinacional liderando la constituyente y conquistando la vida pública."
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
    write_json(f"stories/classics/b2/{c_unit}.json", to_schema_story(story_core_20))
    # Regional lesson stories:
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
        ("b2-20-01", "lesson.b2.20.01", "Voz pasiva analítica con ser y participio",
         "Master analytical passive sentences with 'ser + participio' and enforce strict gender and number agreement with the subject patient.",
         "voz pasiva analítica con ser y concordancia de género y número del participio",
         ["Construct analytical passive sentences with 'ser' in various tenses.", "Ensure gender and number agreement of past participles with subject patients.", "Identify contexts where the analytical passive is preferred over active voice."]),
        ("b2-20-02", "lesson.b2.20.02", "El complemento agente introducido por por",
         "Deploy agentive prepositional phrases with 'por' in passive sentences when the agent provides indispensable historical or legal information.",
         "estructura, uso y restricciones estilísticas del complemento agente con por",
         ["Identify when agentive complements with 'por' are essential in formal prose.", "Distinguish between conscious human agents and instrumental means.", "Avoid redundant or awkward agent phrases in general statements."]),
        ("b2-20-03", "lesson.b2.20.03", "La pasiva de estado con estar y participio",
         "Distinguish processual action passives with 'ser' from resultant state passives with 'estar + participio'.",
         "pasiva de estado resultativa con estar y participio frente a la pasiva de proceso con ser",
         ["Select between eventive 'ser + participio' and stative 'estar + participio'.", "Describe final resultant conditions in institutional and historical contexts.", "Apply correct gender/number agreement in resultative state clauses."]),
        ("b2-20-04", "lesson.b2.20.04", "Participios irregulares y formas dobles",
         "Master regular and irregular double past participle forms and their distinctive verbal vs adjectival syntactic distributions.",
         "morfología y uso de participios dobles regulares e irregulares en español",
         ["Distinguish regular verbal participles (imprimido) from adjectival forms (impreso).", "Apply correct double participles with verbs like elegir/electo and proveer/provisto.", "Avoid confusing pure adjectives with verbal participles."]),
        ("b2-20-05", "lesson.b2.20.05", "Selección estilística entre pasivas",
         "Select with stylistic mastery between reflexive passives, analytical passives with 'ser', and resultative passives with 'estar'.",
         "criterios de selección y alternancia estilística entre pasiva refleja, analítica y de estado",
         ["Evaluate stylistic naturalness across different passive structures.", "Alternate passive types to avoid repetitive Germanic passive calques.", "Produce balanced, elegant formal prose adhering to CEFR B2 house style."])
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
        "id": "lesson.b2.20.consolidation",
        "title": "Consolidación B2: Voz pasiva y Raza de bronce de Alcides Arguedas",
        "level": "B2",
        "goal": "Synthesize analytical and resultative passive structures through Alcides Arguedas's indigenist landmark Raza de bronce.",
        "grammar": "síntesis de voz pasiva analítica y de estado y adaptación de Raza de bronce",
        "sections": [
            {"type": "goal", "items": [
                "Master participle agreement in analytical passives across all tenses.",
                "Differentiate clearly between action passives (ser) and resultative state passives (estar).",
                "Analyze the tragic struggle and rebellion of the Aymara people against feudal dispossession."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/classics/b2/{c_unit}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{l6_con}-ex.json", "exerciseRefs": [f"{l6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Aplico la concordancia de género y número en participios pasivos con 'ser'.",
                "Distingo con precisión entre la pasiva de acción ('fue destruido') y de estado ('está destruido').",
                "Utilizo adecuadamente el complemento agente con 'por' sin caer en calcos forzados.",
                "Manejo las formas dobles de participios regulares e irregulares en la prosa formal."
            ]}
        ]
    })

    # Regional Lessons 1-5
    reg_lessons_info = [
        ("b2-boliviaaltiplano-01", "lesson.b2.boliviaaltiplano.01", "El altiplano a cuatro mil metros y el lago Titicaca",
         "Explore the high-altitude geography of the Bolivian altiplano, Lake Titicaca, and Aymara totora reed navigation.",
         "geomorfología del altiplano boliviano, termorregulación del Titicaca y cosmovisión lacustre",
         ["Analyze the physical geography of the high plateau and Cordillera Real peaks.", "Examine the vital microclimatic role of Lake Titicaca in moderating highland frosts.", "Deploy high-altitude geography, wetlands, and lacustrine vocabulary (altiplano, totora, bofedal, gélido)."]),
        ("b2-boliviaaltiplano-02", "lesson.b2.boliviaaltiplano.02", "El Cerro Rico de Potosí y la plata que cambió el mundo",
         "Investigate the history of the Cerro Rico of Potosí, colonial silver mining, the mita labor levy, and El Tío.",
         "historia minera virreinal del Cerro Rico, economía global de la plata y culto a El Tío",
         ["Analyze the historical impact of the Potosí silver bonanza on global trade.", "Examine the human reality of the colonial mita labor system in the mine shafts.", "Deploy mining history, colonial coinage, and metallurgy vocabulary (socavón, mita, plata, metalúrgico)."]),
        ("b2-boliviaaltiplano-03", "lesson.b2.boliviaaltiplano.03", "La Paz y El Alto: Cholitas, cholets y modernidad aymara",
         "Explore the metropolitan contrast between La Paz and El Alto, urban cable cars, neo-Andean cholets, and proud cholitas.",
         "urbanismo andino, red de teleféricos, arquitectura cholet y empoderamiento de la mujer de pollera",
         ["Analyze the geographic and social articulation between La Paz and El Alto via Mi Teleférico.", "Explore Freddy Mamani's neo-Andean cholets and their Tiwanaku geometric inspiration.", "Deploy urban architecture, indigenous pride, and cultural identity vocabulary (cholet, cholita, pollera, teleférico)."]),
        ("b2-boliviaaltiplano-04", "lesson.b2.boliviaaltiplano.04", "La hoja de coca: Cosmovisión ancestral frente al estigma",
         "Analyze the cultural, nutritional, and diplomatic significance of the sacred coca leaf, acullico, and sovereignty.",
         "etnobotánica de la coca, ritual del acullico, challa a la Pachamama y despenalización internacional",
         ["Trace the millenary cultural and spiritual significance of the coca leaf and acullico.", "Distinguish between natural nutritious coca leaf and illicit refined cocaine.", "Deploy ethnobotanical, ritual, and agrarian sovereignty vocabulary (acullico, chuspa, challa, alcaloide)."]),
        ("b2-boliviaaltiplano-05", "lesson.b2.boliviaaltiplano.05", "El Estado Plurinacional y la refundación constitucional",
         "Examine the 2009 constitutional refoundation of Bolivia as a Plurinational State, 36 indigenous nations, and Suma Qamaña.",
         "derecho constitucional plurinacional, pluralismo jurídico comunitario, Wiphala y Vivir Bien",
         ["Analyze the constitutional recognition of thirty-six native indigenous nations.", "Explore the legal equality between indigenous community justice and ordinary state justice.", "Deploy constitutional law, decolonization, and indigenous statecraft vocabulary (wiphala, plurinacionalidad, originario, comunitario)."])
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
        "id": "lesson.b2.boliviaaltiplano.consolidation",
        "title": "Consolidación Regional: El guardián de las alturas y la Bolivia andina",
        "level": "B2",
        "goal": "Consolidate regional studies on highland Bolivia: Lake Titicaca, Potosí silver mining, neo-Andean cholets, coca dignity, and Plurinational constitutionalism.",
        "grammar": "síntesis de estudios regionales de la Bolivia andina: Titicaca, Potosí, cholets y Estado Plurinacional",
        "sections": [
            {"type": "goal", "items": [
                "Synthesize high-altitude plateau ecology, lake hydrology, and mining history.",
                "Appreciate Aymara urban empowerment, neo-Andean architecture, and cultural pride.",
                "Reflect on the constitutional paradigm of the Plurinational State and Living Well."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": f"stories/world/b2/{r6_con}.json"},
            {"type": "exercise-group", "title": "Review", "ref": f"exercises/b2/{r6_con}-ex.json", "exerciseRefs": [f"{r6_con}.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Comprendo la importancia climática y cultural del lago Titicaca en el altiplano.",
                "Reconozco el impacto económico global y la memoria obrera del Cerro Rico de Potosí.",
                "Valoro la vanguardia de los cholets alteños y el empoderamiento de las cholitas.",
                "Explico la dignidad ancestral de la hoja de coca y el ritual del acullico.",
                "Entiendo los pilares jurídicos y descolonizadores del Estado Plurinacional de Bolivia."
            ]}
        ]
    })

    print("Completed LatAm Unit 20 (Bolivia Altiplano) generation!")

    # -------------------------------------------------------------------------
    # 6. UPDATE CURRICULUM UNITS (b2.json)
    # -------------------------------------------------------------------------
    b2_units_path = LATAM_DIR / "curriculum" / "units" / "b2.json"
    b2_units = json.loads(b2_units_path.read_text(encoding="utf-8"))
    
    # Check if Unit 20 entries already exist
    has_core_20 = any(u.get("title") == "Analytical & Resultative Passives" for u in b2_units)
    has_reg_20 = any(u.get("title") == "Bolivia I: The High Altiplano, Potosí & The Indigenous Majority State" for u in b2_units)
    
    if not has_core_20:
        b2_units.append({
            "title": "Analytical & Resultative Passives",
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
    if not has_reg_20:
        b2_units.append({
            "title": "Bolivia I: The High Altiplano, Potosí & The Indigenous Majority State",
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
    print("Updated curriculum/units/b2.json with Unit 20!")

    # -------------------------------------------------------------------------
    # 7. Word Count Audit for Stories
    # -------------------------------------------------------------------------
    stories_to_audit = [
        ("story_core_20", story_core_20),
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
        print(f"{name:24}: {wc:4} words -> {status}")
        if not (650 <= wc <= 825):
            all_ok = False

    assert all_ok, "Some stories are out of the 650-825 word count bounds!"

if __name__ == "__main__":
    main()
