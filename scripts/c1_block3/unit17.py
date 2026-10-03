#!/usr/bin/env python3
"""
Hungarian C1 Block 3 - Unit 17 Generator:
  - Track 1 (Core): Unit 17 — "Regional Geopolitics, Diplomatic Strategy & Transnational Coalitions" (c1-17)
  - Track 2 (Discourse): Unit 17 — "The Visegrád Group (V4), Regional Alliances & European Cohesion" (c1-visegrad)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block3.registry_helper import register_unit


def generate_unit_17():
    print("=== Generating C1 Unit 17 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-17-vocab": {"kind": "vocabulary"},
        "c1-visegrad-vocab": {"kind": "vocabulary"},
        "c1-diplomatic-hedging-conditional": {"kind": "grammar"},
        "c1-complex-locative-correlatives": {"kind": "grammar"},
        "c1-nominal-compound-geopolitical-syntax": {"kind": "grammar"},
        "c1-adv-temporal-successive-aspect": {"kind": "grammar"},
        "c1-adv-manner-comparative-similes": {"kind": "grammar"},
        "c1-discourse-divergence-markers": {"kind": "grammar"},
        "c1-concessive-stipulative-clauses": {"kind": "grammar"},
        "c1-rhetorical-antithetical-parallelism": {"kind": "grammar"},
        "c1-modal-deontic-treaty-predicates": {"kind": "grammar"},
        "c1-adv-discourse-summation-particles": {"kind": "grammar"},
    }
    new_titles = {
        "c1-17-vocab": "reading",
        "c1-visegrad-vocab": "reading",
        "c1-diplomatic-hedging-conditional": "diplomatic conditional hedging and tentative subjunctive assertion in negotiations",
        "c1-complex-locative-correlatives": "complex spatial and locative correlative constructions in geopolitical descriptions",
        "c1-nominal-compound-geopolitical-syntax": "elaborate geopolitical compound nominalizations and genitive attribute chains",
        "c1-adv-temporal-successive-aspect": "successive temporal adverbial conjunctions expressing chronological antecedence",
        "c1-adv-manner-comparative-similes": "complex comparative similes and analogical markers in historical exposition",
        "c1-discourse-divergence-markers": "discourse markers of geopolitical divergence and diplomatic disagreement",
        "c1-concessive-stipulative-clauses": "concessive stipulative clauses defining treaty conditions and reservations",
        "c1-rhetorical-antithetical-parallelism": "rhetorical antithetical parallelism in international relations analysis",
        "c1-modal-deontic-treaty-predicates": "deontic treaty predicates expressing pact obligations and diplomatic mandates",
        "c1-adv-discourse-summation-particles": "discourse summation particles and definitive conclusions in foreign policy",
    }
    
    core_title = "Regional Geopolitics, Diplomatic Strategy & Transnational Coalitions"
    core_stems = [f"c1-17-0{i}" for i in range(1, 6)] + ["c1-17-consolidation"]
    disc_title = "The Visegrád Group (V4), Regional Alliances & European Cohesion"
    disc_stems = [f"c1-visegrad-0{i}" for i in range(1, 6)] + ["c1-visegrad-consolidation"]
    
    register_unit(17, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-17)
    # ----------------------------------------------------
    core_intro = [
        "Regional geopolitics, diplomatic negotiations, and historical-geographical destiny in Central Europe demand sophisticated conditional hedging, locative correlatives, and dense nominal syntax.",
        "In this unit, inspired by Jenő Szűcs's internationally renowned historical-sociological essay 'Vázlat Európa három történeti régiójáról' (1980), you will master the elevated geopolitical and diplomatic register of Hungarian at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-17-01",
            "title": "Diplomatic Protocol, Strategic Hedging & Geopolitical Realism",
            "grammar_title": "Diplomatic Conditional Hedging and Tentative Subjunctive Assertion in Negotiations",
            "grammar_skill": "c1-diplomatic-hedging-conditional",
            "goals": [
                "I can analyze diplomatic posture, geopolitical realism, and strategic hedging (*diplomáciai protokoll, reálpolitika, stratégiai hintapolitika*).",
                "I can formulate tentative diplomatic assertions using conditional hedging (*úgy vélhetnénk, hajlunk arra a megállapításra, aligha volna célravezető*).",
                "I can evaluate bilateral state treaties and multilateral communiqué formulation in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "diplomáciai protokoll", "translation": "diplomatic protocol", "pos": "expression"},
                {"lemma": "reálpolitika", "translation": "realpolitik", "pos": "noun"},
                {"lemma": "stratégiai hintapolitika", "translation": "strategic hedging / pendulum policy", "pos": "expression"},
                {"lemma": "kétoldalú kapcsolatok", "translation": "bilateral relations", "pos": "expression"},
                {"lemma": "zárónyilatkozat", "translation": "joint communiqué / final declaration", "pos": "noun"},
                {"lemma": "kompromisszumkészség", "translation": "readiness for compromise", "pos": "noun"},
                {"lemma": "geopolitikai mozgástér", "translation": "geopolitical maneuvering room", "pos": "expression"},
                {"lemma": "államérdek", "translation": "raison d'état / state interest", "pos": "noun"}
            ],
            "gr_text1": "Diplomatic hedging avoids confrontational absolutes by deploying epistemic conditional verbs and tentative subjunctive phrases: `Hajlunk arra a megállapításra, hogy a tárgyalások elakadása aligha volna orvosolható egyoldalú nyilatkozatokkal; úgy vélhetnénk, a feleknek a kompromisszumkészség felmutatására volna szükségük`.",
            "gr_text2": "These polite modal hedges (*úgy tűnhetne, óvakodnánk attól, hogy kijelentsük, célszerűnek mutatkoznék*) protect diplomatic flexibility during multilateral bargaining.",
            "gr_table": [
                ["Úgy vélhetnénk, hogy a kétoldalú kapcsolatok normalizálása mindkét fél érdeke volna.", "We might consider that normalizing bilateral relations would be in the interest of both parties."],
                ["Hajlunk arra a feltételezésre, hogy a feszültségek diplomáciai csatornákon keresztül enyhíthetők lennének.", "We are inclined to the assumption that tensions could be eased through diplomatic channels."],
                ["Óvakodnánk attól, hogy a zárónyilatkozatot a tárgyalások kudarcaként értékeljük.", "We would be cautious about evaluating the final declaration as a failure of negotiations."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'reálpolitika' (realpolitik) a nemzetközi kapcsolatokban?", [
                    "Olyan külpolitikai gyakorlatot, amely ideológiai doktrínák helyett a nyers hatalmi érdekekre és a gyakorlati erőviszonyokra épít.",
                    "A televíziós valóságshow-k elemzését.",
                    "A határok nélküli világ azonnali kikiáltását."
                ], 0, ["c1-17-vocab"]),
                fb("grammar", "controlled", "_____ (We might consider / Úgy vélhetnénk), hogy a regionális feszültségek érdemi párbeszéddel csillapíthatók volnának.", "Úgy vélhetnénk", "We might consider that regional tensions could be calmed with substantive dialogue.", ["c1-diplomatic-hedging-conditional"]),
                match("vocabulary", "controlled", [["reálpolitika", "gyakorlati hatalmi érdekpolitika"], ["zárónyilatkozat", "csúcstalálkozó hivatalos közleménye"], ["stratégiai hintapolitika", "két pólus közötti egyensúlyozás"], ["államérdek", "raison d'état"]], ["c1-17-vocab"]),
                fb("grammar", "practice", "Hajlunk arra a megállapításra, hogy a szankciók bevezetése aligha _____ a konfliktus békés lezárását. (would serve / szolgálná)", "szolgálná", "We are inclined to the statement that the introduction of sanctions would hardly serve the peaceful resolution of conflict.", ["c1-diplomatic-hedging-conditional"]),
                sb("grammar", "practice", ["A", "diplomáciai", "mozgástér", "bővítése", "a", "kisállami", "külpolitika", "elsődleges", "célja."], ["A", "diplomáciai", "mozgástér", "bővítése", "a", "kisállami", "külpolitika", "elsődleges", "célja."], "Expanding diplomatic maneuvering room is the primary goal of small-state foreign policy.", ["c1-diplomatic-hedging-conditional"]),
                dc("dialogue", [
                    {"speaker": "Diplomata", "text": "Hogyan fogalmazzuk meg a zárónyilatkozatot a vitatott kérdésben?"},
                    {"speaker": "Nagykövet", "text": "Finom diplomáciai _____ kell élnünk, amely nyitva hagyja a további egyeztetés lehetőségét."},
                ], ["óvatossággal", "támadással", "veszekedéssel"], 0, ["c1-diplomatic-hedging-conditional"]),
                sw("production", [{"prompt": "Write a diplomatically hedged statement about a border dispute.", "answer": "Úgy vélhetnénk, hogy a határellenőrzési protokoll kölcsönös felülvizsgálata célravezetőnek mutatkoznék, elkerülendő a kétoldalú kapcsolatok felesleges elmérgesedését."}], ["c1-diplomatic-hedging-conditional"]),
                mc("grammar", "check", "Melyik fordulat testesíti meg a diplomáciai óvatosságot és a feltételes körülírást?", [
                    "Hajlunk arra a feltételezésre, hogy a felek kompromisszumra törekednének.",
                    "A feleknek azonnal alá kell írniuk a követeléseinket!",
                    "Semmilyen tárgyalás nem fogadható el a jövőben."
                ], 0, ["c1-diplomatic-hedging-conditional"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-17-02",
            "title": "Buffer States, Fault Lines & Spatial Geopolitics",
            "grammar_title": "Complex Spatial and Locative Correlative Constructions in Geopolitical Descriptions",
            "grammar_skill": "c1-complex-locative-correlatives",
            "goals": [
                "I can analyze geopolitical buffer zones, civilizational fault lines, and spheres of influence (*ütközőállam, törésvonal, befolyási övezet*).",
                "I can deploy complex locative and directional correlatives (*ott ahol... éppúgy, ahonnan... odáig terjedően, amerre... arra*).",
                "I can debate the Carpathian Basin as a geopolitical crossroads between East and West."
            ],
            "vocab": [
                {"lemma": "ütközőzóna", "translation": "buffer zone", "pos": "noun"},
                {"lemma": "civilizációs törésvonal", "translation": "civilizational fault line", "pos": "expression"},
                {"lemma": "befolyási övezet", "translation": "sphere of influence", "pos": "expression"},
                {"lemma": "geopolitikai keresztút", "translation": "geopolitical crossroads", "pos": "expression"},
                {"lemma": "területi integritás", "translation": "territorial integrity", "pos": "expression"},
                {"lemma": "szuverenitási kockázat", "translation": "sovereignty risk", "pos": "expression"},
                {"lemma": "határvidék", "translation": "borderland / frontier", "pos": "noun"},
                {"lemma": "stratégiai mélység", "translation": "strategic depth", "pos": "expression"}
            ],
            "gr_text1": "Locative correlatives (*ott, ahol... éppúgy; ahonnan... odáig terjedően; amerre... arra*) establish spatial relationships in geopolitical cartography: `Ott, ahol a nagyhatalmi érdekszférák összeérnek, a szuverenitás megőrzése éppúgy megköveteli a katonai elrettentést, mint a rugalmas diplomáciát`.",
            "gr_text2": "Example in macro-regional prose: `A Kárpát-medence történetét mindig is az határozta meg, hogy amerről a birodalmi expanzió hullámai érkeztek, a helyi államoknak abba az irányba kellett stratégiai védelmi vonalakat kiépíteniük`.",
            "gr_table": [
                ["Ott, ahol a törésvonalak húzódnak, a béke törékeny egyensúlyon nyugszik.", "There where the fault lines run, peace rests upon a fragile equilibrium."],
                ["Ahonnan a keleti birodalmak nyomása kiindul, egészen odáig terjed a közép-európai védelmi zóna.", "From where the pressure of eastern empires emanates, all the way to there extends the Central European defense zone."],
                ["Amerre a transzeurópai folyosók futnak, arra koncentrálódik a gazdasági tőke is.", "Where the trans-European corridors run, there economic capital also concentrates."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a geopolitikai szerepe egy 'ütközőzónának' (buffer zone)?", [
                    "Két rivalizáló nagyhatalom vagy szövetségi rendszer közvetlen katonai összeütközésének elválasztása és a feszültségek tompítása.",
                    "A nemzetközi autóversenyek lebonyolítása.",
                    "A vasúti vagonok ütközőinek ellenőrzése."
                ], 0, ["c1-17-vocab"]),
                fb("grammar", "controlled", "Ott, ahol a történelmi törésvonalak húzódnak, a béke _____ (just as well / éppúgy) diplomáciai, mint katonai készenlétet igényel.", "éppúgy", "There where historical fault lines run, peace just as well demands diplomatic as military readiness.", ["c1-complex-locative-correlatives"]),
                match("vocabulary", "controlled", [["ütközőzóna", "szembenálló feleket elválasztó térség"], ["befolyási övezet", "nagyhatalmi dominancia területe"], ["területi integritás", "államhatárok sérthetetlensége"], ["stratégiai mélység", "hátország védelmi távolsága"]], ["c1-17-vocab"]),
                fb("grammar", "practice", "_____ a geopolitikai nyomás fokozódik, arra kell a szövetségi védelmi kapacitásokat csoportosítani. (Where / Amerre)", "Amerre", "Where geopolitical pressure intensifies, there allied defense capacities must be clustered.", ["c1-complex-locative-correlatives"]),
                sb("grammar", "practice", ["A", "Kárpát-medence", "évszázadokon", "át", "kelet", "és", "nyugat", "geopolitikai", "keresztútján", "feküdt."], ["A", "Kárpát-medence", "évszázadokon", "át", "kelet", "és", "nyugat", "geopolitikai", "keresztútján", "feküdt."], "The Carpathian Basin lay for centuries at the geopolitical crossroads of East and West.", ["c1-complex-locative-correlatives"]),
                dc("dialogue", [
                    {"speaker": "Biztonságpolitikus", "text": "Hogyan óvhatja meg szuverenitását egy kisállam a birodalmak árnyékában?"},
                    {"speaker": "Geopolitikus", "text": "Nem az elszigetelődéssel, hanem a többoldalú szövetségi rendszerekhez való szerves _____ révén."},
                ], ["illeszkedés", "menekülés", "támadás"], 0, ["c1-complex-locative-correlatives"]),
                sw("production", [{"prompt": "Write a locative correlative sentence about geopolitical positioning.", "answer": "Ott, ahol a kontinens keleti és nyugati szövetségi struktúrái érintkeznek, a régió stabilitása éppúgy a belső szolidaritáson, mint a kiszámítható nemzetközi partnerségeken múlik."}], ["c1-complex-locative-correlatives"]),
                mc("grammar", "check", "Melyik mondatpár kapcsol össze helyhatározói korrelációt emelkedett stílusban?", [
                    "Ott, ahol a birodalmak összeütköznek, éppúgy veszélyben forog a kisállami szabadság.",
                    "Mivel a birodalmak összeütköztek, a kisállamok bajba kerültek.",
                    "Bár a birodalmak összeütköztek, a kisállamok megmenekültek."
                ], 0, ["c1-complex-locative-correlatives"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-17-03",
            "title": "Transnational Treaties & Genitive Nominal Chains",
            "grammar_title": "Elaborate Geopolitical Compound Nominalizations and Genitive Attribute Chains",
            "grammar_skill": "c1-nominal-compound-geopolitical-syntax",
            "goals": [
                "I can analyze transnational treaties, collective security, and mutual defense commitments (*kollektív biztonság, kölcsönös védelmi klauzula, szövetségi kötelezettség*).",
                "I can construct elaborate compound nominalizations and multi-tiered genitive chains (*érdekszférák elhatárolása, szövetségi kötelezettségvállalások kölcsönössége*).",
                "I can evaluate North Atlantic Treaty Organization (NATO) Article 5 and European defense integration in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "kollektív védelem", "translation": "collective defense (NATO Art. 5)", "pos": "expression"},
                {"lemma": "kölcsönös segítségnyújtási záradék", "translation": "mutual assistance clause (EU Art. 42.7)", "pos": "expression"},
                {"lemma": "szövetségi kötelezettségvállalás", "translation": "alliance commitment", "pos": "noun"},
                {"lemma": "elrettentési képesség", "translation": "deterrence capability", "pos": "expression"},
                {"lemma": "fegyverkezési verseny", "translation": "arms race", "pos": "noun"},
                {"lemma": "haditechnikai kompatibilitás", "translation": "military-technical interoperability", "pos": "expression"},
                {"lemma": "katonai doktrína", "translation": "military doctrine", "pos": "expression"},
                {"lemma": "haderőfejlesztés", "translation": "armed forces modernization", "pos": "noun"}
            ],
            "gr_text1": "Advanced treaty language deploys multi-tiered genitive attribute chains linked through complex compound head nouns: `a szövetséges tagállamok kollektív védelmi képességének folyamatos korszerűsítése` (the continuous modernization of the collective defense capability of allied member states).",
            "gr_text2": "Syntactic stacking builds authoritative institutional force: `a haderőfejlesztési program nemzetbiztonsági garanciáinak intézményesítése`.",
            "gr_table": [
                ["A szövetségi kötelezettségvállalások érvényesítésének garanciája az elrettentésben rejlik.", "The guarantee of enforcing alliance commitments lies in deterrence."],
                ["A kölcsönös segítségnyújtási záradék alkalmazásának feltétele a fegyveres támadás ténye.", "The condition of applying the mutual assistance clause is the fact of an armed attack."],
                ["A haditechnikai eszközök interoperabilitásának növelése stratégiai prioritás.", "Increasing the interoperability of military-technical equipment is a strategic priority."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a NATO 5. cikkelye szerinti 'kollektív védelem' elve?", [
                    "Hogy a szövetség bármely tagállama elleni fegyveres támadást az összes tagállam elleni támadásnak tekintenek, és kollektíven fellépnek a megtámadott védelmében.",
                    "Hogy minden ország feloszlatja saját rendőrségét.",
                    "Hogy a tagállamok nem tarthatnak közös hadgyakorlatokat."
                ], 0, ["c1-17-vocab"]),
                fb("grammar", "controlled", "A szövetséges államok kollektív védelmi képességének _____ (modernization / korszerűsítése) kiemelt biztonságpolitikai érdek.", "korszerűsítése", "The modernization of the collective defense capability of allied states is a priority security policy interest.", ["c1-nominal-compound-geopolitical-syntax"]),
                match("vocabulary", "controlled", [["kollektív védelem", "támadás esetén közös fellépés"], ["elrettentési képesség", "támadás megelőzése erődemonstrációval"], ["haditechnikai kompatibilitás", "fegyverrendszerek együttműködési képessége"], ["haderőfejlesztés", "hadsereg felszerelésének felújítása"]], ["c1-17-vocab"]),
                fb("grammar", "practice", "A katonai doktrína sarokköve a szövetségi _____ feltétlen tiszteletben tartása. (commitments / kötelezettségvállalások)", "kötelezettségvállalások", "The cornerstone of military doctrine is unconditional respect for alliance commitments.", ["c1-nominal-compound-geopolitical-syntax"]),
                sb("grammar", "practice", ["A", "kölcsönös", "segítségnyújtási", "záradék", "szavatolja", "az", "európai", "térség", "biztonságát."], ["A", "kölcsönös", "segítségnyújtási", "záradék", "szavatolja", "az", "európai", "térség", "biztonságát."], "The mutual assistance clause guarantees the security of the European region.", ["c1-nominal-compound-geopolitical-syntax"]),
                dc("dialogue", [
                    {"speaker": "Védelmi miniszter", "text": "Hogyan emelhetjük a védelmi költségvetést a GDP 2 százalékára?"},
                    {"speaker": "Vezérkari főnök", "text": "Hosszú távú, átgondolt _____ program végrehajtásával és a légvédelem megerősítésével."},
                ], ["haderőfejlesztési", "mezőgazdasági", "turisztikai"], 0, ["c1-nominal-compound-geopolitical-syntax"]),
                sw("production", [{"prompt": "Write a dense genitive nominal sentence on collective defense commitments.", "answer": "A tagállamok elrettentési potenciáljának megkérdőjelezhetetlensége a szövetségi kötelezettségvállalások szilárdságán és a haditechnikai kompatibilitás garantálásán alapul."}], ["c1-nominal-compound-geopolitical-syntax"]),
                mc("grammar", "check", "Melyik szerkezet mutat be többszörösen összetett birtokos szerkezetet geopolitikai kontextusban?", [
                    "a szövetségi elrettentési doktrína hitelességének intézményes védelme",
                    "amikor a szövetség védekezik a támadás ellen",
                    "hogy a szövetség elrettentse az ellenfeleket"
                ], 0, ["c1-nominal-compound-geopolitical-syntax"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-17-04",
            "title": "Diplomatic Chronology & Temporal Successive Conjunctions",
            "grammar_title": "Successive Temporal Adverbial Conjunctions Expressing Chronological Antecedence",
            "grammar_skill": "c1-adv-temporal-successive-aspect",
            "goals": [
                "I can analyze diplomatic chronology, escalation spirals, and summit negotiations (*diplomáciai krónika, eszkaláció, csúcstalálkozó*).",
                "I can employ successive temporal conjunctions (*mielőtt még sor került volna, alighogy megkötötték, mihelyt életbe lépett*).",
                "I can reconstruct historical diplomatic crises and ceasefire pacts in elevated Hungarian historiography."
            ],
            "vocab": [
                {"lemma": "diplomáciai csúcstalálkozó", "translation": "diplomatic summit", "pos": "expression"},
                {"lemma": "eszkalációs spirál", "translation": "escalation spiral", "pos": "expression"},
                {"lemma": "tűzszüneti megállapodás", "translation": "ceasefire agreement", "pos": "expression"},
                {"lemma": "békéltető tárgyalás", "translation": "conciliation / mediation talks", "pos": "expression"},
                {"lemma": "ultimátum", "translation": "ultimatum", "pos": "noun"},
                {"lemma": "patthelyzet", "translation": "stalemate / impasse", "pos": "noun"},
                {"lemma": "demilitarizált övezet", "translation": "demilitarized zone", "pos": "expression"},
                {"lemma": "békefenntartó misszió", "translation": "peacekeeping mission", "pos": "expression"}
            ],
            "gr_text1": "Successive temporal conjunctions (*mielőtt még... volna* [even before ... could take place], *alighogy... máris* [hardly had ... when already], *mihelyt* [as soon as]) structure diplomatic chronicles with precise aspectual timing.",
            "gr_text2": "Example in historical crisis prose: `Mielőtt még a békéltető tárgyalások érdemben megkezdődhettek volna, a felek közötti fegyveres incidensek máris egy újabb eszkalációs spirált indítottak el`.",
            "gr_table": [
                ["Mielőtt még sor kerülhetett volna a csúcstalálkozóra, a határ menti csapatmozgások meghiúsították a megállapodást.", "Even before the summit could take place, border troop movements foiled the agreement."],
                ["Alighogy aláírták a tűzszünetet, máris felmerültek a megállapodás megsértéséről szóló hírek.", "Hardly had they signed the ceasefire when news concerning violations of the agreement already surfaced."],
                ["Mihelyt életbe lépett az egyezmény, a nemzetközi megfigyelők megkezdték a járőrözést.", "As soon as the pact took effect, international observers began patrolling."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'eszkalációs spirál' a konfliktuskutatásban?", [
                    "Olyan folyamatot, amelyben a felek egymást követő válaszlépései kölcsönösen és egyre magasabb szintre növelik a feszültséget vagy az erőszakot.",
                    "A hegyi utak csigalépcsőszerű kialakítását.",
                    "A tárgyalótermek légkondicionálását."
                ], 0, ["c1-17-vocab"]),
                fb("grammar", "controlled", "_____ még a diplomáciai jegyzéket átadhatták volna, a fegyveres konfliktus máris kirobbant. (Even before / Mielőtt)", "Mielőtt", "Even before the diplomatic note could be delivered, armed conflict had already erupted.", ["c1-adv-temporal-successive-aspect"]),
                match("vocabulary", "controlled", [["tűzszüneti megállapodás", "harci cselekmények ideiglenes beszüntetése"], ["patthelyzet", "elakadt tárgyalási állapot"], ["demilitarizált övezet", "fegyvermentes biztonsági sáv"], ["ultimátum", "utolsó, határidős felszólítás"]], ["c1-17-vocab"]),
                fb("grammar", "practice", "Alighogy megkötötték az egyezményt, _____ újabb viták támadtak a határok értelmezése körül. (already / máris)", "máris", "Hardly had they concluded the pact when new disputes already arose surrounding the interpretation of borders.", ["c1-adv-temporal-successive-aspect"]),
                sb("grammar", "practice", ["A", "békéltető", "tárgyalások", "célja", "az", "eszkalációs", "spirál", "haladéktalan", "megtörése."], ["A", "békéltető", "tárgyalások", "célja", "az", "eszkalációs", "spirál", "haladéktalan", "megtörése."], "The goal of conciliation talks is immediately breaking the escalation spiral.", ["c1-adv-temporal-successive-aspect"]),
                dc("dialogue", [
                    {"speaker": "Mediátor", "text": "Hogyan hidalhatjuk át a patthelyzetet a tárgyalásokon?"},
                    {"speaker": "Külügyminiszter", "text": "Feltétel nélküli azonnali _____ és demilitarizált övezet kijelölésével."},
                ], ["tűzszünettel", "támadással", "tüntetéssel"], 0, ["c1-adv-temporal-successive-aspect"]),
                sw("production", [{"prompt": "Write a temporal sentence using 'mielőtt még... volna' about crisis diplomacy.", "answer": "Mielőtt még a békefenntartó erők mandátuma lejárt volna, a feleknek sikerült tető alá hozniuk egy tartós fegyvernyugvási egyezményt."}], ["c1-adv-temporal-successive-aspect"]),
                mc("grammar", "check", "Melyik mondat fejez ki egymásra következést kifejező időhatározói viszonyt előidejűséggel?", [
                    "Alighogy befejeződött a csúcstalálkozó, máris kiadták a közös nyilatkozatot.",
                    "A csúcstalálkozó alatt sok kérdést megvitattak.",
                    "Ha befejeződik a csúcstalálkozó, mindenki hazamegy."
                ], 0, ["c1-adv-temporal-successive-aspect"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-17-05",
            "title": "Jenő Szűcs & The Three Historical Regions of Europe",
            "grammar_title": "Complex Comparative Similes and Analogical Markers in Historical Exposition",
            "grammar_skill": "c1-adv-manner-comparative-similes",
            "goals": [
                "I can analyze Jenő Szűcs's historical-geopolitical thesis in 'The Three Historical Regions of Europe' (1980).",
                "I can deploy comparative similes and analogical markers (*miként, amiképpen, hasonlatosképpen, mintsem*).",
                "I can debate Central Europe's dual heritage: Western structural institutions versus Eastern autocratic vulnerabilities."
            ],
            "vocab": [
                {"lemma": "történeti régió", "translation": "historical region (Szűcs's model)", "pos": "expression"},
                {"lemma": "nyugati kereszténység", "translation": "Western Latin Christendom", "pos": "expression"},
                {"lemma": "feudális struktúra", "translation": "feudal structural autonomy / corporatism", "pos": "expression"},
                {"lemma": "autokrácia", "translation": "autocracy / imperial absolutism", "pos": "noun"},
                {"lemma": "társadalmi autonómia", "translation": "societal autonomy", "pos": "expression"},
                {"lemma": "történelmi skizofrénia", "translation": "historical schizophrenia / dual identity", "pos": "expression"},
                {"lemma": "rendi alkotmányosság", "translation": "estate constitutionalism", "pos": "expression"},
                {"lemma": "szerves fejlődés", "translation": "organic historical development", "pos": "expression"}
            ],
            "gr_text1": "Complex comparative similes (*miként* [as / just as], *amiképpen* [in the manner that], *hasonlatosképpen* [in similar fashion]) draw structural analogies between historical epochs: `Miként a nyugati feudalizmus a hatalom megosztására és a társadalmi autonómiákra épült, akként gyökerezett meg Közép-Európában is a rendi alkotmányosság eszméje`.",
            "gr_text2": "These analogical markers lend elegance to philosophical and sociological historiography: `Hasonlatosképpen a cseh és lengyel fejlődéshez, a magyar államfejlődés is a nyugati intézmények és a keleti periférikus adottságok közötti feszültségben formálódott`.",
            "gr_table": [
                ["Miként a Rajna völgye a nyugati szabadságjogok bölcsője, akként vált a Vltava és a Duna a köztes régió tengelyévé.", "Just as the Rhine valley was the cradle of western liberties, so the Vltava and the Danube became the axis of the intermediate region."],
                ["Amiképpen Szűcs Jenő megfogalmazta, a térség sorsát a kettős orientáció határozta meg.", "In the manner that Jenő Szűcs formulated it, the destiny of the region was determined by dual orientation."],
                ["Hasonlatosképpen a reneszánsz városi autonómiákhoz, a térség polgárosodása is a jogállamiság fundamentuma volt.", "In similar fashion to renaissance municipal autonomies, the region's embourgeoisement was also the fundament of the rule of law."]
            ],
            "classic_story": {
                "slug": "c1-17-szucs",
                "author": "Szűcs Jenő",
                "work": "Vázlat Európa három történeti régiójáról (1980)",
                "title": "Európa három régiója és a közép-európai sors",
                "summary": "Jenő Szűcs's groundbreaking 1980 historical treatise defining Central Europe (Zwischeneuropa) as a distinct historical-structural region straddling Western feudal liberties and Eastern imperial state dominance.",
                "characters": ["Szűcs Jenő"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Szűcs Jenő a Bibó-emlékkönyv számára 1980-ban megírta 'Vázlat Európa három történeti régiójáról' című esszéjét, a huszadik század legmeghatározóbb közép-európai történetfilozófiai művét alkotta meg. Szűcs nem politikai deklarációt tett, hanem ezer év mélystruktúráit tárta fel: a feudalizmus, a jogintézmények, a társadalmi autonómiák és a városiasodás mintázatait vizsgálva bizonyította be, hogy Európa nem osztható egyszerűen 'keletre' és 'nyugatra'."},
                    {"type": "narration", "text": "Tézise szerint Európa a kora középkor óta három eltérő fejlődési pályát járt be. A Nyugat – az egykori Karoling birodalom örököse – a hatalom megosztására, a társadalom államtól való autonómiájára és a szerződéses hűbériségre alapozta civilizációját. Ezzel szemben Kelet-Európa – a bizánci és cári orosz modell – a cári autokrácia, a társadalom állam általi teljes alávetése és a corporatív szabadságjogok hiánya felé mozdult el."},
                    {"type": "narration", "text": "És hol áll a harmadik régió: Közép-Európa, a lengyelek, csehek és magyarok világa? Szűcs meglátása szerint e térség nem a Kelet része, hanem a Nyugat legkeletibb, strukturálisan labilis peremvidéke. A nyugati kereszténység felvétele, a rendi alkotmányosság, a városi privilégiumok és az egyetemek hálózata mind a nyugati struktúrákat honosította meg; ám a török hódoltság, a Habsburg birodalmi centralizáció és a második jobbágyság újra meg újra a perifériára sodorta a régiót."},
                    {"type": "narration", "text": "Szűcs Jenő figyelmeztetése ma, a visegrádi együttműködés korszakában ismét elevenné vált. Arra emlékeztet, hogy Közép-Európa történelmi hivatása nem a két világ közötti ingadozásban vagy az illiberális önfeladásban rejlik, hanem a mélyben szunnyadó nyugati társadalmi autonómiák, a jog uralma és a polgári szabadság védelmében. E régió csak akkor maradhat önmaga, ha nem feledi el ezeréves kötődését az európai szabadsághagyományhoz."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi Szűcs Jenő híres modelljének lényege a három európai történeti régióról?", [
                    "Hogy a Nyugat (társadalmi autonómiák, hatalommegosztás) és a Kelet (cári autokrácia, állami túlsúly) között létezik egy harmadik, önálló Közép-Európa, amely strukturálisan a Nyugathoz kötődik, de történelmileg sérülékeny periféria maradt.",
                    "Hogy Európában csak a sarki jégmezők és a sivatagok számítanak régiónak.",
                    "Hogy Magyarország földrajzilag Ázsiához tartozik."
                ], 0, ["c1-17-vocab"]),
                fb("grammar", "controlled", "_____ (Just as / Miként) a nyugati polgárság kiharcolta szabadságjogait, akként formálódtak a közép-európai városok önkormányzatai is.", "Miként", "Just as the western bourgeoisie fought for its liberties, so the self-governments of Central European towns were formed as well.", ["c1-adv-manner-comparative-similes"]),
                match("vocabulary", "controlled", [["történeti régió", "hosszú távú társadalmi struktúrák területe"], ["rendi alkotmányosság", "nemesi és polgári privilégiumok fékje a királyi hatalmon"], ["autokrácia", "korlátlan cári vagy császári egyeduralom"], ["társadalmi autonómia", "államtól független önszerveződés"]], ["c1-17-vocab"]),
                mc("reading", "practice", "Miért tekinti Szűcs Jenő Közép-Európát a 'Nyugat peremvidékének' ahelyett, hogy Keletnek tekintené?", [
                    "Mert a térség átvette a nyugati kereszténységet, a gótikát, a reneszánszt, a rendiséget és az egyetemek rendszerét, még ha a fejlődés meg-megakadt is.",
                    "Mert a térségben mindenki latinul beszél manapság is.",
                    "Mert nincsenek folyók a térségben."
                ], 0, None),
                sb("grammar", "practice", ["Közép-Európa", "történelmi", "hivatása", "a", "nyugati", "jogállami", "értékek", "hűséges", "őrzése."], ["Közép-Európa", "történelmi", "hivatása", "a", "nyugati", "jogállami", "értékek", "hűséges", "őrzése."], "Central Europe's historical calling is the faithful guarding of western rule-of-law values.", ["c1-adv-manner-comparative-similes"]),
                sw("production", [{"prompt": "Synthesize Jenő Szűcs's thesis on Central Europe using an analogical simile.", "answer": "Miként Szűcs Jenő zseniális történeti elemzése rávilágított, Közép-Európa sorsát akként határozza meg a nyugati társadalmi autonómiák iránti vágy és a keleti autokratikus kísértések örökös küzdelme."}], ["c1-adv-manner-comparative-similes"]),
                mc("grammar", "check", "Melyik kötőszó fejez ki emelkedett összehasonlító-hasonlító viszonyt?", [
                    "miként... akként / amiképpen",
                    "holott",
                    "noha"
                ], 0, ["c1-adv-manner-comparative-similes"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(17, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        17,
        "core",
        "c1-17-consolidation",
        core_title,
        [
            "I can analyze regional geopolitics, diplomatic protocol, and realism.",
            "I can employ diplomatic conditional hedging, locative correlatives, and genitive chains.",
            "I can evaluate Jenő Szűcs's 'Three Historical Regions of Europe' and Central European identity."
        ],
        [
            mc("grammar", "recognize", "Milyen szerepet töltenek be a diplomáciai óvatosságot kifejező modális feltételes szerkezetek?", [
                "Tompítják a kategorikus kijelentéseket és fenntartják a rugalmas tárgyalási mozgásteret.",
                "Kizárólag a szerződések dátumát jelölik.",
                "Megtiltják a külföldi utazást."
            ], 0, ["c1-diplomatic-hedging-conditional"]),
            mc("grammar", "recognize", "Mit fejez ki a 'mielőtt még... volna' temporalitás az események leírásában?", [
                "Olyan előidejűséget, amelyben egy esemény megelőz egy várható vagy tervezett történést.",
                "Egyidejű cselekvést a jelenben.",
                "A jövőbeni parancsot."
            ], 0, ["c1-adv-temporal-successive-aspect"]),
            match("vocabulary", "recognize", [["reálpolitika", "gyakorlati hatalmi érdekpolitika"], ["ütközőzóna", "szembenálló felek közötti térség"], ["kollektív védelem", "támadás esetén közös katonai fellépés"], ["eszkaláció", "feszültség fokozatos növekedése"], ["történeti régió", "hosszú távú civilizációs tér"]], ["c1-17-vocab"]),
            fb("vocabulary", "recall", "A tárgyalások megfeneklettek, így a felek közötti diplomáciai _____ egyelőre megszakadt. (maneuvering room / mozgástér)", "mozgástér", "Negotiations foundered, thus the diplomatic maneuvering room between the parties was temporarily severed.", ["c1-17-vocab"]),
            fb("vocabulary", "recall", "Szűcs szerint Közép-Európa lényege a rendi alkotmányosság és a társadalmi _____ korai megerősödése. (autonomy / autonómiák)", "autonómiák", "According to Szűcs, the essence of Central Europe is the early strengthening of estate constitutionalism and societal autonomies.", ["c1-17-vocab"]),
            fb("grammar", "recall", "Úgy _____ (we might consider / vélhetnénk), hogy a válság békés rendezése mindkét szövetség érdeke.", "vélhetnénk", "We might consider that the peaceful settlement of the crisis is in the interest of both alliances.", ["c1-diplomatic-hedging-conditional"]),
            fb("grammar", "context", "Ott, ahol a nagyhatalmi zónák összeérnek, a szuverenitás _____ törékeny egyensúlyon nyugszik. (just as well / éppúgy)", "éppúgy", "There where great-power zones meet, sovereignty just as well rests upon a fragile equilibrium.", ["c1-complex-locative-correlatives"]),
            fb("grammar", "context", "Mielőtt még a békekonferencia véget ért _____, újabb csapatokat vezényeltek a határra. (would have / volna)", "volna", "Even before the peace conference would have ended, new troops were deployed to the border.", ["c1-adv-temporal-successive-aspect"]),
            mc("grammar", "context", "Mi a lényege a 'Miként... akként' analógiás hasonlatnak Szűcs Jenő szövegében?", [
                "Párhuzamot von a nyugat-európai intézményfejlődés és a közép-európai mintázatok között, kiemelve a strukturális rokonságot.",
                "Kijelenti, hogy nincs semmilyen kapcsolat az országok között.",
                "Időjárási adatokat vet össze."
            ], 0, ["c1-adv-manner-comparative-similes"]),
            sb("grammar", "produce", ["A", "kollektív", "biztonság", "a", "nemzetközi", "stabilitás", "legfontosabb", "záloga."], ["A", "kollektív", "biztonság", "a", "nemzetközi", "stabilitás", "legfontosabb", "záloga."], "Collective security is the most important pledge of international stability.", ["c1-nominal-compound-geopolitical-syntax"]),
            sw("production", [{"prompt": "Write a critical diplomatic evaluation of small-state security alliances.", "answer": "Úgy vélhetnénk, hogy a kisállamok számára a kollektív védelmi szövetségek jelentik az egyetlen hiteles elrettentési garanciát a nagyhatalmi érdekszférák expanziójával szemben."}], ["c1-diplomatic-hedging-conditional"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Central Europe's European calling.", "answer": "Miként Szűcs Jenő tanította, Közép-Európa nem a civilizációs senkiföldje, hanem a nyugati jogi autonómiák és a szabadsághagyomány elválaszthatatlan bástyája a kontinens szívében."}], ["c1-adv-manner-comparative-similes"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-visegrad)
    # ----------------------------------------------------
    disc_title = "The Visegrád Group (V4), Regional Alliances & European Cohesion"
    slug = "visegrad"

    disc_intro = [
        "The Visegrád Group (Hungary, Poland, Czechia, Slovakia) embodies Central Europe's quest for regional weight, infrastructure integration, and diplomatic leverage within the European Union.",
        "Through serialized case studies spanning the 1335 royal summit, post-communist re-emergence (1991), North-South energy and transport corridors (Via Carpatia), geopolitical divergence over Russia and Ukraine, and the Three Seas Initiative, you will master advanced diplomatic discourse in C1 Hungarian."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Historical Rebirth: 1335 Royal Summit to 1991 Visegrád Declaration",
            "grammar_title": "Discourse Markers of Geopolitical Divergence and Diplomatic Disagreement",
            "grammar_skill": "c1-discourse-divergence-markers",
            "goals": [
                "I can analyze the Visegrád cooperation origins: 1335 royal summit and the 1991 declaration (*visegrádi királytalálkozó, Havel, Antall, Wałęsa, euroatlanti integráció*).",
                "I can deploy discourse markers of divergence and disagreement (*éles cezúrát képez, kibékíthetetlen ellentét feszül, homlokegyenest ellenkező, törést okoz*).",
                "I can evaluate post-communist Central European solidarity and transition diplomacy in Hungarian."
            ],
            "vocab": [
                {"lemma": "visegrádi együttműködés", "translation": "Visegrád cooperation (V4)", "pos": "expression"},
                {"lemma": "királytalálkozó", "translation": "royal summit (1335 meeting of Károly Róbert, John of Bohemia, Casimir the Great)", "pos": "noun"},
                {"lemma": "euroatlanti integráció", "translation": "Euro-Atlantic integration (NATO and EU accession)", "pos": "expression"},
                {"lemma": "rendszerváltó diplomácia", "translation": "post-communist transition diplomacy", "pos": "expression"},
                {"lemma": "történelmi szolidaritás", "translation": "historical solidarity", "pos": "expression"},
                {"lemma": "közös fellépés", "translation": "joint diplomatic action", "pos": "expression"},
                {"lemma": "érdekazonosság", "translation": "identity of interests / alignment", "pos": "noun"},
                {"lemma": "disszonancia", "translation": "dissonance, diplomatic friction", "pos": "noun"}
            ],
            "gr_text1": "Discourse markers of divergence (*éles cezúrát képez* [forms a sharp break], *kibékíthetetlen ellentét feszül* [an irreconcilable contradiction tensions], *homlokegyenest ellenkező álláspontot képvisel* [represents a diametrically opposed position]) dissect diplomatic fissures.",
            "gr_text2": "Example in V4 historical analysis: `Míg 1991-ben az euroatlanti integráció célja még teljes érdekazonosságot teremtett Budapest, Prága és Varsó között, addig az évtizedek során felszínre kerülő szuverenitási viták éles cezúrát képeztek a tagállamok jövőképében`.",
            "gr_table": [
                ["A háború megítélése körül kibékíthetetlen ellentét feszül Varsó és Budapest között.", "An irreconcilable contradiction tensions between Warsaw and Budapest surrounding judgment of the war."],
                ["A két kormányfő homlokegyenest ellenkező álláspontot foglalt el az uniós integráció mélyítéséről.", "The two prime ministers took diametrically opposed stances on deepening EU integration."],
                ["Ez a diplomáciai nézeteltérés éles cezúrát képez a visegrádi négyek korábbi egységében.", "This diplomatic dispute forms a sharp break in the former unity of the Visegrád Four."]
            ],
            "world_story_seg": {
                "seg_slug": "tortenet",
                "title": "A Duna-kanyar szelleme: 1335-től a demokratikus V4 megszületéséig",
                "summary": "How Károly Róbert, Casimir the Great, and John of Bohemia bypassed Vienna in 1335, and how Havel, Antall, and Wałęsa revived Visegrád in 1991 to dismantle the Warsaw Pact.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 1335 őszén a visegrádi királyi palotában Károly Róbert magyar király vendégül látta Nagy Kázmér lengyel királyt és Luxemburgi János cseh uralkodót, a középkori Európa egyik legsikeresebb gazdasági és béketeremtő csúcstalálkozója zajlott le. A három uralkodó új kereskedelmi útvonalakat nyitott, kikerülve a bécsi árumegállító jog fojtogató monopóliumát, és szövetségi egyességet kötött a térség békéjének garantálására."},
                    {"type": "narration", "text": "Öt és fél évszázaddal később, 1991 februárjában e történelmi helyszín szimbolikus bölcsőjévé vált a rendszerváltó Közép-Európa feltámadásának. Václav Havel csehszlovák köztársasági elnök, Antall József magyar miniszterelnök és Lech Wałęsa lengyel államfő aláírták a Visegrádi Nyilatkozatot. Céljuk a szovjet megszállási struktúrák – a Varsói Szerződés és a KGST – gyors felszámolása, a határok békés megnyitása és a közös euroatlanti integráció kiharcolása volt: visszavezetve Közép-Európát a nyugati nemzetek családjába."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt az 1991-es Visegrádi Nyilatkozat legfőbb célkitűzése?", [
                    "A szovjet dominancia felszámolása, a térségi együttműködés megerősítése és a közös euroatlanti (NATO, EU) csatlakozás kiharcolása.",
                    "Egy új közép-európai királyság alapítása.",
                    "A Duna teljes lezárása a hajózás elől."
                ], 0, ["c1-visegrad-vocab"]),
                fb("grammar", "controlled", "A jelenlegi geopolitikai kérdésekben _____ ellentét feszül (irreconcilable / kibékíthetetlen) a szövetség egyes tagjai között.", "kibékíthetetlen", "In current geopolitical questions, an irreconcilable contradiction tensions between certain members of the alliance.", ["c1-discourse-divergence-markers"]),
                match("vocabulary", "controlled", [["1335-ös királytalálkozó", "középkori gazdasági csúcs Visegrádon"], ["Visegrádi Nyilatkozat", "1991-es rendszerváltó alapító dokumentum"], ["euroatlanti integráció", "NATO és EU tagság elérése"], ["érdekazonosság", "közös külpolitikai célok egybeesése"]], ["c1-visegrad-vocab"]),
                fb("grammar", "practice", "A biztonságpolitikai irányvonalak megváltozása éles _____ képez a V4 történetében. (break / cezúrát)", "cezúrát", "The alteration of security policy directions forms a sharp break in the history of the V4.", ["c1-discourse-divergence-markers"]),
                sb("grammar", "practice", ["A", "visegrádi", "együttműködés", "történelmi", "sikere", "a", "közös", "euroatlanti", "integrációban", "csúcsosodott", "ki."], ["A", "visegrádi", "együttműködés", "történelmi", "sikere", "a", "közös", "euroatlanti", "integrációban", "csúcsosodott", "ki."], "The historical success of Visegrád cooperation peaked in joint Euro-Atlantic integration.", ["c1-discourse-divergence-markers"]),
                dc("dialogue", [
                    {"speaker": "Diplomáciatörténész", "text": "Mi tette lehetővé a V4 sikerét a kilencvenes években?"},
                    {"speaker": "Külügyi szakértő", "text": "Az a ritka történelmi pillanat, amikor a térség országai között teljes volt az _____."},
                ], ["érdekazonosság", "ellenségeskedés", "elszigetelődés"], 0, ["c1-discourse-divergence-markers"]),
                sw("production", [{"prompt": "Write a sentence using a divergence marker to analyze current V4 foreign policy.", "answer": "Míg a csatlakozási tárgyalások idején teljes egység jellemezte a négy fővárost, addig napjainkban homlokegyenest ellenkező álláspontot képviselnek az európai stratégiai szuverenitás kérdésében."}], ["c1-discourse-divergence-markers"]),
                mc("grammar", "check", "Melyik kifejezés jelöli a politikai/diplomáciai véleménykülönbség éles megjelenését?", [
                    "homlokegyenest ellenkező álláspont / éles cezúra",
                    "teljes és oszthatatlan harmónia",
                    "egyhangú egyetértés"
                ], 0, ["c1-discourse-divergence-markers"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "North-South Connectivity, Energy Corridors & Via Carpatia",
            "grammar_title": "Concessive Stipulative Clauses Defining Treaty Conditions and Reservations",
            "grammar_skill": "c1-concessive-stipulative-clauses",
            "goals": [
                "I can analyze North-South transport and energy corridors (*Via Carpatia, LNG-interkonnektorok, észak-déli folyosó*).",
                "I can construct concessive stipulative clauses (*azzal a megkötéssel hogy, feltéve mindazonáltal hogy, azzal a fenntartással élve*).",
                "I can evaluate regional infrastructure investments overcoming historical East-West pipeline dependencies."
            ],
            "vocab": [
                {"lemma": "észak-déli folyosó", "translation": "North-South corridor", "pos": "expression"},
                {"lemma": "Via Carpatia", "translation": "Via Carpatia (trans-European transport route from Baltic to Aegean)", "pos": "noun"},
                {"lemma": "interkonnektor", "translation": "gas/electricity interconnector", "pos": "noun"},
                {"lemma": "LNG-terminál", "translation": "LNG terminal (Świnoujście, Krk)", "pos": "noun"},
                {"lemma": "hálózatfejlesztés", "translation": "grid development", "pos": "noun"},
                {"lemma": "energetikai diverzifikáció", "translation": "energy diversification", "pos": "expression"},
                {"lemma": "tranzitútvonal", "translation": "transit route", "pos": "noun"},
                {"lemma": "infrastrukturális kohézió", "translation": "infrastructural cohesion", "pos": "expression"}
            ],
            "gr_text1": "Concessive stipulative clauses formulate diplomatic reservations and treaty conditions: `azzal a megkötéssel, hogy...` (with the stipulation that...), `feltéve mindazonáltal, hogy...` (provided however that...), and `azzal a fenntartással, hogy...` (with the reservation that...).",
            "gr_text2": "Example in infrastructure diplomacy: `A kormány hozzájárult a közös gázvezeték finanszírozásához, azzal a kifejezett megkötéssel, hogy a szállítási kapacitások elosztása nem veszélyezteti a hazai ellátásbiztonságot`.",
            "gr_table": [
                ["A felek megállapodtak az autópálya-építésben, azzal a megkötéssel, hogy a költségeket egyenlő arányban viselik.", "The parties agreed on highway construction, with the stipulation that they bear costs in equal proportions."],
                ["Támogatják a projektet, feltéve mindazonáltal, hogy az uniós környezetvédelmi normák maradéktalanul teljesülnek.", "They support the project, provided however that EU environmental norms are fully met."],
                ["Aláírták a szándéknyilatkozatot, azzal a fenntartással, hogy a parlamentek ratifikálják a végleges szerződést.", "They signed the letter of intent, with the reservation that parliaments ratify the final treaty."]
            ],
            "world_story_seg": {
                "seg_slug": "infrastruktura",
                "title": "A Balti-tengertől az Adriáig: Észak-déli tengely és energiabiztonság",
                "summary": "How Central Europe breaks free from Soviet-era East-West pipeline dependencies by building North-South interconnectors, the Via Carpatia expressway, and LNG linkages.",
                "paragraphs": [
                    {"type": "narration", "text": "A hidegháború évtizedei alatt Közép-Európa infrastruktúráját egyoldalúan Moszkva felé hangolták: a kőolaj- és földgázvezetékek, valamint a főbb vasúti nyomvonalak mind kelet-nyugati irányban szelték át a térséget, miközben az észak-déli kapcsolatok szinte teljesen hiányoztak. A V4 tagállamai hamar felismerték, hogy a valódi függetlenség feltétele a tengelyek megfordítása."},
                    {"type": "narration", "text": "A Klaipėda, Świnoujście és a horvát Krk szigetén létesült LNG-terminálok közötti kétirányú interkonnektorok kiépítése megtörte az orosz gázmonopóliumot. Ezzel párhuzamosan a Via Carpatia autópálya-folyosó a Balti-tenger partjától Kassa, Miskolc és Debrecen érintésével köti össze a régió gazdasági vérkeringését. Az észak-déli infrastrukturális integráció a visegrádi gazdasági szuverenitás legkézzelfoghatóbb bizonyítéka."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a stratégiai célja az észak-déli energiainterkonnektorok kiépítésének a V4 térségében?", [
                    "A szovjet örökségből származó egyoldalú kelet-nyugati energiafüggőség felszámolása és a források diverzifikációja a Balti- és az Adriai-tenger felől.",
                    "A vasúti sínek leszerelése.",
                    "Minden nemzetközi kereskedelem leállítása."
                ], 0, ["c1-visegrad-vocab"]),
                fb("grammar", "controlled", "A tagállamok elfogadták a beruházási tervet, azzal a _____ (stipulation / megkötéssel), hogy az uniós társfinanszírozás biztosított marad.", "megkötéssel", "The member states accepted the investment plan, with the stipulation that EU co-financing remains secured.", ["c1-concessive-stipulative-clauses"]),
                match("vocabulary", "controlled", [["Via Carpatia", "észak-déli autópálya-folyosó"], ["interkonnektor", "kétirányú gáz- vagy áramvezeték"], ["LNG-terminál", "cseppfolyósított földgáz fogadóállomás"], ["energetikai diverzifikáció", "több beszállítótól való vásárlás"]], ["c1-visegrad-vocab"]),
                fb("grammar", "practice", "Támogatjuk az új tranzitútvonal kijelölését, feltéve _____ hogy a környezeti hatástanulmányok kedvezőek lesznek. (however / mindazonáltal)", "mindazonáltal", "We support designating the new transit route, provided however that environmental impact assessments are favorable.", ["c1-concessive-stipulative-clauses"]),
                sb("grammar", "practice", ["Az", "észak-déli", "infrastruktúra", "megteremti", "Közép-Európa", "valódi", "gazdasági", "összekapcsoltságát."], ["Az", "észak-déli", "infrastruktúra", "megteremti", "Közép-Európa", "valódi", "gazdasági", "összekapcsoltságát."], "North-South infrastructure creates Central Europe's genuine economic interconnectedness.", ["c1-concessive-stipulative-clauses"]),
                dc("dialogue", [
                    {"speaker": "Közlekedési szakértő", "text": "Mikorra készülhet el a Via Carpatia teljes nyomvonala?"},
                    {"speaker": "Infrastrukturális biztos", "text": "A magyar szakaszok készen állnak, de a határokon átnyúló csatlakozások még összehangolt _____ igényelnek."},
                ], ["beruházásokat", "vitákat", "leállásokat"], 0, ["c1-concessive-stipulative-clauses"]),
                sw("production", [{"prompt": "Write a stipulative sentence outlining conditions for regional energy sharing.", "answer": "A felek megállapodtak a vésztartalék-kapacitások kölcsönös megosztásáról, azzal a kifejezett megkötéssel, hogy válsághelyzetben a hazai fogyasztók ellátása abszolút prioritást élvez."}], ["c1-concessive-stipulative-clauses"]),
                mc("grammar", "check", "Melyik fordulat fejez ki diplomáciai feltételt és fenntartást?", [
                    "azzal a megkötéssel, hogy / feltéve mindazonáltal",
                    "miután kiderült, hogy",
                    "mivel köztudomású, hogy"
                ], 0, ["c1-concessive-stipulative-clauses"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Geopolitical Divergence: Ukraine, Russia & The Fracturing of the V4",
            "grammar_title": "Rhetorical Antithetical Parallelism in International Relations Analysis",
            "grammar_skill": "c1-rhetorical-antithetical-parallelism",
            "goals": [
                "I can analyze geopolitical fractures in the V4 over Russia, Ukraine, and EU integration (*geopolitikai törés, V4-széttartás, orosz agresszió, szankciós politika*).",
                "I can employ rhetorical antithetical parallelism (*Míg Varsó a szövetség kiterjesztésében látja a zálogot, addig Budapest a pragmatikus kapcsolatok fenntartásában*).",
                "I can evaluate diverging strategic cultures in Poland, the Czech Republic, Slovakia, and Hungary."
            ],
            "vocab": [
                {"lemma": "geopolitikai törésvonal", "translation": "geopolitical fault line", "pos": "expression"},
                {"lemma": "szövetségi divergencia", "translation": "alliance divergence / fracturing", "pos": "expression"},
                {"lemma": "stratégiai kultúra", "translation": "strategic culture", "pos": "expression"},
                {"lemma": "szankciós politika", "translation": "sanctions policy", "pos": "expression"},
                {"lemma": "orosz energiafüggőség", "translation": "Russian energy dependence", "pos": "expression"},
                {"lemma": "fegyverszállítás", "translation": "arms supply / military aid", "pos": "noun"},
                {"lemma": "külpolitikai elszigetelődés", "translation": "foreign policy isolation", "pos": "expression"},
                {"lemma": "szuverenitásfelfogás", "translation": "concept of sovereignty", "pos": "noun"}
            ],
            "gr_text1": "Rhetorical antithetical parallelism contrasts diverging foreign policy positions using balanced syntactical structures (*Míg X állam..., addig Y állam...*; *Egyfelől... másfelől...*): `Míg Varsó és Prága az ukrajnai katonai segélyezést egzisztenciális biztonsági kötelességnek tekinti, addig Budapest a fegyverszállítások elutasításával a konfliktusból való kimaradást hirdeti`.",
            "gr_text2": "This balanced syntax highlights systemic ideological divergences without polemical bias.",
            "gr_table": [
                ["Míg Lengyelország a transzatlanti szövetség radikális megerősítését sürgeti, addig Magyarország a keleti nyitás gazdasági kapcsolatait védi.", "While Poland urges radical strengthening of the transatlantic alliance, Hungary defends economic ties of Eastern Opening."],
                ["Míg a cseh vezetés a közös európai fellépésben bízik, addig a szlovák és magyar politika gyakran nemzeti különutakat keres.", "While the Czech leadership trusts in joint European action, Slovak and Hungarian politics often seek separate national paths."],
                ["Egyfelől közös a közép-európai történeti sorsközösség, másfelől kibékíthetetlennek tűnik a háborúhoz való stratégiai viszonyulás.", "On one hand the Central European historical community of destiny is shared; on the other hand the strategic stance toward the war seems irreconcilable."]
            ],
            "world_story_seg": {
                "seg_slug": "divergencia",
                "title": "A visegrádi próbatétel: Háború, szankciók és a politikai széttartás",
                "summary": "How the 2022 Russian invasion of Ukraine exposed deep strategic differences between Poland's existential defense stance and Hungary's transactional energy pragmatism.",
                "paragraphs": [
                    {"type": "narration", "text": "2022. február 24-e nem csupán az európai biztonsági architektúrát rázta meg alapjaiban: a visegrádi négyek több mint három évtizedes szövetségére is a legsúlyosabb csapást mérte. Bár a V4 korábban sikeresen lépett fel egységfrontként a migrációs kvótákkal vagy az uniós költségvetéssel kapcsolatos vitákban, az orosz agresszió megítélésében a felszínre törtek az elfedett stratégiai ellentétek."},
                    {"type": "narration", "text": "Varsó és Prága számára az orosz imperializmus megállítása a nemzeti túlélés kérdésévé vált, amely feltétlen katonai és humanitárius segítséget követel Ukrajnának. Ezzel szemben Budapest az orosz energiafüggőségre és a kárpátaljai magyarság védelmére hivatkozva elutasította a fegyverszállításokat és bírálta a szankciókat. A visegrádi csúcstalálkozók feszült hangulata és az együttműködés megdermedése rávilágított: közös biztonságpolitikai vízió nélkül a regionális szövetség működésképtelenné válik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi okozta a legsúlyosabb belső törést a Visegrádi Négyek (V4) között 2022 után?", [
                    "Az ukrajnai háború, az orosz agresszió, a fegyverszállítások és a szankciós politika megítélésében kialakult mély stratégiai ellentét.",
                    "A közös pénznem bevezetésének időpontja.",
                    "A nemzeti labdarúgó-bajnokságok összevonásának terve."
                ], 0, ["c1-visegrad-vocab"]),
                fb("grammar", "controlled", "Míg Varsó a szankciók szigorítását követeli, _____ (meanwhile / addig) Budapest a pragmatikus gazdasági kapcsolatok megőrzése mellett érvel.", "addig", "While Warsaw demands tightening sanctions, meanwhile Budapest argues for preserving pragmatic economic ties.", ["c1-rhetorical-antithetical-parallelism"]),
                match("vocabulary", "controlled", [["szövetségi divergencia", "tagállamok politikai széttartása"], ["orosz energiafüggőség", "kiszolgáltatottság a keleti nyersanyagoknak"], ["fegyverszállítás", "katonai segélyezés háborús zónába"], ["külpolitikai elszigetelődés", "szövetségesek elvesztésének veszélye"]], ["c1-visegrad-vocab"]),
                fb("grammar", "practice", "Egyfelől adott a közös földrajzi térség, másfelől _____ (on the other hand / viszont) teljesen eltér a stratégiai fenyegetésérzet.", "viszont", "On one hand the common geographic space is given; on the other hand however the strategic threat perception differs completely.", ["c1-rhetorical-antithetical-parallelism"]),
                sb("grammar", "practice", ["A", "stratégiai", "kultúrák", "különbözősége", "megnehezíti", "a", "közös", "közép-európai", "fellépést."], ["A", "stratégiai", "kultúrák", "különbözősége", "megnehezíti", "a", "közös", "közép-európai", "fellépést."], "The diversity of strategic cultures hinders joint Central European action.", ["c1-rhetorical-antithetical-parallelism"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Túlélheti-e a V4 a jelenlegi geopolitikai krízist?"},
                    {"speaker": "Külügyi szakértő", "text": "Csak akkor, ha a magas szintű politikai viták helyett a gyakorlati infrastrukturális és gazdasági _____ helyezik a hangsúlyt."},
                ], ["együttműködésre", "támadásokra", "szankciókra"], 0, ["c1-rhetorical-antithetical-parallelism"]),
                sw("production", [{"prompt": "Write an antithetical parallel sentence analyzing Polish and Hungarian foreign policy stances.", "answer": "Míg Lengyelország az orosz imperializmus elleni transzatlanti szövetség élharcosaként lép fel, addig Magyarország az energiaellátás védelmére hivatkozva a gazdasági kapcsolatok fenntartását részesíti előnyben."}], ["c1-rhetorical-antithetical-parallelism"]),
                mc("grammar", "check", "Melyik mondat alkalmaz retorikai antitetikus párhuzamot külpolitikai elemzésben?", [
                    "Míg az egyik fél a kollektív szolidaritást hangsúlyozza, addig a másik fél a nemzeti szuverenitást tekinti abszolút mérőnek.",
                    "Az egyik fél és a másik fél megállapodtak a közös nyilatkozatról tegnap este.",
                    "Minden tagállam ugyanazt a stratégiát követte a tanácskozáson."
                ], 0, ["c1-rhetorical-antithetical-parallelism"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Cohesion Funds, EU Budget Bargaining & The Three Seas Initiative",
            "grammar_title": "Deontic Treaty Predicates Expressing Pact Obligations and Diplomatic Mandates",
            "grammar_skill": "c1-modal-deontic-treaty-predicates",
            "goals": [
                "I can analyze EU cohesion policy, multi-annual financial framework (MFF) bargaining, and the Three Seas Initiative (*kohéziós alapok, MFF tárgyalások, Három Tenger Kezdeményezés*).",
                "I can deploy deontic treaty predicates of diplomatic obligation (*köteles tiszteletben tartani, vállalja hogy, kötelezettséget ró a felekre, hatáskörében eljárva biztosítja*).",
                "I can debate the balance between European solidarity, net contributions, and national budget autonomy."
            ],
            "vocab": [
                {"lemma": "kohéziós politika", "translation": "cohesion policy", "pos": "expression"},
                {"lemma": "többéves pénzügyi keret", "translation": "multiannual financial framework (MFF)", "pos": "expression"},
                {"lemma": "Három Tenger Kezdeményezés", "translation": "Three Seas Initiative (3SI)", "pos": "expression"},
                {"lemma": "nettó haszonélvező", "translation": "net beneficiary", "pos": "expression"},
                {"lemma": "felzárkózási támogatás", "translation": "catch-up / development funding", "pos": "expression"},
                {"lemma": "költségvetési alkufolyamat", "translation": "budget bargaining process", "pos": "expression"},
                {"lemma": "jogállamisági kondicionalitás", "translation": "rule of law conditionality", "pos": "expression"},
                {"lemma": "regionális érdekérvényesítés", "translation": "regional advocacy / interest representation", "pos": "expression"}
            ],
            "gr_text1": "Deontic treaty predicates (*köteles tiszteletben tartani* [is obliged to respect], *vállalja, hogy szavatolja* [undertakes to guarantee], *kötelezettséget ró a tagállamokra* [imposes an obligation on member states], *kötelességévé teszi* [makes it its duty]) define legal requirements in multilateral pacts.",
            "gr_text2": "Example in EU funds governance: `A tagállamok a partnerségi megállapodás értelmében kötelesek tiszteletben tartani a pénzügyi átláthatóság elvét, és vállalják, hogy a kohéziós források elosztása során kizárják a korrupció és az összeférhetetlenség kockázatát`.",
            "gr_table": [
                ["A támogatási szerződés értelmében a kedvezményezett köteles elszámolni minden egyes eurócenttel.", "Pursuant to the grant agreement, the beneficiary is obliged to account for every single euro-cent."],
                ["A felek kötelezettséget vállalnak arra, hogy az infrastrukturális beruházásokat határidőre befejezik.", "The parties undertake the commitment that they will complete infrastructural investments on schedule."],
                ["Az uniós szabályozás szigorú felügyeleti kötelezettséget ró a nemzeti ellenőrző hatóságokra.", "EU regulation imposes a strict oversight obligation on national audit authorities."]
            ],
            "world_story_seg": {
                "seg_slug": "kohezio",
                "title": "A felzárkózás mérlege: Kohézió, brüsszeli alku és a Három Tenger Kezdeményezés",
                "summary": "How Central European states leveraged EU cohesion funding to modernize their infrastructure, and why the Three Seas Initiative created a twelve-nation platform between the Baltic, Black, and Adriatic Seas.",
                "paragraphs": [
                    {"type": "narration", "text": "Az Európai Unióhoz való 2004-es csatlakozás óta a kohéziós alapok a közép-európai gazdasági felzárkózás motorjává váltak. Autópályák, vasúti fővonalak, szennyvíztisztítók és kutatóközpontok ezrei épültek fel a brüsszeli támogatásokból, modernizálva a V4 országainak elhanyagolt infrastruktúráját."},
                    {"type": "narration", "text": "A költségvetési tárgyalások során a visegrádiak gyakran sikeresen léptek fel a kohéziós források megvédése érdekében. E regionális logikát emelte magasabb szintre a 2015-ben elindított Három Tenger Kezdeményezés (3SI), amely a Balti-, az Égei- és a Fekete-tenger közötti tizenkét uniós tagállamot tömöríti. Célja az észak-déli digitális, energetikai és közlekedési folyosók magántőke bevonásával történő gyors kiépítése, biztosítva a térség geopolitikai ellenállóképességét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a célja a Három Tenger Kezdeményezésnek (Three Seas Initiative)?", [
                    "A Balti-, az Adriai- és a Fekete-tenger közötti 12 uniós tagállam észak-déli energetikai, közlekedési és digitális összekapcsolása.",
                    "A tengeri halászat betiltása Európában.",
                    "A tengerpartok mesterséges meghosszabbítása a szárazföld belsejébe."
                ], 0, ["c1-visegrad-vocab"]),
                fb("grammar", "controlled", "A szerződés értelmében minden tagállam köteles _____ tartani (to respect / tiszteletben) a pénzügyi elszámolhatóság normáit.", "tiszteletben", "Pursuant to the treaty every member state is obliged to respect norms of financial accountability.", ["c1-modal-deontic-treaty-predicates"]),
                match("vocabulary", "controlled", [["kohéziós politika", "elmaradott régiók felzárkóztatása"], ["Három Tenger Kezdeményezés", "12 térségi ország infrastruktúra-platformja"], ["MFF", "az EU 7 éves pénzügyi kerete"], ["jogállamisági kondicionalitás", "támogatások jogállami normákhoz kötése"]], ["c1-visegrad-vocab"]),
                fb("grammar", "practice", "A beruházók kötelezettséget _____ arra, hogy az új interkonnektort határidőre átadják. (undertake / vállalnak)", "vállalnak", "Investors undertake the commitment to hand over the new interconnector on schedule.", ["c1-modal-deontic-treaty-predicates"]),
                sb("grammar", "practice", ["A", "kohéziós", "források", "felhasználása", "szigorú", "szabályozási", "kötelezettségeket", "ró", "az", "államra."], ["A", "kohéziós", "források", "felhasználása", "szigorú", "szabályozási", "kötelezettségeket", "ró", "az", "államra."], "The utilization of cohesion funds imposes strict regulatory obligations on the state.", ["c1-modal-deontic-treaty-predicates"]),
                dc("dialogue", [
                    {"speaker": "Tárgyalódelegátus", "text": "Hogyan védhetjük meg a felzárkózási forrásokat a brüsszeli költségvetési vitában?"},
                    {"speaker": "Pénzügyi szakértő", "text": "Közös visegrádi és három-tengeri szövetségben, a beruházások gazdasági megtérülését _____."},
                ], ["bizonyítva", "eltitkolva", "visszavonva"], 0, ["c1-modal-deontic-treaty-predicates"]),
                sw("production", [{"prompt": "Write a deontic treaty sentence outlining obligations under EU cohesion agreements.", "answer": "A támogatási megállapodás értelmében a nemzeti hatóságok kötelesek garantálni a közbeszerzések átláthatóságát, és kifejezett kötelezettséget vállalnak a visszaélések független kivizsgálására."}], ["c1-modal-deontic-treaty-predicates"]),
                mc("grammar", "check", "Melyik állítmány fejez ki szerződéses kötelezettséget jogi kontextusban?", [
                    "köteles tiszteletben tartani / kötelezettséget ró",
                    "esetleg megfontolhatja",
                    "kedve szerint eljárhat"
                ], 0, ["c1-modal-deontic-treaty-predicates"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "The Future of Central Europe: Bridge, Buffer, or Sovereign Core?",
            "grammar_title": "Discourse Summation Particles and Definitive Conclusions in Foreign Policy",
            "grammar_skill": "c1-adv-discourse-summation-particles",
            "goals": [
                "I can analyze Central Europe's strategic future: bridge between civilizational blocs, buffer zone, or sovereign core (*hídszerep, ütközőállam, szuverén mag-régió*).",
                "I can deploy discourse summation particles (*végeredményben, summázva, összességében nézve, mindent egybevetve*).",
                "I can synthesize debates on Central European destiny, federalism versus nation-states, and democratic resilience."
            ],
            "vocab": [
                {"lemma": "hídszerep illúziója", "translation": "illusion of the bridge role", "pos": "expression"},
                {"lemma": "mag-Európa", "translation": "core Europe (core integration)", "pos": "noun"},
                {"lemma": "többsebességes Európa", "translation": "multi-speed Europe", "pos": "expression"},
                {"lemma": "stratégiai autonómia", "translation": "strategic autonomy", "pos": "expression"},
                {"lemma": "közép-európai identitás", "translation": "Central European identity", "pos": "expression"},
                {"lemma": "civilizációs elköteleződés", "translation": "civilizational commitment", "pos": "expression"},
                {"lemma": "geopolitikai realizmus", "translation": "geopolitical realism", "pos": "expression"},
                {"lemma": "összefogás", "translation": "solidarity / joint rallying", "pos": "noun"}
            ],
            "gr_text1": "Discourse summation particles (*végeredményben* [in the final analysis / ultimately], *summázva* [summarizing], *összességében nézve* [looking at it on the whole], *mindent egybevetve* [taking everything together]) draw rigorous overarching conclusions in analytical essays.",
            "gr_text2": "Example in geopolitical synthesis: `Végeredményben a visegrádi együttműködés jövője azon múlik, hogy a tagállamok képesek-e meghaladni a nemzeti partikularizmusokat, és felismerik-e, hogy az európai egységen kívül Közép-Európa elkerülhetetlenül a nagyhatalmak prédájává válik`.",
            "gr_table": [
                ["Végeredményben a híd-koncepció történelmi tévedésnek bizonyult: a hidakon átvonulnak a seregek.", "In the final analysis, the bridge concept proved to be a historical error: armies march across bridges."],
                ["Összességében nézve a V4 fennmaradása a pragmatikus érdekazonosságok mentén lehetséges.", "Looking at it on the whole, the survival of the V4 is possible along pragmatic interest alignments."],
                ["Summázva az elmondottakat: Közép-Európa biztonsága elválaszthatatlan a nyugati szövetségi hűségtől.", "Summarizing what has been said: Central Europe's security is inseparable from western allied loyalty."]
            ],
            "world_story_seg": {
                "seg_slug": "jovo",
                "title": "Híd vagy kompország: Közép-Európa válaszútjai a huszonegyedik században",
                "summary": "Synthesizing the eternal dilemma of Central Europe: Ady's 'ferryland' metaphor, Kundera's 'tragedy of Central Europe', and the imperative of democratic solidarity in an age of geopolitical turbulence.",
                "paragraphs": [
                    {"type": "narration", "text": "Ady Endre híres metaforájában Magyarország 'kompországként' ingázott Kelet és Nyugat partjai között, soha meg nem lelvén a végleges megnyugvást. Milan Kundera pedig a 'Közép-Európa tragédiája' című esszéjében arra figyelmeztetett: e térség nemzeteit kulturálisan mindig is a Nyugat formálta, ám a történelem viharai újra és újra a keleti despociák szorításába lökték őket."},
                    {"type": "narration", "text": "A huszonegyedik században a visegrádi országok válaszúthoz érkeztek. A hídszerep romantikus illúziója szertefoszlott: a geopolitika rideg törvényei szerint a híd nem menedék, hanem átjáróház, amelyen a hódító hadseregek vonulnak át. Végeredményben Közép-Európa egyetlen járható útja az önálló, cselekvőképes szubjektummá válás: amely az európai integráció szerves részeként, szilárd demokratikus intézményekkel és regionális szolidaritással szavatolja a Kárpát-medence és a visegrádi térség ezeréves szabadságát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinti a modern külpolitikai elemzés veszélyes illúziónak a 'hídszerepet' Közép-Európában?", [
                    "Mert a két eltérő civilizációs blokk közötti 'híd' valójában nem biztosít egyensúlyt, hanem ütközőzónává és felvonulási területté teszi a régiót a nagyhatalmak számára.",
                    "Mert a folyami hidak építése túlságosan drága a térségben.",
                    "Mert a hidak nem engedik át a repülőgépeket."
                ], 0, ["c1-visegrad-vocab"]),
                fb("grammar", "controlled", "_____ (In the final analysis / Végeredményben) Közép-Európa nem maradhat meg a két világ közötti semleges zónában.", "Végeredményben", "In the final analysis, Central Europe cannot remain in a neutral zone between two worlds.", ["c1-adv-discourse-summation-particles"]),
                match("vocabulary", "controlled", [["hídszerep illúziója", "veszélyes el nem köteleződési kísérlet"], ["mag-Európa", "legszorosabban integrálódó uniós mag"], ["stratégiai autonómia", "független európai cselekvőképesség"], ["összefogás", "térségi szolidaritás"]], ["c1-visegrad-vocab"]),
                fb("grammar", "practice", "_____ nézve a V4 gazdasági súlya meghaladja a legtöbb nyugati középállamét. (Overall / Összességében)", "Összességében", "Overall, the economic weight of the V4 exceeds that of most western medium-sized states.", ["c1-adv-discourse-summation-particles"]),
                sb("grammar", "practice", ["Közép-Európa", "jövője", "az", "európai", "demokratikus", "szövetség", "megkérdőjelezhetetlen", "része."], ["Közép-Európa", "jövője", "az", "európai", "demokratikus", "szövetség", "megkérdőjelezhetetlen", "része."], "Central Europe's future is an unquestionable part of the European democratic alliance.", ["c1-adv-discourse-summation-particles"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Hogyan oldható fel Ady 'kompország' tragédiája?"},
                    {"speaker": "Történész", "text": "Végleges és egyértelmű nyugati intézményi és kulturális _____ révén."},
                ], ["elköteleződéssel", "lebegéssel", "tagadással"], 0, ["c1-adv-discourse-summation-particles"]),
                sw("production", [{"prompt": "Write a summation sentence about the strategic future of Central Europe.", "answer": "Végeredményben Közép-Európa történelmi stabilitása azon múlik, hogy a térség nemzetei képesek-e feladni a veszélyes hintapolitikát, és elkötelezetten a nyugati jogállami szövetség oszlopaiként fellépni."}], ["c1-adv-discourse-summation-particles"]),
                mc("grammar", "check", "Melyik partikula szolgál végső, összegző következtetés levonására politikai elemzésben?", [
                    "végeredményben / summázva",
                    "eleinte",
                    "kezdetben"
                ], 0, ["c1-adv-discourse-summation-particles"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(17, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A visegrádi horizont: Közép-Európa ezeréves útja és geopolitikai jövője",
            "level": "C1",
            "type": "world",
            "order": 17,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of Central European geopolitics and the Visegrád Group: from the medieval 1335 royal summit and the 1991 democratic renaissance under Havel, Antall, and Wałęsa, North-South transport and LNG energy interconnectors (Via Carpatia), geopolitical fracturing over Russia and Ukraine, cohesion funding dynamics, to the philosophical future of Central European identity within Europe.",
            "grammar": [
                "c1-discourse-divergence-markers",
                "c1-concessive-stipulative-clauses",
                "c1-rhetorical-antithetical-parallelism",
                "c1-modal-deontic-treaty-predicates",
                "c1-adv-discourse-summation-particles"
            ],
            "vocabularyTopics": [
                "The Visegrád Group (V4), Regional Alliances & European Cohesion",
                "Historical Rebirth: 1335 Royal Summit to 1991 Visegrád Declaration",
                "North-South Connectivity, Energy Corridors & Via Carpatia",
                "Geopolitical Divergence: Ukraine, Russia & The Fracturing of the V4",
                "Cohesion Funds, EU Budget Bargaining & The Three Seas Initiative",
                "The Future of Central Europe: Bridge, Buffer, or Sovereign Core?"
            ],
            "paragraphs": [
                {"type": "narration", "text": "Közép-Európa sorsa mindig is a történelem és a földrajz metszéspontjában formálódott. Amikor Károly Róbert 1335-ben Visegrádra hívta a lengyel és cseh uralkodót, egy olyan regionális együttműködés alapjait rakta le, amely felismerte: a Duna, a Vltava és a Visztula mentén élő népek csak közös gazdasági szövetségben védhetik meg szuverenitásukat a birodalmi törekvésekkel szemben."},
                {"type": "narration", "text": "Ezt az ősi felismerést támasztotta fel 1991-ben Václav Havel, Antall József és Lech Wałęsa, amikor a szovjet elnyomás romjain megkötötték a Visegrádi Nyilatkozatot. A V4 nemcsak a Varsói Szerződés lebontásának lett a faltörő kosa, hanem a sikeres euroatlanti integráció kovácsa is: bizonyítva, hogy a térség elválaszthatatlanul a nyugati civilizációhoz tartozik."},
                {"type": "narration", "text": "Az évtizedek során a szövetség kézzelfogható fizikai valósággá érett: az észak-déli gáz-interkonnektorok és a Via Carpatia autópálya-folyosó megtörték a fél évszázados szovjet kelet-nyugati egyoldalúságot, megteremtve a Balti-, az Adriai- és a Fekete-tenger közötti Három Tenger Kezdeményezés gazdasági gerincét."},
                {"type": "narration", "text": "A 2022-es ukrajnai háború azonban a V4 történetének legsúlyosabb belső feszültségeit hozta felszínre: míg Lengyelország és Csehország a szabadság védelmének élvonalába állt, addig a magyar és szlovák politika eltérő stratégiai utakat keresett. A divergencia megmutatta, hogy közös biztonsági elköteleződés nélkül az intézményi keretek kiüresedhetnek."},
                {"type": "narration", "text": "Végeredményben Szűcs Jenő és Bibó István igazsága világítja meg a jövőt: Közép-Európa nem lehet 'kompország', sem a birodalmak prédájául szolgáló ütközőzóna. A visegrádi térség egyetlen méltó történelmi hivatása az európai szabadsághagyomány és a demokratikus jogállamiság szilárd őrzése: garantálva, hogy a Duna-kanyar szelleme a huszonegyedik században is a bátor, független és szolidáris nemzetek otthona maradjon."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        17,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze the Visegrád Group historical origins (1335, 1991) and post-communist transition.",
            "I can evaluate North-South infrastructure corridors, energy interconnectors, and the Three Seas Initiative.",
            "I can debate geopolitical divergence over Russia and Ukraine, EU cohesion policy, and Central European identity."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki éles diplomáciai véleménykülönbséget?", [
                "kibékíthetetlen ellentét feszül / homlokegyenest ellenkező álláspont / éles cezúra",
                "mindazonáltal megegyeztek",
                "mivel egyhangúlag döntöttek"
            ], 0, ["c1-discourse-divergence-markers"]),
            mc("grammar", "recognize", "Milyen kifejezésekkel fogalmazhatunk meg nemzetközi szerződésben kikötéseket és feltételeket?", [
                "azzal a megkötéssel, hogy / feltéve mindazonáltal",
                "miután hazautaztak",
                "amikor a szerződést kinyomtatták"
            ], 0, ["c1-concessive-stipulative-clauses"]),
            match("vocabulary", "recognize", [["1335-ös királytalálkozó", "Visegrád történelmi előképe"], ["Via Carpatia", "észak-déli autópálya-tengely"], ["divergencia", "politikai széttartás"], ["Három Tenger Kezdeményezés", "12 országos infrastruktúra platform"], ["hídszerep illúziója", "veszélyes geopolitikai lebegés"]], ["c1-visegrad-vocab"]),
            fb("vocabulary", "recall", "A visegrádi együttműködés 1991-es megújításának legfőbb célja a közös euroatlanti _____ elérése volt. (integration / integráció)", "integráció", "The foremost goal of renewing Visegrád cooperation in 1991 was achieving joint Euro-Atlantic integration.", ["c1-visegrad-vocab"]),
            fb("vocabulary", "recall", "A Balti- és Adriai-tenger közötti kétirányú _____ révén sikerült felszámolni az orosz gázfüggőséget. (interconnectors / interkonnektorok)", "interkonnektorok", "Via bidirectional interconnectors between the Baltic and Adriatic Seas, Russian gas dependence was successfully eliminated.", ["c1-visegrad-vocab"]),
            fb("grammar", "recall", "Míg Varsó a szankciók szigorítását sürgette, _____ Budapest a felmentések mellett érvelt. (meanwhile / addig)", "addig", "While Warsaw urged tightening sanctions, meanwhile Budapest argued for exemptions.", ["c1-rhetorical-antithetical-parallelism"]),
            fb("grammar", "context", "A felek aláírták a megállapodást, azzal a kifejezett _____ hogy a vitás kérdéseket békésen rendezik. (stipulation / megkötéssel)", "megkötéssel", "The parties signed the agreement, with the explicit stipulation that they resolve disputed issues peacefully.", ["c1-concessive-stipulative-clauses"]),
            fb("grammar", "context", "A szerződés értelmében a felek _____ tiszteletben tartani a nemzetközi jog normáit. (obliged / kötelesek)", "kötelesek", "Pursuant to the treaty the parties are obliged to respect norms of international law.", ["c1-modal-deontic-treaty-predicates"]),
            mc("grammar", "context", "Mi a lényege a 'Végeredményben...' típusú összegző mondatoknak a politikai diskurzusban?", [
                "Egy elemzés vagy vita összes szempontját szintetizálva megfogalmazzák a legfőbb, elkerülhetetlen végső tanulságot.",
                "Megváltoztatják a téma jellegét.",
                "Elnézést kérnek az olvasótól."
            ], 0, ["c1-adv-discourse-summation-particles"]),
            sb("grammar", "produce", ["A", "közép-európai", "szolidaritás", "nélkülözhetetlen", "a", "térség", "stabilitásának", "megőrzéséhez."], ["A", "közép-európai", "szolidaritás", "nélkülözhetetlen", "a", "térség", "stabilitásának", "megőrzéséhez."], "Central European solidarity is indispensable for preserving the region's stability.", ["c1-adv-discourse-summation-particles"]),
            sw("production", [{"prompt": "Write a critical evaluation of the V4 alliance balancing unity and divergence.", "answer": "Míg a visegrádi országok az infrastruktúra és az energiabiztonság terén figyelemre méltó sikereket értek el, addig a geopolitikai nézetkülönbségek rávilágítottak arra, hogy a szövetség fennmaradása a közös stratégiai értékek tiszteletben tartásán múlik."}], ["c1-rhetorical-antithetical-parallelism"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Central European identity in twenty-first century Europe.", "answer": "Végeredményben Közép-Európa sorsa nem az elszigetelődésben vagy a birodalmi ingázásban rejlik, hanem abban a bátor elköteleződésben, amellyel a térség a nyugati jogállami demokrácia elidegeníthetetlen bástyájaként határozza meg önmagát."}], ["c1-adv-discourse-summation-particles"])
        ]
    )

    print("=== Finished C1 Unit 17 ===")


if __name__ == "__main__":
    generate_unit_17()
