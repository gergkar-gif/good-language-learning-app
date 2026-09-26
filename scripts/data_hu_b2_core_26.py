#!/usr/bin/env python3
"""
Hungarian B2 Core Unit 26: Pluralism, Heritage & Minority Perspectives
Grammar skill: b2-reciprocal-distributive
Vocab skill: b2-26-vocab
"""
from helpers_hu_b2_exercises import mc, match, fb, sb, dc, sw

UNIT_26 = {
    "unit_num": 26,
    "title": "Pluralism, Heritage & Minority Perspectives",
    "grammar_summary": "Reciprocal postpositions and case-marked pronouns (egymás iránt, egymással szemben, egymás mellett, egymásból), distributive morphology with -onként/-enként/-önként (egyenként, csoportonként, nemzetiségenként, fejenként), and intercultural discourse framing.",
    "grammar_skill": "b2-reciprocal-distributive",
    "vocab_skill": "b2-26-vocab",
    "theme": "Pluralism, heritage and minority perspectives",
    "intro_body": [
        "A Kárpát-medence történelme a sokszínű kultúrák, nyelvek és felekezetek évszázados együttélésének szövete. A kölcsönös tisztelet, a kisebbségi jogok védelme és a kulturális autonómia nem csupán jogi kategóriák, hanem a mindennapi társadalmi béke elengedhetetlen feltételei. A különböző közösségek egymás mellett élése gazdag nyelvi és gondolkodásbeli mintázatokat teremtett.",
        "Ebben a fejezetben elsajátíthatja a kölcsönös viszonyokat kifejező névmási és névutós szerkezeteket (egymás iránt, egymással szemben, egymás mellett), a disztributív határozók és képzők használatát (egyenként, csoportonként, nemzetiségenként), valamint az interkulturális párbeszéd és emlékezetpolitika árnyalt kifejezéstárát. Kertész Imre megrázó remekműve, a 'Sorstalanság' nyomán pedig az emberi méltóság és a személyes felelősség egyetemes kérdéseit tárhatja fel.",
    ],
    "classic_story": {
        "slug": "sorstalansag",
        "author": "Kertész Imre",
        "work": "Sorstalanság (1975)",
        "title": "Szembenézés a történelemmel és az emberi méltóság",
        "summary": "Köves Gyuri hazatérése a koncentrációs táborokból a háború utáni budapesti bérházba: megrázó párbeszéd az idős szomszéddal a sorsról, a személyes döntésekről és az emberi méltóság megtartásáról az abszurditásban.",
        "characters": ["Köves Gyuri", "A szomszéd"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A pesti bérház udvarán a nyári délután porlepte csendje honolt. Köves Gyuri lassan lépkedett fel a körfolyosó kopott lépcsőin, bőrönd nélkül, a viseltes zubbonyban, amely még mindig magán viselte a táborok keserű porát.",
            },
            {
                "type": "narration",
                "text": "A harmadik emeleti fordulóban hirtelen kinyílt a folyosó ajtaja. Steiner úr, az egykori szomszéd lépett ki a gangra; tekintete megakadt a fiú beesett arcán, és a felismerés pillanatában a megdöbbenés zavart hallgatássá dermedt az arcán.",
            },
            {
                "type": "dialogue",
                "speaker": "A szomszéd",
                "text": "Gyuri! Hát te vagy az, valóban hazatértél? Istenem, miféle borzalmakon mehettél keresztül... De most már vége van, fiam. Most már el kell felejteni mindent, mintha csak egy szörnyű természeti csapás lett volna, amelyből szerencsésen megmenekültél.",
            },
            {
                "type": "dialogue",
                "speaker": "Köves Gyuri",
                "text": "Nem lehet elfelejteni, Steiner úr. És nem is természeti csapás volt. A természeti csapások maguktól jönnek, mint a villám vagy a földrengés. De ott emberek cselekedtek egymással szemben; minden egyes lépést emberek tettek meg egyenként, parancsra vagy megszokásból.",
            },
            {
                "type": "dialogue",
                "speaker": "A szomszéd",
                "text": "De értsd meg, senki sem tehetett róla! A vak végzet, a történelem vihara sodorta el az embereket. Hogyan lehet egyáltalán élni ezzel a teherrel, ha nem a felejtést választjuk?",
            },
            {
                "type": "dialogue",
                "speaker": "Köves Gyuri",
                "text": "Ha a sorsot okoljuk mindenért, akkor lemondunk a szabadságunkról. A lágerben is létezett az emberi méltóság; még a legnehezebb percekben is volt választásunk egymás iránt, még ha csupán egy darab kenyér megosztásáról vagy egy csendes gesztusról volt is szó. Nem a végzet volt elkerülhetetlen, hanem a mi saját lépéseink következtek egymásból.",
            },
            {
                "type": "dialogue",
                "speaker": "A szomszéd",
                "text": "Különös fiú vagy te, Gyuri... Úgy beszélsz a múltról, mintha nem áldozatként, hanem a saját életed bírájaként tekintenél vissza mindenre.",
            },
            {
                "type": "narration",
                "text": "Gyuri nem válaszolt mindjárt; odalépett a körfolyosó korlátjához, és lenézett a belső udvarra, ahol a napfény éles geometriai sávokat rajzolt a kövezetre. Tudta, hogy az igazi megmaradás nem a múlt letagadásában, hanem a tisztánlátásban és az emberi felelősség bátor vállalásában rejlik.",
            },
        ],
        "reading_questions": [
            {
                "question": "Miért utasítja el Köves Gyuri azt a nézetet, hogy a lágerek világa természeti csapáshoz hasonlított?",
                "options": [
                    "Mert az események tudatos emberi cselekedetek és döntések láncolatából fakadtak egymással szemben.",
                    "Mert a természeti csapások sokkal nagyobb anyagi kárt okoztak volna a városban.",
                    "Mert a táborokban mindennap esett az eső a foglyok beszámolói szerint.",
                ],
                "correct": 0,
            },
            {
                "question": "Hogyan értelmezi Gyuri a saját lépéseit és a sors fogalmát?",
                "options": [
                    "Úgy véli, hogy a vak végzet helyett az ember személyes döntései és egymás iránti lépései alakítják a történetet.",
                    "Úgy gondolja, hogy semmilyen választása nem volt, és teljes apátiába kell süllyednie.",
                    "Azt állítja, hogy mindenért kizárólag a szomszédok közötti anyagi vita volt a felelős.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen etikai tanulságot fogalmaz meg a regényrészlet az emberi méltóságról?",
                "options": [
                    "A méltóság lényege a legnehezebb körülmények között is megőrzött döntési szabadság és a felelősség vállalása.",
                    "A méltóság csak akkor létezik, ha az ember teljesen elfelejti a múlt nehézségeit.",
                    "A méltóságot kizárólag a katonai győzelem és a fizikai erő határozza meg.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Toward and Against Each Other (egymás iránt, egymással szemben)",
            "grammar_label": "Reciprocal case-marked phrases (egymás iránt, egymással szemben, egymás mellett)",
            "goals": [
                "I can express reciprocal sentiments and attitudes using egymás iránt",
                "I can articulate mutual opposition, parity, or bilateral stances with egymással szemben",
                "I can describe physical and cultural proximity using egymás mellett and egymásból",
            ],
            "grammar_doc": {
                "slug": "reciprocal-postpositional-phrases",
                "title": "Reciprocal Pronouns and Postpositions: egymás iránt, egymással szemben",
                "text1_title": "Reciprocal Attitudes and Orientations: egymás iránt",
                "text1": "The reciprocal pronoun 'egymás' ('each other / one another') combines with oblique case suffixes and postpositions to express bilateral social and psychological relations. When paired with 'iránt' ('toward / regarding'), it conveys emotional, moral, or ethical orientation: 'A különböző nemzetiségek tisztelettel viseltetnek egymás iránt' ('The different nationalities bear respect toward one another'); 'kölcsönös szolidaritás egymás iránt' ('mutual solidarity toward one another').",
                "text2_title": "Opposition, Contrast, and Adjacency: egymással szemben and egymás mellett",
                "text2": "'Egymással szemben' denotes bilateral confrontation, competing legal obligations, or reciprocal expectations: 'A felek kötelezettségeket vállalnak egymással szemben' ('The parties undertake obligations vis-à-vis each other'); 'előítéletek egymással szemben' ('prejudices against one another'). Meanwhile, 'egymás mellett' ('side by side') expresses spatial coexistence and harmonious diversity: 'Évszázadok óta élnek békében egymás mellett' ('They have lived peacefully side by side for centuries').",
                "table_title": "Reciprocal Case-Marked and Postpositional Patterns",
                "table_rows": [
                    ["egymás iránt", "felelősség egymás iránt (responsibility toward one another)"],
                    ["egymással szemben", "követelmények egymással szemben (claims / demands against each other)"],
                    ["egymás mellett", "békés együttélés egymás mellett (peaceful coexistence side by side)"],
                    ["egymásból", "a lépések egymásból következnek (the steps follow from one another)"],
                ],
                "examples": [
                    {
                        "spanish": "A közösség tagjai mély bizalmat és szolidaritást éreznek egymás iránt.",
                        "english": "The members of the community feel deep trust and solidarity toward one another.",
                    },
                    {
                        "spanish": "A tárgyaló felek tiszteletben tartották az egymással szemben fennálló kötelezettségeiket.",
                        "english": "The negotiating parties respected their obligations existing vis-à-vis each other.",
                    },
                    {
                        "spanish": "A Kárpát-medencében magyarok, szászok és románok évszázadokig éltek egymás mellett.",
                        "english": "In the Carpathian Basin, Hungarians, Saxons, and Romanians lived side by side for centuries.",
                    },
                    {
                        "spanish": "A párbeszéd során felismerték, hogy problémáik közvetlenül egymásból fakadnak.",
                        "english": "During the dialogue, they recognized that their problems stemmed directly from one another.",
                    },
                ],
                "tip": "Pay close attention to case agreement: 'egymás iránt' requires the bare stem of 'egymás' because 'iránt' is a postposition, whereas 'egymással szemben' requires the instrumental suffix -val/-vel on 'egymás' before the postposition 'szemben'.",
            },
            "words": [
                {"lemma": "egymás iránt", "translation": "toward one another / mutual", "pos": "expression"},
                {"lemma": "egymással szemben", "translation": "against one another / vis-à-vis each other", "pos": "expression"},
                {"lemma": "egymás mellett", "translation": "side by side / next to each other", "pos": "expression"},
                {"lemma": "kölcsönösség", "translation": "reciprocity / mutual exchange", "pos": "noun"},
                {"lemma": "szolidaritás", "translation": "solidarity", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the meaning of 'kölcsönösség' in sociological and diplomatic relations?",
                        [
                            "reciprocity and mutual balance of rights and commitments between parties",
                            "a financial loan given with high interest rates",
                            "a unilateral declaration without response from the counterpart",
                        ],
                        0,
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which reciprocal phrase means 'side by side / in harmonious coexistence'?",
                        ["egymás mellett", "egymás nélkül", "egymás helyett"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["egymás iránt", "toward one another"],
                            ["egymással szemben", "vis-à-vis each other"],
                            ["egymás mellett", "side by side"],
                            ["kölcsönösség", "reciprocity"],
                            ["szolidaritás", "solidarity"],
                        ],
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which reciprocal phrase best fits: 'A békés közösségek mély tiszteletet tanúsítanak ____'?",
                        ["egymás iránt", "egymásról", "egymásért"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the phrase expressing mutual claims or reciprocal opposition:",
                        ["egymással szemben", "egymás alatt", "egymás után"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A különböző felekezetek békésen éltek évszázadokon át ____ a történelmi városban. (side by side)",
                        "egymás mellett",
                        "The different denominations lived peacefully side by side for centuries in the historic town.",
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A válság idején az állampolgárok valódi szolidaritást mutattak ____. (toward one another)",
                        "egymás iránt",
                        "During the crisis, citizens demonstrated genuine solidarity toward one another.",
                        ["b2-reciprocal-distributive"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "két", "nemzet", "bizalmat", "épített", "ki", "egymás", "iránt."],
                        ["A", "két", "nemzet", "bizalmat", "épített", "ki", "egymás", "iránt."],
                        "The two nations built trust toward one another.",
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A nemzetközi szerződés a teljes ____ elvén alapul. (reciprocity)",
                        "kölcsönösség",
                        "The international treaty is founded on the principle of full reciprocity.",
                        ["b2-26-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "társadalmi", "szolidaritás", "megerősíti", "a", "közösségek", "összetartozását."],
                        ["A", "társadalmi", "szolidaritás", "megerősíti", "a", "közösségek", "összetartozását."],
                        "Social solidarity strengthens the cohesion of communities.",
                        ["b2-26-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Szociológus", "text": "Hogyan javítható a többségi és kisebbségi közösségek kapcsolata?"},
                            {"speaker": "Kutató", "text": "____"},
                        ],
                        [
                            "Az egymás iránti tisztelet elmélyítésével és a kölcsönös előítéletek lebontásával.",
                            "Úgy, ha a felek soha többé nem találkoznak és nem beszélnek egymással.",
                            "Mivel senki sem felelős semmiért, ezért felesleges tenni bármit is.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Moderátor", "text": "Milyen elvárásokat fogalmaztak meg a partnerek a kerekasztalnál?"},
                            {"speaker": "Résztvevő", "text": "____"},
                        ],
                        [
                            "Világos kötelezettségeket rögzítettek egymással szemben a kulturális autonómia biztosítására.",
                            "Mindenki csak magára gondolt, és azonnal elhagyta a tárgyalótermet.",
                            "Egymás mellett állva nem mondtak semmit, mert senki sem tudott magyarul.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'egymás iránt' describing inter-ethnic solidarity.",
                                "answer": "A soknemzetiségű településeken a lakók őszinte felelősséget éreznek egymás iránt a nehéz időkben.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'egymás mellett' describing multi-cultural coexistence.",
                                "answer": "Különböző vallási és nyelvi hagyományok élnek békében egymás mellett a régióban.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A vitás kérdések rendezése során a felek nem ellenségesen léptek fel ____. (against one another / vis-à-vis each other)",
                        "egymással szemben",
                        "During the settlement of disputed issues, the parties did not act hostilely against one another.",
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes mutual support and ethical cohesion among members of a society?",
                        ["szolidaritás", "elkülönülés", "távolságtartás"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Group by Group: Distributive Syntax (egyenként, csoportonként)",
            "grammar_label": "Distributive syntax (-onként/-enként/-önként and distributive numerals)",
            "goals": [
                "I can form distributive adverbs using -onként/-enként/-önként with nouns and numerals",
                "I can express unit-by-unit and per-capita distributions (egyenként, fejenként, csoportonként)",
                "I can structure sociological comparisons broken down by community or cohort",
            ],
            "grammar_doc": {
                "slug": "distributive-morphology-and-syntax",
                "title": "Distributive Suffixes: -onként, -enként, -önként",
                "text1_title": "Morphological Distribution: Unit by Unit and Cohort by Cohort",
                "text1": "Hungarian expresses distribution across individuals, entities, or temporal units using the productive suffix '-onként / -enként / -önként'. When suffixed to the numeral 'egy', it produces 'egyenként' ('one by one / individually'): 'A szakértők egyenként vizsgálták meg a kérelmeket' ('The experts examined the applications one by one'). Attached to collective nouns, it breaks demographic analysis down group by group: 'csoportonként' ('by groups'), 'nemzetiségenként' ('nationality by nationality'), 'családonként' ('family by family').",
                "text2_title": "Quantitative, Per-Capita, and Temporal Allocation",
                "text2": "The distributive suffix is foundational in public policy, budgeting, and sociological reporting. 'Fejenként' ('per capita / per head') allocates quotas or subsidies per person: 'fejenként tízezer forint támogatás' ('ten thousand forints subsidy per head'). When suffixed to nouns of frequency or occasion, it specifies intermittent or episodic occurrence: 'esetenként' ('case by case / on occasion'), 'időnként' ('from time to time'), 'naponként' ('daily / per day').",
                "table_title": "Productive Distributive Formations",
                "table_rows": [
                    ["egyenként", "egyenként meghallgatni a tanúkat (to hear the witnesses one by one)"],
                    ["csoportonként", "csoportonként értékelni az eredményeket (to evaluate results group by group)"],
                    ["nemzetiségenként", "nemzetiségenként vezetett statisztikák (statistics kept by nationality)"],
                    ["fejenként", "fejenként járó kulturális normatíva (cultural per-capita subsidy allowance)"],
                ],
                "examples": [
                    {
                        "spanish": "A bizottság tagjai egyenként szavaztak a módosító javaslatokról.",
                        "english": "The committee members voted one by one on the amendment proposals.",
                    },
                    {
                        "spanish": "A kutatók csoportonként elemezték a diákok nyelvi kompetenciáit.",
                        "english": "The researchers analyzed the students' linguistic competencies group by group.",
                    },
                    {
                        "spanish": "A támogatási összeget nemzetiségenként és régiónként arányosan osztották szét.",
                        "english": "The subsidy funds were distributed proportionately by nationality and by region.",
                    },
                    {
                        "spanish": "A kulturális programokra fejenként meghatározott költségvetési keret áll rendelkezésre.",
                        "english": "A budgetary quota determined per capita is available for cultural programs.",
                    },
                ],
                "tip": "Vowel harmony applies systematically: back vowels take '-onként' (falunként, házanként), front unrounded take '-enként' (fejenként, népenként), and front rounded take '-önként' (községenként, körönként).",
            },
            "words": [
                {"lemma": "egyenként", "translation": "one by one / individually", "pos": "adverb"},
                {"lemma": "csoportonként", "translation": "group by group / by groups", "pos": "adverb"},
                {"lemma": "nemzetiségenként", "translation": "nationality by nationality", "pos": "adverb"},
                {"lemma": "fejenként", "translation": "per head / per capita", "pos": "adverb"},
                {"lemma": "esetenként", "translation": "case by case / occasionally", "pos": "adverb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the meaning of the distributive adverb 'fejenként'?",
                        [
                            "per person / per capita allocation",
                            "turning one's head toward the speaker",
                            "a collective fine imposed on an entire village",
                        ],
                        0,
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adverb means 'individually / one by one'?",
                        ["egyenként", "együtt", "egyszerre"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["egyenként", "one by one / individually"],
                            ["csoportonként", "group by group"],
                            ["nemzetiségenként", "nationality by nationality"],
                            ["fejenként", "per capita / per head"],
                            ["esetenként", "case by case / occasionally"],
                        ],
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which distributive suffix attaches to the noun 'község' (front rounded vowel)?",
                        ["-önként (községenként)", "-onként (községonként)", "-an (községan)"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the adverb expressing data categorized by national minority:",
                        ["nemzetiségenként", "nemzetiségből", "nemzetiségért"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A felvételizőket ____ hívták be a terembe a szóbeli vizsgára. (one by one)",
                        "egyenként",
                        "The applicants were called into the room one by one for the oral examination.",
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A támogatást az iskolákban tanuló diákok száma szerint, ____ határozták meg. (per head / per capita)",
                        "fejenként",
                        "The subsidy was determined per capita according to the number of students studying in the schools.",
                        ["b2-reciprocal-distributive"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "résztvevőket", "csoportonként", "osztották", "be", "a", "műhelymunkára."],
                        ["A", "résztvevőket", "csoportonként", "osztották", "be", "a", "műhelymunkára."],
                        "The participants were assigned group by group to the workshops.",
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A népszámlálási adatokat nemcsak régiónként, hanem ____ is közzétették. (nationality by nationality)",
                        "nemzetiségenként",
                        "The census data were published not only by region, but also nationality by nationality.",
                        ["b2-26-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "szabályoktól", "eltérő", "kérelmeket", "esetenként", "bírálják", "el."],
                        ["A", "szabályoktól", "eltérő", "kérelmeket", "esetenként", "bírálják", "el."],
                        "Applications departing from the rules are evaluated case by case.",
                        ["b2-26-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kutatásvezető", "text": "Hogyan dolgozzuk fel a kérdőíves felmérés eredményeit?"},
                            {"speaker": "Adatelemző", "text": "____"},
                        ],
                        [
                            "Érdemes az adatokat korosztályonként és nemzetiségenként külön-külön összegezni az összehasonlíthatóság végett.",
                            "Dobjuk ki az összes kérdőívet, mert túl sok betű van rajtuk.",
                            "Minden adatot egyetlen halomba öntünk anélkül, hogy csoportosítanánk.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Pályázati referens", "text": "Mekkora összeg jut az anyanyelvi tankönyvtámogatásra?"},
                            {"speaker": "Pénzügyi vezető", "text": "____"},
                        ],
                        [
                            "A költségvetés fejenként húszezer forint normatív támogatást biztosít minden jogosult diáknak.",
                            "Egyáltalán nincs pénz, mert a tankönyvek feleslegesek az iskolában.",
                            "Egyenként megkérjük a diákokat, hogy kézzel másolják le a könyvtárat.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'egyenként' describing individual examination of heritage artifacts.",
                                "answer": "A restaurátorok egyenként vizsgálták át a múzeumba beérkezett néprajzi tárgyakat.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence with 'nemzetiségenként' detailing cultural funding allocation.",
                                "answer": "A kulturális minisztérium nemzetiségenként elkülönített pénzügyi keretet biztosít az anyanyelvi színházaknak.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A rendkívüli jogorvoslati kérelmeket a minisztérium egyedi mérlegelés alapján, ____ vizsgálja felül. (case by case)",
                        "esetenként",
                        "The ministry reviews extraordinary legal remedy requests based on individual discretion, case by case.",
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adverb means dividing or analyzing population cohorts broken down by ethnic/national group?",
                        ["nemzetiségenként", "folyamatosan", "véletlenül"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Shared Spaces, Distinct Traditions",
            "grammar_label": "Minority cultural autonomy and multiethnic coexistence",
            "goals": [
                "I can discuss institutional autonomy and minority self-governance",
                "I can describe parallel cultural traditions coexisting in shared geographic space",
                "I can analyze linguistic preservation and community self-determination",
            ],
            "grammar_doc": {
                "slug": "minority-autonomy-and-coexistence",
                "title": "Minority Cultural Autonomy: Shared Spaces and Distinct Traditions",
                "text1_title": "Cultural Autonomy and Institutional Self-Governance",
                "text1": "In Hungarian political and constitutional thought, the preservation of national minorities relies on the concept of cultural autonomy ('kulturális autonómia'). Under the Nationalities Act, recognized nationalities exercise local and national self-governance ('nemzetiségi önkormányzatiság'), operating their own schools, theatres, and libraries. This framework ensures that linguistic communities govern their cultural heritage autonomously within the wider sovereign state.",
                "text2_title": "Tradition Keeping and Coexistence: hagyományőrzés and együttélés",
                "text2": "Multiethnic communities in regions like Baranya, Békés, or the Bakony celebrate historical coexistence ('békés együttélés') while nurturing distinct customs through active preservation of folklore and language ('hagyományőrzés'). In expository analysis, reciprocal verbs and compound nouns express these dual dynamics: 'A közösségek megőrzik sajátos identitásukat, miközben gazdagítják a közös hazát' ('The communities preserve their distinct identity while enriching the common homeland').",
                "table_title": "Key Terminology for Cultural Diversity",
                "table_rows": [
                    ["kulturális autonómia", "a közösség joga saját intézményeinek önálló irányítására (right of community to self-direct institutions)"],
                    ["nemzetiségi önkormányzat", "választott testület a kisebbségi jogok gyakorlására (elected body exercising minority rights)"],
                    ["hagyományőrzés", "az anyanyelv, a szokások és a népi kultúra ápolása (preservation of mother tongue, customs, and folk culture)"],
                    ["békés együttélés", "különböző kultúrák harmonikus közös élete (harmonious shared life of diverse cultures)"],
                ],
                "examples": [
                    {
                        "spanish": "A kulturális autonómia révén a nemzetiségek maguk dönthetnek az iskoláik működéséről.",
                        "english": "Through cultural autonomy, nationalities can decide themselves on the operation of their schools.",
                    },
                    {
                        "spanish": "A sváb és szlovák falvakban a hagyományőrzés nem csupán nosztalgia, hanem élő valóság.",
                        "english": "In Swabian and Slovak villages, the preservation of traditions is not merely nostalgia, but living reality.",
                    },
                    {
                        "spanish": "Az évszázados együttélés során a népszokások és a konyhaművészet kölcsönösen gazdagították egymást.",
                        "english": "In the course of centuries-old coexistence, folk customs and gastronomy mutually enriched one another.",
                    },
                    {
                        "spanish": "A nemzetiségi önkormányzatiság rendszere biztosítja a kisebbségi érdekek intézményes védelmét.",
                        "english": "The system of nationality self-governance guarantees the institutional protection of minority interests.",
                    },
                ],
                "tip": "In official terminology, Hungarian uses 'nemzetiség' (nationality / national minority) rather than 'kisebbség' (minority) when referring to the 13 constitutionally recognized historical nationalities (e.g. németség, romák, szlovákok, horvátok).",
            },
            "words": [
                {"lemma": "kulturális autonómia", "translation": "cultural autonomy", "pos": "expression"},
                {"lemma": "nemzetiség", "translation": "national minority / nationality", "pos": "noun"},
                {"lemma": "együttélés", "translation": "coexistence", "pos": "noun"},
                {"lemma": "hagyományőrzés", "translation": "preservation of traditions", "pos": "noun"},
                {"lemma": "önkormányzatiság", "translation": "self-governance / local autonomy", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'kulturális autonómia' in Hungarian public law?",
                        [
                            "the institutional right of a minority to independently manage its educational and cultural affairs",
                            "a total geographic separation of ethnic groups into gated communities",
                            "the complete prohibition of teaching minority languages in public schools",
                        ],
                        0,
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which noun denotes the active safeguarding of ancestral folk customs, songs, and language?",
                        ["hagyományőrzés", "hagyatéki eljárás", "újítás"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["kulturális autonómia", "cultural autonomy"],
                            ["nemzetiség", "national minority / nationality"],
                            ["együttélés", "coexistence"],
                            ["hagyományőrzés", "preservation of traditions"],
                            ["önkormányzatiság", "self-governance"],
                        ],
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which body represents the educational and cultural interests of historical nationalities in Hungary?",
                        ["a nemzetiségi önkormányzat", "a kereskedelmi kamara", "a sporthivatal"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the best expression for centuries of harmonious multi-ethnic life in a shared region:",
                        ["békés együttélés", "zárt elkülönülés", "egyoldalú lemondás"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A helyi közösségek kiemelt figyelmet fordítanak a sváb népszokások ____. (to the preservation of traditions)",
                        "hagyományőrzésére",
                        "Local communities pay highlighted attention to the preservation of Swabian folk customs.",
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A törvény elismeri a tizenhárom honos ____ saját identitáshoz való jogát. (national minority; accusative/possessive: nemzetiség)",
                        "nemzetiség",
                        "The law recognizes the right of the thirteen native nationalities to their own identity.",
                        ["b2-reciprocal-distributive"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "kulturális", "autonómia", "megerősíti", "a", "kisebbségek", "megmaradását."],
                        ["A", "kulturális", "autonómia", "megerősíti", "a", "kisebbségek", "megmaradását."],
                        "Cultural autonomy strengthens the preservation of minorities.",
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A sokszínű régióban a harmonikus ____ évszázados hagyományokra tekint vissza. (coexistence)",
                        "együttélés",
                        "In the diverse region, harmonious coexistence looks back on centuries-old traditions.",
                        ["b2-26-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "nemzetiségi", "önkormányzatiság", "intézményes", "védelmet", "biztosít", "mindenkinek."],
                        ["A", "nemzetiségi", "önkormányzatiság", "intézményes", "védelmet", "biztosít", "mindenkinek."],
                        "Nationality self-governance provides institutional protection for everyone.",
                        ["b2-26-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Polgármester", "text": "Hogyan támogatja a város a helyi nemzetiségi közösségeket?"},
                            {"speaker": "Kulturális alpolgármester", "text": "____"},
                        ],
                        [
                            "Biztosítjuk a kulturális autonómia feltételeit és támogatjuk a kétnyelvű iskolák hagyományőrző munkáját.",
                            "Semmit sem teszünk, mert mindenki beszéljen csak egyetlen nyelven.",
                            "Az együttélés helyett elrendeltük a nemzetiségi egyesületek azonnali bezárását.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Egyetemi hallgató", "text": "Milyen szerepet töltenek be a nemzetiségi önkormányzatok?"},
                            {"speaker": "Oktató", "text": "____"},
                        ],
                        [
                            "Közvetlen döntési jogkörrel rendelkeznek saját kulturális és oktatási intézményeik irányításában.",
                            "Kizárólag adókat szednek be és nem szerveznek semmilyen programot.",
                            "Nem csinálnak semmit, mert az önkormányzatiság csupán papíron létezik.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'kulturális autonómia' asserting educational rights for minorities.",
                                "answer": "A nemzetiségek kulturális autonómiája garanciát nyújt a saját anyanyelvi iskolarendszer fenntartására.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'együttélés' and 'hagyományőrzés' regarding regional heritage.",
                                "answer": "A békés együttélés évszázadai alatt a hagyományőrzés szervesen beépült a térség közös kulturális örökségébe.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A Kárpát-medencei népek több évszázados ____ gazdag és sokszínű folklórt eredményezett. (coexistence)",
                        "együttélése",
                        "The centuries-long coexistence of Carpathian Basin peoples resulted in rich and diverse folklore.",
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which institutional term describes local minority representation with authority over cultural affairs?",
                        ["nemzetiségi önkormányzatiság", "központi vámhivatal", "bírósági végrehajtás"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Memory, Dignity, and Testimony",
            "grammar_label": "Expressing historical witness, collective identity, and human dignity",
            "goals": [
                "I can articulate historical witness and moral testimony (tanúságtétel)",
                "I can discuss inalienable human dignity in the face of totalitarian violence (emberi méltóság)",
                "I can analyze collective remembrance and reconciliation (történelmi emlékezet, megbékélés)",
            ],
            "grammar_doc": {
                "slug": "memory-dignity-and-testimony",
                "title": "Historical Memory, Human Dignity, and Moral Testimony",
                "text1_title": "Inalienable Dignity: emberi méltóság and tanúságtétel",
                "text1": "Post-war Hungarian literature and philosophy, epitomized by Kertész Imre and Pilinszky János, redefined human dignity ('emberi méltóság') not as an abstract philosophical ideal, but as a lived ethical stance under catastrophic conditions. Bearing witness ('tanúságtétel') rejects false heroics or sentimentality, insisting on precise, uncompromising truth-telling: 'A tanúságtétel célja nem a vádaskodás, hanem az igazság felmutatása az eljövendő nemzedékek számára' ('The aim of testimony is not recrimination, but holding up the truth for future generations').",
                "text2_title": "Collective Memory and Reconciliation: történelmi emlékezet and megbékélés",
                "text2": "Confronting dark chapters of history requires active collective memory ('történelmi emlékezet') rather than collective amnesia. True reconciliation ('megbékélés') between communities cannot occur by glossing over historical trauma or minimizing victims ('áldozatok'), but by creating shared spaces of remembrance where reciprocal accountability is acknowledged without hatred.",
                "table_title": "Ethical and Commemorative Terms",
                "table_rows": [
                    ["emberi méltóság", "minden embert megillető elidegeníthetetlen érték (inalienable value due to every human)"],
                    ["tanúságtétel", "a megtapasztalt igazság hiteles elmondása (authentic narration of experienced truth / bearing witness)"],
                    ["történelmi emlékezet", "egy társadalom közös tudása a múlt sorsfordulóiról (society's shared knowledge of historical turns)"],
                    ["megbékélés", "a történelmi sebek őszinte feldolgozása (sincere processing of historical wounds / reconciliation)"],
                ],
                "examples": [
                    {
                        "spanish": "Az emberi méltóság tiszteletben tartása minden demokratikus rend abszolút alapköve.",
                        "english": "Respect for human dignity is the absolute cornerstone of every democratic order.",
                    },
                    {
                        "spanish": "A túlélők tanúságtétele nélkül a történelmi emlékezet hiányos és sebezhető maradna.",
                        "english": "Without the testimony of survivors, historical memory would remain incomplete and vulnerable.",
                    },
                    {
                        "spanish": "A valódi megbékélés csak a múlt tényeivel való bátor szembenézés árán érhető el.",
                        "english": "Genuine reconciliation can only be achieved at the price of courageously confronting the facts of the past.",
                    },
                    {
                        "spanish": "A múzeum méltó emléket állít az üldöztetések és háborúk ártatlan áldozatainak.",
                        "english": "The museum erects a worthy memorial to the innocent victims of persecutions and wars.",
                    },
                ],
                "tip": "Distinguish between 'áldozat' as victim of violence or injustice, and 'áldozatvállalás' (willing self-sacrifice or altruistic exertion on behalf of others).",
            },
            "words": [
                {"lemma": "emberi méltóság", "translation": "human dignity", "pos": "expression"},
                {"lemma": "tanúságtétel", "translation": "bearing witness / testimony", "pos": "noun"},
                {"lemma": "történelmi emlékezet", "translation": "historical memory", "pos": "expression"},
                {"lemma": "megbékélés", "translation": "reconciliation", "pos": "noun"},
                {"lemma": "áldozat", "translation": "victim / sacrifice", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the philosophical and constitutional meaning of 'emberi méltóság'?",
                        [
                            "the inherent, inalienable worth of every human being that must never be violated",
                            "a prestigious title awarded to military commanders after retirement",
                            "a ceremonial dress worn by aristocrats during parliamentary openings",
                        ],
                        0,
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the moral act of giving voice to experienced historical trauma?",
                        ["tanúságtétel", "szóbeszéd", "hallgatás"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["emberi méltóság", "human dignity"],
                            ["tanúságtétel", "bearing witness / testimony"],
                            ["történelmi emlékezet", "historical memory"],
                            ["megbékélés", "reconciliation"],
                            ["áldozat", "victim / sacrifice"],
                        ],
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which phrase denotes a society's collective awareness of its traumatic past?",
                        ["a történelmi emlékezet", "a napi hírfolyam", "a gazdasági ciklus"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What is essential for genuine historical reconciliation ('megbékélés') between nations?",
                        [
                            "Sincere confrontation with historical facts and reciprocal empathy toward all victims.",
                            "The complete erasure of history textbooks from school curricula.",
                            "Demanding monetary compensation without any dialogue.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A túlélő író megrázó műve nem pusztán regény, hanem etikai ____ is egyben. (bearing witness / testimony)",
                        "tanúságtétel",
                        "The survivor writer's moving work is not merely a novel, but an ethical testimony as well.",
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A totalitárius rendszerek legfőbb célja az ____ megtörése és a személyiség elpusztítása volt. (human dignity; possessive: emberi méltóság)",
                        "emberi méltóság",
                        "The primary goal of totalitarian regimes was the breaking of human dignity and the destruction of personality.",
                        ["b2-reciprocal-distributive"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "történelmi", "emlékezet", "megóvása", "minden", "nemzedék", "kötelessége."],
                        ["A", "történelmi", "emlékezet", "megóvása", "minden", "nemzedék", "kötelessége."],
                        "Preserving historical memory is the duty of every generation.",
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A háborúk ártatlan ____ emlékére országszerte emlékhelyeket hoztak létre. (victims)",
                        "áldozatainak",
                        "In memory of the innocent victims of wars, memorials were established nationwide.",
                        ["b2-26-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Az", "őszinte", "párbeszéd", "nélkülözhetetlen", "a", "népek", "megbékéléséhez."],
                        ["Az", "őszinte", "párbeszéd", "nélkülözhetetlen", "a", "népek", "megbékéléséhez."],
                        "Sincere dialogue is indispensable for the reconciliation of peoples.",
                        ["b2-26-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Történész", "text": "Hogyan segítheti az irodalom a traumák feldolgozását?"},
                            {"speaker": "Író", "text": "____"},
                        ],
                        [
                            "A hiteles tanúságtétel által, amely visszaadja az áldozatok emberi méltóságát és gazdagítja a történelmi emlékezetet.",
                            "Úgy, ha vidám meséket találunk ki a háborúkról, hogy senki se szomorkodjon.",
                            "Az irodalom nem segíthet semmit, mert az emberek csak a televíziót nézik.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Konferencia-elnök", "text": "Milyen feltételei vannak a szomszédos népek megbékélésének?"},
                            {"speaker": "Kutató", "text": "____"},
                        ],
                        [
                            "Az egymással szembeni múltbeli sérelmek őszinte feltárása és a közös áldozatok kölcsönös tisztelete.",
                            "A határátkelők azonnali lezárása és a kapcsolatok teljes megszakítása.",
                            "A megbékéléshez elég egy hivatalos pecsét, beszélgetni nem szükséges.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'emberi méltóság' asserting unassailable rights in ethics.",
                                "answer": "Az emberi méltóságot semmilyen ideológia vagy politikai hatalom nevében nem lehet lábbal tiporni.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'tanúságtétel' and 'történelmi emlékezet'.",
                                "answer": "A túlélők bátor tanúságtétele nélkülözhetetlen támasza a nemzet történelmi emlékezetének.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A megrázó kiállítás célja a múlttal való szembenézés és a nemzetek közötti ____ előmozdítása. (reconciliation)",
                        "megbékélés",
                        "The goal of the moving exhibition is confronting the past and promoting reconciliation among nations.",
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes the moral record and shared narrative of a community's historical past?",
                        ["történelmi emlékezet", "gazdasági előrejelzés", "időjárás-jelentés"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Facilitating Intercultural Dialogue",
            "grammar_label": "Synthesizing reciprocal constructions in intercultural communication",
            "goals": [
                "I can moderate multi-perspective discussions on diversity, prejudice, and inclusion",
                "I can integrate reciprocal postpositions and distributive markers in nuanced dialogue",
                "I can advocate constructive bridge-building among diverse cultural communities",
            ],
            "grammar_doc": {
                "slug": "facilitating-intercultural-dialogue",
                "title": "Intercultural Dialogue, Mediation, and Bridge-Building",
                "text1_title": "Dismantling Prejudices: előítélet and párbeszéd",
                "text1": "Constructive intercultural communication requires creating spaces for structured dialogue ('párbeszéd') aimed at dismantling deep-rooted prejudices ('előítéletek lebontása'). In Hungarian public discourse, syntactic reciprocity plays a crucial role: participants move from defending stances 'egymással szemben' to fostering understanding 'egymás iránt', recognizing that stereotypes arise when communities talk about each other rather than to each other.",
                "text2_title": "Mediation and Bridge-Building: közvetítés and hídépítés",
                "text2": "Community mediation ('közvetítés') seeks balance between cultural preservation and broader societal integration ('társadalmi integráció'). Metaphorical idioms like 'hídépítés' ('bridge-building') capture civic initiatives that unite disparate ethnic or social groups. Distributive syntax (-onként/-enként) ensures fair institutional representation across all stakeholder cohorts: 'településenként és közösségenként szervezett találkozók' ('gatherings organized by settlement and by community').",
                "table_title": "Intercultural and Mediation Concepts",
                "table_rows": [
                    ["párbeszéd", "kölcsönös meghallgatáson alapuló eszmecsere (constructive exchange based on mutual listening)"],
                    ["előítélet", "tényeken nem alapuló, merev negatív megítélés (rigid negative judgment not based on facts)"],
                    ["közvetítés", "pártatlan segítségnyújtás viták feloldására (impartial facilitation to resolve disputes / mediation)"],
                    ["hídépítés", "kapcsolatok teremtése különböző csoportok között (fostering ties between distinct groups / bridge-building)"],
                ],
                "examples": [
                    {
                        "spanish": "Az őszinte párbeszéd az egyetlen hatékony eszköz az előítéletek felszámolására.",
                        "english": "Sincere dialogue is the only effective tool for the dismantling of prejudices.",
                    },
                    {
                        "spanish": "A civil szervezetek sikeres közvetítést végeztek a többségi és kisebbségi lakosok között.",
                        "english": "Civil organizations performed successful mediation between majority and minority residents.",
                    },
                    {
                        "spanish": "A kulturális fesztivál igazi hídépítés volt a szomszédos nemzetiségek között.",
                        "english": "The cultural festival was a true bridge-building between neighboring nationalities.",
                    },
                    {
                        "spanish": "A társadalmi integráció előfeltétele az egyenlő esélyek és a méltóság garantálása.",
                        "english": "The prerequisite of social integration is guaranteeing equal opportunities and dignity.",
                    },
                ],
                "tip": "When moderating intercultural exchanges, pair reciprocal pronouns with purposive connectors: 'azért ültek asztalhoz, hogy megértsék egymás nézőpontját' ('they sat at the table in order to understand each other's perspective').",
            },
            "words": [
                {"lemma": "párbeszéd", "translation": "dialogue / conversation", "pos": "noun"},
                {"lemma": "előítélet", "translation": "prejudice / bias", "pos": "noun"},
                {"lemma": "közvetítés", "translation": "mediation / facilitation", "pos": "noun"},
                {"lemma": "hídépítés", "translation": "bridge-building / fostering ties", "pos": "noun"},
                {"lemma": "társadalmi integráció", "translation": "social integration", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the meaning of 'előítélet' in sociological psychology?",
                        [
                            "a preconceived, unfounded opinion or bias held toward a group or individual",
                            "an official court ruling issued before the final trial",
                            "a preliminary exam score in an academic course",
                        ],
                        0,
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which metaphorical compound refers to fostering ties and trust across divided communities?",
                        ["hídépítés", "falbontás", "árokásás"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["párbeszéd", "dialogue / conversation"],
                            ["előítélet", "prejudice / bias"],
                            ["közvetítés", "mediation / facilitation"],
                            ["hídépítés", "bridge-building"],
                            ["társadalmi integráció", "social integration"],
                        ],
                        ["b2-26-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which phrase denotes neutral facilitation aimed at resolving inter-community conflict?",
                        ["pártatlan közvetítés", "katonai beavatkozás", "egyoldalú ultimátum"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the best expression for overcoming social fragmentation and ensuring equal participation:",
                        ["társadalmi integráció", "teljes asszimiláció", "elszigetelődés"],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A kerekasztal-konferencia célja az őszinte interkulturális ____ megindítása volt. (dialogue)",
                        "párbeszéd",
                        "The goal of the round-table conference was initiating sincere intercultural dialogue.",
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A független szakértők sikeres ____ folytattak a vitás felek között a békés megállapodásért. (mediation)",
                        "közvetítést",
                        "The independent experts conducted successful mediation between the disputing parties for a peaceful agreement.",
                        ["b2-reciprocal-distributive"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "közös", "kulturális", "programok", "lebontják", "a", "makacs", "előítéleteket."],
                        ["A", "közös", "kulturális", "programok", "lebontják", "a", "makacs", "előítéleteket."],
                        "Joint cultural programs dismantle stubborn prejudices.",
                        ["b2-reciprocal-distributive"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A színházi társulat munkája valódi ____ jelentett a többségi és kisebbségi fiatalok között. (bridge-building)",
                        "hídépítést",
                        "The work of the theatre troupe represented true bridge-building between majority and minority youth.",
                        ["b2-26-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "sikeres", "társadalmi", "integráció", "kölcsönös", "erőfeszítést", "követel", "mindenkitől."],
                        ["A", "sikeres", "társadalmi", "integráció", "kölcsönös", "erőfeszítést", "követel", "mindenkitől."],
                        "Successful social integration demands mutual effort from everyone.",
                        ["b2-26-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Közösségszervező", "text": "Hogyan lehet fellépni a mélyen gyökerező sztereotípiák ellen?"},
                            {"speaker": "Tréner", "text": "____"},
                        ],
                        [
                            "Személyes találkozásokkal és strukturált párbeszéddel, amely lehetővé teszi egymás tapasztalatainak megismerését.",
                            "Úgy, ha betiltjuk a beszélgetést és mindenki otthon marad a lakásában.",
                            "Előítéletek nélkül az élet unalmas lenne, ezért nem kell változtatni semmin.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Önkormányzati képviselő", "text": "Milyen eredményt hozott a mediációs fórum?"},
                            {"speaker": "Mediátor", "text": "____"},
                        ],
                        [
                            "A felek elismerték egymás igényeit, és közös bizottságot hoztak létre a viták megelőzésére.",
                            "A felek még jobban összevesztek és feljelentették egymást a bíróságon.",
                            "Nem történt semmi, mert senki sem figyelt a másikra.",
                        ],
                        0,
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'párbeszéd' and 'előítélet' urging constructive civic interaction.",
                                "answer": "Kizárólag a folyamatos és nyílt párbeszéd képes felszámolni a generációk óta öröklődő előítéleteket.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'hídépítés' describing inter-cultural educational programs.",
                                "answer": "A kétnyelvű iskolai projektek a valódi hídépítés mintapéldái a térség nemzetiségei között.",
                            }
                        ],
                        ["b2-reciprocal-distributive"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A civil szervezet legfőbb célkitűzése a hátrányos helyzetű fiatalok zökkenőmentes ____. (social integration; possessive: társadalmi integráció)",
                        "társadalmi integrációja",
                        "The primary objective of the civil organization is the seamless social integration of disadvantaged youth.",
                        ["b2-reciprocal-distributive"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes structured, mutual exchange aimed at overcoming estrangement?",
                        ["párbeszéd", "monológ", "parancs"],
                        0,
                        ["b2-26-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can master reciprocal case-marked phrases and postpositions (egymás iránt, egymással szemben, egymás mellett)",
            "I can systematically apply distributive morphology with -onként/-enként/-önként across sociological contexts",
            "I can articulate nuanced positions on cultural autonomy, historical testimony, and inter-ethnic bridge-building",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["kölcsönösség", "reciprocity"],
                    ["egyenként", "one by one / individually"],
                    ["kulturális autonómia", "cultural autonomy"],
                    ["emberi méltóság", "human dignity"],
                    ["párbeszéd", "dialogue"],
                ],
                ["b2-26-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'nemzetiségenként' mean in public statistics and cultural policy?",
                [
                    "analyzed or distributed broken down by each recognized national minority group",
                    "without regard to national or ethnic background",
                    "exclusively within the national capital city",
                ],
                0,
                ["b2-26-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly illustrates reciprocal attitude using 'egymás iránt'?",
                [
                    "A közösség tagjai mély felelősséget és empátiát éreznek egymás iránt.",
                    "A közösség tagjai egymás iránt mentek a boltba kenyeret venni.",
                    "Egymás iránt volt a tegnapi eső, ezért nem mentünk ki a szabadba.",
                ],
                0,
                ["b2-reciprocal-distributive"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A kulturális fesztivál valódi ____ bizonyult a különböző anyanyelvű lakosok között. (bridge-building)",
                "hídépítésnek",
                "The cultural festival proved to be true bridge-building between residents of different mother tongues.",
                ["b2-26-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A két szomszédos nép évszázadokon keresztül élt békében ____ a határvidéken. (side by side)",
                "egymás mellett",
                "The two neighboring peoples lived peacefully side by side for centuries in the border region.",
                ["b2-reciprocal-distributive"],
            ),
            fb(
                "grammar",
                "recall",
                "A pályázati támogatást a regisztrált résztvevők száma alapján, ____ számolták ki. (per capita / per head)",
                "fejenként",
                "The grant funding was calculated per capita on the basis of the number of registered participants.",
                ["b2-reciprocal-distributive"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'egymással szemben' correctly expresses reciprocal obligations:",
                [
                    "A nemzetiségi önkormányzat és a városvezetés világos kötelezettségeket vállalt egymással szemben.",
                    "A két ház egymással szemben sétált a parkban tegnap délelőtt.",
                    "Egymással szemben ették meg a reggelit a madarak a fán.",
                ],
                0,
                ["b2-reciprocal-distributive"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Emlékezetpolitikai szakértő", "text": "Hogyan szolgálja a múlt feltárása a jövő társadalmi békéjét?"},
                    {"speaker": "Történész", "text": "____"},
                ],
                [
                    "A túlélők tanúságtétele és az emberi méltóság tisztelete révén, amely elengedhetetlen a népek őszinte megbékéléséhez.",
                    "Úgy, ha teljesen elfelejtjük a történelmet, és nem tartunk semmilyen megemlékezést.",
                    "A múlt vitái helyett inkább mindenki foglalkozzon a saját kertjével.",
                ],
                0,
                ["b2-reciprocal-distributive"],
            ),
            mc(
                "grammar",
                "in-context",
                "Why is 'csoportonként' preferred over 'csoportban' in: 'A diákokat ____ értékelték'?",
                [
                    "Because the distributive suffix -onként conveys sequential and comparative evaluation broken down cohort by cohort.",
                    "Because 'csoportban' can only be used with singular subjects in Hungarian.",
                    "Because 'csoportonként' is an archaic legal term used only in official courts.",
                ],
                0,
                ["b2-reciprocal-distributive"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "történelmi", "együttélés", "során", "a", "kultúrák", "kölcsönösen", "gazdagították", "egymást."],
                ["A", "történelmi", "együttélés", "során", "a", "kultúrák", "kölcsönösen", "gazdagították", "egymást."],
                "In the course of historical coexistence, cultures mutually enriched each other.",
                ["b2-reciprocal-distributive"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "bizottság", "egyenként", "vizsgálta", "meg", "a", "nemzetiségi", "panaszokat."],
                ["A", "bizottság", "egyenként", "vizsgálta", "meg", "a", "nemzetiségi", "panaszokat."],
                "The committee examined the minority complaints one by one.",
                ["b2-reciprocal-distributive"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause essay statement combining 'egymás iránt' (reciprocal respect), 'nemzetiségenként' (distributive allocation), and 'emberi méltóság' (human dignity).",
                        "answer": "Bár a kulturális támogatásokat nemzetiségenként elkülönítve osztják el, a közösségek mély tiszteletet tanúsítanak egymás iránt; hiszen a sokszínű társadalom legfőbb alapértéke az emberi méltóság maradéktalan védelme.",
                    }
                ],
                ["b2-reciprocal-distributive"],
            ),
        ],
    },
}
