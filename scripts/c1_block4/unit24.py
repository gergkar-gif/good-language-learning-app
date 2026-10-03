#!/usr/bin/env python3
"""
Hungarian C1 Block 4 - Unit 24 Generator:
  - Track 1 (Core): Unit 24 — "Epistemology of Research, Academic Autonomy & Scientific Discovery" (c1-24)
  - Track 2 (Discourse): Unit 24 — "The University in Turmoil: Model Change, Autonomy & The European Horizon" (c1-felsooktatas)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block4.registry_helper import register_unit


def generate_unit_24():
    print("=== Generating C1 Unit 24 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-24-vocab": {"kind": "vocabulary"},
        "c1-felsooktatas-vocab": {"kind": "vocabulary"},
        "c1-adv-epistemic-methodological-evaluation": {"kind": "grammar"},
        "c1-participle-epistemological-chains": {"kind": "grammar"},
        "c1-adv-contrastive-academic-adversatives": {"kind": "grammar"},
        "c1-modal-teleological-scientific-inquiry": {"kind": "grammar"},
        "c1-adv-scalar-scientific-significance": {"kind": "grammar"},
        "c1-discourse-institutional-threat-framing": {"kind": "grammar"},
        "c1-modal-deontic-academic-freedom": {"kind": "grammar"},
        "c1-adv-proportional-academic-mobility": {"kind": "grammar"},
        "c1-epistemic-academic-uncertainty": {"kind": "grammar"},
        "c1-adv-conclusive-scientific-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-24-vocab": "reading",
        "c1-felsooktatas-vocab": "reading",
        "c1-adv-epistemic-methodological-evaluation": "epistemic methodological adverbials formulating rigorous scientific research evaluations",
        "c1-participle-epistemological-chains": "complex participial epistemic chains articulating sequential scientific induction",
        "c1-adv-contrastive-academic-adversatives": "contrastive academic adversative connectors distinguishing empirical proof from speculation",
        "c1-modal-teleological-scientific-inquiry": "teleological postpositional structures formulating epistemic scientific research objectives",
        "c1-adv-scalar-scientific-significance": "scalar evaluative adverbials calibrating scientific breakthroughs and paradigm shifts",
        "c1-discourse-institutional-threat-framing": "discourse framing markers diagnosing institutional crises in higher education",
        "c1-modal-deontic-academic-freedom": "deontic modal structures formulating statutory guarantees for academic freedom",
        "c1-adv-proportional-academic-mobility": "proportional correlative conjunctions mapping international academic isolation and drain",
        "c1-epistemic-academic-uncertainty": "epistemic stance markers articulating scientific hypotheses on institutional decline",
        "c1-adv-conclusive-scientific-synthesis": "evaluative synthesis particles formulating comprehensive manifestos for university autonomy",
    }
    
    core_title = "Epistemology of Research, Academic Autonomy & Scientific Discovery"
    core_stems = [f"c1-24-0{i}" for i in range(1, 6)] + ["c1-24-consolidation"]
    disc_title = "The University in Turmoil: Model Change, Autonomy & The European Horizon"
    disc_stems = [f"c1-felsooktatas-0{i}" for i in range(1, 6)] + ["c1-felsooktatas-consolidation"]
    
    register_unit(24, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-24)
    # ----------------------------------------------------
    core_intro = [
        "Hungarian scientific culture has given the world towering geniuses—from Bolyai and Eötvös to Szent-Györgyi, Neumann, and Katalin Karikó. Yet the pursuit of truth has always unfolded against the backdrop of political intrusion, institutional vulnerability, and the imperative for fearless intellectual freedom.",
        "In this unit, anchored by Albert Szent-Györgyi's philosophical essays and Nobel lectures on scientific integrity, university research, and human freedom ('Az emberi természet és a tudományos kutatás'), you will master the elevated academic register of epistemology, methodological evaluation, hypothesis formulation, and scientific paradigm shifts at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-24-01",
            "title": "Epistemology, Hypothesis Testing & Methodological Adverbials",
            "grammar_title": "Epistemic Methodological Adverbials Formulating Rigorous Scientific Research Evaluations",
            "grammar_skill": "c1-adv-epistemic-methodological-evaluation",
            "goals": [
                "I can analyze epistemology, scientific falsifiability, and empirical verification (*episztemológia, falszifikálhatóság, empirikus verifikáció, módszertani szigor*).",
                "I can employ elevated methodological adverbials evaluating research rigor (*módszertanilag, szisztematikusan, hipotetikusan, empirikusan alátámasztott módon*).",
                "I can debate the demarcation problem between empirical science and dogma in academic register."
            ],
            "vocab": [
                {"lemma": "episztemológia", "translation": "epistemology", "pos": "noun"},
                {"lemma": "falszifikálhatóság", "translation": "falsifiability", "pos": "noun"},
                {"lemma": "empirikus verifikáció", "translation": "empirical verification", "pos": "expression"},
                {"lemma": "módszertani szigor", "translation": "methodological rigor", "pos": "expression"},
                {"lemma": "tudományos paradigma", "translation": "scientific paradigm", "pos": "expression"},
                {"lemma": "hipotézis-felállítás", "translation": "hypothesis formulation", "pos": "noun"},
                {"lemma": "kutatási etika", "translation": "research ethics", "pos": "expression"},
                {"lemma": "ismételhetőség", "translation": "reproducibility / replicability", "pos": "noun"}
            ],
            "gr_text1": "Methodological adverbials qualify the epistemic status, validity, and procedural rigor of scientific findings: `módszertanilag megalapozottan` (methodologically well-founded), `szisztematikusan vizsgálva` (examining systematically), `empirikusan igazoltan` (empirically confirmed), `hipotetikusan felvetve` (hypothetically positing).",
            "gr_text2": "Example: `A kutatócsoport módszertanilag kifogástalanul, szisztematikusan ellenőrzött kísérletekkel és empirikusan igazolt adatokkal támasztotta alá az új elméletet`.",
            "gr_table": [
                ["A tézis módszertanilag megalapozottan cáfolja a korábbi hipotézist.", "The thesis methodologically solidly refutes the previous hypothesis."],
                ["Szisztematikusan elemezve a mintákat egyértelmű törvényszerűségek rajzolódnak ki.", "Systematically analyzing samples unambiguous regularities emerge."],
                ["A kísérlet eredményei empirikusan igazolt módon megismételhetők bármely laboratóriumban.", "The results of the experiment are reproducible in any laboratory in an empirically confirmed manner."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'falszifikálhatóság' Karl Popper tudományfilozófiájában?", [
                    "Azt a kritériumot, hogy egy tudományos elméletnek elvileg cáfolhatónak kell lennie tapasztalati adatok vagy kísérletek által.",
                    "A laboratóriumi műszerek szándékos megrongálását.",
                    "A tudományos cikkek latin nyelvű lefordítását."
                ], 0, ["c1-24-vocab"]),
                fb("grammar", "controlled", "A felállított tézis _____ megalapozott kísérleti adatokon nyugszik. (methodologically / módszertanilag)", "módszertanilag", "The established thesis rests on methodologically well-founded experimental data.", ["c1-adv-epistemic-methodological-evaluation"]),
                match("vocabulary", "controlled", [["episztemológia", "a megismerés természetét és határait vizsgáló filozófia"], ["falszifikálhatóság", "az elmélet kísérleti cáfolhatóságának követelménye"], ["empirikus verifikáció", "tapasztalati adatokkal történő igazolás"], ["ismételhetőség", "a kísérlet reprodukálhatósága független kutatók által"]], ["c1-24-vocab"]),
                fb("grammar", "practice", "A hipotézist _____ igazolt mérésekkel kell bizonyítani a bírálóbizottság előtt. (empirically / empirikusan)", "empirikusan", "The hypothesis must be proven with empirically confirmed measurements before the review committee.", ["c1-adv-epistemic-methodological-evaluation"]),
                sb("grammar", "practice", ["A", "kutatók", "szisztematikusan", "elemezték", "a", "kísérleti", "eredményeket."], ["A", "kutatók", "szisztematikusan", "elemezték", "a", "kísérleti", "eredményeket."], "Researchers systematically analyzed the experimental results.", ["c1-adv-epistemic-methodological-evaluation"]),
                dc("dialogue", [
                    {"speaker": "Tudományfilozófus", "text": "Mikor tekinthetünk egy elméletet valóban tudományosnak?"},
                    {"speaker": "Kutatóprofesszor", "text": "Csak akkor, ha módszertanilag kifogástalan, és kísérletileg _____ adatokra épül."},
                ], ["alátámasztott", "letagadott", "álmodott"], 0, ["c1-adv-epistemic-methodological-evaluation"]),
                sw("production", [{"prompt": "Write a sentence formulating an evaluation of research validity using a methodological adverbial.", "answer": "A kutatócsoport módszertanilag kifogástalan eljárással, szisztematikusan dokumentált laboratóriumi kísérletekkel cáfolta a korábbi biokémiai dogmákat."}], ["c1-adv-epistemic-methodological-evaluation"]),
                mc("grammar", "check", "Melyik kifejezés testesíti meg az empirikus kutatásformálás emelkedett határozói alakját?", [
                    "módszertanilag megalapozottan / szisztematikusan",
                    "hirtelen felkiáltva",
                    "lassan sétálva"
                ], 0, ["c1-adv-epistemic-methodological-evaluation"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-24-02",
            "title": "Scientific Induction & Complex Participial Chains",
            "grammar_title": "Complex Participial Epistemic Chains Articulating Sequential Scientific Induction",
            "grammar_skill": "c1-participle-epistemological-chains",
            "goals": [
                "I can analyze scientific induction, deductive reasoning, and paradigm shifts (*indukció, dedukció, paradigmaváltás, anomáliák felhalmozódása*).",
                "I can construct complex participial chains in `-va/-ve` articulating sequential discovery steps (*kísérletileg alátámasztva, hipotézist felállítva, tézist igazolva, adatokat összesítve*).",
                "I can characterize the epistemological leap from anomaly observation to theoretical revolution."
            ],
            "vocab": [
                {"lemma": "induktív következtetés", "translation": "inductive inference", "pos": "expression"},
                {"lemma": "deduktív levezetés", "translation": "deductive derivation", "pos": "expression"},
                {"lemma": "paradigmaváltás", "translation": "paradigm shift", "pos": "noun"},
                {"lemma": "anomália", "translation": "anomaly", "pos": "noun"},
                {"lemma": "heurisztikus érték", "translation": "heuristic value", "pos": "expression"},
                {"lemma": "elméleti modell", "translation": "theoretical model", "pos": "expression"},
                {"lemma": "kísérleti elrendezés", "translation": "experimental setup", "pos": "expression"},
                {"lemma": "szellemi áttörés", "translation": "intellectual breakthrough", "pos": "expression"}
            ],
            "gr_text1": "Complex participial chains in `-va/-ve` articulate the multi-step intellectual trajectory of scientific induction: `hipotézist felállítva` (having formulated a hypothesis), `adatokat összevetve` (comparing data), `anomáliákat feltárva` (uncovering anomalies), `kísérletileg alátámasztva` (experimentally substantiated).",
            "gr_text2": "Example: `A kutató a megfigyelt anomáliákból kiindulva, merész hipotézist felállítva és azt szigorú laboratóriumi mérésekkel alátámasztva hajtotta végre a tudományos áttörést`.",
            "gr_table": [
                ["A korábbi tévedéseket feltárva új elméleti keretet dolgoztak ki.", "Uncovering previous errors they developed a new theoretical framework."],
                ["A mérési adatokat szisztematikusan összegezve igazolták a felfedezést.", "Systematically summarizing measurement data they verified the discovery."],
                ["Új kísérleti elrendezést alkalmazva sikerült izolálni az ismeretlen molekulát.", "Applying a new experimental setup they succeeded in isolating the unknown molecule."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez Thomas Kuhn 'paradigmaváltásnak' a tudomány fejlődésében?", [
                    "Azt a forradalmi fordulatot, amikor a felhalmozódó anomáliák megdöntik a régi elméletet, és egy alapvetően új világkép válik uralkodóvá.",
                    "A laboratóriumi fehér köpenyek kékre cserélését.",
                    "A professzorok évi fizetésemelését az egyetemeken."
                ], 0, ["c1-24-vocab"]),
                fb("grammar", "controlled", "A megfigyelt anomáliákból kiindulva, merész hipotézist _____, új elméletet alkotott. (formulating / felállítva)", "felállítva", "Starting from observed anomalies, formulating a bold hypothesis, he created a new theory.", ["c1-participle-epistemological-chains"]),
                match("vocabulary", "controlled", [["paradigmaváltás", "az uralkodó tudományos világkép alapvető forradalmi átalakulása"], ["anomália", "a meglévő elmélettel nem magyarázható váratlan jelenség"], ["heurisztikus érték", "egy elmélet új felfedezéseket ösztönző ereje"], ["dedukció", "általános törvényekből az egyedire való logikai következtetés"]], ["c1-24-vocab"]),
                fb("grammar", "practice", "A kísérleti eredményeket szigorúan _____ bizonyították be az új molekula hatását. (substantiating / alátámasztva)", "alátámasztva", "Strictly substantiating the experimental results they proved the effect of the new molecule.", ["c1-participle-epistemological-chains"]),
                sb("grammar", "practice", ["A", "tényeket", "összegezve", "igazolták", "a", "forradalmi", "felfedezést."], ["A", "tényeket", "összegezve", "igazolták", "a", "forradalmi", "felfedezést."], "Summarizing the facts they verified the revolutionary discovery.", ["c1-participle-epistemological-chains"]),
                dc("dialogue", [
                    {"speaker": "Fizikus", "text": "Hogyan jutott el Einstein a relativitáselmélethez?"},
                    {"speaker": "Tudománytörténész", "text": "A fénysebesség állandóságának paradoxonából kiindulva, a newtoni téridőt _____ alkotta meg új elméletét."},
                ], ["újraértelmezve", "elfelejtve", "letagadva"], 0, ["c1-participle-epistemological-chains"]),
                sw("production", [{"prompt": "Write a sentence describing a scientific discovery process using an epistemic participial chain.", "answer": "A kutatók a korábbi elmélet tarthatatlanságát felismerve, új kísérleti elrendezést kidolgozva és az adatokat szigorúan elemezve hajtották végre a paradigmaváltó áttörést."}], ["c1-participle-epistemological-chains"]),
                mc("grammar", "check", "Melyik igeneves forma fejez ki logikai következtetési láncolatot a tudományos leírásban?", [
                    "hipotézist felállítva és kísérletileg alátámasztva",
                    "miután kiment a laboratóriumból",
                    "hogyha van kedve kutatni"
                ], 0, ["c1-participle-epistemological-chains"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-24-03",
            "title": "Empirical Proof vs. Speculation: Academic Adversatives",
            "grammar_title": "Contrastive Academic Adversative Connectors Distinguishing Empirical Proof from Speculation",
            "grammar_skill": "c1-adv-contrastive-academic-adversatives",
            "goals": [
                "I can analyze the boundary between speculative hypothesis and verified empirical evidence (*empirikus bizonyíték, spekulatív feltevés, replikációs válság*).",
                "I can employ elevated contrastive academic adversative connectors (*míg az elméleti premissza... addig a kísérleti verifikáció, ezzel szemben, ezzel ellentétben*).",
                "I can critique methodological over-claims and scientific publication bias in peer-reviewed literature."
            ],
            "vocab": [
                {"lemma": "empirikus bizonyíték", "translation": "empirical evidence", "pos": "expression"},
                {"lemma": "spekulatív feltevés", "translation": "speculative assumption", "pos": "expression"},
                {"lemma": "replikációs válság", "translation": "replication crisis", "pos": "expression"},
                {"lemma": "szakértői bírálat", "translation": "peer review", "pos": "expression"},
                {"lemma": "publikációs torzítás", "translation": "publication bias", "pos": "expression"},
                {"lemma": "tudományos konszenzus", "translation": "scientific consensus", "pos": "expression"},
                {"lemma": "statisztikai szignifikancia", "translation": "statistical significance", "pos": "expression"},
                {"lemma": "kontrollcsoport", "translation": "control group", "pos": "noun"}
            ],
            "gr_text1": "Contrastive academic adversatives rigorously differentiate between theoretical conjecture and empirical reality: `míg az elmélet... addig a tapasztalat` (while the theory... yet the experience), `ezzel szemben a kísérleti adatok` (in contrast with this the experimental data), `nem puszta spekuláció, hanem verifikált tény` (not mere speculation, but verified fact).",
            "gr_text2": "Example: `Míg a matematikai modell csupán elméleti lehetőséget vázolt fel, addig a laboratóriumi kontrollcsoportos mérések megdönthetetlen empirikus bizonyítékot szolgáltattak`.",
            "gr_table": [
                ["Míg az elméleti feltevés tetszetős volt, addig a kísérleti adatok egyértelműen megcáfolták.", "While the theoretical assumption was attractive, experimental data unambiguously refuted it."],
                ["Ezzel szemben a szigorú kettős vak vizsgálatok igazolták a gyógyszer hatékonyságát.", "In contrast with this, rigorous double-blind trials verified the medicine's efficacy."],
                ["A szerző nem puszta spekulációkra támaszkodott, hanem empirikusan igazolt tényekre.", "The author did not rely on mere speculations, but on empirically confirmed facts."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez a modern tudomány 'replikációs válságnak' (replication crisis)?", [
                    "Azt a riasztó jelenséget, hogy számos rangos folyóiratban megjelent kísérlet eredményeit független kutatók nem tudják megismételni.",
                    "A nyomtatott folyóiratok papírhiány miatti késését.",
                    "A mikroszkópok lencséinek párásodását a laboratóriumokban."
                ], 0, ["c1-24-vocab"]),
                fb("grammar", "controlled", "Míg a modell csupán spekulatív feltételezés volt, _____ a mérések vitathatatlan bizonyítékot szolgáltattak. (meanwhile / addig)", "addig", "While the model was merely a speculative assumption, meanwhile measurements provided indisputable evidence.", ["c1-adv-contrastive-academic-adversatives"]),
                match("vocabulary", "controlled", [["empirikus bizonyíték", "tapasztalati úton, mérésekkel igazolt tény"], ["spekulatív feltevés", "bizonyítatlan elméleti feltételezés"], ["szakértői bírálat", "független tudósok által végzett minőségellenőrzés (peer review)"], ["kontrollcsoport", "a kísérleti beavatkozásnak alá nem vetett összehasonlító csoport"]], ["c1-24-vocab"]),
                fb("grammar", "practice", "Az elmélet tetszetős volt, ezzel _____ a valóságban a kísérlet kudarcot vallott. (in contrast / szemben)", "szemben", "The theory was attractive, in contrast with this in reality the experiment failed.", ["c1-adv-contrastive-academic-adversatives"]),
                sb("grammar", "practice", ["Míg", "a", "hipotézis", "bizonytalan,", "addig", "a", "tény", "szilárd."], ["Míg", "a", "hipotézis", "bizonytalan,", "addig", "a", "tény", "szilárd."], "While the hypothesis is uncertain, the fact is solid.", ["c1-adv-contrastive-academic-adversatives"]),
                dc("dialogue", [
                    {"speaker": "Biokémikus", "text": "Elfogadhatjuk-e az új felfedezést kontrollcsoport nélkül?"},
                    {"speaker": "Kutatóintézeti vezető", "text": "Semmiképp; míg a spekuláció ingyenes, addig a tudományos igazság szigorú kontrollt _____."},
                    {"speaker": "Biokémikus", "text": "Akkor megismételjük a vaktesztet."}
                ], ["követel", "tilt", "tagad"], 0, ["c1-adv-contrastive-academic-adversatives"]),
                sw("production", [{"prompt": "Write a sentence contrasting theoretical speculation with empirical verification using 'Míg... addig...'.", "answer": "Míg a korábbi elmélet pusztán spekulatív premisszákra épült, addig az új kutatás szisztematikusan kontrollált kísérletekkel szolgáltatott megdönthetetlen empirikus bizonyítékot."}], ["c1-adv-contrastive-academic-adversatives"]),
                mc("grammar", "check", "Melyik kötőszószerkezet fejez ki tudományos állítások közötti szigorú ellentétezést?", [
                    "Míg a spekuláció... addig a kísérlet / Ezzel szemben",
                    "Ezért tehát örömmel",
                    "Nemcsak szép, hanem hasznos is"
                ], 0, ["c1-adv-contrastive-academic-adversatives"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-24-04",
            "title": "Teleological Scientific Inquiry & Research Objectives",
            "grammar_title": "Teleological Postpositional Structures Formulating Epistemic Scientific Research Objectives",
            "grammar_skill": "c1-modal-teleological-scientific-inquiry",
            "goals": [
                "I can analyze scientific inquiry objectives, experimental design, and teleological grant proposals (*kutatási célkitűzés, oksági mechanizmusok feltárása, alapkutatás vs. alkalmazott kutatás*).",
                "I can employ teleological postpositional structures articulating scientific goals (*az oksági viszonyok feltárása céljából, a törvényszerűségek tisztázása végett, az igazság kiderítése érdekében*).",
                "I can formulate elevated academic research proposals defending the intrinsic value of basic research."
            ],
            "vocab": [
                {"lemma": "alapkutatás", "translation": "basic / fundamental research", "pos": "noun"},
                {"lemma": "alkalmazott kutatás", "translation": "applied research", "pos": "expression"},
                {"lemma": "kutatási célkitűzés", "translation": "research objective / aim", "pos": "expression"},
                {"lemma": "oksági mechanizmus", "translation": "causal mechanism", "pos": "expression"},
                {"lemma": "tudományos disszemináció", "translation": "scientific dissemination", "pos": "expression"},
                {"lemma": "interdiszciplináris megközelítés", "translation": "interdisciplinary approach", "pos": "expression"},
                {"lemma": "pályázati támogatás", "translation": "grant funding", "pos": "expression"},
                {"lemma": "szellemi kíváncsiság", "translation": "intellectual curiosity", "pos": "expression"}
            ],
            "gr_text1": "Teleological postpositional phrases formulate elevated epistemological research mandates: `céljából` (for the purpose of), `végett` (with a view to / in order to), `érdekében` (in the interest of), `feltárására törekedve` (striving to uncover).",
            "gr_text2": "Example: `A molekuláris szintű oksági mechanizmusok feltárása céljából a laboratórium új spektroszkópiai eljárást dolgozott ki a rákos sejtek viselkedésének megértése végett`.",
            "gr_table": [
                ["A genetikai mutációk azonosítása céljából átfogó szekvenálást végeztek.", "For the purpose of identifying genetic mutations they performed comprehensive sequencing."],
                ["A sejtburjánzás mechanizmusának megértése végett új modellt állítottak fel.", "With a view to understanding the mechanism of cell proliferation they established a new model."],
                ["A tudományos igazság felderítése érdekében elengedhetetlen a független kutatás szabadsága.", "In the interest of discovering scientific truth the freedom of independent research is indispensable."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényegi különbség az 'alapkutatás' és az 'alkalmazott kutatás' között?", [
                    "Az alapkutatást a tiszta szellemi kíváncsiság és a természet mély törvényeinek megismerése vezérli közvetlen haszon nélkül, míg az alkalmazott kutatás konkrét gyakorlati célokat szolgál.",
                    "Az alapkutatást csak diákok végezhetik, az alkalmazottat csak professzorok.",
                    "Az alapkutatás kizárólag könyvtárakban zajlik számítógépek nélkül."
                ], 0, ["c1-24-vocab"]),
                fb("grammar", "controlled", "A betegség biológiai okainak feltárása _____ nemzetközi kutatócsoport alakult. (for the purpose of / céljából)", "céljából", "For the purpose of uncovering the biological causes of the disease an international research group was formed.", ["c1-modal-teleological-scientific-inquiry"]),
                match("vocabulary", "controlled", [["alapkutatás", "a világ mélyebb törvényeit kutató, közvetlen profitot nem célzó tudomány"], ["alkalmazott kutatás", "konkrét ipari vagy orvosi terméket célzó fejlesztés"], ["oksági mechanizmus", "egy jelenséget előidéző biológiai vagy fizikai folyamat"], ["interdiszciplináris", "több tudományterület módszereit ötvöző megközelítés"]], ["c1-24-vocab"]),
                fb("grammar", "practice", "A törvényszerűségek egzakt tisztázása _____ új mérési módszert vezettek be. (with a view to / végett)", "végett", "With a view to the exact clarification of regularities they introduced a new measurement method.", ["c1-modal-teleological-scientific-inquiry"]),
                sb("grammar", "practice", ["Az", "igazság", "kiderítése", "érdekében", "végeztek", "új", "kísérleteket."], ["Az", "igazság", "kiderítése", "érdekében", "végeztek", "új", "kísérleteket."], "In the interest of finding out the truth they conducted new experiments.", ["c1-modal-teleological-scientific-inquiry"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Miért kérünk állami támogatást erre az elméleti projektre?"},
                    {"speaker": "Intézetigazgató", "text": "A kvantumfizikai alapok megértése _____ kell forrást biztosítanunk a laboratóriumnak."},
                ], ["végett", "kárára", "ellenére"], 0, ["c1-modal-teleological-scientific-inquiry"]),
                sw("production", [{"prompt": "Write a sentence formulating a scientific research objective using 'céljából' or 'végett'.", "answer": "A sejtek molekuláris öregedési mechanizmusának megértése céljából a kutatók interdiszciplináris genetikai vizsgálatokat indítottak a hatékonyabb terápiák kidolgozása végett."}], ["c1-modal-teleological-scientific-inquiry"]),
                mc("grammar", "check", "Melyik névutó fejez ki tudományos célt és intenciót formális stílusban?", [
                    "céljából / végett / érdekében",
                    "nélkül / helyett",
                    "mögött / előtt"
                ], 0, ["c1-modal-teleological-scientific-inquiry"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-24-05",
            "title": "Albert Szent-Györgyi & Scalar Scientific Significance",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating Scientific Breakthroughs and Paradigm Shifts",
            "grammar_skill": "c1-adv-scalar-scientific-significance",
            "goals": [
                "I can analyze Albert Szent-Györgyi's philosophical and scientific legacy ('Az emberi természet és a tudományos kutatás', Nobel-díj, C-vitamin felfedezése).",
                "I can deploy scalar evaluative adverbials calibrating scientific breakthroughs (*korszakalkotó módon, forradalmian, elhanyagolható mértékben, alapjaiban átírva*).",
                "I can synthesize the ethical duty of the scientist: truth-seeking, anti-authoritarianism, and peace advocacy."
            ],
            "vocab": [
                {"lemma": "korszakalkotó felfedezés", "translation": "epoch-making discovery", "pos": "expression"},
                {"lemma": "tudományos integritás", "translation": "scientific integrity", "pos": "expression"},
                {"lemma": "Nobel-díj", "translation": "Nobel Prize", "pos": "noun"},
                {"lemma": "szegedi iskola", "translation": "Szeged school of biochemistry", "pos": "expression"},
                {"lemma": "C-vitamin szintézis", "translation": "vitamin C synthesis", "pos": "expression"},
                {"lemma": "tudósi felelősség", "translation": "scientist's responsibility", "pos": "expression"},
                {"lemma": "dogmatizmus elleni harc", "translation": "fight against dogmatism", "pos": "expression"},
                {"lemma": "egyetemes emberi haladás", "translation": "universal human progress", "pos": "expression"}
            ],
            "gr_text1": "Scalar evaluative adverbials calibrate the magnitude, historical weight, and transformative power of discoveries: `korszakalkotó módon` (in an epoch-making manner), `forradalmian újítva meg` (revolutionarily renewing), `alapjaiban átírva` (rewriting at its foundations), `vitathatatlanul` (inarguably).",
            "gr_text2": "Example: `Szent-Györgyi Albert a szegedi paprikából kivont aszkorbinsavval korszakalkotó módon bizonyította a C-vitamin szerkezetét, forradalmian megváltoztatva az orvosi biokémia jövőjét`.",
            "gr_table": [
                ["A felfedezés korszakalkotó módon alakította át az immunológia alapelveit.", "The discovery in an epoch-making manner transformed the principles of immunology."],
                ["Forradalmian új módszert dolgozott ki a sejtbiológiai folyamatok mérésére.", "He developed a revolutionarily new method for measuring cell biological processes."],
                ["A kutatási eredmények alapjaiban írták felül a korábbi tankönyvi téziseket.", "The research results at their foundations overwrote previous textbook theses."]
            ],
            "classic_story": {
                "slug": "c1-24-szentgyorgyi",
                "author": "Szent-Györgyi Albert",
                "work": "Az emberi természet és a tudományos kutatás (1937)",
                "title": "Szent-Györgyi Albert: A felfedezés öröme és a tudós felelőssége",
                "summary": "Albert Szent-Györgyi's luminous philosophical reflection on the essence of scientific discovery, the Szeged biochemistry school, isolating vitamin C from paprika, and the moral duty of academia to resist political tyranny.",
                "characters": ["Szent-Györgyi Albert"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Szent-Györgyi Albert 1937-ben átvette a fiziológiai és orvostudományi Nobel-díjat – az egyetlen Nobel-díjat, amelyet magyar kutató teljes egészében hazai egyetemen, a szegedi laboratóriumban végzett munkájáért kapott –, a világ nemcsak egy zseniális biokémikust, hanem egy mélységesen szabad szellemű humanistát ünnepelt. A szegedi paprika aszkorbinsav-tartalmának felismerése korszakalkotó felfedezés volt: Szent-Györgyi a biológiai égés folyamatainak feltárásával alapjaiban formálta át az emberi élet megértését."},
                    {"type": "narration", "text": "Ám Szent-Györgyi számára a tudomány sosem jelentett száraz, élettelen képletekbe zárkózó elefántcsonttornyot. 'Felfedezni valamit annyit tesz, mint látni, amit mindenki lát, és gondolni, amit senki sem gondolt' – vallotta híres aforizmájában. A tudományos kutatás legmélyebb hajtóereje a gyermeki kíváncsiság, a dogmák elutasítása és az elme feltétlen szabadsága volt. Ahol a politika vagy az ideológia megszabja, hogy mit szabad kutatni és mit nem, ott a tudomány azonnal halottá válik."},
                    {"type": "narration", "text": "Amikor a második világháború sötétsége és az elnyomó diktatúra rátelepedett Európára, Szent-Györgyi nem maradt csendben: ellenállóként, embermentőként és békekövetként kockáztatta az életét. Vallotta, hogy a tudós felelőssége nem ér véget a laboratórium ajtajában: ha a tudás hatalmát a rombolás és az emberi méltóság eltiprásának szolgálatába állítják, a tudós köteles szembeszállni a zsarnoksággal."},
                    {"type": "narration", "text": "Szent-Györgyi Albert öröksége a mai magyar tudomány legfénylőbb csillaga. Megtanította nekünk, hogy a tudományos nagyság nem pénz vagy hivatalos kinevezések függvénye, hanem a belső integritás, az intellektuális bátorság és a szabad egyetemi szellem kérdése. Amíg vannak kutatók, akik nem a hatalom kegyét, hanem az igazság tiszta fényét keresik, addig Szent-Györgyi szelleme elevenen él a magyar szellemben."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik Szent-Györgyi Albert Nobel-díját egyedülállónak a magyar tudománytörténetben?", [
                    "Mert ő az egyetlen magyar Nobel-díjas, aki a díjazott kutatásait teljes egészében Magyarországon, a Szegedi Tudományegyetemen végezte el.",
                    "Mert ő volt a világ legfiatalabb díjazottja.",
                    "Mert ő fedezte fel az első mesterséges műanyagot."
                ], 0, ["c1-24-vocab"]),
                fb("grammar", "controlled", "Szent-Györgyi felfedezése _____ módon alakította át az orvostudomány fejlődését. (in an epoch-making / korszakalkotó)", "korszakalkotó", "Szent-Györgyi's discovery in an epoch-making manner transformed the development of medicine.", ["c1-adv-scalar-scientific-significance"]),
                match("vocabulary", "controlled", [["korszakalkotó felfedezés", "egy tudományterületet alapjaiban megújító áttörés"], ["tudományos integritás", "az igazság feltétlen tisztelete a politikai és pénzügyi érdekekkel szemben"], ["szegedi iskola", "a Szent-Györgyi köré szerveződő nemzetközi hírű biokémiai műhely"], ["tudósi felelősség", "a kutató erkölcsi kötelessége a társadalom védelmében"]], ["c1-24-vocab"]),
                mc("reading", "practice", "Mit jelent Szent-Györgyi híres aforizmája a felfedezésről?", [
                    "Azt, hogy a tudós ugyanazokat a tényeket látja, mint bárki más, de képes új, eredeti összefüggésekben gondolkodni róluk dogmák nélkül.",
                    "Azt, hogy a kutatóknak mindent le kell rajzolniuk színes ceruzával.",
                    "Azt, hogy a felfedezésekhez csupán drága szemüvegre van szükség."
                ], 0, None),
                sb("grammar", "practice", ["A", "felfedezés", "alapjaiban", "írta", "át", "a", "tudomány", "történetét."], ["A", "felfedezés", "alapjaiban", "írta", "át", "a", "tudomány", "történetét."], "The discovery at its foundations rewrote the history of science.", ["c1-adv-scalar-scientific-significance"]),
                sw("production", [{"prompt": "Write a reflection on Albert Szent-Györgyi's legacy using a scalar significance adverbial.", "answer": "Szent-Györgyi Albert korszakalkotó módon bizonyította, hogy a valódi tudományos nagyság a bátor intellektuális szabadságban, a dogmák elvetésében és a tudósi integritás megalkuvás nélküli vállalásában gyökerezik."}], ["c1-adv-scalar-scientific-significance"]),
                mc("grammar", "check", "Melyik kifejezés fejez ki kimagasló, történelmi léptékű tudományos jelentőséget?", [
                    "korszakalkotó módon / forradalmian megújítva",
                    "nagyon csendesen",
                    "tavaly tavasszal"
                ], 0, ["c1-adv-scalar-scientific-significance"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(24, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        24,
        "core",
        "c1-24-consolidation",
        core_title,
        [
            "I can master C1 academic vocabulary of epistemology, falsifiability, and scientific integrity.",
            "I can deploy methodological adverbials, epistemic participial chains, and contrastive academic adversatives.",
            "I can evaluate teleological research objectives, scalar significance markers, and Albert Szent-Györgyi's legacy."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat fejez ki magas szintű tudománymetodológiai értékelést?", [
                "A kutatócsoport módszertanilag megalapozottan, szisztematikus kísérletekkel cáfolta a korábbi tézist.",
                "A professzor leült a könyvtárban és kinyitotta az új könyvet.",
                "Mivel szép volt az idő, a laboránsok kimentek ebédelni a parkba."
            ], 0, ["c1-adv-epistemic-methodological-evaluation"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki induktív tudományos következtetési láncot?", [
                "az anomáliákat feltárva, merész hipotézist felállítva és empirikusan alátámasztva",
                "miután megitták a reggeli kávét az egyetemen",
                "hogyha holnap kinyit a laboratórium ajtaja"
            ], 0, ["c1-participle-epistemological-chains"]),
            match("vocabulary", "recognize", [["episztemológia", "a megismerés és tudományos tudás elmélete"], ["falszifikálhatóság", "az elméletek cáfolhatóságának Popper-féle követelménye"], ["paradigmaváltás", "uralkodó tudományos világképek forradalmi átalakulása"], ["alapkutatás", "a valóság mély törvényeit feltáró, közvetlen haszon nélküli tudomány"], ["tudományos integritás", "az igazság megalkuvás nélküli etikai tisztelete"]], ["c1-24-vocab"]),
            fb("vocabulary", "recall", "A kísérlet megismételhetőségének tudományos követelménye a _____. (reproducibility / ismételhetőség)", "ismételhetőség", "The scientific requirement of experiment reproducibility is reproducibility.", ["c1-24-vocab"]),
            fb("vocabulary", "recall", "A tudományos világkép alapvető forradalmi fordulatát _____ nevezzük. (paradigm shift / paradigmaváltásnak)", "paradigmaváltásnak", "The fundamental revolutionary turning point of the scientific worldview is called a paradigm shift.", ["c1-24-vocab"]),
            fb("grammar", "recall", "A hipotézist szisztematikusan _____ igazolták a kutatók az új gyógyszer hatását. (substantiating / alátámasztva)", "alátámasztva", "Systematically substantiating the hypothesis researchers verified the effect of the new medicine.", ["c1-participle-epistemological-chains"]),
            fb("grammar", "context", "Míg a korábbi nézet spekulatív volt, _____ az új mérések szilárd empirikus bizonyítékot adtak. (meanwhile / addig)", "addig", "While the previous view was speculative, meanwhile the new measurements gave solid empirical evidence.", ["c1-adv-contrastive-academic-adversatives"]),
            fb("grammar", "context", "Szent-Györgyi Albert _____ módon írta át a biokémia történetét. (in an epoch-making / korszakalkotó)", "korszakalkotó", "Albert Szent-Györgyi in an epoch-making manner rewrote the history of biochemistry.", ["c1-adv-scalar-scientific-significance"]),
            mc("grammar", "context", "Mi a szerepe az ellenfaktikus és megengedő szerkezeteknek a tudományos érvelésben?", [
                "Lehetővé teszik a bizonyított tények és a még igazolatlan elméleti sejtések szigorú, kritikai szétválasztását.",
                "Kifejezik a kutatók bizonytalanságát a saját nevükkel kapcsolatban.",
                "Elnézést kérnek a laboratóriumi vegyszerek magas ára miatt."
            ], 0, ["c1-adv-contrastive-academic-adversatives"]),
            sb("grammar", "produce", ["A", "szabad", "gondolkodás", "minden", "tudományos", "haladás", "egyetlen", "forrása."], ["A", "szabad", "gondolkodás", "minden", "tudományos", "haladás", "egyetlen", "forrása."], "Free thinking is the sole source of all scientific progress.", ["c1-adv-scalar-scientific-significance"]),
            sw("production", [{"prompt": "Write a sentence formulating an evaluation of a scientific discovery using an epistemic methodological adverbial.", "answer": "A kutatók módszertanilag szigorúan ellenőrzött kísérletekkel, empirikusan alátámasztva cáfolták meg a korábbi dogmákat, korszakalkotó áttörést érve el a molekuláris biológiában."}], ["c1-adv-epistemic-methodological-evaluation"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Albert Szent-Györgyi and the moral duty of scientists.", "answer": "Szent-Györgyi Albert élete arra tanít, hogy a tudós igazi nagysága nemcsak a laboratóriumi zsenialitásban, hanem az igazság melletti megalkuvás nélküli kiállásban és az emberi szabadság védelmében nyilvánul meg."}], ["c1-adv-scalar-scientific-significance"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-felsooktatas)
    # ----------------------------------------------------
    slug = "felsooktatas"
    disc_intro = [
        "Hungarian higher education and academic life have been shaken to their core: the privatization of historic public universities into politically controlled private trust foundations ('KEKVA'), the resulting exclusion of Hungarian researchers and students from European Union Erasmus+ and Horizon Europe funding, the student occupation of SZFE, and the bitter irony of Hungarian Nobel laureates achieving global glory in emigration.",
        "In this unit, you will master the elevated discourse of institutional threat framing, statutory academic freedom, international mobility correlatives, and scientific sovereignty in contemporary Hungary."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Foundation Model Transition & Institutional Threat Framing",
            "grammar_title": "Discourse Framing Markers Diagnosing Institutional Crises in Higher Education",
            "grammar_skill": "c1-discourse-institutional-threat-framing",
            "goals": [
                "I can analyze the privatization of Hungarian universities into trust foundations (KEKVA) and board-of-trustees control (*egyetemi modellváltás, közérdekű vagyonkezelő alapítvány, kuratóriumi hatalom, autonómiavesztés*).",
                "I can deploy discourse framing markers diagnosing institutional crises in higher education (*egzisztenciális csapást mér az autonómiára, aláássa az intézményi függetlenséget, felszámolja a szenátusi döntési jogot*).",
                "I can debate political capture vs. financial flexibility in contemporary university governance."
            ],
            "vocab": [
                {"lemma": "modellváltás", "translation": "model change / university restructuring", "pos": "noun"},
                {"lemma": "közérdekű vagyonkezelő alapítvány", "translation": "public interest trust foundation (KEKVA)", "pos": "expression"},
                {"lemma": "kuratóriumi kontroll", "translation": "board of trustees control", "pos": "expression"},
                {"lemma": "egyetemi autonómia", "translation": "university autonomy", "pos": "expression"},
                {"lemma": "szenátusi jogkörök megnyirbálása", "translation": "curtailment of senate powers", "pos": "expression"},
                {"lemma": "politikai kinevezett", "translation": "political appointee", "pos": "expression"},
                {"lemma": "intézményi kiszolgáltatottság", "translation": "institutional vulnerability", "pos": "expression"},
                {"lemma": "felsőoktatási szuverenitás", "translation": "higher education sovereignty", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers articulate constitutional and institutional crises in academia: `egzisztenciális csapást mér az autonómiára` (deals an existential blow to autonomy), `aláássa az intézményi függetlenséget` (undermines institutional independence), `felszámolja a demokratikus önrendelkezést` (eradicates democratic self-determination), `politikai zsákmánnyá silányítja az egyetemet` (degrades the university into political spoils).",
            "gr_text2": "Example: `A közérdekű alapítványi modellváltás egzisztenciális csapást mért a magyar felsőoktatás autonómiájára, mivel a pártpolitikai kuratóriumok felszámolták az egyetemi szenátusok döntési jogkörét`.",
            "gr_table": [
                ["A kormányzati átalakítás súlyos csapást mér a tanszabadságra.", "Government restructuring deals a severe blow to academic freedom."],
                ["A politikusokkal feltöltött kuratóriumok aláássák az egyetemi autonómia alapjait.", "Trustee boards stacked with politicians undermine the foundations of university autonomy."],
                ["A modellváltás kiszolgáltatottá tette a professzori kart a politikai hatalomnak.", "The model change rendered the professoriate vulnerable to political power."]
            ],
            "world_story_seg": {
                "seg_slug": "modellvaltas",
                "title": "Az elveszett autonómia: a magyar egyetemek alapítványi fogsága",
                "summary": "Investigating how Hungary's major universities (Debrecen, Szeged, Pécs, Corvinus) were transferred to private foundations led by active government ministers, sparking domestic protest and European condemnation.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a magyar parlament 2020 és 2021 folyamán szinte az összes nagy múltú állami egyetemet – a Szegedi Tudományegyetemtől a Pécsi és Debreceni Egyetemen át a Corvinusig – közérdekű vagyonkezelő alapítványok (KEKVA) tulajdonába adta, a rendszerváltás utáni felsőoktatás legmélyebb és legvitatottabb átalakítása ment végbe. A kormányzati retorika a bürokratikus kötelékek levetéséről, a piacbarát működésről és a dinamikusabb bérezésről szólt. Ám a törvények valódi lényege a kuratóriumok összetételében mutatkozott meg: a testületek élére aktív miniszterek, államtitkárok és kormányközeli üzletemberek ültek be, élethosszig szóló megbízatással."},
                    {"type": "narration", "text": "Az akadémiai közösség számára ez a fordulat egzisztenciális csapást jelentett az évszázados egyetemi autonómiára. Az évszázados hagyományokkal rendelkező egyetemi szenátusokat – a professzorok és diákok választott testületeit – lényegében megfosztották döntési jogaiktól: a rektorok kinevezése, a költségvetés elfogadása és a stratégiai irányok kijelölése a pártpolitikai kontroll alatt álló kuratóriumok kizárólagos monopóliumává vált. A tanszabadság és az intellektuális függetlenség bástyái helyett az egyetemek a politikai hatalomgyakorlás és gazdasági befolyásszerzés eszközeivé silányultak."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért váltott ki heves tiltakozást a magyar egyetemek 'modellváltása' az Európai Unióban és itthon?", [
                    "Mert az egyetemeket felügyelő alapítványi kuratóriumokba élethosszig aktív kormánypolitikusokat ültettek be, felszámolva az intézményi és akadémiai függetlenséget.",
                    "Mert az egyetemi könyvtárakat kötelezték a latin nyelvű könyvek megsemmisítésére.",
                    "Mert a diákoknak megtiltották a kávéfogyasztást a vizsgaidőszakban."
                ], 0, ["c1-felsooktatas-vocab"]),
                fb("grammar", "controlled", "A politikai kuratóriumok felállítása egzisztenciális _____ mért a hazai egyetemi autonómiára. (blow / csapást)", "csapást", "The setting up of political boards of trustees dealt an existential blow to domestic university autonomy.", ["c1-discourse-institutional-threat-framing"]),
                match("vocabulary", "controlled", [["modellváltás", "az állami egyetemek magánalapítványi tulajdonba adása"], ["közérdekű vagyonkezelő alapítvány", "a KEKVA-törvény szerinti speciális fenntartó forma"], ["egyetemi autonómia", "az egyetemek önrendelkezése a kutatásban és oktatásban"], ["szenátusi jogkörök megnyirbálása", "a választott oktatói testület döntési hatalmának elvétele"]], ["c1-felsooktatas-vocab"]),
                fb("grammar", "practice", "Az összeférhetetlen politikai irányítás súlyosan _____ az intézmény nemzetközi hitelét. (undermines / aláássa)", "aláássa", "Incompatible political leadership severely undermines the institution's international credibility.", ["c1-discourse-institutional-threat-framing"]),
                sb("grammar", "practice", ["A", "modellváltás", "csapást", "mért", "az", "egyetemek", "függetlenségére."], ["A", "modellváltás", "csapást", "mért", "az", "egyetemek", "függetlenségére."], "The model change dealt a blow to universities' independence.", ["c1-discourse-institutional-threat-framing"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi oktató", "text": "Miért tiltakoznak a professzorok a KEKVA-modell ellen?"},
                    {"speaker": "Oktatáskutató", "text": "Mert a pártpolitikai kuratóriumok kinevezése alapjaiban ássa alá a tanszabadságot és az egyetem _____."},
                ], ["önrendelkezését", "szépségét", "méretét"], 0, ["c1-discourse-institutional-threat-framing"]),
                sw("production", [{"prompt": "Write a sentence diagnosing the crisis of university autonomy using an institutional threat framing marker.", "answer": "Az állami egyetemek politikai kuratóriumok alá rendelése egzisztenciális csapást mért a magyar felsőoktatás autonómiájára, súlyosan aláásva a tudományos kutatás függetlenségét és nemzetközi elismertségét."}], ["c1-discourse-institutional-threat-framing"]),
                mc("grammar", "check", "Melyik kifejezés tölt be diagnosztikus szerepet a felsőoktatási intézményi válság megfogalmazásakor?", [
                    "egzisztenciális csapást mér / aláássa az autonómiát",
                    "nagyon szép a diplomaosztó ünnepség",
                    "új padokat vettek a könyvtárba"
                ], 0, ["c1-discourse-institutional-threat-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Exclusion from Europe: Erasmus, Horizon & Deontic Rights",
            "grammar_title": "Deontic Modal Structures Formulating Statutory Guarantees for Academic Freedom",
            "grammar_skill": "c1-modal-deontic-academic-freedom",
            "goals": [
                "I can analyze the European Commission's funding freeze on Erasmus+ and Horizon Europe for Hungarian foundation universities (*Erasmus-kizárás, Horizont Európa, forrásbefagyasztás, jogállamisági kondicionalitás*).",
                "I can formulate statutory deontic modal structures guaranteeing academic freedom (*kötelessége garantálni a tanszabadságot, elidegeníthetetlen jogként rögzíti, összeférhetetlenségi tilalmat kell előírnia*).",
                "I can debate the devastating consequences of academic isolation for Hungarian students and young researchers."
            ],
            "vocab": [
                {"lemma": "Erasmus-program", "translation": "Erasmus+ student exchange program", "pos": "noun"},
                {"lemma": "Horizont Európa", "translation": "Horizon Europe research program", "pos": "expression"},
                {"lemma": "forrásbefagyasztás", "translation": "funding freeze", "pos": "noun"},
                {"lemma": "összeférhetetlenségi szabály", "translation": "conflict of interest rule", "pos": "expression"},
                {"lemma": "tanszabadság", "translation": "academic freedom / freedom of teaching", "pos": "noun"},
                {"lemma": "jogállamisági feltételrendszer", "translation": "rule of law conditionality", "pos": "expression"},
                {"lemma": "nemzetközi elszigetelődés", "translation": "international isolation", "pos": "expression"},
                {"lemma": "kutatói mobilitás", "translation": "researcher mobility", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal expressions define constitutional obligations and statutory safeguards for academic integrity: `kötelessége garantálni a tanszabadságot` (is obligated to guarantee academic freedom), `összeférhetetlenségi tilalmat kell előírnia` (must prescribe a conflict-of-interest ban), `elidegeníthetetlen jogként kell biztosítani` (must be ensured as an inalienable right).",
            "gr_text2": "Example: `A kormánynak törvényi kötelessége garantálni a tanszabadságot és szigorú összeférhetetlenségi szabályokat kell előírnia a kuratóriumokban, hogy a magyar diákok ne essenek el az Erasmus-ösztöndíjaktól`.",
            "gr_table": [
                ["Az államnak kötelessége garantálni a kutatók szabad nemzetközi mobilitását.", "The state has the duty to guarantee the free international mobility of researchers."],
                ["Szigorú összeférhetetlenségi szabályokat kell előírni a politikusok egyetemi jelenlétére.", "Strict conflict-of-interest rules must be prescribed for politicians' university presence."],
                ["A tanszabadság védelme alkotmányos kötelezettségként nehezedik a jogalkotóra.", "The protection of academic freedom weighs on the legislator as a constitutional obligation."]
            ],
            "world_story_seg": {
                "seg_slug": "erasmus",
                "title": "Zárt kapuk Európa előtt: az Erasmus- és Horizont-kizárás tragédiája",
                "summary": "Exploring the impact of the European Union's December 2022 decision to block foundation universities from Erasmus+ student exchanges and Horizon Europe research consortia due to rule-of-law violations.",
                "paragraphs": [
                    {"type": "narration", "text": "2022 decemberében a magyar felsőoktatás fekete napra ébredt: az Európai Unió Tanácsa a jogállamisági feltételrendszer keretében úgy döntött, hogy az alapítványi fenntartású magyar egyetemek nem részesülhetnek az Erasmus+ oktatási csereprogram és a Horizont Európa kutatás-fejlesztési keretprogram uniós forrásaiból. Az indoklás kíméletlen pontossággal fogalmazott: a politikusokkal feltöltött kuratóriumok és a közpénzek átláthatatlan kezelése súlyos összeférhetetlenséget teremt, amely sérti az unió pénzügyi érdekeit és az akadémiai szabadságot."},
                    {"type": "narration", "text": "A döntés következményei katasztrofálisak. Magyar egyetemisták ezrei veszítették el a lehetőséget, hogy európai egyetemeken tanuljanak féléveket, a hazai kutatócsoportokat pedig kirekesztik a legjelentősebb nemzetközi tudományos konzorciumokból. A jogalkotónak elemi kötelessége felszámolni ezt az elszigeteltséget: nemzeti érdek, hogy törvényi garanciákkal állítsák helyre az összeférhetetlenségi tilalmakat, kivezessék a pártpolitikusokat az egyetemek éléről, és visszaadják a magyar fiatalságnak a szabad, korlátlan európai jövő jogát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért zárta ki az Európai Unió a modellváltott magyar egyetemeket az Erasmus+ és Horizont programokból?", [
                    "A kuratóriumokban lévő politikusok összeférhetetlensége és az egyetemi autonómia csorbulása miatt, ami sérti az uniós jogállamisági normákat.",
                    "Mert a magyar diákok nem akartak idegen nyelveket tanulni külföldön.",
                    "Mert a brüsszeli épületben elromlott a számítógépes hálózat."
                ], 0, ["c1-felsooktatas-vocab"]),
                fb("grammar", "controlled", "A kormánynak törvényi kötelessége _____ a tanszabadságot és a kutatók függetlenségét. (to guarantee / garantálni)", "garantálni", "The government has a statutory duty to guarantee academic freedom and the independence of researchers.", ["c1-modal-deontic-academic-freedom"]),
                match("vocabulary", "controlled", [["Erasmus-program", "európai egyetemi hallgatói és oktatói csereprogram"], ["Horizont Európa", "az Európai Unió legjelentősebb kutatás-innovációs keretprogramja"], ["forrásbefagyasztás", "a támogatási pénzek kifizetésének jogi felfüggesztése"], ["összeférhetetlenségi szabály", "a politikai és egyetemi vezetői posztok összefonódásának tilalma"]], ["c1-felsooktatas-vocab"]),
                fb("grammar", "practice", "A jogalkotónak szigorú összeférhetetlenségi tilalmat kell _____ a kuratóriumok tagjaira. (prescribe / előírnia)", "előírnia", "The legislator must prescribe a strict conflict-of-interest ban on board members.", ["c1-modal-deontic-academic-freedom"]),
                sb("grammar", "practice", ["Kötelességünk", "visszaszerezni", "a", "diákok", "európai", "Erasmus-jogait."], ["Kötelességünk", "visszaszerezni", "a", "diákok", "európai", "Erasmus-jogait."], "It is our duty to regain students' European Erasmus rights.", ["c1-modal-deontic-academic-freedom"]),
                dc("dialogue", [
                    {"speaker": "Egyetemista", "text": "Hogyan utazhatunk újra Erasmusszal külföldre?"},
                    {"speaker": "Oktatásjogi szakértő", "text": "Az államnak kötelessége garantálni a politikai összeférhetetlenség felszámolását és az egyetemi autonómia _____."},
                ], ["visszaállítását", "megszüntetését", "tagadását"], 0, ["c1-modal-deontic-academic-freedom"]),
                sw("production", [{"prompt": "Write a sentence demanding statutory guarantees for academic freedom using 'kötelessége garantálni'.", "answer": "A mindenkori kormánynak elidegeníthetetlen alkotmányos kötelessége garantálni a tanszabadságot és felszámolni a politikai összeférhetetlenséget az egyetemek élén az Erasmus-tagság helyreállítása érdekében."}], ["c1-modal-deontic-academic-freedom"]),
                mc("grammar", "check", "Melyik kifejezés testesíti meg az akadémiai szabadságot védő kógens kötelezettséget?", [
                    "kötelessége garantálni a tanszabadságot / elő kell írnia",
                    "talán elmehet kirándulni",
                    "ha ideje engedi, tanul"
                ], 0, ["c1-modal-deontic-academic-freedom"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "The Siege of SZFE, Student Solidarity & Proportional Brain Drain",
            "grammar_title": "Proportional Correlative Conjunctions Mapping International Academic Isolation and Drain",
            "grammar_skill": "c1-adv-proportional-academic-mobility",
            "goals": [
                "I can analyze the 2020 student blockade of the University of Theatre and Film Arts (SZFE), civic disobedience, and institutional resistance (*SZFE-blokád, egyetemi ellenállás, piros-fehér szalag, FreeSZFE*).",
                "I can employ proportional correlative conjunctions mapping international academic isolation (*minél inkább elzárják a kutatókat a nemzetközi forrásoktól, annál gyorsabb az agyelszívás*).",
                "I can debate the role of student solidarity in defending civic liberties and cultural institutions."
            ],
            "vocab": [
                {"lemma": "SZFE-blokád", "translation": "SZFE university blockade (2020)", "pos": "expression"},
                {"lemma": "FreeSZFE mozgalom", "translation": "FreeSZFE movement", "pos": "expression"},
                {"lemma": "diákszolidaritás", "translation": "student solidarity", "pos": "noun"},
                {"lemma": "egyetemfoglalás", "translation": "university occupation / sit-in", "pos": "noun"},
                {"lemma": "piros-fehér szalag", "translation": "red-and-white ribbon (symbol of SZFE)", "pos": "expression"},
                {"lemma": "nemzetközi elszigetelődés", "translation": "international isolation", "pos": "expression"},
                {"lemma": "kutatói agyelszívás", "translation": "researcher brain drain", "pos": "expression"},
                {"lemma": "szellemi emigráció", "translation": "intellectual emigration / exile", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlatives (`minél... annál...` / `amennyivel... annyival...`) establish the direct relationship between authoritarian institutional interventions and the acceleration of intellectual flight: `Minél inkább korlátozza a hatalom a tanszabadságot, annál gyorsabban vándorolnak el a legtehetségesebb fiatal oktatók és kutatók az országból`.",
            "gr_text2": "This structure is essential in higher education policy to demonstrate the compounding, self-reinforcing damage of political purges on national scientific vitality.",
            "gr_table": [
                ["Minél mélyebb az egyetemek elszigeteltsége, annál pusztítóbb a kutatói agyelszívás.", "The deeper the isolation of universities, the more destructive the researcher brain drain."],
                ["Minél agresszívabban avatkozik be a politika, annál erősebb a diákszolidaritás ellenállása.", "The more aggressively politics intervenes, the stronger the resistance of student solidarity."],
                ["Amennyivel kevesebb európai forráshoz jut a tudomány, annyival nagyobb hátrányba kerül az ország.", "Inasmuch as less European funding reaches science, by so much greater disadvantage does the country suffer."]
            ],
            "world_story_seg": {
                "seg_slug": "szfe",
                "title": "A piros-fehér szalagok ősze: az SZFE blokádja és a szabadság őrzői",
                "summary": "Remembering the autumn of 2020: students occupying the Vas utca building of the University of Theatre and Film Arts for 71 days, creating a national movement for academic freedom.",
                "paragraphs": [
                    {"type": "narration", "text": "2020 kora őszén a budapesti Vas utca szűk járdáin különös és felemelő dolog történt. A Színház- és Filmművészeti Egyetem (SZFE) diákjai, tiltakozva az egyetemük erőszakos, felülről vezényelt kuratóriumi megszállása és az oktatói autonómia felszámolása ellen, elbarikádozták az épület bejáratait: egyetemfoglalást hirdettek. A híres piros-fehér kordonszalag pillanatok alatt a polgári bátorság, a szabad gondolat és az egyetemi önrendelkezés nemzeti jelképévé vált: tízezrek vonultak az utcára fáklyákkal a diákok mellett."},
                    {"type": "narration", "text": "Hetvenegy napon át tartott a blokád, amely bebizonyította, hogy a szolidaritás képes szembeszállni a hatalmi arroganciával. Noha az államhatalom végül adminisztratív eszközökkel feloszlatta a tiltakozást, a diákok és tanárok létrehozták a FreeSZFE Egyesületet, átmentve az intézmény szellemiségét. A szociológusok rámutattak a keserű törvényszerűségre: minél inkább megpróbálja a politikai hatalom engedelmességre kényszeríteni a kreatív alkotókat, annál elkerülhetetlenebbé válik a legkiválóbb tehetségek szellemi emigrációja és külföldre menekülése."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi tette történelmi jelentőségűvé az SZFE hallgatói blokádját 2020 őszén?", [
                    "A hallgatók 71 napos békés egyetemfoglalása, amellyel a politikai kinevezettek elleni tiltakozásul az akadémiai autonómia és a művészi szabadság szimbólumává váltak.",
                    "A diákok által szervezett ingyenes filmvetítések a Duna-parton.",
                    "Az egyetem épületének teljes átfestése piros-fehérre."
                ], 0, ["c1-felsooktatas-vocab"]),
                fb("grammar", "controlled", "Minél jobban korlátozzák az egyetemi szabadságot, _____ gyorsabb lesz a fiatal kutatók elvándorlása. (the more / annál)", "annál", "The more university freedom is restricted, the faster the out-migration of young researchers will be.", ["c1-adv-proportional-academic-mobility"]),
                match("vocabulary", "controlled", [["SZFE-blokád", "a diákok békés egyetemfoglalása az autonómia védelmében"], ["piros-fehér szalag", "az egyetemi ellenállás és szolidaritás jelképe"], ["FreeSZFE", "a független oktatást civil alapon folytató egyesület"], ["szellemi emigráció", "a hazai ellehetetlenülés elől külföldre távozó tehetségek"]], ["c1-felsooktatas-vocab"]),
                fb("grammar", "practice", "_____ inkább bezárkózik a hazai akadémia, annál mélyebb lesz a lemaradása a globális tudományban. (The more / Minél)", "Minél", "The more domestic academia closes in, the deeper its falling behind in global science will be.", ["c1-adv-proportional-academic-mobility"]),
                sb("grammar", "practice", ["Minél", "kevesebb", "a", "szabadság,", "annál", "nagyobb", "az", "agyelszívás."], ["Minél", "kevesebb", "a", "szabadság,", "annál", "nagyobb", "az", "agyelszívás."], "The less freedom, the greater the brain drain.", ["c1-adv-proportional-academic-mobility"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Miért tiltakoztak az SZFE diákjai a barikádokon?"},
                    {"speaker": "Történész", "text": "Minél bátrabban álltak ki az autonómiáért, _____ világosabbá vált, hogy a szabadság nem alku tárgya."},
                ], ["annál", "ugyan", "aligha"], 0, ["c1-adv-proportional-academic-mobility"]),
                sw("production", [{"prompt": "Write a proportional correlative sentence demonstrating the impact of academic repression on brain drain using 'Minél... annál...'.", "answer": "Minél inkább megfosztja a politikai hatalom az egyetemeket az autonómiájuktól, annál gyorsabb és pusztítóbb lesz a fiatal kutatók és orvosok tömeges külföldi agyelszívása."}], ["c1-adv-proportional-academic-mobility"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki funkcionális kölcsönhatást a szabadságkorlátozás és az agyelszívás között?", [
                    "Minél... annál...",
                    "Sem... sem...",
                    "Mivel... ezért..."
                ], 0, ["c1-adv-proportional-academic-mobility"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Nobel Laureates in Exile: Karikó, Krausz & Epistemic Projections",
            "grammar_title": "Epistemic Stance Markers Articulating Scientific Hypotheses on Institutional Decline",
            "grammar_skill": "c1-epistemic-academic-uncertainty",
            "goals": [
                "I can analyze the 2023 Hungarian Nobel laureates (Katalin Karikó, Ferenc Krausz) and their discoveries made outside Hungary (*Nobel-díj az emigrációban, mRNS technológia, attoszekundumos fizika, intézményi elutasítás*).",
                "I can employ calibrated epistemic stance markers assessing institutional decline and reform prospects (*nemzetközi elemzések alapján valószínűsíthetően, becslések szerint, prognosztizálható módon*).",
                "I can critique the paradox of domestic political self-congratulation vs. the structural underfunding that drove researchers abroad."
            ],
            "vocab": [
                {"lemma": "Nobel-díj az emigrációban", "translation": "Nobel Prize in emigration / exile", "pos": "expression"},
                {"lemma": "mRNS technológia", "translation": "mRNA technology (Karikó)", "pos": "expression"},
                {"lemma": "attoszekundumos fizika", "translation": "attosecond physics (Krausz)", "pos": "expression"},
                {"lemma": "intézményi elutasítás", "translation": "institutional rejection / dismissal", "pos": "expression"},
                {"lemma": "alulfinanszírozottság", "translation": "underfunding / financial starvation", "pos": "noun"},
                {"lemma": "kutatói kitartás", "translation": "researcher perseverance / tenacity", "pos": "expression"},
                {"lemma": "tudományos ökoszisztéma", "translation": "scientific ecosystem", "pos": "expression"},
                {"lemma": "visszatelepülési program", "translation": "repatriation program", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers formulate objective, data-backed hypotheses regarding institutional stagnation: `nemzetközi elemzések alapján valószínűsíthetően` (probabilistically based on international analyses), `statisztikák szerint` (according to statistics), `prognosztizálható módon` (predictably), `kutatói felmérések alapján feltételezhetően` (presumably based on researcher surveys).",
            "gr_text2": "Example: `Nemzetközi elemzések alapján valószínűsíthetően a hazai kutatóintézetek alulfinanszírozottsága és a politikai kontroll miatt a jövő magyar Nobel-díjasai is külföldi egyetemeken érik majd el sikereiket`.",
            "gr_table": [
                ["Nemzetközi felmérések alapján valószínűsíthetően csökken a hazai tudományos publikációk impaktja.", "Based on international surveys probabilistically the impact of domestic scientific publications declines."],
                ["Statisztikák szerint a PhD-fokozatot szerzett fiatalok jelentős része elhagyja az országot.", "According to statistics a significant portion of youth obtaining a PhD degree leaves the country."],
                ["Prognosztizálható módon valódi egyetemi autonómia nélkül nem teremthető meg a Nobel-díjas kutatási háttér.", "Predictably without genuine university autonomy a Nobel-caliber research background cannot be created."]
            ],
            "world_story_seg": {
                "seg_slug": "nobeldij",
                "title": "A Nobel-díj keserédes diadala: Karikó Katalin és a szülőföld paradoxona",
                "summary": "Investigating the bittersweet national triumph of October 2023: Katalin Karikó and Ferenc Krausz winning Nobel Prizes for discoveries made after fleeing or leaving the underfunded Hungarian academic system.",
                "paragraphs": [
                    {"type": "narration", "text": "2023 októberének elején Magyarország büszkeségtől és ujjongástól volt hangos: huszonnégy órán belül két magyar származású tudós is átvehette a Nobel-díjat. Karikó Katalin az orvosi-élettani, Krausz Ferenc pedig a fizikai Nobel-díjjal írta be nevét az emberiség halhatatlanjai közé. A hazai politikai elit azonnal a nemzeti géniusz, a magyar iskolarendszer és a tehetség végső diadalaként ünnepelte a sikert. Ám a csillogó szalagcímek mögött ott feszült a modern magyar tudomány legfájdalmasabb, keserédes igazsága."},
                    {"type": "narration", "text": "Sem Karikó, sem Krausz nem a hazai rendszernek köszönhetően, hanem annak ellenére lett világelső. Karikó Katalint a nyolcvanas években elbocsátották a Szegedi Biológiai Kutatóközpontból, források híján Amerikába kényszerült, ahol évtizedeken át megalázó félreállítások közepette, megdönthetetlen hittel fejlesztette ki az mRNS-alapú vakcinák technológiáját. Krausz Ferenc Münchenben és Bécsben építette fel lézerfizikai laboratóriumát. Elemzések alapján valószínűsíthetően a magyar tudomány mindaddig a tehetségek elpazarlója marad, amíg az alapkutatások szabadságát és méltó finanszírozását nem tekinti szent nemzeti kötelességnek."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik Karikó Katalin és Krausz Ferenc 2023-as Nobel-díját 'keserédes diadalnak' a magyar tudományban?", [
                    "Mert mindketten külföldi intézményekben érték el korszakalkotó eredményeiket, miután a hazai rendszer forráshiány és intézményi elutasítás miatt nem tudta megtartani őket.",
                    "Mert a Nobel-díj érmei túl nehezek voltak a hazaszállításhoz.",
                    "Mert a díjat kizárólag angol nyelven adták át Stockholmban."
                ], 0, ["c1-felsooktatas-vocab"]),
                fb("grammar", "controlled", "Nemzetközi elemzések alapján _____ a hazai kutatás forráshiánya gyorsítja az agyelszívást. (probabilistically / valószínűsíthetően)", "valószínűsíthetően", "Probabilistically based on international analyses the domestic research funding shortage accelerates brain drain.", ["c1-epistemic-academic-uncertainty"]),
                match("vocabulary", "controlled", [["Nobel-díj az emigrációban", "külföldi kutatóhelyeken elért magyar tudományos csúcssiker"], ["mRNS technológia", "Karikó Katalin által forradalmasított génterápiás módszer"], ["attoszekundumos fizika", "Krausz Ferenc által kidolgozott szupergyors fényimpulzus-mérés"], ["intézményi elutasítás", "a tehetséges kutatók támogatásának elutasítása vagy elbocsátása"]], ["c1-felsooktatas-vocab"]),
                fb("grammar", "practice", "A statisztikai adatok szerint _____ tovább nő a külföldön publikáló magyar tudósok aránya. (predictably / prognosztizálható módon)", "prognosztizálható módon", "According to statistical data predictably the proportion of Hungarian scientists publishing abroad further grows.", ["c1-epistemic-academic-uncertainty"]),
                sb("grammar", "practice", ["A", "tudományos", "szabadság", "a", "Nobel-díjas", "kutatások", "alapja."], ["A", "tudományos", "szabadság", "a", "Nobel-díjas", "kutatások", "alapja."], "Scientific freedom is the foundation of Nobel-caliber research.", ["c1-epistemic-academic-uncertainty"]),
                dc("dialogue", [
                    {"speaker": "Kutatóbiológus", "text": "Hazatérhetnek-e a külföldön sikeres magyar tudósok?"},
                    {"speaker": "Akadémikus", "text": "Nemzetközi tapasztalatok alapján valószínűsíthetően csak akkor, ha biztosítjuk a teljes kutatói _____."},
                ], ["autonómiát", "kiszolgáltatottságot", "elszigeteltséget"], 0, ["c1-epistemic-academic-uncertainty"]),
                sw("production", [{"prompt": "Write a sentence reflecting on Katalin Karikó's Nobel Prize using an epistemic stance marker.", "answer": "Nemzetközi elemzések alapján valószínűsíthetően Karikó Katalin példája arra figyelmeztet, hogy a tudományos tehetségek megtartásához a politikai szlogenek helyett valódi egyetemi autonómiára és méltó alapkutatási finanszírozásra van szükség."}], ["c1-epistemic-academic-uncertainty"]),
                mc("grammar", "check", "Melyik kifejezés tölt be tudományos valószínűséget és hipotézist kifejező szerepet?", [
                    "nemzetközi elemzések alapján valószínűsíthetően / prognosztizálható módon",
                    "nagyon örültek az ünnepségen",
                    "reggel hétkor megérkezett"
                ], 0, ["c1-epistemic-academic-uncertainty"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Academic Sovereignty, Brain Gain & Conclusive Synthesis",
            "grammar_title": "Evaluative Synthesis Particles Formulating Comprehensive Manifestos for University Autonomy",
            "grammar_skill": "c1-adv-conclusive-scientific-synthesis",
            "goals": [
                "I can formulate a comprehensive manifesto for university autonomy, scientific sovereignty, and brain gain (*tudományos szuverenitás, agyvisszaszívás, akadémiai szabadságjogok, kutatói hálózat*).",
                "I can employ elevated evaluative synthesis particles (*mindent összegezve, végső akadémiai konklúzióként, elvitathatatlanul*).",
                "I can synthesize the vital role of free universities as the guardians of critical thinking, democracy, and national progress."
            ],
            "vocab": [
                {"lemma": "tudományos szuverenitás", "translation": "scientific sovereignty", "pos": "expression"},
                {"lemma": "agyvisszaszívás", "translation": "brain gain / scientific repatriation", "pos": "expression"},
                {"lemma": "kritikai gondolkodás", "translation": "critical thinking", "pos": "expression"},
                {"lemma": "egyetemi önrendelkezés", "translation": "university self-determination", "pos": "expression"},
                {"lemma": "akadémiai szabadságjog", "translation": "academic liberty / right", "pos": "expression"},
                {"lemma": "nemzeti innovációs ökoszisztéma", "translation": "national innovation ecosystem", "pos": "expression"},
                {"lemma": "demokratikus nyilvánosság", "translation": "democratic public sphere", "pos": "expression"},
                {"lemma": "tudományos felemelkedés", "translation": "scientific advancement / elevation", "pos": "expression"}
            ],
            "gr_text1": "Academic synthesis particles formulate definitive manifestos and institutional conclusions: `mindent összegezve` (summarizing everything / all in all), `végső akadémiai konklúzióként` (as a final academic conclusion), `elvitathatatlanul` (inarguably), `összegzésképpen kijelenthető` (by way of summary it can be declared).",
            "gr_text2": "Example: `Mindent összegezve, a szabad egyetem nem az államhatalom ellenfele, hanem a nemzet fennmaradásának legfőbb záloga: végső akadémiai konklúzióként kimondható, hogy tanszabadság nélkül nincs valódi európai jövőnk`.",
            "gr_table": [
                ["Mindent összegezve, a tudományos szuverenitás alapköve a kutatók függetlensége.", "Summarizing everything, the cornerstone of scientific sovereignty is researchers' independence."],
                ["Végső akadémiai konklúzióként kijelenthető, hogy az egyetemeket vissza kell adni az oktatóknak és diákoknak.", "As a final academic conclusion it can be stated that universities must be returned to educators and students."],
                ["Elvitathatatlanul a szabad szellemű kutatás jelenti a magyar felemelkedés egyetlen útját.", "Inarguably free-spirited research represents the sole path of Hungarian elevation."]
            ],
            "world_story_seg": {
                "seg_slug": "tudomanyos-szuverenitas",
                "title": "A szabad szellem vára: az egyetemi autonómia és a nemzet jövője",
                "summary": "Drawing together the lessons of the foundation model change, Erasmus exclusion, SZFE resistance, and Karikó's Nobel triumph into an inspiring manifesto for the rebirth of Hungarian academic freedom.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a magyar felsőoktatás és tudomány jövőjére tekintünk, világosan kell látnunk: egy ország nagyságát és jövőjét sosem a hadseregek mérete vagy a gyárak kéményei, hanem az egyetemi katedrák szabadsága és a kutatóintézetek szellemi ereje méri. Magyarország évszázadokon át a szellem bajnokait adta a világnak, mert még a legsötétebb történelmi viharokban is akadtak professzorok és diákok, akik nem hódoltak be a politikai akaratnak, és az igazság tiszta keresését mindennél előbbre valónak tartották."},
                    {"type": "narration", "text": "Mindent összegezve, a huszonegyedik században a tudományos szuverenitás nem a nemzetközi világtól való bezárkózást jelenti, hanem az egyetemi autonómia bátor visszaállítását, a diákok európai mobilitásának garanciáit és a külföldre kényszerült magyar tehetségek hazacsábítását. Végső akadémiai konklúzióként kimondható: a szabad egyetem nem a hatalom birtoka, hanem a nemzet közös szentélye. Amíg a magyar egyetemek a kritikai gondolkodás, a humanizmus és a szabad kutatás bástyái maradnak, addig a haza jövője megingathatatlanul biztos alapokon áll."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'tudományos szuverenitás' fogalma a 21. századi tudománypolitikában?", [
                    "A nemzet azon képességét, hogy független, nemzetközileg integrált és politikailag nem befolyásolt intézményekben saját maga termelje újra a magas szintű tudást és innovációt.",
                    "A külföldi folyóiratok előfizetésének törvényi megtiltását.",
                    "Az egyetemi épületek katonai őrizet alá helyezését."
                ], 0, ["c1-felsooktatas-vocab"]),
                fb("grammar", "controlled", "Mindent _____, a szabad egyetemi szellem a nemzeti felemelkedés legfőbb záloga. (summarizing / összegezve)", "összegezve", "Summarizing everything, free university spirit is the foremost pledge of national elevation.", ["c1-adv-conclusive-scientific-synthesis"]),
                match("vocabulary", "controlled", [["tudományos szuverenitás", "az önálló, szabad kutatás és innováció nemzeti képessége"], ["agyvisszaszívás", "a külföldön élő magyar kutatók hazacsábításának programja"], ["kritikai gondolkodás", "az előítéletektől és hatalmi elvárásoktól mentes önálló elemzés"], ["egyetemi önrendelkezés", "az oktatók és hallgatók joga intézményük demokratikus vezetésére"]], ["c1-felsooktatas-vocab"]),
                fb("grammar", "practice", "Végső akadémiai _____ kijelenthető, hogy autonómia nélkül nincs nemzetközileg versenyképes tudomány. (conclusion / konklúzióként)", "konklúzióként", "As a final academic conclusion it can be stated that without autonomy there is no internationally competitive science.", ["c1-adv-conclusive-scientific-synthesis"]),
                sb("grammar", "practice", ["Mindent", "összegezve,", "a", "szabad", "egyetem", "a", "nemzet", "jövője."], ["Mindent", "összegezve,", "a", "szabad", "egyetem", "a", "nemzet", "jövője."], "Summarizing everything, the free university is the nation's future.", ["c1-adv-conclusive-scientific-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi rektor", "text": "Hogyan foglalható össze a magyar felsőoktatás jövője?"},
                    {"speaker": "Akadémikus professzor", "text": "Mindent összegezve, az egyetemi autonómia helyreállítása az európai jövőnk egyetlen járható _____."},
                ], ["útja", "veszélye", "kudarcra"], 0, ["c1-adv-conclusive-scientific-synthesis"]),
                sw("production", [{"prompt": "Write a concluding synthesis on university autonomy and scientific sovereignty using 'Mindent összegezve'.", "answer": "Mindent összegezve, a magyar felsőoktatás megújulásának és a tudományos szuverenitás megőrzésének egyetlen feltétele az egyetemi autonómia helyreállítása, a tanszabadság törvényi védelme és az európai kutatási integráció visszaállítása."}], ["c1-adv-conclusive-scientific-synthesis"]),
                mc("grammar", "check", "Melyik kifejezés tölt be ünnepélyes, akadémiai összegző funkciót a tézis zárlatában?", [
                    "Mindent összegezve / Végső akadémiai konklúzióként",
                    "A lépcsőn lefelé sietve",
                    "Kikapcsolva a lámpát a teremben"
                ], 0, ["c1-adv-conclusive-scientific-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(24, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        ROOT / "content" / "hu" / "stories" / "world" / "c1" / f"c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A szellem bástyái: autonómia, Erasmus-kizárás és a magyar tudomány szabadsága",
            "level": "C1",
            "type": "world",
            "order": 24,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of Hungary's higher education crisis and academic resilience: the foundation model change, exclusion from EU Erasmus+ and Horizon Europe funding, the student occupation of SZFE, the bittersweet emigration triumph of Nobel laureates Karikó and Krausz, and the manifesto for scientific sovereignty.",
            "grammar": [
                "c1-discourse-institutional-threat-framing",
                "c1-modal-deontic-academic-freedom",
                "c1-adv-proportional-academic-mobility",
                "c1-epistemic-academic-uncertainty",
                "c1-adv-conclusive-scientific-synthesis"
            ],
            "vocabularyTopics": [
                "The University in Turmoil: Model Change, Autonomy & The European Horizon",
                "The Foundation Model Transition & Institutional Threat Framing",
                "Exclusion from Europe: Erasmus, Horizon & Deontic Rights",
                "The Siege of SZFE, Student Solidarity & Proportional Brain Drain",
                "Nobel Laureates in Exile: Karikó, Krausz & Epistemic Projections",
                "Academic Sovereignty, Brain Gain & Conclusive Synthesis"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A huszonegyedik század harmadik évtizedében a magyar felsőoktatás és tudományos élet mély, történelmi jelentőségű válságon megy keresztül. A nagy állami egyetemek magánalapítványi fenntartásba adása és a pártpolitikai kuratóriumok felállítása egzisztenciális csapást mért a hagyományos akadémiai autonómiára, aláásva a szenátusok és oktatói karok évszázados önrendelkezését."},
                {"type": "narration", "text": "A politikai összeférhetetlenség legsúlyosabb árat követelő következménye az Európai Unió válaszlépése volt: az Erasmus+ csereprogramok és a Horizont Európa kutatási források befagyasztása magyar hallgatók és kutatók tízezreit zárta el a szabad nemzetközi mobilitástól. Ezzel párhuzamosan az SZFE hallgatói blokádja és a FreeSZFE mozgalom bizonyította: a diákszolidaritás és a szabad szellem nem törhető meg pusztán adminisztratív hatalmi döntésekkel."},
                {"type": "narration", "text": "A helyzet drámai paradoxonát Karikó Katalin és Krausz Ferenc 2023-as Nobel-díjai mutatták meg legtisztábban: mindkét magyar zseni külföldön, a hazai alulfinanszírozottság és intézményi akadályok elől elmenekülve érte el a világ tetejét. A felmérések riasztóak: nemzetközi elemzések alapján valószínűsíthetően a hazai tudomány mindaddig a tehetségek elszívója marad, amíg a politika nem ismeri el a szabad kutatás feltétlen szentségét."},
                {"type": "narration", "text": "Mindent összegezve, a szabad egyetem a nemzet fennmaradásának, szellemi függetlenségének és gazdasági felemelkedésének legfőbb garanciája. Végső akadémiai konklúzióként kimondható: az egyetemi autonómia helyreállítása, a tanszabadság kógens védelme és az európai szellemi közösségbe való visszatérés jelenti az egyetlen méltó utat a magyar szellem Szent-Györgyi Albert által kijelölt örökségéhez."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        24,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze university foundation privatization, board of trustees capture, and Erasmus funding freezes.",
            "I can evaluate student protest blockades (SZFE), Nobel laureates in emigration (Karikó, Krausz), and brain drain.",
            "I can debate academic freedom manifestos, university self-determination, and scientific sovereignty in Hungary."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki súlyos intézményi válságot és az autonómia felszámolását?", [
                "egzisztenciális csapást mér az autonómiára / aláássa az intézményi függetlenséget",
                "mivel befejeződött a tanév az egyetemen nyáron",
                "amikor új tankönyveket rendeltek a diákoknak"
            ], 0, ["c1-discourse-institutional-threat-framing"]),
            mc("grammar", "recognize", "Melyik kifejezés testesíti meg az akadémiai szabadság törvényi garanciáját?", [
                "kötelessége garantálni a tanszabadságot / összeférhetetlenségi tilalmat kell előírnia",
                "szabadon választhatnak a tollak színe közül a vizsgán",
                "ha kedvük tartja, sétálnak a folyosón"
            ], 0, ["c1-modal-deontic-academic-freedom"]),
            match("vocabulary", "recognize", [["modellváltás", "állami egyetemek magánalapítványi kiszervezése"], ["Erasmus-program", "európai egyetemi hallgatói mobilitási program"], ["SZFE-blokád", "diákok 71 napos békés egyetemfoglalása"], ["Nobel-díj az emigrációban", "külföldre kényszerült magyar tudósok sikere"], ["tudományos szuverenitás", "az önálló és szabad nemzeti kutatás képessége"]], ["c1-felsooktatas-vocab"]),
            fb("vocabulary", "recall", "Az állami egyetemek alapítványi fenntartásba adását a magyar felsőoktatásban _____ nevezik. (model change / modellváltásnak)", "modellváltásnak", "The transferring of state universities to foundation governance in Hungarian higher education is called model change.", ["c1-felsooktatas-vocab"]),
            fb("vocabulary", "recall", "A külföldön sikeres kutatók hazatérését célzó folyamat az _____. (brain gain / agyvisszaszívás)", "agyvisszaszívás", "The process aiming at the return of successful researchers from abroad is brain gain.", ["c1-felsooktatas-vocab"]),
            fb("grammar", "recall", "A kormánynak alkotmányos _____ garantálni az egyetemek autonómiáját. (duty / kötelessége)", "kötelessége", "The government has a constitutional duty to guarantee university autonomy.", ["c1-modal-deontic-academic-freedom"]),
            fb("grammar", "context", "Minél tovább tart az Erasmus-kizárás, _____ súlyosabb károkat szenved a magyar diákság. (the more / annál)", "annál", "The longer the Erasmus exclusion lasts, the more severe damage Hungarian students suffer.", ["c1-adv-proportional-academic-mobility"]),
            fb("grammar", "context", "Mindent _____, a tanszabadság a nemzet szellemi felemelkedésének záloga. (summarizing / összegezve)", "összegezve", "Summarizing everything, academic freedom is the pledge of the nation's intellectual elevation.", ["c1-adv-conclusive-scientific-synthesis"]),
            mc("grammar", "context", "Mi a funkciója a 'Minél... annál...' arányossági szerkezetnek a mobilitási elemzésekben?", [
                "Bemutatja a nemzetközi elszigetelődés és a tehetségek elvándorlása közötti közvetlen, felgyorsuló arányosságot.",
                "Kijelenti, hogy nincs szükség külföldi ösztöndíjakra.",
                "Elnézést kér az uniós tárgyalások lassúsága miatt."
            ], 0, ["c1-adv-proportional-academic-mobility"]),
            sb("grammar", "produce", ["A", "szabad", "egyetem", "a", "nemzet", "szellemi", "függetlenségének", "vára."], ["A", "szabad", "egyetem", "a", "nemzet", "szellemi", "függetlenségének", "vára."], "The free university is the castle of the nation's intellectual independence.", ["c1-adv-conclusive-scientific-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of university capture using an institutional threat framing marker.", "answer": "Az állami egyetemek politikai kuratóriumok alá rendelése és az európai uniós források elvesztése egzisztenciális csapást mért a magyar felsőoktatás autonómiájára és nemzetközi versenyképességére."}], ["c1-discourse-institutional-threat-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on scientific sovereignty and academic freedom in Hungary.", "answer": "Mindent összegezve, Magyarország csak akkor őrizheti meg tudományos nagyságát és szellemi szuverenitását, ha bátor politikai elszántsággal helyreállítja az egyetemi autonómiát és a tanszabadság feltétlen védelmét."}], ["c1-adv-conclusive-scientific-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 24 ===")


if __name__ == "__main__":
    generate_unit_24()
