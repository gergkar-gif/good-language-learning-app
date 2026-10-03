#!/usr/bin/env python3
"""
Hungarian C1 Block 3 - Unit 16 Generator:
  - Track 1 (Core): Unit 16 — "Public Sphere, Rhetorical Framing & Deliberative Communication" (c1-16)
  - Track 2 (Discourse): Unit 16 — "Media Pluralism, Algorithmic Filters & Information Integrity" (c1-mediakritika)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block3.registry_helper import register_unit


def generate_unit_16():
    print("=== Generating C1 Unit 16 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-16-vocab": {"kind": "vocabulary"},
        "c1-mediakritika-vocab": {"kind": "vocabulary"},
        "c1-concessive-adversative-connectors": {"kind": "grammar"},
        "c1-rhetorical-hypothetical-questions": {"kind": "grammar"},
        "c1-adv-passive-substitute-phrases": {"kind": "grammar"},
        "c1-modal-epistemic-distancing": {"kind": "grammar"},
        "c1-adv-circumstantial-participial-clauses": {"kind": "grammar"},
        "c1-discourse-polarizing-contrastives": {"kind": "grammar"},
        "c1-evaluative-adverbial-stance": {"kind": "grammar"},
        "c1-adversative-resumptive-markers": {"kind": "grammar"},
        "c1-subjunctive-regulatory-mandates": {"kind": "grammar"},
        "c1-adv-emphatic-scalar-particles": {"kind": "grammar"},
    }
    new_titles = {
        "c1-16-vocab": "reading",
        "c1-mediakritika-vocab": "reading",
        "c1-concessive-adversative-connectors": "complex concessive and adversative sentence connectors in argumentation",
        "c1-rhetorical-hypothetical-questions": "rhetorical and deliberative interrogative structures in political prose",
        "c1-adv-passive-substitute-phrases": "impersonal passive equivalent verbal periphrases with modal necessity",
        "c1-modal-epistemic-distancing": "epistemic distancing markers and evidential qualification in journalism",
        "c1-adv-circumstantial-participial-clauses": "circumstantial participial adjunct clauses in deliberative discourse",
        "c1-discourse-polarizing-contrastives": "polarizing and contrastive discourse coordinators in media critique",
        "c1-evaluative-adverbial-stance": "evaluative stance adverbials expressing moral or intellectual judgement",
        "c1-adversative-resumptive-markers": "adversative resumptive discourse markers structuring complex commentary",
        "c1-subjunctive-regulatory-mandates": "deontic and regulatory subjunctive clauses in institutional mandates",
        "c1-adv-emphatic-scalar-particles": "emphatic scalar additive particles highlighting extreme propositions",
    }
    
    core_title = "Public Sphere, Rhetorical Framing & Deliberative Communication"
    core_stems = [f"c1-16-0{i}" for i in range(1, 6)] + ["c1-16-consolidation"]
    disc_title = "Media Pluralism, Algorithmic Filters & Information Integrity"
    disc_stems = [f"c1-mediakritika-0{i}" for i in range(1, 6)] + ["c1-mediakritika-consolidation"]
    
    register_unit(16, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-16)
    # ----------------------------------------------------
    core_intro = [
        "The democratic public sphere, rhetorical framing, and communicative rationality in Hungarian require nuanced command of concessive nuance, impersonal passive modalities, and deliberative rhetoric.",
        "In this unit, anchored by István Bibó's immortal political philosophy ('The Misery of Small Eastern European States', 1946) dissecting political hysteria, fear, and democratic deliberation, you will master the analytical vocabulary and structural syntax of the public sphere at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-16-01",
            "title": "Deliberative Democracy & The Structural Public Sphere",
            "grammar_title": "Complex Concessive and Adversative Connectors in Argumentation",
            "grammar_skill": "c1-concessive-adversative-connectors",
            "goals": [
                "I can analyze Habermas's public sphere and deliberative democracy (*nyilvánosság szerkezete, konszenzuskeresés, racionális diskurzus*).",
                "I can deploy complex concessive connectors (*mindazonáltal, ámbár, annak dacára hogy, mindamellett*).",
                "I can debate citizen participation and communicative ethics in intellectual Hungarian."
            ],
            "vocab": [
                {"lemma": "nyilvánosság szerkezete", "translation": "structure of the public sphere", "pos": "expression"},
                {"lemma": "deliberatív demokrácia", "translation": "deliberative democracy", "pos": "expression"},
                {"lemma": "konszenzuskeresés", "translation": "consensus seeking", "pos": "noun"},
                {"lemma": "racionális diskurzus", "translation": "rational discourse", "pos": "expression"},
                {"lemma": "érvelési hiba", "translation": "fallacy, argumentative flaw", "pos": "noun"},
                {"lemma": "társadalmi párbeszéd", "translation": "social dialogue", "pos": "expression"},
                {"lemma": "érdekegyeztetés", "translation": "interest reconciliation", "pos": "noun"},
                {"lemma": "elszámoltathatóság", "translation": "accountability", "pos": "noun"}
            ],
            "gr_text1": "Complex concessive and adversative connectors (*mindazonáltal* [nevertheless], *ámbár* [although], *mindamellett* [at the same time / besides], *annak dacára, hogy* [in spite of the fact that]) balance conflicting claims: `A nyilvános vita gyakran polarizált; mindazonáltal a deliberáció marad a demokratikus legitimáció egyetlen hiteles forrása`.",
            "gr_text2": "In academic political discourse, concessive clauses concede an opponent's valid point before asserting an overriding systemic conclusion: `Ámbár az egyeztetési eljárások időigényesek, a részvételi döntések tartósabb társadalmi békét eredményeznek`.",
            "gr_table": [
                ["A felek álláspontja távol állt egymástól, mindazonáltal sikerült közös nevezőre jutniuk.", "The parties' positions stood far apart; nevertheless, they managed to find common ground."],
                ["Annak dacára, hogy a vitát heves indulatok kísérték, a racionális érvek érvényesültek.", "In spite of the fact that intense tempers accompanied the debate, rational arguments prevailed."],
                ["Ámbár a törvényjavaslat nem hibátlan, mindamellett lényeges előrelépést jelent a civil jogok terén.", "Although the bill is not flawless, besides it represents substantial progress in civil rights."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'deliberatív demokrácia' fogalma a politikatudományban?", [
                    "Olyan döntéshozatali modellt, amelyben a politikai döntések érvényességét a polgárok közötti racionális, egyenlő és nyílt vita adja.",
                    "A választások teljes eltörlését és egyetlen vezető kijelölését.",
                    "A televíziós hirdetések kötelező megtekintését minden este."
                ], 0, ["c1-16-vocab"]),
                fb("grammar", "controlled", "A politikai polarizáció rendkívül mély, _____ (nevertheless / mindazonáltal) a kompromisszumos megoldás nem lehetetlen.", "mindazonáltal", "Political polarization is extremely deep, nevertheless a compromise solution is not impossible.", ["c1-concessive-adversative-connectors"]),
                match("vocabulary", "controlled", [["konszenzuskeresés", "közös megegyezés célja"], ["racionális diskurzus", "észérveken alapuló párbeszéd"], ["érvelési hiba", "logikai tévedés a vitában"], ["elszámoltathatóság", "hatalom felelősségre vonhatósága"]], ["c1-16-vocab"]),
                fb("grammar", "practice", "_____ dacára, hogy a részvétel alacsony volt, a konzultáció eredménye tanulságosnak bizonyult. (In spite of / Annak)", "Annak", "In spite of the fact that participation was low, the outcome of the consultation proved instructive.", ["c1-concessive-adversative-connectors"]),
                sb("grammar", "practice", ["A", "demokratikus", "nyilvánosság", "alapfeltétele", "a", "vélemények", "szabad", "és", "egyenlő", "ütköztetése."], ["A", "demokratikus", "nyilvánosság", "alapfeltétele", "a", "vélemények", "szabad", "és", "egyenlő", "ütköztetése."], "The precondition of the democratic public sphere is the free and equal clash of opinions.", ["c1-concessive-adversative-connectors"]),
                dc("dialogue", [
                    {"speaker": "Politológus", "text": "Hogyan mérhető a társadalmi vita minősége egy modern államban?"},
                    {"speaker": "Szociológus", "text": "Nem a hangos jelszavak száma, hanem a résztvevők közötti érvelési _____ és kölcsönös tisztelet alapján."},
                ], ["fegyelem", "zavar", "kiabálás"], 0, ["c1-concessive-adversative-connectors"]),
                sw("production", [{"prompt": "Write a concessive sentence on deliberative democracy.", "answer": "Ámbár a társadalmi egyeztetések lefolytatása jelentős időbeli és anyagi ráfordítást követel meg, mindazonáltal a döntések tartós legitimitása kárpótolja a döntéshozókat."}], ["c1-concessive-adversative-connectors"]),
                mc("grammar", "check", "Melyik mondat alkalmaz helyesen megengedő kötőszót emelkedett politikai szövegben?", [
                    "A tárgyalások megfeneklettek, mindazonáltal a felek nyitottak maradtak a közvetítésre.",
                    "A tárgyalások megfeneklettek, miközben a felek nyitottak maradtak a közvetítésre.",
                    "A tárgyalások megfeneklettek, miután a felek nyitottak maradtak a közvetítésre."
                ], 0, ["c1-concessive-adversative-connectors"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-16-02",
            "title": "Rhetorical Framing & Political Communication",
            "grammar_title": "Rhetorical and Deliberative Interrogative Structures in Political Prose",
            "grammar_skill": "c1-rhetorical-hypothetical-questions",
            "goals": [
                "I can analyze political framing, narrative dominance, and spin (*retorikai keretezés, narratívaépítés, politikai tematizáció*).",
                "I can deploy rhetorical questions and deliberative interrogatives (*vajon mi másra utalhatna, nemde éppen arról tanúskodik-e, felmerül a kérdés, hogy vajon*).",
                "I can deconstruct emotional manipulation and demagogy in Hungarian campaign discourse."
            ],
            "vocab": [
                {"lemma": "retorikai keretezés", "translation": "rhetorical framing", "pos": "expression"},
                {"lemma": "narratívaépítés", "translation": "narrative construction", "pos": "noun"},
                {"lemma": "tematizáció", "translation": "agenda-setting, thematization", "pos": "noun"},
                {"lemma": "politikai diskurzus", "translation": "political discourse", "pos": "expression"},
                {"lemma": "demagógia", "translation": "demagoguery", "pos": "noun"},
                {"lemma": "ellenségkép-gyártás", "translation": "construction of enemy images / scapegoating", "pos": "noun"},
                {"lemma": "meggyőzés művészete", "translation": "art of persuasion", "pos": "expression"},
                {"lemma": "tömegpszichológia", "translation": "mass psychology", "pos": "noun"}
            ],
            "gr_text1": "Rhetorical and deliberative interrogatives (*vajon mi másra utalna... mintsem...*, *nemde éppen ez bizonyítja-e...*, *hát kérdéses lehet-e még...*) guide the listener toward an inevitable analytical deduction without overt dogmatism.",
            "gr_text2": "Example in critical essay style: `Vajon mi másra utalhatna a független intézmények szisztematikus leépítése, mintsem a hatalomfékek kiiktatásának leplezetlen szándékára? Nemde éppen a kritikai hangok elhallgattatása jelzi a demokrácia erózióját?`",
            "gr_table": [
                ["Vajon elképzelhető-e valódi pluralizmus az információk sokszínűsége nélkül?", "Is genuine pluralism conceivable without the diversity of information?"],
                ["Nemde éppen a hatalom korlátozhatósága különbözteti meg a jogállamot az önkénytől?", "Is it not precisely the limitability of power that distinguishes the rule of law from tyranny?"],
                ["Felmerül a kérdés: vajon meddig tartható fenn egy mesterségesen szított ellenségkép?", "The question arises: how long can an artificially stoked enemy image be maintained?"]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'retorikai keretezés' (framing) a politikai kommunikációban?", [
                    "A valóság olyan szempontú bemutatását és megfogalmazását, amely előre meghatározza a választó értelmezési keretét és érzelmi reakcióját.",
                    "A választási plakátok bekeretezését fa- vagy fémlécekkel.",
                    "A rádióstúdiók hangszigetelését."
                ], 0, ["c1-16-vocab"]),
                fb("grammar", "controlled", "_____ (Is it not precisely / Nemde éppen) az intézményi függetlenség hiánya bizonyítja a hatalomgyakorlás torzulását?", "Nemde éppen", "Is it not precisely the lack of institutional independence that proves the distortion of exercising power?", ["c1-rhetorical-hypothetical-questions"]),
                match("vocabulary", "controlled", [["narratívaépítés", "politikai történet megalkotása"], ["ellenségkép-gyártás", "társadalmi bűnbakképzés"], ["tematizáció", "napirend uralása a médiában"], ["demagógia", "érzelmi manipuláció a tények helyett"]], ["c1-16-vocab"]),
                fb("grammar", "practice", "Vajon mi másra _____ a kritikai sajtó ellehetetlenítése, mintsem a nyilvánosság szűkítésére? (could point / utalhatna)", "utalhatna", "To what else could the disabling of critical press point, if not to the narrowing of the public sphere?", ["c1-rhetorical-hypothetical-questions"]),
                sb("grammar", "practice", ["A", "politikai", "tematizáció", "célja", "a", "közbeszéd", "figyelmének", "folyamatos", "irányítása."], ["A", "politikai", "tematizáció", "célja", "a", "közbeszéd", "figyelmének", "folyamatos", "irányítása."], "The goal of political thematization is the continuous steering of public discourse attention.", ["c1-rhetorical-hypothetical-questions"]),
                dc("dialogue", [
                    {"speaker": "Médiaelemző", "text": "Hogyan ér el sikert egy populista kampány?"},
                    {"speaker": "Szociálpszichológus", "text": "Egyszerűsítő üzenetekkel, félelemkeltéssel és a társadalmi _____ tudatos szításával."},
                ], ["törésvonalak", "építkezések", "kirándulások"], 0, ["c1-rhetorical-hypothetical-questions"]),
                sw("production", [{"prompt": "Write a persuasive rhetorical question challenging censorship.", "answer": "Vajon tekinthető-e szabadnak egy olyan társadalom, amelyben az állampolgárok félnek kinyilvánítani véleményüket, és ahol a kritikai reflexiót azonnal nemzetárulásként bélyegzik meg?"}], ["c1-rhetorical-hypothetical-questions"]),
                mc("grammar", "check", "Melyik mondat alkalmaz költői/deliberatív kérdést egy politikai tézis alátámasztására?", [
                    "Vajon megmaradhat-e az igazságosság eszméje ott, ahol a törvények csak a kevesek kiváltságait szolgálják?",
                    "Hány órakor kezdődik ma este a politikai vita a televízióban?",
                    "Megérkezett-e már a hivatalos levél a minisztériumból?"
                ], 0, ["c1-rhetorical-hypothetical-questions"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-16-03",
            "title": "Institutional Oversight & Passive Periphrases",
            "grammar_title": "Impersonal Passive Equivalent Verbal Periphrases with Modal Necessity",
            "grammar_skill": "c1-adv-passive-substitute-phrases",
            "goals": [
                "I can analyze public accountability, institutional checks, and ombudsman reports (*intézményi felügyelet, ombudsman, számvevőszék*).",
                "I can construct impersonal passive-equivalent phrases expressing necessity (*figyelembe veendő, orvoslásra szorul, megválaszolandó kérdés*).",
                "I can evaluate official reports on freedom of information and public spending in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "intézményi felügyelet", "translation": "institutional oversight", "pos": "expression"},
                {"lemma": "számvevőszék", "translation": "state audit office", "pos": "noun"},
                {"lemma": "alapvető jogok biztosa", "translation": "commissioner for fundamental rights (ombudsman)", "pos": "expression"},
                {"lemma": "közérdekű adat", "translation": "data of public interest / FOIA data", "pos": "expression"},
                {"lemma": "visszaélés", "translation": "abuse of power, malpractice", "pos": "noun"},
                {"lemma": "orvoslás", "translation": "remedy, redress", "pos": "noun"},
                {"lemma": "átláthatósági hiányosság", "translation": "transparency deficiency", "pos": "expression"},
                {"lemma": "közpénzfelhasználás", "translation": "use of public funds", "pos": "noun"}
            ],
            "gr_text1": "Hungarian formal prose creates passive-equivalent necessity periphrases via the future/modal participle in *-andó/-endő* (e.g. `számításba veendő` [must be taken into account], `megválaszolandó` [to be answered], `elkerülendő` [to be avoided]) and noun + `szorul` (e.g. `orvoslásra szorul` [requires remedy], `felülvizsgálatra szorul` [needs review]).",
            "gr_text2": "Example in audit report style: `A közpénzek elköltésének átláthatatlansága haladéktalan orvoslásra szorul; az audit során feltárt rendellenességek mindazonáltal nem tekinthetők egyedi eseteknek`.",
            "gr_table": [
                ["A jelentésben megfogalmazott kritikák alapos megfontolásra szorulnak.", "The criticisms formulated in the report require thorough consideration."],
                ["Mindenekelőtt az a kérdés tisztázandó, hogy történt-e jogtalan adateltitkolás.", "First of all, the question to be clarified is whether unlawful withholding of data occurred."],
                ["A feltárt szabálytalanságok súlyos természetűek, ennélfogva szigorúan szankcionálandók.", "The uncovered irregularities are of a severe nature, therefore to be strictly sanctioned."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'közérdekű adat' fogalma a magyar jogrendben?", [
                    "Az állami vagy helyi önkormányzati feladatot ellátó szervek kezelésében lévő, a tevékenységükre vagy közpénzekre vonatkozó nyilvános adatot.",
                    "A magánszemélyek banki jelszavait.",
                    "A televíziós műsorvezetők magánéleti titkait."
                ], 0, ["c1-16-vocab"]),
                fb("grammar", "controlled", "A közbeszerzési eljárások átláthatósági hiányosságai sürgős _____ szorulnak. (remedy / orvoslásra)", "orvoslásra", "The transparency deficiencies of public procurement procedures require urgent remedy.", ["c1-adv-passive-substitute-phrases"]),
                match("vocabulary", "controlled", [["számvevőszék", "közpénzek ellenőrző szerve"], ["ombudsman", "alapjogok védője"], ["közérdekű adat", "nyilvános állami információ"], ["közpénzfelhasználás", "adóbevételek elköltése"]], ["c1-16-vocab"]),
                fb("grammar", "practice", "A jogállami normák érvényesülése szempontjából kulcsfontosságú a kérdés: milyen garanciák _____ a jövőben? (to be built in / beépítendők)", "beépítendők", "From the standpoint of rule-of-law norms, the question is key: what guarantees are to be built in for the future?", ["c1-adv-passive-substitute-phrases"]),
                sb("grammar", "practice", ["A", "közérdekű", "adatok", "megismerésének", "joga", "minden", "állampolgárt", "megillet."], ["A", "közérdekű", "adatok", "megismerésének", "joga", "minden", "állampolgárt", "megillet."], "The right of access to data of public interest belongs to every citizen.", ["c1-adv-passive-substitute-phrases"]),
                dc("dialogue", [
                    {"speaker": "Oknyomozó", "text": "Miért nem adják ki a kért szerződéseket?"},
                    {"speaker": "Hivatalnok", "text": "A dokumentumok állításuk szerint még belső döntéselőkészítési szakaszban vannak, így nem _____."},
                ], ["kiadhatók", "elfeledhetők", "lemásolhatók"], 0, ["c1-adv-passive-substitute-phrases"]),
                sw("production", [{"prompt": "Write a formal sentence using a passive periphrasis (-andó/-endő or szorul) on public spending.", "answer": "A gyanús közbeszerzési túlárazások haladéktalan kivizsgálásra szorulnak, és a felelősök megnevezése elkerülhetetlen feladatként hárul az ellenőrző hatóságokra."}], ["c1-adv-passive-substitute-phrases"]),
                mc("grammar", "check", "Melyik kifejezés fejez ki passzív jellegű, modális kényszert hordozó körülírást?", [
                    "tisztázásra szorul / megválaszolandó",
                    "tisztázták a dolgot",
                    "amikor tisztázzák"
                ], 0, ["c1-adv-passive-substitute-phrases"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-16-04",
            "title": "Epistemic Distancing in Journalistic Discourse",
            "grammar_title": "Epistemic Distancing Markers and Evidential Qualification in Journalism",
            "grammar_skill": "c1-modal-epistemic-distancing",
            "goals": [
                "I can analyze investigative reporting, source verification, and journalistic neutrality (*forráskritika, oknyomozás, tényszerűség*).",
                "I can deploy epistemic distancing markers (*állítólag, minden bizonnyal, tudomásunk szerint, mintegy, mondhatni*).",
                "I can evaluate leak analysis and unattributed institutional statements in professional Hungarian journalism."
            ],
            "vocab": [
                {"lemma": "forráskritika", "translation": "source criticism / verification", "pos": "noun"},
                {"lemma": "oknyomozó újságírás", "translation": "investigative journalism", "pos": "expression"},
                {"lemma": "tényszerűség", "translation": "factuality, objectivity", "pos": "noun"},
                {"lemma": "kiszivárogtatás", "translation": "leak (information leak)", "pos": "noun"},
                {"lemma": "megbízhatatlan forrás", "translation": "unreliable source", "pos": "expression"},
                {"lemma": "cáfolat", "translation": "refutation, rebuttal", "pos": "noun"},
                {"lemma": "sajtóetika", "translation": "press ethics", "pos": "noun"},
                {"lemma": "közérdekű bejelentő", "translation": "whistleblower", "pos": "expression"}
            ],
            "gr_text1": "Quality journalism preserves neutrality and legal safety through epistemic distancing markers: `állítólag` (allegedly), `tudomásunk szerint` (to our knowledge), `információink szerint` (according to our information), `a hírek tanúsága szerint` (as reported), and conditional verbs (*történhetett, kerülhetett sor*).",
            "gr_text2": "Example in investigative reporting: `A birtokunkba jutott dokumentumok szerint a pénzek átutalására állítólag egy offshore cégen keresztül kerülhetett sor; az érintett minisztérium mindazonáltal határozottan cáfolta a vádakat`.",
            "gr_table": [
                ["Információink szerint a döntést már a hivatalos bejelentés előtt meghozták.", "According to our information, the decision had already been made prior to official announcement."],
                ["Az állítólagos visszaélésekről szóló iratokat egy belső forrás szivárogtatta ki.", "Documents concerning the alleged malpractices were leaked by an inside source."],
                ["Minden jel szerint rendszerszintű mulasztás történt a közpénzek elosztásakor.", "By all indications, systemic negligence occurred during allocation of public funds."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért van kiemelt szerepe a forráskritikának az oknyomozó újságírásban?", [
                    "Mert garantálja, hogy a közzétett állítások hiteles, többszörösen ellenőrzött tényeken alapuljanak, kizárva a manipulációt.",
                    "Hogy a riporterek minél kevesebbet dolgozzanak a cikkeken.",
                    "Hogy kizárólag névtelen kommentekre lehessen hivatkozni."
                ], 0, ["c1-16-vocab"]),
                fb("grammar", "controlled", "A tárcavezető _____ (allegedly / állítólag) tudott a szabálytalan kifizetésekről, ám ezt a sajtótájékoztatón cáfolta.", "állítólag", "The minister allegedly knew about the irregular payments, but refuted this at the press briefing.", ["c1-modal-epistemic-distancing"]),
                match("vocabulary", "controlled", [["forráskritika", "információk ellenőrzése"], ["kiszivárogtatás", "bizalmas adatok átadása"], ["közérdekű bejelentő", "visszaélést feltáró személy"], ["cáfolat", "állítás hivatalos visszautasítása"]], ["c1-16-vocab"]),
                fb("grammar", "practice", "Minden jel _____ a szerződést versenyeztetés nélkül ítélték oda az egyetlen pályázónak. (according to / szerint)", "szerint", "By all indications, the contract was awarded without competition to the single bidder.", ["c1-modal-epistemic-distancing"]),
                sb("grammar", "practice", ["A", "független", "sajtó", "elsődleges", "kötelessége", "a", "hatalom", "elszámoltathatóságának", "biztosítása."], ["A", "független", "sajtó", "elsődleges", "kötelessége", "a", "hatalom", "elszámoltathatóságának", "biztosítása."], "The primary duty of the independent press is ensuring the accountability of power.", ["c1-modal-epistemic-distancing"]),
                dc("dialogue", [
                    {"speaker": "Főszerkesztő", "text": "Lehozhatjuk a holnapi címlapon a botrányt?"},
                    {"speaker": "Rovetvezető", "text": "Csak akkor, ha legalább két független forrásból származó bizonyítékkal tudjuk _____ a tényeket."},
                ], ["igazolni", "tagadni", "törölni"], 0, ["c1-modal-epistemic-distancing"]),
                sw("production", [{"prompt": "Write an investigative lead paragraph using epistemic distancing markers.", "answer": "Információink szerint a gyanús offshore tranzakciókra állítólag egy olyan tanácsadó cég közbeiktatásával került sor, amely minden jel szerint szoros szálakkal kötődik a döntéshozókhoz."}], ["c1-modal-epistemic-distancing"]),
                mc("grammar", "check", "Melyik kifejezés szolgál episztemikus távolságtartásra újságírói szövegben?", [
                    "tudomásunk szerint / állítólag",
                    "egyértelműen és vitathatatlanul",
                    "minden kétséget kizáróan"
                ], 0, ["c1-modal-epistemic-distancing"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-16-05",
            "title": "István Bibó & The Anatomy of Political Hysteria",
            "grammar_title": "Circumstantial Participial Adjunct Clauses in Deliberative Discourse",
            "grammar_skill": "c1-adv-circumstantial-participial-clauses",
            "goals": [
                "I can analyze István Bibó's political diagnosis in 'The Misery of Small Eastern European States' (1946).",
                "I can employ circumstantial participial adjunct clauses (*a kialakult helyzetet mérlegelve, a félelem mechanizmusát látván*).",
                "I can synthesize Bibó's concepts of democratic maturity, political neurosis, and moral courage in Hungarian."
            ],
            "vocab": [
                {"lemma": "politikai hisztéria", "translation": "political hysteria", "pos": "expression"},
                {"lemma": "félelem légköre", "translation": "climate of fear", "pos": "expression"},
                {"lemma": "közösségi neurózis", "translation": "collective neurosis", "pos": "expression"},
                {"lemma": "hamis realizmus", "translation": "false realism (opportunism masquerading as pragmatism)", "pos": "expression"},
                {"lemma": "demokratikus érettség", "translation": "democratic maturity", "pos": "expression"},
                {"lemma": "erkölcsi bátorság", "translation": "moral courage", "pos": "expression"},
                {"lemma": "történelmi zsákutca", "translation": "historical dead end", "pos": "expression"},
                {"lemma": "önbecsülés", "translation": "national self-esteem / dignity", "pos": "noun"}
            ],
            "gr_text1": "Circumstantial participial adjunct clauses (*-va/-ve, -ván/-vén*) capture psychological and political conditions preceding state action: `A kelet-európai nemzetek történelmi traumáit elemezve, Bibó István rámutatott: a szabadság legfőbb ellensége nem a külső elnyomás, hanem a belső félelem`.",
            "gr_text2": "These adjunct clauses condense complex historical diagnoses into rigorous academic periods: `Felismerve a politikai hisztéria öngerjesztő spirálját, a társadalomnak vissza kell nyernie a józan mértéktartást`.",
            "gr_table": [
                ["A nemzeti félelmeket mérlegelve megérthetjük a kelet-európai kisállamok politikai görcseit.", "Weighing national fears, we can understand the political cramps of Eastern European small states."],
                ["Látván a hamis realizmus pusztítását, Bibó a demokrácia morális fundamentumai mellett állt ki.", "Seeing the devastation of false realism, Bibó stood up for the moral fundamentals of democracy."],
                ["A múlt torzulásait meghaladva a polgárok képessé válnak a békés deliberációra.", "Surpassing distortions of the past, citizens become capable of peaceful deliberation."]
            ],
            "classic_story": {
                "slug": "c1-16-bibo",
                "author": "Bibó István",
                "work": "A kelet-európai kisállamok nyomorúsága (1946)",
                "title": "A politikai hisztéria anatómiája és a szabad nyilvánosság",
                "summary": "István Bibó's towering 1946 treatise analyzing how existential fear, territorial trauma, and fake realism cripple democratic culture in Central and Eastern Europe, advocating for courage and truth in the public sphere.",
                "characters": ["Bibó István"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Bibó István 1946-ban közzétette 'A kelet-európai kisállamok nyomorúsága' című tanulmányát, a huszadik század legmélyebb és legmegrázóbb társadalomtudományi látleletét adta a Kárpát-medence és a környező térség tragédiájáról. Bibó nem gazdasági vagy fegyveres mutatókból indult ki: a politikai közösségek pszichéjét, a kollektív félelmeket és a szabadság morális feltételeit állította gondolkodása középpontjába."},
                    {"type": "narration", "text": "Diagnózisa szerint a kelet-európai nemzetek történetét a létbizonytalanság és az egzisztenciális rettegés torzította el. 'A félelem légkörében nem lehet szabadnak lenni' – fogalmazott Bibó, rámutatva arra a veszedelmes reflexre, amelyet ő 'politikai hisztériának' nevezett. Amikor egy nép félni kezd állami vagy nemzeti létének megsemmisülésétől, hajlamos felfüggeszteni az erkölcsi mércéket, és a gátlástalan demagógia, a hamis realizmus és a vezérkultusz felé fordul."},
                    {"type": "narration", "text": "Ebben a kóros állapotban a nyilvánosság nem a racionális vita fóruma, hanem az ellenségkép-gyártás harctere lesz. A hatalom a nemzetféltésre hivatkozva csorbítja a jogállamot, a polgárok pedig önként mondanak le szabadságjogaikról abban a téves hitben, hogy a belső egység megköveteli a kritika elfojtását. Bibó zseniálisan leplezte le ezt a zsákutcát: a belső szabadság feladása sohasem hoz külső biztonságot, csupán morális lezüllést és újabb nemzeti katasztrófákat."},
                    {"type": "narration", "text": "Bibó öröksége a mai közép-európai nyilvánosság számára a legfontosabb szellemi iránytű. Arra tanít, hogy a demokrácia nem intézményi homlokzat, hanem belső morális tartás: 'Demokratának lenni mindenekelőtt annyit tesz, mint nem félni.' Csak egy olyan nyilvánosság képes megvédeni a jövőt, amelyben a polgárok mernek autonómok lenni, és nem hagyják, hogy a félelem és a hisztéria diktálja a társadalom törvényeit."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi Bibó István híres meghatározása a demokráciáról?", [
                    "'Demokratának lenni mindenekelőtt annyit tesz, mint nem félni.'",
                    "'A demokrácia a legerősebb hadsereget jelenti.'",
                    "'Demokrácia az, amikor senki sem fizet adót.'"
                ], 0, ["c1-16-vocab"]),
                fb("grammar", "controlled", "A történelmi tényeket behatóan _____, (analyzing / elemezve) világossá válik a félelem légkörének romboló hatása.", "elemezve", "Analyzing historical facts thoroughly, the destructive effect of the climate of fear becomes clear.", ["c1-adv-circumstantial-participial-clauses"]),
                match("vocabulary", "controlled", [["politikai hisztéria", "kollektív társadalmi rettegés állapota"], ["hamis realizmus", "erkölcstelen megalkuvás"], ["közösségi neurózis", "társadalmi szintű szorongás"], ["demokratikus érettség", "félelemmentes autonóm állampolgárság"]], ["c1-16-vocab"]),
                mc("reading", "practice", "Hogyan torzítja el a politikai hisztéria a nyilvánosságot Bibó szerint?", [
                    "A racionális vita és a kritika helyét az ellenségkép-gyártás és a nemzetféltésre hivatkozó hatalmi önkény veszi át.",
                    "A viták kizárólag a mezőgazdasági terményárakra korlátozódnak.",
                    "Minden polgár azonnal felhagy az olvasással."
                ], 0, None),
                sb("grammar", "practice", ["A", "félelem", "légkörében", "lehetetlenné", "válik", "a", "józan", "és", "szabad", "deliberáció."], ["A", "félelem", "légkörében", "lehetetlenné", "válik", "a", "józan", "és", "szabad", "deliberáció."], "In a climate of fear, sober and free deliberation becomes impossible.", ["c1-adv-circumstantial-participial-clauses"]),
                sw("production", [{"prompt": "Synthesize István Bibó's critique of fear in politics using a participial adjunct.", "answer": "Felismerve a politikai hisztéria öngerjesztő természetét, Bibó István rámutatott, hogy a demokratikus megújulás záloga a mesterségesen táplált kollektív félelmek meghaladása és a szabad nyilvánosság helyreállítása."}], ["c1-adv-circumstantial-participial-clauses"]),
                mc("grammar", "check", "Melyik mondat tartalmaz állapot- vagy körülményhatározói participiális mellékmondatot?", [
                    "A közvélemény reakcióit látván a kormányzat visszavonta a vitatott törvényt.",
                    "A közvélemény azért reagált, mert a kormányzat visszavonta a törvényt.",
                    "A közvélemény és a kormányzat megegyeztek a törvény visszavonásáról."
                ], 0, ["c1-adv-circumstantial-participial-clauses"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(16, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        16,
        "core",
        "c1-16-consolidation",
        core_title,
        [
            "I can analyze the public sphere, deliberative ethics, and institutional accountability.",
            "I can utilize concessive connectors, rhetorical interrogatives, and modal passive periphrases.",
            "I can evaluate István Bibó's political philosophy on fear, hysteria, and democratic maturity."
        ],
        [
            mc("grammar", "recognize", "Milyen kötőszóval fejezhetünk ki kifinomult ellentétes megengedést?", [
                "mindazonáltal / annak dacára, hogy",
                "azért, hogy / abból a célból",
                "amikor / mihelyt"
            ], 0, ["c1-concessive-adversative-connectors"]),
            mc("grammar", "recognize", "Mit fejez ki a '-andó/-endő' participium az adminisztratív vagy jogi stílusban?", [
                "Szükségszerűséget, elvégzendő kötelességet vagy szigorú elvárást.",
                "Befejezett múltbeli történést.",
                "Feltételes kívánságot."
            ], 0, ["c1-adv-passive-substitute-phrases"]),
            match("vocabulary", "recognize", [["deliberatív demokrácia", "racionális párbeszédre épülő rend"], ["retorikai keretezés", "értelmezési keret tudatos kialakítása"], ["közérdekű adat", "nyilvános állami információ"], ["állítólag", "feltételezett, nem megerősített"], ["politikai hisztéria", "félelmen alapuló társadalmi reakció"]], ["c1-16-vocab"]),
            fb("vocabulary", "recall", "A vitában a demagóg fél klasszikus érvelési _____ esett, amikor személyében támadta ellenfelét. (fallacy / hibába)", "hibába", "In the debate the demagogic party committed a classic argumentative fallacy when attacking his opponent personally.", ["c1-16-vocab"]),
            fb("vocabulary", "recall", "Bibó szerint a kelet-európai politika legnagyobb rákfenéje a félelem és a hamis _____ eluralkodása. (realism / realizmus)", "realizmus", "According to Bibó, the greatest cancer of Eastern European politics is the prevalence of fear and false realism.", ["c1-16-vocab"]),
            fb("grammar", "recall", "A vádak súlyosak, _____ dacára, hogy a vádlott mindent tagadott a bíróság előtt. (in spite of / annak)", "annak", "The charges are severe, in spite of the fact that the defendant denied everything before the court.", ["c1-concessive-adversative-connectors"]),
            fb("grammar", "context", "A feltárt visszaélések haladéktalan kivizsgálásra _____ az igazságszolgáltatásban. (require / szorulnak)", "szorulnak", "The uncovered malpractices require immediate investigation in the justice system.", ["c1-adv-passive-substitute-phrases"]),
            fb("grammar", "context", "Minden jel _____ a kiszivárogtatott dokumentumok hitelesek. (according to / szerint)", "szerint", "By all indications, the leaked documents are authentic.", ["c1-modal-epistemic-distancing"]),
            mc("grammar", "context", "Mit fejez ki a 'Vajon mi másra utalhatna...' szerkezet egy politikai vitában?", [
                "Egy költői, deliberatív kérdést, amely logikailag egyetlen elkerülhetetlen következtetésre vezeti rá a hallgatót.",
                "Kételyt afelől, hogy létezik-e a valóság.",
                "Kérdést a helyes időjárás-előrejelzésről."
            ], 0, ["c1-rhetorical-hypothetical-questions"]),
            sb("grammar", "produce", ["A", "szabad", "nyilvánosság", "a", "jogállami", "demokrácia", "legfőbb", "védőbástyája."], ["A", "szabad", "nyilvánosság", "a", "jogállami", "demokrácia", "legfőbb", "védőbástyája."], "The free public sphere is the foremost bastion of constitutional democracy.", ["c1-concessive-adversative-connectors"]),
            sw("production", [{"prompt": "Write a synthesized reflection on István Bibó's political diagnostic.", "answer": "Bibó István diagnózisa mindmáig időszerű figyelmeztetés: a politikai hisztéria és a félelem kultúrája elsorvasztja a szabad nyilvánosságot, amelynek helyreállítása megköveteli az állampolgári autonómiát és az erkölcsi bátorságot."}], ["c1-adv-circumstantial-participial-clauses"]),
            sw("production", [{"prompt": "Formulate a statement on freedom of information and public accountability.", "answer": "A közpénzek elköltésének átláthatósága és a közérdekű adatok szabad megismerhetősége olyan alapjog, amely nem szorulhat háttérbe semmilyen politikai hatalmi érdekkel szemben."}], ["c1-adv-passive-substitute-phrases"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-mediakritika)
    # ----------------------------------------------------
    disc_title = "Media Pluralism, Algorithmic Filters & Information Integrity"
    slug = "mediakritika"

    disc_intro = [
        "In Central Europe and Hungary, media pluralism faces unprecedented challenges: institutional consolidation (KESMA), algorithmic filter bubbles, hybrid disinformation, and state advertising dominance.",
        "Through serialized case studies examining media ownership concentration, social media echo chambers, deepfake manipulation, Pegasus investigative revelations, and civic crowdfunding models, you will master critical media analysis in C1 Hungarian."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Media Landscape & Institutional Concentration",
            "grammar_title": "Polarizing and Contrastive Discourse Coordinators in Media Critique",
            "grammar_skill": "c1-discourse-polarizing-contrastives",
            "goals": [
                "I can analyze media concentration, state advertising distortion, and conglomerates (*médiapiaci koncentráció, KESMA, állami hirdetések*).",
                "I can utilize polarizing and contrastive coordinators (*nemhogy nem..., sőt éppenséggel; korántsem..., sokkal inkább; nem csupán... hanem*).",
                "I can debate public broadcasting neutrality versus governmental propaganda in contemporary Hungary."
            ],
            "vocab": [
                {"lemma": "médiapiaci koncentráció", "translation": "media market concentration", "pos": "expression"},
                {"lemma": "közszolgálati média", "translation": "public service broadcasting", "pos": "expression"},
                {"lemma": "médiabirodalom", "translation": "media empire / conglomerate (KESMA)", "pos": "noun"},
                {"lemma": "állami reklámköltés", "translation": "state advertising expenditure", "pos": "expression"},
                {"lemma": "piaci torzulás", "translation": "market distortion", "pos": "expression"},
                {"lemma": "független sajtó", "translation": "independent press", "pos": "expression"},
                {"lemma": "hírhamisítás", "translation": "news falsification / propaganda", "pos": "noun"},
                {"lemma": "médiatanács", "translation": "media authority / regulatory council", "pos": "noun"}
            ],
            "gr_text1": "Polarizing and contrastive coordinators (*nemhogy nem..., sőt éppenséggel...* [not only does not..., on the contrary indeed...], *korántsem..., sokkal inkább...* [far from being..., much rather...]) sharpen analytical critique of institutional capture.",
            "gr_text2": "Example in media policy critique: `A közmédia korántsem a kiegyensúlyozott tájékoztatás fóruma, hanem sokkal inkább a kormányzati kommunikációs üzenetek egyoldalú felerősítője`.",
            "gr_table": [
                ["A konglomerátum létrehozása nemhogy nem növelte a versenyt, sőt éppenséggel felszámolta a regionális sajtó sokszínűségét.", "The creation of the conglomerate not only did not increase competition; on the contrary, it outright abolished the diversity of the regional press."],
                ["Ez a lépés korántsem piaci logika, sokkal inkább politikai befolyásszerzés eredménye.", "This move is far from market logic; much rather the outcome of political influence-seeking."],
                ["Nem csupán gazdasági kérdésről van szó, hanem a demokratikus nyilvánosság alapvető feltételéről.", "It is not merely an economic issue, but a fundamental condition of the democratic public sphere."]
            ],
            "world_story_seg": {
                "seg_slug": "pluralizmus",
                "title": "A centralizált hírvilág: A KESMA és a magyar médiarendszer átalakulása",
                "summary": "How the creation of the Central European Press and Media Foundation (KESMA) concentrated hundreds of media outlets under a unified editorial line.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 2018 késő őszén csaknem ötszáz kormánypárti sajtótermék – az összes megyei napilap, országos rádiók, televíziók és online portálok – egyetlen nap leforgása alatt beolvadt a Közép-európai Sajtó és Média Alapítványba (KESMA), a rendszerváltás utáni magyar médiarendszer addigi legnagyobb koncentrációja jött létre."},
                    {"type": "narration", "text": "A kormányzat a lépést nemzetstratégiai jelentőségűnek minősítette, kivonva azt a Gazdasági Versenyhivatal és a Médiatanács vizsgálata alól. Ezzel szemben a független szakmai szervezetek és az Európai Parlament jelentései arra mutattak rá, hogy az állami reklámköltések egyoldalú átirányítása és az egységes központi narratívák terjesztése drasztikusan eltorzította a médiapiacot, marginalizálva a vidéki független tájékozódás lehetőségét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi jellemezte a KESMA (Közép-európai Sajtó és Média Alapítvány) 2018-as megalakulását?", [
                    "Közel ötszáz kormánypárti médium (többek között az összes megyei napilap) egyetlen alapítvány alá történő centralizálása.",
                    "A magántelevíziók teljes betiltása.",
                    "Minden újságíró fizetésének megkétszerezése az állami költségvetésből."
                ], 0, ["c1-mediakritika-vocab"]),
                fb("grammar", "controlled", "A fúzió nemhogy nem javította a tájékoztatás minőségét, _____ (on the contrary indeed / sőt éppenséggel) felszámolta a helyi szerkesztőségek autonómiáját.", "sőt éppenséggel", "The merger not only did not improve information quality, on the contrary indeed it eliminated the autonomy of local newsrooms.", ["c1-discourse-polarizing-contrastives"]),
                match("vocabulary", "controlled", [["KESMA", "központosított médiakonglomerátum"], ["állami reklámköltés", "politikai alapon torzított piac"], ["közszolgálati média", "elméletileg semleges állami adó"], ["médiapiaci koncentráció", "tulajdonviszonyok monopolizálódása"]], ["c1-mediakritika-vocab"]),
                fb("grammar", "practice", "A közmédia műsorai _____ sem a pártatlanság elvét követik, sokkal inkább a napi politikai napirendet szolgálják ki. (far / korántsem)", "korántsem", "Public service programming far from follows the principle of impartiality; much rather it caters to the daily political agenda.", ["c1-discourse-polarizing-contrastives"]),
                sb("grammar", "practice", ["A", "médiapiac", "sokszínűsége", "nélkülözhetetlen", "a", "tájékozott", "választói", "döntésekhez."], ["A", "médiapiac", "sokszínűsége", "nélkülözhetetlen", "a", "tájékozott", "választói", "döntésekhez."], "The diversity of the media market is indispensable for informed voter decisions.", ["c1-discourse-polarizing-contrastives"]),
                dc("dialogue", [
                    {"speaker": "Médiakutató", "text": "Hogyan torzítja az állam a piaci viszonyokat a magyar médiában?"},
                    {"speaker": "Közgazdász", "text": "Nem a piaci verseny elvei, hanem a politikai lojalitás alapján kiosztott állami _____ révén."},
                ], ["hirdetések", "díjak", "könyvek"], 0, ["c1-discourse-polarizing-contrastives"]),
                sw("production", [{"prompt": "Write a contrastive sentence analyzing media conglomerate dominance.", "answer": "A gigantikus médiakonglomerátum létrejötte korántsem a magyar kultúra védelmét szolgálja, hanem sokkal inkább a politikai üzenetek monolitikus és ellentmondást nem tűrő sulykolását teszi lehetővé."}], ["c1-discourse-polarizing-contrastives"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki fokozó-polarizáló ellentétet?", [
                    "nemhogy nem..., sőt éppenséggel",
                    "holott egyébként",
                    "miközben egyúttal"
                ], 0, ["c1-discourse-polarizing-contrastives"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Echo Chambers, Algorithmic Bubbles & Polarization",
            "grammar_title": "Evaluative Stance Adverbials Expressing Moral or Intellectual Judgement",
            "grammar_skill": "c1-evaluative-adverbial-stance",
            "goals": [
                "I can analyze algorithmic echo chambers and confirmation bias (*véleménybuborék, algoritmusos szűrés, megerősítési torzítás*).",
                "I can employ evaluative stance adverbials (*aggasztó módon, vitathatatlanul, döbbenetes módon, érthető módon*).",
                "I can evaluate how social media algorithms monetize outrage and deepen societal fissures."
            ],
            "vocab": [
                {"lemma": "véleménybuborék", "translation": "echo chamber / filter bubble", "pos": "noun"},
                {"lemma": "megerősítési torzítás", "translation": "confirmation bias", "pos": "expression"},
                {"lemma": "kattintásvadászat", "translation": "clickbait", "pos": "noun"},
                {"lemma": "felháborodás-gazdaságtan", "translation": "outrage economy / attention economy", "pos": "expression"},
                {"lemma": "társadalmi polarizáció", "translation": "social polarization", "pos": "expression"},
                {"lemma": "ajánlóalgoritmus", "translation": "recommendation algorithm", "pos": "noun"},
                {"lemma": "törzsi gondolkodás", "translation": "tribal thinking / political sectarianism", "pos": "expression"},
                {"lemma": "mikrocélzás", "translation": "microtargeting", "pos": "noun"}
            ],
            "gr_text1": "Evaluative stance adverbials (*aggasztó módon* [in an alarming manner], *vitathatatlanul* [unquestionably], *döbbenetes módon* [astonishingly], *helyteleníthetően* [deplorably]) frame the analyst's normative and intellectual evaluation of systemic phenomena.",
            "gr_text2": "Example in platform critique: `Aggasztó módon a közösségi média ajánlóalgoritmusai a felháborodást generáló tartalmakat részesítik előnyben, ami vitathatatlanul a társadalmi kohézió megbomlásához vezet`.",
            "gr_table": [
                ["Aggasztó módon a felhasználók többsége kizárólag a saját nézeteit megerősítő hírekkel találkozik.", "In an alarming manner, the majority of users exclusively encounter news confirming their own views."],
                ["Vitathatatlanul a polarizáció növekedése a közösségi média gazdasági modelljének egyenes következménye.", "Unquestionably, the increase in polarization is the direct consequence of social media's economic model."],
                ["Döbbenetes módon a téves információk hatszor gyorsabban terjednek, mint a valós tények.", "Astonishingly, false information spreads six times faster than verified facts."]
            ],
            "world_story_seg": {
                "seg_slug": "buborekok",
                "title": "A láthatatlan falak: Véleménybuborékok és az algoritmusok fogsága",
                "summary": "How social media recommendation systems divide Hungarian society into mutually sealed informational tribes unable to communicate with each other.",
                "paragraphs": [
                    {"type": "narration", "text": "A Facebook és a TikTok korszakában a valóság már nem közös élmény, hanem személyre szabott digitális tükörterem. Az ajánlóalgoritmusok egyetlen célra lettek optimalizálva: a képernyőidő maximalizálására. Mivel az emberi pszichológia a felháborodásra és a félelemre reagál a legerősebben, a rendszerek a szélsőséges, érzelmileg fűtött tartalmakat tolják előtérbe."},
                    {"type": "narration", "text": "Magyarországon ez a mechanizmus aggasztó módon felerősítette a meglévő politikai törésvonalakat. A választók hermetikusan zárt buborékokban élnek, ahol a másik oldal érvei vagy nem jutnak át a szűrőkön, vagy eleve hazugságként és ellenséges propagandaként jelennek meg. A deliberatív demokrácia alapját jelentő közös valóságérzékelés fokozatosan elpárolog a hírfolyamok örvényében."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működnek a közösségi média 'véleménybuborékai' (filter bubbles)?", [
                    "Az algoritmusok a korábbi aktivitás alapján szűrik a tartalmat, így a felhasználó csak a saját nézeteit megerősítő üzenetekkel találkozik.",
                    "Szappanbuborékokat fújnak a számítógép ventilátorából.",
                    "Kizárólag tudományos enciklopédiák szócikkeit mutatják be."
                ], 0, ["c1-mediakritika-vocab"]),
                fb("grammar", "controlled", "_____ módon (In an alarming manner / Aggasztó) a közösségi platformok a társadalmi megosztottság elmélyítéséből húznak profitot.", "Aggasztó", "In an alarming manner, social platforms draw profit from deepening societal division.", ["c1-evaluative-adverbial-stance"]),
                match("vocabulary", "controlled", [["véleménybuborék", "önmegerősítő zárt információs tér"], ["megerősítési torzítás", "saját hiedelmet igazoló tények keresése"], ["felháborodás-gazdaságtan", "negatív érzelmek monetizálása"], ["mikrocélzás", "személyre szabott hirdetési manipuláció"]], ["c1-mediakritika-vocab"]),
                fb("grammar", "practice", "A törzsi gondolkodás elterjedése _____ megnehezíti az észérveken nyugvó közös döntéshozatalt. (unquestionably / vitathatatlanul)", "vitathatatlanul", "The spread of tribal thinking unquestionably hinders joint decision making based on rational arguments.", ["c1-evaluative-adverbial-stance"]),
                sb("grammar", "practice", ["Az", "ajánlóalgoritmusok", "tudatosan", "a", "felhasználók", "érzelmi", "reakcióira", "építenek."], ["Az", "ajánlóalgoritmusok", "tudatosan", "a", "felhasználók", "érzelmi", "reakcióira", "építenek."], "Recommendation algorithms consciously build on users' emotional reactions.", ["c1-evaluative-adverbial-stance"]),
                dc("dialogue", [
                    {"speaker": "Társadalomkutató", "text": "Miért nem állnak szóba egymással a különböző politikai táborok hívei?"},
                    {"speaker": "Digitális etikus", "text": "Mert a buborékok miatt már az alaptényekben sem értenek egyet: mindenkinek megvan a maga saját _____."},
                ], ["valósága", "cipője", "biciklije"], 0, ["c1-evaluative-adverbial-stance"]),
                sw("production", [{"prompt": "Write an evaluative stance sentence about algorithmic radicalization.", "answer": "Aggasztó módon a platformok algoritmikus szűrői ahelyett, hogy a sokszínű tájékozódást segítenék, vitathatatlanul a polarizációt és a dogmatikus törzsi szemléletet erősítik fel a társadalomban."}], ["c1-evaluative-adverbial-stance"]),
                mc("grammar", "check", "Melyik határozószó fejez ki morális vagy intellektuális értékítéletet?", [
                    "aggasztó módon",
                    "lassan",
                    "délelőtt"
                ], 0, ["c1-evaluative-adverbial-stance"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Disinformation, Deepfakes & Hybrid Information Warfare",
            "grammar_title": "Adversative Resumptive Discourse Markers Structuring Complex Commentary",
            "grammar_skill": "c1-adversative-resumptive-markers",
            "goals": [
                "I can analyze hybrid warfare, troll factories, and synthetic deepfakes (*dezinformáció, mélyhamisítás, hibrid hadviselés*).",
                "I can employ adversative resumptive discourse markers (*mindent összevetve, másfelől viszont, ezzel szemben, ugyanakkor*).",
                "I can evaluate fact-checking methodologies and informational resilience in Central Europe."
            ],
            "vocab": [
                {"lemma": "dezinformáció", "translation": "disinformation (deliberate falsehood)", "pos": "noun"},
                {"lemma": "mélyhamisítás", "translation": "deepfake (synthetic media)", "pos": "noun"},
                {"lemma": "hibrid hadviselés", "translation": "hybrid warfare", "pos": "expression"},
                {"lemma": "trollhadsereg", "translation": "troll army / coordinated bot network", "pos": "noun"},
                {"lemma": "tényellenőrzés", "translation": "fact-checking", "pos": "noun"},
                {"lemma": "információs integritás", "translation": "information integrity", "pos": "expression"},
                {"lemma": "kiberbiztonsági kockázat", "translation": "cybersecurity risk", "pos": "expression"},
                {"lemma": "médiaértés", "translation": "media literacy", "pos": "noun"}
            ],
            "gr_text1": "Adversative resumptive markers (*mindent összevetve* [all things considered], *másfelől viszont* [on the other hand, however], *ezzel szemben* [in contrast], *ugyanakkor* [at the same time]) synthesize multi-layered geopolitical and media analyses.",
            "gr_text2": "Example in geopolitical media context: `A közösségi hálózatok technológiai szűrői egyre fejlettebbek; ugyanakkor a mesterséges intelligenciával előállított mélyhamisítások felismerése másfelől viszont folyamatos versenyfutást jelent a védelmi szakemberek számára`.",
            "gr_table": [
                ["A tényellenőrzés nélkülözhetetlen eszköz; ezzel szemben a cáfolatok hatása gyakran elmarad az eredeti álhírekétől.", "Fact-checking is an indispensable tool; in contrast, the impact of refutations often falls behind that of the original fake news."],
                ["Mindent összevetve a dezinformáció elleni leghatékonyabb védelmet a kritikus médiaértés fejlesztése jelenti.", "All things considered, the most effective protection against disinformation is developing critical media literacy."],
                ["Egyfelől a technológia veszélyforrás; másfelől viszont az automatizált ellenőrzésben is hatalmas segítséget nyújt.", "On one hand technology is a threat vector; on the other hand, however, it also provides immense help in automated verification."]
            ],
            "world_story_seg": {
                "seg_slug": "dezinformacio",
                "title": "A virtuális frontvonal: Álhírek, deepfake és információs hadviselés Közép-Európában",
                "summary": "How foreign and domestic actors deploy automated botnets, AI-generated synthetic media, and coordinated narratives to undermine trust in democratic institutions.",
                "paragraphs": [
                    {"type": "narration", "text": "A huszonegyedik századi hadviselés nem csupán páncélosokkal és drónokkal, hanem bitekkel és narratívákkal zajlik. A közép-európai térség az orosz-ukrán háború kitörése óta kiemelt célpontjává vált a koordinált dezinformációs hadműveleteknek. Álhíroldalak hálózatai, mesterségesen vezérelt közösségi profilok és generatív MI-vel készült mélyhamisítások árasztják el a digitális teret."},
                    {"type": "narration", "text": "Ezek célja nem feltétlenül az, hogy az embereket egyetlen konkrét alternatív igazságról győzzék meg, hanem az, hogy szétzilálják magát a tényekbe és az intézményekbe vetett bizalmat. Ha minden információ gyanús és relatív, a társadalom apátiába süllyed. Mindent összevetve az információs szuverenitás megőrzése a katonai védelemnél is alapvetőbb nemzetbiztonsági feladattá lépett elő."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a koordinált dezinformációs kampányok legfőbb stratégiai célja?", [
                    "A tényekbe és a demokratikus intézményekbe vetett bizalom szétzilálása, a társadalmi apátia és bizonytalanság előidézése.",
                    "A számítógépes játékok népszerűsítése.",
                    "A szótárak árának csökkentése."
                ], 0, ["c1-mediakritika-vocab"]),
                fb("grammar", "controlled", "A technikai szűrés javult, _____ (at the same time / ugyanakkor) a mélyhamisítások élethűsége is ugrásszerűen növekszik.", "ugyanakkor", "Technical filtering improved, at the same time the realism of deepfakes is also increasing by leaps and bounds.", ["c1-adversative-resumptive-markers"]),
                match("vocabulary", "controlled", [["dezinformáció", "szándékos megtévesztés"], ["mélyhamisítás", "MI-vel generált szintetikus kép/videó"], ["tényellenőrzés", "állítások valóságtartalmának vizsgálata"], ["médiaértés", "kritikus hírhasználati készség"]], ["c1-mediakritika-vocab"]),
                fb("grammar", "practice", "Mindent _____ a digitális öntisztulás legfontosabb eszköze a független újságírók munkája. (considered / összevetve)", "összevetve", "All things considered, the most important tool of digital self-cleansing is the work of independent journalists.", ["c1-adversative-resumptive-markers"]),
                sb("grammar", "practice", ["A", "mélyhamisítások", "megkérdőjelezik", "a", "vizuális", "bizonyítékok", "hagyományos", "hitelességét."], ["A", "mélyhamisítások", "megkérdőjelezik", "a", "vizuális", "bizonyítékok", "hagyományos", "hitelességét."], "Deepfakes call into question the traditional credibility of visual evidence.", ["c1-adversative-resumptive-markers"]),
                dc("dialogue", [
                    {"speaker": "Biztonsági szakértő", "text": "Hogyan védekezhet egy állampolgár az álhírekkel szemben?"},
                    {"speaker": "Médiaoktató", "text": "Több forrás párhuzamos ellenőrzésével és a kiemelten szenzációhajhász címekkel szembeni _____."},
                ], ["szkepticizmussal", "rajongással", "támogatással"], 0, ["c1-adversative-resumptive-markers"]),
                sw("production", [{"prompt": "Write a resumptive sentence summarizing the threat of deepfakes.", "answer": "Mindent összevetve a mesterséges intelligenciával manipulált felvételek elterjedése példátlan kihívás elé állítja a nyilvánosságot, ugyanakkor felértékeli a hitelesített tényellenőrző műhelyek szerepét."}], ["c1-adversative-resumptive-markers"]),
                mc("grammar", "check", "Melyik kifejezés funkcionál összegző-szembeállító diskurzusjelölőként?", [
                    "mindent összevetve / ugyanakkor",
                    "azután",
                    "mindig"
                ], 0, ["c1-adversative-resumptive-markers"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Investigative Journalism & Pegasus Surveillance",
            "grammar_title": "Deontic and Regulatory Subjunctive Clauses in Institutional Mandates",
            "grammar_skill": "c1-subjunctive-regulatory-mandates",
            "goals": [
                "I can analyze investigative journalism, spyware surveillance, and whistleblower protection (*Pegasus, kémszoftver, forrásvédelem*).",
                "I can construct deontic regulatory subjunctive sentences (*követelményként írja elő, hogy biztosítsák; nélkülözhetetlen, hogy garantálja; elvárja, hogy fellépjenek*).",
                "I can debate the Pegasus scandal and surveillance of journalists by state intelligence in Hungary."
            ],
            "vocab": [
                {"lemma": "kémszoftver", "translation": "spyware (Pegasus)", "pos": "noun"},
                {"lemma": "titkosszolgálati megfigyelés", "translation": "secret service surveillance", "pos": "expression"},
                {"lemma": "forrásvédelem", "translation": "protection of journalistic sources", "pos": "noun"},
                {"lemma": "oknyomozó műhely", "translation": "investigative newsroom (Direkt36, Átlátszó)", "pos": "expression"},
                {"lemma": "hatósági engedélyezés", "translation": "regulatory authorization / judicial warrant", "pos": "expression"},
                {"lemma": "jogállami garancia", "translation": "rule-of-law safeguard", "pos": "expression"},
                {"lemma": "magánszféra védelme", "translation": "protection of privacy", "pos": "expression"},
                {"lemma": "visszaélés kivizsgálása", "translation": "investigation of abuse", "pos": "expression"}
            ],
            "gr_text1": "Deontic and regulatory subjunctive expressions (*követelményként írja elő, hogy...* [prescribes as a requirement that...], *elengedhetetlen, hogy biztosítsák* [it is indispensable that they ensure], *elvárható, hogy a hatóságok függetlenül járjanak el* [it is expected that authorities proceed independently]) define institutional accountability standards.",
            "gr_text2": "Example in human rights and surveillance context: `Az Emberi Jogok Európai Bírósága egyértelműen előírja, hogy a titkosszolgálati megfigyeléseket független bírói engedélyhez kössék, megelőzve az újságírók forrásvédelmének önkényes megsértését`.",
            "gr_table": [
                ["A nemzetközi normák megkövetelik, hogy a hatóságok szigorúan tartsák tiszteletben a forrásvédelmet.", "International norms require that authorities strictly respect protection of sources."],
                ["Nélkülözhetetlen, hogy független vizsgálóbizottság tárja fel a kémszoftver alkalmazásának körülményeit.", "It is indispensable that an independent inquiry committee uncover circumstances of spyware deployment."],
                ["A jogszabályok előírják, hogy a megfigyelést csak bűncselekmény alapos gyanúja esetén engedélyezzék.", "Regulations prescribe that surveillance be authorized only in case of grounded suspicion of crime."]
            ],
            "world_story_seg": {
                "seg_slug": "oknyomozas",
                "title": "Kémszoftver a zsebben: A Pegasus-ügy és a magyar oknyomozók bátorsága",
                "summary": "How independent Hungarian journalists (Direkt36) uncovered that Israeli Pegasus cyber-weapons were deployed against domestic reporters, lawyers, and political figures.",
                "paragraphs": [
                    {"type": "narration", "text": "2021 júliusában a nemzetközi sajtóval szoros együttműködésben dolgozó magyar oknyomozó portál, a Direkt36 leleplezte a rendszerváltás utáni legsúlyosabb megfigyelési botrányt. A bizonyítékok feltárták, hogy az izraeli NSO cég Pegasus nevű katonai kémszoftverét – amely észrevétlenül képes átvenni az irányítást az okostelefonok kamerája, mikrofonja és titkosított üzenetei felett – magyar újságírók, médiatulajdonosok és ügyvédek ellen is bevetették."},
                    {"type": "narration", "text": "A lehallgatásokhoz az engedélyeket az Igazságügyi Minisztérium adta ki, külső bírói kontroll nélkül. A feltárás rávilágított arra a mély dilemmára, amely a nemzetbiztonsági érdekek és a sajtószabadság között feszül: ha az állam büntetlenül kémkedhet a saját kritikusai után, a független forrásvédelem és a demokratikus elszámoltathatóság alapjai omlanak össze."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt a Pegasus-botrány legfőbb tanulsága Magyarországon?", [
                    "Hogy a nemzetbiztonsági hivatkozással végzett katonai kémszoftveres megfigyelések független bírói kontroll nélkül súlyosan veszélyeztetik a sajtószabadságot és a forrásvédelmet.",
                    "Hogy a mobiltelefonok akkumulátora gyorsan lemerül télen.",
                    "Hogy Izraelben tilos szoftvereket fejleszteni."
                ], 0, ["c1-mediakritika-vocab"]),
                fb("grammar", "controlled", "A strasbourgi bíróság elvárja, hogy a titkos megfigyeléseket független bírói kontrollnak _____ alá. (subject / vessék)", "vessék", "The Strasbourg court expects that secret surveillances be subjected to independent judicial control.", ["c1-subjunctive-regulatory-mandates"]),
                match("vocabulary", "controlled", [["Pegasus", "katonai fokozatú kémszoftver"], ["forrásvédelem", "újságírói informátorok védelme"], ["Direkt36", "hazai oknyomozó műhely"], ["jogállami garancia", "hatalmi önkény fékje"]], ["c1-mediakritika-vocab"]),
                fb("grammar", "practice", "Alapvető követelményként fogalmazódik meg, hogy az állam _____ a polgárok magánszféráját. (guarantee / garantálja)", "garantálja", "It is formulated as a basic requirement that the state guarantee the privacy of citizens.", ["c1-subjunctive-regulatory-mandates"]),
                sb("grammar", "practice", ["A", "forrásvédelem", "az", "oknyomozó", "újságírás", "megkérdőjelezhetetlen", "etikai", "alapköve."], ["A", "forrásvédelem", "az", "oknyomozó", "újságírás", "megkérdőjelezhetetlen", "etikai", "alapköve."], "Protection of sources is the unquestionable ethical cornerstone of investigative journalism.", ["c1-subjunctive-regulatory-mandates"]),
                dc("dialogue", [
                    {"speaker": "Jogvédő", "text": "Miért van szükség külső bírói engedélyre a megfigyelésekhez?"},
                    {"speaker": "Alkotmányjogász", "text": "Hogy a hatalom ne élhessen vissza az eszközzel politikai ellenfeleinek és a sajtó képviselőinek _____ céljából."},
                ], ["megfélemlítése", "kitüntetése", "meghívása"], 0, ["c1-subjunctive-regulatory-mandates"]),
                sw("production", [{"prompt": "Write a deontic subjunctive sentence demanding judicial oversight over surveillance.", "answer": "Elengedhetetlen, hogy a jogalkotó szigorú szabályokat vezessen be annak érdekében, hogy semmilyen titkosszolgálati megfigyelést ne lehessen elrendelni független és érdemi bírói engedély nélkül."}], ["c1-subjunctive-regulatory-mandates"]),
                mc("grammar", "check", "Melyik mondat alkalmaz kötelezettséget kifejező kötőmódot intézményi összefüggésben?", [
                    "A törvény követelményként írja elő, hogy az adatokat hozzák nyilvánosságra.",
                    "A törvény szerint az adatokat nyilvánosságra hozták tegnap.",
                    "Ha az adatokat nyilvánosságra hoznák, mindenki örülne."
                ], 0, ["c1-subjunctive-regulatory-mandates"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Civic Resilience, Crowdfunding & Epistemic Hygiene",
            "grammar_title": "Emphatic Scalar Additive Particles Highlighting Extreme Propositions",
            "grammar_skill": "c1-adv-emphatic-scalar-particles",
            "goals": [
                "I can analyze civic community financing, media resilience, and reader donations (*közösségi finanszírozás, olvasói támogatás, reziliencia*).",
                "I can utilize emphatic scalar particles (*még maga a... is, egyetlenegy sem, mégoly csekély, sőt mi több*).",
                "I can debate citizen media autonomy, subscription models (Telex, 444, Válasz Online), and epistemic hygiene."
            ],
            "vocab": [
                {"lemma": "közösségi finanszírozás", "translation": "crowdfunding / reader funding", "pos": "expression"},
                {"lemma": "olvasói támogatás", "translation": "reader subscription / donation", "pos": "expression"},
                {"lemma": "médiareziliencia", "translation": "media resilience", "pos": "noun"},
                {"lemma": "episztemikus higiénia", "translation": "epistemic hygiene / critical discernment", "pos": "expression"},
                {"lemma": "előfizetői modell", "translation": "subscription model", "pos": "expression"},
                {"lemma": "közösségi felelősségvállalás", "translation": "civic assumption of responsibility", "pos": "expression"},
                {"lemma": "hírdiéta", "translation": "news diet (curation of media intake)", "pos": "noun"},
                {"lemma": "szerkesztőségi integritás", "translation": "editorial integrity", "pos": "expression"}
            ],
            "gr_text1": "Emphatic scalar additive particles (*még maga a... is* [even ... itself], *egyetlenegy sem* [not a single one], *mégoly csekély* [however slight], *sőt mi több* [what is more]) heighten argumentative climax in civic discourse.",
            "gr_text2": "Example in reader empowerment context: `Még maga a legszerényebb mikroadomány is a szerkesztőségi függetlenség bástyájává válik egy olyan környezetben, ahol az állami hirdetési piacot politikai fegyverként használják`.",
            "gr_table": [
                ["Még maga a nemzetközi szakma is elámult azon a gyorsaságon, amellyel a magyar olvasók felépítették a Telexet.", "Even the international profession itself was amazed at the speed with which Hungarian readers built Telex."],
                ["Mégoly csekély összegű rendszeres előfizetés is közvetlen hozzájárulást jelent a média túléléséhez.", "However slight an amount of regular subscription represents a direct contribution to media survival."],
                ["Egyetlenegy független hang elnémítása sem maradhat társadalmi tiltakozás nélkül.", "Not a single independent voice's silencing can remain without social protest."]
            ],
            "world_story_seg": {
                "seg_slug": "jovo",
                "title": "Az olvasók ereje: Közösségi finanszírozás és a magyar sajtóreziliencia",
                "summary": "How Hungarian citizens saved independent newsrooms through crowdfunding (Index mass-resignation, creation of Telex, Válasz Online, and 444 memberships).",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 2020 nyarán az Index szerkesztősége a politikai befolyásolási kísérletek elleni tiltakozásul felállt és távozott, sokan a magyar független internetes újságírás végét jövendölték. Ám az ezt követő események a hazai polgári társadalom páratlan érettségéről tettek tanúbizonyságot: tízezrek nyitották meg pénztárcájukat, és napok alatt összeadták az új szerkesztőség, a Telex megalapításához szükséges tőkét."},
                    {"type": "narration", "text": "Ez a közösségi fordulat új korszakot nyitott. A Válasz Online, a 444 és a Direkt36 modellje bebizonyította, hogy az olvasói előfizetések és mikroadományok képesek ellensúlyozni az állami piactorzítást. A független sajtó nem a hirdetőknek vagy az oligarcháknak tartozik elszámolással, hanem kizárólag a közönségének. Ez a részvételi modell az episztemikus higiénia és a társadalmi ellenállóképesség legfőbb garanciája."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinthető történelmi áttörésnek a magyar közösségi médiafinanszírozás sikere?", [
                    "Mert megmutatta, hogy a tudatos olvasók mikroadományai és előfizetései képesek fenntartani a független szerkesztőségeket politikai nyomás ellenére is.",
                    "Mert az újságok innentől kezdve ingyen osztottak ajándékokat.",
                    "Mert minden olvasó miniszteri kinevezést kapott."
                ], 0, ["c1-mediakritika-vocab"]),
                fb("grammar", "controlled", "_____ maga a legnagyobb gazdasági nyomás sem tudta megtörni az olvasók elszántságát. (Even / Még)", "Még", "Even the greatest economic pressure itself could not break the determination of readers.", ["c1-adv-emphatic-scalar-particles"]),
                match("vocabulary", "controlled", [["közösségi finanszírozás", "olvasói mikroadományok rendszere"], ["szerkesztőségi integritás", "külső nyomástól független újságírás"], ["médiareziliencia", "túlélési képesség válságban"], ["episztemikus higiénia", "kritikus és tiszta tájékozódási kultúra"]], ["c1-mediakritika-vocab"]),
                fb("grammar", "practice", "Mégoly _____ (however slight / csekély) rendszeres havi támogatás is létfontosságú a lap fennmaradásához.", "csekély", "However slight a regular monthly support is vital for the survival of the paper.", ["c1-adv-emphatic-scalar-particles"]),
                sb("grammar", "practice", ["A", "közösségi", "finanszírozás", "a", "sajtószabadság", "legközvetlenebb", "állampolgári", "védelme."], ["A", "közösségi", "finanszírozás", "a", "sajtószabadság", "legközvetlenebb", "állampolgári", "védelme."], "Crowdfunding is the most direct civic protection of freedom of the press.", ["c1-adv-emphatic-scalar-particles"]),
                dc("dialogue", [
                    {"speaker": "Főszerkesztő", "text": "Hogyan maradhatunk meg a piacról kiszorulva is függetlennek?"},
                    {"speaker": "Kiadóvezető", "text": "A hirdetők helyett kizárólag az olvasói _____ modelljére támaszkodva."},
                ], ["előfizetések", "kölcsönök", "segélyek"], 0, ["c1-adv-emphatic-scalar-particles"]),
                sw("production", [{"prompt": "Write an emphatic scalar sentence about civic responsibility in funding journalism.", "answer": "Még maga a legkisebb összegű olvasói támogatás is felbecsülhetetlen jelentőségű, hiszen a független szerkesztőségek megmentése a demokratikus jövőnk záloga."}], ["c1-adv-emphatic-scalar-particles"]),
                mc("grammar", "check", "Melyik kifejezés funkcionál skáláris fokozó partikulaként emelkedett szövegben?", [
                    "még maga a... is / mégoly csekély",
                    "néha",
                    "esetleg"
                ], 0, ["c1-adv-emphatic-scalar-particles"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(16, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A szabad szó ára: Médiapluralizmus, algoritmusok és polgári reziliencia Magyarországon",
            "level": "C1",
            "type": "world",
            "order": 16,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of the Hungarian media landscape and information ecosystem: from the creation of the KESMA conglomerate and state advertising distortion, the polarizing mechanics of social media echo chambers, deepfake and hybrid warfare threats, the courageous revelations of Pegasus surveillance by Direkt36, to the triumph of reader-driven crowdfunding and democratic resilience.",
            "grammar": [
                "c1-discourse-polarizing-contrastives",
                "c1-evaluative-adverbial-stance",
                "c1-adversative-resumptive-markers",
                "c1-subjunctive-regulatory-mandates",
                "c1-adv-emphatic-scalar-particles"
            ],
            "vocabularyTopics": [
                "Media Pluralism, Algorithmic Filters & Information Integrity",
                "Media Landscape & Institutional Concentration",
                "Echo Chambers, Algorithmic Bubbles & Polarization",
                "Disinformation, Deepfakes & Hybrid Information Warfare",
                "Investigative Journalism & Pegasus Surveillance",
                "Civic Resilience, Crowdfunding & Epistemic Hygiene"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A nyilvánosság szabadsága nem magától értetődő természeti adottság, hanem a demokratikus polgárok szüntelen éberségét igénylő közös vívmány. Magyarországon az elmúlt évtizedek a médiaviszonyok radikális átrendeződését hozták: a több száz médiumot egyetlen politikai ernyő alá vonó KESMA konglomerátum létrehozása és az állami hirdetési piac tudatos torzítása soha nem látott kihívás elé állította a pluralizmust."},
                {"type": "narration", "text": "Mindeközben a digitális forradalom újabb törésvonalakat hozott felszínre: a közösségi platformok felháborodás-vezérelt ajánlóalgoritmusai aggasztó módon zárt véleménybuborékokba kényszerítették a polgárokat, elmélyítve a törzsi gondolkodást és kiszolgáltatva a közbeszédet a hibrid hadviselés célzott álhíreinek és mélyhamisításainak."},
                {"type": "narration", "text": "A hatalom és a nyilvánosság drámai összeütközését a Pegasus-ügy világította meg a legélesebben: amikor kiderült, hogy katonai kémszoftvereket vetettek be független újságírók és ügyvédek ellen, a forrásvédelem és a magánszféra sérthetetlensége a jogállamiság végső próbakövévé vált."},
                {"type": "narration", "text": "A magyar történet mégsem a behódolásról, hanem a rendkívüli polgári rezilienciáról szól. Az Index szerkesztőségének felállása után a semmiből felépített Telex, a Válasz Online, a 444 és a Direkt36 sikere bizonyította be, hogy az olvasói közösségek hajlandók felelősséget vállalni a saját tájékozódásukért. Még a legszerényebb mikroadományok is a függetlenség szilárd bástyájává válhatnak."},
                {"type": "narration", "text": "Bibó István igazsága ma érvényesebb, mint valaha: a szabadság ott kezdődik, ahol a polgárok nem félnek a tényektől, és nem hagyják, hogy a manipuláció elsorvassza a deliberatív vitát. A szabad sajtó jövője végső soron nem az algoritmusokon vagy az állami szabályokon múlik, hanem azon a közös elszántságon, amellyel a társadalom megvédi a valóság tiszta, független tükrét."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        16,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze media market concentration (KESMA) and state advertising distortion.",
            "I can evaluate algorithmic echo chambers, deepfakes, and Pegasus surveillance.",
            "I can discuss civic media crowdfunding, reader resilience, and epistemic hygiene at the C1 level."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki éles, fokozó-polarizáló ellentétet?", [
                "nemhogy nem..., sőt éppenséggel / korántsem..., sokkal inkább",
                "mindössze annyiban, hogy",
                "hacsak nem"
            ], 0, ["c1-discourse-polarizing-contrastives"]),
            mc("grammar", "recognize", "Mit fejeznek ki a 'még maga a... is', 'mégoly csekély' szerkezetek?", [
                "Skáláris fokozást, amely a szélső vagy legkisebb értéket is hangsúlyozza az érvelésben.",
                "Időbeli egymásutániságot.",
                "Kételyt a beszélő kilétét illetően."
            ], 0, ["c1-adv-emphatic-scalar-particles"]),
            match("vocabulary", "recognize", [["KESMA", "központosított kormánypárti médiakonglomerátum"], ["véleménybuborék", "algoritmusok által elszigetelt nézőpont"], ["mélyhamisítás", "MI-vel előállított szintetikus média"], ["forrásvédelem", "újságírói titoktartás és informátori védelem"], ["közösségi finanszírozás", "olvasói mikroadományok modellje"]], ["c1-mediakritika-vocab"]),
            fb("vocabulary", "recall", "A médiarendszerben az állami reklámköltések egyoldalú elosztása súlyos piaci _____ eredményezett. (distortion / torzulást)", "torzulást", "In the media system, unilateral allocation of state advertising expenditure resulted in severe market distortion.", ["c1-mediakritika-vocab"]),
            fb("vocabulary", "recall", "A modern újságírás legfőbb fegyvere a manipuláció ellen az adatok alapos _____ elvégzése. (fact-checking / tényellenőrzésének)", "tényellenőrzésének", "The foremost weapon of modern journalism against manipulation is performing thorough fact-checking of data.", ["c1-mediakritika-vocab"]),
            fb("grammar", "recall", "A koncentráció _____ sem a sokszínűséget szolgálta, sokkal inkább a centralizációt. (far / koránt)", "koránt", "The concentration far from served diversity; much rather centralization.", ["c1-discourse-polarizing-contrastives"]),
            fb("grammar", "context", "_____ módon a fiatalok egyre nagyobb hányada csak rövid közösségi videókból tájékozódik. (In an alarming / Aggasztó)", "Aggasztó", "In an alarming manner, an ever larger proportion of young people informs itself solely from short social videos.", ["c1-evaluative-adverbial-stance"]),
            fb("grammar", "context", "A nemzetközi normák elvárják, hogy a hatóságok _____ a sajtó képviselőit a jogtalan megfigyelésektől. (protect / megvédjék)", "megvédjék", "International norms expect that authorities protect representatives of the press from unlawful surveillance.", ["c1-subjunctive-regulatory-mandates"]),
            mc("grammar", "context", "Mi a közösségi média gazdasági modelljének legfőbb kritikája?", [
                "Hogy a figyelem maximalizálása érdekében a felháborodást és a polarizációt jutalmazza a higgadt érvek helyett.",
                "Hogy túl olcsóvá teszi az internet-előfizetéseket.",
                "Hogy nem enged zenét hallgatni a háttérben."
            ], 0, ["c1-evaluative-adverbial-stance"]),
            sb("grammar", "produce", ["A", "független", "sajtó", "túlélése", "a", "tudatos", "olvasói", "közösségek", "felelőssége."], ["A", "független", "sajtó", "túlélése", "a", "tudatos", "olvasói", "közösségek", "felelőssége."], "The survival of the independent press is the responsibility of conscious reader communities.", ["c1-adv-emphatic-scalar-particles"]),
            sw("production", [{"prompt": "Write a critical evaluation of media pluralism and civic crowdfunding.", "answer": "A médiapiac monopolizálása és az állami hirdetések torzító hatása korántsem vezetett a kritikai hangok elhallgatásához: az olvasói közösségi finanszírozás sikere bebizonyította a társadalom elszántságát a szabad tájékozódás megőrzése mellett."}], ["c1-discourse-polarizing-contrastives"]),
            sw("production", [{"prompt": "Formulate a concluding thought on information integrity and democratic public sphere.", "answer": "Mindent összevetve az információs integritás megóvása nem pusztán technikai feladat, hanem a polgárok közös etikai kötelessége: a szabad nyilvánosság védelme a demokratikus jogállam legfőbb garanciája."}], ["c1-adversative-resumptive-markers"])
        ]
    )

    print("=== Finished C1 Unit 16 ===")


if __name__ == "__main__":
    generate_unit_16()
