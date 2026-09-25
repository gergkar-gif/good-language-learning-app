#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 1, 2, and 3:
  - Unit 1: b2-kavehazikultura ("The Coffeehouse Republic: Nyugat & Print Culture")
  - Unit 2: b2-szecesszio ("Fin-de-Siècle Budapest & Hungarian Secession")
  - Unit 3: b2-nyelvujitas ("The Language Reform & the Politics of Hungarian")
"""
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
from b2_unit_builder_helper import build_culture_unit


# ============================================================================
# CULTURE UNIT 1: b2-kavehazikultura
# ============================================================================
UNIT_1_KAVEHAZIKULTURA = {
    "unit_num": 1,
    "slug": "kavehazikultura",
    "title": "The Coffeehouse Republic: Nyugat & Print Culture",
    "grammar_skill": "b2-contrastive-topic",
    "vocab_skill": "b2-kavehazikultura-vocab",
    "theme": "Coffeehouse literary culture and Nyugat",
    "location": "Budapest (New York, Centrál és Hadik kávéház)",
    "combined_story_title": "A New York kávéház tintatartója",
    "combined_story_summary": "How Budapest's 500 turn-of-the-century coffeehouses and the journal Nyugat (1908) forged modern Hungarian literature through fierce public debates between modernists and conservatives.",
    "intro_body": [
        "At the turn of the twentieth century, Budapest boasted more than five hundred coffeehouses. Far more than places to drink espresso, institutions like the New York, the Centrál, and the Hadik functioned as open editorial offices, heated living rooms for penniless poets, and democratic arenas of intellectual debate.",
        "In this unit, you will explore how the literary review Nyugat (1908–1941) transformed Hungarian prose and poetry while mastering B2 contrastive topicalization (ami X-et illeti, ezzel szemben, míg ... addig, X viszont) and focus-preverb inversion."
    ],
    "lessons": [
        {
            "num": 1,
            "title": "Five Hundred Coffeehouses on the Danube",
            "grammar_label": "Contrastive topicalization with ami X-et illeti and viszont",
            "goals": [
                "I can describe the social and literary role of turn-of-the-century Budapest coffeehouses.",
                "I can frame contrasting topics using ami X-et illeti ('as for X') and X viszont ('X, on the other hand').",
                "I can distinguish between everyday hospitality vocabulary and literary café terminology."
            ],
            "story_segment": {
                "seg_slug": "otszazkavehaz",
                "title": "Ötszáz kávéház a Duna partján",
                "summary": "Around 1900, Budapest's five hundred coffeehouses became a second home and open editorial room for writers, offering paper, ink, and encyclopedias for the price of a single cup.",
                "location": "Budapest, Erzsébet körút (New York kávéház)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az ezernyolcszázas évek végén és a huszadik század hajnalán Budapestet joggal nevezték a kávéházak fővárosának. Míg más európai nagyvárosokban az írók többnyire zárt szalonokban vagy egyetemi klubokban találkoztak, addig a Duna-parti világvárosban több mint ötszáz kávéház várta a szellemi élet szereplőit. A New York, a Centrál vagy a későbbi Hadik nem pusztán vendéglátóhely volt, hanem a modern magyar irodalom nyitott műhelye."
                    },
                    {
                        "type": "narration",
                        "text": "Ami a fiatal újságírókat és költőket illeti, sokuknak saját fűtött szobára sem tellett a szűkös albérletekben. A kávéház ezzel szemben egész napra meleget, csillárfényt, friss külföldi hírlapokat és lexikonokat kínált egyetlen csésze fekete áráért. A főpincér nemcsak a rendelést vette fel, hanem gyakran postásként, hitelezőként és bizalmas tanácsadóként is segítette a törzsvendégeket."
                    },
                    {
                        "type": "narration",
                        "text": "A New York kávéház legendája szerint a megnyitó éjszakáján Molnár Ferenc és barátai a Dunába dobták az épület kulcsát, hogy a csarnok soha többé ne zárhasson be. Akár igaz ez az anekdota, akár a városi folklór szülte, pontosan kifejezi a korszak életszemléletét: az irodalom nem a magányos dolgozószobában, hanem a nyilvános tér pezsgésében született meg."
                    },
                    {
                        "type": "narration",
                        "text": "A márványasztaloknál sajátos munkamegosztás alakult ki. A karzaton a szerkesztők javították a friss kefelenyomatokat, a mélyvíznek nevezett alsó szinten viszont a kritikusok, színészek és színházigazgatók vitatkoztak hajnalig. Aki írásból akart megélni, annak elég volt kérnie egy adag úgynevezett írói készletet: néhány ív keskeny papírszeletet, azaz kutyanyelvet, valamint egy üveg kékesfekete tintát."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a demokratikus tér lebontotta a társadalmi korlátokat is. A vidékről érkező, ismeretlen tehetség ugyanannál a márványasztalnál ülhetett le, ahol a korszak ünnepelt tárcaírói dolgoztak, és egyetlen jól sikerült kézirat elegendő volt ahhoz, hogy másnap már az egész körút az ő nevét emlegesse."
                    }
                ]
            },
            "words": [
                {"lemma": "kávéház", "translation": "coffeehouse, grand café", "pos": "noun"},
                {"lemma": "törzsvendég", "translation": "regular patron / regular guest", "pos": "noun"},
                {"lemma": "márványasztal", "translation": "marble table", "pos": "noun"},
                {"lemma": "kutyanyelv", "translation": "narrow paper slip used by writers in cafés", "pos": "noun"},
                {"lemma": "kefelenyomat", "translation": "galley proof", "pos": "noun"},
                {"lemma": "ami azt illeti", "translation": "as far as that is concerned / for that matter", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "contrastive-topic-intro",
                "title": "Framing Contrastive Topics: ami X-et illeti and viszont",
                "text1_title": "Setting the Stage with ami X-et illeti",
                "text1": "In B2 Hungarian essayistic and historical prose, writers frequently shift perspective between social groups, institutions, or viewpoints. The construction ami + [Accusative noun phrase] + illeti ('as for X / as far as X is concerned') places a new or contrasted topic at the left periphery of the sentence before the main comment is made.",
                "text2_title": "Postpositive Contrast with viszont",
                "text2": "While de ('but') stands at the beginning of a clause, viszont ('however / on the other hand / by contrast') is enclitic: it immediately follows the newly contrasted topic (e.g., A karzaton a szerkesztők dolgoztak, az alsó szinten viszont a kritikusok vitatkoztak). This immediately signals to the listener which two elements are being weighed against each other.",
                "table_title": "Core Contrastive Topic Frames",
                "table_rows": [
                    ["Ami a fiatal költőket illeti, ...", "As for the young poets, ..."],
                    ["Ami a szerkesztőséget illeti, ...", "As far as the editorial office is concerned, ..."],
                    ["A szalonok zártak voltak, a kávéház viszont nyitott.", "Salons were closed; the coffeehouse, by contrast, was open."],
                    ["A főpincér nemcsak felszolgált, hanem hitelezett is.", "The headwaiter not only served, but also extended credit."]
                ],
                "examples": [
                    {
                        "spanish": "Ami a fiatal újságírókat illeti, sokuknak saját fűtött szobára sem tellett.",
                        "english": "As for the young journalists, many of them could not even afford a heated room of their own."
                    },
                    {
                        "spanish": "A karzaton a szerkesztők javították a szöveget, az alsó szinten viszont a kritikusok vitatkoztak.",
                        "english": "On the gallery the editors corrected the text, whereas on the lower level the critics debated."
                    },
                    {
                        "spanish": "Ami a New York kávéházat illeti, az épület éjjel-nappal nyitva állt az írók előtt.",
                        "english": "As far as the New York Café was concerned, the building stood open to writers day and night."
                    }
                ],
                "tip": "Remember that illeti requires the direct object case (-t) on the noun phrase inside the ami ... illeti frame: Ami a modern irodalmat illeti (never nominative *Ami a modern irodalom illeti)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelentett a pesti kávéházi nyelvben a 'kutyanyelv' kifejezés?",
                    "options": [
                        "Keskeny papírszeletet, amelyre az írók és újságírók a kézirataikat írták.",
                        "Egy különleges, fűszeres feketekávét.",
                        "A kávéház bejárata előtti vörös szőnyeget."
                    ],
                    "correct": 0,
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A szerkesztők a kávéház karzatán javították a nyomdából érkezett friss _____ példányokat. (galley proof)",
                    "answer": "kefelenyomat",
                    "english": "On the gallery of the coffeehouse, the editors corrected the fresh galley-proof copies arriving from the printing press.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Ami a fiatal _____ illeti, a kávéház számukra egyszerre volt otthon és munkahely. (költőket)",
                    "answer": "költőket",
                    "english": "As for the young poets, for them the coffeehouse was both a home and a workplace.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat használja helyesen a szembeállító 'viszont' kötőszót?",
                    "options": [
                        "A szalonokba csak meghívóval lehetett belépni, a kávéházak viszont mindenki előtt nyitva álltak.",
                        "A szalonokba csak meghívóval lehetett belépni, viszont a kávéházak mindenki előtt nyitva álltak.",
                        "Viszont a szalonokba csak meghívóval lehetett belépni, a kávéházak nyitva álltak."
                    ],
                    "correct": 0,
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Ami", "a", "törzsvendégeket", "illeti,", "a", "főpincér", "mindenkit", "név", "szerint", "ismert."],
                    "solution": ["Ami", "a", "törzsvendégeket", "illeti,", "a", "főpincér", "mindenkit", "név", "szerint", "ismert."],
                    "english": "As for the regular patrons, the headwaiter knew everyone by name.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért volt különösen fontos a kávéház a szegényebb sorsú fiatal írók számára a századfordulón?",
                    "options": [
                        "Mert egyetlen csésze fekete áráért fűtött teret, világítást, papírt, tintát és külföldi lapokat kaptak.",
                        "Mert a kávéház tulajdonosa minden hónapban állami fizetést osztott szét közöttük.",
                        "Mert a kávéházban tilos volt politikáról és irodalomról vitatkozni."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "márványasztal", "mellett", "születtek", "a", "modern", "magyar", "irodalom", "remekművei."],
                    "solution": ["A", "márványasztal", "mellett", "születtek", "a", "modern", "magyar", "irodalom", "remekművei."],
                    "english": "The masterpieces of modern Hungarian literature were born beside the marble table.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Contrast 19th-century private salons with Budapest's coffeehouses using 'viszont'.",
                            "answer": "A zárt szalonok csak a kiváltságosokat fogadták be, a pesti kávéházak viszont minden tehetséges író előtt nyitva álltak."
                        },
                        {
                            "prompt": "Introduce a comment about regular patrons using 'Ami a törzsvendégeket illeti, ...'.",
                            "answer": "Ami a törzsvendégeket illeti, ők gyakran reggeltől késő éjszakáig ugyanannál a márványasztalnál dolgoztak."
                        }
                    ],
                    "teaches": ["b2-contrastive-topic"]
                }
            ]
        },
        {
            "num": 2,
            "title": "The Birth of Nyugat (1908)",
            "grammar_label": "Correlative contrast with míg ... addig and ezzel szemben",
            "goals": [
                "I can explain the historical significance of the founding of Nyugat in January 1908.",
                "I can build balanced two-clause contrasts using míg ... addig and ezzel szemben.",
                "I can discuss literary journals, aesthetic orientation, and European modernism in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "nyugatszuletese",
                "title": "A Nyugat születése (1908)",
                "summary": "Launched in January 1908 by Ignotus, Ernő Osvát, and Miksa Fenyő, the journal Nyugat looked toward Paris and Western European aesthetic freedom while renewing Hungarian poetic language.",
                "location": "Budapest, Centrál kávéház",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1908. január elsején új folyóirat jelent meg a budapesti könyvkereskedések kirakatában és a kávéházak olvasóállványain: a Nyugat. A cím maga is bátor szellemi kiállás volt. Míg a hivatalos akadémiai kritika a népies-nemzeti hagyomány változatlan ismétlését várta el az íróktól, addig az új lap alapítói — Ignotus, Osvát Ernő és Fenyő Miksa — a nyugat-európai modernség szabadságát kívánták meghonosítani Magyarországon."
                    },
                    {
                        "type": "narration",
                        "text": "Az első számban jelent meg Ignotus híres programadó esszéje, a Kelet népe, amely Széchenyi István egykori vitairatának címét idézte meg. A konzervatív lapok azzal vádolták a Nyugat körét, hogy elszakadnak a hazai gyökerektől. Ignotus ezzel szemben amellett érvelt, hogy a magyar irodalom csak akkor válhat igazán szuverénné és egyetemessé, ha bátran párbeszédet folytat Párizs, Berlin és London szellemi áramlataival."
                    },
                    {
                        "type": "narration",
                        "text": "A folyóirat emblémájává később Beck Ö. Fülöp emlékérme vált, amely Kelemen kőműves lantot pengető alakját ábrázolta. Ez a jelkép pontosan sűrítette magába a szerkesztők hitvallását: az alkotás áldozattal jár, de a felépített mű szilárdabb minden politikai jelszónál. A Nyugat nem egyetlen stílusirányzatot képviselt, hanem a minőség és az alkotói autonómia szövetségét."
                    },
                    {
                        "type": "narration",
                        "text": "Míg a korabeli tömegsajtó a gyors szenzációt kereste, addig a Nyugat alig néhány száz, később néhány ezer előfizetővel is képes volt alapjaiban megváltoztatni a magyar közgondolkodást. Oldalain egyszerre kapott helyet Ady Endre prófétai szimbolizmusa, Babits Mihály filozófiai fegyelme, Kosztolányi Dezső nyelvi virtuozitása és Móricz Zsigmond kíméletlen társadalomrajza."
                    },
                    {
                        "type": "narration",
                        "text": "A Centrál és a New York kávéház asztalainál a kéziratokat nem a szerző társadalmi rangja, hanem kizárólag az esztétikai színvonal alapján ítélték meg. Így vált az 1908-as esztendő a modern magyar irodalom valódi fordulópontjává."
                    }
                ]
            },
            "words": [
                {"lemma": "folyóirat", "translation": "periodical / literary journal", "pos": "noun"},
                {"lemma": "hitvallás", "translation": "credo / artistic profession of faith", "pos": "noun"},
                {"lemma": "irányzat", "translation": "movement / artistic trend", "pos": "noun"},
                {"lemma": "előfizető", "translation": "subscriber", "pos": "noun"},
                {"lemma": "ezzel szemben", "translation": "in contrast to this / by contrast", "pos": "expression"},
                {"lemma": "meghonosít", "translation": "to naturalize / establish at home", "pos": "verb"}
            ],
            "grammar_doc": {
                "slug": "correlative-contrast-mig-addig",
                "title": "Balanced Discourse Contrast: míg ... addig and ezzel szemben",
                "text1_title": "Parallel Antithesis with míg ... addig",
                "text1": "When Hungarian writers contrast two simultaneous historical realities or opposing ideological stances within a single complex sentence, they pair míg ('while / whereas') in the first clause with addig ('by contrast / meanwhile') at the head of the second clause. Unlike English, where 'while' suffices alone, Hungarian B2 prose strongly favors explicit correlative balancing with addig.",
                "text2_title": "Inter-sentential Pivot with ezzel szemben",
                "text2": "Across sentence boundaries, ezzel szemben ('in contrast to this / opposed to this') links a new sentence back to the entire proposition of the preceding sentence. It typically stands either sentence-initially or immediately after the new contrastive topic (e.g., Ignotus ezzel szemben amellett érvelt, hogy...).",
                "table_title": "Correlative and Discourse Contrast Connectors",
                "table_rows": [
                    ["Míg az akadémiai kritika a múltat védte, addig a Nyugat a jövőt kereste.", "Whereas academic criticism defended the past, Nyugat sought the future."],
                    ["Míg a napilapok tízezres példányszámban fogytak, addig a folyóirat szűkebb réteghez szólt.", "While dailies sold in tens of thousands, the journal addressed a narrower stratum."],
                    ["A konzervatívok bezárkózást sürgettek. A modernisták ezzel szemben nyitottságot hirdettek.", "Conservatives urged isolation. Modernists, by contrast, proclaimed openness."]
                ],
                "examples": [
                    {
                        "spanish": "Míg a hivatalos kritika a hagyomány ismétlését várta el, addig a Nyugat az alkotói szabadságot hirdette.",
                        "english": "Whereas official criticism expected the repetition of tradition, Nyugat proclaimed creative freedom."
                    },
                    {
                        "spanish": "A konzervatív lapok kozmopolitizmussal vádolták őket. Ignotus ezzel szemben a nemzeti irodalom megújításáról írt.",
                        "english": "Conservative papers accused them of cosmopolitanism. Ignotus, by contrast, wrote about renewing national literature."
                    }
                ],
                "tip": "Always place a comma before addig when it introduces the second clause of a míg ... addig correlative structure."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a 'meghonosít' ige a Nyugat irodalmi programjával kapcsolatban?",
                    "options": [
                        "Külföldi szellemi vagy művészeti értékeket bevezet és otthonossá tesz a hazai kultúrában.",
                        "Idegen nyelvű könyveket betilt a könyvtárakban.",
                        "Régi falusi házakat bont le a fővárosban."
                    ],
                    "correct": 0,
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A Nyugat című irodalmi _____ 1908 januárjában jelent meg először Budapesten. (literary journal)",
                    "answer": "folyóirat",
                    "english": "The literary journal titled Nyugat first appeared in Budapest in January 1908.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Míg a tömegsajtó a napi szenzációt kereste, _____ a Nyugat az esztétikai minőséget helyezte előtérbe. (by contrast / correlative)",
                    "answer": "addig",
                    "english": "Whereas the mass press sought daily sensation, Nyugat placed aesthetic quality in the foreground.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik kifejezés illik legjobban a két mondat közötti tartalmi ellentét kifejezésére? 'Az akadémikusok elutasították a szimbolizmust. Az új nemzedék _____ lelkesen fogadta Ady verseit.'",
                    "options": [
                        "ezzel szemben",
                        "ennek ellenére hogy",
                        "amiatt"
                    ],
                    "correct": 0,
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Míg", "a", "konzervatívok", "a", "múltat", "védték,", "addig", "Ignotus", "a", "nyitottság", "mellett", "érvelt."],
                    "solution": ["Míg", "a", "konzervatívok", "a", "múltat", "védték,", "addig", "Ignotus", "a", "nyitottság", "mellett", "érvelt."],
                    "english": "Whereas the conservatives defended the past, Ignotus argued in favor of openness.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen szempont alapján válogatták a kéziratokat a Nyugat szerkesztői?",
                    "options": [
                        "Kizárólag az esztétikai színvonal és az alkotói minőség alapján, nem pedig a szerző rangja szerint.",
                        "Csak olyan szerzőket közöltek, akiknek már volt akadémiai tagságuk.",
                        "Kizárólag francia nyelven írt verseket jelentettek meg."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "folyóirat", "kevés", "előfizető", "mellett", "is", "formálta", "a", "magyar", "közgondolkodást."],
                    "solution": ["A", "folyóirat", "kevés", "előfizető", "mellett", "is", "formálta", "a", "magyar", "közgondolkodást."],
                    "english": "Even with few subscribers, the journal shaped Hungarian public thought.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence contrasting the mass press and Nyugat using 'Míg ..., addig ...'.",
                            "answer": "Míg a korabeli napilapok a gyors szórakoztatásra törekedtek, addig a Nyugat maradandó irodalmi értékeket teremtett."
                        },
                        {
                            "prompt": "Write a follow-up sentence using 'ezzel szemben' to describe Ignotus's viewpoint.",
                            "answer": "Ignotus ezzel szemben bebizonyította, hogy a nyugati hatások nem gyengítik, hanem gazdagítják a magyar kultúrát."
                        }
                    ],
                    "teaches": ["b2-contrastive-topic"]
                }
            ]
        },
        {
            "num": 3,
            "title": "Osvát Ernő, the Invisible Editor",
            "grammar_label": "Exhaustive focus and preverb-verb inversion in biographical narrative",
            "goals": [
                "I can explain Ernő Osvát's legendary editorial ethic and why he published almost nothing of his own.",
                "I can invert preverbs (meg-, el-, fel-, ki-) when placing a constituent into exhaustive focus.",
                "I can use precise editorial and literary-criticism vocabulary."
            ],
            "story_segment": {
                "seg_slug": "osvaterno",
                "title": "Osvát Ernő, a láthatatlan szerkesztő",
                "summary": "Ernő Osvát wrote almost no books of his own, conducting his entire editorial work from a marble coffeehouse table and discovering talents like Móricz and Babits.",
                "location": "Budapest, New York és Centrál kávéház",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Ha a Nyugat első évtizedeinek szellemi motorját keressük, nem a leghangosabb szónokok között találjuk meg, hanem egy szikár, szigorú tekintetű férfi alakjában, aki egész életében alig néhány oldalnyi saját aforizmát adott közre. Osvát Ernő volt az, aki a kávéház márványasztalát valódi szerkesztőségi íróasztallá avatta. Nem saját műveket akart hátrahagyni, hanem mások tehetségét bontakoztatta ki."
                    },
                    {
                        "type": "narration",
                        "text": "Éppen Osvát fedezte fel Móricz Zsigmondot is, amikor 1908 őszén elolvasta a Hét krajcár című novella kéziratát. Míg más szerkesztők talán átsiklottak volna az ismeretlen író szövege felett, addig Osvát azonnal felismerte benne az őseredeti drámai erőt. A novellát a Nyugat következő számában közölte, és Móricz egyetlen éjszaka alatt az ország egyik legismertebb prózaírójává vált."
                    },
                    {
                        "type": "narration",
                        "text": "Osvát megvesztegethetetlen kritikai mércéje legendás volt a pesti irodalmi életben. Még a legközelebbi barátainak sem engedte meg, hogy félkész vagy gyenge sort adjanak ki a kezükből; csak a tökéletesre csiszolt kéziratot fogadta el. Ha egy versben egyetlen hamis jelzőt talált, órákon át vitatkozott a szerzővel a kávéházi füstben, amíg meg nem született a pontos kifejezés."
                    },
                    {
                        "type": "narration",
                        "text": "Sajátos életmódjához hozzátartozott, hogy szinte sohasem írt hivatalos levelet: a kéziratokat személyesen a kávéházban vette át, és ott is bírálta el őket. Ami az anyagi javakat illeti, Osvát teljes önzetlenséggel élt, és gyakran a saját szerény jövedelméből segítette ki a nyomorgó fiatal költőket."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor az írók arról vitatkoztak, ki teremtette meg a modern magyar irodalom erkölcsi rangját, mindannyian tudták a választ: Osvát Ernő szigora emelte a Nyugatot európai magaslatra."
                    }
                ]
            },
            "words": [
                {"lemma": "kézirat", "translation": "manuscript", "pos": "noun"},
                {"lemma": "mérce", "translation": "standard / benchmark / yardstick", "pos": "noun"},
                {"lemma": "megvesztegethetetlen", "translation": "incorruptible", "pos": "adjective"},
                {"lemma": "önzetlenség", "translation": "selflessness / altruism", "pos": "noun"},
                {"lemma": "felfedez", "translation": "to discover", "pos": "verb"},
                {"lemma": "elbírál", "translation": "to evaluate / judge (a submission)", "pos": "verb"}
            ],
            "grammar_doc": {
                "slug": "focus-preverb-inversion-osvat",
                "title": "Exhaustive Focus and Preverb Inversion in Biographical Prose",
                "text1_title": "Neutral Preverb Order vs. Focused Identification",
                "text1": "In neutral Hungarian sentences, a separable verbal prefix (igekötő such as meg-, fel-, el-, ki-, át-) stands immediately before the verb stem as a single word: Osvát felfedezte Móricz Zsigmondot ('Osvát discovered Zsigmond Móricz'). However, when another phrase is placed in the immediately pre-verbal Focus slot to express exhaustive identification ('It was X—and no one else—who...'), the preverb detaches and moves AFTER the conjugated verb: Éppen Osvát fedezte fel Móricz Zsigmondot.",
                "text2_title": "Focus Triggers with csak, éppen, nem, and Interrogatives",
                "text2": "Particles such as csak ('only'), éppen ('precisely / it was none other than'), negation (nem), and question words (ki, mi, mikor) automatically occupy the pre-verbal focus slot and force preverb inversion: Csak a tökéletes kéziratot fogadta el (from elfogadta).",
                "table_title": "Neutral vs. Focused Word Order with Preverbs",
                "table_rows": [
                    ["Osvát felfedezte Móricz tehetségét. (Neutral)", "Éppen Osvát fedezte fel Móricz tehetségét. (Focused subject)"],
                    ["A szerkesztő elfogadta a kéziratot. (Neutral)", "Csak a tökéletes kéziratot fogadta el. (Focused object)"],
                    ["A kávéházban átvette a verseket. (Neutral)", "A kávéházban vette át a verseket. (Focused location)"],
                    ["Mások tehetségét kibontakoztatta. (Neutral)", "Mások tehetségét bontakoztatta ki. (Contrastive focus)"]
                ],
                "examples": [
                    {
                        "spanish": "Éppen Osvát fedezte fel Móricz Zsigmondot, amikor elolvasta a Hét krajcár kéziratát.",
                        "english": "It was precisely Osvát who discovered Zsigmond Móricz when he read the manuscript of Seven Pennies."
                    },
                    {
                        "spanish": "A szigorú szerkesztő csak a tökéletesre csiszolt kéziratot fogadta el.",
                        "english": "The strict editor accepted only the manuscript polished to perfection."
                    },
                    {
                        "spanish": "A beküldött verseket személyesen a kávéházban bírálta el.",
                        "english": "It was in the coffeehouse in person that he evaluated the submitted poems."
                    }
                ],
                "tip": "Whenever you place csak + Noun Phrase immediately before a prefixed verb, split the prefix and put it right after the conjugated verb: csak a minőséget ismerte el (never *csak a minőséget elismerte)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az, hogy Osvát Ernő kritikai 'mércéje' megvesztegethetetlen volt?",
                    "options": [
                        "Szigorú minőségi követelményeiből még a barátai kedvéért sem engedett.",
                        "Csak azoknak a művét közölte, akik kifizették a nyomdaköltséget.",
                        "Sohasem olvasott el egyetlen beküldött kéziratot sem."
                    ],
                    "correct": 0,
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Móricz Zsigmond a Hét krajcár című novella _____ révén vált híressé, amelyet Osvát olvasott el először. (manuscript - kézirata)",
                    "answer": "kézirata",
                    "english": "Zsigmond Móricz became famous through the manuscript of the short story Seven Pennies, which Osvát read first.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A legendás szerkesztő csak a hibátlanul megírt szövegeket _____ el közlésre. (accepted - fogadta)",
                    "answer": "fogadta",
                    "english": "The legendary editor accepted only impeccably written texts for publication.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Válaszd ki a helyes szórendű mondatot, ha a 'kávéházban' határozószón van a kizárólagos fókusz!",
                    "options": [
                        "Osvát Ernő személyesen a kávéházban bírálta el a beküldött kéziratokat.",
                        "Osvát Ernő személyesen a kávéházban elbírálta a beküldött kéziratokat.",
                        "Osvát Ernő elbírálta személyesen a kávéházban a beküldött kéziratokat."
                    ],
                    "correct": 0,
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Éppen", "Osvát", "Ernő", "fedezte", "fel", "Móricz", "Zsigmond", "őseredeti", "tehetségét."],
                    "solution": ["Éppen", "Osvát", "Ernő", "fedezte", "fel", "Móricz", "Zsigmond", "őseredeti", "tehetségét."],
                    "english": "It was precisely Ernő Osvát who discovered Zsigmond Móricz's primordial talent.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan viszonyult Osvát Ernő a saját írói életművéhez?",
                    "options": [
                        "Alig publikált saját művet, mert egész életét mások tehetségének kibontakoztatására szentelte.",
                        "Több mint harminc regényt írt, amelyeket minden számban folytatásokban közölt.",
                        "Csak francia nyelvű drámákat írt a Nemzeti Színház számára."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "megvesztegethetetlen", "szerkesztő", "sohasem", "engedett", "a", "szigorú", "esztétikai", "mércéből."],
                    "solution": ["A", "megvesztegethetetlen", "szerkesztő", "sohasem", "engedett", "a", "szigorú", "esztétikai", "mércéből."],
                    "english": "The incorruptible editor never compromised on the strict aesthetic standard.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a focused sentence using 'Csak ... fogadta el' about Osvát's editorial standard.",
                            "answer": "Osvát Ernő csak a legmagasabb színvonalú kéziratokat fogadta el a Nyugat számára."
                        },
                        {
                            "prompt": "Write a sentence with preverb inversion ('fedezte fel') emphasizing who discovered Móricz.",
                            "answer": "A fiatal prózaíró tehetségét éppen a Nyugat szerkesztője fedezte fel 1908 őszén."
                        }
                    ],
                    "teaches": ["b2-contrastive-topic"]
                }
            ]
        },
        {
            "num": 4,
            "title": "Modernists vs. Conservatives in Public Debate",
            "grammar_label": "Polemical contrast with egyrészt ... másrészt and korántsem ... hanem",
            "goals": [
                "I can analyze the polemical debates around Endre Ady's Új versek and the Nyugat generation.",
                "I can structure multi-pronged arguments with egyrészt ... másrészt and refute claims with korántsem ... hanem.",
                "I can use polemical and literary-debate vocabulary at B2 level."
            ],
            "story_segment": {
                "seg_slug": "modernistakvita",
                "title": "Modernisták és konzervatívok nyilvános vitája",
                "summary": "Fierce public polemics erupted between Prime Minister István Tisza's conservative camp and the modernists around Endre Ady and Nyugat over what it meant to be Hungarian and modern.",
                "location": "Budapest, sajtóviták és kávéházi asztaltársaságok",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Amikor Ady Endre 1906-ban megjelentette az Új versek című kötetét, majd a Nyugat élére állt, a magyar szellemi élet két kibékíthetetlen táborra szakadt. A vita korántsem pusztán verstani kérdésekről szólt, hanem arról, hogy merre tartson a huszadik századi Magyarország. Egyrészt a hagyományőrző akadémikusok és Rákosi Jenő köre a nemzeti múlt megszentelt formáit féltette, másrészt a Nyugat írói a társadalmi önvizsgálatot és az európai horizontot követelték."
                    },
                    {
                        "type": "narration",
                        "text": "Az ellenfelek gyakran azzal támadták Ady költészetét, hogy szokatlan képei érthetetlenek, sőt idegenek a magyar nyelv szellemétől. A modernisták ezzel szemben kimutatták, hogy Ady nyelve egyrészt a kuruc kori énekek és a Károli-biblia zsoltáros erejéből táplálkozik, másrészt a modern nagyvárosi ember szorongásait fejezi ki."
                    },
                    {
                        "type": "narration",
                        "text": "A sajtópárbajokba még a kor vezető politikusai is bekapcsolódtak: Tisza István és köre a Kelet népe valamint a Magyar Figyelő hasábjain próbált szellemi ellensúlyt teremteni a Nyugattal szemben. Ezek a viták azonban nem elhallgattatták az új irodalmat, hanem éppen ellenkezőleg: minden eddiginél szélesebb olvasóközönség figyelmét irányították rá a modern költészetre."
                    },
                    {
                        "type": "narration",
                        "text": "A kávéházakban az ellentétes táborok képviselői sokszor egymástól alig néhány asztalnyira ültek. Míg a konzervatív kritikusok a reggeli vezércikkekben élesen bírálták a Nyugat legújabb számát, addig este a Centrálban személyesen vitatták meg érveiket a modernistákkal."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a nyilvános vitakultúra megtanította a magyar értelmiséget arra, hogy a hazaszeretet nem a hibák elhallgatását jelenti, hanem a bátor szellemi szembenézést."
                    }
                ]
            },
            "words": [
                {"lemma": "vitairat", "translation": "polemical essay / pamphlet", "pos": "noun"},
                {"lemma": "hagyományőrző", "translation": "traditionalist / conservative", "pos": "adjective"},
                {"lemma": "önvizsgálat", "translation": "self-examination / introspection", "pos": "noun"},
                {"lemma": "ellensúly", "translation": "counterweight / counterbalance", "pos": "noun"},
                {"lemma": "korántsem", "translation": "by no means / far from", "pos": "adverb"},
                {"lemma": "egyrészt ... másrészt", "translation": "on the one hand ... on the other hand", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "polemical-contrast-korantsem",
                "title": "Polemical Argumentation: korántsem ... hanem and egyrészt ... másrészt",
                "text1_title": "Emphatic Refutation with korántsem ... hanem",
                "text1": "In B2 critical essays and historical analysis, simple nem ('not') is often replaced by korántsem ('by no means / far from') paired with hanem ('but rather') to refute a superficial interpretation before presenting the deeper truth: A vita korántsem pusztán verstani kérdésekről szólt, hanem az ország jövőjéről ('The debate was by no means merely about prosody, but rather about the country's future').",
                "text2_title": "Dual Facets with egyrészt ... másrészt",
                "text2": "To show that a phenomenon combines two seemingly opposing qualities—or to present two sides of a debate—Hungarian pairs egyrészt ('on the one hand / partly') with másrészt ('on the other hand / partly'). For instance, Ady's language drew egyrészt on 16th-century Protestant biblical Hungarian, and másrészt on Parisian symbolism.",
                "table_title": "Polemical & Analytical Structures",
                "table_rows": [
                    ["korántsem pusztán X, hanem Y", "by no means merely X, but rather Y"],
                    ["nem elhallgattatta, hanem éppen ellenkezőleg: ...", "it did not silence it, but quite the contrary: ..."],
                    ["egyrészt a bibliai hagyományból, másrészt a modernségből", "on the one hand from biblical tradition, on the other from modernity"]
                ],
                "examples": [
                    {
                        "spanish": "A vita korántsem pusztán verstani kérdésekről szólt, hanem a huszadik századi Magyarország jövőjéről.",
                        "english": "The debate was by no means merely about questions of versification, but rather about the future of twentieth-century Hungary."
                    },
                    {
                        "spanish": "Ady költészete egyrészt a kuruc énekekből táplálkozott, másrészt a modern nagyvárosi ember szorongásait fejezte ki.",
                        "english": "Ady's poetry drew on the one hand from Kuruc songs, and on the other hand expressed the anxieties of modern urban man."
                    }
                ],
                "tip": "Note that korántsem already contains negation (-sem), so never add a second nem before the verb (*korántsem nem szólt -> korántsem szólt)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a 'korántsem' határozószó a vitázó esszényelvben?",
                    "options": [
                        "Egyáltalán nem, a legkevésbé sem.",
                        "Kora reggel, hajnalban.",
                        "Minden kétséget kizáróan, biztosan."
                    ],
                    "correct": 0,
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A Nyugat írói a nemzeti önelégültség helyett bátor társadalmi _____ sürgettek. (self-examination - önvizsgálatot)",
                    "answer": "önvizsgálatot",
                    "english": "Instead of national complacency, the writers of Nyugat urged courageous social self-examination.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az irodalmi vita _____ pusztán a rímekről szólt, hanem a társadalom megújításáról is. (by no means - korántsem)",
                    "answer": "korántsem",
                    "english": "The literary debate was by no means merely about rhymes, but also about the renewal of society.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat használja helyesen az 'egyrészt ... másrészt' szerkezetet?",
                    "options": [
                        "Ady nyelve egyrészt a Károli-biblia hagyományából táplálkozott, másrészt a francia szimbolizmus hatását mutatta.",
                        "Ady nyelve egyrészt a Károli-biblia hagyományából táplálkozott, sem a francia szimbolizmus hatását mutatta.",
                        "Egyrészt Ady nyelve nem táplálkozott, hanem másrészt korántsem."
                    ],
                    "correct": 0,
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "vita", "korántsem", "gyengítette", "a", "lapot,", "hanem", "új", "olvasókat", "vonzott."],
                    "solution": ["A", "vita", "korántsem", "gyengítette", "a", "lapot,", "hanem", "új", "olvasókat", "vonzott."],
                    "english": "The debate by no means weakened the journal, but rather attracted new readers.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mivel érveltek a modernisták, amikor Ady Endre nyelvezetét idegenséggel vádolták?",
                    "options": [
                        "Kimutatták, hogy Ady költészete mélyen gyökerezik a kuruc kori énekekben és a protestáns bibliafordítás nyelvében.",
                        "Elismerve a vádat kijelentették, hogy a magyar nyelvet le kell cserélni latinra.",
                        "Tagadták, hogy Ady Endre valaha is írt volna verseket a Nyugatba."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "hagyományőrző", "kritikusok", "szellemi", "ellensúlyt", "próbáltak", "teremteni", "a", "folyóirattal", "szemben."],
                    "solution": ["A", "hagyományőrző", "kritikusok", "szellemi", "ellensúlyt", "próbáltak", "teremteni", "a", "folyóirattal", "szemben."],
                    "english": "Traditionalist critics tried to create an intellectual counterweight against the journal.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Refute a claim about the 1908 debates using 'korántsem ... hanem'.",
                            "answer": "A Nyugat körüli sajtóvita korántsem gyengítette a modern irodalmat, hanem az egész ország figyelmét ráirányította."
                        },
                        {
                            "prompt": "Describe two aspects of Ady's poetry using 'egyrészt ... másrészt'.",
                            "answer": "Költészete egyrészt őrizte a régi magyar zsoltárok erejét, másrészt bátran kimondta a modern ember kételyeit."
                        }
                    ],
                    "teaches": ["b2-contrastive-topic"]
                }
            ]
        },
        {
            "num": 5,
            "title": "Legacy of the Literary Coffeehouse",
            "grammar_label": "Synthesizing contrastive discourse and focus across historical eras",
            "goals": [
                "I can trace the fate of Budapest's coffeehouse culture through the 20th century and its revival after 1989.",
                "I can combine contrastive topicalization and focus-preverb inversion in extended historical summaries.",
                "I can discuss cultural continuity, public spheres, and literary heritage."
            ],
            "story_segment": {
                "seg_slug": "kavehaziorokseg",
                "title": "Az irodalmi kávéház öröksége",
                "summary": "From Karinthy's Hadik circle in Buda to the closures after 1948 and the revival of Budapest's historic cafés after 1989, the coffeehouse remains an enduring symbol of Hungarian intellectual freedom.",
                "location": "Budapest, Bartók Béla út (Hadik kávéház)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A két világháború között az irodalmi élet súlypontja fokozatosan átterjedt Budára is: a Bartók Béla úti Hadik kávéházban Karinthy Frigyes, Kosztolányi Dezső és Déry Tibor asztaltársasága teremtett új, szellemes legendákat. Míg a pesti New York a századelő pompáját idézte, addig a budai Hadik családiasabb, ironikusabb hangulatával vonzotta a művészeket."
                    },
                    {
                        "type": "narration",
                        "text": "A Nyugat 1941-ben, Babits Mihály halálával megszűnt, mert a háborús cenzúra nem engedte meg a lap fennmaradását az eredeti nevén. Illyés Gyula ugyan Magyar Csillag címen továbbvitte a folyóirat szellemiségét 1944-ig, a második világháború pusztítása és az 1948 utáni államosítások azonban véget vetettek a klasszikus kávéházi köztársaságnak."
                    },
                    {
                        "type": "narration",
                        "text": "Ami az ötvenes éveket illeti, a hatalom gyanakvással figyelte a szabad és ellenőrizhetetlen kávéházi beszélgetéseket. A patinás csarnokok többségét bezárták, raktárrá vagy gyorsbüfévé alakították át; csak néhány presszó, például a Hungária vagy a Lukács őrizte meg a szellemi találkozóhelyek emlékét."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1989-es rendszerváltás után viszont megkezdődött a történelmi kávéházak újjászületése. A Centrál, a New York és a Hadik ismét megnyitotta kapuit, és a márványasztalok mellett ma újra irodalmi esteket, könyvbemutatókat és nyilvános vitákat rendeznek."
                    },
                    {
                        "type": "narration",
                        "text": "A pesti kávéház története így korántsem pusztán nosztalgikus emlék, hanem élő bizonyíték arra, hogy a magyar kultúra legjava mindig a szabad párbeszédben és a nyitott városi terekben született meg."
                    }
                ]
            },
            "words": [
                {"lemma": "asztaltársaság", "translation": "regular table circle / literary coterie", "pos": "noun"},
                {"lemma": "szellemiség", "translation": "ethos / intellectual spirit", "pos": "noun"},
                {"lemma": "cenzúra", "translation": "censorship", "pos": "noun"},
                {"lemma": "államosítás", "translation": "nationalization", "pos": "noun"},
                {"lemma": "újjászületés", "translation": "rebirth / revival", "pos": "noun"},
                {"lemma": "továbbvisz", "translation": "to carry on / continue (a legacy)", "pos": "verb"}
            ],
            "grammar_doc": {
                "slug": "contrastive-synthesis-legacy",
                "title": "Synthesizing Contrast and Focus Across Historical Eras",
                "text1_title": "Weaving Temporal and Spatial Shifts",
                "text1": "When summarizing a century-long cultural trajectory, B2 Hungarian prose alternates between spatial contrasts (Míg a pesti New York ..., addig a budai Hadik ...) and chronological topic shifts (Ami az ötvenes éveket illeti, ...; Az 1989-es rendszerváltás után viszont ...). This keeps the logical thread crystal-clear without repetitive conjunctions.",
                "text2_title": "Combining Focus Inversion with Contrastive Conjunctions",
                "text2": "Within contrasted clauses, preverb inversion pinpoints the exact historical survival or exception: A csarnokok többségét bezárták; csak néhány presszó őrizte meg a hagyományt ('Most halls were shut down; only a few espresso bars preserved the tradition', from megőrizte).",
                "table_title": "Integrated Historical Discourse Markers",
                "table_rows": [
                    ["Míg a pesti New York ..., addig a budai Hadik ...", "Whereas Pest's New York ..., Buda's Hadik ..."],
                    ["Ami az ötvenes éveket illeti, ...", "As far as the 1950s were concerned, ..."],
                    ["Csak néhány presszó őrizte meg az emléket.", "Only a few espresso bars preserved the memory."],
                    ["Az örökség korántsem pusztán emlék, hanem élő példa.", "The legacy is by no means merely a memory, but a living example."]
                ],
                "examples": [
                    {
                        "spanish": "Míg a pesti New York a századelő pompáját idézte, addig a budai Hadik családiasabb hangulatával vonzotta a művészeket.",
                        "english": "Whereas Pest's New York evoked turn-of-the-century splendor, Buda's Hadik attracted artists with its more intimate atmosphere."
                    },
                    {
                        "spanish": "A kávéházak többségét bezárták; csak néhány presszó őrizte meg a szellemi találkozóhelyek emlékét.",
                        "english": "Most of the coffeehouses were closed; only a few espresso bars preserved the memory of intellectual meeting places."
                    }
                ],
                "tip": "Notice how továbbvisz ('carry on') and megőriz ('preserve') split when a focused noun phrase precedes them: Illyés Gyula Magyar Csillag címen vitte tovább a lap szellemiségét."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az 'asztaltársaság' fogalma a magyar kávéházi kultúrában?",
                    "options": [
                        "Ugyanahhoz a kávéházi asztalhoz rendszeresen visszajáró írók, művészek és gondolkodók baráti-szellemi köre.",
                        "Egy bútoripari vállalat, amely márványasztalokat gyártott.",
                        "A pincérek szakszervezeti bizottsága."
                    ],
                    "correct": 0,
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Babits Mihály halála után Illyés Gyula Magyar Csillag címen vitte tovább a Nyugat _____. (intellectual spirit / ethos - szellemiségét)",
                    "answer": "szellemiségét",
                    "english": "After Mihály Babits's death, Gyula Illyés carried on the ethos of Nyugat under the title Magyar Csillag.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az államosítás után csak néhány belvárosi presszó _____ meg a szabad beszélgetések hagyományát. (preserved - őrizte)",
                    "answer": "őrizte",
                    "english": "After nationalization, only a few downtown espresso bars preserved the tradition of free conversation.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat kapcsolja össze helyesen a két korszak közötti ellentétet?",
                    "options": [
                        "Ami az ötvenes éveket illeti, a kávéházak többségét bezárták; a rendszerváltás után viszont megkezdődött az újjászületésük.",
                        "Ami az ötvenes évek illeti, a kávéházak többségét bezárták; viszont a rendszerváltás után megkezdődött.",
                        "Míg az ötvenes éveket illeti, korántsem a rendszerváltás után újjászületett."
                    ],
                    "correct": 0,
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Illyés", "Gyula", "Magyar", "Csillag", "címen", "vitte", "tovább", "a", "Nyugat", "szellemiségét."],
                    "solution": ["Illyés", "Gyula", "Magyar", "Csillag", "címen", "vitte", "tovább", "a", "Nyugat", "szellemiségét."],
                    "english": "It was under the title Magyar Csillag that Gyula Illyés carried on the ethos of Nyugat.",
                    "teaches": ["b2-contrastive-topic"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért szűnt meg a Nyugat 1941-ben?",
                    "options": [
                        "Mert Babits Mihály elhunyt, és a háborús cenzúra nem engedélyezte a lap továbbélését az eredeti Nyugat néven.",
                        "Mert az összes pesti kávéház leégett egyetlen éjszaka alatt.",
                        "Mert a szerkesztők úgy döntöttek, hogy inkább napilapot indítanak Párizsban."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "budai", "Hadik", "kávéházban", "Karinthy", "Frigyes", "legendás", "asztaltársasága", "gyűlt", "össze."],
                    "solution": ["A", "budai", "Hadik", "kávéházban", "Karinthy", "Frigyes", "legendás", "asztaltársasága", "gyűlt", "össze."],
                    "english": "Frigyes Karinthy's legendary table circle gathered in the Hadik Coffeehouse in Buda.",
                    "teaches": ["b2-kavehazikultura-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Contrast the fate of coffeehouses in the 1950s and after 1989 using 'Ami az ötvenes éveket illeti' and 'viszont'.",
                            "answer": "Ami az ötvenes éveket illeti, a hatalom bezáratta a nagy kávéházakat, 1989 után viszont a történelmi csarnokok újjászülettek."
                        },
                        {
                            "prompt": "Summarize the significance of coffeehouse culture using 'korántsem pusztán ... hanem'.",
                            "answer": "A kávéházi örökség korántsem pusztán nosztalgikus emlék, hanem a szabad szellemi párbeszéd élő jelképe."
                        }
                    ],
                    "teaches": ["b2-contrastive-topic"]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can discuss the history of Budapest's literary coffeehouses and the review Nyugat (1908–1941) with B2 lexical precision.",
            "I can deploy contrastive topic frames (ami X-et illeti, ezzel szemben, míg ... addig, korántsem ... hanem) fluently.",
            "I can apply preverb-verb inversion accurately whenever a constituent occupies the pre-verbal focus slot."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik fogalom jelöli azt a keskeny papírszeletet, amelyre a pesti írók a kávéházban dolgoztak?",
                "options": ["kutyanyelv", "kefelenyomat", "előfizető", "vitairat"],
                "correct": 0,
                "teaches": ["b2-kavehazikultura-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban áll a 'ami ... illeti' szerkezet nyelvtanilag hibátlan alakban?",
                "options": [
                    "Ami a Nyugat szerkesztőit illeti, ők a minőséget minden más elé helyezték.",
                    "Ami a Nyugat szerkesztői illeti, ők a minőséget minden más elé helyezték.",
                    "Ami a Nyugat szerkesztőknél illeti, ők a minőséget minden más elé helyezték."
                ],
                "correct": 0,
                "teaches": ["b2-contrastive-topic"]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki volt a Nyugat legendás, saját könyvet szinte soha nem publikáló, megvesztegethetetlen szerkesztője?",
                "options": ["Osvát Ernő", "Rákosi Jenő", "Tisza István", "Károli Gáspár"],
                "correct": 0,
                "teaches": ["b2-kavehazikultura-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kávéházban minden nap ugyanannál az asztalnál ülő írók szoros _____ alkottak. (table circle - asztaltársaságot)",
                "answer": "asztaltársaságot",
                "english": "The writers sitting at the same table every day in the coffeehouse formed a close-knit table circle.",
                "teaches": ["b2-kavehazikultura-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Míg az akadémiai kritika a múltba révedt, _____ a Nyugat bátran nyitott Európa felé. (meanwhile / correlative - addig)",
                "answer": "addig",
                "english": "Whereas academic criticism gazed into the past, Nyugat boldly opened toward Europe.",
                "teaches": ["b2-contrastive-topic"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szigorú szerkesztő csak a hibátlan kéziratot _____ el a folyóirat számára. (accepted - fogadta)",
                "answer": "fogadta",
                "english": "The strict editor accepted only the flawless manuscript for the journal.",
                "teaches": ["b2-contrastive-topic"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "vita", "korántsem", "pusztán", "a", "versformákról", "szólt,", "hanem", "az", "ország", "jövőjéről."],
                "solution": ["A", "vita", "korántsem", "pusztán", "a", "versformákról", "szólt,", "hanem", "az", "ország", "jövőjéről."],
                "english": "The debate was by no means merely about verse forms, but rather about the future of the country.",
                "teaches": ["b2-contrastive-topic"]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "főpincér", "hitelbe", "adott", "feketekávét", "és", "tintát", "a", "szegény", "törzsvendégeknek."],
                "solution": ["A", "főpincér", "hitelbe", "adott", "feketekávét", "és", "tintát", "a", "szegény", "törzsvendégeknek."],
                "english": "The headwaiter gave black coffee and ink on credit to the poor regular patrons.",
                "teaches": ["b2-kavehazikultura-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban van helyes igekötő-hátravetés fókusz miatt?",
                "options": [
                    "Éppen a kávéházakban született meg a modern magyar újságírás.",
                    "Éppen a kávéházakban megszületett a modern magyar újságírás.",
                    "Megszületett éppen a kávéházakban a modern magyar újságírás."
                ],
                "correct": 0,
                "teaches": ["b2-contrastive-topic"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "zárt", "szalonok", "keveseket", "fogadtak,", "a", "kávéház", "viszont", "mindenki", "előtt", "nyitva", "állt."],
                "solution": ["A", "zárt", "szalonok", "keveseket", "fogadtak,", "a", "kávéház", "viszont", "mindenki", "előtt", "nyitva", "állt."],
                "english": "Closed salons welcomed few, whereas the coffeehouse stood open to everyone.",
                "teaches": ["b2-contrastive-topic"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Write a two-part contrast between conservative critics and Nyugat editors using 'Míg ..., addig ...'.",
                        "answer": "Míg a konzervatív kritikusok a népies formák ismétlését követelték, addig a Nyugat szerkesztői az alkotói szabadságot támogatták."
                    }
                ],
                "teaches": ["b2-contrastive-topic"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Describe Ernő Osvát's role using focused preverb inversion ('fedezte fel' or 'bírálta el').",
                        "answer": "Éppen Osvát Ernő fedezte fel a huszadik századi magyar próza legnagyobb tehetségeit a kávéházi márványasztalnál."
                    }
                ],
                "teaches": ["b2-contrastive-topic"]
            }
        ]
    }
}


# ============================================================================
# CULTURE UNIT 2: b2-szecesszio
# ============================================================================
UNIT_2_SZECESSZIO = {
    "unit_num": 2,
    "slug": "szecesszio",
    "title": "Fin-de-Siècle Budapest & Hungarian Secession",
    "grammar_skill": "b2-participial-clauses",
    "vocab_skill": "b2-szecesszio-vocab",
    "theme": "Fin-de-siècle architecture and Hungarian Secession",
    "location": "Budapest (Iparművészeti Múzeum, Postatakarékpénztár, Andrássy út)",
    "combined_story_title": "Zsolnay-máz és vasbeton: Egy világváros születése",
    "combined_story_summary": "How Budapest grew into a European metropolis between 1873 and 1914, and how Ödön Lechner and Zsolnay ceramics created a unique Hungarian Secessionist architectural language.",
    "intro_body": [
        "Between the unification of Buda, Pest, and Óbuda in 1873 and the outbreak of the First World War in 1914, Budapest was the fastest-growing metropolis in Europe. Alongside historicist avenues like Andrássy út and continental Europe's first underground railway, Hungarian architects led by Ödön Lechner pioneered a dazzling national variant of Art Nouveau: the Hungarian Secession (magyar szecesszió).",
        "In this unit, you will learn how to read Budapest's architectural history while mastering extended pre-nominal participial modifiers (-ó/-ő active and -t/-tt passive/anterior participles) that pack rich visual and historical detail directly before the noun."
    ],
    "lessons": [
        {
            "num": 1,
            "title": "Uniting Buda, Pest, and Óbuda",
            "grammar_label": "Active pre-nominal participial clauses (-ó/-ő) with complements",
            "goals": [
                "I can explain the 1873 unification of Buda, Pest, and Óbuda and the work of the Board of Public Works.",
                "I can build extended left-branching active participial modifiers (-ó/-ő) before nouns.",
                "I can use urban-planning and architectural vocabulary in B2 descriptions."
            ],
            "story_segment": {
                "seg_slug": "egyesites",
                "title": "Buda, Pest és Óbuda egyesítése",
                "summary": "In November 1873, Buda, Pest, and Óbuda united into a single capital, launching decades of rapid urban planning guided by the Fővárosi Közmunkák Tanácsa.",
                "location": "Budapest, Andrássy út és Duna-korzó",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1873. november tizenhetedikén történelmi fordulat következett be a Duna két partján: a korábban külön közigazgatás alatt álló Buda, Pest és Óbuda egyesülésével megszületett Budapest, az ország modern fővárosa. A kiegyezést követő gazdasági fellendülés példátlan építkezési lázat indított el, amely néhány évtized alatt csendes tartományi városokból európai világvárost formált."
                    },
                    {
                        "type": "narration",
                        "text": "A látványos átalakulást a londoni mintára létrehozott Fővárosi Közmunkák Tanácsa irányította. Ez a testület nem csupán egyes telkekről döntött, hanem a teljes városszerkezetet átfogó szabályozási tervet dolgozott ki. A belvárost a Városligettel összekötő Andrássy út, valamint a félkörívben húzódó Nagykörút európai léptékű sugárutak és körutak hálózatát hozta létre."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1896-os millenniumi ünnepségekre elkészült az Andrássy út burkolata alatt futó földalatti vasút is, amely az európai kontinens legelső elektromos kéregvasútja volt. A sárga kocsikkal közlekedő járat egyszerre bizonyította a magyar mérnöki tudás élvonalbeli színvonalát és a főváros polgárságának modern életformáját."
                    },
                    {
                        "type": "narration",
                        "text": "Az első évtizedekben a középületeket még a historizmus szellemében emelték: az Ybl Miklós tervei alapján felépült Operaház a neoreneszánsz, a Steindl Imre által megálmodott Országház pedig a neogótika pompáját hirdette. A századforduló fiatal építészei azonban hamarosan feltették a kérdést: vajon létezik-e a múlt stílusait másoló irányzatok helyett sajátosan magyar, mégis modern építészeti nyelv?"
                    },
                    {
                        "type": "narration",
                        "text": "Ebből a keresésből született meg a magyar szecesszió, amely a keleti ornamentikát, a népművészeti motívumokat és a legmodernebb ipari anyagokat ötvözte."
                    }
                ]
            },
            "words": [
                {"lemma": "városrendezés", "translation": "urban planning / town development", "pos": "noun"},
                {"lemma": "sugárút", "translation": "avenue / radial boulevard", "pos": "noun"},
                {"lemma": "világváros", "translation": "metropolis / world city", "pos": "noun"},
                {"lemma": "középület", "translation": "public building", "pos": "noun"},
                {"lemma": "összekötő", "translation": "connecting / linking (participle)", "pos": "adjective"},
                {"lemma": "átfogó", "translation": "comprehensive / overarching", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "active-participial-clauses-o-o",
                "title": "Left-Branching Active Participial Clauses (-ó/-ő)",
                "text1_title": "Replacing Relative Clauses with Pre-Nominal Participles",
                "text1": "Where English places relative clauses AFTER a noun ('the avenue that connects the city center with the City Park'), Hungarian formal and architectural prose places the entire modifier phrase BEFORE the head noun using the active present participle (-ó/-ő): a belvárost a Városligettel összekötő Andrássy út.",
                "text2_title": "Internal Word Order of the Participial Phrase",
                "text2": "Inside the pre-nominal participial phrase, all objects, adverbs, and case-marked complements precede the -ó/-ő participle, and the participle itself stands immediately before the head noun it modifies: [Article of Head Noun] + [Complements/Objects] + [Participle in -ó/-ő] + [Head Noun].",
                "table_title": "Relative Clause vs. Pre-Nominal -ó/-ő Participial Clause",
                "table_rows": [
                    ["az út, amely összeköti a belvárost a Városligettel", "a belvárost a Városligettel összekötő út"],
                    ["a vasút, amely az Andrássy út alatt fut", "az Andrássy út alatt futó vasút"],
                    ["az irányzatok, amelyek a múlt stílusait másolják", "a múlt stílusait másoló irányzatok"]
                ],
                "examples": [
                    {
                        "spanish": "A belvárost a Városligettel összekötő Andrássy út európai léptékű sugárút lett.",
                        "english": "Andrássy Avenue, connecting the downtown with the City Park, became a boulevard on a European scale."
                    },
                    {
                        "spanish": "Az Andrássy út burkolata alatt futó földalatti vasút 1896-ra készült el.",
                        "english": "The underground railway running beneath the pavement of Andrássy Avenue was completed by 1896."
                    }
                ],
                "tip": "Notice the initial definite article belongs to the head noun at the end of the phrase: [A] [belvárost a Városligettel összekötő] [Andrássy út]."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Melyik fogalom jelenti egy város utcahálózatának, tereinek és középületeinek tervszerű kialakítását?",
                    "options": [
                        "városrendezés",
                        "kefelenyomat",
                        "cenzúra",
                        "előfizető"
                    ],
                    "correct": 0,
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Az Andrássy út Budapest legreprezentatívabb _____, amely a Városligetig vezet. (radial avenue - sugárútja)",
                    "answer": "sugárútja",
                    "english": "Andrássy Avenue is Budapest's most representative radial boulevard, leading to the City Park.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A belvárost a Városligettel _____ Andrássy út az 1870-es években épült ki. (connecting - összekötő)",
                    "answer": "összekötő",
                    "english": "Andrássy Avenue, connecting the downtown with the City Park, was built out in the 1870s.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Alakítsd át melléknévi igeneves szerkezetté: 'a földalatti vasút, amely a sugárút alatt fut'!",
                    "options": [
                        "a sugárút alatt futó földalatti vasút",
                        "a földalatti vasút futó a sugárút alatt",
                        "a futó sugárút alatt földalatti vasút"
                    ],
                    "correct": 0,
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "múlt", "stílusait", "másoló", "irányzatok", "helyett", "új", "nyelvet", "kerestek."],
                    "solution": ["A", "múlt", "stílusait", "másoló", "irányzatok", "helyett", "új", "nyelvet", "kerestek."],
                    "english": "Instead of trends copying the styles of the past, they sought a new language.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mi volt a Fővárosi Közmunkák Tanácsának legfőbb feladata 1873 után?",
                    "options": [
                        "A teljes városszerkezetet átfogó szabályozási terv kidolgozása, sugárutak és körutak kialakításával.",
                        "Irodalmi folyóiratok szerkesztése a kávéházakban.",
                        "A budai vár lebontása és gyárteleppé alakítása."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Három", "város", "egyesülésével", "modern", "európai", "világváros", "született", "a", "Duna", "partján."],
                    "solution": ["Három", "város", "egyesülésével", "modern", "európai", "világváros", "született", "a", "Duna", "partján."],
                    "english": "Through the unification of three cities, a modern European metropolis was born on the banks of the Danube.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Describe Andrássy út using an '-ó/-ő' pre-nominal participial phrase ('összekötő').",
                            "answer": "A belvárost a Városligettel összekötő Andrássy út a modern városrendezés jelképe lett."
                        },
                        {
                            "prompt": "Describe the Millennium Underground using an '-ó/-ő' participial phrase ('futó' or 'közlekedő').",
                            "answer": "Az út burkolata alatt közlekedő földalatti vasút 1896-ban nyílt meg."
                        }
                    ],
                    "teaches": ["b2-participial-clauses"]
                }
            ]
        },
        {
            "num": 2,
            "title": "Ödön Lechner and the Search for a National Style",
            "grammar_label": "Passive/anterior pre-nominal participial clauses (-t/-tt) with által",
            "goals": [
                "I can explain Ödön Lechner's architectural philosophy and his major Budapest masterpieces.",
                "I can construct passive/anterior pre-nominal participial modifiers (-t/-tt) with agent phrases (X által tervezett).",
                "I can describe architectural structures, domes, and ornamental forms in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "lechnerodon",
                "title": "Lechner Ödön és a nemzeti formanyelv keresése",
                "summary": "Often called the Hungarian Gaudí, Ödön Lechner rejected historicist imitation to create a modern national style in the Museum of Applied Arts and the Postal Savings Bank.",
                "location": "Budapest, Üllői út (Iparművészeti Múzeum) és Hold utca (Postatakarékpénztár)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "„Magyar formanyelv nem volt, hanem lesz” — hirdette Lechner Ödön, akit a nemzetközi építészettörténet gyakran a magyar Gaudíként emleget. Miután éveket töltött Párizsban és Londonban, Lechner felismerte, hogy a görög oszlopokat vagy gótikus csúcsíveket utánzó historizmus nem fejezheti ki a modern magyar társadalom önazonosságát."
                    },
                    {
                        "type": "narration",
                        "text": "Lechner a magyar népművészet — különösen a hímzett szűrök, a virágos kerámiák és a keleti szőnyegek — motívumkincséhez fordult inspirációért. Ezeket a díszítőelemeket azonban nem egyszerűen ráfestette a falakra, hanem magának az épületnek a tömegformálásába, az ívelt párkányokba és az áttört csarnokokba építette bele."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1896-ban felavatott Iparművészeti Múzeum az Üllői úton azonnal heves vitákat váltott ki. A Pártos Gyulával közösen tervezett palota smaragdzöld és aranysárga tetőzete, keleties kupolája, valamint a hófehér belső üvegcsarnok merészen szakított az akadémikus hagyománnyal. A belső térben Lechner bátran láthatóvá tette a modern acélszerkezetet, miközben a korlátokat virágos vonalakkal lágyította."
                    },
                    {
                        "type": "narration",
                        "text": "Még kiforrottabb remekműnek bizonyult a Hold utcában 1901-ben átadott Magyar Királyi Postatakarékpénztár. A szűk belvárosi utcában álló épület homlokzatát Lechner felfelé egyre gazdagodó díszítéssel látta el, így a járókelő tekintete önkéntelenül a tetőzet színes kerámiakoronájára és a szorgalmat jelképező arany méhkaptárakra emelkedik."
                    },
                    {
                        "type": "narration",
                        "text": "Bár a hivatalos állami megbízók később háttérbe szorították, a Lechner Ödön által elindított szecessziós mozgalom fiatal építészek egész nemzedékét — köztük Lajta Bélát, Komor Marcellt és Kós Károlyt — ihlette meg."
                    }
                ]
            },
            "words": [
                {"lemma": "formanyelv", "translation": "formal language / architectural idiom", "pos": "noun"},
                {"lemma": "kupola", "translation": "dome / cupola", "pos": "noun"},
                {"lemma": "párkány", "translation": "cornice / ledge", "pos": "noun"},
                {"lemma": "motívumkincs", "translation": "repertoire of motifs", "pos": "noun"},
                {"lemma": "méhkaptár", "translation": "beehive", "pos": "noun"},
                {"lemma": "felavatott", "translation": "inaugurated / dedicated (past participle)", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "passive-participial-clauses-t-tt",
                "title": "Passive & Anterior Pre-Nominal Participles (-t/-tt) with által",
                "text1_title": "Describing Completed Actions Before the Noun",
                "text1": "To describe a building or work of art through who designed it, when it was built, or how it was decorated, Hungarian uses the past/passive participle (-t/-tt) before the noun: az 1896-ban felavatott Iparművészeti Múzeum ('the Museum of Applied Arts inaugurated in 1896').",
                "text2_title": "Expressing the Agent with [Noun] + által + [-t/-tt Participle]",
                "text2": "Since Hungarian rarely uses passive main verbs in everyday sentences, the agentive postposition által ('by') thrives inside pre-nominal -t/-tt participial clauses: a Lechner Ödön által tervezett Postatakarékpénztár ('the Postal Savings Bank designed by Ödön Lechner').",
                "table_title": "Agentive & Temporal -t/-tt Participial Modifiers",
                "table_rows": [
                    ["a Lechner Ödön által tervezett épület", "the building designed by Ödön Lechner"],
                    ["az 1896-ban felavatott múzeum", "the museum inaugurated in 1896"],
                    ["a Pártos Gyulával közösen megalkotott palota", "the palace co-created with Gyula Pártos"],
                    ["a virágos vonalakkal díszített üvegcsarnok", "the glass hall decorated with floral lines"]
                ],
                "examples": [
                    {
                        "spanish": "A Lechner Ödön által tervezett Postatakarékpénztár a magyar szecesszió csúcspontja.",
                        "english": "The Postal Savings Bank designed by Ödön Lechner is the pinnacle of the Hungarian Secession."
                    },
                    {
                        "spanish": "Az 1896-ban felavatott Iparművészeti Múzeum smaragdzöld kupolája messziről ragyog.",
                        "english": "The emerald-green dome of the Museum of Applied Arts, inaugurated in 1896, shines from afar."
                    }
                ],
                "tip": "Keep the exact order: [Article] + [Agent + által] + [Adverbs/Cases] + [-t/-tt Participle] + [Head Noun], e.g. a Lechner által 1901-ben átadott épület."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelképeztek a Postatakarékpénztár tetején elhelyezett arany 'méhkaptárak'?",
                    "options": [
                        "A takarékosságot és a szorgalmas gyűjtögető munkát.",
                        "A méhészek országos szakszervezetét.",
                        "A francia királyi udvar címerét."
                    ],
                    "correct": 0,
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Lechner Ödön a magyar népművészet gazdag _____ merített ihletet az épületeihez. (repertoire of motifs - motívumkincséből)",
                    "answer": "motívumkincséből",
                    "english": "Ödön Lechner drew inspiration for his buildings from the rich motif repertoire of Hungarian folk art.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A Lechner Ödön _____ tervezett Postatakarékpénztár 1901-ben nyílt meg a Hold utcában. (by - által)",
                    "answer": "által",
                    "english": "The Postal Savings Bank designed by Ödön Lechner opened in 1901 on Hold Street.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban áll helyesen a befejezett melléknévi igeneves szerkezet?",
                    "options": [
                        "Az 1896-ban felavatott Iparművészeti Múzeum merészen szakított a historizmussal.",
                        "Az Iparművészeti Múzeum felavatott 1896-ban merészen szakított a historizmussal.",
                        "A felavatott az 1896-ban Iparművészeti Múzeum merészen szakított a historizmussal."
                    ],
                    "correct": 0,
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "Lechner", "Ödön", "által", "elindított", "mozgalom", "fiatal", "építészeket", "ihletett", "meg."],
                    "solution": ["A", "Lechner", "Ödön", "által", "elindított", "mozgalom", "fiatal", "építészeket", "ihletett", "meg."],
                    "english": "The movement launched by Ödön Lechner inspired young architects.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mit gondolt Lechner Ödön a magyar építészeti formanyelvről?",
                    "options": [
                        "Úgy vélte, hogy magyar formanyelv a múltban nem volt, hanem a népművészet és a modern technika ötvözésével a jövőben fog megszületni.",
                        "Azt vallotta, hogy kizárólag a középkori gótikus templomokat szabad szolgai módon lemásolni.",
                        "Elutasította a kerámia és a vasbeton használatát a városi építészetben."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Az", "Iparművészeti", "Múzeum", "smaragdzöld", "kupolája", "messziről", "magára", "vonja", "a", "tekintetet."],
                    "solution": ["Az", "Iparművészeti", "Múzeum", "smaragdzöld", "kupolája", "messziről", "magára", "vonja", "a", "tekintetet."],
                    "english": "The emerald-green dome of the Museum of Applied Arts draws the eye from afar.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence about the Postal Savings Bank using 'a Lechner Ödön által tervezett ...'.",
                            "answer": "A Lechner Ödön által tervezett Postatakarékpénztár homlokzatát színes kerámiák és arany méhkaptárak díszítik."
                        },
                        {
                            "prompt": "Describe the Museum of Applied Arts using an '-t/-tt' participial phrase with a year ('az 1896-ban átadott').",
                            "answer": "Az 1896-ban átadott Iparművészeti Múzeum belső csarnoka acélt és üveget ötvözött."
                        }
                    ],
                    "teaches": ["b2-participial-clauses"]
                }
            ]
        },
        {
            "num": 3,
            "title": "Zsolnay Ceramics and Folk Motifs in Stone",
            "grammar_label": "Combining instrumental and locative arguments inside participial phrases",
            "goals": [
                "I can explain the technological innovation of Vilmos Zsolnay's pyrogranite and eosin glazes in Pécs.",
                "I can embed instrumental (-val/-vel) and locative (-ban/-ben, -on/-en) arguments inside pre-nominal participial clauses.",
                "I can describe architectural materials, glazes, and decorative surfaces."
            ],
            "story_segment": {
                "seg_slug": "zsolnaymaza",
                "title": "Zsolnay-kerámia és kőbe álmodott népi motívumok",
                "summary": "Vilmos Zsolnay's factory in Pécs developed frost-resistant pyrogranite and iridescent eosin glaze, enabling Lechner's colorful rooftops and facades across Budapest.",
                "location": "Pécs (Zsolnay-gyár) és Budapest",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Lechner Ödön építészeti látomása aligha valósulhatott volna meg egyetlen rendkívüli ipari szövetséges nélkül: ez a pécsi Zsolnay Vilmos kerámiagyára volt. Lechner tudta, hogy a nagyvárosi füsttel és a kemény téli faggyal szemben a hagyományos vakolat hamar elszürkül. Olyan anyagra volt szüksége, amely egyszerre viseli el az időjárás viszontagságait, és ragyogó színekkel emeli ki a népművészeti ihletésű ornamentikát."
                    },
                    {
                        "type": "narration",
                        "text": "A megoldást a Zsolnay-gyárban kifejlesztett pirogránit jelentette. Ez a különleges összetételű, magas hőfokon kiégetett kerámia teljesen fagyállónak és savállónak bizonyult, így tetőcserepek, homlokzati burkolólapok és szobrászati díszek formájában egyaránt alkalmazható volt. A napsütésben szikrázó Zsolnay-tetők — az Iparművészeti Múzeumtól a Földtani Intézet kék hullámaiig — új színt vittek a budapesti látképbe."
                    },
                    {
                        "type": "narration",
                        "text": "Zsolnay Vilmos másik világhírű találmánya a hajnali pír görög nevéről elnevezett eozinmáz volt, amelyet Wartha Vince műegyetemi professzorral közösen kísérletezett ki. A fémesen irizáló, rubinvörös, zöld és arany fényben játszó máz a dísztárgyakat és a belső terek burkolatait egyaránt elvarázsolta."
                    },
                    {
                        "type": "narration",
                        "text": "A szecessziós épületeken megjelenő tulipánok, pávák, gránátalmák és indák nem véletlenszerű díszek voltak. A színes mázzal bevont kerámiák a falusi fazekasság és a pásztorművészet formáit emelték át a modern nagyváros kőből és vasbetonból épült palotáira."
                    },
                    {
                        "type": "narration",
                        "text": "Így találkozott a pécsi műhely vegyészeti tudása és a pesti építészek művészi képzelete: a tudomány és a népművészet szövetségéből olyan épületek születtek, amelyek több mint egy évszázad múltán is eredeti színeikben ragyognak."
                    }
                ]
            },
            "words": [
                {"lemma": "pirogránit", "translation": "pyrogranite (frost-resistant architectural ceramic)", "pos": "noun"},
                {"lemma": "máz", "translation": "ceramic glaze", "pos": "noun"},
                {"lemma": "fagyálló", "translation": "frost-resistant", "pos": "adjective"},
                {"lemma": "tetőcserép", "translation": "roof tile", "pos": "noun"},
                {"lemma": "ornamentika", "translation": "ornamentation / decorative patternwork", "pos": "noun"},
                {"lemma": "irizáló", "translation": "iridescent / shimmering", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "participial-instrumental-locative",
                "title": "Packing Instrumental and Locative Details into Participial Modifiers",
                "text1_title": "Material and Means with -val/-vel Inside the Participial Phrase",
                "text1": "In architectural and art-historical descriptions, Hungarian regularly embeds instrumental complements (-val/-vel, 'with/in') inside pre-nominal participial clauses to specify materials, glazes, or techniques: a színes mázzal bevont kerámiák ('the ceramics coated with colorful glaze') or a fémes fényben játszó eozinmáz ('the eosin glaze playing in metallic light').",
                "text2_title": "Locative and Manner Modifiers Before the Participle",
                "text2": "Locative phrases (a Zsolnay-gyárban kifejlesztett) and manner phrases (magas hőfokon kiégetett) can stack sequentially before the noun without needing a single relative pronoun: a Zsolnay-gyárban kifejlesztett, magas hőfokon kiégetett pirogránit.",
                "table_title": "Multi-Complement Pre-Nominal Participial Modifiers",
                "table_rows": [
                    ["a színes mázzal bevont tetőcserepek", "the roof tiles coated with colorful glaze"],
                    ["a magas hőfokon kiégetett pirogránit", "the pyrogranite fired at a high temperature"],
                    ["a napsütésben szikrázó Zsolnay-tetők", "the Zsolnay roofs sparkling in the sunshine"],
                    ["a hajnali pírról elnevezett eozinmáz", "the eosin glaze named after the flush of dawn"]
                ],
                "examples": [
                    {
                        "spanish": "A Zsolnay-gyárban kifejlesztett pirogránit teljesen fagyállónak bizonyult.",
                        "english": "The pyrogranite developed in the Zsolnay factory proved completely frost-resistant."
                    },
                    {
                        "spanish": "A színes mázzal bevont kerámiák a falusi fazekasság formáit emelték át a nagyvárosba.",
                        "english": "The ceramics coated with colorful glaze transferred the forms of village pottery into the metropolis."
                    }
                ],
                "tip": "When stacking two participial modifiers before a single noun, separate them with a comma: a magas hőfokon kiégetett, színes mázzal bevont kerámiák."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Miért volt forradalmi jelentőségű a Zsolnay-gyárban kifejlesztett 'pirogránit' az építészetben?",
                    "options": [
                        "Mert magas hőfokon kiégetett, teljesen fagy- és saválló kerámia volt, így kültéri tetők és homlokzatok díszítésére is alkalmasnak bizonyult.",
                        "Mert papírból készült, és esőben könnyen lemosható volt.",
                        "Mert kizárólag fekete-fehér színben lehetett előállítani."
                    ],
                    "correct": 0,
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A Zsolnay-dísztárgyak felületén fémes fényben _____ eozinmáz világhírűvé tette a pécsi gyárat. (shimmering / iridescent - irizáló)",
                    "answer": "irizáló",
                    "english": "The eosin glaze shimmering in metallic light on the surface of Zsolnay art objects made the Pécs factory world-famous.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A színes mázzal _____ tetőcserepek több mint száz éve díszítik az épületet. (coated - bevont)",
                    "answer": "bevont",
                    "english": "The roof tiles coated with colorful glaze have decorated the building for more than a hundred years.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat sűríti helyesen melléknévi igeneves szerkezetbe a következő két állítást? 'A pirogránitot a Zsolnay-gyárban fejlesztették ki. A pirogránit magas hőfokon égett ki.'",
                    "options": [
                        "A Zsolnay-gyárban kifejlesztett, magas hőfokon kiégetett pirogránit ellenállt a téli fagynak.",
                        "A kifejlesztett Zsolnay-gyárban pirogránit kiégetett magas hőfokon ellenállt a téli fagynak.",
                        "A pirogránit a Zsolnay-gyárban kifejlesztett ellenállt a téli fagynak."
                    ],
                    "correct": 0,
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "napsütésben", "szikrázó", "Zsolnay-tetők", "új", "színt", "vittek", "a", "budapesti", "látképbe."],
                    "solution": ["A", "napsütésben", "szikrázó", "Zsolnay-tetők", "új", "színt", "vittek", "a", "budapesti", "látképbe."],
                    "english": "The Zsolnay roofs sparkling in the sunshine brought new color to the Budapest skyline.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Kivel közösen kísérletezte ki Zsolnay Vilmos a fémes fényű eozinmázat?",
                    "options": [
                        "Wartha Vince műegyetemi professzorral.",
                        "Molnár Ferenc drámaíróval.",
                        "Kazinczy Ferenc nyelvújítóval."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "fagyálló", "tetőcserepek", "és", "a", "gazdag", "ornamentika", "ellenálltak", "az", "időjárásnak."],
                    "solution": ["A", "fagyálló", "tetőcserepek", "és", "a", "gazdag", "ornamentika", "ellenálltak", "az", "időjárásnak."],
                    "english": "The frost-resistant roof tiles and rich ornamentation withstood the weather.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Describe Zsolnay roof tiles using a pre-nominal participial phrase ('a színes mázzal bevont ...').",
                            "answer": "A színes mázzal bevont tetőcserepek a legszürkébb téli napon is ragyognak."
                        },
                        {
                            "prompt": "Describe pyrogranite using 'a magas hőfokon kiégetett ...'.",
                            "answer": "A magas hőfokon kiégetett pirogránit lehetővé tette a homlokzatok gazdag szobrászati díszítését."
                        }
                    ],
                    "teaches": ["b2-participial-clauses"]
                }
            ]
        },
        {
            "num": 4,
            "title": "Grand Boulevards and Courtyard Tenements",
            "grammar_label": "Nested and stacked pre-nominal participial modifiers in spatial prose",
            "goals": [
                "I can explain the social geography of a Budapest bérház (courtyard tenement) from street-front apartments to inner galleries.",
                "I can build nested and stacked participial modifiers to contrast architectural spaces.",
                "I can use residential architecture vocabulary (bérház, függőfolyosó, kovácsoltvas, udvar)."
            ],
            "story_segment": {
                "seg_slug": "korutakberhazak",
                "title": "Nagykörúti paloták és gangos bérházak",
                "summary": "Budapest's turn-of-the-century tenement buildings (bérházak) brought diverse social classes under one roof, with opulent street-facing salons and wrought-iron courtyard galleries (gangok).",
                "location": "Budapest, Nagykörút és belső udvarok",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A századfordulós Budapest társadalomtörténetét nemcsak a múzeumok és bankpaloták őrzik, hanem a Nagykörút és a mellékutcák több ezer gangos bérháza is. Ezek az épületek különös társadalmi keresztmetszetet alkottak: egyetlen kapu mögött, ugyanazon tető alatt élt a nagypolgár, a hivatalnok, a kisiparos és a cseléd."
                    },
                    {
                        "type": "narration",
                        "text": "Az utcára néző, erkélyes első és második emeleti lakásokban tágas szalonok, parkettás ebédlők és színes ólomüveg ablakokkal megvilágított főlépcsőházak fogadták a tehetősebb bérlőket. A belső udvarra nyíló, kovácsoltvas korlátos függőfolyosók — a pesti nyelvben gangok — mentén viszont jóval kisebb, gyakran csak szoba-konyhás lakások sorakoztak."
                    },
                    {
                        "type": "narration",
                        "text": "A szecessziós építészek azonban a bérházak tervezésekor is arra törekedtek, hogy a mindennapi lakókörnyezetet művészi élménnyé emeljék. A Kőrössy Albert Kálmán, Vágó József vagy Lajta Béla által tervezett bérpaloták kapualját márványburkolat, pávás kovácsoltvas rács és virágmintás stukkó díszítette."
                    },
                    {
                        "type": "narration",
                        "text": "A függőfolyosó egyszerre volt közlekedési útvonal és nyilvános színpad. A korlátra könyöklő lakók innen figyelték az udvaron játszó gyerekeket, a szőnyeget poroló szomszédokat vagy az utcai árusokat. A Pál utcai fiúk és számos huszadik századi magyar regény világa éppen ezekben a gangos udvarokban kelt életre."
                    },
                    {
                        "type": "narration",
                        "text": "A pesti bérház így sajátos városi közösséget teremtett: miközben a homlokzat a világváros eleganciáját mutatta, a belső udvar megőrizte az emberi léptékű szomszédság intimitását."
                    }
                ]
            },
            "words": [
                {"lemma": "bérház", "translation": "apartment building / tenement house", "pos": "noun"},
                {"lemma": "függőfolyosó", "translation": "open courtyard gallery / 'gang' walkway", "pos": "noun"},
                {"lemma": "kovácsoltvas", "translation": "wrought iron", "pos": "noun"},
                {"lemma": "ólomüveg", "translation": "stained glass / leaded glass", "pos": "noun"},
                {"lemma": "kapualj", "translation": "arched gateway / entrance passage", "pos": "noun"},
                {"lemma": "társadalmi keresztmetszet", "translation": "social cross-section", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "stacked-participial-modifiers-berhaz",
                "title": "Stacked & Contrasted Participial Modifiers in Spatial Description",
                "text1_title": "Contrasting Street-Facing vs. Courtyard-Facing Spaces",
                "text1": "When describing complex spatial layouts like the Budapest bérház, Hungarian uses parallel pre-nominal participial phrases to contrast different zones within the same sentence: az utcára néző, erkélyes lakások ('the balconied apartments facing the street') versus a belső udvarra nyíló, kovácsoltvas korlátos függőfolyosók ('the wrought-iron railed galleries opening onto the inner courtyard').",
                "text2_title": "Nesting Participial Modifiers Inside Larger Noun Phrases",
                "text2": "A pre-nominal participial phrase can modify a noun that itself serves as an argument of another noun or postposition: a színes ólomüveg ablakokkal megvilágított főlépcsőházak ('the main staircases illuminated by colorful stained-glass windows').",
                "table_title": "Spatial Participial Contrasts in Tenement Architecture",
                "table_rows": [
                    ["az utcára néző, tágas lakások", "the spacious apartments facing the street"],
                    ["a belső udvarra nyíló függőfolyosók", "the open galleries opening onto the inner courtyard"],
                    ["az ólomüveg ablakokkal megvilágított lépcsőház", "the staircase illuminated by stained-glass windows"],
                    ["a korlátra könyöklő lakók", "the residents leaning on the railing"]
                ],
                "examples": [
                    {
                        "spanish": "Az utcára néző lakásokban tágas szalonok voltak, a belső udvarra nyíló függőfolyosók mentén viszont kisebb lakások sorakoztak.",
                        "english": "In the apartments facing the street there were spacious salons, whereas along the galleries opening onto the inner courtyard smaller flats were lined up."
                    },
                    {
                        "spanish": "A korlátra könyöklő lakók a függőfolyosóról figyelték az udvaron játszó gyerekeket.",
                        "english": "The residents leaning on the railing watched the children playing in the courtyard from the gallery."
                    }
                ],
                "tip": "Notice how directional suffixes (-ra/-re with néző/nyíló, -on/-en with játszó) attach to the noun BEFORE the participle: az utcára néző, az udvaron játszó."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit neveznek a budapesti bérházakban 'függőfolyosónak' (vagy pesti szóval 'gangnak')?",
                    "options": [
                        "A belső udvarra nyíló, emeleti lakásokat összekötő, kovácsoltvas korlátos nyitott folyosót.",
                        "A Duna felett átívelő vasúti hidat.",
                        "Az alagsorban működő szénraktárt."
                    ],
                    "correct": 0,
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A szecessziós bérpaloták lépcsőházát virágmintás _____ korlátok és színes ólomüveg ablakok díszítették. (wrought iron - kovácsoltvas)",
                    "answer": "kovácsoltvas",
                    "english": "The staircases of Secessionist apartment palaces were decorated with floral wrought-iron railings and colorful stained-glass windows.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az utcára _____ első emeleti lakásokban a tehetősebb polgárok éltek. (facing - néző)",
                    "answer": "néző",
                    "english": "More affluent burghers lived in the first-floor apartments facing the street.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat tartalmaz két helyesen felépített, jelzői szerepű melléknévi igeneves szerkezetet?",
                    "options": [
                        "A korlátra könyöklő lakók mosolyogva figyelték a belső udvaron játszó gyerekeket.",
                        "A lakók könyöklő a korlátra mosolyogva figyelték a gyerekeket játszó a belső udvaron.",
                        "A könyöklő korlátra lakók figyelték a játszó belső udvaron gyerekeket."
                    ],
                    "correct": 0,
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Az", "ólomüveg", "ablakokkal", "megvilágított", "főlépcsőház", "a", "szecessziós", "bérház", "dísze", "volt."],
                    "solution": ["Az", "ólomüveg", "ablakokkal", "megvilágított", "főlépcsőház", "a", "szecessziós", "bérház", "dísze", "volt."],
                    "english": "The main staircase illuminated by stained-glass windows was the ornament of the Secessionist apartment building.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért mondhatjuk, hogy a századfordulós pesti bérház 'társadalmi keresztmetszetet' alkotott?",
                    "options": [
                        "Mert ugyanazon tető alatt, az utcai szalonoktól az udvari kis lakásokig különböző társadalmi rétegek éltek együtt.",
                        "Mert minden egyes bérházban csak egyetlen szakma képviselői lakhattak.",
                        "Mert a bérházakba tilos volt családoknak beköltözni."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "pesti", "bérház", "kapualját", "márványburkolat", "és", "pávás", "kovácsoltvas", "rács", "díszítette."],
                    "solution": ["A", "pesti", "bérház", "kapualját", "márványburkolat", "és", "pávás", "kovácsoltvas", "rács", "díszítette."],
                    "english": "The entrance passage of the Pest tenement house was decorated with marble cladding and a peacock wrought-iron grille.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Contrast street-facing apartments ('az utcára néző lakások') with courtyard galleries ('a belső udvarra nyíló függőfolyosók').",
                            "answer": "Az utcára néző lakásokban tágas szalonok voltak, a belső udvarra nyíló függőfolyosók mentén viszont szerényebb otthonok sorakoztak."
                        },
                        {
                            "prompt": "Describe the main staircase using 'a színes ólomüveg ablakokkal megvilágított ...'.",
                            "answer": "A színes ólomüveg ablakokkal megvilágított lépcsőház már a belépéskor művészi élményt nyújtott."
                        }
                    ],
                    "teaches": ["b2-participial-clauses"]
                }
            ]
        },
        {
            "num": 5,
            "title": "Reading History in Budapest's Facades",
            "grammar_label": "Extended temporal and passive participial chains (-andó/-endő and layered -t/-tt)",
            "goals": [
                "I can trace the evolution from floral Secession to Béla Lajta's pre-modern geometric architecture and contemporary heritage preservation.",
                "I can use future/gerundive participles (-andó/-endő) and layered -t/-tt modifiers in formal descriptions.",
                "I can discuss architectural conservation, facades, and reinforced concrete in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "homlokzatok",
                "title": "Történelemolvasás Budapest homlokzatain",
                "summary": "From Béla Lajta's Rózsavölgyi House combining pre-modern reinforced concrete with folk geometry to modern restoration, Budapest's facades preserve over a century of history.",
                "location": "Budapest, Szervita tér és belváros",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1910-es évek elejére a magyar szecesszió új szakaszba lépett. A Lechner Ödön nyomdokain induló fiatalabb építészek — mindenekelőtt Lajta Béla — a buja virágdíszítés helyett a fegyelmezettebb geometriai formák és a legmodernebb vasbeton szerkezetek felé fordultak. A Szervita téren 1912-ben felépült Rózsavölgyi-ház már a huszadik századi modern építészet előfutára volt: alsó szintjeit hatalmas üvegkirakatok, felső emeleteit pedig népi szőtteseket idéző Zsolnay-kerámiasávok tagolták."
                    },
                    {
                        "type": "narration",
                        "text": "Hasonlóan bátor kísérlet volt a Kós Károly és Zrumeczky Dezső által megálmodott Fővárosi Állat- és Növénykert épületegyüttese, amely az erdélyi Kalotaszeg faépítészetét és tornyait ültette át a Városligetbe. Ezek az alkotások megmutatták, hogy a nemzeti hagyomány és a modern mérnöki gondolkodás nem kizárja, hanem erősíti egymást."
                    },
                    {
                        "type": "narration",
                        "text": "A huszadik század viharai mély nyomokat hagytak Budapest homlokzatain. A második világháborús ostrom és az 1956-os harcok során megsérült párkányok, valamint az évtizedeken át elhanyagolt kerámiadíszek sok helyen veszélybe kerültek. Egy-egy belvárosi bérház falán a figyelmes szemlélő ma is egyszerre olvashatja le a századelő polgári önbizalmát és a diktatúrák sebeit."
                    },
                    {
                        "type": "narration",
                        "text": "Az elmúlt évtizedekben azonban a megőrzendő műemléki értékek védelme új lendületet kapott. A gondosan restaurált homlokzatok — a Gresham-palotától a Zeneakadémián át az Iparművészeti Múzeum megújuló épületéig — ismét eredeti pompájukban mutatják meg a századforduló alkotóerejét."
                    },
                    {
                        "type": "narration",
                        "text": "Aki ma végigsétál Budapest utcáin, és felemeli a tekintetét az emeletek fölé, kőbe, vasba és Zsolnay-mázba írt történelemkönyvet lapoz végig."
                    }
                ]
            },
            "words": [
                {"lemma": "homlokzat", "translation": "facade", "pos": "noun"},
                {"lemma": "vasbeton", "translation": "reinforced concrete", "pos": "noun"},
                {"lemma": "műemlék", "translation": "protected historic monument / heritage building", "pos": "noun"},
                {"lemma": "előfutár", "translation": "forerunner / precursor", "pos": "noun"},
                {"lemma": "megőrzendő", "translation": "to be preserved / worthy of preservation (-andó/-endő participle)", "pos": "adjective"},
                {"lemma": "restaurált", "translation": "restored (past participle)", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "participial-gerundive-and-synthesis",
                "title": "Gerundive Participles (-andó/-endő) and Layered Architectural Modifiers",
                "text1_title": "Necessity Before the Noun: The -andó/-endő Participle",
                "text1": "Alongside active (-ó/-ő) and passive/anterior (-t/-tt) participles, Hungarian possesses a third pre-nominal participle in -andó/-endő ('to be done / that must be done'): a megőrzendő műemléki értékek ('the heritage values to be preserved'), a felújítandó homlokzatok ('the facades to be renovated'). It is especially frequent in civic, architectural, and legal registers.",
                "text2_title": "Synthesizing All Three Participial Types",
                "text2": "At B2 level, you can distinguish all three temporal/voice relationships before a single noun: a várost díszítő homlokzat ('the facade decorating the city', active ongoing), a gondosan restaurált homlokzat ('the carefully restored facade', completed passive), and a jövőnek megőrzendő homlokzat ('the facade to be preserved for the future', deontic future).",
                "table_title": "The Three Hungarian Pre-Nominal Participles",
                "table_rows": [
                    ["Active (-ó/-ő): a népi szőtteseket idéző kerámiasávok", "the ceramic bands evoking folk weavings"],
                    ["Passive/Anterior (-t/-tt): az ostrom során megsérült párkányok", "the cornices damaged during the siege"],
                    ["Deontic/Future (-andó/-endő): a megőrzendő műemléki értékek", "the heritage values to be preserved"]
                ],
                "examples": [
                    {
                        "spanish": "Az ostrom során megsérült párkányok és a megőrzendő műemléki értékek gondos restaurálásra szorultak.",
                        "english": "The cornices damaged during the siege and the heritage values to be preserved required careful restoration."
                    },
                    {
                        "spanish": "A Szervita téren 1912-ben felépült Rózsavölgyi-ház a modern építészet előfutára volt.",
                        "english": "The Rózsavölgyi House built in 1912 on Szervita Square was a forerunner of modern architecture."
                    }
                ],
                "tip": "Vowel harmony determines -andó (back vowels: felújítandó, megoldandó) vs. -endő (front vowels: megőrzendő, követendő)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit fejez ki a 'megőrzendő műemlék' szerkezetben a '-endő' képzős melléknévi igenév?",
                    "options": [
                        "Azt, hogy a műemléket a jövő generációi számára kötelességünk megőrizni és megvédeni.",
                        "Azt, hogy a műemléket már régen lebontották.",
                        "Azt, hogy a műemlék saját maga őrzi a szomszédos utcát."
                    ],
                    "correct": 0,
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Lajta Béla a Rózsavölgyi-ház tervezésekor modern _____ szerkezetet és Zsolnay-kerámiát ötvözött. (reinforced concrete - vasbeton)",
                    "answer": "vasbeton",
                    "english": "When designing the Rózsavölgyi House, Béla Lajta combined a modern reinforced concrete structure with Zsolnay ceramics.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A háborús ostrom során _____ homlokzatokat az elmúlt években gondosan restaurálták. (damaged - megsérült)",
                    "answer": "megsérült",
                    "english": "The facades damaged during the wartime siege have been carefully restored in recent years.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik melléknévi igenév fejezi ki a jövőbeli szükségszerűséget ('facades that need to be renovated')?",
                    "options": [
                        "a sürgősen felújítandó homlokzatok",
                        "a sürgősen felújító homlokzatok",
                        "a sürgősen felújított homlokzatok"
                    ],
                    "correct": 0,
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "gondosan", "restaurált", "homlokzatok", "ismét", "eredeti", "pompájukban", "ragyognak."],
                    "solution": ["A", "gondosan", "restaurált", "homlokzatok", "ismét", "eredeti", "pompájukban", "ragyognak."],
                    "english": "The carefully restored facades shine once again in their original splendor.",
                    "teaches": ["b2-participial-clauses"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mi jellemezte Lajta Béla 1912-es Rózsavölgyi-házát a Szervita téren?",
                    "options": [
                        "A modern vasbeton és üvegkirakatok összekapcsolása a népi szőtteseket idéző geometriai Zsolnay-kerámiasávokkal.",
                        "A középkori várárok és felvonóhíd visszaépítése a belvárosban.",
                        "A teljes ablaknélküliség és a nyers téglafalak használata."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "megőrzendő", "műemlékek", "Budapest", "századfordulós", "történelmét", "mesélik", "el."],
                    "solution": ["A", "megőrzendő", "műemlékek", "Budapest", "századfordulós", "történelmét", "mesélik", "el."],
                    "english": "The historic monuments to be preserved recount Budapest's turn-of-the-century history.",
                    "teaches": ["b2-szecesszio-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Describe the Rózsavölgyi House using a pre-nominal participial modifier ('a népi szőtteseket idéző ...').",
                            "answer": "A népi szőtteseket idéző kerámiasávok egyedülálló ritmust adnak a Rózsavölgyi-ház homlokzatának."
                        },
                        {
                            "prompt": "Write a sentence about protecting historic buildings using 'megőrzendő' or 'felújítandó'.",
                            "answer": "A jövő nemzedékei számára megőrzendő szecessziós paloták Budapest legértékesebb kincsei közé tartoznak."
                        }
                    ],
                    "teaches": ["b2-participial-clauses"]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can discuss Budapest's urban unification, Ödön Lechner's Hungarian Secession, and Zsolnay ceramics with B2 precision.",
            "I can construct active (-ó/-ő), passive/anterior (-t/-tt), and gerundive (-andó/-endő) pre-nominal participial clauses.",
            "I can embed agentive (X által), instrumental (-val/-vel), and locative arguments before the head noun."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik építészeti anyag tette lehetővé a szecessziós épületek fagyálló, színes tető- és homlokzatburkolatát?",
                "options": ["pirogránit", "kutyanyelv", "kefelenyomat", "vitairat"],
                "correct": 0,
                "teaches": ["b2-szecesszio-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban szerepel helyes előidejű/szenvedő melléknévi igeneves jelző?",
                "options": [
                    "A Lechner Ödön által tervezett Postatakarékpénztár a Hold utcában áll.",
                    "A tervezett Lechner Ödön által Postatakarékpénztár a Hold utcában áll.",
                    "A Postatakarékpénztár által Lechner Ödön tervező a Hold utcában áll."
                ],
                "correct": 0,
                "teaches": ["b2-participial-clauses"]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan hívják a pesti bérházak belső udvarra nyíló, kovácsoltvas korlátos emeleti folyosóját?",
                "options": ["függőfolyosó (gang)", "sugárút", "kupola", "méhkaptár"],
                "correct": 0,
                "teaches": ["b2-szecesszio-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Zsolnay Vilmos által kifejlesztett _____ fémes, szivárványos fényben ragyog a kerámiákon. (eosin glaze - eozinmáz)",
                "answer": "eozinmáz",
                "english": "The eosin glaze developed by Vilmos Zsolnay shines in a metallic, iridescent light on the ceramics.",
                "teaches": ["b2-szecesszio-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A belvárost a Városligettel _____ Andrássy út alatt épült meg a kontinens első földalattija. (connecting - összekötő)",
                "answer": "összekötő",
                "english": "The continent's first underground railway was built beneath Andrássy Avenue, which connects the downtown with the City Park.",
                "teaches": ["b2-participial-clauses"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A közös örökségként _____ műemlékeket nagy gonddal kell restaurálni. (to be preserved - megőrzendő)",
                "answer": "megőrzendő",
                "english": "The historic monuments to be preserved as shared heritage must be restored with great care.",
                "teaches": ["b2-participial-clauses"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "színes", "mázzal", "bevont", "tetőcserepek", "a", "pécsi", "Zsolnay-gyárban", "készültek."],
                "solution": ["A", "színes", "mázzal", "bevont", "tetőcserepek", "a", "pécsi", "Zsolnay-gyárban", "készültek."],
                "english": "The roof tiles coated with colorful glaze were made in the Zsolnay factory in Pécs.",
                "teaches": ["b2-participial-clauses"]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Lechner", "Ödön", "a", "magyar", "népművészet", "motívumkincséből", "teremtett", "modern", "formanyelvet."],
                "solution": ["Lechner", "Ödön", "a", "magyar", "népművészet", "motívumkincséből", "teremtett", "modern", "formanyelvet."],
                "english": "Ödön Lechner created a modern architectural idiom from the motif repertoire of Hungarian folk art.",
                "teaches": ["b2-szecesszio-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent 'az udvarra nyíló függőfolyosó' kifejezés?",
                "options": [
                    "A függőfolyosó, amely a belső udvar felé nyílik.",
                    "A függőfolyosó, amelyet tegnap bezártak.",
                    "Az udvar, amelyet hamarosan fel kell újítani."
                ],
                "correct": 0,
                "teaches": ["b2-participial-clauses"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "1896-ban", "felavatott", "Iparművészeti", "Múzeum", "kupolája", "messziről", "ragyog."],
                "solution": ["Az", "1896-ban", "felavatott", "Iparművészeti", "Múzeum", "kupolája", "messziről", "ragyog."],
                "english": "The dome of the Museum of Applied Arts, inaugurated in 1896, shines from afar.",
                "teaches": ["b2-participial-clauses"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Write a sentence describing an Ödön Lechner building using 'által tervezett' and an '-ó/-ő' participle.",
                        "answer": "A Lechner Ödön által tervezett épület a napsütésben szikrázó Zsolnay-kerámiával nyűgözi le a látogatókat."
                    }
                ],
                "teaches": ["b2-participial-clauses"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Describe the difference between the street front and inner courtyard of a Budapest bérház using participial modifiers.",
                        "answer": "Az utcára néző homlokzat a világvárosi pompát hirdette, a belső udvarra nyíló függőfolyosó pedig a lakók mindennapi találkozóhelye volt."
                    }
                ],
                "teaches": ["b2-participial-clauses"]
            }
        ]
    }
}


# ============================================================================
# CULTURE UNIT 3: b2-nyelvujitas
# ============================================================================
UNIT_3_NYELVUJITAS = {
    "unit_num": 3,
    "slug": "nyelvujitas",
    "title": "The Language Reform & the Politics of Hungarian",
    "grammar_skill": "b2-nominalization-chains",
    "vocab_skill": "b2-nyelvujitas-vocab",
    "theme": "The Hungarian Language Reform and official state language",
    "location": "Széphalom, Pozsony és Pest",
    "combined_story_title": "Kazinczy tollától az államnyelvig",
    "combined_story_summary": "How Ferenc Kazinczy and the Language Reformers coined ten thousand Hungarian words, battled conservative orthologists, and achieved the 1844 milestone making Hungarian the language of state.",
    "intro_body": [
        "Until 1844, the official language of legislation and administration in the Kingdom of Hungary was Latin, while German dominated imperial administration and urban commerce. Between the 1780s and the 1840s, a remarkable movement known as the Language Reform (nyelvújítás), led by Ferenc Kazinczy from his small estate in Széphalom, created more than ten thousand new Hungarian words that we still use in every sentence today.",
        "In this unit, you will explore the cultural politics of the Language Reform while mastering B2 nominalization chains (-ás/-és action nouns with possessive and postpositional complements) and abstract noun derivations (-ság/-ség)."
    ],
    "lessons": [
        {
            "num": 1,
            "title": "When Latin Ruled the Diet",
            "grammar_label": "Action nominalizations (-ás/-és) with possessive genitive arguments",
            "goals": [
                "I can explain why Latin served as the official language of the Hungarian Diet until the 19th century and how Joseph II's 1784 language decree sparked the language movement.",
                "I can form -ás/-és verbal nouns and link their underlying object or subject via the possessive suffix (-a/-e, -ja/-je).",
                "I can discuss multilingual administration, decrees, and Enlightenment reforms in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "latinorszaggyules",
                "title": "Amikor a latin uralta az országgyűlést",
                "summary": "For centuries, Latin was the official language of the Hungarian Diet and courts; when Emperor Joseph II mandated German in 1784, he inadvertently triggered the Hungarian language movement.",
                "location": "Pozsony és Buda",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A tizennyolcadik század végén a Magyar Királyság nyilvános életét különös nyelvi kettősség jellemezte. Míg a falvakban és a mezővárosokban milliók beszéltek magyarul, addig a törvényhozás, a vármegyei közigazgatás, a bíróságok és a felsőoktatás hivatalos nyelve évszázadok óta a latin volt. A rendi országgyűlésen a követek latinul szónokoltak, és a törvénycikkek megszövegezése is kizárólag ezen a holt nyelven történt."
                    },
                    {
                        "type": "narration",
                        "text": "A fordulópontot II. József 1784-ben kiadott nyelvrendelete hozta el. A felvilágosult abszolutizmus uralkodója a birodalom hatékonyabb kormányzása érdekében elrendelte a latin nyelv felváltását a némettel a hivatali ügyintézésben. Bár az uralkodó pusztán gyakorlati racionalizálásra törekedett, a rendelet bevezetése váratlan és elemi erejű tiltakozást váltott ki a magyar vármegyékben."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar értelmiség és a nemesség ekkor döbbent rá arra, hogy ha a latint egy élő nyelv váltja fel, annak az ország saját nyelvének kell lennie. Ezzel egy időben azonban egy kíméletlen igazsággal is szembe kellett nézniük: a korabeli magyar szókincs még nem volt alkalmas a modern filozófia, a természettudományok, az államjog és az ipar fogalmainak pontos kifejezésére."
                    },
                    {
                        "type": "narration",
                        "text": "Bessenyei György, a bécsi testőrírók vezéralakja már 1778-ban megfogalmazta a felvilágosodás alaptételét: „Minden nemzet a maga nyelvén lett tudós, de idegenen sohasem.” A tudományok művelése és a nemzeti irodalom felemelése tehát elválaszthatatlanná vált az anyanyelv tudatos megújításától."
                    },
                    {
                        "type": "narration",
                        "text": "Így indult el az a fél évszázados szellemi küzdelem, amelynek célja egyrészt a magyar szókincs bővítése, másrészt a magyar nyelv hivatalos elismertetése volt."
                    }
                ]
            },
            "words": [
                {"lemma": "nyelvrendelet", "translation": "language decree / edict", "pos": "noun"},
                {"lemma": "törvényhozás", "translation": "legislation / legislature", "pos": "noun"},
                {"lemma": "közigazgatás", "translation": "public administration", "pos": "noun"},
                {"lemma": "szókincs", "translation": "vocabulary / lexicon", "pos": "noun"},
                {"lemma": "megszövegezés", "translation": "drafting / wording (nominalization)", "pos": "noun"},
                {"lemma": "elismertetés", "translation": "securing recognition of (nominalization)", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "nominalization-possessive-chains",
                "title": "Action Nominalizations (-ás/-és) with Possessive Genitive Arguments",
                "text1_title": "Turning Finite Clauses into Compact Noun Phrases",
                "text1": "Hungarian B2 academic, historical, and legal prose relies heavily on productive deverbal nouns formed with -ás/-és (e.g., bevezet -> bevezetés 'introduction', bővít -> bővítés 'expansion', megszövegez -> megszövegezés 'drafting'). When a transitive verb is nominalized, its former direct object becomes the possessor in a possessive construction: a törvénycikkek megszövegezése ('the drafting of the statutory articles'), a szókincs bővítése ('the expansion of the vocabulary').",
                "text2_title": "Chaining Nominalizations with Postpositions",
                "text2": "These possessed -ás/-és phrases regularly combine with postpositions such as érdekében ('in the interest of / in order to'), során ('in the course of'), or révén ('by means of'): a birodalom hatékonyabb kormányzása érdekében ('in the interest of governing the empire more effectively').",
                "table_title": "Finite Clause vs. Nominalized Possessive Chain",
                "table_rows": [
                    ["bevezették a rendeletet", "a rendelet bevezetése (the introduction of the decree)"],
                    ["bővítették a magyar szókincset", "a magyar szókincs bővítése (the expansion of the Hungarian vocabulary)"],
                    ["hogy hatékonyabban kormányozzák a birodalmat", "a birodalom hatékonyabb kormányzása érdekében"],
                    ["hogy hivatalosan elismertessék a nyelvet", "a nyelv hivatalos elismertetése (securing official recognition of the language)"]
                ],
                "examples": [
                    {
                        "spanish": "II. József a birodalom hatékonyabb kormányzása érdekében elrendelte a latin nyelv felváltását.",
                        "english": "In the interest of governing the empire more effectively, Joseph II ordered the replacement of the Latin language."
                    },
                    {
                        "spanish": "A rendelet bevezetése elemi erejű tiltakozást váltott ki a vármegyékben.",
                        "english": "The introduction of the decree provoked elemental protest in the counties."
                    }
                ],
                "tip": "Notice that adjectives modifying the original verb's manner become regular adjectives before the -ás/-és noun: hivatalosan elismertet -> a nyelv hivatalos elismertetése."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Milyen nyelven folyt a törvényhozás és a bírósági ügyintézés a Magyar Királyságban a 18. század végén?",
                    "options": [
                        "Latin nyelven.",
                        "Francia nyelven.",
                        "Olasz nyelven."
                    ],
                    "correct": 0,
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "II. József 1784-es _____ a latin helyett a németet kívánta hivatalos nyelvvé tenni. (language decree - nyelvrendelete)",
                    "answer": "nyelvrendelete",
                    "english": "Joseph II's 1784 language decree sought to make German the official language in place of Latin.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A magyar szókincs tudatos _____ nélkül nem születhetett volna meg a modern tudományos szaknyelv. (expansion of - bővítése)",
                    "answer": "bővítése",
                    "english": "Without the conscious expansion of the Hungarian vocabulary, modern scientific terminology could not have been born.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Alakítsd át főnévi igeneves/főnevesített szerkezetté: 'hogy hatékonyabban kormányozzák a birodalmat'!",
                    "options": [
                        "a birodalom hatékonyabb kormányzása érdekében",
                        "a birodalmat hatékonyabban kormányzás érdekében",
                        "a kormányzás a birodalom hatékonyabb érdekében"
                    ],
                    "correct": 0,
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "nyelvrendelet", "bevezetése", "heves", "tiltakozást", "váltott", "ki", "az", "országban."],
                    "solution": ["A", "nyelvrendelet", "bevezetése", "heves", "tiltakozást", "váltott", "ki", "az", "országban."],
                    "english": "The introduction of the language decree provoked fierce protest in the country.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mit mondott ki Bessenyei György híres 1778-as gondolata?",
                    "options": [
                        "Azt, hogy minden nemzet csak a saját anyanyelvén válhat igazán műveltté és tudóssá.",
                        "Azt, hogy a tudományokat kizárólag latin nyelven szabad tanítani az egyetemeken.",
                        "Azt, hogy a szókincs bővítése felesleges a modern korban."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "törvényhozás", "és", "a", "közigazgatás", "nyelve", "évszázadokon", "át", "a", "latin", "volt."],
                    "solution": ["A", "törvényhozás", "és", "a", "közigazgatás", "nyelve", "évszázadokon", "át", "a", "latin", "volt."],
                    "english": "For centuries, the language of legislation and public administration was Latin.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Rewrite 'A reformerek bővítették a magyar szókincset' as a nominalized subject phrase ('A magyar szókincs bővítése ...').",
                            "answer": "A magyar szókincs tudatos bővítése elengedhetetlen volt a modern tudományok műveléséhez."
                        },
                        {
                            "prompt": "Explain Joseph II's decree using a nominalization + 'érdekében'.",
                            "answer": "Az uralkodó a birodalom egységes irányítása érdekében adta ki az 1784-es nyelvrendeletet."
                        }
                    ],
                    "teaches": ["b2-nominalization-chains"]
                }
            ]
        },
        {
            "num": 2,
            "title": "Kazinczy and the Neologist Revolution",
            "grammar_label": "Multi-layered nominalization chains with során, révén, and ellenére",
            "goals": [
                "I can explain how Ferenc Kazinczy directed the Hungarian literary and language movement from Széphalom through sixteen thousand letters.",
                "I can construct multi-layered nominalization chains with postpositions (során, révén, céljából, ellenére).",
                "I can discuss aesthetic style (fentebb stíl), lexical coinage, and literary correspondence."
            ],
            "story_segment": {
                "seg_slug": "kazinczy",
                "title": "Kazinczy Ferenc és a neológus forradalom",
                "summary": "After more than six years as a political prisoner, Ferenc Kazinczy settled at Széphalom and organized the Neologist movement through an astonishing network of 16,000 letters.",
                "location": "Széphalom (Zemplén vármegye)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar nyelvújítás vezéralakja, Kazinczy Ferenc különös helyről irányította az ország szellemi megújulását. Miután a Martinovics-féle jakobinus mozgalomban való részvétele miatt több mint hat évet töltött várbörtönben — Kufstein, Spielberg és Munkács kazamatáiban —, 1801-ben szabadulva a zempléni Széphalomra vonult vissza. Akkoriban még nem létezett Magyar Tudós Társaság, sem központi irodalmi folyóirat, Kazinczy azonban egyszemélyes akadémiává változtatta szerény falusi kúriáját."
                    },
                    {
                        "type": "narration",
                        "text": "A kapcsolatépítés legfőbb eszköze a levelezés volt: Kazinczy élete során több mint tizenhatezer levelet váltott az ország íróival, tanáraival és tudósaival. A kéziratok átdolgozása, a fiatal tehetségek — köztük Berzsenyi Dániel és Kölcsey Ferenc — bátorítása, valamint az új kifejezések megalkotása révén egész nemzedéket nevelt igényes magyar stílusra."
                    },
                    {
                        "type": "narration",
                        "text": "Kazinczy esztétikai elméletének középpontjában az úgynevezett „fentebb stíl” állt. Úgy vélte, hogy az irodalmi nyelvnek nem csupán a hétköznapi közérthetőségre kell törekednie, hanem a gondolatok választékos, zenei és árnyalt kifejezésére is. Ennek elérése érdekében bátran javasolta régi, feledésbe merült magyar szavak felújítását, tájszavak beemelését és új szótövek képzését."
                    },
                    {
                        "type": "narration",
                        "text": "A nyelvújítás tehát Kazinczy szemében korántsem pusztán szótári gyűjtőmunka volt, hanem a nemzet esztétikai ízlésének nemesítése. Mint írta: „Jól és szépen az ír, aki tüzesen gondol, s érzékenyen érez.”"
                    },
                    {
                        "type": "narration",
                        "text": "A széphalmi mester fáradhatatlan szervezőmunkája nélkül a széttagolt magyar szellemi élet aligha válhatott volna egységes, modern irodalmi közvéleménnyé."
                    }
                ]
            },
            "words": [
                {"lemma": "nyelvújítás", "translation": "language reform / lexical renewal", "pos": "noun"},
                {"lemma": "levelezés", "translation": "correspondence (exchange of letters)", "pos": "noun"},
                {"lemma": "tájszó", "translation": "regional / dialect word", "pos": "noun"},
                {"lemma": "választékos", "translation": "refined / elegant / choice (of style)", "pos": "adjective"},
                {"lemma": "átdolgozás", "translation": "revision / reworking", "pos": "noun"},
                {"lemma": "beemelés", "translation": "incorporation / elevation into (the standard language)", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "nominalization-postposition-chains",
                "title": "Nominalization Chains with során, révén, and miatt",
                "text1_title": "Instrumentality and Process: révén and során",
                "text1": "To express HOW or DURING WHAT PROCESS a historical result was achieved, B2 Hungarian attaches postpositions like révén ('through / by means of'), során ('during / in the course of'), and miatt ('because of') to possessed -ás/-és nominalizations: az új kifejezések megalkotása révén ('through the creation of new expressions'), a kéziratok átdolgozása során ('in the course of revising the manuscripts').",
                "text2_title": "Double Possessive Nominalization Chains",
                "text2": "A nominalization can govern another possessed noun phrase in a three-element genitive chain: [a nemzet esztétikai ízlésének] [a nemesítése] ('the ennobling of the aesthetic taste of the nation'). Notice that the first inner possessor takes the dative-genitive suffix -nak/-nek when a second possessed head follows.",
                "table_title": "Complex Nominalization + Postposition Patterns",
                "table_rows": [
                    ["a mozgalomban való részvétele miatt", "because of his participation in the movement"],
                    ["az új szavak megalkotása révén", "by means of creating new words"],
                    ["a kéziratok átdolgozása során", "in the course of revising the manuscripts"],
                    ["a nemzet esztétikai ízlésének nemesítése", "the ennobling of the nation's aesthetic taste"]
                ],
                "examples": [
                    {
                        "spanish": "Kazinczy a fiatal tehetségek bátorítása és az új kifejezések megalkotása révén formálta az irodalmat.",
                        "english": "Kazinczy shaped literature by encouraging young talents and creating new expressions."
                    },
                    {
                        "spanish": "A jakobinus mozgalomban való részvétele miatt több mint hat évet töltött várbörtönben.",
                        "english": "Because of his participation in the Jacobin movement, he spent more than six years in fortress prisons."
                    }
                ],
                "tip": "When linking a case-marked complement (like mozgalomban) to a nominalized noun (részvétele), insert való ('being') between them: a mozgalomban való részvétele."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit értett Kazinczy Ferenc a 'fentebb stíl' fogalma alatt?",
                    "options": [
                        "A hétköznapi beszédnél választékosabb, zeneibb és esztétikailag igényesebb irodalmi kifejezésmódot.",
                        "A várbörtönök legfelső emeletén írt hivatalos kérvényeket.",
                        "A német nyelvű katonai parancsok szó szerinti fordítását."
                    ],
                    "correct": 0,
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Kazinczy a régi szavak felújítása mellett a vidéki _____ beemelését is támogatta a köznyelvbe. (dialect words - tájszavak)",
                    "answer": "tájszavak",
                    "english": "Alongside reviving old words, Kazinczy also supported incorporating regional dialect words into the standard language.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az új kifejezések tudatos megalkotása _____ a magyar nyelv alkalmassá vált a modern tudományok közvetítésére. (by means of / through - révén)",
                    "answer": "révén",
                    "english": "By means of the conscious creation of new expressions, the Hungarian language became suitable for conveying modern sciences.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban kapcsolódik helyesen a helyhatározós bővítmény ('a mozgalomban') a főnevesített alaptaghoz ('részvétele')?",
                    "options": [
                        "A jakobinus mozgalomban való részvétele miatt Kazinczy éveket töltött börtönben.",
                        "A jakobinus mozgalomban részvétele miatt Kazinczy éveket töltött börtönben.",
                        "A részvétele a jakobinus mozgalomban való miatt Kazinczy éveket töltött börtönben."
                    ],
                    "correct": 0,
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "kéziratok", "gondos", "átdolgozása", "során", "számos", "új", "kifejezés", "született."],
                    "solution": ["A", "kéziratok", "gondos", "átdolgozása", "során", "számos", "új", "kifejezés", "született."],
                    "english": "In the course of carefully revising the manuscripts, numerous new expressions were born.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan tudta Kazinczy Ferenc a távoli Széphalomról irányítani a magyar irodalmi életet?",
                    "options": [
                        "Hatalmas, több mint tizenhatezer levelet számláló levelezése révén, amely egyszemélyes akadémiaként működött.",
                        "Egy naponta megjelenő budapesti napilap főszerkesztőjeként.",
                        "A pozsonyi országgyűlés elnökeként hozott törvényekkel."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Kazinczy", "a", "választékos", "irodalmi", "stílus", "és", "a", "nyelvújítás", "mestere", "volt."],
                    "solution": ["Kazinczy", "a", "választékos", "irodalmi", "stílus", "és", "a", "nyelvújítás", "mestere", "volt."],
                    "english": "Kazinczy was the master of refined literary style and the Language Reform.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Explain how Kazinczy shaped Hungarian literature using two nominalizations + 'révén'.",
                            "answer": "Kazinczy a fiatal írók bátorítása és az új szavak megalkotása révén megújította a magyar irodalmi nyelvet."
                        },
                        {
                            "prompt": "Use 'a ...-ban/-ben való részvétel' in a sentence about historical involvement.",
                            "answer": "A nyelvújítási mozgalomban való aktív részvétel a korabeli értelmiség hazafias kötelességévé vált."
                        }
                    ],
                    "teaches": ["b2-nominalization-chains"]
                }
            ]
        },
        {
            "num": 3,
            "title": "Orthologists vs. Neologists: A Cultural War",
            "grammar_label": "Abstract noun derivations (-ság/-ség) and ideological nominalizations",
            "goals": [
                "I can explain the pamphlet war between the conservative Orthologists (Mondolat, 1813) and the modernist Neologists (Felelet a Mondolatra, 1815).",
                "I can form and inflect abstract nouns in -ság/-ség to express ideological concepts and qualities.",
                "I can analyze how Ferenc Kazinczy's 1819 essay forged a classic golden mean."
            ],
            "story_segment": {
                "seg_slug": "ortologusneologus",
                "title": "Ortológusok és neológusok szellemi háborúja",
                "summary": "The Language Reform sparked a fierce pamphlet war between conservative Orthologists (who published the satirical Mondolat in 1813) and Neologists (Kölcsey and Szemere's Felelet in 1815), resolved by Kazinczy's 1819 synthesis.",
                "location": "Debrecen, Pest és Széphalom",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1810-es évekre a nyelvújítás ügye országos szellemi háborúvá szélesedett. A vitázó felek két táborra oszlottak: az újítókat neológusoknak, a hagyományos nyelvszokás híveit pedig ortológusoknak nevezték. Az ortológusok — különösen a debreceni és dunántúli tudósok — nem magát az anyanyelv ápolását ellenezték, hanem a szabálytalanul megalkotott, németes szerkezetű vagy mesterkéltnek érzett szavakat utasították el."
                    },
                    {
                        "type": "narration",
                        "text": "A vita legélesebb fegyvere a gúnyirat lett. 1813-ban Somogyi Gedeon és társai kiadták a Mondolat című szatirikus füzetet, amelynek címlapján Kazinczyt szamáron ülve ábrázolták, szövegében pedig egyetlen mondatba sűrítették össze a neológusok legfurcsább szóalkotásait, hogy nevetségessé tegyék a mozgalmat."
                    },
                    {
                        "type": "narration",
                        "text": "A válasz nem váratott sokáig magára: 1815-ben Kölcsey Ferenc és Szemere Pál megjelentette a Felelet a Mondolatra című vitairatot. Míg a Mondolat az újítások túlzásait figurázta ki, addig a Felelet éles szellemességgel mutatta ki az ortológusok maradiságát és nehézkes, avítt kifejezésmódját."
                    },
                    {
                        "type": "narration",
                        "text": "A szenvedélyek lecsillapítására maga Kazinczy Ferenc vállalkozott 1819-ben megjelent, Ortológus és neológus nálunk és más nemzeteknél című klasszikus tanulmányában. Ebben a kiegyensúlyozott értekezésben leszögezte: minden élő nyelvnek egyszerre van szüksége a hagyományt védő óvatosságra és a fejlődést biztosító merészségre."
                    },
                    {
                        "type": "narration",
                        "text": "A történeti nyelvfejlődés végül igazolta ezt a bölcs középutat: a túlzó, mesterkélt szószörnyek kihullottak a használatból, a találó és kifejező új szavak ezrei viszont végleg beépültek a magyar köznyelvbe."
                    }
                ]
            },
            "words": [
                {"lemma": "gúnyirat", "translation": "lampoon / satirical pamphlet", "pos": "noun"},
                {"lemma": "maradiság", "translation": "backwardness / ultraconservatism", "pos": "noun"},
                {"lemma": "merészség", "translation": "boldness / audacity", "pos": "noun"},
                {"lemma": "középút", "translation": "middle way / golden mean", "pos": "noun"},
                {"lemma": "mesterkélt", "translation": "artificial / contrived / affected", "pos": "adjective"},
                {"lemma": "értekezés", "translation": "treatise / scholarly essay", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "abstract-nouns-sag-seg",
                "title": "Abstract Noun Derivations (-ság/-ség) in Ideological Discourse",
                "text1_title": "Deriving Abstract Qualities and Stances with -ság/-ség",
                "text1": "While -ás/-és nominalizes actions and processes (újítás 'innovation', fejlődés 'development'), the suffix -ság/-ség turns adjectives and nouns into abstract qualities, attitudes, or intellectual stances: óvatos -> óvatosság ('caution'), merész -> merészség ('boldness'), maradi -> maradiság ('backwardness'), szellemes -> szellemesség ('wit').",
                "text2_title": "Pairing -ság/-ség and -ás/-és in Balanced Argumentation",
                "text2": "In B2 essays like Kazinczy's 1819 treatise, -ság/-ség abstract nouns regularly pair with pre-nominal participial modifiers containing -ás/-és nouns: a hagyományt védő óvatosság ('caution protecting tradition') and a fejlődést biztosító merészség ('boldness ensuring development').",
                "table_title": "Adjective/Noun Base -> Abstract Quality (-ság/-ség)",
                "table_rows": [
                    ["óvatos (cautious) -> óvatosság", "a hagyományt védő óvatosság (caution protecting tradition)"],
                    ["merész (bold) -> merészség", "a fejlődést biztosító merészség (boldness ensuring progress)"],
                    ["maradi (hidebound) -> maradiság", "az ortológusok maradisága (the backwardness of the orthologists)"],
                    ["közérthető (intelligible) -> közérthetőség", "a nyelv közérthetősége (the intelligibility of the language)"]
                ],
                "examples": [
                    {
                        "spanish": "Minden élő nyelvnek egyszerre van szüksége a hagyományt védő óvatosságra és a fejlődést biztosító merészségre.",
                        "english": "Every living language simultaneously needs caution that protects tradition and boldness that ensures development."
                    },
                    {
                        "spanish": "Kölcsey és Szemere éles szellemességgel mutatta ki az ellenfelek maradiságát.",
                        "english": "Kölcsey and Szemere demonstrated the backwardness of their opponents with sharp wit."
                    }
                ],
                "tip": "Vowel harmony governs -ság (back vowels: óvatosság, maradiság, szabadság) vs. -ség (front vowels: merészség, szellemesség, közérthetőség)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi volt az 1813-ban megjelent 'Mondolat' című kiadvány?",
                    "options": [
                        "Az ortológusok szatirikus gúnyirata, amely a nyelvújítók túlzó szóalkotásait figurázta ki.",
                        "Az első magyar–angol műszaki szótár.",
                        "A pozsonyi országgyűlés hivatalos latin jegyzőkönyve."
                    ],
                    "correct": 0,
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A túlzó, _____ szóalkotások kihullottak a nyelvből, a találó szavak viszont megmaradtak. (artificial / contrived - mesterkélt)",
                    "answer": "mesterkélt",
                    "english": "The exaggerated, contrived coinages dropped out of the language, whereas the apt words remained.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Kazinczy szerint a nyelvfejlődéshez egyszerre van szükség óvatosságra és alkotói _____. (on boldness - merészségre)",
                    "answer": "merészségre",
                    "english": "According to Kazinczy, language development requires both caution and creative boldness.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik elvont főnév képzése helyes a 'közérthető' melléknévből?",
                    "options": [
                        "közérthetőség",
                        "közérthetőság",
                        "közérthetőés"
                    ],
                    "correct": 0,
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "hagyományt", "védő", "óvatosság", "és", "az", "újító", "merészség", "kiegyensúlyozta", "egymást."],
                    "solution": ["A", "hagyományt", "védő", "óvatosság", "és", "az", "újító", "merészség", "kiegyensúlyozta", "egymást."],
                    "english": "Caution protecting tradition and innovating boldness balanced each other.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen álláspontot képviselt Kazinczy Ferenc az 1819-es 'Ortológus és neológus' című értekezésében?",
                    "options": [
                        "A bölcs középutat: elismerte, hogy a nyelvnek a hagyományt védő óvatosságra és a fejlődést szolgáló újításra egyaránt szüksége van.",
                        "Azt követelte, hogy minden 1800 után alkotott új szót törvényileg tiltsanak be.",
                        "Kijelentette, hogy az ortológusoknak mindenben igazuk volt, és feloszlatta a mozgalmat."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Kölcsey", "és", "Szemere", "szellemes", "vitairatban", "felelt", "az", "ortológusok", "gúnyiratára."],
                    "solution": ["Kölcsey", "és", "Szemere", "szellemes", "vitairatban", "felelt", "az", "ortológusok", "gúnyiratára."],
                    "english": "Kölcsey and Szemere replied to the orthologists' lampoon in a witty polemical essay.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Summarize Kazinczy's 1819 synthesis using the abstract nouns 'óvatosság' and 'merészség'.",
                            "answer": "Kazinczy 1819-es értekezése kimutatta, hogy a hagyományt őrző óvatosság és az alkotói merészség együttesen gazdagítja a nyelvet."
                        },
                        {
                            "prompt": "Describe what happened to contrived words versus successful neologisms.",
                            "answer": "A mesterkélt szóalkotások feledésbe merültek, a kifejező új szavak használata viszont általánossá vált."
                        }
                    ],
                    "teaches": ["b2-nominalization-chains"]
                }
            ]
        },
        {
            "num": 4,
            "title": "Ten Thousand New Words We Speak Today",
            "grammar_label": "Morphological word-formation procedures and explanatory nominalizations",
            "goals": [
                "I can recognize the five major word-formation methods of the Hungarian Language Reform (derivation, compounding, back-formation, calques, and dialect revival).",
                "I can explain everyday Hungarian words coined during the Language Reform (anyag, állam, irodalom, művészet, társadalom, előfizet).",
                "I can use metalinguistic and morphological nominalizations to explain how words are constructed."
            ],
            "story_segment": {
                "seg_slug": "tizezerujszo",
                "title": "Tízezer új szó, amelyet ma is beszélünk",
                "summary": "From anyag ('matter', from anya 'mother'), irodalom ('literature'), and állam ('state') to back-formations like kapocs and árny, the Language Reformers shaped modern Hungarian vocabulary.",
                "location": "Pest és Debrecen (szótárműhelyek és nyomdák)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Ma egyetlen magyar mondatot sem tudnánk kimondani a nyelvújítók alkotásai nélkül. Amikor olyan mindennapi szavakat használunk, mint az anyag, az állam, a társadalom, az irodalom, a művészet, a rendőr, a hangverseny vagy a pincér, valójában a tizennyolcadik–tizenkilencedik századi írók és tudósok nyelvi leleményét szólaltatjuk meg."
                    },
                    {
                        "type": "narration",
                        "text": "A szókincs gazdagítása többféle tudatos szóalkotási eljárás alkalmazásával történt. A leggyakoribb módszer a szóképzés volt: az anya főnévből így született a latin materia megfelelőjeként az anyag, az ír igéből az irodalom, az áll igéből pedig az állam. Számos kifejezést szóösszetétellel vagy tükörfordítással alkottak meg: a német Konzert mintájára jött létre a hangverseny, a Bahnhof megfelelőjeként pedig a pályaudvar."
                    },
                    {
                        "type": "narration",
                        "text": "Különösen merész eljárásnak számított a szóelvonás, vagyis a meglévő hosszabb szavak megrövidítése. Az árnyék főnévből így vonták el a költőibb árny szót, a kapocsol igéből a kapocs főnevet, a lángol igéből pedig a dísz és a pír mintájára számos rövid, kifejező alapszót."
                    },
                    {
                        "type": "narration",
                        "text": "A természettudományok magyar szaknyelvének megteremtésében Bugát Pál orvosprofesszor és Schuster János játszott úttörő szerepet: nekik köszönhetjük többek között a vegytan, az izom, az ideg, a láz és a kórház szavakat. Ami néhány évtizeddel korábban még csak latinul volt megnevezhető, az az 1830-as évekre kristálytiszta magyar kifejezéssé vált."
                    },
                    {
                        "type": "narration",
                        "text": "Becslések szerint a nyelvújítás évtizedei alatt több mint tízezer új szó épült be tartósan a magyar nyelvbe — olyan sikeresen, hogy a mai beszélők többsége ősi szavaknak érzi őket."
                    }
                ]
            },
            "words": [
                {"lemma": "szóképzés", "translation": "word derivation (by suffixes)", "pos": "noun"},
                {"lemma": "szóösszetétel", "translation": "word compounding", "pos": "noun"},
                {"lemma": "szóelvonás", "translation": "back-formation / clipping", "pos": "noun"},
                {"lemma": "tükörfordítás", "translation": "calque / loan translation", "pos": "noun"},
                {"lemma": "szaknyelv", "translation": "technical / specialized terminology", "pos": "noun"},
                {"lemma": "megfelelő", "translation": "equivalent / counterpart", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "nominalization-word-formation",
                "title": "Metalinguistic Nominalizations: Explaining Word-Formation Processes",
                "text1_title": "Instrumental Process Phrases (-ás/-és + -val/-vel)",
                "text1": "When explaining how linguistic, scientific, or institutional innovations are carried out, Hungarian combines an -ás/-és nominalization with the instrumental suffix -val/-vel ('by / through the process of'): a meglévő szavak megrövidítésével ('by shortening existing words'), új képzők hozzáadásával ('by adding new derivational suffixes').",
                "text2_title": "Defining Terms with [Foreign Term] + magyar megfelelőjeként",
                "text2": "To explain why a term was coined, B2 expository Hungarian uses the essive-formal suffix -ként ('as') attached to the possessed noun megfelelője ('its equivalent'): a latin materia magyar megfelelőjeként született meg az anyag szó ('the word anyag was born as the Hungarian equivalent of the Latin materia').",
                "table_title": "Key Language Reform Coinages & Their Formation",
                "table_rows": [
                    ["anya (mother) -> anyag (matter/material)", "szóképzéssel (by suffix derivation)"],
                    ["árnyék (shadow) -> árny (shade)", "szóelvonással (by back-formation)"],
                    ["Konzert -> hang + verseny (hangverseny)", "tükörfordítással és szóösszetétellel (by calque & compounding)"],
                    ["a tudományos szaknyelv megteremtése", "the creation of scientific terminology"]
                ],
                "examples": [
                    {
                        "spanish": "Az árnyék főnévből szóelvonással, vagyis a szóvég megrövidítésével hozták létre az árny szót.",
                        "english": "From the noun árnyék they created the word árny by back-formation, that is, by shortening the end of the word."
                    },
                    {
                        "spanish": "Az anya főnévből a latin materia magyar megfelelőjeként született meg az anyag kifejezés.",
                        "english": "From the noun anya, the term anyag was born as the Hungarian equivalent of Latin materia."
                    }
                ],
                "tip": "Notice the contrast between szóképzés (adding a suffix: áll -> állam) and szóelvonás (removing an assumed suffix to create a shorter root: árnyék -> árny)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Melyik szóalkotási eljárással jött létre az 'árnyék' szóból a rövidebb 'árny' főnév?",
                    "options": [
                        "szóelvonással",
                        "szóösszetétellel",
                        "latin kölcsönzéssel"
                    ],
                    "correct": 0,
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A 'hangverseny' és a 'pályaudvar' szavakat idegen minták alapján _____ és szóösszetétellel alkották meg. (by loan translation / calque - tükörfordítással)",
                    "answer": "tükörfordítással",
                    "english": "The words 'hangverseny' (concert) and 'pályaudvar' (railway station) were coined by loan translation and compounding based on foreign models.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A meglévő hosszabb szavak _____ számos rövid, költői alapszó született a nyelvújítás idején. (by shortening of - megrövidítésével)",
                    "answer": "megrövidítésével",
                    "english": "By shortening existing longer words, numerous short, poetic root words were born during the Language Reform.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki nyelvtanilag pontosan az 'anyag' szó születését?",
                    "options": [
                        "Az anya főnévből a latin materia magyar megfelelőjeként született meg az anyag szó.",
                        "Az anya főnévből a latin materia magyar megfelelőként született meg az anyag szó.",
                        "Az anya főnévből a latin materia magyar megfelelője született megként az anyag szó."
                    ],
                    "correct": 0,
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Az", "orvosi", "szaknyelv", "megteremtésében", "Bugát", "Pál", "játszott", "úttörő", "szerepet."],
                    "solution": ["Az", "orvosi", "szaknyelv", "megteremtésében", "Bugát", "Pál", "játszott", "úttörő", "szerepet."],
                    "english": "Pál Bugát played a pioneering role in the creation of medical terminology.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik szópár köszönhető a magyar nyelvújításnak?",
                    "options": [
                        "anyag (az 'anya' szóból) és irodalom (az 'ír' igéből)",
                        "víz és tűz",
                        "kéz és láb"
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "nyelvújítók", "szóképzéssel", "és", "szóösszetétellel", "tízezer", "új", "szót", "alkottak."],
                    "solution": ["A", "nyelvújítók", "szóképzéssel", "és", "szóösszetétellel", "tízezer", "új", "szót", "alkottak."],
                    "english": "The language reformers created ten thousand new words through derivation and compounding.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Explain how the word 'anyag' or 'irodalom' was created using 'szóképzéssel' and 'megfelelőjeként'.",
                            "answer": "Az anyag szót az anya főnévből szóképzéssel hozták létre a latin materia magyar megfelelőjeként."
                        },
                        {
                            "prompt": "Explain the role of the Language Reform in creating scientific terminology ('a tudományos szaknyelv megteremtése').",
                            "answer": "A tudományos szaknyelv megteremtése lehetővé tette az orvostudomány és a jog oktatását magyar nyelven."
                        }
                    ],
                    "teaches": ["b2-nominalization-chains"]
                }
            ]
        },
        {
            "num": 5,
            "title": "1844: Hungarian Becomes the Language of State",
            "grammar_label": "Statutory and historical nominalization chains in constitutional prose",
            "goals": [
                "I can trace the institutional milestones from István Széchenyi's 1825 founding of the Academy to Act II of 1844 establishing Hungarian as the official state language.",
                "I can deploy statutory nominalization chains (elfogadásával, megalapítása révén, hatálybalépése után) in historical summaries.",
                "I can discuss institutional nation-building, parliamentary speeches, and linguistic sovereignty."
            ],
            "story_segment": {
                "seg_slug": "allamnyelv1844",
                "title": "1844: A magyar államnyelvvé válik",
                "summary": "From István Széchenyi's 1825 pledge founding the Hungarian Academy of Sciences in Pozsony to Act II of 1844, Hungarian replaced Latin as the official language of legislation, government, and education.",
                "location": "Pozsony (Országgyűlés) és Pest (Magyar Tudós Társaság)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az irodalmi nyelvújítás sikere megteremtette a feltételeket ahhoz, hogy a magyar nyelv a politikai és tudományos intézményekben is elfoglalja méltó helyét. A döntő fordulat az 1825. november harmadiki pozsonyi országgyűlésen következett be: amikor Felsőbüki Nagy Pál szenvedélyes beszédben sürgette a nemzeti nyelv védelmét, a fiatal gróf Széchenyi István felállt, és birtokainak egy teljes évi jövedelmét — hatvanezer forintot — ajánlotta fel egy Magyar Tudós Társaság megalapítására."
                    },
                    {
                        "type": "narration",
                        "text": "A mai Magyar Tudományos Akadémia elődjeként létrejött intézmény első feladata a magyar helyesírás szabályozása és a nagy akadémiai szótárak összeállítása volt. Vörösmarty Mihály, Czuczor Gergely és Fogarasi János munkája révén a nyelvújítás eredményei hivatalos tudományos rendszerré szilárdultak."
                    },
                    {
                        "type": "narration",
                        "text": "Eközben az országgyűléseken lépésről lépésre szorították vissza a latin nyelv kizárólagosságát. Előbb a magyar nyelvű jegyzőkönyvek vezetését és a törvények magyar szövegének hitelességét vívták ki, majd a reformellenzék — Kölcsey Ferenc, Deák Ferenc és Kossuth Lajos — kitartó küzdelme nyomán elérkezett az 1843–1844-es pozsonyi országgyűlés."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1844. évi II. törvénycikk elfogadásával végül lezárult a több mint fél évszázados küzdelem: a törvény kimondta, hogy Magyarországon a törvényhozás, a kormányzat, a bíráskodás és a közoktatás hivatalos államnyelve a magyar. Amikor az uralkodó szentesítette a törvényt, Pesten és szerte az országban fáklyás felvonulásokkal és színházi díszelőadásokkal ünnepelték a nyelvi szuverenitás kivívását."
                    },
                    {
                        "type": "narration",
                        "text": "Kazinczy Ferenc széphalmi dolgozószobájától a pozsonyi országgyűlésig így ívelt át az a páratlan szellemi mozgalom, amely bebizonyította: egy nyelv tudatos megújítása képes modern polgári nemzetet teremteni."
                    }
                ]
            },
            "words": [
                {"lemma": "államnyelv", "translation": "official state language", "pos": "noun"},
                {"lemma": "törvénycikk", "translation": "statutory article / act of parliament", "pos": "noun"},
                {"lemma": "jegyzőkönyv", "translation": "official minutes / parliamentary record", "pos": "noun"},
                {"lemma": "helyesírás", "translation": "orthography / spelling", "pos": "noun"},
                {"lemma": "felajánlás", "translation": "endowment / pledge / offering", "pos": "noun"},
                {"lemma": "megalapítás", "translation": "founding / establishment", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "statutory-nominalizations",
                "title": "Institutional & Statutory Nominalization Chains",
                "text1_title": "Milestone Phrases: elfogadásával and megalapítására",
                "text1": "In Hungarian constitutional and historical prose, turning points are expressed by attaching case endings (-val/-vel 'with/by', -ra/-re 'for the purpose of', -ig 'up until') directly to possessed -ás/-és nominalizations: az 1844. évi II. törvénycikk elfogadásával ('with the adoption of Act II of 1844'), a Magyar Tudós Társaság megalapítására ('for the founding of the Hungarian Learned Society').",
                "text2_title": "Synthesizing Nominalizations (-ás/-és) and Abstract Nouns (-ság/-ség)",
                "text2": "Notice how a single B2 historical sentence weaves both nominalization types seamlessly: a latin nyelv kizárólagosságának a visszaszorítása ('curbing the exclusivity of the Latin language') and a nyelvi szuverenitás kivívása ('achieving linguistic sovereignty').",
                "table_title": "Institutional & Constitutional Nominalization Chains",
                "table_rows": [
                    ["egy Magyar Tudós Társaság megalapítására", "for the founding of a Hungarian Learned Society"],
                    ["a magyar helyesírás szabályozása", "the regulation of Hungarian orthography"],
                    ["az 1844. évi II. törvénycikk elfogadásával", "with the adoption of Act II of 1844"],
                    ["a nyelvi szuverenitás kivívása", "the achievement of linguistic sovereignty"]
                ],
                "examples": [
                    {
                        "spanish": "Széchenyi István birtokainak egyévi jövedelmét ajánlotta fel a Magyar Tudós Társaság megalapítására.",
                        "english": "István Széchenyi offered one full year's income of his estates for the founding of the Hungarian Learned Society."
                    },
                    {
                        "spanish": "Az 1844. évi II. törvénycikk elfogadásával a magyar vált az ország hivatalos államnyelvévé.",
                        "english": "With the adoption of Act II of 1844, Hungarian became the country's official state language."
                    }
                ],
                "tip": "When an -ás/-és nominalization takes the sublative suffix -ra/-re after a 3rd-person possessive ending (-a/-e), the vowel lengthens to -á-/-é-: megalapítása -> megalapítására."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Melyik törvény mondta ki, hogy Magyarország hivatalos államnyelve a latin helyett a magyar?",
                    "options": [
                        "Az 1844. évi II. törvénycikk.",
                        "II. József 1784-es német nyelvrendelete.",
                        "Az 1813-as Mondolat című kiadvány."
                    ],
                    "correct": 0,
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A Magyar Tudós Társaság egyik legelső feladata az egységes magyar _____ szabályozása volt. (orthography / spelling - helyesírás)",
                    "answer": "helyesírás",
                    "english": "One of the very first tasks of the Hungarian Learned Society was the regulation of unified Hungarian orthography.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az 1844. évi II. törvénycikk _____ a magyar nyelv hivatalosan is államnyelvvé vált. (with the adoption of - elfogadásával)",
                    "answer": "elfogadásával",
                    "english": "With the adoption of Act II of 1844, the Hungarian language officially became the language of state.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki helyesen Széchenyi 1825-ös felajánlásának célját?",
                    "options": [
                        "Széchenyi István egyévi jövedelmét ajánlotta fel a Magyar Tudós Társaság megalapítására.",
                        "Széchenyi István egyévi jövedelmét ajánlotta fel a Magyar Tudós Társaság megalapításra.",
                        "Széchenyi István egyévi jövedelmét ajánlotta fel megalapítására a Magyar Tudós Társaságot."
                    ],
                    "correct": 0,
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "magyar", "helyesírás", "szabályozása", "az", "Akadémia", "első", "feladata", "volt."],
                    "solution": ["A", "magyar", "helyesírás", "szabályozása", "az", "Akadémia", "első", "feladata", "volt."],
                    "english": "The regulation of Hungarian orthography was the first task of the Academy.",
                    "teaches": ["b2-nominalization-chains"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mit tett gróf Széchenyi István az 1825. november 3-i pozsonyi országgyűlésen?",
                    "options": [
                        "Birtokainak egy teljes évi jövedelmét (hatvanezer forintot) ajánlotta fel a Magyar Tudós Társaság megalapítására.",
                        "Javasolta, hogy a latin maradjon az országgyűlés nyelve még száz évig.",
                        "Megírta a Mondolat című gúnyiratot Kazinczy Ferenc ellen."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Az", "országgyűlés", "jegyzőkönyveit", "és", "a", "törvénycikkeket", "1844-től", "magyarul", "írták."],
                    "solution": ["Az", "országgyűlés", "jegyzőkönyveit", "és", "a", "törvénycikkeket", "1844-től", "magyarul", "írták."],
                    "english": "From 1844 onward, the minutes of the Diet and the statutory articles were written in Hungarian.",
                    "teaches": ["b2-nyelvujitas-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence about the 1825 founding of the Academy using 'megalapítására' and 'felajánlás'.",
                            "answer": "Széchenyi István nagylelkű felajánlása a Magyar Tudós Társaság megalapítására új korszakot nyitott a tudományban."
                        },
                        {
                            "prompt": "Summarize the significance of 1844 using 'az 1844. évi II. törvénycikk elfogadásával'.",
                            "answer": "Az 1844. évi II. törvénycikk elfogadásával a magyar nyelv a törvényhozás és a közoktatás hivatalos államnyelve lett."
                        }
                    ],
                    "teaches": ["b2-nominalization-chains"]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can recount the history of the Hungarian Language Reform from 1784 to 1844 with accurate cultural and linguistic terminology.",
            "I can construct possessive and postpositional nominalization chains (-ás/-és) fluently.",
            "I can form and deploy abstract nouns (-ság/-ség) in analytical and historical prose."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szóalkotási módszerrel jött létre az 'anya' szóból az 'anyag', illetve az 'ír' igéből az 'irodalom'?",
                "options": ["szóképzéssel", "szóelvonással", "betűszóval", "idézéssel"],
                "correct": 0,
                "teaches": ["b2-nyelvujitas-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat tartalmaz nyelvtanilag hibátlan főnevesített birtokos szerkezetet?",
                "options": [
                    "A magyar szókincs tudatos bővítése lehetővé tette a tudományok anyanyelvi művelését.",
                    "A magyar szókincset tudatos bővítés lehetővé tette a tudományok anyanyelvi művelését.",
                    "A tudatos bővítése a magyar szókincs lehetővé tette a tudományok művelését."
                ],
                "correct": 0,
                "teaches": ["b2-nominalization-chains"]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik évben vált a magyar nyelv hivatalos államnyelvvé a Magyar Királyságban?",
                "options": ["1844-ben", "1784-ben", "1813-ban", "1908-ban"],
                "correct": 0,
                "teaches": ["b2-nyelvujitas-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az 1813-as Mondolat című _____ szamáron ülve ábrázolta Kazinczy Ferencet. (satirical lampoon - gúnyirat)",
                "answer": "gúnyirat",
                "english": "The 1813 satirical lampoon titled Mondolat depicted Ferenc Kazinczy sitting on a donkey.",
                "teaches": ["b2-nyelvujitas-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az új szavak megalkotása _____ a magyar nyelv alkalmassá vált a modern filozófia kifejezésére. (by means of - révén)",
                "answer": "révén",
                "english": "By means of creating new words, the Hungarian language became suitable for expressing modern philosophy.",
                "teaches": ["b2-nominalization-chains"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nyelv fejlődéséhez a hagyományt védő óvatosságra és az újító _____ egyaránt szükség van. (on boldness - merészségre)",
                "answer": "merészségre",
                "english": "For the development of the language, caution protecting tradition and innovating boldness are equally needed.",
                "teaches": ["b2-nominalization-chains"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "1844.", "évi", "törvénycikk", "elfogadásával", "a", "magyar", "hivatalos", "államnyelvvé", "vált."],
                "solution": ["Az", "1844.", "évi", "törvénycikk", "elfogadásával", "a", "magyar", "hivatalos", "államnyelvvé", "vált."],
                "english": "With the adoption of the statutory article of 1844, Hungarian became the official state language.",
                "teaches": ["b2-nominalization-chains"]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Kazinczy", "Ferenc", "Széphalomról", "irányította", "a", "magyar", "nyelvújítás", "országos", "mozgalmát."],
                "solution": ["Kazinczy", "Ferenc", "Széphalomról", "irányította", "a", "magyar", "nyelvújítás", "országos", "mozgalmát."],
                "english": "Ferenc Kazinczy directed the nationwide movement of the Hungarian Language Reform from Széphalom.",
                "teaches": ["b2-nyelvujitas-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szerkezet fejezi ki helyesen: 'because of his participation in the movement'?",
                "options": [
                    "a mozgalomban való részvétele miatt",
                    "a mozgalomban részvétele miatt",
                    "a mozgalom való részvétele miatt"
                ],
                "correct": 0,
                "teaches": ["b2-nominalization-chains"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tudományos", "szaknyelv", "megteremtése", "és", "a", "helyesírás", "szabályozása", "sikeres", "volt."],
                "solution": ["A", "tudományos", "szaknyelv", "megteremtése", "és", "a", "helyesírás", "szabályozása", "sikeres", "volt."],
                "english": "The creation of scientific terminology and the regulation of orthography were successful.",
                "teaches": ["b2-nominalization-chains"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Describe how the Language Reform enriched Hungarian using two '-ás/-és' nominalizations with '-val/-vel'.",
                        "answer": "A nyelvújítók régi szavak felújításával és új kifejezések megalkotásával tízezer szóval gazdagították a magyar nyelvet."
                    }
                ],
                "teaches": ["b2-nominalization-chains"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explain the path from Széphalom to 1844 using 'megalapítása' and 'elfogadásával'.",
                        "answer": "A Magyar Tudós Társaság megalapítása után az 1844-es törvénycikk elfogadásával a magyar végleg az ország hivatalos államnyelve lett."
                    }
                ],
                "teaches": ["b2-nominalization-chains"]
            }
        ]
    }
}


def main():
    build_culture_unit(UNIT_1_KAVEHAZIKULTURA)
    build_culture_unit(UNIT_2_SZECESSZIO)
    build_culture_unit(UNIT_3_NYELVUJITAS)
    print("Successfully generated Hungarian B2 Culture Units 1, 2, and 3.")


if __name__ == "__main__":
    main()
