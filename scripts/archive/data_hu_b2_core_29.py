"""
Hungarian B2 Core Track Unit 29:
  b2-29: Diplomacy, Alliances & Sovereignty
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_29 = {
    "unit_num": 29,
    "title": "Diplomacy, Alliances & Sovereignty",
    "grammar_summary": "Diplomatic conditionals and polite hedging (célszerű lenne, indokolt volna, kívánatosnak tartaná), case government of abstract diplomatic verbs (-ra/-re, -hoz/-hez/-höz, mellett), and multilateral communique drafting.",
    "grammar_skill": "b2-diplomatic-conditionals",
    "vocab_skill": "b2-29-vocab",
    "theme": "Diplomacy, alliances and sovereignty",
    "intro_body": [
        "A diplomácia és a nemzetközi kapcsolatok világa rendkívüli nyelvi pontosságot és kifinomultságot igényel. Az államok közötti egyeztetések során a nyílt konfrontáció helyett a feltételes mód árnyalatai, az udvarias enyhítések (hedging) és a szigorú vonzatok biztosítják a kölcsönös tiszteletet és a diplomáciai mozgásteret.",
        "Ebben a fejezetben megismerheti a diplomáciai feltételes mód és a távolságtartó enyhítés fordulatait (célszerű lenne, indokolt volna, kívánatosnak tartaná), a nemzetközi szerződések legfontosabb vonzatos igéit (törekszik vmire, hozzájárul vmihez, elkötelezi magát vmi mellett), valamint a geopolitikai szövetségek és az állami szuverenitás szókincsét. Bánffy Miklós klasszikus erdélyi regénye, a 'Megszámláltattál...' segítségével a történelmi viharok előtti diplomáciai egyensúlyozás művészetét is átélheti.",
    ],
    "classic_story": {
        "slug": "banffymiklos",
        "author": "Bánffy Miklós",
        "work": "Erdélyi történet: Megszámláltattál... (1934)",
        "title": "Politikai egyensúlyozás a vihar előtt",
        "summary": "Abády Balázs gróf és a külügyminiszter a bécsi Ballhausplatz szalonjában a fenyegető európai háború árnyékában tárgyalnak a Monarchia szövetségi politikájáról és a szuverenitás megőrzéséről.",
        "characters": ["Abády Balázs gróf", "A külügyminiszter"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A bécsi Ballhausplatz aranyozott termeiben nehéz bársonyfüggönyök tompították a külvilág zaját. Abády Balázs gróf a hatalmas barokk ablaknál állva figyelte az érkező diplomáciai hintókat; a balkáni válság fenyegető feszültsége szinte tapintható volt a szalon fojtogató csendjében.",
            },
            {
                "type": "dialogue",
                "speaker": "A külügyminiszter",
                "text": "Kedves Balázs, a nemzetközi helyzet rendkívül kényes. Indokolt volna egyértelmű üzenetet küldenünk a szövetségeseinknek, mégis célszerűbb lenne elkerülni minden olyan lépést, amely nyílt provokációnak minősülhetne.",
            },
            {
                "type": "dialogue",
                "speaker": "Abády Balázs gróf",
                "text": "Kormányunk minden bizonnyal kívánatosnak tartaná a status quo békés fenntartását, excellenciás uram. Ám amennyiben a nagyhatalmak nem törekednének érdemi kompromisszumra, úgy a fegyveres konfliktus elkerülhetetlenné válna a határaink mentén.",
            },
            {
                "type": "narration",
                "text": "A miniszter lassan fel-alá sétált a vastag perzsaszőnyegen. Jól ismerte a Monarchia belső gyengeségeit: a nemzetiségi feszültségek, a parlament merevsége és a német szövetségi elköteleződés alig hagytak önálló diplomáciai mozgásteret a béke megőrzésére.",
            },
            {
                "type": "dialogue",
                "speaker": "A külügyminiszter",
                "text": "Ön szerint a budapesti parlament hozzájárulna a katonai póthitelek megszavazásához, feltéve, hogy a kormány határozottan elkötelezné magát a diplomáciai közvetítés mellett?",
            },
            {
                "type": "dialogue",
                "speaker": "Abády Balázs gróf",
                "text": "A magyar képviselők csak abban az esetben támogatnák ezt az áldozatot, ha garanciát kapnának a nemzeti szuverenitás védelmére. Senki sem szeretné, ha a birodalom külpolitikája idegen katonai érdekek kiszolgálójává válnék.",
            },
            {
                "type": "narration",
                "text": "A két államférfi tekintete összefonódott. Mindketten érezték a történelmi felelősség súlyát: a kimért diplomáciai fordulatok, a finom feltételes szerkezetek mögött népek sorsa és egy egész korszak jövője forgott kockán az európai kontinensen.",
            },
            {
                "type": "narration",
                "text": "Amikor a miniszter végül lezárta a tárgyalási aktát, a Szent István-dóm harangja jelezte az alkonyatot. A diplomáciai játszma folytatódott, de az egyensúlyozás törékeny pillanatai meg voltak számlálva a kitörni készülő vihar előtt.",
            },
        ],
        "reading_questions": [
            {
                "question": "Milyen diplomáciai megfontolást fogalmaz meg a külügyminiszter a beszélgetés kezdetén?",
                "options": [
                    "Célszerű lenne elkerülni a nyílt provokációt, miközben világos üzenetet kell küldeni a szövetségeseknek.",
                    "Azonnal hadat kell üzenni minden szomszédos államnak a feszültség enyhítése céljából.",
                    "A diplomácia teljesen felesleges, ezért minden külföldi követséget be kell zárni.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen feltétellel támogatná a magyar parlament a katonai hitelek megszavazását Abády szerint?",
                "options": [
                    "Ha garanciát kapnak a nemzeti szuverenitás védelmére és a diplomáciai közvetítésre.",
                    "Ha a miniszter azonnal lemond hivataláról és Bécsbe költözik.",
                    "Ha a Monarchia azonnal felbontja a német szövetségi szerződést.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen történelmi hangulat jellemzi a szövegben leírt találkozót?",
                "options": [
                    "Fenyegető nemzetközi krízis előtti törékeny diplomáciai egyensúlyozást.",
                    "Gondtalan és vidám ünnepi hangulatot a bécsi arisztokrácia körében.",
                    "Egy megkötött békeszerződés utáni békés és tartós nyugalmat.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Diplomatic Conditionals and Polite Hedging",
            "grammar_label": "Diplomatic conditionals and polite hedging (célszerű lenne, indokolt volna, kívánatosnak tartaná)",
            "goals": [
                "I can use diplomatic conditionals like indokolt volna and célszerű lenne to formulate tactful proposals",
                "I can express institutional preference politely using kívánatosnak tartaná",
                "I can deploy hedging techniques (enyhítés) to soften firm positions (álláspont)",
            ],
            "grammar_doc": {
                "slug": "diplomatic-conditionals-and-hedging",
                "title": "Diplomatic Conditionals and Polite Hedging: célszerű lenne, indokolt volna",
                "text1_title": "Softening Assertions through Modal Conditionals",
                "text1": "In high-level diplomatic, political, and institutional negotiations, direct imperatives or bald assertions are strictly avoided. Instead, the conditional mood softens proposals and cushions disagreements. Common impersonal constructions include: 'célszerű lenne' (it would be advisable / expedient), 'indokolt volna' (it would be justified / warranted), and 'szükségesnek mutatkozna' (it would appear necessary).",
                "text2_title": "Third-Person Attributive Hedging: kívánatosnak tartaná",
                "text2": "When attributing a stance to a government, delegation, or ministry, diplomatic Hungarian couples factitive verbs with the translative-factitive case (-nak/-nek): 'A kormány kívánatosnak tartaná a párbeszéd folytatását' (The government would consider continuation of the dialogue desirable). This cushions the assertion while maintaining formal resolve.",
                "table_title": "Diplomatic Hedging Formulae",
                "table_rows": [
                    ["célszerű lenne (+ inf)", "Célszerű lenne elnapolni a döntést. (It would be advisable to adjourn.)"],
                    ["indokolt volna (+ inf)", "Indokolt volna pontosítani a feltételeket. (It would be justified to clarify terms.)"],
                    ["kívánatosnak tartaná (+ acc)", "Kívánatosnak tartanánk a megállapodást. (We would consider an agreement desirable.)"],
                    ["álláspontot képvisel", "A küldöttség határozott álláspontot képvisel. (The delegation represents a firm stance.)"],
                ],
                "examples": [
                    {
                        "spanish": "A feszültség mérséklése érdekében célszerű lenne sürgősen összehívni a kétoldalú vegyesbizottságot.",
                        "english": "In the interest of mitigating tension, it would be advisable to urgently convene the bilateral joint committee.",
                    },
                    {
                        "spanish": "A szakértők szerint indokolt volna újraértékelni a biztonsági garanciák pontos szövegét.",
                        "english": "According to the experts, it would be justified to reevaluate the exact wording of the security guarantees.",
                    },
                    {
                        "spanish": "A minisztérium kifejezetten kívánatosnak tartaná egy közös nyilatkozat elfogadását a csúcstalálkozón.",
                        "english": "The ministry would explicitly consider the adoption of a joint declaration at the summit desirable.",
                    },
                    {
                        "spanish": "A nagykövet finom diplomáciai enyhítéssel jelezte kormánya fenntartásait a tervezet kapcsán.",
                        "english": "With subtle diplomatic hedging, the ambassador indicated his government's reservations regarding the draft.",
                    },
                ],
                "tip": "Distinguish between present conditional ('célszerű lenne' = it would be advisable now/future) and past conditional ('indokolt lett volna' = it would have been justified in retrospect).",
            },
            "words": [
                {"lemma": "célszerű", "translation": "expedient / advisable", "pos": "adjective"},
                {"lemma": "indokolt", "translation": "justified / warranted", "pos": "adjective"},
                {"lemma": "kívánatos", "translation": "desirable / preferable", "pos": "adjective"},
                {"lemma": "enyhítés", "translation": "hedging / mitigation / softening", "pos": "noun"},
                {"lemma": "álláspont", "translation": "stance / position", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective means 'expedient' or 'advisable' in formal negotiation contexts?",
                        ["célszerű", "véletlen", "veszélyes"],
                        0,
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the diplomatic function of 'enyhítés' (hedging)?",
                        [
                            "softening definitive statements to preserve polite dialogue and negotiation leeway",
                            "terminating diplomatic relations abruptly without warning",
                            "translating official documents literally word for word",
                        ],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["célszerű", "expedient / advisable"],
                            ["indokolt", "justified / warranted"],
                            ["kívánatos", "desirable"],
                            ["enyhítés", "hedging / softening"],
                            ["álláspont", "stance / position"],
                        ],
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which diplomatic conditional phrase best completes: 'A felek közötti bizalom megerősítése végett ____ felülvizsgálni a szerződés pontjait'?",
                        ["célszerű lenne", "kellene már tegnap", "nem szabadott"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the correct translative form: 'A miniszterelnök kifejezetten kívánatos____ tartaná a kompromisszumot.'",
                        ["-nak", "-ként", "-ért"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A kialakult válsághelyzetben ____ volna egy rendkívüli plenáris ülést összehívni. (it would be justified)",
                        "indokolt",
                        "In the crisis that had developed, it would be justified to convene an extraordinary plenary session.",
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A félreértések elkerülése végett rendkívül ____ lenne írásban is rögzíteni a szóbeli ígéreteket. (expedient)",
                        "célszerű",
                        "In order to avoid misunderstandings, it would be extremely expedient to record oral promises in writing as well.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "küldöttség", "kívánatosnak", "tartaná", "a", "békés", "tárgyalások", "folytatását."],
                        ["A", "küldöttség", "kívánatosnak", "tartaná", "a", "békés", "tárgyalások", "folytatását."],
                        "The delegation would consider continuation of the peaceful talks desirable.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A két tárgyaló fél merev ____ miatt a megbeszélések átmenetileg holtpontra jutottak. (position)",
                        "álláspontja",
                        "Due to the rigid position of the two negotiating parties, the talks temporarily reached a deadlock.",
                        ["b2-29-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "diplomáciai", "enyhítés", "segít", "megőrizni", "a", "kölcsönös", "tiszteletet."],
                        ["A", "diplomáciai", "enyhítés", "segít", "megőrizni", "a", "kölcsönös", "tiszteletet."],
                        "Diplomatic hedging helps maintain mutual respect.",
                        ["b2-29-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Diplomata", "text": "Hogyan fogalmazzuk meg az észrevételeinket anélkül, hogy megsértenénk a partnert?"},
                            {"speaker": "Nagykövet", "text": "____"},
                        ],
                        [
                            "Használjunk feltételes enyhítést: mondjuk azt, hogy indokolt volna néhány záradékot pontosítani, mert ezt kívánatosnak tartanánk.",
                            "Mondjuk nekik azt, hogy a javaslatuk teljesen értelmetlen és elfogadhatatlan.",
                            "Hagyjuk el a tárgyalótermet szó nélkül, és üzenjünk hadat a sajtón keresztül.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Külügyi szóvivő", "text": "Hogyan értékelné kormánya a legújabb tervezetet?"},
                            {"speaker": "Államtitkár", "text": "____"},
                        ],
                        [
                            "Bár látunk előremutató elemeket, célszerű lenne további szakértői egyeztetéseket folytatni a vitás kérdésekről.",
                            "Semmit sem olvastunk el, de azonnal aláírunk mindent.",
                            "A tervezet túl hosszú, ezért nem tartjuk indokoltnak a diplomáciát.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence using 'célszerű lenne' to propose a diplomatic consultation.",
                                "answer": "A feszültség csökkentése céljából célszerű lenne haladéktalanul kétoldalú konzultációt kezdeményezni.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'kívánatosnak tartaná' to state a government's preference.",
                                "answer": "Kormányunk kifejezetten kívánatosnak tartaná a fegyverszüneti megállapodás mielőbbi aláírását.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A jelenlegi helyzetben nem lenne ____ egyoldalú nyilatkozatot tenni. (advisable)",
                        "célszerű",
                        "In the current situation it would not be advisable to make a unilateral declaration.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes an official viewpoint or posture held by a delegation?",
                        ["álláspont", "enyhítés", "útlevél"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Abstract Verbs Governing Sublative and Allative",
            "grammar_label": "Verbal government in diplomacy: törekszik (-ra/-re), hozzájárul (-hoz/-hez/-höz), elkötelezi magát (mellett)",
            "goals": [
                "I can use törekszik with the sublative (-ra/-re) to express strategic objectives",
                "I can use hozzájárul with the allative (-hoz/-hez/-höz) to describe contributing to agreements",
                "I can express institutional commitment with elkötelezi magát vmi mellett",
            ],
            "grammar_doc": {
                "slug": "case-government-diplomatic-verbs",
                "title": "Abstract Verbs Governing Sublative and Allative: törekszik, hozzájárul",
                "text1_title": "Goal-Oriented Government: törekszik (-ra/-re) and támaszkodik (-ra/-re)",
                "text1": "Verbs expressing strategic aspiration and evidential grounding govern the sublative case (-ra/-re). 'Törekszik vmire' (to strive for / aim at) articulates diplomatic objectives: 'A felek a békés rendezésre törekednek' (The parties strive for peaceful settlement). Similarly, 'támaszkodik vmire' (to rely / lean on) and 'hivatkozik vmire' (to invoke / cite) point towards treaties and legal precedents as their grammatical target.",
                "text2_title": "Accession and Commitment: hozzájárul (-hoz/-hez/-höz) and elkötelezi magát (mellett)",
                "text2": "'Hozzájárul vmihez' governs the allative case (-hoz/-hez/-höz) to indicate contributing resources, political support, or consent to an international endeavor: 'hozzájárul a stabilitáshoz'. When expressing enduring loyalty or adherence to principles, the reflexive idiom 'elkötelezi magát vmi mellett' (to commit oneself to / stand by something) takes the postposition 'mellett'.",
                "table_title": "Government Summary for Diplomatic Verbs",
                "table_rows": [
                    ["törekszik (+ -ra/-re)", "Békés kompromisszumra törekednek. (They strive for peaceful compromise.)"],
                    ["hozzájárul (+ -hoz/-hez/-höz)", "Hozzájárultak a szerződés sikeréhez. (Contributed to the treaty's success.)"],
                    ["elkötelezi magát (mellett)", "Elkötelezte magát az elvek mellett. (Committed itself to the principles.)"],
                    ["hivatkozik (+ -ra/-re)", "A nemzetközi jogra hivatkozik. (Invokes international law.)"],
                ],
                "examples": [
                    {
                        "spanish": "A tárgyaló felek mindvégig a kölcsönösen előnyös megállapodásra törekedtek.",
                        "english": "The negotiating parties strove throughout for a mutually advantageous agreement.",
                    },
                    {
                        "spanish": "Az Európai Unió tagállamai jelentős forrásokkal járulnak hozzá a térség újjáépítéséhez.",
                        "english": "The member states of the European Union contribute significant resources to the reconstruction of the region.",
                    },
                    {
                        "spanish": "A kormány határozottan elkötelezte magát a nemzetközi szerződésben vállalt kötelezettségek mellett.",
                        "english": "The government firmly committed itself to the obligations undertaken in the international treaty.",
                    },
                    {
                        "spanish": "A diplomáciai jegyzék az ENSZ Alapokmányának vonatkozó cikkelyére hivatkozik.",
                        "english": "The diplomatic note refers to the relevant article of the UN Charter.",
                    },
                ],
                "tip": "Remember that 'törekszik' is an -ik verb with a stem alternation: 'törekszik' (he/she strives), 'törekednek' (they strive), 'törekedett' (strove).",
            },
            "words": [
                {"lemma": "törekszik", "translation": "to strive for / aim at (-ra/-re)", "pos": "verb"},
                {"lemma": "hozzájárul", "translation": "to contribute to (-hoz/-hez/-höz)", "pos": "verb"},
                {"lemma": "elkötelezi magát", "translation": "to commit oneself to (mellett)", "pos": "expression"},
                {"lemma": "hivatkozik", "translation": "to refer to / invoke (-ra/-re)", "pos": "verb"},
                {"lemma": "támaszkodik", "translation": "to rely on / lean on (-ra/-re)", "pos": "verb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which case is governed by the verb 'törekszik'?",
                        ["sublative (-ra/-re)", "allative (-hoz/-hez/-höz)", "dative (-nak/-nek)"],
                        0,
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which postposition is paired with 'elkötelezi magát' to express political commitment?",
                        ["mellett", "ellen", "nélkül"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["törekszik", "to strive for (-ra/-re)"],
                            ["hozzájárul", "to contribute to (-hoz/-hez/-höz)"],
                            ["elkötelezi magát", "to commit oneself (mellett)"],
                            ["hivatkozik", "to invoke / refer to (-ra/-re)"],
                            ["támaszkodik", "to rely on (-ra/-re)"],
                        ],
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct case suffix: 'A két állam a feszültség békés rendezésé____ törekszik.'",
                        ["-re", "-hez", "-től"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case suffix is governed by 'hozzájárul' in 'Jelentősen hozzájárult a stabilitás____'?",
                        ["-hoz", "-ra", "-val"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A delegáció a korábbi bilaterális megállapodásokra ____ a vitában. (referred / invoked)",
                        "hivatkozott",
                        "The delegation referred to prior bilateral agreements in the debate.",
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A miniszterelnök kijelentette, hogy országa elkötelezte magát a demokratikus értékek ____. (alongside / in support of)",
                        "mellett",
                        "The prime minister stated that his country committed itself to democratic values.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "felek", "a", "konfliktus", "diplomáciai", "megoldására", "törekednek."],
                        ["A", "felek", "a", "konfliktus", "diplomáciai", "megoldására", "törekednek."],
                        "The parties strive for the diplomatic solution of the conflict.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az új gazdasági csomag hatékonyan fog ____ a regionális fejlődéshez. (contribute)",
                        "hozzájárulni",
                        "The new economic package will effectively contribute to regional development.",
                        ["b2-29-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "biztonságpolitika", "a", "megbízható", "szövetségesekre", "támaszkodik."],
                        ["A", "biztonságpolitika", "a", "megbízható", "szövetségesekre", "támaszkodik."],
                        "Security policy relies on reliable allies.",
                        ["b2-29-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Diplomáciai tudósító", "text": "Milyen irányt követ a nagykövetség a válságkezelésben?"},
                            {"speaker": "Külügyi tanácsos", "text": "____"},
                        ],
                        [
                            "A nagykövetség mindvégig a békés megegyezésre törekszik, és elkötelezte magát a nemzetközi jog normái mellett.",
                            "A nagykövetség nem csinál semmit, mert bezárták az irodát.",
                            "A követség kizárólag a fegyveres beavatkozáshoz járul hozzá minden nap.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Külügyminiszter", "text": "Hogyan viszonyulnak a partnereink a közös alap létrehozásához?"},
                            {"speaker": "Főosztályvezető", "text": "____"},
                        ],
                        [
                            "Valamennyi tagállam kész hozzájárulni a pénzügyi kerethez, amennyiben világosak az ellenőrzési mechanizmusok.",
                            "Senki sem akar hozzájárulni, mert elfelejtették a bankszámlaszámot.",
                            "A partnerek csak a turizmusra támaszkodnak a szerződések helyett.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'törekszik' (-ra/-re) describing peace negotiations.",
                                "answer": "A két delegáció a határok biztonságát garantáló tartós egyezményre törekszik.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'hozzájárul' (-hoz/-hez/-höz) in an international cooperation context.",
                                "answer": "A humanitárius segélyszállítmány nagyban hozzájárult a polgári lakosság szenvedéseinek enyhítéséhez.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A kormány határozottan elkötelezte magát a klímavédelmi egyezmény betartása ____. (in commitment to)",
                        "mellett",
                        "The government firmly committed itself to upholding the climate agreement.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which verb requires the sublative case (-ra/-re) to express aiming toward a target?",
                        ["törekszik", "hozzájárul", "elkötelezi magát"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Negotiating Compromises and Red Lines",
            "grammar_label": "Conditional concessions and non-negotiable boundaries (vörös vonal, kompromisszum, záradék)",
            "goals": [
                "I can identify and express non-negotiable boundaries using vörös vonal",
                "I can formulate balanced compromises with concessive conditional clauses",
                "I can analyze legal conditions using treaty terminology like záradék and engedmény",
            ],
            "grammar_doc": {
                "slug": "concessions-and-red-lines",
                "title": "Negotiating Compromises, Concessions, and Red Lines",
                "text1_title": "Formulating Non-Negotiables and Compromise Boundaries",
                "text1": "In treaty negotiations, parties establish their 'vörös vonal' (red line)—a fundamental boundary beyond which no further concessions ('engedmény') can be made without compromising sovereign interests. Achieving a balanced 'kompromisszum' requires synthesizing firm red lines with conditional flexibility.",
                "text2_title": "Conditional Concessions: bár indokolt lenne..., mégis hajlandóak vagyunk...",
                "text2": "Concessionary rhetoric couples concessive conjunctions ('bár', 'jóllehet', 'noha') with conditional clauses to signal generosity while underscoring that a sacrifice is being made: 'Bár indokolt volna a garanciák szigorítása, a megállapodás érdekében hajlandóak lennénk engedményt tenni a határidők tekintetében.' Specific caveats are codified in special contract clauses ('záradék').",
                "table_title": "Negotiation and Treaty Lexicon",
                "table_rows": [
                    ["vörös vonal", "A határvédelem feladása számunkra vörös vonal. (Red line.)"],
                    ["kompromisszumot köt", "A felek ésszerű kompromisszumot kötöttek. (Struck a compromise.)"],
                    ["engedményt tesz", "Nem tehetünk további engedményeket. (Make concessions.)"],
                    ["záradék", "A szerződésbe beépítettek egy felülvizsgálati záradékot. (Review clause.)"],
                ],
                "examples": [
                    {
                        "spanish": "A nemzeti szuverenitás csorbítása vörös vonalat jelent, amelyet egyetlen kormány sem léphet át.",
                        "english": "Curtailing national sovereignty represents a red line that no government may cross.",
                    },
                    {
                        "spanish": "A többnapos maratoni egyeztetés végén sikerült kölcsönösen elfogadható kompromisszumot kötni.",
                        "english": "At the end of days of marathon consultations, they managed to strike a mutually acceptable compromise.",
                    },
                    {
                        "spanish": "A vitás kérdések rendezése érdekében mindkét fél hajlandó volt lényeges engedményeket tenni.",
                        "english": "In the interest of settling contested questions, both parties were willing to make substantive concessions.",
                    },
                    {
                        "spanish": "A kétoldalú megállapodás tartalmaz egy titkos záradékot a katonai segélynyújtás feltételeiről.",
                        "english": "The bilateral agreement contains a confidential clause on the conditions of military assistance.",
                    },
                ],
                "tip": "Remember the verbal collocation: 'kompromisszumot köt' (to conclude/make a compromise) and 'engedményt tesz' (to make a concession).",
            },
            "words": [
                {"lemma": "vörös vonal", "translation": "red line / non-negotiable limit", "pos": "expression"},
                {"lemma": "kompromisszum", "translation": "compromise", "pos": "noun"},
                {"lemma": "engedmény", "translation": "concession", "pos": "noun"},
                {"lemma": "záradék", "translation": "clause / stipulation", "pos": "noun"},
                {"lemma": "egyeztetés", "translation": "consultation / coordination", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'vörös vonal' in multilateral diplomatic talks?",
                        [
                            "an absolute, non-negotiable boundary or core interest that cannot be abandoned",
                            "a red ink line drawn across an invalidated diplomatic passport",
                            "a carpet placed on the tarmac for the arrival of foreign dignitaries",
                        ],
                        0,
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which noun denotes a specific legal stipulation or rider in a treaty?",
                        ["záradék", "engedmény", "vörös vonal"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["vörös vonal", "non-negotiable red line"],
                            ["kompromisszum", "compromise"],
                            ["engedmény", "concession"],
                            ["záradék", "clause / stipulation"],
                            ["egyeztetés", "consultation / coordination"],
                        ],
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the correct verbal collocation: 'A felek a békés megállapodás érdekében késznek mutatkoztak kompromisszumot ____.'",
                        ["kötni", "tenni", "építeni"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct verb pairing: 'A küldöttség hajlandó volna bizonyos engedményeket ____.'",
                        ["tenni", "kötni", "hozni"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Bár indokolt lett volna a követelések fenntartása, a delegáció végül ____ tett a gazdasági kérdésekben. (made concessions)",
                        "engedményeket",
                        "Although maintaining the demands would have been justified, the delegation finally made concessions on economic matters.",
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A szerződésbe beépített biztonsági ____ garantálja, hogy rendkívüli helyzetben a megállapodás felfüggeszthető. (clause)",
                        "záradék",
                        "The security clause built into the treaty guarantees that in an extraordinary situation the agreement can be suspended.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "nemzeti", "szuverenitás", "megőrzése", "világos", "vörös", "vonalat", "jelent."],
                        ["A", "nemzeti", "szuverenitás", "megőrzése", "világos", "vörös", "vonalat", "jelent."],
                        "Preserving national sovereignty represents a clear red line.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A minisztériumok közötti előzetes ____ nélkül nem lehetett benyújtani a tervezetet. (consultation)",
                        "egyeztetés",
                        "Without prior consultation between the ministries, the draft could not be submitted.",
                        ["b2-29-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "két", "ország", "történelmi", "kompromisszumot", "kötött", "a", "határkérdésben."],
                        ["A", "két", "ország", "történelmi", "kompromisszumot", "kötött", "a", "határkérdésben."],
                        "The two countries struck a historic compromise on the border issue.",
                        ["b2-29-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Főtárgyaló", "text": "Meddig mehetünk el a gazdasági vitában anélkül, hogy veszítenénk a hitelességünkből?"},
                            {"speaker": "Külügyi szakértő", "text": "____"},
                        ],
                        [
                            "A vámok csökkentésében tehetünk engedményeket, de az állami támogatások teljes eltörlése vörös vonal kell hogy maradjon.",
                            "Azonnal adjunk fel minden követelést, mert nem szeretünk tárgyalni.",
                            "A vörös vonalat piros ceruzával kell meghúzni a térképen.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Várható áttörés a holnapi csúcstalálkozón?"},
                            {"speaker": "Külügyminiszter", "text": "____"},
                        ],
                        [
                            "Amennyiben mindkét fél törekszik a kompromisszumra, úgy indokolt lenne egy közös nyilatkozat elfogadása.",
                            "Semmiképpen, mert nem beszélünk a szomszédos ország képviselőivel.",
                            "Minden záradékot törölni fogunk a nemzetközi jogból.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'vörös vonal' to express an immutable diplomatic stance.",
                                "answer": "A határok sérthetetlensége olyan vörös vonal, amelyből a kormány semmilyen körülmények között nem enged.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'kompromisszumot köt' and 'engedményt tesz'.",
                                "answer": "A felek csak úgy tudtak kompromisszumot kötni, hogy mindketten fájdalmas engedményeket tettek.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Ha a szövetségesek nem kötnének ____, a konfliktus tovább mélyülne. (compromise)",
                        "kompromisszumot",
                        "If the allies did not strike a compromise, the conflict would deepen further.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which expression denotes making a concession in formal negotiations?",
                        ["engedményt tesz", "vonalat húz", "szankciót vet ki"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Small States Between Great Powers",
            "grammar_label": "Geopolitical balancing, alliance obligations, and sovereignty (szuverenitás, egyensúlypolitika)",
            "goals": [
                "I can analyze geopolitical constraints on small states navigating great power rivalries",
                "I can discuss sovereignty (szuverenitás), spheres of influence, and alliance systems",
                "I can evaluate diplomatic maneuvering room (mozgástér) using hypothetical conditional periods",
            ],
            "grammar_doc": {
                "slug": "geopolitics-small-states-sovereignty",
                "title": "Small States Between Great Powers: egyensúlypolitika és szuverenitás",
                "text1_title": "The Geopolitical Dilemma of Middle and Small Powers",
                "text1": "Historically situated at the crossroads of imperial rivalries, Hungarian statecraft developed the doctrine of 'egyensúlypolitika' (balance-of-power policy). Trapped between competing 'érdekszférák' (spheres of influence), a small state must safeguard its national 'szuverenitás' (sovereignty) while fulfilling obligations within a multilateral 'szövetségi rendszer' (alliance system).",
                "text2_title": "Hypothetical Conditional Reasoning on Strategic Leeway",
                "text2": "Evaluating geopolitical choices requires complex hypothetical conditionals ('amennyiben... úgy...', 'ha... volna/lenne...'): 'Amennyiben az ország egyoldalúan feladná szövetségi kötelezettségeit, úgy drasztikusan beszűkülne a diplomáciai mozgástere.' Precision in modal and conditional morphology prevents rhetorical ambiguity.",
                "table_title": "Geopolitical Statecraft Lexicon",
                "table_rows": [
                    ["szuverenitás", "A nemzeti szuverenitás védelme az alaptörvény fundamentuma. (Sovereignty.)"],
                    ["szövetségi rendszer", "Az ország megbízható tagja a szövetségi rendszernek. (Alliance system.)"],
                    ["érdekszféra", "A térség két nagyhatalmi érdekszféra metszéspontjában fekszik. (Sphere of influence.)"],
                    ["mozgástér", "A kormánynak sikerült bővítenie diplomáciai mozgásterét. (Room for maneuver.)"],
                ],
                "examples": [
                    {
                        "spanish": "A kis államok számára a nemzetközi jog intézményei jelentik a szuverenitás leghatékonyabb védőpajzsát.",
                        "english": "For small states, institutions of international law represent the most effective protective shield of sovereignty.",
                    },
                    {
                        "spanish": "A hidegháború évtizedeiben Közép-Európa szovjet érdekszférába kényszerült.",
                        "english": "During the decades of the Cold War, Central Europe was forced into the Soviet sphere of influence.",
                    },
                    {
                        "spanish": "Az ügyes diplomácia képes maximalizálni az ország politikai mozgásterét még a nagyhatalmi konfliktusok idején is.",
                        "english": "Skilled diplomacy is capable of maximizing the country's political room for maneuver even in times of great power conflicts.",
                    },
                    {
                        "spanish": "A történelmi tapasztalatok azt mutatják, hogy az egyensúlypolitika feladása súlyos következményekkel járt.",
                        "english": "Historical experiences show that abandoning balance-of-power policy carried grave consequences.",
                    },
                ],
                "tip": "Distinguish between 'szuverenitás' (state legal sovereignty) and 'függetlenség' (broad political/economic independence); both are key B2 keywords.",
            },
            "words": [
                {"lemma": "szuverenitás", "translation": "sovereignty", "pos": "noun"},
                {"lemma": "szövetségi rendszer", "translation": "alliance system", "pos": "expression"},
                {"lemma": "érdekszféra", "translation": "sphere of influence", "pos": "noun"},
                {"lemma": "egyensúlypolitika", "translation": "balance-of-power policy", "pos": "noun"},
                {"lemma": "mozgástér", "translation": "room for maneuver / leeway", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'szuverenitás' represent in public law and international relations?",
                        [
                            "a state's supreme, independent authority to govern its territory and people without external control",
                            "a monetary subsidy distributed to small organic farms",
                            "a ceremonial medal awarded to retired ambassadors",
                        ],
                        0,
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the diplomatic policy of avoiding one-sided dependence by balancing between powers?",
                        ["egyensúlypolitika", "fellebbezés", "kivándorlás"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["szuverenitás", "sovereignty"],
                            ["szövetségi rendszer", "alliance system"],
                            ["érdekszféra", "sphere of influence"],
                            ["egyensúlypolitika", "balance-of-power policy"],
                            ["mozgástér", "room for maneuver"],
                        ],
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which correlative pair best introduces a formal hypothetical statement: '____ az állam elszigetelődne, ____ elveszítené mozgásterét'?",
                        ["Amennyiben... úgy...", "Mivel... ezért...", "Jóllehet... mégis..."],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the conditional verb form: 'A miniszterelnök nem ____ kockára a nemzeti szuverenitást egyetlen nagyhatalom kedvéért sem.'",
                        ["tenné", "tesz", "tette volna tegnap"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A többoldalú diplomáciai kapcsolatok ápolásával a kormány jelentősen bővíteni tudná a nemzetközi ____. (room for maneuver)",
                        "mozgásterét",
                        "By cultivating multilateral diplomatic relations, the government would be able to significantly expand its international room for maneuver.",
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Ha az ország nem tartozna egy stabil ____, sokkal sebezhetőbb lenne a külső nyomással szemben. (alliance system)",
                        "szövetségi rendszerhez",
                        "If the country did not belong to a stable alliance system, it would be much more vulnerable against external pressure.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "kis", "államok", "számára", "létfontosságú", "a", "szuverenitás", "megőrzése."],
                        ["A", "kis", "államok", "számára", "létfontosságú", "a", "szuverenitás", "megőrzése."],
                        "For small states, preserving sovereignty is of vital importance.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A történelmi tapasztalatok arra intenek, hogy az egyoldalú függés egyetlen ____ sem fenntartható. (sphere of influence)",
                        "érdekszférában",
                        "Historical experiences warn that one-sided dependence is not sustainable in any sphere of influence.",
                        ["b2-29-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "hagyományos", "egyensúlypolitika", "célja", "a", "békés", "együttélés", "biztosítása."],
                        ["A", "hagyományos", "egyensúlypolitika", "célja", "a", "békés", "együttélés", "biztosítása."],
                        "The goal of traditional balance-of-power policy is ensuring peaceful coexistence.",
                        ["b2-29-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Politológus", "text": "Hogyan érvényesítheti érdekeit egy közép-európai állam a globális versengésben?"},
                            {"speaker": "Biztonságpolitikai szakértő", "text": "____"},
                        ],
                        [
                            "A szuverenitás megőrzése mellett aktív egyensúlypolitikát kell folytatnia, kihasználva a szövetségi rendszer adta lehetőségeket.",
                            "Úgy, hogy feladja a hadseregét és nem beszél a szomszédos országokkal.",
                            "A szuverenitás elavult fogalom, ezért nem kell vele foglalkozni a diplomáciában.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Diplomata", "text": "Nem szűkül be túlságosan a mozgásterünk a nagyhatalmi blokkok árnyékában?"},
                            {"speaker": "Államtitkár", "text": "____"},
                        ],
                        [
                            "Csak akkor szűkülne be, ha passzívak maradnánk; a sokrétű gazdasági és kulturális kapcsolatok bővítik a mozgásteret.",
                            "A mozgástér teljesen megszűnt, ezért minden szerződést felbontunk holnap.",
                            "A blokkok nem léteznek a valóságban, csupán a könyvtárakban találkozunk velük.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'egyensúlypolitika' to describe navigating international pressure.",
                                "answer": "A függetlenség megőrzése érdekében az ország évszázadokon át kényes egyensúlypolitikát folytatott a szomszédos birodalmak között.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a conditional sentence using 'szuverenitás' and 'mozgástér'.",
                                "answer": "Amennyiben a kormány megvédené a nemzeti szuverenitást, úgy jelentősen megnőne a külpolitikai mozgástere a nemzetközi fórumokon.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A szövetségesek közötti szolidaritás elengedhetetlen ahhoz, hogy a tagállamok megőrizzék nemzeti ____. (sovereignty)",
                        "szuverenitásukat",
                        "Solidarity among allies is indispensable in order for member states to preserve their national sovereignty.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes a geopolitical zone dominated by an imperial great power?",
                        ["érdekszféra", "álláspont", "vörös vonal"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Simulating a Diplomatic Summit",
            "grammar_label": "Writing a diplomatic communique using polite conditional hedging and formal government",
            "goals": [
                "I can draft clauses of a formal diplomatic communique (zárónyilatkozat)",
                "I can contrast bilateral (kétoldalú) and multilateral (többoldalú) summit frameworks",
                "I can express historical reconciliation (megbékélés) using refined diplomatic conditional phrasing",
            ],
            "grammar_doc": {
                "slug": "simulating-summit-communique",
                "title": "Drafting Diplomatic Communiques: zárónyilatkozat és megbékélés",
                "text1_title": "Anatomy and Register of the Diplomatic Communique",
                "text1": "A formal summit communique ('zárónyilatkozat') synthesizes multilateral consensus into authoritative diplomatic prose. It employs third-person collective plural verbs, solemn declaratives ('kinyilvánítják', 'megerősítik'), and polished conditional formulations where aspirations exceed binding commitments: 'A felek kívánatosnak tartanák a kulturális csereprogramok bővítését.'",
                "text2_title": "Bilateral vs. Multilateral Formats and Reconciliation",
                "text2": "Debates distinguish 'kétoldalú' (bilateral) pacts from 'többoldalú' (multilateral) frameworks. Historic breakthrough moments center on 'megbékélés' (reconciliation), where former adversaries pledge mutual respect, non-aggression, and collaborative mechanisms to prevent resurgence of hostility.",
                "table_title": "Summit and Communique Vocabulary",
                "table_rows": [
                    ["zárónyilatkozat", "A csúcstalálkozó végén elfogadták a zárónyilatkozatot. (Final communique.)"],
                    ["csúcstalálkozó", "A kétoldalú csúcstalálkozó történelmi sikert hozott. (Summit meeting.)"],
                    ["kétoldalú", "Kétoldalú egyezményt kötöttek a határforgalomról. (Bilateral treaty.)"],
                    ["megbékélés", "A két szomszédos nép megbékélése új korszakot nyitott. (Reconciliation.)"],
                ],
                "examples": [
                    {
                        "spanish": "A zárónyilatkozatban a résztvevő államok megerősítették elkötelezettségüket a békés vitarendezés mellett.",
                        "english": "In the final communique, participating states reaffirmed their commitment to the peaceful settlement of disputes.",
                    },
                    {
                        "spanish": "A nemzetközi csúcstalálkozó kitűnő alkalmat teremtett a kétoldalú kapcsolatok áttekintésére.",
                        "english": "The international summit created an excellent opportunity for reviewing bilateral relations.",
                    },
                    {
                        "spanish": "A többoldalú diplomáciai mechanizmusok nélkülözhetetlenek a globális éghajlati válság kezeléséhez.",
                        "english": "Multilateral diplomatic mechanisms are indispensable for addressing the global climate crisis.",
                    },
                    {
                        "spanish": "A történelmi megbékélés folyamata türelmet, kölcsönös empátiát és őszinte párbeszédet követel.",
                        "english": "The process of historic reconciliation demands patience, mutual empathy, and sincere dialogue.",
                    },
                ],
                "tip": "In formal communiques, verbs of declaration are often accompanied by dependent clauses introduced by 'hogy': 'A felek leszögezték, hogy elkötelezettek a béke mellett.'",
            },
            "words": [
                {"lemma": "zárónyilatkozat", "translation": "final communique / declaration", "pos": "noun"},
                {"lemma": "csúcstalálkozó", "translation": "summit meeting", "pos": "noun"},
                {"lemma": "kétoldalú", "translation": "bilateral", "pos": "adjective"},
                {"lemma": "többoldalú", "translation": "multilateral", "pos": "adjective"},
                {"lemma": "megbékélés", "translation": "reconciliation", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'zárónyilatkozat' in international relations?",
                        [
                            "the official final communique or joint declaration summarizing a summit's conclusions",
                            "a customs form required for transporting commercial goods across borders",
                            "a letter of resignation submitted by an outgoing prime minister",
                        ],
                        0,
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective refers to agreements conducted between two sovereign states?",
                        ["kétoldalú", "többoldalú", "egyoldalú"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["zárónyilatkozat", "final communique"],
                            ["csúcstalálkozó", "summit meeting"],
                            ["kétoldalú", "bilateral"],
                            ["többoldalú", "multilateral"],
                            ["megbékélés", "reconciliation"],
                        ],
                        ["b2-29-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the appropriate diplomatic conditional phrasing in a communique: 'A felek kívánatosnak ____ az együttműködés elmélyítését.'",
                        ["tartanák", "tartják meg tegnap", "tartani tilos"],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence correctly employs government with 'elkötelezi magát':",
                        [
                            "A csúcstalálkozó résztvevői elkötelezték magukat a megbékélés és a stabilitás mellett.",
                            "A résztvevők elkötelezték magukat a stabilitásra.",
                            "A résztvevők elkötelezték magukat a stabilitástól.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A miniszterek hangsúlyozták, hogy a gazdasági kapcsolatok fejlesztése érdekében ____ lenne a vámok csökkentése. (advisable)",
                        "célszerű",
                        "The ministers emphasized that in the interest of developing economic relations, reducing tariffs would be advisable.",
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A delegációk konszenzussal fogadták el a konferencia hivatalos ____. (final communique)",
                        "zárónyilatkozatát",
                        "The delegations adopted the official final communique of the conference by consensus.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "történelmi", "megbékélés", "biztosítja", "a", "régió", "tartós", "békéjét."],
                        ["A", "történelmi", "megbékélés", "biztosítja", "a", "régió", "tartós", "békéjét."],
                        "Historic reconciliation ensures the lasting peace of the region.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A két szomszédos ország államfője éves rendszerességgel tart ____. (summit meeting)",
                        "csúcstalálkozót",
                        "The heads of state of the two neighboring countries hold a summit meeting on an annual basis.",
                        ["b2-29-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "többoldalú", "tárgyalások", "hatékony", "keretet", "nyújtanak", "a", "párbeszédhez."],
                        ["A", "többoldalú", "tárgyalások", "hatékony", "keretet", "nyújtanak", "a", "párbeszédhez."],
                        "Multilateral negotiations provide an effective framework for dialogue.",
                        ["b2-29-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Diplomáciai tudósító", "text": "Hogyan zárult az idei kétoldalú csúcstalálkozó?"},
                            {"speaker": "Külügyi szóvivő", "text": "____"},
                        ],
                        [
                            "A vezetők közös zárónyilatkozatot írtak alá, amelyben megerősítették elkötelezettségüket a megbékélés és az együttműködés mellett.",
                            "A felek nem voltak hajlandóak találkozni, és azonnal hazautaztak.",
                            "A csúcstalálkozó helyett inkább színházba mentek a miniszterek.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Milyen konkrét javaslatokat tartalmaz a zárónyilatkozat?"},
                            {"speaker": "Külügyminiszter", "text": "____"},
                        ],
                        [
                            "A dokumentum rögzíti, hogy indokolt volna felgyorsítani a határ menti infrastruktúra modernizálását a gazdasági élénkülés érdekében.",
                            "Semmilyen javaslat nincs benne, csupán üres papírlapokat írtak alá.",
                            "Minden határátkelőt végleg bezárnak a lakosság elől.",
                        ],
                        0,
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal communique sentence using 'zárónyilatkozat' and 'elkötelezi magát' (mellett).",
                                "answer": "A konferencia zárónyilatkozatában valamennyi résztvevő állam határozottan elkötelezte magát a nukleáris fegyverkezés korlátozása mellett.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'kívánatosnak tartaná' to formulate a summit recommendation.",
                                "answer": "A két küldöttség kívánatosnak tartaná a gazdasági vegyesbizottság félévenkénti rendszeres összehívását.",
                            }
                        ],
                        ["b2-diplomatic-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A két szomszédos nép közötti őszinte ____ nélkül nem képzelhető el a határok békés nyugalma. (reconciliation)",
                        "megbékélés",
                        "Without sincere reconciliation between the two neighboring peoples, the peaceful calm of the borders is unimaginable.",
                        ["b2-diplomatic-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adjective designates diplomacy involving more than two state actors?",
                        ["többoldalú", "kétoldalú", "egyoldalú"],
                        0,
                        ["b2-29-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can formulate diplomatic proposals using polite conditionals and hedging (indokolt volna, célszerű lenne)",
            "I can correctly employ case governments of abstract diplomatic verbs (-ra/-re, -hoz/-hez/-höz, mellett)",
            "I can analyze geopolitical balancing, sovereignty, and draft clauses of a diplomatic communique",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["szuverenitás", "sovereignty"],
                    ["vörös vonal", "red line / non-negotiable limit"],
                    ["kompromisszum", "compromise"],
                    ["zárónyilatkozat", "final communique"],
                    ["megbékélés", "reconciliation"],
                ],
                ["b2-29-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'egyensúlypolitika' aim to achieve in foreign policy?",
                [
                    "maneuvering between powerful rivals to avoid domination by any single power",
                    "spending equal amounts of state funds on road maintenance and theater subsidies",
                    "enforcing physical fitness standards among newly recruited diplomats",
                ],
                0,
                ["b2-29-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence illustrates correct diplomatic conditional hedging with 'kívánatosnak tartaná'?",
                [
                    "A küldöttség kifejezetten kívánatosnak tartaná a fegyverszüneti megállapodás mielőbbi meghosszabbítását.",
                    "A küldöttség kívánatosnak tartja tegnapelőtt a vacsorát.",
                    "Kívánatos tartaná a miniszter a repülőtér lezárását azonnal.",
                ],
                0,
                ["b2-diplomatic-conditionals"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A területi integritás feladása olyan ____, amelyet a kormány semmilyen nyomásra nem fog átlépni. (red line)",
                "vörös vonal",
                "Abandoning territorial integrity is a red line that the government will not cross under any pressure.",
                ["b2-29-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A tárgyalások korai szakaszában rendkívül ____ lenne elkerülni a sajtó előtti éles nyilatkozatokat. (advisable)",
                "célszerű",
                "In the early phase of the negotiations, it would be extremely advisable to avoid sharp declarations before the press.",
                ["b2-diplomatic-conditionals"],
            ),
            fb(
                "grammar",
                "recall",
                "A nemzetközi közösség elkötelezte magát a kis államok szuverenitásának tiszteletben tartása ____. (in commitment to)",
                "mellett",
                "The international community committed itself to respecting the sovereignty of small states.",
                ["b2-diplomatic-conditionals"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'indokolt volna' chosen in formal diplomatic notes instead of 'kell'?",
                [
                    "Because it softens a requirement into an objective, polite recommendation, preserving negotiation goodwill.",
                    "Because 'kell' is grammatically forbidden in official written Hungarian.",
                    "Because 'indokolt volna' can only be used with past tense verbs.",
                ],
                0,
                ["b2-diplomatic-conditionals"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Diplomáciai tudósító", "text": "Hogyan értékeli a két miniszterelnök csúcstalálkozóját Bánffy regényének szellemében?"},
                    {"speaker": "Történész", "text": "____"},
                ],
                [
                    "A felek elkötelezték magukat a békés kompromisszum mellett, miközben világossá tették a szuverenitásuk védelmét garantáló vörös vonalakat.",
                    "A miniszterek nem álltak szóba egymással, és a vacsorán összevesztek az étlapon.",
                    "A diplomácia teljesen felesleges, mert a háborúk elkerülhetetlenek a kontinensen.",
                ],
                0,
                ["b2-diplomatic-conditionals"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence with correct case government for both 'törekszik' and 'hozzájárul':",
                [
                    "A felek a megegyezésre törekszenek, és készek hozzájárulni a regionális stabilitáshoz.",
                    "A felek a megegyezéshez törekszenek, és készek hozzájárulni a stabilitásra.",
                    "A felek megegyezéstől törekszenek, és hozzájárulnak a stabilitásban.",
                ],
                0,
                ["b2-diplomatic-conditionals"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "kormány", "mindvégig", "a", "békés", "diplomáciai", "kompromisszumra", "törekedett."],
                ["A", "kormány", "mindvégig", "a", "békés", "diplomáciai", "kompromisszumra", "törekedett."],
                "The government strove throughout for a peaceful diplomatic compromise.",
                ["b2-diplomatic-conditionals"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "zárónyilatkozatban", "a", "résztvevők", "megerősítették", "elkötelezettségüket", "a", "megbékélés", "mellett."],
                ["A", "zárónyilatkozatban", "a", "résztvevők", "megerősítették", "elkötelezettségüket", "a", "megbékélés", "mellett."],
                "In the final communique, the participants reaffirmed their commitment to reconciliation.",
                ["b2-diplomatic-conditionals"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause diplomatic argument using 'célszerű lenne', 'hozzájárul (-hoz/-hez/-höz)', and 'vörös vonal'.",
                        "answer": "Bár a tárgyalások e szakaszában célszerű lenne bizonyos gazdasági engedményeket tenni, a nemzeti szuverenitás korlátozása vörös vonalat jelent; ezért a delegáció csak olyan feltételekhez hajlandó hozzájárulni, amelyek garantálják az ország biztonságát.",
                    }
                ],
                ["b2-diplomatic-conditionals"],
            ),
        ],
    },
}
