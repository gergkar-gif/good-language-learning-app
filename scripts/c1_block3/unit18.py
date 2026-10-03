#!/usr/bin/env python3
"""
Hungarian C1 Block 3 - Unit 18 Generator:
  - Track 1 (Core): Unit 18 — "Digital Sovereignty, Algorithmic Surveillance & Information Security" (c1-18)
  - Track 2 (Discourse): Unit 18 — "Cyber Warfare, Critical Infrastructure Protection & Citizen Resilience" (c1-kiberbiztonsag)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block3.registry_helper import register_unit


def generate_unit_18():
    print("=== Generating C1 Unit 18 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-18-vocab": {"kind": "vocabulary"},
        "c1-kiberbiztonsag-vocab": {"kind": "vocabulary"},
        "c1-adv-adversative-concessive-clauses": {"kind": "grammar"},
        "c1-infinitive-predicative-necessity": {"kind": "grammar"},
        "c1-adv-evaluative-parentheticals": {"kind": "grammar"},
        "c1-complex-modal-contingency": {"kind": "grammar"},
        "c1-adv-syntactic-focus-clefting": {"kind": "grammar"},
        "c1-discourse-threat-framing": {"kind": "grammar"},
        "c1-regulatory-compliance-syntax": {"kind": "grammar"},
        "c1-epistemic-uncertainty-markers": {"kind": "grammar"},
        "c1-adv-proportional-threat-correlatives": {"kind": "grammar"},
        "c1-adv-conclusive-synthesis-markers": {"kind": "grammar"},
    }
    new_titles = {
        "c1-18-vocab": "reading",
        "c1-kiberbiztonsag-vocab": "reading",
        "c1-adv-adversative-concessive-clauses": "adversative-concessive clauses expressing nuanced theoretical reservations in academic exposition",
        "c1-infinitive-predicative-necessity": "impersonal predicative constructions expressing systemic necessity with infinitival complements",
        "c1-adv-evaluative-parentheticals": "parenthetical evaluative markers modifying truth value and epistemic commitment",
        "c1-complex-modal-contingency": "complex adverbial expressions of structural contingency and mutual functional dependence",
        "c1-adv-syntactic-focus-clefting": "syntactic cleft structures and focus fronting in analytical argument contrast",
        "c1-discourse-threat-framing": "rhetorical threat-framing connectors characterizing cybersecurity risks and systemic vulnerabilities",
        "c1-regulatory-compliance-syntax": "deontic regulatory compliance structures establishing statutory audits and operational mandates",
        "c1-epistemic-uncertainty-markers": "epistemic uncertainty markers modulating attribution confidence in threat intelligence analysis",
        "c1-adv-proportional-threat-correlatives": "proportional correlative constructions analyzing systemic complexity and attack surface exposure",
        "c1-adv-conclusive-synthesis-markers": "strategic synthesis particles deriving definitive policy conclusions in national security doctrine",
    }
    
    core_title = "Digital Sovereignty, Algorithmic Surveillance & Information Security"
    core_stems = [f"c1-18-0{i}" for i in range(1, 6)] + ["c1-18-consolidation"]
    disc_title = "Cyber Warfare, Critical Infrastructure Protection & Citizen Resilience"
    disc_stems = [f"c1-kiberbiztonsag-0{i}" for i in range(1, 6)] + ["c1-kiberbiztonsag-consolidation"]
    
    register_unit(18, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-18)
    # ----------------------------------------------------
    core_intro = [
        "In the digital era, state sovereignty, industrial resilience, and fundamental human rights depend on cybersecurity, cryptographic architectures, and algorithmic integrity.",
        "In this unit, drawing on the foundational cybernetic reflections of Hungarian mathematician László Kalmár ('A kibernetika és az emberi gondolkodás határai', 1962), you will master the elevated technical, legal, and philosophical register of information security at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-18-01",
            "title": "Digital Sovereignty, Cloud Colonialism & Technological Autonomy",
            "grammar_title": "Adversative-Concessive Clauses Expressing Nuanced Theoretical Reservations in Academic Exposition",
            "grammar_skill": "c1-adv-adversative-concessive-clauses",
            "goals": [
                "I can evaluate digital sovereignty, data colonialism, and technological exposure (*digitális szuverenitás, adatgyarmatosítás, technológiai kitettség*).",
                "I can formulate nuanced theoretical reservations using adversative-concessive clauses (*jóllehet... mindazonáltal, ámbár... mégis, noha... semmiképp sem*).",
                "I can debate local cloud infrastructure vs. multinational platform reliance in academic Hungarian."
            ],
            "vocab": [
                {"lemma": "digitális szuverenitás", "translation": "digital sovereignty", "pos": "expression"},
                {"lemma": "adatgyarmatosítás", "translation": "data colonialism", "pos": "noun"},
                {"lemma": "technológiai kitettség", "translation": "technological exposure / vulnerability", "pos": "expression"},
                {"lemma": "felhőalapú infrastruktúra", "translation": "cloud-based infrastructure", "pos": "expression"},
                {"lemma": "adatlokalizáció", "translation": "data localization", "pos": "noun"},
                {"lemma": "digitális önrendelkezés", "translation": "digital self-determination", "pos": "expression"},
                {"lemma": "szuperszámítógép", "translation": "supercomputer", "pos": "noun"},
                {"lemma": "algoritmusos autonómia", "translation": "algorithmic autonomy", "pos": "expression"}
            ],
            "gr_text1": "Adversative-concessive clauses in C1 academic Hungarian introduce a recognized fact or concession in the subordinate clause, followed by an emphatic, restrictive, or counter-balancing reservation in the main clause: `Jóllehet a globális felhőszolgáltatók páratlan számítási kapacitást kínálnak, mindazonáltal a nemzeti adatlokalizáció hiánya elfogadhatatlan technológiai kitettséget teremt`.",
            "gr_text2": "Key paired connectors include `jóllehet... mindazonáltal`, `ámbár... mégsem`, `noha... ennek ellenére`, and `ugyan... mindamellett`.",
            "gr_table": [
                ["Jóllehet a digitalizáció rendkívüli gazdasági hatékonyságot teremt, mindazonáltal súlyos szuverenitási kockázatokat rejt magában.", "Although digitalization creates extraordinary economic efficiency, it nevertheless harbors grave sovereignty risks."],
                ["Ámbár az adatlokalizáció költséges beruházásokat igényel, mégsem mondhatunk le a nemzeti adatközpontok függetlenségéről.", "Although data localization requires costly investments, we still cannot renounce the independence of national data centers."],
                ["Noha a felhőalapú infrastruktúra kényelmes, ennek ellenére kiszolgáltatottá teszi az állami szerveket a külső technológiai monopóliumoknak.", "Even though cloud-based infrastructure is convenient, it nonetheless leaves state organs vulnerable to external tech monopolies."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'digitális szuverenitás' (digital sovereignty) fogalma?", [
                    "Egy állam vagy közösség képességét arra, hogy maga rendelkezzék digitális adatai, technológiai infrastruktúrája és szoftveres rendszerei felett.",
                    "A monitor fényerejének automatikus szabályozását.",
                    "Minden külföldi weboldal teljes betiltását gazdasági okokból."
                ], 0, ["c1-18-vocab"]),
                fb("grammar", "controlled", "_____ a felhőszolgáltatók gyors skálázhatóságot ígérnek, mindazonáltal a stratégiai adatok feletti ellenőrzés elvesztése végzetes lehet. (Although / Jóllehet)", "Jóllehet", "Although cloud providers promise rapid scalability, nevertheless the loss of control over strategic data can be fatal.", ["c1-adv-adversative-concessive-clauses"]),
                match("vocabulary", "controlled", [["adatgyarmatosítás", "technológiai monopóliumok adatelvonása"], ["adatlokalizáció", "szerverek kötelező országon belüli elhelyezése"], ["szuperszámítógép", "kiemelkedő tudományos számítási kapacitás"], ["technológiai kitettség", "külső beszállítóktól való sebezhető függés"]], ["c1-18-vocab"]),
                fb("grammar", "practice", "Ámbár a szoftverlicencek megvásárlása rövid távon olcsóbb, _____ garantálja a nemzeti informatikai önrendelkezést. (still / mégsem)", "mégsem", "Although purchasing software licenses is cheaper in the short term, it still does not guarantee national IT self-determination.", ["c1-adv-adversative-concessive-clauses"]),
                sb("grammar", "practice", ["Jóllehet", "az", "innováció", "gyorsul,", "mindazonáltal", "a", "kibertér", "szabályozatlan", "maradt."], ["Jóllehet", "az", "innováció", "gyorsul,", "mindazonáltal", "a", "kibertér", "szabályozatlan", "maradt."], "Although innovation is accelerating, nevertheless cyberspace has remained unregulated.", ["c1-adv-adversative-concessive-clauses"]),
                dc("dialogue", [
                    {"speaker": "Miniszteri biztos", "text": "Megbízhatunk a globális felhőszolgáltatók biztonsági ígéreteiben?"},
                    {"speaker": "Kiberbiztonsági szakértő", "text": "Jóllehet a titkosításuk fejlett, mindazonáltal az állami adatvagyont saját nemzeti _____ kell tartanunk."},
                ], ["adatközpontokban", "közösségi oldalakon", "nyilvános fórumokon"], 0, ["c1-adv-adversative-concessive-clauses"]),
                sw("production", [{"prompt": "Write an argument in defense of digital sovereignty using the 'jóllehet... mindazonáltal' structure.", "answer": "Jóllehet a globális technológiai platformok jelentős kényelmet biztosítanak, mindazonáltal az állami adatvagyon védelme elengedhetetlenné teszi a szuverén digitális infrastruktúra kiépítését."}], ["c1-adv-adversative-concessive-clauses"]),
                mc("grammar", "check", "Melyik páros kötőszó fejez ki emelkedett megengedő-szembeállító (adversative-concessive) viszonyt?", [
                    "jóllehet... mindazonáltal",
                    "ezért... mert",
                    "holott... mintha"
                ], 0, ["c1-adv-adversative-concessive-clauses"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-18-02",
            "title": "Critical Infrastructure, Industrial Control Systems & Grid Protection",
            "grammar_title": "Impersonal Predicative Constructions Expressing Systemic Necessity with Infinitival Complements",
            "grammar_skill": "c1-infinitive-predicative-necessity",
            "goals": [
                "I can analyze critical infrastructure protection and industrial control systems (*kritikus infrastruktúra, SCADA-rendszerek, kiberfizikai rendszerek*).",
                "I can express systemic necessity and institutional imperatives using impersonal predicative structures (*elengedhetetlen biztosítani, célszerű megfontolni, indokolt elkerülni*).",
                "I can discuss electrical grid cyber protection and supply chain resilience in formal discourse."
            ],
            "vocab": [
                {"lemma": "kritikus infrastruktúra", "translation": "critical infrastructure", "pos": "expression"},
                {"lemma": "ipari vezérlőrendszer", "translation": "industrial control system (ICS)", "pos": "expression"},
                {"lemma": "villamosenergia-hálózat", "translation": "electrical power grid", "pos": "noun"},
                {"lemma": "SCADA-rendszer", "translation": "SCADA system", "pos": "noun"},
                {"lemma": "üzemfolytonosság", "translation": "business / operational continuity", "pos": "noun"},
                {"lemma": "kiberfizikai rendszerek", "translation": "cyber-physical systems", "pos": "expression"},
                {"lemma": "ellátási lánc sebezhetősége", "translation": "supply chain vulnerability", "pos": "expression"},
                {"lemma": "redundáns architektúra", "translation": "redundant architecture", "pos": "expression"}
            ],
            "gr_text1": "In technical policy and institutional governance, Hungarian expresses non-personal systemic necessity using evaluative predicates governing an infinitive: `elengedhetetlen / nélkülözhetetlen / elkerülhetetlen / indokolt / célszerű + főnévi igenév`. Example: `Az üzemfolytonosság garantálásához elengedhetetlen kiépíteni a redundáns hálózati architektúrát`.",
            "gr_text2": "When the agent is specified, Hungarian employs a dative complement (`állami szerveknek / mérnököknek elengedhetetlen felkészülniük`) or remains purely impersonal.",
            "gr_table": [
                ["Elengedhetetlen biztosítani az ipari vezérlőrendszerek fizikai leválasztását a nyilvános internetről.", "It is indispensable to ensure the physical air-gapping of industrial control systems from the public internet."],
                ["Célszerű megfontolni a villamosenergia-hálózat redundáns vezérlési központjainak kialakítását.", "It is advisable to consider establishing redundant control centers for the electrical power grid."],
                ["Indokolt szigorúan ellenőrizni az ellátási láncba belépő hardverelemek eredetét.", "It is justified to rigorously inspect the origin of hardware components entering the supply chain."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mely létesítmények minősülnek 'kritikus infrastruktúrának' egy modern társadalomban?", [
                    "Azok a hálózatok és rendszerek (pl. áramhálózat, ivóvízellátás, kórházak, vasút), amelyek kiesése megbénítja a társadalom és gazdaság működését.",
                    "Kizárólag az autópályák melletti benzinkutak és pihenőhelyek.",
                    "A közösségi média hirdetési felületei."
                ], 0, ["c1-18-vocab"]),
                fb("grammar", "controlled", "A kibertámadások elhárításához _____ az ipari hálózatok folyamatos felügyeletét. (indispensable to ensure / elengedhetetlen biztosítani)", "elengedhetetlen biztosítani", "For repelling cyber attacks it is indispensable to ensure continuous monitoring of industrial networks.", ["c1-infinitive-predicative-necessity"]),
                match("vocabulary", "controlled", [["SCADA-rendszer", "ipari folyamatirányító és adatgyűjtő hálózat"], ["üzemfolytonosság", "megszakítás nélküli működés képessége"], ["redundáns architektúra", "tartalék elemekkel megerősített megbízható felépítés"], ["villamosenergia-hálózat", "az áramellátás stratégiai gerince"]], ["c1-18-vocab"]),
                fb("grammar", "practice", "Az áramkimaradások megelőzése érdekében _____ a vészhelyzeti tartalékrendszereket. (advisable to establish / célszerű kiépíteni)", "célszerű kiépíteni", "In order to prevent blackouts it is advisable to establish emergency reserve systems.", ["c1-infinitive-predicative-necessity"]),
                sb("grammar", "practice", ["Elengedhetetlen", "felkészíteni", "a", "szervezeteket", "a", "kiberfizikai", "incidensekre."], ["Elengedhetetlen", "felkészíteni", "a", "szervezeteket", "a", "kiberfizikai", "incidensekre."], "It is indispensable to prepare organizations for cyber-physical incidents.", ["c1-infinitive-predicative-necessity"]),
                dc("dialogue", [
                    {"speaker": "Hálózatüzemeltető", "text": "Hogyan védhetjük ki a transzformátorok távoli leállítását?"},
                    {"speaker": "Biztonsági mérnök", "text": "Elengedhetetlen _____ az ipari vezérlőhálózatokat a publikus felhőszolgáltatásoktól."},
                ], ["fizikailag leválasztani", "összekapcsolni", "feloldani"], 0, ["c1-infinitive-predicative-necessity"]),
                sw("production", [{"prompt": "Write a sentence on critical infrastructure protection using 'elengedhetetlen garantálni'.", "answer": "A villamosenergia-hálózat kiberbiztonsága kapcsán elengedhetetlen garantálni az ipari vezérlőrendszerek azonnali és megbízható redundanciáját."}], ["c1-infinitive-predicative-necessity"]),
                mc("grammar", "check", "Melyik kifejezés fejez ki személytelen, rendszerszintű kötelezettséget főnévi igenévvel?", [
                    "elengedhetetlen biztosítani",
                    "talán láttuk már",
                    "amikor megcsináltuk"
                ], 0, ["c1-infinitive-predicative-necessity"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-18-03",
            "title": "Algorithmic Surveillance, Biometrics & Civil Liberties",
            "grammar_title": "Parenthetical Evaluative Markers Modifying Truth Value and Epistemic Commitment",
            "grammar_skill": "c1-adv-evaluative-parentheticals",
            "goals": [
                "I can critique algorithmic surveillance, biometric identification, and surveillance capitalism (*megfigyelési kapitalizmus, biometrikus azonosítás, arcfelismerő technológia*).",
                "I can insert parenthetical evaluative markers to modulate argumentative certainty (*megfontolandó módon, vitán felül állóan, némiképp sarkítva, aggodalomra okot adóan*).",
                "I can evaluate the constitutional balance between public safety and citizen privacy rights."
            ],
            "vocab": [
                {"lemma": "algoritmusos felügyelet", "translation": "algorithmic surveillance", "pos": "expression"},
                {"lemma": "biometrikus azonosítás", "translation": "biometric identification", "pos": "expression"},
                {"lemma": "arcfelismerő technológia", "translation": "facial recognition technology", "pos": "expression"},
                {"lemma": "megfigyelési kapitalizmus", "translation": "surveillance capitalism", "pos": "expression"},
                {"lemma": "digitális lábnyom", "translation": "digital footprint", "pos": "expression"},
                {"lemma": "magánszféra védelme", "translation": "protection of privacy", "pos": "expression"},
                {"lemma": "tömeges adatgyűjtés", "translation": "bulk / mass data collection", "pos": "expression"},
                {"lemma": "profilalkotás", "translation": "profiling", "pos": "noun"}
            ],
            "gr_text1": "Parenthetical evaluative adverbs in C1 analytical prose frame the writer's epistemological stance and normative stance without disrupting sentence flow: `megfontolandó módon` (prudently/notably), `vitán felül állóan` (beyond dispute), `aggodalomra okot adóan` (worryingly), `némiképp sarkítva` (somewhat exaggeratedly/put bluntly). Example: `A biometrikus azonosítás, vitán felül állóan, alapjaiban formálja át az állam és a polgár viszonyát`.",
            "gr_text2": "These adverbial markers typically sit between commas immediately following the topic or in clause-initial position, calibrating the objective authority of the critique.",
            "gr_table": [
                ["Az algoritmusos felügyelet terjedése, vitán felül állóan, a demokratikus nyilvánosság visszaszorulásához vezethet.", "The spread of algorithmic surveillance, beyond dispute, can lead to the retreat of the democratic public sphere."],
                ["Megfontolandó módon, a jogalkotónak meg kell húznia az arcfelismerő rendszerek alkalmazásának végső határait.", "Prudently, the legislator must draw the ultimate boundaries for deploying facial recognition systems."],
                ["A magánszféra eróziója, aggodalomra okot adóan, ma már a mindennapi digitális rutin elkerülhetetlen velejárójává vált.", "The erosion of privacy, worryingly, has today become an inevitable concomitant of daily digital routine."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevezünk Shoshana Zuboff elmélete nyomán 'megfigyelési kapitalizmusnak' (surveillance capitalism)?", [
                    "Azt a gazdasági logikát, amely az emberi élményeket ingyenes nyersanyagként zsákmányolja ki viselkedési adatokká formálva és azokat piacra dobva.",
                    "A banki biztonsági kamerák gyártási technológiáját.",
                    "A postai bélyeggyűjtők zárt körű aukcióit."
                ], 0, ["c1-18-vocab"]),
                fb("grammar", "controlled", "A tömeges adatgyűjtés, _____ sérti a polgárok információs önrendelkezési jogát. (beyond dispute / vitán felül állóan)", "vitán felül állóan", "Mass data collection, beyond dispute, violates citizens' right to informational self-determination.", ["c1-adv-evaluative-parentheticals"]),
                match("vocabulary", "controlled", [["arcfelismerő technológia", "képmáson alapuló biometrikus nyomkövetés"], ["digitális lábnyom", "online aktivitás során hagyott adathalmaz"], ["profilalkotás", "viselkedési adatok automatizált kiértékelése"], ["magánszféra védelme", "az egyén intimszférájának alkotmányos védelme"]], ["c1-18-vocab"]),
                fb("grammar", "practice", "A közterületi kamerarendszerek kiterjesztése, _____ normalizálja az állandó megfigyeltség érzetét. (worryingly / aggodalomra okot adóan)", "aggodalomra okot adóan", "The extension of public surveillance camera networks, worryingly, normalizes the feeling of constant observation.", ["c1-adv-evaluative-parentheticals"]),
                sb("grammar", "practice", ["A", "technológia,", "vitán", "felül", "állóan,", "új", "etikai", "dilemmákat", "teremt."], ["A", "technológia,", "vitán", "felül", "állóan,", "új", "etikai", "dilemmákat", "teremt."], "The technology, beyond dispute, creates new ethical dilemmas.", ["c1-adv-evaluative-parentheticals"]),
                dc("dialogue", [
                    {"speaker": "Jogvédő", "text": "Hogyan hathat a közterületi arcfelismerés a gyülekezési jogra?"},
                    {"speaker": "Alkotmányjogász", "text": "A technológia elterjedése, vitán felül állóan, dermesztő hatást gyakorolhat a szabad polgári _____."},
                ], ["véleménynyilvánításra", "vásárlási kedvre", "időjárás-előrejelzésre"], 0, ["c1-adv-evaluative-parentheticals"]),
                sw("production", [{"prompt": "Write a critical sentence about facial recognition systems using 'vitán felül állóan'.", "answer": "A közterületi arcfelismerés alkalmazása, vitán felül állóan, aránytalanul korlátozza a polgárok gyülekezési és magánéleti szabadságát."}], ["c1-adv-evaluative-parentheticals"]),
                mc("grammar", "check", "Melyik határozói kifejezés szolgál az állítás bizonyosságának és megkérdőjelezhetetlenségének nyomatékosítására?", [
                    "vitán felül állóan",
                    "esetleg talán",
                    "elvileg elhanyagolhatóan"
                ], 0, ["c1-adv-evaluative-parentheticals"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-18-04",
            "title": "Cryptography, Quantum Threat & Key Architecture",
            "grammar_title": "Complex Adverbial Expressions of Structural Contingency and Mutual Functional Dependence",
            "grammar_skill": "c1-complex-modal-contingency",
            "goals": [
                "I can analyze cryptography, post-quantum encryption, and key management architectures (*posztkvantum-titkosítás, aszimmetrikus kriptográfia, zéró tudású bizonyítás*).",
                "I can express structural contingency and functional interdependence (*attól függően, hogy miként; annak függvényében, hogy milyen; arányában*).",
                "I can debate the quantum computing threat to global banking and diplomatic security."
            ],
            "vocab": [
                {"lemma": "aszimmetrikus kriptográfia", "translation": "asymmetric cryptography", "pos": "expression"},
                {"lemma": "kvantumfenyegetés", "translation": "quantum threat", "pos": "noun"},
                {"lemma": "posztkvantum-titkosítás", "translation": "post-quantum cryptography", "pos": "expression"},
                {"lemma": "nyilvános kulcsú infrastruktúra", "translation": "public key infrastructure (PKI)", "pos": "expression"},
                {"lemma": "végpontok közötti titkosítás", "translation": "end-to-end encryption", "pos": "expression"},
                {"lemma": "brute force támadás", "translation": "brute force attack", "pos": "expression"},
                {"lemma": "entrópia", "translation": "entropy (cryptographic randomness)", "pos": "noun"},
                {"lemma": "zéró tudású bizonyítás", "translation": "zero-knowledge proof", "pos": "expression"}
            ],
            "gr_text1": "Structural contingency and functional co-dependence in technical Hungarian are expressed via relational markers: `annak függvényében, hogy [ige]` (as a function of / depending on whether), `attól függően, hogy [ige]` (contingent on how), `azzal párhuzamosan, ahogyan` (in parallel with how). Example: `A titkosítás feltörhetetlensége annak függvényében változik, hogy a kulcshossz mekkora matematikai entrópiát biztosít`.",
            "gr_text2": "These postpositional and correlative structures allow sophisticated mathematical and technical calibration of cause, condition, and functional outcome.",
            "gr_table": [
                ["A kommunikáció biztonsága annak függvényében garantálható, hogy a kulcscsere protokollja védett-e a kvantumalgoritmusokkal szemben.", "The security of communication is guaranteed depending on whether the key exchange protocol is protected against quantum algorithms."],
                ["Attól függően, hogy a hardver mekkora entrópiát generál, a titkosító kulcs ellenáll a brute force támadásoknak.", "Depending on how much entropy the hardware generates, the encryption key resists brute force attacks."],
                ["A banki rendszerek biztonsága az új posztkvantum-algoritmusok bevezetésének üteme arányában növekszik.", "The security of banking systems increases in proportion to the pace of introducing new post-quantum algorithms."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért jelent egzisztenciális 'kvantumfenyegetést' a kvantumszámítógép az aszimmetrikus titkosításra?", [
                    "Mert a Shor-algoritmus segítségével a kvantumszámítógépek percek alatt képesek feltörni az RSA- és elliptikus görbe alapú kulcscserét.",
                    "Mert a kvantumszámítógépek fizikai mágnesként vonzzák magukhoz az internetkábeleket.",
                    "Mert a kvantumszámítógépek túl sok villanyáramot fogyasztanak a bankfiókokban."
                ], 0, ["c1-18-vocab"]),
                fb("grammar", "controlled", "A védelem hatékonysága _____ alakul, mikor kezdődik meg a posztkvantum-titkosításra való átállás. (depending on whether / annak függvényében, hogy)", "annak függvényében, hogy", "The effectiveness of defence shapes depending on whether when the transition to post-quantum encryption begins.", ["c1-complex-modal-contingency"]),
                match("vocabulary", "controlled", [["végpontok közötti titkosítás", "csak a küldő és a fogadó látja a nyers adatot"], ["posztkvantum-titkosítás", "kvantumszámítógépeknek is ellenálló algoritmusok"], ["zéró tudású bizonyítás", "információ igazolása a titok felfedése nélkül"], ["entrópia", "kriptográfiai véletlenszerűség mértéke"]], ["c1-18-vocab"]),
                fb("grammar", "practice", "A rendszer sérülékenysége _____ nő vagy csökken, hogy a hálózat milyen gyakran frissíti a biztonsági kulcsokat. (depending on / attól függően)", "attól függően", "The vulnerability of the system increases or decreases depending on how often the network updates security keys.", ["c1-complex-modal-contingency"]),
                sb("grammar", "practice", ["A", "biztonság", "annak", "függvényében", "változik,", "hogy", "milyen", "erős", "a", "kriptográfia."], ["A", "biztonság", "annak", "függvényében", "változik,", "hogy", "milyen", "erős", "a", "kriptográfia."], "Security varies depending on how strong the cryptography is.", ["c1-complex-modal-contingency"]),
                dc("dialogue", [
                    {"speaker": "Kriptográfus", "text": "Mikor kell leváltanunk a jelenlegi nyilvános kulcsú infrastruktúrát?"},
                    {"speaker": "Biztonsági igazgató", "text": "Annak függvényében, hogy mikorra várható a működőképes kriptográfiai _____ megjelenése."},
                ], ["kvantumszámítógépek", "analóg telefonok", "mechanikus írógépek"], 0, ["c1-complex-modal-contingency"]),
                sw("production", [{"prompt": "Write a technical proposition about encryption using 'annak függvényében, hogy'.", "answer": "Egy kiberrendszer ellenálló képessége annak függvényében mérhető, hogy a titkosítási kulcsok mekkora entrópiát biztosítanak a külső behatolási kísérletekkel szemben."}], ["c1-complex-modal-contingency"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki funkcionális kölcsönös függőséget és strukturális feltételességet?", [
                    "annak függvényében, hogy / attól függően, hogy",
                    "annak ellenére, hogy",
                    "anélkül, hogy"
                ], 0, ["c1-complex-modal-contingency"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-18-05",
            "title": "Kalmár László: Cybernetics & The Limits of Machine Thought",
            "grammar_title": "Syntactic Cleft Structures and Focus Fronting in Analytical Argument Contrast",
            "grammar_skill": "c1-adv-syntactic-focus-clefting",
            "goals": [
                "I can analyze László Kalmár's philosophical and mathematical pioneering essay on cybernetics and thinking machines (*Kalmár László: A kibernetika és az emberi gondolkodás határai*).",
                "I can construct syntactic cleft structures and focus fronting to contrast theoretical propositions (*nem az X, hanem az Y; nem annyira X, mint inkább Y*).",
                "I can interpret the epistemological distinction between mechanical computation and human creative understanding."
            ],
            "vocab": [
                {"lemma": "kibernetikai automata", "translation": "cybernetic automaton", "pos": "expression"},
                {"lemma": "formális logika", "translation": "formal logic", "pos": "expression"},
                {"lemma": "heurisztikus algoritmus", "translation": "heuristic algorithm", "pos": "expression"},
                {"lemma": "gondolkodó gépek", "translation": "thinking machines", "pos": "expression"},
                {"lemma": "algoritmikus eldönthetőség", "translation": "algorithmic decidability", "pos": "expression"},
                {"lemma": "mesterséges neurális háló", "translation": "artificial neural network", "pos": "expression"},
                {"lemma": "humán intellektus", "translation": "human intellect", "pos": "expression"},
                {"lemma": "ontológiai határvonal", "translation": "ontological boundary line", "pos": "expression"}
            ],
            "gr_text1": "Syntactic clefting and focus fronting in Hungarian place the contrasted element immediately before the finite verb, paired with an explicit negative-contrastive clause: `Nem annyira a számítási sebesség, mint inkább a minőségi jelentésalkotás képessége különbözteti meg az embert a géptől` (It is not so much computation speed as rather the capacity for qualitative meaning-making that distinguishes human from machine).",
            "gr_text2": "Common syntactic formulas: `Nem [X], hanem [Y] [Ige]...` / `Nem annyira [X], mint inkább [Y] jelenti a valódi kihívást`. The preverbal position receives nuclear pitch accent.",
            "gr_table": [
                ["Nem a gép mechanikus működése, hanem az emberi célkitűzés határozza meg a technológia erkölcsi súlyát.", "It is not the mechanical operation of the machine, but human goal-setting that determines the moral weight of technology."],
                ["Nem annyira a formális kalkulus hibátlansága, mint inkább a heurisztikus kreativitás képezi a humán intellektus lényegét.", "It is not so much the flawlessness of formal calculus as rather heuristic creativity that constitutes the essence of human intellect."],
                ["Nem az algoritmus autonómiája, hanem a tervező felelőssége áll a kibernetikai etika középpontjában.", "It is not the autonomy of the algorithm, but the designer's responsibility that stands at the center of cybernetic ethics."]
            ],
            "classic_story": {
                "slug": "c1-18-kalmar",
                "author": "Kalmár László",
                "work": "A kibernetika és az emberi gondolkodás határai (1962)",
                "title": "Kalmár László: A kibernetika és az emberi gondolkodás határai",
                "summary": "László Kalmár's foundational 1962 treatise exploring cybernetics, mathematical logic, Gödel's incompleteness theorem, and the irreducibility of human consciousness to mechanical computation.",
                "characters": ["Kalmár László"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor az első elektronikus számítógépek megjelentek, azonnal fellángolt a vita arról, vajon képes-e a gép valóban gondolkodni. A szegedi matematikai iskola nagy alakja, Kalmár László professzor 1962-ben megjelent tanulmányában tiszta logikai szigorral és mély filozófiai belátással tisztázta a kérdést, eloszlatva mind a naiv mechanisztikus illúziókat, mind a tudománytalan misztifikációt."},
                    {"type": "narration", "text": "Kalmár rámutatott: a kibernetikai automata formális logikai szabályok szerint működő zárt rendszer. Képes percenként milliónyi aritmetikai művelet elvégzésére, szimbolikus formulák átalakítására, sőt heurisztikus algoritmusok révén sakkjátszmák elemzésére is. Mindazonáltal a mechanikus számítás és az emberi gondolkodás között ontológiai minőségi különbség feszül: a gép nem tudja, mit csinál; számára a szimbólum nem hordoz szándékolt jelentést, csupán feszültségállapotok láncolatát."},
                    {"type": "narration", "text": "Gödel híres nemteljességi tételére támaszkodva Kalmár meggyőzően bizonyította: minden formális rendszerben léteznek olyan igaz állítások, amelyek magán a rendszeren belül algoritmikusan levezethetetlenek. Az emberi intellektus csodája éppen abban áll, hogy képes kilépni az adott axiómarendszer keretei közül, reflektálni saját korlátaira, és új, tágabb összefüggéseket teremteni."},
                    {"type": "narration", "text": "A kibernetika tehát nem az ember trónfosztása, hanem szellemi képességeink rendkívüli meghosszabbítása. Nem a gép emberszerűvé válása a valódi kihívás, hanem az, hogy az ember megőrizze erkölcsi és intellektuális méltóságát az általa teremtett technológiai világban: biztosítva, hogy a gépek szolgálják a szabadságot, s ne az elnyomás vagy az önkény digitális eszközeivé váljanak."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen úttörő felismerést fogalmazott meg Kalmár László matematikus a gondolkodó gépekről?", [
                    "Hogy a gép bármilyen bonyolult formális számításra képes, de a jelentéstulajdonítás és a kreatív célkitűzés az ember sajátja marad.",
                    "Hogy a számítógépeknek nincs szükségük elektromos áramra a működéshez.",
                    "Hogy a matematika tanulása feleslegessé válik az automaták megalkotásával."
                ], 0, ["c1-18-vocab"]),
                fb("grammar", "controlled", "Nem a merev szabályok másolása, _____ problémamegoldás jelenti a valódi intellektus próbáját. (but rather the heuristic / hanem a heurisztikus)", "hanem a heurisztikus", "Not copying rigid rules, but rather heuristic problem solving represents the test of real intellect.", ["c1-adv-syntactic-focus-clefting"]),
                match("vocabulary", "controlled", [["formális logika", "szimbolikus szabályokon alapuló következtetés"], ["algoritmikus eldönthetőség", "egy probléma mechanikus megoldhatósága"], ["heurisztikus algoritmus", "gyakorlati tapasztalaton alapuló keresés"], ["ontológiai határvonal", "a létmódok közötti lényegi elválasztó vonal"]], ["c1-18-vocab"]),
                mc("reading", "practice", "Mi a lényegi különbség Kalmár szerint a számítógép műveletei és az emberi elme között?", [
                    "A gép pusztán mechanikus szimbólummanipulációt végez jelentés nélkül, míg az ember képes szemantikai jelentést tulajdonítani és reflexív módon új összefüggéseket alkotni.",
                    "A gép egyáltalán nem képes számokat összeadni.",
                    "Az emberi elme lassabban számol, ezért teljesen felesleges."
                ], 0, None),
                sb("grammar", "practice", ["Nem", "a", "gép,", "hanem", "az", "ember", "felelős", "a", "döntésekért."], ["Nem", "a", "gép,", "hanem", "az", "ember", "felelős", "a", "döntésekért."], "Not the machine, but human is responsible for the decisions.", ["c1-adv-syntactic-focus-clefting"]),
                sw("production", [{"prompt": "Formulate a thought on the difference between machine and human thinking using the 'nem annyira... mint inkább' focus cleft structure.", "answer": "Nem annyira a gigantikus műveleti sebesség, mint inkább a kontextusértés és az etikai felelősségvállalás alkotja az emberi elme meghaladhatatlan sajátosságát."}], ["c1-adv-syntactic-focus-clefting"]),
                mc("grammar", "check", "Melyik mondatszerkezet valósít meg fókuszos kiemelést szembeállítással (syntactic clefting)?", [
                    "Nem annyira az adatok mennyisége, mint inkább a kód megbízhatósága a kulcs.",
                    "Minden adatot lemásoltak a szerverre tegnap este.",
                    "Bár sok adat volt ott, nem csináltak vele semmit."
                ], 0, ["c1-adv-syntactic-focus-clefting"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(18, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        18,
        "core",
        "c1-18-consolidation",
        core_title,
        [
            "I can master C1 technical and philosophical discourse on cybersecurity and digital sovereignty.",
            "I can employ adversative-concessive clauses, impersonal necessity predicates, evaluative parentheticals, modal contingency expressions, and focus clefting.",
            "I can interpret Kalmár László's cybernetic philosophy and evaluate critical infrastructure defence."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat alkalmaz helyes adversative-concessive szerkezetet?", [
                "Jóllehet a technológia gyorsan fejlődik, mindazonáltal a jogi szabályozás évtizedes lemaradásban van.",
                "Mivel a technológia fejlődik, azért nem csinálunk semmit.",
                "Hogy a technológia fejlődjön, ahhoz sok pénz kell."
            ], 0, ["c1-adv-adversative-concessive-clauses"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki rendszerszintű elengedhetetlen szükségszerűséget?", [
                "Elengedhetetlen biztosítani a kritikus infrastruktúrák redundáns áramellátását.",
                "Talán szép lenne biztosítani valamikor.",
                "Nem szükséges vele foglalkozni."
            ], 0, ["c1-infinitive-predicative-necessity"]),
            match("vocabulary", "recognize", [["digitális szuverenitás", "önálló technológiai önrendelkezés"], ["SCADA-rendszer", "ipari vezérlőhálózat"], ["posztkvantum-titkosítás", "kvantumbiztos kriptográfia"], ["megfigyelési kapitalizmus", "viselkedési adatok profitcélú kizsákmányolása"], ["kibernetikai automata", "szabályvezérelt számítási gépezet"]], ["c1-18-vocab"]),
            fb("vocabulary", "recall", "A modern villamosenergia-hálózat biztonságához elengedhetetlen a robusztus _____ felépítése. (redundant architecture / redundáns architektúra)", "redundáns architektúra", "For the security of modern electrical power grid, building a robust redundant architecture is indispensable.", ["c1-18-vocab"]),
            fb("vocabulary", "recall", "A kvantumszámítógépek megjelenése miatt a szakértők sürgetik a _____ bevezetését. (post-quantum cryptography / posztkvantum-titkosítás)", "posztkvantum-titkosítás", "Due to the emergence of quantum computers, experts urge the introduction of post-quantum cryptography.", ["c1-18-vocab"]),
            fb("grammar", "recall", "_____ a kényelem csábító, mindazonáltal a magánszféra feladása visszafordíthatatlan károkat okoz. (Although / Jóllehet)", "Jóllehet", "Although convenience is tempting, nevertheless relinquishing privacy causes irreversible damage.", ["c1-adv-adversative-concessive-clauses"]),
            fb("grammar", "context", "A kiberbűnözés elleni védekezés, _____ nemzetbiztonsági prioritássá vált. (beyond dispute / vitán felül állóan)", "vitán felül állóan", "Defending against cybercrime, beyond dispute, has become a national security priority.", ["c1-adv-evaluative-parentheticals"]),
            fb("grammar", "context", "A kulcscsere biztonsága _____ alakul, mekkora az entrópia. (depending on whether / annak függvényében, hogy)", "annak függvényében, hogy", "The security of key exchange shapes depending on whether how large the entropy is.", ["c1-complex-modal-contingency"]),
            mc("grammar", "context", "Hogyan működik a 'nem annyira X, mint inkább Y' fókuszos kiemelés egy érvelésben?", [
                "Egymással szembeállít két tényezőt, visszaszorítva a felszínes magyarázatot és a lényegi okra irányítva a figyelmet.",
                "Kijelenti, hogy mindkét dolog teljesen lényegtelen.",
                "Elnézést kér a felmerülő hibákért."
            ], 0, ["c1-adv-syntactic-focus-clefting"]),
            sb("grammar", "produce", ["Nem", "a", "technológia,", "hanem", "az", "emberi", "szándék", "dönt."], ["Nem", "a", "technológia,", "hanem", "az", "emberi", "szándék", "dönt."], "Not the technology, but human intent decides.", ["c1-adv-syntactic-focus-clefting"]),
            sw("production", [{"prompt": "Write an argument evaluating the balance between state security and personal privacy in cyberspace.", "answer": "Jóllehet a kritikus infrastruktúrák védelme határozott állami fellépést igényel, mindazonáltal elengedhetetlen biztosítani a polgárok magánszférájának és digitális önrendelkezésének védelmét."}], ["c1-adv-adversative-concessive-clauses"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Kalmár László's cybernetic legacy.", "answer": "Nem annyira a gépek intelligenciája, mint inkább az ember etikai felelősségvállalása jelenti a huszonegyedik század legnagyobb civilizációs próbatételét."}], ["c1-adv-syntactic-focus-clefting"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-kiberbiztonsag)
    # ----------------------------------------------------
    slug = "kiberbiztonsag"
    disc_intro = [
        "Cyberspace is no longer merely a communication network: it is the fifth operational domain of warfare, where critical energy grids, hospital databases, and electoral systems face constant disruption.",
        "In this unit, you will master the elevated discourse of strategic cyber warfare, zero-day vulnerabilities, the NIS2 regulatory framework, and societal resilience in Central Europe."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "State-Sponsored Cyber Warfare & Critical Infrastructure Siege",
            "grammar_title": "Rhetorical Threat-Framing Connectors Characterizing Cybersecurity Risks and Systemic Vulnerabilities",
            "grammar_skill": "c1-discourse-threat-framing",
            "goals": [
                "I can analyze state-sponsored cyber warfare, APT groups, and ransomware attacks on critical infrastructure (*államilag támogatott hekkercsoport, zsarolóvírus, kiberhadviselés*).",
                "I can employ rhetorical threat-framing connectors to assess existential systemic risks (*akut nemzetbiztonsági kockázatot hordoz, közvetlen veszélyt idéz elő, sérülékenységet tár fel*).",
                "I can debate the vulnerabilities of hospital systems and electrical grids under hostile cyber siege."
            ],
            "vocab": [
                {"lemma": "államilag támogatott hekkercsoport", "translation": "state-sponsored hacker group / APT", "pos": "expression"},
                {"lemma": "zsarolóvírus", "translation": "ransomware", "pos": "noun"},
                {"lemma": "kiberhadviselés", "translation": "cyber warfare", "pos": "noun"},
                {"lemma": "adatszivárgás", "translation": "data breach / leakage", "pos": "noun"},
                {"lemma": "kritikus hálózati komponens", "translation": "critical network component", "pos": "expression"},
                {"lemma": "kibertér mint hadszíntér", "translation": "cyberspace as domain of warfare", "pos": "expression"},
                {"lemma": "zéró megbízhatóság elve", "translation": "zero trust principle", "pos": "expression"},
                {"lemma": "kiberzsarolás", "translation": "cyber extortion", "pos": "noun"}
            ],
            "gr_text1": "In strategic security discourse, threats to infrastructure are articulated through formal causative and evaluative predicates: `akut nemzetbiztonsági kockázatot hordoz / rejt magában` (bears acute national security risk), `közvetlen veszélyt idéz elő / jelent` (poses an immediate danger), `kritikus sebezhetőséget tár fel` (reveals critical vulnerability), `súlyos következményeket von maga után` (entails grave consequences).",
            "gr_text2": "Example: `A kórházi informatikai hálózatok ellen intézett zsarolóvírus-támadás nem csupán adatszivárgást okoz, hanem akut veszélyt idéz elő az intenzív osztályok életmentő működésében`.",
            "gr_table": [
                ["Az energetikai hálózatok feltörése közvetlen veszélyt jelent az egész társadalom működésére.", "The breaching of energy networks poses an immediate danger to the functioning of the entire society."],
                ["A hálózati eszközök elavultsága kritikus sebezhetőséget tár fel a külföldi behatolókkal szemben.", "The obsolescence of network devices reveals a critical vulnerability toward foreign intruders."],
                ["A zsarolóvírusos támadások terjedése akut nemzetbiztonsági kockázatot rejt magában a közszférában.", "The proliferation of ransomware attacks harbors an acute national security risk in the public sector."]
            ],
            "world_story_seg": {
                "seg_slug": "tamadas",
                "title": "A digitális ostrom: MVM villamosenergia-hálózat és a kritikus infrastruktúrák védelme",
                "summary": "How coordinated state-sponsored cyber attacks targeted Hungary's power grid control and regional hospitals, testing emergency air-gapping and redundancy.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 2024 téli éjszakáján a magyar villamosenergia-ipari átviteli rendszerirányító képernyőin szokatlan anomáliák tűntek fel, a mérnökök azonnal tudták: nem egyszerű hálózati túlterhelésről van szó. A terheléselosztó SCADA-rendszereket koordinált külső támadás érte. A háttérben egy jól ismert, államilag támogatott hekkercsoport digitális szondái tapogatták le a transzformátorállomások vezérlőlogikáját, arra készülve, hogy egyetlen kattintással sötétségbe borítsák Közép-Magyarországot."},
                    {"type": "narration", "text": "Az azonnali fizikai leválasztás és a szigorúan tesztelt redundáns architektúra megakadályozta az országos áramszünetet. Ugyanezen az éjszakán azonban három regionális kórház hálózatát zsarolóvírus titkosította le, megbénítva a betegfelvételt és a műtéti beosztásokat. Az események brutális tisztasággal világítottak rá: a kritikus infrastruktúrák kiberbiztonsága nem elméleti informatikai dilemma, hanem a mindennapi emberi élet és túlélés legégetőbb feltétele."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit ért a katonai doktrína a 'kibertér mint hadszíntér' kifejezés alatt?", [
                    "Azt, hogy a szárazföld, a tenger, a levegő és a világűr mellett a digitális információs tér hivatalosan is az önálló hadműveletek ötödik dimenziójává vált.",
                    "Hogy a katonáknak számítógépes játékokban kell gyakorolniuk a célbalövést.",
                    "A katonai toborzóirodák weboldalainak karbantartását."
                ], 0, ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "controlled", "A villamos hálózat vezérlésének megbénítása akut _____ a társadalom működésére. (national security risk bears / nemzetbiztonsági kockázatot hordoz)", "nemzetbiztonsági kockázatot hordoz", "Paralyzing the control of electrical grid bears acute national security risk for the functioning of society.", ["c1-discourse-threat-framing"]),
                match("vocabulary", "controlled", [["államilag támogatott hekkercsoport", "hadseregekhez és titkosszolgálatokhoz kötődő APT"], ["zsarolóvírus", "adatokat titkosító és váltságdíjat követelő kártevő"], ["zéró megbízhatóság elve", "soha ne bízz, mindig ellenőrizz modell"], ["adatszivárgás", "bizalmas információk illetéktelen kikerülése"]], ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "practice", "A biztonsági frissítések elmulasztása közvetlen _____ a szerverpark stabilitására. (poses immediate danger / veszélyt idéz elő)", "veszélyt idéz elő", "Neglecting security patches poses immediate danger to the stability of the server farm.", ["c1-discourse-threat-framing"]),
                sb("grammar", "practice", ["A", "támadás", "közvetlen", "veszélyt", "jelent", "az", "ellátásbiztonságra."], ["A", "támadás", "közvetlen", "veszélyt", "jelent", "az", "ellátásbiztonságra."], "The attack poses an immediate danger to security of supply.", ["c1-discourse-threat-framing"]),
                dc("dialogue", [
                    {"speaker": "Hálózatbiztonsági parancsnok", "text": "Hogyan minősítsük a transzformátorállomások elleni kísérletet?"},
                    {"speaker": "Elemző", "text": "Ez a behatolás akut nemzetbiztonsági _____ rejt magában, és azonnali védelmi készültséget igényel."},
                ], ["kockázatot", "lehetőséget", "meglepetést"], 0, ["c1-discourse-threat-framing"]),
                sw("production", [{"prompt": "Write a threat analysis sentence using 'közvetlen veszélyt idéz elő'.", "answer": "A kórházi vezérlőrendszerek elégtelen titkosítása közvetlen veszélyt idéz elő a betegellátás folyamatosságára nézve."}], ["c1-discourse-threat-framing"]),
                mc("grammar", "check", "Melyik kifejezés fejez ki súlyos nemzetbiztonsági fenyegetést a kiberbiztonsági diskurzusban?", [
                    "akut nemzetbiztonsági kockázatot hordoz",
                    "időnként kellemetlenséget szül",
                    "csekély érdeklődésre tarthat számot"
                ], 0, ["c1-discourse-threat-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Pegasus, Zero-Days & Lawful Interception Ethics",
            "grammar_title": "Deontic Regulatory Compliance Structures Establishing Statutory Audits and Operational Mandates",
            "grammar_skill": "c1-regulatory-compliance-syntax",
            "goals": [
                "I can analyze the Pegasus surveillance affair, zero-day vulnerabilities, and lawful interception frameworks (*nulladik napi sebezhetőség, Pegasus-ügy, törvényes megfigyelés, bírói kontroll*).",
                "I can formulate deontic regulatory mandates and audit requirements (*szigorú auditkötelezettséget ír elő, megfelelési minimumot szab, garanciákat követel meg*).",
                "I can debate the legal and constitutional balance between intelligence operations and journalist/civilian protection."
            ],
            "vocab": [
                {"lemma": "nulladik napi sebezhetőség", "translation": "zero-day vulnerability", "pos": "expression"},
                {"lemma": "kémprogram", "translation": "spyware", "pos": "noun"},
                {"lemma": "törvényes megfigyelés", "translation": "lawful interception", "pos": "expression"},
                {"lemma": "bírói engedélyezés", "translation": "judicial authorization / warrant", "pos": "expression"},
                {"lemma": "visszaélési kockázat", "translation": "risk of abuse", "pos": "expression"},
                {"lemma": "digitális integritás", "translation": "digital integrity", "pos": "expression"},
                {"lemma": "okostelefon-kompromittálás", "translation": "smartphone compromise", "pos": "expression"},
                {"lemma": "fegyverként használt szoftver", "translation": "weaponized software / cyber weapon", "pos": "expression"}
            ],
            "gr_text1": "Deontic regulatory language uses formal verbs expressing statutory obligation, legal mandate, and institutional compliance: `auditkötelezettséget ír elő` (prescribes audit obligation), `megfelelési minimumot szab meg` (sets compliance minimum), `független bírói kontrollt követel meg` (mandates independent judicial control), `jogszabályi kötelezettséget ró a felekre` (imposes statutory duty on parties).",
            "gr_text2": "Example: `A nemzetközi jogi normák és az alkotmányos alapelvek szigorú előzetes bírói engedélyezést követelnek meg a titkosszolgálati megfigyelések minden egyes esetében`.",
            "gr_table": [
                ["A törvényhozás szigorú auditkötelezettséget ír elő a kémszoftvereket alkalmazó állami szervek számára.", "The legislature prescribes a strict audit obligation for state organs deploying spyware."],
                ["Az alkotmányos rend független bírói kontrollt követel meg a polgárok digitális eszközeinek megfigyelésekor.", "The constitutional order demands independent judicial oversight when monitoring citizens' digital devices."],
                ["A jogszabály kötelező garanciákat szab meg a visszaélések hatékony megelőzése érdekében.", "The statute sets mandatory guarantees in order to effectively prevent abuses."]
            ],
            "world_story_seg": {
                "seg_slug": "pegasus",
                "title": "A láthatatlan fegyver: Pegasus, nulladik napi sebezhetőségek és az elszámoltathatóság",
                "summary": "Exploring the legal shockwaves of Pegasus military-grade spyware in Central Europe and the imperative of judicial oversight over intelligence surveillance.",
                "paragraphs": [
                    {"type": "narration", "text": "A Pegasus-botrány kirobbanása alapjaiban rázta meg a közép-európai nyilvánosságot. A civil társadalomnak és a jogászoknak szembe kellett nézniük a ténnyel: léteznek olyan katonai szintű, fegyverként használt kémprogramok, amelyek ellen a hagyományos felhasználói óvatosság teljesen hatástalan. A 'zero-click' nulladik napi sebezhetőségek révén a célpont okostelefonja anélkül váltott át észrevétlen lehallgatókészülékké, hogy a tulajdonosa bármilyen gyanús linkre rákattintott volna."},
                    {"type": "narration", "text": "A botrány nyomán fellángoló vita a jogállam alapkérdéseit érintette. Miközben a terrorelhárítás a modern technológiák szükségességét hangsúlyozta, az alkotmánybíróságok és a nemzetközi emberi jogi bíróságok rámutattak: független előzetes bírói engedélyezés és szigorú utólagos auditkötelezettség nélkül a titkos megfigyelés elkerülhetetlenül a hatalommal való politikai visszaélés eszközévé torzul."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinthető a katonai minőségű kémszoftver (pl. Pegasus) 'fegyverként használt szoftvernek'?", [
                    "Mert felhasználói beavatkozás nélkül (zero-click) töri fel a telefont, átveszi a mikrofon, a kamera és a titkosított csevegések teljes irányítását.",
                    "Mert fizikailag felrobbantja a telefontöltőt a konnektorban.",
                    "Mert automatikusan letiltja a kéretlen reklámleveleket."
                ], 0, ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "controlled", "A jogállami működés szigorú előzetes bírói _____ a megfigyelések előtt. (authorization demands / engedélyezést követel meg)", "engedélyezést követel meg", "The rule of law demands strict prior judicial authorization before surveillance.", ["c1-regulatory-compliance-syntax"]),
                match("vocabulary", "controlled", [["nulladik napi sebezhetőség", "a gyártó által még nem ismert biztonsági rés"], ["kémprogram", "titokban adatokat gyűjtő kártevő"], ["bírói engedélyezés", "független bíróság által jóváhagyott megfigyelési határozat"], ["digitális integritás", "az adatok és rendszerek érintetlensége"]], ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "practice", "A kibervédelmi szabályozás részletes megfelelési _____ valamennyi állami intézménynek. (minimum sets / minimumot szab meg)", "minimumot szab meg", "The cybersecurity regulation sets a detailed compliance minimum for all state institutions.", ["c1-regulatory-compliance-syntax"]),
                sb("grammar", "practice", ["A", "törvény", "független", "bírói", "kontrollt", "ír", "elő", "minden", "esetben."], ["A", "törvény", "független", "bírói", "kontrollt", "ír", "elő", "minden", "esetben."], "The law prescribes independent judicial oversight in every case.", ["c1-regulatory-compliance-syntax"]),
                dc("dialogue", [
                    {"speaker": "Vizsgálóbizottsági tag", "text": "Hogyan garantálható, hogy a kémszoftvereket ne használják politikai ellenfelek ellen?"},
                    {"speaker": "Ombudsman", "text": "A jogszabálynak szigorú, előzetes és független bírói _____ kell megkövetelnie."},
                ], ["engedélyezést", "segítséget", "ünneplést"], 0, ["c1-regulatory-compliance-syntax"]),
                sw("production", [{"prompt": "Formulate a legal mandate on spyware regulation using 'garanciákat követel meg'.", "answer": "A demokratikus jogállam szigorú eljárási garanciákat követel meg, hogy megakadályozza az újságírók és jogvédők politikai motivációjú megfigyelését."}], ["c1-regulatory-compliance-syntax"]),
                mc("grammar", "check", "Melyik állítmány fejez ki kötelező erejű jogszabályi előírást (deontic regulatory predicate)?", [
                    "auditkötelezettséget ír elő",
                    "reményét fejezi ki",
                    "szívesen látna javulást"
                ], 0, ["c1-regulatory-compliance-syntax"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "NIS2 Directive, GovCERT & Institutional Defence Reform",
            "grammar_title": "Epistemic Uncertainty Markers Modulating Attribution Confidence in Threat Intelligence Analysis",
            "grammar_skill": "c1-epistemic-uncertainty-markers",
            "goals": [
                "I can evaluate EU cybersecurity governance, the NIS2 Directive, and GovCERT-Hungary incident response (*NIS2-irányelv, GovCERT-Hungary, incidenskezelés, kiberhigiénia*).",
                "I can calibrate threat intelligence attribution using epistemic uncertainty markers (*minden valószínűség szerint, vélhetően államilag támogatott, feltételezhetően, hitelt érdemlően nem bizonyítható*).",
                "I can explain mandatory incident notification thresholds and supply chain cybersecurity audits."
            ],
            "vocab": [
                {"lemma": "NIS2-irányelv", "translation": "NIS2 Directive (EU)", "pos": "noun"},
                {"lemma": "kiberbiztonsági tanúsítás", "translation": "cybersecurity certification", "pos": "expression"},
                {"lemma": "incidenskezelés", "translation": "incident handling / response", "pos": "noun"},
                {"lemma": "szigorú incidensbejelentési kötelezettség", "translation": "strict incident notification duty", "pos": "expression"},
                {"lemma": "kiberhigiénia", "translation": "cyber hygiene", "pos": "noun"},
                {"lemma": "megfelelési audit", "translation": "compliance audit", "pos": "expression"},
                {"lemma": "GovCERT-Hungary", "translation": "GovCERT-Hungary (national CSIRT)", "pos": "noun"},
                {"lemma": "ellátási lánc átvilágítása", "translation": "supply chain screening", "pos": "expression"}
            ],
            "gr_text1": "In cybersecurity threat intelligence and technical attribution, absolute certainty is rare due to obfuscation, VPN bouncing, and false-flag operations. Hungarian modulates attribution confidence via epistemic markers: `minden valószínűség szerint` (in all likelihood), `vélhetően / vélhetőleg` (presumably), `feltételezhetően állami hátterű` (presumably state-sponsored), `hitelt érdemlően nem zárható ki` (cannot credibly be excluded), `a rendelkezésre álló bizonyítékok arra engednek következtetni` (available evidence leads to the conclusion).",
            "gr_text2": "Example: `A támadók taktikai módszerei és kódmintái minden valószínűség szerint egy külföldi katonai hírszerzéshez köthető APT-csoport közreműködésére engednek következtetni`.",
            "gr_table": [
                ["A kormányzati hálózat elleni behatolást, minden valószínűség szerint, egy külföldi APT-csoport hajtotta végre.", "The intrusion against the government network was, in all likelihood, executed by a foreign APT group."],
                ["A zsarolóvírus forráskódja vélhetően egy ismert kiberbűnözői szindikátustól származik.", "The ransomware's source code presumably originates from a known cybercrime syndicate."],
                ["Bár az elkövetők rejtőzködnek, a technikai bizonyítékok feltételezhetően állami támogatásra utalnak.", "Although the perpetrators hide, technical evidence presumably points to state sponsorship."]
            ],
            "world_story_seg": {
                "seg_slug": "nis2",
                "title": "A védelem reformja: A NIS2-irányelv és a GovCERT-Hungary intézményi küzdelme",
                "summary": "How NIS2 compliance obligations and GovCERT incident response units re-engineer Hungary's national cyber defence posture across public and private sectors.",
                "paragraphs": [
                    {"type": "narration", "text": "Az Európai Unió válasza a hibrid hadviselés eszkalációjára a NIS2-irányelv elfogadása volt, amely radikális szemléletváltást kényszerített ki az állami és a versenyszféra szereplőiből egyaránt. A szabályozás nemcsak drasztikusan szigorította az incidensbejelentési kötelezettséget, hanem a cégek felsővezetőinek személyes jogi és anyagi felelősségét is megállapította kiberbiztonsági mulasztások esetén."},
                    {"type": "narration", "text": "Magyarországon a GovCERT-Hungary csapata vette át az országos incidenskezelés karmesteri pálcáját. A szakértők éjjel-nappali monitorozással védik a minisztériumi gerinchálózatokat, elemzik a rosszindulatú kódmintákat, és közvetlen kapcsolatot tartanak az európai kiberbiztonsági ügynökséggel (ENISA). A feladat gigantikus: az ellátási láncok több ezer kis- és középvállalkozását kell felkészíteni az auditokra, garantálva, hogy egyetlen elhanyagolt beszállító se válhasson a nemzeti infrastruktúra Achilles-sarkává."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen áttörést hoz az Európai Unió NIS2-irányelve a vállalati kibervédelemben?", [
                    "Kötelezővé teszi a 24 órán belüli incidensbejelentést, kiterjeszti a felelősséget a felsővezetésre, és szigorú bírságokat szab ki a mulasztásokra.",
                    "Ingyenes laptopot biztosít minden európai középiskolás diáknak.",
                    "Megtiltja a számítógépek éjszakai kikapcsolását a minisztériumokban."
                ], 0, ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "controlled", "A támadás komplexitása alapján az akciót _____ egy állami háttérrel rendelkező egység szervezte. (in all likelihood / minden valószínűség szerint)", "minden valószínűség szerint", "Based on the complexity of the attack, the action was in all likelihood organized by a unit with state backing.", ["c1-epistemic-uncertainty-markers"]),
                match("vocabulary", "controlled", [["NIS2-irányelv", "az EU megújított kiberbiztonsági jogszabálya"], ["GovCERT-Hungary", "a nemzeti kormányzati incidenskezelő központ"], ["kiberhigiénia", "alapvető biztonsági szokások és eljárások"], ["megfelelési audit", "a biztonsági előírások teljesülésének hivatalos vizsgálata"]], ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "practice", "A logfájlok elemzése alapján az elkövetők _____ több hónapon át észrevétlenül tartózkodtak a rendszerben. (presumably / vélhetően)", "vélhetően", "Based on the analysis of log files, the perpetrators presumably remained unnoticed in the system for several months.", ["c1-epistemic-uncertainty-markers"]),
                sb("grammar", "practice", ["A", "támadók", "minden", "valószínűség", "szerint", "orosz", "nyomokat", "hagytak."], ["A", "támadók", "minden", "valószínűség", "szerint", "orosz", "nyomokat", "hagytak."], "The attackers in all likelihood left Russian traces.", ["c1-epistemic-uncertainty-markers"]),
                dc("dialogue", [
                    {"speaker": "Védelmi tanácsadó", "text": "Biztosak lehetünk abban, hogy melyik külföldi hírszerzés áll a támadás mögött?"},
                    {"speaker": "Hálózatelemző", "text": "A technikai bizonyítékok minden valószínűség szerint egy keleti APT-csoportra utalnak, ám a felelősségvállalás teljes bizonyossággal nem _____."},
                ], ["bizonyítható", "tagadható", "ünnepelhető"], 0, ["c1-epistemic-uncertainty-markers"]),
                sw("production", [{"prompt": "Write a threat attribution assessment sentence using 'minden valószínűség szerint'.", "answer": "A támadás módszertana és a célpontok köre minden valószínűség szerint államilag támogatott szereplők beavatkozását valószínűsíti."}], ["c1-epistemic-uncertainty-markers"]),
                mc("grammar", "check", "Melyik kifejezés fejez ki óvatos, magas valószínűségű tényattribúciót (epistemic uncertainty marker)?", [
                    "minden valószínűség szerint / vélhetően",
                    "biztosan nem és soha",
                    "teljesen kizárt módon"
                ], 0, ["c1-epistemic-uncertainty-markers"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Surveillance Capitalism, Big Tech & GDPR in the AI Era",
            "grammar_title": "Proportional Correlative Constructions Analyzing Systemic Complexity and Attack Surface Exposure",
            "grammar_skill": "c1-adv-proportional-threat-correlatives",
            "goals": [
                "I can critique platform monopolies, surveillance capitalism, and GDPR enforcement (*megfigyelési kapitalizmus, GDPR, platformmonopólium, biometrikus profilalkotás*).",
                "I can construct proportional correlatives linking systemic exposure to threat surface (*minél összetettebb a hálózat, annál nagyobb a támadási felület; minél több adatot gyűjtenek, annál sebezhetőbb a magánszféra*).",
                "I can debate data minimization and accountability principles in generative AI training."
            ],
            "vocab": [
                {"lemma": "adatvédelmi incidens", "translation": "personal data breach", "pos": "expression"},
                {"lemma": "célzott dezinformáció", "translation": "targeted disinformation", "pos": "expression"},
                {"lemma": "biometrikus profilalkotás", "translation": "biometric profiling", "pos": "expression"},
                {"lemma": "platformmonopólium", "translation": "platform monopoly", "pos": "noun"},
                {"lemma": "felhasználói hozzájárulás", "translation": "user consent", "pos": "expression"},
                {"lemma": "elszámoltathatóság elve", "translation": "principle of accountability", "pos": "expression"},
                {"lemma": "adatminimalizálás", "translation": "data minimization", "pos": "noun"},
                {"lemma": "felügyeleti hatóság", "translation": "supervisory authority (e.g. NAIH)", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures (`minél [fokozott melléknév/határozószó], annál / annál is inkább [fokozott melléknév/határozószó]`) in C1 analysis link two variable phenomena in proportional causality: `Minél összetettebb egy informatikai architektúra, annál kiszolgáltatottabbá válik a váratlan zéró napi sebezhetőségekkel szemben`.",
            "gr_text2": "This structure is fundamental when modeling scaling laws, systemic risks, and proportional regulatory requirements in digital policy.",
            "gr_table": [
                ["Minél több személyes adatot halmoznak fel a tech-óriások, annál súlyosabb következményekkel jár egy esetleges adatszivárgás.", "The more personal data the tech giants accumulate, the graver consequences any potential data breach entails."],
                ["Minél mélyebben integrálódik a mesterséges intelligencia a döntéshozatalba, annál szigorúbb emberi felügyeletre van szükség.", "The more deeply artificial intelligence is integrated into decision making, the stricter human oversight is required."],
                ["Minél kiterjedtebb a digitális profilalkotás, annál kiszolgáltatottabb a választópolgár a célzott dezinformációs kampányoknak.", "The more extensive digital profiling is, the more vulnerable the voter is to targeted disinformation campaigns."]
            ],
            "world_story_seg": {
                "seg_slug": "adatvedelem",
                "title": "Adatbányászat és manipuláció: A megfigyelési kapitalizmus hálójában",
                "summary": "Analyzing the silent societal transformation of big data extraction, platform dominance, and how GDPR and the AI Act attempt to restore informational human dignity.",
                "paragraphs": [
                    {"type": "narration", "text": "Miközben a hírek a látványos hekkertámadásoktól hangosak, a polgárok mindennapi életét egy sokkal csendesebb, de mélyebb folyamat formálja át: a megfigyelési kapitalizmus. A digitális platformmonopóliumok láthatatlan algoritmusai másodpercenként milliárdnyi viselkedési adatot rögzítenek, elemeznek és alakítanak át prediktív profilokká. Nemcsak azt tudják, mit vásárolunk, hanem azt is, mitől félünk, mit gyűlölünk, és melyik pillanatban vagyunk a leginkább befolyásolhatók."},
                    {"type": "narration", "text": "A GDPR és a legújabb uniós Mesterséges Intelligencia Rendelet (AI Act) gigantikus jogi kísérlet arra, hogy gátat szabjon ennek a gátlástalan adatgyarmatosításnak. Az adatminimalizálás és az átláthatóság alkotmányos követelménye azt hirdeti: az ember nem válhat algoritmusok által manipulált digitális biomasszává. A technológia igazi próbája az, hogy képesek vagyunk-e megvédeni a szabad véleményformálás és a magánélet intimitását a mesterséges neurális hálók korában."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit ír elő az 'adatminimalizálás' (data minimization) elve a GDPR szerint?", [
                    "Hogy a szervezetek kizárólag a feltétlenül szükséges mértékű és típusú személyes adatot gyűjthetik és kezelhetik a megjelölt cél érdekében.",
                    "Hogy az adatbázisokat minél kisebb betűmérettel kell kinyomtatni papírra.",
                    "Hogy a cégek csak heti egyetlen emailt küldhetnek az ügyfeleiknek."
                ], 0, ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "controlled", "_____ az ellátási lánc, annál nagyobb a rejtett sebezhetőségek beépülésének kockázata. (The more complex / Minél összetettebb)", "Minél összetettebb", "The more complex the supply chain, the greater the risk of embedding hidden vulnerabilities.", ["c1-adv-proportional-threat-correlatives"]),
                match("vocabulary", "controlled", [["platformmonopólium", "a digitális piacokat uraló óriásvállalat"], ["biometrikus profilalkotás", "testi jellemzőkön alapuló viselkedéselemzés"], ["adatminimalizálás", "csak a célhoz feltétlenül szükséges adatok kezelése"], ["felügyeleti hatóság", "a GDPR betartását ellenőrző nemzeti szerv"]], ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "practice", "Minél kiterjedtebb az adathalászat, _____ válik a digitálisan képzetlen lakosság. (the more vulnerable / annál sebezhetőbbé)", "annál sebezhetőbbé", "The more extensive the phishing, the more vulnerable the digitally uneducated population becomes.", ["c1-adv-proportional-threat-correlatives"]),
                sb("grammar", "practice", ["Minél", "több", "az", "adat,", "annál", "nagyobb", "a", "kockázat."], ["Minél", "több", "az", "adat,", "annál", "nagyobb", "a", "kockázat."], "The more data there is, the greater the risk.", ["c1-adv-proportional-threat-correlatives"]),
                dc("dialogue", [
                    {"speaker": "Adatvédelmi tisztviselő", "text": "Mekkora kockázatot jelent a felhasználói adatok korlátlan gyűjtése?"},
                    {"speaker": "Biztonsági auditor", "text": "Minél több adatot tárolunk egy helyen, annál kívánatosabb _____ válik az adatbázis a hackerek számára."},
                ], ["célponttá", "játékszerré", "ajándékká"], 0, ["c1-adv-proportional-threat-correlatives"]),
                sw("production", [{"prompt": "Write a proportional analytical sentence about artificial intelligence using 'minél... annál...'.", "answer": "Minél önállóbban működnek az autonóm algoritmusok, annál nélkülözhetetlenebbé válik a szigorú és átlátható jogi felelősségre vonhatóság garantálása."}], ["c1-adv-proportional-threat-correlatives"]),
                mc("grammar", "check", "Melyik kötőszópáros fejez ki fokozott arányossági viszonyt (proportional correlative)?", [
                    "minél... annál",
                    "holott... mégis",
                    "miután... ezért"
                ], 0, ["c1-adv-proportional-threat-correlatives"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "National Resilience, Quantum Cryptography & Sovereign Future",
            "grammar_title": "Strategic Synthesis Particles Deriving Definitive Policy Conclusions in National Security Doctrine",
            "grammar_skill": "c1-adv-conclusive-synthesis-markers",
            "goals": [
                "I can articulate strategic national cyber resilience, quantum communication, and digital defense doctrines (*társadalmi ellenállóképesség, kvantumkriptográfia, szuverén európai felhő, hibrid hadviselés elhárítása*).",
                "I can synthesize strategic policy recommendations using conclusive discourse markers (*mindent egybevetve, végkövetkeztetésként levonható, összességében megállapítható, összegzésképpen leszögezhető*).",
                "I can formulate a holistic vision for Central European cyber independence in a multipolar world."
            ],
            "vocab": [
                {"lemma": "társadalmi ellenállóképesség", "translation": "societal resilience", "pos": "expression"},
                {"lemma": "kvantumkriptográfia", "translation": "quantum cryptography", "pos": "noun"},
                {"lemma": "szuverén európai felhő", "translation": "sovereign European cloud", "pos": "expression"},
                {"lemma": "digitális immunitás", "translation": "digital immunity", "pos": "expression"},
                {"lemma": "védelmi doktrína", "translation": "defense doctrine", "pos": "expression"},
                {"lemma": "hibrid hadviselés elhárítása", "translation": "countering hybrid warfare", "pos": "expression"},
                {"lemma": "stratégiai autonómia", "translation": "strategic autonomy", "pos": "expression"},
                {"lemma": "információs integritás", "translation": "information integrity", "pos": "expression"}
            ],
            "gr_text1": "The ultimate strategic synthesis in defense white papers and policy treatises uses conclusive introductory markers to integrate multifaceted evidence into an authoritative verdict: `mindent egybevetve` (all things considered / taking everything together), `végkövetkeztetésként levonható, hogy...` (as an ultimate conclusion it can be drawn that), `összességében megállapítható` (on the whole it can be stated), `összegzésképpen leszögezhető` (in summary it can be firmly laid down that).",
            "gr_text2": "Example: `Mindent egybevetve, a kiberbiztonság ma már nem elszigetelt informatikai kérdés, hanem a nemzeti önrendelkezés és a társadalmi túlélés alapköve`.",
            "gr_table": [
                ["Mindent egybevetve, a kibertér védelme a huszonegyedik századi nemzetvédelem első vonalává vált.", "All things considered, defending cyberspace has become the frontline of twenty-first-century national defence."],
                ["Végkövetkeztetésként levonható, hogy a szuverén infrastruktúra kiépítése nélkül nincs valódi geopolitikai függetlenség.", "As an ultimate conclusion it can be drawn that without building sovereign infrastructure there is no genuine geopolitical independence."],
                ["Összegzésképpen leszögezhető, hogy a társadalmi ellenállóképesség kulcsa az állampolgárok kiberhigiénés tudatosságában rejlik.", "In summary it can be firmly stated that the key to societal resilience lies in citizens' cyber hygiene awareness."]
            ],
            "world_story_seg": {
                "seg_slug": "reziliencia",
                "title": "A szuverén jövő: Kvantumkriptográfia és nemzeti ellenállóképesség",
                "summary": "Exploring quantum key distribution (QKD) physics and why technological protection must be rooted in citizen education and democratic institutions to achieve true resilience.",
                "paragraphs": [
                    {"type": "narration", "text": "A jövő információs harctere már a kvantumfizika laboratóriumaiban épül. A kvantumszámítógépek elméleti ígérete a jelenlegi banki és katonai titkosítások felbomlásával fenyeget. Válaszul a magyar és európai kutatók olyan kvantum-kulcsszétosztási (QKD) protokollokon dolgoznak, amelyek a fény polarizációjával teszik fizikailag lehetetlenné a lehallgatást: amint egy illetéktelen behatoló megkísérli a mérést, a fotonok állapota összeomlik, és a támadás azonnal lelepleződik."},
                    {"type": "narration", "text": "Mindent egybevetve, a technológiai bravúrok önmagukban mégsem elégségesek. A nemzet valódi védőbástyája a társadalmi ellenállóképesség: a kritikus gondolkodásra nevelt, digitálisan művelt polgárok közössége, akik felismerik a dezinformációt, óvják személyes adataikat, és ragaszkodnak a jogállami intézmények védelméhez. A digitális szuverenitás nem a külvilágtól való bezárkózást jelenti, hanem azt a belső erőt és intellektuális függetlenséget, amellyel egy kis nemzet is képes szabadon és méltósággal megállni a helyét a globális kibertér viharaiban."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'társadalmi ellenállóképesség' (societal resilience) a kibertérben?", [
                    "A társadalom, az intézmények és az állampolgárok azon képességét, hogy elviseljék, kivédjék és gyorsan kiheverjék a súlyos dezinformációs és kiberinfrastruktúra-támadásokat.",
                    "A lakosság fizikai állóképességének tesztelését az edzőtermekben.",
                    "A wifi-jelszavak betiltását az irodákban."
                ], 0, ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "controlled", "_____, a digitális szuverenitás megteremtése a nemzet fennmaradásának záloga. (All things considered / Mindent egybevetve)", "Mindent egybevetve", "All things considered, establishing digital sovereignty is the pledge of the nation's survival.", ["c1-adv-conclusive-synthesis-markers"]),
                match("vocabulary", "controlled", [["kvantumkriptográfia", "a fizika törvényein alapuló feltörhetetlen kulcscsere"], ["szuverén európai felhő", "európai joghatóság alá tartozó adatközpont-hálózat"], ["stratégiai autonómia", "független döntéshozatali képesség kulcsfontosságú területeken"], ["digitális immunitás", "a rendszerek képessége az azonnali öngyógyításra"]], ["c1-kiberbiztonsag-vocab"]),
                fb("grammar", "practice", "Végkövetkeztetésként _____ hogy az oktatás és a technológia együttesen teremtheti meg a biztonságunkat. (can be drawn / levonható)", "levonható", "As an ultimate conclusion it can be drawn that education and technology together can create our security.", ["c1-adv-conclusive-synthesis-markers"]),
                sb("grammar", "practice", ["Mindent", "egybevetve,", "a", "kiberbiztonság", "a", "szabadság", "alapja."], ["Mindent", "egybevetve,", "a", "kiberbiztonság", "a", "szabadság", "alapja."], "All things considered, cybersecurity is the foundation of freedom.", ["c1-adv-conclusive-synthesis-markers"]),
                dc("dialogue", [
                    {"speaker": "Külügyi szakértő", "text": "Hogyan összegezhetjük a digitális szuverenitásért folytatott küzdelmet?"},
                    {"speaker": "Nemzetbiztonsági tanácsadó", "text": "Mindent egybevetve, a technológiai önrendelkezés nélkül a nemzeti szuverenitás üres _____ válik."},
                ], ["jelszóvá", "ajándékká", "fegyverré"], 0, ["c1-adv-conclusive-synthesis-markers"]),
                sw("production", [{"prompt": "Write a concluding thesis on national cybersecurity using 'Végkövetkeztetésként levonható, hogy...'.", "answer": "Végkövetkeztetésként levonható, hogy az államnak a kritikus infrastruktúrák megerősítése mellett a lakosság digitális műveltségét is fejlesztenie kell az ellenállóképesség biztosításához."}], ["c1-adv-conclusive-synthesis-markers"]),
                mc("grammar", "check", "Melyik partikula szolgál végső stratégiai szintézis és doktrinális konklúzió levonására?", [
                    "mindent egybevetve / végkövetkeztetésként levonható",
                    "eleinte még",
                    "olykor-olykor"
                ], 0, ["c1-adv-conclusive-synthesis-markers"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(18, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A láthatatlan frontvonal: Kiberhadviselés, digitális szuverenitás és polgári ellenállóképesség",
            "level": "C1",
            "type": "world",
            "order": 18,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of twenty-first century cyber warfare, critical infrastructure defense (MVM grid, hospital ransomware), Pegasus surveillance ethics and judicial oversight, NIS2 compliance, surveillance capitalism under GDPR, and quantum cryptographic sovereignty.",
            "grammar": [
                "c1-discourse-threat-framing",
                "c1-regulatory-compliance-syntax",
                "c1-epistemic-uncertainty-markers",
                "c1-adv-proportional-threat-correlatives",
                "c1-adv-conclusive-synthesis-markers"
            ],
            "vocabularyTopics": [
                "Cyber Warfare, Critical Infrastructure Protection & Citizen Resilience",
                "State-Sponsored Cyber Warfare & Critical Infrastructure Siege",
                "Pegasus, Zero-Days & Lawful Interception Ethics",
                "NIS2 Directive, GovCERT & Institutional Defence Reform",
                "Surveillance Capitalism, Big Tech & GDPR in the AI Era",
                "National Resilience, Quantum Cryptography & Sovereign Future"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A huszonegyedik században a hadviselés és a geopolitikai hatalomgyakorlás jellege gyökeresen megváltozott: a tankok és repülőgépek mellett a láthatatlan bites folyamok váltak a nemzeti szuverenitás elsődleges védelmi vonalává. Amikor 2024-ben az MVM villamosenergia-hálózatát és több regionális kórházat összehangolt kiberostrom ért, nyilvánvalóvá vált: az ipari SCADA-rendszerek és az egészségügyi adatbázisok biztonsága az egész társadalom életképességének záloga."},
                {"type": "narration", "text": "A technológia fegyverré válása azonban nemcsak külső ellenségek formájában jelentkezik: a Pegasus-ügy feltárta, hogy a katonai minőségű kémszoftverek független bírói kontroll nélküli alkalmazása közvetlen veszélyt jelent az állampolgárok magánszférájára és a demokratikus nyilvánosságra. A zero-click sebezhetőségek korában a jogállami garanciák megerősítése elengedhetetlen előfeltétel."},
                {"type": "narration", "text": "Az intézményi válasz sem késlekedhetett: az Európai Unió NIS2-irányelve és a GovCERT-Hungary szakértői hálózata új védelmi doktrínát léptetett életbe. A szigorú incidensbejelentési kötelezettség és az ellátási láncok mélyreható auditja arra kényszeríti a szervezeteket, hogy a kiberhigiéniát ne adminisztratív teherként, hanem a napi működés alapvető reflexeként kezeljék."},
                {"type": "narration", "text": "Ugyanakkor a polgárok jogait a megfigyelési kapitalizmus profitéhes adatgyarmatosításával szemben is meg kell védeni. A GDPR és az új mesterséges intelligencia szabályozás elvei szerint az ember nem válhat algoritmusok által kiszámított és manipulált biometrikus profillá: a digitális önrendelkezés elidegeníthetetlen alkotmányos alapjog."},
                {"type": "narration", "text": "Mindent egybevetve, a jövő biztonsága a kvantumkriptográfia fizikai feltörhetetlenségén és a társadalmi ellenállóképesség kiművelésén múlik. A digitális szuverenitás nem elszigetelődés a technológiai fejlődéstől, hanem az a tudatos képesség, amellyel egy független nemzet megvédi polgárai szabadságát, intézményei integritását és szellemi méltóságát a kibertér állandóan változó világában."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        18,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze cyber warfare, ransomware attacks on infrastructure, and the zero trust security model.",
            "I can evaluate Pegasus spyware ethics, NIS2 regulatory compliance, and threat intelligence attribution.",
            "I can debate surveillance capitalism, data minimization under GDPR, and quantum cryptography resilience."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fogalmazhatunk meg rendszerszintű fenyegetést a kiberbiztonsági elemzésben?", [
                "akut nemzetbiztonsági kockázatot hordoz / közvetlen veszélyt idéz elő / sérülékenységet tár fel",
                "mindazonáltal megbeszélték a dolgot",
                "szép időben sétálnak a parkban"
            ], 0, ["c1-discourse-threat-framing"]),
            mc("grammar", "recognize", "Milyen kifejezésekkel írhatunk le hatósági kötelezettséget a NIS2-irányelv kapcsán?", [
                "szigorú auditkötelezettséget ír elő / megfelelési minimumot szab meg / bírói engedélyezést követel meg",
                "ha van kedvük, megcsinálják",
                "nem szükséges jelentést írni"
            ], 0, ["c1-regulatory-compliance-syntax"]),
            match("vocabulary", "recognize", [["SCADA-rendszer", "ipari infrastruktúra-vezérlés"], ["Pegasus", "katonai fokozatú kémszoftver"], ["GovCERT-Hungary", "kormányzati incidenskezelő központ"], ["adatminimalizálás", "GDPR alapelv: csak a szükséges adat gyűjtése"], ["kvantumkriptográfia", "feltörhetetlen kulcscsere fizikai alapokon"]], ["c1-kiberbiztonsag-vocab"]),
            fb("vocabulary", "recall", "A kórházak informatikai leállását egy zsarolási célból terjesztett _____ okozta. (ransomware / zsarolóvírus)", "zsarolóvírus", "The IT outage of hospitals was caused by ransomware distributed for extortion purposes.", ["c1-kiberbiztonsag-vocab"]),
            fb("vocabulary", "recall", "A kibertámadások kivédésére a modern rendszerek a _____ alapján épülnek fel. (zero trust principle / zéró megbízhatóság elve)", "zéró megbízhatóság elve", "To repel cyber attacks, modern systems are built upon the zero trust principle.", ["c1-kiberbiztonsag-vocab"]),
            fb("grammar", "recall", "A támadás komplexitása alapján a nyomok _____ egy állami hekkercsoportra utalnak. (presumably / minden valószínűség szerint)", "minden valószínűség szerint", "Based on the attack complexity the traces in all likelihood point to a state hacker group.", ["c1-epistemic-uncertainty-markers"]),
            fb("grammar", "context", "Minél kiterjedtebb az adatgyűjtés, _____ válik a polgárok magánélete. (the more vulnerable / annál sebezhetőbbé)", "annál sebezhetőbbé", "The more extensive data collection is, the more vulnerable citizens' private life becomes.", ["c1-adv-proportional-threat-correlatives"]),
            fb("grammar", "context", "A törvényhozás szigorú incidensbejelentési határidőt _____ a bankok számára. (prescribes / ír elő)", "ír elő", "The legislature prescribes a strict incident notification deadline for banks.", ["c1-regulatory-compliance-syntax"]),
            mc("grammar", "context", "Milyen funkciót tölt be a 'Mindent egybevetve...' indítás egy szakpolitikai doktrínában?", [
                "Egybekapcsolja az összes részletes biztonsági tapasztalatot egy megkérdőjelezhetetlen stratégiai végső tanulsággá.",
                "Megváltoztatja a megbeszélés helyszínét.",
                "Elnézést kér az olvasótól az összetett szakszavak miatt."
            ], 0, ["c1-adv-conclusive-synthesis-markers"]),
            sb("grammar", "produce", ["A", "társadalmi", "ellenállóképesség", "a", "kibertérben", "is", "döntő", "tényező."], ["A", "társadalmi", "ellenállóképesség", "a", "kibertérben", "is", "döntő", "tényező."], "Societal resilience in cyberspace is also a decisive factor.", ["c1-adv-conclusive-synthesis-markers"]),
            sw("production", [{"prompt": "Write a critical assessment of Pegasus and surveillance spyware ethics.", "answer": "A kémszoftverek bevetése, független bírói kontroll hiányában, közvetlen veszélyt idéz elő a demokratikus jogállam és a sajtószabadság épségére nézve."}], ["c1-regulatory-compliance-syntax"]),
            sw("production", [{"prompt": "Formulate a concluding thought on cyber resilience and digital sovereignty in Central Europe.", "answer": "Mindent egybevetve, a kiberbiztonság nem pusztán technikai feladvány, hanem a nemzeti önrendelkezés, az emberi méltóság és a polgári szabadság huszonegyedik századi záloga."}], ["c1-adv-conclusive-synthesis-markers"])
        ]
    )

    print("=== Finished C1 Unit 18 ===")


if __name__ == "__main__":
    generate_unit_18()
