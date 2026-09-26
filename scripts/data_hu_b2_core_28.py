"""
Hungarian B2 Core Track Unit 28:
  b2-28: Exile, Emigration & Global Networks
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_28 = {
    "unit_num": 28,
    "title": "Exile, Emigration & Global Networks",
    "grammar_summary": "Figurative preverbs of integration and alienation (beilleszkedik, elidegenedik, elvándorol, hazatelepül, gyökeret ver), subtle directional contrasts (ki-, el-, vissza-, haza-), and diasporic narratives.",
    "grammar_skill": "b2-figurative-preverbs",
    "vocab_skill": "b2-28-vocab",
    "theme": "Exile, emigration and global networks",
    "intro_body": [
        "A 20. és 21. századi magyar történelem egyik legmeghatározóbb tapasztalata a migráció, a politikai emigráció és a nemzetközi mobilitás. Az elvándorlás és a hazatérés nem csupán földrajzi helyváltoztatás, hanem mély identitásbeli átalakulás, amely a nyelvben is gazdagon tükröződik.",
        "Ebben a fejezetben megismerkedhet az integráció és az elidegenedés átvitt értelmű igekötőivel (beilleszkedik, elidegenedik, gyökeret ver, hazatelepül), elemezheti az igekötők finom jelentésbeli árnyalatait (kivándorol vs. elvándorol, hazatér vs. visszatér), valamint feltárhatja az agyelszívás (brain drain) és a nemzetközi tudáscsere (brain circulation) kérdéseit. A fejezet végén Márai Sándor megrázó emigrációs naplóján keresztül pillanthat be az anyanyelvhez való ragaszkodás mély dilemmáiba.",
    ],
    "classic_story": {
        "slug": "marainaplo",
        "author": "Márai Sándor",
        "work": "Napló (1945–1957)",
        "title": "Anyanyelv és haza az emigrációban",
        "summary": "Márai Sándor és felesége, Lola az olaszországi Posillipóban és New Yorkban élik meg az emigráció magányát, ahol az író számára az anyanyelv marad az egyetlen igazi hazája és menedéke.",
        "characters": ["Márai Sándor", "Lola"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A posillipói sziklák felett a déli napfény ragyogott a Nápolyi-öböl vizén, de Márai Sándor íróasztalánál a csendet csak a toll sercegése törte meg. A budai Mikó utcai lakás romjai, az elhagyott könyvtár és az otthoni irodalmi élet emlékei kísértettek a dél-olasz tengerparton.",
            },
            {
                "type": "dialogue",
                "speaker": "Lola",
                "text": "Sándor, sikerült ma haladnod a kézirattal, vagy még mindig a legfrissebb pesti hírek járnak a gondolataidban?",
            },
            {
                "type": "dialogue",
                "speaker": "Márai Sándor",
                "text": "Az ember elvándorolhat ezer mérföldre, elhagyhatja a szülőföldjét, de az anyanyelvét nem tudja levetni, mint egy elnyűtt felöltőt. Itt, az idegen tenger partján döbbenek rá nap mint nap: amíg magyarul gondolkodom és írok, addig a haza bennem él, nem a határok között.",
            },
            {
                "type": "narration",
                "text": "Lola leült a fonott karosszékbe a nyitott erkélyajtó mellett. Felidézte magában az 1948-as elindulás feszültségét: az elidegenedés folyamata már otthon elkezdődött a kiépülő diktatúrában, a határ átlépése csupán a végleges szakítást jelentette egy torzuló világgal.",
            },
            {
                "type": "dialogue",
                "speaker": "Lola",
                "text": "Gondolod, hogy egyszer még hazatérünk, ha megváltozik a rendszer? Vagy végleg gyökeret verünk valahol a tengerentúlon?",
            },
            {
                "type": "dialogue",
                "speaker": "Márai Sándor",
                "text": "Visszatérni egy fizikai helyre talán lehetséges volna évek múltával, de hazatérni abba az elveszett ifjúságba és polgári világba már soha többé nem lehet. Az emigráns sorsa az örökös lebegés: otthon már idegenné vált, az új világban pedig még nem honos.",
            },
            {
                "type": "narration",
                "text": "Az író kinyitotta vaskos naplóját, és folytatta a bejegyzést. Minden egyes leírt magyar szó védőbástya volt az elmagányosodás és a szellemi asszimiláció ellen; tudta, hogy olvasói nincsenek a közelben, mégis a nyelvhez való hűség jelentette létezésének egyetlen igazolását.",
            },
            {
                "type": "narration",
                "text": "Ahogy az alkonyi fények lassan aranyra festették a Vezúv vonulatát, Márai letette a tollat. A száműzetés keserűsége mély volt, de a szabadság tudata és a megalkuvást elutasító lelkiismeret erőt adott a magányos küzdelemhez.",
            },
        ],
        "reading_questions": [
            {
                "question": "Miért tekinti Márai az anyanyelvet a valódi hazájának az emigrációban?",
                "options": [
                    "Mert az anyanyelv belső szellemi menedék, amely a földrajzi határoktól függetlenül megőrzi az identitást.",
                    "Mert Olaszországban mindenki megtanult magyarul beszélni a környezetében.",
                    "Mert a külföldi könyvkiadók kötelezték arra, hogy csak magyarul publikáljon.",
                ],
                "correct": 0,
            },
            {
                "question": "Hogyan határozza meg Márai a hazatérés és a visszatérés közötti különbséget?",
                "options": [
                    "Egy földrajzi helyre vissza lehet térni, de a letűnt múltba és az elveszett polgári világba már nem lehet hazatérni.",
                    "A visszatérés mindig végleges letelepedést jelent, míg a hazatérés csupán rövid utazást.",
                    "Szerinte a két fogalom teljesen azonos, csupán a szavak stílusa különbözik.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen belső lelki állapotot tükröz az emigráns léte a szöveg szerint?",
                "options": [
                    "Két világ közötti lebegést, ahol az ember otthon már idegen, az új helyen pedig még nem honos.",
                    "A szülőföld emlékeinek gyors és felhőtlen elfelejtését.",
                    "A teljes társadalmi beolvadást és a korábbi kultúra megtagadását.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Figurative Preverbs of Integration and Alienation",
            "grammar_label": "Figurative preverbs of integration and alienation (beilleszkedik, elidegenedik, elvándorol, hazatelepül, gyökeret ver)",
            "goals": [
                "I can use figurative preverbs like beilleszkedik and elidegenedik to describe social integration and alienation",
                "I can express spatial and demographic movement with elvándorol and hazatelepül",
                "I can use the idiomatic expression gyökeret ver in formal migration discourse",
            ],
            "grammar_doc": {
                "slug": "figurative-preverbs-integration-alienation",
                "title": "Figurative Preverbs of Integration and Alienation: beilleszkedik, elidegenedik, gyökeret ver",
                "text1_title": "Metaphorical Extension of Inward and Outward Preverbs",
                "text1": "In Hungarian, spatial preverbs frequently undergo figurative shifts into social and psychological domains. The preverb 'be-' extends from physical inward motion to deep social assimilation: 'beilleszkedik a társadalomba' (to integrate into society), 'beolvad' (to assimilate). Conversely, 'el-' denotes gradual distancing, estrangement, or permanent departure: 'elidegenedik a környezetétől' (to become alienated from one's environment), 'elvándorol' (to migrate away from origin).",
                "text2_title": "Repatriation and Rooting Idioms",
                "text2": "'Hazatelepül' combines the affective directional preverb 'haza-' with 'települ' to denote official or permanent resettlement back in the home country. The idiomatic phrase 'gyökeret ver' (literally 'to strike root') describes successfully establishing long-term ties, family life, or professional existence in a new host country.",
                "table_title": "Key Figurative Preverbs of Integration and Alienation",
                "table_rows": [
                    ["beilleszkedik (+ -ba/-be)", "Sikeresen beilleszkedett a helyi közösségbe. (Integrated into the community.)"],
                    ["elidegenedik (+ -tól/-től)", "Fokozatosan elidegenedett a régi barátaitól. (Became alienated from old friends.)"],
                    ["elvándorol (+ -ból/-ből, -ról/-ről)", "Sokan elvándoroltak a szülőfalujukból. (Many migrated away from their native village.)"],
                    ["hazatelepül", "Évtizedek múltán hazatelepült Magyarországra. (Repatriated to Hungary.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az emigráns családok többsége gyorsan beilleszkedik az új ország oktatási rendszerébe.",
                        "english": "The majority of emigrant families integrate quickly into the new country's educational system.",
                    },
                    {
                        "spanish": "Ha valaki elveszíti a kapcsolatot az anyanyelvével, könnyen elidegenedik saját kulturális örökségétől.",
                        "english": "If someone loses contact with their mother tongue, they easily become alienated from their own cultural heritage.",
                    },
                    {
                        "spanish": "A tehetséges kutatók jelentős része elvándorol a jobb infrastrukturális lehetőségek reményében.",
                        "english": "A significant portion of talented researchers migrate away in the hope of better infrastructural opportunities.",
                    },
                    {
                        "spanish": "A külföldön töltött évek után a házaspár végleg gyökeret vert az új-zélandi kikötővárosban.",
                        "english": "After the years spent abroad, the couple put down roots permanently in the New Zealand harbor town.",
                    },
                ],
                "tip": "Note case governments: 'beilleszkedik' requires the illative (-ba/-be), whereas 'elidegenedik' requires the ablative (-tól/-től). 'Gyökeret ver' is an expression where 'gyökeret' remains in the accusative.",
            },
            "words": [
                {"lemma": "beilleszkedik", "translation": "to integrate / assimilate into", "pos": "verb"},
                {"lemma": "elidegenedik", "translation": "to become alienated / estranged", "pos": "verb"},
                {"lemma": "elvándorol", "translation": "to emigrate / migrate away", "pos": "verb"},
                {"lemma": "hazatelepül", "translation": "to repatriate / resettle back home", "pos": "verb"},
                {"lemma": "gyökeret ver", "translation": "to put down roots / settle permanently", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'beilleszkedik' express in sociological contexts?",
                        [
                            "to integrate harmoniously into a new community or social environment",
                            "to violently reject foreign cultural traditions",
                            "to travel as a short-term tourist across European capitals",
                        ],
                        0,
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which verb means to become emotionally or socially alienated from one's origins?",
                        ["elidegenedik", "hazatelepül", "beilleszkedik"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["beilleszkedik", "to integrate / assimilate into"],
                            ["elidegenedik", "to become alienated / estranged"],
                            ["elvándorol", "to migrate away"],
                            ["hazatelepül", "to repatriate back home"],
                            ["gyökeret ver", "to put down roots"],
                        ],
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case suffix is governed by 'beilleszkedik' in 'Sikeresen beilleszkedett a helyi társadalom____'?",
                        ["-ba", "-tól", "-ként"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct case suffix governed by 'elidegenedik' in 'Elidegenedett a gyökerei____':",
                        ["-től", "-be", "-re"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A nyugdíjba vonulás után az idős professzor végleg ____ Magyarországra. (repatriated)",
                        "hazatelepült",
                        "After retiring, the elderly professor repatriated to Hungary permanently.",
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Az idegen környezetben élő művész nem tudott megszokni, és lassanként ____ a szülőföldjétől. (became alienated)",
                        "elidegenedett",
                        "Living in an unfamiliar environment, the artist could not adjust and gradually became alienated from his homeland.",
                        ["b2-figurative-preverbs"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "fiatal", "diplomás", "könnyen", "beilleszkedett", "a", "nemzetközi", "csapatba."],
                        ["A", "fiatal", "diplomás", "könnyen", "beilleszkedett", "a", "nemzetközi", "csapatba."],
                        "The young graduate integrated easily into the international team.",
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A gazdasági válság éveiben több tízezer szakmunkás ____ a régióból. (migrated away)",
                        "elvándorolt",
                        "In the years of economic crisis, tens of thousands of skilled workers migrated away from the region.",
                        ["b2-28-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "család", "végleg", "gyökeret", "vert", "az", "új", "hazájában."],
                        ["A", "család", "végleg", "gyökeret", "vert", "az", "új", "hazájában."],
                        "The family permanently put down roots in their new homeland.",
                        ["b2-28-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Interjúkészítő", "text": "Hogyan éli meg a külföldre költöző magyarok második generációja az identitását?"},
                            {"speaker": "Szociológus", "text": "____"},
                        ],
                        [
                            "A legtöbben zökkenőmentesen beilleszkednek a fogadó társadalomba, de sokan nem akarnak elidegenedni az anyanyelvüktől sem.",
                            "Mindenki azonnal elfelejti a szülei nyelvét, és soha többé nem beszél magyarul.",
                            "A beilleszkedés tilos a nemzetközi jog szerint, ezért mindenki elvándorol.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kutató", "text": "Mi ösztönözheti a magasan képzett szakembereket a visszatérésre?"},
                            {"speaker": "Egyetemi dékán", "text": "____"},
                        ],
                        [
                            "Ha versenyképes kutatási feltételeket teremtünk, sokan szívesen hazatelepülnek a szülőföldjükre.",
                            "Csak akkor vándorolnak el, ha túl sok támogatást kapnak az államtól.",
                            "A gyökeret verés kizárólag a kertészek feladata a botanikus kertben.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'beilleszkedik' with the illative case (-ba/-be) describing social adaptation.",
                                "answer": "Az új munkatárs meglepően gyorsan beilleszkedett a soknemzetiségű kutatócsoportba.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'gyökeret ver' to express permanent settlement abroad.",
                                "answer": "Bár kezdetben csak néhány évre terveztek, végül teljesen gyökeret vertek Svédországban.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A hosszú távollét miatt a diák szinte teljesen ____ a hazai kulturális élettől. (became alienated)",
                        "elidegenedett",
                        "Due to the long absence, the student became almost completely alienated from cultural life back home.",
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which expression means to permanently establish oneself in a new location?",
                        ["gyökeret ver", "útra kel", "határt lép"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Subtle Directional Contrasts (ki-, el-, vissza-, haza-)",
            "grammar_label": "Directional preverb contrasts in migration contexts (kivándorol vs. elvándorol, hazatér vs. visszatér)",
            "goals": [
                "I can distinguish kivándorol (border-crossing emigration) from elvándorol (general departure)",
                "I can contrast hazatér (affective homecoming) with visszatér (neutral spatial return)",
                "I can use formal noun derivations like kivándorlás and hazatérés in analytical prose",
            ],
            "grammar_doc": {
                "slug": "directional-preverb-contrasts-migration",
                "title": "Directional Preverb Contrasts in Migration: ki-, el-, vissza-, haza-",
                "text1_title": "Boundary Crossing (ki-) vs. Origin Departure (el-)",
                "text1": "While both verbs relate to migration, 'kivándorol' explicitly highlights crossing an external national or continental boundary to reside abroad ('kivándorolt Amerikába'). In contrast, 'elvándorol' focuses on moving away from the source or departure point without necessarily emphasizing the external boundary, frequently describing domestic demographic shifts: 'elvándorol a vidéki térségekből' (to migrate away from rural areas).",
                "text2_title": "Affective Homecoming (haza-) vs. Neutral Return (vissza-)",
                "text2": "'Hazatér' is emotionally charged, denoting an existential return to one's native land, ancestral home, or family hearth ('hazatér az emigrációból', 'hazatér a szülőföldre'). 'Visszatér' is directionally neutral and iterative, signifying merely going back to a prior location or recurring theme: 'visszatér Londonba' (goes back to London), 'visszatér a vitás kérdésre' (returns to the contested issue).",
                "table_title": "Directional Contrast Matrix",
                "table_rows": [
                    ["kivándorol", "A 20. század elején százezrek vándoroltak ki Amerikába. (Emigrated abroad.)"],
                    ["elvándorol", "A hátrányos helyzetű falvakból elvándorol a fiatalság. (Migrates away from origin.)"],
                    ["hazatér", "Húsz év száműzetés után meghatódva tért haza Budapestre. (Returned home to homeland.)"],
                    ["visszatér", "A konferencia után a kutató visszatért a bécsi laboratóriumába. (Returned neutrally to base.)"],
                ],
                "examples": [
                    {
                        "spanish": "A 19. század végén a gazdasági válság következtében hatalmas tömegek vándoroltak ki az Egyesült Államokba.",
                        "english": "At the end of the 19th century, enormous masses emigrated to the United States as a consequence of economic crisis.",
                    },
                    {
                        "spanish": "Az északi megyékből folyamatosan elvándorol a munkaképes lakosság a főváros irányába.",
                        "english": "From the northern counties, the working-age population continuously migrates away towards the capital.",
                    },
                    {
                        "spanish": "Az idős költő élete alkonyán hazatért szülővárosába, hogy ott fejezze be memoárját.",
                        "english": "At the dusk of his life, the elderly poet returned home to his native town to complete his memoir there.",
                    },
                    {
                        "spanish": "A szakmai ösztöndíj lejárta után a mérnök visszatért korábbi munkahelyére.",
                        "english": "After the professional scholarship expired, the engineer returned to his previous workplace.",
                    },
                ],
                "tip": "Note that nominal forms follow identical distinctions: 'kivándorlás' (emigration abroad) vs. 'elvándorlás' (out-migration); 'hazatérés' (homecoming) vs. 'visszatérés' (return).",
            },
            "words": [
                {"lemma": "kivándorol", "translation": "to emigrate / move abroad permanently", "pos": "verb"},
                {"lemma": "hazatér", "translation": "to return home / return to one's homeland", "pos": "verb"},
                {"lemma": "visszatér", "translation": "to return / go back (to a place or topic)", "pos": "verb"},
                {"lemma": "kivándorlás", "translation": "emigration / outward migration", "pos": "noun"},
                {"lemma": "hazatérés", "translation": "homecoming / repatriation", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which verb implies an emotional return to one's homeland or native soil?",
                        ["hazatér", "visszatér", "kivándorol"],
                        0,
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the focus of 'kivándorol' compared to 'elvándorol'?",
                        [
                            "crossing an international or continental border to settle abroad",
                            "moving from one street to another within the same town",
                            "returning home after an afternoon shopping trip",
                        ],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["kivándorol", "to emigrate abroad"],
                            ["hazatér", "to return home / repatriate"],
                            ["visszatér", "to go back neutrally"],
                            ["kivándorlás", "emigration"],
                            ["hazatérés", "homecoming"],
                        ],
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the best verb: 'A háború után a tudós nem akart többé ____ a szülőföldjére, mert félt a megtorlástól.'",
                        ["hazatérni", "kivándorolni", "beilleszkedni"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which preverb best completes internal regional migration: 'A fiatalok többsége ____vándorol a szegényebb falvakból'?",
                        ["el-", "ki-", "vissza-"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Az orvos a külföldi műtét elvégzése után azonnal ____ a müncheni klinikára. (returned)",
                        "visszatért",
                        "After performing the surgery abroad, the doctor returned immediately to the Munich clinic.",
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A forradalom leverését követően kétszázezer magyar állampolgár ____ nyugati országokba. (emigrated abroad)",
                        "vándorolt ki",
                        "Following the crushing of the revolution, two hundred thousand Hungarian citizens emigrated to Western countries.",
                        ["b2-figurative-preverbs"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "politikai", "menekült", "hosszú", "évtizedek", "után", "végre", "hazatért."],
                        ["A", "politikai", "menekült", "hosszú", "évtizedek", "után", "végre", "hazatért."],
                        "After long decades, the political refugee finally returned home.",
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A tömeges ____ következtében egész országrészek néptelenedtek el a 19. század végén. (emigration)",
                        "kivándorlás",
                        "As a consequence of mass emigration, entire parts of the country became depopulated at the end of the 19th century.",
                        ["b2-28-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Az", "ünnepélyes", "hazatérés", "mély", "érzelmeket", "váltott", "ki", "mindenkiből."],
                        ["Az", "ünnepélyes", "hazatérés", "mély", "érzelmeket", "váltott", "ki", "mindenkiből."],
                        "The ceremonial homecoming elicited deep emotions from everyone.",
                        ["b2-28-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Történész", "text": "Mi jellemezte az 1956-os magyar menekülthullámot?"},
                            {"speaker": "Levéltáros", "text": "____"},
                        ],
                        [
                            "A legtöbben kénytelenek voltak kivándorolni, és csak a rendszerváltás után térhettek haza.",
                            "Mindenki azonnal visszatért a forradalom másnapján a munkahelyére.",
                            "Az emberek nem vándoroltak el sehova, hanem otthon maradtak.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Miért dönt úgy egy nemzetközi karriert befutott kutató, hogy hazatér?"},
                            {"speaker": "Professzor", "text": "____"},
                        ],
                        [
                            "Mert a szakmai sikerek mellett a hazatérés lehetőséget ad arra, hogy a tudását a szülőföldjén kamatoztassa.",
                            "Mert a kivándorlás mindenki számára törvényileg tiltott dolog.",
                            "Mert a repülőjegyek ára miatt nem tud visszatérni sehova.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence contrasting 'kivándorol' (abroad) and 'hazatér' (homecoming).",
                                "answer": "Bár a fiatal mérnök gazdasági okokból vándorolt ki Nyugatra, évek múltán mégis hazatért Magyarországra.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'visszatér' describing a neutral return to a university or workplace.",
                                "answer": "A külföldi tanulmányút befejeztével a hallgató visszatért a budapesti egyetemére.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Az író a száműzetésben sem felejtette el az anyanyelvét, és mindig remélte, hogy egyszer még ____. (will return home)",
                        "hazatér",
                        "Even in exile, the writer did not forget his mother tongue, and always hoped that one day he would return home.",
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes the act of returning to one's native country after living abroad?",
                        ["hazatérés", "kivándorlás", "elvándorlás"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Leaving, Returning, and Starting Over",
            "grammar_label": "Narrative aspectual structures and diasporic longing (honvágy, diaszpóra, száműzetés)",
            "goals": [
                "I can narrate personal and historical experiences of exile using aspectual preverbs",
                "I can discuss concepts of diaspora, homesickness (honvágy), and fresh beginnings (újrakezdés)",
                "I can describe dual cultural identity using nuanced B2 vocabulary",
            ],
            "grammar_doc": {
                "slug": "narrating-exile-and-diaspora",
                "title": "Narrating Exile, Diaspora, and Starting Anew",
                "text1_title": "Aspectual Interplay in Migration Narratives",
                "text1": "Personal accounts of migration rely heavily on the dynamic aspectual interplay of perfective and imperfective verb forms. Preverbs pinpoint decisive turning points: 'elhatározta magát' (resolved to leave), 'átlépte a határt' (crossed the border), 'letelepedett' (settled down). Ongoing states of emotional friction, cultural preservation, and nostalgia are expressed using bare imperfective verbs or iterative adverbials: 'folyamatosan küzdött a honvággyal', 'őrizte az anyanyelvét'.",
                "text2_title": "Existential Vocabulary of the Diasporic Experience",
                "text2": "The experience of living outside the motherland involves specific sociological concepts: 'diaszpóra' (dispersed ethnic community abroad), 'száműzetés' (political exile or banishment), 'újrakezdés' (starting over in a new milieu), and 'kettős identitás' (navigating dual cultural allegiances without sacrificing one's heritage).",
                "table_title": "Aspectual and Diasporic Narrative Markers",
                "table_rows": [
                    ["átlépte a határt", "1956 őszén gyalog lépte át a határt. (Crossed the border on foot.)"],
                    ["letelepedett", "A család Torontóban telepedett le. (Settled down in Toronto.)"],
                    ["honvágyat érez", "Éveken át marcangoló honvágyat érzett. (Felt agonizing homesickness.)"],
                    ["újrakezdi az életét", "Idős kora ellenére újrakezdte az életét. (Started his/her life over.)"],
                ],
                "examples": [
                    {
                        "spanish": "A politikai száműzetésben élő költő verseiben mindvégig jelen volt a csillapíthatatlan honvágy.",
                        "english": "In the poems of the poet living in political exile, unquenchable homesickness was present throughout.",
                    },
                    {
                        "spanish": "A nyugati magyar diaszpóra évtizedeken át kitartóan támogatta a hazai kulturális intézményeket.",
                        "english": "The Western Hungarian diaspora persistently supported cultural institutions back home across decades.",
                    },
                    {
                        "spanish": "Az emigránsok számára az újrakezdés nem csupán anyagi, hanem mély lelki kihívást is jelentett.",
                        "english": "For the emigrants, starting over represented not only a financial but also a profound spiritual challenge.",
                    },
                    {
                        "spanish": "A külföldön felnőtt gyermekek büszkén vállalják a kettős identitás gazdagságát.",
                        "english": "The children raised abroad proudly embrace the richness of a dual identity.",
                    },
                ],
                "tip": "When narrating past habitual actions in exile, remember to use preverbal detachment with 'gyakran' or negative words: 'Gyakran felidézte az otthoni tájakat', 'Soha nem felejtette el a szülőföldjét'.",
            },
            "words": [
                {"lemma": "honvágy", "translation": "homesickness / nostalgia for homeland", "pos": "noun"},
                {"lemma": "diaszpóra", "translation": "diaspora", "pos": "noun"},
                {"lemma": "száműzetés", "translation": "exile / banishment", "pos": "noun"},
                {"lemma": "újrakezdés", "translation": "starting anew / fresh start", "pos": "noun"},
                {"lemma": "kettős identitás", "translation": "dual identity", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'honvágy' signify in Hungarian literature and life?",
                        [
                            "a deep, painful yearning for one's homeland when living far away",
                            "a desire to buy a larger house in the suburbs",
                            "a physical allergy caused by unfamiliar foreign spices",
                        ],
                        0,
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term describes an ethnic community living dispersed outside its historical homeland?",
                        ["diaszpóra", "száműzetés", "beilleszkedés"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["honvágy", "homesickness"],
                            ["diaszpóra", "diaspora"],
                            ["száműzetés", "exile / banishment"],
                            ["újrakezdés", "fresh start / starting anew"],
                            ["kettős identitás", "dual identity"],
                        ],
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the perfective sentence indicating a completed action of settlement:",
                        [
                            "A menekült család 1957 telén végleg letelepedett Ausztráliában.",
                            "A menekült család letelepedni akart minden évben.",
                            "A menekült család telepedett lefele a dombon.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which preverb shows detaching in the negative sentence: 'Az író soha nem ____ felejtette a hazáját'?",
                        ["felejtette el", "elfelejtette", "belefelejtette"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Bár mindent elveszített a háborúban, negyvenévesen mégis képes volt az ____. (fresh start)",
                        "újrakezdésre",
                        "Although he lost everything in the war, at the age of forty he was still capable of a fresh start.",
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A diktatúra évei alatt sok ellenzéki értelmiségi kényszerült önkéntes ____. (into exile)",
                        "száműzetésbe",
                        "During the years of dictatorship, many dissident intellectuals were forced into voluntary exile.",
                        ["b2-figurative-preverbs"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "magyar", "diaszpóra", "szervezetei", "ápolják", "a", "nemzeti", "hagyományokat."],
                        ["A", "magyar", "diaszpóra", "szervezetei", "ápolják", "a", "nemzeti", "hagyományokat."],
                        "The organizations of the Hungarian diaspora foster national traditions.",
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az első hónapok magányában a diákot szinte megbénította a kínzó ____. (homesickness)",
                        "honvágy",
                        "In the loneliness of the first months, the student was almost paralyzed by agonizing homesickness.",
                        ["b2-28-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kettős", "identitás", "nem", "hátrány,", "hanem", "rendkívüli", "kulturális", "érték."],
                        ["A", "kettős", "identitás", "nem", "hátrány,", "hanem", "rendkívüli", "kulturális", "érték."],
                        "Dual identity is not a disadvantage, but an extraordinary cultural asset.",
                        ["b2-28-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Rádiós műsorvezető", "text": "Hogyan tudta feldolgozni a száműzetés éveit a neves író?"},
                            {"speaker": "Irodalomtörténész", "text": "____"},
                        ],
                        [
                            "A honvágyat az anyanyelvű írásba fojtotta, és az újrakezdés nehézségeit műalkotássá formálta.",
                            "Egyszerűen abbahagyta az írást, és soha többé nem gondolt Magyarországra.",
                            "A száműzetésben csak idegen nyelven publikált bestseller regényeket.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Egyetemista", "text": "Nem okoz belső konfliktust a kettős identitás megélése?"},
                            {"speaker": "Kutató", "text": "____"},
                        ],
                        [
                            "Kezdetben hozhat feszültséget, de érett személyiségként az ember mindkét kultúra értékeit magáénak vallja.",
                            "A törvény tiltja a kettős identitást, ezért az embernek választania kell egyetlen nyelvet.",
                            "Csak azoknak van kettős identitásuk, akik soha nem utaztak külföldre.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'honvágy' describing how an emigrant endured life far from home.",
                                "answer": "Bár sikeres karriert futott be Londonban, a honvágy soha nem múlt el a szívéből.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'diaszpóra' explaining the cultural preservation role of communities abroad.",
                                "answer": "A tengerentúli magyar diaszpóra hétvégi iskolák fenntartásával őrzi az anyanyelvet a fiatalok körében.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Az emigránsok a kezdeti bizonytalanság után sikeresen ____ az életüket az új környezetben. (restarted)",
                        "újrakezdték",
                        "After initial uncertainty, the emigrants successfully restarted their lives in the new environment.",
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes possessing belonging to two cultures simultaneously?",
                        ["kettős identitás", "egyoldalú beolvadás", "ideiglenes tartózkodás"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Brain Drain vs. Brain Circulation",
            "grammar_label": "Preverb verbs in academic mobility and intellectual networks (agyelszívás, tudástranszfer)",
            "goals": [
                "I can discuss brain drain (agyelszívás) vs. brain circulation in academic and economic life",
                "I can employ academic mobility collocations like tudástranszfer and szellemi tőke",
                "I can analyze the value of international networks (kapcsolati háló) with formal preverbs",
            ],
            "grammar_doc": {
                "slug": "brain-drain-and-knowledge-circulation",
                "title": "Brain Drain vs. Brain Circulation: agyelszívás és tudástranszfer",
                "text1_title": "From Unidirectional Loss to Dynamic Circulation",
                "text1": "In contemporary socio-economic discourse, the unidirectional outflow of highly trained talent is termed 'agyelszívás' (brain drain). When researchers return home or maintain institutional bridges with their native country, scholars speak of 'tudástranszfer' (knowledge transfer) or 'agyforgás' (brain circulation). Preverb verbs of exchange, enrichment, and accumulation feature prominently: 'felhalmoz' (to accumulate), 'kicserél' (to exchange), 'átad' (to pass on), 'hazahoz' (to bring back home).",
                "text2_title": "Intellectual Capital and Professional Networks",
                "text2": "'Szellemi tőke' (intellectual capital) refers to the collective knowledge, technical expertise, and innovation capacity embodied in specialists. A mobile professional builds a far-reaching 'kapcsolati háló' (network of professional contacts), which serves as a conduit for collaborative grants, joint publications, and technological innovation.",
                "table_title": "Academic Mobility Terminology",
                "table_rows": [
                    ["agyelszívás", "A gazdaságilag fejlettebb centrumok felé irányuló agyelszívás aggasztó. (Brain drain.)"],
                    ["tudástranszfer", "A két egyetem közötti tudástranszfer új szabadalmakhoz vezetett. (Knowledge transfer.)"],
                    ["kutatói mobilitás", "A kutatói mobilitás nélkülözhetetlen az akadémiai fejlődéshez. (Researcher mobility.)"],
                    ["kapcsolati háló", "Kiterjedt nemzetközi kapcsolati hálót épített ki. (Built up an extensive network.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az orvosi szférában tapasztalható agyelszívás súlyos ellátási problémákat okoz a származási országban.",
                        "english": "The brain drain experienced in the medical sphere causes severe care issues in the country of origin.",
                    },
                    {
                        "spanish": "A nemzetközi ösztöndíjak célja, hogy a megszerzett tapasztalatok tudástranszfer útján hazajussanak.",
                        "english": "The goal of international scholarships is for acquired experience to return home via knowledge transfer.",
                    },
                    {
                        "spanish": "A szellemi tőke megőrzése és gyarapítása a modern gazdaságok legfontosabb stratégiai feladata.",
                        "english": "Preserving and expanding intellectual capital is the most important strategic task of modern economies.",
                    },
                    {
                        "spanish": "A külföldi vendégprofesszori év során felbecsülhetetlen értékű kapcsolati háló jött létre a felek között.",
                        "english": "During the year as visiting professor abroad, an invaluable network of contacts came into being between the parties.",
                    },
                ],
                "tip": "Compound terms like 'szellemi tőke' and 'kapcsolati háló' behave syntactically as standard noun phrases; watch out for preverbs showing transfer: 'hazahozza a tudást' vs. 'kiviszi a szaktudást'.",
            },
            "words": [
                {"lemma": "agyelszívás", "translation": "brain drain", "pos": "noun"},
                {"lemma": "tudástranszfer", "translation": "knowledge transfer", "pos": "noun"},
                {"lemma": "kutatói mobilitás", "translation": "researcher mobility", "pos": "expression"},
                {"lemma": "szellemi tőke", "translation": "intellectual capital", "pos": "expression"},
                {"lemma": "kapcsolati háló", "translation": "networking / network of contacts", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'agyelszívás' in economic and demographic discourse?",
                        [
                            "the migration of highly qualified and talented individuals to wealthier regions",
                            "a neurological surgical procedure performed in university hospitals",
                            "an advertising strategy designed to hypnotize consumers",
                        ],
                        0,
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term designates the exchange and dissemination of expertise across institutions?",
                        ["tudástranszfer", "száműzetés", "kivándorlás"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["agyelszívás", "brain drain"],
                            ["tudástranszfer", "knowledge transfer"],
                            ["kutatói mobilitás", "researcher mobility"],
                            ["szellemi tőke", "intellectual capital"],
                            ["kapcsolati háló", "network of contacts"],
                        ],
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which preverb fits best in 'A fiatal mérnök hazatérve haza____hozta a legmodernebb technológiai ismereteket'?",
                        ["-", "el-", "ki-"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the verb expressing knowledge accumulation: 'A kutató évtizedeken át hatalmas tudást ____halmozott fel.'",
                        ["fel-", "le-", "szét-"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A fejlett országok kutatóintézetei tudatosan igyekeznek ____ a kelet-európai tehetségeket. (to attract/draw away)",
                        "elszívni",
                        "Research institutes of developed countries consciously strive to drain Eastern European talent.",
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A nemzetközi konferenciákon való részvétel elősegíti a szakmai tapasztalatok hatékony ____. (exchange)",
                        "kicserélését",
                        "Participation in international conferences promotes the effective exchange of professional experiences.",
                        ["b2-figurative-preverbs"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "kutatói", "mobilitás", "elősegíti", "az", "innovatív", "ötletek", "terjedését."],
                        ["A", "kutatói", "mobilitás", "elősegíti", "az", "innovatív", "ötletek", "terjedését."],
                        "Researcher mobility promotes the spread of innovative ideas.",
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az egyetemek közötti kétoldalú együttműködés felgyorsította a közvetlen ____ folyamatát. (knowledge transfer)",
                        "tudástranszfer",
                        "Bilateral cooperation between universities accelerated the process of direct knowledge transfer.",
                        ["b2-28-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "nemzetközi", "kapcsolati", "háló", "nélkülözhetetlen", "a", "sikeres", "pályázatokhoz."],
                        ["A", "nemzetközi", "kapcsolati", "háló", "nélkülözhetetlen", "a", "sikeres", "pályázatokhoz."],
                        "An international network of contacts is indispensable for successful grant applications.",
                        ["b2-28-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Oktatáspolitikus", "text": "Hogyan fordítható át az agyelszívás kölcsönösen előnyös tudáscserévé?"},
                            {"speaker": "Kutatóintézet vezetője", "text": "____"},
                        ],
                        [
                            "Olyan vendégoktatói és csereprogramokat kell finanszírozni, amelyek hazavonzzák a szellemi tőkét és erősítik a tudástranszfert.",
                            "Minden fiatal diplomásnak el kell venni az útlevelét a határon.",
                            "Az agyelszívás nem létezik, csupán a televízióban beszélnek róla.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "PhD-hallgató", "text": "Érdemes néhány évre külföldi egyetemre menni posztdoktori kutatóként?"},
                            {"speaker": "Témavezető", "text": "____"},
                        ],
                        [
                            "Feltétlenül, hiszen a kutatói mobilitás révén olyan kapcsolati hálót építhetsz ki, amely egész pályádon segít majd.",
                            "Nem érdemes, mert a külföldön szerzett tudás Magyarországon teljesen értéktelen.",
                            "A külföldi munka automatikusan az állampolgárság elvesztésével jár.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'szellemi tőke' to describe a nation's human resource value.",
                                "answer": "A jól képzett mérnökök és orvosok jelentik egy kis ország legértékesebb szellemi tőkéjét.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'tudástranszfer' in an academic or industrial context.",
                                "answer": "Az egyetem és a technológiai vállalatok közötti tudástranszfer számos új munkahelyet teremtett.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A külföldről hazatérő tudósok értékes tapasztalatokat ____ haza az anyaországba. (brought home)",
                        "hoztak",
                        "Scientists returning from abroad brought valuable experiences home to the motherland.",
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the loss of highly educated professionals to foreign economies?",
                        ["agyelszívás", "szellemi tőke", "kapcsolati háló"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Debating Mobility in a Globalized Europe",
            "grammar_label": "Analytical discourse on migration policy and repatriation incentives (fogadó ország, megtartó erő)",
            "goals": [
                "I can contrast sending countries (kibocsátó ország) and host countries (fogadó ország)",
                "I can formulate policy proposals regarding retention power (megtartó erő) and repatriation (hazavonz)",
                "I can structure an analytical argument about mobility in a globalized European context",
            ],
            "grammar_doc": {
                "slug": "debating-mobility-and-return-policies",
                "title": "Debating Mobility, Retention, and Repatriation Policies",
                "text1_title": "Push and Pull Framework in Analytical Discourse",
                "text1": "Formal policy debates analyze migration through the dynamic between 'kibocsátó ország' (sending country) and 'fogadó ország' (host country). Push factors (taszító tényezők) such as lower wages, rigid hierarchies, or lack of funding are weighed against pull factors (vonzó tényezők) such as technological infrastructure and meritocratic advancement.",
                "text2_title": "Retention Power and Repatriation Strategies",
                "text2": "States design public policies to bolster their domestic 'megtartó erő' (capacity to retain skilled labor) and formulate incentives aimed to 'hazavonz' (attract back home) experienced expatriates. This register relies on modal verbs of necessity, conditional hedging ('szükségesnek mutatkozna', 'célszerű lenne'), and complex compound nouns.",
                "table_title": "Policy Argumentation Terms",
                "table_rows": [
                    ["kibocsátó ország", "A kibocsátó országok demográfiai veszteséget szenvednek el. (Sending countries.)"],
                    ["fogadó ország", "A fogadó ország integrációs programokat biztosít. (Host country.)"],
                    ["megtartó erő", "A hazai munkaerőpiac megtartó erejét növelni kell. (Retention capacity.)"],
                    ["hazavonz", "Célzott kutatási ösztöndíjakkal kívánják hazavonzani a fiatalokat. (Attract back.)"],
                ],
                "examples": [
                    {
                        "spanish": "A közép-európai kibocsátó országok gazdasági felzárkózását lassítja a szakképzett munkaerő hiánya.",
                        "english": "The economic catch-up of Central European sending countries is slowed by the shortage of skilled labor.",
                    },
                    {
                        "spanish": "A nyugati fogadó országok profitálnak a képzett vendégmunkások adóbefizetéseiből.",
                        "english": "Western host countries profit from the tax contributions of skilled guest workers.",
                    },
                    {
                        "spanish": "A versenyképes fizetések és a kiszámítható lakhatás erősítik a hazai megtartó erőt.",
                        "english": "Competitive salaries and predictable housing strengthen domestic retention power.",
                    },
                    {
                        "spanish": "Korszerű kutatói laboratóriumok létesítésével sikeresen haza lehet vonzani a külföldön dolgozó tudósokat.",
                        "english": "By establishing state-of-the-art research laboratories, scientists working abroad can be successfully attracted back home.",
                    },
                ],
                "tip": "Note the verbal prefix split with 'haza-': 'sikeresen haza lehet vonzani' (infinitive with modal) vs. 'a kormány hazavonzza a tehetségeket' (present indicative).",
            },
            "words": [
                {"lemma": "fogadó ország", "translation": "host country", "pos": "expression"},
                {"lemma": "kibocsátó ország", "translation": "sending country / country of origin", "pos": "expression"},
                {"lemma": "megtartó erő", "translation": "retention power / retaining capacity", "pos": "expression"},
                {"lemma": "nemzetközi tapasztalat", "translation": "international experience", "pos": "expression"},
                {"lemma": "hazavonz", "translation": "to attract home / draw back home", "pos": "verb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the state that receives arriving migrant workers?",
                        ["fogadó ország", "kibocsátó ország", "őshaza"],
                        0,
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'megtartó erő' in demographic policy?",
                        [
                            "an economy's ability to keep its educated workforce from migrating away",
                            "the tensile strength of architectural cables used in bridge building",
                            "the legal authority to detain foreign criminals at the border",
                        ],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["fogadó ország", "host country"],
                            ["kibocsátó ország", "sending country"],
                            ["megtartó erő", "retention power"],
                            ["nemzetközi tapasztalat", "international experience"],
                            ["hazavonz", "to attract back home"],
                        ],
                        ["b2-28-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the correct word order with a modal auxiliary: 'A modern laboratóriumokkal haza ____ vonzani a kutatókat.'",
                        ["lehet", "nem lehetne sehova", "vándorol"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which preverb is appropriate in 'Az állam célzott programokkal igyekszik ____telepíteni a külföldön élő szakembereket'?",
                        ["haza-", "ki-", "le-"],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A gazdasági stabilitás megteremtése elengedhetetlen ahhoz, hogy a kormány ____ a külföldön élő fiatalokat. (may attract back home)",
                        "hazavonzza",
                        "Creating economic stability is essential in order for the government to attract back home the young people living abroad.",
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A minisztérium olyan támogatási rendszert dolgozott ki, amely hatékonyan képes ____ a tehetséges mérnököket. (to attract home)",
                        "hazavonzani",
                        "The ministry developed a support system that is capable of effectively attracting home talented engineers.",
                        ["b2-figurative-preverbs"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "fogadó", "ország", "széles", "körű", "integrációs", "képzést", "biztosít."],
                        ["A", "fogadó", "ország", "széles", "körű", "integrációs", "képzést", "biztosít."],
                        "The host country provides broad integration training.",
                        ["b2-figurative-preverbs"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A kelet-közép-európai térség mint ____ súlyos munkaerőhiánnyal küzd az egészségügyben. (sending country)",
                        "kibocsátó ország",
                        "The East-Central European region as a sending country struggles with a severe labor shortage in healthcare.",
                        ["b2-28-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "nemzetközi", "tapasztalat", "jelentős", "előnyt", "jelent", "a", "hazai", "munkaerőpiacon."],
                        ["A", "nemzetközi", "tapasztalat", "jelentős", "előnyt", "jelent", "a", "hazai", "munkaerőpiacon."],
                        "International experience represents a significant advantage on the domestic job market.",
                        ["b2-28-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Vitavezető", "text": "Milyen eszközökkel növelhető a hazai gazdaság megtartó ereje?"},
                            {"speaker": "Közgazdász", "text": "____"},
                        ],
                        [
                            "Versenyképes bérekkel, kiszámítható karrierpályával és a nemzetközi tapasztalat megbecsülésével.",
                            "A külföldi utazások teljes betiltásával és a határok azonnali lezárásával.",
                            "A megtartó erő nem növelhető, mert minden ember elvándorol a szülőföldjéről.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Egyetemi oktató", "text": "Hogyan értékelik a vállalatok a külföldön szerzett diplomát?"},
                            {"speaker": "HR-vezető", "text": "____"},
                        ],
                        [
                            "A nemzetközi tapasztalat óriási előny, különösen ha a jelölt képes azt a hazai környezetben alkalmazni.",
                            "A külföldi diploma gyanús, ezért a jelentkezőket azonnal elutasítják.",
                            "A vállalatok csak azokat veszik fel, akik soha nem tanultak idegen nyelveket.",
                        ],
                        0,
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'megtartó erő' to describe economic retention strategies.",
                                "answer": "A kutatói ösztöndíjak jelentősen növelik az egyetemi szféra megtartó erejét a fiatal szakemberek körében.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'hazavonz' to express attracting expatriates back to their homeland.",
                                "answer": "Az új innovációs központ célja, hogy hazavonzza a külföldön dolgozó magyar mérnököket.",
                            }
                        ],
                        ["b2-figurative-preverbs"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A kedvező adózási feltételek és az induló támogatások sok vállalkozót ____ Magyarországra. (attracted back home)",
                        "hazavonzottak",
                        "Favorable tax conditions and startup subsidies attracted many entrepreneurs back home to Hungary.",
                        ["b2-figurative-preverbs"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase designates the origin country from which migrants leave?",
                        ["kibocsátó ország", "fogadó ország", "tranzitállam"],
                        0,
                        ["b2-28-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can master figurative preverbs of integration and alienation (beilleszkedik, elidegenedik, gyökeret ver)",
            "I can discern directional preverb contrasts in migration contexts (kivándorol vs. elvándorol, hazatér vs. visszatér)",
            "I can discuss diasporic longing, brain drain, and return mobility policies at an advanced B2 level",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["beilleszkedik", "to integrate / assimilate into"],
                    ["elidegenedik", "to become alienated from"],
                    ["hazatelepül", "to repatriate back home"],
                    ["honvágy", "homesickness"],
                    ["agyelszívás", "brain drain"],
                ],
                ["b2-28-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'kettős identitás' signify in diasporic sociological studies?",
                [
                    "the simultaneous identification with both one's heritage culture and the host culture",
                    "carrying two passports with different false names",
                    "suffering from a severe psychological dissociative disorder",
                ],
                0,
                ["b2-28-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly illustrates the directional contrast between 'hazatér' and 'visszatér'?",
                [
                    "A professzor az emigrációból végleg hazatért szülőföldjére, majd a konferenciáról visszatért szállodájába.",
                    "A professzor hazatért a szállodájába aludni három órára.",
                    "A professzor kivándorolt a szobájából a konyhába.",
                ],
                0,
                ["b2-figurative-preverbs"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A hazai munkaerőpiac alacsony ____ miatt sok tehetséges szakember dönt a külföldi munka mellett. (retention power)",
                "megtartó ereje",
                "Due to the low retention power of the domestic job market, many talented specialists decide in favor of working abroad.",
                ["b2-28-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A hosszú külföldi tartózkodás során a művész teljesen ____ az anyanyelvi közegétől. (became alienated)",
                "elidegenedett",
                "During the long stay abroad, the artist became completely alienated from his native-language milieu.",
                ["b2-figurative-preverbs"],
            ),
            fb(
                "grammar",
                "recall",
                "A nyugdíjas mérnök három évtizedes kanadai munka után végleg ____ Budapestre. (repatriated)",
                "hazatelepült",
                "The retired engineer repatriated to Budapest permanently after three decades of Canadian work.",
                ["b2-figurative-preverbs"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'elvándorol' chosen over 'kivándorol' in: 'A keleti megyékből tízezrek vándoroltak el a fővárosba'?",
                [
                    "Because it denotes internal movement away from a region within the country rather than crossing national borders.",
                    "Because 'kivándorol' can never take a past tense suffix in Hungarian.",
                    "Because 'elvándorol' only applies to seasonal agricultural workers.",
                ],
                0,
                ["b2-figurative-preverbs"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Egyetemi hallgató", "text": "Hogyan birkózott meg az író az emigráció magányával Márai naplója szerint?"},
                    {"speaker": "Magyartanár", "text": "____"},
                ],
                [
                    "Az anyanyelvbe kapaszkodott, és a mindennapi írás révén őrizte meg belső integritását az idegen világban.",
                    "Azonnal feladta a magyar nyelvet, és kizárólag olaszul társalgott mindenkivel.",
                    "Hazatért Budapestre az első adandó alkalommal, mert nem bírta a tengeri levegőt.",
                ],
                0,
                ["b2-figurative-preverbs"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'gyökeret ver' is used in its correct idiomatic meaning:",
                [
                    "A menekült család sok viszontagság után végleg gyökeret vert az új-zélandi kikötővárosban.",
                    "A kertész tegnap délután gyökeret vert a virágágyás közepébe a lapáttal.",
                    "A repülőgép gyökeret vert a kifutópályán a leszállás közben.",
                ],
                0,
                ["b2-figurative-preverbs"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "fiatal", "kutató", "könnyen", "beilleszkedett", "a", "nemzetközi", "tudományos", "közösségbe."],
                ["A", "fiatal", "kutató", "könnyen", "beilleszkedett", "a", "nemzetközi", "tudományos", "közösségbe."],
                "The young researcher integrated easily into the international scientific community.",
                ["b2-figurative-preverbs"],
            ),
            sb(
                "grammar",
                "produce",
                ["Célzott", "támogatásokkal", "sikeresen", "haza", "lehet", "vonzani", "a", "külföldön", "élő", "mérnököket."],
                ["Célzott", "támogatásokkal", "sikeresen", "haza", "lehet", "vonzani", "a", "külföldön", "élő", "mérnököket."],
                "With targeted subsidies, engineers living abroad can be successfully attracted back home.",
                ["b2-figurative-preverbs"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause analytical argument contrasting 'elvándorol', 'tudástranszfer', and 'hazatelepül'.",
                        "answer": "Bár a fiatal szakemberek jelentős része jobb lehetőségek reményében elvándorol a szülőföldjéről, a nemzetközi tudástranszfer révén kapcsolatban maradnak az anyaországgal; sőt évek múltával sokan sikeresen hazatelepülnek, gazdagítva a hazai tudományos életet.",
                    }
                ],
                ["b2-figurative-preverbs"],
            ),
        ],
    },
}
