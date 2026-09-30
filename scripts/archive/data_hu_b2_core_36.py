"""
Hungarian B2 Core Track Unit 36:
  b2-36: Mastery & Voice: Upper-Intermediate Synthesis
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_36 = {
    "unit_num": 36,
    "title": "Mastery & Voice: Upper-Intermediate Synthesis",
    "grammar_summary": "Full B2 communicative synthesis: information structure, left-branching participial compression, nominalization, diplomatic hedging, literary comprehension, and sovereign rhetorical voice.",
    "grammar_skill": "b2-mastery-synthesis",
    "vocab_skill": "b2-36-vocab",
    "theme": "Mastery, voice and upper-intermediate synthesis",
    "intro_body": [
        "A B2 szintű nyelvtudás csúcsa nem pusztán a nyelvtani szabályok hibátlan ismerete, hanem a saját kifejező hang megtalálása, az árnyalt gondolatok elegáns közvetítése és a stíluseszközök magabiztos uralása. A magyar nyelv rendkívül érzékeny a hangsúlyra, a szórendre, az igeneves sűrítésre és a szövegkohéziós elemek finom hálójára.",
        "Ebben a zárófejezetben szintetizáljuk az eddig elsajátított magas szintű szintaktikai és pragmatikai eszközöket: a topik-fókusz architektúrát, a balra ágazó igeneves szerkezeteket, a diplomáciai tompítást és a nyilvános vita retorikáját. A fejezet végén Kosztolányi Dezső Esti Kornéljának híres utazásán keresztül hódolunk a nyelv csodájának, mielőtt megalkotná saját, szuverén B2 záróbeszédét és esszéjét.",
    ],
    "classic_story": {
        "slug": "estikornel",
        "author": "Kosztolányi Dezső",
        "work": "Esti Kornél kalandjai (1933)",
        "title": "A nyelv csodája és a szabad szellem utazásai",
        "summary": "Esti Kornél és az író a zakatoló éjszakai vonaton az anyanyelv páratlan zeneiségéről, a fordítás elérhetetlen pontosságáról és a szavak varázsáról cserélnek eszmét, miközben a vonat új európai tájak felé repíti őket.",
        "characters": ["Esti Kornél", "Az író"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A nemzetközi gyorsvonat fülkéjében tompa sárga fény derengett, miközben a kerekek egyenletes ritmusban kattogtak a síneken. Odakint a közép-európai síkság sötétje suhant el az ablak előtt; a fülkében csak ketten ültek: Esti Kornél, az örök vándor és szellemi kalandor, valamint barátja, az író.",
            },
            {
                "type": "dialogue",
                "speaker": "Esti Kornél",
                "text": "Nézd ezt a zakatolást! Olyan, mint egy jambikus versritmus. Mindig elbűvöl, hogy az emberi nyelv miként képes a világ nyers zűrzavarából tiszta zenét és kristálytiszta gondolatot teremteni.",
            },
            {
                "type": "dialogue",
                "speaker": "Az író",
                "text": "Gyakran eltűnődöm azon, Kornél, hogy vajon megértheti-e egy idegen a mi nyelvünk legbensőbb titkait. Azokat a finom hangsúlyeltolódásokat és rejtett árnyalatokat, amelyeket csak az anyatejjel szív magába az ember.",
            },
            {
                "type": "dialogue",
                "speaker": "Esti Kornél",
                "text": "Megértheti, ha nem csupán a szabályokat tanulja, hanem felfedezi a nyelv lelkét! A magyar nyelvben a szórend nem börtön, hanem végtelen szabadság: ahová a fókuszt helyezed, ott gyúlsz világot a mondatban. Minden mondat egy kis dráma.",
            },
            {
                "type": "narration",
                "text": "Az író kinyitotta noteszát, és a rázkódó asztalkán lejegyzett néhány sort. Felidézte magában Kosztolányi híres hitvallását: a szavak nem egyszerű használati tárgyak, hanem ékszerek, amelyeknek súlya, színe, illata és történelmi emlékezete van.",
            },
            {
                "type": "dialogue",
                "speaker": "Az író",
                "text": "És mi a helyzet az idegen nyelvekkel? Te, aki tucatnyi nyelven beszélsz, nem érzed néha a fordítás fájdalmas elégtelenségét?",
            },
            {
                "type": "dialogue",
                "speaker": "Esti Kornél",
                "text": "A fordítás csodálatos hűtlenség. Egy másik nyelven megszólalni olyan, mint új életet kezdeni: másképp látod a világot, más hangsúlyokat keresel. De a valódi nyelvi mesterség ott kezdődik, amikor rátalálsz a saját egyéni hangodra, és azon a hangon szólalsz meg szabadon.",
            },
            {
                "type": "narration",
                "text": "A vonat lassan lefékezett egy határállomáson. A gőz fehér felhőkben gomolygott az ablak előtt a hideg éjszakában; Kornél rámosolygott barátjára, felállt, és a fülke ablakát lehúzva mélyen beszívta a friss hajnali levegőt. Tudta, hogy a határok csupán térképeken léteznek: a nyelv és a szabad szellem szárnyalása előtt nincsenek akadályok.",
            },
        ],
        "reading_questions": [
            {
                "question": "Hogyan értelmezi Esti Kornél a magyar szórend és fókusz szerepét a fülkében folytatott beszélgetésben?",
                "options": [
                    "A szabad kifejezés eszközeként, ahol a fókusz áthelyezése új fényt és dramaturgiát ad a mondatnak.",
                    "Merev és szigorú korlátként, amely tilt minden egyéni stílust.",
                    "A német nyelvből átvett mechanikus szerkezetként.",
                ],
                "correct": 0,
            },
            {
                "question": "Mit tart Esti Kornél a valódi nyelvi mesterség legfőbb ismérvének?",
                "options": [
                    "A puszta szabályokon túl a saját autentikus egyéni hang megtalálását és a szabad megszólalást.",
                    "Az összes idegen szó azonnali kitörlését a szótárakból.",
                    "Kizárólag a hivatalos jogi kifejezések hibátlan memorizálását.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen metaforával jellemzi a szöveg a fordítás természetét?",
                "options": [
                    "Csodálatos kísérletként és új életként, amely más perspektívát nyit a világra.",
                    "Felesleges és káros időpocsékolásként.",
                    "Egy matematikai gépezet automatikus kalkulációjaként.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Synthesizing Focus, Word Order, and Register in Authentic Prose",
            "grammar_label": "Advanced synthesis of Hungarian information structure: topic-focus dynamics, preverbal stress, and register harmony",
            "goals": [
                "I can master topic-focus inversion to highlight precise informational elements in complex sentences",
                "I can vary preverbal stress and word order to create rhythmic, natural Hungarian prose",
                "I can align informational prominence with appropriate stylistic registers",
            ],
            "grammar_doc": {
                "slug": "synthesizing-focus-word-order-register",
                "title": "Synthesizing Focus, Word Order, and Register in Authentic Prose",
                "text1_title": "The Architectural Core of Hungarian Syntax: Topic and Focus",
                "text1": "Hungarian sentence structure is fundamentally discourse-configurational: linear word order is governed not by grammatical relations (subject-verb-object) but by communicative function. The sentence begins with the Topic (topik) – the shared context or framework of the assertion. Immediately preceding the conjugated finite verb is the structural Focus Position (fókuszpozíció), which receives primary sentence stress and identifies exhaustive identification ('Péter érkezett meg tegnap, nem János').",
                "text2_title": "Preverbal Stress and Focus-Induced Inversion",
                "text2": "When an argument moves into the preverbal focus position, the verbal preverb (igekötő) is systematically displaced behind the verb: 'János tegnap megérkezett' (neutral topic statement) versus 'János TEGNAP érkezett meg' (exhaustive temporal focus). Mastering B2 prose requires handling these subtle shifts of emphasis ('hangsúlyeltolódás') to control the reader's attention and imbue written Hungarian with natural cadence and persuasive force.",
                "table_title": "Topic-Focus Inversion and Stress Contrasts",
                "table_rows": [
                    ["Semleges közlés (Topic + Verb)", "A professzor elolvasta a tanulmányt. (The professor read the study.)"],
                    ["Alanyi fókusz (Subject Focus)", "A PROFESSZOR olvasta el a tanulmányt. (It was the professor who read the study.)"],
                    ["Időhatározói fókusz (Temporal Focus)", "TEGNAP olvasta el a tanulmányt a professzor. (It was yesterday that he read it.)"],
                    ["Tárgyi fókusz (Object Focus)", "A TANULMÁNYT olvasta el a professzor. (It was the study that the professor read.)"],
                    ["Ellentétes fókusz (Contrastive Focus)", "Nem a könyvet, hanem a TANULMÁNYT olvasta el. (Not the book, but the study.)"],
                ],
                "examples": [
                    {
                        "spanish": "A magyar mondatban a fókuszpozícióba helyezett kifejezés hordozza a legerősebb mondathangsúlyt.",
                        "english": "In the Hungarian sentence, the phrase placed in the focus position carries the strongest sentence stress.",
                    },
                    {
                        "spanish": "A finom hangsúlyeltolódás révén a beszélő anélkül változtathatja meg a mondat értelmét, hogy új szavakat használna.",
                        "english": "Through subtle shifts of emphasis, the speaker can alter the meaning of the sentence without using new words.",
                    },
                    {
                        "spanish": "Az igényes irodalmi mondatszerkezet elkerüli az egyhangúságot és zenei ritmust kölcsönöz a szövegnek.",
                        "english": "Demanding literary sentence structure avoids monotony and lends a musical rhythm to the text.",
                    },
                    {
                        "spanish": "A nyelv valódi kifejezőereje a nyelvtani finomságok és a stílusrétegek harmonikus egységében rejlik.",
                        "english": "The true expressive power of the language lies in the harmonious unity of linguistic subtleties and stylistic registers.",
                    },
                ],
                "tip": "Pay close attention to where the preverb lands: whenever a focused element, question word, or negation ('nem') precedes the verb, the preverb MUST follow the verb ('ki érkezett meg?', 'nem jött el').",
            },
            "words": [
                {"lemma": "fókuszpozíció", "translation": "focus position / emphatic slot", "pos": "noun"},
                {"lemma": "hangsúlyeltolódás", "translation": "shift of emphasis / stress shift", "pos": "noun"},
                {"lemma": "mondatszerkezet", "translation": "sentence structure / syntax", "pos": "noun"},
                {"lemma": "kifejezőerő", "translation": "expressive power / expressiveness", "pos": "noun"},
                {"lemma": "nyelvi finomság", "translation": "linguistic nuance / subtlety", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the grammatical role of the 'fókuszpozíció' in Hungarian syntax?",
                        [
                            "the preverbal slot that carries primary stress and identifies exhaustive prominence",
                            "the final punctuation mark at the end of an exclamatory sentence",
                            "a grammatical prefix attached to comparative adjectives",
                        ],
                        0,
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which compound noun denotes the expressive impact and communicative strength of language?",
                        ["kifejezőerő", "mondatszerkezet", "hangsúlyeltolódás"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["fókuszpozíció", "focus position / emphatic slot"],
                            ["hangsúlyeltolódás", "shift of emphasis"],
                            ["mondatszerkezet", "sentence structure / syntax"],
                            ["kifejezőerő", "expressive power"],
                            ["nyelvi finomság", "linguistic nuance / subtlety"],
                        ],
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What happens to the verbal preverb when an argument occupies the preverbal focus position?",
                        [
                            "The preverb moves behind the conjugated verb (preverb-verb inversion).",
                            "The preverb disappears entirely from the sentence.",
                            "The preverb duplicates before and after the verb.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence where exhaustive focus on 'Péter' causes correct inversion:",
                        [
                            "PÉTER oldotta meg a legnehezebb feladatot a vizsgán.",
                            "Péter megoldotta a legnehezebb feladatot tegnap.",
                            "Megoldotta Péter a feladatot este csendben.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A magyar nyelvben a finom ____ alapvetően megváltoztathatja a mondat közlési célját. (shift of emphasis)",
                        "hangsúlyeltolódás",
                        "In Hungarian, a subtle shift of emphasis can fundamentally alter the communicative intent of the sentence.",
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Nem a dékán, hanem a miniszter ____ alá a nemzetközi megállapodást. (signed - with inversion)",
                        "írta",
                        "Not the dean, but the minister signed the international agreement.",
                        ["b2-mastery-synthesis"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "magyar", "nyelv", "rendkívüli", "kifejezőerővel", "képes", "megragadni", "az", "érzelmeket."],
                        ["A", "magyar", "nyelv", "rendkívüli", "kifejezőerővel", "képes", "megragadni", "az", "érzelmeket."],
                        "The Hungarian language is capable of capturing emotions with extraordinary expressive power.",
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A szónok változatos ____ tették dinamikussá és élvezetessé a beszédet. (sentence structures)",
                        "mondatszerkezetei",
                        "The speaker's varied sentence structures made the address dynamic and enjoyable.",
                        ["b2-36-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "műfordító", "minden", "rejtett", "nyelvi", "finomságra", "kínosan", "ügyelt", "a", "szövegben."],
                        ["A", "műfordító", "minden", "rejtett", "nyelvi", "finomságra", "kínosan", "ügyelt", "a", "szövegben."],
                        "The literary translator painstakingly attended to every hidden linguistic nuance in the text.",
                        ["b2-36-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Nyelvész", "text": "Miért okoz nehézséget a magyar fókuszszerkezet a külföldi tanulóknak?"},
                            {"speaker": "Tanár", "text": "____"},
                        ],
                        [
                            "Mert a hangsúlyeltolódás azonnal megváltoztatja az igekötő helyét és a mondat logikai hangsúlyát.",
                            "Mert a fókuszpozíció tilos minden modern európai nyelvben.",
                            "Ugyan már, a mondatszerkezet csak a limlomoknak fontos a padláson.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Költő", "text": "Hogyan éred el, hogy a prózád zeneinek hasson felolvasáskor?"},
                            {"speaker": "Író", "text": "____"},
                        ],
                        [
                            "A topik-fókusz ritmusával játszom, és a mondatszerkezetek tudatos variálásával adok lüktetést a gondolatoknak.",
                            "Kizárólag háromszavas mondatokat írok egymás után megszakítás nélkül.",
                            "Minden mondatba beleteszem a gizgaz szót a biztonság kedvéért.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using contrastive focus (Nem X, hanem Y + inverted verb) on the subject.",
                                "answer": "Nem a bizottság elnöke, hanem a független szakértő tárta fel a vizsgálat során a rendszer súlyos hiányosságait.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence reflecting on the 'kifejezőerő' and 'nyelvi finomság' of Hungarian.",
                                "answer": "A magyar nyelv páratlan kifejezőereje a szóképzés gazdagságában és a mondatszerkesztés számtalan finomságában nyilvánul meg.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Az igazi mester tisztában van a magyar szórend minden rejtett ____. (nuance / subtlety)",
                        "finomságával",
                        "The true master is aware of every hidden subtlety of Hungarian word order.",
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the linear syntax and clause architecture of a sentence?",
                        ["mondatszerkezet", "hangsúlyeltolódás", "kifejezőerő"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Mastering Participles, Nominalizations, and Complex Connectors",
            "grammar_label": "Syntactic compression: left-branching participial clauses, action nominalization, and cohesive connectors",
            "goals": [
                "I can condense subordinate clauses into sophisticated left-branching participial modifiers",
                "I can deploy action nominalizations with possessive and postpositional chains in formal prose",
                "I can weave cohesive essays using high-register connectors like 'mindazonáltal' and 'következésképp'",
            ],
            "grammar_doc": {
                "slug": "participles-nominalizations-connectors",
                "title": "Mastering Participles, Nominalizations, and Complex Connectors",
                "text1_title": "Syntactic Compression via Left-Branching Participial Modifiers",
                "text1": "Advanced Hungarian achieves intellectual elegance through syntactic compression (szintaktikai sűrítés). Instead of sprawling relative clauses introduced by 'amely' or 'aki', formal prose condenses information into left-branching adjectival participles (melléknévi igenevek: present in -ó/-ő, past in -t/-tt, and future/obligatory in -andó/-endő) that precede the head noun along with all their governed complements: 'a kormányzat által a válság kezelésére tavaly kidolgozott stratégia' (the strategy developed last year by the government to manage the crisis).",
                "text2_title": "Action Nominalization and Discourse Connectors",
                "text2": "Nominal structures (névszói szerkezetek) formed with the productive suffix -ás/-és allow processes to become syntactic subjects or objects. These are seamlessly linked across paragraphs using high-register cohesive connectors: 'mindazonáltal' (nevertheless, nonetheless) introduces sophisticated concessions, while 'következésképp' (consequently, as a result) establishes airtight deductive conclusions.",
                "table_title": "Syntactic Compression and Cohesive Connectors",
                "table_rows": [
                    ["Relatív mellékmondat (Sprawling)", "A törvényjavaslat, amelyet a parlament a múlt héten fogadott el..."],
                    ["Balra ágazó igeneves szerkezet (Compressed)", "A parlament által a múlt héten elfogadott törvényjavaslat..."],
                    ["Névszósítás (-ás/-és)", "A szabályozás felülvizsgálata elkerülhetetlenné vált. (Revision of regulation.)"],
                    ["mindazonáltal", "A terv kockázatos; mindazonáltal érdemes megvalósítani. (Nevertheless worthy.)"],
                    ["következésképp", "A határidő lejárt, következésképp a beadvány érvénytelen. (Consequently invalid.)"],
                ],
                "examples": [
                    {
                        "spanish": "A szakértők által hetek óta vizsgált dokumentumok egyértelműen bizonyítják a mulasztást.",
                        "english": "The documents examined for weeks by the experts unequivocally prove the negligence.",
                    },
                    {
                        "spanish": "A szintaktikai sűrítés révén a tudományos értekezés elkerüli a felesleges mellékmondatok halmozását.",
                        "english": "Through syntactic compression, the scientific dissertation avoids the accumulation of superfluous subordinate clauses.",
                    },
                    {
                        "spanish": "A reformok bevezetése rendkívül nehéz feladat; mindazonáltal a nemzetgazdaság stabilitása ezt követeli meg.",
                        "english": "The introduction of reforms is an extremely difficult task; nevertheless, the stability of the national economy demands this.",
                    },
                    {
                        "spanish": "A tárgyalások eredménytelenül zárultak, következésképp a felek kénytelenek a bírósághoz fordulni.",
                        "english": "The negotiations concluded unsuccessfully; consequently, the parties are obliged to turn to the court.",
                    },
                ],
                "tip": "When building extended left-branching participial clauses, ensure the participle directly precedes the noun it modifies, with all adverbs and objects placed immediately before the participle: '[A bizottság által tegnap elfogadott] határozat'.",
            },
            "words": [
                {"lemma": "melléknévi igenév", "translation": "adjectival participle", "pos": "expression"},
                {"lemma": "névszói szerkezet", "translation": "nominal structure / phrase", "pos": "expression"},
                {"lemma": "szintaktikai sűrítés", "translation": "syntactic compression / clause condensation", "pos": "expression"},
                {"lemma": "mindazonáltal", "translation": "nevertheless / nonetheless / for all that", "pos": "conjunction"},
                {"lemma": "következésképp", "translation": "consequently / as a result", "pos": "adverb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'szintaktikai sűrítés' in advanced Hungarian stylistic register?",
                        [
                            "condensing subordinate clauses into compact participial and nominal structures",
                            "cutting a sentence in half to create an incomplete thought",
                            "erasing all vowels from a written document",
                        ],
                        0,
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which connector introduces an adversative concession meaning 'nevertheless' or 'nonetheless'?",
                        ["mindazonáltal", "következésképp", "ugyan már"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["melléknévi igenév", "adjectival participle"],
                            ["névszói szerkezet", "nominal structure / phrase"],
                            ["szintaktikai sűrítés", "syntactic compression"],
                            ["mindazonáltal", "nevertheless / nonetheless"],
                            ["következésképp", "consequently / as a result"],
                        ],
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "How is the relative clause 'a stratégia, amelyet a kutatók dolgoztak ki' condensed into a left-branching participial phrase?",
                        [
                            "a kutatók által kidolgozott stratégia",
                            "a stratégia ami kidolgozott a kutatóktól",
                            "kidolgoztak a kutatók egy stratégiát",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which word functions as a deductive consequential connector equivalent to 'ezért / ennek következtében'?",
                        ["következésképp", "mindazonáltal", "elvégre"],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A gazdasági helyzet kétségkívül súlyos; ____ nem szabad elveszítenünk a reményt. (nevertheless / nonetheless)",
                        "mindazonáltal",
                        "The economic situation is undoubtedly grave; nevertheless, we must not lose hope.",
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A felek nem tudtak megegyezni, ____ a döntőbizottságnak kell határozatot hoznia az ügyben. (consequently / as a result)",
                        "következésképp",
                        "The parties could not agree; consequently, the arbitration committee must make a decision on the matter.",
                        ["b2-mastery-synthesis"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "bizottság", "által", "tavaly", "elfogadott", "határozat", "minden", "tagállamra", "nézve", "kötelező."],
                        ["A", "bizottság", "által", "tavaly", "elfogadott", "határozat", "minden", "tagállamra", "nézve", "kötelező."],
                        "The resolution adopted last year by the committee is binding on all member states.",
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A balra ágazó ____ használata elegáns és tömör kifejezést biztosít az akadémiai értekezésekben. (adjectival participles)",
                        "melléknévi igenevek",
                        "The use of left-branching adjectival participles provides elegant and concise expression in academic dissertations.",
                        ["b2-36-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "szintaktikai", "sűrítés", "révén", "a", "szerző", "rendkívül", "tömören", "fogalmazta", "meg", "mondanivalóját."],
                        ["A", "szintaktikai", "sűrítés", "révén", "a", "szerző", "rendkívül", "tömören", "fogalmazta", "meg", "mondanivalóját."],
                        "Through syntactic compression, the author formulated his message extremely concisely.",
                        ["b2-36-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Egyetemi hallgató", "text": "Hogyan tehetem érettebbé és professzionálisabbá a szakdolgozatom stílusát?"},
                            {"speaker": "Konzulens", "text": "____"},
                        ],
                        [
                            "Alkalmazz szintaktikai sűrítést: cseréld a nehézkes mellékmondatokat elegáns melléknévi igeneves szerkezetekre és használj pontos kötőszókat.",
                            "Használj minél több utcai szlenget és gizgazt minden fejezetben.",
                            "Töröld ki az összes állítmányt és hagyj csak főneveket.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Szerkesztő", "text": "Nem érzed úgy, hogy ez a két bekezdés kissé szétesik logikailag?"},
                            {"speaker": "Újságíró", "text": "____"},
                        ],
                        [
                            "Igazad van, beillesztem a 'mindazonáltal' kötőszót az elejére, hogy világos legyen az ellentétes gondolatmenet.",
                            "Dehogyis, a limlom sosem igényel logikai kapcsolatot a szövegben.",
                            "Ugyan már, a következésképp csak a villamoson érvényes reggel.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Rewrite the relative clause 'A jelentés, amelyet a minisztérium készített a válságról' into a compressed left-branching participial phrase.",
                                "answer": "A minisztérium által a válságról készített átfogó jelentés világosan feltárta a problémák gyökerét.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a cohesive two-clause analytical sentence using 'mindazonáltal'.",
                                "answer": "A reformtervezet bevezetése komoly költségvetési áldozatokat követel; mindazonáltal a hosszú távú gazdasági versenyképesség megőrzése érdekében elkerülhetetlen.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A pályázati feltételek nem teljesültek, ____ az eljárást érvénytelennek kell nyilvánítani. (consequently)",
                        "következésképp",
                        "The application conditions were not fulfilled; consequently, the procedure must be declared invalid.",
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which linguistic term designates phrases constructed from nouns and their modifiers rather than verbs?",
                        ["névszói szerkezet", "melléknévi igenév", "fókuszpozíció"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Politeness, Hedging, and Nuanced Debate in Hungarian",
            "grammar_label": "Diplomatic hedging, nuanced refutation, and stance qualification (ha szabad úgy fogalmaznom, indokolt volna megfontolni)",
            "goals": [
                "I can soften strong opinions using diplomatic conditional hedging formulas",
                "I can structure polite, high-register counter-arguments and concessions in debates",
                "I can maintain an eloquent, constructive tone during contentious intellectual discussions",
            ],
            "grammar_doc": {
                "slug": "politeness-hedging-nuanced-debate",
                "title": "Politeness, Hedging, and Nuanced Debate in Hungarian",
                "text1_title": "Diplomatic Hedging and Stance Mitigation (Udvarias tompítás)",
                "text1": "In upper-intermediate intellectual discourse, assertiveness must be balanced with diplomatic mitigation (tompítás). Rather than making absolute declarative assertions ('Ez a terv hibás'), polished Hungarian deploys epistemic conditional parentheticals and modal formulas: 'Ha szabad úgy fogalmaznom...', 'Nem áll szándékomban kétségbe vonni az Ön szakértelmét, mindazonáltal...', or 'Indokolt volna megfontolni a javaslat esetleges árnyoldalait.'",
                "text2_title": "Structuring Nuanced Refutations and Standpoint Clarification",
                "text2": "Articulating a differentiated stance ('árnyalt álláspont') on controversial issues ('vitatott kérdések') requires structured refutations ('cáfolat'). An eloquent debater concedes the merits of the opposing argument ('Kétségtelen, hogy az érvelésnek van alapja...') before pivoting to the counter-evidence ('A rendelkezésre álló adatok fényében azonban megkérdőjelezhető...').",
                "table_title": "Diplomatic Debate and Hedging Formulae",
                "table_rows": [
                    ["Ha szabad úgy fogalmaznom...", "Ha szabad úgy fogalmaznom, a javaslat némileg elhamarkodott. (If I may put it so.)"],
                    ["Indokolt volna megfontolni...", "Indokolt volna megfontolni a döntés pénzügyi következményeit. (It would be justified to consider.)"],
                    ["Nem áll szándékomban vitatni...", "Nem áll szándékomban vitatni az eredményeket, mindazonáltal... (It is not my intent to dispute.)"],
                    ["Megkockáztatom a feltevést...", "Megkockáztatom a feltevést, hogy a modell pontosításra szorul. (I venture the assumption.)"],
                    ["Hajlok arra a véleményre...", "Hajlok arra a véleményre, hogy a kompromisszum elkerülhetetlen. (I lean towards the view.)"],
                ],
                "examples": [
                    {
                        "spanish": "A professzor rendkívül árnyalt álláspontot képviselt a heves egyetemi vitában.",
                        "english": "The professor represented an extremely nuanced standpoint in the fierce university debate.",
                    },
                    {
                        "spanish": "Bár a kérdés erősen vitatott, a tárgyalófelek kölcsönös tisztelettel hallgatták meg egymás érveit.",
                        "english": "Although the issue is heavily disputed, the negotiating parties listened to each other's arguments with mutual respect.",
                    },
                    {
                        "spanish": "A meggyőző cáfolat nem a másik fél megbántásán, hanem a tények logikus bemutatásán alapul.",
                        "english": "A convincing refutation is based not on hurting the other party, but on the logical presentation of facts.",
                    },
                    {
                        "spanish": "A tompítás és az udvarias kifejezésmód a magas szintű diplomáciai tárgyalások elengedhetetlen kelléke.",
                        "english": "Hedging and polite phrasing are indispensable requirements of high-level diplomatic negotiations.",
                    },
                ],
                "tip": "Use the conditional with impersonal verbs to soften criticism: replace 'Meg kell változtatni' with 'Célszerű volna megváltoztatni' or 'Indokolt lenne felülvizsgálni'.",
            },
            "words": [
                {"lemma": "árnyalt", "translation": "nuanced / subtle / differentiated", "pos": "adjective"},
                {"lemma": "vitatott", "translation": "controversial / disputed / debatable", "pos": "adjective"},
                {"lemma": "álláspont", "translation": "standpoint / stance / point of view", "pos": "noun"},
                {"lemma": "tompítás", "translation": "hedging / softening / mitigation", "pos": "noun"},
                {"lemma": "cáfolat", "translation": "refutation / counter-argument / rebuttal", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'tompítás' (hedging) in pragmatic linguistics and rhetoric?",
                        [
                            "the diplomatic mitigation or softening of assertions to avoid sounding overly dogmatic or offensive",
                            "speaking in a whisper so nobody in the room can hear",
                            "repeating every word twice for emphasis",
                        ],
                        0,
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective characterizes an argument that carefully considers multiple subtleties rather than being black-and-white?",
                        ["árnyalt", "vitatott", "cáfolat"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["árnyalt", "nuanced / subtle / differentiated"],
                            ["vitatott", "controversial / disputed"],
                            ["álláspont", "standpoint / stance"],
                            ["tompítás", "hedging / softening"],
                            ["cáfolat", "refutation / rebuttal"],
                        ],
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which phrase serves as a polite conditional hedge to soften a critical observation?",
                        [
                            "Ha szabad úgy fogalmaznom, a döntés kissé elhamarkodottnak tűnik.",
                            "Mindenki tudja, hogy Ön egyáltalán nem ért a dologhoz!",
                            "Azonnal vonja vissza a javaslatát, mert nevetséges!",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "How can the aggressive statement 'Ez a tanulmány tele van tévedésekkel' be refined diplomatically?",
                        [
                            "Indokolt volna a tanulmány egyes módszertani feltételezéseit újra megvizsgálni.",
                            "Ugyan már, a tanulmány tele van gizgazzal és limlommal.",
                            "A szerző azonnal kérjen bocsánatot minden olvasótól.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A történész részletes és megdönthetetlen ____ adott a korábbi téves elméletre. (refutation / rebuttal)",
                        "cáfolatot",
                        "The historian gave a detailed and irrefutable refutation of the previous erroneous theory.",
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A konferencián a felszólaló rendkívül ____ és meggyőző álláspontot fejtett ki. (nuanced / subtle)",
                        "árnyalt",
                        "At the conference, the speaker articulated an extremely nuanced and convincing stance.",
                        ["b2-mastery-synthesis"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Indokolt", "volna", "megfontolni", "az", "alternatív", "javaslatokat", "a", "döntéshozatal", "előtt."],
                        ["Indokolt", "volna", "megfontolni", "az", "alternatív", "javaslatokat", "a", "döntéshozatal", "előtt."],
                        "It would be justified to consider the alternative proposals before decision-making.",
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Bár a reformtervezet rendkívül ____ téma a közéletben, a párbeszédet folytatni kell. (controversial / disputed)",
                        "vitatott",
                        "Although the reform proposal is a highly controversial topic in public life, the dialogue must be continued.",
                        ["b2-36-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "diplomata", "mindvégig", "következetesen", "kitartott", "az", "országa", "hivatalos", "álláspontja", "mellett."],
                        ["A", "diplomata", "mindvégig", "következetesen", "kitartott", "az", "országa", "hivatalos", "álláspontja", "mellett."],
                        "The diplomat consistently adhered to his country's official standpoint throughout.",
                        ["b2-36-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Vitavezető", "text": "Hogyan foglalná össze a javaslattal kapcsolatos aggályait?"},
                            {"speaker": "Szakértő", "text": "____"},
                        ],
                        [
                            "Ha szabad úgy fogalmaznom, a célkitűzésekkel egyetértünk, de indokolt volna a végrehajtás ütemezését átgondolni.",
                            "A javaslat egy nagy limlom, amit azonnal a szemétbe kell dobni.",
                            "Dehogyis vannak aggályaim, a gizgaz már mindent megoldott tegnap.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Résztvevő", "text": "Nem tartja sértőnek az ellenfele kemény kritikáját?"},
                            {"speaker": "Előadó", "text": "____"},
                        ],
                        [
                            "Egyáltalán nem: a vita vitatott kérdésekről szól, és a higgadt, logikus cáfolat mindig előreviszi az igazság keresését.",
                            "Ugyan már, azonnal kiakadok és bevállalom a hercehurcát a folyosón.",
                            "A tompítás miatt nem hallottam semmit, amit mondott.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a diplomatically hedged counter-argument beginning with 'Indokolt volna megfontolni...'.",
                                "answer": "Indokolt volna megfontolni a döntés hosszú távú társadalmi következményeit, mielőtt végleges kötelezettséget vállalnánk a projekt mellett.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence presenting an 'árnyalt álláspont' on a contentious debate.",
                                "answer": "Az egyetem vezetése árnyalt álláspontot alakított ki, amely egyaránt tekintettel van a hallgatók igényeire és az akadémiai minőség megőrzésére.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A diplomáciában a finom ____ művészete elengedhetetlen a felesleges konfliktusok elkerüléséhez. (hedging / mitigation)",
                        "tompítás",
                        "In diplomacy, the art of subtle hedging is indispensable for avoiding unnecessary conflicts.",
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes an individual's or institution's coherent intellectual stance on an issue?",
                        ["álláspont", "cáfolat", "kifejezőerő"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Reading Unabridged Hungarian Literature with Confidence",
            "grammar_label": "Literary syntax, archaisms, and metaphorical interpretation in unabridged Hungarian classics",
            "goals": [
                "I can navigate complex literary sentence structures and poetic inversions without loss of comprehension",
                "I can identify archaic verbal forms and historical derivations in classic literature",
                "I can analyze metaphorical imagery and authorial voice across diverse literary genres",
            ],
            "grammar_doc": {
                "slug": "reading-unabridged-literature",
                "title": "Reading Unabridged Hungarian Literature with Confidence",
                "text1_title": "Navigating Literary Syntax and Authorial Voice",
                "text1": "Reading unabridged Hungarian belles-lettres (szépirodalom) from the 19th and 20th centuries – from Mór Jókai and Kálmán Mikszáth to Dezső Kosztolányi and Sándor Márai – represents the true coronation of B2 literacy. Literary prose employs stylistic devices (stíluseszközök) such as rhythmic inversion, complex participial chaining, ellipsis, and polyphonic shifts between narrator and character perspectives.",
                "text2_title": "Deciphering Archaisms in Textual Context",
                "text2": "Classic texts contain occasional archaic forms (archaikus kifejezések: narrative past endings like '-vala', translative archaisms, or Latin loanwords). Fluent readers do not need a dictionary for every word; rather, they infer precise meanings from surrounding textual context (szövegkörnyezet) and focus on interpretive depth ('értelmezés'), appreciating the author's philosophical and aesthetic vision.",
                "table_title": "Literary Styles and Interpretive Concepts",
                "table_rows": [
                    ["szépirodalom", "A magyar szépirodalom remekművei gazdag emberi tapasztalatot sűrítenek. (Belles-lettres masterpieces.)"],
                    ["archaikus", "Az archaikus kifejezések régmúlt korok sajátos hangulatát idézik fel. (Archaic expressions evoke mood.)"],
                    ["stíluseszköz", "A metafora és a metonímia a költészet leggyakoribb stíluseszközei. (Stylistic devices.)"],
                    ["szövegkörnyezet", "Az ismeretlen kifejezés jelentését a szövegkörnyezet alapján fejtette meg. (Deduced from context.)"],
                    ["értelmezés", "A regény többrétegű értelmezése új szempontokat nyújt az olvasónak. (Multi-layered interpretation.)"],
                ],
                "examples": [
                    {
                        "spanish": "A magyar szépirodalom olvasása során a nyelvtanuló nemcsak szavakat tanul, hanem a magyar gondolkodásmódot is megismeri.",
                        "english": "During the reading of Hungarian literature, the language learner not only learns words, but also gets to know the Hungarian mindset.",
                    },
                    {
                        "spanish": "Bár Jókai regényeiben számos archaikus szófordulattal találkozunk, a lendületes cselekmény mindvégig magával ragadja az olvasót.",
                        "english": "Although we encounter numerous archaic idioms in Jókai's novels, the gripping plot captivates the reader throughout.",
                    },
                    {
                        "spanish": "Az író tudatosan élt a késleltetés stíluseszközével, hogy fokozza a drámai feszültséget a fejezet végén.",
                        "english": "The writer consciously made use of the stylistic device of delay to heighten dramatic tension at the end of the chapter.",
                    },
                    {
                        "spanish": "Ha egy régies kifejezéssel szembesülünk, a tágabb szövegkörnyezet szinte mindig elárulja a valódi jelentést.",
                        "english": "When we encounter an archaic expression, the broader textual context almost always reveals the true meaning.",
                    },
                ],
                "tip": "When reading classics, do not stop at every unfamiliar 19th-century word. Read for narrative flow, identifying the main subject and verb first, then examine how modifiers enrich the scene.",
            },
            "words": [
                {"lemma": "szépirodalom", "translation": "belles-lettres / literary fiction / high literature", "pos": "noun"},
                {"lemma": "archaikus", "translation": "archaic / antiquated", "pos": "adjective"},
                {"lemma": "stíluseszköz", "translation": "stylistic device / literary technique", "pos": "noun"},
                {"lemma": "szövegkörnyezet", "translation": "textual context / surrounding text", "pos": "noun"},
                {"lemma": "értelmezés", "translation": "interpretation / reading / analysis", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'szépirodalom' encompass in Hungarian cultural life?",
                        [
                            "high-quality imaginative literature, belles-lettres, including novels, poetry, and drama",
                            "technical instructions for household electronic appliances",
                            "weather bulletins broadcast on marine radios",
                        ],
                        0,
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which noun denotes an artistic literary device or rhetorical technique (e.g. metaphor, irony)?",
                        ["stíluseszköz", "szövegkörnyezet", "értelmezés"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["szépirodalom", "belles-lettres / literature"],
                            ["archaikus", "archaic / antiquated"],
                            ["stíluseszköz", "stylistic device"],
                            ["szövegkörnyezet", "textual context"],
                            ["értelmezés", "interpretation / reading"],
                        ],
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "How should a reader approach archaic grammatical forms in 19th-century Hungarian novels?",
                        [
                            "Infer meaning from the textual context without disrupting reading comprehension.",
                            "Close the book immediately and never read literature again.",
                            "Report the archaic words to the police as spelling errors.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case suffix is governed by 'értelmezés' when discussing the interpretation of a text?",
                        ["genitive possessive (-nak/-nek az értelmezése)", "ablative (-tól/-től)", "delative (-ról/-ről)"],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A regény sűrű nyelvezete többféle filozófiai ____ enged teret. (interpretation)",
                        "értelmezésnek",
                        "The dense language of the novel leaves room for multiple philosophical interpretations.",
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A ritka szó jelentése könnyen kikövetkeztethető a tágabb ____ alapján. (textual context)",
                        "szövegkörnyezet",
                        "The meaning of the rare word can be easily deduced based on the broader textual context.",
                        ["b2-mastery-synthesis"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "klasszikus", "magyar", "szépirodalom", "olvasása", "fejleszti", "az", "esztétikai", "érzéket."],
                        ["A", "klasszikus", "magyar", "szépirodalom", "olvasása", "fejleszti", "az", "esztétikai", "érzéket."],
                        "Reading classic Hungarian literature develops aesthetic sensibility.",
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A 19. századi balladákban gyakran bukkannak fel ____ igealakok és régies fordulatok. (archaic)",
                        "archaikus",
                        "In 19th-century ballads, archaic verb forms and antiquated idioms frequently crop up.",
                        ["b2-36-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Az", "író", "a", "metaforát", "mint", "központi", "stíluseszközt", "használta", "a", "művében."],
                        ["Az", "író", "a", "metaforát", "mint", "központi", "stíluseszközt", "használta", "a", "művében."],
                        "The writer used metaphor as a central stylistic device in his work.",
                        ["b2-36-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Olvasó", "text": "Nem túl nehéz egy B2 szintű tanulónak eredeti Kosztolányit vagy Krúdyt olvasni?"},
                            {"speaker": "Irodalomtanár", "text": "____"},
                        ],
                        [
                            "Egyáltalán nem: a nyelvtani alapok birtokában a szövegkörnyezet segít, a szépirodalom zeneisége pedig magával ragadja az olvasót.",
                            "Dehogyis szabad olvasni őket, a törvény tiltja a szépirodalmat.",
                            "Ugyan már, a könyvekben csak hercehurca és csecsebecse található.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Diák", "text": "Mit tegyek, ha egy archaikus kifejezést találok a novellában?"},
                            {"speaker": "Mentor", "text": "____"},
                        ],
                        [
                            "Ne ess pánikba! Nézd meg a mondat cselekményét, támaszkodj a szövegkörnyezetre, és haladj bátran tovább.",
                            "Azonnal dobd ki a könyvet és fuss el a parkba.",
                            "Kérdezd meg a szervetlen lényt Faremidóban a válaszról.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence reflecting on the rewards of reading Hungarian 'szépirodalom'.",
                                "answer": "Az eredeti magyar szépirodalom rendszeres olvasása páratlan módon gazdagítja a szókincset és elmélyíti a kulturális empátiát.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence explaining how to deduce unfamiliar words from 'szövegkörnyezet'.",
                                "answer": "Ha ismeretlen kifejezéssel találkozunk, a szövegkörnyezet és a logikai összefüggések gondos elemzésével szinte mindig feltárható a helyes jelentés.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A költő zseniálisan alkalmazta a megszemélyesítés ____ a tájleírásban. (stylistic device)",
                        "stíluseszközét",
                        "The poet brilliantly applied the stylistic device of personification in the landscape description.",
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adjective means 'archaic' or belonging to a distant historical era?",
                        ["archaikus", "árnyalt", "szellemes"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Finding Your Voice: Comprehensive B2 Capstone Speech & Essay",
            "grammar_label": "Comprehensive discourse synthesis: classical rhetoric, argumentatio, and individual voice in B2 capstones",
            "goals": [
                "I can deliver a well-structured, persuasive B2 capstone speech with authentic rhetoric",
                "I can author an extended analytical essay integrating all major B2 grammatical structures",
                "I can demonstrate sovereign communicative competence and stylistic versatility in Hungarian",
            ],
            "grammar_doc": {
                "slug": "comprehensive-b2-capstone-voice",
                "title": "Finding Your Voice: Comprehensive B2 Capstone Speech & Essay",
                "text1_title": "The Classical Rhetorical Framework of a B2 Capstone",
                "text1": "The culmination of upper-intermediate Hungarian is the capstone presentation and essay. Drawing on classical rhetoric (retorika), an effective address follows a time-tested four-part structure: (1) Exordium (bevezetés / figyelemfelkeltés) setting context; (2) Narratio et Propositio (tényállás és tézismeghatározás); (3) Argumentatio et Refutatio (érvelés és cáfolat) deploying left-branching participles, causatives, and conditional hedging; and (4) Peroratio (összegzés / zárszó) delivering a memorable conclusion.",
                "text2_title": "Delivery Style, Persuasion, and Authentic Personal Voice",
                "text2": "True linguistic mastery goes beyond grammatical correctness to embrace delivery style ('előadásmód'), persuasiveness ('meggyőzőerő'), and the emergence of one's own authentic voice ('saját hang'). In this capstone lesson, you synthesize everything learned across 36 B2 units: from focus inversion and figurative preverbs to diplomatic register and philosophical nuance.",
                "table_title": "B2 Rhetorical Architecture and Synthesis Formulas",
                "table_rows": [
                    ["Bevezetés (Exordium)", "Tisztelt Hallgatóság! Engedjék meg, hogy mai előadásomat egy gondolattal kezdjem..."],
                    ["Tézisfelállítás (Propositio)", "Álláspontom lényege a következőképpen foglalható össze: ..."],
                    ["Érvelés (Argumentatio)", "Két nyomós érv támasztja alá ezt a megközelítést: egyrészt..., másrészt..."],
                    ["Cáfolat (Refutatio)", "Bár gyakran felmerül az a nézet, hogy..., a valóság ezzel szemben azt mutatja..."],
                    ["Összegzés (Peroratio)", "Mindent egybevetve elmondhatjuk: a jövő záloga a felelős és bátor cselekvés."],
                ],
                "examples": [
                    {
                        "spanish": "A meggyőző előadásmód titka a pontosan felépített retorika és az őszinte, hiteles saját hang megtalálása.",
                        "english": "The secret of a persuasive delivery style is precisely structured rhetoric and finding an honest, authentic voice.",
                    },
                    {
                        "spanish": "A szónok rendkívüli meggyőzőerővel érvelt a társadalmi szolidaritás és a kulturális sokszínűség megőrzése mellett.",
                        "english": "The speaker argued with extraordinary persuasive power for the preservation of social solidarity and cultural diversity.",
                    },
                    {
                        "spanish": "Az előadás végén egy tömör és hatásos összegzésben foglalta össze a legfontosabb tanulságokat.",
                        "english": "At the end of the presentation, he summarized the most important takeaways in a concise and impactful conclusion.",
                    },
                    {
                        "spanish": "A B2 szint elérése azt jelenti, hogy az ember már képes magyarul gondolkodni és a maga egyéni hangján megszólalni.",
                        "english": "Reaching the B2 level means that one is already able to think in Hungarian and speak in their own individual voice.",
                    },
                ],
                "tip": "In your final capstone speech, maintain good eye contact, use measured pauses after key focus points, and let your natural enthusiasm shine through your Hungarian delivery.",
            },
            "words": [
                {"lemma": "retorika", "translation": "rhetoric / art of public speaking", "pos": "noun"},
                {"lemma": "összegzés", "translation": "summary / synthesis / concluding balance", "pos": "noun"},
                {"lemma": "meggyőzőerő", "translation": "power of persuasion / persuasiveness", "pos": "noun"},
                {"lemma": "előadásmód", "translation": "delivery style / presentation manner", "pos": "noun"},
                {"lemma": "saját hang", "translation": "one's own voice / authentic personal voice", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the ultimate communicative goal of the B2 capstone speech and essay?",
                        [
                            "finding one's authentic personal voice and persuasively delivering a structured address in Hungarian",
                            "reciting a dictionary list of irregular verbs in alphabetical order",
                            "translating legal tax codes without punctuation",
                        ],
                        0,
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which noun denotes the classical discipline and art of persuasive public speaking?",
                        ["retorika", "összegzés", "előadásmód"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["retorika", "rhetoric / public speaking"],
                            ["összegzés", "summary / synthesis"],
                            ["meggyőzőerő", "persuasive power"],
                            ["előadásmód", "delivery style / presentation"],
                            ["saját hang", "one's own voice / authentic voice"],
                        ],
                        ["b2-36-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which classical rhetorical sequence structures a professional capstone address?",
                        [
                            "Bevezetés (Exordium) -> Tézisfelállítás -> Érvelés és cáfolat -> Összegzés (Peroratio)",
                            "Összegzés -> Cáfolat -> Semleges csend -> Búcsúzás",
                            "Szitkozódás -> Tények letagadása -> Menekülés a teremből",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence demonstrating complete upper-intermediate discourse synthesis:",
                        [
                            "A gondosan megválasztott érvek és a szuggesztív előadásmód révén a szónok mély hatást gyakorolt a hallgatóságra.",
                            "A retorika felmászott a fára és elaludt tegnap este nyolckor.",
                            "Minden mondat egy gizgaz, ami kiakad a limlom miatt.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A záróbeszéd lényegét egy frappáns és emlékezetes ____ foglalta össze a hallgatóknak. (summary / synthesis)",
                        "összegzésben",
                        "He summarized the essence of the concluding speech for the audience in a snappy and memorable synthesis.",
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A szónok beszéde rendkívüli ____ bírt, és minden jelenlévőt meggyőzött az ügy fontosságáról. (persuasive power)",
                        "meggyőzőerővel",
                        "The orator's speech possessed extraordinary persuasive power and convinced everyone present of the importance of the cause.",
                        ["b2-mastery-synthesis"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "klasszikus", "retorika", "szabályai", "segítenek", "a", "gondolatok", "világos", "és", "hatásos", "elrendezésében."],
                        ["A", "klasszikus", "retorika", "szabályai", "segítenek", "a", "gondolatok", "világos", "és", "hatásos", "elrendezésében."],
                        "The rules of classical rhetoric help in the clear and effective arrangement of thoughts.",
                        ["b2-mastery-synthesis"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A hosszú tanulási folyamat legfőbb célja, hogy a diák rátaláljon a maga autentikus ____ az idegen nyelven is. (own voice)",
                        "saját hangjára",
                        "The ultimate goal of the long learning process is for the student to find their authentic own voice in the foreign language too.",
                        ["b2-36-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "természetes", "és", "magabiztos", "előadásmód", "azonnal", "megragadta", "a", "közönség", "figyelmét."],
                        ["A", "természetes", "és", "magabiztos", "előadásmód", "azonnal", "megragadta", "a", "közönség", "figyelmét."],
                        "The natural and confident delivery style immediately captured the audience's attention.",
                        ["b2-36-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Vizsgáztató", "text": "Hogyan értékeli a jelölt B2 szintű záróelőadását?"},
                            {"speaker": "Elnök", "text": "____"},
                        ],
                        [
                            "Kiválónak: nemcsak a nyelvtant uralja tökéletesen, hanem megtalálta a saját hangját, és lenyűgöző meggyőzőerővel beszélt.",
                            "Sajnos a jelölt semmit sem tudott elmondani, mert a gizgaz megzavarta.",
                            "Ugyan már, a retorika tilos minden európai vizsgaközpontban.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Hallgató", "text": "Mit tanácsolsz a záróbeszéd előtti utolsó percekre?"},
                            {"speaker": "Barát", "text": "____"},
                        ],
                        [
                            "Lélegezz mélyeket, bízz a felkészültségedben, és beszélj természetes, őszinte előadásmóddal a közönséghez!",
                            "Fuss ki az épületből és ne gyere vissza soha többé.",
                            "Dehogyis beszélsz, a fülke ablakát már bezárták a vonaton.",
                        ],
                        0,
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an exordium sentence opening a formal B2 capstone speech.",
                                "answer": "Tisztelt Hölgyeim és Uraim, kedves Kollégák! Nagy megtiszteltetés számomra, hogy ma itt állhatok és megoszthatom Önökkel a magyar nyelv tanulása során szerzett legfontosabb tapasztalataimat.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a peroratio (concluding synthesis) sentence uniting 'összegzés' and 'saját hang'.",
                                "answer": "Összegzésképpen elmondhatom: a nyelvtanulás valódi gyümölcse nem a hibátlan szabálykövetés, hanem a szabadság, amellyel immár magyarul is képes vagyok megszólalni a saját egyéni hangomon.",
                            }
                        ],
                        ["b2-mastery-synthesis"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A diák érett gondolkodásról és kiváló stílusérzékről tanúskodó beszéde óriási ____ gyakorolt mindenkire. (persuasive power / impact)",
                        "meggyőzőerőt",
                        "The student's speech, testifying to mature thinking and excellent sense of style, exerted immense persuasive power on everyone.",
                        ["b2-mastery-synthesis"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes an individual's authentic, unique style of expression?",
                        ["saját hang", "szövegkörnyezet", "fókuszpozíció"],
                        0,
                        ["b2-36-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can demonstrate complete upper-intermediate mastery across topic-focus syntax, participial compression, and hedging",
            "I can analyze and interpret authentic unabridged Hungarian literature with cultural empathy",
            "I can author and deliver an eloquent, persuasive B2 capstone essay and speech with an authentic voice",
        ],
        "exercises": [
            # 1..3 Recognize
            mc(
                "vocabulary",
                "recognize",
                "What does 'szintaktikai sűrítés' accomplish in academic and literary Hungarian?",
                [
                    "It condenses complex subordinate clauses into left-branching participial and nominal modifiers.",
                    "It shortens words by omitting all vowels from the text.",
                    "It transforms all verbs into the imperative mood.",
                ],
                0,
                ["b2-36-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "Which term denotes the art of persuasive discourse and structured public speaking?",
                ["retorika", "melléknévi igenév", "stíluseszköz"],
                0,
                ["b2-36-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence exemplifies complete B2 synthesis of topic-focus architecture and participial compression?",
                [
                    "A minisztérium által kidolgozott javaslatot TEGNAP fogadta el a parlament, nem a múlt heti ülésen.",
                    "Tegnap a parlament elfogadta a javaslatot ami a minisztérium készített régen.",
                    "Elfogadta a minisztérium tegnap a javaslatot gyorsan este.",
                ],
                0,
                ["b2-mastery-synthesis"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A diplomáciai tárgyalások során a finom ____ segített elkerülni a személyeskedő konfliktusokat. (hedging / mitigation)",
                "tompítás",
                "During diplomatic negotiations, subtle hedging helped avoid personal conflicts.",
                ["b2-36-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A reformtervezet vitatott kérdéseket érint; ____ elkerülhetetlen a társadalmi egyeztetés megkezdése. (nevertheless / nonetheless)",
                "mindazonáltal",
                "The reform plan touches upon controversial issues; nevertheless, the launch of social consultation is inevitable.",
                ["b2-mastery-synthesis"],
            ),
            fb(
                "grammar",
                "recall",
                "A tárgyalások megszakadtak, ____ a felek nem tudták aláírni a tervezett békeszerződést. (consequently / as a result)",
                "következésképp",
                "The negotiations were broken off; consequently, the parties were unable to sign the planned peace treaty.",
                ["b2-mastery-synthesis"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'Indokolt volna megfontolni' preferred over 'Azonnal meg kell fontolni' in intellectual debates?",
                [
                    "Because the conditional mood diplomatically softens the assertion, demonstrating respectful academic debate.",
                    "Because 'kell' is illegal in written Hungarian.",
                    "Because 'indokolt volna' only applies to financial accounting.",
                ],
                0,
                ["b2-mastery-synthesis"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Kolléga", "text": "Hogyan élted meg a B2 záróvizsga szóbeli részét?"},
                    {"speaker": "Vizsgázó", "text": "____"},
                ],
                [
                    "Felejthetetlen élmény volt: a felkészültségemnek köszönhetően sikerült megtalálnom a saját hangomat, és árnyaltan érvelhettem a bizottság előtt.",
                    "Azonnal gizgazt gyűjtöttem a vizsgaterem sarkában.",
                    "Dehogyis mentem el, a limlom nem engedte meg a beiratkozást.",
                ],
                0,
                ["b2-mastery-synthesis"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where left-branching participial compression is used with perfect syntactic elegance:",
                [
                    "A nemzetközi kutatócsoport által évek óta végzett vizsgálatok egyértelműen alátámasztják a hipotézist.",
                    "A vizsgálatok amelyeket a kutatók végeztek évek óta tegnap csinálták meg a laborban.",
                    "A hipotézis elszaladt a nemzetközi kutatók elől a parkban reggel.",
                ],
                0,
                ["b2-mastery-synthesis"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "szónok", "rendkívül", "árnyalt", "álláspontot", "képviselt", "a", "heves", "egyetemi", "vitában."],
                ["A", "szónok", "rendkívül", "árnyalt", "álláspontot", "képviselt", "a", "heves", "egyetemi", "vitában."],
                "The speaker represented an extremely nuanced standpoint in the fierce university debate.",
                ["b2-mastery-synthesis"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "klasszikus", "magyar", "szépirodalom", "olvasása", "mély", "bepillantást", "enged", "a", "nemzet", "történelmébe."],
                ["A", "klasszikus", "magyar", "szépirodalom", "olvasása", "mély", "bepillantást", "enged", "a", "nemzet", "történelmébe."],
                "Reading classic Hungarian literature allows a deep insight into the nation's history.",
                ["b2-mastery-synthesis"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause B2 capstone synthesis essay excerpt uniting left-branching participial compression, cohesive connectors ('mindazonáltal'), and finding one's authentic voice ('saját hang').",
                        "answer": "Bár a magyar nyelv bonyolult topik-fókusz architektúrája és a balra ágazó igeneves szerkezetek elsajátítása komoly szellemi erőfeszítést igényelt; mindazonáltal a kitartó tanulás meghozta gyümölcsét, hiszen a B2 szint zárásaként ma már nem csupán megértem a klasszikus szépirodalom legfinomabb rétegeit, hanem büszkén és magabiztosan szólalhatok meg a saját egyéni hangomon ezen a csodálatos anyanyelven.",
                    }
                ],
                ["b2-mastery-synthesis"],
            ),
        ],
    },
}
