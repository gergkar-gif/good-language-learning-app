#!/usr/bin/env python3
"""
Hungarian B2 Core Unit 27: Borders, Kinship & Transborder Identity
Grammar skill: b2-concessive-conditionals
Vocab skill: b2-27-vocab
"""
from helpers_hu_b2_exercises import mc, match, fb, sb, dc, sw

UNIT_27 = {
    "unit_num": 27,
    "title": "Borders, Kinship & Transborder Identity",
    "grammar_summary": "Complex concessive conditionals in present, future, and past counterfactual contexts: emphatic concessives (még akkor is, ha...; akkor sem, ha...), past counterfactual concessives (még ha ... volna is), and detached/independent conditions (függetlenül attól, hogy...; eltekintve attól, hogy...).",
    "grammar_skill": "b2-concessive-conditionals",
    "vocab_skill": "b2-27-vocab",
    "theme": "Borders, kinship and transborder identity",
    "intro_body": [
        "A Kárpát-medencében az országhatárok és a nyelvi-kulturális közösségek határai a 20. század sorscsapásai nyomán elváltak egymástól. A határon túli magyar közösségek — Erdélyben, a Felvidéken, a Vajdaságban és Kárpátalján — az anyanyelvhez, a szülőföldhöz és a szellemi örökséghez való hűséggel őrizték meg identitásukat a változó történelmi korszakokban.",
        "Ebben a fejezetben elsajátíthatja a megengedő-feltételes mellékmondatok (concessive conditionals) összetett szerkezeteit: a nyomatékos megengedést (még akkor is, ha...; akkor sem, ha...), a múlt idejű ellenfaktikus hipotéziseket (még ha ... volna is), valamint a feltételektől függetlenítő formulákat (függetlenül attól, hogy...; eltekintve attól, hogy...). Sütő András lírai vallomása, az 'Anyám könnyű álmot ígér' nyomán pedig a szülőföld és az anyanyelv megtartó erejének mélységeit élheti át.",
    ],
    "classic_story": {
        "slug": "anyamkonnyualmotiger",
        "author": "Sütő András",
        "work": "Anyám könnyű álmot ígér (1970)",
        "title": "Szülőföld, anyanyelv és megtartó közösség",
        "summary": "Sütő András hazalátogatása szülőfalujába, Pusztakamarásra idős édesanyjához: szívszorító és felemelő beszélgetés a mezőségi szülőföldről, az anyanyelv megőrzéséről, a határok feletti összetartozásról és az emberi megmaradásról.",
        "characters": ["Sütő András", "Az édesanyja"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A mezőségi dombok felett csendesen ereszkedett le az alkonyat. A sáros kamarási utca végén álló szülői ház ablakában meleg fény derengett; Sütő András fáradtan lépte át a kapuküszöböt, leporolva kabátjáról a kolozsvári út porát.",
            },
            {
                "type": "dialogue",
                "speaker": "Az édesanyja",
                "text": "Megérkeztél hát, fiam! Gyere közelebb a kemencéhez, melegedj meg. Látom a szemeden a város gondját, a sok nehéz szót, amit magaddal hoztál. De itthon vagy, Pusztakamaráson; itt még a csend is másként beszél az emberhez.",
            },
            {
                "type": "dialogue",
                "speaker": "Sütő András",
                "text": "Nehéz idők járnak, édesanyám. A hivatalok szorításában, a fogyatkozó magyar iskolák láttán az ember szívét néha elfogja a csüggedés. Olyan érzés, mintha még akkor is védekeznünk kellene, ha semmi mást nem akarunk, csupán a saját anyanyelvünkön élni és dolgozni.",
            },
            {
                "type": "dialogue",
                "speaker": "Az édesanyja",
                "text": "Tudom én, fiam, láttam eleget az életemben. Változtak a hatalmak, jöttek-mentek az országhatárok, de a mezőségi föld meg a kamarásszéli szilvafák nem kérdezték, milyen zászló leng a vármegyeházán. Még ha nehezebb lett volna is a sorsunk, a tisztességünket és az imádságainkat akkor sem vehette el tőlünk senki.",
            },
            {
                "type": "dialogue",
                "speaker": "Sütő András",
                "text": "Igaza van, édesanyám. Az anyanyelv nem csupán szavak gyűjteménye, hanem az egyetlen igazi menedékünk. Függetlenül attól, hogy milyen törvényeket hoznak a távoli fővárosokban, a nyelvünk az a láthatatlan haza, amelyben mindannyian otthon vagyunk a határokon túl is.",
            },
            {
                "type": "dialogue",
                "speaker": "Az édesanyja",
                "text": "Úgy van, fiam. Egymásba kapaszkodva kell élni. Ha a szomszéd háza roskadozik, szalmát viszünk a tetejére; ha a gyermeke elindul a világba, anyanyelvi könyvet teszünk a tarisznyájába. A megmaradásunk titka az egyszerű emberség és a hűség a szülőföldünkhöz.",
            },
            {
                "type": "dialogue",
                "speaker": "Sütő András",
                "text": "Köszönöm a szavait, édesanyám. Innen, a szülői házból nézve a kisebbségi lét nem teher, hanem nemes küldetés: megőrizni és továbbadni azt a kincset, amit apáink ránk hagytak.",
            },
            {
                "type": "narration",
                "text": "Az édesanya rámosolygott, elsimította a fehér abroszt az asztalon, és csendesen így szólt: 'Most pedig aludj, fiam; anyád könnyű álmot ígér.' Kint a mezőségi dombok békésen pihentek a csillagos égbolt alatt, őrizve évszázadok néma hűségét.",
            },
        ],
        "reading_questions": [
            {
                "question": "Mit tekint Sütő András és édesanyja a határon túli közösségi megmaradás legfőbb zálogának?",
                "options": [
                    "Az anyanyelvhez való hűséget, a szülőföld szeretetét és az egymást segítő közösségi szolidaritást.",
                    "A hagyományok gyors feladását és a szülőfalu azonnali elhagyását a városi érvényesülésért.",
                    "A politikai eseményektől való teljes elzárkózást és a rokonokkal való kapcsolat megszakítását.",
                ],
                "correct": 0,
            },
            {
                "question": "Hogyan viszonyul az édesanya a történelmi változásokhoz és országhatárokhoz?",
                "options": [
                    "Nyugodt paraszti bölcsességgel fogadja őket: a hatalmak múlandók, de a föld, az emberség és a nyelv megtartó ereje állandó.",
                    "Pánikba esik, és azt követeli a fiától, hogy vándoroljon ki a tengerentúlra.",
                    "Csak a hatósági utasításokat követi, és lemond a saját családi emlékeiről.",
                ],
                "correct": 0,
            },
            {
                "question": "Mi a jelentősége a műben az anya szavainak: „anyád könnyű álmot ígér”?",
                "options": [
                    "A szülői ház biztonsága és az anyai szeretet megnyugvást, reményt és lelki békét ad a világ küzdelmei közepette.",
                    "Az anya altató teát készített gyógynövényekből a hosszú vacsora után.",
                    "Az anya figyelmezteti fiát, hogy korán reggel fel kell kelnie mezei munkára.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Even If: Concessive Conditionals (még akkor is, ha)",
            "grammar_label": "Emphatic concessive conditionals (még akkor is, ha...; akkor sem, ha...)",
            "goals": [
                "I can formulate assertive concessive conditions using még akkor is, ha...",
                "I can construct categorical negative conditions with akkor sem, ha...",
                "I can articulate persistent principles despite severe external adversity",
            ],
            "grammar_doc": {
                "slug": "emphatic-concessive-conditionals",
                "title": "Emphatic Concessive Conditionals: még akkor is, ha... and akkor sem, ha...",
                "text1_title": "Affirmative Concessive Conditionals: még akkor is, ha...",
                "text1": "Concessive conditional clauses contrast a hypothetical hurdle or unfavorable condition with an unyielding main assertion. In Hungarian, the emphatic correlative 'még akkor is..., ha...' ('even in that case..., if...' / 'even if...') places heightened communicative focus on the unconditional validity of the matrix clause: 'Megőrizzük az anyanyelvünket, még akkor is, ha a körülmények kedvezőtlenek' ('We will preserve our mother tongue, even if circumstances are unfavorable'). Notice the cataphoric demonstrative 'akkor is' in the main clause anticipating the subordinate 'ha' clause.",
                "text2_title": "Categorical Negation: akkor sem, ha...",
                "text2": "When the main clause expresses absolute refusal or impossibility under any conceivable circumstance, Hungarian employs the negative correlative 'akkor sem..., ha...' ('not even then..., if...' / 'not even if...'): 'A szülőföldet akkor sem hagyjuk el, ha komoly nehézségekkel kell szembenéznünk' ('We will not leave our homeland even if we must face grave difficulties'). The focus particle 'sem' reinforces the negation categorically across all conditional alternatives.",
                "table_title": "Concessive Conditional Correlatives",
                "table_rows": [
                    ["még akkor is, ha...", "Még akkor is kitartunk, ha nehéz a küzdelem. (We persevere even if the struggle is hard.)"],
                    ["akkor sem, ha...", "Akkor sem adjuk fel, ha mindenki lebeszél róla. (We will not give up even if everyone discourages us.)"],
                    ["még abban az esetben is, ha...", "Még abban az esetben is támogatjuk, ha késik az engedély. (We support it even in the event that the permit is delayed.)"],
                    ["akkor se(m)", "Nem mondunk le a jogainkról, akkor sem, ha fenyegetnek. (We won't surrender our rights, not even if threatened.)"],
                ],
                "examples": [
                    {
                        "spanish": "A közösség ragaszkodik az anyanyelvi oktatáshoz, még akkor is, ha csökken a támogatás.",
                        "english": "The community insists on mother-tongue education, even if subsidies decrease.",
                    },
                    {
                        "spanish": "A szülőföldünkről akkor sem mondunk le, ha a gazdasági válság elvándorlásra kényszerítene.",
                        "english": "We will not renounce our homeland even if the economic crisis would force emigration.",
                    },
                    {
                        "spanish": "Még akkor is megőrizzük a kulturális intézményeinket, ha egyedül kell fenntartanunk őket.",
                        "english": "We will preserve our cultural institutions even if we must maintain them alone.",
                    },
                    {
                        "spanish": "A kisebbségi jogok védelméről akkor sem feledkezhetünk meg, ha a politikai széljárás kedvezőtlen.",
                        "english": "We must not forget the protection of minority rights, not even if the political climate is unfavorable.",
                    },
                ],
                "tip": "Word order tip: the correlative phrase ('még akkor is' or 'akkor sem') can either precede the matrix verb as pre-verbal focus, or appear at the start of the entire sentence (e.g. 'Még akkor is megvédjük a jogainkat, ha...' vs. 'A jogainkat még akkor is megvédjük, ha...').",
            },
            "words": [
                {"lemma": "még akkor is", "translation": "even then / even so", "pos": "expression"},
                {"lemma": "akkor sem", "translation": "not even then / even if not", "pos": "expression"},
                {"lemma": "anyanyelv", "translation": "mother tongue / native language", "pos": "noun"},
                {"lemma": "megmaradás", "translation": "survival / persistence", "pos": "noun"},
                {"lemma": "kisebbségi lét", "translation": "minority existence / life as a minority", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the meaning of 'anyanyelv' in linguistic and cultural identity?",
                        [
                            "one's native language or mother tongue acquired from birth",
                            "a foreign language learned in adulthood for travel",
                            "a dialect spoken exclusively by sailors at sea",
                        ],
                        0,
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which phrase introduces categorical negative condition ('not even if...')?",
                        ["akkor sem, ha", "mivel", "mintha"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["még akkor is", "even then / even so"],
                            ["akkor sem", "not even then / not even if"],
                            ["anyanyelv", "mother tongue"],
                            ["megmaradás", "survival / persistence"],
                            ["kisebbségi lét", "minority existence"],
                        ],
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which correlative best completes: 'Hűségesek maradunk a szülőföldhöz, ____ a körülmények nehezek'?",
                        ["még akkor is, ha", "mivelhogy", "annak ellenére"],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the phrase expressing absolute refusal in: 'Nem hagyjuk el az iskolát, ____ bezárással fenyegetnek':",
                        ["akkor sem, ha", "csak akkor, ha", "feltéve, hogy"],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A diákok kitartóan tanulnak, ____ nehéz vizsgakövetelményekkel szembesülnek. (even if / even in that case if)",
                        "még akkor is, ha",
                        "The students study persistently, even if they face difficult exam requirements.",
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A közösség nem adja fel a kulturális autonómia követelését, ____ elutasítják a kérelmét. (not even if)",
                        "akkor sem, ha",
                        "The community will not give up demanding cultural autonomy, not even if its petition is rejected.",
                        ["b2-concessive-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Még", "akkor", "is", "kitartunk,", "ha", "nehéz", "a", "küzdelem."],
                        ["Még", "akkor", "is", "kitartunk,", "ha", "nehéz", "a", "küzdelem."],
                        "We persevere even if the struggle is difficult.",
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A határon túli magyarság számára a közösségi ____ legfontosabb bástyája az iskola. (persistence / survival)",
                        "megmaradás",
                        "For transborder Hungarians, the most important bastion of community survival is the school.",
                        ["b2-27-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kisebbségi", "lét", "sajátos", "kulturális", "felelősséget", "ró", "az", "értelmiségre."],
                        ["A", "kisebbségi", "lét", "sajátos", "kulturális", "felelősséget", "ró", "az", "értelmiségre."],
                        "Minority existence imposes a distinct cultural responsibility upon intellectuals.",
                        ["b2-27-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Tanár", "text": "Hogyan lehet fenntartani az anyanyelvi óvodát a kis létszámú szórványban?"},
                            {"speaker": "Szülő", "text": "____"},
                        ],
                        [
                            "Összefogással és elszántsággal; még akkor is megnyitjuk az osztályt, ha kevés gyermek jelentkezik.",
                            "Sehogy, azonnal be kell zárni az óvodát és lemondani a magyar szóról.",
                            "Akkor sem megyünk óvodába, ha ingyen adnak ebédet a faluban.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kutató", "text": "Hajlandók a helyi lakosok elhagyni a szülőföldjüket a jobb állásokért?"},
                            {"speaker": "Szociológus", "text": "____"},
                        ],
                        [
                            "A legtöbben ragaszkodnak a gyökereikhez: sokan akkor sem költöznének el, ha máshol magasabb fizetést kapnának.",
                            "Mindenki elmegy holnap reggel, mert senkit sem érdekel a szülőföld.",
                            "Még akkor is elmennek, ha senki sem hívta őket sehova.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence with 'még akkor is, ha' asserting fidelity to mother-tongue education.",
                                "answer": "Az anyanyelvi iskolához ragaszkodnunk kell, még akkor is, ha jelentős adminisztratív akadályok merülnek fel.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence with 'akkor sem, ha' rejecting the abandonment of cultural heritage.",
                                "answer": "A történelmi hagyományainkról akkor sem mondhatunk le, ha a modern világ gyors asszimilációra ösztönöz.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A színház társulata folytatja a munkát, ____ szűkülnek az anyagi támogatások. (even if / even in that case if)",
                        "még akkor is, ha",
                        "The theatre company continues its work, even if financial subsidies diminish.",
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which compound phrase refers to the historical experience and challenges of living as an ethnic minority?",
                        ["kisebbségi lét", "városi élet", "szabadidő"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Even If It Had Been (még ha ... volna is)",
            "grammar_label": "Counterfactual concessive past conditional (még ha ... volna is)",
            "goals": [
                "I can form counterfactual concessive past conditionals with még ha ... volna is",
                "I can correctly position the clitic particle is after the conditional auxiliary volna",
                "I can analyze retrospective historical alternatives and cultural resilience",
            ],
            "grammar_doc": {
                "slug": "counterfactual-concessive-conditionals",
                "title": "Counterfactual Concessive Conditionals: még ha ... volna is",
                "text1_title": "Past Counterfactual Concessives: Structure and Meaning",
                "text1": "To reflect on hypothetical past scenarios that did not occur, Hungarian constructs counterfactual concessive conditionals combining 'még ha' ('even if / even though') with the past conditional (past participle + 'volna') and the postposed focus particle 'is': 'Még ha több támogatást kaptunk volna is, a demográfiai fogyást nem lehetett volna azonnal megállítani' ('Even if we had received more support, demographic decline could not have been halted immediately').",
                "text2_title": "Syntax of the Clitic 'is' in Conditional Verb Phrases",
                "text2": "The focus particle 'is' in past concessive clauses adheres to strict structural placement: it cliticizes directly to the auxiliary 'volna' ('tudtuk volna is' - even had we known; 'lett volna is' - even if there had been). If the verb has a verbal prefix, the prefix detaches when focus or negation is present: 'Még ha el is költözött volna...' ('Even if he had moved away...'). This past concessive structure is essential for high-register historical analysis and retrospective political reflection.",
                "table_title": "Counterfactual Concessive Patterns",
                "table_rows": [
                    ["még ha + verb-volna is", "Még ha tudta volna is az igazságot, nem szólhatott. (Even had he known the truth, he couldn't speak.)"],
                    ["még ha lett volna is", "Még ha lett volna is más választás, ezt az utat járták volna. (Even if there had been another choice, they would have walked this path.)"],
                    ["még ha el is + verb-volna", "Még ha el is fogadták volna a törvényt, nem segített volna. (Even if they had accepted the law, it wouldn't have helped.)"],
                    ["akkor sem ... volna", "Akkor sem adta volna fel, ha egyedül marad. (He wouldn't have given up even had he remained alone.)"],
                ],
                "examples": [
                    {
                        "spanish": "Még ha a határokat megváltoztatták volna is, a kulturális kötelékek nem szakadtak volna meg.",
                        "english": "Even if the borders had been changed, cultural bonds would not have severed.",
                    },
                    {
                        "spanish": "Még ha nehezebb lett volna is a sorsuk, az anyanyelvükhöz akkor is hűségesek maradtak volna.",
                        "english": "Even if their fate had been harder, they still would have remained faithful to their mother tongue.",
                    },
                    {
                        "spanish": "A közösség akkor sem asszimilálódott volna, ha még szigorúbb nyelvtörvényeket vezetnek be.",
                        "english": "The community would not have assimilated even if stricter language laws had been introduced.",
                    },
                    {
                        "spanish": "Még ha el is veszítették volna intézményeiket, a családi hagyomány akkor is megőrizte volna az identitást.",
                        "english": "Even if they had lost their institutions, family tradition still would have preserved their identity.",
                    },
                ],
                "tip": "Notice the position of 'is': write 'ha megpróbálták volna is' or 'ha meg is próbálták volna'. Never place 'is' before 'ha' in this counterfactual past construction (avoid *is ha megpróbálták volna).",
            },
            "words": [
                {"lemma": "még ha", "translation": "even if / even though", "pos": "conjunction"},
                {"lemma": "volna is", "translation": "even had it been / even if it were", "pos": "expression"},
                {"lemma": "asszimiláció", "translation": "assimilation", "pos": "noun"},
                {"lemma": "kettős állampolgárság", "translation": "dual citizenship", "pos": "expression"},
                {"lemma": "határrevízió", "translation": "border revision", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'asszimiláció' mean in sociolinguistics and minority studies?",
                        [
                            "the gradual absorption of a minority group into the dominant majority culture and language",
                            "the legal acquisition of commercial real estate abroad",
                            "an official treaty demarcating customs inspection zones",
                        ],
                        0,
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'kettős állampolgárság'?",
                        [
                            "holding citizenship in two sovereign states simultaneously",
                            "a special driver's license valid in neighboring counties",
                            "a passport reserved exclusively for diplomatic envoys",
                        ],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["még ha", "even if / even though"],
                            ["volna is", "even had it been"],
                            ["asszimiláció", "assimilation"],
                            ["kettős állampolgárság", "dual citizenship"],
                            ["határrevízió", "border revision"],
                        ],
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which phrase correctly completes: '____ nehezebb lett volna is a helyzet, a szülők nem adták volna fel'?",
                        ["Még ha", "Mivelhogy", "Csak akkor"],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Where does the particle 'is' attach in the counterfactual past predicate 'tudta volna'?",
                        ["tudta volna is", "is tudta volna", "tudta is volna"],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Még ha figyelmeztették ____ a döntéshozókat, valószínűleg nem változtattak volna az irányvonalon. (even had they been; volna is)",
                        "volna is",
                        "Even had they warned the decision-makers, they likely would not have changed the course.",
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A lakosság akkor sem hagyta volna el a falut, ____ felajánlottak volna nekik új lakásokat a városban. (even if)",
                        "még ha",
                        "The population would not have left the village even if they had been offered new flats in the city.",
                        ["b2-concessive-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Még", "ha", "nehéz", "lett", "volna", "is,", "kitartottak", "volna."],
                        ["Még", "ha", "nehéz", "lett", "volna", "is,", "kitartottak", "volna."],
                        "Even if it had been difficult, they would have persevered.",
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A természetes nyelvi ____ veszélye különösen a szórványban élő fiatalokat fenyegeti. (assimilation)",
                        "asszimiláció",
                        "The danger of natural linguistic assimilation threatens especially youth living in scattered diaspora.",
                        ["b2-27-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kettős", "állampolgárság", "megerősítette", "a", "határon", "túli", "kapcsolatokat."],
                        ["A", "kettős", "állampolgárság", "megerősítette", "a", "határon", "túli", "kapcsolatokat."],
                        "Dual citizenship strengthened transborder connections.",
                        ["b2-27-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Történész", "text": "Megmenthető lett volna a történelmi együttélés a határok meghúzása után?"},
                            {"speaker": "Professzor", "text": "____"},
                        ],
                        [
                            "Még ha békésebb lett volna is az átmenet, a nacionalista törekvések akkor is súlyos feszültséget okoztak volna.",
                            "Semmi feszültség nem volt, mert a határok nem érdekeltek senkit.",
                            "Még ha mindenki elköltözött volna is, üresen hagyták volna az egész országot.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kisebbségkutató", "text": "Hogyan értékelhető a kettős állampolgárság hatása a szülőföldön maradásra?"},
                            {"speaker": "Elemző", "text": "____"},
                        ],
                        [
                            "Közjogi köteléket teremtett az anyaországgal, megerősítve az identitást még a nehezebb gazdasági körülmények között is.",
                            "Nem jelentett semmit, mert senki sem igényelte az állampolgárságot.",
                            "A határrevízió helyett mindenki azonnal eladta az útlevelét.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a counterfactual sentence with 'még ha ... volna is' reflecting on community survival.",
                                "answer": "Még ha bezárták volna is az iskolát, a családok akkor is megőrizték volna az anyanyelvi kultúrát.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'asszimiláció' and 'kettős állampolgárság' in sociolinguistic analysis.",
                                "answer": "A kulturális támogatások és a kettős állampolgárság intézménye lassíthatja a nyelvvesztést és a spontán asszimilációt.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A kutatók szerint a színház akkor sem zárt volna be, ____ teljesen megvonták volna az állami forrásokat. (even if; még ha)",
                        "még ha",
                        "According to researchers, the theatre would not have closed even if state funds had been completely withdrawn.",
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which legal institution allows individuals to retain ties with their kin-state while residing in their homeland?",
                        ["kettős állampolgárság", "határrevízió", "kényszerkitelepítés"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Regardless of Whether (függetlenül attól, hogy)",
            "grammar_label": "Independent condition markers (függetlenül attól, hogy...; attól eltekintve, hogy...)",
            "goals": [
                "I can formulate independent premises using függetlenül attól, hogy...",
                "I can set aside specific conditions or exceptions with attól eltekintve, hogy...",
                "I can argue transborder cultural unity across diverse geopolitical frameworks",
            ],
            "grammar_doc": {
                "slug": "independent-condition-markers",
                "title": "Detached Conditionals: függetlenül attól, hogy... and eltekintve attól, hogy...",
                "text1_title": "Unconditional Framing: függetlenül attól, hogy...",
                "text1": "In high-register political, sociological, and constitutional discourse, the compound connector 'függetlenül attól, hogy...' ('regardless of whether / irrespective of the fact that...') asserts an outcome or principle that holds true completely detached from varying contingencies: 'Függetlenül attól, hogy melyik országban élünk, az anyanyelvünk összeköt bennünket' ('Regardless of which country we live in, our mother tongue unites us'). Note the ablative case demonstrative 'attól' governed by the postposition 'függetlenül'.",
                "text2_title": "Exclusions and Concessive Exceptions: eltekintve attól, hogy...",
                "text2": "'Eltekintve attól, hogy...' ('apart from the fact that... / setting aside that...') is used to isolate a known factor or constraint in order to focus the argument on broader realities: 'Eltekintve attól, hogy a jogi környezet összetett, a kulturális együttműködés virágzik' ('Apart from the fact that the legal environment is complex, cultural cooperation is flourishing'). Both expressions allow authors to elevate an argument above territorial or bureaucratic contingencies.",
                "table_title": "Detached Condition Connectors",
                "table_rows": [
                    ["függetlenül attól, hogy...", "Függetlenül attól, hogy hol húzódnak a határok... (Regardless of where the borders lie...)"],
                    ["attól eltekintve, hogy...", "Attól eltekintve, hogy nehéz a helyzet... (Apart from the fact that the situation is hard...)"],
                    ["mindattól függetlenül, hogy...", "Mindattól függetlenül, hogy kevés a forrás... (Notwithstanding that resources are scarce...)"],
                    ["eltekintve vmitől", "Eltekintve a bürokratikus akadályoktól... (Apart from bureaucratic obstacles...)"],
                ],
                "examples": [
                    {
                        "spanish": "Függetlenül attól, hogy melyik állam polgárai vagyunk, a magyar nemzet kulturális egységet alkot.",
                        "english": "Regardless of which state's citizens we are, the Hungarian nation constitutes a cultural unity.",
                    },
                    {
                        "spanish": "Attól eltekintve, hogy a távolságok nagyok, a határon túli színházak rendszeresen vendégszerepelnek Budapesten.",
                        "english": "Apart from the fact that distances are large, transborder theatres regularly guest-perform in Budapest.",
                    },
                    {
                        "spanish": "Függetlenül attól, hogy a törvény mikor lép hatályba, a közösség folytatja az anyanyelvi oktatást.",
                        "english": "Regardless of when the statute takes effect, the community continues mother-tongue education.",
                    },
                    {
                        "spanish": "Attól eltekintve, hogy az elcsatolás történelmi sebeket hagyott, a jelen a megbékélésre épül.",
                        "english": "Apart from the fact that annexation left historical wounds, the present is built on reconciliation.",
                    },
                ],
                "tip": "Syntactic precision: ensure 'attól' is in the ablative case (-tól/-től) in both 'függetlenül attól' and 'eltekintve attól'. The subordinate clause must be introduced with 'hogy'.",
            },
            "words": [
                {"lemma": "függetlenül attól", "translation": "regardless of the fact that", "pos": "expression"},
                {"lemma": "eltekintve attól", "translation": "apart from the fact that", "pos": "expression"},
                {"lemma": "szülőföld", "translation": "homeland / native soil", "pos": "noun"},
                {"lemma": "kulturális kötelék", "translation": "cultural tie / bond", "pos": "expression"},
                {"lemma": "elcsatolás", "translation": "annexation / severance / detachment", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'kulturális kötelék' across borders?",
                        [
                            "intangible cultural, linguistic, and emotional ties connecting dispersed communities",
                            "a customs tariff levied on imported folk embroidery",
                            "a concrete highway barrier erected along border checkpoints",
                        ],
                        0,
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which phrase introduces a premise detached from contingencies ('regardless of...')?",
                        ["függetlenül attól, hogy", "annak következtében, hogy", "azzal a céllal, hogy"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["függetlenül attól", "regardless of the fact that"],
                            ["eltekintve attól", "apart from the fact that"],
                            ["szülőföld", "homeland / native soil"],
                            ["kulturális kötelék", "cultural tie / bond"],
                            ["elcsatolás", "annexation / severance"],
                        ],
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case suffix is governed by 'függetlenül' on the demonstrative 'az'?",
                        ["ablative: attól", "instrumental: azzal", "dative: annak"],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the connector expressing an exception set aside in argumentation:",
                        ["eltekintve attól, hogy", "köszönhetően annak, hogy", "miután"],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A nemzet egysége fennmarad, ____ milyen államhatárok választják el az embereket. (regardless of the fact that)",
                        "függetlenül attól, hogy",
                        "The unity of the nation persists, regardless of what state borders separate the people.",
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "____ a bürokratikus akadályok nehezítik az együttműködést, a civil kapcsolatok virágoznak. (Apart from the fact that)",
                        "Attól eltekintve, hogy",
                        "Apart from the fact that bureaucratic obstacles hinder cooperation, civic relations are flourishing.",
                        ["b2-concessive-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Függetlenül", "attól,", "hogy", "hol", "élünk,", "összetartozunk."],
                        ["Függetlenül", "attól,", "hogy", "hol", "élünk,", "összetartozunk."],
                        "Regardless of where we live, we belong together.",
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A határon túli írók műveiben a hűség a ____ iránt központi motívumként jelenik meg. (homeland / native soil)",
                        "szülőföld",
                        "In the works of transborder writers, fidelity toward the homeland appears as a central motif.",
                        ["b2-27-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "közös", "kulturális", "kötelékek", "erősebbnek", "bizonyultak", "a", "határoknál."],
                        ["A", "közös", "kulturális", "kötelékek", "erősebbnek", "bizonyultak", "a", "határoknál."],
                        "The shared cultural ties proved stronger than the borders.",
                        ["b2-27-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Hogyan működhet a határokon átnyúló egyetemi hálózat?"},
                            {"speaker": "Rektor", "text": "____"},
                        ],
                        [
                            "Függetlenül attól, hogy a partnerek különböző országokban működnek, a közös tudományos és anyanyelvi célok egységbe fogják őket.",
                            "Nem működhet sehogy, mert a határokon tilos könyveket átvinni.",
                            "Eltekintve attól, hogy minden egyetem bezárt, senki sem tanul semmit.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Diplomata", "text": "Befolyásolják a politikai viták a szomszédos népek kulturális cseréjét?"},
                            {"speaker": "Kulturális attasé", "text": "____"},
                        ],
                        [
                            "Attól eltekintve, hogy a retorika néha feszült, az intézmények közötti szakmai kötelékek zavartalanul működnek.",
                            "Minden kapcsolatot megszakítottunk a szomszédokkal a tegnapi választások miatt.",
                            "Függetlenül attól, hogy nincs kultúra, a diplomácia felesleges dolog.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'függetlenül attól, hogy' asserting linguistic unity across borders.",
                                "answer": "Függetlenül attól, hogy a történelem határokat emelt közénk, az anyanyelv közös otthont teremt számunkra.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence with 'eltekintve attól, hogy' analyzing cross-border economic ties.",
                                "answer": "Eltekintve attól, hogy az adminisztratív eljárások időigényesek, a határ menti régiók gazdasága egyre szorosabban összefonódik.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A színházi fesztivál óriási sikert aratott, ____ a rossz időjárás miatt elmaradt a szabadtéri megnyitó. (apart from the fact that)",
                        "attól eltekintve, hogy",
                        "The theatre festival achieved enormous success, apart from the fact that the open-air opening was cancelled due to bad weather.",
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes enduring bonds of tradition, language, and arts between communities?",
                        ["kulturális kötelék", "vasúti sín", "vámnyilatkozat"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Living in Two Languages",
            "grammar_label": "Bilingualism, cross-border cultural ties, and mother tongue preservation",
            "goals": [
                "I can analyze the cognitive and social dimensions of bilingualism (kétnyelvűség)",
                "I can evaluate language preservation strategies in scattered diaspora communities (szórvány)",
                "I can advocate mother-tongue educational rights using concessive conditional reasoning",
            ],
            "grammar_doc": {
                "slug": "bilingualism-and-language-preservation",
                "title": "Living in Two Languages: Bilingualism and Cultural Resilience",
                "text1_title": "Bilingual Dynamics: kétnyelvűség and anyanyelvi oktatás",
                "text1": "For transborder Hungarian communities, bilingualism ('kétnyelvűség') is a multifaceted reality: it represents an enriching cultural asset while posing risks of language attrition if public life lacks institutional support. The foundation of linguistic survival is comprehensive mother-tongue education ('anyanyelvi oktatás') from kindergarten through university, allowing individuals to attain academic register mastery in their mother tongue while speaking the state language fluently.",
                "text2_title": "Diaspora Challenges: nyelvmegőrzés and the szórvány",
                "text2": "In scattered minority enclaves ('szórvány'), where Hungarians constitute small minorities in predominantly majority environments, language preservation ('nyelvmegőrzés') requires robust institutional networks ('kulturális intézményrendszer'). In public debates, concessive structures emphasize that cultural investments in diaspora regions remain essential even if student numbers are modest: 'Még akkor is támogatni kell a szórványkollégiumokat, ha kevesebb diák él a kistelepüléseken' ('Scattered diaspora boarding schools must be supported even if fewer students live in small villages').",
                "table_title": "Sociolinguistic Terminology",
                "table_rows": [
                    ["kétnyelvűség", "két nyelv egyidejű és magas szintű ismerete (simultaneous high-level command of two languages)"],
                    ["anyanyelvi oktatás", "a tanulás joga az anyanyelven minden képzési szinten (right to learn in native language at all levels)"],
                    ["szórvány", "többségi környezetben elszórtan élő kisebbség (minority living dispersed in majority environment / enclave)"],
                    ["nyelvmegőrzés", "az anyanyelv aktív használatának fenntartása (maintaining active use of native language)"],
                ],
                "examples": [
                    {
                        "spanish": "A kétnyelvűség nem hátrány, hanem felbecsülhetetlen intellektuális és kulturális gazdagság.",
                        "english": "Bilingualism is not a disadvantage, but an invaluable intellectual and cultural richness.",
                    },
                    {
                        "spanish": "A szórványvidékeken működő magyar kollégiumok a megmaradás legfontosabb mentsvárai.",
                        "english": "Hungarian boarding schools operating in diaspora regions are the most important safe harbors of survival.",
                    },
                    {
                        "spanish": "A hatékony nyelvmegőrzéshez a családi környezet mellett stabil anyanyelvi oktatásra van szükség.",
                        "english": "For effective language preservation, stable mother-tongue education is needed alongside the family environment.",
                    },
                    {
                        "spanish": "A határon túli kulturális intézményrendszer biztosítja a közösségi élet folytonosságát.",
                        "english": "The transborder cultural institutional network ensures the continuity of community life.",
                    },
                ],
                "tip": "Distinguish between 'tömbmagyarság' (compact majority-Hungarian regions like Székelyföld) and 'szórvány' (scattered minority diaspora where Hungarian speakers are a numerical minority).",
            },
            "words": [
                {"lemma": "kétnyelvűség", "translation": "bilingualism", "pos": "noun"},
                {"lemma": "nyelvmegőrzés", "translation": "language preservation", "pos": "noun"},
                {"lemma": "anyanyelvi oktatás", "translation": "mother-tongue education", "pos": "expression"},
                {"lemma": "kulturális intézményrendszer", "translation": "cultural institutional network", "pos": "expression"},
                {"lemma": "szórvány", "translation": "scattered minority community / diaspora enclave", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'szórvány' describe in Hungarian demographics and sociolinguistics?",
                        [
                            "a minority population living dispersed in small numbers within a majority environment",
                            "a dense, compact demographic majority living in the capital city",
                            "a mountainous uninhabited wilderness area with no settlements",
                        ],
                        0,
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which phrase denotes institutional schooling conducted in the student's native language?",
                        ["anyanyelvi oktatás", "idegen nyelvi kurzus", "esti tanfolyam"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["kétnyelvűség", "bilingualism"],
                            ["nyelvmegőrzés", "language preservation"],
                            ["anyanyelvi oktatás", "mother-tongue education"],
                            ["kulturális intézményrendszer", "cultural institutional network"],
                            ["szórvány", "scattered minority community"],
                        ],
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Why is 'anyanyelvi oktatás' critical for language preservation in diaspora areas?",
                        [
                            "Because it ensures literacy and academic register development in the native language.",
                            "Because it completely bans speaking any other languages at home.",
                            "Because it lowers exam requirements for graduation.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence correctly combines concessive conditions with diaspora education?",
                        [
                            "A szórványiskolákat még akkor is fenn kell tartani, ha kis létszámmal működnek.",
                            "A szórványiskolákat mivel senki sem jár oda ezért zárjuk be.",
                            "Ha a szórványban nem lett volna iskola mert mindenki hazament volna tegnap.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A természetes ____ mindkét nyelv magas szintű elsajátítását teszi lehetővé a gyermekek számára. (bilingualism)",
                        "kétnyelvűség",
                        "Natural bilingualism enables children to acquire a high-level mastery of both languages.",
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A civil alapítvány célja a hatékony ____ támogatása a legkisebb falvakban is. (language preservation)",
                        "nyelvmegőrzés",
                        "The goal of the civil foundation is supporting effective language preservation in the smallest villages as well.",
                        ["b2-concessive-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Az", "anyanyelvi", "oktatás", "minden", "kisebbség", "alapvető", "joga."],
                        ["Az", "anyanyelvi", "oktatás", "minden", "kisebbség", "alapvető", "joga."],
                        "Mother-tongue education is a fundamental right of every minority.",
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A Mezőségen és Dél-Erdélyben a magyar lakosság nagy része ____ él. (in diaspora / scattered community)",
                        "szórványban",
                        "In the Mezőség and Southern Transylvania, a large part of the Hungarian population lives in scattered diaspora.",
                        ["b2-27-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "stabil", "kulturális", "intézményrendszer", "garantálja", "a", "megmaradást."],
                        ["A", "stabil", "kulturális", "intézményrendszer", "garantálja", "a", "megmaradást."],
                        "A stable cultural institutional network guarantees survival.",
                        ["b2-27-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Oktatáspolitikus", "text": "Érdemes-e kis létszámú magyar tagozatokat fenntartani a szórványban?"},
                            {"speaker": "Iskolaigazgató", "text": "____"},
                        ],
                        [
                            "Igen, mert az anyanyelvi oktatás nélkül a nyelvvesztés megállíthatatlan lenne; még akkor is megéri, ha költséges.",
                            "Nem érdemes, mert a kis iskolák túl sok fűtést igényelnek télen.",
                            "Akkor sem nyitunk iskolát, ha ezer gyermek jelentkezik beiratkozásra.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Egyetemi hallgató", "text": "Hogyan élik meg a határon túli fiatalok a kétnyelvűséget?"},
                            {"speaker": "Pszicholingvista", "text": "____"},
                        ],
                        [
                            "Természetes adottságként: rugalmasan mozognak mindkét kultúrában, megőrizve az anyanyelvi identitásukat.",
                            "Nagy teherként, mert az agy nem képes egyszerre két nyelvet befogadni.",
                            "Függetlenül a nyelvtől, a fiatalok már csak emotikonokkal beszélgetnek.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'anyanyelvi oktatás' arguing for constitutional minority protection.",
                                "answer": "Az államnak kötelessége biztosítani a minőségi anyanyelvi oktatást a bölcsődétől az egyetemig.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'szórvány' and 'nyelvmegőrzés' in cultural strategy.",
                                "answer": "A szórványban élő közösségek számára a nyelvmegőrzés a kulturális túlélés mindennapos záloga.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A határon túli magyarság intézményei a kulturális ____ alapköveiként szolgálnak. (language preservation)",
                        "nyelvmegőrzés",
                        "The institutions of transborder Hungarians serve as cornerstones of cultural language preservation.",
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes dispersed minority populations living in numerical minority outside compact ethnic blocks?",
                        ["szórvány", "tömb", "főváros"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Personal Narratives of Belonging",
            "grammar_label": "Writing a narrative essay on homeland and transborder identity",
            "goals": [
                "I can synthesize transborder personal reflections in an elegant essayistic register",
                "I can interweave past counterfactual and present concessive clauses smoothly in narration",
                "I can articulate multi-layered identity, memory, and geographic belonging",
            ],
            "grammar_doc": {
                "slug": "narratives-of-belonging-and-identity",
                "title": "Narratives of Belonging: Identity, Memory, and Homeland",
                "text1_title": "Multi-Layered Identity: többes identitás and hovatartozás",
                "text1": "Personal narratives written by transborder authors (such as Sütő András, Bodor Ádám, or Grendel Lajos) portray national identity not as an exclusive dogma, but as a multi-layered belonging ('többes identitás'). A person can feel deep civic loyalty to their home region, active connection to local multiethnic culture, and profound spiritual belonging ('hovatartozás') to the wider Hungarian linguistic and literary universe: 'Az identitás nem elválaszt, hanem gazdagabbá teszi a világot' ('Identity does not separate, but enriches the world').",
                "text2_title": "Sustaining Ties and National Consciousness: kötődés and megtartó erő",
                "text2": "In essayistic writing, authors weave emotional attachment ('kötődés') with the concept of sustaining community force ('megtartó erő') and cultural consciousness ('nemzettudat'). Sophisticated syntax alternates between present concessives ('még akkor is..., ha...') to express ongoing commitment, and counterfactuals ('még ha másként történt volna is...') to reflect on historical memory, creating a nuanced, moving synthesis of belonging.",
                "table_title": "Essayistic and Narrative Vocabulary",
                "table_rows": [
                    ["hovatartozás", "egyéni és közösségi önazonosság (personal and communal sense of affiliation / belonging)"],
                    ["többes identitás", "egymást nem kizáró, rétegzett azonosságtudat (layered, non-exclusive identity)"],
                    ["megtartó erő", "a közösség túlélését biztosító szellemi támasz (spiritual anchor ensuring community survival)"],
                    ["nemzettudat", "a nemzeti közösséghez való tudatos tartozás (conscious belonging to the national community)"],
                ],
                "examples": [
                    {
                        "spanish": "A szülőföldhöz való ragaszkodás a személyes identitásunk legerősebb megtartó ereje.",
                        "english": "Attachment to the homeland is the strongest sustaining force of our personal identity.",
                    },
                    {
                        "spanish": "A modern határon túli értelmiség gyakran él meg többes identitást a két kultúra metszéspontjában.",
                        "english": "Modern transborder intellectuals often experience multiple identity at the intersection of two cultures.",
                    },
                    {
                        "spanish": "Függetlenül a politikai változásoktól, a hovatartozás érzése mélyen gyökerezik a szülői házban.",
                        "english": "Regardless of political changes, the sense of belonging is deeply rooted in the parental home.",
                    },
                    {
                        "spanish": "Az irodalmi művek generációkon át táplálták és ébren tartották a nemzettudatot.",
                        "english": "Literary works nourished and kept awake national consciousness across generations.",
                    },
                ],
                "tip": "In reflective narrative essays, balance abstract analytical terminology ('nemzettudat', 'hovatartozás') with concrete sensory imagery of place ('a szülői ház kemencéje', 'a mezőségi dombok pora') to create emotional authenticity.",
            },
            "words": [
                {"lemma": "hovatartozás", "translation": "belonging / affiliation / identity", "pos": "noun"},
                {"lemma": "többes identitás", "translation": "multiple identity", "pos": "expression"},
                {"lemma": "kötődés", "translation": "attachment / emotional bond", "pos": "noun"},
                {"lemma": "megtartó erő", "translation": "sustaining force / cohesive power", "pos": "expression"},
                {"lemma": "nemzettudat", "translation": "national consciousness", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'többes identitás' in contemporary European sociology?",
                        [
                            "possessing harmoniously integrated cultural, regional, and national identities simultaneously",
                            "forgetting one's mother tongue in order to learn a new language",
                            "carrying multiple forged identification documents across borders",
                        ],
                        0,
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which phrase denotes the spiritual and communal anchor that ensures group survival?",
                        ["megtartó erő", "vásárlóerő", "légellenállás"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["hovatartozás", "belonging / affiliation"],
                            ["többes identitás", "multiple identity"],
                            ["kötődés", "attachment / emotional bond"],
                            ["megtartó erő", "sustaining force"],
                            ["nemzettudat", "national consciousness"],
                        ],
                        ["b2-27-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence best exemplifies an essayistic reflection on transborder belonging?",
                        [
                            "A szülőföldhöz fűződő mély kötődés még akkor is megtartja a közösséget, ha a határok elválasztanak.",
                            "A határok miatt nem megyünk sehova és nem olvasunk semmit.",
                            "Ha nem lett volna hovatartozás mert mindenki elfelejtett beszélni.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the term for conscious belonging and loyalty to one's linguistic and cultural nation:",
                        ["nemzettudat", "fegyelem", "közlekedés"],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A szülőfalumhoz fűződő mély ____ semmilyen idegen nagyváros sem tudta elhalványítani. (emotional bond / attachment)",
                        "kötődést",
                        "No foreign metropolis could dim the deep attachment tying me to my native village.",
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Az anyanyelv és az irodalom a legfőbb ____ jelentik a határon túli közösségek számára. (sustaining force; plural/possessive: megtartó erőt)",
                        "megtartó erőt",
                        "The mother tongue and literature represent the primary sustaining force for transborder communities.",
                        ["b2-concessive-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "közös", "emlékek", "erősítik", "a", "nemzettudatot", "és", "az", "összetartozást."],
                        ["A", "közös", "emlékek", "erősítik", "a", "nemzettudatot", "és", "az", "összetartozást."],
                        "Shared memories strengthen national consciousness and solidarity.",
                        ["b2-concessive-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A határon túli fiatalok sokszor gazdag ____ élnek meg a régióban. (multiple identity)",
                        "többes identitást",
                        "Transborder youth often experience a rich multiple identity in the region.",
                        ["b2-27-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kulturális", "hovatartozás", "mélyebb", "minden", "adminisztratív", "szabályozásnál."],
                        ["A", "kulturális", "hovatartozás", "mélyebb", "minden", "adminisztratív", "szabályozásnál."],
                        "Cultural belonging is deeper than any administrative regulation.",
                        ["b2-27-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Esszéíró", "text": "Hogyan fogalmazná meg a szülőföldhöz fűződő viszonyát a határon túli létben?"},
                            {"speaker": "Író", "text": "____"},
                        ],
                        [
                            "A szülőföld nem csupán földrajz, hanem lelki otthon; még akkor is oda vágyom vissza, ha a világ túlsó felén élek.",
                            "A szülőföld nem érdekel senkit, mert a repülőjegyek túl olcsók lettek.",
                            "Akkor sem mennék vissza, ha palotát építenének nekem a faluban.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kulturális riporter", "text": "Mi ad erőt az elszigetelt szórványban élőknek?"},
                            {"speaker": "Lelkész", "text": "____"},
                        ],
                        [
                            "A hit, a családi hagyományok megtartó ereje és a tudat, hogy nem vagyunk egyedül a világban.",
                            "Semmi sem ad erőt, mindenki teljesen elkeseredett.",
                            "A többes identitás helyett inkább senki sem gondol semmire.",
                        ],
                        0,
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an essayistic sentence using 'hovatartozás' and 'még akkor is, ha' regarding cultural roots.",
                                "answer": "A kulturális hovatartozás érzése megingathatatlan marad, még akkor is, ha az élet messze sodor a szülőföldtől.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an essayistic sentence with 'megtartó erő' praising the role of mother tongue in literature.",
                                "answer": "Az anyanyelv a legnagyobb megtartó erő, amely évszázadokon át biztosította nemzetünk szellemi folytonosságát.",
                            }
                        ],
                        ["b2-concessive-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A határon túli szerző esszéjében a szülőföld iránti mély ____ vallott megindító őszinteséggel. (emotional bond / attachment)",
                        "kötődésről",
                        "In his essay, the transborder author testified with moving sincerity to his deep attachment toward his homeland.",
                        ["b2-concessive-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes an individual's conscious cultural and communal affiliation?",
                        ["hovatartozás", "érdektelenség", "ideiglenesség"],
                        0,
                        ["b2-27-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can master emphatic concessive conditionals (még akkor is, ha...; akkor sem, ha...)",
            "I can formulate counterfactual concessive past conditionals (még ha ... volna is)",
            "I can employ independent condition markers (függetlenül attól, hogy...) in analytical essays on transborder identity",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["anyanyelv", "mother tongue"],
                    ["megmaradás", "survival / persistence"],
                    ["kettős állampolgárság", "dual citizenship"],
                    ["szülőföld", "homeland / native soil"],
                    ["kötődés", "attachment / bond"],
                ],
                ["b2-27-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'kisebbségi lét' embody in Central European history?",
                [
                    "the historical experience, legal struggles, and cultural endurance of national communities living outside their kin-state",
                    "a short-term recreational trip to mountain tourist resorts",
                    "a temporary commercial license issued to foreign merchants",
                ],
                0,
                ["b2-27-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly illustrates a counterfactual past concessive condition?",
                [
                    "Még ha nehezebb lett volna is a helyzet, a szülők akkor sem adták volna fel az anyanyelvi iskolát.",
                    "Még ha nehezebb lett volna is mert senki sem akart iskolába menni tegnap.",
                    "Akkor sem mennének iskolába ha ma reggel süt a nap kint az udvaron.",
                ],
                0,
                ["b2-concessive-conditionals"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A civil kezdeményezés célja a kulturális ____ megerősítése az anyaország és a diaszpóra között. (cultural ties / bonds)",
                "kötelékek",
                "The goal of the civic initiative is strengthening cultural ties between the kin-state and the diaspora.",
                ["b2-27-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A közösség ragaszkodik az anyanyelvéhez, ____ hátrányos megkülönböztetéssel kell szembenéznie. (even if / even in that case if)",
                "még akkor is, ha",
                "The community insists on its mother tongue, even if it must face adverse discrimination.",
                ["b2-concessive-conditionals"],
            ),
            fb(
                "grammar",
                "recall",
                "A lakosság a nehéz időkben sem hagyta el a szülőfaluját, ____ felajánlottak volna jobb lakásokat máshol. (even if; még ha)",
                "még ha",
                "The population did not leave their native village in difficult times either, even if they had been offered better flats elsewhere.",
                ["b2-concessive-conditionals"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'függetlenül attól, hogy' correctly detaches the principle from borders:",
                [
                    "Függetlenül attól, hogy melyik országban élünk, az anyanyelvünk közös szellemi hazát teremt számunkra.",
                    "Függetlenül attól, hogy reggel hét óra van, megittuk a tejet a pohárból tegnap.",
                    "Attól függetlenül ettünk kenyeret, hogy nem volt semmilyen törvény az asztalon.",
                ],
                0,
                ["b2-concessive-conditionals"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Egyetemi előadó", "text": "Miért olyan ellenálló a határon túli magyar kultúra a történelem viharaiban?"},
                    {"speaker": "Kutató", "text": "____"},
                ],
                [
                    "Mert a közösségi megmaradás legfőbb megtartó ereje az anyanyelv, amelyhez még akkor is hűek maradnak, ha a külső körülmények nehezek.",
                    "Mert senkit sem érdekel a történelem, és mindenki külföldre költözött.",
                    "A határok eltűnése után már felesleges beszélgetni a szülőföldről.",
                ],
                0,
                ["b2-concessive-conditionals"],
            ),
            mc(
                "grammar",
                "in-context",
                "Why is 'akkor sem, ha' preferred over plain 'ha nem' in categorical assertions?",
                [
                    "Because 'akkor sem, ha' expresses an unyielding, categorical negation that holds across all conceivable hypothetical conditions.",
                    "Because 'ha nem' can only be used in questions, never in statements.",
                    "Because 'akkor sem' is an imperative formula used only by judges.",
                ],
                0,
                ["b2-concessive-conditionals"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["Még", "akkor", "is", "megőrizzük", "az", "anyanyelvünket,", "ha", "nehéz", "a", "sorsunk."],
                ["Még", "akkor", "is", "megőrizzük", "az", "anyanyelvünket,", "ha", "nehéz", "a", "sorsunk."],
                "We preserve our mother tongue even if our fate is difficult.",
                ["b2-concessive-conditionals"],
            ),
            sb(
                "grammar",
                "produce",
                ["Függetlenül", "attól,", "hogy", "hol", "húzódnak", "a", "határok,", "egy", "nemzet", "vagyunk."],
                ["Függetlenül", "attól,", "hogy", "hol", "húzódnak", "a", "határok,", "egy", "nemzet", "vagyunk."],
                "Regardless of where the borders lie, we are one nation.",
                ["b2-concessive-conditionals"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause transborder essay thesis combining 'még akkor is, ha' (concessive condition), 'függetlenül attól, hogy' (independent condition), and 'megtartó erő' (sustaining force).",
                        "answer": "Függetlenül attól, hogy milyen országhatárok választják el egymástól a közösségeket, az anyanyelv felbecsülhetetlen megtartó erőt jelent; amelyhez még akkor is hűségesek maradunk, ha a modern világ kihívásai komoly erőfeszítést követelnek tőlünk.",
                    }
                ],
                ["b2-concessive-conditionals"],
            ),
        ],
    },
}
