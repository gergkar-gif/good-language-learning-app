#!/usr/bin/env python3
"""
Hungarian C1 Block 2 - Unit 07 Generator:
  - Track 1 (Core): Unit 7 — "Legal Syntactic Architecture & Normative Modality" (c1-07)
  - Track 2 (Discourse): Unit 7 — "The Rule of Law & Constitutional Evolution" (c1-jogallamisag)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block2.registry_helper import register_unit


def generate_unit_7():
    print("=== Generating C1 Unit 7 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-07-vocab": {"kind": "vocabulary"},
        "c1-jogallamisag-vocab": {"kind": "vocabulary"},
        "c1-normative-participles": {"kind": "grammar"},
        "c1-statutory-predicates": {"kind": "grammar"},
        "c1-legal-conditions": {"kind": "grammar"},
        "c1-normative-modality": {"kind": "grammar"},
        "c1-constitutional-discourse": {"kind": "grammar"},
    }
    new_titles = {
        "c1-07-vocab": "reading",
        "c1-jogallamisag-vocab": "reading",
        "c1-normative-participles": "normative future and obligatory participles in legal register",
        "c1-statutory-predicates": "statutory duty entitlement predicates and formal legal formulas",
        "c1-legal-conditions": "high precision restrictive legal conditions and stipulations",
        "c1-normative-modality": "normative modality and statutory compliance framing",
        "c1-constitutional-discourse": "constitutional jurisprudence and historic legal evolution",
    }
    
    core_title = "Legal Syntactic Architecture & Normative Modality"
    core_stems = [f"c1-07-0{i}" for i in range(1, 6)] + ["c1-07-consolidation"]
    disc_title = "The Rule of Law & Constitutional Evolution"
    disc_stems = [f"c1-jogallamisag-0{i}" for i in range(1, 6)] + ["c1-jogallamisag-consolidation"]
    
    register_unit(7, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-07)
    # ----------------------------------------------------
    core_intro = [
        "Hungarian legal and constitutional syntax is one of the most intellectually demanding registers of the language. It operates through severe precision, normative participles (-andó/-endő), statutory duty predicates, and recursive conditional hedging.",
        "In this unit, inspired by Baron József Eötvös's classical liberal statecraft in 'A XIX. század uralkodó eszméinek befolyása az államra' (1851), you will master normative future participles, formal entitlement predicates (jogosult, köteles, terheli a kötelezettség), and high-precision statutory draftsmanship."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-07-01",
            "title": "The Normative Participle: Obligations and Inevitability",
            "grammar_title": "The Normative Participle (-andó / -endő) in Formal and Legal Syntax",
            "grammar_skill": "c1-normative-participles",
            "goals": [
                "I can form and interpret normative participles (*-andó / -endő*) expressing legal necessity.",
                "I can distinguish between descriptive future participles and mandatory legal obligations.",
                "I can draft formal administrative stipulations using pre-nominal participial modifiers."
            ],
            "vocab": [
                {"lemma": "alkalmazandó", "translation": "to be applied, applicable", "pos": "adjective"},
                {"lemma": "fizetendő", "translation": "payable, to be paid", "pos": "adjective"},
                {"lemma": "követendő", "translation": "to be followed, model (procedure)", "pos": "adjective"},
                {"lemma": "megoldandó", "translation": "to be resolved", "pos": "adjective"},
                {"lemma": "végrehajtandó", "translation": "to be executed, enforceable", "pos": "adjective"},
                {"lemma": "figyelembe veendő", "translation": "to be taken into account", "pos": "adjective"},
                {"lemma": "jogszabály", "translation": "statute, legal rule", "pos": "noun"},
                {"lemma": "rendelkezés", "translation": "provision, disposition, decree", "pos": "noun"}
            ],
            "gr_text1": "In formal Hungarian, legal and institutional necessity is densely encoded using the participle in *-andó / -endő*. Unlike the English modal 'must be done', Hungarian compresses this into a single modifier: *az alkalmazandó jogszabály* (the statute that must be applied).",
            "gr_text2": "When used predicatively (*A határozat haladéktalanul végrehajtandó*), it functions as an absolute legal imperative, leaving no discretionary room.",
            "gr_table": [
                ["Az ügyben alkalmazandó eljárási szabályok...", "The procedural rules to be applied in the case..."],
                ["A határidőre megfizetendő illeték összege...", "The sum of duty payable by the deadline..."],
                ["E rendelkezés szigorúan követendő minden hivatalban.", "This provision is strictly to be followed in every office."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'végrehajtandó' kifejezés a jogi szövegekben?", ["Kötelező érvényű cselekvést, amelyet végre kell hajtani.", "Olyan feladatot, amit tetszés szerint el lehet hagyni.", "Múltbeli, már lezárt eseményt."], 0, ["c1-07-vocab"]),
                fb("grammar", "controlled", "A jelen eljárásban az Európai Unió közvetlenül _____ rendelete az irányadó. (to be applied / alkalmazandó)", "alkalmazandó", "In the present proceeding, the directly applicable regulation of the European Union is governing.", ["c1-normative-participles"]),
                match("vocabulary", "controlled", [["alkalmazandó", "to be applied"], ["fizetendő", "payable"], ["követendő", "to be followed"], ["jogszabály", "statute"]], ["c1-07-vocab"]),
                fb("grammar", "practice", "A bíróság döntése minden érintett szerv számára kötelező és haladéktalanul _____. (to be executed / végrehajtandó)", "végrehajtandó", "The court's decision is binding and to be executed without delay for every affected body.", ["c1-normative-participles"]),
                sb("grammar", "practice", ["A", "döntéshozatal", "során", "minden", "releváns", "körülmény", "figyelembe", "veendő."], ["A", "döntéshozatal", "során", "minden", "releváns", "körülmény", "figyelembe", "veendő."], "During decision-making, every relevant circumstance is to be taken into account.", ["c1-normative-participles"]),
                dc("dialogue", [
                    {"speaker": "Jogtanácsos", "text": "Milyen jogszabályt kell figyelembe vennünk a szerződéskötéskor?"},
                    {"speaker": "Ügyvéd", "text": "A Polgári Törvénykönyv hatályos, kötelezően _____ rendelkezéseit."},
                ], ["alkalmazandó", "elfelejtett", "nem létező"], 0, ["c1-normative-participles"]),
                sw("production", [{"prompt": "Formulate a formal legal instruction using an '-andó/-endő' participle.", "answer": "A panasz kivizsgálása során a vonatkozó adatvédelmi elvek szigorúan tiszteletben tartandók."}], ["c1-normative-participles"]),
                mc("grammar", "check", "Melyik mondat fejezi ki a legpontosabban a jogi kötelezettséget?", [
                    "A határozat ellen fellebbezésnek helye nincs, a döntés jogerős és azonnal végrehajtandó.",
                    "Talán majd végrehajtjuk ezt a határozatot, ha lesz rá időnk.",
                    "A határozat szép volt, ezért mindenki örült neki."
                ], 0, ["c1-normative-participles"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-07-02",
            "title": "Statutory Duty and Entitlement Predicates",
            "grammar_title": "Legal Duty and Entitlement Formulas: Köteles, Jogosult, and Terheli",
            "grammar_skill": "c1-statutory-predicates",
            "goals": [
                "I can deploy statutory duty verbs (*terheli a kötelezettség, felelősséggel tartozik*).",
                "I can formulate legal rights and entitlements using *jogosult* and *illeti meg*.",
                "I can distinguish between permissive (*jogosult*) and mandatory (*köteles*) statutory clauses."
            ],
            "vocab": [
                {"lemma": "jogosult", "translation": "entitled, authorized", "pos": "adjective"},
                {"lemma": "köteles", "translation": "obligated, bound to", "pos": "adjective"},
                {"lemma": "illeti meg", "translation": "is entitled to (rights)", "pos": "expression"},
                {"lemma": "terheli a kötelezettség", "translation": "bears the obligation", "pos": "expression"},
                {"lemma": "hatályát veszti", "translation": "loses effect, ceases to be in force", "pos": "expression"},
                {"lemma": "jogerő", "translation": "legal force, finality", "pos": "noun"},
                {"lemma": "jogorvoslat", "translation": "legal remedy, appeal", "pos": "noun"},
                {"lemma": "kötelezettségszegés", "translation": "breach of duty / obligation", "pos": "noun"}
            ],
            "gr_text1": "Hungarian statutory prose avoids informal modal verbs like *kell* in favor of explicit predicates: *A bérlő köteles megfizetni...* (The tenant is obligated to pay) vs. *A bérbeadó jogosult felmondani...* (The lessor is entitled to terminate).",
            "gr_text2": "Abstract burdens take the verb *terhel*: *A bizonyítási teher az alperest terheli.* (The burden of proof lies upon the defendant).",
            "gr_table": [
                ["A felet indokolt esetben jogorvoslat illeti meg.", "The party is entitled to legal remedy in justified cases."],
                ["A munkavállaló köteles haladéktalanul értesíteni a munkáltatót.", "The employee is obligated to notify the employer without delay."],
                ["A kártérítés megfizetésének kötelezettsége a károkozót terheli.", "The obligation to pay damages lies upon the tortfeasor."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Melyik kifejezés jelöli a jogi kötelezettség fennállását?", ["terheli a kötelezettség", "szabadon eldöntheti", "nem érdekli a dolog"], 0, ["c1-07-vocab"]),
                fb("grammar", "controlled", "A szerződő fél súlyos szerződésszegés esetén azonnali hatályú felmondásra _____. (entitled / jogosult)", "jogosult", "The contracting party is entitled to immediate termination in case of gross breach of contract.", ["c1-statutory-predicates"]),
                match("vocabulary", "controlled", [["jogosult", "entitled"], ["köteles", "obligated"], ["jogorvoslat", "legal remedy"], ["jogerő", "legal force"]], ["c1-07-vocab"]),
                fb("grammar", "practice", "A jogszabályi előírások betartásának bizonyítása a kérelmezőt _____. (bears / terheli)", "terheli", "The burden of proving compliance with statutory rules lies upon the applicant.", ["c1-statutory-predicates"]),
                sb("grammar", "practice", ["Minden", "állampolgárt", "megillet", "a", "tisztességes", "eljáráshoz", "való", "alapvető", "jog."], ["Minden", "állampolgárt", "megillet", "a", "tisztességes", "eljáráshoz", "való", "alapvető", "jog."], "Every citizen is entitled to the fundamental right to fair proceedings.", ["c1-statutory-predicates"]),
                dc("dialogue", [
                    {"speaker": "Ügyfél", "text": "Van még lehetőségem vitatni az elmarasztaló határozatot?"},
                    {"speaker": "Ügyvéd", "text": "Igen, a törvény értelmében tizenöt napon belül jogorvoslat _____ meg."},
                ], ["illeti", "fosztja", "tagadja"], 0, ["c1-statutory-predicates"]),
                sw("production", [{"prompt": "Write a formal contractual clause defining a duty and entitlement.", "answer": "A vevő a vételár megfizetésére köteles, míg a dolog birtokba vételére a teljesítést követően válik jogosulttá."}], ["c1-statutory-predicates"]),
                mc("grammar", "check", "Melyik megfogalmazás felel meg a szabatos jogi stílusnak?", [
                    "A szerződés a felek kölcsönös megegyezése hiányában harminc nap elteltével hatályát veszti.",
                    "A papír érvénytelen lesz egy hónap múlva, ha nem dumálnak egymással.",
                    "Nem tudjuk pontosan, mikor szűnik meg a papírunk."
                ], 0, ["c1-statutory-predicates"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-07-03",
            "title": "Precision Restrictive Clauses in Statutory Drafting",
            "grammar_title": "Restrictive Conditions: Kizárólag abban az esetben, Amennyiben, and Kivéve ha",
            "grammar_skill": "c1-legal-conditions",
            "goals": [
                "I can structure conditional restrictions using *kizárólag abban az esetben, amennyiben*.",
                "I can draft legal exceptions using *kivéve, ha* and *azzal a feltétellel, hogy*.",
                "I can eliminate semantic ambiguity in multi-tiered legal caveats."
            ],
            "vocab": [
                {"lemma": "amennyiben", "translation": "insofar as, provided that, in case", "pos": "conjunction"},
                {"lemma": "kizárólag abban az esetben", "translation": "solely in the case that", "pos": "expression"},
                {"lemma": "azzal a feltétellel, hogy", "translation": "on the condition that", "pos": "expression"},
                {"lemma": "kivéve, ha", "translation": "unless, except if", "pos": "expression"},
                {"lemma": "feltéve, hogy", "translation": "provided that, on condition that", "pos": "expression"},
                {"lemma": "jogvesztés", "translation": "forfeiture of rights", "pos": "noun"},
                {"lemma": "kikötés", "translation": "stipulation, covenant, clause", "pos": "noun"},
                {"lemma": "megtámadható", "translation": "voidable, contestable", "pos": "adjective"}
            ],
            "gr_text1": "Ambiguity in law causes catastrophic litigation. Formal drafting uses strict correlatives: *kizárólag abban az esetben... amennyiben* (solely in the case that / insofar as) establishes an exhaustive necessary condition.",
            "gr_text2": "Negative exceptions are introduced by *kivéve, ha* followed by indicative or potential verb forms, precisely delineating the boundaries of lawful conduct.",
            "gr_table": [
                ["Kizárólag abban az esetben, amennyiben a feltételek maradéktalanul teljesülnek...", "Solely in the event that the conditions are completely met..."],
                ["A szerződés érvényes, kivéve, ha a jogszabály írásbeli formát ír elő.", "The contract is valid, unless statutory law prescribes written form."],
                ["Hozzájárulását adja, azzal a feltétellel, hogy a költségeket megtérítik.", "Grants consent, on condition that costs are reimbursed."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Melyik kötőszó vezet be szabatos jogi feltételt a 'ha' helyett?", ["amennyiben", "mert", "pedig"], 0, ["c1-07-vocab"]),
                fb("grammar", "controlled", "A felmondási jog gyakorolható, _____ a bérlő a fizetési felszólításnak határidőre nem tesz eleget. (provided that / amennyiben)", "amennyiben", "The right of termination may be exercised, provided that the tenant does not comply with the payment notice on time.", ["c1-legal-conditions"]),
                match("vocabulary", "controlled", [["amennyiben", "insofar as / provided that"], ["kivéve, ha", "unless / except if"], ["jogvesztés", "forfeiture of rights"], ["kikötés", "stipulation"]], ["c1-07-vocab"]),
                fb("grammar", "practice", "A megállapodás módosítása _____ abban az esetben hatályos, amennyiben mindkét fél írásban megerősíti. (solely / kizárólag)", "kizárólag", "The modification of the agreement is effective solely in the event that both parties confirm in writing.", ["c1-legal-conditions"]),
                sb("grammar", "practice", ["A", "nyilatkozat", "érvényes,", "kivéve,", "ha", "a", "fél", "jogosulatlanul", "járt", "el."], ["A", "nyilatkozat", "érvényes,", "kivéve,", "ha", "a", "fél", "jogosulatlanul", "járt", "el."], "The statement is valid, unless the party acted without authorization.", ["c1-legal-conditions"]),
                dc("dialogue", [
                    {"speaker": "Bíró", "text": "Hivatkozhat-e az alperes a határidő elmulasztására?"},
                    {"speaker": "Felperes", "text": "Nem, mert a mulasztás jogvesztéssel jár, _____ igazolási kérelmet nem nyújt be."},
                ], ["kivéve ha", "mivelhogy", "ezért"], 0, ["c1-legal-conditions"]),
                sw("production", [{"prompt": "Draft a legal clause restricting liability using 'kizárólag abban az esetben, amennyiben'.", "answer": "A vállalkozó kizárólag abban az esetben tartozik felelősséggel, amennyiben a kár közvetlen szándékosságból ered."}], ["c1-legal-conditions"]),
                mc("grammar", "check", "Melyik megfogalmazás zárja ki a legvilágosabban az értelmezési kétségeket?", [
                    "A jogorvoslati kérelem kizárólag határidőben nyújtható be, azzal a feltétellel, hogy tartalmazza a jogsérelem pontos megjelölését.",
                    "Ha van kedve, bejelentheti a problémát a határidő körül.",
                    "Bármikor lehet fellebbezni, nem számít semmi."
                ], 0, ["c1-legal-conditions"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-07-04",
            "title": "Normative Modality and Statutory Compliance",
            "grammar_title": "Normative Deontic Framing in Institutional Governance",
            "grammar_skill": "c1-normative-modality",
            "goals": [
                "I can formulate institutional compliance requirements using normative modality.",
                "I can employ passive-like impersonal predicates (*hatáskörébe tartozik, feladatát képezi*).",
                "I can articulate regulatory boundaries and jurisdictional limits in Hungarian."
            ],
            "vocab": [
                {"lemma": "hatáskör", "translation": "jurisdiction, scope of competence", "pos": "noun"},
                {"lemma": "illetékesség", "translation": "territorial jurisdiction, venue", "pos": "noun"},
                {"lemma": "összeférhetetlenség", "translation": "conflict of interest", "pos": "noun"},
                {"lemma": "feladatát képezi", "translation": "forms part of one's duty", "pos": "expression"},
                {"lemma": "hatáskörébe tartozik", "translation": "falls within one's jurisdiction", "pos": "expression"},
                {"lemma": "jogkövetkezmény", "translation": "legal consequence", "pos": "noun"},
                {"lemma": "szankció", "translation": "sanction, penalty", "pos": "noun"},
                {"lemma": "mellőzhetetlen", "translation": "indispensable, that cannot be bypassed", "pos": "adjective"}
            ],
            "gr_text1": "Institutional governance replaces personal agency with institutional functions: instead of saying 'the mayor decides', Hungarian administrative law states: *A döntéshozatal a polgármester kizárólagos hatáskörébe tartozik.*",
            "gr_text2": "Failure to observe jurisdictional boundaries (*hatáskör és illetékesség*) renders administrative decisions null and void (*semmis*), making compliance clauses (*mellőzhetetlen feltétel*) critical.",
            "gr_table": [
                ["A panasz elbírálása a felügyeleti szerv hatáskörébe tartozik.", "The adjudication of the complaint falls within the jurisdiction of the supervisory body."],
                ["Összeférhetetlenség fennállása esetén a döntéshozó köteles eljárni.", "In the event of a conflict of interest, the decision-maker is obligated to recuse himself."],
                ["A jogkövetkezmények alkalmazása mellőzhetetlen kötelesség.", "The application of legal consequences is an indispensable duty."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'hatáskör' fogalma a közigazgatásban?", ["Az adott hatóság által jogszabály alapján eldönthető ügyek körét.", "A hivatalnokok fizetését.", "A tárgyalóterem méretét."], 0, ["c1-07-vocab"]),
                fb("grammar", "controlled", "A környezetvédelmi bírság kiszabása a területi környezetvédelmi hatóság kizárólagos _____ tartozik. (falls within jurisdiction / hatáskörébe)", "hatáskörébe", "The imposition of an environmental fine falls within the exclusive jurisdiction of the regional environmental authority.", ["c1-normative-modality"]),
                match("vocabulary", "controlled", [["hatáskör", "jurisdiction / competence"], ["illetékesség", "venue / territorial competence"], ["összeférhetetlenség", "conflict of interest"], ["jogkövetkezmény", "legal consequence"]], ["c1-07-vocab"]),
                fb("grammar", "practice", "Az eljárási garanciák maradéktalan érvényesítése a jogállami működés _____ eleme. (indispensable / mellőzhetetlen)", "mellőzhetetlen", "The full enforcement of procedural guarantees is an indispensable element of rule-of-law functioning.", ["c1-normative-modality"]),
                sb("grammar", "practice", ["A", "törvényesség", "felügyelete", "a", "főügyészség", "kiemelt", "feladatát", "képezi."], ["A", "törvényesség", "felügyelete", "a", "főügyészség", "kiemelt", "feladatát", "képezi."], "The supervision of legality forms a highlighted part of the Chief Prosecutor's duty.", ["c1-normative-modality"]),
                dc("dialogue", [
                    {"speaker": "Hivatalnok", "text": "Eljárhatunk-e ebben az ügyben a szomszédos vármegyében?"},
                    {"speaker": "Osztályvezető", "text": "Nem, mivel az eset a mi területi _____ kívül esik."},
                ], ["illetékességünkön", "szabadságunkon", "ötleteinken"], 0, ["c1-normative-modality"]),
                sw("production", [{"prompt": "Write a formal statement declaring an institutional competence limit.", "answer": "A vitás kérdés eldöntése polgári bíróság hatáskörébe tartozik, így közigazgatási úton nem bírálható el."}], ["c1-normative-modality"]),
                mc("grammar", "check", "Melyik állítás fejezi ki legpontosabban a közigazgatási jogszerűség alapelvét?", [
                    "A közigazgatási szerv kizárólag a törvényben meghatározott hatáskörében és eljárási rendben járhat el.",
                    "A hatóság bármit megtehet, amiről úgy gondolja, hogy jó ötlet.",
                    "A jogszabályok csak baráti javaslatok a hivataloknak."
                ], 0, ["c1-normative-modality"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-07-05",
            "title": "Classical Liberal Statecraft: Baron József Eötvös",
            "grammar_title": "Constitutional Philosophy and The Limits of State Power",
            "grammar_skill": "c1-constitutional-discourse",
            "goals": [
                "I can analyze Baron József Eötvös's classical liberal philosophy of state power.",
                "I can evaluate 19th-century Hungarian constitutional concepts (liberty, equality, nationality).",
                "I can synthesize abstract constitutional principles in sophisticated prose."
            ],
            "vocab": [
                {"lemma": "államhatalom", "translation": "state power", "pos": "noun"},
                {"lemma": "jogállam", "translation": "rule of law, constitutional state", "pos": "noun"},
                {"lemma": "egyéni szabadság", "translation": "individual liberty", "pos": "noun"},
                {"lemma": "önkényuralom", "translation": "autocracy, tyranny, arbitrary rule", "pos": "noun"},
                {"lemma": "korlát", "translation": "constraint, barrier, limit", "pos": "noun"},
                {"lemma": "törvény előtti egyenlőség", "translation": "equality before the law", "pos": "noun"},
                {"lemma": "kormányforma", "translation": "form of government", "pos": "noun"},
                {"lemma": "egyensúly", "translation": "equilibrium, balance", "pos": "noun"}
            ],
            "gr_text1": "Baron József Eötvös (1813–1871) was Hungary's premier constitutional philosopher. In his magnum opus *A XIX. század uralkodó eszméinek befolyása az államra*, he warned that popular sovereignty without institutional counterweights leads to tyranny.",
            "gr_text2": "His Hungarian is characterized by sweeping European vision, balanced syntactic antithesis, and an unyielding commitment to individual liberty constrained by constitutional law.",
            "gr_table": [
                ["A szabadság, egyenlőség és nemzetiség hármas eszméje...", "The triple ideas of liberty, equality, and nationality..."],
                ["Az államhatalom korlátai mint a polgári béke zálogai...", "The limits of state power as the pledges of civil peace..."],
                ["A törvény előtti egyenlőség nem válhat az egyén elnyomásává.", "Equality before the law must not become the oppression of the individual."]
            ],
            "classic_story": {
                "slug": "c1-07-eotvos",
                "author": "Eötvös József",
                "work": "A XIX. század uralkodó eszméinek befolyása az államra (1851–1854)",
                "title": "A szabadság korlátai és az államhatalom mérlege",
                "summary": "Baron József Eötvös's timeless analysis of the delicate balance between state authority, individual liberty, and constitutional counterweights.",
                "characters": ["Eötvös József"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor az 1848-as forradalmak lángja Európa-szerte ellobbant, és a remények helyét a katonai elnyomás és az önkényuralom vette át, báró Eötvös József nem a kétségbeesésnek adta át magát. Emigrációjában tollat ragadott, hogy megírja a magyar és az európai politikai gondolkodás egyik legnagyobb szabású államelméleti művét: A XIX. század uralkodó eszméinek befolyása az államra című monumentális értekezést."},
                    {"type": "narration", "text": "Eötvös felismerte korának legmélyebb paradoxonát: a tizenkilencedik század három vezéreszméje – a szabadság, az egyenlőség és a nemzetiség – látszólagos harmóniájuk ellenére szüntelen belső harcban áll egymással. Ha az egyenlőség vágya korlátlan hatalmat ad az állam kezébe, az egyenlősítés szükségszerűen eltiporja az egyéni szabadságot; ha pedig a nemzeti kizárólagosság válik abszolút elvvé, az szétzúzza a polgárok közötti testvériséget."},
                    {"type": "narration", "text": "A mű legfőbb tanulsága ma is eleven: a szabadság igazi garanciája nem a hatalom birtokosainak jóakaratában, hanem az államhatalom intézményes korlátaiban rejlik. Egyetlen kormányzat sem követelhet magának abszolút felhatalmazást a közjó nevében sem. A jogállam lényege az autonómiák tisztelete: a szabad önkormányzatok, a független bíróságok és az egyén elidegeníthetetlen méltósága."},
                    {"type": "narration", "text": "Eötvös emelkedett mondatai a mai olvasót is arra figyelmeztetik, hogy a jogállamiság nem statikus állapot, hanem szüntelen éberséget igénylő egyensúlyozás. Csak az az állam maradhat szabad, amely képes önnön hatalmának gátat szabni a törvény uralma előtt."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi képezi a jogállamiság lényegét Eötvös József gondolatrendszerében?", ["Az államhatalom szigorú intézményes korlátai és az egyéni autonómiák védelme.", "Az uralkodó korlátlan akarata.", "A törvények tetszőleges mellőzése."], 0, ["c1-07-vocab"]),
                fb("grammar", "controlled", "Eötvös szerint az államhatalom nem válhat korlátlanná, mert a fékek hiánya elkerülhetetlenül _____ torkollik. (tyranny / önkényuralomba)", "önkényuralomba", "According to Eötvös, state power must not become unlimited, because the lack of checks inevitably culminates in tyranny.", ["c1-constitutional-discourse"]),
                match("vocabulary", "controlled", [["államhatalom", "state power"], ["jogállam", "rule of law"], ["egyéni szabadság", "individual liberty"], ["önkényuralom", "arbitrary rule / tyranny"]], ["c1-07-vocab"]),
                mc("reading", "practice", "Miért áll Eötvös szerint belső feszültségben a szabadság és az egyenlőség eszméje?", [
                    "Mert ha az állam mindenáron egyenlősíteni akar, ahhoz korlátlan hatalom kell, ami eltiporja a szabadságot.",
                    "Mert a két szó ugyanazt jelenti a szótárban.",
                    "Mert a forradalmakban senki sem akart egyenlőséget."
                ], 0, None),
                sb("grammar", "practice", ["A", "szabadság", "valódi", "záloga", "a", "hatalom", "törvényes", "korlátozásában", "rejlik."], ["A", "szabadság", "valódi", "záloga", "a", "hatalom", "törvényes", "korlátozásában", "rejlik."], "The true pledge of freedom lies in the lawful limitation of power.", ["c1-constitutional-discourse"]),
                sw("production", [{"prompt": "Summarize Eötvös József's warning about state power in two sentences.", "answer": "Eötvös figyelmeztetése szerint a korlátlan államhatalom még a legnemesebb eszmék nevében is önkényuralomhoz vezet. A valódi szabadság feltétele a független intézmények és az egyéni jogok megkérdőjelezhetetlen védelme."}], ["c1-constitutional-discourse"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legméltóbban Eötvös állambölcseletét?", [
                    "Csak az az állam maradhat szabad, amely önnön hatalmának intézményes gátat szab a jog uralma előtt.",
                    "A legerősebb hadsereggel rendelkező állam mindig a legszabadabb.",
                    "A törvényeket nem kell betartani, ha forradalom van."
                ], 0, ["c1-constitutional-discourse"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(7, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        7,
        "core",
        "c1-07-consolidation",
        core_title,
        [
            "I can manipulate normative participles (-andó/-endő) with grammatical accuracy.",
            "I can draft legal entitlement and duty formulas (jogosult, köteles, terheli).",
            "I can formulate restrictive legal clauses and analyze Eötvös's constitutional philosophy."
        ],
        [
            mc("grammar", "recognize", "Melyik végződés fejez ki kötelező érvényű normatív melléknévi igenevet?", [
                "-andó / -endő",
                "-hatatlan / -hetetlen",
                "-kodó / -kedő"
            ], 0, ["c1-normative-participles"]),
            mc("grammar", "recognize", "Milyen igét használ a jogi szaknyelv a kötelezettség alanyának kifejezésére?", [
                "terheli a kötelezettség",
                "szalad a kötelezettség után",
                "alszik a kötelezettségen"
            ], 0, ["c1-statutory-predicates"]),
            match("vocabulary", "recognize", [["alkalmazandó", "applicable / to be applied"], ["jogosult", "entitled"], ["hatáskör", "jurisdiction"], ["jogállam", "constitutional state"], ["jogorvoslat", "legal remedy"]], ["c1-07-vocab"]),
            fb("vocabulary", "recall", "A bíróság döntése mindenki számára kötelező és haladéktalanul _____. (to be executed / végrehajtandó)", "végrehajtandó", "The court's decision is binding and to be executed without delay for everyone.", ["c1-07-vocab"]),
            fb("vocabulary", "recall", "A kártérítés megfizetése a károkozót _____. (burdens / terheli)", "terheli", "The payment of damages burdens the tortfeasor.", ["c1-07-vocab"]),
            fb("grammar", "recall", "A szerződés módosítása _____ abban az esetben hatályos, amennyiben írásba foglalják. (solely / kizárólag)", "kizárólag", "The modification of the contract is effective solely in the event that it is recorded in writing.", ["c1-legal-conditions"]),
            fb("grammar", "context", "A döntéshozatal a bíróság kizárólagos _____ tartozik. (jurisdiction / hatáskörébe)", "hatáskörébe", "Decision making falls within the exclusive jurisdiction of the court.", ["c1-normative-modality"]),
            fb("grammar", "context", "Eötvös szerint az állam nem válhat korlátlanná, mert a fékek hiánya _____ vezet. (to tyranny / önkényuralomhoz)", "önkényuralomhoz", "According to Eötvös the state cannot become limitless, because the lack of checks leads to tyranny.", ["c1-constitutional-discourse"]),
            mc("grammar", "context", "Melyik megfogalmazás alkalmaz helyesen megszorító jogi feltételt?", [
                "A kérelem teljesíthető, kivéve, ha az ügyfél nem fizeti meg az eljárási illetéket.",
                "A kérelem biztosan jó lesz, kivéve mert nem.",
                "Mindenki kaphat mindent, kivéve aki ott van."
            ], 0, ["c1-legal-conditions"]),
            sb("grammar", "produce", ["A", "jogállam", "alapja", "a", "hatalom", "intézményes", "korlátozása", "és", "az", "egyéni", "méltóság."], ["A", "jogállam", "alapja", "a", "hatalom", "intézményes", "korlátozása", "és", "az", "egyéni", "méltóság."], "The foundation of the rule of law is the institutional limitation of power and individual dignity.", ["c1-constitutional-discourse"]),
            sw("production", [{"prompt": "Draft a formal legal instruction combining a normative participle and a jurisdictional clause.", "answer": "A határozatban foglalt kötelezettségek maradéktalanul végrehajtandók, amennyiben az ügy az eljáró hatóság törvényes hatáskörébe tartozik."}], ["c1-normative-participles"]),
            sw("production", [{"prompt": "Write a critical reflection on Baron Eötvös's constitutional thought.", "answer": "Báró Eötvös József állambölcselete bebizonyította, hogy a törvényes fékek és egyensúlyok rendszere nélkül még a népfelség is a zsarnokság eszközévé válhat."}], ["c1-constitutional-discourse"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-jogallamisag)
    # ----------------------------------------------------
    slug = "jogallamisag"
    disc_intro = [
        "The Hungarian constitutional tradition is among the oldest in Europe. It spans eight centuries: from the Arpadian Golden Bull (Aranybulla, 1222) through Werbőczy's Tripartitum, the 1848 April Laws, the historical constitution, to post-1989 Constitutional Court jurisprudence.",
        "In this unit, you will examine the conceptual and rhetorical architecture of Hungarian constitutionalism, the tension between the historic unwritten constitution and codified fundamental law, and the ongoing European debates on the rule of law."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Golden Bull of 1222: The Resistance Clause",
            "grammar_title": "The Right of Resistance and Early Constitutional Compacts",
            "grammar_skill": "c1-constitutional-discourse",
            "goals": [
                "I can analyze the historical significance of the Golden Bull of 1222 (*Aranybulla*).",
                "I can evaluate the medieval resistance clause (*ellenállási záradék*) as a constitutional check.",
                "I can use archaic and modern constitutional vocabulary in parallel analysis."
            ],
            "vocab": [
                {"lemma": "Aranybulla", "translation": "Golden Bull of 1222", "pos": "noun"},
                {"lemma": "ellenállási záradék", "translation": "resistance clause (jus resistendi)", "pos": "noun"},
                {"lemma": "királyi önkény", "translation": "royal tyranny / arbitrary royal rule", "pos": "noun"},
                {"lemma": "szabadságlevél", "translation": "charter of liberties", "pos": "noun"},
                {"lemma": "nemesi kiváltság", "translation": "noble privilege", "pos": "noun"},
                {"lemma": "hűtlenség", "translation": "treason, disloyalty", "pos": "noun"},
                {"lemma": "sértetlenség", "translation": "inviolability, integrity", "pos": "noun"},
                {"lemma": "alku", "translation": "compact, bargain, compromise", "pos": "noun"}
            ],
            "gr_text1": "Issued by King Andrew II in 1222, just seven years after the Magna Carta, the *Aranybulla* was Hungary's seminal charter of liberties (*szabadságlevél*). Its famous 31st article granted the nobility the legal right of resistance (*jus resistendi*).",
            "gr_text2": "Crucially, resistance against an unlawful monarch was not considered treason (*hűtlenség*), but a lawful act of constitutional preservation (*a törvények védelme*).",
            "gr_table": [
                ["Az Aranybulla mint az alkotmányos fejlődés sarokköve...", "The Golden Bull as the cornerstone of constitutional evolution..."],
                ["Az ellenállási jog törvénybe iktatása a királyi önkénnyel szemben...", "Enshrining the right of resistance against royal tyranny..."],
                ["A nemesség jogainak és sértetlenségének biztosítása...", "Guaranteeing the rights and inviolability of the nobility..."]
            ],
            "world_story_seg": {
                "seg_slug": "aranybulla",
                "title": "Az Aranybulla és az ellenállás joga (1222)",
                "summary": "King Andrew II issues the Golden Bull of 1222, establishing the legal right of the nobility to resist royal overreach.",
                "paragraphs": [
                    {"type": "narration", "text": "1222 tavaszán a székesfehérvári királyi törvénynapon pattanásig feszült a hangulat. II. András király mértéktelen birtokadományozásai és idegen kegyencei felbőszítették a királyi servienseket és a bárókat. A fegyveres nemesség gyűrűjében az uralkodó kénytelen volt pecsétjét adni arra a harmincegy cikkelyből álló oklevélre, amely Aranybulla néven vonult be a történelembe."},
                    {"type": "narration", "text": "Az oklevél legforradalmibb része a híres harmincegyedik cikkely, az úgynevezett ellenállási záradék (jus resistendi) volt. Ez kimondta, hogy amennyiben a király vagy utódai megszegnék az oklevélben biztosított szabadságjogokat, a püspökök, urak és nemesek mindörökké jogosultak fegyverrel is ellenszegülni anélkül, hogy a hűtlenség bűnébe esnének. A törvény felette állt magának a királynak is."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jogot biztosított az Aranybulla 31. cikkelye a nemességnek?", ["A fegyveres ellenállás jogát a törvényszegő királlyal szemben.", "A király teljes adómentességét.", "A külföldre vándorlás jogát."], 0, ["c1-jogallamisag-vocab"]),
                fb("grammar", "controlled", "Az Aranybulla kimondta, hogy a királyi jogsértéssel szembeni fellépés nem minősül _____ vétkének. (treason / hűtlenség)", "hűtlenség", "The Golden Bull declared that taking action against royal rights violations does not qualify as the sin of treason.", ["c1-constitutional-discourse"]),
                match("vocabulary", "controlled", [["Aranybulla", "Golden Bull (1222)"], ["ellenállási záradék", "resistance clause"], ["királyi önkény", "royal tyranny"], ["szabadságlevél", "charter of liberties"]], ["c1-jogallamisag-vocab"]),
                sb("grammar", "practice", ["A", "törvényesség", "védelmében", "az", "ellenállás", "nem", "bűn,", "hanem", "kötelesség."], ["A", "törvényesség", "védelmében", "az", "ellenállás", "nem", "bűn,", "hanem", "kötelesség."], "In defense of legality, resistance is not a sin, but a duty.", ["c1-constitutional-discourse"]),
                sw("production", [{"prompt": "Explain the significance of the 'ellenállási záradék' in Hungarian constitutional history.", "answer": "Az ellenállási záradék megteremtette a királyi hatalom jogi korlátozásának elvét, rögzítve, hogy a törvények és az alkotmányos szokások a mindenkori uralkodó felett állnak."}], ["c1-constitutional-discourse"]),
                mc("grammar", "check", "Melyik állítás világítja meg legpontosabban az Aranybulla jogtörténeti értékét?", [
                    "A korai európai alkotmányfejlődésben az írott szabadságlevél rögzítette a hatalom és az alattvalók szerződéses viszonyát.",
                    "Egyszerű mezőgazdasági szerződés volt a jobbágyok között.",
                    "Semmilyen hatása nem volt a magyar történelemre."
                ], 0, ["c1-constitutional-discourse"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Historic Constitution vs. Codification",
            "grammar_title": "The Doctrine of the Holy Crown and Unwritten Constitutionalism",
            "grammar_skill": "c1-constitutional-discourse",
            "goals": [
                "I can analyze the concept of Hungary's unwritten 'Historic Constitution' (*történeti alkotmány*).",
                "I can explain the Doctrine of the Holy Crown (*Szent Korona-tan*) as legal entity.",
                "I can debate the merits of codified basic laws versus common law constitutional custom."
            ],
            "vocab": [
                {"lemma": "történeti alkotmány", "translation": "historic constitution (unwritten)", "pos": "noun"},
                {"lemma": "kartális alkotmány", "translation": "codified / written constitution", "pos": "noun"},
                {"lemma": "Szent Korona-tan", "translation": "Doctrine of the Holy Crown", "pos": "noun"},
                {"lemma": "jogfolytonosság", "translation": "legal continuity", "pos": "noun"},
                {"lemma": "szokásjog", "translation": "customary law, common law", "pos": "noun"},
                {"lemma": "közjogi berendezkedés", "translation": "public law framework / order", "pos": "noun"},
                {"lemma": "hatalommegosztás", "translation": "separation of powers", "pos": "noun"},
                {"lemma": "alaptörvény", "translation": "fundamental law, basic law", "pos": "noun"}
            ],
            "gr_text1": "Unlike post-revolutionary France or the United States, Hungary did not possess a single written constitution until 1949. Instead, like Great Britain, it operated under a *történeti alkotmány* (Historic Constitution) composed of fundamental statutes and centuries of customary law (*szokásjog*).",
            "gr_text2": "Central to this system was the *Szent Korona-tan*: the Holy Crown was not an object of jewelry, but a juristic person representing the state, uniting monarch and nation (*a korona tagjai*).",
            "gr_table": [
                ["A magyar történeti alkotmány évezredes fejlődése...", "The millennial development of the Hungarian historic constitution..."],
                ["A Szent Korona mint a nemzeti szuverenitás megtestesítője...", "The Holy Crown as the embodiment of national sovereignty..."],
                ["Jogfolytonosság és szokásjogi hagyomány a közjogban...", "Legal continuity and customary legal tradition in public law..."]
            ],
            "world_story_seg": {
                "seg_slug": "szentkorona",
                "title": "A Szent Korona-tan és a történeti alkotmány",
                "summary": "How medieval customary law and Werbőczy's Tripartitum shaped Hungary's unique unwritten constitutional doctrine.",
                "paragraphs": [
                    {"type": "narration", "text": "Werbőczy István 1514-ben összeállított Hármaskönyve (Tripartitum) évszázadokra kőbe véste a magyar szokásjogot. Ebben teljesedett ki a Szent Korona-tan klasszikus elmélete: a király és a nemzet a korona misztikus testének tagjai. A hatalom nem kizárólag a királyé, és nem kizárólag a rendeké, hanem a Szent Koronáé, amely az állam jogi személyiségét hordozza."},
                    {"type": "narration", "text": "Ez a történeti alkotmányos berendezkedés páratlan rugalmasságot biztosított a magyar közjognak. Nem egy papírlap rögzítette a jogokat, hanem az évszázadok során kiérlelt törvények és szokások szerves szövete, amely a legnehezebb hódoltsági és elnyomó korszakokban is a nemzeti önazonosság végső menedékét jelentette."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelentett a 'történeti alkotmány' fogalma a magyar jogfejlődésben?", ["Íratlan, törvényekből és szokásjogból szervesen építkező alkotmányos rendszert.", "Egyetlen nap alatt írt modern alkotmánykönyvet.", "Kizárólag külföldi törvények átvételét."], 0, ["c1-jogallamisag-vocab"]),
                fb("grammar", "controlled", "A magyar közjog felfogásában a Szent Korona nem ékszer, hanem az állami szuverenitást megtestesítő jogi _____. (entity / személyiség)", "személyiség", "In the conception of Hungarian public law, the Holy Crown is not a jewel, but a legal personality embodying state sovereignty.", ["c1-constitutional-discourse"]),
                match("vocabulary", "controlled", [["történeti alkotmány", "historic constitution"], ["szokásjog", "customary law"], ["jogfolytonosság", "legal continuity"], ["alaptörvény", "fundamental law"]], ["c1-jogallamisag-vocab"]),
                sb("grammar", "practice", ["A", "Szent", "Korona-tan", "a", "király", "és", "a", "nemzet", "szerves", "egységét", "hirdette."], ["A", "Szent", "Korona-tan", "a", "király", "és", "a", "nemzet", "szerves", "egységét", "hirdette."], "The Doctrine of the Holy Crown proclaimed the organic unity of king and nation.", ["c1-constitutional-discourse"]),
                sw("production", [{"prompt": "Contrast the historic unwritten constitution with a codified written constitution.", "answer": "Míg a kartális alkotmány egyetlen írott alaptörvényben rögzíti a közjogi kereteket, addig a történeti alkotmány évszázadok törvényeinek és szokásjogának szerves folytonosságára épül."}], ["c1-constitutional-discourse"]),
                mc("grammar", "check", "Melyik állítás határozza meg legpontosabban a jogfolytonosság szerepét?", [
                    "A jogállami átmenetek során biztosítja az intézmények és jogszabályok törvényes működését és stabilitását.",
                    "Azt jelenti, hogy soha semmilyen törvényen nem szabad változtatni.",
                    "A jogfolytonosság a forradalmi zűrzavar előidézését jelenti."
                ], 0, ["c1-constitutional-discourse"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "The April Laws of 1848: The Birth of Modern Constitutionalism",
            "grammar_title": "The 1848 Constitutional Turning Point and Parliamentary Responsibility",
            "grammar_skill": "c1-constitutional-discourse",
            "goals": [
                "I can evaluate the 1848 April Laws (*áprilisi törvények*) as the foundation of modern civic Hungary.",
                "I can analyze parliamentary executive responsibility and civic equality.",
                "I can describe the abolition of serfdom and censorship using advanced historical discourse."
            ],
            "vocab": [
                {"lemma": "áprilisi törvények", "translation": "April Laws of 1848", "pos": "noun"},
                {"lemma": "felelős minisztérium", "translation": "responsible ministry / cabinet", "pos": "noun"},
                {"lemma": "jobbágyfelszabadítás", "translation": "emancipation of serfs", "pos": "noun"},
                {"lemma": "közteherviselés", "translation": "universal proportional taxation", "pos": "noun"},
                {"lemma": "sajtószabadság", "translation": "freedom of the press", "pos": "noun"},
                {"lemma": "népképviselet", "translation": "popular representation", "pos": "noun"},
                {"lemma": "cenzúra", "translation": "censorship", "pos": "noun"},
                {"lemma": "polgári átalakulás", "translation": "civic / bourgeois transformation", "pos": "noun"}
            ],
            "gr_text1": "The April Laws sanctioning the 1848 Revolution transformed Hungary from a feudal estates monarchy into a modern constitutional democracy in just three weeks without bloodshed.",
            "gr_text2": "The cornerstone was Act III of 1848, creating a government responsible to parliament (*felelős minisztérium*), ending centuries of Viennese absolutist decrees.",
            "gr_table": [
                ["A feudális kiváltságok felszámolása és a polgári átalakulás...", "The abolition of feudal privileges and the civic transformation..."],
                ["Általános közteherviselés és jobbágyfelszabadítás...", "Universal taxation and the emancipation of serfs..."],
                ["Népképviseleti országgyűlés és független felelős kormány...", "Popular representative parliament and independent responsible government..."]
            ],
            "world_story_seg": {
                "seg_slug": "aprilitorvenyek",
                "title": "Az 1848-as áprilisi törvények és a polgári jogállam",
                "summary": "The enactment of the 31 articles of the April Laws laying the groundwork for modern Hungarian civic statehood.",
                "paragraphs": [
                    {"type": "narration", "text": "1848. április 11-én Pozsonyban V. Ferdinánd király szentesítette az utolsó rendi országgyűlés által megalkotott harmincegy törvénycikket. Ezzel egyetlen tollvonással véget ért a feudalizmus korszaka Magyarországon. A jobbágyfelszabadítás azonnal több millió parasztot emelt szabad, birtokos polgárrá, miközben a közteherviselés eltörölte a nemesség adómentességét."},
                    {"type": "narration", "text": "Az áprilisi törvények igazi mesterműve a független magyar felelős minisztérium megalapítása volt Batthyány Lajos vezetésével. A királyi rendeletek ettől kezdve kizárólag a miniszterek ellenjegyzésével váltak érvényessé, a végrehajtó hatalom pedig a választott népképviseleti országgyűlésnek tartozott felelősséggel. Megszületett a modern magyar alkotmányos jogállam."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Melyik vívmány tette a kormányt az országgyűlésnek felelőssé 1848-ban?", ["A független, felelős magyar minisztérium intézménye.", "A nemesi adómentesség visszaállítása.", "A királyi cenzúra bevezetése."], 0, ["c1-jogallamisag-vocab"]),
                fb("grammar", "controlled", "A jobbágyfelszabadítás és az általános _____ megteremtette a polgári egyenlőség alapjait. (universal taxation / közteherviselés)", "közteherviselés", "The emancipation of serfs and universal taxation created the foundations of civic equality.", ["c1-constitutional-discourse"]),
                match("vocabulary", "controlled", [["közteherviselés", "universal taxation"], ["jobbágyfelszabadítás", "emancipation of serfs"], ["népképviselet", "popular representation"], ["sajtószabadság", "freedom of the press"]], ["c1-jogallamisag-vocab"]),
                sb("grammar", "practice", ["A", "miniszteri", "ellenjegyzés", "nélkül", "a", "királyi", "rendelet", "érvénytelen", "volt."], ["A", "miniszteri", "ellenjegyzés", "nélkül", "a", "királyi", "rendelet", "érvénytelen", "volt."], "Without ministerial countersignature, the royal decree was invalid.", ["c1-constitutional-discourse"]),
                sw("production", [{"prompt": "Summarize the significance of the 1848 April Laws in one sentence.", "answer": "Az 1848-as áprilisi törvények vérontás nélkül számolták fel a feudalizmust, megalapozva a népképviseleten és kormányzati felelősségen nyugvó polgári jogállamot."}], ["c1-constitutional-discourse"]),
                mc("grammar", "check", "Miért tekinthető az 1848-as fordulat a modern magyar jogállam születésének?", [
                    "Mert felszámolta a rendi előjogokat és törvény előtti polgári egyenlőséget hozott létre.",
                    "Mert visszatért a középkori feudális bíráskodáshoz.",
                    "Mert betiltotta a független újságírást."
                ], 0, ["c1-constitutional-discourse"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "The Post-1989 Constitutional Court: The Invisible Constitution",
            "grammar_title": "Judicial Review, Fundamental Rights, and the Invisible Constitution",
            "grammar_skill": "c1-constitutional-discourse",
            "goals": [
                "I can analyze the role of the Hungarian Constitutional Court (*Alkotmánybíróság*) in the democratic transition.",
                "I can explain László Sólyom's concept of the 'Invisible Constitution' (*láthatatlan alkotmány*).",
                "I can evaluate landmark rulings on capital punishment, human dignity, and freedom of expression."
            ],
            "vocab": [
                {"lemma": "Alkotmánybíróság", "translation": "Constitutional Court", "pos": "noun"},
                {"lemma": "láthatatlan alkotmány", "translation": "invisible constitution (jurisprudential doctrine)", "pos": "noun"},
                {"lemma": "emberi méltóság", "translation": "human dignity", "pos": "noun"},
                {"lemma": "normakontroll", "translation": "constitutional review of norms", "pos": "noun"},
                {"lemma": "arányossági teszt", "translation": "proportionality test", "pos": "noun"},
                {"lemma": "halálbüntetés", "translation": "death penalty, capital punishment", "pos": "noun"},
                {"lemma": "szólásszabadság", "translation": "freedom of speech", "pos": "noun"},
                {"lemma": "alapjog", "translation": "fundamental right", "pos": "noun"}
            ],
            "gr_text1": "Following the 1989 regime change, the Hungarian Constitutional Court under President László Sólyom became one of the most powerful constitutional courts in the world. Its hallmark was the 'actio popularis': anyone could challenge any law without proving personal standing.",
            "gr_text2": "Sólyom coined the doctrine of the *láthatatlan alkotmány* (invisible constitution): the idea that constitutional adjudication must follow a coherent, morally grounded system of fundamental principles that transcends the literal text of the written constitution.",
            "gr_table": [
                ["Az emberi méltósághoz való jog mint anyajog...", "The right to human dignity as a mother right..."],
                ["A halálbüntetés eltörlése alkotmánybírósági határozattal...", "The abolition of capital punishment by Constitutional Court ruling..."],
                ["A szükségességi és arányossági teszt alkalmazása az alapjogok korlátozásakor...", "Applying necessity and proportionality tests when limiting fundamental rights..."]
            ],
            "world_story_seg": {
                "seg_slug": "alkotmanybirosag",
                "title": "A rendszerváltás és a 'láthatatlan alkotmány'",
                "summary": "How the Hungarian Constitutional Court guided the peaceful transition to democracy through groundbreaking jurisprudence.",
                "paragraphs": [
                    {"type": "narration", "text": "1990-ben a rendszerváltó Magyarország békés átmenetének legfőbb őre az újonnan felállított Alkotmánybíróság lett. A Sólyom László vezette testület példátlan bátorsággal és szellemi szigorral látott munkához. Már az első évben meghozták történelmi döntésüket a halálbüntetés eltörléséről, kimondva, hogy az élethez és az emberi méltósághoz való jog elidegeníthetetlen és korlátozhatatlan 'anyajog'."},
                    {"type": "narration", "text": "Sólyom László megfogalmazta a 'láthatatlan alkotmány' elméletét: a testület nem pusztán a gyakran módosított alaptörvény betűjéhez igazodott, hanem az európai jogállamiság és az emberi méltóság elveiből épített fel egy koherens, szilárd értékrendszert. Ezzel a bíróság évtizedekre meghatározta a magyar demokrácia alapjogi kultúráját."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'láthatatlan alkotmány' koncepciója Sólyom László felfogásában?", ["Az Alkotmánybíróság határozataiból kibontakozó, az emberi jogokat koherens rendszerbe foglaló elveket.", "Egy titkos törvénykönyvet, amit senki sem láthat.", "A jogszabályok teljes eltörlését."], 0, ["c1-jogallamisag-vocab"]),
                fb("grammar", "controlled", "Az Alkotmánybíróság szerint az emberi _____ való jog minden más alapjog forrása és korlátja. (to dignity / méltósághoz)", "méltósághoz", "According to the Constitutional Court, the right to human dignity is the source and boundary of all other fundamental rights.", ["c1-constitutional-discourse"]),
                match("vocabulary", "controlled", [["Alkotmánybíróság", "Constitutional Court"], ["emberi méltóság", "human dignity"], ["normakontroll", "review of norms"], ["arányossági teszt", "proportionality test"]], ["c1-jogallamisag-vocab"]),
                sb("grammar", "practice", ["Az", "alapvető", "jogok", "korlátozása", "csak", "szükséges", "és", "arányos", "lehet."], ["Az", "alapvető", "jogok", "korlátozása", "csak", "szükséges", "és", "arányos", "lehet."], "The limitation of fundamental rights can only be necessary and proportionate.", ["c1-constitutional-discourse"]),
                sw("production", [{"prompt": "Explain the role of the proportionality test in fundamental rights adjudication.", "answer": "Az arányossági teszt biztosítja, hogy az állam kizárólag elkerülhetetlen kényszer esetén, a célhoz kötötten és a legkisebb mértékben korlátozhassa a polgárok alapvető jogait."}], ["c1-constitutional-discourse"]),
                mc("grammar", "check", "Miért volt korszakalkotó a Sólyom-bíróság halálbüntetést eltörlő határozata?", [
                    "Mert elvi alapon mondta ki az emberi élet és az emberi méltóság abszolút, sérthetetlen jellegét.",
                    "Mert pénzügyi okokra hivatkozva takarékoskodni akart az államkasszával.",
                    "Mert a törvényhozók elfelejtettek szavazni róla."
                ], 0, ["c1-constitutional-discourse"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Contemporary Rule of Law Debates in the European Context",
            "grammar_title": "Sovereignty, Constitutional Identity, and European Integration",
            "grammar_skill": "c1-constitutional-discourse",
            "goals": [
                "I can evaluate contemporary debates on the rule of law (*jogállamisági vita*) between Budapest and Brussels.",
                "I can analyze the legal concepts of 'constitutional identity' (*alkotmányos önazonosság*) and European primacy.",
                "I can formulate nuanced, high-register arguments on judicial independence and democratic checks."
            ],
            "vocab": [
                {"lemma": "alkotmányos identitás", "translation": "constitutional identity", "pos": "noun"},
                {"lemma": "jogállamisági mechanizmus", "translation": "rule of law mechanism / conditionality", "pos": "noun"},
                {"lemma": "bírói függetlenség", "translation": "judicial independence", "pos": "noun"},
                {"lemma": "szuverenitás", "translation": "sovereignty", "pos": "noun"},
                {"lemma": "európai jog elsőbbsége", "translation": "primacy of European law", "pos": "expression"},
                {"lemma": "fékek és ellensúlyok", "translation": "checks and balances", "pos": "expression"},
                {"lemma": "jogharmonizáció", "translation": "legal harmonization", "pos": "noun"},
                {"lemma": "demokratikus deficit", "translation": "democratic deficit", "pos": "noun"}
            ],
            "gr_text1": "In the 21st century, Hungarian constitutional discourse is shaped by the dialectic between national constitutional identity (*alkotmányos identitás*) and the supranational legal order of the European Union.",
            "gr_text2": "Key points of debate involve the rule of law conditionality mechanism (*kondicionalitási eljárás*), the limits of EU competence, and maintaining the institutional equilibrium of checks and balances (*fékek és ellensúlyok*).",
            "gr_table": [
                ["A nemzeti alkotmányos identitás védelme az uniós integrációban...", "Protecting national constitutional identity in EU integration..."],
                ["A bírói függetlenség és a fékek és ellensúlyok rendszere...", "Judicial independence and the system of checks and balances..."],
                ["A jogállamisági kritériumok és a pénzügyi kondicionalitás...", "Rule of law criteria and financial conditionality..."]
            ],
            "world_story_seg": {
                "seg_slug": "eu-jogallamisag",
                "title": "A jogállamiság európai horizontja és a jövő",
                "summary": "Contemporary European debates on constitutional identity, judicial autonomy, and the preservation of democratic norms.",
                "paragraphs": [
                    {"type": "narration", "text": "A huszonegyedik században a magyar közjogi gondolkodás új, globális kihívásokkal szembesült. Az Európai Unióhoz való csatlakozással a nemzeti szuverenitás és az európai jog primátusa közötti egyensúlyozás a politikai és jogi viták középpontjába került. Míg Brüsszel a jogállamiság univerzális mércéit és a bírói függetlenség védelmét hangsúlyozza, addig a nemzeti szuverenitás védelmezői a történelmi alkotmányos önazonosság primátusát vallják."},
                    {"type": "narration", "text": "Ez a párbeszéd nem a jogállamiság tagadása, hanem a demokrácia természetéről szóló mély filozófiai küzdelem. A nyolc évszázados magyar alkotmányos hagyomány – az Aranybullától az 1848-as törvényeken át a rendszerváltás vívmányaiig – arra tanít, hogy a hatalom korlátozása és az emberi méltóság tisztelete a magyar nemzeti identitás legmélyebb, elidegeníthetetlen alapköve."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Melyik fogalom jelöli a hatalmi ágak elválasztását és kölcsönös ellenőrzését?", ["fékek és ellensúlyok rendszere", "egyszemélyi döntéshozatal", "állami monopólium"], 0, ["c1-jogallamisag-vocab"]),
                fb("grammar", "controlled", "A modern európai jogállam működésének elengedhetetlen feltétele a bírói _____ védelme a végrehajtó hatalommal szemben. (independence / függetlenség)", "függetlenség", "The indispensable condition of modern European rule-of-law functioning is the protection of judicial independence against executive power.", ["c1-constitutional-discourse"]),
                match("vocabulary", "controlled", [["alkotmányos identitás", "constitutional identity"], ["szuverenitás", "sovereignty"], ["bírói függetlenség", "judicial independence"], ["fékek és ellensúlyok", "checks and balances"]], ["c1-jogallamisag-vocab"]),
                sb("grammar", "practice", ["A", "demokrácia", "lényege", "a", "hatalom", "átláthatósága", "és", "elszámoltathatósága."], ["A", "demokrácia", "lényege", "a", "hatalom", "átláthatósága", "és", "elszámoltathatósága."], "The essence of democracy is the transparency and accountability of power.", ["c1-constitutional-discourse"]),
                sw("production", [{"prompt": "Formulate a balanced perspective on national sovereignty vs. European legal integration.", "answer": "A sikeres integráció záloga a tagállami alkotmányos önazonosság tiszteletben tartása mellett a közös európai jogállami normák és a bírói függetlenség megkérdőjelezhetetlen védelme."}], ["c1-constitutional-discourse"]),
                mc("grammar", "check", "Mi a magyar alkotmányos hagyomány legfontosabb üzenete a modern kor számára?", [
                    "A hatalom intézményes korlátozása és az egyéni méltóság védelme a magyar történelmi identitás szerves része.",
                    "A hatalmat soha nem szabad ellenőrizni.",
                    "A jogállamiság csak felesleges akadály a kormányzás útjában."
                ], 0, ["c1-constitutional-discourse"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(7, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined world story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A magyar jogállamiság és alkotmányfejlődés krónikája",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive eight-century chronicle of Hungarian constitutionalism: from the Golden Bull (1222), the Historic Constitution and Holy Crown doctrine through the 1848 April Laws, Sólyom's Constitutional Court to contemporary European rule of law debates.",
            "paragraphs": [
                {"type": "narration", "text": "A magyar alkotmányos fejlődés Európa egyik legősibb és legkülönlegesebb közjogi hagyománya. 1222-ben, mindössze hét évvel az angol Magna Charta után megszületett az Aranybulla, amely a királyi önkénnyel szemben a fegyveres ellenállás törvényes jogát garantálta a nemességnek."},
                {"type": "narration", "text": "Az évszázadok során kiérlelődött íratlan 'történeti alkotmány' és a Szent Korona-tan kivételes jogi stabilitást kölcsönzött a nemzetnek. A hatalom forrása nem a király személye volt, hanem a Szent Korona misztikus teste, amely magában foglalta az uralkodót és a nemzet polgárait."},
                {"type": "narration", "text": "1848 tavaszán az áprilisi törvények egyetlen tollvonással számolták fel a feudalizmust. A jobbágyfelszabadítás, az általános közteherviselés és az országgyűlésnek felelős kormány megalapítása vérontás nélkül teremtette meg a modern polgári demokrácia jogi kereteit."},
                {"type": "narration", "text": "Az 1989-es békés rendszerváltást követően az Alkotmánybíróság a 'láthatatlan alkotmány' doktrínájával az emberi méltóság sérthetetlenségét tette a jogrendszer középpontjává, eltörölve a halálbüntetést és megszilárdítva az alapjogok védelmét."},
                {"type": "narration", "text": "Ez a nyolcszáz éves közjogi örökség ma a nemzeti szuverenitás és az európai jogállamisági normák termékeny párbeszédében él tovább, emlékeztetve arra, hogy a szabadság egyetlen tartós garanciája a jog uralma és a hatalom intézményes korlátozása."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        7,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze key turning points in Hungarian constitutional history (1222, 1514, 1848, 1989).",
            "I can decode unwritten constitutional doctrines (Historic Constitution, Holy Crown, Invisible Constitution).",
            "I can formulate sophisticated legal arguments on judicial independence and rule of law norms."
        ],
        [
            mc("grammar", "recognize", "Mi volt az Aranybulla legfontosabb közjogi újítása?", [
                "A királyi önkénnyel szembeni törvényes ellenállás joga (jus resistendi).",
                "A jobbágyok kötelező katonai szolgálata.",
                "A latin nyelv teljes betiltása."
            ], 0, ["c1-constitutional-discourse"]),
            mc("grammar", "recognize", "Mit fejez ki a 'Szent Korona-tan' a magyar közjogban?", [
                "Az állami szuverenitás és a nemzet szerves egységének jogi megtestesülését.",
                "Egy aranykorona piaci értékét.",
                "A középkori templomok építési szabályzatát."
            ], 0, ["c1-constitutional-discourse"]),
            match("vocabulary", "recognize", [["Aranybulla", "Golden Bull (1222)"], ["történeti alkotmány", "historic constitution"], ["közteherviselés", "universal taxation"], ["Alkotmánybíróság", "Constitutional Court"], ["bírói függetlenség", "judicial independence"]], ["c1-jogallamisag-vocab"]),
            fb("vocabulary", "recall", "1848-ban az áprilisi törvények megteremtették a parlamentnek felelős magyar _____ intézményét. (ministry / kormány / minisztérium)", "minisztérium", "In 1848 the April Laws created the institution of the Hungarian ministry responsible to parliament.", ["c1-jogallamisag-vocab"]),
            fb("vocabulary", "recall", "A Sólyom-bíróság történelmi döntésével eltörölte a _____ intézményét Magyarországon. (death penalty / halálbüntetés)", "halálbüntetés", "With a historic decision the Sólyom court abolished the institution of the death penalty in Hungary.", ["c1-jogallamisag-vocab"]),
            fb("grammar", "recall", "A jogállam működésének elengedhetetlen garanciája a hatalmi ágak elválasztása és a fékek és _____ rendszere. (balances / ellensúlyok)", "ellensúlyok", "The indispensable guarantee of the rule of law is the separation of branches of power and the system of checks and balances.", ["c1-constitutional-discourse"]),
            fb("grammar", "context", "A törvényhozó hatalom nem csorbíthatja a bírói _____ elvét. (independence / függetlenség)", "függetlenség", "The legislative power cannot curtail the principle of judicial independence.", ["c1-constitutional-discourse"]),
            fb("grammar", "context", "Az alapjogok védelmében az Alkotmánybíróság alkalmazza a szükségességi és _____ tesztet. (proportionality / arányossági)", "arányossági", "In defense of fundamental rights the Constitutional Court applies the necessity and proportionality test.", ["c1-constitutional-discourse"]),
            mc("grammar", "context", "Hogyan értelmezhető az alkotmányos önazonosság és az európai jog viszonya?", [
                "Egyensúlyozás a nemzeti történelmi hagyományok és a közös európai normák között.",
                "Az egyik fél teljes megsemmisítése.",
                "A törvények tetszőleges figyelmen kívül hagyása."
            ], 0, ["c1-constitutional-discourse"]),
            sb("grammar", "produce", ["A", "jog", "uralma", "minden", "politikai", "hatalom", "felett", "áll."], ["A", "jog", "uralma", "minden", "politikai", "hatalom", "felett", "áll."], "The rule of law stands above all political power.", ["c1-constitutional-discourse"]),
            sw("production", [{"prompt": "Write a critical evaluation of the 1848 April Laws.", "answer": "Az 1848-as áprilisi törvények zsenialitása abban állt, hogy a rendi elit önként mondott le kiváltságairól a polgári egyenlőség és a nemzeti szuverenitás megteremtése érdekében."}], ["c1-constitutional-discourse"]),
            sw("production", [{"prompt": "Formulate a concluding thought on eight centuries of Hungarian constitutionalism.", "answer": "A magyar alkotmányfejlődés legfőbb tanulsága, hogy a szabadság nem adottság, hanem intézményes garanciák és szüntelen polgári éberség által védett érték."}], ["c1-constitutional-discourse"])
        ]
    )
    print("=== Finished C1 Unit 7 ===")


if __name__ == "__main__":
    generate_unit_7()
