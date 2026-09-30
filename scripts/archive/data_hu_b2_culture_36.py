# -*- coding: utf-8 -*-
"""
Hungarian B2 Culture Track Unit 36:
Synthesis: What It Means to Speak and Understand Hungarian Today (b2-magyaridentitas)
"""
from helpers_hu_b2_exercises import dc, fb, match, mc, sb, sw

VOCAB_SKILL = "b2-magyaridentitas-vocab"
GRAMMAR_SKILL = "b2-mastery-synthesis"

UNIT_36_MAGYARIDENTITAS = {
    "unit_num": 36,
    "slug": "magyaridentitas",
    "title": "Synthesis: What It Means to Speak and Understand Hungarian Today",
    "grammar_skill": GRAMMAR_SKILL,
    "vocab_skill": VOCAB_SKILL,
    "theme": "Synthesis of Hungarian identity, language, literature and culture",
    "location": "A Kárpát-medence, a Duna-part, a budapesti kávéházak és a világ",
    "intro_body": [
        "A magyar nyelv és identitás megértése olyan intellektuális utazás, amely a Kárpát-medence történelmének legmélyebb rétegeibe vezet. Európa szívében, egy túlnyomórészt indoeurópai tengerben a magyar mint ragozó finnugor szigetnyelv évezredeken át képes volt megőrizni egyedülálló grammatikai szerkezetét és belső logikáját, miközben szervesen beépítette a vele együtt élő szomszédos népek kulturális és nyelvi hatásait.",
        "Ebben a záró B2 fejezetben szintetizáljuk a magyar szellemtörténet legfontosabb sarokköveit: a költők mint nemzeti próféták küldetéstudatát Petőfitől Radnótiig, a melankólia és az önironikus pesti akasztófahumor kettősségét, azokat a rejtett kulturális kódokat, amelyeket a „Belső Pista” fogalma testesít meg, valamint azt a felemelő távlatot, amelyet a B2 szint elérése és a C1 szint felé vezető út nyújt.",
        "Nyelvtanilag a B2 szint teljes szintaktikai integrációját hajtjuk végre: az emelkedett megengedő és ellentétes kötőszavak (jóllehet, noha, mindazonáltal, mindamellett, egyszersmind), a határozói és melléknévi igeneves szerkezetek, valamint a stilisztikai mondatfonás művészetét sajátítjuk el a hibátlan, választékos kifejezésmód érdekében."
    ],
    "combined_story_title": "Szigetnyelv Európa szívében: A magyar nyelv és identitás szintézise",
    "combined_story_summary": "The capstone journey through Hungarian linguistic and cultural identity: the mystery and beauty of an isolated Finno-Ugric language, the civic responsibility of poets and writers, the Hungarian blend of irony and melancholy, and looking forward from B2 toward C1 mastery.",
    "lessons": [
        {
            "num": 1,
            "title": "An Island Language: Finno-Ugric Roots in an Indo-European Continent",
            "grammar_label": "Syntactic integration and discourse concession (*jóllehet, noha, mindazonáltal*)",
            "goals": [
                "I can explain the Finno-Ugric genealogical origin of Hungarian and its position as an agglutinative island language.",
                "I can use formal concessive discourse connectors (*jóllehet, noha, mindazonáltal*) to construct balanced arguments.",
                "I can trace the historical layers of vocabulary (Finno-Ugric, Turkic, Slavic, Latin, German) that enrich Hungarian."
            ],
            "story_segment": {
                "seg_slug": "finnugorgyokerek",
                "title": "Egy szigetnyelv gyökerei: Finnugor alapok indoeurópai környezetben",
                "summary": "Surrounded by Germanic, Slavic, and Romance languages, Hungarian preserved its Uralic agglutinative root system while assimilating diverse cultural and lexical influences into a vibrant whole.",
                "location": "Kárpát-medence és a Duna-kanyar",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A Kárpát-medencébe érkező utazót vagy nyelvtanulót mindmáig lenyűgözi a tény, hogy Közép-Európa kellős közepén olyan nyelv él, amely sem a szláv, sem a germán, sem az újlatin nyelvekkel nem áll közvetlen rokonságban. A magyar nyelv mint finnugor szigetnyelv több mint ezer éve áll őrt Európa kereszteződésében, hűségesen megőrizve uráli gyökereit és jellegzetes agglutináló grammatikáját."
                    },
                    {
                        "type": "narration",
                        "text": "Az anyanyelv alapszókincse – a testrészek, az elemi természeti jelenségek, a családi viszonyok és a legegyszerűbb cselekvések nevei – a mai napig finnugor eredetűek, amint azt a kéz, szem, víz, vér vagy él szavak ősi hangzása is tanúsítja. Ezt az ősi magot azonban a vándorlások és az együttélés évszázadai során gazdag rétegek vették körül: a honfoglalás előtti török kölcsönszavak a földművelést és az állattartást, a szláv jövevényszavak a keresztény hitéletet és a mezőgazdaságot gazdagították."
                    },
                    {
                        "type": "narration",
                        "text": "Később a latin nyelv több évszázados államnyelvi szerepe a jogi, orvosi és tudományos gondolkodást formálta, miközben a német hatás a polgári mesterségek és a városi kultúra szókincsét gyarapította. Mindezek a hatások azonban nem szétzilálták, hanem megerősítették a magyar nyelv önálló karakterét, hiszen a nyelvtan belső törvényszerűségei minden idegen elemet magyarrá formáltak."
                    },
                    {
                        "type": "narration",
                        "text": "A nyelvi elszigeteltség tudata évszázadokon át kettős érzést táplált a magyar gondolkodásban: egyfelől a magányosság és a rokontalanság fájdalmas melankóliáját, másfelől a büszkeséget, hogy a történelem viharaiban, tatár, török és birodalmi elnyomás közepette is sikerült megőrizni az anyanyelvet."
                    },
                    {
                        "type": "narration",
                        "text": "Ma a magyar nyelv nem csupán történelmi relikvia, hanem tizenhárommillió ember eleven, vibráló kommunikációs közege. Megtanulni e nyelvet annyit tesz, mint belépni egy zárt, mégis végtelenül vendégszerető szellemi univerzumba, ahol minden szó mögött ezer év költészete és történelme visszhangzik."
                    }
                ]
            },
            "words": [
                {"lemma": "szigetnyelv", "translation": "island language / isolated linguistic entity", "pos": "noun"},
                {"lemma": "finnugor eredet", "translation": "Finno-Ugric origin", "pos": "expression"},
                {"lemma": "ragozó nyelv", "translation": "agglutinative language", "pos": "expression"},
                {"lemma": "nyelvi rétegződés", "translation": "linguistic stratification / layers", "pos": "expression"},
                {"lemma": "jövevényszó", "translation": "loanword / integrated historical borrowing", "pos": "noun"},
                {"lemma": "nyelvi elszigeteltség", "translation": "linguistic isolation", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "concessive-connectors-jollehet",
                "title": "Elevated Concessive Connectors: Jóllehet, Noha, and Mindazonáltal",
                "text1_title": "Nuances of Concessive Subordination: Jóllehet and Noha",
                "text1": "In high-register prose and academic synthesis, concessive subordinate clauses are introduced by 'jóllehet' or 'noha' (both equivalent to 'although / albeit / even though'). Unlike colloquial 'bár' or 'habár', these markers convey intellectual gravity: 'Jóllehet a magyar nyelv környezete indoeurópai, belső szerkezete mindmáig megőrizte uráli sajátosságait.'",
                "text2_title": "Adversative Concession in the Main Clause: Mindazonáltal",
                "text2": "'Mindazonáltal' (nevertheless / nonetheless / for all that) acts as an adversative sentence connector. It contrasts a preceding reservation with a firm counter-assertion, maintaining syntactic balance in extended philosophical and historical paragraphs.",
                "table_title": "Concessive Connectors in Elevated Discourse",
                "table_rows": [
                    ["Jóllehet nehéz a nyelvtan, rendkívül logikus.", "Although the grammar is difficult, it is extremely logical."],
                    ["Noha elszigetelt a nyelv, nyitott a világra.", "Even though the language is isolated, it is open to the world."],
                    ["Voltak nehézségek; mindazonáltal sikert értek el.", "There were difficulties; nevertheless, they achieved success."],
                    ["Jóllehet sok jövevényszó van, a mag ősi maradt.", "Albeit there are many loanwords, the core remained ancient."]
                ],
                "examples": [
                    {"spanish": "Jóllehet a magyar nyelv szókincse számos idegen hatást mutat, nyelvtani rendszere teljesen egyedi maradt.", "english": "Although the Hungarian vocabulary exhibits numerous foreign influences, its grammatical system remained entirely unique."},
                    {"spanish": "A történelmi viharok megtépázták az országot; mindazonáltal az anyanyelv megőrizte kifejezőerejét.", "english": "Historical storms battered the country; nevertheless, the mother tongue preserved its expressive power."},
                    {"spanish": "Noha a rokontalanság tudata olykor melankóliát szült, büszkeséget is adott a nemzetnek.", "english": "Even though the consciousness of having no close kin sometimes engendered melancholy, it also gave pride to the nation."}
                ],
                "tip": "Word order note: 'jóllehet' and 'noha' introduce subordinate clauses that require a comma. 'Mindazonáltal' is usually preceded by a semicolon or period when connecting two complete independent propositions."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["szigetnyelv", "island language"],
                        ["finnugor eredet", "Finno-Ugric origin"],
                        ["ragozó nyelv", "agglutinative language"],
                        ["nyelvi rétegződés", "linguistic stratification"],
                        ["jövevényszó", "historical loanword"],
                        ["nyelvi elszigeteltség", "linguistic isolation"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Melyik állítás írja le legpontosabban a magyar nyelv rokonságát és szerkezeti típusát?",
                    [
                        "A finnugor nyelvcsaládba tartozó, agglutináló (ragozó) szigetnyelv Európa szívében.",
                        "Az indoeurópai nyelvcsalád szláv ágához tartozó, izoláló szerkezetű nyelv.",
                        "Egy mesterségesen létrehozott nyelv, amelyet a tizenkilencedik században találtak ki."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A magyar nyelv évszázadokon át szervesen beépítette a török, szláv és latin _____ anélkül, hogy elveszítette volna ősi karakterét.",
                    "jövevényszavakat",
                    "Over centuries, the Hungarian language organically integrated loanwords without losing its ancient character.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik emelkedett megengedő kötőszó illik leginkább a tudományos stílusú mondatba? '_____ a magyar nyelv szókészlete folyamatosan gazdagodott, nyelvtani alapjai évezredek óta változatlanok.'",
                    ["Jóllehet", "Hacsak", "Minthogy", "Feltéve"],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A tanulás folyamata sok türelmet igényelt; _____ a diákok elérték a kitűzött B2 szintet.",
                    "mindazonáltal",
                    "The learning process demanded much patience; nevertheless, the students attained the targeted B2 level.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["Jóllehet", "a", "nyelvtan", "összetett,", "a", "belső", "logikája", "lenyűgöző."],
                    ["Jóllehet", "a", "nyelvtan", "összetett,", "a", "belső", "logikája", "lenyűgöző."],
                    "Although the grammar is complex, its internal logic is fascinating.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Külföldi nyelvész", "text": "Hogyan maradhatott fenn a magyar nyelv egy szláv és germán többségű kontinensen?"},
                        {"speaker": "Magyar professzor", "text": "_____"}
                    ],
                    [
                        "Jóllehet folyamatos külső hatások érték, a közösség ragaszkodása az anyanyelvhez és a gazdag irodalom megvédte az asszimilációtól.",
                        "Mert tilos volt bármilyen idegen szót kimondani a határátlépés után.",
                        "Kizárólag azért, mert a szomszédos népek nem tudtak írni és olvasni."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Milyen lelki hatást gyakorolt a magyar nemzettudatra a nyelvi elszigeteltség történelmi tapasztalata?",
                    [
                        "A magányosság melankolikus érzését ötvözte a büszkeséggel, hogy sikerült megőrizni az anyanyelvet a viharok közepette.",
                        "Azonnali beolvadási vágyat ébresztett a szomszédos birodalmak kultúrájába.",
                        "Teljes közönyt váltott ki az irodalom és a költészet iránt a társadalomban."
                    ],
                    0
                )
            ]
        },
        {
            "num": 2,
            "title": "The Poet as National Conscience: From Petőfi to Radnóti",
            "grammar_label": "Stylistic inversion and participial integration in elevated discourse",
            "goals": [
                "I can analyze the sacred civic role of poets and writers as moral leaders and spokespersons for the Hungarian nation.",
                "I can integrate participial constructions (-va/-ve, -ó/-ő, -ott/-ett) to create fluid, elevated syntactic structures.",
                "I can discuss how literature preserved Hungarian national identity across centuries of political turmoil."
            ],
            "story_segment": {
                "seg_slug": "koltokhivatasa",
                "title": "A költő mint a nemzet lelkiismerete: Petőfitől Radnótiig",
                "summary": "In Hungary, literature has always carried existential weight. From Petőfi's 1848 revolutionary verses to Radnóti Miklós's tragic camp notebooks, poets served as the moral conscience of their people.",
                "location": "Pest, Pilvax Kávéház, Debrecen és a bori tábor emlékezete",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar kultúra egyik legszembetűnőbb sajátossága az irodalom, és különösen a költészet kivételes társadalmi presztízse. Míg Nyugat-Európában az írók gyakran az egyén belső vívódásaira vagy az esztétikai formákra összpontosítottak, Magyarországon a költő hagyományosan a nemzet lelkiismereteként, prófétai váteszként lépett fel a sorskérdések eldöntésekor."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor a politikai intézmények megbénultak vagy idegen elnyomás alá kerültek, a nemzeti önazonosság őrzésének felelőssége a költők vállára nehezedett. Zrínyi Miklós karddal és tollal védte a hazát, Kölcsey Ferenc a Himnuszban fogalmazta meg a nemzet tragikus imáját, Petőfi Sándor pedig a Nemzeti dallal egyenesen az 1848-as forradalom lángját lobbantotta fel a Pilvax kávéház asztaláról indulva."
                    },
                    {
                        "type": "narration",
                        "text": "A huszadik század megpróbáltatásai közepette ez a hivatástudat még tovább mélyült. Ady Endre ostorozó, mégis féltő versei a magyar ugar elmaradottságával szembesítették az országot, József Attila a külvárosi nyomor és az emberi lélek legmélyebb magányának adott egyetemes hangot, míg Radnóti Miklós a munkaszolgálat és a fasiszta barbárság poklában is a tiszta forma és az erkölcsi méltóság hűséges őrzője maradt."
                    },
                    {
                        "type": "narration",
                        "text": "Radnóti Bori noteszének versei a világirodalom legmegrendítőbb alkotásai közé tartoznak: a halálmenet sarában menetelve, ceruzacsonkkal füzetbe rótt sorai bizonyították, hogy a költői szó képes felülemelkedni az embertelenségen és a fizikai pusztuláson."
                    },
                    {
                        "type": "narration",
                        "text": "A költészet iránti tisztelet ma is él a magyar társadalomban. A szavalóversenyek, az utcai idézetek és a nemzeti ünnepek szónoklatai mind arról tanúskodnak, hogy a magyar ember számára a költészet nem úri passzió, hanem az önismeret és a közösségi megmaradás legmélyebb forrása."
                    }
                ]
            },
            "words": [
                {"lemma": "költői hivatástudat", "translation": "poetic vocation / calling", "pos": "expression"},
                {"lemma": "nemzeti lelkiismeret", "translation": "national conscience", "pos": "expression"},
                {"lemma": "váteszköltő", "translation": "prophet-poet / visionary poet", "pos": "noun"},
                {"lemma": "sorskérdés", "translation": "existential question of destiny", "pos": "noun"},
                {"lemma": "történelmi megpróbáltatás", "translation": "historical trial / ordeal", "pos": "expression"},
                {"lemma": "irodalmi kánon", "translation": "literary canon", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "participial-integration-inversion",
                "title": "Participial Integration and Stylistic Inversion in Intellectual Hungarian",
                "text1_title": "Condensing Subclauses with Participles (-va/-ve, -ó/-ő, -ott/-ett)",
                "text1": "Literary and formal Hungarian condenses complex narrative subordinate clauses into compact participial phrases. Adverbial participles in '-va/-ve' express attendant circumstances: 'A költő a nemzet szószólójaként fellépve figyelmeztette a társadalmat.' Past participles in '-ott/-ett/-ött' provide dense attributive framing: 'A ceruzával feljegyzett versek örök mementóvá váltak.'",
                "text2_title": "Stylistic Inversion for Rhetorical Focus",
                "text2": "In formal rhetoric, word order is inverted to place emphasis on the moral or qualitative predicate before the verb, creating a grave, measured cadence: 'Nem csupán költő volt ő, hanem a nemzet élő lelkiismerete.' Placing the predicate focus immediately before the conjugated verb imparts heightened emotional resonance.",
                "table_title": "Participial Structures and Rhetorical Inversion",
                "table_rows": [
                    ["A halálmenetben menetelve írta verseit.", "Marching in the death march, he wrote his poems."],
                    ["A nép sorsáért küzdve lépett fel a forradalomban.", "Striving for the people's fate, he stepped up in the revolution."],
                    ["Fennmaradtak a táborban papírra vetett sorok.", "The lines cast onto paper in the camp survived."],
                    ["Büszkén vallotta magát a magyar nyelv hívének.", "Proudly he proclaimed himself a devotee of the Hungarian language."]
                ],
                "examples": [
                    {"spanish": "A nemzet sorskérdéseit kutatva a magyar költők mindig az igazság szószólóiként léptek fel.", "english": "Exploring the existential questions of the nation, Hungarian poets always stepped forward as advocates of truth."},
                    {"spanish": "A legnehezebb időkben születve a versek nemzeti imádsággá nemesedtek az évszázadok során.", "english": "Born in the hardest times, the poems were ennobled into national prayers over the centuries."},
                    {"spanish": "Nem a dicsőséget keresve írtak, hanem a megmaradásért küzdöttek.", "english": "Not seeking glory did they write, but fought for survival."}
                ],
                "tip": "Ensure the subject of an adverbial participle in '-va/-ve' matches the subject of the main predicate: 'A füzetet kézbe véve megértette a tragédiát' (Taking the notebook in hand, he understood the tragedy)."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["költői hivatástudat", "poetic vocation"],
                        ["nemzeti lelkiismeret", "national conscience"],
                        ["váteszköltő", "prophet-poet"],
                        ["sorskérdés", "question of destiny"],
                        ["történelmi megpróbáltatás", "historical trial"],
                        ["irodalmi kánon", "literary canon"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Milyen egyedülálló társadalmi szerepet töltöttek be a költők a magyar történelem válságos korszakaiban?",
                    [
                        "A nemzeti lelkiismeret szószólóiként és prófétai váteszként vezették a közösséget.",
                        "Kizárólag az udvari bálok szórakoztatásáért feleltek és elzárkóztak a közélettől.",
                        "Az államkincstár adóbehajtóiként működtek a falusi plébániákon."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "Radnóti Miklós versei a legszörnyűbb emberi _____ közepette is megőrizték az erkölcsi méltóságot.",
                    "megpróbáltatások",
                    "Miklós Radnóti's poems preserved moral dignity even amid the most terrible human trials.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik mondatban szerepel helyesen a határozói igeneves (-va/-ve) szerkezet?",
                    [
                        "A nemzet sorsáért aggódva a költő bátorító sorokat vetett papírra.",
                        "A nemzet sorsáért aggódván a költő bátorító sorokat vetett papírra.",
                        "A nemzet sorsáért aggódni a költő bátorító sorokat vetett papírra.",
                        "A nemzet sorsáért aggódott a költő bátorító sorokat vetett papírra."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A táborban ceruzával papírra _____ sorok a világirodalom megrázó remekműveivé váltak.",
                    "vetett",
                    "The lines cast onto paper with pencil in the camp became shocking masterpieces of world literature.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["A", "költők", "a", "nemzet", "szószólóiként", "léptek", "fel", "a", "sorskérdésekben."],
                    ["A", "költők", "a", "nemzet", "szószólóiként", "léptek", "fel", "a", "sorskérdésekben."],
                    "The poets stepped forward as spokespersons of the nation in questions of destiny.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Külföldi diák", "text": "Miért olyan fontos Petőfi Sándor vagy Radnóti Miklós a mai magyarok számára?"},
                        {"speaker": "Irodalomtanár", "text": "_____"}
                    ],
                    [
                        "Mert verseikben a nemzet történelmi sorskérdései, a szabadságvágy és az emberi méltóság legmagasabb szintű megfogalmazását találjuk.",
                        "Mert kötelező őket megvenni minden könyvesboltban a törvény szerint.",
                        "Kizárólag azért, mert mindketten külföldi nyelveken publikálták az összes kötetüket."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Hogyan maradt fenn Radnóti Miklós utolsó füzete, a legendás Bori notesz?",
                    [
                        "A költő zsebében maradt a tömegsírban, ahonnan az exhumálás után megmentették és közzétették a verseket.",
                        "Postán feladta Párizsba a halála előtt egy héttel egy barátjának.",
                        "Egy svéd diplomata vásárolta meg a bori rézbányák igazgatójától."
                    ],
                    0
                )
            ]
        },
        {
            "num": 3,
            "title": "Melancholy and Gallows Humor: The Hungarian Sensibility",
            "grammar_label": "Register nuance: blending tragic solemnity with self-ironic understatement",
            "goals": [
                "I can explore the unique coexistence of tragic historical melancholy ('sírva vigad a magyar') and razor-sharp self-irony.",
                "I can deploy rhetorical antithesis (*egyfelől... másfelől; nem annyira..., mint inkább*) to capture nuanced emotional registers.",
                "I can discuss the social function of gallows humor (akasztófahumor) and cabaret wit as psychological survival tools."
            ],
            "story_segment": {
                "seg_slug": "humoresmelankolia",
                "title": "Sírva vigadás és akasztófahumor: A magyar lélek kettőssége",
                "summary": "From the solemn lament of the national anthem to the wicked wit of Budapest cabarets, Hungarians combine tragic historical memory with sharp, self-deprecating irony.",
                "location": "Budapesti kávéházak és pesti kabaré színpadok",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A külföldi megfigyelők gyakran megjegyzik a magyar lelki alkat látszólagos ellentmondásait. A magyar nemzeti himnusz – Kölcsey Ferenc fenséges költeménye – a világ kevés himnuszának egyike, amely nem katonai diadalról vagy büszke hatalomról énekel, hanem a megpróbáltatásokkal sújtott népért könyörög bűnbánó és méltóságteljes hangon. A „sírva vigadás” közmondásos tapasztalata évszázadok óta a nemzeti érzésvilág alapmotívuma."
                    },
                    {
                        "type": "narration",
                        "text": "Ám ha valaki ebből arra következtetne, hogy a magyarok komor és levert nép, alaposan tévedne. E mély történelmi melankólia elválaszthatatlan ikertestvére a maró önirónia, a sziporkázó pesti humor és a híres akasztófahumor, amely a legkilátástalanabb történelmi helyzetekben is képes volt feloldani a szorongást és kinevetni a hatalmaskodókat."
                    },
                    {
                        "type": "narration",
                        "text": "A budapesti kávéházak és kabaré színpadok – Nagy Endrétől Hofi Gézáig – valóságos intézménnyé emelték a szatírát. Amikor a társadalom tehetetlen volt az idegen hadseregekkel, a szovjet tankokkal vagy a pártbürokráciával szemben, a politikai viccek és az önleleplező poénok jelentették a belső függetlenség utolsó, elvehetetlen védőbástyáját."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a kettősség tükröződik a mindennapi nyelvhasználatban is: a magyar ember egyszerre hajlamos a végzetes panaszkodásra és az azonnali, nevetve történő elbagatellizálásra. Egyetlen mondaton belül képes a legsötétebb pesszimizmust egy felszabadító önironikus csattanóval feloldani, jelezve, hogy a dolgokat túl komolyan venni éppoly veszélyes, mint megfeledkezni a súlyukról."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar humor tehát nem a felelőtlenség, hanem a túlélés stratégiája. Aki megérti ezt a finom egyensúlyt a tragikus pátosz és a gyógyító önirónia között, az a magyar identitás és gondolkodásmód legrejtettebb szívkamrájába nyer betekintést."
                    }
                ]
            },
            "words": [
                {"lemma": "sírva vigadás", "translation": "reveling through tears / bittersweet merriment", "pos": "expression"},
                {"lemma": "akasztófahumor", "translation": "gallows humor / macabre wit", "pos": "noun"},
                {"lemma": "melankólia", "translation": "melancholy / deep sorrow", "pos": "noun"},
                {"lemma": "önirónia", "translation": "self-irony / self-deprecating wit", "pos": "noun"},
                {"lemma": "lelki alkat", "translation": "psychological temperament / mental disposition", "pos": "expression"},
                {"lemma": "túlélési stratégia", "translation": "survival strategy", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "rhetorical-antithesis-nuance",
                "title": "Rhetorical Antithesis and Tone Balancing: Egyfelől... másfelől",
                "text1_title": "Structuring Duality with Egyfelől... másfelől",
                "text1": "To articulate complex cultural paradoxes, Hungarian employs paired antithetical conjunctions: 'Egyfelől a magyar történelem tele van tragikus cezúrákkal, másfelől a társadalom páratlan humorral vértezte fel magát.' This formula balances contrasting truths without canceling either side.",
                "text2_title": "Nuancing Assertions: Nem annyira..., mint inkább",
                "text2": "When fine-tuning a psychological or cultural claim, 'nem annyira [A], mint inkább [B]' (not so much [A], but rather [B]) shifts the interpretive focus toward deeper motivations: 'A pesti humor nem annyira cinizmus volt, mint inkább a túlélés elengedhetetlen eszköze.'",
                "table_title": "Antithetical Formulas for Cultural Characterization",
                "table_rows": [
                    ["Egyfelől szomorú a zene, másfelől táncra hív.", "On the one hand the music is sorrowful, on the other hand it calls to dance."],
                    ["Nem annyira panaszkodás ez, mint inkább önirónia.", "It is not so much complaining, but rather self-irony."],
                    ["Egyfelől tragikus a múlt, másfelől élni kell a mában.", "On the one hand the past is tragic, on the other hand one must live in the present."],
                    ["Nem a csüggedés hangja ez, hanem a belső dac kifejezése.", "This is not the voice of despair, but the expression of inner defiance."]
                ],
                "examples": [
                    {"spanish": "Egyfelől jelen van a történelmi melankólia, másfelől az önironikus humor minden nehézségen átsegít.", "english": "On the one hand historical melancholy is present, on the other hand self-ironic humor helps through every hardship."},
                    {"spanish": "A politikai vicc nem annyira szórakozás volt, mint inkább a szellemi szabadság utolsó menedéke.", "english": "The political joke was not so much entertainment, but rather the last haven of intellectual freedom."},
                    {"spanish": "A kabaré színpadán a nevetés egyfelől leleplezte a hatalmat, másfelől összekovácsolta a közönséget.", "english": "On the cabaret stage, laughter on the one hand unmasked power, on the other hand bonded the audience."}
                ],
                "tip": "In formal Hungarian, always balance 'egyfelől' with 'másfelől'. Leaving out 'másfelől' weakens the antithesis and leaves the sentence syntactically incomplete."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["sírva vigadás", "bittersweet merriment"],
                        ["akasztófahumor", "gallows humor"],
                        ["melankólia", "melancholy"],
                        ["önirónia", "self-irony"],
                        ["lelki alkat", "psychological disposition"],
                        ["túlélési stratégia", "survival strategy"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Milyen funkciót töltött be a pesti kabaré és a politikai vicc a diktatúra éveiben?",
                    [
                        "A belső függetlenség és a lelki túlélés elengedhetetlen eszköze volt a társadalom számára.",
                        "Az állami rendőrség hivatalos képzési anyaga volt az új tiszteknek.",
                        "A külföldi turisták kizárólagos szórakoztatását szolgálta a luxusszállodákban."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A magyar kultúrában a nehézségekkel való szembenézés legfőbb pszichológiai eszköze a maró _____ és a humor.",
                    "önirónia",
                    "In Hungarian culture, the primary psychological tool for confronting hardships is biting self-irony and humor.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik kifejezéspár alkot helyes retorikai ellentétpárt az alábbi mondatban? '_____ a nemzeti múlt tele van fájdalmas emlékekkel, _____ a humor képessé tesz az újrakezdésre.'",
                    ["Egyfelől / másfelől", "Ezért / azért", "Minthogy / ennélfogva", "Hacsak / amennyiben"],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A politikai kabaré nem annyira egyszerű szórakoztatás volt, _____ inkább a szellemi ellenállás sajátos formája.",
                    "mint",
                    "The political cabaret was not so much simple entertainment, but rather a peculiar form of intellectual resistance.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["Egyfelől", "jelen", "van", "a", "melankólia,", "másfelől", "segít", "az", "önirónia."],
                    ["Egyfelől", "jelen", "van", "a", "melankólia,", "másfelől", "segít", "az", "önirónia."],
                    "On the one hand melancholy is present, on the other hand self-irony helps.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Külföldi vendég", "text": "Miért nevetnek a magyarok a legnehezebb válságok idején is saját magukon?"},
                        {"speaker": "Szociológus", "text": "_____"}
                    ],
                    [
                        "Mert az önirónia és az akasztófahumor segít megőrizni a méltóságot és feloldani a szorongást a legsötétebb időkben is.",
                        "Mert tilos szomorúnak lenni a magyar törvények szerint.",
                        "Mert soha senki nem veszi észre, ha baj történik az országban."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Miben tér el a magyar nemzeti himnusz a legtöbb európai ország himnuszától?",
                    [
                        "Nem győzelmeket és katonai hatalmat dicsőít, hanem könyörgő, bűnbánó és méltóságteljes fohász a népért.",
                        "Kizárólag dobszóra éneklik szöveg nélkül minden hivatalos ceremónián.",
                        "Egy vidám táncdal, amelyet a szüreti bálokon szoktak énekelni a falvakban."
                    ],
                    0
                )
            ]
        },
        {
            "num": 4,
            "title": "Through the Eyes of 'Belső Pista': Inside the Hungarian Mindset",
            "grammar_label": "Complex sentence architectures and parenthetical qualification (*mindamellett, egyszersmind*)",
            "goals": [
                "I can decipher implicit cultural codes, legendary literary allusions, and idiomatic mental frames in Hungarian.",
                "I can use parenthetical qualification adverbs (*egyszersmind, mindamellett, mintegy*) to modulate assertions.",
                "I can explain what it means to grasp the cultural unspoken nuances of native Hungarian conversations."
            ],
            "story_segment": {
                "seg_slug": "belsopisztaszemmel",
                "title": "A „Belső Pista” szemével: Rejtett kulturális kódok és gondolkodásmód",
                "summary": "True fluency is understanding what is left unsaid: Mikszáth's anecdotes, Rejtő's legendary one-liners, and the internal compass that Hungarians call 'Belső Pista'.",
                "location": "Budapesti kiskocsmák, antikváriumok és a Duna-part",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A nyelvtanulás B2 szintjén a tanuló már birtokában van a nyelvtan szabályainak és bőséges szókincsnek, ám a legmélyebb megértéshez még egy rejtett ajtón be kell lépnie: a közös kulturális utalások, szállóigék és kimondatlan gondolati kódok birodalmába. Ezt a belső kulturális iránytűt szokták a magyar köznyelvben félig tréfásan a „Belső Pista” hangjának nevezni."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar beszélgetések szövetét sűrűn átszövik az irodalmi és történelmi allúziók. Amikor valaki azt mondja, hogy „nem enged a negyvennyolcból”, vagy egy abszurd bürokratikus helyzetben A tanú című kultikus filmből idézi, hogy „a nemzetközi helyzet egyre fokozódik”, vagy Rejtő Jenő ponyvaregényeinek valamelyik halhatatlan mondatával üti el a bajt, a résztvevők azonnal egy hullámhosszra kerülnek."
                    },
                    {
                        "type": "narration",
                        "text": "Mikszáth Kálmán anekdotikus bölcsessége, Karinthy Frigyes kifinomult abszurdizmusa és Örkény István egyperces novellái nem csupán iskolai tananyagok, hanem a mindennapi reflexió részei. Az a képesség, hogy az ember a sorok között olvasva megértse a finom iróniát, a félmosolyt vagy a hangsúly apró eltolódását, a nyelvi otthonosság valódi védjegye."
                    },
                    {
                        "type": "narration",
                        "text": "A „Belső Pista” mindamellett a magyar történelem és tapasztalat sűrítménye: a szkeptikus józanságé, amely nem dől be a hangzatos jelszavaknak, a túlélés leleményességéé, amely a legszűkebb kiskaput is észreveszi, és a mély emberségé, amely a látszólagos cinizmus mögött valódi együttérzést rejt."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor a külföldi nyelvtanuló eljut odáig, hogy egy baráti asztaltársaságnál elkapja ezeket a finom árnyalatokat és maga is képes egy találó szállóigével reagálni, leomlik a külföldi és az anyanyelvi beszélő közötti utolsó láthatatlan válaszfal is."
                    }
                ]
            },
            "words": [
                {"lemma": "kulturális kód", "translation": "cultural code / shared cultural referent", "pos": "expression"},
                {"lemma": "rejtett utalás", "translation": "implicit allusion / subtextual reference", "pos": "expression"},
                {"lemma": "szállóige", "translation": "famous quote / household saying", "pos": "noun"},
                {"lemma": "gondolkodásmód", "translation": "mindset / mental outlook", "pos": "noun"},
                {"lemma": "közösségi emlékezet", "translation": "collective memory", "pos": "expression"},
                {"lemma": "finom árnyalat", "translation": "subtle nuance / shade of meaning", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "parenthetical-qualification-cohesion",
                "title": "Parenthetical Qualification and Semantic Cohesion: Egyszersmind and Mindamellett",
                "text1_title": "Simultaneous Roles with Egyszersmind",
                "text1": "'Egyszersmind' (at the same time / simultaneously) links two attributes or social roles that coexist harmoniously, elevating the stylistic tone: 'A magyar költő nem csupán esztéta volt, hanem egyszersmind a nép politikai szószólója is.' It avoids repetitive 'és egyben' formulations.",
                "text2_title": "Nuanced Qualification with Mindamellett",
                "text2": "'Mindamellett' (nevertheless / with that said / at the same time) introduces a necessary contextual qualification or counter-consideration without negating the primary assertion: 'A pesti vicc maró és szkeptikus; mindamellett mély emberséget és szolidaritást fejez ki.'",
                "table_title": "Cohesive Adverbs of Qualification",
                "table_rows": [
                    ["A regény szórakoztató, egyszersmind mély filozófia.", "The novel is entertaining, and at the same time profound philosophy."],
                    ["Kritikus a hangja; mindamellett tele van szeretettel.", "Its tone is critical; with that said, it is full of love."],
                    ["Egyszersmind tükrözi a múltat és a jövőt.", "At the same time it reflects the past and the future."],
                    ["Mindamellett fontos szem előtt tartani az összefüggéseket.", "Nevertheless, it is important to keep the context in mind."]
                ],
                "examples": [
                    {"spanish": "A szállóigék ismerete szórakoztató, egyszersmind a magyar kultúrába való beilleszkedés legfőbb kulcsa.", "english": "Knowledge of famous sayings is entertaining, and at the same time the main key to integrating into Hungarian culture."},
                    {"spanish": "A mindennapi beszélgetések tele vannak iróniával; mindamellett a baráti kapcsolatok rendkívül mélyek.", "english": "Everyday conversations are full of irony; nevertheless, friendly relationships are exceptionally deep."},
                    {"spanish": "A szerző humorosan ábrázolja a helyzetet, egyszersmind felhívja a figyelmet a társadalmi felelősségre.", "english": "The author humorously depicts the situation, and simultaneously draws attention to social responsibility."}
                ],
                "tip": "Use 'egyszersmind' when synthesizing two positive or complementary functions. Use 'mindamellett' when providing an important caveat or balancing nuance."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["kulturális kód", "cultural code"],
                        ["rejtett utalás", "implicit allusion"],
                        ["szállóige", "household saying"],
                        ["gondolkodásmód", "mindset"],
                        ["közösségi emlékezet", "collective memory"],
                        ["finom árnyalat", "subtle nuance"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Mit jelent a magyar beszédben a kulturális kódok és szállóigék természetes használata?",
                    [
                        "Azt, hogy a beszélő a felszíni szavak mögött érti az irodalmi, történelmi és filmes utalásokat is.",
                        "Azt, hogy a beszélő titkos kódolt üzeneteket küld a katonai hírszerzésnek.",
                        "Azt, hogy a beszélő képtelen befejezni a mondatait idegen szavak nélkül."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A magyar irodalomból származó bölcs mondások és híres _____ a mindennapi beszélgetések szerves részét képezik.",
                    "szállóigék",
                    "Wise sayings and famous quotes originating from Hungarian literature form an organic part of everyday conversations.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik kötőszó fejezi ki legválasztékosabban a két szerep egyidejű jelenlétét? 'A művész kiváló szobrász volt, _____ elismert egyetemi tanárként is tevékenykedett.'",
                    ["egyszersmind", "hacsak", "noha", "feltéve"],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A helyzet rendkívül bonyolult volt; _____ sikerült minden részletben békés megállapodásra jutni.",
                    "mindamellett",
                    "The situation was exceptionally complicated; nevertheless, they succeeded in reaching a peaceful agreement on every detail.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["A", "szállóigék", "ismerete", "egyszersmind", "a", "kulturális", "otthonosság", "kulcsa."],
                    ["A", "szállóigék", "ismerete", "egyszersmind", "a", "kulturális", "otthonosság", "kulcsa."],
                    "Knowledge of household sayings is at the same time the key to cultural feeling at home.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Nyelvtanuló", "text": "Hogyan tanulhatom meg a magyarok rejtett kulturális utalásait és finom iróniáját?"},
                        {"speaker": "Mentortanár", "text": "_____"}
                    ],
                    [
                        "Olvass klasszikus novellákat, nézz kultikus magyar filmeket, és figyelj arra, mit mondanak a sorok között a barátaid.",
                        "Kizárólag a szótárakat olvasd és kerüld a személyes beszélgetéseket.",
                        "Ezeket az utalásokat lehetetlen megtanulni, ezért kár velük foglalkozni."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Mit jelképez a „Belső Pista” fogalma a magyar szellemi önreflexióban?",
                    [
                        "A józan szkepticizmus, a leleményes túlélés és a mély emberség belső iránytűjét.",
                        "Egy szigorú hivatalnokot a budapesti polgármesteri hivatalban.",
                        "Egy kitalált mesehőst, akit a gyermekek ijesztgetésére használnak."
                    ],
                    0
                )
            ]
        },
        {
            "num": 5,
            "title": "The Path Beyond B2: Toward C1 Fluency and Life in Hungarian",
            "grammar_label": "Capstone discourse cohesion: transitioning from B2 precision to C1 native-like spontaneity",
            "goals": [
                "I can reflect on my linguistic and cultural journey to B2 mastery in Hungarian and chart a course toward C1 fluency.",
                "I can integrate advanced discourse cohesion strategies for natural, spontaneous, and intellectually refined communication.",
                "I can enjoy authentic Hungarian novels, theatrical performances, intellectual debates, and everyday humor without hesitation."
            ],
            "story_segment": {
                "seg_slug": "utac1fele",
                "title": "Úton a C1 felé: Otthon lenni a magyar nyelvben",
                "summary": "Reaching B2 in Hungarian is a monumental milestone. Looking ahead to C1 means not just understanding the language, but living inside its poetry, debates, and vibrant warmth.",
                "location": "Budapest, a Duna-korzó és a Kárpát-medence szellemi tere",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A B2 szintű magyar nyelvtudás megszerzése kivételes intellektuális és emberi teljesítmény. A tanuló, aki átküzdötte magát a tizennyolc eset ragjain, az igekötők sokrétű szemantikai hálóján, az alanyi és tárgyas ragozás finomságain és a gazdag történelmi-kulturális fejezeteken, immár nem külső szemlélője, hanem aktív részese a magyar nyelvi világnak."
                    },
                    {
                        "type": "narration",
                        "text": "A B2 szinten a kommunikáció már nem a helyes ragok kereséséről szól, hanem a gondolatok szabad és árnyalt kifejezéséről. A tanuló képes követni egy színházi előadás gyors dialógusait a Katona József Színházban, élvezni Márai Sándor vagy Kosztolányi Dezső prózájának zeneiségét, és érdemben hozzászólni a legélesebb társadalmi és gazdasági vitákhoz is."
                    },
                    {
                        "type": "narration",
                        "text": "A C1 szint felé vezető út azonban még tágasabb távlatokat nyit. A C1 mesterszint nem egyszerűen több szót jelent, hanem a stílusbeli rugalmasság kiteljesedését: azt a képességet, hogy az ember könnyedén váltson a budapesti kávéházi csevegés közvetlen hangneme, a hivatalos jogi érvelés szabatossága és a lírai emelkedettség között."
                    },
                    {
                        "type": "narration",
                        "text": "Otthon lenni egy nyelvben annyit jelent, mint érezni a szavak ritmusát és belső dallamát. Amikor a nyelvtanuló már nem fejben fordít a saját anyanyelvéből, hanem közvetlenül magyarul álmodik, nevet és vitatkozik, a nyelv megszűnik idegen eszköznek lenni: otthonná válik, amelyben a lélek kiteljesedhet."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a tanulási utazás nem ér véget a B2 bizonyítvánnyal: épp ellenkezőleg, most kezdődik az igazi felfedezés. A magyar nyelv gazdagsága, játékossága és történelmi mélysége egész életre szóló szellemi kalandot kínál mindazoknak, akik nyitott szívvel lépnek be ebbe a csodálatos világba."
                    }
                ]
            },
            "words": [
                {"lemma": "nyelvi magabiztosság", "translation": "linguistic confidence / fluency", "pos": "expression"},
                {"lemma": "árnyalt kifejezésmód", "translation": "nuanced mode of expression", "pos": "expression"},
                {"lemma": "anyanyelvi szint", "translation": "native-like level", "pos": "expression"},
                {"lemma": "gördülékenység", "translation": "fluency / smoothness of delivery", "pos": "noun"},
                {"lemma": "kulturális otthonosság", "translation": "cultural feeling at home / belonging", "pos": "expression"},
                {"lemma": "elmélyülés", "translation": "deep immersion / deepening of insight", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "capstone-discourse-cohesion",
                "title": "Capstone Hungarian Discourse Cohesion and Stylistic Mastery",
                "text1_title": "Discourse Architecture: From Sentence Grammar to Textual Harmony",
                "text1": "At the apex of B2 and threshold of C1, grammar ceases to be an obstacle and becomes an artistic instrument. Discourse cohesion relies on orchestrating topic-comment structures, varied discourse connectors (mindamellett, egyszersmind, jóllehet, noha), participial embedding, and balanced rhetorical rhythm.",
                "text2_title": "Spontaneous Fluency and Register Control",
                "text2": "True mastery is demonstrated by knowing intuitively when to deploy concise participial phrases and elevated conjunctions in formal lectures, and when to drop into relaxed colloquial cadence without hesitation. This stylistic self-awareness transforms a competent speaker into a persuasive, memorable communicator.",
                "table_title": "Discourse Connectors Across Registers",
                "table_rows": [
                    ["emelkedett: jóllehet / noha", "köznyelvi: bár / habár (although)"],
                    ["emelkedett: mindazonáltal / mindamellett", "köznyelvi: mégis / azért (nevertheless)"],
                    ["emelkedett: egyszersmind", "köznyelvi: és egyben (at the same time)"],
                    ["emelkedett: amennyiben / feltéve, ha", "köznyelvi: ha (if / provided that)"]
                ],
                "examples": [
                    {"spanish": "A kitartó munka meghozta gyümölcsét: a diák nyelvi magabiztossága képessé teszi őt az önálló életre Magyarországon.", "english": "Persevering work bore fruit: the student's linguistic confidence enables them to live independently in Hungary."},
                    {"spanish": "A szavak pontos megválasztása és a gördülékeny előadásmód a C1 szint legfontosabb ismérve.", "english": "Accurate word choice and fluent delivery are the most important hallmarks of the C1 level."},
                    {"spanish": "Aki belép a magyar nyelv világába, az egy egész nép történelmével és kultúrájával gazdagodik.", "english": "Whoever enters the world of the Hungarian language is enriched by the history and culture of an entire people."}
                ],
                "tip": "Congratulations on completing the B2 Culture Track! Keep reading contemporary Hungarian literature, listening to podcasts, and engaging in lively conversations to sustain your fluency toward C1."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["nyelvi magabiztosság", "linguistic confidence"],
                        ["árnyalt kifejezésmód", "nuanced expression"],
                        ["anyanyelvi szint", "native-like level"],
                        ["gördülékenység", "fluency / smoothness"],
                        ["kulturális otthonosság", "cultural feeling at home"],
                        ["elmélyülés", "deep immersion"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Mit jelent a nyelvi és kulturális otthonosság elérése egy idegen nyelv tanulása során?",
                    [
                        "Azt, hogy a tanuló közvetlenül a célnyelven gondolkodik, és otthonosan mozog annak szellemi világában.",
                        "Azt, hogy a tanuló feladja a saját anyanyelvét és megtagadja korábbi kultúráját.",
                        "Azt, hogy kizárólag szállodákban és repülőtereken hajlandó tartózkodni."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A B2 szintű tudás megszilárdítása után a tanuló célja a C1 szint elérése és a beszéd tökéletes _____ .",
                    "gördülékenysége",
                    "After consolidating B2 knowledge, the student's goal is reaching C1 and the perfect fluency of speech.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik mondat testesíti meg a legválasztékosabb B2/C1 szintű mondatszerkesztést?",
                    [
                        "Jóllehet a nyelvtanulás kitartó munkát igényelt, a megszerzett tudás felbecsülhetetlen értékű szellemi kincs.",
                        "Bár sokat tanultam, de azért mégis marha nehéz volt az egész dolog.",
                        "Ha nem tanultam volna, akkor nem tudnék semmit sem most se.",
                        "Tanultam sokat, oszt most már beszélek magyarul rendesen."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A magyar kultúrában való elmélyülés _____ a személyiség fejlődésének és a világ megértésének csodálatos útja.",
                    "egyszersmind",
                    "Deep immersion in Hungarian culture is at the same time a wonderful path of personality development and understanding the world.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["A", "kitartó", "tanulás", "meghozta", "a", "kívánt", "nyelvi", "magabiztosságot."],
                    ["A", "kitartó", "tanulás", "meghozta", "a", "kívánt", "nyelvi", "magabiztosságot."],
                    "Persevering study brought about the desired linguistic confidence.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Tanár", "text": "Hogyan érzed magad most, hogy sikeresen teljesítetted a B2 magyar kultúra kurzust?"},
                        {"speaker": "Diák", "text": "_____"}
                    ],
                    [
                        "Büszke vagyok a megszerzett tudásra, és izgatottan várom a C1 szintű elmélyülést és a magyar irodalom további felfedezését.",
                        "Azonnal elfelejtek minden szót, mert nem akarok többé magyarul megszólalni.",
                        "Úgy érzem, a magyar nyelvnek nincs semmi értelme a modern világban."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Mi a legfőbb üzenete a B2 szintű magyar nyelvi utazás lezárásának?",
                    [
                        "A nyelv nem csupán kommunikációs eszköz, hanem egy egész nép történelmének és lelkének csodálatos otthona.",
                        "A nyelvtanulás kizárólag a nyelvvizsga bizonyítvány megszerzéséig fontos.",
                        "A magyar nyelv túl nehéz ahhoz, hogy bárki valaha is igazán megértse."
                    ],
                    0
                )
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can synthesize the overarching themes of Hungarian cultural, literary, and historical identity at B2 mastery.",
            "I can fluently integrate complex discourse connectors, participial clauses, and register shifts across varied topics.",
            "I can articulate my personal relationship with the Hungarian language and express readiness for C1 fluency."
        ],
        "exercises": [
            match(
                "vocabulary",
                "recognize",
                [
                    ["szigetnyelv", "island language"],
                    ["váteszköltő", "prophet-poet"],
                    ["sírva vigadás", "bittersweet merriment"],
                    ["szállóige", "household saying"],
                    ["kulturális kód", "cultural code"],
                    ["nyelvi magabiztosság", "linguistic confidence"]
                ],
                [VOCAB_SKILL]
            ),
            mc(
                "vocabulary",
                "recognize",
                "Melyik fogalom jelöli a magyar irodalom azon prófétai hagyományát, amely a költőt a nemzet lelkiismeretévé avatja?",
                ["váteszköltészet", "szleng", "nyelvújítás", "fotonika"],
                0,
                [VOCAB_SKILL]
            ),
            fb(
                "vocabulary",
                "recognize",
                "A magyar gondolkodásmód mélyebb megértéséhez elengedhetetlen a közös _____ és rejtett utalások ismerete.",
                "kulturális kódok",
                "For a deeper understanding of the Hungarian mindset, knowledge of shared cultural codes and implicit allusions is indispensable.",
                [VOCAB_SKILL]
            ),
            mc(
                "grammar",
                "recall",
                "Melyik mondat köti össze helyesen az ellentétes és kiegészítő állításokat választékos stílusban?",
                [
                    "A magyar irodalom mélyen nemzeti gyökerű, egyszersmind egyetemes emberi értékeket hordoz.",
                    "A magyar irodalom mélyen nemzeti gyökerű, hacsak egyetemes emberi értékeket hordoz.",
                    "A magyar irodalom mélyen nemzeti gyökerű, feltéve egyetemes emberi értékeket hordoz.",
                    "A magyar irodalom mélyen nemzeti gyökerű, minthogyha egyetemes emberi értékeket hordozna."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            fb(
                "grammar",
                "recall",
                "_____ a magyar nyelv rokontalan szigetként él Közép-Európában, ezer év kultúráját és gazdagságát őrzi magában.",
                "Jóllehet",
                "Although the Hungarian language lives as a kinless island in Central Europe, it preserves a thousand years of culture and richness within itself.",
                [GRAMMAR_SKILL]
            ),
            dc(
                "dialogue",
                [
                    {"speaker": "Kutató", "text": "Hogyan foglalnád össze a magyar nemzeti identitás és az anyanyelv kapcsolatát?"},
                    {"speaker": "Történész", "text": "_____"}
                ],
                [
                    "Az anyanyelv a nemzeti megmaradás legfőbb záloga: a történelem viharaiban a magyar nyelv őrizte meg a közösség önazonosságát.",
                    "Nincs semmilyen kapcsolat a nyelv és az identitás között, a magyarok bármilyen nyelven élhettek volna.",
                    "A nemzeti identitás kizárólag a katonai egyenruhák szabásmintáján alapul."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            dc(
                "dialogue",
                [
                    {"speaker": "Diák", "text": "Milyen érzés elérni a B2 szintet és felkészülni a C1 kihívásaira?"},
                    {"speaker": "Nyelvtanár", "text": "_____"}
                ],
                [
                    "Fantasztikus mérföldkő, hiszen a nyelvtan mechanikus tanulása után mostantól a gondolatok és stílusok szabad szárnyalása következik.",
                    "Nagy csalódás, mert a B2 szint után tilos új könyveket olvasni magyarul.",
                    "Semmit sem jelent, mert a nyelveket nem lehet szintekre osztani."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            mc(
                "grammar",
                "in-context",
                "Melyik kötőszó fejezi ki a legpontosabban a fenntartást vagy megfontolást az alábbi összetett mondatban? 'A történelmi kihívások rendkívül súlyosak voltak; _____ a nemzet mindig talált erőt az újrakezdéshez.'",
                ["mindazonáltal", "hacsak", "amennyiben", "minthogy"],
                0,
                [GRAMMAR_SKILL]
            ),
            dc(
                "dialogue",
                [
                    {"speaker": "Érdeklődő", "text": "Mi teszi a magyar költészetet annyira különlegessé és időtállóvá?"},
                    {"speaker": "Irodalmár", "text": "_____"}
                ],
                [
                    "Az, hogy a legmélyebb személyes érzelmeket szervesen összekapcsolta a társadalmi igazságosság és a nemzeti sorskérdések iránti felelősséggel.",
                    "Az, hogy minden költemény kizárólag két sorból állt és nem használt rímeket.",
                    "Az, hogy a költők kizárólag az uralkodók dicséretét zengték pénzjutalomért."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            sb(
                "grammar",
                "produce",
                ["A", "magyar", "nyelv", "ismerete", "egész", "életre", "szóló", "szellemi", "gazdagságot", "ad."],
                ["A", "magyar", "nyelv", "ismerete", "egész", "életre", "szóló", "szellemi", "gazdagságot", "ad."],
                "Knowledge of the Hungarian language gives a lifelong intellectual wealth.",
                [GRAMMAR_SKILL]
            ),
            sb(
                "grammar",
                "produce",
                ["Jóllehet", "nehéz", "volt", "az", "út,", "megérte", "elsajátítani", "ezt", "a", "szép", "nyelvet."],
                ["Jóllehet", "nehéz", "volt", "az", "út,", "megérte", "elsajátítani", "ezt", "a", "szép", "nyelvet."],
                "Although the journey was difficult, it was worth mastering this beautiful language.",
                [GRAMMAR_SKILL]
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a sentence using 'jóllehet' or 'mindazonáltal' summarizing the resilience of the Hungarian language.",
                        "answer": "Jóllehet a Kárpát-medencét évszázadokon át súlyos történelmi viharok tépázták, a magyar nyelv mindmáig megőrizte ősi finnugor gyökereit és egyedülálló kifejezőerejét."
                    },
                    {
                        "prompt": "Write a sentence using 'egyszersmind' reflecting on the transition from B2 to C1 mastery.",
                        "answer": "A B2 szintű tudás megszilárdítása hatalmas siker, egyszersmind inspiráló kaput nyit a C1 szint és a magyar kultúrában való teljes otthonosság felé."
                    }
                ],
                [GRAMMAR_SKILL]
            )
        ]
    }
}
