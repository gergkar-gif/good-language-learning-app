"""
Hungarian B2 Core Track Unit 34:
  b2-34: Slang, Register Shifting & Living Language
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_34 = {
    "unit_num": 34,
    "title": "Slang, Register Shifting & Living Language",
    "grammar_summary": "Expressive Hungarian twin-words and reduplications (gizgaz, limlom, csecsebecse, hercehurca, ímmel-ámmal), colloquial ellipsis, youth slang, register shifting from street vernacular to administrative prose, and linguistic wit.",
    "grammar_skill": "b2-twin-words-register",
    "vocab_skill": "b2-34-vocab",
    "theme": "Slang, register shifting and living language",
    "intro_body": [
        "Az élő magyar nyelv egyik legszínesebb és legdinamikusabb rétege a szleng, a mindennapi köznyelv és a vagány argó. A magyar különösen gazdag hangutánzó és hangulatfestő ikerszókban (csecsebecse, gizgaz, limlom, hercehurca), amelyek sajátos ritmust és képi kifejezőerőt kölcsönöznek a beszédnek.",
        "Ebben a fejezetben feltárjuk a magyar szleng belső logikáját, a társalgási ellipszist (mondatcsonkítást), valamint a stílusrétegek közötti tudatos váltás (register shifting) művészetét. Megtanulhatja, miként fordítható le egy laza ifjúsági fordulat hivatalos, választékos megfogalmazásra, és miként alkalmazható a finom pesti humor és irónia. A fejezet végén Rejtő Jenő felejthetetlen figurái, Piszkos Fred és Fülig Jimmy vezetik be a kikötői vagány nyelv rejtelmeibe.",
    ],
    "classic_story": {
        "slug": "piszkosfred",
        "author": "Rejtő Jenő",
        "work": "Piszkos Fred, a kapitány (1940)",
        "title": "Kalandok és vagány párbeszédek a kikötőben",
        "summary": "A szingapúri kikötő füstös kocsmájában Fülig Jimmy és a titokzatos Piszkos Fred sajátos pesti vagány humorral és szójátékokkal fűszerezve tárgyalják meg a legújabb tengeri zűrzavart.",
        "characters": ["Piszkos Fred", "Fülig Jimmy"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A szingapúri kikötő egyik sötét, füstös ivójában, ahol a világ minden tengerének matrózai megfordultak már, Fülig Jimmy éppen egy pohár rum mellett üldögélt, és a legújabb kalamajkán törte a fejét. Az asztalok körül zsibongott a sokféle nyelv, de az igazi pesti vagány duma összetéveszthetetlen maradt volna a világ végén is.",
            },
            {
                "type": "dialogue",
                "speaker": "Piszkos Fred",
                "text": "Látom, Jimmy fiam, megint beleütötted az orrodat olyan hercehurcába, amiből csak csip-csup pofonok árán lehet kikeveredni. Mi ez a nagy titkolózás a gőzös körül?",
            },
            {
                "type": "dialogue",
                "speaker": "Fülig Jimmy",
                "text": "Ugyan már, tisztelt kapitány úr! Nincs itt semmi hercehurca, csak némi apró-cseprő félreértés a hatóságokkal. Azt hitték, hogy az a láda tele van arannyal, holott csak ócska limlom és néhány csecsebecse lapult benne.",
            },
            {
                "type": "narration",
                "text": "Piszkos Fred gyanakvó pillantást vetett cinkostársára, miközben viharvert cilinderét a homlokába húzta. Jól ismerte Jimmy szószátyár természetét: valahányszor ilyen ártatlan képpel magyarázkodott, biztosra lehetett venni, hogy a dolgok hátterében valami egetverő csínytevés húzódik.",
            },
            {
                "type": "dialogue",
                "speaker": "Piszkos Fred",
                "text": "Ne etess engem ezzel a mesével, Jimmy! Nem ma jöttem a falvédőről. Ha a felügyelő rákattan a nyomunkra, mindketten beégünk a kikötői rendőrségen, és akkor aztán magyarázhatod hivatalos nyelven az ártatlanságodat.",
            },
            {
                "type": "dialogue",
                "speaker": "Fülig Jimmy",
                "text": "Nyugalom, Fred úr, én mindig bevállalom a kockázatot! A haverok már elrendezték a papírokat, úgyhogy ha kénytelenek leszünk hivatalos stílusra váltani, a jegyzőkönyv szerint feddhetetlen tengeri kereskedők vagyunk, akik csupán jóhiszeműen jártak el.",
            },
            {
                "type": "narration",
                "text": "A kocsma zaja hirtelen alábbhagyott, amikor odakint felbőgött egy gőzhajó szirénája. Az éjszaka leple alatt megérkezett a várva várt szállítmány, és mindketten tudták, hogy most már nincs helye több viccelődésnek meg szócséplésnek: cselekedni kellett.",
            },
            {
                "type": "narration",
                "text": "Fred bólintott, fizetett a pultnál, és kilépett a párás trópusi éjszakába, Jimmy pedig szorosan a sarkában loholt. Rejtő hősei még a legveszélyesebb helyzetekben is hűek maradtak sajátos pesti humorukhoz, amelyben a fanyar irónia és a vagány talpraesettség jelentette a túlélés zálogát.",
            },
        ],
        "reading_questions": [
            {
                "question": "Miért figyelmezteti Piszkos Fred Fülig Jimmyt a kikötői ivóban?",
                "options": [
                    "Mert tart attól, hogy Jimmy felelőtlen csínytevése felkelti a hatóságok figyelmét és lebuknak.",
                    "Mert Jimmy nem akarta kifizetni a pultosnak a rendelt italokat.",
                    "Mert Fred azonnal el akarta adni Jimmy gőzhajóját egy kereskedőnek.",
                ],
                "correct": 0,
            },
            {
                "question": "Mit állít Fülig Jimmy a gyanús tengeri láda tartalmáról?",
                "options": [
                    "Hogy arany helyett csupán értéktelen limlom és néhány csecsebecse lapult benne.",
                    "Hogy a láda tele volt a sziget kormányzójának szánt kincsekkel.",
                    "Hogy a ládát a viharban elveszítették a tenger mélyén.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen túlélési stratégiát tükröz a szereplők viselkedése a nehéz helyzetekben?",
                "options": [
                    "A fanyar humort, a vagány talpraesettséget és a laza stílusrétegek magabiztos kezelését.",
                    "A hatóságok előtti megalázkodást és a szigorú bűnbánatot.",
                    "A teljes csendet és a társalgás teljes elkerülését.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Expressive Twin-Words and Reduplications (gizgaz, limlom, csecsebecse, hercehurca)",
            "grammar_label": "Expressive Hungarian twin-words and reduplications (gizgaz, limlom, csecsebecse, hercehurca, ímmel-ámmal)",
            "goals": [
                "I can identify and use Hungarian rhyming compounds and twin-words in spoken and written discourse",
                "I can distinguish vowel-alternating reduplications like csihi-puhi from rhyming pairs",
                "I can express reluctance and negligence using idiomatic twin-words like ímmel-ámmal",
            ],
            "grammar_doc": {
                "slug": "expressive-twin-words-reduplications",
                "title": "Expressive Twin-Words and Reduplications: gizgaz, limlom, csecsebecse, hercehurca",
                "text1_title": "Morphological Structure of Hungarian Twin-Words (Ikerszók)",
                "text1": "Hungarian features an exceptionally rich layer of expressive twin-words (ikerszók) and reduplicated stems. These words are created either through rhyming (rímelő ikerszók) where the initial consonant alters while the vowel core remains identical ('gizgaz', 'limlom', 'hercehurca', 'csecsebecse'), or through vowel alternation (ablaut or tőbelseji magánhangzó-váltakozás) where the consonants remain stable while the vowel alternates between front and back ('csihi-puhi', 'dirib-darab', 'ingó-bingó').",
                "text2_title": "Discourse Functions and Suffixation Rules",
                "text2": "Twin-words infuse Hungarian speech with expressive, diminutive, or mildly derogatory nuances. When twin-words are written as a single hyphenated or compound noun, inflectional suffixes attach solely to the second stem: 'limlomot', 'csecsebecsékkel', 'hercehurcát'. Adverbial twin-words express attitude or manner: 'ímmel-ámmal' signifies doing something half-heartedly, grudgingly, or without genuine enthusiasm.",
                "table_title": "Core Hungarian Expressive Twin-Words",
                "table_rows": [
                    ["gizgaz", "A kert végében teljesen elszaporodott a gizgaz. (The scrub and weeds grew wildly.)"],
                    ["limlom", "Hétvégén kidobjuk a pincéből a felgyülemlett limlomot. (We will throw out the accumulated junk.)"],
                    ["csecsebecse", "Csillogó csecsebecsékkel díszítették fel a polcokat. (They decorated the shelves with trinkets.)"],
                    ["hercehurca", "Végre véget ért az adóbevallással járó sok hercehurca. (Finally the hassle of the tax return ended.)"],
                    ["ímmel-ámmal", "Csak ímmel-ámmal fogott hozzá a takarításhoz. (He started cleaning only half-heartedly.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az elhagyatott gyárudvart az évek során teljesen felverte a szúrós gizgaz.",
                        "english": "Over the years, the abandoned factory yard was completely overgrown with prickly weeds.",
                    },
                    {
                        "spanish": "Mielőtt az új lakásba költöznénk, meg kell szabadulnunk a felesleges limlomtól.",
                        "english": "Before moving into the new apartment, we must get rid of the unnecessary junk.",
                    },
                    {
                        "spanish": "A bazárban rengeteg színes csecsebecsét kínáltak a turistáknak.",
                        "english": "In the bazaar, they offered heaps of colorful trinkets to the tourists.",
                    },
                    {
                        "spanish": "A bürokratikus hercehurca miatt hónapokat késett az építkezés megkezdése.",
                        "english": "Due to the bureaucratic hassle, the start of construction was delayed by months.",
                    },
                ],
                "tip": "Remember that compound twin-words inflect only on their second part in contemporary Hungarian: 'limlomot gyűjt', 'csecsebecsékért rajong'. Do not inflect both elements unless dealing with fixed historical adverbs such as 'ímmel-ámmal'.",
            },
            "words": [
                {"lemma": "gizgaz", "translation": "weeds / scrub / unwanted growth", "pos": "noun"},
                {"lemma": "limlom", "translation": "junk / bric-a-brac / clutter", "pos": "noun"},
                {"lemma": "csecsebecse", "translation": "knick-knack / trinket / bauble", "pos": "noun"},
                {"lemma": "hercehurca", "translation": "hassle / fuss / bureaucratic runaround", "pos": "noun"},
                {"lemma": "ímmel-ámmal", "translation": "reluctantly / half-heartedly", "pos": "adverb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does the Hungarian twin-word 'limlom' designate?",
                        [
                            "worthless clutter, discarded junk, or miscellaneous bric-a-brac",
                            "a prestigious high-society formal dinner party",
                            "an official government stamp on legal certificates",
                        ],
                        0,
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which twin-word means tedious hassle, fuss, or administrative runaround?",
                        ["hercehurca", "csecsebecse", "gizgaz"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["gizgaz", "weeds / unwanted scrub"],
                            ["limlom", "junk / clutter / bric-a-brac"],
                            ["csecsebecse", "knick-knack / trinket"],
                            ["hercehurca", "hassle / bureaucratic fuss"],
                            ["ímmel-ámmal", "reluctantly / half-heartedly"],
                        ],
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "How do compound twin-words like 'csecsebecse' and 'limlom' take case suffixes in modern Hungarian?",
                        [
                            "Only the second stem is suffixed (e.g., 'csecsebecséket', 'limlommal').",
                            "Both stems must receive identical suffixes simultaneously.",
                            "Twin-words are completely indeclinable and cannot take suffixes.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What attitude is conveyed by the adverbial expression 'ímmel-ámmal dolgozik'?",
                        [
                            "Working reluctantly, half-heartedly, and without enthusiasm.",
                            "Working with lightning speed and flawless precision.",
                            "Working under strict military supervision.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A telek sarkát teljesen benőtte a száraz ____. (weeds / wild scrub)",
                        "gizgaz",
                        "The corner of the lot was completely overgrown with dry weeds.",
                        ["b2-twin-words-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Nem éri meg az a rengeteg hivatali ____, amibe a beadvány kerülne. (hassle / fuss)",
                        "hercehurca",
                        "The enormous amount of bureaucratic hassle that the submission would entail is not worth it.",
                        ["b2-twin-words-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "fiú", "csak", "ímmel-ámmal", "végezte", "el", "a", "rábízott", "feladatot."],
                        ["A", "fiú", "csak", "ímmel-ámmal", "végezte", "el", "a", "rábízott", "feladatot."],
                        "The boy performed the entrusted task only half-heartedly.",
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A költözéskor három doboznyi felesleges ____ dobtunk ki a lomtalanításkor. (junk / clutter)",
                        "limlomot",
                        "When moving, we threw out three boxes of unnecessary junk during clearance.",
                        ["b2-34-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "polc", "tele", "volt", "mindenféle", "csillogó", "csecsebecsével."],
                        ["A", "polc", "tele", "volt", "mindenféle", "csillogó", "csecsebecsével."],
                        "The shelf was full of all kinds of glittering trinkets.",
                        ["b2-34-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Gábor", "text": "Végre sikerült elintézned az építési engedélyt a telekre?"},
                            {"speaker": "Eszter", "text": "____"},
                        ],
                        [
                            "Igen, de olyan elképesztő hercehurca volt a hivatalban, hogy majdnem feladtam.",
                            "Persze, a virágágyásban csak limlom nőtt a tavasz óta.",
                            "Nem, mert a csecsebecsék azonnal kigyulladtak a napon.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Mihály", "text": "Miért haladsz ilyen lassan a fordítással?"},
                            {"speaker": "Katalin", "text": "____"},
                        ],
                        [
                            "Őszintén szólva ma csak ímmel-ámmal dolgozom, mert nagyon kimerült vagyok.",
                            "Mert a gizgaz azonnal lefordította az egész fejezetet.",
                            "Minden mondat hercehurcát képez a szótárban.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'limlom' in the accusative (-ot) to describe clearing out a cluttered space.",
                                "answer": "Hétvégén végre rászántuk magunkat, és elszállíttattuk a padláson összegyűlt limlomot.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'hercehurca' describing a complicated administrative procedure.",
                                "answer": "Senki sem számított arra, hogy az útlevél megújítása ilyen hosszas hercehurcával fog járni.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A nagymama vitrinjében számtalan apró porcelán ____ sorakozott. (trinket / knick-knack)",
                        "csecsebecse",
                        "Countless tiny porcelain trinkets lined the grandmother's display cabinet.",
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adverb means 'half-heartedly' or 'reluctantly'?",
                        ["ímmel-ámmal", "hercehurca", "gizgaz"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Colloquial Shortenings, Expressive Interjections, and Sentence Fragments",
            "grammar_label": "Colloquial syntax, expressive particle ellipsis, and emotional tags (ugyan már, dehogyis, elvégre, mondhatni, lényegében)",
            "goals": [
                "I can use expressive interjections like 'ugyan már' and 'dehogyis' to refute assumptions emphatically",
                "I can deploy colloquial tags like 'elvégre' and 'szóval' to structure informal explanations",
                "I can interpret conversational ellipsis and expressive sentence fragments in spoken Hungarian",
            ],
            "grammar_doc": {
                "slug": "colloquial-shortenings-ellipsis",
                "title": "Colloquial Shortenings, Expressive Interjections, and Sentence Fragments",
                "text1_title": "Conversational Ellipsis and Emotional Interjections",
                "text1": "Spoken Hungarian relies heavily on conversational ellipsis (társalgási ellipszis), where shared background knowledge allows speakers to omit full verb phrases, copulas, and formal subordinators. Emotional tags and pragmatic particles step into these omitted spaces to steer speaker stance: 'ugyan már' expresses dismissal of an exaggeration or mild disbelief ('come on!', 'as if!'), while 'dehogyis' provides an emphatic, categorical denial ('by no means!', 'not in the slightest!').",
                "text2_title": "Structuring Informal Explanations with Discourse Markers",
                "text2": "Particles such as 'elvégre' (after all, at the end of the day) introduce rationalizations or pragmatic justification. Modifiers like 'lényegében' (essentially) and 'mondhatni' (one might say, so to speak) allow speakers to qualify assertions without sounding pedantic, softening assertions and maintaining interpersonal rapport.",
                "table_title": "Core Colloquial Tags and Shortenings",
                "table_rows": [
                    ["ugyan már", "Ugyan már, nem kell mindent a szívedre venned! (Come on, you shouldn't take everything to heart!)"],
                    ["dehogyis", "Dehogyis haragszom rád, csak meglepődtem. (Not at all am I angry with you, I was just surprised.)"],
                    ["elvégre", "Segítenünk kell neki, elvégre régi jó barátunk. (We must help him; after all, he is our old good friend.)"],
                    ["mondhatni", "Az előadás mondhatni várakozáson felül sikerült. (The presentation succeeded, one might say, beyond expectations.)"],
                    ["lényegében", "Lényegében mindenben megegyeztünk a tárgyaláson. (Essentially, we agreed on everything at the negotiation.)"],
                ],
                "examples": [
                    {
                        "spanish": "Ugyan már, ne mondd nekem, hogy nem vetted észre a nyilvánvaló jeleket!",
                        "english": "Come on, don't tell me that you didn't notice the obvious signs!",
                    },
                    {
                        "spanish": "Félsz a vizsgától? – Dehogyis, alaposan felkészültem az összes tételből.",
                        "english": "Are you afraid of the exam? – Not at all, I prepared thoroughly from all the topics.",
                    },
                    {
                        "spanish": "Nem szabad feladnod a kutatást, elvégre éveket fektettél ebbe a projektbe.",
                        "english": "You must not give up the research; after all, you invested years into this project.",
                    },
                    {
                        "spanish": "A terv lényegében életképes, habár néhány apró részlet még pontosításra szorul.",
                        "english": "The plan is essentially viable, although a few minor details still need refinement.",
                    },
                ],
                "tip": "In colloquial conversation, 'ugyan már' is often spoken with a falling-rising intonation that indicates friendly skepticism. Avoid using it in formal written appeals, where 'tiszteletteljesen vitatom' or 'megkérdőjelezhetőnek tartom' is required.",
            },
            "words": [
                {"lemma": "ugyan már", "translation": "come on / nonsense / don't be ridiculous", "pos": "expression"},
                {"lemma": "dehogyis", "translation": "not at all / by no means / no way", "pos": "adverb"},
                {"lemma": "elvégre", "translation": "after all / when all is said and done", "pos": "adverb"},
                {"lemma": "mondhatni", "translation": "so to speak / one might say", "pos": "adverb"},
                {"lemma": "lényegében", "translation": "essentially / in essence", "pos": "adverb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the communicative function of 'ugyan már' in spoken Hungarian?",
                        [
                            "to express friendly disbelief, dismissal of an overstatement, or reassuring protest",
                            "to greet a superior in a ministry office",
                            "to announce the departure of an intercity train",
                        ],
                        0,
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which word means 'after all' or 'when all is said and done' when justifying an action?",
                        ["elvégre", "dehogyis", "ugyan már"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["ugyan már", "come on / nonsense / don't be ridiculous"],
                            ["dehogyis", "not at all / by no means"],
                            ["elvégre", "after all / when all is said and done"],
                            ["mondhatni", "so to speak / one might say"],
                            ["lényegében", "essentially / in essence"],
                        ],
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which tag provides an emphatic, categorical negative response to a question?",
                        ["dehogyis", "elvégre", "lényegében"],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence where 'elvégre' functions correctly as a justifying discourse marker:",
                        [
                            "Megbocsátottam neki, elvégre emberből vagyunk és mindannyian tévedhetünk.",
                            "Elvégre megitta a kávét az asztal alatt tegnap este.",
                            "A vonat elvégre a síneken futott háromszor.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Nem kell aggódnod a késés miatt, ____ még el sem kezdődött a megbeszélés. (after all)",
                        "elvégre",
                        "You don't need to worry about being late; after all, the meeting hasn't even started yet.",
                        ["b2-twin-words-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "____, ne beszélj butaságokat, senki sem akar megbántani téged! (come on / nonsense)",
                        "Ugyan már",
                        "Come on, don't talk nonsense, nobody wants to hurt you!",
                        ["b2-twin-words-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "vita", "során", "lényegében", "minden", "fontos", "kérdésben", "dűlőre", "jutottunk."],
                        ["A", "vita", "során", "lényegében", "minden", "fontos", "kérdésben", "dűlőre", "jutottunk."],
                        "During the debate, we essentially reached an agreement on every important issue.",
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Megbántódtál a megjegyzésemen? – ____, egyáltalán nem vettem magamra. (not at all / no way)",
                        "Dehogyis",
                        "Were you offended by my remark? – Not at all, I didn't take it personally at all.",
                        ["b2-34-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kísérlet", "mondhatni", "tökéletesen", "igazolta", "a", "korábbi", "hipotézisünket."],
                        ["A", "kísérlet", "mondhatni", "tökéletesen", "igazolta", "a", "korábbi", "hipotézisünket."],
                        "The experiment, so to speak, perfectly verified our previous hypothesis.",
                        ["b2-34-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Zoltán", "text": "Biztos vagy benne, hogy nem sértődött meg a kolléga a kritikádon?"},
                            {"speaker": "Lilla", "text": "____"},
                        ],
                        [
                            "Dehogyis sértődött meg, elvégre kifejezetten kérte a szakmai visszajelzést.",
                            "Ugyan már, a gizgaz azonnal felrobbant a laborban.",
                            "Lényegében minden limlomot megvettünk az árverésen tegnap.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Béla", "text": "Nem túl kockázatos belevágni ebbe a vállalkozásba most?"},
                            {"speaker": "Ágnes", "text": "____"},
                        ],
                        [
                            "Ugyan már, minden vállalkozás kockázattal jár, de lényegében alaposan felkészültünk.",
                            "Dehogyis, a hercehurca mindig süteményt eszik a konyhában.",
                            "Elvégre a mondhatni sosem lép be a hivatalos terembe.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'ugyan már' to gently dismiss a friend's excessive self-criticism.",
                                "answer": "Ugyan már, ne hibáztasd magad a történtekért, hiszen te mindent megtettél a sikerért!",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'elvégre' to justify making an exception for someone.",
                                "answer": "Megérdemli a pihenést a nehéz hét után, elvégre éjt nappallá téve dolgozott a projekten.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A két javaslat között ____ nincs érdemi különbség. (essentially / in essence)",
                        "lényegében",
                        "Between the two proposals, there is essentially no substantive difference.",
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adverbial phrase means 'so to speak' or 'one might say'?",
                        ["mondhatni", "ugyan már", "dehogyis"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Youth Slang, Street Register, and Subcultural Jargon",
            "grammar_label": "Youth slang, street register, and subcultural jargon (bevállal, kiakad, rákattan, átlát, duma)",
            "goals": [
                "I can recognize and interpret common Hungarian youth slang verbs with metaphorical preverbs",
                "I can use expressive colloquial verbs like bevállal, kiakad, and rákattan in social conversations",
                "I can evaluate the stylistic appropriateness of slang terms across different communicative settings",
            ],
            "grammar_doc": {
                "slug": "youth-slang-street-register",
                "title": "Youth Slang, Street Register, and Subcultural Jargon: bevállal, kiakad, rákattan",
                "text1_title": "Metaphorical Extension in Slang Verbs",
                "text1": "Hungarian youth slang generates new expressive vocabulary largely through preverbal metaphor. Standard spatial verbs take on psychological and social connotations: 'bevállal' (to take on a challenge, dare to commit to something risky), 'kiakad' (literally 'to unhook/jam', colloquially to freak out, lose one's temper, or be appalled), and 'rákattan' (literally 'to click onto', colloquially to become hooked or obsessed with something).",
                "text2_title": "Sociolinguistic Boundaries and Communicative Competence",
                "text2": "Nouns like 'duma' (smooth talk, chatter, banter, or empty rhetoric) and verbs like 'átlát' (to see through someone's pretenses or fathom a complex system) bridge colloquial street talk and informal peer interactions. Achieving B2 competence means understanding these vivid figures of speech when native speakers use them in casual settings, while recognizing where their usage would be inappropriate (such as academic essays or formal administration).",
                "table_title": "Popular Contemporary Colloquial and Slang Terms",
                "table_rows": [
                    ["bevállal", "Ki merné bevállalni az előadást a beteg kolléga helyett? (Who would dare take on the presentation?)"],
                    ["kiakad", "Teljesen kiakadt, amikor meglátta a horribilis számlát. (He totally freaked out when he saw the bill.)"],
                    ["rákattan", "A fiatalok azonnal rákattantak az új videójátékra. (The young people instantly got hooked on the new game.)"],
                    ["átlát", "Gyorsan átlátja a legbonyolultabb helyzeteket is. (He sees through even the most complex situations quickly.)"],
                    ["duma", "Hagyd a felesleges dumát, térjünk a lényegre! (Cut the idle chatter, let's get down to business!)"],
                ],
                "examples": [
                    {
                        "spanish": "Nem mindenki meri bevállalni azt a kockázatot, amivel egy induló startup vezetése jár.",
                        "english": "Not everyone dares take on the risk involved in running an early-stage startup.",
                    },
                    {
                        "spanish": "A professzor teljesen kiakadt, amikor a diákok puskázni próbáltak a vizsgán.",
                        "english": "The professor completely freaked out when the students tried to cheat on the exam.",
                    },
                    {
                        "spanish": "A lány annyira rákattant a magyar irodalomra, hogy naponta kiolvas egy könyvet.",
                        "english": "The girl got so hooked on Hungarian literature that she finishes a book every day.",
                    },
                    {
                        "spanish": "A tapasztalt nyomozó azonnal átlátta a gyanúsított ravasz trükkjeit.",
                        "english": "The experienced investigator immediately saw through the suspect's cunning tricks.",
                    },
                ],
                "tip": "While 'bevállal' is widely used even in contemporary media interviews, avoid using 'duma' or 'kiakad' in formal correspondence. Replace 'bevállal' with 'elvállal' or 'felvállal', 'kiakad' with 'megdöbben' or 'felháborodik', and 'duma' with 'érvelés' or 'beszéd'.",
            },
            "words": [
                {"lemma": "bevállal", "translation": "to take on / step up to / dare to do", "pos": "verb"},
                {"lemma": "kiakad", "translation": "to freak out / lose one's temper", "pos": "verb"},
                {"lemma": "rákattan", "translation": "to get hooked on / become obsessed with", "pos": "verb"},
                {"lemma": "átlát", "translation": "to see through / grasp clearly", "pos": "verb"},
                {"lemma": "duma", "translation": "smooth talk / banter / chatter", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does the colloquial verb 'rákattan' express?",
                        [
                            "to become hooked, enthusiastic, or obsessed with something",
                            "to turn off a computer switch manually",
                            "to lock a front door with two turns of a key",
                        ],
                        0,
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which slang verb means to freak out, lose one's temper, or be deeply shocked?",
                        ["kiakad", "bevállal", "átlát"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["bevállal", "to take on / dare to do"],
                            ["kiakad", "to freak out / lose temper"],
                            ["rákattan", "to get hooked on"],
                            ["átlát", "to see through / grasp"],
                            ["duma", "smooth talk / banter"],
                        ],
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case does 'rákattan' govern when indicating the object of obsession?",
                        ["sublative (-ra/-re)", "inessive (-ban/-ben)", "ablative (-tól/-től)"],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What is the formal, standard equivalent of the slang verb 'bevállal'?",
                        ["elvállal / felelősséget vállal", "kiakad / felháborodik", "elszalad / elmenekül"],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A diákok teljesen ____, amikor kiderült, hogy szombaton is be kell jönniük. (freaked out / lost temper)",
                        "kiakadtak",
                        "The students completely freaked out when it turned out they also had to come in on Saturday.",
                        ["b2-twin-words-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Ki merné ____ a nehéz feladat vezetését a jelenlegi körülmények között? (take on / step up to)",
                        "bevállalni",
                        "Who would dare take on leading the difficult task under the present circumstances?",
                        ["b2-twin-words-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "fiatal", "mérnök", "nagyon", "gyorsan", "átlátta", "a", "bonyolult", "rendszer", "működését."],
                        ["A", "fiatal", "mérnök", "nagyon", "gyorsan", "átlátta", "a", "bonyolult", "rendszer", "működését."],
                        "The young engineer grasped the functioning of the complex system very quickly.",
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A nyári szünetben a testvérem teljesen ____ a kerékpározásra. (got hooked on)",
                        "rákattant",
                        "During the summer break, my brother got totally hooked on cycling.",
                        ["b2-34-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Ne", "foglalkozz", "a", "rosszindulatú", "dumával,", "inkább", "a", "munkádra", "figyelj!"],
                        ["Ne", "foglalkozz", "a", "rosszindulatú", "dumával,", "inkább", "a", "munkádra", "figyelj!"],
                        "Don't mind the malicious talk, pay attention to your work instead!",
                        ["b2-34-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Tamás", "text": "Hogy fogadta a főnök az új projekttervet?"},
                            {"speaker": "Nóra", "text": "____"},
                        ],
                        [
                            "Először kiakadt a magas költségek miatt, de miután bevállaltuk az optimalizálást, megnyugodott.",
                            "Azonnal gizgazt evett a teraszon minden munkatárs előtt.",
                            "Nem mondott semmit, mert a csecsebecse elfelejtette a jelszót.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Péter", "text": "Hogyan tanultál meg ilyen gyorsan programozni?"},
                            {"speaker": "Anna", "text": "____"},
                        ],
                        [
                            "Tavaly rákattantam a gépi tanulásra, és hamar átláttam a legfontosabb algoritmusokat.",
                            "Mindig hercehurcát hordok a táskámban a biztonság kedvéért.",
                            "A duma miatt a vonat sosem érkezik meg időben az állomásra.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'bevállal' describing undertaking a demanding personal challenge.",
                                "answer": "Sokan meglepődtek, hogy Péter bevállalta a maratoni futást felkészülés nélkül.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'átlát' with an accusative object describing analytical competence.",
                                "answer": "A rutinos vezető azonnal átlátta a gazdasági válság valós kockázatait.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Nem tudom, mi történt vele, de tegnap valami apróság miatt teljesen ____. (freaked out)",
                        "kiakadt",
                        "I don't know what happened to him, but yesterday he completely freaked out over some minor thing.",
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which colloquial noun refers to smooth talk, empty chatter, or banter?",
                        ["duma", "gizgaz", "limlom"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Register Shifting: Translating Slang to Formal Hungarian",
            "grammar_label": "Register shifting: converting colloquial discourse to formal and administrative Hungarian",
            "goals": [
                "I can translate colloquial slang expressions into formal and administrative equivalents",
                "I can apply nominalization and high-register vocabulary to elevate conversational sentences",
                "I can select appropriate stylistic registers based on addressee and communicative purpose",
            ],
            "grammar_doc": {
                "slug": "register-shifting-slang-to-formal",
                "title": "Register Shifting: Translating Slang to Formal Hungarian",
                "text1_title": "The Register Spectrum in Contemporary Hungarian",
                "text1": "Hungarian operates along a pronounced register continuum ranging from intimate street slang (szleng / argó) through colloquial vernacular (köznyelvi / bizalmas) to cultured formal and administrative registers (választékos / hivatalos stílusréteg). Mastery of B2 Hungarian involves the ability to consciously shift between registers: translating informal notions into precise, objective formulations suitable for official petitions, workplace reports, or academic debate.",
                "text2_title": "Lexical Substitution and Syntactic Elevation",
                "text2": "When elevating colloquial Hungarian to formal style, several systematic transformations occur. Colloquial idioms are replaced by precise adjectives and nominalizations: 'a haverokkal lóg' becomes 'társas kapcsolatokat ápol', 'a meló befuccsolt' transforms into 'a projekt meghiúsult'. The adjective 'illetékes' (authorized/competent) replaces casual references to officials, while verbs like 'megfogalmaz' denote the deliberate articulation of opinions.",
                "table_title": "Colloquial vs. Formal Register Equivalents",
                "table_rows": [
                    ["haver / cimbora", "kolléga / munkatárs / ismerős (Formal equivalent)"],
                    ["meló / melózik", "munkavégzés / tevékenységet folytat (Formal equivalent)"],
                    ["befuccsol / beég", "meghiúsul / kudarccal végződik (Formal equivalent)"],
                    ["bevállal", "felelősséget vállal / magára vállal (Formal equivalent)"],
                    ["duma / sóder", "állásfoglalás / érvelés / nyilatkozat (Formal equivalent)"],
                ],
                "examples": [
                    {
                        "spanish": "A laza társalgási formákat a hivatalos levélben választékos stílusrétegre kell cserélnünk.",
                        "english": "We must replace informal conversational forms with a polished stylistic register in an official letter.",
                    },
                    {
                        "spanish": "Kérjük, hogy beadványát az illetékes hivatal vezetőjének címezve szíveskedjék elküldeni.",
                        "english": "Please be so kind as to send your petition addressed to the head of the competent office.",
                    },
                    {
                        "spanish": "A panaszos pontosan és szabatosan megfogalmazta kifogásait a jegyzőkönyvben.",
                        "english": "The complainant formulated their objections precisely and accurately in the official record.",
                    },
                    {
                        "spanish": "A köznyelvi kifejezések helyett a hivatalos ügyintézésben szakkifejezéseket alkalmazunk.",
                        "english": "Instead of colloquial expressions, we use specialized terminology in official administration.",
                    },
                ],
                "tip": "Pay close attention to passive and nominal constructions when writing formally. Whereas a spoken conversation might use active personal forms ('Kipécéztük a hibát'), official reports prefer impersonal nominal phrases ('A hiba azonosításra került').",
            },
            "words": [
                {"lemma": "illetékes", "translation": "competent / authorized / relevant", "pos": "adjective"},
                {"lemma": "hivatalos", "translation": "official / formal", "pos": "adjective"},
                {"lemma": "megfogalmaz", "translation": "to formulate / word / phrase", "pos": "verb"},
                {"lemma": "köznyelvi", "translation": "colloquial / standard vernacular", "pos": "adjective"},
                {"lemma": "stílusréteg", "translation": "stylistic register / level of style", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'illetékes hatóság' designate in formal administrative Hungarian?",
                        [
                            "the authorized or competent authority possessing jurisdiction over a matter",
                            "a casual group of friends chatting in an online forum",
                            "an illegal assembly of merchants in a street market",
                        ],
                        0,
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which verb means to formally articulate, word, or formulate a statement?",
                        ["megfogalmaz", "kiakad", "bevállal"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["illetékes", "competent / authorized"],
                            ["hivatalos", "official / formal"],
                            ["megfogalmaz", "to formulate / articulate"],
                            ["köznyelvi", "colloquial / vernacular"],
                            ["stílusréteg", "stylistic register / level"],
                        ],
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "How should the colloquial sentence 'A meló befuccsolt a haver miatt' be translated into formal Hungarian?",
                        [
                            "A projekt a munkatárs mulasztása következtében meghiúsult.",
                            "A duma nagyon kiakadt a gizgaz miatt.",
                            "A limlom elrepült a hercehurcával együtt tegnap.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which linguistic register is appropriate for an official appeal to an administrative court?",
                        [
                            "hivatalos és választékos stílusréteg (formal and refined register)",
                            "ifjúsági szleng és argó (youth slang and argot)",
                            "családi bizalmas társalgás (informal family conversation)",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A kérelmet közvetlenül az ____ minisztériumi osztályhoz kell benyújtani. (competent / relevant)",
                        "illetékes",
                        "The application must be submitted directly to the competent ministerial department.",
                        ["b2-twin-words-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A jogi képviselő rendkívül szabatosan ____ meg ügyfele követeléseit. (formulated / articulated)",
                        "fogalmazta",
                        "The legal representative formulated his client's claims extremely accurately.",
                        ["b2-twin-words-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "beadványban", "a", "köznyelvi", "szófordulatokat", "hivatalos", "kifejezésekre", "kell", "cserélni."],
                        ["A", "beadványban", "a", "köznyelvi", "szófordulatokat", "hivatalos", "kifejezésekre", "kell", "cserélni."],
                        "In the petition, colloquial idioms must be replaced with official expressions.",
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az írásbeli vizsgán a jelöltnek igazolnia kell a különböző ____ közötti váltás képességét. (stylistic registers)",
                        "stílusrétegek",
                        "In the written exam, the candidate must demonstrate the ability to switch between different stylistic registers.",
                        ["b2-34-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "szerződés", "bontásáról", "szóló", "hivatalos", "értesítés", "tegnap", "érkezett", "meg."],
                        ["A", "szerződés", "bontásáról", "szóló", "hivatalos", "értesítés", "tegnap", "érkezett", "meg."],
                        "The official notification concerning the termination of the contract arrived yesterday.",
                        ["b2-34-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Gyakornok", "text": "Hogyan fogalmazzam meg ezt a mondatot a hivatalos levélben: 'Nem jött be a buli'?"},
                            {"speaker": "Mentor", "text": "____"},
                        ],
                        [
                            "Írd úgy: 'A tervezett rendezvény sajnálatos módon nem érte el a kitűzött célokat.'",
                            "Írd azt: 'A gizgaz teljesen kiakadt a limlom miatt tegnap este.'",
                            "Hagyd változatlanul, mert a hivatal szereti a vagány dumát.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ügyintéző", "text": "Milyen stílusban kell megválaszolnunk az ügyfél panaszlevelét?"},
                            {"speaker": "Osztályvezető", "text": "____"},
                        ],
                        [
                            "Kizárólag udvarias, tárgyilagos és hivatalos stílusban, az illetékes jogszabályokra hivatkozva.",
                            "Ugyan már, válaszoljunk laza ifjúsági szlengben, az sokkal barátságosabb.",
                            "Küldjünk neki néhány csecsebecsét a válaszlevél helyett.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Rewrite the colloquial phrase 'Nem vállalom be ezt a melót' into elevated formal Hungarian.",
                                "answer": "Sajnálattal közlöm, hogy a felkérést az említett feladatkör ellátására nem áll módomban elfogadni.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'illetékes' and 'hivatalos' in the context of an administrative inquiry.",
                                "answer": "Kérdésével kérjük, forduljon bizalommal az ügyben eljárni jogosult illetékes hivatalos szervekhez.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A miniszteri rendelet szövegét rendkívül körültekintően ____ meg a jogászok. (formulated / drafted)",
                        "fogalmazták",
                        "The lawyers formulated the text of the ministerial decree extremely carefully.",
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adjective means 'colloquial' or 'standard vernacular'?",
                        ["köznyelvi", "illetékes", "hivatalos"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Humor, Irony, and Linguistic Playfulness in Hungarian",
            "grammar_label": "Humor, irony, and linguistic playfulness in spoken Hungarian (szójáték, önirónia, élcelődik, kétértelműség, szellemes)",
            "goals": [
                "I can appreciate puns, double entendres, and verbal playfulness in conversational Hungarian",
                "I can recognize self-irony and understated sarcasm in spoken discourse",
                "I can analyze humor mechanisms in classic Hungarian literary and colloquial texts",
            ],
            "grammar_doc": {
                "slug": "humor-irony-linguistic-playfulness",
                "title": "Humor, Irony, and Linguistic Playfulness in Hungarian",
                "text1_title": "The Mechanisms of Hungarian Linguistic Wit",
                "text1": "Hungarian culture cultivates a legendary tradition of urban humor and verbal wit (pesti humor), popularized by authors like Jenő Rejtő, Frigyes Karinthy, and István Örkény. Linguistic humor in Hungarian operates through phonetic puns (szójáték), literal interpretations of dead metaphors, unexpected register clashes, and structural ambiguity (kétértelműség).",
                "text2_title": "Self-Irony and Understatement as Discourse Strategies",
                "text2": "Self-irony (önirónia) and understatement (eufemizmus, tompítás) serve as primary survival and rapport mechanisms in Hungarian conversation. Verbs like 'élcelődik' denote playful, good-natured teasing or bantering. A 'szellemes' remark displays sharp intelligence and verbal agility, often turning serious dilemmas into humorous intellectual insights without causing personal offense.",
                "table_title": "Core Vocabulary for Wit, Irony, and Humor",
                "table_rows": [
                    ["szójáték", "Karinthy művei tele vannak zseniális szójátékokkal. (Karinthy's works are full of puns.)"],
                    ["önirónia", "Az egészséges önirónia segít elviselni a nehéz pillanatokat. (Healthy self-irony helps endure hard moments.)"],
                    ["kétértelműség", "A mondat szándékos kétértelműsége mosolyt csalt az arcokra. (The intentional ambiguity elicited smiles.)"],
                    ["élcelődik", "A kollégák jókedvűen élcelődtek a főnök új frizuráján. (The colleagues bantered good-naturedly.)"],
                    ["szellemes", "Rendkívül szellemes választ adott a riporter provokatív kérdésére. (He gave a witty response.)"],
                ],
                "examples": [
                    {
                        "spanish": "Rejtő Jenő regényeinek utánozhatatlan báját a szellemes párbeszédek és a fanyar irónia adják.",
                        "english": "The inimitable charm of Jenő Rejtő's novels comes from witty dialogues and dry irony.",
                    },
                    {
                        "spanish": "A jó humorista képes az önirónia eszközével saját gyengeségein is szívből nevetni.",
                        "english": "A good humorist is able to laugh heartily at their own weaknesses using the tool of self-irony.",
                    },
                    {
                        "spanish": "A diplomáciában veszélyes lehet a kétértelműség, míg a kabaréban ez a siker alapja.",
                        "english": "In diplomacy, ambiguity can be dangerous, whereas in cabaret it is the foundation of success.",
                    },
                    {
                        "spanish": "Nem kell megsértődnöd, a barátaid csak ártatlanul élcelődtek a baklövéseden.",
                        "english": "You don't need to get offended, your friends were only innocently teasing you about your blunder.",
                    },
                ],
                "tip": "Hungarian humor frequently relies on hyper-literal readings of idioms. When analyzing satirical texts or cabaret, look for moments where an abstract figurative expression is dramatized as if it were a physical reality.",
            },
            "words": [
                {"lemma": "szójáték", "translation": "pun / play on words", "pos": "noun"},
                {"lemma": "önirónia", "translation": "self-irony / self-deprecation", "pos": "noun"},
                {"lemma": "kétértelműség", "translation": "ambiguity / double entendre", "pos": "noun"},
                {"lemma": "élcelődik", "translation": "to banter / joke / tease good-naturedly", "pos": "verb"},
                {"lemma": "szellemes", "translation": "witty / clever / humorous", "pos": "adjective"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'önirónia' in conversational and literary contexts?",
                        [
                            "the ability to mock or laugh at one's own shortcomings with humorous detachment",
                            "an aggressive personal insult aimed at an adversary",
                            "a strictly formal grammatical rule of punctuation",
                        ],
                        0,
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which verb means to joke, tease good-naturedly, or banter with friends?",
                        ["élcelődik", "megfogalmaz", "átlát"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["szójáték", "pun / play on words"],
                            ["önirónia", "self-irony / self-deprecation"],
                            ["kétértelműség", "ambiguity / double entendre"],
                            ["élcelődik", "to banter / tease playfully"],
                            ["szellemes", "witty / clever"],
                        ],
                        ["b2-34-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case does the verb 'élcelődik' govern when indicating the subject of teasing?",
                        ["superessive (-on/-en/-ön)", "inessive (-ban/-ben)", "sublative (-ra/-re)"],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What role does 'kétértelműség' play in satirical Hungarian literature?",
                        [
                            "It allows authors to express subversive political critique or humor under censorship.",
                            "It prevents readers from understanding any part of the story.",
                            "It is strictly forbidden by standard Hungarian orthography.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A diákok jókedvűen ____ a professzor különös szokásain. (bantered / teased)",
                        "élcelődtek",
                        "The students bantered good-naturedly about the professor's peculiar habits.",
                        ["b2-twin-words-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A vitában nem a harag, hanem a finom ____ segített elviselni a kritikát. (self-irony)",
                        "önirónia",
                        "In the debate, not anger but subtle self-irony helped endure the criticism.",
                        ["b2-twin-words-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "szónok", "rendkívül", "szellemes", "megjegyzéssel", "oldotta", "fel", "a", "teremben", "a", "feszültséget."],
                        ["A", "szónok", "rendkívül", "szellemes", "megjegyzéssel", "oldotta", "fel", "a", "teremben", "a", "feszültséget."],
                        "The speaker relieved the tension in the hall with an extremely witty remark.",
                        ["b2-twin-words-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Rejtő Jenő stílusa tele van bravúros ____, amelyek ma is megnevettetik az olvasókat. (puns / plays on words)",
                        "szójátékokkal",
                        "Jenő Rejtő's style is full of brilliant puns that still make readers laugh today.",
                        ["b2-34-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "szerződés", "szövegéből", "minden", "félrevezető", "kétértelműséget", "ki", "kellett", "küszöbölni."],
                        ["A", "szerződés", "szövegéből", "minden", "félrevezető", "kétértelműséget", "ki", "kellett", "küszöbölni."],
                        "All misleading ambiguity had to be eliminated from the text of the contract.",
                        ["b2-34-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Gergő", "text": "Hogy bírod elviselni a sok kellemetlenséget a munkahelyeden?"},
                            {"speaker": "Bori", "text": "____"},
                        ],
                        [
                            "Némi öniróniával és humorral: ha az ember képes nevetni a nehézségeken, minden könnyebb.",
                            "Azonnal gizgazt gyűjtök a fénymásoló mellett minden reggel.",
                            "Dehogyis, a hercehurca mindig szigorúan tilos az irodában.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Feri", "text": "Tetszett a tegnapi színházi előadás?"},
                            {"speaker": "Zsófi", "text": "____"},
                        ],
                        [
                            "Nagyon, a főszereplő szellemes dialógusai és bravúros szójátékai lenyűgözték a közönséget.",
                            "Nem, mert a limlom nem tudta bevállalni az illetékes szerepet.",
                            "Ugyan már, a színészek mind kiakadtak a hivatalos stílusréteg miatt.",
                        ],
                        0,
                        ["b2-twin-words-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'szellemes' and 'szójáték' describing an entertaining writer or orator.",
                                "answer": "A népszerű író szellemes előadásában számtalan bravúros szójátékkal szórakoztatta a hallgatóságot.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'önirónia' in a personal reflection about handling failure.",
                                "answer": "Kudarc esetén az egészséges önirónia segít abban, hogy ne veszítsük el önbizalmunkat és optimizmusunkat.",
                            }
                        ],
                        ["b2-twin-words-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A humorista virtuóz ____ kápráztatta el a kabaré nézőit. (plays on words / puns)",
                        "szójátékokkal",
                        "The comedian dazzled the cabaret audience with virtuoso wordplays.",
                        ["b2-twin-words-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adjective describes a witty, clever, or mentally agile person?",
                        ["szellemes", "illetékes", "köznyelvi"],
                        0,
                        ["b2-34-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can fluently navigate between Hungarian slang, colloquial expressions, and formal registers",
            "I can correctly deploy expressive twin-words like gizgaz, limlom, csecsebecse, and hercehurca",
            "I can appreciate and produce Hungarian conversational humor, irony, and communicative tags",
        ],
        "exercises": [
            # 1..3 Recognize
            mc(
                "vocabulary",
                "recognize",
                "Which Hungarian twin-word means an ordeal of bureaucratic paperwork or tedious fuss?",
                ["hercehurca", "csecsebecse", "limlom"],
                0,
                ["b2-34-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does the colloquial youth slang verb 'bevállal' mean?",
                [
                    "to boldly take on, dare to undertake, or step up to a challenging task",
                    "to hide behind another person during an argument",
                    "to submit an official application to a government ministry",
                ],
                0,
                ["b2-34-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence demonstrates proper register shifting from informal to formal Hungarian?",
                [
                    "A bizalmas 'A haverom befuccsolt a melóval' helyett a hivatalos 'A kolléga munkája meghiúsult' használatos.",
                    "A hivatalos iratban a 'kiakadt a miniszter' a legudvariasabb megfogalmazás.",
                    "A köznyelvi beszédben kizárólag latin jogi szakkifejezésekkel szabad válaszolni.",
                ],
                0,
                ["b2-twin-words-register"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "Mielőtt elköltöznénk, ki kell dobnunk a pincében heverő sok felesleges ____. (junk / clutter)",
                "limlomot",
                "Before we move, we must throw out the lots of unnecessary junk lying in the cellar.",
                ["b2-34-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "Nem kell aggódnod a vizsga miatt, ____ alaposan felkészültél minden tételből. (after all)",
                "elvégre",
                "You don't need to worry about the exam; after all, you prepared thoroughly for every topic.",
                ["b2-twin-words-register"],
            ),
            fb(
                "grammar",
                "recall",
                "A jogi beadványban az ügyvéd rendkívül szabatosan ____ meg az ügyfele követelését. (formulated / drafted)",
                "fogalmazta",
                "In the legal submission, the lawyer formulated his client's claim extremely accurately.",
                ["b2-twin-words-register"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'Ugyan már' preferred in friendly banter over 'Határozottan cáfolom'?",
                [
                    "Because it conveys conversational informality, friendly dismissal of an overstatement, and natural rapport.",
                    "Because 'cáfolom' cannot be used in spoken Hungarian under any circumstances.",
                    "Because 'Ugyan már' is an ancient military command.",
                ],
                0,
                ["b2-twin-words-register"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Kolléga", "text": "Hogyan élted túl a hosszas várakozást a földhivatalban?"},
                    {"speaker": "Ügyfél", "text": "____"},
                ],
                [
                    "Némi öniróniával és türelemmel: a bürokratikus hercehurcát csak humorral lehet elviselni.",
                    "Azonnal rákattantam a gizgazra a parkolóban.",
                    "Dehogyis, a limlom sosem fogalmaz meg hivatalos beadványt.",
                ],
                0,
                ["b2-twin-words-register"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'rákattan' is used correctly in contemporary colloquial discourse:",
                [
                    "A diák annyira rákattant a sakkozásra, hogy egész éjszaka nagymesterek partijait elemezte.",
                    "A könyvtáros rákattant a villanykapcsolóra a falon egy kalapáccsal.",
                    "A vonat rákattant a peronra a menetrend szerint délelőtt.",
                ],
                0,
                ["b2-twin-words-register"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "fiatal", "mérnök", "bátran", "bevállalta", "az", "új", "fejlesztési", "projekt", "vezetését."],
                ["A", "fiatal", "mérnök", "bátran", "bevállalta", "az", "új", "fejlesztési", "projekt", "vezetését."],
                "The young engineer boldly took on leading the new development project.",
                ["b2-twin-words-register"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "tárgyalófelek", "lényegében", "minden", "vitatott", "kérdésben", "sikeres", "megállapodásra", "jutottak."],
                ["A", "tárgyalófelek", "lényegében", "minden", "vitatott", "kérdésben", "sikeres", "megállapodásra", "jutottak."],
                "The negotiating parties essentially reached a successful agreement on every disputed issue.",
                ["b2-twin-words-register"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause reflection explaining how mastery of different stylistic registers ('stílusrétegek') and self-irony ('önirónia') enriches communication.",
                        "answer": "A különböző stílusrétegek magabiztos uralása lehetővé teszi, hogy a kötetlen köznyelvi fordulatoktól a hivatalos érvelésig mindig a helyzethez illően fejezzük ki magunkat; ráadásul az egészséges önirónia és a finom humor még a legfeszültebb vitákban is segít megőrizni az emberi közvetlenséget és a kölcsönös tiszteletet.",
                    }
                ],
                ["b2-twin-words-register"],
            ),
        ],
    },
}
