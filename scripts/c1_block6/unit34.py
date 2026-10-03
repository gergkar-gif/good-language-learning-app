#!/usr/bin/env python3
"""
Hungarian C1 Block 6 - Unit 34 Generator:
  - Track 1 (Core): Unit 34 — "Philosophy of Science, Epistemic Rigor & Discovery" (c1-34)
  - Track 2 (Discourse): Unit 34 — "The Stripping of MTA Research Institutes & The CEU Expulsion" (c1-tudomanyosszabadsag)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block6.registry_helper import register_unit


def generate_unit_34():
    print("=== Generating C1 Unit 34 ===")
    
    new_skills = {
        "c1-34-vocab": {"kind": "vocabulary"},
        "c1-tudomanyosszabadsag-vocab": {"kind": "vocabulary"},
        "c1-adv-epistemic-tacit-knowledge": {"kind": "grammar"},
        "c1-participle-scientific-falsificationism": {"kind": "grammar"},
        "c1-modal-deontic-epistemic-rigor": {"kind": "grammar"},
        "c1-adv-comparative-paradigmatic-shift": {"kind": "grammar"},
        "c1-syntax-republic-of-science-deduction": {"kind": "grammar"},
        "c1-discourse-academic-asset-stripping-framing": {"kind": "grammar"},
        "c1-adv-academic-expulsion-critique": {"kind": "grammar"},
        "c1-modal-deontic-senate-autonomy-defense": {"kind": "grammar"},
        "c1-adv-proportional-academic-exclusion-isolation": {"kind": "grammar"},
        "c1-adv-conclusive-epistemic-freedom": {"kind": "grammar"},
    }
    new_titles = {
        "c1-34-vocab": "reading",
        "c1-tudomanyosszabadsag-vocab": "reading",
        "c1-adv-epistemic-tacit-knowledge": "evaluative adverbials formulating epistemic tacit knowledge and personal discovery",
        "c1-participle-scientific-falsificationism": "participial clauses analyzing scientific falsificationism and methodological fallibilism",
        "c1-modal-deontic-epistemic-rigor": "deontic modal structures asserting intellectual duty of scientific objectivity",
        "c1-adv-comparative-paradigmatic-shift": "scalar comparative adverbials tracing epistemological paradigm shifts and discovery",
        "c1-syntax-republic-of-science-deduction": "hypothetical and deductive syntax structuring the republic of science doctrine",
        "c1-discourse-academic-asset-stripping-framing": "discourse markers diagnosing authoritarian asset stripping of scientific academies",
        "c1-adv-academic-expulsion-critique": "critical evaluative adverbials exposing state-enforced academic exile and university purges",
        "c1-modal-deontic-senate-autonomy-defense": "deontic modal structures formulating university senates duty of self-governance",
        "c1-adv-proportional-academic-exclusion-isolation": "proportional correlative structures linking university politicization to european research isolation",
        "c1-adv-conclusive-epistemic-freedom": "evaluative conclusive particles declaring foundational necessity of academic freedom",
    }
    
    core_title = "Philosophy of Science, Epistemic Rigor & Discovery"
    core_stems = [f"c1-34-0{i}" for i in range(1, 6)] + ["c1-34-consolidation"]
    disc_title = "The Stripping of MTA Research Institutes & The CEU Expulsion"
    slug = "tudomanyosszabadsag"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(34, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-34)
    # ----------------------------------------------------
    core_intro = [
        "The philosophy of science explores the nature of truth, discovery, and epistemic justification, proving that genuine scientific breakthrough relies upon autonomous human judgment and uncoerced inquiry.",
        "In this unit, centered on Mihály Polányi's revolutionary epistemology in 'Személyes tudás' (Personal Knowledge, 1958) and his doctrine of 'A tudomány köztársasága' (The Republic of Science), you will master the elevated academic register of tacit knowledge, falsificationism, scientific ethics, paradigmatic shifts, and academic self-governance at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-34-01",
            "title": "Tacit Knowledge & Personal Epistemology",
            "grammar_title": "Evaluative Adverbials Formulating Epistemic Tacit Knowledge and Personal Discovery",
            "grammar_skill": "c1-adv-epistemic-tacit-knowledge",
            "goals": [
                "I can analyze tacit knowledge, personal participation in knowing, and epistemic intuition (*hallgatólagos tudás, személyes tudás, episztemikus intuíció, kimondhatatlan előtudás*).",
                "I can deploy elevated evaluative adverbials formulating epistemic intuition (*episztemikusan megalapozva, hallgatólagos tudásra támaszkodva, intuitív módon felismerve a mintázatokat*).",
                "I can critique radical positivism in epistemology of science."
            ],
            "vocab": [
                {"lemma": "hallgatólagos tudás", "translation": "tacit knowledge (Polányi concept)", "pos": "expression"},
                {"lemma": "személyes tudás", "translation": "personal knowledge", "pos": "expression"},
                {"lemma": "episztemológia", "translation": "epistemology / theory of knowledge", "pos": "noun"},
                {"lemma": "episztemikus intuíció", "translation": "epistemic intuition", "pos": "expression"},
                {"lemma": "pozitivizmus", "translation": "positivism / logical empiricism", "pos": "noun"},
                {"lemma": "tudományos felfedezés", "translation": "scientific discovery", "pos": "expression"},
                {"lemma": "megismerési folyamat", "translation": "cognitive / epistemic process", "pos": "expression"},
                {"lemma": "heurisztikus erő", "translation": "heuristic power", "pos": "expression"}
            ],
            "gr_text1": "Evaluative adverbials in epistemology articulate the subtle, non-formalizable dimensions of human knowing: `episztemikusan megalapozott módon` (in an epistemologically well-grounded manner), `a hallgatólagos tudás láthatatlan rétegeire támaszkodva` (relying on the invisible layers of tacit knowledge), `intuitív módon megragadva a valóság összefüggéseit` (intuitively grasping the interrelations of reality).",
            "gr_text2": "Example: `Polányi szerint a kutató hallgatólagos tudásra támaszkodva és episztemikusan megalapozott módon jut el a felfedezés pillanatához, hiszen többet tudunk, mint amennyit elmondani vagyunk képesek`.",
            "gr_table": [
                ["A kutató a hallgatólagos tudásra támaszkodva ismeri fel a mikroszkóp alatti eltérést.", "Relying on tacit knowledge the researcher recognizes the anomaly under the microscope."],
                ["A felismerés episztemikusan megalapozott módon vezet új hipotézisekhez.", "The realization leads to new hypotheses in an epistemologically grounded manner."],
                ["Intuitív módon megragadva a problémát a tudós túllép a száraz formulákon.", "Intuitively grasping the problem the scientist moves beyond dry formulas."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan fogalmazta meg Polányi Mihály a hallgatólagos tudás alapelvét?", [
                    "'Többet tudunk, mint amennyit el tudunk mondani': a tudás jelentős része kimondhatatlan, tapasztalati és személyes meggyőződésen alapul.",
                    "A tudomány minden állítása matematikai egyenletekkel maradéktalanul leírható.",
                    "A laboratóriumokban tilos hangosan beszélni a kísérletek alatt."
                ], 0, ["c1-34-vocab"]),
                fb("grammar", "controlled", "A tudós a hallgatólagos tudásra _____ ismerte fel az elméleti anomáliát. (relying / támaszkodva)", "támaszkodva", "Relying on tacit knowledge the scientist recognized the theoretical anomaly.", ["c1-adv-epistemic-tacit-knowledge"]),
                match("vocabulary", "controlled", [
                    ["hallgatólagos tudás", "a megfogalmazhatatlan, gyakorlati tapasztalatban rejlő előtudás"],
                    ["személyes tudás", "a megismerő alany aktív elköteleződésén alapuló igazság"],
                    ["episztemológia", "a tudás természetét és határait kutató filozófiai ág"],
                    ["heurisztikus erő", "az új összefüggések felfedezését segítő szellemi lendület"]
                ], ["c1-34-vocab"]),
                fb("grammar", "practice", "A hipotézis episztemikusan _____ módon vezet el a valóság mélyebb megértéséhez. (grounded / megalapozott)", "megalapozott", "The hypothesis leads to a deeper understanding of reality in an epistemologically grounded manner.", ["c1-adv-epistemic-tacit-knowledge"]),
                sb("grammar", "practice", ["A", "kutató", "hallgatólagos", "tudásra", "támaszkodva", "jutott", "el", "a", "felfedezéshez."], ["A", "kutató", "hallgatólagos", "tudásra", "támaszkodva", "jutott", "el", "a", "felfedezéshez."], "Relying on tacit knowledge the researcher arrived at the discovery.", ["c1-adv-epistemic-tacit-knowledge"]),
                dc("dialogue", [
                    {"speaker": "Fizikus", "text": "Lehetséges-e a tudományos felfedezést puszta algoritmusokkal helyettesíteni?"},
                    {"speaker": "Tudományfilozófus", "text": "Polányi szerint kizárt, hiszen a tudós személyes elköteleződése és hallgatólagos _____ nélkül nincs valódi intuíció."},
                    {"speaker": "Fizikus", "text": "A megismerés mindig emberi aktus marad."}
                ], ["tudása", "könyve", "gépe"], 0, ["c1-adv-epistemic-tacit-knowledge"]),
                sw("production", [{"prompt": "Write an epistemological sentence about tacit knowledge using an evaluative adverbial.", "answer": "A tudományos kutató a hallgatólagos tudás gazdag rétegeire támaszkodva és episztemikusan megalapozott módon képes megragadni azokat az összefüggéseket, amelyek formális algoritmusokkal kifejezhetetlenek."}], ["c1-adv-epistemic-tacit-knowledge"]),
                mc("grammar", "check", "Melyik határozói kifejezés elemzi a megismerés rejtett lélektanát a legszakszerűbben?", [
                    "hallgatólagos tudásra támaszkodva / episztemikusan megalapozott módon",
                    "nagyon sokat gondolkodva a laborban délután",
                    "amikor a tudós felír egy számot a táblára"
                ], 0, ["c1-adv-epistemic-tacit-knowledge"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-34-02",
            "title": "Falsificationism & Methodological Fallibilism",
            "grammar_title": "Participial Clauses Analyzing Scientific Falsificationism and Methodological Fallibilism",
            "grammar_skill": "c1-participle-scientific-falsificationism",
            "goals": [
                "I can analyze Karl Popper's falsificationism, fallibilism, and empirical refutation (*falszifikáció, cáfolhatóság, esendőség, módszertani fallibilizmus, hipotézis-ellenőrzés*).",
                "I can construct participial clauses analyzing empirical refutability (*az elméletet kísérleti cáfolatnak kitéve, a prekoncepciókat kritikai szűrőn átfuttatva, az esendőség tudatát ébren tartva*).",
                "I can evaluate the demarcation line between genuine science and dogmatic pseudoscience."
            ],
            "vocab": [
                {"lemma": "falszifikáció", "translation": "falsification / empirical refutation", "pos": "noun"},
                {"lemma": "cáfolhatóság", "translation": "falsifiability", "pos": "noun"},
                {"lemma": "fallibilizmus", "translation": "fallibilism (recognition of human fallibility)", "pos": "noun"},
                {"lemma": "demarkációs vonal", "translation": "demarcation line (science vs. pseudoscience)", "pos": "expression"},
                {"lemma": "empirikus korrobáció", "translation": "empirical corroboration", "pos": "expression"},
                {"lemma": "cáfoló kísérlet", "translation": "crucial / falsifying experiment", "pos": "expression"},
                {"lemma": "módszertani szigor", "translation": "methodological rigor", "pos": "expression"},
                {"lemma": "dogmatizmus", "translation": "dogmatism", "pos": "noun"}
            ],
            "gr_text1": "Participial clauses in philosophy of science formalize the rigorous critical testing of hypotheses: `az elméleteket könyörtelen empirikus cáfolatnak kitéve` (subjecting theories to ruthless empirical falsification), `a tudományos tévedhetetlenség illúzióját elutasítva` (rejecting the illusion of scientific infallibility), `a demarkációs kritériumot szigorúan alkalmazva` (strictly applying the demarcation criterion).",
            "gr_text2": "Example: `A tudomány a felállított elméleteket szisztematikus cáfolatnak kitéve és a fallibilizmus elvét tiszteletben tartva halad előre`.",
            "gr_table": [
                ["A kutatók az elméletet szigorú tesztelésnek kitéve keresik a cáfoló bizonyítékokat.", "Subjecting the theory to rigorous testing researchers look for refuting evidence."],
                ["A saját tévedhetőségüket beismerve a tudósok megőrzik a nyitottságot.", "Acknowledging their own fallibility scientists preserve openness."],
                ["A cáfolhatatlan dogmákat elutasítva a tudomány elhatárolódik az áltudománytól.", "Rejecting unfalsifiable dogmas science demarcates itself from pseudoscience."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi Karl Popper demarkációs kritériumának lényege a tudományosság meghatározásában?", [
                    "Egy elmélet csak akkor tekinthető tudományosnak, ha elvileg cáfolható (falszifikálható), vagyis megfogalmazható olyan lehetséges empirikus tapasztalat, amely megdöntheti.",
                    "Az, hogy egy állítást mindenki elhisz-e a társadalomban.",
                    "Hogy hány oldalas matematikai bizonyítás tartozik hozzá."
                ], 0, ["c1-34-vocab"]),
                fb("grammar", "controlled", "A hipotézist kísérleti cáfolatnak _____ a kutatók igazolták annak érvényességét. (subjecting / kitéve)", "kitéve", "Subjecting the hypothesis to experimental falsification researchers confirmed its validity.", ["c1-participle-scientific-falsificationism"]),
                match("vocabulary", "controlled", [
                    ["falszifikáció", "az elmélet tapasztalati cáfolatának kísérlete"],
                    ["cáfolhatóság", "a tudományosság alapkövetelménye: elvi megdönthetőség"],
                    ["fallibilizmus", "annak beismerése, hogy minden tudásunk esendő és korrigálható"],
                    ["demarkációs vonal", "a valódi tudomány és a dogmatikus áltudomány közötti határ"]
                ], ["c1-34-vocab"]),
                fb("grammar", "practice", "A dogmatikus feltevéseket elszántan _____ a kutatók megőrizték a módszertani szigort. (rejecting / elutasítva)", "elutasítva", "Rejecting dogmatic assumptions determinedly researchers preserved methodological rigor.", ["c1-participle-scientific-falsificationism"]),
                sb("grammar", "practice", ["A", "tudomány", "az", "elméleteket", "cáfolatnak", "kitéve", "halad", "előre."], ["A", "tudomány", "az", "elméleteket", "cáfolatnak", "kitéve", "halad", "előre."], "Subjecting theories to falsification science advances forward.", ["c1-participle-scientific-falsificationism"]),
                dc("dialogue", [
                    {"speaker": "Biológus", "text": "Miért nem tekinthető tudományosnak a kreacionizmus?"},
                    {"speaker": "Filozófus", "text": "Mert nem teszi ki magát a cáfolatnak: a cáfolhatóság követelményét _____ dogmává merevedik."},
                    {"speaker": "Biológus", "text": "A tudomány éppen a tévedés lehetőségétől tudomány."}
                ], ["megkerülve", "tisztelve", "olvasva"], 0, ["c1-participle-scientific-falsificationism"]),
                sw("production", [{"prompt": "Write a sentence analyzing scientific falsification using a participial clause.", "answer": "A kutatók az új hipotéziseket szisztematikus kísérleti cáfolatnak kitéve és a módszertani fallibilizmus elvét érvényesítve választják el a valódi tudományos eredményeket a dogmatikus áltudománytól."}], ["c1-participle-scientific-falsificationism"]),
                mc("grammar", "check", "Melyik szerkezet fogalmazza meg a tudományos cáfolhatóságot a legszakszerűbben?", [
                    "az elméleteket kísérleti cáfolatnak kitéve és a tévedhetetlenséget elutasítva",
                    "nagyon gyorsan elvégezve a méréseket délben",
                    "ha a laboratórium tiszta és rendezett"
                ], 0, ["c1-participle-scientific-falsificationism"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-34-03",
            "title": "Epistemic Rigor & Intellectual Integrity",
            "grammar_title": "Deontic Modal Structures Asserting Intellectual Duty of Scientific Objectivity",
            "grammar_skill": "c1-modal-deontic-epistemic-rigor",
            "goals": [
                "I can analyze scientific ethics, peer review, data integrity, and epistemic honesty (*episztemikus szigor, adatintegritás, szakmai lektorálás, tudományos etika*).",
                "I can deploy deontic modal structures asserting intellectual duty and scientific objectivity (*a kutatónak kötelessége ragaszkodnia a tényekhez az ideológiai elvárásokkal szemben, megalkuvást nem ismerve kell védeni az adatok integritását, nem engedhető meg a kutatási eredmények politikai megrendelésre történő kozmetikázása*).",
                "I can critique academic fraud and political censorship in scientific publishing."
            ],
            "vocab": [
                {"lemma": "episztemikus szigor", "translation": "epistemic rigor", "pos": "expression"},
                {"lemma": "adatintegritás", "translation": "data integrity", "pos": "noun"},
                {"lemma": "szakmai lektorálás", "translation": "peer review", "pos": "expression"},
                {"lemma": "tudományos objektivitás", "translation": "scientific objectivity", "pos": "expression"},
                {"lemma": "intellektuális tisztesség", "translation": "intellectual honesty / probity", "pos": "expression"},
                {"lemma": "kutatási etika", "translation": "research ethics", "pos": "expression"},
                {"lemma": "eredmények hamisítása", "translation": "falsification / fabrication of data", "pos": "expression"},
                {"lemma": "független bírálat", "translation": "independent review / evaluation", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate the uncompromising ethical responsibility of researchers to truth: `a kutatónak kötelessége a legszigorúbb forráskritikát alkalmaznia` (it is the duty of the researcher to apply the strictest source criticism), `megalkuvást nem ismerve kell ellenállni a politikai és pénzügyi megrendelők nyomásának` (one must resist the pressure of political and financial funders without compromise), `nem engedhető meg a statisztikai adatok manipulatív torzítása` (the manipulative distortion of statistical data cannot be permitted).",
            "gr_text2": "Example: `A tudományos közösségnek feltétlen kötelessége megvédenie a kutatási etika és az adatintegritás tisztaságát a politikai befolyással szemben`.",
            "gr_table": [
                ["A kutatónak kötelessége beismernie, ha a kísérleti adatok nem igazolják az elméletét.", "It is the researcher's duty to admit if experimental data do not confirm their theory."],
                ["Elengedhetetlen a független szakmai lektorálás tisztaságának megőrzése.", "Preserving the purity of independent peer review is indispensable."],
                ["Megalkuvást nem ismerve kell őrködni a tudományos etika sérthetetlensége felett.", "One must watch over the inviolability of research ethics without compromise."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért a független szakmai lektorálás (peer review) a modern tudomány legfőbb minőségi garanciája?", [
                    "Mert biztosítja, hogy egy kutatási eredményt a szakterület független szakértői匿名 módon, szigorú módszertani és etikai szempontok alapján ellenőrizzenek a publikálás előtt.",
                    "Mert a lektorok kapják meg a könyv eladásából származó profitot.",
                    "Mert ez szabályozza a folyóiratok papírméretét."
                ], 0, ["c1-34-vocab"]),
                fb("grammar", "controlled", "A tudósnak etikai _____ a tényekhez ragaszkodni, még ha kellemetlenek is. (duty / kötelessége)", "kötelessége", "It is the scientist's ethical duty to stick to facts even if they are uncomfortable.", ["c1-modal-deontic-epistemic-rigor"]),
                match("vocabulary", "controlled", [
                    ["episztemikus szigor", "a bizonyítási eljárások megalkuvás nélküli pontossága"],
                    ["adatintegritás", "a mérési eredmények torzítatlan és hiteles megőrzése"],
                    ["szakmai lektorálás", "a kéziratok független tudományos szakértői ellenőrzése"],
                    ["tudományos objektivitás", "mentesség minden személyes vagy politikai elfogultságtól"]
                ], ["c1-34-vocab"]),
                fb("grammar", "practice", "Megalkuvást nem ismerve kell _____ az adatok tisztasága felett. (guard / őrködni)", "őrködni", "Without compromise one must watch over the purity of data.", ["c1-modal-deontic-epistemic-rigor"]),
                sb("grammar", "practice", ["A", "kutatónak", "kötelessége", "megvédeni", "a", "tudományos", "igazság", "tisztaságát."], ["A", "kutatónak", "kötelessége", "megvédeni", "a", "tudományos", "igazság", "tisztaságát."], "It is the duty of the researcher to defend the purity of scientific truth.", ["c1-modal-deontic-epistemic-rigor"]),
                dc("dialogue", [
                    {"speaker": "Kutatóintézet vezetője", "text": "Mit kell tennünk, ha a minisztérium a politikai elvárásokhoz igazított eredményeket kér?"},
                    {"speaker": "Akadémikus", "text": "Alkotmányos kötelességünk megtagadni a manipulációt, és megalkuvást nem ismerve kiállni az adatok _____ mellett."},
                    {"speaker": "Kutatóintézet vezetője", "text": "A tudomány hitele mindennél fontosabb."}
                ], ["integritása", "ára", "színe"], 0, ["c1-modal-deontic-epistemic-rigor"]),
                sw("production", [{"prompt": "Write an ethical declaration of scientific objectivity using a deontic modal.", "answer": "A tudományos kutatóknak erkölcsi kötelességük ragaszkodni az episztemikus szigorhoz és a tényekhez, és megalkuvást nem ismerve kell megvédeniük az adatintegritást minden külső politikai és gazdasági nyomással szemben."}], ["c1-modal-deontic-epistemic-rigor"]),
                mc("grammar", "check", "Melyik deontikus szerkezet fogalmazza meg a kutatói felelősséget a leghatározottabban?", [
                    "kötelessége ragaszkodni a tényekhez / megalkuvást nem ismerve kell védeni az objektivitást",
                    "talán jobb lenne még egyszer átnézni a számokat ha ráérünk",
                    "a professzorok néha beszélgessenek a kísérletekről"
                ], 0, ["c1-modal-deontic-epistemic-rigor"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-34-04",
            "title": "Paradigm Shifts & Epistemological Revolutions",
            "grammar_title": "Scalar Comparative Adverbials Tracing Epistemological Paradigm Shifts and Discovery",
            "grammar_skill": "c1-adv-comparative-paradigmatic-shift",
            "goals": [
                "I can analyze Thomas Kuhn's paradigm shifts, scientific revolutions, and incommensurability (*paradigmaváltás, tudományos forradalom, normál tudomány, összemérhetetlenség*).",
                "I can deploy scalar comparative adverbials tracing epistemological ruptures (*radikálisabban szakítva a korábbi mechanisztikus világképpel, sokkal átfogóbban magyarázva a kozmikus jelenségeket, felülmúlhatatlanul forradalmasítva az elméletet*).",
                "I can discuss the transition from Newtonian mechanics to Einsteinian relativity in philosophy of physics."
            ],
            "vocab": [
                {"lemma": "paradigmaváltás", "translation": "paradigm shift (Kuhn concept)", "pos": "noun"},
                {"lemma": "tudományos forradalom", "translation": "scientific revolution", "pos": "expression"},
                {"lemma": "normál tudomány", "translation": "normal science", "pos": "expression"},
                {"lemma": "anomália", "translation": "anomaly", "pos": "noun"},
                {"lemma": "összemérhetetlenség", "translation": "incommensurability", "pos": "noun"},
                {"lemma": "elméleti áttörés", "translation": "theoretical breakthrough", "pos": "expression"},
                {"lemma": "fogalmi keret", "translation": "conceptual framework", "pos": "expression"},
                {"lemma": "világkép-váltás", "translation": "shift in worldview / cosmology", "pos": "expression"}
            ],
            "gr_text1": "Scalar comparative adverbials describe the profound rupture brought by new scientific paradigms: `radikálisabban kérdőjelezve meg az alapfeltevéseket, mint elődei` (questioning fundamental assumptions more radically than predecessors), `sokkal átfogóbban szintetizálva a tapasztalati tényeket` (synthesizing empirical facts much more comprehensively), `felülmúlhatatlanul forradalmasítva a fizika fogalmi kereteit` (insurpassably revolutionizing the conceptual frameworks of physics).",
            "gr_text2": "Example: `Einstein relativitáselmélete radikálisabban formálta át a tér és idő fogalmát, sokkal mélyebbre hatolva a valóság természetébe, mint a klasszikus mechanika`.",
            "gr_table": [
                ["Az új paradigma radikálisabban magyarázta az anomáliákat, mint a régi elmélet.", "The new paradigm explained anomalies more radically than the old theory."],
                ["Einstein sokkal mélyebbre hatolt a gravitáció megértésében, mint kortársai.", "Einstein penetrated much deeper into understanding gravity than his contemporaries."],
                ["A kvantumelmélet felülmúlhatatlanul forradalmasította az anyagról vallott nézeteket.", "Quantum theory insurpassably revolutionized views held about matter."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez Thomas Kuhn 'paradigmaváltásnak' a tudománytörténetben?", [
                    "Azt a forradalmi folyamatot, amikor a felhalmozódó anomáliák hatására a korábbi uralkodó elméleti és módszertani keret összeomlik, és egy új, összemérhetetlen világkép lép a helyébe.",
                    "Amikor a professzorok új irodába költöznek az egyetemen.",
                    "A laboratóriumi műszerek évenkénti kötelező selejtezését."
                ], 0, ["c1-34-vocab"]),
                fb("grammar", "controlled", "Az új elmélet radikálisabban _____ át a világképet, mint a korábbi hipotézisek. (transformed / formálta)", "formálta", "The new theory transformed the worldview more radically than previous hypotheses.", ["c1-adv-comparative-paradigmatic-shift"]),
                match("vocabulary", "controlled", [
                    ["paradigmaváltás", "az uralkodó tudományos világkép gyökeres megváltozása"],
                    ["normál tudomány", "a meglévő paradigma keretein belüli rutinszerű kutatómunka"],
                    ["anomália", "a jelenlegi elmélet által megmagyarázhatatlan kísérleti jelenség"],
                    ["összemérhetetlenség", "a versengő paradigmák közös fogalmi mérce nélküli eltérése"]
                ], ["c1-34-vocab"]),
                fb("grammar", "practice", "A kvantumfizika sokkal átfogóbban _____ a mikrovilágot, mint a newtoni modell. (explained / magyarázta)", "magyarázta", "Quantum physics explained the microworld much more comprehensively than the Newtonian model.", ["c1-adv-comparative-paradigmatic-shift"]),
                sb("grammar", "practice", ["Az", "új", "paradigma", "radikálisabban", "szakított", "a", "múlt", "dogmáival."], ["Az", "új", "paradigma", "radikálisabban", "szakított", "a", "múlt", "dogmáival."], "The new paradigm broke more radically with the dogmas of the past.", ["c1-adv-comparative-paradigmatic-shift"]),
                dc("dialogue", [
                    {"speaker": "Fizikatörténész", "text": "Hogyan értékelhető a relativitáselmélet hatása a modern ember gondolkodására?"},
                    {"speaker": "Filozófus", "text": "Úgy, hogy felülmúlhatatlanul forradalmasítva a fogalmi kereteket, sokkal mélyebbre hatolt a kozmosz titkaiba, mint bármely korábbi _____."},
                    {"speaker": "Fizikatörténész", "text": "Ez volt a huszadik század legnagyobb episztemológiai fordulata."}
                ], ["elmélet", "törvény", "írás"], 0, ["c1-adv-comparative-paradigmatic-shift"]),
                sw("production", [{"prompt": "Write a comparative analysis of a paradigm shift using a scalar comparative adverbial.", "answer": "Az új tudományos paradigma sokkal átfogóbban szintetizálva a felhalmozódott anomáliákat és radikálisabban szakítva a mechanisztikus világképpel, felülmúlhatatlanul forradalmasította a modern fizika fogalmi alapjait."}], ["c1-adv-comparative-paradigmatic-shift"]),
                mc("grammar", "check", "Melyik fokozó hasonlító határozói forma írja le a tudományos forradalmat a legpontosabban?", [
                    "radikálisabban szakítva a dogmákkal / sokkal átfogóbban szintetizálva a tényeket",
                    "kicsit gyorsabban számolva mint a számológép",
                    "több cikket írva mint az előző évben"
                ], 0, ["c1-adv-comparative-paradigmatic-shift"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-34-05",
            "title": "Mihály Polányi: The Republic of Science & Academic Freedom",
            "grammar_title": "Hypothetical and Deductive Syntax Structuring the Republic of Science Doctrine",
            "grammar_skill": "c1-syntax-republic-of-science-deduction",
            "goals": [
                "I can analyze Mihály Polányi's foundational essay 'A tudomány köztársasága' (The Republic of Science, 1962), spontaneous coordination, and anti-totalitarian academic freedom (*A tudomány köztársasága, spontán rend, tudományos önigazgatás, szovjet tervtudomány bírálata*).",
                "I can construct hypothetical and deductive syntax structuring academic self-governance (*amennyiben az állam központi tervutasításokkal próbálja irányítani a kutatást, úgy a tudományos felfedezés szerves önszerveződése elkerülhetetlenül megsemmisül*).",
                "I can synthesize the economic and philosophical defense of academic autonomy against state intervention."
            ],
            "vocab": [
                {"lemma": "A tudomány köztársasága", "translation": "The Republic of Science (Polányi manifesto)", "pos": "expression"},
                {"lemma": "spontán rend", "translation": "spontaneous order / decentralized coordination", "pos": "expression"},
                {"lemma": "tudományos önigazgatás", "translation": "scientific self-governance", "pos": "expression"},
                {"lemma": "tervezett tudomány", "translation": "centrally planned science (Lysenkoism)", "pos": "expression"},
                {"lemma": "kölcsönös alkalmazkodás", "translation": "mutual adjustment / coordination among peers", "pos": "expression"},
                {"lemma": "kutatási szabadság", "translation": "freedom of basic research", "pos": "expression"},
                {"lemma": "alapkutatás", "translation": "basic / fundamental research", "pos": "noun"},
                {"lemma": "tudományos piac", "translation": "free marketplace of scientific ideas", "pos": "expression"}
            ],
            "gr_text1": "Hypothetical and deductive syntax in political philosophy of science proves that centrally planned science is a contradiction in terms: `amennyiben a politikai hatalom megfosztja a kutatókat az autonóm témaválasztástól, úgy a tudomány belső hajtóereje megbénul` (insofar as political power deprives researchers of autonomous choice of topics, so the internal engine of science is paralyzed), `hacsak a kutatók nem hangolják össze munkájukat a spontán koordináció révén, a tudományos haladás elakad` (unless researchers coordinate their work through spontaneous coordination, scientific progress stalls).",
            "gr_text2": "Example: `Amennyiben a bürokrácia felülről szabja meg a kutatási irányokat, úgy a felfedezések kiszámíthatatlan heurisztikus természete vész el, elsorvasztva az egész intézményrendszert`.",
            "gr_table": [
                ["Amennyiben tiszteletben tartják az autonómiát, úgy a tudósok közössége spontán rendet alkot.", "Insofar as autonomy is respected, so the community of scientists forms a spontaneous order."],
                ["Hacsak a kutatás nem szabad, a gazdasági innováció is zátonyra fut.", "Unless research is free, economic innovation also runs aground."],
                ["Mivel a felfedezés előre nem látható, a központi tervezés abszurdum a tudományban.", "Since discovery is unforeseen, central planning is an absurdity in science."]
            ],
            "classic_story": {
                "slug": "polanyi-tudomany-koztarsasaga",
                "title": "Polányi Mihály: A tudomány köztársasága és a szabadság",
                "author": "Polányi Mihály",
                "work": "A tudomány köztársasága (Minerva, 1962) / Személyes tudás (1958)",
                "summary": "Polányi Mihály (1891–1976) fiziko-kémikus, gazdaságtudós és filozófus, a Magyar Tudományos Akadémia tagja volt, a huszadik század egyik legmélyebb gondolkodója. Amikor a szovjet mintájú totalitárius állam és a nyugati technokraták a kutatás központi állami megtervezését követelték, Polányi megírta 'A tudomány köztársasága' című korszakalkotó esszéjét. Ebben bebizonyította, hogy a tudományos közösség egy láthatatlan, decentralizált köztársaság: a kutatók kölcsönösen ellenőrzik és inspirálják egymást, mint a sakkozók egy gigantikus szimultán játszmában. Ha a hatalom politikai vagy gazdasági célszerűségből felülről akarja vezényelni a tudományt, elpusztítja magát a felfedezés képességét.",
                "characters": ["Polányi Mihály, a szabadság filozófusa", "Nemzetközi kutatók közössége"],
                "paragraphs": [
                    {"type": "narration", "text": "A huszadik század közepén félelmetes illúzió hódított a világban: a szovjet lizsenkóizmus és a totalitárius államhatalom azt hirdette, hogy a tudománynak kizárólag a párt által meghatározott gazdasági és politikai célokat kell szolgálnia, a szabad alapkutatás pedig haszontalan polgári luxus."},
                    {"type": "dialogue", "speaker": "Polányi Mihály", "text": "A tudomány köztársasága olyan önkéntes polgárok szövetsége, akik a független kutatás szabadságában élnek. Ahogyan a szabad piacon az árak koordinálják a cselekvést, úgy a tudományban a kutatók spontán rendje, az egymás eredményeihez való kölcsönös alkalmazkodás biztosítja a haladást. Ha ezt a spontán koordinációt bürokratikus parancsokkal helyettesítik, a tudomány elsorvad."},
                    {"type": "narration", "text": "Polányi rámutatott, hogy a legfontosabb áttörések mindig kiszámíthatatlanok: a penicillin, a röntgensugár vagy a kvantummechanika felfedezése soha nem születhetett volna meg központi minisztériumi tervek alapján. A szabadság nem a tudomány mellékes kelléke, hanem létének legfőbb előfeltétele."},
                    {"type": "narration", "text": "Polányi Mihály szellemi öröksége a demokratikus világ legfőbb érve maradt: a kutatás szabadsága, az akadémiai önigazgatás és a tudomány köztársasága a modern civilizáció legdrágább vívmánya, amelyet minden tekintélyelvű beavatkozással szemben meg kell védenünk."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működik 'a tudomány köztársasága' Polányi Mihály elméletében?", [
                    "A tudósok autonóm, decentralizált közösségeként, akik a spontán rend és a kölcsönös szakmai kontroll révén szabadon koordinálják kutatásaikat minden központi állami parancs nélkül.",
                    "Egy olyan parlamentként, ahol a politikusok szavaznak a fizikai képletekről.",
                    "Egy állami minisztériumként, amely megszabja a kutatók heti órarendjét."
                ], 0, ["c1-34-vocab"]),
                fb("grammar", "controlled", "Amennyiben a kormányzat megvonja az autonómiát, _____ a tudományos felfedezés motorja áll le. (so / úgy)", "úgy", "Insofar as the government withdraws autonomy, so the engine of scientific discovery stalls.", ["c1-syntax-republic-of-science-deduction"]),
                match("vocabulary", "controlled", [
                    ["A tudomány köztársasága", "Polányi koncepciója a független kutatók önigazgató szövetségéről"],
                    ["spontán rend", "a kutatók decentralizált, kölcsönös szakmai koordinációja"],
                    ["tervezett tudomány", "a kutatási irányok felülről vezényelt, kudarcra ítélt totalitárius modellje"],
                    ["alapkutatás", "a közvetlen hasznot nem kereső, a valóság megértésére irányuló tiszta tudomány"]
                ], ["c1-34-vocab"]),
                fb("grammar", "practice", "Hacsak a kutatók nem szabadok, az egész innovációs rendszer _____ fut. (runs aground / zátonyra)", "zátonyra", "Unless researchers are free, the entire innovation system runs aground.", ["c1-syntax-republic-of-science-deduction"]),
                sb("grammar", "practice", ["Amennyiben", "a", "kutatás", "szabad,", "úgy", "virágzik", "a", "tudományos", "haladás."], ["Amennyiben", "a", "kutatás", "szabad,", "úgy", "virágzik", "a", "tudományos", "haladás."], "Insofar as research is free, so scientific progress flourishes.", ["c1-syntax-republic-of-science-deduction"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Miért nem lehet a tudományos felfedezést ötéves tervekkel előre megjósolni?"},
                    {"speaker": "Polányi-kutató", "text": "Mivel a felfedezések lényege a kiszámíthatatlanság, amennyiben a bürokrácia parancsol, úgy megsemmisül a kutatás heurisztikus _____."},
                    {"speaker": "Kutató", "text": "A szabadság a tudomány legfőbb termelőereje."}
                ], ["ereje", "ára", "neve"], 0, ["c1-syntax-republic-of-science-deduction"]),
                sw("production", [{"prompt": "Write a deductive defense of academic freedom using hypothetical syntax.", "answer": "Amennyiben a politikai hatalom centralizált bürokratikus parancsokkal kényszeríti rá akaratát az akadémiai szférára, úgy a tudomány köztársaságának spontán rendje felbomlik, és a nemzet menthetetlenül lemarad a globális fejlődésben."}], ["c1-syntax-republic-of-science-deduction"]),
                mc("grammar", "check", "Melyik mondatszerkezet dedukálja a tudományos szabadság szükségességét?", [
                    "amennyiben korlátozzák az önigazgatást, úgy a tudományos felfedezés heurisztikus ereje elvész",
                    "amikor a laborban felkapcsolják a villanyt reggel",
                    "ha sok könyv van a polcon, nehéz megtalálni a megfelelőt"
                ], 0, ["c1-syntax-republic-of-science-deduction"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(34, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        34,
        "core",
        "c1-34-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of epistemology, tacit knowledge, falsificationism, and academic self-governance.",
            "I can employ evaluative tacit knowledge adverbials, participial falsification clauses, and deontic modal structures of integrity.",
            "I can formulate and deduce Polányi Mihály's Republic of Science doctrine and epistemological paradigm shifts."
        ],
        [
            mc("grammar", "recognize", "Melyik határozói kifejezés formulázza a rejtett megismerés természetét a legszakszerűbben?", [
                "hallgatólagos tudásra támaszkodva / episztemikusan megalapozott módon",
                "hogyha valaki sokat kísérletezik a műhelyben",
                "amikor a tudósok kávéznak az előadás előtt"
            ], 0, ["c1-adv-epistemic-tacit-knowledge"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhető ki a tudományos cáfolhatóság metodológiája a leghitelesebben?", [
                "az elméleteket könyörtelen kísérleti cáfolatnak kitéve és a fallibilizmus elvét tiszteletben tartva",
                "amikor a professzor aláírja a dolgozatot",
                "ha a könyvtárban sok új könyv jelenik meg"
            ], 0, ["c1-participle-scientific-falsificationism"]),
            match("vocabulary", "recognize", [
                ["hallgatólagos tudás", "a kimondhatatlan, de a cselekvésben megnyilvánuló mély előtudás"],
                ["falszifikáció", "az elmélet tapasztalati cáfolatának szigorú módszertana"],
                ["paradigmaváltás", "az uralkodó tudományos világkép forradalmi összeomlása és megújulása"],
                ["A tudomány köztársasága", "Polányi tétele a kutatók autonóm, spontán önszerveződéséről"]
            ], ["c1-34-vocab"]),
            fb("vocabulary", "recall", "Minden tudásunk esendő és felülvizsgálatra szorul a módszertani _____ szerint. (fallibilism / fallibilizmus)", "fallibilizmus", "All our knowledge is fallible and subject to revision according to methodological fallibilism.", ["c1-34-vocab"]),
            fb("vocabulary", "recall", "A tudósok közössége központi parancsok nélkül, _____ rendben koordinálja munkáját. (spontaneous / spontán)", "spontán", "The community of scientists coordinates its work in spontaneous order without central commands.", ["c1-34-vocab"]),
            fb("grammar", "recall", "A hipotézist szisztematikus cáfolatnak _____ választjuk el a tudományt a dogmáktól. (subjecting / kitéve)", "kitéve", "Subjecting the hypothesis to systematic falsification we separate science from dogmas.", ["c1-participle-scientific-falsificationism"]),
            fb("grammar", "context", "A kutatónak etikai _____ az igazsághoz ragaszkodnia a politikai nyomással szemben. (duty / kötelessége)", "kötelessége", "It is the researcher's ethical duty to adhere to truth against political pressure.", ["c1-modal-deontic-epistemic-rigor"]),
            fb("grammar", "context", "Amennyiben megfosztják a tudományt a szabadságtól, _____ elvész a felfedezés heurisztikus ereje. (so / úgy)", "úgy", "Insofar as science is deprived of freedom, so the heuristic power of discovery is lost.", ["c1-syntax-republic-of-science-deduction"]),
            mc("grammar", "context", "Mi Polányi szerint a tudomány köztársaságának legfőbb gazdasági és társadalmi tanulsága?", [
                "A központi bürokratikus tervezés képtelen a felfedezések vezérlésére, így a társadalmi haladás záloga az autonóm önszerveződés és a szabadság.",
                "A tudományra nem szabad pénzt költeni a költségvetésből.",
                "A kutatóknak mind vállalkozóvá kell válniuk."
            ], 0, ["c1-syntax-republic-of-science-deduction"]),
            sb("grammar", "produce", ["A", "tudományos", "kutatás", "szabadsága", "a", "modern", "társadalom", "legfőbb", "értéke."], ["A", "tudományos", "kutatás", "szabadsága", "a", "modern", "társadalom", "legfőbb", "értéke."], "Freedom of scientific research is the paramount value of modern society.", ["c1-syntax-republic-of-science-deduction"]),
            sw("production", [{"prompt": "Write a critical evaluation of scientific fallibilism using a participial clause.", "answer": "A kutatók a felállított elméleteket szigorú empirikus cáfolatnak kitéve és a módszertani fallibilizmus elvét érvényesítve garantálják, hogy a tudomány mentes maradjon a politikai és ideológiai dogmáktól."}], ["c1-participle-scientific-falsificationism"]),
            sw("production", [{"prompt": "Synthesize the Republic of Science doctrine using hypothetical and deductive syntax.", "answer": "Amennyiben az állam tiszteletben tartja a kutatás autonómiáját, úgy a tudósok köztársasága a spontán koordináció révén olyan heurisztikus erőt és innovációt teremt, amely az egész nemzet felemelkedését szolgálja."}], ["c1-syntax-republic-of-science-deduction"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-tudomanyosszabadsag)
    # ----------------------------------------------------
    disc_intro = [
        "In post-2010 Hungary, academic freedom and institutional scientific autonomy suffered unprecedented state-driven assaults, culminating in the hostile takeover of the Academy of Sciences research institutes, the forced expulsion of CEU, and the privatization of universities into oligarchic political foundations.",
        "In this unit, following the dramatic timeline of the stripping of MTA research institutes, the 'Lex CEU' exile, the KEKVA foundation model, and the subsequent EU exclusion from Erasmus and Horizon programs, you will master the elevated analytical discourse of academic freedom, institutional asset stripping, and intellectual resistance at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Hostile Takeover of MTA Research Institutes",
            "grammar_title": "Discourse Markers Diagnosing Authoritarian Asset Stripping of Scientific Academies",
            "grammar_skill": "c1-discourse-academic-asset-stripping-framing",
            "goals": [
                "I can analyze the 2019 dismantling and stripping of the Hungarian Academy of Sciences (MTA) research network (*MTA kutatóhálózat elcsatolása, Palkovics-ultimátum, Eötvös Loránd Kutatási Hálózat / HUN-REN, szellemi és vagyoni fosztogatás*).",
                "I can deploy discourse markers diagnosing authoritarian asset stripping (*az akadémiai autonómia elleni brutális hatalmi támadásként értékelve, a kutatóhálózat politikai célzatú einstandolásaként aposztrofálva, a tudományos vagyon önkényes elvonásának jegyében*).",
                "I can critique the subordination of basic research to short-term government industrial interests."
            ],
            "vocab": [
                {"lemma": "MTA kutatóhálózat", "translation": "research network of the Hungarian Academy of Sciences", "pos": "expression"},
                {"lemma": "kutatóhálózat elcsatolása", "translation": "stripping / detachment of the research network", "pos": "expression"},
                {"lemma": "akadémiai autonómia", "translation": "academic autonomy", "pos": "expression"},
                {"lemma": "Palkovics-ultimátum", "translation": "Palkovics ultimatum (ministerial coercion)", "pos": "expression"},
                {"lemma": "vagyonelvonás", "translation": "confiscation / asset stripping of institutional property", "pos": "noun"},
                {"lemma": "alapkutatás elsorvasztása", "translation": "atrophy / crippling of basic research", "pos": "expression"},
                {"lemma": "tudományos tiltakozás", "translation": "protest of the scientific community", "pos": "expression"},
                {"lemma": "politikai einstand", "translation": "hostile political takeover / expropriation", "pos": "expression"}
            ],
            "gr_text1": "Discourse markers expose state-directed hostile takeovers and expropriation of scientific institutions: `az akadémiai autonómia elleni brutális merényletként értékelve` (evaluated as a brutal assault against academic autonomy), `a történelmi kutatóintézeti hálózat politikai einstandolásaként aposztrofálva` (characterized as hostile political expropriation of the historic research network), `a kutatói szabadság adminisztratív megfojtásának jegyében` (in the spirit of administratively suffocating research freedom).",
            "gr_text2": "Example: `A Magyar Tudományos Akadémia kutatóhálózatának 2019-es elcsatolását a tudományos világ nyílt politikai vagyonelkobzásként értékelve egyhangúlag elítélte`.",
            "gr_table": [
                ["A lépést az akadémiai szabadság felszámolásaként értékelve tüntettek a kutatók.", "Evaluating the step as the elimination of academic freedom researchers demonstrated."],
                ["A kutatóhálózat elcsatolását nyílt politikai einstandként aposztrofálták a tudósok.", "Scientists characterized the detachment of the research network as a hostile political takeover."],
                ["A vagyonelvonás jegyében fosztották meg az Akadémiát saját intézeteitől.", "In the spirit of asset stripping they deprived the Academy of its own institutes."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-01-mta-kutatohalozat-elcsatolasa",
                "title": "A tudomány einstandolása: Az MTA kutatóhálózatának elrablása",
                "summary": "2019-ben Palkovics László innovációs miniszter ultimátumot adott a közel kétszáz éves Magyar Tudományos Akadémiának: a kormányzat erőszakkal elcsatolta az Akadémia teljes, tizenötezer fős kutatóhálózatát és vagyonát.",
                "paragraphs": [
                    {"type": "narration", "text": "2019 nyarán a magyar tudományosság történetének legsötétebb napjai következtek el: a kormányzat törvénnyel szakította el a Széchenyi István által 1825-ben alapított Magyar Tudományos Akadémiától (MTA) teljes kutatóhálózatát."},
                    {"type": "dialogue", "speaker": "Lovász László", "text": "Az akadémiai autonómia elleni nyílt támadásként értékelve a döntést hangsúlyoznom kell: az Akadémia nem pártpolitikai játszótér, hanem a nemzet legfőbb szellemi vagyona. A kutatóintézetek elvétele nem reform, hanem erőszakos politikai einstand."},
                    {"type": "narration", "text": "Kutatók ezrei vonultak az utcára, élőlánccal vették körül az Akadémia székházát a Széchenyi téren, könyveket magasba tartva tiltakoztak a kormányzati önkény ellen. Palkovics László miniszter a források azonnali megvonásával zsarolta a professzorokat, hogy kikényszerítse a behódolást."},
                    {"type": "narration", "text": "A hálózatot végül kiszakították az MTA kebeléből és kormányzati felügyelet alá helyezték. Bár a kutatók szakmai tisztessége megmaradt, az állami erőszak precedenst teremtett: bebizonyosodott, hogy a hatalom a tudományos szférát is vazallusi sorba kívánja taszítani."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan hajtotta végre a kormányzat az MTA kutatóhálózatának elcsatolását 2019-ben?", [
                    "Költségvetési zsarolással és törvénymódosítással erőszakkal elvette az Akadémiától a teljes kutatóintézeti hálózatát és ingatlanvagyonát, és kormányzati ellenőrzés alá vonta.",
                    "Megkérdezte a kutatókat titkos szavazással és elfogadta a döntésüket.",
                    "Megduplázta az alapkutatások támogatását feltételek nélkül."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A döntést az akadémiai szabadság felszámolásaként _____ a nemzetközi tudományos társaságok tiltakoztak. (evaluating / értékelve)", "értékelve", "Evaluating the decision as the elimination of academic freedom international scientific societies protested.", ["c1-discourse-academic-asset-stripping-framing"]),
                match("vocabulary", "controlled", [
                    ["MTA kutatóhálózat", "a magyar alapkutatások közel kétszáz éves intézményrendszere"],
                    ["Palkovics-ultimátum", "kormányzati pénzügyi fenyegetés az MTA önállóságának megtörésére"],
                    ["akadémiai autonómia", "a kutatók joga a független kutatási témaválasztásra és vezetésre"],
                    ["politikai einstand", "az önálló intézmények erőszakos állami kisajátítása"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A lépést politikai fosztogatásként _____ az egyetemi karok szolidaritást vállaltak. (characterizing / aposztrofálva)", "aposztrofálva", "Characterizing the step as political looting university faculties showed solidarity.", ["c1-discourse-academic-asset-stripping-framing"]),
                sb("grammar", "practice", ["Az", "állam", "erőszakkal", "elcsatolta", "az", "MTA", "kutatóhálózatát."], ["Az", "állam", "erőszakkal", "elcsatolta", "az", "MTA", "kutatóhálózatát."], "The state detached the MTA research network by force.", ["c1-discourse-academic-asset-stripping-framing"]),
                dc("dialogue", [
                    {"speaker": "Kutatóorvos", "text": "Mi volt a célja az akadémiai kutatóhálózat elszakításának?"},
                    {"speaker": "Tudományszociológus", "text": "Az, hogy a független alapkutatások helyett közvetlen politikai és gazdasági befolyás alá vonják a kutatási _____."},
                    {"speaker": "Kutatóorvos", "text": "De az alapkutatás nélkül nincs innováció."}
                ], ["témákat", "utazásokat", "szobákat"], 0, ["c1-discourse-academic-asset-stripping-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of the MTA takeover using a discourse marker.", "answer": "Az MTA kutatóhálózatának erőszakos elcsatolását a tudományos autonómia elleni brutális politikai beavatkozásként értékelve a nemzetközi akadémiai közösség rávilágított arra, hogy az önkényes vagyonelvonás jóvátehetetlen károkat okoz a magyar tudománynak."}], ["c1-discourse-academic-asset-stripping-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a kutatóhálózat kisajátítását a legpontosabban?", [
                    "az akadémiai autonómia elleni politikai merényletként értékelve / nyílt einstandként aposztrofálva",
                    "amikor a laborba új mikroszkópot szállítanak a munkások",
                    "hogyha a kutatók elmennek egy nemzetközi konferenciára"
                ], 0, ["c1-discourse-academic-asset-stripping-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Lex CEU & The Forced Exile of a University",
            "grammar_title": "Critical Evaluative Adverbials Exposing State-Enforced Academic Exile and University Purges",
            "grammar_skill": "c1-adv-academic-expulsion-critique",
            "goals": [
                "I can analyze the 'Lex CEU' of 2017, the political campaign against Central European University, and its forced relocation to Vienna (*Lex CEU, egyetem elüldözése, Bécsbe költözés, Európai Bíróság elmarasztalása, Michael Ignatieff*).",
                "I can deploy critical evaluative adverbials exposing state-enforced academic exile (*példátlan módon elüldözve egy kiváló egyetemet, a felsőoktatási törvényt diszkriminatív módon módosítva, a nemzetközi normákat nyíltan lábbal tiporva*).",
                "I can critique the European Court of Justice ruling declaring the Hungarian Lex CEU unlawful."
            ],
            "vocab": [
                {"lemma": "Lex CEU", "translation": "Lex CEU (discriminatory university amendment)", "pos": "expression"},
                {"lemma": "egyetem elüldözése", "translation": "forced expulsion / exile of a university", "pos": "expression"},
                {"lemma": "Közép-európai Egyetem", "translation": "Central European University (CEU)", "pos": "expression"},
                {"lemma": "Bécsbe költözés", "translation": "relocation to Vienna", "pos": "expression"},
                {"lemma": "Európai Bíróság ítélete", "translation": "judgment of the European Court of Justice", "pos": "expression"},
                {"lemma": "felsőoktatási autonómia", "translation": "higher education autonomy", "pos": "expression"},
                {"lemma": "nemzetközi felháborodás", "translation": "international outcry / condemnation", "pos": "expression"},
                {"lemma": "szabad egyetem", "translation": "free university movement", "pos": "expression"}
            ],
            "gr_text1": "Critical evaluative adverbials expose state-driven political purges and the expulsion of academic institutions: `példátlan módon elüldözve egy nemzetközileg elismert egyetemet` (expelling an internationally renowned university in an unprecedented manner), `a jogszabályokat célzottan és diszkriminatív módon módosítva` (amending legislation in a targeted and discriminatory manner), `a tudományos élet szabadságát cinikusan lábbal tiporva` (cynically trampling on the freedom of scientific life).",
            "gr_text2": "Example: `A hatalom a Lex CEU révén diszkriminatív módon eljárva és a nemzetközi szerződéseket megsértve kényszerítette a Közép-európai Egyetemet bécsi száműzetésbe`.",
            "gr_table": [
                ["A kormányzat diszkriminatív módon módosítva a törvényt lehetetlenítette el a CEU-t.", "Amending the law in a discriminatory manner the government paralyzed CEU."],
                ["Példátlan módon elüldözve az egyetemet hatalmas presztízsveszteséget okoztak az országnak.", "Expelling the university in an unprecedented manner they caused massive prestige loss to the country."],
                ["A nemzetközi normákat cinikusan figyelmen kívül hagyva tagadták meg az engedélyt.", "Cynically ignoring international norms they refused permission."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-02-lex-ceu-egyetem-eluldzese",
                "title": "A tanszabadság fekete napja: A CEU elűzése Budapestről",
                "summary": "2017 tavaszán a kormányzat elfogadta a hírhedt 'Lex CEU-t', amely lehetetlen feltételekhez kötötte a Közép-európai Egyetem budapesti működését. A tömegtüntetések és az Európai Bíróság ítélete ellenére az egyetem kénytelen volt Bécsbe költözni.",
                "paragraphs": [
                    {"type": "narration", "text": "2017 áprilisában több mint nyolcvanezer ember vonult végig Budapest utcáin a 'Szabad ország, szabad egyetem!' jelszót skandálva. A felháborodást a parlament által villámgyorsan áterőltetett Lex CEU váltotta ki, amely célzottan a Soros György által alapított kiváló egyetem ellehetetlenítésére készült."},
                    {"type": "dialogue", "speaker": "Michael Ignatieff", "text": "A modern Európa történetében a második világháború óta nem fordult elő, hogy egy demokratikusnak mondott kormány elüldözzön egy akkreditált, világhírű egyetemet a fővárosából. Diszkriminatív módon eljárva nemcsak minket sértettek meg, hanem a magyar egyetemi ifjúság jövőjét tették tönkre."},
                    {"type": "narration", "text": "Bár a CEU minden koholt törvényi feltételt teljesített – még New York államban is létesített campust –, a magyar kormányfő egyszerűen megtagadta a már letárgyalt nemzetközi megállapodás aláírását. Az egyetem nem várhatott tovább: amerikai akkreditációjú képzéseit Bécsbe költöztette."},
                    {"type": "narration", "text": "Évekkel később a luxembourgi Európai Bíróság kimondta: a Lex CEU sértette az uniós jogot és a WTO szerződéseit. Az igazságtétel azonban megkésett: az egyetem már Ausztriában működött, Budapest pedig örökre elveszítette a régió legkiválóbb szellemi központját."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinthető a Lex CEU és az egyetem elüldözése a rendszerváltás utáni legsúlyosabb tanszabadság-ellenes aktusnak?", [
                    "Mert a második világháború óta először fordult elő Európában, hogy egy kormány politikai bosszúból, diszkriminatív törvénnyel száműzött egy világhírű egyetemet a fővárosából.",
                    "Mert az egyetem nem fizette ki a fűtésszámlát a budapesti épületben.",
                    "Mert a diákok túl sok angol nyelvű könyvet olvastak a könyvtárban."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A jogszabályt diszkriminatív módon _____ a kormányzat ellehetetlenítette az egyetem működését. (amending / módosítva)", "módosítva", "Amending the statute in a discriminatory manner the government made the university's operation impossible.", ["c1-adv-academic-expulsion-critique"]),
                match("vocabulary", "controlled", [
                    ["Lex CEU", "a Közép-európai Egyetem ellen hozott diszkriminatív felsőoktatási törvény"],
                    ["egyetem elüldözése", "egy nemzetközi intézmény politikai kényszerítése az ország elhagyására"],
                    ["felsőoktatási autonómia", "az egyetemek szabadsága a kutatásban és oktatásban"],
                    ["szabad egyetem", "a polgárok és diákok mozgalma a tanszabadság megvédéséért"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Példátlan módon elüldözve az egyetemet a hatalom cinikusan _____ a nemzetközi jogot. (trampled / tiporta)", "tiporta", "Expelling the university in an unprecedented manner power cynically trampled international law.", ["c1-adv-academic-expulsion-critique"]),
                sb("grammar", "practice", ["A", "kormányzat", "diszkriminatív", "módon", "elüldözte", "a", "CEU-t", "Budapestről."], ["A", "kormányzat", "diszkriminatív", "módon", "elüldözte", "a", "CEU-t", "Budapestről."], "The government expelled CEU from Budapest in a discriminatory manner.", ["c1-adv-academic-expulsion-critique"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Hogyan értékelte a döntést az Európai Bíróság?"},
                    {"speaker": "Nemzetközi jogász", "text": "Úgy, hogy a nemzetközi normákat cinikusan lábbal tiporva a magyar törvény súlyosan megsértette a tanszabadság _____."},
                    {"speaker": "Egyetemi hallgató", "text": "De a CEU addigra már Bécsben tanított."}
                ], ["alapjogát", "árát", "épületét"], 0, ["c1-adv-academic-expulsion-critique"]),
                sw("production", [{"prompt": "Write a critical evaluation of the CEU expulsion using an evaluative adverbial.", "answer": "A felsőoktatási törvényt célzottan és diszkriminatív módon módosítva a hatalom példátlan módon elüldözte a Közép-európai Egyetemet Budapestről, pótolhatatlan intellektuális és nemzetközi veszteséget okozva a magyar kultúrának."}], ["c1-adv-academic-expulsion-critique"]),
                mc("grammar", "check", "Melyik kifejezés bélyegzi meg a CEU elűzését a legpontosabb jogi-kritikai formában?", [
                    "diszkriminatív módon eljárva / példátlan módon elüldözve az egyetemet",
                    "amikor az egyetem bezárta az ajtót délután ötkor",
                    "hogyha a diákok elutaznak Bécsbe vonattal"
                ], 0, ["c1-adv-academic-expulsion-critique"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "The KEKVA Model & Oligarchic University Foundations",
            "grammar_title": "Deontic Modal Structures Formulating University Senates Duty of Self-Governance",
            "grammar_skill": "c1-modal-deontic-senate-autonomy-defense",
            "goals": [
                "I can analyze the privatization of state universities into KEKVA public trust foundations, kuratóriumok, and the stripping of senatorial power (*KEKVA modellváltás, közérdekű vagyonkezelő alapítványok, kuratóriumok politikai megszállása, szenátusi jogkörök megfosztása, SZFE ellenállása*).",
                "I can deploy deontic modal structures asserting the duty of university senates to defend autonomy (*a szenátusnak kötelessége ellenállnia a politikai helytartók kinevezésének, megalkuvást nem ismerve kell őrizni a professzori önrendelkezést, nem engedhető meg az egyetemi autonómia alapítványi kisajátítása*).",
                "I can evaluate the historic blockade of the University of Theatre and Film Arts (SZFE) in 2020."
            ],
            "vocab": [
                {"lemma": "KEKVA modellváltás", "translation": "KEKVA foundation model change (public trust foundation)", "pos": "expression"},
                {"lemma": "közérdekű vagyonkezelő alapítvány", "translation": "public trust foundation", "pos": "expression"},
                {"lemma": "kuratórium", "translation": "board of trustees (stacked with politicians)", "pos": "noun"},
                {"lemma": "szenátusi autonómia", "translation": "senate autonomy", "pos": "expression"},
                {"lemma": "egyetemi privatizáció", "translation": "privatization of universities", "pos": "expression"},
                {"lemma": "SZFE blokád", "translation": "SZFE student blockade (2020)", "pos": "expression"},
                {"lemma": "politikai kinevezett", "translation": "political appointee / trustee", "pos": "expression"},
                {"lemma": "rektorválasztás szabadsága", "translation": "freedom of electing university rectors", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate the moral and institutional obligation of university senates and faculties to preserve self-governance: `az egyetemi polgárságnak szent kötelessége védelmeznie a szenátus döntési jogköreit` (it is the sacred duty of university citizens to defend senate decision-making powers), `megalkuvást nem ismerve kell elutasítani a politikai pártkatonák kuratóriumi uralmát` (one must reject the board rule of political party soldiers without compromise), `nem engedhető meg a rektorválasztás és a professzori kar alárendelése a hatalmi érdekeknek` (subordinating rector elections and faculty to power interests cannot be permitted).",
            "gr_text2": "Example: `A Színház- és Filmművészeti Egyetem polgárainak kötelessége volt szembeszállniuk az önkényes alapítványi modellel, demonstrálva a szabad alkotás sérthetetlenségét`.",
            "gr_table": [
                ["A szenátusnak kötelessége megvédenie a tanszabadság és az önkormányzatiság jogát.", "It is the duty of the senate to defend the right to academic freedom and self-governance."],
                ["Elengedhetetlen a politikusok kizárása az egyetemi kuratóriumokból.", "Excluding politicians from university boards of trustees is indispensable."],
                ["Megalkuvást nem ismerve kell ragaszkodni a demokratikus rektorválasztáshoz.", "One must stick to democratic rector elections without compromise."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-03-alapitvanyi-modellvaltas-kekva",
                "title": "Az autonómia felszámolása: A KEKVA-modell és az SZFE blokádja",
                "summary": "2020–21-ben a kormány szinte az összes magyar állami egyetemet kiszervezte politikusok által vezetett 'közérdekű vagyonkezelő alapítványokba' (KEKVA). A Színház- és Filmművészeti Egyetem (SZFE) diákjai és tanárai hónapokig tartó hősies blokáddal álltak ellen.",
                "paragraphs": [
                    {"type": "narration", "text": "Néhány hónap leforgása alatt a magyar felsőoktatás évszázados állami és közjogi struktúráját egyetlen tollvonással privatizálták. A 'modellváltásnak' álcázott folyamat során huszonegy egyetemet szerveztek ki közérdekű vagyonkezelő alapítványokba (KEKVA)."},
                    {"type": "dialogue", "speaker": "SZFE diákképviselő", "text": "A kuratóriumok élére kinevezett miniszterek és kormánypárti oligarchák megfosztották a szenátust minden érdemi jogkörétől. Kötelességünk volt ellenállni a politikai megszállásnak: a Vas utcai épületet elbarikádozva, hetvenegy napon át tartottuk a frontot a szabad művészetért."},
                    {"type": "narration", "text": "Az SZFE blokádja a huszonegyedik századi magyar diáklázadás legemlékezetesebb szimbólumává vált. Piros-fehér szalagok lepték el a fővárost, a társadalom pedig szolidaritási tüntetéseken állt ki a fiatalok mellett. A hatalom azonban könyörtelen volt: új vezetést ültetett a nyakukra, mire a legendás tanári kar testületileg felmondott."},
                    {"type": "narration", "text": "A KEKVA-modell a politikai lojalitás intézményesítését jelentette: az egyetemek autonómiáját elrabolták, a professzori kar döntési jogait pedig egy maroknyi pártkáder kezébe adták."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért jelentett súlyos csapást az egyetemi autonómiára a KEKVA alapítványi modellváltás?", [
                    "Mert a választott egyetemi szenátusokat megfosztották döntési jogköreiktől, és az egyetemek vezetését élethosszig kinevezett kormánypárti politikusok és oligarchák kuratóriumainak adták át.",
                    "Mert minden diákot arra köteleztek, hogy alapítványi kötvényeket vásároljon.",
                    "Mert az egyetemek új épületeit nem festették le időben."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Az egyetemi polgároknak alkotmányos _____ volt ellenállni a szenátusi jogkörök megcsonkításának. (duty / kötelességük)", "kötelességük", "It was the constitutional duty of university citizens to resist the curtailment of senate powers.", ["c1-modal-deontic-senate-autonomy-defense"]),
                match("vocabulary", "controlled", [
                    ["KEKVA modellváltás", "az állami egyetemek kiszervezése politikai alapítványokba"],
                    ["kuratórium", "az egyetem felett korlátlan hatalmat kapott, politikusokból álló testület"],
                    ["szenátusi autonómia", "az oktatók és diákok demokratikusan választott önkormányzati joga"],
                    ["SZFE blokád", "az egyetemi polgárság hősies ellenállása az erőszakos alapítványi átvétellel szemben"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Megalkuvást nem ismerve kell _____ az egyetemi önkormányzatiság elveit. (defend / védeni)", "védeni", "Without compromise one must defend the principles of university self-governance.", ["c1-modal-deontic-senate-autonomy-defense"]),
                sb("grammar", "practice", ["A", "szenátusnak", "kötelessége", "megvédeni", "az", "egyetemi", "autonómia", "jogait."], ["A", "szenátusnak", "kötelessége", "megvédeni", "az", "egyetemi", "autonómia", "jogait."], "It is the duty of the senate to defend the rights of university autonomy.", ["c1-modal-deontic-senate-autonomy-defense"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi oktató", "text": "Hogyan működhet tovább egy egyetem, ha a kuratórium politikai felügyelőként lép fel?"},
                    {"speaker": "Professzor", "text": "Úgy, hogy kötelességünk ragaszkodni a szakmai minőséghez, és nem engedhető meg a politikai elvárásoknak való _____."},
                    {"speaker": "Egyetemi oktató", "text": "A tudás méltósága nem lehet alku tárgya."}
                ], ["behódolás", "segítség", "öröm"], 0, ["c1-modal-deontic-senate-autonomy-defense"]),
                sw("production", [{"prompt": "Write a defense of university autonomy using a deontic modal structure.", "answer": "Az egyetemi szenátusoknak és a professzori karnak alkotmányos kötelességük megvédeni az intézményi autonómiát, és megalkuvást nem ismerve kell ellenállniuk a politikai kinevezettek önkényes kuratóriumi hatalomgyakorlásának."}], ["c1-modal-deontic-senate-autonomy-defense"]),
                mc("grammar", "check", "Melyik szerkezet fogalmazza meg a szenátusi önrendelkezés védelmét a leghatározottabban?", [
                    "kötelessége ellenállni a politikai megszállásnak / megalkuvást nem ismerve kell őrizni az önrendelkezést",
                    "jó lenne ha a kuratórium tagjai néha meglátogatnák az előadásokat",
                    "az egyetemi épületeket érdemes kifesteni a szünetben"
                ], 0, ["c1-modal-deontic-senate-autonomy-defense"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Erasmus Exclusion & European Academic Isolation",
            "grammar_title": "Proportional Correlative Structures Linking University Politicization to European Research Isolation",
            "grammar_skill": "c1-adv-proportional-academic-exclusion-isolation",
            "goals": [
                "I can analyze the European Union's exclusion of Hungarian KEKVA universities from Erasmus+ student mobility and Horizon Europe research funding (*Erasmus kizárás, Horizont Európa forrásmegvonás, összeférhetetlenség, európai elszigetelődés, agyelszívás felgyorsulása*).",
                "I can construct proportional correlative structures linking political control to international academic isolation (*minél inkább ragaszkodik a kormány a politikusok kuratóriumi tagságához, annál mélyebbre süllyed a magyar tudomány az európai elszigeteltségben*).",
                "I can evaluate brain drain and the loss of youth mobility in Central Europe."
            ],
            "vocab": [
                {"lemma": "Erasmus kizárás", "translation": "exclusion from Erasmus+ program", "pos": "expression"},
                {"lemma": "Horizont Európa", "translation": "Horizon Europe research framework program", "pos": "expression"},
                {"lemma": "összeférhetetlenség", "translation": "conflict of interest (politicians on boards)", "pos": "noun"},
                {"lemma": "nemzetközi elszigetelődés", "translation": "international academic isolation", "pos": "expression"},
                {"lemma": "agyelszívás", "translation": "brain drain / flight of human capital", "pos": "noun"},
                {"lemma": "hallgatói mobilitás", "translation": "student mobility", "pos": "expression"},
                {"lemma": "európai kutatási térség", "translation": "European Research Area (ERA)", "pos": "expression"},
                {"lemma": "pénzügyi szankció", "translation": "financial sanctions / fund freeze", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures link political university capture directly to international sanctions and professional isolation: `minél inkább bebetonozza a hatalom a pártpolitikai kádereket a kuratóriumokba, annál súlyosabb kárt szenved a hallgatói mobilitás` (the more power cements party cadres into boards, the more severe damage student mobility suffers), `amilyen mértékben szigetelődik el a magyar kutatás az uniós forrásoktól, olyan mértékben gyorsul fel az agyelszívás` (to the extent Hungarian research is isolated from EU funds, to that extent brain drain accelerates).",
            "gr_text2": "Example: `Minél makacsabbul tagadja meg a kormány az összeférhetetlenségi szabályok elfogadását, annál végzetesebb nemzetközi elszigetelődés fenyegeti a magyar egyetemeket`.",
            "gr_table": [
                ["Minél tovább késik a kuratóriumi reform, annál több diák esik el az Erasmus-ösztöndíjtól.", "The longer board reform is delayed, the more students lose Erasmus scholarships."],
                ["Amilyen mértékben zárolják a kutatási pénzeket, olyan mértékben vándorolnak el a fiatal kutatók.", "To the extent research funds are frozen, to that extent young researchers emigrate."],
                ["Minél elmélyültebb a konfliktus Brüsszellel, annál inkább lemaradunk az európai élmezőnytől.", "The deeper the conflict with Brussels, the further we fall behind the European vanguard."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-04-erasmus-kizaras-agyelszivas",
                "title": "Bezáruló kapuk: Az Erasmus-kizárás és a kutatási karantén",
                "summary": "2022 végén az Európai Tanács felfüggesztette a KEKVA alapítványi egyetemek részvételét az Erasmus+ és a Horizont Európa programokban a politikusok összeférhetetlensége miatt. A magyar diákok és kutatók tízezrei váltak a politikai makacsság túszaivá.",
                "paragraphs": [
                    {"type": "narration", "text": "2022 decemberében hidegzuhanyként érte a magyar egyetemi világot az Európai Tanács határozata: az uniós döntéshozók kizárták a modellváltó, alapítványi fenntartású magyar egyetemeket az Erasmus+ csereprogramokból és a Horizont Európa kutatási keretprogramból."},
                    {"type": "dialogue", "speaker": "Fiatal kutató", "text": "Az ok a legnyilvánvalóbb összeférhetetlenség volt: az egyetemeket felügyelő kuratóriumokban hivatalban lévő miniszterek és államtitkárok ültek, akik saját maguknak osztottak milliós juttatásokat és döntöttek közpénzekről. Minél tovább halogatja a kormány a politikusok visszahívását, annál tragikusabb elszigetelődésbe taszítja a jövőnket."},
                    {"type": "narration", "text": "A szankciók közvetlenül sújtották a magyar egyetemisták tízezreit, akiktől elvették a külföldi tanulás és tapasztalatszerzés esélyét. A kutatócsoportok nemzetközi konzorciumokból estek ki, mert a nyugati egyetemek kockázatosnak tartották a magyar partnerek bevonását."},
                    {"type": "narration", "text": "Az agyelszívás drámai módon felgyorsult: a legtehetségesebb fiatal oktatók és doktoranduszok tömegesen hagyták el az országot, bizonyítva, hogy a politikai hatalomvágyért a nemzet legértékesebb szellemi tőkéjével kell fizetni."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért függesztette fel az Európai Unió a magyar alapítványi egyetemek Erasmus+ és Horizont Európa forrásait?", [
                    "Mert a kuratóriumokban ülő aktív kormánypárti politikusok jelenléte súlyos összeférhetetlenséget és korrupciós kockázatot jelentett, sértve az uniós költségvetés védelmét és az egyetemi autonómiát.",
                    "Mert a magyar diákok túl jó jegyeket szereztek a külföldi egyetemeken.",
                    "Mert lejárt a magyar diákok útlevele."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Minél tovább tart a politikai összeférhetetlenség, _____ súlyosabb elszigetelődés vár a kutatókra. (the / annál)", "annál", "The longer political conflict of interest lasts, the more severe isolation awaits researchers.", ["c1-adv-proportional-academic-exclusion-isolation"]),
                match("vocabulary", "controlled", [
                    ["Erasmus kizárás", "a magyar diákok eltiltása az uniós csereprogramoktól"],
                    ["Horizont Európa", "a világ legnagyobb nemzetközi tudományos kutatási programja"],
                    ["összeférhetetlenség", "politikai tisztség és egyetemi kuratóriumi tagság tiltott egybeesése"],
                    ["agyelszívás", "a legkiválóbb fiatal tudósok elvándorlása a kilátástalanság miatt"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben kiesünk a nemzetközi hálózatokból, _____ mértékben növekszik a tudományos lemaradásunk. (such / olyan)", "olyan", "To such an extent as we drop out of international networks, to that extent our scientific lag increases.", ["c1-adv-proportional-academic-exclusion-isolation"]),
                sb("grammar", "practice", ["Minél", "mélyebb", "az", "elszigetelődés,", "annál", "gyorsabb", "az", "agyelszívás."], ["Minél", "mélyebb", "az", "elszigetelődés,", "annál", "gyorsabb", "az", "agyelszívás."], "The deeper the isolation, the faster the brain drain.", ["c1-adv-proportional-academic-exclusion-isolation"]),
                dc("dialogue", [
                    {"speaker": "Egyetemista", "text": "Hogyan befolyásolja az Erasmus-kizárás a magyar diplomák nemzetközi értékét?"},
                    {"speaker": "Oktatáskutató", "text": "Úgy, hogy minél tovább rekedünk kívül az európai kutatási téren, annál drámaibb mértékben csökken az intézményeink _____."},
                    {"speaker": "Egyetemista", "text": "A diákoknak nem szabad feladniuk a harcot."}
                ], ["hitele", "mérete", "ára"], 0, ["c1-adv-proportional-academic-exclusion-isolation"]),
                sw("production", [{"prompt": "Write a proportional sentence linking politicization to academic isolation.", "answer": "Minél makacsabbul tagadja meg a kormány az összeférhetetlenség felszámolását és a valódi autonómia visszaállítását, annál mélyebbre süllyed a magyar felsőoktatás az európai elszigeteltségben és annál pusztítóbbá válik az agyelszívás."}], ["c1-adv-proportional-academic-exclusion-isolation"]),
                mc("grammar", "check", "Melyik páros kötőszó fejezi ki a politikai beavatkozás és a tudományos veszteség arányát?", [
                    "minél makacsabb a politikai önkény, annál súlyosabbá válik a nemzetközi elszigetelődés",
                    "bár esik az eső, mégis bemegyünk az egyetemre",
                    "vagy a diák tanul vagy a könyvtárban olvas"
                ], 0, ["c1-adv-proportional-academic-exclusion-isolation"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Academic Freedom as a Democratic Imperative",
            "grammar_title": "Evaluative Conclusive Particles Declaring Foundational Necessity of Academic Freedom",
            "grammar_skill": "c1-adv-conclusive-epistemic-freedom",
            "goals": [
                "I can analyze the democratic and constitutional necessity of academic freedom, institutional restitution, and scientific dignity (*tudományos szabadság, tanszabadság, akadémiai helyreállítás, a tudás köztársasága, európai integráció*).",
                "I can deploy conclusive evaluative particles articulating the indispensability of intellectual freedom (*értelemszerűen nélkülözhetetlen, fundamentálisan megkérdőjelezhetetlen, kétséget kizáróan létfontosságú, végső soron elidegeníthetetlen*).",
                "I can debate the long-term conditions for scientific renewal in democratic Central Europe."
            ],
            "vocab": [
                {"lemma": "tudományos szabadság", "translation": "scientific / academic freedom", "pos": "expression"},
                {"lemma": "tanszabadság", "translation": "freedom of teaching and learning", "pos": "noun"},
                {"lemma": "akadémiai helyreállítás", "translation": "restitution of academic institutions", "pos": "expression"},
                {"lemma": "a tudás köztársasága", "translation": "republic of knowledge / letters", "pos": "expression"},
                {"lemma": "európai integráció", "translation": "European academic integration", "pos": "expression"},
                {"lemma": "tudományos méltóság", "translation": "scientific dignity / integrity", "pos": "expression"},
                {"lemma": "demokratikus imperatívusz", "translation": "democratic imperative", "pos": "expression"},
                {"lemma": "jövő záloga", "translation": "guarantee of the future", "pos": "expression"}
            ],
            "gr_text1": "Conclusive evaluative particles assert the absolute, non-negotiable nature of academic freedom for the survival of democracy and progress: `értelemszerűen nélkülözhetetlen a tanszabadság teljes körű visszaállítása` (fully restoring freedom of teaching is naturally indispensable), `fundamentálisan megkérdőjelezhetetlen a kutatói autonómia prioritása` (the priority of researcher autonomy is fundamentally unquestionable), `végső soron elidegeníthetetlen a nemzet joga a független tudományhoz` (ultimately the nation's right to independent science is inalienable).",
            "gr_text2": "Example: `A történelem megkérdőjelezhetetlenül igazolja: a tudományos szabadság nem politikai kegy, hanem értelemszerűen nélkülözhetetlen és fundamentálisan megkérdőjelezhetetlen demokratikus alapérték`.",
            "gr_table": [
                ["A kutatás szabadsága értelemszerűen nélkülözhetetlen a nemzet felemelkedéséhez.", "Freedom of research is naturally indispensable for the nation's advancement."],
                ["Az egyetemi autonómia fundamentálisan megkérdőjelezhetetlen európai norma.", "University autonomy is a fundamentally unquestionable European norm."],
                ["Végső soron elidegeníthetetlen a tudósok joga az önálló kutatómunkához.", "Ultimately the right of scientists to independent research work is inalienable."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-05-tudomanyos-autonomia-jovo",
                "title": "A szellem nem rab: A tudományos autonómia helyreállítása",
                "summary": "A magyar tudományos és egyetemi közösség helytállása bizonyítja: a kutatás szabadságát nem lehet örökre politikai pórázra fogni. A jövő záloga az MTA intézményeinek visszaadása, a KEKVA-modell lebontása és az európai nyitottság.",
                "paragraphs": [
                    {"type": "narration", "text": "Az elmúlt évtized brutális politikai beavatkozásai – az MTA kutatóintézeteinek elcsatolása, a CEU elüldözése, az egyetemek oligarchikus privatizációja és az Erasmus-kizárás – mély sebeket ejtettek a magyar tudományosságon. A szellemi autonómia lángja azonban nem aludt ki."},
                    {"type": "dialogue", "speaker": "Akadémikus", "text": "Fundamentálisan megkérdőjelezhetetlen igazság, hogy a tudomány csak a szabadság levegőjében képes lélegezni. Értelemszerűen nélkülözhetetlen a kutatóintézetek visszaadása a tudósok közösségének, a pártpolitikai kuratóriumok felszámolása és a tanszabadság maradéktalan helyreállítása."},
                    {"type": "narration", "text": "Ahogyan Polányi Mihály tanította: a tudomány köztársasága nem hódolhat be semmilyen földi hatalomnak. A magyar kutatók és diákok bátor helytállása megteremtette az erkölcsi alapot ahhoz, hogy Magyarország visszatérhessen az európai szellemi élvonalba."},
                    {"type": "narration", "text": "A jövő a szabad, kritikus és független tudásé. A politikai rendszerek múlandóak, de a tudományos igazság és az emberi szabadság keresése az örökkévalóság része marad."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinthető a tudományos autonómia demokratikus imperatívusznak egy modern társadalomban?", [
                    "Mert a politikai és gazdasági nyomástól mentes, független kutatás és oktatás nélkül a társadalom elveszíti a valóság megismerésének és a kritikai gondolkodásnak a képességét, kiszolgáltatva magát az autoriter propagandának.",
                    "Mert a professzoroknak több szabadság jár nyáron, mint más dolgozóknak.",
                    "Mert a laboratóriumi kísérletek túl sok áramot fogyasztanak."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A tudományos kutatás autonómiája értelemszerűen _____ a társadalmi haladáshoz. (indispensable / nélkülözhetetlen)", "nélkülözhetetlen", "The autonomy of scientific research is naturally indispensable for social progress.", ["c1-adv-conclusive-epistemic-freedom"]),
                match("vocabulary", "controlled", [
                    ["tudományos szabadság", "a politikai utasításoktól mentes kutatás alkotmányos alapjoga"],
                    ["tanszabadság", "a professzorok és diákok joga a szabad tanulásra és tanításra"],
                    ["a tudás köztársasága", "az önigazgató és demokratikus nemzetközi tudósközösség eszménye"],
                    ["jövő záloga", "a nemzet felemelkedésének elengedhetetlen garanciája"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A kutatói függetlenség prioritása fundamentálisan _____ alapérték. (unquestionable / megkérdőjelezhetetlen)", "megkérdőjelezhetetlen", "The priority of researcher independence is a fundamentally unquestionable core value.", ["c1-adv-conclusive-epistemic-freedom"]),
                sb("grammar", "practice", ["A", "tudományos", "szabadság", "értelemszerűen", "nélkülözhetetlen", "minden", "demokráciában."], ["A", "tudományos", "szabadság", "értelemszerűen", "nélkülözhetetlen", "minden", "demokráciában."], "Scientific freedom is naturally indispensable in every democracy.", ["c1-adv-conclusive-epistemic-freedom"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi rektor", "text": "Hogyan nyerheti vissza a magyar felsőoktatás az elveszített nemzetközi megbecsülést?"},
                    {"speaker": "Akadémikus", "text": "Úgy, hogy végső soron elidegeníthetetlen a tanszabadság joga, és fundamentálisan megkérdőjelezhetetlen az intézményi önkormányzatiság _____."},
                    {"speaker": "Egyetemi rektor", "text": "A tudomány szabadsága nem lehet politikai alku tárgya."}
                ], ["helyreállítása", "megvonása", "feledése"], 0, ["c1-adv-conclusive-epistemic-freedom"]),
                sw("production", [{"prompt": "Write a conclusive synthesis on the necessity of academic freedom using an evaluative particle.", "answer": "A tudományos szabadság és az egyetemi autonómia értelemszerűen nélkülözhetetlen és fundamentálisan megkérdőjelezhetetlen, hiszen a politikai beavatkozás elsorvasztja az innovációt, de a független kutatás a nemzeti megmaradás egyetlen szilárd fundamentuma."}], ["c1-adv-conclusive-epistemic-freedom"]),
                mc("grammar", "check", "Melyik konkluzív kifejezés szintetizálja a tudományos szabadság helyreállítását a legerőteljesebben?", [
                    "értelemszerűen nélkülözhetetlen / fundamentálisan megkérdőjelezhetetlen / végső soron elidegeníthetetlen",
                    "reméljük a tudósok sokat dolgoznak majd a jövőben",
                    "jó lenne ha minden diák kapna egy új könyvet"
                ], 0, ["c1-adv-conclusive-epistemic-freedom"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(34, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-tudomanyos-autonomia-ceu.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "A tudományos szabadság küzdelme és az egyetemi autonómia Magyarországon",
            "level": "C1",
            "lesson": 5,
            "order": 34,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-epistemic-freedom"],
            "summary": "Átfogó krónika a magyar tudományos élet és felsőoktatás elleni politikai offenzíváról: az MTA kutatóintézeteinek 2019-es elcsatolásáról, a Közép-európai Egyetem (CEU) Lex CEU általi elüldözéséről, a KEKVA alapítványi modellváltásról és az SZFE blokádjáról, az Erasmus-kizárásról és nemzetközi elszigetelődésről, valamint az akadémiai szabadság helyreállításának küzdelméről.",
            "vocabularyTopics": [
                "The Stripping of MTA Research Institutes & The CEU Expulsion",
                "Academic Freedom as a Democratic Imperative"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A 2010 utáni évtizedben a magyar szellemi élet legfüggetlenebb bástyája, az akadémiai és egyetemi szféra a tekintélyelvű államhatalom frontális támadásának célpontjává vált. A kétharmados kormányzat szisztematikus lépések sorozatával kísérelte meg a független kutatás és oktatás felszámolását, helyébe a politikai klientúra-rendszert és a központosított felügyeletet állítva."},
                {"type": "narration", "text": "A folyamat legbrutálisabb állomása a Lex CEU volt: 2017-ben a kormányzat példátlan módon, diszkriminatív jogszabályokkal elüldözte a világhírű Közép-európai Egyetemet Budapestről, hatalmas nemzetközi tiltakozást és tüntetéshullámot váltva ki. Két évvel később az MTA közel kétszáz éves, tizenötezer fős kutatóhálózatát szakították el az Akadémiától erőszakkal és forrásmegvonási zsarolással."},
                {"type": "narration", "text": "Ezt követte a magyar állami felsőoktatás privatizációja: huszonegy egyetemet szerveztek ki kormánypárti politikusok által uralt KEKVA alapítványokba, felszámolva a választott szenátusok jogköreit. A Színház- és Filmművészeti Egyetem (SZFE) polgársága hősies, hónapokig tartó barikádokkal állt ellen a megszállásnak, a szabadság örök szimbólumává emelve a Vas utcát."},
                {"type": "narration", "text": "A politikai önkény azonban súlyos nemzetközi árat követelt: az Európai Unió kizárta az alapítványi egyetemeket az Erasmus+ csereprogramokból és a Horizont Európa kutatási forrásokból, nemzetközi karanténba taszítva a magyar diákokat és felgyorsítva a tehetségek tömeges agyelszívását."},
                {"type": "narration", "text": "Polányi Mihály tanítása azonban ma is útmutató: a tudomány köztársasága nem rab. A tudományos autonómia és a tanszabadság helyreállítása fundamentálisan megkérdőjelezhetetlen, hiszen szabad szellem nélkül egyetlen nemzet sem építhet sikeres, modern és demokratikus jövőt."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        34,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can master the critical discourse of academic asset stripping, university exile, and foundation capture.",
            "I can employ discourse markers of institutional takeover, critical evaluative adverbials, and deontic modal structures of academic defense.",
            "I can construct proportional correlative structures and conclusive evaluative syntheses on academic freedom."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés diagnosztizálja az akadémiai vagyonelvonást a legpontosabban?", [
                "az akadémiai autonómia elleni merényletként értékelve / a kutatóhálózat politikai einstandolásaként aposztrofálva",
                "hogyha új kísérleteket végeznek a laborban",
                "amikor a minisztérium új levelet küld postán"
            ], 0, ["c1-discourse-academic-asset-stripping-framing"]),
            mc("grammar", "recognize", "Milyen szerkezettel leplezhető le az egyetemek politikai alapítványosítása a leghitelesebben?", [
                "a szenátusi jogköröket önkényesen felszámolva és pártpolitikai kuratóriumokat ültetve a vezetésbe",
                "egy szép beszédet mondva a diplomaosztó ünnepségen",
                "amikor új kollégiumot építenek a városban"
            ], 0, ["c1-adv-academic-expulsion-critique"]),
            match("vocabulary", "recognize", [
                ["MTA kutatóhálózat", "a magyar tudomány 2019-ben elrabolt történelmi hálózata"],
                ["Lex CEU", "a Közép-európai Egyetemet elüldöző diszkriminatív jogszabály"],
                ["KEKVA modellváltás", "az egyetemek kiszervezése politikusok által uralt alapítványokba"],
                ["Erasmus kizárás", "a hallgatói mobilitás ellehetetlenülése az összeférhetetlenség miatt"]
            ], [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A kutatók tömeges elvándorlása a határokon túlra az _____ tragikus következménye. (brain drain / agyelszívás)", "agyelszívás", "Mass emigration of researchers abroad is the tragic consequence of brain drain.", [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A kutatás és oktatás szabadsága a sérthetetlen _____ alapelve. (academic freedom / tanszabadság)", "tanszabadság", "Freedom of research and teaching is the foundational principle of inviolable academic freedom.", [f"c1-{slug}-vocab"]),
            fb("grammar", "recall", "A döntést politikai einstandként _____ az akadémikusok tiltakoztak. (characterizing / aposztrofálva)", "aposztrofálva", "Characterizing the decision as hostile political takeover academics protested.", ["c1-discourse-academic-asset-stripping-framing"]),
            fb("grammar", "context", "Minél tovább tart az összeférhetetlenség, _____ mélyebb a nemzetközi elszigetelődés. (the / annál)", "annál", "The longer conflict of interest lasts, the deeper international isolation is.", ["c1-adv-proportional-academic-exclusion-isolation"]),
            fb("grammar", "context", "A kutatás szabadsága értelemszerűen _____ a demokráciában. (indispensable / nélkülözhetetlen)", "nélkülözhetetlen", "Freedom of research is naturally indispensable in a democracy.", ["c1-adv-conclusive-epistemic-freedom"]),
            mc("grammar", "context", "Mi az egyetemi szenátusok és oktatók legfőbb etikai kötelessége az alapítványi önkénnyel szemben?", [
                "A tanszabadság megingathatatlan védelme, a professzori autonómia őrzése és a politikai megrendelések elutasítása.",
                "A kormánypárti politikusok azonnali kinevezése díszpolgárrá.",
                "A nemzetközi kapcsolatok önkéntes megszakítása."
            ], 0, ["c1-modal-deontic-senate-autonomy-defense"]),
            sb("grammar", "produce", ["A", "tudományos", "szabadság", "fundamentálisan", "megkérdőjelezhetetlen", "minden", "szabad", "országban."], ["A", "tudományos", "szabadság", "fundamentálisan", "megkérdőjelezhetetlen", "minden", "szabad", "országban."], "Scientific freedom is fundamentally unquestionable in every free country.", ["c1-adv-conclusive-epistemic-freedom"]),
            sw("production", [{"prompt": "Write a critical evaluation of university isolation using a proportional correlative structure.", "answer": "Minél inkább ragaszkodik a politikai hatalom az egyetemek oligarchikus ellenőrzéséhez, annál elkerülhetetlenebbé válik a nemzetközi források zárolása és annál pusztítóbb agyelszívással kell szembenéznie a nemzetnek."}], ["c1-adv-proportional-academic-exclusion-isolation"]),
            sw("production", [{"prompt": "Synthesize the necessity of academic restitution using a conclusive evaluative particle.", "answer": "Az akadémiai autonómia és a tanszabadság helyreállítása értelemszerűen nélkülözhetetlen és fundamentálisan megkérdőjelezhetetlen, hiszen a tudás köztársasága nem rab, s a független kutatás a demokratikus Magyarország legfőbb záloga."}], ["c1-adv-conclusive-epistemic-freedom"])
        ]
    )

    print("=== Finished C1 Unit 34 ===")


if __name__ == "__main__":
    generate_unit_34()
