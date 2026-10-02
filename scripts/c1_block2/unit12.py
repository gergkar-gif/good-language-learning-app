#!/usr/bin/env python3
"""
Hungarian C1 Block 2 - Unit 12 Generator:
  - Track 1 (Core): Unit 12 — "Civic Resistance, Dissent & Legal Philosophy" (c1-12)
  - Track 2 (Discourse): Unit 12 — "Civil Disobedience & Democratic Checks" (c1-polgariengedetlenseg)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block2.registry_helper import register_unit


def generate_unit_12():
    print("=== Generating C1 Unit 12 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-12-vocab": {"kind": "vocabulary"},
        "c1-polgariengedetlenseg-vocab": {"kind": "vocabulary"},
        "c1-subjunctive-concessives": {"kind": "grammar"},
        "c1-ethical-stance-markers": {"kind": "grammar"},
        "c1-radbruch-formula-syntax": {"kind": "grammar"},
        "c1-legitimacy-vs-legality": {"kind": "grammar"},
        "c1-dissent-deliberation": {"kind": "grammar"},
    }
    new_titles = {
        "c1-12-vocab": "reading",
        "c1-polgariengedetlenseg-vocab": "reading",
        "c1-subjunctive-concessives": "subjunctive concessive clauses with indefinite pronouns",
        "c1-ethical-stance-markers": "ethical stance markers and conscience-based legal justification",
        "c1-radbruch-formula-syntax": "statutory injustice and supra-statutory law legal phrasing",
        "c1-legitimacy-vs-legality": "tensions between democratic legitimacy and formal positive legality",
        "c1-dissent-deliberation": "dissenting opinions and public justification in constitutional deliberation",
    }
    
    core_title = "Civic Resistance, Dissent & Legal Philosophy"
    core_stems = [f"c1-12-0{i}" for i in range(1, 6)] + ["c1-12-consolidation"]
    disc_title = "Civil Disobedience & Democratic Checks"
    disc_stems = [f"c1-polgariengedetlenseg-0{i}" for i in range(1, 6)] + ["c1-polgariengedetlenseg-consolidation"]
    
    register_unit(12, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-12)
    # ----------------------------------------------------
    core_intro = [
        "Hungarian discourse surrounding civic resistance, dissent, and legal philosophy bridges jurisprudence with moral philosophy, utilizing concessive subjunctive syntax (történjék bármi; döntsön bárhogy a hatalom), ethical stance adverbials (lelkiismereti meggyőződésből fakadóan), and the classic jurisprudence of supra-statutory law.",
        "In this capstone unit of Block 2, anchored by György Konrád's landmark philosophical work 'Az autonómia kísértése' (Antipolitics / The Temptation of Autonomy, 1980), you will dissect the vocabulary and syntax of passive resistance, civil disobedience, and conscientious objection."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-12-01",
            "title": "Subjunctive Concessive Clauses with Indefinite Pronouns",
            "grammar_title": "Concessive Subjunctive Structures in Civic Defiance",
            "grammar_skill": "c1-subjunctive-concessives",
            "goals": [
                "I can form inverted subjunctive concessive clauses (*történjék bármi, hozzon a hatalom bármilyen rendeletet*).",
                "I can deploy vocabulary of non-compliance and resistance (*passzív rezisztencia, megingathatatlan*).",
                "I can express unconditional ethical defiance in formal C1 Hungarian."
            ],
            "vocab": [
                {"lemma": "engedetlenség", "translation": "disobedience, non-compliance", "pos": "noun"},
                {"lemma": "passzív rezisztencia", "translation": "passive resistance", "pos": "expression"},
                {"lemma": "történjék", "translation": "may it happen, happen what may (formal subjunctive)", "pos": "verb"},
                {"lemma": "megingathatatlan", "translation": "unshakeable, steadfast", "pos": "adjective"},
                {"lemma": "kikényszeríthetetlen", "translation": "unenforceable", "pos": "adjective"},
                {"lemma": "szembeszegül", "translation": "to defy, stand up against, resist", "pos": "verb"},
                {"lemma": "dacol", "translation": "to brave, defy, flout", "pos": "verb"},
                {"lemma": "önkény", "translation": "arbitrariness, despotism, autocracy", "pos": "noun"}
            ],
            "gr_text1": "In elevated Hungarian rhetoric, indefinite concessive clauses expressing unconditional defiance employ the subjunctive-imperative verbal mood (`-j-` suffix) inverted or followed by relative pronouns: `Bármit mondjon is a törvény...` (Whatever the law may say...), `Történjék bármi...` (Happen what may...).",
            "gr_text2": "Notice the alternative literary word order with `bár`: `hozzon bár a hatalom új rendeleteket...` (though the regime enact new decrees...). These structures emphasize that moral integrity supersedes arbitrary positive laws.",
            "gr_table": [
                ["Történjék bármi, a polgárok nem hátrálnak meg.", "Happen what may, citizens do not back down."],
                ["Bármilyen megtorlással fenyegessen is a hatalom...", "However severe reprisals the regime may threaten with..."],
                ["Hozzon bár az önkény új törvényeket, azok morálisan érvénytelenek.", "Though autocracy enact new laws, they are morally invalid."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'passzív rezisztencia' fogalma a magyar politikai eszmetörténetben?", ["Erőszakmentes ellenállást, az önkénnyel való együttműködés és adófizetés megtagadását.", "Fegyveres felkelést.", "A törvények azonnali és lelkes elfogadását."], 0, ["c1-12-vocab"]),
                fb("grammar", "controlled", "Történjék _____, a lelkiismereti ellenállás erkölcsi kötelesség marad. (whatever / bármi)", "bármi", "Whatever may happen, conscientious resistance remains a moral imperative.", ["c1-subjunctive-concessives"]),
                match("vocabulary", "controlled", [["engedetlenség", "non-compliance"], ["önkény", "autocracy, arbitrariness"], ["szembeszegül", "to defy, resist"], ["megingathatatlan", "steadfast, unshakeable"]], ["c1-12-vocab"]),
                fb("grammar", "practice", "Bármilyen büntetéssel _____ is a hatalom, a polgárok nem adják fel elveiket. (threaten / fenyegessen)", "fenyegessen", "However severely the power may threaten with punishment, citizens do not surrender their principles.", ["c1-subjunctive-concessives"]),
                sb("grammar", "practice", ["Hozzon", "bár", "az", "önkényuralom", "új", "törvényeket,", "azok", "morálisan", "érvénytelenek."], ["Hozzon", "bár", "az", "önkényuralom", "új", "törvényeket,", "azok", "morálisan", "érvénytelenek."], "Though despotism enact new laws, they are morally invalid.", ["c1-subjunctive-concessives"]),
                dc("dialogue", [
                    {"speaker": "Polgár", "text": "Nem tartasz a bírósági eljárástól és a pénzbírságtól?"},
                    {"speaker": "Aktivista", "text": "Bármilyen szankcióval sújtsanak is, a szolidaritás hálózata _____ marad."},
                ], ["megingathatatlan", "titkos", "elveszett"], 0, ["c1-subjunctive-concessives"]),
                sw("production", [{"prompt": "Write a sentence declaring moral non-compliance using 'Történjék bármi...'.", "answer": "Történjék bármi, a lelkiismereti meggyőződésből fakadó békés tiltakozást egyetlen önkényuralmi rendelet sem törheti meg."}], ["c1-subjunctive-concessives"]),
                mc("grammar", "check", "Melyik mondat alkalmazza helyesen a kötőmódos megengedő szerkezetet?", [
                    "Bármilyen nyomást gyakoroljon is a kormányzat, a bírói függetlenség megkérdőjelezhetetlen.",
                    "Bármilyen nyomást gyakorol a kormányzat, a bírói függetlenség megkérdőjeleződik.",
                    "Ha nyomást gyakorolna, a bírói függetlenség elesne."
                ], 0, ["c1-subjunctive-concessives"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-12-02",
            "title": "Ethical Stance Markers & Conscience-Based Formulations",
            "grammar_title": "Conscience Adverbials & Normative Stance Framing",
            "grammar_skill": "c1-ethical-stance-markers",
            "goals": [
                "I can frame conscientious objection (*lelkiismereti okból fakadóan, meggyőződéstől vezérelve*).",
                "I can formulate ethical arguments based on human dignity (*emberi méltóságra hivatkozva*).",
                "I can distinguish between pragmatic disobedience and principled non-compliance."
            ],
            "vocab": [
                {"lemma": "lelkiismereti ok", "translation": "conscientious reason", "pos": "noun"},
                {"lemma": "meggyőződés", "translation": "conviction, persuasion", "pos": "noun"},
                {"lemma": "morális imperatívusz", "translation": "moral imperative", "pos": "noun"},
                {"lemma": "elvvitathatatlan", "translation": "indisputable, uncontestable", "pos": "adjective"},
                {"lemma": "együttműködés megtagadása", "translation": "refusal of collaboration/compliance", "pos": "expression"},
                {"lemma": "méltányosság", "translation": "equity, fairness, reasonableness", "pos": "noun"},
                {"lemma": "belső szabadság", "translation": "inner freedom, internal autonomy", "pos": "noun"},
                {"lemma": "hivatkozásképpen", "translation": "by way of reference", "pos": "adverb"}
            ],
            "gr_text1": "Ethical dissent in legal contexts requires explicit stance framing markers using ablative, causal-final, and essive-formal postpositions or suffixes: `lelkiismereti okból fakadóan` (stemming from conscientious grounds), `morális meggyőződéstől vezérelve` (guided by moral conviction).",
            "gr_text2": "Participle phrases such as `a méltányosság elvére hivatkozva` (citing the principle of equity) or `belső szabadságának megőrzése végett` ground non-compliance in higher-order moral imperatives.",
            "gr_table": [
                ["Lelkiismereti meggyőződésüktől vezérelve tagadták meg az utasítást.", "Guided by conscientious conviction they refused the order."],
                ["Az emberi méltóság védelmére hivatkozva léptek fel.", "Citing the defense of human dignity they stepped forward."],
                ["Belső szabadságának megőrzése végett nem működött együtt.", "For the sake of preserving inner freedom he did not cooperate."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan indokolja a jogfilozófia a 'lelkiismereti okból fakadó' engedetlenséget?", ["Olyan mély erkölcsi meggyőződéssel, amely tiltja az igazságtalan törvény betartását.", "Gazdasági haszonszerzéssel.", "Hanyagsággal vagy figyelmetlenséggel."], 0, ["c1-12-vocab"]),
                fb("grammar", "controlled", "A katonai szolgálatot mélységes lelkiismereti _____ fakadóan tagadta meg. (reason / okból)", "okból", "He refused military service stemming from profound conscientious grounds.", ["c1-ethical-stance-markers"]),
                match("vocabulary", "controlled", [["morális imperatívusz", "moral imperative"], ["elvvitathatatlan", "indisputable"], ["méltányosság", "equity, fairness"], ["belső szabadság", "inner freedom"]], ["c1-12-vocab"]),
                fb("grammar", "practice", "A tiltakozók az emberi méltóság elvére _____ tagadták meg az aláírást. (citing / hivatkozva)", "hivatkozva", "The protesters refused the signature citing the principle of human dignity.", ["c1-ethical-stance-markers"]),
                sb("grammar", "practice", ["Az", "emberi", "méltóság", "védelmére", "hivatkozva", "választották", "az", "együttműködés", "megtagadását."], ["Az", "emberi", "méltóság", "védelmére", "hivatkozva", "választották", "az", "együttműködés", "megtagadását."], "Citing the defense of human dignity they chose the refusal of cooperation.", ["c1-ethical-stance-markers"]),
                dc("dialogue", [
                    {"speaker": "Vizsgáló", "text": "Miért nem hajtja végre a felettese által kiadott utasítást?"},
                    {"speaker": "Tisztviselő", "text": "Mert az nyíltan jogsértő, és én erkölcsi _____ vezérelve nem lehetek bűnrészes."},
                ], ["meggyőződésemtől", "fizetésemtől", "kedvemtől"], 0, ["c1-ethical-stance-markers"]),
                sw("production", [{"prompt": "Formulate a statement of conscientious objection using 'lelkiismereti meggyőződéstől vezérelve'.", "answer": "A polgárok lelkiismereti meggyőződésüktől vezérelve elutasították a diktatórikus rendszerrel való együttműködést, vállalva a meghurcoltatást."}], ["c1-ethical-stance-markers"]),
                mc("grammar", "check", "Melyik kifejezés illik leginkább a választékos jogi állásfoglalásba?", [
                    "mélységes lelkiismereti meggyőződéstől vezérelve",
                    "mert éppen nem volt kedve hozzá",
                    "csak azért sem csinálva meg a dolgot"
                ], 0, ["c1-ethical-stance-markers"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-12-03",
            "title": "The Radbruch Formula & Statutory Injustice",
            "grammar_title": "Legal Philosophy Terminology: Törvényes Jogtalanság",
            "grammar_skill": "c1-radbruch-formula-syntax",
            "goals": [
                "I can analyze Gustav Radbruch's formula (*törvényes jogtalanság, törvény feletti jog*).",
                "I can evaluate the tension between formal legality and substantive justice (*elviselhetetlen igazságtalanság*).",
                "I can discuss crimes against humanity and imprescriptibility (*elévülhetetlenség*)."
            ],
            "vocab": [
                {"lemma": "törvényes jogtalanság", "translation": "statutory injustice, legal unlawfulness", "pos": "expression"},
                {"lemma": "törvény feletti jog", "translation": "supra-statutory law, natural law", "pos": "expression"},
                {"lemma": "elévülhetetlen", "translation": "imprescriptible, not subject to statute of limitations", "pos": "adjective"},
                {"lemma": "érvénytelenség", "translation": "invalidity, nullity", "pos": "noun"},
                {"lemma": "pozitív jog", "translation": "positive law (enacted statutes)", "pos": "noun"},
                {"lemma": "természetjog", "translation": "natural law", "pos": "noun"},
                {"lemma": "igazságossághiány", "translation": "deficit of justice, gross unjustness", "pos": "noun"},
                {"lemma": "jogfosztás", "translation": "disenfranchisement, deprivation of rights", "pos": "noun"}
            ],
            "gr_text1": "Gustav Radbruch's legal formula (Radbruch-formula) forms the core of European post-totalitarian legal philosophy: when a positive statutory law conflicts with elementary justice to an intolerable degree, it ceases to be law (`elviselhetetlen mértékű igazságtalanság esetén a törvény elveszíti jogi jellegét`).",
            "gr_text2": "Syntactically, this uses complex contrastive concessives and privative predicate nominals: `bár formailag érvényes, mégis lényegileg törvényes jogtalanság` (although formally valid, it is essentially statutory injustice).",
            "gr_table": [
                ["Ahol a pozitív jog és az igazságosság ellentmondása elviselhetetlenné válik...", "Where the contradiction between positive law and justice becomes intolerable..."],
                ["A szélsőségesen igazságtalan törvény nem minősül jognak.", "An extremely unjust law does not qualify as law."],
                ["A törvényes jogtalanság elve kizárja a jogfosztó jogszabályok védelmét.", "The principle of statutory injustice excludes protection of disenfranchising statutes."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a Radbruch-formula alapvető tézise?", ["Hogy a kirívóan és elviselhetetlenül igazságtalan törvény elveszíti jogi érvényét mint törvényes jogtalanság.", "Hogy minden törvény szent és sérthetetlen.", "Hogy a bíróságoknak nem szabad gondolkodniuk."], 0, ["c1-12-vocab"]),
                fb("grammar", "controlled", "A nürnbergi perekben kimondták, hogy a faji törvények formailag léteztek ugyan, de lényegüket tekintve törvényes _____ minősültek. (injustice / jogtalanságnak)", "jogtalanságnak", "In the Nuremberg trials it was held that racial statutes existed formally, but in essence constituted statutory injustice.", ["c1-radbruch-formula-syntax"]),
                match("vocabulary", "controlled", [["törvényes jogtalanság", "statutory injustice"], ["törvény feletti jog", "supra-statutory law"], ["pozitív jog", "positive enacted law"], ["elévülhetetlen", "imprescriptible"]], ["c1-12-vocab"]),
                fb("grammar", "practice", "Az emberiesség elleni bűncselekmények büntethetősége nemzetközi jogilag _____, így soha nem évül el. (imprescriptible / elévülhetetlen)", "elévülhetetlen", "The prosecutability of crimes against humanity is internationally imprescriptible, thus never expires.", ["c1-radbruch-formula-syntax"]),
                sb("grammar", "practice", ["A", "törvényes", "jogtalanság", "fogalma", "a", "természetjog", "újjáéledését", "jelentette", "Európában."], ["A", "törvényes", "jogtalanság", "fogalma", "a", "természetjog", "újjáéledését", "jelentette", "Európában."], "The concept of statutory injustice signaled the revival of natural law in Europe.", ["c1-radbruch-formula-syntax"]),
                dc("dialogue", [
                    {"speaker": "Joghallgató", "text": "Hivatkozhat-e a vádlott arra, hogy csupán az akkori törvényeket hajtotta végre?"},
                    {"speaker": "Professzor", "text": "Nem, mert az elviselhetetlen igazságtalanság esetén a jogszabály elveszíti _____ jellegét."},
                ], ["jogi", "gazdasági", "katonai"], 0, ["c1-radbruch-formula-syntax"]),
                sw("production", [{"prompt": "Summarize the Radbruch formula in one compound legal sentence.", "answer": "A Radbruch-formula értelmében amennyiben a pozitív jog és az igazságosság konfliktusa elviselhetetlenné válik, a jogszabály nem tekinthető érvényes jognak, hanem törvényes jogtalansággá minősül."}], ["c1-radbruch-formula-syntax"]),
                mc("grammar", "check", "Mikor enged a pozitív jog az igazságosság előtt a Radbruch-formula szerint?", [
                    "Amikor az igazságtalanság mértéke elviselhetetlenné és nyilvánvalóvá válik.",
                    "Bármikor, amikor egy politikus ezt kéri.",
                    "Csak gazdasági válságok idején."
                ], 0, ["c1-radbruch-formula-syntax"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-12-04",
            "title": "Legitimacy vs. Legality in Democratic Theory",
            "grammar_title": "Antithetical Parataxis in Legal-Philosophical Antitheses",
            "grammar_skill": "c1-legitimacy-vs-legality",
            "goals": [
                "I can distinguish conceptually between legality (*legalitás*) and democratic legitimacy (*legitimitás*).",
                "I can deploy antithetical paratactic structures (*Nem csupán a formális jogszerűség a mérce, hanem...*).",
                "I can analyze crises of democratic representation (*társadalmi szerződés felbomlása, demokratikus deficit*)."
            ],
            "vocab": [
                {"lemma": "legitimitás", "translation": "legitimacy", "pos": "noun"},
                {"lemma": "legalitás", "translation": "legality", "pos": "noun"},
                {"lemma": "törvényesség", "translation": "lawfulness, rule-compliance", "pos": "noun"},
                {"lemma": "joghézag", "translation": "legal vacuum, lacuna in law", "pos": "noun"},
                {"lemma": "demokratikus deficit", "translation": "democratic deficit", "pos": "noun"},
                {"lemma": "társadalmi szerződés", "translation": "social contract", "pos": "noun"},
                {"lemma": "híján van", "translation": "to be devoid of, lack sth", "pos": "expression"},
                {"lemma": "felülbírál", "translation": "to overrule, review, re-evaluate", "pos": "verb"}
            ],
            "gr_text1": "Philosophical analysis of public resistance hinges on the distinction between `legalitás` (formal adherence to written statutory rules) and `legitimitás` (normative justification rooted in popular consent and democratic principles).",
            "gr_text2": "Expressing this antithesis requires balanced paratactic structures: `Nem elegendő pusztán a formális legalitás, amennyiben a döntéshozatal híján van a demokratikus legitimitásnak` (Mere formal legality does not suffice insofar as decision-making lacks democratic legitimacy).",
            "gr_table": [
                ["Egy rezsim lehet formálisan legális, miközben híján van a legitimitásnak.", "A regime may be formally legal while lacking legitimacy."],
                ["A társadalmi szerződés felbomlása megkérdőjelezi az engedelmességet.", "The collapse of the social contract calls obedience into question."],
                ["Mély ellentmondás feszül a törvény betűje és az igazságérzet között.", "A deep tension strains between the letter of law and the sense of justice."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a különbség a legalitás és a legitimitás között a politikatudományban?", ["A legalitás az alaki törvényességet, a legitimitás a társadalmi elfogadottságot és erkölcsi indokoltságot jelenti.", "A legalitás a pénzre, a legitimitás a hadseregre vonatkozik.", "Nincs különbség, szinonimák."], 0, ["c1-12-vocab"]),
                fb("grammar", "controlled", "A törvény formailag érvényes volt, ám az elfogadási eljárás súlyos demokratikus _____ szenvedett. (deficit / deficitben)", "deficitben", "The law was formally valid, but the adoption procedure suffered from severe democratic deficit.", ["c1-legitimacy-vs-legality"]),
                match("vocabulary", "controlled", [["legalitás", "formal statutory lawfulness"], ["legitimitás", "moral & democratic justification"], ["társadalmi szerződés", "social contract"], ["joghézag", "legal lacuna"]], ["c1-12-vocab"]),
                fb("grammar", "practice", "A rendelet híján volt a társadalmi konszenzusnak, ami aláásta annak valós _____. (legitimacy / legitimitását)", "legitimitását", "The decree lacked social consensus, which undermined its real legitimacy.", ["c1-legitimacy-vs-legality"]),
                sb("grammar", "practice", ["A", "társadalmi", "szerződés", "felbomlása", "megkérdőjelezi", "a", "kormányzati", "hatalom", "legitimitását."], ["A", "társadalmi", "szerződés", "felbomlása", "megkérdőjelezi", "a", "kormányzati", "hatalom", "legitimitását."], "The unraveling of the social contract calls into question the legitimacy of governmental power.", ["c1-legitimacy-vs-legality"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Hogyan lehetséges, hogy a lakosság elutasít egy szabályosan elfogadott törvényt?"},
                    {"speaker": "Szociológus", "text": "Úgy, hogy a puszta alaki jogszerűség nem pótolja a demokratikus _____ hiányát."},
                ], ["legitimitás", "pénz", "idő"], 0, ["c1-legitimacy-vs-legality"]),
                sw("production", [{"prompt": "Contrast legality and legitimacy in a formal analytical statement.", "answer": "Míg a legalitás a jogszabályok alaki érvényességét követeli meg, addig a valódi legitimitás a kormányzottak hozzájárulásán és a jogállami értékek tiszteletén alapszik."}], ["c1-legitimacy-vs-legality"]),
                mc("grammar", "check", "Melyik állítás világítja meg helyesen a kettő viszonyát?", [
                    "A törvényi legalitás szükséges, de nem elégséges feltétele a társadalmi legitimitásnak.",
                    "A legalitás automatikusan biztosítja az örökös legitimitást.",
                    "A legitimitás független a választásoktól és a szabadságjogoktól."
                ], 0, ["c1-legitimacy-vs-legality"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-12-05",
            "title": "Dissenting Opinions & Deliberative Democracy",
            "grammar_title": "Juridical Dissent and Counter-Argumentation Rhetoric",
            "grammar_skill": "c1-dissent-deliberation",
            "goals": [
                "I can analyze judicial dissent mechanisms (*különvélemény, párhuzamos indokolás*).",
                "I can interpret György Konrád's 'Az autonómia kísértése' (Antipolitics).",
                "I can formulate deliberative democratic arguments in sophisticated constitutional Hungarian."
            ],
            "vocab": [
                {"lemma": "különvélemény", "translation": "dissenting opinion (judicial)", "pos": "noun"},
                {"lemma": "párhuzamos indokolás", "translation": "concurring opinion", "pos": "expression"},
                {"lemma": "bírói függetlenség", "translation": "judicial independence", "pos": "noun"},
                {"lemma": "deliberatív", "translation": "deliberative", "pos": "adjective"},
                {"lemma": "érvelési láncolat", "translation": "chain of argumentation", "pos": "noun"},
                {"lemma": "diszkurzus", "translation": "discourse", "pos": "noun"},
                {"lemma": "antipolitika", "translation": "antipolitics (civil autonomy)", "pos": "noun"},
                {"lemma": "összeférhetetlen", "translation": "incompatible", "pos": "adjective"}
            ],
            "gr_text1": "Constitutional court practice preserves minority judicial views via `különvélemény` (dissenting opinion) and `párhuzamos indokolás` (concurrence). In deliberative democracy, dissent is treated as the vital intellectual engine of legal evolution.",
            "gr_text2": "Rhetorical markers for formal dissent include: `Álláspontom szerint a többségi határozat téves premisszán alapul` (In my view the majority resolution rests on a flawed premise), `Nem oszthatom azt a felfogást, miszerint...` (I cannot share the understanding whereby...).",
            "gr_table": [
                ["Nem oszthatom a többségi döntést, amennyiben az sérti az alkotmányt.", "I cannot share the majority decision insofar as it violates the constitution."],
                ["Az alkotmánybíró éles hangú különvéleményt fűzött a határozathoz.", "The constitutional judge attached a sharp dissenting opinion to the resolution."],
                ["A különvélemény a jövőbeli jogfejlődés és reflexió fundamentuma.", "The dissenting opinion is the foundation of future legal development and reflection."]
            ],
            "classic_story": {
                "slug": "c1-12-konrad",
                "author": "Konrád György",
                "work": "Az autonómia kísértése (1980)",
                "title": "Antipolitika és a polgári autonómia védelme",
                "summary": "György Konrád's foundational manifesto on civil society's self-defense against the overreach of the state, defining intellectual autonomy and non-violent civic resistance.",
                "characters": ["Konrád György"],
                "paragraphs": [
                    {"type": "narration", "text": "Az antipolitika a civil társadalom önvédelme az államhatalom túlterjeszkedésével szemben. A polgár nem akarja átvenni a hatalmat; nem akar miniszter lenni, sem rendőrfőnök. A polgár békén akarja hagyni az államot, feltéve, hogy az állam is békén hagyja őt. Ám amikor a hatalom az emberi méltóság és a személyes autonómia legbensőbb köreit veszi ostrom alá, a hallgatás bűnrészességgé silányul."},
                    {"type": "narration", "text": "Történjék bármi, hozzon a bürokrácia bármilyen represszív intézkedést, a szellemi autonómia nem adható fel. A csendes, erőszakmentes ellenállás nem pusztán politikai taktika: ez a morális önazonosság egyetlen lehetséges formája. A független értelmiségi és a szabad polgár feladata nem az ideológiai igazodás, hanem a valóság elfogulatlan megfigyelése és az igazság bátor kimondása."},
                    {"type": "narration", "text": "Amikor a törvények maguk válnak az igazságtalanság eszközeivé, az engedetlenség nem felforgatás, hanem a jog valódi szellemének megőrzése. Az antipolitika elutasítja a politikai monopóliumot, és visszaköveteli a társadalom számára a döntés szabadságát: a kultúrában, a közösségi életben és a mindennapi erkölcsben."},
                    {"type": "narration", "text": "Konrád műve a közép-európai demokratikus ellenzék alapvető kiáltványává vált. Arra tanít, hogy a szabadság nem felülről kapott adomány, hanem a polgárok mindennapi, autonóm cselekvésének és méltóságának megbonthatatlan eredménye."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'különvélemény' intézménye az Alkotmánybíróságon?", ["A többségi döntéssel egyet nem értő bíró hivatalosan közzétett ellenvéleményét és érvelését.", "A bíróság épületének külön bejáratát.", "A bíró titkos magánnaplóját."], 0, ["c1-12-vocab"]),
                fb("grammar", "controlled", "A bíró határozott hangú _____ fűzött a döntéshez, vitatva a többség alkotmányértelmezését. (dissent / különvéleményt)", "különvéleményt", "The judge appended a resolute dissenting opinion to the decision, disputing the majority's constitutional interpretation.", ["c1-dissent-deliberation"]),
                match("vocabulary", "controlled", [["különvélemény", "dissenting opinion"], ["párhuzamos indokolás", "concurring opinion"], ["bírói függetlenség", "judicial independence"], ["érvelési láncolat", "chain of argumentation"]], ["c1-12-vocab"]),
                mc("reading", "practice", "Konrád György szerint mi az antipolitika alapvető törekvése?", [
                    "A civil társadalom önvédelme és a személyes autonómia megőrzése az államhatalom túlterjeszkedésével szemben.",
                    "A miniszteri székek elfoglalása és forradalmi diktatúra kiépítése.",
                    "A parlament épületének eladása külföldi befektetőknek."
                ], 0, None),
                sb("grammar", "practice", ["A", "deliberatív", "demokrácia", "lényege", "az", "érvek", "nyílt", "és", "racionális", "ütköztetése."], ["A", "deliberatív", "demokrácia", "lényege", "az", "érvek", "nyílt", "és", "racionális", "ütköztetése."], "The essence of deliberative democracy is the open and rational confrontation of arguments.", ["c1-dissent-deliberation"]),
                sw("production", [{"prompt": "Write a sentence articulating a principled judicial dissent.", "answer": "Nem oszthatom a bírósági többség álláspontját, mivel az ítélet indokolása összeférhetetlen a jogállamiság és az emberi méltóság alkotmányos követelményeivel."}], ["c1-dissent-deliberation"]),
                mc("grammar", "check", "Miért tekinthető a különvélemény a deliberatív jogfejlődés motorjának?", [
                    "Mert feltárja a joghézagokat és alternatív érveket szolgáltat a jövőbeli jogalkotás számára.",
                    "Mert automatikusan megsemmisíti az ítéletet.",
                    "Mert elbocsátják miatta az ellenszavazó bírákat."
                ], 0, ["c1-dissent-deliberation"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(12, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        12,
        "core",
        "c1-12-consolidation",
        core_title,
        [
            "I can formulate subjunctive concessives in civic defiance (*történjék bármi, hozzon bár új törvényeket*).",
            "I can apply ethical stance markers (*lelkiismereti okból fakadóan, meggyőződéstől vezérelve*).",
            "I can navigate the Radbruch formula, legality vs. legitimacy, and judicial dissent in deliberative democracy."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat alkalmazza helyesen a C1 kötőmódos megengedő szerkezetet?", [
                "Bármilyen fenyegetéssel éljen is a hatalom, az állampolgárok szilárdak maradnak.",
                "Bármilyen fenyegetéssel él a hatalom, az állampolgárok szilárdak voltak.",
                "Ha fenyegetéssel élne a hatalom, szilárdak maradnának."
            ], 0, ["c1-subjunctive-concessives"]),
            mc("grammar", "recognize", "Mi a lényege a Radbruch-formulának a jogbölcseletben?", [
                "Ahol a törvény elviselhetetlenül igazságtalan, ott elveszíti jogi érvényét mint törvényes jogtalanság.",
                "Hogy minden törvényt kötelező betű szerint végrehajtani erkölcstől függetlenül.",
                "Hogy a bíró dönthet pénzfeldobással."
            ], 0, ["c1-radbruch-formula-syntax"]),
            match("vocabulary", "recognize", [["passzív rezisztencia", "passive resistance"], ["lelkiismereti ok", "conscientious reason"], ["törvényes jogtalanság", "statutory injustice"], ["különvélemény", "dissenting opinion"], ["antipolitika", "antipolitics"]], ["c1-12-vocab"]),
            fb("vocabulary", "recall", "A bíró ellenvéleményét írásban rögzített _____ fejtette ki a nyilvánosság előtt. (dissent / különvéleményben)", "különvéleményben", "The judge expounded his dissent before the public in a written dissenting opinion.", ["c1-12-vocab"]),
            fb("vocabulary", "recall", "A diktatúra faji törvényei a természetjog szempontjából törvényes _____ minősültek. (injustice / jogtalanságnak)", "jogtalanságnak", "The dictatorship's racial laws qualified from a natural law perspective as statutory injustice.", ["c1-12-vocab"]),
            fb("grammar", "recall", "Történjék _____, az alapvető emberi jogok csorbítatlanul fennmaradnak. (whatever / bármi)", "bármi", "Whatever may happen, fundamental human rights endure unimpaired.", ["c1-subjunctive-concessives"]),
            fb("grammar", "context", "A tisztviselők mélységes morális _____ vezérelve tagadták meg az együttműködést. (conviction / meggyőződéstől)", "meggyőződéstől", "Guided by profound moral conviction, the officials refused collaboration.", ["c1-ethical-stance-markers"]),
            fb("grammar", "context", "A parlament által hozott jogszabály formailag legális volt, ám súlyos demokratikus _____ szenvedett. (deficit / deficitben)", "deficitben", "The statute enacted by parliament was formally legal, but suffered from severe democratic deficit.", ["c1-legitimacy-vs-legality"]),
            mc("grammar", "context", "Hogyan foglalható össze a legalitás és a legitimitás viszonya?", [
                "A formális legalitás önmagában nem garantálja az erkölcsi és társadalmi legitimitást.",
                "A legalitás és a legitimitás tökéletesen azonos fogalmak.",
                "A legitimitás csak diktatúrákban létezik."
            ], 0, ["c1-legitimacy-vs-legality"]),
            sb("grammar", "produce", ["A", "szankciók", "vállalása", "igazolja", "a", "polgári", "engedetlenség", "erkölcsi", "hitelét."], ["A", "szankciók", "vállalása", "igazolja", "a", "polgári", "engedetlenség", "erkölcsi", "hitelét."], "Acceptance of sanctions confirms the moral credibility of civil disobedience.", ["c1-dissent-deliberation"]),
            sw("production", [{"prompt": "Synthesize György Konrád's concept of antipolitics in relation to citizen autonomy.", "answer": "Konrád szerint az antipolitika a civil társadalom autonómiájának védelme az állam túlterjeszkedésével szemben: a belső szabadság és az emberi méltóság megőrzése békés, erőszakmentes ellenállással."}], ["c1-dissent-deliberation"]),
            sw("production", [{"prompt": "Formulate a concluding thought on the ethics of democratic resistance.", "answer": "Amikor az államhatalom kiüresíti a jogállamiság alapjait, a lelkiismereti alapon álló, szankciókat nyíltan vállaló polgári engedetlenség nem a rend megbontását, hanem a jog valódi szellemének megőrzését szolgálja."}], ["c1-ethical-stance-markers"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-polgariengedetlenseg)
    # ----------------------------------------------------
    slug = "polgariengedetlenseg"
    disc_intro = [
        "From Ferenc Deák's 19th-century passive resistance through the underground samizdat presses of the democratic opposition, the 1990 Taxi Blockade, and modern teachers' strikes, Hungarian history has repeatedly tested the boundaries of civic courage, institutional defiance, and democratic checks.",
        "In this unit, you will analyze the theory and practice of civil disobedience in Hungary: non-cooperation doctrines, open-name samizdat dissidence, direct civic blockades, strike right restrictions, and the political philosophy of John Rawls and Ronald Dworkin."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Historical Precedents: Ferenc Deák & 19th-Century Passive Resistance",
            "grammar_title": "Historical Rhetoric of Non-Cooperation and Constitutional Restitution",
            "grammar_skill": "c1-subjunctive-concessives",
            "goals": [
                "I can analyze Ferenc Deák's doctrine of passive resistance (*passzív rezisztencia, adómegtagadás*).",
                "I can deploy historical rhetoric of non-cooperation and legal continuity (*közjogi kontinuitás*).",
                "I can evaluate 19th-century constitutional defiance in advanced Hungarian."
            ],
            "vocab": [
                {"lemma": "passzív ellenállás", "translation": "passive resistance", "pos": "expression"},
                {"lemma": "közjogi kontinuitás", "translation": "public-law continuity", "pos": "noun"},
                {"lemma": "adómegtagadás", "translation": "tax refusal, withholding taxes", "pos": "noun"},
                {"lemma": "alkotmányos rend", "translation": "constitutional order", "pos": "noun"},
                {"lemma": "kényszerintézkedés", "translation": "coercive measure", "pos": "noun"},
                {"lemma": "hódol", "translation": "to yield, submit, pay homage", "pos": "verb"},
                {"lemma": "törvénytelen", "translation": "unlawful, illegitimate", "pos": "adjective"},
                {"lemma": "fennmarad", "translation": "to persist, survive, endure", "pos": "verb"}
            ],
            "gr_text1": "Following the defeat of the 1848–49 Revolution, Ferenc Deák championed 'passzív rezisztencia': refusing public office, withholding Austrian taxes, and asserting that unconstitutional decrees had no binding force upon Hungarian citizens.",
            "gr_text2": "Syntactically, historical texts deploy modal participle clauses and concessives: `Nem hódolva az önkénynek, a nemzet ragaszkodott az 1848-as törvényekhez` (Not bowing to autocracy, the nation clung to the 1848 laws).",
            "gr_table": [
                ["A nemzet elutasította, hogy önként hódoljon a császári pátensnek.", "The nation refused to voluntarily submit to the imperial patent."],
                ["Az adómegtagadás a passzív ellenállás leghatásosabb fegyvere volt.", "Tax refusal was the most effective weapon of passive resistance."],
                ["Ragaszkodva a közjogi kontinuitáshoz, megőrizték az alkotmányt.", "Clinging to public-law continuity, they preserved the constitution."]
            ],
            "world_story_seg": {
                "seg_slug": "deak",
                "title": "A passzív rezisztencia etikája: Deák Ferenc és a nemzeti ellenállás",
                "summary": "How Ferenc Deák guided Hungarian society through the Bach absolutist era using disciplined non-cooperation and constitutional persistence.",
                "paragraphs": [
                    {"type": "narration", "text": "Deák Ferenc politikája a magyar történelem talán legfegyelmezettebb polgári engedetlenségi stratégiája volt. Az 1848–49-es szabadságharc leverése után a nemzet nem lázadt fel újból fegyverrel, de nem volt hajlandó hódolni a bécsi önkényuralmi pátensnek sem. A nemesek és polgárok nem fizettek önként adót, nem vállaltak hivatalt az abszolutista adminisztrációban, és a végrehajtókkal szemben rideg elutasítással léptek fel."},
                    {"type": "narration", "text": "Deák világossá tette: a nemzet elviselheti az elnyomást, de önként egyetlen jottányit sem engedhet saját közjogi alkotmányából. 'Ha kell, szenvedni fog a nemzet, hogy megmentse az utókornak alkotmányos szabadságát' – hangoztatta. E passzív, jogi alapú ellenállás nélkül a kiegyezés kompromisszuma elképzelhetetlen lett volna."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt Deák Ferenc passzív rezisztenciájának lényege?", ["A békés, erőszakmentes együtt nem működés és a közjogi törvényekhez való ragaszkodás.", "A fegyveres gerillaharc.", "Az azonnali megadás és hódolat."], 0, ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "controlled", "Bármilyen megtorlást alkalmazzon is a hatalom, a társadalom megtagadta az önkéntes _____ fizetését. (tax / adó)", "adó", "Whatever reprisal the authority might apply, society refused the voluntary payment of tax.", ["c1-subjunctive-concessives"]),
                match("vocabulary", "controlled", [["passzív ellenállás", "passive resistance"], ["közjogi kontinuitás", "public-law continuity"], ["adómegtagadás", "tax refusal"], ["kényszerintézkedés", "coercive measure"]], ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "practice", "A nemzet elutasította, hogy önként _____ a törvénytelen rendeleteknek. (submit / hódoljon)", "hódoljon", "The nation refused to voluntarily submit to unlawful decrees.", ["c1-subjunctive-concessives"]),
                sb("grammar", "practice", ["Az", "adómegtagadás", "a", "passzív", "rezisztencia", "legfontosabb", "gazdasági", "fegyvere", "volt."], ["Az", "adómegtagadás", "a", "passzív", "rezisztencia", "legfontosabb", "gazdasági", "fegyvere", "volt."], "Tax refusal was the most important economic weapon of passive resistance.", ["c1-subjunctive-concessives"]),
                dc("dialogue", [
                    {"speaker": "Osztrák tisztviselő", "text": "Miért nem fizeti be az előírt hadiadót a város lakossága?"},
                    {"speaker": "Magyar alispán", "text": "Mert az országgyűlési hozzájárulás nélkül kivetett adó törvénytelen, és mi ragaszkodunk az _____ rendhez."},
                ], ["alkotmányos", "új", "katonai"], 0, ["c1-subjunctive-concessives"]),
                sw("production", [{"prompt": "Explain Ferenc Deák's strategy of non-cooperation in one complex historical sentence.", "answer": "Deák felismerte, hogy a fegyvertelen nemzet leghatékonyabb védelme a jogi intégritás megőrzése: az önkénnyel való együttműködés és adófizetés erőszakmentes megtagadása."}], ["c1-subjunctive-concessives"]),
                mc("grammar", "check", "Melyik állítás fogalmazza meg a közjogi kontinuitás elvét?", [
                    "A törvénytelen önkényuralmi rendeletek nem érvényteleníthetik az ország legitim alkotmányát.",
                    "Aki fegyverrel győz, az hozhat új törvényt érvényesen.",
                    "A régi törvények automatikusan törlődnek háború után."
                ], 0, ["c1-subjunctive-concessives"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Samizdat & The Democratic Opposition (1977–1989)",
            "grammar_title": "Parallel Structures in Underground Dissidence and Clandestine Publishing",
            "grammar_skill": "c1-ethical-stance-markers",
            "goals": [
                "I can analyze the democratic opposition and samizdat culture (*Beszélő, szamizdat, névvállalás*).",
                "I can deploy correlative causal contrasts (*Nem azért..., hanem mert...*).",
                "I can describe totalitarian censorship and ethical dissent in advanced Hungarian."
            ],
            "vocab": [
                {"lemma": "szamizdat", "translation": "samizdat (underground self-published literature)", "pos": "noun"},
                {"lemma": "demokratikus ellenzék", "translation": "democratic opposition", "pos": "noun"},
                {"lemma": "cenzúra kikerülése", "translation": "circumvention of censorship", "pos": "expression"},
                {"lemma": "besúgóhálózat", "translation": "informer network, state security net", "pos": "noun"},
                {"lemma": "represszió", "translation": "repression, state coercion", "pos": "noun"},
                {"lemma": "terjeszt", "translation": "to disseminate, distribute", "pos": "verb"},
                {"lemma": "stencilez", "translation": "to stencil / mimeograph", "pos": "verb"},
                {"lemma": "szólásszabadság védelme", "translation": "defense of free speech", "pos": "expression"}
            ],
            "gr_text1": "Under state socialism, the democratic opposition (Beszélő, Hírmondó) practiced systematic disobedience through illegal publishing and distribution of uncensored ideas.",
            "gr_text2": "Rhetorical discourse on dissent highlights moral imperatives over personal safety, using correlative contrastives: `Nem azért terjesztették a szamizdatot, mintha veszélytelen lett volna, hanem mert a nyilvánosság megteremtése elemi erkölcsi kötelességük volt`.",
            "gr_table": [
                ["Nem félelemből hallgattak, hanem a cenzúra ellen küzdöttek.", "They did not remain silent out of fear, but fought censorship."],
                ["A lap készítői nyílt névvel vállalták a megjelenést.", "The makers of the paper took responsibility with open names."],
                ["A szamizdat az alternatív nyilvánosság megteremtését szolgálta.", "Samizdat served the creation of an alternative public sphere."]
            ],
            "world_story_seg": {
                "seg_slug": "szamizdat",
                "title": "A független nyilvánosság születése: A Beszélő és a szamizdat",
                "summary": "How the Hungarian democratic opposition founded the open-name samizdat journal Beszélő, defying totalitarian censorship.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 1981-ben megjelent a Beszélő című szamizdat folyóirat első száma, a szerkesztők – köztük Kis János, Haraszti Miklós és Kőszeg Ferenc – tudatosan vállalták nevüket a címlapon. Ez a polgári engedetlenség radikális fordulata volt: az illegális konspiráció helyett nyílt arccal deklarálták, hogy a szólásszabadság veleszületett alapjog."},
                    {"type": "narration", "text": "A stencilezett lapok magánlakásokban, eldugott pincékben készültek, és bár az állambiztonság házkutatásokkal zaklatta a terjesztőket, a szamizdat a szabadság szigetét hozta létre. Nem azért cselekedtek így, mert nem féltek a büntetéstől, hanem mert felismerték: a diktatúrát a hazugság élteti, és az igazság kimondása az ellenállás legfontosabb formája."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért volt korszakalkotó a Beszélő szerkesztőinek nyílt névvállalása?", ["Mert a polgári engedetlenséget nyílt, erőszakmentes és felelős joggyakorlásként fogalmazta meg.", "Mert a pártállam kérte tőlük.", "Mert pénzjutalmat kaptak érte."], 0, ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "controlled", "A szerkesztők mély erkölcsi kötelességüktől _____ vállalták a politikai rendőrség zaklatásait. (guided / vezérelve)", "vezérelve", "Guided by their deep moral duty the editors undertook the harassment of political police.", ["c1-ethical-stance-markers"]),
                match("vocabulary", "controlled", [["szamizdat", "tiltott, illegális folyóirat"], ["demokratikus ellenzék", "pártállam békés ellenfelei"], ["besúgóhálózat", "állambiztonsági ügynökök"], ["represszió", "hatalmi elnyomás"]], ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "practice", "Nem azért terjesztették a lapot, mintha keresték volna a mártíromságot, _____ mert nem hazudhattak tovább. (but because / hanem)", "hanem", "They disseminated the paper not as if seeking martyrdom, but because they could no longer lie.", ["c1-ethical-stance-markers"]),
                sb("grammar", "practice", ["A", "cenzúra", "megkerülése", "a", "szellemi", "szabadság", "visszaszerzését", "szolgálta."], ["A", "cenzúra", "megkerülése", "a", "szellemi", "szabadság", "visszaszerzését", "szolgálta."], "Circumvention of censorship served the reclamation of intellectual freedom.", ["c1-ethical-stance-markers"]),
                dc("dialogue", [
                    {"speaker": "Rendőrtiszt", "text": "Tudja, hogy a szamizdat terjesztése izgatásnak minősül a törvény szerint?"},
                    {"speaker": "Ellenzéki író", "text": "Tudom, ám a véleménynyilvánítás szabadsága olyan jog, amelyet államhatalom nem _____ meg."},
                ], ["vonhat", "láthat", "vehet"], 0, ["c1-ethical-stance-markers"]),
                sw("production", [{"prompt": "Write a sentence contrasting censorship with samizdat distribution using 'nem azért..., hanem...'.", "answer": "Az ellenzéki értelmiségiek nem azért terjesztették a szamizdatot, mintha figyelmen kívül hagyták volna a veszélyt, hanem mert a független nyilvánosság megteremtése elemi erkölcsi kötelességük volt."}], ["c1-ethical-stance-markers"]),
                mc("grammar", "check", "Milyen nyelvi struktúra fejezi ki legpontosabban a polgári ellenállás etikai indoklását?", [
                    "A 'nem azért..., hanem mert...' ellentétes és kauzális mellérendelés.",
                    "A feltételes jelen idő harmadik személyben.",
                    "A felszólító mód tiltó formája."
                ], 0, ["c1-ethical-stance-markers"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "The 1990 Taxi Blockade: Crisis of the Young Democracy",
            "grammar_title": "Rhetoric of Spontaneous Civic Blockade and Conflict Resolution",
            "grammar_skill": "c1-radbruch-formula-syntax",
            "goals": [
                "I can analyze the 1990 Taxi Blockade (*taxisblokád, hidak lezárása, Érdekegyeztető Tanács*).",
                "I can evaluate direct civic blockade vs. public infrastructure order.",
                "I can discuss crisis management and negotiated consensus in democratic governance."
            ],
            "vocab": [
                {"lemma": "taxisblokád", "translation": "taxi blockade (October 1990)", "pos": "noun"},
                {"lemma": "bénultság", "translation": "paralysis, standstill", "pos": "noun"},
                {"lemma": "árrobbanás", "translation": "price explosion, sudden price hike", "pos": "noun"},
                {"lemma": "tárgyalóasztal", "translation": "negotiating table", "pos": "noun"},
                {"lemma": "kompromisszumkészség", "translation": "willingness to compromise", "pos": "noun"},
                {"lemma": "elzár", "translation": "to block, obstruct, seal off", "pos": "verb"},
                {"lemma": "fennakadás", "translation": "disruption, impediment", "pos": "noun"},
                {"lemma": "válságkezelés", "translation": "crisis management", "pos": "noun"}
            ],
            "gr_text1": "In October 1990, just months after Hungary's first free democratic elections, a drastic gas price hike triggered the 'Taxisblokád', where taxi drivers paralyzed the country's bridges and highway arteries.",
            "gr_text2": "Legal and political analysis combines concessive clauses with causality: `Bár a blokád formailag sértette a közlekedési rendet, a kialakult válságot a kormányzat csak tárgyalásos kompromisszummal oldhatta fel`.",
            "gr_table": [
                ["A hidak lezárása teljes közlekedési bénultságot okozott.", "The closing of bridges caused total transportation paralysis."],
                ["A kormányzat a karhatalmi fellépés helyett a tárgyalást választotta.", "The government chose negotiation instead of armed police crackdown."],
                ["Az Érdekegyeztető Tanács kompromisszuma oldotta fel a krízist.", "The compromise of the Reconciliation Council resolved the crisis."]
            ],
            "world_story_seg": {
                "seg_slug": "taxisblokad",
                "title": "Négy nap, amely megrázta a köztársaságot: A Taxisblokád",
                "summary": "How the young Hungarian democracy faced its first existential crisis during the October 1990 taxi blockade and resolved it through televised negotiations.",
                "paragraphs": [
                    {"type": "narration", "text": "1990. október 25-én este a kormány drasztikus benzináremelést jelentett be. Órákon belül taxik ezrei zárták le a budapesti Duna-hidakat, majd a főbb autópályákat és csomópontokat. Magyarország közlekedése megbénult. A frissen választott Antall-kormány súlyos dilemma elé került: bevesse-e a rendőrséget és a hadsereget, vagy üljön tárgyalóasztalhoz a tiltakozókkal?"},
                    {"type": "narration", "text": "Göncz Árpád köztársasági elnök határozottan kiállt a fegyveres erőszak ellen. Végül az Érdekegyeztető Tanács maratoni, élőben közvetített tárgyalásán kompromisszum született: a kormány csökkentette az áremelést, a fuvarozók pedig feloldották a zárlatot. A taxisblokád bebizonyította: a demokratikus békét konszenzussal, nem pedig karhatalommal kell megteremteni."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan oldódott meg az 1990-es taxisblokád válsága?", ["Az Érdekegyeztető Tanács élőben közvetített tárgyalásán elért kompromisszummal.", "A hadsereg fegyveres beavatkozásával és tömeges letartóztatásokkal.", "A hidak végleges lerombolásával."], 0, ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "controlled", "A hidak lezárása teljes országos közlekedési _____ okozott. (paralysis / bénultságot)", "bénultságot", "The sealing of bridges caused complete nationwide transportation paralysis.", ["c1-radbruch-formula-syntax"]),
                match("vocabulary", "controlled", [["taxisblokád", "spontán hídfoglaló tiltakozás"], ["árrobbanás", "hirtelen benzináremelés"], ["tárgyalóasztal", "békés egyeztetés fóruma"], ["válságkezelés", "konfliktus feloldása"]], ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "practice", "A kormányzat végül a tárgyalásos _____ útját választotta az erőszak helyett. (compromise / kompromisszum)", "kompromisszum", "The government ultimately chose the path of negotiated compromise instead of violence.", ["c1-radbruch-formula-syntax"]),
                sb("grammar", "practice", ["A", "kormány", "a", "tárgyalásos", "kompromisszum", "útját", "választotta", "a", "karhatalom", "helyett."], ["A", "kormány", "a", "tárgyalásos", "kompromisszum", "útját", "választotta", "a", "karhatalom", "helyett."], "The government chose the path of negotiated compromise instead of armed enforcement.", ["c1-radbruch-formula-syntax"]),
                dc("dialogue", [
                    {"speaker": "Miniszter", "text": "A blokád törvénytelen, a rendőrségnek fel kellene szabadítania az utakat."},
                    {"speaker": "Közvetítő", "text": "A társadalmi béke ára nem lehet fegyveres összecsapás; üljünk le a _____ mellé."},
                ], ["tárgyalóasztal", "gépkocsi", "sorompó"], 0, ["c1-radbruch-formula-syntax"]),
                sw("production", [{"prompt": "Assess the democratic significance of the 1990 taxi blockade.", "answer": "A taxisblokád a magyar demokrácia első nagy próbája volt, amely megmutatta, hogy még a rendkívüli társadalmi feszültségek is feloldhatók karhatalom nélkül, nyílt társadalmi párbeszéddel."}], ["c1-radbruch-formula-syntax"]),
                mc("grammar", "check", "Miért volt történelmi jelentőségű a válság békés feloldása?", [
                    "Mert megerősítette a kialakulóban lévő jogállami intézmények és az érdekegyeztetés tekintélyét.",
                    "Mert ingyenessé tette a benzin forgalmazását.",
                    "Mert betiltották az összes gépkocsit Budapesten."
                ], 0, ["c1-radbruch-formula-syntax"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Contemporary Civic Strikes & Teachers' Disobedience",
            "grammar_title": "Legal Disobedience vs. Strike Rights in Contemporary Administrative Law",
            "grammar_skill": "c1-legitimacy-vs-legality",
            "goals": [
                "I can analyze the legal conflict surrounding teachers' protests (*sztrájkjog, polgári engedetlenség*).",
                "I can evaluate statutory restrictions (*még elégséges szolgáltatás, rendkívüli felmentés*).",
                "I can assess constitutional proportionality and labour law sanctions in modern Hungary."
            ],
            "vocab": [
                {"lemma": "sztrájkjog", "translation": "right to strike", "pos": "noun"},
                {"lemma": "elégséges szolgáltatás", "translation": "minimum necessary service level", "pos": "noun"},
                {"lemma": "munkabeszüntetés", "translation": "work stoppage, walkout", "pos": "noun"},
                {"lemma": "rendkívüli felmentés", "translation": "extraordinary dismissal / termination", "pos": "noun"},
                {"lemma": "aránytalan hátrány", "translation": "disproportionate disadvantage", "pos": "expression"},
                {"lemma": "kiállás", "translation": "stand, solidarity demonstration", "pos": "noun"},
                {"lemma": "kötelezettségszegés", "translation": "breach of official duty", "pos": "noun"},
                {"lemma": "élőlánc", "translation": "human chain (protest form)", "pos": "noun"}
            ],
            "gr_text1": "Recent Hungarian civic movements—notably the educators' protests of 2022–2023—faced strict legislative curtailment of strike rights via mandatory 'még elégséges szolgáltatás'. When formal strike avenues were rendered ineffective, educators engaged in conscious civil disobedience (`polgári engedetlenség`).",
            "gr_text2": "Syntactically, analyzing this balances labour law duties against constitutional rights: `A pedagógusok tudatában voltak a kötelezettségszegésnek, ám az oktatás védelmében mégis ezt a végső eszközt választották`.",
            "gr_table": [
                ["A sztrájkjog korlátozása polgári engedetlenséghez vezetett.", "The curtailment of strike rights led to civil disobedience."],
                ["A tanárok vállalták a rendkívüli felmentés kockázatát.", "The teachers undertook the risk of extraordinary dismissal."],
                ["Diákok és szülők élőlánccal fejezték ki szolidaritásukat.", "Students and parents expressed solidarity with a human chain."]
            ],
            "world_story_seg": {
                "seg_slug": "tanarok",
                "title": "A tanterem mint a lelkiismeret fóruma: Pedagógusok az engedetlenség útján",
                "summary": "How Hungarian educators turned to civil disobedience when strike rights were curtailed, sparking widespread solidarity movements.",
                "paragraphs": [
                    {"type": "narration", "text": "2022 tavaszán a kormány rendeleti úton úgy szabályozta a tanári sztrájk feltételeit, hogy a munkabeszüntetés alatt is meg kellett tartani az órák túlnyomó részét és a gyermekfelügyeletet. Sok pedagógus úgy érezte: a rendelet kiüresítette a sztrájkjogot, hisz a láthatatlan tiltakozás nem képes nyomást gyakorolni a döntéshozókra."},
                    {"type": "narration", "text": "Ekkor országszerte gimnáziumok és általános iskolák tantestületei polgári engedetlenséget hirdettek. Nem vették fel a munkát, jóllehet tudták, hogy elbocsátás vagy fegyelmi büntetés fenyegeti őket. Álláspontjuk szerint az oktatás minőségének romlása és a szabad tiltakozás ellehetetlenítése olyan súlyos kár, amellyel szemben a jogsértés tudatos vállalása erkölcsi kötelességgé vált."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért fordultak a pedagógusok a polgári engedetlenséghez a sztrájk helyett?", ["Mert a sztrájkszabályok kiüresítették a munkabeszüntetés láthatóságát és hatékonyságát.", "Mert több fizetést reméltek a törvénysértéstől.", "Mert a minisztérium kifejezetten erre utasította őket."], 0, ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "controlled", "A tankerület rendkívüli _____ bocsátotta el a polgári engedetlenségben részt vevő oktatókat. (dismissal / felmentéssel)", "felmentéssel", "The school district dismissed the educators participating in civil disobedience by extraordinary dismissal.", ["c1-legitimacy-vs-legality"]),
                match("vocabulary", "controlled", [["sztrájkjog", "alkotmányos munkabeszüntetés joga"], ["elégséges szolgáltatás", "minimálisan biztosítandó ellátás"], ["rendkívüli felmentés", "azonnali hatályú elbocsátás"], ["kötelezettségszegés", "munkaköri kötelesség megsértése"]], ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "practice", "A sztrájkjog aránytalan korlátozása közvetlenül a polgári _____ kibontakozásához vezetett. (disobedience / engedetlenség)", "engedetlenség", "The disproportionate curtailment of strike rights directly led to the unfolding of civil disobedience.", ["c1-legitimacy-vs-legality"]),
                sb("grammar", "practice", ["A", "sztrájkjog", "kiüresítése", "a", "polgári", "engedetlenség", "térnyeréséhez", "vezetett."], ["A", "sztrájkjog", "kiüresítése", "a", "polgári", "engedetlenség", "térnyeréséhez", "vezetett."], "Hollowing out the right to strike led to the expansion of civil disobedience.", ["c1-legitimacy-vs-legality"]),
                dc("dialogue", [
                    {"speaker": "Szülő", "text": "Nem féltették az állásukat, amikor megtagadták a tanítást?"},
                    {"speaker": "Tanár", "text": "De igen, ám a sztrájk ellehetetlenítése után ez maradt az egyetlen hiteles _____ formánk."},
                ], ["tiltakozási", "gazdasági", "pihenési"], 0, ["c1-legitimacy-vs-legality"]),
                sw("production", [{"prompt": "Analyze the dilemma between labour obligations and conscientious protest in education.", "answer": "A pedagógusok tudatos munkajogi kötelezettségszegést követtek el, mert felismerték, hogy a törvényes sztrájk kiüresítése miatt csak a polgári engedetlenség képes felhívni a társadalom figyelmét az oktatás válságára."}], ["c1-legitimacy-vs-legality"]),
                mc("grammar", "check", "Milyen jogi következménnyel szembesültek a polgári engedetlenséget választó tanárok?", [
                    "A munkaviszony rendkívüli felmentéssel történő azonnali megszüntetésével.",
                    "Automatikus előléptetéssel.",
                    "Külföldi ösztöndíjakkal."
                ], 0, ["c1-legitimacy-vs-legality"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Legal Philosophy of Dissent: Rawls, Dworkin & Constitutional Limits",
            "grammar_title": "Juridical Discourse on Civil Disobedience in Democratic Theory",
            "grammar_skill": "c1-dissent-deliberation",
            "goals": [
                "I can analyze John Rawls' and Ronald Dworkin's theories of civil disobedience.",
                "I can evaluate the requirement of non-violence and acceptance of sanctions (*erőszakmentesség, szankcióvállalás*).",
                "I can synthesize the role of civil disobedience as a democratic corrective mechanism."
            ],
            "vocab": [
                {"lemma": "lelkiismereti szabadság", "translation": "freedom of conscience", "pos": "noun"},
                {"lemma": "nyilvános igazolás", "translation": "public justification", "pos": "noun"},
                {"lemma": "erőszakmentesség", "translation": "non-violence", "pos": "noun"},
                {"lemma": "szankcióvállalás", "translation": "acceptance of sanctions / penalty", "pos": "noun"},
                {"lemma": "jogkövetés", "translation": "compliance with law, law-abidance", "pos": "noun"},
                {"lemma": "apellál", "translation": "to appeal (to conscience/reason)", "pos": "verb"},
                {"lemma": "korrekciós mechanizmus", "translation": "corrective mechanism", "pos": "noun"},
                {"lemma": "jogrendszer hűsége", "translation": "fidelity to the legal system as a whole", "pos": "expression"}
            ],
            "gr_text1": "In liberal political philosophy (John Rawls, Ronald Dworkin), civil disobedience is defined not as revolution, but as a public, non-violent, conscientious, yet politically illegal act aimed at bringing about a change in unjust laws, while expressing fidelity to law through the willing acceptance of sanctions.",
            "gr_text2": "Syntactically, texts combine teleological subordinations with high-register legal nouns: `A büntetés önkéntes vállalása a jogrendszer iránti hűséget igazolja, miközben a cselekvés a társadalom többségi igazságérzetére apellál`.",
            "gr_table": [
                ["A polgári engedetlenség nyilvános, békés és a szankciókat vállaló tett.", "Civil disobedience is a public, peaceful act accepting sanctions."],
                ["Nem a jogrend felforgatása, hanem annak korrekciós mechanizmusa.", "Not the subversion of legal order, but its corrective mechanism."],
                ["A tiltakozók a többség igazságérzetéhez intéznek felhívást.", "The protesters address an appeal to the majority's sense of justice."]
            ],
            "world_story_seg": {
                "seg_slug": "dworkin",
                "title": "A jog tisztelete és a lelkiismeret: Rawls és Dworkin nyomán",
                "summary": "The classic legal-philosophical foundation of civil disobedience as an appeal to the public sense of justice and a constitutional safety valve.",
                "paragraphs": [
                    {"type": "narration", "text": "A liberális jogfilozófia legfontosabb gondolkodói – mindenekelőtt John Rawls és Ronald Dworkin – szerint a polgári engedetlenség nem a jogállam ellensége, hanem annak nélkülözhetetlen korrekciós mechanizmusa. Rawls definíciója szerint a polgári engedetlenség nyilvános, erőszakmentes és lelkiismereti alapú cselekvés, amely a törvény ellen irányul, ám a jogsértő a büntetés vállalásával fejezi ki hűségét a jogrendszer egésze iránt."},
                    {"type": "narration", "text": "Dworkin hozzáteszi: ha egy törvény alkotmányossága mélyen vitatható, az államnak mérlegelnie kell, hogy büntetőjogilag felelősségre vonja-e azokat, akik lelkiismereti okokból szembeszegülnek vele. A polgári engedetlenség nem a káosz hirdetése, hanem ünnepélyes felhívás a többség igazságérzetéhez: emlékeztető arra, hogy a valódi jogrendnek az igazságosságon kell nyugodnia."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen három fő feltételt határoz meg Rawls a polgári engedetlenségre?", ["Nyilvános, erőszakmentes cselekvés, amely a szankciók vállalásával fejezi ki a jogrendszer iránti hűséget.", "Fegyveres erőszak, titkos összeesküvés és a hatalom átvétele.", "Minden bírósági ítélet automatikus semmibe vétele."], 0, ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "controlled", "A polgári engedetlenség a többségi társadalom veleszületett _____ apellál. (sense of justice / igazságérzetére)", "igazságérzetére", "Civil disobedience appeals to the innate sense of justice of majority society.", ["c1-dissent-deliberation"]),
                match("vocabulary", "controlled", [["szankcióvállalás", "büntetés tudatos elfogadása"], ["erőszakmentesség", "békés eszközök primátusa"], ["korrekciós mechanizmus", "demokratikus önjavító folyamat"], ["nyilvános igazolás", "erkölcsi indokok nyilvános bemutatása"]], ["c1-polgariengedetlenseg-vocab"]),
                fb("grammar", "practice", "A jogkövetkezmények önkéntes vállalása a jogrendszer egésze iránti _____ igazolja. (fidelity / hűséget)", "hűséget", "The voluntary acceptance of legal consequences confirms fidelity toward the legal system as a whole.", ["c1-dissent-deliberation"]),
                sb("grammar", "practice", ["A", "szankciók", "önkéntes", "vállalása", "igazolja", "a", "tett", "erkölcsi", "komolyságát."], ["A", "szankciók", "önkéntes", "vállalása", "igazolja", "a", "tett", "erkölcsi", "komolyságát."], "Voluntary acceptance of sanctions confirms the moral gravity of the deed.", ["c1-dissent-deliberation"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Miért nem tekinthető anarchiának a polgári engedetlenség?"},
                    {"speaker": "Jogtudós", "text": "Mert a tiltakozó nem a jogrend felszámolására tör, hanem a szankciók vállalásával annak mélyebb _____ hívja fel a figyelmet."},
                ], ["igazságosságára", "költségére", "hosszára"], 0, ["c1-dissent-deliberation"]),
                sw("production", [{"prompt": "Formulate John Rawls' definition of civil disobedience.", "answer": "Rawls szerint a polgári engedetlenség olyan nyilvános, erőszakmentes és lelkiismereti alapú cselekedet, amely a törvénysértés szankcióinak vállalásával apellál a társadalom többségi igazságérzetére."}], ["c1-dissent-deliberation"]),
                mc("grammar", "check", "Miért nélkülözhetetlen a szankciók vállalása a polgári engedetlenségben?", [
                    "Mert ez különbözteti meg az erkölcsi indíttatású engedetlenséget a közönséges köztörvényes bűnözéstől.",
                    "Mert a börtönben ingyenes az ellátás.",
                    "Mert ezt írja elő a büntető törvénykönyv minden tüntetőnek."
                ], 0, ["c1-dissent-deliberation"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(12, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A lelkiismeret lázadása: A polgári engedetlenség magyar fejezetei",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive chronicle of civil disobedience and democratic checks in Hungarian history: Ferenc Deák's 19th-century passive resistance, underground samizdat dissidence in Beszélő, the 1990 Taxi Blockade, modern teachers' strikes, and the legal philosophy of Rawls and Dworkin.",
            "paragraphs": [
                {"type": "narration", "text": "A polgári engedetlenség nem felforgatás, hanem a közösség erkölcsi lelkiismeretének legtisztább megnyilvánulása. A magyar történelemben e nemes hagyomány Deák Ferenc 19. századi passzív rezisztenciájával kezdődött, amely a fegyveres vereség után a törvénytelen bécsi pátenssel szemben az adómegtagadás és a tisztségvállalástól való elzárkózás erőszakmentes útját választotta."},
                {"type": "narration", "text": "Ezt folytatta a nyolcvanas években a Beszélő köré csoportosuló demokratikus ellenzék, amely a névvel vállalt szamizdat lapokkal törte át a totalitárius állam cenzúráját, bizonyítva, hogy a belső szabadság nem függ az államhatalom engedélyétől."},
                {"type": "narration", "text": "Az 1990-es taxisblokád a friss köztársaságot állította próbatétel elé, bebizonyítva, hogy a társadalmi békét a tárgyalóasztal konszenzusa, nem pedig a karhatalom fegyverei szavatolják."},
                {"type": "narration", "text": "Napjainkban a sztrájkjogukban korlátozott tanárok bátor kiállása emlékeztet arra, amit John Rawls és Ronald Dworkin megfogalmazott: ha a jogszabályok kiüresítik az alapvető jogokat, a szankciókat nyíltan vállaló engedetlenség nem a rend megbontása, hanem a jog valódi, igazságos szellemének végső megmentése."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        12,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can evaluate historical passive resistance, public-law continuity, and tax refusal.",
            "I can analyze samizdat publishing, open-name dissidence, and the circumvention of censorship.",
            "I can discuss the 1990 Taxi Blockade, contemporary teachers' strikes, and Rawlsian civil disobedience theory."
        ],
        [
            mc("grammar", "recognize", "Mi jellemezte Deák Ferenc passzív rezisztenciáját?", [
                "Az együtt nem működés és a közjogi alapokhoz való feltétlen ragaszkodás erőszakmentes formája.",
                "A fegyveres lázadás.",
                "A bécsi udvarral kötött titkos egyezség."
            ], 0, ["c1-subjunctive-concessives"]),
            mc("grammar", "recognize", "Miért választották a pedagógusok a polgári engedetlenséget 2022-ben?", [
                "Mert a sztrájkjog törvényi korlátozása kiüresítette a munkabeszüntetés hatékonyságát.",
                "Mert szabadságra akartak menni.",
                "Mert a tankerület ezt javasolta."
            ], 0, ["c1-legitimacy-vs-legality"]),
            match("vocabulary", "recognize", [["passzív ellenállás", "passive resistance"], ["szamizdat", "underground literature"], ["taxisblokád", "spontaneous blockade"], ["sztrájkjog", "right to strike"], ["szankcióvállalás", "acceptance of penalties"]], ["c1-polgariengedetlenseg-vocab"]),
            fb("vocabulary", "recall", "A Beszélő szerkesztői nyílt _____ vállalták a szamizdat cikkek megjelentetését. (name / névvel)", "névvel", "The editors of Beszélő undertook the publication of samizdat articles with open names.", ["c1-polgariengedetlenseg-vocab"]),
            fb("vocabulary", "recall", "A polgári engedetlenség alapvető ismérve a szankciók tudatos és önkéntes _____. (acceptance / vállalása)", "vállalása", "The fundamental hallmark of civil disobedience is the conscious and voluntary acceptance of sanctions.", ["c1-polgariengedetlenseg-vocab"]),
            fb("grammar", "recall", "Bármilyen fenyegetést alkalmazzon is a rezsim, a polgárok megtagadták az adók _____ befizetését. (voluntary / önkéntes)", "önkéntes", "Whatever threat the regime may apply, citizens refused the voluntary payment of taxes.", ["c1-subjunctive-concessives"]),
            fb("grammar", "context", "A taxisblokád feszültségét az Érdekegyeztető Tanácsban elért tárgyalásos _____ oldotta fel. (compromise / kompromisszum)", "kompromisszum", "The tension of the taxi blockade was resolved by the negotiated compromise reached in the Reconciliation Council.", ["c1-radbruch-formula-syntax"]),
            fb("grammar", "context", "A polgári engedetlenség nem anarchia, hanem a társadalom többségi _____ való apellálás. (sense of justice / igazságérzetére)", "igazságérzetére", "Civil disobedience is not anarchy, but an appeal to the majority sense of justice of society.", ["c1-dissent-deliberation"]),
            mc("grammar", "context", "Hogyan illeszkedik a polgári engedetlenség a deliberatív demokráciába Rawls szerint?", [
                "Mint az igazságtalan törvények korrekcióját szolgáló, a jogrend iránti hűséget megőrző békés mechanizmus.",
                "Mint a jogrendszer teljes és erőszakos megsemmisítése.",
                "Mint a mindenkori kormány kizárólagos joga."
            ], 0, ["c1-dissent-deliberation"]),
            sb("grammar", "produce", ["A", "polgári", "engedetlenség", "a", "jogállam", "nélkülözhetetlen", "korrekciós", "mechanizmusa."], ["A", "polgári", "engedetlenség", "a", "jogállam", "nélkülözhetetlen", "korrekciós", "mechanizmusa."], "Civil disobedience is the indispensable corrective mechanism of the rule of law.", ["c1-dissent-deliberation"]),
            sw("production", [{"prompt": "Explain why civil disobedience is fundamentally non-violent according to legal philosophy.", "answer": "A polgári engedetlenség azért erőszakmentes, mert célja nem a hatalom fegyveres megdöntése, hanem a társadalom igazságérzetének felébresztése és a jogrend erkölcsi megújítása a törvénysértés szankcióinak bátor vállalásával."}], ["c1-dissent-deliberation"]),
            sw("production", [{"prompt": "Formulate a concluding thought on civil resistance in modern Central Europe.", "answer": "A passzív rezisztencia és a polgári engedetlenség magyar fejezetei bebizonyították, hogy a jog valódi tekintélye nem a karhatalom erejéből, hanem a polgárok szabadság iránti elkötelezettségéből és erkölcsi méltóságából fakad."}], ["c1-dissent-deliberation"])
        ]
    )

    print("=== Finished C1 Unit 12 ===")


if __name__ == "__main__":
    generate_unit_12()
