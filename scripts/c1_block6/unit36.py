#!/usr/bin/env python3
"""
Hungarian C1 Block 6 - Unit 36 Generator:
  - Track 1 (Core): Unit 36 — "The Architecture of Liberty: Deák, Eötvös, Bibó & The Democratic Tradition" (c1-36)
  - Track 2 (Discourse): Unit 36 — "The Democratic Minimum: Civil Society, Resistance & The European Horizon" (c1-magyarjovo)

This is the Capstone Finale of the Hungarian C1 curriculum!
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block6.registry_helper import register_unit


def generate_unit_36():
    print("=== Generating C1 Unit 36 (Capstone Finale) ===")
    
    new_skills = {
        "c1-36-vocab": {"kind": "vocabulary"},
        "c1-magyarjovo-vocab": {"kind": "vocabulary"},
        "c1-adv-rule-of-law-constitutional-tradition": {"kind": "grammar"},
        "c1-participle-passive-resistance-ethos": {"kind": "grammar"},
        "c1-modal-deontic-ten-commandments-freedom": {"kind": "grammar"},
        "c1-adv-comparative-democratic-compromise": {"kind": "grammar"},
        "c1-syntax-democratic-renewal-manifesto": {"kind": "grammar"},
        "c1-discourse-civil-disobedience-framing": {"kind": "grammar"},
        "c1-adv-grassroots-municipal-autonomy-critique": {"kind": "grammar"},
        "c1-modal-deontic-environmental-sovereignty": {"kind": "grammar"},
        "c1-adv-proportional-civic-resistance-renewal": {"kind": "grammar"},
        "c1-adv-conclusive-democratic-horizon": {"kind": "grammar"},
    }
    new_titles = {
        "c1-36-vocab": "reading",
        "c1-magyarjovo-vocab": "reading",
        "c1-adv-rule-of-law-constitutional-tradition": "evaluative adverbials formulating constitutional continuity and historic rule of law",
        "c1-participle-passive-resistance-ethos": "participial clauses analyzing passive resistance and moral non-collaboration",
        "c1-modal-deontic-ten-commandments-freedom": "deontic modal structures asserting ten commandments of a freedom-loving person",
        "c1-adv-comparative-democratic-compromise": "scalar comparative adverbials balancing historical compromise against constitutional integrity",
        "c1-syntax-democratic-renewal-manifesto": "evaluative correlative syntax formulating democratic renewal and civic constitutionalism",
        "c1-discourse-civil-disobedience-framing": "discourse framing markers diagnosing legitimate civil disobedience and democratic protest",
        "c1-adv-grassroots-municipal-autonomy-critique": "critical evaluative adverbials asserting grassroots local democracy against central autocracy",
        "c1-modal-deontic-environmental-sovereignty": "deontic modal structures formulating citizens duty of ecological defense",
        "c1-adv-proportional-civic-resistance-renewal": "proportional correlative structures mapping civic resistance against authoritarian decay",
        "c1-adv-conclusive-democratic-horizon": "evaluative conclusive particles declaring irrepressible horizon of european hungarian democracy",
    }
    
    core_title = "The Architecture of Liberty: Deák, Eötvös, Bibó & The Democratic Tradition"
    core_stems = [f"c1-36-0{i}" for i in range(1, 6)] + ["c1-36-consolidation"]
    disc_title = "The Democratic Minimum: Civil Society, Resistance & The European Horizon"
    slug = "magyarjovo"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(36, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-36)
    # ----------------------------------------------------
    core_intro = [
        "Hungarian constitutional thought contains a deep and enduring tradition of civic liberty, institutional rule of law, and non-violent resistance against tyranny.",
        "In this capstone unit, you will study the foundational principles of Ferenc Deák (constitutional continuity and passive resistance), József Eötvös (separation of powers and public education), and István Bibó (the ethics of the freedom-loving citizen). You will master the most refined legal-philosophical and civic registers of Hungarian at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-36-01",
            "title": "Deák Ferenc and the Jurisprudence of Passive Resistance",
            "grammar_title": "Evaluative Adverbials Formulating Constitutional Continuity and Historic Rule of Law",
            "grammar_skill": "c1-adv-rule-of-law-constitutional-tradition",
            "goals": [
                "I can analyze constitutional continuity and passive resistance (*alkotmányos jogfolytonosság, passzív ellenállás, oktrojált rendelet, közjogi integritás*).",
                "I can formulate historical rule-of-law arguments using elevated evaluative adverbials (*közjogilag megalapozottan, az alkotmányos jogfolytonosság elvéből kiindulva, az önkényuralmi dekrétumokat következetesen elutasítva*).",
                "I can articulate why legitimate law cannot arise from mere executive power without constitutional consent."
            ],
            "vocab": [
                {"lemma": "alkotmányos jogfolytonosság", "translation": "constitutional continuity", "pos": "expression"},
                {"lemma": "passzív ellenállás", "translation": "passive resistance", "pos": "expression"},
                {"lemma": "közjogi integritás", "translation": "constitutional integrity", "pos": "expression"},
                {"lemma": "oktrojált rendelet", "translation": "octroyed (imposed) decree", "pos": "expression"},
                {"lemma": "önkényuralom", "translation": "autocracy / absolutist tyranny", "pos": "noun"},
                {"lemma": "jogorvoslat", "translation": "legal remedy", "pos": "noun"},
                {"lemma": "el nem ismerés", "translation": "non-recognition", "pos": "noun"},
                {"lemma": "törvényesség", "translation": "legality / rule of law", "pos": "noun"}
            ],
            "gr_text1": "Evaluative adverbials in constitutional analysis define the legal legitimacy of political action: `közjogilag megalapozottan` (soundly based in constitutional law), `az alkotmányos jogfolytonosság elvéből kiindulva` (proceeding from the principle of constitutional continuity), `az önkényuralom dekrétumait következetesen érvénytelennek tekintve` (consistently regarding authoritarian decrees as void).",
            "gr_text2": "Example: `A nemzet az alkotmányos jogfolytonosság talaján szilárdan megállva és az oktrojált törvényeket elvből elutasítva őrizte meg önrendelkezését`.",
            "gr_table": [
                ["Közjogilag megalapozottan csak a törvényes országgyűlés alkothat kötelező jogot.", "Soundly based in constitutional law only a legitimate parliament can make binding law."],
                ["Az alkotmányos jogfolytonosságból kiindulva az abszolutista dekrétumok semmisek.", "Proceeding from constitutional continuity absolutist decrees are null and void."],
                ["A passzív ellenállás fegyverével élve a társadalom megtagadta az együttműködést.", "Employing the weapon of passive resistance society refused collaboration."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'passzív ellenállás' Deák Ferenc jogfilozófiájában?", [
                    "A törvénytelen, önkényuralmi rendeletekkel való bárminemű együttműködés békés, jogi elvű megtagadását.",
                    "Fegyveres felkelés szervezését idegen hatalmak segítségével.",
                    "A politikától való teljes visszavonulást és a birtok gazdálkodásának elhanyagolását."
                ], 0, ["c1-36-vocab"]),
                fb("grammar", "controlled", "Az alkotmányos jogfolytonosság elvéből _____ minden oktrojált rendelet érvénytelen. (proceeding / kiindulva)", "kiindulva", "Proceeding from the principle of constitutional continuity every octroyed decree is void.", ["c1-adv-rule-of-law-constitutional-tradition"]),
                match("vocabulary", "controlled", [
                    ["alkotmányos jogfolytonosság", "a nemzet történelmi és jogi alaptörvényeinek töretlen érvényessége"],
                    ["passzív ellenállás", "a törvénytelen hatalommal való együttműködés elvi megtagadása"],
                    ["oktrojált rendelet", "a népképviselet hozzájárulása nélkül, felülről ráerőszakolt jogszabály"],
                    ["közjogi integritás", "az alkotmányos rend elvi és intézményi csorbíthatatlansága"]
                ], ["c1-36-vocab"]),
                fb("grammar", "practice", "A jogtudósok közjogilag _____ bizonyították be az önkényuralom törvénytelenségét. (soundly / megalapozottan)", "megalapozottan", "The jurists soundly proved the illegitimacy of autocratic rule in constitutional law.", ["c1-adv-rule-of-law-constitutional-tradition"]),
                sb("grammar", "practice", ["Közjogilag", "megalapozottan", "az", "alkotmányos", "jogfolytonosság", "nem", "enged", "kompromisszumot."], ["Közjogilag", "megalapozottan", "az", "alkotmányos", "jogfolytonosság", "nem", "enged", "kompromisszumot."], "Soundly based in constitutional law constitutional continuity allows no compromise.", ["c1-adv-rule-of-law-constitutional-tradition"]),
                dc("dialogue", [
                    {"speaker": "Jogtörténész", "text": "Hogyan kényszerítette ki Deák Ferenc a jogállami rendezést?"},
                    {"speaker": "Kutató", "text": "Úgy, hogy a nemzet az alkotmányos jogfolytonosság elvéből _____ megtagadta az adófizetést és a hivatalviselést."},
                    {"speaker": "Jogtörténész", "text": "A jog ereje győzött a nyers erőszak felett."}
                ], ["kiindulva", "elfutva", "lemondva"], 0, ["c1-adv-rule-of-law-constitutional-tradition"]),
                sw("production", [{"prompt": "Write a sentence articulating constitutional resistance using an evaluative adverbial.", "answer": "Közjogilag megalapozottan és az alkotmányos jogfolytonosság elvéből szigorúan kiindulva a nemzet elutasította a bécsi önkényuralom oktrojált dekrétumait, mert a hatalom önkénye soha nem írhatja felül a törvényes szabadságjogokat."}], ["c1-adv-rule-of-law-constitutional-tradition"]),
                mc("grammar", "check", "Melyik kifejezés fejezi ki legpontosabban a deáki jogfolytonosság érvrendszerét?", [
                    "az alkotmányos jogfolytonosság elvéből szigorúan kiindulva",
                    "valahogyan megpróbálva elkerülni a kellemetlenségeket",
                    "amikor mindenki hazament pihenni a birtokára"
                ], 0, ["c1-adv-rule-of-law-constitutional-tradition"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-36-02",
            "title": "Eötvös József and Modern Rule of Law Institutions",
            "grammar_title": "Participial Clauses Analyzing Passive Resistance and Moral Non-Collaboration",
            "grammar_skill": "c1-participle-passive-resistance-ethos",
            "goals": [
                "I can analyze institutional guarantees of liberty (*hatalommegosztás, népoktatás, lelkiismereti szabadság, jogegyenlőség*).",
                "I can construct complex participial clauses analyzing moral non-collaboration and institutional ethics (*az abszolutista hatalmat erkölcsileg ellehetetlenítő polgári magatartás, a népnevelést a szabadság alapfeltételének tekintő reformátorok*).",
                "I can debate the relationship between education, religious freedom, and civic democracy."
            ],
            "vocab": [
                {"lemma": "hatalommegosztás", "translation": "separation of powers", "pos": "noun"},
                {"lemma": "népoktatás", "translation": "public education / national education", "pos": "noun"},
                {"lemma": "lelkiismereti szabadság", "translation": "freedom of conscience", "pos": "expression"},
                {"lemma": "jogegyenlőség", "translation": "equality before the law", "pos": "noun"},
                {"lemma": "szekularizáció", "translation": "secularization", "pos": "noun"},
                {"lemma": "jogállamisági garancia", "translation": "rule of law guarantee", "pos": "expression"},
                {"lemma": "társadalmi mobilitás", "translation": "social mobility", "pos": "expression"},
                {"lemma": "polgári intézményrendszer", "translation": "civic institutional system", "pos": "expression"}
            ],
            "gr_text1": "Participial clauses analyzing moral action and civic resistance condense historical and ethical synthesis into complex attributive structures: `az önkényuralmi erőszakkal való együttműködést következetesen megtagadó tisztviselők` (officials consistently refusing cooperation with autocratic violence), `a műveltséget a szabadság zálogának tekintő Eötvös-féle reformok` (Eötvös reforms regarding education as the pledge of liberty).",
            "gr_text2": "Example: `A népoktatási törvény a polgárosodást előmozdító és a feudális kiváltságokat véglegesen felszámoló modern jogállami pillérré vált`.",
            "gr_table": [
                ["A jogtiprást passzív ellenállással elutasító társadalom megőrizte méltóságát.", "Society rejecting rights abuses through passive resistance preserved its dignity."],
                ["A hatalommegosztást az önkény gátjának tekintő gondolkodók intézményeket építettek.", "Thinkers regarding separation of powers as the check on autocracy built institutions."],
                ["A lelkiismereti szabadságot törvényben garantáló állam biztosítja a békét.", "The state guaranteeing freedom of conscience in law ensures civic peace."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintette Eötvös József a népoktatást a jogállam legfontosabb alapjának?", [
                    "Mert úgy vallotta: a szabadságjogokkal csak a kiművelt, önállóan gondolkodni képes és jogaival tisztában lévő polgárság tud felelősen élni.",
                    "Mert az iskolák építése olcsóbb volt, mint a hadsereg fenntartása.",
                    "Mert a törvényeket csak latinul akarta taníttatni a nemeseknek."
                ], 0, ["c1-36-vocab"]),
                fb("grammar", "controlled", "A jogtiprással való együttműködést következetesen _____ polgárok megroppantották az önkényuralmat. (refusing / megtagadó)", "megtagadó", "Citizens consistently refusing cooperation with rights violations broke the autocracy.", ["c1-participle-passive-resistance-ethos"]),
                match("vocabulary", "controlled", [
                    ["hatalommegosztás", "a törvényhozó, végrehajtó és bírói hatalom kölcsönös ellenőrzése"],
                    ["népoktatás", "az államilag finanszírozott, kötelező és felekezetsemleges közoktatás"],
                    ["lelkiismereti szabadság", "a vallási és világnézeti meggyőződés szabad gyakorlása"],
                    ["jogegyenlőség", "minden polgár azonos jogi státusza a törvény előtt kiváltságok nélkül"]
                ], ["c1-36-vocab"]),
                fb("grammar", "practice", "A műveltséget a szabadság zálogának _____ Eötvös József megalkotta a modern népoktatási törvényt. (regarding / tekintő)", "tekintő", "Regarding culture as the pledge of freedom, József Eötvös created modern public education.", ["c1-participle-passive-resistance-ethos"]),
                sb("grammar", "practice", ["A", "feudális", "kiváltságokat", "felszámoló", "törvények", "megalapozták", "a", "modern", "jogállamot."], ["A", "feudális", "kiváltságokat", "felszámoló", "törvények", "megalapozták", "a", "modern", "jogállamot."], "The laws dismantling feudal privileges laid the foundation of the modern rule of law.", ["c1-participle-passive-resistance-ethos"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Hogyan kapcsolódik össze a deáki ellenállás és az eötvösi intézményépítés?"},
                    {"speaker": "Filozófus", "text": "A jogtiprást passzív ellenállással megtagadó társadalom után Eötvös a szabadságot törvényi _____ védő intézményeket hozott létre."},
                    {"speaker": "Történész", "text": "Ez a magyar liberalizmus aranykora."}
                ], ["garanciákkal", "fegyverekkel", "pénzzel"], 0, ["c1-participle-passive-resistance-ethos"]),
                sw("production", [{"prompt": "Write a sentence with a complex participial clause analyzing civic resistance.", "answer": "A törvénytelen központosítást és az önkényuralmi zsarolást következetesen megtagadó és elveihez tántoríthatatlanul ragaszkodó polgárság nélkülözhetetlen erkölcsi alapot teremtett a jogállami intézmények újjáépítéséhez."}], ["c1-participle-passive-resistance-ethos"]),
                mc("grammar", "check", "Melyik mondatszerkezet valósít meg emelkedett participiális kifejezést?", [
                    "A hatalommal való megalkuvást elutasító és az autonómiát védelmező polgárok",
                    "A polgárok nagyon mérgesek voltak és bezárták az ajtót",
                    "Amikor mindenki otthon ült és nem akart semmit csinálni"
                ], 0, ["c1-participle-passive-resistance-ethos"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-36-03",
            "title": "Bibó István and the Ten Commandments of Freedom",
            "grammar_title": "Deontic Modal Structures Asserting Ten Commandments of a Freedom-Loving Person",
            "grammar_skill": "c1-modal-deontic-ten-commandments-freedom",
            "goals": [
                "I can analyze Bibó's political ethics and the overcoming of hysteria (*szabadságszerető ember, politikai hisztéria, félelemmentesség, kölcsönös méltóság*).",
                "I can formulate deontic modal structures asserting human rights and democratic duties (*nem szabad félni a szabadságtól, el kell utasítani az erőszak kultuszát, kötelességünk elismerni mások szabadságát*).",
                "I can articulate why a democracy must be grounded in moral fearlessness rather than reciprocal demonization."
            ],
            "vocab": [
                {"lemma": "szabadságszerető ember", "translation": "freedom-loving person", "pos": "expression"},
                {"lemma": "félelemmentesség", "translation": "fearlessness / freedom from fear", "pos": "noun"},
                {"lemma": "kölcsönös elismerés", "translation": "mutual recognition", "pos": "expression"},
                {"lemma": "politikai hisztéria", "translation": "political hysteria", "pos": "expression"},
                {"lemma": "emberi méltóság", "translation": "human dignity", "pos": "expression"},
                {"lemma": "erkölcsi tartás", "translation": "moral integrity / backbone", "pos": "expression"},
                {"lemma": "felelősségvállalás", "translation": "taking responsibility", "pos": "noun"},
                {"lemma": "demokratikus elkötelezettség", "translation": "democratic commitment", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures asserting democratic ethics and categorical civic duties utilize: `nem szabad félnünk a szabadságtól` (we must not fear freedom), `kötelességünk feltétlenül tiszteletben tartani` (it is our duty to unconditionally respect), `a polgárnak nem engedhető meg, hogy feladja erkölcsi integritását` (a citizen cannot be permitted to abandon moral integrity), `kell, hogy a hatalom korlátozottsága megkérdőjelezhetetlen legyen` (it is necessary that the limitation of power be unquestionable).",
            "gr_text2": "Example: `A szabadságszerető embernek nem szabad félnie attól, hogy a szabadság másoknak is jut, és kötelessége szembeszállni a gyűlöletkeltéssel`.",
            "gr_table": [
                ["Nem szabad félnünk a szabadságtól és a másként gondolkodók egyenjogúságától.", "We must not fear freedom and the equal rights of those who think differently."],
                ["Kötelességünk határozottan elutasítani a politikai hisztériát és az ellenségkép-gyártást.", "It is our duty to firmly reject political hysteria and enemy-fabrication."],
                ["Minden demokratikus rendszernek az emberi méltóság feltétlen tiszteletén kell alapulnia.", "Every democratic system must be founded upon unconditional respect for human dignity."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Ki a 'szabadságszerető ember' Bibó István híres meghatározása szerint?", [
                    "Az, aki nem fél a szabadságtól, aki nem fél attól, hogy a szabadság másoknak is jut, és aki elutasítja az erőszak minden formáját.",
                    "Az, aki egyedül él a hegyekben és nem fizet adót az államnak.",
                    "Az, aki bármilyen törvényt áthághat saját vagyonszerzése érdekében."
                ], 0, ["c1-36-vocab"]),
                fb("grammar", "controlled", "A valódi demokratának soha nem _____ félnie a polgári szabadságjogok kiteljesedésétől. (must not / szabad)", "szabad", "A true democrat must never fear the fulfillment of civil liberties.", ["c1-modal-deontic-ten-commandments-freedom"]),
                match("vocabulary", "controlled", [
                    ["szabadságszerető ember", "aki nem fél mások szabadságától és tiszteli a közös méltóságot"],
                    ["politikai hisztéria", "a valóságtól elszakadó, félelemre és ellenségkeresésre épülő hatalmi állapot"],
                    ["emberi méltóság", "minden ember veleszületett, elidegeníthetetlen értéke és jogalapja"],
                    ["félelemmentesség", "a szabad polgári létezés és az önálló döntéshozatal lelki előfeltétele"]
                ], ["c1-36-vocab"]),
                fb("grammar", "practice", "Minden jogállamban kötelességünk határozottan szembeszállni a hatalmi önkénnyel, és _____ védenünk a kisebbségek jogait. (must / meg kell)", "meg kell", "In every rule of law state it is our duty to firmly confront autocratic power, and we must protect minorities' rights.", ["c1-modal-deontic-ten-commandments-freedom"]),
                sb("grammar", "practice", ["Nem", "szabad", "félnünk", "attól,", "hogy", "a", "szabadság", "másoknak", "is", "jut."], ["Nem", "szabad", "félnünk", "attól,", "hogy", "a", "szabadság", "másoknak", "is", "jut."], "We must not fear that freedom is granted to others as well.", ["c1-modal-deontic-ten-commandments-freedom"]),
                dc("dialogue", [
                    {"speaker": "Filozófushallgató", "text": "Hogyan győzhető le a kelet-európai politikai hisztéria?"},
                    {"speaker": "Professzor", "text": "Bibó szerint úgy, hogy nem szabad félni a valóságtól, és meg kell tanulnunk a kölcsönös _____ nyelvét."},
                    {"speaker": "Filozófushallgató", "text": "Ez a demokratikus érettség legfőbb vizsgája."}
                ], ["elismerés", "gyűlölet", "megvetés"], 0, ["c1-modal-deontic-ten-commandments-freedom"]),
                sw("production", [{"prompt": "Write a sentence formulating Bibó's civic ethic using a deontic modal structure.", "answer": "A szabadságszerető embernek nem szabad engednie a félelemkeltésnek és a politikai hisztériának; feltétlen erkölcsi kötelességünk, hogy a szabadságjogokat és az emberi méltóság sérthetetlenségét minden polgártársunk számára maradéktalanul garantáljuk."}], ["c1-modal-deontic-ten-commandments-freedom"]),
                mc("grammar", "check", "Melyik deontikus szerkezet fogalmazza meg a bibói tízparancsolat szellemiségét a legerőteljesebben?", [
                    "Nem szabad félnünk a szabadságtól, és kötelességünk megvédeni a humanizmus értékeit",
                    "Lehet, hogy néha nem baj, ha nem csinálunk semmit sem",
                    "Bárki csinálhat bármit, ha a rendőrség nem látja"
                ], 0, ["c1-modal-deontic-ten-commandments-freedom"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-36-04",
            "title": "Compromise vs Integrity: The Debate on Hungarian Destiny",
            "grammar_title": "Scalar Comparative Adverbials Balancing Historical Compromise Against Constitutional Integrity",
            "grammar_skill": "c1-adv-comparative-democratic-compromise",
            "goals": [
                "I can evaluate the historic debate between Deák's Compromise and Kossuth's Cassandra Letter (*Kiegyezés, Cassandra-levél, pragmatikus reálpolitika, nemzeti szuverenitás*).",
                "I can balance competing historical imperatives using scalar comparative adverbials (*sokkal inkább a reálpolitikai megmaradás, mintsem a jogi elvtelenség jegyében; lényegesen mélyebb történelmi felelősséggel mérlegelve*).",
                "I can write a nuanced critical essay weighing pragmatic state-building against principled intransigence."
            ],
            "vocab": [
                {"lemma": "Cassandra-levél", "translation": "Cassandra letter (Kossuth's warning)", "pos": "expression"},
                {"lemma": "pragmatikus reálpolitika", "translation": "pragmatic realpolitik", "pos": "expression"},
                {"lemma": "nemzeti szuverenitás", "translation": "national sovereignty", "pos": "expression"},
                {"lemma": "alkotmányos hűség", "translation": "constitutional loyalty", "pos": "expression"},
                {"lemma": "történelmi távlat", "translation": "historical perspective", "pos": "expression"},
                {"lemma": "elvi integritás", "translation": "principled integrity", "pos": "expression"},
                {"lemma": "közjogi vita", "translation": "constitutional law dispute", "pos": "expression"},
                {"lemma": "nemzeti önrendelkezés", "translation": "national self-determination", "pos": "expression"}
            ],
            "gr_text1": "Scalar comparative adverbials balancing historical arguments structure complex dialectics: `sokkal inkább a békés gazdasági fejlődés, mintsem a közjogi elvfeladás jegyében` (much more in the spirit of peaceful economic growth rather than abandoning constitutional principles), `lényegesen árnyaltabb megközelítést igényelve` (demanding a substantially more nuanced approach), `jóval szilárdabb intézményi garanciákat követelve` (demanding far firmer institutional guarantees).",
            "gr_text2": "Example: `Deák politikája sokkal inkább az elérhető békét és polgárosodást, semmint a heroikus nemzethalált választotta, miközben Kossuth a jövőbeli birodalmi összeomlásra figyelmeztetett`.",
            "gr_table": [
                ["A kiegyezés sokkal inkább a reálpolitika diadala volt, semmint a jogok eladása.", "The Compromise was much more a victory of realpolitik than selling out rights."],
                ["Kossuth lényegesen sötétebb történelmi jövőt látott a Habsburg-birodalomhoz kötve.", "Kossuth saw a substantially darker historical future bound to the Habsburg Empire."],
                ["Jóval alaposabban mérlegelve mindkét álláspontnak mély igazságai tárulnak fel.", "Weighing far more thoroughly, profound truths of both positions are revealed."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt Kossuth Lajos Cassandra-levelének legfőbb figyelmeztetése 1867-ben?", [
                    "Hogy Magyarország a sorsát egy pusztulásra ítélt soknemzetiségű birodalomhoz köti, ami elkerülhetetlen történelmi katasztrófához vezet.",
                    "Hogy a budapesti Lánchíd vámjai túl magasak a kereskedők számára.",
                    "Hogy Ausztria azonnal bevezeti a német nyelv kizárólagos használatát az iskolákban."
                ], 0, ["c1-36-vocab"]),
                fb("grammar", "controlled", "Deák döntése sokkal _____ a nemzet gazdasági megmaradását, semmint a meddő ellenállást szolgálta. (rather / inkább)", "inkább", "Deák's decision served the nation's economic survival much rather than sterile resistance.", ["c1-adv-comparative-democratic-compromise"]),
                match("vocabulary", "controlled", [
                    ["Cassandra-levél", "Kossuth látnoki inteleme a Monarchiához kötött nemzeti sors veszélyeiről"],
                    ["pragmatikus reálpolitika", "a megvalósítható lehetőségekre épülő, kompromisszumkész cselekvés"],
                    ["nemzeti szuverenitás", "az állam független, külső beavatkozástól mentes önrendelkezése"],
                    ["elvi integritás", "a meggyőződésekhez és az alaptörvényekhez való feltétlen hűség"]
                ], ["c1-36-vocab"]),
                fb("grammar", "practice", "A történelmi felelősséget lényegesen _____ mérlegelve mindkét politikus nagysága kirajzolódik. (more deeply / mélyebben)", "mélyebben", "Weighing historical responsibility substantially more deeply, the greatness of both statesmen emerges.", ["c1-adv-comparative-democratic-compromise"]),
                sb("grammar", "practice", ["A", "kiegyezés", "sokkal", "inkább", "a", "polgári", "fejlődést,", "semmint", "a", "megalkuvást", "szolgálta."], ["A", "kiegyezés", "sokkal", "inkább", "a", "polgári", "fejlődést,", "semmint", "a", "megalkuvást", "szolgálta."], "The Compromise served civic development much rather than compromise.", ["c1-adv-comparative-democratic-compromise"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi oktató", "text": "Igaza volt Kossuthnak vagy Deáknak a kiegyezés vitájában?"},
                    {"speaker": "Doktorandusz", "text": "Deák a jelent mentette meg a gazdasági felvirágzással, Kossuth viszont lényegesen _____ távlatban látta a birodalom összeomlását."},
                    {"speaker": "Egyetemi oktató", "text": "Ez a magyar történelem legtragikusabb dilemmája."}
                ], ["hosszabb", "rövidebb", "szűkebb"], 0, ["c1-adv-comparative-democratic-compromise"]),
                sw("production", [{"prompt": "Write a sentence balancing compromise and integrity using a scalar comparative adverbial.", "answer": "A kiegyezés közjogi művét sokkal inkább a nemzet reális túlélését és polgárosodását szolgáló kompromisszumnak, mintsem elvtelen árulásnak kell tekintenünk, jóllehet Kossuth intelmei lényegesen mélyebb történelmi aggodalmakat fogalmaztak meg."}], ["c1-adv-comparative-democratic-compromise"]),
                mc("grammar", "check", "Melyik mondat alkalmaz skálaszerű összehasonlító határozói szerkezetet?", [
                    "sokkal inkább a polgári felvirágzást, semmint a behódolást választva",
                    "mind a kettő nagyon jó volt és mindenki örült neki",
                    "egyáltalán nem érdekes, hogy ki mit mondott régen"
                ], 0, ["c1-adv-comparative-democratic-compromise"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-36-05",
            "title": "Civic Humanism and Democratic Renewal",
            "grammar_title": "Evaluative Correlative Syntax Formulating Democratic Renewal and Civic Constitutionalism",
            "grammar_skill": "c1-syntax-democratic-renewal-manifesto",
            "goals": [
                "I can synthesize the Hungarian democratic canon (*polgári humanizmus, cselekvő állampolgárság, közjó, köztársasági eszme, szellemi örökség*).",
                "I can construct synthetic correlative structures formulating democratic renewal (*nemcsak az intézmények formális kereteit kell helyreállítani, hanem a polgári öntudatot is újra kell éleszteni; amilyen mértékben erősödik a szolidaritás, olyan mértékben szorul vissza az autokrácia*).",
                "I can interpret classic foundational texts by Deák Ferenc and Bibó István."
            ],
            "vocab": [
                {"lemma": "polgári humanizmus", "translation": "civic humanism", "pos": "expression"},
                {"lemma": "demokratikus megújulás", "translation": "democratic renewal", "pos": "expression"},
                {"lemma": "cselekvő állampolgárság", "translation": "active citizenship", "pos": "expression"},
                {"lemma": "közjó szolgálata", "translation": "service to the public good", "pos": "expression"},
                {"lemma": "köztársasági eszme", "translation": "republican ideal", "pos": "expression"},
                {"lemma": "szellemi örökség", "translation": "intellectual heritage", "pos": "expression"},
                {"lemma": "szolidaritás hálózata", "translation": "network of solidarity", "pos": "expression"},
                {"lemma": "intézményi garancia", "translation": "institutional guarantee", "pos": "expression"}
            ],
            "gr_text1": "Correlative evaluative syntax articulates programmatic civic manifestos and constitutional synthesis: `nemcsak..., hanem... is` (not only..., but also...), `amilyen mértékben..., olyan mértékben...` (to the extent that..., to that same extent...), `egyfelől..., másfelől viszont...` (on the one hand..., but on the other hand...), `ahol nincs szabadság, ott nincs emberi méltóság sem` (where there is no freedom, there is no human dignity either).",
            "gr_text2": "Example: `Nemcsak a jogállami intézményeket kell helyreállítani, hanem a polgárokban élő demokratikus felelősségérzetet is újra kell éleszteni`.",
            "gr_table": [
                ["Nemcsak az alkotmány betűjét kell tisztelni, hanem annak szellemiségét is követni kell.", "Not only must the letter of the constitution be respected, but its spirit must be followed."],
                ["Amilyen mértékben növekszik a polgári szolidaritás, olyan mértékben gyengül az önkény.", "To the extent that civic solidarity grows, to that extent arbitrary rule weakens."],
                ["Ahol az igazságosság uralkodik, ott a törvény a szabadság legfőbb védelmezője.", "Where justice reigns, there the law is the supreme defender of liberty."]
            ],
            "classic_story": {
                "slug": "deak-bibo-a-szabadsag-hagyomanya",
                "title": "Deák Ferenc és Bibó István: A szabadság magyar hagyománya",
                "author": "Deák Ferenc & Bibó István",
                "work": "Adalék a magyar közjoghoz (1865) / A szabadságszerető ember tízparancsolata (1956)",
                "summary": "Deák Ferenc az alkotmányos jogfolytonosság és a törvényes passzív ellenállás elméletével megvédte a nemzet integritását az önkénnyel szemben. Bibó István ezt kiteljesítve a félelemmentes demokratikus polgár erkölcsi tízparancsolatát fogalmazta meg, örök érvényű iránytűt adva a magyar jogállamiságnak.",
                "characters": [
                    "Deák Ferenc, a haza bölcse",
                    "Bibó István, a magyar demokrácia erkölcsi iránytűje"
                ],
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Deák Ferenc 1865 húsvétján megjelent híres közjogi értekezéseiben a magyar alkotmányosság legmélyebb filozófiáját fogalmazta meg a bécsi abszolutizmussal szemben: 'Engedni a jogból, melyet a haza alkotmányos szabadsága nyújt, annyi volna, mint elismerni, hogy a hatalom megelőzi a jogot. A törvény nem az uralkodó kegye, hanem a nemzet és a korona szent szerződése. Amit erő és hatalom vesz el, azt idő és szerencse visszahozhatja; de miről a nemzet önként lemond, annak visszaszerzése mindig nehéz és kétséges.' A deáki passzív ellenállás ezzel vált az erőszakmentes jogvédelem egyetemes történelmi mintájává."
                    },
                    {
                        "type": "narration",
                        "text": "Ezt a gondolatot fejlesztette tovább a huszadik század közepén Bibó István, aki a modern magyar demokrácia legtárgyilagosabb erkölcsi kódexét alkotta meg 1956 sorsdöntő napjaiban és politikai tanulmányaiban. Bibó felismerte, hogy Kelet-Európa legnagyobb történelmi sorstragédiája a zsarnokság és a kölcsönös félelem ördögi köre, amely hisztériába és kölcsönös elnyomásba kergeti a társadalmakat."
                    },
                    {
                        "type": "narration",
                        "text": "'Szabadságszerető ember az' – írta Bibó –, 'aki nem fél a szabadságtól; aki nem fél attól, hogy a szabadság másoknak is jut; aki nem hiszi, hogy a szabadság az ő kiváltsága, s aki tudja, hogy a szabadság ott kezdődik, ahol a hatalom megáll.' A szabadságszerető ember elutasítja azt a hazugságot, hogy a rend fenntartásához emberi életeket és méltóságokat kell sárba tiporni, és vallja, hogy a jogállam az emberi méltóság intézményesített formája."
                    },
                    {
                        "type": "narration",
                        "text": "Deák elvi tántoríthatatlansága és Bibó humánus bátorsága egyetlen közös magyar hagyományban forr össze. Ez a hagyomány arra tanít, hogy semmiféle hatalmi túlerő nem teheti törvényessé az önkényt, és hogy a polgári szabadság mindennapi erkölcsi felelősségvállalás nélkül elsorvad. A magyar köztársaság jövője azok kezében van, akik a félelemmentes cselekvés és a testvéri szolidaritás szellemében védelmezik a jogállamot."
                    }
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'cselekvő állampolgárság' a polgári humanizmus szellemében?", [
                    "A közügyekben való tudatos, felelős részvételt, a közösség szabadságának és jogainak aktív védelmét.",
                    "A választásokon való kötelező fizikai jelenlétet büntetés terhe mellett.",
                    "Az állami hivatalok döntéseinek kritika nélküli végrehajtását."
                ], 0, ["c1-36-vocab"]),
                fb("grammar", "controlled", "Nemcsak a törvényeket kell megalkotni, _____ a jogállami kultúrát is meg kell honosítani a társadalomban. (but also / hanem)", "hanem", "Not only must laws be created, but the rule-of-law culture must also be rooted in society.", ["c1-syntax-democratic-renewal-manifesto"]),
                match("vocabulary", "controlled", [
                    ["polgári humanizmus", "az emberi méltóságot és a közjót a közélet középpontjába állító eszme"],
                    ["cselekvő állampolgárság", "a társadalmi szolidaritásra és felelősségre épülő aktív polgári szerep"],
                    ["köztársasági eszme", "a népszuverenitáson és a fékek és egyensúlyok rendszerén alapuló államforma"],
                    ["szellemi örökség", "a történelmi elődök szabadságeszméinek élő, továbbadandó hagyománya"]
                ], ["c1-36-vocab"]),
                fb("grammar", "practice", "_____ mértékben erősödik a civil társadalom, olyan mértékben szorul vissza a korrupció és az elnyomás. (To the extent that / Amilyen)", "Amilyen", "To the extent that civil society strengthens, to that extent corruption and oppression recede.", ["c1-syntax-democratic-renewal-manifesto"]),
                sb("grammar", "practice", ["Nemcsak", "a", "szabadságot", "kell", "kivívni,", "hanem", "meg", "is", "kell", "védeni."], ["Nemcsak", "a", "szabadságot", "kell", "kivívni,", "hanem", "meg", "is", "kell", "védeni."], "Not only must freedom be won, but it must also be defended.", ["c1-syntax-democratic-renewal-manifesto"]),
                dc("dialogue", [
                    {"speaker": "Közéleti esszéíró", "text": "Hogyan tartható fenn a deáki és bibói örökség a 21. században?"},
                    {"speaker": "Jogfilozófus", "text": "Úgy, hogy nemcsak a történelmi emlékezetet ápoljuk, hanem a cselekvő állampolgárság révén mindennap újra _____ a jogállamot."},
                    {"speaker": "Közéleti esszéíró", "text": "Ez a köztársaság egyetlen igazi védelme."}
                ], ["megteremtjük", "elfelejtjük", "leromboljuk"], 0, ["c1-syntax-democratic-renewal-manifesto"]),
                sw("production", [{"prompt": "Write a synthetic manifesto sentence using correlative grammar formulating democratic renewal.", "answer": "Nemcsak az alkotmányos fékek és egyensúlyok rendszerét kell visszavonhatatlanul helyreállítanunk, hanem a kölcsönös szolidaritáson és emberi méltóságon alapuló cselekvő állampolgárságot is a magyar politikai kultúra szívévé kell tennünk."}], ["c1-syntax-democratic-renewal-manifesto"]),
                mc("grammar", "check", "Melyik korrelatív szerkezet fogalmaz meg emelkedett demokratikus megújulást?", [
                    "Nemcsak az intézményeket kell újjáépítenünk, hanem a polgári szabadságtudatot is újra kell teremtenünk",
                    "Volt ott sokféle dolog és mindenki mondott valamit",
                    "Ha jó idő lesz holnap, elmegyünk a parkba sétálni"
                ], 0, ["c1-syntax-democratic-renewal-manifesto"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(36, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson (12 exercises: 3 recognize, 3 recall, 3 context, 3 produce)
    emit_consolidation_lesson(
        36,
        "core",
        "c1-36-consolidation",
        core_title,
        [
            "I can master the legal, philosophical, and civic vocabulary of Deák Ferenc, Eötvös József, and Bibó István.",
            "I can deploy constitutional evaluative adverbials, participial resistance clauses, and deontic modal structures of human rights.",
            "I can balance historic compromises against constitutional integrity and formulate synthetic manifestos of democratic renewal."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés fogalmazza meg a deáki jogfolytonosság elvét a legszakszerűbben?", [
                "az alkotmányos jogfolytonosság elvéből kiindulva és az önkényuralmi rendeleteket semmisnek tekintve",
                "hogyha valaki nem akar dolgozni a hivatalban hétfőn",
                "amikor a király levelet ír a parlamentnek a palotából"
            ], 0, ["c1-adv-rule-of-law-constitutional-tradition"]),
            mc("grammar", "recognize", "Milyen szerkezettel elemezhető az erőszakmentes ellenállás erkölcsi ethosza a leghitelesebben?", [
                "a törvénytelen hatalommal való együttműködést elvből megtagadó és a jogokhoz ragaszkodó polgárság",
                "az emberek nagyon dühösek voltak és bezárkóztak a házaikba",
                "amikor senki sem ment el a vásárba vasárnap reggel"
            ], 0, ["c1-participle-passive-resistance-ethos"]),
            match("vocabulary", "recognize", [
                ["alkotmányos jogfolytonosság", "a törvényes jogrend megszakítatlan történelmi érvényessége"],
                ["szabadságszerető ember", "aki nem fél a szabadságtól és tiszteletben tartja mások jogait"],
                ["hatalommegosztás", "az intézményi fékek és ellensúlyok rendszere az önkény ellen"],
                ["cselekvő állampolgárság", "a társadalmi szolidaritásban és a közjó védelmében megvalósuló polgári felelősség"]
            ], ["c1-36-vocab"]),
            fb("vocabulary", "recall", "A szabadságszerető ember alapvető lélektani vonása a félelemtől való mentesség, a belső _____ . (fearlessness / félelemmentesség)", "félelemmentesség", "The fundamental psychological trait of a freedom-loving person is freedom from fear, internal fearlessness.", ["c1-36-vocab"]),
            fb("vocabulary", "recall", "Eötvös József szerint a modern jogállam fundamentuma az ingyenes és kötelező _____ . (public education / népoktatás)", "népoktatás", "According to József Eötvös the foundation of the modern rule of law is free and compulsory public education.", ["c1-36-vocab"]),
            fb("grammar", "recall", "Az alkotmányos jogfolytonosság elvéből szigorúan _____ minden oktrojált rendelet érvénytelen. (proceeding / kiindulva)", "kiindulva", "Proceeding strictly from constitutional continuity every octroyed decree is void.", ["c1-adv-rule-of-law-constitutional-tradition"]),
            fb("grammar", "context", "A polgárnak soha nem _____ meghajolnia a politikai félelemkeltés és hisztéria előtt. (must not / szabad)", "szabad", "A citizen must never bow before political fearmongering and hysteria.", ["c1-modal-deontic-ten-commandments-freedom"]),
            fb("grammar", "context", "A kiegyezést sokkal _____ a békés fejlődés zálogának, semmint a jogok feladásának kell tekintenünk. (rather / inkább)", "inkább", "The Compromise must be seen much rather as the pledge of peaceful development than surrendering rights.", ["c1-adv-comparative-democratic-compromise"]),
            mc("grammar", "context", "Mi a bibói politikai etika legfőbb tanulsága a 21. századi demokráciák számára?", [
                "A félelemmentesség kultúrája: a szabadság nem privilégium, és a jogállam az emberi méltóság kölcsönös elismerésén alapul.",
                "Hogy a hatalomnak joga van bármilyen törvényt módosítani éjszaka.",
                "Hogy a kisebbségek jogait fel kell áldozni a többség kényelméért."
            ], 0, ["c1-modal-deontic-ten-commandments-freedom"]),
            sb("grammar", "produce", ["Nemcsak", "a", "szabadságot", "kell", "kivívni,", "hanem", "az", "intézményeket", "is", "meg", "kell", "védeni."], ["Nemcsak", "a", "szabadságot", "kell", "kivívni,", "hanem", "az", "intézményeket", "is", "meg", "kell", "védeni."], "Not only must freedom be won, but institutions must also be protected.", ["c1-syntax-democratic-renewal-manifesto"]),
            sw("production", [{"prompt": "Write a capstone evaluation of passive resistance using a participial clause.", "answer": "Az önkényuralmi dekrétumokkal való együttműködést következetesen megtagadó és a jogfolytonosság elvéhez hűséges polgárság bebizonyította, hogy a hatalom nyers erőszakja soha nem írhatja felül az erkölcsi méltóságot és a nemzeti önrendelkezést."}], ["c1-participle-passive-resistance-ethos"]),
            sw("production", [{"prompt": "Synthesize the entire democratic tradition using correlative syntax.", "answer": "Nemcsak az alkotmányos fékek és egyensúlyok rendszerét kell visszavonhatatlanul helyreállítanunk, hanem a kölcsönös tiszteleten és szolidaritáson alapuló cselekvő állampolgárságot is a magyar politikai nemzet élő fundamentumává kell emelnünk."}], ["c1-syntax-democratic-renewal-manifesto"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-magyarjovo)
    # ----------------------------------------------------
    disc_intro = [
        "Contemporary Hungarian democracy faces critical challenges: systemic centralization, erosion of checks and balances, capture of public institutions, and civic vulnerability.",
        "In this capstone discourse track, you will analyze the vital forces of democratic resilience: teacher strikes and civil disobedience, autonomous municipalities, environmental citizen resistance against battery factories, the Democratic Minimum, and Hungary's irreversible European future. You will master the critical argumentative register of democratic resistance at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Teachers' Protests and Civil Disobedience",
            "grammar_title": "Discourse Framing Markers Diagnosing Legitimate Civil Disobedience and Democratic Protest",
            "grammar_skill": "c1-discourse-civil-disobedience-framing",
            "goals": [
                "I can analyze teacher strikes, civic disobedience, and solidarity movements (*polgári engedetlenség, sztrájkjog korlátozása, élőlánc, rendkívüli felmentés*).",
                "I can frame moral and constitutional legitimacy versus formal legality using discourse markers (*a jogállamiság szempontjából nézve, erkölcsi kötelességként megélve, a hatalmi elnyomásra válaszul*).",
                "I can articulate why peaceful civil disobedience becomes necessary when legal strike avenues are stripped."
            ],
            "vocab": [
                {"lemma": "polgári engedetlenség", "translation": "civil disobedience", "pos": "expression"},
                {"lemma": "sztrájkjog korlátozása", "translation": "restriction of the right to strike", "pos": "expression"},
                {"lemma": "élőlánc", "translation": "human chain", "pos": "noun"},
                {"lemma": "rendkívüli felmentés", "translation": "summary dismissal / immediate termination", "pos": "expression"},
                {"lemma": "szolidaritási nyilatkozat", "translation": "declaration of solidarity", "pos": "expression"},
                {"lemma": "diáktüntetés", "translation": "student protest", "pos": "noun"},
                {"lemma": "oktatási autonómia", "translation": "educational autonomy", "pos": "expression"},
                {"lemma": "megfélemlítés", "translation": "intimidation", "pos": "noun"}
            ],
            "gr_text1": "Discourse framing markers distinguish legitimate constitutional resistance from statutory authoritarian decrees: `a jogállamiság szempontjából vizsgálva` (examined from the perspective of the rule of law), `erkölcsi imperatívuszként megélve az ellenállást` (experiencing resistance as a moral imperative), `a sztrájkjog ellehetetlenítésére válaszul` (in response to the crippling of the right to strike), `a polgári engedetlenség legitim eszköztárához nyúlva` (reaching for the legitimate toolkit of civil disobedience).",
            "gr_text2": "Example: `A pedagógusok a sztrájkjog kiüresítésére válaszul és erkölcsi kötelességből cselekedve a polgári engedetlenség eszközével védték meg az oktatás jövőjét`.",
            "gr_table": [
                ["A jogállamiság szempontjából nézve a sztrájkjog korlátozása alaptörvény-ellenes.", "Viewed from the perspective of the rule of law, restricting the right to strike is unconstitutional."],
                ["Erkölcsi kötelességként megélve a tanárok kiálltak a diákok méltóságáért.", "Experienced as a moral duty, teachers stood up for students' dignity."],
                ["A megfélemlítésre válaszul tízezres élőláncok vették körül az iskolákat.", "In response to intimidation, human chains of tens of thousands surrounded schools."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-01-tanartuntetesek-polgari-engedetlenseg",
                "title": "A tanárok lázadása: Sztrájkjog és polgári engedetlenség",
                "summary": "Amikor a hatalom adminisztratív úton megsemmisítette a pedagógusok sztrájkjogát, a tanárok polgári engedetlenségbe kezdtek. A megtorló elbocsátásokra válaszul diákok és szülők tízezrei vontak élőláncot az iskolák köré.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a kormány rendeleti úton lényegében megsemmisítette a pedagógusok sztrájkjogát – előírva, hogy a sztrájk alatt is kötelező a tanórák jelentős részét megtartani –, a magyar oktatás dolgozói történelmi döntés elé kerültek. A törvényes érdekérvényesítés csatornáit a hatalom szisztematikusan elzárta."},
                    {"type": "dialogue", "speaker": "Gimnáziumi tanár", "text": "Erkölcsi imperatívuszként éltük meg a döntést: ha a törvényes sztrájkjogot elrabolják tőlünk, nem maradt más eszközünk, mint a békés polgári engedetlenség. Nem rombolni akartunk, hanem megmutatni, hogy szabad oktatás nélkül nincs szabad ország."},
                    {"type": "narration", "text": "A hatalom válasza a nyers megfélemlítés volt: neves budapesti és vidéki gimnáziumok legelismertebb mesterpedagógusait bocsátották el rendkívüli felmentéssel. Ám a megtorlás nem hozott csendet: másnap reggel diákok és szülők tízezrei fontak élőláncot az iskolák köré, hidakat foglaltak el, s az egész társadalmat megrengető szolidaritási mozgalom indult útjára."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi váltotta ki a magyar pedagógusok polgári engedetlenségi mozgalmát?", [
                    "A kormányrendelet, amely adminisztratív eszközökkel gyakorlatilag ellehetetlenítette az érdemi sztrájkjog gyakorlását.",
                    "A nyári iskolai szünetek hosszának csökkentése két nappal.",
                    "A pedagógusok kötelező sportfoglalkozásainak bevezetése."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A sztrájkjog adminisztratív ellehetetlenítésére _____, a pedagógusok a polgári engedetlenség eszközéhez nyúltak. (in response / válaszul)", "válaszul", "In response to the administrative crippling of the right to strike, teachers reached for the tool of civil disobedience.", ["c1-discourse-civil-disobedience-framing"]),
                match("vocabulary", "controlled", [
                    ["polgári engedetlenség", "a lelkiismereti alapú, békés, nyilvános törvényszegés a jogtalanság leleplezésére"],
                    ["élőlánc", "polgárok egymás kezét fogó, fizikai szolidaritást kifejező tiltakozása"],
                    ["rendkívüli felmentés", "a munkaviszony azonnali, büntető jellegű megszüntetése a hatalom által"],
                    ["sztrájkjog korlátozása", "a munkabeszüntetés törvényes lehetőségének felszámolása rendeletekkel"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A jogállamiság szempontjából _____ a pedagógusok elbocsátása a hatalmi megfélemlítés eszköze volt. (viewed / nézve)", "nézve", "Viewed from the perspective of the rule of law, dismissing the teachers was a tool of autocratic intimidation.", ["c1-discourse-civil-disobedience-framing"]),
                sb("grammar", "practice", ["A", "hatalmi", "megfélemlítésre", "válaszul", "a", "diákok", "szolidaritási", "élőláncot", "alkottak."], ["A", "hatalmi", "megfélemlítésre", "válaszul", "a", "diákok", "szolidaritási", "élőláncot", "alkottak."], "In response to autocratic intimidation, students formed a solidarity human chain.", ["c1-discourse-civil-disobedience-framing"]),
                dc("dialogue", [
                    {"speaker": "Diákvezető", "text": "Miért álltunk ki a tanáraink mellett az élőláncban?"},
                    {"speaker": "Tanár", "text": "Mert erkölcsi kötelességként megélve az ellenállást, megértettétek, hogy az iskola jövője a ti _____ záloga."},
                    {"speaker": "Diákvezető", "text": "Nem hagyjuk, hogy elhallgattassák a tanárainkat."}
                ], ["szabadságotok", "gazdagságotok", "kényelmetek"], 0, ["c1-discourse-civil-disobedience-framing"]),
                sw("production", [{"prompt": "Write a sentence framing civil disobedience using a discourse marker.", "answer": "A törvényes sztrájkjog szisztematikus felszámolására válaszul és a jogállamiság alapelveiből kiindulva a pedagógusok polgári engedetlensége olyan legitim tiltakozás volt, amely leleplezte a hatalmi önkény megfélemlítő természetét."}], ["c1-discourse-civil-disobedience-framing"]),
                mc("grammar", "check", "Melyik diskurzusjelölő keretezi a polgári engedetlenség legitimitását a legszakszerűbben?", [
                    "A jogállamiság szempontjából nézve és a sztrájkjog kiüresítésére válaszul",
                    "Mivel úgy érezték, hogy nem akarnak dolgozni menni",
                    "Azért, mert az időjárás kedvezett a tüntetésnek"
                ], 0, ["c1-discourse-civil-disobedience-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Defending Local Municipal Autonomy",
            "grammar_title": "Critical Evaluative Adverbials Asserting Grassroots Local Democracy Against Central Autocracy",
            "grammar_skill": "c1-adv-grassroots-municipal-autonomy-critique",
            "goals": [
                "I can analyze municipal autonomy and financial starvation (*önkormányzatiság, forráselvonás, szolidaritási adó, szabad városok szövetsége*).",
                "I can deploy critical evaluative adverbials asserting grassroots local democracy (*önkormányzati szempontból vizsgálva, a decentralizáció elvét agresszívan felszámolva, a helyi közösségeket szándékosan kivéreztetve*).",
                "I can debate fiscal decentralization versus central government coercion."
            ],
            "vocab": [
                {"lemma": "önkormányzati autonómia", "translation": "municipal autonomy", "pos": "expression"},
                {"lemma": "szabad városok szövetsége", "translation": "alliance of free cities", "pos": "expression"},
                {"lemma": "pénzügyi kivéreztetés", "translation": "financial starvation / draining of funds", "pos": "expression"},
                {"lemma": "forráselvonás", "translation": "withdrawal / siphoning of municipal resources", "pos": "noun"},
                {"lemma": "szolidaritási adó", "translation": "solidarity tax (punitive municipal levy)", "pos": "expression"},
                {"lemma": "helyi önszerveződés", "translation": "local grassroots self-organization", "pos": "expression"},
                {"lemma": "közösségi költségvetés", "translation": "participatory budgeting", "pos": "expression"},
                {"lemma": "decentralizáció", "translation": "decentralization", "pos": "noun"}
            ],
            "gr_text1": "Critical evaluative adverbials in municipal politics diagnose centralist overreach and fiscal strangulation: `önkormányzati szempontból vizsgálva` (examined from a municipal perspective), `a helyi autonómiát szándékosan kivéreztetve` (deliberately starving local autonomy), `a pénzügyi forrásokat politikai bosszúból elvonva` (siphoning off financial resources out of political revenge), `a decentralizáció európai elvét agresszívan felszámolva` (aggressively dismantling the European principle of decentralization).",
            "gr_text2": "Example: `A kormány a szolidaritási hozzájárulás drasztikus megemelésével és a forrásokat politikai alapon elvonva büntette az ellenzéki vezetésű településeket`.",
            "gr_table": [
                ["A forrásokat szándékosan elvonva a központosító hatalom a városokat bünteti.", "Deliberately withdrawing funds the centralizing power punishes cities."],
                ["Önkormányzati szempontból vizsgálva az önálló gazdálkodás a demokrácia feltétele.", "Examined from a municipal perspective autonomous finance is the precondition of democracy."],
                ["A helyi közösségek önszerveződését támogatva védhető meg a szabadság.", "Supporting the self-organization of local communities freedom can be protected."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-02-helyi-kozossegek-onkormanyzatisag",
                "title": "A szabad városok küzdelme: Autonómia a kivéreztetés ellen",
                "summary": "A 2019-es önkormányzati áttörés után a kormányzat célzott forráselvonásokkal és a szolidaritási adó tízszeresére emelésével próbálta megtörni a független városokat, ám a helyi közösségek önszerveződése ellenállt.",
                "paragraphs": [
                    {"type": "narration", "text": "A 2019-es önkormányzati választásokon a magyar választók Budapesten és számos nagyvárosban megtörték a kormánypárt monolit uralmát. A központosító államhatalom válasza azonnali volt: megkezdődött a független önkormányzatok szisztematikus gazdasági kivéreztetése."},
                    {"type": "dialogue", "speaker": "Városvezető", "text": "A veszélyhelyzet ürügyén elvonták a helyi adóbevételeket, megtiltották az önálló díjemeléseket, és a szolidaritási hozzájárulás címén milliárdokat szivattyúztak el a városainkból. A cél világos volt: működésképtelenné tenni a helyi demokráciát."},
                    {"type": "narration", "text": "A városok azonban összefogtak: a Szabad Városok Szövetsége és a közvetlen brüsszeli forrásokért folytatott küzdelem új dimenziót nyitott. A közösségi költségvetések révén a polgárok közvetlenül dönthettek fejlesztésekről, megerősítve, hogy a demokrácia alapja a helyi önszerveződés."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan próbálta meg a centrális hatalom megtörni a független önkormányzatokat?", [
                    "A hatáskörök elvonásával, a 'szolidaritási adó' drasztikus megemelésével és célzott pénzügyi kivéreztetéssel.",
                    "Új villamosvonalak ingyenes átadásával és többlettámogatásokkal.",
                    "A polgármesterek fizetésének megkétszerezésével."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A központi kormány a pénzügyi forrásokat szándékosan _____ próbálta térdre kényszeríteni a független városokat. (withdrawing / elvonva)", "elvonva", "Deliberately withdrawing financial resources, the central government tried to bring independent cities to their knees.", ["c1-adv-grassroots-municipal-autonomy-critique"]),
                match("vocabulary", "controlled", [
                    ["önkormányzati autonómia", "a helyi települések független döntéshozatali és gazdálkodási joga"],
                    ["pénzügyi kivéreztetés", "a működéshez szükséges bevételek elvonása politikai céllal"],
                    ["szabad városok szövetsége", "a demokratikus önkormányzatok együttműködése a központosítás ellen"],
                    ["közösségi költségvetés", "a lakosság közvetlen döntése a városi források egy részének felhasználásáról"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A helyi autonómiát agresszívan _____ a hatalom a tanácsrendszer központosítását állította vissza. (dismantling / felszámolva)", "felszámolva", "Aggressively dismantling local autonomy, the regime restored the centralization of the council system.", ["c1-adv-grassroots-municipal-autonomy-critique"]),
                sb("grammar", "practice", ["A", "forrásokat", "elvonva", "a", "hatalom", "a", "helyi", "demokráciát", "gyengíti."], ["A", "forrásokat", "elvonva", "a", "hatalom", "a", "helyi", "demokráciát", "gyengíti."], "Withdrawing resources, the regime weakens local democracy.", ["c1-adv-grassroots-municipal-autonomy-critique"]),
                dc("dialogue", [
                    {"speaker": "Polgármester", "text": "Hogyan működhet a város, ha elvonják a bevételeink jelentős részét?"},
                    {"speaker": "Városfejlesztő", "text": "Úgy, hogy a polgárokat bevonva és a közösségi költségvetést működtetve megvédjük a helyi _____."},
                    {"speaker": "Polgármester", "text": "Az önkormányzatiság nem ajándék, hanem alkotmányos alapjog."}
                ], ["autonómiát", "központosítást", "fővárost"], 0, ["c1-adv-grassroots-municipal-autonomy-critique"]),
                sw("production", [{"prompt": "Write a critical sentence diagnosing municipal centralization using an evaluative adverbial.", "answer": "A pénzügyi forrásokat szándékosan elvonva és a szolidaritási adót politikai fegyverként használva a központi hatalom az önkormányzati autonómia elsorvasztására törekszik, megsértve a szubszidiaritás európai alapelvét."}], ["c1-adv-grassroots-municipal-autonomy-critique"]),
                mc("grammar", "check", "Melyik határozói szerkezet fejezi ki a helyi demokrácia autonómiájának elvét?", [
                    "A pénzügyi forrásokat politikai bosszúból szándékosan elvonva",
                    "Amikor a városházán nem égtek a lámpák este",
                    "Minden városban nagyon szép virágokat ültettek a tavaszon"
                ], 0, ["c1-adv-grassroots-municipal-autonomy-critique"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Ecological Sovereignty and Citizen Resistance",
            "grammar_title": "Deontic Modal Structures Formulating Citizens Duty of Ecological Defense",
            "grammar_skill": "c1-modal-deontic-environmental-sovereignty",
            "goals": [
                "I can analyze environmental conflicts, battery mega-factories, and water resource defense (*akkumulátorgyár, talajvízszennyezés, kiemelt beruházás, ökológiai önrendelkezés*).",
                "I can formulate deontic modal structures asserting ecological sovereignty and constitutional environmental rights (*meg kell védenünk a termőföldeket és a vízkészletet, az államnak kötelező garantálnia az egészséges környezethez való jogot*).",
                "I can critique executive overriding of environmental licensing and local democratic consultation."
            ],
            "vocab": [
                {"lemma": "ökológiai önrendelkezés", "translation": "ecological self-determination", "pos": "expression"},
                {"lemma": "akkumulátorgyár", "translation": "battery factory / gigafactory", "pos": "noun"},
                {"lemma": "talajvízszennyezés", "translation": "groundwater pollution", "pos": "noun"},
                {"lemma": "kiemelt beruházás", "translation": "priority government project (exempt from local rules)", "pos": "expression"},
                {"lemma": "környezethasználati engedély", "translation": "environmental usage permit", "pos": "expression"},
                {"lemma": "termőföldvédelem", "translation": "protection of arable land", "pos": "noun"},
                {"lemma": "lakossági tiltakozás", "translation": "grassroots citizen protest", "pos": "expression"},
                {"lemma": "közmeghallgatás", "translation": "public hearing", "pos": "noun"}
            ],
            "gr_text1": "Deontic modal structures asserting ecological defense and intergenerational justice formulate civic imperatives: `meg kell védenünk a jövő generációk vízkészletét` (we must protect the water resources of future generations), `az államnak kötelező garantálnia az egészséges környezethez való jogot` (the state is obliged to guarantee the right to a healthy environment), `nem engedhető meg a termőföldek feláldozása ipari spekulációért` (sacrificing arable land for industrial speculation cannot be permitted).",
            "gr_text2": "Example: `A helyi lakosságnak elidegeníthetetlen joga van tudni, milyen veszélyes anyagokat bocsátanak ki a gyárak, és az államnak kötelező érvényesítenie a szigorú határértékeket`.",
            "gr_table": [
                ["Meg kell védenünk a karsztvizeket és a termőföldeket a veszélyes ipari beruházásoktól.", "We must protect karst waters and arable land from hazardous industrial investments."],
                ["A kormánynak kötelező tiszteletben tartania az Alaptörvény környezetvédelmi cikkét.", "The government is obliged to respect the environmental article of the Fundamental Law."],
                ["Nem engedhető meg, hogy a lakosság feje felett, titokban döntsenek veszélyes gyárakról.", "It cannot be permitted that hazardous factories are decided upon secretly over citizens' heads."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-03-kornyezetvedelem-akkumulatorgyarak",
                "title": "Víz és termőföld: A helyi közösségek ökológiai önvédelme",
                "summary": "Magyarország a lakosság megkérdezése nélkül vált az ázsiai akkumulátorgyárak célpontjává. Debrecenben és Gödön a polgárok a közmeghallgatásokon és a bíróságokon védték meg a vizet és a földet.",
                "paragraphs": [
                    {"type": "narration", "text": "A kormányzat önkényes iparpolitikája nyomán Magyarország óriási ázsiai akkumulátorgyárak telephelyévé vált. Debrecenben, Gödön, Iváncsán és Komáromban tízezer hektáros kiváló termőföldeket betonoznak le, s a gyárak elképesztő víz- és energiaigénye közvetlenül veszélyezteti az ivóvízbázisokat."},
                    {"type": "dialogue", "speaker": "Debreceni civil aktivista", "text": "A kormánynak kötelező lenne megvédenie a vízkincsünket, ehelyett kiemelt beruházássá nyilvánítva megkerülik a környezetvédelmi hatóságokat. Nem engedhetjük meg, hogy a gyermekeink jövőjét és az unokáink vizét külföldi konszernek profitjáért áldozzák fel."},
                    {"type": "narration", "text": "A botrányos debreceni közmeghallgatásokon a helyi lakosok dacos kiállása megingatta a rezsim magabiztosságát. A független mérések, amelyek Gödön mérgező oldószert mutattak ki a kutakban, országos ökológiai ébredést indítottak el: a környezetvédelem az önrendelkezés szent ügyévé vált."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tiltakoznak a helyi lakosok az akkumulátorgyárak terjeszkedése ellen?", [
                    "A hatalmas vízigény, a termőföldek elvétele és a mérgező anyagok talajvízbe jutásának reális kockázata miatt.",
                    "Mert a gyárak túl sok napelemet telepítenek a tetőkre.",
                    "Mert nem tetszik nekik a gyárépületek szürke színe."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Az államnak kötelessége _____ a polgárok alkotmányos jogát az egészséges környezethez. (to guarantee / garantálnia)", "garantálnia", "The state has a duty to guarantee citizens' constitutional right to a healthy environment.", ["c1-modal-deontic-environmental-sovereignty"]),
                match("vocabulary", "controlled", [
                    ["ökológiai önrendelkezés", "a helyi közösség joga saját természeti környezetének megóvására"],
                    ["kiemelt beruházás", "kormányzati döntés, amely felmenti a projektet a helyi építési és környezeti szabályok alól"],
                    ["talajvízszennyezés", "veszélyes ipari vegyszerek és oldószerek bejutása az ivóvízbázisba"],
                    ["közmeghallgatás", "törvényileg előírt lakossági fórum a környezeti hatások megvitatására"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Minden felelős társadalomnak meg _____ védenie az ivóvízbázisait a profitorientált mérgezéstől. (must / kell)", "kell", "Every responsible society must protect its drinking water reserves from profit-oriented poisoning.", ["c1-modal-deontic-environmental-sovereignty"]),
                sb("grammar", "practice", ["Meg", "kell", "védenünk", "a", "termőföldeket", "és", "a", "tiszta", "ivóvizet."], ["Meg", "kell", "védenünk", "a", "termőföldeket", "és", "a", "tiszta", "ivóvizet."], "We must protect the arable lands and clean drinking water.", ["c1-modal-deontic-environmental-sovereignty"]),
                dc("dialogue", [
                    {"speaker": "Környezetvédő", "text": "Hogyan akadályozhatjuk meg az ivóvízbázisaink elszennyezését?"},
                    {"speaker": "Jogvédő", "text": "Úgy, hogy fel kell lépnünk a hatóságok mulasztása ellen, és nem szabad engednünk a közmeghallgatások _____."},
                    {"speaker": "Környezetvédő", "text": "A tiszta víz nemzeti kincs, nem eladó nyersanyag."}
                ], ["eltörlését", "megtartását", "javítását"], 0, ["c1-modal-deontic-environmental-sovereignty"]),
                sw("production", [{"prompt": "Write a sentence formulating the civic duty of ecological defense using a deontic modal.", "answer": "Minden öntudatos polgárnak és felelős közösségnek feltétlenül kötelessége megvédenie a nemzeti ivóvízkincset és a termőföldeket, és az államnak haladéktalanul be kell tiltania a környezetvédelmi garanciák nélküli kiemelt beruházásokat."}], ["c1-modal-deontic-environmental-sovereignty"]),
                mc("grammar", "check", "Melyik mondat alkalmaz deontikus modális struktúrát az ökológiai felelősség kifejezésére?", [
                    "Meg kell védenünk a természeti erőforrásokat a jövő nemzedékek számára",
                    "A fák zöldek a parkban tavasszal és nyáron",
                    "Néha jó lenne eső, de ma nem esik az eső"
                ], 0, ["c1-modal-deontic-environmental-sovereignty"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Principles of the Democratic Minimum",
            "grammar_title": "Proportional Correlative Structures Mapping Civic Resistance Against Authoritarian Decay",
            "grammar_skill": "c1-adv-proportional-civic-resistance-renewal",
            "goals": [
                "I can analyze the structural consensus of the Democratic Minimum (*demokratikus minimum, fékek és ellensúlyok, sajtószabadság, antikorrupciós ügyészség, arányos választási rendszer*).",
                "I can construct proportional correlative structures mapping institutional decay and democratic rebuilding (*minél mélyebbre süllyed a rendszer a korrupcióban, annál elengedhetetlenebbé válik a jogállami minimum; minél szélesebb a civil konszenzus, annál biztosabb a megújulás*).",
                "I can debate the non-negotiable legal and moral foundations required to restore constitutional democracy."
            ],
            "vocab": [
                {"lemma": "demokratikus minimum", "translation": "Democratic Minimum", "pos": "expression"},
                {"lemma": "fékek és ellensúlyok", "translation": "checks and balances", "pos": "expression"},
                {"lemma": "sajtószabadság", "translation": "freedom of the press", "pos": "noun"},
                {"lemma": "független igazságszolgáltatás", "translation": "independent judiciary", "pos": "expression"},
                {"lemma": "antikorrupciós ügyészség", "translation": "anti-corruption prosecution office", "pos": "expression"},
                {"lemma": "arányos választási rendszer", "translation": "proportional electoral system", "pos": "expression"},
                {"lemma": "átláthatóság", "translation": "transparency", "pos": "noun"},
                {"lemma": "közbizalom", "translation": "public trust", "pos": "noun"}
            ],
            "gr_text1": "Proportional correlative structures (`minél..., annál...` / `amivel..., annál...`) map civic mobilization directly against authoritarian decay: `minél inkább elnyomja a hatalom az autonóm intézményeket, annál erősebbé válik a polgári ellenállás` (the more power suppresses autonomous institutions, the stronger civic resistance becomes), `minél átláthatóbbá tesszük a közpénzek elköltését, annál gyorsabban áll helyre a társadalmi bizalom` (the more transparent we make the spending of public funds, the faster public trust is restored).",
            "gr_text2": "Example: `Minél szélesebb körben fogadják el a demokratikus minimum alapelveit, annál biztosabb garanciát kap a nemzet az önkényuralom visszatérése ellen`.",
            "gr_table": [
                ["Minél mélyebb a politikai válság, annál világosabbá válik a demokratikus minimum szükségessége.", "The deeper the political crisis, the clearer becomes the necessity of the democratic minimum."],
                ["Minél szilárdabbak a fékek és ellensúlyok, annál kevésbé alakulhat ki autokrácia.", "The firmer the checks and balances, the less an autocracy can emerge."],
                ["Amivel nagyobb a civil szolidaritás, annál tehetetlenebb a megfélemlítő hatalom.", "The greater the civic solidarity, the more helpless the intimidating regime."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-04-demokratikus-minimum-alapelvek",
                "title": "A köztársaság fundamentuma: A Demokratikus Minimum",
                "summary": "A civil társadalom és az alkotmányjogászok megfogalmazták a Demokratikus Minimum sarkalatos pontjait: független igazságszolgáltatás, tiszta választások, szabad sajtó és csatlakozás az Európai Ügyészséghez.",
                "paragraphs": [
                    {"type": "narration", "text": "A hibrid rezsim másfél évtizedes uralma után a magyar civil társadalom, az alkotmányjogászok és a független értelmiség felismerte: a pusztán pártpolitikai küzdelmek önmagukban nem hozhatnak rendszerváltást. Létre kellett hozni a 'Demokratikus Minimum' chartáját – azokat a vitathatatlan alapelveket, amelyek nélkül nincs szabad és igazságos társadalom."},
                    {"type": "dialogue", "speaker": "Alkotmányjogász", "text": "Minél tovább halogatjuk az alapelvek rögzítését, annál mélyebbre süllyed az ország. A minimum négy sérthetetlen pilléren nyugszik: a független bíróságokon, a sajtó pártpropaganda alóli felszabadításán, a választási törvény arányosításán és az Európai Ügyészséghez való azonnali csatlakozáson."},
                    {"type": "narration", "text": "A Demokratikus Minimum nem jobb- vagy baloldali ideológia, hanem a köztársaság létezésének elemi feltétele. Ahogyan a nyilatkozat összegzi: amíg ezek az intézményi garanciák nem valósulnak meg, addig a nemzet nem szabad polgárok közössége, csupán a hatalom foglya a saját hazájában."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Melyek a 'Demokratikus Minimum' legfontosabb sarokkövei?", [
                    "A független bíróságok, a sajtószabadság, az arányos választási rendszer és a rendszerszintű korrupció elleni független fellépés.",
                    "A kötelező katonai szolgálat és a külföldi utazások korlátozása.",
                    "Az állami televízió egyeduralmának fenntartása és a magánmédia betiltása."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Minél jobban átlátható a közpénzek elköltése, _____ kevésbé tud terjedni a korrupció. (the less / annál)", "annál", "The more transparent the spending of public funds, the less corruption can spread.", ["c1-adv-proportional-civic-resistance-renewal"]),
                match("vocabulary", "controlled", [
                    ["demokratikus minimum", "azok az alapvető jogállami normák, amelyekről nem köthető politikai kompromisszum"],
                    ["fékek és ellensúlyok", "a hatalmi ágak szétválasztásának és kölcsönös kontrolljának rendszere"],
                    ["antikorrupciós ügyészség", "a politikai bűncselekményeket a kormánytól függetlenül vizsgáló hatóság"],
                    ["arányos választási rendszer", "a leadott szavazatok arányát híven tükröző parlamenti mandátummegosztás"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "_____ erősebb a civil kontroll, annál szilárdabbak a demokratikus garanciák. (The stronger / Minél)", "Minél", "The stronger the civic control, the firmer the democratic guarantees.", ["c1-adv-proportional-civic-resistance-renewal"]),
                sb("grammar", "practice", ["Minél", "erősebb", "a", "társadalom,", "annál", "gyengébb", "az", "önkényuralom."], ["Minél", "erősebb", "a", "társadalom,", "annál", "gyengébb", "az", "önkényuralom."], "The stronger society is, the weaker autocracy becomes.", ["c1-adv-proportional-civic-resistance-renewal"]),
                dc("dialogue", [
                    {"speaker": "Jogvédő", "text": "Miért nem elegendő egy egyszerű kormányváltás a jogállam helyreállításához?"},
                    {"speaker": "Alkotmánybíró", "text": "Mert minél mélyebben beépült az államfoglyul ejtés az intézményekbe, annál nélkülözhetetlenebb a demokratikus minimum alkotmányos _____."},
                    {"speaker": "Jogvédő", "text": "Az alapokat kell újraépíteni, nemcsak a homlokzatot lefesteni."}
                ], ["garanciája", "eltörlése", "kifosztása"], 0, ["c1-adv-proportional-civic-resistance-renewal"]),
                sw("production", [{"prompt": "Write a sentence formulating the relationship between civic solidarity and democratic renewal using a proportional correlative structure.", "answer": "Minél szélesebb körű konszenzus teremti meg a demokratikus minimum tiszteletben tartását, annál megkérdőjelezhetetlenebbé válik a független igazságszolgáltatás és az alkotmányos fékek rendszere Magyarországon."}], ["c1-adv-proportional-civic-resistance-renewal"]),
                mc("grammar", "check", "Melyik szerkezet valósít meg arányos korrelatív összefüggést a C1 szinten?", [
                    "Minél átláthatóbb a választási rendszer, annál erősebb a polgárok bizalma a parlamentben",
                    "A parlamentben sok képviselő ült és mindannyian szavaztak",
                    "Ha van időnk délután, elolvassuk a napilapokat"
                ], 0, ["c1-adv-proportional-civic-resistance-renewal"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "The Horizon of a European Hungary",
            "grammar_title": "Evaluative Conclusive Particles Declaring Irrepressible Horizon of European Hungarian Democracy",
            "grammar_skill": "c1-adv-conclusive-democratic-horizon",
            "goals": [
                "I can formulate the long-term vision of a democratic, European Hungary (*európai horizont, transzatlanti integráció, jogállami elkötelezettség, cselekvő remény*).",
                "I can employ elevated conclusive particles declaring irrepressible democratic horizons (*végső soron, mindent egybevetve, feltartóztathatatlanul, megkérdőjelezhetetlenül arra mutatva, hogy a magyar jövő európai jövő*).",
                "I can summarize the entire C1 Discourse Track in a vision of civic courage and democratic renewal."
            ],
            "vocab": [
                {"lemma": "európai horizont", "translation": "European horizon", "pos": "expression"},
                {"lemma": "demokratikus Magyarország", "translation": "democratic Hungary", "pos": "expression"},
                {"lemma": "jogállami integráció", "translation": "rule-of-law integration", "pos": "expression"},
                {"lemma": "transzatlanti szövetség", "translation": "transatlantic alliance", "pos": "expression"},
                {"lemma": "cselekvő remény", "translation": "active hope", "pos": "expression"},
                {"lemma": "félelem nélküli társadalom", "translation": "society without fear", "pos": "expression"},
                {"lemma": "szolidaritás kultúrája", "translation": "culture of solidarity", "pos": "expression"},
                {"lemma": "polgári jövő", "translation": "civic future", "pos": "expression"}
            ],
            "gr_text1": "Conclusive evaluative particles and conclusive clause-linkers crystallize irreversible democratic horizons and moral closure: `végső soron` (ultimately / in the final analysis), `mindent egybevetve` (all things considered), `feltartóztathatatlanul` (unstoppably / irrepressibly), `kétséget kizáróan arra engedve következtetni` (allowing one to conclude beyond doubt), `a történelmi fejlődés megmásíthatatlan iránya szerint` (according to the immutable direction of historical progress).",
            "gr_text2": "Example: `Végső soron Magyarország sorsa feltartóztathatatlanul az európai demokratikus közösséghez tartozik, mert a nemzet soha nem mond le a szabadságról`.",
            "gr_table": [
                ["Végső soron a szabadság szeretete és a szolidaritás győzedelmeskedik a félelem felett.", "Ultimately the love of freedom and solidarity triumphs over fear."],
                ["Mindent egybevetve a magyar társadalom európai elkötelezettsége megingathatatlan.", "All things considered, Hungarian society's European commitment is steadfast."],
                ["Feltartóztathatatlanul kirajzolódik egy új, demokratikus és szolidáris polgári jövő.", "Unstoppably emerges a new, democratic and solidary civic future."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-05-europai-magyarorszag-jovo",
                "title": "Európai horizont: A cselekvő remény köztársasága",
                "summary": "Magyarország ezeréves történelme elválaszthatatlan Európától. Az autoriter kitérők után végső soron a cselekvő remény és a polgári szolidaritás teremti meg az új, szabad köztársaságot.",
                "paragraphs": [
                    {"type": "narration", "text": "Magyarország történelme több mint ezer éve Európa szerves része. Szent István királytól a reformkor nagyjain, 1956 hősein és a vasfüggöny 1989-es lebontásán át a nemzet mindannyiszor a nyugati polgári civilizáció, a szabadság és az emberi méltóság mellett tette le voksát."},
                    {"type": "dialogue", "speaker": "Európai parlamenti képviselő", "text": "Végső soron mindent egybevetve és a történelem távlatát vizsgálva: a magyar társadalom szíve európai szív. Az autoriter hatalmi kísérletek múló epizódok; a fiatalok szabadságvágya és a tanárok kiállása megállíthatatlanul az európai jogállam felé mutat."},
                    {"type": "narration", "text": "A szabadság nem adomány, hanem mindennapi felelősség: tanárok bátorsága a katedrán, polgárok szolidaritása az utcákon, közösségek harca a tiszta vízért és a szabad sajtóért. Ez a cselekvő remény az az elpusztíthatatlan kőszikla, amelyre a jövő szabad, európai és virágzó Magyarországa felépül."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinthető Magyarország jövője elválaszthatatlannak az európai demokratikus közösségtől?", [
                    "Mert ezeréves történelme, szellemi öröksége és a polgári szabadság iránti rendíthetetlen vágya megmásíthatatlanul Európához köti.",
                    "Mert a kontinens térképén nem lehet áthelyezni az országot Ázsiába.",
                    "Mert az európai utakon nincsenek sebességkorlátozások."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "_____ soron a polgári bátorság és a szolidaritás erősebbnek bizonyul a hatalmi elnyomásnál. (Ultimately / Végső)", "Végső", "Ultimately civic courage and solidarity prove stronger than autocratic oppression.", ["c1-adv-conclusive-democratic-horizon"]),
                match("vocabulary", "controlled", [
                    ["európai horizont", "a nyugati demokráciákhoz, az emberi jogokhoz és a szolidaritáshoz való elkötelezettség"],
                    ["cselekvő remény", "nem tétlen várakozás, hanem mindennapi aktív munka a szabad jövőért"],
                    ["félelem nélküli társadalom", "ahol a hatalom nem tarthatja rettegésben a polgárokat véleményük miatt"],
                    ["szolidaritás kultúrája", "az elesettek és az üldözöttek melletti kölcsönös kiállás közösségi etikája"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Mindent egybevetve Magyarország jövője _____ az európai demokratikus értékek talaján áll. (irrevocably / feltartóztathatatlanul)", "feltartóztathatatlanul", "All things considered Hungary's future stands irrevocably on the foundation of European democratic values.", ["c1-adv-conclusive-democratic-horizon"]),
                sb("grammar", "practice", ["Végső", "soron", "a", "szabad", "Magyarország", "az", "európai", "értékekre", "épül."], ["Végső", "soron", "a", "szabad", "Magyarország", "az", "európai", "értékekre", "épül."], "Ultimately free Hungary is built upon European values.", ["c1-adv-conclusive-democratic-horizon"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Van remény arra, hogy Magyarország újra virágzó jogállammá váljon?"},
                    {"speaker": "Professzor", "text": "Igen, mert végső soron a szabadság szeretete a nemzet DNS-ében él, és ez a cselekvő remény _____ fogja a jövőt."},
                    {"speaker": "Egyetemi hallgató", "text": "A jövő a mi kezünkben van."}
                ], ["megváltoztatni", "elrontani", "megállítani"], 0, ["c1-adv-conclusive-democratic-horizon"]),
                sw("production", [{"prompt": "Write a capstone conclusive sentence declaring the European future of Hungary using a conclusive particle.", "answer": "Végső soron mindent egybevetve és a történelmi tapasztalatokat mérlegelve feltartóztathatatlanul bizonyos, hogy a magyar nép szabadságvágya legyőzi az önkényt, és Magyarország büszke, szilárd jogállamként foglalja el méltó helyét az európai nemzetek közösségében."}], ["c1-adv-conclusive-democratic-horizon"]),
                mc("grammar", "check", "Melyik konkluzív kifejezés összegzi a legünnepélyesebben a C1 tanterv záró horizontját?", [
                    "Végső soron mindent egybevetve és feltartóztathatatlanul az európai értékek mellett állva",
                    "Szóval nagyjából ennyi volt, amit el akartunk mondani a témáról",
                    "Talán egyszer majd minden sokkal jobb lesz valahogyan"
                ], 0, ["c1-adv-conclusive-democratic-horizon"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(36, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-demokratikus-minimum-jovo.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "A demokratikus minimum: Civil társadalom, ellenállás és az európai jövő",
            "level": "C1",
            "lesson": 5,
            "order": 36,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-democratic-horizon"],
            "summary": "Átfogó összefoglaló a kortárs magyar civil társadalom és jogállamiság küzdelmeiről: a pedagógusok polgári engedetlenségéről és a szolidaritási élőláncokról, a szabad önkormányzatok küzdelméről a pénzügyi kivéreztetés ellen, a helyi közösségek ökológiai önrendelkezéséről az akkumulátorgyárakkal szemben, a Demokratikus Minimum alkotmányos alapelveiről, valamint Magyarország feltartóztathatatlan európai jövőjéről.",
            "vocabularyTopics": [
                "The Democratic Minimum: Civil Society, Resistance & The European Horizon",
                "Principles of the Democratic Minimum & Constitutional Governance"
            ],
            "paragraphs": [
                {"type": "narration", "text": "Amikor a hatalom adminisztratív rendeletekkel felszámolta a sztrájkjogot, a magyar pedagógusok a békés polgári engedetlenség eszközéhez nyúltak. A megtorló elbocsátásokra válaszul diákok és szülők tízezrei vontak élőláncot az iskolák köré, bebizonyítva, hogy a polgári szolidaritás erősebb a megfélemlítésnél."},
                {"type": "narration", "text": "Ezzel párhuzamosan a szabad városok önkormányzatai a brutális forráselvonások és a büntető szolidaritási adók ellenére megvédték a helyi demokráciát. A közösségi költségvetések és a decentralizáció védelme megmutatta, hogy a köztársaság igazi fundamentuma a helyi önszerveződésben rejlik."},
                {"type": "narration", "text": "A környezetvédelem területén Debrecen, Göd és más települések lakói határozottan szembeszálltak a veszélyes akkumulátorgyárak önkényes telepítésével. A termőföldek és a tiszta ivóvízkészlet védelme az ökológiai önrendelkezés nemzeti ügyévé vált."},
                {"type": "narration", "text": "A civil társadalom és az alkotmányjogászok megalkották a Demokratikus Minimumot: a független bíróságok, a szabad sajtó, az arányos választási rendszer és az Európai Ügyészséghez való csatlakozás vitathatatlan követelményét."},
                {"type": "narration", "text": "Végső soron mindent egybevetve: Magyarország ezeréves európai elkötelezettsége megingathatatlan. A cselekvő remény, a szabadság szeretete és a polgári bátorság feltartóztathatatlanul megteremti az új, szabad, demokratikus és szolidáris magyar köztársaságot."}
            ]
        }
    )

    # Discourse Consolidation Lesson (12 exercises: 3 recognize, 3 recall, 3 context, 3 produce)
    emit_consolidation_lesson(
        36,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can master the high-level critical discourse of civil disobedience, municipal resistance, ecological defense, and the Democratic Minimum.",
            "I can employ discourse framing markers, critical municipal adverbials, deontic environmental modals, proportional correlatives, and conclusive particles.",
            "I have synthesized the full scope of the Hungarian C1 Dual-Track Curriculum in active civic defense of democracy."
        ],
        [
            mc("grammar", "recognize", "Melyik diskurzusjelölő keretezi a polgári engedetlenség jogállami legitimitását a leghitelesebben?", [
                "a jogállamiság szempontjából nézve és a sztrájkjog ellehetetlenítésére válaszul",
                "amikor a tanárok nem akartak bemenni a terembe tanítani",
                "hogyha valakinek rossz kedve van reggel az iskolában"
            ], 0, ["c1-discourse-civil-disobedience-framing"]),
            mc("grammar", "recognize", "Milyen szerkezettel bírálható a települések pénzügyi kivéreztetése a legszakszerűbben?", [
                "a pénzügyi forrásokat politikai bosszúból szándékosan elvonva és az autonómiát megsértve",
                "amikor a polgármester kevesebb pénzt kap a boltban",
                "ha a városokban lekapcsolják a lámpákat éjfél után"
            ], 0, ["c1-adv-grassroots-municipal-autonomy-critique"]),
            match("vocabulary", "recognize", [
                ["polgári engedetlenség", "lelkiismereti alapú békés kiállás a jogfosztó szabályokkal szemben"],
                ["önkormányzati autonómia", "a helyi közösségek önrendelkezése a központi elvonások ellenére"],
                ["ökológiai önrendelkezés", "a termőföld és a tiszta ivóvízkészlet védelme az ipari szennyezéstől"],
                ["demokratikus minimum", "a fékek és egyensúlyok, a sajtószabadság és a tiszta közélet elengedhetetlen alapelvei"]
            ], [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A polgárok szolidaritásának leglátványosabb formája a budapesti iskolákat körülvevő _____ volt. (human chain / élőlánc)", "élőlánc", "The most spectacular form of citizens' solidarity was the human chain surrounding Budapest schools.", [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A helyi demokrácia jövőjének záloga a polgárok közvetlen bevonása a közösségi _____ révén. (participatory budgeting / költségvetés)", "költségvetés", "The pledge of local democracy's future is involving citizens directly through participatory budgeting.", [f"c1-{slug}-vocab"]),
            fb("grammar", "recall", "A sztrájkjog adminisztratív megsemmisítésére _____, a tanárok polgári engedetlenséget hirdettek. (in response / válaszul)", "válaszul", "In response to the administrative destruction of the right to strike, teachers announced civil disobedience.", ["c1-discourse-civil-disobedience-framing"]),
            fb("grammar", "context", "Az államnak kötelező _____ a lakosság egészséges környezethez való alapjogát. (to guarantee / garantálnia)", "garantálnia", "The state is obliged to guarantee the population's fundamental right to a healthy environment.", ["c1-modal-deontic-environmental-sovereignty"]),
            fb("grammar", "context", "Minél szélesebb a civil konszenzus, _____ biztosabb a jogállam megújulása. (the / annál)", "annál", "The wider civic consensus is, the more certain the renewal of the rule of law.", ["c1-adv-proportional-civic-resistance-renewal"]),
            mc("grammar", "context", "Mi a Demokratikus Minimum legfőbb intézményi garanciája a korrupcióval szemben?", [
                "A független ügyészség, az Európai Ügyészséghez való csatlakozás és a bíróságok autonómiája.",
                "A minisztériumok létszámának csökkentése.",
                "A készpénzhasználat betiltása az üzletekben."
            ], 0, ["c1-adv-proportional-civic-resistance-renewal"]),
            sb("grammar", "produce", ["Végső", "soron", "a", "szabad", "Magyarország", "az", "európai", "szolidaritásra", "épül."], ["Végső", "soron", "a", "szabad", "Magyarország", "az", "európai", "szolidaritásra", "épül."], "Ultimately free Hungary is built upon European solidarity.", ["c1-adv-conclusive-democratic-horizon"]),
            sw("production", [{"prompt": "Write a critical evaluation of ecological defense using a deontic modal structure.", "answer": "Minden felelős társadalomnak és öntudatos polgárnak kötelező megvédenie a nemzeti ivóvízkincset és a termőföldeket a veszélyes ipari beruházásoktól, és az államnak feltétlenül garantálnia kell a közmeghallgatások és környezeti hatástanulmányok nyilvánosságát."}], ["c1-modal-deontic-environmental-sovereignty"]),
            sw("production", [{"prompt": "Synthesize the entire C1 Discourse Track declaring the European horizon of Hungary using a conclusive particle.", "answer": "Végső soron mindent egybevetve és a civil társadalom rendíthetetlen ellenállását vizsgálva feltartóztathatatlanul bizonyos, hogy a magyar nemzet szabadságszeretete és a demokratikus minimum iránti elkötelezettsége megteremti az európai, szolidáris és büszke köztársaságot."}], ["c1-adv-conclusive-democratic-horizon"])
        ]
    )

    print("=== Finished C1 Unit 36 ===")


if __name__ == "__main__":
    generate_unit_36()
